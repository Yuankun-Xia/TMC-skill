# Source maps, equations, and visual evidence

## Stable anchors

Use PDF page numbers (one-based) and, where helpful, printed page numbers separately. Record section, equation, figure or table identifiers. Do not treat a PDF viewer index as the printed journal page.

For a full aligned reader, use a compact source map such as:

```json
{"source_file":"paper.pdf","version":"user-supplied PDF","blocks":[
  {"id":"p003-b02","pdf_page":3,"section":"III. System Model","type":"paragraph","translated":true},
  {"id":"p004-e07","pdf_page":4,"type":"equation","label":"(7)","checked":true}
]}
```

Only record checks actually performed. Add crop coordinates or page links when the format/tool supports them. For ordinary summaries, page/section anchors in prose are enough; a JSON file is unnecessary.

## Two-column PDFs

Extraction sorted by vertical position can mix the left and right columns into one paragraph. Inspect block positions and reading order. Keep footnotes, author affiliations, headers, and license notices out of the abstract and argument. A DOI on the first two pages can belong to a cited conference version; identify the paper's own DOI from its front matter and verify metadata separately if needed.

Read the full relevant page to interpret a table, figure, or theorem. Check multi-line headings, captions continuing across columns, appendix references and figure panels. Extracted counts are candidates, not verified structure.

## Translation contract

Use stable pairs with source locations, for example:

```markdown
<a id="p003-b02"></a>
Source: PDF p. 3, Section III

Original: [source paragraph from the user-provided document]

中文: [faithful translation]
```

Preserve paragraph scope, citation markers, qualifiers, assumptions, negations and the strength of claims. Translate technical terminology consistently; keep a short terminology table for terms that recur or could be confused. Do not silently repair a source error; add a separate note.

The reader's own image links should resolve relative to the artifact or use absolute paths supported by the client. Keep figure captions and panel labels attached. Do not substitute redrawn data or a generated illustration for an extracted original figure without labelling the change.

## Equations and proofs

Build a notation table on demand: `symbol | meaning | unit/domain | source`. Check superscripts, transpose versus conjugate transpose, norms, summation limits, conditional expectations, staleness indices and dimensions. If OCR is uncertain, show a crop or mark the exact symbol uncertain.

For explanation, separate `paper equation`, `derivation/explanation`, and `interpretation`. State the assumptions needed for each step. For a convergence bound, identify its target quantity, rate, noise/heterogeneity terms, topology dependence, and regime; do not infer wall-clock behavior from a round-based bound.

## Coverage verification

For a full request, account for title/abstract, body sections, captions/tables, equations, appendix and bibliography according to scope. Reference lists may remain untranslated if the user wants the scientific prose translated, but retain their markers and disclose the choice. List any missing or unreadable items. Do not call a document complete merely because a file was saved.
