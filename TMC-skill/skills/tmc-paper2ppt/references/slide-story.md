# Slide story and evidence

## A flexible story

For a research group talk, a useful sequence is:

`application and constraint -> failure of existing approach -> design insight -> architecture/timeline -> key mechanism/analysis -> evaluation setup -> decisive results -> limitations and discussion`.

Adjust detail to the audience and time. A 15-minute slot does not imply a mandatory slide count. Remove peripheral related work or proof detail before rushing the central mechanism. A comparison of several papers needs a shared question and comparison axes rather than repeated independent paper summaries.

## Explain the technical contribution

- **System work:** explain what runs where, message/data flow, scheduling decisions, overhead, and the actual implementation boundary.
- **Optimization/theory:** show objective and constraints in readable form, the difficulty, solution idea, and exact guarantee. Explain assumptions without pasting the proof.
- **FL/PEFT:** show the update/aggregation timeline, adaptation decision, heterogeneous resources or ranks, and what is uploaded or kept local.
- **Security:** show assets, adversary visibility/capabilities, attack/defense flow, empirical versus formal guarantee, and benign utility cost.

Treat the paper's own diagram as a source to explain, not a substitute for explanation. A simplified redraw should preserve operational meaning and be labelled as adapted.

## Results slides

State the question or supported conclusion in the title, with the condition needed to make it true. Explain axes, baseline, budget, evidence type and the visual feature the audience should notice. Zoom to a panel if the full multi-panel figure is unreadable; retain panel identity and do not crop away a contrary condition that changes interpretation.

Keep time, rounds, communication, energy and accuracy separate. A real dataset does not make a simulator result a real-device measurement. An ablation supports a mechanism only under its comparison assumptions. Do not silently strengthen an abstract's reported claims while translating them.

## Source and critique discipline

Keep `PDF page | figure/table/equation/section | slide(s)` in notes or a small source map. Identify source authors/title/version in the deck. Clearly mark presenter interpretations, unresolved questions, and possible research ideas. Do not attribute an extension to the paper unless it actually contains it.

## Visual checks

Use large enough labels to read in presentation mode. Split dense equations and tables; do not shrink a page screenshot until every annotation is illegible. Maintain consistent terms, colors and symbols. Explain acronyms on first use. Add notes when the slide alone is intentionally terse.

Verify the rendered deck and editable output, all figure assets and source anchors, and the correspondence between slide claims and paper evidence. Do not claim the audience will reproduce results from slides alone.
