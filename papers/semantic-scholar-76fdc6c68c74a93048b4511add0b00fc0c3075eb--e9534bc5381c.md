---
arxiv_id: s2:76fdc6c68c74a93048b4511add0b00fc0c3075eb
title: Prosody Prediction with Discriminative Representation Method
authors:
  - Jipeng Zhang
  - Hankiz Yilahun
  - Xiaoqin Feng
  - Yunlin Chen
  - Xipeng Yang
  - Askar Hamdulla
submitted: "2022-07-22"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/76fdc6c68c74a93048b4511add0b00fc0c3075eb
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:31:33+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Rhythm affects the naturalness and intelligibility of Text-To-Speech (TTS). However, rhythm prediction remains a great challenge, usually in two aspects: 1) the united annotation is a relatively difficult task, which depends on expert’s experience. 2) traditional methods based on conditional random field (CRF), which heavily rely on feature engineering, such as word segmentation, part of speech(pos) etc. For above problems, we propose a method to reduce the dependency for united annotation data and conduct the joint experiment which use one unified model on independent data. Meanwhile, we also propose an algorithm of Layer Look Up Table (LLUT): use an embedding layer to learn a discriminative representation for different level of prosody data without any feature engineering. By using this method, the classifier can share the parameters and predict for different prosody level separately, which reduces the number of trainable model parameters. In order to better represent the input text, we use the pre-training model, like BERT, to provide the semantic information. Our experiment shows that the method of LLUT, is better able to acquire the discriminative meaning of different prosody levels. And also, our algorithm is proved to be general for sequence annotation tasks thus we can do extra task, like polyphone-prosody prediction.
