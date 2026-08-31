#!/usr/bin/env python3
"""Consistency checks for the toolkit.

Run locally with `python3 scripts/check-repo.py`, or let CI run it. Every check here
exists because the corresponding drift actually happened at least once.
"""
from __future__ import annotations

import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIBLING_REGO = (
    "https://raw.githubusercontent.com/mmubarak-io/ai-compliance-gates"
    "/main/policy/terraform_compliance.rego"
)

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def md_files() -> list[Path]:
    """Only files git tracks. Anything ignored or local is not our business."""
    out = subprocess.run(
        ["git", "ls-files", "*.md"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    return [ROOT / line for line in out.stdout.splitlines() if line]


def check_internal_links() -> None:
    """Every relative markdown link resolves to something on disk."""
    pattern = re.compile(r"\]\((?!https?://|mailto:|#)([^)]+)\)")
    for path in md_files():
        for link in pattern.findall(path.read_text(encoding="utf-8")):
            target = link.split("#")[0]
            if not target:
                continue
            if not (path.parent / target).exists():
                fail(f"broken link: {path.relative_to(ROOT)} -> {link}")


def check_no_em_dashes() -> None:
    """House style is a plain hyphen. Covers markdown and the fillable binaries."""
    for path in md_files():
        text = path.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if "—" in line:
                fail(f"em-dash: {path.relative_to(ROOT)}:{i}")

    import zipfile

    for path in list(ROOT.rglob("*.xlsx")) + list(ROOT.rglob("*.docx")):
        if ".git" in path.parts:
            continue
        with zipfile.ZipFile(path) as z:
            for name in z.namelist():
                if not name.endswith(".xml"):
                    continue
                if not any(
                    k in name
                    for k in ("sharedStrings", "document.xml", "header", "footer")
                ):
                    continue
                if "—" in z.read(name).decode("utf-8", "ignore"):
                    fail(f"em-dash inside {path.relative_to(ROOT)} ({name})")


def check_yaml() -> None:
    """Both machine-readable files parse, and documented_by paths resolve."""
    try:
        import yaml
    except ImportError:
        warn("pyyaml not installed - skipped YAML checks (pip install pyyaml)")
        return

    for name in ("classification.yaml", "policy-register.yaml"):
        path = ROOT / "machine-readable" / name
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            fail(f"{name} does not parse: {exc}")
            continue

        if name == "policy-register.yaml":
            for policy in data["policies"]:
                for doc in policy["documented_by"]:
                    if not (ROOT / doc).exists():
                        fail(f"{policy['policy_id']} documented_by missing: {doc}")
                if policy.get("enforcement") not in {"enforced", "planned"}:
                    fail(
                        f"{policy['policy_id']} needs enforcement: enforced|planned"
                    )

        if name == "classification.yaml":
            keys = [set(t["controls"]) for t in data["tiers"]]
            if len({frozenset(k) for k in keys}) != 1:
                fail("classification.yaml tiers do not share the same control keys")


def check_policy_ids_match_sibling() -> None:
    """IDs marked `enforced` must actually appear in ai-compliance-gates."""
    try:
        import yaml
    except ImportError:
        return
    try:
        with urllib.request.urlopen(SIBLING_REGO, timeout=20) as resp:
            rego = resp.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        warn(f"could not fetch ai-compliance-gates policy ({exc}) - skipped ID sync")
        return

    sibling_ids = set(re.findall(r"POL-[A-Z]+-\d+", rego))
    register = yaml.safe_load(
        (ROOT / "machine-readable" / "policy-register.yaml").read_text(encoding="utf-8")
    )
    ours = {p["policy_id"]: p.get("enforcement") for p in register["policies"]}

    for pid, status in ours.items():
        if status == "enforced" and pid not in sibling_ids:
            fail(f"{pid} is marked enforced but no gate in ai-compliance-gates emits it")
    for pid in sorted(sibling_ids - set(ours)):
        fail(f"{pid} is enforced in ai-compliance-gates but missing from the register")


def check_disclaimers() -> None:
    """Templates get copied out standalone, so the notice travels with the file."""
    pattern = re.compile(
        r"not legal advice|not legal definitions|fictional|synthetic", re.I
    )
    for path in list((ROOT / "templates").rglob("*.md")) + list(
        (ROOT / "examples").rglob("*.md")
    ) + list((ROOT / "docs").rglob("*.md")):
        if not pattern.search(path.read_text(encoding="utf-8")):
            fail(f"no disclaimer: {path.relative_to(ROOT)}")


def check_every_artefact_has_an_example() -> None:
    """The README claims one for every artefact. Keep that true."""
    expected = {
        "data-classification": "classification",
        "ropa": "ropa",
        "dpia": "dpia",
        "ai-system-risk-checklist": "ai-risk-checklist",
        "breach-response": "breach",
    }
    examples = [p.name for p in (ROOT / "examples").glob("*.md")]
    for template_dir, marker in expected.items():
        if not (ROOT / "templates" / template_dir).exists():
            fail(f"template directory missing: {template_dir}")
        if not any(marker in name for name in examples):
            fail(f"no worked example for {template_dir} (looked for '{marker}')")


def main() -> int:
    for check in (
        check_internal_links,
        check_no_em_dashes,
        check_yaml,
        check_policy_ids_match_sibling,
        check_disclaimers,
        check_every_artefact_has_an_example,
    ):
        check()

    for w in warnings:
        print(f"warn: {w}")
    for f in failures:
        print(f"FAIL: {f}")

    if failures:
        print(f"\n{len(failures)} problem(s) found.")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
