---
arxiv_id: s2:26916f3a9c4b5470adbacacbbe23ea1b69234e52
title:
  Joint Modeling and KAFusion Feature Fusion for Prosody-Controllable Speech
  Synthesis
authors:
  - Dongfeng Ye
  - Lin Jiang
  - Nianxin Ni
  - Wei Wan
submitted: "2026-03-25"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/26916f3a9c4b5470adbacacbbe23ea1b69234e52
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T15:48:16+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

To address the limited expressiveness in current speech synthesis caused by coarse-grained prosody modeling and simplistic feature fusion strategies, a joint prosody modeling framework and a nonlinear fusion method named KAFusion are proposed, based on the Kolmogorov–Arnold (KA) representation theorem. The joint modeling integrates pitch and energy as prosodic priors with text encodings to jointly guide duration prediction, enabling explicit control over speech rate and tone. During feature fusion, KAFusion facilitates nonlinear interactions among features through its nested inner and outer functions. Information entropy serves as the quantitative metric, and both theoretical and experimental results demonstrate the fusion module’s efficacy in suppressing redundancy while preserving task-critical content. Evaluations on the AISHELL3 dataset show a 5.8% improvement in MOS over the baseline. Ablation studies further validate the effectiveness of the proposed components, where KAFusion achieves an output entropy of 3.47, which is 18.4% higher than that of linear fusion (2.93) and indicates richer information content.
