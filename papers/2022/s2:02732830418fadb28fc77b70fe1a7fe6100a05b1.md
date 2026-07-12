---
arxiv_id: s2:02732830418fadb28fc77b70fe1a7fe6100a05b1
title:
  "MIST-Tacotron: End-to-End Emotional Speech Synthesis Using Mel-Spectrogram
  Image Style Transfer"
authors:
  - Sung-Woo Moon
  - Sunghyun Kim
  - Yong-Hoon Choi
submitted: "2022-01-01"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/02732830418fadb28fc77b70fe1a7fe6100a05b1
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:36:06+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

With the development of voice synthesis technology using deep learning, voice synthesis research that expresses the characteristics and emotions of speakers is actively being conducted. Current technology does not satisfactorily express various emotions and characteristics for speakers with very low or high vocal ranges and for speakers with dialects. In this paper, we propose mel-spectrogram image transfer (MIST)-Tacotron, a Tacotron 2-based speech synthesis model that adds a reference encoder with an image style transfer module. The proposed method is a technique that adds image style transfer to the existing Tacotron 2 model and extracts the speaker’s feature from the reference mel-spectrogram using a pre-trained deep learning model. Through the extracted feature, the style such as pitch, tone, and duration of the speaker are trained to express the style and emotion of the speaker more clearly. To extract the speaker’s style independently from the speaker’s timbre and emotion, the ID value for the speaker and the ID value for the emotional state were used as inputs. Performance is evaluated by F0 voiced error (FVE), F0 gross pitch error (F0 GPE), mel-cepstral distortion (MCD), band aperiodicity distortion (BAPD), voiced/unvoiced error (VUVE), false positive rate (FPR), and false negative rate (FNR). The performance of the proposed model was observed to have lower error values than the existing models, GST (Global Style Token) Tacotron and VAE (Variational Autoencoder) Tacotron. As a result of measuring mean opinion score (MOS), the sound quality of the proposed model received the highest score in terms of emotional expression and speaker style reflection.
