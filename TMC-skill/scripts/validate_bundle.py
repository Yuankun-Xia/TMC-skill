#!/usr/bin/env python3
"""Validate the nine-skill bundle and portable local references. Requires PyYAML."""
import argparse
import ast
import json
import re
from pathlib import Path
from urllib.parse import unquote

EXPECTED = {"tmc-reader", "tmc-writing", "tmc-polishing", "tmc-figure", "tmc-response",
            "tmc-academic-search", "tmc-citation", "tmc-data", "tmc-paper2ppt"}


def validate(root):
    import yaml
    errors = []
    root = Path(root).resolve()
    skill_root = root / "skills"
    actual = {p.name for p in skill_root.iterdir() if p.is_dir()} if skill_root.is_dir() else set()
    if actual != EXPECTED:
        errors.append(f"skill directories differ: missing {EXPECTED-actual}; extra {actual-EXPECTED}")
    for name in sorted(EXPECTED & actual):
        folder = skill_root / name
        entry = folder / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{name}: SKILL.md is missing")
            continue
        content = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
        try:
            meta = yaml.safe_load(match.group(1)) if match else None
            if not isinstance(meta, dict) or meta.get("name") != name or not meta.get("description"):
                errors.append(f"{name}: invalid name/description frontmatter")
            elif len(meta["description"]) > 1024:
                errors.append(f"{name}: discovery description is too long")
        except yaml.YAMLError as error:
            errors.append(f"{name}: frontmatter YAML {error}")
        ui_path = folder / "agents/openai.yaml"
        try:
            ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
            interface = ui["interface"]
            if not 25 <= len(interface["short_description"]) <= 64:
                errors.append(f"{name}: short_description length")
            if "$" + name not in interface.get("default_prompt", ""):
                errors.append(f"{name}: default_prompt does not invoke this skill")
            if ui.get("policy", {}).get("allow_implicit_invocation") is False:
                errors.append(f"{name}: unexpectedly disabled implicit invocation")
        except (OSError, KeyError, TypeError, yaml.YAMLError) as error:
            errors.append(f"{name}: invalid UI metadata: {error}")
        for document in folder.rglob("*.md"):
            body = document.read_text(encoding="utf-8")
            if re.search(r"\b(?:twc-|nature_citation|scope cns|pubmed_search_articles)", body, re.I):
                errors.append(f"{document.relative_to(root)}: legacy dependency")
            for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
                if re.match(r"^[a-z][a-z0-9+.-]*:", link, re.I) or link.startswith("#"):
                    continue
                destination = (document.parent / unquote(link.split("#")[0])).resolve()
                if not destination.is_relative_to(folder.resolve()):
                    errors.append(f"{name}: non-portable cross-skill link {link}")
                elif not destination.exists():
                    errors.append(f"{document.relative_to(root)}: broken link {link}")
    for source in root.rglob("*.py"):
        try:
            ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
        except SyntaxError as error:
            errors.append(f"{source.relative_to(root)}: {error}")
    plugin = json.loads((root / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    if plugin.get("name") != "tmc-skills":
        errors.append("plugin name mismatch")
    corpus = json.loads((skill_root / "tmc-writing/references/tmc-corpus-inventory.json").read_text(encoding="utf-8"))
    papers, summary = corpus["papers"], corpus["summary"]
    if len(papers) != summary["pdf_count"] or sum(p.get("pages", 0) for p in papers) != summary["page_total"]:
        errors.append("corpus summary inconsistent")
    if len({p["sha256"] for p in papers}) != len(papers):
        errors.append("duplicate source PDF hashes")
    if len({p["id"] for p in papers}) != len(papers):
        errors.append("duplicate corpus IDs")
    if any(p.get("status") != "ok" for p in papers):
        errors.append("corpus contains extraction failures")
    if any(root.rglob("*.pdf")):
        errors.append("unexpected PDF in distributable; original papers must stay in the library")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print("ERROR:", error)
    if not errors:
        print("PASS: nine skills, frontmatter, UI metadata, portable links, Python syntax, plugin and corpus inventory")
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
