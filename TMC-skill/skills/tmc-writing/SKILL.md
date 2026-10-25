---
name: tmc-writing
description: Draft, restructure, or review IEEE Transactions on Mobile Computing manuscripts from author-provided notes, methods, results, or Chinese drafts. Use for TMC abstracts, introductions, system models, problem formulations, methods, evaluations, and full-paper argument design; use tmc-polishing for sentence-level editing of finished prose.
---

# TMC Manuscript Writing

Build a defensible mobile-computing argument from the author's evidence. Accept Chinese or mixed-language notes. Unless the user explicitly requests a Chinese or other-language manuscript draft, write submission prose in English and decision notes in Chinese. The language of the notes or chat alone does not change this manuscript-language default.

## Select only the needed references

| Task | Reference |
|---|---|
| Venue fit or submission requirements | [TMC context and sources](references/tmc-context.md) |
| Learn from the supplied TMC papers | [Corpus observations](references/tmc-corpus-observations.md); use the linked inventory to locate papers |
| Title, abstract, introduction, related work, conclusion | [Section blueprints](references/section-blueprints.md) |
| System model, algorithm, theorem, proof, complexity | [Model and analysis](references/model-and-analysis.md) |
| Experimental design or Results | [Evaluation](references/evaluation.md) |
| Full manuscript audit | [Review checklist](references/review-checklist.md) |

Read the corpus observations for a substantial TMC outline or manuscript rewrite. Do not load every reference for a short paragraph edit. The local corpus emphasizes FL and edge computing; it does not define all of TMC.

## Establish the argument

Identify the requested section and available manuscript version. Recover these items from supplied material before asking for missing information:

- Mobile setting and workload: who computes, communicates, senses, or makes decisions, and under what deadline or resource limit.
- Concrete failure of existing approaches under that setting, supported by a source, measurement, derivation, or explicit author hypothesis.
- Proposed mechanism and why it addresses that failure.
- Available theory and empirical evidence, with applicable assumptions and boundaries.

For extensive work, keep a compact claim ledger: `claim | source/result | condition | status`. Distinguish `supported`, `author-stated`, `planned`, and `missing`. For a small request, use brief notes instead of a compulsory report.

A useful argument is: `Under [mobile constraint], existing [mechanism] fails because [reason]; [design] addresses it through [mechanism], supported by [actual evidence], within [conditions].`

## Draft from evidence

1. Select the architecture that fits the contribution: systems implementation, optimization/theory, learning method in a mobile application, security/privacy, or a combination. A theorem, testbed, separate Discussion section, and fixed contribution count are not universal requirements.
2. Map each major contribution to a mechanism and its verifying experiment or analysis. Separate a new formulation, a solution, and its evaluation without counting the same idea three times.
3. Explain relevant coupling: for example, model rank changes local memory, computation, payload, and aggregation compatibility. Explain only couplings present in this work.
4. Write reproducible definitions before relying on shorthand. Keep notation, units, indexing, system timeline, and causal claims consistent.
5. Report results at the tested budget and setting. Distinguish observed trends from explanations and theoretical guarantees.
6. Check title, abstract, introduction, evaluation, and conclusion against the same contribution and evidence ledger.

If results are absent, deliver a useful outline or provisional prose with explicit author fields such as `[NEEDED: measured time to the stated accuracy target]`. Do not fill these fields with plausible numbers. For submission-ready text, identify unresolved fields separately and do not call the draft complete.

## TMC decisions that matter

- Explain what the mobile system gains and pays: latency, energy, memory, traffic, fairness, reliability, availability, or another relevant metric. Accuracy alone may leave a system contribution unsupported.
- A wireless equation or the word "edge" does not by itself establish venue fit. Explain the mobile-computing problem and evaluate the consequences of the proposed design.
- Accuracy versus rounds does not establish wall-clock speedup. FLOPs do not establish measured energy savings. A local optimum or stationary point is not a global optimum.
- Keeping raw data local does not establish formal privacy or security. State the threat model or the limited data-locality claim.
- Use real mobility traces, hardware, or emulation when the claim requires them and the author has them. Label simulations accurately and bound deployment claims when direct evidence is absent.
- Preserve negative results and limitations. Suggest missing evidence as a proposed action; do not claim it was already obtained.

## Deliver the requested scope

Lead with the requested prose or edited file. Add only material structural decisions, evidence gaps, or notation changes. For a full outline or paper audit, include the claim ledger and prioritized issues with verified source locations. Do not attach every possible checklist to every answer.
