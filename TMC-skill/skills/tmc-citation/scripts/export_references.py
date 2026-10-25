#!/usr/bin/env python3
"""Export preparer-verified plain-text JSON metadata; no network verification."""
import argparse
import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

TYPES = {"article": ("article", "JOUR", "Journal Article"),
         "conference": ("inproceedings", "CONF", "Conference Paper"),
         "preprint": ("misc", "UNPB", "Preprint"),
         "dataset": ("misc", "DATA", "Dataset"),
         "software": ("misc", "COMP", "Computer Program")}
SUPPORT = {"direct", "partial", "background", "limiting/contradictory", "metadata-only"}


def text(value):
    return " ".join(str(value).split())


def normalize_doi(value):
    value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", text(value), flags=re.I)
    return value.rstrip(".,;").lower()


def is_url(value):
    parts = urlsplit(value)
    return parts.scheme in {"https", "http"} and bool(parts.netloc)


def validate(records):
    if not isinstance(records, list) or not records:
        raise ValueError("records must be a nonempty list")
    clean, keys, dois, titles = [], set(), set(), set()
    for index, source in enumerate(records, 1):
        if not isinstance(source, dict):
            raise ValueError(f"record {index} is not an object")
        row = {k: text(v) for k, v in source.items() if v is not None and k != "authors"}
        if row.get("metadata_status") != "verified":
            raise ValueError(f"record {index}: metadata must be checked before export")
        if not is_url(row.get("source_url", "")):
            raise ValueError(f"record {index}: checked source_url is required")
        try:
            checked = date.fromisoformat(row["checked_at"])
            if checked.isoformat() != row["checked_at"]:
                raise ValueError("date must use YYYY-MM-DD")
        except (KeyError, ValueError) as error:
            raise ValueError(f"record {index}: checked_at must be an ISO date") from error
        if not row.get("title"):
            raise ValueError(f"record {index}: title is required")
        authors = source.get("authors")
        if not isinstance(authors, list) or not authors or any(not isinstance(a, str) or not a.strip() for a in authors):
            raise ValueError(f"record {index}: authors must be a nonempty string list")
        row["authors"] = [text(a) for a in authors]
        if not re.fullmatch(r"\d{4}", row.get("year", "")):
            raise ValueError(f"record {index}: four-digit verified year is required")
        row.setdefault("type", "article")
        if row["type"] not in TYPES:
            raise ValueError(f"record {index}: unsupported type")
        if row["type"] in {"article", "conference"} and not row.get("venue"):
            raise ValueError(f"record {index}: article/conference venue is required")
        row.setdefault("support_status", "metadata-only")
        if row["support_status"] not in SUPPORT:
            raise ValueError(f"record {index}: unsupported support_status")
        row.setdefault("key", f"Ref{row['year']}_{index:02d}")
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.:+-]*", row["key"]):
            raise ValueError(f"record {index}: invalid BibTeX key")
        if row["key"] in keys:
            raise ValueError(f"record {index}: duplicate key {row['key']}")
        keys.add(row["key"])
        if row.get("doi"):
            row["doi"] = normalize_doi(row["doi"])
            if not re.fullmatch(r"10\.\d{4,9}/\S+", row["doi"]):
                raise ValueError(f"record {index}: malformed DOI")
            if row["doi"] in dois:
                raise ValueError(f"record {index}: duplicate DOI")
            dois.add(row["doi"])
        title_key = re.sub(r"[^\w]", "", unicodedata.normalize("NFKC", row["title"]).casefold())
        if title_key in titles:
            raise ValueError(f"record {index}: duplicate normalized title; resolve versions")
        titles.add(title_key)
        if row.get("url") and not is_url(row["url"]):
            raise ValueError(f"record {index}: malformed url")
        clean.append(row)
    return clean


def bib_escape(value):
    escapes = {"\\": r"\textbackslash{}", "{": r"\{", "}": r"\}",
               "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
               "_": r"\_", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(escapes.get(char, char) for char in value)


def export(records, fmt):
    blocks = []
    for row in records:
        if fmt == "bib":
            fields = [("author", " and ".join(bib_escape(a) for a in row["authors"])),
                      ("title", "{" + bib_escape(row["title"]) + "}"),
                      ("year", row["year"])]
            if row.get("venue"):
                venue_field = "booktitle" if row["type"] == "conference" else "journal" if row["type"] == "article" else "howpublished"
                fields.append((venue_field, bib_escape(row["venue"])))
            for key, target in [("volume", "volume"), ("issue", "number"), ("pages", "pages")]:
                if row.get(key):
                    fields.append((target, bib_escape(row[key])))
            # DOI/URL fields are identifier fields, not prose; do not corrupt underscores.
            for key in ("doi", "url"):
                if row.get(key):
                    if any(c in row[key] for c in "{}\\"):
                        raise ValueError(f"{key} contains unsupported BibTeX delimiters")
                    fields.append((key, row[key]))
            blocks.append("@" + TYPES[row["type"]][0] + "{" + row["key"] + ",\n" +
                          ",\n".join(f"  {k} = {{{v}}}" for k, v in fields) + "\n}")
        else:
            ris = fmt == "ris"
            lines = [("TY", TYPES[row["type"]][1])] if ris else [("0", TYPES[row["type"]][2])]
            lines += [("AU" if ris else "A", a) for a in row["authors"]]
            lines += [("TI" if ris else "T", row["title"]), ("PY" if ris else "D", row["year"])]
            mapping = [("venue", "T2", "J" if row["type"] == "article" else "B"),
                       ("volume", "VL", "V"), ("issue", "IS", "N"),
                       ("doi", "DO", "R"), ("url", "UR", "U")]
            for key, ris_tag, enw_tag in mapping:
                if row.get(key):
                    lines.append((ris_tag if ris else enw_tag, row[key]))
            if row.get("pages"):
                if ris:
                    page_range = re.split(r"\s*(?:--|–|-)\s*", row["pages"], maxsplit=1)
                    lines.append(("SP", page_range[0]))
                    if len(page_range) == 2:
                        lines.append(("EP", page_range[1]))
                else:
                    lines.append(("P", row["pages"]))
            if ris:
                lines.append(("ER", ""))
            blocks.append("\n".join((f"{tag}  - {value}" if ris else f"%{tag} {value}").rstrip()
                                    for tag, value in lines))
    return "\n\n".join(blocks) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--format", choices=["bib", "ris", "enw"], required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    if args.output.exists() and not args.overwrite:
        parser.error("output exists; choose a new path or pass --overwrite")
    if args.output.suffix.lower() != "." + args.format:
        parser.error("output extension must match the requested format")
    try:
        source = json.loads(args.input.read_text(encoding="utf-8-sig"))
        rows = validate(source.get("records") if isinstance(source, dict) else source)
        result = export(rows, args.format)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(f"Exported {len(rows)} preparer-verified records; scientific support is not verified by this tool.")


if __name__ == "__main__":
    main()
