# Metadata verification and claim support

## Two independent checks

**Identity check:** title, authors, venue, publication status/date, DOI and source record agree. Metadata-only publisher records can pass identity verification.

**Support check:** the content actually establishes the claim at the stated scope. Record a section/page/figure/equation or other retrievable anchor. Bibliographic correctness alone cannot pass this check.

| Support state | Meaning |
|---|---|
| direct | Examines the stated relationship/method under applicable conditions and supports the clause |
| partial | Supports a narrower condition or one part; narrow the sentence or add sources |
| background | Gives context or a broader overview, not the specific result |
| limiting/contradictory | Narrows or conflicts with the clause; report it rather than hiding it |
| metadata-only | Content not examined; cannot support a scientific claim yet |

These are human/agent reading judgments, not confidence scores computed from keywords. Preserve the scope and uncertainty of the original paper. Cite the source actually examined, and distinguish secondary interpretation from primary evidence.

## Identity pitfalls

- Use the paper's own DOI, not a conference version DOI mentioned in its first-page footnote.
- DOI case/prefix normalization helps deduplication but does not fix a wrong identity.
- First public, early-access, issue and preprint dates can differ. Use the correct one for the task.
- A journal extension and conference paper may share a title yet contain different results.
- Preserve author order and full available names; do not guess initials or affiliations.
- Check visible correction/retraction notices and use the relevant version.

## Export JSON schema

The helper accepts a list or an object with a `records` list. Each record requires:

```json
{
  "records": [{
    "key": "Example2026",
    "type": "article",
    "title": "Synthetic Format Example, Not a Real Reference",
    "authors": ["Example, Alice", "Sample, Bo"],
    "year": 2026,
    "venue": "Example Venue",
    "metadata_status": "verified",
    "source_url": "https://example.org/verified-record",
    "checked_at": "2026-10-25",
    "support_status": "metadata-only"
  }]
}
```

This is a synthetic schema example. Setting `metadata_status` is an assertion by the preparer, not proof of verification. Populate it only after checking the source. Optional fields are `doi`, `volume`, `issue`, `pages`, `url`, `publication_status`, and `evidence_location`.

Allowed types: `article`, `conference`, `preprint`, `dataset`, `software`. Venue is required for article/conference records; choose a preprint/repository name when known for other types. Authors are supplied in reference-manager name form, preferably `Family, Given`, in the verified order; the helper does not infer name components. Use `key` for an existing BibTeX key. Do not put raw LaTeX commands into metadata strings; the helper escapes plain text.

`metadata_status` must be `verified`, with an ISO `checked_at` date and a checked HTTPS/HTTP `source_url`. `support_status` defaults to `metadata-only`; it is independent of permission to export a bibliographic record. The helper does not assert that an exported record supports any manuscript sentence. Keep the claim map in the working notes or requested report.

Before export, examine missing fields. Early-access records may lack volume/issue/pages. A preprint uses the verified preprint identifier or URL, not an invented journal assignment. The exporter rejects duplicate DOI or normalized title identities and duplicate BibTeX keys so conflicts can be resolved deliberately.

## Primary metadata sources

Use primary publisher pages or original papers, with Crossref DOI records and DBLP as identity cross-checks where useful. Crossref API documentation: https://www.crossref.org/documentation/retrieve-metadata/rest-api/ . A bibliographic service does not substitute for reading evidence. Consult current service documentation when implementing network access; the bundled exporter is entirely local.
