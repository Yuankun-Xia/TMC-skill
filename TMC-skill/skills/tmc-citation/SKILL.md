---
name: tmc-citation
description: Verify bibliographic records and whether papers support specific claims in TMC manuscripts, then insert or export verified references in BibTeX, RIS or EndNote format. Use for TMC citation checks, missing references, claim-to-source mapping, DOI/version resolution and reference-manager exports.
---

# TMC Citation Verification

Verify identity and scientific support separately. Read [metadata and support](references/metadata-and-support.md) for states, export schema and pitfalls. Read [TMC context](references/tmc-context.md) when journal identity or scope matters.

## Workflow

1. Identify the sentence/claim, source manuscript, existing citation keys and requested format. Split compound claims so references attach to the clauses they support.
2. Resolve candidate records using supplied PDFs and primary publisher/author sources. Check title, authors, venue, DOI and publication version/date. A DOI printed in a reference list is not necessarily the current paper's DOI.
3. Read the relevant abstract, method or results. Record the evidence location and classify support as `direct`, `partial`, `background`, `limiting/contradictory`, or `metadata-only`. Do not call a metadata match verified scientific support.
4. Recommend insertion points and, where necessary, narrow the sentence to what the source actually establishes. Label unavailable full text. Keep a preprint/journal extension distinction explicit.
5. Export only verified metadata. Preserve existing citation keys and journal abbreviations when appropriate. Missing pages/issue for early access should remain absent. Do not invent a DOI, author, date or page range.
6. Reconcile in-text citations and the final bibliography, including duplicates and unresolved keys when source files are available. Verify compilable LaTeX when actually building the manuscript.

Prioritize relevance and primary evidence over venue prestige. Include TMC, other journals and conferences according to the user's scope. No Nature-family, PubMed or flagship-only restriction applies by default.

## Export helper

[scripts/export_references.py](scripts/export_references.py) converts already checked JSON records to one BibTeX, RIS or EndNote tagged file. It validates required fields and duplicate identities, escapes format characters, and refuses unverified records. It performs no network search and does not independently verify metadata or scientific support.

Run `python scripts/export_references.py checked-records.json --output references.bib --format bib`. Use `.ris`/`--format ris` or `.enw`/`--format enw` as requested. Read the schema reference before preparing JSON. Do not import a fake record simply to make an export nonempty.

## Output

Return the claim-to-source mapping, verification state and source links, plus the requested export file when applicable. Keep metadata gaps and support gaps distinct. If no source supports a clause, say so and propose a narrower claim or a further search rather than inserting a weak citation silently.
