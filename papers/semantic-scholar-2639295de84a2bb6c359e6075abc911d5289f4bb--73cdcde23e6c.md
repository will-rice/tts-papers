---
identifier: semantic_scholar:2639295de84a2bb6c359e6075abc911d5289f4bb
title: A New End-to-End Long-Time Speech Synthesis System Based on Tacotron2
authors:
- Renyuan Liu
- Jian Yang
- Mengyuan Liu
published: '2019-09-20T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/2639295de84a2bb6c359e6075abc911d5289f4bb
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

End-to-end speech synthesis breaks away from the original system framework and directly converts text into speech. Although it is shown that Tacotron2 is superior to traditional piping systems in terms of speech naturalness, it still has many defects. A flaw in tacotron2 is mentioned in this paper., which impacts negatively upon the synthesis quality and the synthesized length of speech. It is cumulative error between training process (forward) and synthesis process (inference). In order to improve this problem, an unsupervised GAN (Generative Adversarial Network) model was proposed based on the Tacotron2. The proposed GAN model can also optimize the prosody of synthesize speech because of the prosody discriminator is also designed in our model. For further reduce the cumulative error mentioned above, this paper propose a training strategy called "random down" based on Tacotron2. And then demonstrate that the unimportant attention weights could be a contributing factor to cumulative error when the input sequence is too long. For this, a window has been added to the attention weights. Through these method, the length of the speech synthesis is improved to about 1000 encoder output. The prosody of synthetic speech has also been improved.
