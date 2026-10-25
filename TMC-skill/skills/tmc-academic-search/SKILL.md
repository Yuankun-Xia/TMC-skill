---
name: tmc-academic-search
description: Find and compare research for TMC and mobile/edge computing questions, including federated learning, resource scheduling, mobile sensing, decentralized networks, security and PEFT. Use for literature surveys, related-work searches, baseline discovery and date-bounded updates; use tmc-citation to validate specific claim-to-reference matches and export citations.
---

# TMC Literature Search

Read [search strategy](references/search-strategy.md) to construct queries and record coverage. Read [TMC context](references/tmc-context.md) when screening venue relevance. Search the user's local library first when the task is about that library; use current external search when asking for new, recent or comprehensive literature.

## Search around the actual problem

Identify the mobile setting, failure mechanism, desired capability, important constraints, date range and requested output. Infer these from the user's materials where possible. Build a concept grid with synonyms, then search several combinations. Distinguish asynchronous, semi-synchronous and synchronous FL; statistical, system and temporal heterogeneity; parameter-efficient tuning and generic compression.

Prefer primary publisher pages and original papers. IEEE Xplore/CSDL are useful for TMC metadata and papers; ACM and other primary venues may supply essential mobile-systems baselines; arXiv provides versions/preprints; Crossref and DBLP help resolve metadata. Use the tools actually available. If a connector is absent, use browser/web or documented APIs; do not invent an MCP tool, require an API key without need, or install a service automatically.

Do not restrict to TMC unless the user asks for that scope. A relevant conference method can be a stronger baseline than a tangential journal paper. Do not route mobile-computing searches to PubMed/MeSH by default.

## Screen and verify

1. Search with enough variants to cover the mechanism and application. Preserve exact queries, sources and search date when coverage matters.
2. Deduplicate by canonical DOI, then bibliographic identity. Link conference/preprint/journal versions rather than assuming they are duplicates of the same scientific contribution.
3. Read abstract/method/evaluation as needed. Record the contribution, assumptions, comparable task/budget, evaluation type, limitations and code availability only when checked.
4. Separate `metadata candidate`, `abstract screened`, and `full-text examined`. A keyword match is not evidence that a paper meets the user's constraints.
5. Check publisher correction/retraction/version information when visible. Treat publication date, early-access date, issue date and preprint date as distinct.

## Output

Give a relevant shortlist or the requested survey, with title, verified venue/version/year, DOI or primary URL, reason for inclusion and screening state. Use a mechanism/assumption comparison table when it helps position the user's work. Report search boundaries and inaccessible sources. Do not call an ad hoc search systematic or exhaustive without a reproducible protocol and coverage accounting.

For exact sentence support and reference-manager export, continue with the citation workflow if it is available, or apply the self-contained verification rules in the search reference. Searching itself does not authorize contacting authors, uploading manuscripts, purchasing access, or subscribing to alerts.
