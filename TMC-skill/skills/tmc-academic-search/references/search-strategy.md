# Search strategy for mobile and edge research

## Concept grid

| Axis | Examples; select only what is relevant |
|---|---|
| Setting | mobile edge, on-device, vehicular, UAV, LEO satellite, wireless sensor, TSN, crowdsensing |
| Mechanism | scheduling, client selection, topology, resource allocation, distillation, layer freezing, submodel, LoRA, PEFT |
| Failure | straggler, staleness, memory limit, intermittent connectivity, drift, non-IID, label scarcity, leakage |
| Target | time-to-accuracy, energy, memory, communication, fairness, reliability, deadline, attack success |

Construct queries such as `"federated learning" asynchronous resource adaptation`, `"LoRA" federated heterogeneous edge memory`, or `"decentralized learning" topology energy`. These are examples, not a frozen search strategy. Add venue/year constraints only when the user asks or after a broad mechanism search. Search titles exactly to resolve records, not as the only discovery method.

## Provenance record

For a review or update, retain `query | source | date | filters | results screened | exclusions`. A practical paper record is `title | primary URL/DOI | publication status/date | task | assumption | mechanism | evidence type | access/screening state | relevance`.

Metadata can establish identity, not a detailed experimental claim. Before recommending a baseline, check that its method can operate under the relevant information, resource and synchronization assumptions. If not, explain the adaptation or label it as an oracle/comparison of a different setting.

## Version and date handling

DOI normalization removes an explicit DOI URL/prefix and terminal bibliographic punctuation. Match titles/authors too; a DOI conflict needs investigation. Without a DOI, compare normalized title, authors, venue and date manually. A preprint and journal extension may differ in method and evidence; record which one was read and cite the version that supports the claim.

For a recent-literature request, state the search date and date field used. Do not treat the journal issue month as first public availability. If first-visible publication time is the task, consult official early-access surfaces and record evidence rather than inferring from volume numbers.

## Claim support when no separate citation skill is loaded

Split compound claims. Map each clause to a paper location and classify `direct`, `partial`, `background`, `limiting/contradictory`, or `metadata-only`. Read the relevant content before assigning direct support. A review can support a field overview; it is weaker than an original result for a specific experimental claim. Do not infer a paper's performance, code license or resource requirements from its title.

## Unavailable sources

Try lawful author/preprint copies and label version differences. If only an abstract is available, give an abstract-screened candidate and the access limitation. Do not invent full-text conclusions or bypass paywalls. When a service fails, use remaining sources and disclose a material coverage gap instead of repeatedly retrying an unchanged failure.
