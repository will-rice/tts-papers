# tts-papers

A curated, automatically-updated collection of papers on **text-to-speech synthesis**, neural vocoders, voice conversion, voice cloning, prosody, and related topics — starting from the Tacotron/WaveNet era (2017) and growing every day.

Beyond a reading list, this repo is built to be **browsed by LLMs**. Every paper is mirrored as a markdown file with structured YAML frontmatter and inline citation links that resolve to sibling files in the corpus when the cited work is here, or to arXiv / DOI otherwise. Point an agent at [`papers/README.md`](papers/README.md) and it can crawl the literature graph the same way you would.

## How it works

- Papers are sourced from [arXiv](https://arxiv.org/) and [Hugging Face Papers](https://huggingface.co/papers) via their public APIs.
- Query this corpus over MCP: `https://wrice-papers-mcp.hf.space/tts/mcp` ([server code](https://huggingface.co/spaces/wrice/papers-mcp)).
- A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs **daily at 06:00 UTC** to pull papers submitted in the previous 8 days.
- Results are filtered with a negative-keyword blacklist plus an ML signal check and a positive TTS/speech-generation relevance gate.
- The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Markdown corpus

Each paper is also available as LLM-friendly markdown under `papers/<year>/<arxiv_id>.md`. The conversion pipeline:

- Converts arXiv's HTML rendering (`arxiv.org/html/<id>`, falling back to [ar5iv](https://ar5iv.labs.arxiv.org) for pre-2024 papers) — the article is extracted from the page, figures become absolute-URL images, and equations become GitHub-native ` ```math ` blocks.
- Papers without a usable HTML rendering fall back to LaTeX source (`arxiv.org/e-print/<id>`) via [pandoc](https://pandoc.org), then PDF via [marker](https://github.com/datalab-to/marker).
- Auto-flagged or manually-listed (`papers/.fixme.txt`) low-quality outputs go through a Claude Sonnet remediation pass.
- Citations are rewritten as clickable links — local sibling MD when the cited paper is in this corpus, external arXiv/DOI URLs otherwise.

Browse the corpus at [papers/README.md](papers/README.md). Each paper file has YAML frontmatter with metadata + diagnostics (`source`, `converter`, `llm_remediated`, `citations_resolved`).

## Running locally

You'll need pandoc and Node (for Prettier, which normalizes the generated markdown):

```bash
# macOS
brew install pandoc node

# Ubuntu
sudo apt-get install pandoc nodejs npm
```

Then run `npm ci` to install the pinned Prettier used by the pipeline, CI, and pre-commit.

```bash
# Incremental fetch (last 8 days)
uv run python scripts/fetch_papers.py

# Full historical fetch (everything since 2017-01-01)
uv run python scripts/fetch_papers.py --full
uv run python scripts/convert_papers.py --regenerate-all

# Custom window
uv run python scripts/fetch_papers.py --days 30
```

The fetch script uses only the Python standard library (plus a Prettier pass on the README); the conversion pipeline adds `marker-pdf`, `anthropic`, `pyyaml`, and the `pandoc` system binary (managed via `uv` and your package manager). Both scripts format the markdown they generate with the repo-pinned [Prettier](https://prettier.io/) (`npm ci`), and a [Format workflow](.github/workflows/format.yml) enforces it on every PR.

## Triggering a manual update

Open the **Actions** tab → **Fetch TTS Papers** → **Run workflow**.
Select _full = true_ to back-fill from 2017 and rebuild all paper markdown, or leave it as _false_ for an incremental update.

## Search terms

The following keyword queries are used against arXiv title and abstract fields and Hugging Face Papers search:

`text to speech` · `text-to-speech` · `speech synthesis` · `neural text to speech` · `neural vocoder` · `voice conversion` · `voice cloning` · `speech generation` · `acoustic model speech` · `prosody prediction` · `expressive speech synthesis` · `zero-shot TTS` · `end-to-end speech synthesis` · `diffusion speech synthesis`

## Papers

<!-- PAPERS_TABLE_START -->

_Showing the last 30 days (50 of 3304 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [Qwen-Audio-3.0-TTS: Freely Controllable and Highly Robust Speech Synthesis with Multi-Stage Training Paradigm](https://arxiv.org/abs/2607.23938)

**Bajian Xiang, Cheng Wen, Han Zhao, Hao Wang et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

In this report, we present Qwen-Audio-3.0-TTS, a production-oriented speech synthesis system that jointly advances content consistency, speaker similarity, prosodic naturalness, audio quality, controllability, multilingual coverage, efficiency, and robustness. It combines a 12.5~Hz low-frame-rate speech tokenizer for reduced inference latency with a five-stage progressive training paradigm for coordinated language model (LM) and flow-matching model (FM) optimization. The model provides production-level control through free-style natural-language instructions and fine-grained inline tags, while supporting 16 languages, 20 Chinese dialect regions, one-pass long-form synthesis up to 3 minutes, and robust generation from noisy, reverberant, or unclear reference speech. Across SEED-TTS-Eval, CV3-Eval, instruction-following, long-form, and acoustic-robustness evaluations, Qwen-Audio-3.0-TTS achieves state-of-the-art performance on many reported dimensions or the strongest aggregate results. It also ranks first on the independent Artificial Analysis Text-to-Speech Leaderboard. These results establish Qwen-Audio-3.0-TTS as a strong foundation for production-level speech synthesis.

</details>

#### [Let Me Look at You: Advanced Facial Expression Modeling for Conversational Speech Synthesis](https://arxiv.org/abs/2607.24430)

**Yifan Hu, Shuwei He, Rui Liu, Haizhou Li** · 2026-07-27

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis is a fundamental component of human-computer interaction, aiming to generate contextually appropriate, expressive, and empathetic speech. However, facial expressions encode subtle and rich affective cues that are crucial for empathetic speech interaction, whereas existing approaches often overlook this important modality. In addition, the lack of large-scale natural conversational datasets with both speech and visual modalities also limits the development of visual affect understanding in conversational settings.To address these limitations, we propose FacialTalker, a facial-expression-aware CSS framework built upon a large language model backbone. To efficiently encode facial expressions, we propose AUTokenizer, a single-codebook visual tokenizer that discretizes each frame-level facial expression into a compact token, trained with supervision from combinations of facial Action Units. We further introduce a dual direct preference optimization (DualDPO) strategy, which extends the DPO by jointly imposing preference constraints on both visual and speech token sequences, to enhance the model's understanding of facial expressions and speech semantics in multimodal conversational contexts. Moreover, we construct VSDD-1K, a large-scale multimodal dialogue dataset collected through a fully automated pipeline from real-world Internet conversations, comprising over 1,033 hours of synchronized speaker videos and speech, with more than 85\% of frames containing valid faces. Extensive objective and subjective experiments demonstrate that FacialTalker consistently outperforms strong baselines in facial-expression perception and speech synthesis quality, generating speech that is more natural, expressive, and better aligned with the conversational context. The results also validate the effectiveness of our training strategy and dataset construction pipeline.

</details>

#### [Leveraging Gradient Reversal Loss and Multitask Learning for Datasets-Aware Audio Deepfake Detection](https://arxiv.org/abs/2607.23961)

**Mingrui Liang, Thomas Thebaud, Lukasz Wojciak, Laureano Moro Velazquez et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis and voice conversion, which pose threats to security and privacy, have underscored the need for deepfake detection technology. Although existing detection systems achieve strong performance on individual datasets, they often fail to generalize across diverse datasets. Prior methods for improving generalization, including data augmentation, adversarial training on auxiliary factors such as language or codec types, and Mixture-of-Experts (MoE), are limited by predefined augmentation coverage, difficulties in obtaining auxiliary factors, and substantial model complexity. In this work, we propose a practical dataset-aware framework for deepfake detection. Our method targets heterogeneous datasets for which auxiliary annotations such as language, codec, or spoofing method may not be consistently available. We therefore rely only on dataset identity as a naturally available supervisory signal for multitask (MT) and gradient reversal layer (GRL) training, allowing the model to investigate both dataset-aware multitask supervision and adversarial suppression of dataset-specific information. We conduct experiments following the 2025 Speech DeepFake Arena benchmark protocol, evaluating our model across multiple evaluation datasets and reporting aggregate performance in terms of Equal Error Rate (EER), including Average EER and Pooled EER. Compared with the baseline, MT reduces Average EER by 13.14% relatively, while GRL reduces Pooled EER by 5.32% relatively. These results demonstrate that our method can improve aggregate detection performance across heterogeneous evaluation datasets, offering a practical solution for deploying reliable deepfake detection systems on diverse and unseen real-world data.

</details>

#### [Revisiting Vocos: That Phasiness Business in Time-Frequency Neural Vocoding](https://arxiv.org/abs/2607.24323)

**Ünal Ege Gaznepoğlu, Frank Zalkow, Mohammad Joshaghani, Emanuël A. P. Habets et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

Recently, time-frequency neural vocoders have been approaching the state-of-the-art quality of time-domain neural vocoders. Vocos is a notable example due to its efficiency, but its audio quality lags behind the time-domain vocoders and the reasons remain debated. Thus, in this study, we revisit Vocos from a phase reconstruction perspective. First, we quantify the gap between time-domain and time-frequency domain vocoders using bandlimited mel spectrograms as inputs. Later, via an ablation study, we verify the Vocos architecture is effective for magnitude modeling, but less so for phase. We then adapt the Vocos backbone to predict phase differences, a precursor for phase reconstruction, and identify 1D convolutional layers are hindering their accurate prediction. Our findings indicate that future research needs to focus on inductive biases that allow the architecture to better model the time-frequency structure of speech signals, without sacrificing the support for arbitrary input representations.

</details>

#### [Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers](https://arxiv.org/abs/2607.23811)

**Dongseong Hwang, Prasanth Yadla, Kaan Elgin, Shifas Padinjaru Veettil et al.** · 2026-07-26

<details>
<summary>Abstract</summary>

Siri Expressive Voices synthesize rich, configurable speech in real time and entirely on device, powered by AFM 3 Core Advanced, Apple's most powerful on-device foundation model. This work presents the memory-efficient audio synthesis architecture behind that capability: a detokenizer that converts the semantic audio tokens emitted by the foundation model into high-fidelity audio within the tight compute and memory budget of the Apple Matrix Coprocessor (AMX). We convert semantic audio tokens to a residual vector quantization (RVQ) representation with a three-component design, a streaming encoder, a temporal decoder, and a depth decoder, that systematically decouples temporal and depth processing. A single reusable depth decoder with Diffusion Transformer (DiT)-style stage conditioning generates all RVQ levels autoregressively, replacing the dedicated per-level decoders of prior multi-decoder architectures, while causal sliding window attention with fixed-window key-value caching yields constant memory complexity independent of sequence length. Deployed on the AMX, the detokenizer sustains roughly 10 ms per generation step, about 16x faster than real time, with a peak runtime memory of only 21 MB and 329 MB of on-device assets, enabling continuous streaming synthesis of 20-320 seconds of audio. This constant, small footprint replaces the linear and quadratic memory scaling of conventional transformer- and GAN-based approaches. Ablation studies validate the key architectural components, and audio quality assessment confirms that the architecture maintains synthesis fidelity while achieving efficiency gains over existing methods. Operating at a 1-billion-parameter activation size within AFM 3 Core Advanced, it improves Mean Opinion Score by +0.28 overall (4.15 vs. 3.87) and by +0.42 on conversational speech (4.24 vs. 3.82) over the prior on-device text-to-speech system.

</details>

#### [Singlish, Can or Not? Fine-Tuning and Evaluating Zero-Shot TTS for Singapore English](https://arxiv.org/abs/2607.23027)

**Ivan Kukanov, Zheng Xin Chai** · 2026-07-25

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (ZS-TTS) achieves near-human quality for standard English, but it copies regional accents poorly. Prompted with a short Singlish utterance, state-of-the-art systems reproduce a speaker's timbre while flattening the accent toward generic English. We investigate whether targeted fine-tuning off-the-shelf ZS-TTS can close the gap for Singapore English (Singlish). We fine-tune two cutting-edge ZS-TTS models, Chatterbox and CosyVoice 3, on 50 Singlish speakers from the IMDA National Speech Corpus. Three speech distributions are evaluated: real recordings against off-the-shelf and fine-tuned generation driven by the same Singlish audio prompts. The evaluation covers four dimensions: naturalness, intelligibility, speaker similarity, and accent similarity. We separate adaptation (in-domain speakers seen during fine-tuning) from consistency (held-out speakers) to test whether accent transfer generalises beyond the training data. Fine-tuning raises accent similarity on in-domain and out-of-domain speakers for both Chatterbox and CosyVoice 3. It moves the generated distribution measurably toward real Singlish, with the gain persisting on held-out speakers. To our knowledge, this is the first systematic study of Singlish-accented TTS.

</details>

#### [VisionPulse: A Virtual Reality System Enabling Accessible Discovery and Navigation for Blind and Low Vision Users](https://arxiv.org/abs/2607.21944) · [📄 Read](papers/2026/2607.21944.md)

**Samuel Martin, Pooyan Fazli, Hasti Seifi** · 2026-07-24

<details>
<summary>Abstract</summary>

Free exploration is an important aspect of many engaging virtual reality (VR) experiences, yet remains largely inaccessible to blind and low vision (BLV) users due to its reliance on visual feedback. Existing approaches support BLV navigation through prebuilt menus of environment and audio beacons, but offer limited support for free-form discovery. We present VisionPulse, an accessible VR system that enables BLV users to explore virtual environments through natural head and hand movements, combined with auditory, haptic, and text-to-speech feedback. VisionPulse introduces a discovery-driven approach that allows users to progressively uncover regions and objects, alongside navigation support through waypoint guidance and object localization via responsive audio and orientation-based haptics. A study with 12 BLV participants showed a strong preference for VisionPulse's discovery-based exploration and multimodal feedback, without negatively impacting task performance or perceived workload. Our findings underscore the importance of accessible, free-form VR experiences, and contribute insights for inclusive VR design.

</details>

#### [Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning](https://arxiv.org/abs/2607.22304) · [📄 Read](papers/2026/2607.22304.md)

**Roseline Polle, Owen Parsons, George Fairs, Luis Miguel San Martin Fernandez et al.** · 2026-07-24

<details>
<summary>Abstract</summary>

Synthetic data augmentation in speech is common practice for linguistic tasks like ASR, but has seen far less work for paralinguistic ones, especially clinical tasks where labelled data is expensive and some patient groups are underrepresented. Voice cloning is one such augmentation approach, but is typically evaluated on speech intelligibility (WER) or speaker similarity (SS) rather than on downstream performance, and it remains unclear whether these preserve the paralinguistic signal such tasks depend on. We benchmark eight voice cloning models on five paralinguistic tasks across public and clinical datasets, showing most preserve signal with modest degradation. We then clone English clinical speech into Japanese and find that training on cloned data outperforms raw cross-lingual transfer for depression and anxiety detection on real Japanese speech, suggesting voice cloning is a promising direction for augmenting clinical speech data in low-resource languages.

</details>

#### [Cycles of Discourse, Speech Dysfluency, and Active Inference](https://arxiv.org/abs/2607.22180) · [📄 Read](papers/2026/2607.22180.md)

**Thomas Parr, Birtan Demirel, Youssuf Saleh, Sanjay Manohar** · 2026-07-24

<details>
<summary>Abstract</summary>

Speech is a complex motor and social act. We must not only produce and understand sequences of variable-length words formed of ordered syllables but also speak and listen in turn. This theoretical paper introduces a computational model of speech production and auditory segmentation based upon sequences of discrete phonemes. The purpose of this is to develop a vehicle to test (in silico) hypotheses about the mechanisms that govern loss of speech fluency, something that may happen transiently in people who stutter or progressively in various neurodegenerative conditions. The modelling here appeals to Partially Observable Markov Decision Processes that provide a useful generic formulation for specifying the internal model our brains might use to describe dynamic environments in which they can exert partial control and make partial observations. The core features of the specific model used here are: (1) a reciprocal mapping from words to sequences of varying numbers of phonemes (2) a common subset of states for both speech generation and speech perception. A further novel feature is a social component, in which one must infer who is speaking (self or other). We propose a series of hypotheses about the computational mechanisms that might underwrite speech breakdown. For example, we demonstrate that reducing the precision in the next word introduces pauses and start-of-word repetitions of the sort associated with stuttering. We examine the patterns of behaviour and belief-updating predicted by each of these hypotheses, with implications for both speaking and listening. Finally, we discuss plausible neural substrates for the underlying message passing that might be amenable to interrogation with functional imaging.

</details>

#### [Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs](https://arxiv.org/abs/2607.21042) · [📄 Read](papers/2026/2607.21042.md)

**Muyang Du, Shuang Yu, Junjie Lai** · 2026-07-23

<details>
<summary>Abstract</summary>

Autoregressive text-to-speech models achieve strong naturalness but suffer from slow inference due to sequential token generation, limiting their deployment in production applications that require low latency. IndexTTS-2 is a state-of-the-art autoregressive TTS model consisting of a GPT, a flow-matching Diffusion Transformer, and a vocoder. Despite its high synthesis quality, its inference speed barely reaches real-time without streaming or batching support. We present Faster IndexTTS-2, which accelerates all neural network components of IndexTTS-2 for production deployment on GPUs using NVIDIA TensorRT and TensorRT-LLM. Faster IndexTTS-2 also enables streaming synthesis for latency-sensitive interactive applications, and batched inference across all components to maximize GPU utilization. Experiments on the Seed-TTS benchmark for both English and Chinese demonstrate up to 5.0$\times$ speedup on the autoregressive GPT and 3.6$\times$ end-to-end, with minimal degradation in word error rate, speaker similarity, and naturalness. Our methodology provides a practical reference for efficiently accelerating similar autoregressive speech models on GPUs.

</details>

#### [Designed Vocalizations Dataset: Sound-Designed Human and Animal Voices for Non-human Voice Conversion](https://arxiv.org/abs/2607.20951) · [📄 Read](papers/2026/2607.20951.md)

**Seolhee Lee, Minsu Kang, Yangsun Lee, Woosun Min et al.** · 2026-07-23

<details>
<summary>Abstract</summary>

Advances in AI-based voice conversion have enabled a wide range of media applications, including films, audiobooks, and games. However, most research and public benchmarks still focus on natural human speech, leaving designed vocalizations, such as monster growls and robotic voices, underexplored, partly due to the lack of publicly available resources. To address this gap, we introduce the Designed Vocalizations Dataset, constructed by curating diverse raw vocal sources, including speech and animal vocalizations, and applying professional vocal effects processing to produce corresponding effect modified variants. We further provide a standardized test set with explicit seen/unseen splits over source timbre groups and preset styles to assess generalization under controlled conditions. Finally, we report baseline benchmark results to support reproducible evaluation and future research. The dataset and demo samples are available at https://ncai-official.github.io/speech/publications/designed-vocalizations-dataset/.

</details>

#### [Probing Speaker Identity Sensitivity in Audio Deepfake Detectors](https://arxiv.org/abs/2607.21820) · [📄 Read](papers/2026/2607.21820.md)

**Daniyal Kabir Dar, Arun Ross** · 2026-07-23

<details>
<summary>Abstract</summary>

Audio deepfake detectors are trained to distinguish genuine speech from synthetic speech and often perform well on standard benchmarks. Yet the same detector that achieves less than 1% error on one dataset can see its error rate increase twentyfold when evaluated on a different dataset. We argue that one contributing factor is speaker-identity reliance: standard training corpora correlate speaker identity with the genuine/synthetic label, allowing detectors to partially rely on speaker-related cues rather than synthesis artifacts alone. We propose the Identity Sensitivity Score (ISS), a per-utterance diagnostic that quantifies how much a detector's output changes across different speaker identity contexts. ISS requires no ground-truth labels at inference time and can be computed from the detector score and a pool of reference speaker examples. Across two detectors and two datasets, incorrectly classified utterances have ISS scores 29 to 52 times higher than correctly classified utterances, and ISS alone predicts misclassification with area-under-curve (AUC) up to 0.954. To test whether ISS actually captures identity-sensitive behavior rather than serving only as a proxy for prediction confidence, we apply voice conversion to 500 utterances and measure the resulting detector-score shift. Utterances flagged as identity-sensitive by ISS respond 19 to 30 times more strongly to this manipulation than utterances flagged as stable. These results position ISS as a practical inference-time diagnostic for speaker-dependent failure analysis in audio deepfake detection.

</details>

#### [Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models](https://arxiv.org/abs/2607.19932) · [📄 Read](papers/2026/2607.19932.md)

**Pengchao Feng, Chao-Hong Tan, Qian Chen, Wen Wang et al.** · 2026-07-22

<details>
<summary>Abstract</summary>

Spoken language models (SLMs) enable natural human-computer interaction, but their reasoning ability still lags behind that of text-based large language models, especially on spoken mathematical question answering tasks. One important reason is that SLMs reason over purely verbalized mathematical expressions, which are harder to interpret than symbolic text. However, directly transferring text-based reasoning to SLMs is nontrivial due to architectural constraints and the additional computational requirements. To address this challenge, we propose Efficient Chain-of-Modality Reasoning (ECoM Reasoning), the first framework to introduce compressed reasoning into SLMs. By compressing the textual component so that it jointly serves as speech guidance and reasoning representation, ECoM Reasoning improves reasoning accuracy while using a smaller token budget than the standard Chain-of-Modality (CoM) architecture, which generates intermediate text before speech. To train this capability, we further propose Progressive Compression, a curriculum-based strategy that gradually trains the model from full-form reasoning to compressed reasoning. Experiments on spoken mathematical question answering benchmarks show that ECoM Reasoning improves accuracy by 21% over standard CoM without explicit reasoning, and by 3% over CoM with full reasoning traces while using only 40% of the text tokens, demonstrating that it enhances SLM reasoning while remaining inference-efficient.

</details>

#### [StellarTTS: Sparse Temporal Embedding for Low-Latency and Robust Speech Synthesis](https://arxiv.org/abs/2607.19859) · [📄 Read](papers/2026/2607.19859.md)

**Kaicheng Luo, Xuefei Gong, Yutao Sun, Jinling He et al.** · 2026-07-22

<details>
<summary>Abstract</summary>

The trade-off between robustness, latency, and prosody critically challenges text-to-speech (TTS) systems. Autoregressive models, despite fidelity, are slow and error-prone; non-autoregressive (NAR) alternatives, while fast, often sacrifice prosodic naturalness via rigid alignments. This paper introduces StellarTTS, a novel mobile-optimized NAR TTS framework based on a sparse temporal embedding strategy, enabling granular control of phoneme duration, pronunciation, and prosody. Furthermore, we propose a semantic-aware codec that facilitates efficient single-stage decoding. Conditioned on the sparse temporal embedding, our 83M-parameter lightweight masked generative transformer achieves a real-time factor (RTF) of 0.08. Experiments demonstrate that StellarTTS attains lower latency and stronger robustness compared to state-of-the-art TTS systems, while maintaining competitive performance in audio quality, prosodic naturalness, and speaker similarity.

</details>

#### [ETPDesigner: Multi-Agent Orchestration for Interactive Multimodal Electronic Theater Program](https://arxiv.org/abs/2607.19947) · [📄 Read](papers/2026/2607.19947.md)

**Mengtian Li, Xinru Guo, Xiaoru Lin, Xiao Rong et al.** · 2026-07-22

<details>
<summary>Abstract</summary>

Electronic Theater Programs (ETPs) serve as critical promotional media in the performing arts, comprising a multi-page collection of heterogeneous visual assets such as theatrical posters, performance details, and character portraits. However, existing text-to-image paradigms struggle with such complex design tasks due to their inability to comprehend long-context narratives and maintain visual consistency across multiple distinct pages. To address this, we introduce ETPDesigner, a collaborative Multi-Agent framework that directly synthesizes high-quality ETPs from raw dramatic scripts. Emulating a professional design pipeline, our framework orchestrates specialized agents for semantic script analysis, core poster synthesis, functional background generation, and the stratified composition of character assets. Central to ETPDesigner is a global style anchor mechanism that extracts visual priors from the core poster to enforce strict aesthetic uniformity across all generated components. Furthermore, we elevate the ETP from a static publication to an immersive interactive companion. By integrating portrait animation, customized speech synthesis, and persona-grounded Large Language Models (LLMs), our system enables users to engage in real-time, voice-enabled conversations with the generated virtual characters. To rigorously benchmark this task, we construct ETP-Pro, a domain-specific benchmark of professional theater posters and high-quality character portraits. Extensive evaluations demonstrate our method's superiority in producing semantically faithful, aesthetically consistent, and highly interactive program sets.

</details>

#### [CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses](https://arxiv.org/abs/2607.18629) · [📄 Read](papers/2026/2607.18629.md)

**Sajid Fardin Dipto, Tarikul Islam Tamiti, David Vergano, Luke Baja-Ricketts et al.** · 2026-07-21

<details>
<summary>Abstract</summary>

We propose a chaos-inspired new architecture for EMG-to-Speech (ETS) synthesis called CS-ETS, which combines a Samba-based encoder with two novel chaos-inspired loss functions -- Lyapunov Exponent Regularization (LER) and Multi-Scale Detrended Fluctuation Analysis (MSDFA). LER is designed based on Lyapunov exponents to capture nonlinear fluctuations and sensitivity to initial conditions. MSDFA exploits detrended fluctuation analysis to quantify fractal-like, long-range temporal chaotic correlation. CS-ETS surpasses prior work with a 40.79\% lower parameter count (32M vs 54.1M) and introduces a new Post-Vocoder Alignment approach that improves LSD by 2.1x, STOI by 4.7x, and SI-SDR by 1.25x. CS-ETS reduces computation by 13.33\% while maintaining improved performance. To the best of our knowledge, for the first time, we show how ETS can be supervised by the subtle non-linear chaotic physics with Samba attention to achieve a significantly smaller model with superior performance.

</details>

#### [SSTMark: Robust Training-Free Semantic-Level Speech Watermarking](https://arxiv.org/abs/2607.17592) · [📄 Read](papers/2026/2607.17592.md)

**Kuan-Lin Chu, Jun-Cheng Chen, Chun-Shien Lu** · 2026-07-20

<details>
<summary>Abstract</summary>

As speech generation models become increasingly realistic and widely accessible, concerns about the misuse, attribution, and governance of synthetic speech continue to grow. Watermarking provides a practical way to make synthesized speech traceable and verifiable. Most existing speech watermarking methods embed watermark information into signal-level representations, such as waveforms or spectrograms. Under sufficiently strong distortions, the embedded watermark may be weakened or destroyed, leading to degraded detectability. In this paper, we propose SSTMark, a training-free speech watermarking framework that operates at the semantic level through text watermarking. Unlike conventional signal-level watermarking methods, SSTMark encodes watermark information into the semantic content conveyed by generated speech, and detects the watermark from the recovered linguistic content. Experiments on AudioMarkBench demonstrate that SSTMark exhibits the strongest average robustness. Compared with the state-of-the-art baselines at a fixed false positive rate of 1\%, SSTMark improves the average detection rate by 4.6\% and 16.9\% on signal-processing edits and compression edits, respectively.

</details>

#### [Harness TTS: Towards Context-Aware Expressive Speech Synthesis with Harness Layer](https://arxiv.org/abs/2607.17900) · [📄 Read](papers/2026/2607.17900.md)

**Shengfan Shen, Di Wu, Xingchen Song, Dinghao Zhou et al.** · 2026-07-20

<details>
<summary>Abstract</summary>

Expressive speech synthesis for voice assistants requires flexible style control that adapts to explicit requests and broader interaction context. We propose Harness TTS, a lightweight control layer that wraps around a TTS engine to externalize and govern its expressive behavior. It reformulates style control as closed-set prompt-tool routing: offline, a compact registry of stylistic prompt tools is constructed with structured metadata; online, an LLM planner selects the appropriate tool based on a priority-aware observation schema, and the TTS executor synthesizes speech using the corresponding prompt audio. We evaluate Harness TTS on both routing and synthesis tasks. In routing, Qwen3-4B achieves Top-1 accuracies of 74.3%, 43.0%, and 64.6% on explicit, implicit, and conflict subsets. For synthesis, experiments on CosyVoice3 and VoxCPM2 show that Harness TTS outperforms instruction-only control, achieving higher instruction-following win rates (margins of 23.1-35.6 points on CosyVoice3 and 13.8-20.0 points on VoxCPM2) and improving UTMOSv2 scores by 0.11-0.38. Moreover, the 4B planner delivers its first tool recommendation in under 50 ms in standard mode, introducing negligible latency for real-time interaction. These results demonstrate that equipping TTS engines with a dedicated Harness layer offers a practical, auditable, and context-aware solution for voice assistant expression control.

</details>

#### [Staged Depth-Pruning Distillation of a Flow-Matching Text-to-Speech Teacher: A Compact Hindi Speech Synthesizer](https://arxiv.org/abs/2607.18662) · [📄 Read](papers/2026/2607.18662.md)

**Sivateja Trikutam** · 2026-07-19

<details>
<summary>Abstract</summary>

We present a practical recipe for building a compact Hindi text-to-speech (TTS) model by distilling a large flow-matching teacher (IndicF5, 337M-parameter DiT) under a severe data budget (~17.6 hours). Training a small model from scratch on this much data fails outright. Instead we warm-start the student from the teacher by pruning depth only: keeping the teacher's width, text dimension, attention heads, and mel/text I/O fixed so all non-block tensors copy one-to-one, and retaining an evenly-spaced subset of transformer blocks. We first measure how much depth the teacher tolerates (it remains near-functional at -27% blocks but collapses past -50%), then descend gradually (22 -> 16 -> 12 -> 8 -> 6 blocks), re-fine-tuning after each prune, with each step gated by an objective ASR word-error-rate (WER) check. The resulting students reach WER 0.00 on unseen sentences at 249M and 190M parameters, and remain robust down to 131M; at 102M we observe a clear capacity cliff that we attribute to the data budget rather than the recipe. We also document two train/inference feature- and library-parity failures (mel filterbank and rotary-embedding library versions) that silently degrade audio, and a version-independent fix. The method yields a high-quality Hindi voice that runs in real time on a 6 GB laptop GPU. An independent 50-sentence FLEURS benchmark compares the released 190M student against its teacher and MMS-TTS-hin.

</details>

#### [AuEmoChat: Authentic Emotion Understanding and Rendering for Conversational Speech Synthesis](https://arxiv.org/abs/2607.15755) · [📄 Read](papers/2026/2607.15755.md)

**Zhenqi Jia, Yuan Zhao, Aruukhan, Rui Liu et al.** · 2026-07-17

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis (CSS) aims to synthesize speech with human-like emotional expression and contextual consistency in user-agent interactions. Existing CSS methods struggle to render authentic human emotions due to limited predefined emotion label spaces (e.g., seven emotion categories), while redundant multimodal tokens in multi-turn dialogue history interfere with context understanding. To address these issues, we propose AuEmoChat, a CSS framework for authentic emotion understanding and rendering. First, we develop AuEmoCodec, which learns a discrete authentic emotion token space from large-scale emotional speech via finite scalar quantization, enabling a more authentic emotion representation than limited basic emotion categories. We further propose AuEmoToMe, an authentic-emotion-guided token merging algorithm that merges redundant tokens in multimodal dialogue history while preserving emotion-relevant context. We integrate it into an autoregressive text-speech model to predict the target authentic emotion token and speech tokens. Finally, we propose Authentic Emotion Flow Matching, which renders speech by jointly conditioning on merged dialogue context, target authentic emotion, and acoustic priors. Extensive experiments on the NCSSD-EmCap dataset demonstrate that AuEmoChat outperforms state-of-the-art CSS baselines and generates more expressive and authentic emotional speech.

</details>

#### [AutoSIFT: Automatic Style Sifting for Controllable Speech Generation with Arbitrary Style Infilling](https://arxiv.org/abs/2607.12706) · [📄 Read](papers/2026/2607.12706.md)

**Haowei Lou, Junda Wu, Chengkai Huang, Tong Yu et al.** · 2026-07-14

<details>
<summary>Abstract</summary>

State-of-the-art text-to-speech (TTS) models achieve impressive naturalness and expressiveness, yet fine-grained, disentangled control over speaking styles remains challenging. In professional scenarios such as film dubbing, game voice acting, and video content generation, users often need to modify a specific style category, such as emotion, age, or gender, while preserving all others. Existing style-controllable TTS methods typically rely on either text-described styles or speech-reference style transfer, making it difficult to jointly control explicit semantic attributes and preserve subtle, text-undescribed prosodic details. We propose AutoSIFT, a controllable speech generation framework for category-level style editing. AutoSIFT decomposes speaking style into known text-describable categories and unknown residual styles that capture non-verbal prosody and speaker-specific nuances. It consists of a generalized Style Disentangler, which extracts category-aware style prototypes from reference speech, and an Arbitrary Style Infiller, which selectively infills unspecified style categories from the reference. By replacing only text-specified style categories while preserving residual speech-derived styles, AutoSIFT enables natural, expressive, and highly customizable speech generation.

</details>

#### [A Semi-Automated System for Generating Dialogue-Based TTS Lessons Using Large Language Models: An Exploratory Study of Educational Potential](https://arxiv.org/abs/2607.12235) · [📄 Read](papers/2026/2607.12235.md)

**Gendo Kumoi, Fumie Watanabe, Tota Suko, Takashi Ishida et al.** · 2026-07-14

<details>
<summary>Abstract</summary>

This study proposes a semi-automated system for generating dialogue-based lessons using Large Language Models (LLMs) and Text-to-Speech (TTS) technology, and exploratorily examines its educational potential via a practical quasi-experiment. The system augments rather than replaces educators through a three-stage human-in-the-loop workflow (LLM-based slide/narration generation, educator review, automated audiovisual integration), and introduces a novel method for generating Expert-Novice dialogue narration based on cognitive apprenticeship theory. In a study of 245 first-year high school students who sequentially experienced three lesson formats (instructor voice, single-speaker TTS, dialogue TTS; content differed across sessions, limiting format/content separation), we conducted within-subject (Friedman test, N<=183) and repeated cross-sectional (Mann-Whitney U, N=229/206) analyses. TTS audio did not substantially degrade the learning experience versus instructor voice, supported by TOST equivalence testing. Dialogue TTS was significantly superior to single TTS in comprehension (p=.006, q=.025) and cognitive engagement (p=.019, q=.048); enjoyment was non-significant after FDR correction (q=.081) but reached significance after controlling for prior knowledge (proportional-odds model, OR=1.65, q=.025), and these advantages were not attributable to prior-knowledge imbalance. Conversely, single TTS was superior in audio naturalness (p<.001, q<.001, r=-.238), revealing a trade-off between dialogue's benefits and higher extraneous cognitive load. Dialogue format was preferred by 66.9% of learners as most enjoyable (p<.001). These results reflect a fixed-order design; replication is needed before generalizing them as effects of lesson format. This study provides a theoretical and empirical basis for the educational acceptability of TTS audio and for TTS lesson-format design.

</details>

#### [Explainable-by-Design Audio Deepfake Detection via Wiener-Hopf Linear Prediction](https://arxiv.org/abs/2607.12584) · [📄 Read](papers/2026/2607.12584.md)

**Mattia Tamiazzo, Simone Milani, Massimo Iuliani, Marco Fontani** · 2026-07-14

<details>
<summary>Abstract</summary>

The rapid advancement of synthetic speech generation methods has made audio deepfake detection a critical challenge in multimedia forensics. While recent approaches achieve high detection accuracy, they typically rely on black-box architectures that offer limited interpretability and high computational complexity. In this paper, we propose an explainable-by-design audio deepfake detection framework based on Wiener-Hopf linear prediction, processed by a lightweight 2D Convolutional Neural Network (CNN). This design enables a direct and transparent connection between classification outcomes and the acoustic properties of the signal. Experimental results on benchmark datasets demonstrate competitive detection performance while maintaining significantly lower computational complexity compared to state-of-the-art solutions. The interpretability analysis using Grad-CAM reveals that the classifier focuses on low-order predictor coefficients and on silence and transitional regions, suggesting that the Wiener-Hopf predictor captures reverberation characteristics and subtle statistical inconsistencies in synthetic speech. Finally, robustness experiments show that fine-tuning effectively recovers detection performance under common post-processing degradations, including additive noise, MP3 compression, and telephone filtering.

</details>

#### [Adapting a Diffusion-Based Music Synthesis Model to Human Voice Conversion](https://arxiv.org/abs/2607.13278) · [📄 Read](papers/2026/2607.13278.md)

**Ben Maman, Frank Zalkow, Hans-Ulrich Berendes, Paolo Sani et al.** · 2026-07-14

<details>
<summary>Abstract</summary>

Recent diffusion-based generative models have achieved strong results in domain-specific audio generation tasks such as speech, singing, and instrumental music synthesis. However, these models are typically specialized and do not generalize well to mixed or intermediate audio types. In this work, we adapt a diffusion-based model originally designed for multi-instrument music synthesis to voice conversion, covering both speech and singing within a unified framework. Specifically, we extend musical note-based conditioning to include phonetic posteriorgrams (PPGs) and pitch contours, and reinterpret timbre conditioning as speaker or singer identity via feature-wise linear modulation. Experiments show that the adapted model matches or surpasses a dedicated voice conversion system in terms of naturalness and performer similarity, while maintaining accurate pitch control across speech and singing. At the same time, we observe limitations in phonetic fidelity and a degradation in vocal quality when incorporating instrumental training data. Furthermore, we demonstrate that off-the-shelf feature extractors provide effective conditioning signals, enabling large-scale self-supervised training without manual annotations. These results highlight the potential of cross-domain model transfer towards unified audio generation systems capable of handling speech, singing, and music. Qualitative samples can be found on our project page: https://benadar293.github.io/voice-conversion

</details>

#### [VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion](https://arxiv.org/abs/2607.11706) · [📄 Read](papers/2026/2607.11706.md)

**Aastha Sharma, Guangjing Wang** · 2026-07-13

<details>
<summary>Abstract</summary>

Modern LLM-driven text-to-speech (TTS) and voice conversion (VC) systems produce synthetic speech that differs from the generators represented in many legacy spoofing benchmarks. This mismatch creates a temporal generalization gap that can overestimate detector robustness under real-world post-processing conditions. We bridge this gap by introducing VoxENES 2026, a bilingual (English and Spanish) benchmark of 53,628 audio samples generated using 10 contemporary speech synthesis methods and evaluated under 10 standardized post-processing conditions. Using VoxENES 2026, we benchmark eight pretrained detectors without fine-tuning and observe substantial performance degradation: the best model achieves 28.98\% EER overall, while most perform near or below random chance across modern generators and perturbations. Our results highlight the reliance on brittle artifacts in current detectors and establish VoxENES 2026 as a practical testbed for developing robust audio spoofing countermeasures.

</details>

#### [Data Augmentation for L2 English Speaking Assessment using TTS](https://arxiv.org/abs/2607.10790) · [📄 Read](papers/2026/2607.10790.md)

**Stefano Bannò, Penny Karanasou, Mengjie Qian, Kate M. Knill et al.** · 2026-07-12

<details>
<summary>Abstract</summary>

Automated assessment of second language (L2) speaking proficiency relies on large-scale annotated speech data, which remains scarce compared to widely available written learner corpora. A promising direction for addressing this imbalance is to use text-to-speech (TTS) and voice cloning to convert written L2 production into synthetic speech. However, written and spoken L2 differ fundamentally: spontaneous speech includes disfluencies and discourse markers, while writing is more planned and complex. This raises the question of what is required to generate synthetic L2 speech suitable for assessment. We address this through a systematic analysis of speaker-text relationships using COREFL, a publicly available corpus containing paired spoken and written responses from the same L2 learners to the same questions across modalities. In our proposed framework, we first address the structural differences between written and spoken language by transforming written responses into spoken-style transcripts ("speechification") using a large language model. These transcripts are then converted into speech using a TTS/voice-cloning model. To assign a voice to each synthetic response, we investigate different speaker-text pairing strategies based on shared learner attributes (proficiency level, first language, both, or neither). We evaluate our data augmentation techniques on the language assessment task, with improvements shown in both wav2vec2 (audio-based) and ModernBERT (text-based) scoring systems. Results show that matching speakers and texts by proficiency level yields the most robust synthetic speech. Moreover, raw written text leads to a strong mismatch with spoken language, while speechification substantially reduces this gap and improves grading performance.

</details>

#### [FreyaTTS Technical Report](https://arxiv.org/abs/2607.09530) · [📄 Read](papers/2026/2607.09530.md)

**Ahmet Erdem Pamuk, Ömer Yentür, Ahmet Tunga Bayrak, Yavuz Alp Sencer Öztürk et al.** · 2026-07-10

<details>
<summary>Abstract</summary>

We introduce Freya-TTS, a compact, tokenizer-free, Turkish-first text-to-speech model designed for highly reliable and efficient conversational synthesis. Freya-TTS is a 183.2M-parameter non-autoregressive conditional flow-matching Diffusion Transformer (DiT) that operates in the frozen continuous latent space of AudioVAE2 (16 kHz encode, 48 kHz decode), allowing the model to focus its capacity on text-to-latent mapping while inheriting high-quality 48 kHz reconstruction. We advance the framework along three key dimensions: (1) rule-free end-to-end modeling from a 92-symbol Turkish character vocabulary without a phonemizer, grapheme-to-phoneme frontend, or discrete speech tokenizer; (2) non-autoregressive parallel denoising, which predicts the entire latent sequence simultaneously over a predicted duration; and (3) a production-oriented two-stage post-training recipe consisting of single-speaker voice locking and short-utterance coverage, improving speaker consistency and robustness on short inputs. On the Freya-TR-Eval benchmark, Freya-TTS achieves a band-matched word error rate (WER) of 8.0% and character error rate (CER) of 3.0%, outperforming substantially larger open-source systems while using a fraction of their parameters. The model achieves a real-time factor of 0.11 on consumer GPUs and runs faster than real time on a laptop CPU, making it well suited for resource-constrained edge deployment. We release the model weights, training and inference code, and evaluation benchmark under the Apache-2.0 license.

</details>

#### [ReGen: Hierarchical Multi-Prompt Representation Generation for Efficient Waveform Diffusion Models](https://arxiv.org/abs/2607.09134) · [📄 Read](papers/2026/2607.09134.md)

**Sang-Hoon Lee, Ha-Yeong Choi** · 2026-07-10

<details>
<summary>Abstract</summary>

Representation alignment (REPA) has been investigated to accelerate diffusion training, but we observe that regularizing intermediate representations in diffusion Transformers (DiT) may implicitly entangle latents and limit generative capacity. To address this issue, we propose ReGen, a hierarchical multi-prompt representation generation framework that jointly estimates multiple vector fields for both representations and data within a single diffusion model. We further introduce generalized flow matching (GFM) to improve the generalization of conditional flow matching (CFM). We validate ReGen on single-stage waveform diffusion models including neural audio codec and Wave-VAE. ReGen significantly improves waveform generation quality from highly compressed latent representations at 12.5 Hz. We also present ReGenVoice, a latent diffusion model (LDM)-based text-to-speech model that achieves strong speech intelligibility (WER) and speaker similarity (SIM) with a small dataset. Moreover, operating the LDM at 6.25 Hz with rich semantic and acoustic latent representation enables efficient training and sampling, requiring only 1 day of training on 4 GPUs and fast inference with an RTF of 0.08. Audio samples are available at https://regenvoice.github.io/demo/.

</details>

#### [When Synthetic Speech Is All You Have: Better Call GRPO](https://arxiv.org/abs/2607.08409) · [📄 Read](papers/2026/2607.08409.md)

**Shashi Kumar, Yanis Labrak, Hasindri Watawana, Sergio Burdisso et al.** · 2026-07-09

<details>
<summary>Abstract</summary>

LLM-based ASR adapted to regulated domains such as banking is bottlenecked by privacy: real speech is costly and legally constrained to collect, making synthetic text-to-speech (TTS) an attractive substitute. Yet synthetic speech stays acoustically mismatched with real recordings, and work on this gap has stayed within supervised fine-tuning (SFT). We instead turn to reinforcement learning, and show that Group Relative Policy Optimization (GRPO) extracts far more from the same synthetic speech than SFT. Synthetic-only adaptation of the model with GRPO, a critic-free method rewarding low-WER hypotheses, reduces WER by 40\% relative to SFT (36.71\%$\to$22.09\%), and an SFT-then-GRPO combination pushes this further to 45\%. We trace the gain to behavior rather than representation: GRPO reduces insertion errors by improving stopping calibration and speech-to-text alignment by better anchoring attention to audio, leaving early-layer representations intact. When synthetic speech is the main resource, reinforcement learning should be preferred over supervised fine-tuning.

</details>

#### [Diarization-Guided Qwen-ASR Adaptation for Multilingual Two-Speaker Conversational Speech](https://arxiv.org/abs/2607.08208) · [📄 Read](papers/2026/2607.08208.md)

**Hao Wu, RongQi Han, Zhen Wang, Wei Liang et al.** · 2026-07-09

<details>
<summary>Abstract</summary>

This paper describes our self-designed system for Task 1 of the MLC-SLM 2026 Challenge for multilingual two-speaker conversational speech. The system combines a modular speaker diarization front end with a challenge-adapted Qwen3-ASR-1.7B recognizer. The diarization front end performs voice activity detection, subsegment generation, CAMPPlus speaker embedding extraction, two-speaker spectral clustering, and RTTM-based audio segmentation. The resulting speaker-attributed segments are grouped by language or region and decoded by the adapted ASR model. For ASR adaptation, we first perform supervised full fine-tuning on the official training data, then apply LoRA fine-tuning with synthetic speech generated by a three-pipeline TTS-based synthetic speech augmentation framework, and finally refine the model using GRPO reinforcement learning with rewards based on WER/CER and penalties for hallucination, repetition, and length deviation. On the official development set, the full system achieves an average tcpMER of 23.70, reducing the error rate by 6.83 absolute points relative to the released Qwen-ASR-1.7B performance. On the final evaluation set, the system achieves an average tcpMER of 17.97. Ablation results show that supervised fine-tuning provides the largest gain, while synthetic-speech LoRA adaptation and reinforcement learning further improve robustness.

</details>

#### [WordVoice: Explicit and Decoupled Multi-Dimensional Word-Level Control for LLM-Based TTS](https://arxiv.org/abs/2607.06461) · [📄 Read](papers/2026/2607.06461.md)

**Sihang Nie, Jinxin Ji, Xiaofen Xing, Deyi Tuo et al.** · 2026-07-07

<details>
<summary>Abstract</summary>

While recent Large Language Model (LLM)-based Text-to-Speech (TTS) systems have achieved remarkable naturalness, they predominantly rely on implicit end-to-end generation paradigms, resulting in coarse-grained control. In scenarios demanding precise stylistic interventions and strict temporal alignment, such as audiobook narration and video dubbing, the inability to explicitly manipulate word-level acoustic attributes remains a critical bottleneck. This limitation is primarily amplified by the severe scarcity of fine-grained annotated datasets and the architectural challenge of integrating multi-dimensional control signals into discrete autoregressive generation. To address this, we propose a unified framework for highly precise word-level control. First, we construct WordVoice-5A, a massive 4.7k-hour bilingual dataset featuring five-dimensional word-level annotations (duration, boundary, energy, pitch and tone) developed through a rigorous linguistically-guided pipeline. Second, we introduce WordVoice to transform the implicit generation process into an explicit, highly controllable paradigm. Specifically, we introduce a bound-token mechanism within the LLM to formulate an explicit ``acoustic planning'' process, enabling adaptive multi-task prosodic planning and flexible manual intervention. Furthermore, we augment the token-to-waveform stage with a fine-grained acoustic modulation module, bridging the resolution gap to strictly align word-level attributes between highly compressed discrete tokens and continuous waveforms. Extensive experiments demonstrate that WordVoice achieves superior, decoupled control over multiple acoustic dimensions while maintaining competitive zero-shot synthesis stability. The code and audio samples are publicly available at https://xxh333.github.io/wordvoice-demo/.

</details>

#### [Fréchet Distance Loss on Speech Representations for Text-to-Speech Synthesis](https://arxiv.org/abs/2607.06027) · [📄 Read](papers/2026/2607.06027.md)

**Ho-Lam Chung, Kuan-Po Huang, Bo-Ru Lu, Hung-yi Lee** · 2026-07-07

<details>
<summary>Abstract</summary>

Few-step diffusion and flow-matching text-to-speech (TTS) models are usually trained with local objectives, such as conditional flow matching, reconstruction, and stop prediction. These losses provide stable optimization, but they never ask whether sampled speech follows the distribution of high-quality speech. We propose Speech Representation Fr'echet Distance loss (SR-FD), a training-time distributional regularizer for tokenizer-free flow-matching autoregressive TTS. During fine-tuning, the model synthesizes speech with the same few-step sampler used at deployment, and SR-FD matches the mean and covariance of frozen Whisper and CTC features of this speech to reference statistics computed offline from three complementary content targets. The loss requires no discriminator and no inference-time computation. On Seed-TTS English, four-step SR-FD fine-tuning reduces WER from the original four-step VoxCPM2 baseline's 2.2279% to 1.4147%, a 36.5% relative reduction, and also surpasses the original ten-step baseline at 1.7366%; both gains are significant under an utterance-level paired bootstrap. Speaker similarity and objective quality proxies are preserved at the ten-step level, and an error analysis shows the gain comes from content substitutions across all prompt lengths. SR-FD is thus an intelligibility-improving distributional regularizer for few-step TTS.

</details>

#### [Hierarchical Acoustic-Semantic Modeling: Modality Separation and Semantic Coherence for Full-Duplex SLMs](https://arxiv.org/abs/2607.06540) · [📄 Read](papers/2026/2607.06540.md)

**Zhenyu Liu, Yunxin Li, Xuanyu Zhang, Qixun Teng et al.** · 2026-07-07

<details>
<summary>Abstract</summary>

Developing seamless, high-performance, native intelligent full-duplex Spoken Language Models (SLMs) remains a critical challenge and long-standing goal for the speech and NLP community. Despite notable progress, recent endeavors are fundamentally constrained by severe modality interference, which causes substantial knowledge degradation and compromises semantic integrity -- ultimately making full-duplex SLMs feel unnatural and unintelligent. In this paper, through an exhaustive fine-grained analysis of model optimization dynamics, we uncover the root cause of such performance degradation, revealing that modality interference arises from inherent gradient conflicts between acoustic and semantic modeling when the two modalities are forced to share a deep parameter space. Guided by this key insight, we introduce Lychee-FD, a native end-to-end full-duplex framework designed to mitigate modality interference. Importantly, we propose a hierarchical parameter separation strategy that decouples conflicting modalities in deep layers while preserving cross-modality coherence via a dedicated semantic alignment channel. Extensive experiments on multiple full-duplex benchmarks demonstrate that our method significantly advances the state of the art, yielding substantial improvements in both speech intelligence (+7.4% on Spoken QA) and full-duplex interaction fluidity (+28.5% on FullDuplexBench 1.5) without compromising inference efficiency. To the best of our knowledge, this work is the first to achieve two key advances: 1) uncovering and elucidating the root cause of modality interference in full-duplex SLMs, and 2) designing an elegant hierarchical model together with a practical solution for seamless, high-performance, native intelligent full-duplex SLMs.

</details>

#### [ProPS: Prompted Profile Synthesis for Natural Language-Conditioned Speaker Embedding Distributions](https://arxiv.org/abs/2607.05276) · [📄 Read](papers/2026/2607.05276.md)

**Thomas Thebaud, Junhyeok Lee, Laureano Moro-Velazquez, Jesus Villalba Lopez et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

Speaker embeddings, or x-vectors, are widely used to represent speaker identity and speaker-related attributes, but existing embedding extractors are typically descriptive rather than generative: they map an observed speech segment to an x-vector, which is then used for downstream applications. We introduce ProPS, Prompted Profile Synthesis, a framework for generating distributions of speaker embeddings conditioned on natural language prompts such as "a thirties male speaker with an Indian accent". ProPS converts human-written profile descriptions into sentence embeddings and uses a mixture density network trained on a large-scale dataset to predict a Gaussian mixture model in the x-vector space. The model is trained by maximizing the likelihood that real speaker embeddings match the requested profile, and its generated distributions are evaluated by negative log-likelihood on held-out x-vectors and by attribute classification accuracies on sampled synthetic x-vectors. Experiments show that ProPS produces profile-conditioned distributions and generates x-vectors that preserve requested speaker attributes such as age, gender, accent, and prosodic characteristics. This design enables controllable speaker-profile synthesis for speech generation systems like Text-To-Speech (TTS) or Voice Conversion (VC) while anchoring generated distributions in observed speaker-embedding structure.

</details>

#### [Streaming Neural Speech Codecs through Time-Invariant Representations](https://arxiv.org/abs/2607.05250) · [📄 Read](papers/2026/2607.05250.md)

**Kélian Estève, Salima Mhdaffar, Mickael Rouvier, Richard Dufour et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

Neural speech codecs are increasingly used as intermediate representations in codec-based speech generation systems. TiCodec introduces a factorized representation that separates time-varying speech content from time-invariant information through a Time-Invariant Representation Extraction (TIRE) module, potentially reducing the amount of information that must be modeled at the frame-level. In this work, we investigate the nature of the information captured by TIRE representations and their suitability for low-latency speech processing. Using a series of probing tasks, we analyze the influence of the encoder layer and show that intermediate layers capture complementary speaker- and environment-related information while containing little linguistic content. We further study several segment selection strategies for TIRE training and demonstrate that cross-file sampling improves the robustness of invariant representations. Based on these findings, we propose Dual-TIRE, a multi-level architecture that exploits the complementarity of different encoder layers and improves speech reconstruction quality and speaker similarity. Finally, we evaluate TiCodec in a streaming inference setting using successive 660ms processing blocks. Results show that streaming operation can be achieved without significant degradation in reconstruction performance, highlighting the potential of factorized neural codec representations for future low-latency speech generation systems.

</details>

#### [Towards Digital Preservation of Efik: TTS for a Low-Resource African Language](https://arxiv.org/abs/2607.04515) · [📄 Read](papers/2026/2607.04515.md)

**Offiong Bassey Edet, Emmanuel Oyo-Ita, Archibong Okon Archibong, David Effanga Bassey et al.** · 2026-07-05

<details>
<summary>Abstract</summary>

Efik, a tonal language spoken by about 3 million second language speakers and 1.5 million native speakers in Southeastern Nigeria, remains underrepresented in speech synthesis research. We present the first documented end-to-end text-to-speech study for Efik, introducing a curated single speaker corpus of 2,632 utterances totaling three hours and a comparative evaluation of four neural models (VITS, MMS-TTS, SpeechT5, and Orpheus-TTS) under low resource conditions. Native speakers evaluated the systems using MOS, Nat-MOS, and A-MOS. MMS-TTS achieved the highest MOS of 3.80 +/- 0.63 and produced more stable long form speech, though tonal errors persisted. Other models showed greater tonal and prosodic inconsistencies. These results provide a reproducible baseline and highlight the need for larger corpora and tone aware modeling for tonal African languages.

</details>

#### [DELTA-TTS: Adapting Autoregressive Model into Diffusion Language Model for Text-to-Speech](https://arxiv.org/abs/2607.04140) · [📄 Read](papers/2026/2607.04140.md)

**Junwon Moon, Seungbeom Kim, Yejin Lee, Hoseong Ahn et al.** · 2026-07-05

<details>
<summary>Abstract</summary>

Autoregressive (AR) text-to-speech (TTS) models generate discrete speech tokens sequentially, which makes inference slow and can degrade robustness by propagating local errors and hallucinations. This limitation stems from their left-to-right AR commitment: each token must be determined before future speech-token context is available. However, such ordering is not an inherent requirement for TTS, as the full input text is available before synthesis. In this paper, we introduce DELTA-TTS, a lightweight LoRA-based adaptation framework that converts a pretrained AR TTS model into a discrete diffusion language model (dLLM) for confidence-ordered speech-token decoding. To better capture the local structure of speech, DELTA-TTS incorporates a convolution module that injects local acoustic context, together with a $1/t$-weighted training objective and a time-shifted inference schedule that defer low-confidence positions to later steps. Trained on only $585$ hours of LibriTTS, DELTA-TTS achieves a $\textbf{1.75}\%$ WER on Seed-TTS test-en, outperforming its AR backbone while generating tokens $\textbf{3.3}\times$ faster. Further analysis shows that DELTA-TTS produces sharper text--speech alignment, increases overall decoding confidence, and mitigates hallucinations observed in AR generation.

</details>

#### [TRACE-EVC: Text-Guided Relative Affective Control for Zero-Shot Emotional Voice Conversion](https://arxiv.org/abs/2607.03666) · [📄 Read](papers/2026/2607.03666.md)

**Zihan Zhang, Shreeram Suresh Chandra, Zongyang Du, Xiutian Zhao et al.** · 2026-07-04

<details>
<summary>Abstract</summary>

Traditional emotional voice conversion (EVC) conditions generation on explicit target emotions like labels or references, defining the target affective state but omitting the direction or nature of the transition. We introduce instruction-guided relative emotional voice conversion, a task where natural-language instructions specify source-conditioned affective transformations (e.g., "make the speech slightly calmer" or "sound noticeably more confident") instead of fixed targets. To support this task, we construct TRACE-Instruct, a dataset of relative emotion instructions covering categorical transitions, intensity modifications, and open-ended affective changes. We propose TRACE-EVC, a zero-shot framework built around Emo-Compass, a module that models each conversion as a source-anchored rectified flow. Rather than conditioning on an explicit target, it predicts the direction and degree of the affective change. Experiments demonstrate that TRACE-EVC accurately follows relative emotion instructions while preserving speaker identity, linguistic content, and speech quality, and remains competitive with conventional EVC systems on standard categorical emotion conversion.

</details>

#### [VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval](https://arxiv.org/abs/2607.02371) · [📄 Read](papers/2026/2607.02371.md)

**Cristian-Gabriel Florea, Stelian Spînu** · 2026-07-02

<details>
<summary>Abstract</summary>

Over 285 million people worldwide live with a visual impairment, for whom everyday tasks such as avoiding obstacles, locating personal belongings, recognizing familiar faces, or handling cash remain persistent obstacles to personal autonomy. Existing assistive applications are typically limited to recognizing predefined categories, depend heavily on cloud connectivity, or require dedicated hardware. We present VisionAId, an Android application that turns a commodity smartphone into a real-time visual assistant. The system integrates six on-device deep learning models (metric monocular depth estimation, instance segmentation, visual and facial embeddings, face detection, and a custom banknote detector) running entirely through ONNX Runtime, with an optional cloud large language model (Google Gemini Flash) used only for narrative scene description and automatic object labeling. A distinctive contribution is a few-shot pipeline for personal objects: the user photographs an object from several angles, and the system later locates that specific instance in the environment, guiding the user toward it with augmented-reality markers, spatial audio, and distance-proportional haptics. All feedback is multimodal (Romanian speech synthesis, voice commands, vibration). On a reference device (Samsung Galaxy S21 Ultra), INT8 quantization reduces depth latency from ~1200 ms to ~491 ms, the custom banknote detector reaches an mAP@50 of 0.986, and metric depth is calibrated to below 1 cm of error within 3 m.

</details>

#### [LuxSQA: Ask Me in Luxembourgish with TTS-Augmented Spoken Question Answering](https://arxiv.org/abs/2607.02763) · [📄 Read](papers/2026/2607.02763.md)

**Nina Hosseini-Kivanani, Marco Matassoni, Alessio Brutti** · 2026-07-02

<details>
<summary>Abstract</summary>

Spoken Question Answering (SQA) remains largely focused on high-resource languages and carefully recorded speech, limiting the reach of speech-LLM methods in low-resource settings. This paper investigates whether text-to-speech (TTS) can provide task-specific training data for Luxembourgish SQA without requiring a large human-recorded QA corpus. Starting from existing text-based QA resources, we translate questions into Luxembourgish, synthesize spoken questions with multiple TTS systems, and pair them with textual answers. We train a parameter-efficient SLAM-style architecture that connects a frozen Whisper encoder to frozen multilingual LLM backends through a learned projector and LoRA adapters. We compare MMS-TTS, Qwen3-TTS, and OmniVoice variants, including single-source corpora of about 48k questions and a 4TTS multi-source mix of approximately 230k questions. Evaluation on LLAMA-LB-Test with two real Luxembourgish speaker conditions shows that multi-source and voice-design-based synthetic training configurations yield the strongest SQA performance. The results also show that no-reference TTS quality scores do not monotonically predict downstream QA performance, indicating that synthetic speech must be evaluated as task-specific training data rather than only as natural-sounding audio.

</details>

#### [GRAFT: Grafted Reference Audio for Fine-grained Pronunciation in Zero-shot Text-to-Speech](https://arxiv.org/abs/2607.02633) · [📄 Read](papers/2026/2607.02633.md)

**Antonis Asonitis, Francesco Verdini, Aref Farhadipour, Vijeta Avijeet et al.** · 2026-07-02

<details>
<summary>Abstract</summary>

We present GRAFT, a per-word pronunciation conditioning mechanism for text-to-speech neural codec language modeling. Existing systems reach high intelligibility and naturalness but inherit the ambiguity of text and mispronounce rare proper nouns, loanwords and technical terms. Even phoneme-conditioned models offer no direct acoustic handle for per-word pronunciation. GRAFT controls the pronunciation of a chosen word from a short spoken sample of it, encoded with the model's own speech tokenizer and bound to the word's position in the prompt. Voice conversion during training-data construction disentangles the hint speaker from the target speaker, so the hint may come from any voice while the output stays in the target voice. In a blind English listening study, human raters rank GRAFT first by a clear margin, judging its rendering of the difficult word closest to a reference recording of that word. On a five-language objective benchmark, GRAFT reduces target-word phoneme error rate by 22-39% over the identical text-only backbone and outperforms competitive open-source zero-shot systems, both phoneme- and text-conditioned, on target-word pronunciation, while preserving speaker similarity and naturalness.

</details>

#### [A Geometric Perspective on Composable Emotion Steering in Text-to-Speech Models](https://arxiv.org/abs/2607.00946) · [📄 Read](papers/2026/2607.00946.md)

**Siyi Wang, James Bailey, Ting Dang** · 2026-07-01

<details>
<summary>Abstract</summary>

While prior work has explored emotion control in hybrid text-to-speech systems, the geometric properties of these modules, and their implications for steerability, remain poorly understood. We present the first comparative study of speech language model (SLM) and conditional flow-matching (CFM) modules as activation steering sites for mixed emotion speech synthesis. We first characterize emotion representations using linear probing and local intrinsic dimensionality (LID), and then evaluate single-site and joint steering for mixed-emotion synthesis. Our results show that SLM offers a clean, low-dimensional emotion-specific subspace with strong speaker--emotion disentanglement, while CFM exhibitspoor cross-speaker generalization due to speaker--emotion entanglement. Joint steering increases emotion intensity but degrades proportional control and speech quality on in-distribution data. These findings provide practical guidance for multi-site activation steering in hybrid TTS systems and highlight the importance of representation geometry in controllable speech generation.

</details>

#### [Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis](https://arxiv.org/abs/2607.00363) · [📄 Read](papers/2026/2607.00363.md)

**Zuda Yu, Qianhui Xu, Ting Chen, Junhui Zhang et al.** · 2026-07-01

<details>
<summary>Abstract</summary>

Flow Matching (FM) has emerged as a powerful paradigm for speech generation but remains constrained by high inference latency and timbre leakage. To address these bottlenecks, we propose a unified guidance framework that enhances generation efficiency and robustness through two complementary strategies. On the data front, we introduce Data-guidance via heterogeneous augmentation, encouraging the model to disentangle linguistic content from acoustic residue. In parallel, we propose an enhanced Model-guidance mechanism that synergizes trajectory rectification with a novel intrinsic guidance objective. This approach distills conditional knowledge into network weights and straightens inference trajectory path, thereby eliminating Classifier-Free Guidance (CFG) overhead. Experiments demonstrate that our framework accelerates inference by nearly three times while effectively improving speaker similarity compared to state-of-the-art baselines.

</details>

#### [LuxEmo: Expressive Text-to-Speech Corpus for Luxembourgish](https://arxiv.org/abs/2606.31947) · [📄 Read](papers/2026/2606.31947.md)

**Nina Hosseini-Kivanani, Sandipana Dowerah** · 2026-06-30

<details>
<summary>Abstract</summary>

State-of-the-art speech datasets predominantly focus on widely spoken languages, often overlooking low-resource languages such as Luxembourgish, which remain underrepresented in speech technology research. In this work, we introduce LuxEmo, a 21-hour conversational expressive speech corpus for Luxembourgish with 4 emotion categories. LuxEmo is derived from Radio Télévision Luxembourg (RTL) youth broadcasts, using automated detection followed by human validation. We propose a semi-automatic curation workflow combining voice activity detection, denoising, language identification, LuxASR-based segmentation, automatic emotion prediction, lexical cues, and targeted human review. Additionally, we benchmark five expressive TTS systems covering German-based cross-lingual transfer, multilingual Luxembourgish support, Luxembourgish adaptation, and non-parametric prosody transfer. Performance is evaluated using both objective metrics and human evaluation.

</details>

#### [Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation](https://arxiv.org/abs/2606.31729) · [📄 Read](papers/2026/2606.31729.md)

**Dominika Woszczyk, Andreas Triantafyllopoulos, Jura Miniota, Éva Székely et al.** · 2026-06-30

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) evaluation is an open challenge. While the primary target was "naturalness," recent fidelity gains shifted focus toward "appropriateness" and whether speech is correct for its context. In this work, we examine how perception changes when the expected downstream use varies. We measure the appropriateness and human-likeness of five SOTA TTS systems across five domains: AI assistant, reader, actor, animated character, and spontaneous speaker. Results show appropriateness varies across domains independently of naturalness. While systems shine at reading, expressive domains remain challenging, and optimizing for one can degrade others. Furthermore, naturalness scores tend to penalize stylized speech while rewarding spontaneity. Finally, our study also highlights blind spots in one-size-fits-all evaluation metrics across more expressive domains. We demonstrate that TTS performance is not "solved" but depends on the target domain, requiring context-aware evaluation.

</details>

#### [Beyond Cross-Reconstruction: Probing-Based Disentanglement Evaluation for Acoustic Teleportation Codecs](https://arxiv.org/abs/2606.31365) · [📄 Read](papers/2026/2606.31365.md)

**Philipp Grundhuber, Emanuël A. P. Habets** · 2026-06-30

<details>
<summary>Abstract</summary>

Some neural audio codecs disentangle speech into latent subspaces encoding content, speaker identity, and acoustics, enabling acoustic teleportation and voice conversion. Existing evaluations rely on cross-reconstruction quality, which cannot reliably detect leakage across partitions. We extend a probing based framework to assess disentanglement by regressing room-acoustic parameters (reverberation time, clarity, and direct-to-reverberant ratio) and classifying speaker identity, using the gap between intended and unintended partitions as the disentanglement measure. Applied to an acoustic teleportation codec, we find speaker identity is largely confined to its partition, while acoustics leak into the speech embeddings due to the training objective. Acoustic embeddings blindly estimate room parameters within 0.02 s of supervised baselines, indicating physically meaningful structure emerges without explicit supervision.

</details>

#### [Preserving Speech-to-Text LLM Capabilities in Speech-to-Speech Generation](https://arxiv.org/abs/2606.30944) · [📄 Read](papers/2026/2606.30944.md)

**Yuxuan Hu, Heng Lu, Ruchao Fan, Yao Qian et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Strong speech-to-text (S2T) LLMs already provide robust speech perception and text reasoning, but adding speech-to-speech (S2S) output is challenging: fine-tuning the backbone can degrade the original S2T performance, while attaching a downstream talker reintroduces a serial text-to-speech bottleneck. We present PRIME-Speech, a frozen-backbone S2S conversion framework that trains only speech-generation modules. PRIME-Speech synchronizes a causal audio post-decoder with intermediate hidden states of the frozen backbone, so codec tokens are generated from the model's evolving reasoning trajectory rather than from completed text chunks. The post-decoder uses mixed hidden-state, text, and audio-history conditioning, and a training-time packing strategy with turn-level audio KV-cache and position reset stabilizes multi-turn spoken interaction without additional multi-turn S2S training data. Multi-token prediction further reduces the effective codec prediction rate and improves first-audio latency without modifying the reasoning path. Across speech translation, spoken QA, speech understanding, and multi-turn dialogue, PRIME-Speech preserves the S2T behavior of the frozen backbone while producing accurate, low-WER spoken responses.

</details>

#### [DialogPII: A multilingual dataset of synthetic dialog transcripts to detect personal information](https://arxiv.org/abs/2606.30312) · [📄 Read](papers/2026/2606.30312.md)

**Roland Roller, Vera Czehmann, Derya Erman, Luke Flanagan et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Conversational data collected in domains such as healthcare or social sciences is a valuable resource for research and automated analysis. However, responsible data sharing requires the detection and removal of personally identifiable and sensitive information to protect individual privacy. To support the development and evaluation of automatic de-identification systems, we present DialogPII, a multilingual dataset of synthetic dialogs and speech-derived transcripts for personal information detection. DialogPII covers eight interaction scenarios (emergency calls, medical anamnesis interviews, therapy sessions, insurance communication, customer support, clinical interviews regarding an AI-supported dashboard, police reports, and group therapy discussions), 19 entity types, and 11 languages (English, Arabic, Finnish, French, German, Hindi, Italian, Polish, Portuguese, Spanish, and Turkish). Dialogs were generated semi-automatically using large language models, manually curated for plausibility and diversity, and localized to country- and city-specific contexts. All dialogs were additionally converted to speech via text-to-speech synthesis, transcribed with Whisper, and annotated through automatic projection and manual correction, yielding aligned written and speech-derived resources across all languages. We further release baseline multilingual named entity recognition models and provide technical validation through inter-annotator agreement analysis, translation quality evaluation, annotation projection assessment, and benchmark experiments with transformer-based sequence labeling models.

</details>

#### [FacePlex: Full-Duplex Joint Speech-Facial Motion Generation for Conversational Avatars](https://arxiv.org/abs/2606.30145) · [📄 Read](papers/2026/2606.30145.md)

**Habin Lim, Jae-Ho Lee, Hah Min Lew, Ji-Su Kang et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Natural face-to-face conversation requires real-time speech generation together with synchronized facial motion. Existing systems only partially address this problem: speech-only full-duplex models can generate speech in real time but do not produce facial motion, while audio-driven facial motion models animate a face from already available audio rather than jointly generating speech and motion online. To bridge this gap, we first formalize full-duplex joint speech-facial motion generation, where speech tokens and facial motion tokens are produced together every step. Building on this formulation, we propose FacePlex, a unified streaming framework with two key components. First, Rolling Flow Matching adapts flow matching to online motion generation by committing new motion frames at each streaming step. Second, Rolling Cross-Attention couples the streaming audio queue with the motion queue, allowing speech and facial motion to condition each other as generation progresses. Through extensive experiments, ablation studies, and a user study, we show that FacePlex enables full-duplex joint speech-facial motion generation under online streaming constraints, while achieving stronger lip-sync quality and motion fidelity than audio-driven facial motion baselines.

</details>

#### [VeRe-Flow: Guiding Flow Matching toward Clean Speech via Velocity Contrastive Regularization and Representation Alignment for Noise-Robust Bandwidth Expansion](https://arxiv.org/abs/2606.29450) · [📄 Read](papers/2026/2606.29450.md)

**Sujin Koo, Sangyoon Kim, Ji Sub Um, Hoirin Kim** · 2026-06-28

<details>
<summary>Abstract</summary>

Noise-robust bandwidth expansion aims to reconstruct high-fidelity wideband speech from noisy low-resolution inputs. While flow matching has shown strong performance in speech generation, accurately recovering clean speech from noisy inputs remains challenging due to the ambiguity of velocity estimation under noise. In this work, we propose VeRe-Flow, a clean-guided flow matching framework that introduces multi-level clean supervision to guide the generative process toward clean speech. At the velocity level, we introduce velocity contrastive regularization, which attracts the predicted velocity toward the clean trajectory while repelling it from noisy trajectories. At the representation level, we incorporate representation alignment that aligns intermediate features with clean self-supervised learning representations. The results demonstrate that the proposed method achieves the lowest LSD and highest DNSMOS OVRL among all baselines, and the highest MOS among generative baselines.

</details>

</details>
<!-- PAPERS_TABLE_END -->
