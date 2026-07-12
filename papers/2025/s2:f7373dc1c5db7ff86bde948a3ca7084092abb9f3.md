---
arxiv_id: s2:f7373dc1c5db7ff86bde948a3ca7084092abb9f3
title:
  "DistillW2N: A Lightweight One-Shot Whisper to Normal Voice Conversion Model
  Using Distillation of Self-Supervised Features"
authors:
  - Tianyi Tan
  - Haoxin Ruan
  - Xin'an Chen
  - Kai-Jyun Chen
  - Zhibin Lin
  - Jing Lu
submitted: "2025-04-06"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/f7373dc1c5db7ff86bde948a3ca7084092abb9f3
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:04:09+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Whisper to Normal voice conversion (W2N) holds great promise for assistive communication and healthcare, making it an exciting area of research and development. Recent advancements in W2N are predominantly driven by self-supervised speech representation learning (SSL) techniques. While effective, SSL requires extensive parameters and high computational costs, making it impractical to be deployed in real-world applications. We propose DistillW2N, a lightweight one-shot W2N model. DistillW2N consists of a speech-to-unit (S2U) encoder, which seeks to close the gap between whispered and normal content units by distilling HuBERT-Soft representations from both normal speech and pseudo-whisper, and a unit-to-speech (U2S) decoder, which incorporates content units with timbre units by Style-Adaptive Layer Normalization (SALN) and leverages SoundStream decoder for lightweight high-quality speech synthesis. Moreover, we discover that the S2U encoder is able to learn from a VAD model to trim noise. Experiments show that DistillW2N significantly improves the intelligibility for whisper while preserving speaker similarity compared to prevailing SSL approaches. The resulting model demands only 10.91 M parameters and 1.63 GMACs per second and runs approximately 5 times faster than QuickVC. All samples and code are available at https://github.com/tan90xx/distillw2n.
