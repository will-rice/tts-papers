---
identifier: semantic_scholar:76fdc6c68c74a93048b4511add0b00fc0c3075eb
title: Prosody Prediction with Discriminative Representation Method
authors:
- Jipeng Zhang
- Hankiz Yilahun
- Xiaoqin Feng
- Yunlin Chen
- Xipeng Yang
- Askar Hamdulla
published: '2022-07-22T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/76fdc6c68c74a93048b4511add0b00fc0c3075eb
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Rhythm affects the naturalness and intelligibility of Text-To-Speech (TTS). However, rhythm prediction remains a great challenge, usually in two aspects: 1) the united annotation is a relatively difficult task, which depends on expert’s experience. 2) traditional methods based on conditional random field (CRF), which heavily rely on feature engineering, such as word segmentation, part of speech(pos) etc. For above problems, we propose a method to reduce the dependency for united annotation data and conduct the joint experiment which use one unified model on independent data. Meanwhile, we also propose an algorithm of Layer Look Up Table (LLUT): use an embedding layer to learn a discriminative representation for different level of prosody data without any feature engineering. By using this method, the classifier can share the parameters and predict for different prosody level separately, which reduces the number of trainable model parameters. In order to better represent the input text, we use the pre-training model, like BERT, to provide the semantic information. Our experiment shows that the method of LLUT, is better able to acquire the discriminative meaning of different prosody levels. And also, our algorithm is proved to be general for sequence annotation tasks thus we can do extra task, like polyphone-prosody prediction.
