---
identifier: semantic_scholar:dd62b9638086e422581f60e24e5b39d67f2eebe8
title: 'TM-SPEECH: END-TO-END TEXT TO SPEECH BASED ON INTEGRATING TRANSFORMER AND MAMBA'
authors:
- Long Wang
published: '2025-01-01T00:00:00+00:00'
url: https://www.semanticscholar.org/paper/dd62b9638086e422581f60e24e5b39d67f2eebe8
source: semantic_scholar
doi: null
arxiv_id: null
categories: []
---

## Abstract

Text-to-speech synthesis is the process of converting natural language text into speech. In recent years, deep learning has made significant strides in this field. Although the Transformer model is effective at capturing dependencies, its attention mechanism’s quadratic complexity results in longer training times and increased costs. Recent advancements in state-space models SSMs have demonstrated impressive performance in modeling long-range dependencies due to their sub-quadratic complexity. Mamba, a notable example of SSMs, exhibits linear time complexity and excels in tasks involving long sequences, similar to those in natural language. In this paper, we propose TM-Speech, which integrates Mamba for modeling long-range dependencies and Transformer for capturing short-range dependencies, thereby reducing model training costs. Comparative experiments show that TM-Speech is almost 2× smaller and 3× faster than FastSpeech2 during training, while also achieving superior inferred audio quality. The code is available at https: github.com Apolarity886 TMSpeech.
