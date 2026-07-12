---
arxiv_id: "2012.02626"
title: "GraphPB: Graphical Representations of Prosody Boundary in Speech Synthesis"
authors:
  - Aolan Sun
  - Jianzong Wang
  - Ning Cheng
  - Huayi Peng
  - Zhen Zeng
  - Lingwei Kong
  - Jing Xiao
submitted: "2020-12-03"
categories:
  - eess.AS
  - cs.CL
  - cs.SD
arxiv_url: https://arxiv.org/abs/2012.02626
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-07-07T16:43:20+00:00"
references_parsed: 0
arxiv_version: ""
---

# GraphPB: Graphical Representations of Prosody Boundary in Speech Synthesis

###### Abstract

This paper introduces a graphical representation approach of prosody boundary (GraphPB) in the task of Chinese speech synthesis, intending to parse the semantic and syntactic relationship of input sequences in a graphical domain for improving the prosody performance. The nodes of the graph embedding are formed by prosodic words, and the edges are formed by the other prosodic boundaries, namely prosodic phrase boundary (PPH) and intonation phrase boundary (IPH). Different Graph Neural Networks (GNN) like Gated Graph Neural Network (GGNN) and Graph Long Short-term Memory (G-LSTM) are utilised as graph encoders to exploit the graphical prosody boundary information. Graph-to-sequence model is proposed and formed by a graph encoder and an attentional decoder. Two techniques are proposed to embed sequential information into the graph-to-sequence text-to-speech model. The experimental results show that this proposed approach can encode the phonetic and prosody rhythm of an utterance. The mean opinion score (MOS) of these GNN models shows comparative results with the state-of-the-art sequence-to-sequence models with better performance in the aspect of prosody. This provides an alternative approach for prosody modelling in end-to-end speech synthesis.\

Index Terms—  graph neural network, neural text-to-speech, speech synthesis, prosody modelling

## 1 Introduction

In the field of neural text-to-speech, prosody is a crucial factor to determine intelligibility and naturalness of synthesised speech. Prosody can be refined as three suprasegmental features, fundamental frequency, loudness, and duration \[1, 2\]. In the task of prosody modelling in neural text-to-speech, \[3, 4\] firstly try to introduce a latent vector for prosody embedding which is extracted from the mel-spectrograms of the reference audios, then a global style token is introduced to be trained by multi-head attention for style encoding \[5, 6\]. Variational Auto Encoder (VAE) \[7\] is tried to be used for prosody classifying for good prosody control. \[8\] learns a latent embedding space of emotion derived from a desired emotional identity in a multi-speaker system. In order to achieve more precise local prosody control, \[9\] introduces temporal structure to enable fine-grained control of the speaking style of the synthesised speech. \[10\] tries a semi-supervised speech synthesis framework in which prosodic labels of training data are partially annotated. \[11\] introduces a novel multi-reference structure to Tacotron to extract and separate different classes of speech styles: speaker, emotion and prosody.

Most of these methods try to analyse the prosody of a sentence from the speech-side, specifically exploiting prosody embedding from spectrograms of audios\[12\]. With the development of the pre-trained models like Bidirectional Encoder Representation from Transformers (BERT) \[13\] in the Natural Language Processing (NLP) tasks, some research is conducted on analysing prosody from text-side of text-to-speech. \[14, 15\] try to use BERT to encode input phrases, as an additional input to a Tacotron2-based sequence-to-sequence TTS model. However, the connection relationship between words is not fully reflected, which is an important factor that affects the rhythm and emotion of synthesised speech. \[16\] firstly proposes to exploit the information embedded in a syntactically parse tree information to further improve the TTS quality. \[17\] proposes GraphTTS to model character-level and phoneme-level graph structure of the input utterance .The prosody boundary information \[18\] is tried to be embedded into the Tacotron \[19, 20\] model by \[21\] through adding a context encoder analysing the context information. But the two separate Tacotron-like encoders project context features into two different domains. This may result in the exposure bias during model training and inference.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x1.png)

Fig. 1: Prosody boundary

Chinese utterance can be analysed in a hierarchical structure shown in Figure 1, which is defined according to the pause duration among phrases of a sentence. This can be manually labelled by human annotators, which is also open-sourced in some Chinese corpus. Four levels of prosody boundaries can also be seen a type of classification problem that different levels of boundaries can be predicted by the prosody boundary prediction model, which is a hot topic recently in the field of Chinese text-to-speech\[22, 23\]. Graph neural network can make use of the graph structure of prosody boundaries to hierarchically structure prosodic information. Potential models of the graph encoder in the task of text-to-speech can be graph convolutional network (GCN), gated graph neural network (GGNN), graph long-short term network (GLSTM), etc. This paper utilises GNN to model the hierarchical structure of Chinese prosody boundaries for context modelling. The contributions of this paper are:

- •
  Proposes two solutions to construct graph embedding by different levels of hierarchical prosody boundaries;
- •
  Provides two approaches of phonetic sequential modelling, sequential edges and graph sequential encoder;
- •
  Provides an alternative framework for text-to-speech, namely text-to-graph and then graph-to-speech modelling, to incorporate the prosody modelling module into the end-to-end speech synthesis process.

## 2 Related Work

Text-to-speech, a procedure to make talking machines, has been a developing hot topic in recent years because of the development of deep learning methods. Chinese is an ideogram language that each character has no relation with its phoneme, which is different from the phonetic language like English. However, the interrelation among words significantly influences the speaking rhythm of an input utterance.

For the purpose of visualisation of prosody embeddings, \[24\] tries to visualise and interpret these latent expressive variables through clustering plots. However, context features of texts are also essential to prosody modelling. The Recurrent Neural Network (RNN) encoder extracts parts of context information. \[25\] has conducted experiments on investigating the similarity and difference between encoder outputs of the end-to-end system and the context information of the statistical parametric TTS. The experiment results show that the encoder outputs reflect both linguistic and phonetic contexts such as vowel reduction at phoneme level, lexical stress at syllable level, and part-of-speech at word level. Prosodic words are the basic unit of a sentence. The consecutive words of the sentence form a prosodic word. Prosodic phrases are mostly composed of 2 or 3 prosodic words. Intonation phrases are separated by punctuation marks, such as commas, semicolons, etc.

Graph Neural Network (GNN) is an effective solution for modelling complex relationships and interdependency between objects \[26, 27\]. Gated recurrent unit and Long-short term memory models are two effective approaches in the field of sequential modelling methods. The design of the forget gate is the essence of these two model. Similar gates are added in the graph neural network models in GLSTM and GRU. Li et al. The inputs are firstly converted into a graph and then the GNN are utilised to learn the representation from the input graph. The gated graph neural network (GGNN) uses the Gate Recurrent Units (GRU) in the propagation step, which is designed for sequential problems \[28\]. \[29, 30\] proposed Graph Long Short-Term Memory network (G-LSTM) to address the text encoding and semantic object parsing task. They follow the same idea of generalising the existing LSTMs into the graph-structured data in the non-Euclidean domain. The graph-to-sequence models have already been tested in the field of Neural Machine Translation (NMT) and Abstract Mean Representation (AMR) which shows outperforming the sequence-to-sequence models\[31, 32, 33\].

### 2.1 Graph convolutional network

Graph convolutional networks (GCNs) aim to generalize convolutions to graph domain. The methods in this direction are often categorized as spectral approaches and spatial approaches. GCN is a procedure to aggregate information from neighbourhood via a normalized Laplacian matrix. The shared parameters are from feature transformation.

In the task of text-to-speech, since the input features are an undirected graph denotes by $`X`$, the nodes neighbouring to it can be denoted by the adjacency matrix $`A`$. The propagation procedure can be denoted by the equation below.

```math
{f\hspace{0pt}{(X,A)}} = {A\hspace{0pt}R\hspace{0pt}e\hspace{0pt}l\hspace{0pt}u\hspace{0pt}{({A\hspace{0pt}X\hspace{0pt}W^{(0)}})}\hspace{0pt}W^{(1)}}
```

This convolutional process can be regarded as a feature extraction process. In the field of speech synthesis, features are extracted from the input features which is used to be calculated attention matrix with the decoding spectrograms. However, the sequential relationships cannot be reasonably modelled through GCN, which might result in weak performance on long-term sentence.

### 2.2 Graph recurrent network

The GGNN model is designed for problems defined on graphs which require outputting sequences which is quite suitable for the speech synthesis task\[31\]. LSTMs are also used similarly as GRU through the propagation process based on a tree or a graph. Two types of Tree-LSTMs and graph-structured LSTM are proposed to address different tasks. They all follow the same idea of generalizing the existing LSTMs into the graph-structured data but has a specific updating sequence. A sentence-LSTM is also proposed for improving text encoding. It converts text into a graph and utilizes the Graph-LSTM to learn the representation.

## 3 Graph Embedding

The graph embeddings are defined according to a graph structure $`\mathcal{G} = {(\mathcal{V},\mathcal{E})}`$, where $`v \in \mathcal{V}`$, take unique values from $`1,\ldots,|\mathcal{V}|`$, and edges are pairs $`e = {(v,v')}`$. we focus on undirected edges in this paper represented by the directed edge $`v\rightarrow v'`$ and the reverse one $`v'\rightarrow v`$. The node embedding (or node representation or node vector) for node $`v`$ is denoted by $`{\mathbf{h}}_{v} \in {\mathbb{R}}^{D}`$ \[34, 35\].

### 3.1 Prosody boundary modelling

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x2.png)

(a) $`P\hspace{0pt}P\hspace{0pt}H_{1}`$

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x3.png)

(b) $`P\hspace{0pt}P\hspace{0pt}H_{2}`$

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x4.png)

(c) $`P\hspace{0pt}P\hspace{0pt}H_{3}`$

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x5.png)

(d) $`I\hspace{0pt}P\hspace{0pt}H_{2}`$

Fig. 2: Graphical prosodic boundary graph embeddings

The graph embeddings are constructed according to the hierarchical prosody boundary structure, prosodic word (PW), prosodic phrase (PPH), intonation prosodic phrase (IPH) and utterance (utter) denoted by $`\mathcal{L}_{p\hspace{0pt}w},\mathcal{L}_{p\hspace{0pt}p\hspace{0pt}h},\mathcal{L}_{i\hspace{0pt}p\hspace{0pt}h},\mathcal{L}_{u\hspace{0pt}t\hspace{0pt}t\hspace{0pt}e\hspace{0pt}r}`$. There is a containment relationship that shows in the equation below.

```math
\mathcal{L}_{p\hspace{0pt}w} \subseteq \mathcal{L}_{p\hspace{0pt}p\hspace{0pt}h} \subseteq \mathcal{L}_{i\hspace{0pt}p\hspace{0pt}h} \subseteq \mathcal{L}_{u\hspace{0pt}t\hspace{0pt}t\hspace{0pt}e\hspace{0pt}r}
```

The nodes are composed of PWs that $`v = \mathcal{L}_{p\hspace{0pt}w}`$ because the PWs are the minimum units of the prosody boundaries. The relationship of the PWs, PPHs and IPHs is heterogeneous, which makes it difficult to model edges among different level’s nodes. So we model the containment relationship among different levels of prosody boundaries as edges $`e \in \mathcal{E}`$.

```math
v = \mathcal{L}_{p\hspace{0pt}w} \in \mathcal{V}
```

```math
e = \left\{ \mathcal{L}_{p\hspace{0pt}p\hspace{0pt}h},\mathcal{L}_{i\hspace{0pt}p\hspace{0pt}h},\mathcal{L}_{u\hspace{0pt}t\hspace{0pt}t\hspace{0pt}e\hspace{0pt}r} \right\} \in \mathcal{E}
```

The prosody boundaries of the Figure 1 is converted to graph-structured shown in the Figure 2. To be specific, because the second PPH in the Figure 1 composed of the $`5^{t\hspace{0pt}h}`$ and $`6^{t\hspace{0pt}h}`$ PWs, there is an edge connecting nodes $`v_{5}`$ and $`v_{6}`$, denoted by $`e_{56} = {(v_{5},v_{6})}`$ shown in Figure 2(b). Similarly, the graph embeddings of $`P\hspace{0pt}P\hspace{0pt}H_{1}`$ and $`P\hspace{0pt}P\hspace{0pt}H_{3}`$ constructed are shown in Figure 2(a) and Figure 2(c). In Figure 1, the second IPH comprises of $`P\hspace{0pt}P\hspace{0pt}H_{2}`$ and $`P\hspace{0pt}P\hspace{0pt}H_{3}`$. So the $`I\hspace{0pt}P\hspace{0pt}H_{2}`$ can be modelled as in Figure 2(d) that six edges are connected from the PWs of $`P\hspace{0pt}P\hspace{0pt}H_{2}`$ to the PWs of $`P\hspace{0pt}P\hspace{0pt}H_{3}`$. Only one edge remains when pph-edge and iph-edge are duplicate.

### 3.2 Sequential modelling

The sequential relationship among phonemes cannot be ignored because the significant variants of Chinese pronunciation like soft tone, transposed tone is highly related to the words connection scenarios. So it is necessary to add sequential representations into the graph embedding.

Two methods are proposed and experimented. One approach is to solve the problem in the process of making the graph embedding, that sequential edges, $`e = {(v_{i},v_{i + 1})}`$ where $`i = {1,\ldots,n}`$, are added between adjacent nodes for better representation of the timing relationship. This may result in duplicate edges with the prosodic boundaries but this can be interpreted as a second pass of the messages in this scenario that the adjacent nodes may have a strong relationship than the not adjacent ones. An alternative approach is to add an additive encoder, which will be detailly described in Section 4.1.

### 3.3 Algorithm

The algorithm of constructing graph embedding is shown in Algorithm 1. The input is the sentence with prosody boundaries $`S`$ and the set of prosody boundaries $`\mathcal{P} = {\{ P_{1},P_{2}\}}`$. These prosody boundaries can be predicted by the prediction models or annotated manually. The output of the algorithm is graph embedding of the sentence $`\mathcal{G} = {(\mathcal{V},\mathcal{E})}`$, which is an intermediate embedding as the input of the graph-to-sequence TTS model. The notations are shown in the Table1.

1:Sentence with prosody boundaries $`S`$; The set of prosody boundaries $`\mathcal{P} = {\{ P_{1},P_{2}\}}`$

2:Graph Embedding of the sentence $`\mathcal{G} = {(\mathcal{V},\mathcal{E})}`$

3:Initialize $`{{b,{b\hspace{0pt}b},{s\hspace{0pt}s},{p\hspace{0pt}b},\mathcal{V},\mathcal{E}}\leftarrow{\lbrack\rbrack}},{{i\hspace{0pt}d\hspace{0pt}x}\leftarrow 0}`$

4:for each $`s \in S`$ do

5:     $`{c\hspace{0pt}u\hspace{0pt}r}\leftarrow{\lbrack b;s\rbrack}`$

6:     if $`{c\hspace{0pt}u\hspace{0pt}r} \in \mathcal{P}`$ then

7:         $`{i\hspace{0pt}d\hspace{0pt}x}\leftarrow{{i\hspace{0pt}d\hspace{0pt}x} + 1}`$

8:         $`{p\hspace{0pt}b}\leftarrow{\lbrack{p\hspace{0pt}b};{c\hspace{0pt}u\hspace{0pt}r}\rbrack}`$

9:         $`{s\hspace{0pt}s}\leftarrow{\lbrack{s\hspace{0pt}s};{i\hspace{0pt}d\hspace{0pt}x};{c\hspace{0pt}u\hspace{0pt}r}\rbrack}`$

10:         $`\mathcal{V}\leftarrow{\lbrack\mathcal{V};{c\hspace{0pt}u\hspace{0pt}r}\rbrack}`$

11:     end if

12:     $`b\leftarrow s`$

13:end for

14:for each $`n \in {s\hspace{0pt}s}`$ do

15:     if $`n \neq P_{2}`$ then

16:         $`{b\hspace{0pt}b}\leftarrow{\lbrack{b\hspace{0pt}b};n\rbrack}`$

17:     else

18:         $`{n\hspace{0pt}n\hspace{0pt}s}\leftarrow{b\hspace{0pt}b}`$ segmented by $`P_{1}`$

19:         $`{e\hspace{0pt}e}\leftarrow`$the combinations of two random elements in $`n\hspace{0pt}n\hspace{0pt}s`$

20:         $`\mathcal{E}\leftarrow{\lbrack\mathcal{E};{e\hspace{0pt}e}\rbrack}`$

21:         $`{b\hspace{0pt}b}\leftarrow^{\operatorname{\prime\prime}}`$

22:     end if

23:end for

24:$`{r\hspace{0pt}e\hspace{0pt}s\hspace{0pt}u\hspace{0pt}l\hspace{0pt}t}\leftarrow{(\mathcal{V},\mathcal{E})}`$

25:return $`r\hspace{0pt}e\hspace{0pt}s\hspace{0pt}u\hspace{0pt}l\hspace{0pt}t`$

Algorithm 1 Graph Embedding Construction

| Notation                        |     | Meaning                                                  |
| ------------------------------- | --- | -------------------------------------------------------- |
| $`\mathcal{S}`$                 |     | The sentence with prosody boundaries                     |
| $`\mathcal{P}`$                 |     | The set of prosody boundaries                            |
| $`P_{1}`$                       |     | The prosody-word boundary                                |
| $`P_{2}`$                       |     | The phrase-prosody boundary                              |
| $`\mathcal{G}`$                 |     | The graph embedding of the sentence                      |
| $`\mathcal{V}`$                 |     | The vertices of the graph embedding                      |
| $`\mathcal{E}`$                 |     | The edges of the graph embedding                         |
| $`b`$                           |     | The previous character                                   |
| $`s\hspace{0pt}s`$              |     | $`\mathcal{S}`$ with characters replaced by placeholders |
| $`p\hspace{0pt}b`$              |     | The array of prosody boundaries $`\mathcal{S}`$          |
| $`s`$                           |     | The current character in the sentence $`\mathcal{S}`$    |
| $`c\hspace{0pt}u\hspace{0pt}r`$ |     | Current scanning word                                    |
| $`i\hspace{0pt}d\hspace{0pt}x`$ |     | The placeholder of the character                         |
| $`b\hspace{0pt}b`$              |     | The consecutive characters                               |
| $`n`$                           |     | The current character in the $`s\hspace{0pt}s`$          |
| $`n\hspace{0pt}n\hspace{0pt}s`$ |     | The nodes connecting by this $`P_{2}`$                   |
| $`e\hspace{0pt}e`$              |     | The edges connected by $`P_{2}`$                         |

Table 1: Notation of Algorithm 1

## 4 Graph-to-sequence TTS

The graph-to-sequence structure is an alternative approach of sequence-to-sequence models \[36\] in the task of the end-to-end process, which has shown effectiveness in the field of neural machine translation (NMT). In the task of text-to-speech (TTS), graph embedding is the information converted from sequential text to a non-Euclidean space, which requires a graph encoder to compute and pass the messages embedded in nodes and edges of the input graph.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x6.png)

(a) Graph-to-Sequence TTS

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x7.png)

(b) Graph Sequential Encoder

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x8.png)

(c) Graph Neural Network Propagation

Fig. 3: Graph-to-sequence TTS

### 4.1 Model Structure

In the Graph-to-Sequence TTS model, the converted prosody boundary graph embeddings are first consumed by $`N`$ GNN layers to encode the embedding information. The propagation process of the model is shown in Figure 3(c). The number of neurons of the first layer of GNN encoder is the same as the number of nodes of graph embeddings. The nodes embedding are randomly initialised and the information aggregates along the edges connected to it. The propagation process shown in Figure 3(c) is quite similar to the fully-connected neural network. However, the key difference is that the messages will only aggregate among adjacent nodes connected by graph edges.

This propagation process will converge to a fixed point that nodes embedding achieves a steady state. In the task of speech synthesis, 2-3 layers of GNN is enough for text encoding. The Graph neural network (GNN) layer can make use of GGNN or G-LSTM models for this sequential task. The output of this GNN encoder is the value vector $`H_{P\hspace{0pt}B}`$ attending the calculation process of the attentional decoding procedure same as the one used in Tacotron2. Sequential encoding calculated by the Graph Sequential Encoder is optionally concatenated with the encoder outputs $`H_{P\hspace{0pt}B}`$ . Mel-spectrograms are output through the attentional decoder for generating waveforms.

### 4.2 Graph Sequential Encoder

To solve the problem of sequential modelling, an additive encoder, Graph Sequential Encoder, can be added for sequential modelling shown in Figure 3(b). The input of the Graph Sequential Encoder is the phoneme-level graph embeddings. The nodes of the phoneme-level graph embeddings are the phoneme characters of a sentence and the edges are the sequential edges connecting the characters representing the sequential information. These phoneme-level graph embeddings are input into $`N`$ GNN layers for encoding. Similar to the GGNN module in the graph encoder shown in 4.1, the Graph neural network (GNN) layer can make use of GGNN or G-LSTM for the prosody encoding task. The output sequential encoding $`\Theta`$ can be concatenated with the prosody boundary graphical representations $`H_{P\hspace{0pt}B}`$ to attend the calculation process of attentional decoding as the keys and values of the attention mechanism. This may give the decoder more information about phoneme-level and sequential information, which is expected to improve the synthesis performance.

## 5 Experiments

### 5.1 Training setup

The experiments are conducted on the open-source dataset from the Databaker company \[37\]. The dataset contains graphemes, phonemes, prosodic labels and the corresponding audios. The prosodic labels can also be predicted by the prosody boundary prediction models. The total hour of the dataset is about 12 hours with 10000 utterances recorded by a professional Chinese female news anchor. Because of the data sparsity of Chinese characters, the Chinese graphemes $`\Psi`$ are firstly converted to phonetic characters in a compact space denoted by $`\psi`$. The dimensions of $`\psi`$ are significantly smaller than that of $`\Psi`$. The baseline model as the benchmark is Tacotron2. Griffin-Lim \[38\] is selected as the vocoder for the mainly comparative experiment on prosody performance. The frame length and frameshift in the models are 50ms and 12.5ms, and the output acoustic features are 80-dim mel-spectrograms. Batch-size is $`32`$ and Adam optimizer is utilised. The learning rate follows a designed annealing strategy starting from $`{1\hspace{0pt}e} - 3`$ decreasing to $`{1\hspace{0pt}e} - 5`$ after $`5000`$ iterations.

The subjective evaluation metric chosen in this paper is Mean Opinion Score (MOS), scaling from 0 - 5 with stages increased by 0.5. The listening tests are rated by 50 native speakers on 100 randomly chosen test sentences. Each sentence is scored by at least 10 raters. The MOS tests were crowdsourced to the raters through an internal platform similarly to Amazon’s Mechanical Turk.

### 5.2 Experiment Design

#### 5.2.1 Experiment I – Benchmark experiment

Experiment I is designed to show the technical feasibility of using GNN models to solve TTS problems using prosody boundary inputs. Two GNN approaches are selected as the encoder, GGNN and GLSTM respectively. Only PPH edges are modelled in this experiment for simplicity and sequential edges are added for avoiding missing edges in some utterances. The MOS results of the baseline model and GraphPB models as shown in the Table 2.

| Model                 |     | MOS               |
| --------------------- | --- | ----------------- |
| Baseline Tacotron2    |     | $`4.05 \pm 0.12`$ |
| GraphPB GGNN Encoder  |     | $`4.28 \pm 0.22`$ |
| GraphPB GLSTM Encoder |     | $`4.25 \pm 0.26`$ |
| Human Recording       |     | $`4.60 \pm 0.17`$ |

Table 2: Benchmark experiment

From Table 2, it can be seen that the GraphPB GGNN and GLSTM Encoder model achieve competitive performance with the baseline model. The model of GGNN Encoder achieves slightly higher MOS than GLSTM Encoder. However, the robustness of the two GraphPB models performs not that good as the baseline model. This may be due to the huge complexity of the edge information.

The mel-spectrogram figures of the baseline Tacotron and GraphPB GGNN Encoder are shown in Figure 4. It can be seen that the pausing in Tacotron2 is more obvious, which is determined by the space symbols in the input text, whereas the pausing information in the GGNN Encoder model is more smooth among words, which gives a better flow of speaking rhythm. Besides the spectrogram of the end part of the GraphPB model has more energy than that of Tacotron2, which shows better rhythm at the end of the audio.

![Refer to caption](https://ar5iv.labs.arxiv.org/html/2012.02626/assets/x9.png)

Fig. 4: Comparison of Tacotron2 and GraphPB

#### 5.2.2 Experiment II – Sequential modelling

Two approaches for encoding sequential information introduced in Section 3.2 and Section 4.1 are compared in this experiment for the necessity of phoneme-level sequential modelling. The level of prosody boundary edges used in the experiment is PPH.

| Model                    |     | MOS               |
| ------------------------ | --- | ----------------- |
| No Sequential Info       |     | $`3.97 \pm 0.35`$ |
| Sequential Edges         |     | $`4.28 \pm 0.22`$ |
| Graph Sequential Encoder |     | $`4.30 \pm 0.19`$ |

Table 3: Sequential modelling

It can be observed from Table 3 that the injection of sequential information improves the final results of the naturalness. The average MOS of graph embeddings without sequential info is the lowest with the highest variance. This may be due to high probabilities of null edges. The addition of Graph Sequential Encoder achieves the highest MOS and the lowest variance. But the model complexity is relatively high with low convergency efficiency.

#### 5.2.3 Experiment III – Number of level of PBs

Experiment III is designed to fine-tune the number of levels of prosody boundaries to be considered in graph embeddings. The encoder used in this experiment is GGNN Encoder and sequential edges are added. The experiment results are shown in Table 4.

It is shown in Table 4 that the additive IPH information slightly improves the MOS results with a gap of 0.01 and the slight drop of variance. However, the duplicate edges and complex hierarchical structure results in low convergency efficiency.

| Prosody boundary | MOS               | Convergency Steps   |
| ---------------- | ----------------- | ------------------- |
| PPH              | $`4.28 \pm 0.22`$ | $`11\hspace{0pt}k`$ |
| PPH & IPH        | $`4.29 \pm 0.21`$ | $`23\hspace{0pt}k`$ |

Table 4: Number of levels of PBs

#### 5.2.4 Experiment IV – Comparative analysis

To deeply discover the representations of prosody boundary, one utterance is segmented through two different methods shown below.

- •
  U1: $`{\mathcal{V} = {\{ v_{1},v_{2}\}}};{\mathcal{E} = {\{{(v_{1},v_{2})}\}}}`$
- •
  U2: $`{\mathcal{V} = {\{ v_{1},v_{2},v_{3},v_{4},v_{5}\}}};{\mathcal{E} = {\{{(v_{1},v_{2})},{(v_{4},v_{5})}\}}}`$

U1 segments the utterance into two parts according to the comma and period punctuation, so that there are only two nodes $`v_{1},v_{2}`$ representing each part and one edge connecting them, $`(v_{1},v_{2})`$. U2 segments the sentence to 5 parts represented by 5 nodes, $`v_{1},v_{2},v_{3},v_{4},v_{5}`$, and 2 PPHs are added in this version of segmentation represented by 2 edges, $`{(v_{1},v_{2})},{(v_{4},v_{5})}`$.

The level of prosody boundary to make graph embedding is PPH and the GGNN Encoder is used in this experiment. The MOS experiment results are shown in Table 5. The MOS of U2 is higher with better robustness because more reasonable segmentation rules are applied according to the semantic rules of the utterance. The segmentation of U1 is in a low segmentation resolution which results in slightly lower MOS and higher variance. This empirically shows that the embedding of graphical representations of prosody boundary can improve the prosody performance of speech synthesis.

| Utterance |     | MOS               |
| --------- | --- | ----------------- |
| U1        |     | $`4.19 \pm 0.2`$  |
| U2        |     | $`4.25 \pm 0.12`$ |

Table 5: Comparative analysis

## 6 Conclusions

This paper utilises Chinese prosody boundary to form graph embedding, that is consumed by a graph recurrent model for graph encoding. The encoded context features are passed to an attentional decoder for outputting mel-spectrogram frame-by-frame. The experiment results show competitive performance with the state-of-the-art sequence-to-sequence models in the spectrogram generation module. Similar graph construction techniques and graphical modelling approaches can be tested in other languages.

## 7 Acknowledgements

This paper is supported by the National Key Research and Development Program of China under Grant No.2017YFB1401202, No.2018YFB0204400 and No.2018YFB1003500. The corresponding author is Jianzong Wang from Ping An Technology (Shenzhen) Co., Ltd.

## References

- \[1\] Lesley Carmichael, “Modeling prosody: Different approaches,” Journal of the Acoustical Society of America, vol. 112, no. 5, pp. 2443–2443, 2002.
- \[2\] Adèle Aubin, Alessandra Cervone, Oliver Watts, and Simon King, “Improving Speech Synthesis with Discourse Relations,” in Proc. Interspeech 2019, 2019, pp. 4470–4474.
- \[3\] Yuxuan Wang, RJ Skerry-Ryan, Ying Xiao, Daisy Stanton, Joel Shor, Eric Battenberg, Rob Clark, and Rif A Saurous, “Uncovering latent style factors for expressive speech synthesis,” in Advances in Neural Information Processing Systems(NIPS) ML4Audio Workshop, 2017.
- \[4\] RJ Skerry-Ryan, Eric Battenberg, Ying Xiao, Yuxuan Wang, Daisy Stanton, Joel Shor, Ron Weiss, Rob Clark, and Rif A. Saurous, “Towards end-to-end prosody transfer for expressive speech synthesis with tacotron,” in International Conference on Machine Learning(ICML), 2018, pp. 4693–4702.
- \[5\] Yuxuan Wang, Daisy Stanton, Yu Zhang, Rjskerry Ryan, Eric Battenberg, Joel Shor, Ying Xiao, Ye Jia, Fei Ren, and Rif A Saurous, “Style tokens: Unsupervised style modeling, control and transfer in end-to-end speech synthesis,” in Proceedings of the 35th International Conference on Machine Learning (ICML), 2018, pp. 5167–5176.
- \[6\] Daisy Stanton, Yuxuan Wang, and R. J. Skerry-Ryan, “Predicting expressive speaking style from text in end-to-end speech synthesis,” in 2018 IEEE Spoken Language Technology Workshop, SLT 2018, Athens, Greece, December 18-21, 2018. 2018, pp. 595–602, IEEE.
- \[7\] Y. Zhang, S. Pan, L. He, and Z. Ling, “Learning latent representations for style control and transfer in end-to-end speech synthesis,” in ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2019, pp. 6945–6949.
- \[8\] H. Choi, S. Park, J. Park, and M. Hahn, “Multi-speaker emotional acoustic modeling for cnn-based speech synthesis,” in ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2019, pp. 6950–6954.
- \[9\] Younggun Lee and Taesu Kim, “Robust and fine-grained prosody control of end-to-end speech synthesis,” in International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2019, pp. 5911–5915.
- \[10\] Tomoki Koriyama and Takao Kobayashi, “Semi-Supervised Prosody Modeling Using Deep Gaussian Process Latent Variable Model,” in Proc. Interspeech 2019, 2019, pp. 4450–4454.
- \[11\] Yanyao Bian, Changbin Chen, Yongguo Kang, and Zhenglin Pan, “Multi-reference tacotron by intercross training for style disentangling, transfer and control in speech synthesis,” arXiv preprint arXiv:1904.02373, 2019.
- \[12\] Da-Rong Liu, Chi-Yu Yang, Szu-Lin Wu, and Hung-yi Lee, “Improving unsupervised style transfer in end-to-end speech synthesis with end-to-end speech recognition,” in 2018 IEEE Spoken Language Technology Workshop, SLT 2018, Athens, Greece, December 18-21, 2018. 2018, pp. 640–647, IEEE.
- \[13\] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova, “BERT: Pre-training of deep bidirectional transformers for language understanding,” in Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), Minneapolis, Minnesota, June 2019, pp. 4171–4186, Association for Computational Linguistics.
- \[14\] Tomoki Hayashi, Shinji Watanabe, Tomoki Toda, Kazuya Takeda, Shubham Toshniwal, and Karen Livescu, “Pre-Trained Text Embeddings for Enhanced Text-to-Speech Synthesis,” in Proc. Interspeech 2019, 2019, pp. 4430–4434.
- \[15\] Bing Yang, Jiaqi Zhong, and Shan Liu, “Pre-Trained Text Representations for Improving Front-End Text Processing in Mandarin Text-to-Speech Synthesis,” in Proc. Interspeech 2019, 2019, pp. 4480–4484.
- \[16\] Haohan Guo, Frank K. Soong, Lei He, and Lei Xie, “Exploiting Syntactic Features in a Parsed Tree to Improve End-to-End TTS,” in Proc. Interspeech 2019, 2019, pp. 4460–4464.
- \[17\] Aolan Sun, Jianzong Wang, Ning Cheng, Huayi Peng, Zhen Zeng, and Jing Xiao, “Graphtts: Graph-to-sequence modelling in neural text-to-speech,” in 2020 IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP 2020, Barcelona, Spain, May 4-8, 2020. 2020, pp. 6719–6723, IEEE.
- \[18\] Min Chu and Yao Qian, “Locating boundaries for prosodic constituents in unrestricted Mandarin texts,” in International Journal of Computational Linguistics & Chinese Language Processing, Volume 6, Number 1, February 2001: Special Issue on Natural Language Processing Researches in MSRA, Feb. 2001, pp. 61–82.
- \[19\] Yuxuan Wang, R.J. Skerry-Ryan, Daisy Stanton, Yonghui Wu, Ron J. Weiss, Navdeep Jaitly, Zongheng Yang, Ying Xiao, Zhifeng Chen, Samy Bengio, Quoc Le, Yannis Agiomyrgiannakis, Rob Clark, and Rif A. Saurous, “Tacotron: Towards end-to-end speech synthesis,” in Proc. Interspeech 2017, 2017, pp. 4006–4010.
- \[20\] J. Shen, R. Pang, R. J. Weiss, M. Schuster, N. Jaitly, Z. Yang, Z. Chen, Y. Zhang, Y. Wang, R. Skerrv-Ryan, R. A. Saurous, Y. Agiomvrgiannakis, and Y. Wu, “Natural tts synthesis by conditioning wavenet on mel spectrogram predictions,” in International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2018, pp. 4779–4783.
- \[21\] Y. Lu, M. Dong, and Y. Chen, “Implementing prosodic phrasing in chinese end-to-end speech synthesis,” in ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2019, pp. 7050–7054.
- \[22\] C. Lu, P. Zhang, and Y. Yan, “Self-attention based prosodic boundary prediction for chinese speech synthesis,” in ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2019, pp. 7035–7039.
- \[23\] Huashan Pan, Xiulin Li, and Zhiqiang Huang, “A Mandarin Prosodic Boundary Prediction Model Based on Multi-Task Learning,” in Proc. Interspeech 2019, 2019, pp. 4485–4488.
- \[24\] Noé Tits, Fengna Wang, Kevin El Haddad, Vincent Pagel, and Thierry Dutoit, “Visualization and Interpretation of Latent Spaces for Controlling Expressive Speech Synthesis Through Audio Analysis,” in Proc. Interspeech 2019, 2019, pp. 4475–4479.
- \[25\] K. Mametani, T. Kato, and S. Yamamoto, “Investigating context features hidden in end-to-end tts,” in ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2019, pp. 6920–6924.
- \[26\] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu, “A comprehensive survey on graph neural networks,” IEEE Transactions on Neural Networks and Learning Systems, pp. 1–21, 2020.
- \[27\] Linfeng Song, Yue Zhang, Zhiguo Wang, and Daniel Gildea, “A graph-to-sequence model for amr-to-text generation,” in Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics(ACL), 2018, pp. 1616–1626.
- \[28\] Yujia Li, Daniel Tarlow, Marc Brockschmidt, and Richard S Zemel, “Gated graph sequence neural networks.,” 2016.
- \[29\] Yue Zhang, Qi Liu, and Linfeng Song, “Sentence-state lstm for text representation,” in Meeting of the association for computational linguistics (ACL), 2018, vol. 1, pp. 317–327.
- \[30\] Xiaodan Liang, Xiaohui Shen, Jiashi Feng, Liang Lin, and Shuicheng Yan, “Semantic object parsing with graph lstm,” in European conference on computer vision (ECCV), 2016, pp. 125–143.
- \[31\] Daniel Beck, Gholamreza Haffari, and Trevor Cohn, “Graph-to-sequence learning using gated graph neural networks,” in Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL), 2018, pp. 273–283.
- \[32\] Joost Bastings, Ivan Titov, Wilker Aziz, Diego Marcheggiani, and Khalil Simaan, “Graph convolutional encoders for syntax-aware neural machine translation,” in Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing(EMNLP), 2017, pp. 1957–1967.
- \[33\] Lingpeng Kong, Chris Alberti, Daniel Andor, Ivan Bogatyy, and David Weiss, “Dragnn: A transition-based framework for dynamically connected neural networks,” arXiv preprint arXiv:1703.04474, 2017.
- \[34\] Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbuchner, and Gabriele Monfardini, “The graph neural network model,” IEEE Transactions on Neural Networks, vol. 20, no. 1, pp. 61–80, 2008.
- \[35\] Jie Zhou, Ganqu Cui, Zhengyan Zhang, Cheng Yang, Zhiyuan Liu, Lifeng Wang, Changcheng Li, and Maosong Sun, “Graph neural networks: A review of methods and applications,” arXiv preprint arXiv:1812.08434, 2018.
- \[36\] Ilya Sutskever, Oriol Vinyals, and Quoc V. Le, “Sequence to sequence learning with neural networks,” in Advances in Neural Information Processing Systems 27: Annual Conference on Neural Information Processing Systems(nips) 2014, December 8-13 2014, Montreal, Quebec, Canada, Zoubin Ghahramani, Max Welling, Corinna Cortes, Neil D. Lawrence, and Kilian Q. Weinberger, Eds., 2014, pp. 3104–3112.
- \[37\] Databaker (Beijing) Technology Co.,Ltd., “Chinese standard mandarin speech copus,” https://www.data-baker.com/open_source.html, 2020.
- \[38\] D Griffin and Jae Lim, “Signal estimation from modified short-time fourier transform,” IEEE Transactions on Acoustics, Speech, and Signal Processing, vol. 32, no. 2, pp. 236–243, 1984.
