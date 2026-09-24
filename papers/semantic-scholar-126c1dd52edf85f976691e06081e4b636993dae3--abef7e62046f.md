---
identifier: semantic_scholar:126c1dd52edf85f976691e06081e4b636993dae3
title: 'Wav2vec-VC: Voice Conversion via Hidden Representations of Wav2vec 2.0'
authors:
- Jaemin Lim
- Kiyeon Kim
published: '2024-04-14T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/126c1dd52edf85f976691e06081e4b636993dae3
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

This paper describes an unconventional way to use wav2vec 2.0 representations for voice conversion (VC) purpose. Our experiment shows that aggregate of hidden representations from wav2vec 2.0 layers is more effective in VC than using last-layer representation only. In particular, the aggregate of all hidden representations is dependent on a mainly required characteristic (e.g. vocal or linguistic) by a speech task—but such results are consistent on different datasets for the same task. Based on these results, we propose Wav2vec-VC that uses wav2vec 2.0 hidden-layer representations as input to the disentanglement-based VC. Given a target (/source) utterance, Wav2vec-VC gets an aggregated hidden representation weighted in order to perform the speaker (/content)-related tasks, and feeds it to a speaker (/content) encoder whose output is combined at a decoder to synthesize a voice-converted utterance. Our evaluation shows that Wav2vec-VC outperforms SOTA VC models in terms of both voice similarity and speech intelligibility.
