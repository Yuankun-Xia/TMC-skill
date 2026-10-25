---
name: tmc-data
description: Prepare or audit data/code availability statements and reproducibility packages for TMC research. Use for dataset and model provenance, experiment artifacts, figure source data, repository plans, restricted access, and Chinese-to-English availability statements.
---

# TMC Data and Reproducibility

Connect the paper's evidence to the artifacts a reader can inspect or reuse. Read [availability and artifact checklist](references/availability-and-artifacts.md). Read [TMC context and sources](references/tmc-context.md) before asserting a journal-specific requirement.

IEEE reproducibility guidance encourages sharing methods, data and code. Do not convert that encouragement into a universal TMC mandate to publish every dataset, use a particular repository, or add a statement at a fixed location. Check the current journal/submission requirements when the task depends on them.

## Workflow

1. Inventory reused/generated datasets, data partitions, simulator/traces, models/checkpoints, code/configs, run logs, summary tables and figure source data relevant to the actual claims.
2. Identify what exists, what is shareable, what is released and what remains planned. A local Git repository is not a public release; a planned URL is not an accessible archive.
3. Map each artifact to a public versioned repository, justified controlled/request access, third-party source, paper/supplement, or explicit absence. Preserve source licenses and access terms; do not assume derived model weights can be redistributed.
4. Draft an accurate statement with real identifiers and version/commit information where available. For restricted artifacts, state the real reason, access route and any shareable substitute or metadata.
5. Verify supplied links and release contents when accessible, distinguishing public from private/authenticated access. Identify broken links, missing logs/configs and steps needed for reproducibility.

For FL/mobile research, capture seeds and client splits, data heterogeneity generation, selected clients, time-varying workload/topology traces, device/software versions, network conditions and metric accounting as relevant. These details can matter more than simply naming the public dataset.

Do not invent a DOI, license, repository release, ethics approval, access committee or embargo. Draft planned release text conditionally and keep unresolved fields visible. Do not upload or publish artifacts unless the user authorizes that action.

## Output

Provide the requested availability statement or artifact plan. Normally use English for submission text and brief Chinese notes for unresolved author decisions. For an audit, provide `artifact -> location/version -> access state -> missing action`, prioritized by the claims affected. Do not replace an availability task with a full methods rewrite.
