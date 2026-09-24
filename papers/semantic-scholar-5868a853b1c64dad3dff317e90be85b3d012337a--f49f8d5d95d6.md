---
identifier: semantic_scholar:5868a853b1c64dad3dff317e90be85b3d012337a
title: Improving Naturalness and Controllability of Sequence-to-Sequence Speech Synthesis by Learning Local Prosody Representations
authors:
- Cheng Gong
- Longbiao Wang
- Zhenhua Ling
- Shaotong Guo
- Ju Zhang
- J. Dang
published: '2021-06-06T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/5868a853b1c64dad3dff317e90be85b3d012337a
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

State-of-the-art neural text-to-speech (TTS) networks are trained with a large amount of speech data, which significantly improves the quality of synthetic speech compared with traditional approaches. However, the prosody and controllability of the generated speech is still insufficient, especially in tonal languages. Moreover, the generated prosody is solely defined by the input text, which does not allow for different styles for the same sentence or words. In this study, we extended Tacotron2 with a pitch prediction task to capture discrete pitch-related representations. Specifically, the learned pitch-related suprasegmental information is fed simultaneously with traditional character features into the decoder to generate final Mel spectrogram. Experiments show that the proposed method can improve the quality of the generated speech (mean opinion score of 4.37 vs. 4.22). Moreover, we demonstrated that we can easily achieve word-level pitch control during generation by changing local pitch-related representations before passing them to the decoder network.
