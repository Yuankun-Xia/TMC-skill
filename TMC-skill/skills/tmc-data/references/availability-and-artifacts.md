# Availability and artifact checklist

## Evidence-to-artifact mapping

| Artifact | Reproducibility details to retain |
|---|---|
| Public dataset | Exact source/version, task split, preprocessing, source license and citation |
| FL partition | Client IDs/sizes, partition algorithm and seed, label/feature/quantity skew, drift generation |
| Device/network setup | Hardware, OS/framework, power/memory measurement, bandwidth and timing assumptions |
| Mobility/topology trace | Source/version, timestamps and units, replay/simulation parameters, link/contact model |
| Model/checkpoint | Architecture, initialization, pretrained source/version, PEFT modules/rank/precision, license |
| Experiment code | Commit/release, environment, runnable commands, configuration and seed scope |
| Results/figures | Raw or minimally processed logs, aggregation script, included/excluded runs, source data per figure |
| Security evaluation | Adversary/attack settings, budgets and metrics, synthetic or restricted sensitive artifacts |

Choose rows tied to the paper's claims; do not ask for irrelevant artifacts. A simulator configuration should distinguish measured inputs from modelled quantities. When traces could identify people/devices, use the actual authorized access terms and describe the permitted release rather than assuming open distribution.

## Availability patterns

Use these only after replacing fields with verified facts. They are drafting patterns, not factual statements about an existing release.

- Public code/data: "The implementation and configurations for [experiments] are available at [verified repository and version]. The source data for Figs. [verified identifiers] are included in [verified release path]."
- Reused public data: "This study uses [dataset/version], available from [verified source]. The preprocessing and client partition configurations are provided at [actual location]."
- Restricted data: "The [artifact] cannot be released publicly because [actual restriction]. Access is managed by [actual controller/process]. [Permitted metadata or substitute] is available at [actual location, if any]."
- Planned release: "The authors plan to release [specific artifacts] at [stage]." Keep this as an author-confirmed plan; it does not imply current public access or acceptance by a journal.

For "available upon reasonable request," clarify what can be supplied, the real restriction, who controls access and the actual procedure. Do not invent a formal access process. Avoid saying that everything needed for reproduction is available when only the model code exists.

## Release verification

Check that identifiers resolve to the actual artifact/version. A mutable branch or personal drive link may be less stable than a tagged release/archive; recommend a stable version when useful without mandating a particular vendor. Verify README instructions against the actual files if code audit is in scope. Separate evidence that a link loads from evidence that the experiment reproduces.

Keep data/code/model licenses distinct. A code license does not grant redistribution rights for third-party datasets or pretrained weights. Do not add licensing terms or publish an archive on the author's behalf without authorization.
