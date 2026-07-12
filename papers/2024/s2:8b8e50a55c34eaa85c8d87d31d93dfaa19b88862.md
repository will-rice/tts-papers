---
arxiv_id: s2:8b8e50a55c34eaa85c8d87d31d93dfaa19b88862
title: "CycleDiffusion: Voice Conversion Using Cycle-Consistent Diffusion Models"
authors:
  - D. Yook
  - Geonhee Han
  - Hyung-Pil Chang
  - In-Chul Yoo
submitted: "2024-10-21"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/8b8e50a55c34eaa85c8d87d31d93dfaa19b88862
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:08:56+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Voice conversion (VC) refers to the technique of modifying one speaker’s voice to mimic another’s while retaining the original linguistic content. This technology finds its applications in fields such as speech synthesis, accent modification, medicine, security, privacy, and entertainment. Among the various deep generative models used for voice conversion, including variational autoencoders (VAEs) and generative adversarial networks (GANs), diffusion models (DMs) have recently gained attention as promising methods due to their training stability and strong performance in data generation. Nevertheless, traditional DMs focus mainly on learning reconstruction paths like VAEs, rather than conversion paths as GANs do, thereby restricting the quality of the converted speech. To overcome this limitation and enhance voice conversion performance, we propose a cycle-consistent diffusion (CycleDiffusion) model, which comprises two DMs: one for converting the source speaker’s voice to the target speaker’s voice and the other for converting it back to the source speaker’s voice. By employing two DMs and enforcing a cycle consistency loss, the CycleDiffusion model effectively learns both reconstruction and conversion paths, producing high-quality converted speech. The effectiveness of the proposed model in voice conversion is validated through experiments using the VCTK (Voice Cloning Toolkit) dataset.
