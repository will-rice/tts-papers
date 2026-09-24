---
arxiv_id: s2:bcaf9448e14b750ba5f9eb47770a7aa3012515bf
title:
  "Factorized-VITS: Decoupling Prosody and Text in End-to-End Speech Synthesis
  without External or Secondary Aligner"
authors:
  - Yining Liu
  - Alexander Waibel
submitted: "2025-04-06"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/bcaf9448e14b750ba5f9eb47770a7aa3012515bf
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:04:09+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

We propose Factorized-VITS, an advanced end-to-end text-to-speech model that incorporates explicit text-side prosody modeling control into VITS while achieving a clean factorization of the audio prior hidden space into text and prosody subspaces. Unlike previous works that rely on external or secondary aligners, Factorized-VITS is the first work attempting to do on-the-fly alignment in the factorized text subspace without introducing extra parameters, which not only simplifies the training procedure but also enables the use of a more complex prosody prior. Our experiments demonstrate the accuracy and effectiveness of this approximation strategy. Furthermore, we implement an in-context learning joint predictor for pitch, energy, and duration, which offers a flexible streaming deployment option.
