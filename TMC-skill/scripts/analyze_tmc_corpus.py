#!/usr/bin/env python3
"""Inventory user-supplied PDFs without copying their full text into the skill.

Requires PyMuPDF (pip install pymupdf). All detections are candidates, not
verified bibliographic records or proof of a paper's scientific claims.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

DOI = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)
HEADING = re.compile(r"^([IVX]{1,6})[.\s]+([A-Z][A-Z0-9 ,:&()/'’–-]{3,130})$")
CAPTION = re.compile(r"^(Fig(?:ure)?\.?\s*(\d+)|TABLE\s+([IVX]+|\d+))\b", re.I)
TAGS = {
    "federated-learning": r"federated",
    "asynchrony-scheduling": r"asynchron|semi.synchron|schedul|straggler",
    "heterogeneity": r"heterogen|non.iid|imbalanc|noisy label|long.tail",
    "resource-efficiency": r"energy|memory|resource|efficient|power|quantiz|compress",
    "security-privacy": r"privacy|secure|security|attack|poison|collusion|unlearning",
    "mobility-uav-vehicle": r"mobility|vehicle|in.vehicle|uav|aav|trajectory",
    "space-network": r"space|satellite|leo\b",
    "llm-peft": r"llm|language model|fine.tun|parameter.efficient",
    "decentralized-topology": r"decentral|topology|distributed|consensus|admm",
}


def analyze(path, corpus_root):
    import pymupdf
    record = {
        "file": path.relative_to(corpus_root).as_posix(),
        "title_from_filename": path.stem,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "size_bytes": path.stat().st_size,
        "status": "ok",
    }
    try:
        with pymupdf.open(path) as doc:
            if doc.needs_pass:
                raise ValueError("encrypted PDF requires password")
            pages = [page.get_text(sort=True) for page in doc]
            record["pages"] = len(pages)
            record["pdf_metadata"] = {k: v for k, v in doc.metadata.items() if v}
            front = "\n".join(pages[:2])
            record["doi_candidates_front_matter"] = sorted({
                match.rstrip(".,;") for match in DOI.findall(front)
            })
            record["journal_header_detected"] = bool(re.search(
                r"IEEE\s+TRANSACTIONS\s+ON\s+MOBILE\s+COMPUTING", front, re.I))
            record["low_text_pages"] = [i + 1 for i, page in enumerate(pages)
                                        if len(page.strip()) < 100]
            record["headings_candidates"] = []
            figures, tables = set(), set()
            for page_number, page in enumerate(pages, 1):
                for line in page.splitlines():
                    line = " ".join(line.split())
                    heading = HEADING.match(line)
                    if heading:
                        record["headings_candidates"].append({
                            "page": page_number, "text": line})
                    caption = CAPTION.match(line)
                    if caption:
                        if caption.group(2):
                            figures.add(int(caption.group(2)))
                        else:
                            tables.add(caption.group(3).upper())
            record["figure_numbers_detected"] = sorted(figures)
            record["table_numbers_detected"] = sorted(tables)
            title = record["title_from_filename"]
            record["title_keyword_tags"] = [tag for tag, pattern in TAGS.items()
                                             if re.search(pattern, title, re.I)]
    except Exception as error:
        record["status"] = "error"
        record["error"] = f"{type(error).__name__}: {error}"
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", type=Path, help="PDF folder; searched recursively")
    parser.add_argument("--output", type=Path, required=True, help="new JSON output")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    if not args.corpus.is_dir():
        parser.error("corpus must be an existing directory")
    files = sorted(p for p in args.corpus.rglob("*") if p.suffix.lower() == ".pdf")
    if not files:
        parser.error("no PDFs found")
    if args.output.exists() and not args.overwrite:
        parser.error("output exists; choose a new path or pass --overwrite")
    records = []
    for index, path in enumerate(files, 1):
        record = analyze(path, args.corpus)
        record["id"] = f"TMC{index:02d}"
        records.append(record)
    successful = [r for r in records if r["status"] == "ok"]
    inventory = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "method": "PyMuPDF selectable text; no OCR; filename tags; caption/heading heuristics",
        "limitations": ["Headings and caption counts are candidates requiring visual checks.",
                       "Filename tags overlap and do not establish prevalence across TMC.",
                       "DOIs and journal headers are local detections, not publisher verification."],
        "summary": {"pdf_count": len(files), "readable_count": len(successful),
                    "page_total": sum(r["pages"] for r in successful),
                    "tag_counts": {t: sum(t in r.get("title_keyword_tags", []) for r in records)
                                   for t in TAGS}},
        "papers": records,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(inventory["summary"], ensure_ascii=False))
    return 1 if len(successful) != len(files) else 0


if __name__ == "__main__":
    raise SystemExit(main())
