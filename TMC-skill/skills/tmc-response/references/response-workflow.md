# Response workflow and difficult cases

## Minimal evidence matrix

| Item | Concern | Answer/action | Evidence | Location | Status |
|---|---|---|---|---|---|
| R1.1 | Faithful concern summary | Direct response or revision | Result/log/derivation/source, if present | Verified locator | Completed / planned / needs input / disagreement |

Use subitems when the reviewer asks for several things. Every concern needs an answer, a clearly linked answer elsewhere, or an explicit outstanding state. Do not count a reply as complete merely because it contains a polite paragraph.

## Response paragraph

Use `direct answer -> scientific evidence/reasoning -> actual change -> verified location`. A brief acknowledgment is sufficient. Quote the inserted text when it materially helps verification; do not paste the entire revised section by default.

Before: "Thank you for this insightful comment. We have added comprehensive real-world experiments that prove our method works in all settings."

Better, if only a simulator was used: "The current evaluation uses a simulator and does not establish on-device deployment performance. We have clarified this scope in [verified location] and removed the unsupported deployment claim."

This example is a pattern, not a statement that any current manuscript has been changed. Use completed language only after checking an actual edit or an explicit author revision record.

## Missing experiment

Determine what the concern is testing: fairness, feasibility, overhead, robustness, scalability, or a central claim. Identify whether existing evidence answers it. If new experiments are needed, specify a minimal discriminating test, baseline, budget, metric and required inputs. Keep the response draft provisional until the result exists.

If an experiment cannot be run, explain the real limitation, use existing evidence only for what it supports, and narrow the claim/manuscript accordingly when authorized. Do not invent a device, replace hardware measurements with simulated values, or promise completion without a plan and authorization.

## Misunderstanding or disagreement

First examine whether definitions, assumptions, figures or wording caused the misunderstanding. Clarify the manuscript when useful. For disagreement, state the concern fairly, explain the scientific or scope reason, cite verified evidence, and specify any clarifying change. Avoid "the reviewer is wrong" and authority-based arguments.

If two reviewers conflict, identify the underlying needs and propose a solution that preserves the argument: for example, a concise main-text explanation with a detailed derivation elsewhere if the actual submission rules allow it. Check current rules before claiming an appendix or supplementary file is permitted. Do not promise incompatible revisions to different reviewers.

## TMC-specific concern-to-evidence mapping

- **Only accuracy is shown:** identify the claimed system gain and whether measured time/energy/memory/traffic supports it. Add a proposed test or narrow the gain; do not relabel a round curve as time.
- **Resources are unrealistic:** inspect heterogeneity generation, bandwidth sharing, hardware constraints, contact times, and what was simulated. Explain the abstraction and its scope.
- **Algorithm overhead is omitted:** identify control/solver, profiling, model conversion and extra messages; report only measured or explicitly modelled costs.
- **Guarantee is too strong:** align theorem statement, assumptions and proof. A stationary-point result does not answer a global-optimality request without a correction.
- **Privacy is asserted:** define the threat and guarantee; data locality alone does not answer leakage/attack concerns.
- **Baselines are weak:** check closest mechanisms and fair budgets before recommending additions. A new named method still needs a verified source and implementation basis.

## Final reconciliation

Use the final manuscript to resolve section, equation, table, figure and page/line locators. Ensure numerical comparisons use the same direction and denominator in all files. Check that cited references exist and support the reply. Verify tracked versus clean versions when both are produced. Report unavailable materials and outstanding actions separately from completed changes.
