---
arxiv_id: s2:b9b250920d2fe542a16aab0d8bf5d329d4ca86ab
title: A neural speech decoding framework leveraging deep learning and speech synthesis
authors:
  - Xupeng Chen
  - Ran Wang
  - Amirhossein Khalilian-Gourtani
  - Leyao Yu
  - Patricia Dugan
  - Daniel Friedman
  - W. Doyle
  - O. Devinsky
  - Yao Wang
  - A. Flinker
submitted: "2024-04-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/b9b250920d2fe542a16aab0d8bf5d329d4ca86ab
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-08T06:59:46+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Recent research has focused on restoring speech in populations with neurological deficits. Chen, Wang et al. develop a framework for decoding speech from neural signals, which could lead to innovative speech prostheses. Decoding human speech from neural signals is essential for brain–computer interface (BCI) technologies that aim to restore speech in populations with neurological deficits. However, it remains a highly challenging task, compounded by the scarce availability of neural signals with corresponding speech, data complexity and high dimensionality. Here we present a novel deep learning-based neural speech decoding framework that includes an ECoG decoder that translates electrocorticographic (ECoG) signals from the cortex into interpretable speech parameters and a novel differentiable speech synthesizer that maps speech parameters to spectrograms. We have developed a companion speech-to-speech auto-encoder consisting of a speech encoder and the same speech synthesizer to generate reference speech parameters to facilitate the ECoG decoder training. This framework generates natural-sounding speech and is highly reproducible across a cohort of 48 participants. Our experimental results show that our models can decode speech with high correlation, even when limited to only causal operations, which is necessary for adoption by real-time neural prostheses. Finally, we successfully decode speech in participants with either left or right hemisphere coverage, which could lead to speech prostheses in patients with deficits resulting from left hemisphere damage.
