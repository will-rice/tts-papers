---
arxiv_id: s2:a94a3d53897c0a585d8d7f2d75153f07c00f428c
title:
  Knowledge-Based Linguistic Encoding for End-to-End Mandarin Text-to-Speech
  Synthesis
authors:
  - Jingbei Li
  - Zhiyong Wu
  - Runnan Li
  - Pengpeng Zhi
  - Song Yang
  - H. Meng
submitted: "2019-09-15"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/a94a3d53897c0a585d8d7f2d75153f07c00f428c
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:49:44+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Recent researches have shown superior performance of applying end-to-end architecture in text-to-speech (TTS) synthesis. However, considering the complex linguistic structure of Chinese, using Chinese characters directly for Mandarin TTS may suffer from the poor linguistic encoding performance, resulting in improper word tokenization and pronunciation errors. To ensure the naturalness and intelligibility of synthetic speech, state-of-the-art Mandarin TTS systems employ a list of components, such as word tokenization, part-of-speech (POS) tagging and grapheme-to-phoneme (G2P) conversion, to produce knowledge-enhanced inputs to alleviate the problems caused by linguistic encoding. These components are based on linguistic expertise and well-designed, but trained individually, leading to errors compounding for the TTS system. In this paper, to reduce the complexity of Mandarin TTS system and bring further improvement, we proposed a knowledge-based linguistic encoder for the character-based end-to-end Mandarin TTS system. Developed with multi-task learning structure, the proposed encoder can learn from linguistic analysis subtasks, providing robust and discriminative linguistic encodings for the following speech generation decoder. Experimental results demonstrate the effectiveness of the proposed framework, with word tokenization error dropped from 12.81% to 1.58%, syllable pronunciation error dropped from 10.89% to 2.81% compared with state-of-the-art baseline approach, providing mean opinion score (MOS) improvement from 3.76 to 3.87.
