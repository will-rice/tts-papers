---
identifier: semantic_scholar:ed8789ba7c5962f47faeea3898a8f64d59123790
title: Unifying One-Shot Voice Conversion and Cloning with Disentangled Speech Representations
authors:
- Hui Lu
- Xixin Wu
- Haohan Guo
- Songxiang Liu
- Zhiyong Wu
- Helen M. Meng
published: '2024-04-14T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/ed8789ba7c5962f47faeea3898a8f64d59123790
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

We propose unifying one-shot voice conversion and cloning into a single model that can be end-to-end optimized. To achieve this, we introduce a novel extension to a speech variational auto-encoder (VAE) that disentangles speech into content and speaker representations. Instead of using a fixed Gaussian prior as in the vanilla VAE, we incorporate a learnable text-aware prior as an informative guide for learning the content representation. This results in a content representation with reduced speaker information and more accurate linguistic information. The proposed model can sample the content representation using either the posterior conditioned on speech or the text-aware prior with textual input, enabling one-shot voice conversion and cloning, respectively. Experiments show that the proposed method achieves better or comparable overall performance for one-shot voice conversion and cloning compared to state-of-the-art voice conversion and cloning methods.
