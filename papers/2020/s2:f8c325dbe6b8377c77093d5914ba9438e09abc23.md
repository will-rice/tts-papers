---
arxiv_id: s2:f8c325dbe6b8377c77093d5914ba9438e09abc23
title:
  Dynamic Speaker Representations Adjustment and Decoder Factorization for Speaker
  Adaptation in End-to-End Speech Synthesis
authors:
  - Ruibo Fu
  - J. Tao
  - Zhengqi Wen
  - Jiangyan Yi
  - Tao Wang
  - Chunyu Qiang
submitted: "2020-10-25"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/f8c325dbe6b8377c77093d5914ba9438e09abc23
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:44:14+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

End-to-end speech synthesis can reach high quality and naturalness with low-resource adaptation data. However, the generalization of out-domain texts and the improving modeling accuracy of speaker representations are still challenging tasks. The limited adaptation data leads to unacceptable errors and low similarity of the synthetic speech. In this paper, both speaker representations modeling and acoustic model structure are improved for the speaker adaptation task. On the one hand, compared with the conventional methods that focused on using ﬁxed global speaker representations, the attention gating is proposed to adjust speaker representations dynamically based on the attended context and prosody information, which can describe more pronunciation characteristics in phoneme level. On the other hand, to improve the robustness and avoid over-ﬁtting, the decoder model is factored into average-net and adaptation-net, which are designed for learning speaker independent acoustic features and target speaker timbre imitation respectively. And the context discriminator is pre-trained by large ASR data to supervise the average-net generating proper speaker independent acoustic features for different phoneme. Experimental results on Mandarin dataset show that proposed methods lead to an improvement on intelligibility, naturalness and similarity.
