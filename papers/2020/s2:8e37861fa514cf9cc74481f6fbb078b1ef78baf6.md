---
arxiv_id: s2:8e37861fa514cf9cc74481f6fbb078b1ef78baf6
title: A Graph-Based Framework for Structured Prediction Tasks in Sanskrit
authors:
  - Amrith Krishna
  - Ashim Gupta
  - Pawan Goyal
  - Bishal Santra
  - Pavankumar Satuluri
submitted: "2020-10-22"
categories: []
arxiv_url: https://www.semanticscholar.org/paper/8e37861fa514cf9cc74481f6fbb078b1ef78baf6
source: metadata-only
converter: none
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:44:23+00:00"
references_parsed: 0
arxiv_version: ""
---

## Abstract

Abstract We propose a framework using energy-based models for multiple structured prediction tasks in Sanskrit. Ours is an arc-factored model, similar to the graph-based parsing approaches, and we consider the tasks of word segmentation, morphological parsing, dependency parsing, syntactic linearization, and prosodification, a “prosody-level” task we introduce in this work. Ours is a search-based structured prediction framework, which expects a graph as input, where relevant linguistic information is encoded in the nodes, and the edges are then used to indicate the association between these nodes. Typically, the state-of-the-art models for morphosyntactic tasks in morphologically rich languages still rely on hand-crafted features for their performance. But here, we automate the learning of the feature function. The feature function so learned, along with the search space we construct, encode relevant linguistic information for the tasks we consider. This enables us to substantially reduce the training data requirements to as low as 10%, as compared to the data requirements for the neural state-of-the-art models. Our experiments in Czech and Sanskrit show the language-agnostic nature of the framework, where we train highly competitive models for both the languages. Moreover, our framework enables us to incorporate language-specific constraints to prune the search space and to filter the candidates during inference. We obtain significant improvements in morphosyntactic tasks for Sanskrit by incorporating language-specific constraints into the model. In all the tasks we discuss for Sanskrit, we either achieve state-of-the-art results or ours is the only data-driven solution for those tasks.
