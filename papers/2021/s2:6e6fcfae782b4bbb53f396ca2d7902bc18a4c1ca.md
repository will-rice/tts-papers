---
arxiv_id: s2:6e6fcfae782b4bbb53f396ca2d7902bc18a4c1ca
title:
  Prosody prediction for arabic via the open-source boundary-annotated qur’an
  corpus
authors:
  - M. Sawalha
  - C. Brierley
  - E. Atwell
submitted: "2021-02-04"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/6e6fcfae782b4bbb53f396ca2d7902bc18a4c1ca
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:42:28+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

A phrase break classifier is needed to predict natural prosodic pauses in text to be read out loud by humans or machines. To develop phrase break classifiers, we need a boundary-annotated and part-of-speech tagged corpus. Boundary annotations in English speech corpora are descriptive, delimiting intonation units perceived by the listener; manual annotation must be done by an expert linguist. For Arabic, there are no existing suitable resources. We take a novel approach to phrase break prediction for Arabic, deriving our prosodic annotation scheme from Tajwid (recitation) mark-up in the Qur’an which we then interpret as additional text-based data for computational analysis. This mark-up is prescriptive, and signifies a widely-used recitation style, and one of seven original styles of transmission. Here we report on version 1.0 of our Boundary-Annotated Qur’an dataset of 77430 words and 8230 sentences, where each word is tagged with prosodic and syntactic information at two coarse-grained levels. We then use this dataset to train, test, and compare two probabilistic taggers (trigram and HMM) for Arabic phrase break prediction, where the task is to predict boundary locations in an unseen test set stripped of boundary annotations by classifying words as breaks or non-breaks. The preponderance of non-breaks in the training data sets a challenging baseline success rate: 85.56%. However, we achieve significant gains in accuracy with a trigram tagger, and significant gains in performance recognition of minority class instances with both taggers via the Balanced Classification Rate metric. This is initial work on a long-term research project to produce annotation schemes, language resources, algorithms, and applications for Classical and Modern Standard Arabic.
