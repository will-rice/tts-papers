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

_Showing the last 30 days (52 of 3284 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

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

#### [HPRO: Hierarchical Progressive Reward Optimization via Preference Extraction for Emotional Text-to-Speech](https://arxiv.org/abs/2606.28249) · [📄 Read](papers/2026/2606.28249.md)

**Sihang Nie, Xiaofen Xing, Rui Xing, Haoming Li et al.** · 2026-06-26

<details>
<summary>Abstract</summary>

Recently, Large Language Model (LLM)-based Text-to-Speech (TTS) models have achieved remarkable naturalness. However, the standard Supervised Fine-Tuning paradigm often converges to statistically averaged prosody, limiting emotional expressiveness. While preference-driven optimization offers a promising alternative, existing approaches suffer from two structural mismatches: information conflict, where content and emotion in a shared latent space produce conflicting gradients, leading to reward hacking and semantic degradation; and scale gap, where sparse sentence-level rewards struggle to guide dense frame-level generation. To overcome these challenges, we propose HPRO, a hierarchical progressive reward optimization framework. Within HPRO, we introduce the HD-Emo codec as a novel differentiable reward model to resolve the information conflict. It extracts speech into distinct content and style preference tokens, structurally isolating emotional optimization from semantic content. Building upon this structured preference space, HPRO bridges the scale gap by progressively aligning frame-, word- and sentence-level objectives. Experiments demonstrate that HPRO significantly enhances emotional expressiveness, while effectively preserving linguistic intelligibility. The code and audio samples are publicly available at https://xxh333.github.io/hpro-demo/.

</details>

#### [Closing the Quality Gap in Low-Resource Text-to-Speech: LoRA Fine-Tuning of VoxCPM2 for Khmer and Korean](https://arxiv.org/abs/2606.26618) · [📄 Read](papers/2026/2606.26618.md)

**Phannet Pov, Sovandara Chhoun, Hyun Woo Park, Wan-Sup Cho et al.** · 2026-06-25

<details>
<summary>Abstract</summary>

Large pretrained text-to-speech (TTS) models sound almost human for well-resourced languages, but much worse for languages that are rare in their training data. We study this quality gap for Khmer and Korean using VoxCPM2, a 2.4B-parameter, tokenizer-free TTS model that joins a MiniCPM-4 language-model backbone with a flow-matching diffusion decoder. We build one shared, language-tagged corpus of about 26 hours and adapt VoxCPM2 with a single Low-Rank Adaptation (LoRA) adapter, trained on both languages at once and added to both the language model and the decoder. The adapter is zero-initialized, so training starts exactly at the original (zero-shot) model. In native-speaker listening tests, the Khmer Mean Opinion Score (MOS) rises from 3.85 to 4.23 with the best adapter (rank 64), a highly significant gain (paired Wilcoxon test, p<0.001), while training only 0.19 to 3.03 percent of the parameters. The automatic loss and the human ratings, however, disagree on the best rank: validation loss is lowest at rank 128, yet MOS peaks at rank 64. The same adapter brings no gain for Korean, a language the base model already handles well, and at a high rank it even degrades quality. Adaptation therefore helps mainly where the base model is genuinely weak.

</details>

#### [VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation](https://arxiv.org/abs/2606.26534) · [📄 Read](papers/2026/2606.26534.md)

**Tianxin Xie, Chenxing Li, Dong Yu, Li Liu** · 2026-06-25

<details>
<summary>Abstract</summary>

Recently, zero-shot text-to-speech (TTS) has enabled high-fidelity and expressive speech synthesis, but it often fails to imitate unseen speaking styles from uncommon scenarios (e.g., crosstalk, dialects). Moreover, fine-tuning pretrained models requires large, high-quality datasets, limiting rapid personalization. We propose VoiceTTA, a reinforcement learning-based test-time adaptation (TTA) method that improves voice imitation of pretrained zero-shot TTS models. VoiceTTA introduces two style rewards based on coefficient-of-variation differences of F0 and energy, combined with speaker similarity and intelligibility (WER from a pretrained Whisper model), and optimizes learnable prefixes via group relative preference optimization (GRPO) in a flow matching-based model at inference time. Extensive experiments demonstrate substantial improvements on uncommon speech prompts, outperforming state-of-the-art baselines. Audio samples are available at https://voicetta.pages.dev/

</details>

#### [Joint Residual Reweighting for Classifier Free Guidance in Flow-Matching Zero-Shot TTS](https://arxiv.org/abs/2606.25672) · [📄 Read](papers/2026/2606.25672.md)

**Runwu Shi, Yujin Wang, Hongjin Song, Chunxiang Jin** · 2026-06-24

<details>
<summary>Abstract</summary>

Classifier-free guidance (CFG) is widely used in flow-matching-based zero-shot text-to-speech (TTS), where generation is typically controlled by two conditions: the target text and a prompt speech signal. Standard CFG strengthens these conditions jointly, while recent branch-selective guidance methods attempt to enhance text or speaker conditioning separately, often leading to a trade-off between text correctness and speaker similarity. In this paper, we revisit the CFG under independently masked text and speech-prompt conditions, and decompose the guidance field into text, speaker, and joint residuals. We show that conventional speaker-selective guidance entangles the speaker residual with the joint residual, which may disturb text-related generation. Based on this observation, we propose joint residual reweighting, which independently controls the speaker and joint residuals within the standard CFG framework. Experiments on F5-TTS and CosyVoice2 show that the proposed method improves speaker similarity while maintaining competitive text correctness, demonstrating the usefulness of the joint residual for balancing speaker fidelity and text accuracy in zero-shot TTS.

</details>

#### [Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS](https://arxiv.org/abs/2606.25424) · [📄 Read](papers/2026/2606.25424.md)

**Sandipan Dhar, Nirmesh J. Shah, Ashishkumar P. Gudmalwar, Pankaj Wasnik** · 2026-06-24

<details>
<summary>Abstract</summary>

Diffusion-based text-to-speech (TTS) models have achieved significant improvements in speech quality. However, modeling sharp prosodic transitions and rapid pitch variations in expressive speech remains challenging. Existing diffusion-based TTS decoders commonly utilize periodic nonlinearities such as Snake activation function to capture harmonic structures, but this activation funcation provides limited adaptability when modeling abrupt amplitude and frequency variations. In this paper, we investigate the role of oscillatory inductive bias in diffusion-based TTS decoders and introduce an adaptive oscillatory nonlinearity that enables controllable periodic modulation while maintaining signal stability through a linear bypass component. We refer the resulting TTS system as OscillaTTS. Experiments on the LJSpeech and Emotional Speech Dataset show consistent improvements across objective and subjective evaluations, indicating improved modeling of expressive prosodic dynamics.

</details>

#### [CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations](https://arxiv.org/abs/2606.25403) · [📄 Read](papers/2026/2606.25403.md)

**Ram Annamdevula, Ankit Tatawat, Ashishkumar P. Gudmalwar, Nirmesh J. Shah et al.** · 2026-06-24

<details>
<summary>Abstract</summary>

Accent conversion and controllability remain fundamental challenges in cross-lingual text-to-speech (TTS), particularly for low-resource and phonetically diverse Indic languages. While recent large language model (LLM)-based TTS systems exhibit strong cross-lingual generalization, they provide limited explicit control over accent characteristics and intensity. In this paper, we propose CrossAccentTTS, a framework that enables both accent control and conversion while preserving speaker identity. Specifically, we introduce an Accent Intensity Controller (AIC) that injects weighted language embeddings into the accent subspace, allowing smooth interpolation between accents and fine-grained modulation of accent strength at inference time. Experiments on the Indic Multilingual and L2-arctic datasets shows that CrossAccent-TTS achieves precise control of accent intensity, outperforming strong baselines in accent similarity and controllability by maintaining speaker similarity and naturalness.

</details>

#### [Sarashina2.2-TTS: Tackling Kanji Polyphony in Japanese Speech Generation via Data Scaling and Targeted Data Synthesis](https://arxiv.org/abs/2606.25369) · [📄 Read](papers/2026/2606.25369.md)

**Lianbo Liu, Shiao Zhu, Kai Washizaki, Reo Yoneyama et al.** · 2026-06-24

<details>
<summary>Abstract</summary>

While large language model (LLM)-based text-to-speech (TTS) systems have achieved high-quality speech synthesis, most existing systems focus on English and Chinese. Japanese, however, remains under-explored, and its unique linguistic challenges, such as widespread context-dependent kanji polyphony, have yet to be adequately tackled. Here we introduce Sarashina2.2-TTS (https://github.com/sbintuitions/sarashina2.2-tts), a Japanese-centric LLM-TTS system that tackles these challenges through a dual approach: data strategy and evaluation methodology. First, we scale training to approximately 361k hours of speech, incorporating a balanced mix of Japanese and English data. Furthermore, we design a targeted data augmentation pipeline covering all 2,136 Joyo (regular-use) kanji designated by Japan's Agency for Cultural Affairs to efficiently address kanji polyphony disambiguation. Second, we introduce the Joyo Kanji Yomi Benchmark (https://github.com/sbintuitions/JoyoKanji-Yomi-Benchmark), covering all 2,136 Joyo kanji and their 4,378 readings. Alongside this benchmark, we propose Kana-CER, a metric that compares synthesized speech against reference readings in the kana space, eliminating orthographic variations to directly measure pronunciation correctness. Experiments demonstrate that our targeted data augmentation significantly improves reading accuracy. Overall, Sarashina2.2-TTS achieves state-of-the-art kanji-level reading accuracy and matches top baselines on general sentence-level pronunciation, while delivering the highest speaker similarity in zero-shot Japanese speech synthesis. Furthermore, cross-lingual evaluation reveals that Sarashina2.2-TTS is the only system that maintains stable Japanese pronunciation regardless of the prompt language, confirming that our balanced training approach improves cross-lingual robustness.

</details>

#### [CN-NewsTTS Bench: a target-level automatic benchmark for raw-input Chinese news TTS pronunciation](https://arxiv.org/abs/2606.24714) · [📄 Read](papers/2026/2606.24714.md)

**Shijun Luo** · 2026-06-23

<details>
<summary>Abstract</summary>

Chinese news text contains dense written forms such as scores, hyphenated model names, ranges, unit symbols, percentages, English abbreviations, and mixed Chinese-Latin-digit names. These forms are frequent in real listening workflows, and a text-to-speech (TTS) system can preserve the written string while changing the spoken meaning. We introduce CN-NewsTTS Bench v0.1, an open target-level benchmark for evaluating whether Chinese news TTS products pronounce such targets correctly from raw text, without user-side rules, LLM rewriting, SSML hints, or manual edits. The release contains a 200-record development set, an 800-record public test set, 992 public auto-evaluable targets, fixed transcripts from a three-ASR ensemble, an automatic target scorer, and initial results for seven product TTS systems. We additionally report ASR-route diagnostics, ASR-subset ablations, category-level results, confidence intervals, and provider configuration metadata. The best system reaches 0.879 strict accuracy, while several systems remain below 0.60.

</details>

#### [ZONOS2 Technical Report](https://arxiv.org/abs/2606.24320) · [📄 Read](papers/2026/2606.24320.md)

**Gabriel Clark, Sofian Mejjoute, Mohamed Osman, George Close et al.** · 2026-06-23

<details>
<summary>Abstract</summary>

We present ZONOS2 8B, our latest TTS model, which achieves state-of-the-art naturalness, prosody, and voice cloning fidelity. We improve upon Zonos-v0.1 across scale, data, and training recipe. We scale the model from 1.6B to 8B total parameters (900M active) with a novel mixture-of-experts (MoE) backbone, improving inference latency and throughput. We expand our training corpus from 200K to over 6M hours using a new data processing pipeline, and we simplify our post-training and conditioning recipes to improve naturalness and voice cloning fidelity. We evaluate ZONOS2 8B on quality, speaker similarity, WER, and ZTTS1-Eval, our novel TTS benchmark, where it performs competitively with state-of-the-art systems while maintaining good streaming latency. We release our model weights and example inference code under an Apache 2.0 license on GitHub and Hugging Face.

</details>

#### [On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models](https://arxiv.org/abs/2606.23285) · [📄 Read](papers/2026/2606.23285.md)

**Shunsuke Kando, Wataru Nakata, Shinnosuke Takamichi, Yusuke Miyao** · 2026-06-22

<details>
<summary>Abstract</summary>

Generative Spoken Language Modeling (GSLM) enables text-free speech modeling by training language models (LMs) using discrete speech representations instead of textual transcription. In this paper, we investigate the performance of GSLM on speech synthesis and continuation using discrete speech representations with varying bitrates. We segment speech representations with fixed widths and train K-means models in multiple cluster sizes, resulting in various bitrate settings. We demonstrate that intelligible and natural speech can be synthesized at lower bitrate settings than the baseline. Furthermore, speech continuation quality remains stable at lower bitrates across multiple metrics, suggesting that the conventional GSLM setting may be redundant for effective speech generation. Although LLM-based metrics show higher correlation with human subjective score than conventional metrics, it remains low, highlighting the need for more stable automatic evaluation methods.

</details>

#### [FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech](https://arxiv.org/abs/2606.23190) · [📄 Read](papers/2026/2606.23190.md)

**Haoxu Wang, Biao Tian, Weiqing Li, Xiang Lv et al.** · 2026-06-22

<details>
<summary>Abstract</summary>

Existing Reinforcement Learning (RL) research for Text-to-Speech (TTS) focuses on large language models (LLMs), leaving Flow-Matching (FM) under-explored. We present FlowTTS-GRPO, an online RL framework for FM-based TTS. By converting ordinary differential equation (ODE) trajectories into stochastic differential equation (SDE) paths, our method enables direct fine-tuning of open-source FM models without auxiliary models. We show that a weighted reward combination converges faster than a probabilistic scheme, and identify three practical optimizations: omitting classifier-free guidance (CFG) during training accelerates convergence; synthesizing hard cases improves robustness; and applying RL to the FM component enhances audio-detail metrics. Experiments on CosyVoice 3.0 and F5-TTS demonstrate objective and subjective preference gains in speaker similarity and perceptual quality, with F5-TTS also improving intelligibility.

</details>

#### [Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS](https://arxiv.org/abs/2606.23176) · [📄 Read](papers/2026/2606.23176.md)

**Seymanur Akti, Alexander Waibel** · 2026-06-22

<details>
<summary>Abstract</summary>

Humans tend to speak louder and clearer in challenging environments, such as noisy conditions or when addressing hearingimpaired listeners, which is called Lombard effect. To simulate this behavior in speech synthesis systems, we introduce a flow-matching based text-to-speech (TTS) model trained with vocal effort and articulation pseudo-labels. The proposed model achieves continuous and disentangled control of vocal effort and articulation, while also enabling word-level emphasis for clarifying specific segments of an utterance. Experimental results show that these control mechanisms effectively improve clarityrelated acoustic features. Furthermore, speech-in-noise experiments demonstrate that our model successfully simulates the intelligibility gains of human clear speech in noisy conditions.

</details>

#### [Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis](https://arxiv.org/abs/2606.22811) · [📄 Read](papers/2026/2606.22811.md)

**Jinchuan Tian, Haoran Wang, Siddhant Arora, Takashi Maekaku et al.** · 2026-06-22

<details>
<summary>Abstract</summary>

Classical TTS systems typically rely on rigid input formats and predefined metadata slots, limiting their ability to fulfill flexible user requirements. This paper introduces Bagpiper-TTS, a universal speech synthesis system that deals with diverse natural language user requests. Given a natural language prompt, Bagpiper-TTS first reasons over the users' intent to derive a rich caption, i.e., a comprehensive textual blueprint encompassing both transcription and nuanced metadata. Subsequently, this caption guides the synthesis of the target speech. Our model inherently supports a broad spectrum of tasks besides classical TTS applications, including multi-talker, intent-to-speech, role-play synthesis, singing voice synthesis, and more. Experimental results demonstrate that Bagpiper-TTS achieves an 1.7% Word Error Rate (WER) on the Seed-TTS-Eval benchmark and match the performance of dedicated models in both LLM-as-a-judge and human subjective evaluations across multiple applications.

</details>

#### [Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study](https://arxiv.org/abs/2606.22009) · [📄 Read](papers/2026/2606.22009.md)

**Tomoki Koriyama** · 2026-06-20

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion is essential for controllable and robust text-to-speech, and large language models (LLMs), with broad linguistic knowledge, offer a promising approach. We benchmarked over 30 LLMs on Japanese G2P, comparing them with conventional morphological analyzers on 3000 manually annotated sentences. We evaluated two prompting strategies: a parse mode, where the LLM performs morphological analysis followed by rule-based kana conversion, and a direct mode, where the LLM directly predicts kana readings. The results show that model size, version, and Japanese-specialized training are key factors, with the best LLMs achieving kana character error rate below 0.52\% vs. the best conventional tool (1.03\%). Parse mode outperforms direct mode for most models, as rule-based post-processing relieves the LLM of handling complex pronunciation rules. We also show that feeding LLM-predicted kana into a kana-input TTS yields better pronunciation than end-to-end TTS.

</details>

#### [ISCSLP 2026 CoT-TTS Challenge: Chain-of-Thought Reasoning for Context-Aware Text-to-Speech](https://arxiv.org/abs/2606.21933) · [📄 Read](papers/2026/2606.21933.md)

**Wei Xue, Junlan Feng, Shilei Zhang, Yue Wang et al.** · 2026-06-20

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) have greatly improved speech naturalness, speaker similarity, and controllability. However, most existing controllable TTS systems still rely on explicit user-provided style prompts, making it difficult to automatically determine how a sentence should be spoken in long and complex conversational scenarios. This proposal introduces the ISCSLP 2026 CoT-TTS Challenge, which aims to evaluate whether a system can infer the intended speaking manner from contextual information and generate speech consistent with both the reasoning output and the surrounding scene. The challenge contains two tracks: text-context-aware CoT-TTS and audio-context-aware CoT-TTS. We construct a large-scale bilingual training set from speech-rich media and provide carefully filtered evaluation data for leaderboard comparison. Each system is required to output both a chain-of-thought reasoning analysis and the generated speech waveform. The official evaluation combines objective metrics, multimodal LLM-based evaluation, and human subjective assessment. To facilitate reproducibility, we provide inference code together with a fine-tuning recipe for a 0.6B Qwen3-based model trained via a three-stage strategy. This challenge is expected to support research on context understanding, chain-of-thought reasoning, and expressive speech generation for applications such as film dubbing, audiobook production, virtual characters, and spoken dialogue agents. Further information about the associated challenge is available at:https://iscslp2026-cot-tts.github.io/challenge-website/

</details>

#### [Streaming T5-based Text-to-Speech Synthesis with Limited Lookahead](https://arxiv.org/abs/2606.21882) · [📄 Read](papers/2026/2606.21882.md)

**Muyang Du, Jason Roche, Junjie Lai** · 2026-06-20

<details>
<summary>Abstract</summary>

Streaming text-to-speech synthesis in cascaded LLM-TTS systems still faces latency challenges as most TTS models require full context before initiating generation. We present S5-TTS, a streaming variant of T5-TTS that enables low-latency, word-by-word incremental speech synthesis through encoder-decoder language modeling and monotonic alignment learning. S5-TTS begins generating speech immediately after receiving the first few words, substantially reducing end-to-end response latency. To maintain quality under limited lookahead, we introduce a lookahead-causal masking mechanism with Conv-based auxiliary attention that preserves intelligibility and speaker similarity, and employ interleaved multi-source distillation to further restore naturalness. Experiments show that S5-TTS achieves comparable quality to full-context T5-TTS, supports zero-shot synthesis with high speaker similarity, and significantly reduces end-to-end latency for practical conversational AI systems.

</details>

#### [AugCodec: A Low-Bitrate Disentangled Neural Speech Codec via Data Augmentation](https://arxiv.org/abs/2606.21893) · [📄 Read](papers/2026/2606.21893.md)

**Dongmei Wang, Xiaohang Sun, Yang Liu, Fanjie Kong et al.** · 2026-06-20

<details>
<summary>Abstract</summary>

We propose AugCodec, a low-bitrate disentangled neural speech codec that leverages data augmentation to decompose speech into three distinct components: semantic, speaker, and prosody tokens. Specifically, we employ tailored augmenta tion strategies to transform speech into distinct variants, each serving as input for extracting tokens that preserve the target attribute while suppressing others. This disentanglement strategy enables substantial reduction in token rate. Further more, we introduce an augmentation loss that aligns semantic encoder outputs between source and voice-converted speech, encouraging speaker-agnostic embeddings while mitigating the acoustic mismatch induced by voice conversion. Experiments on LibriSpeech test-clean demonstrate that AugCodec significantly outperforms state-of-the-art methods in both reconstruction quality and disentanglement, while operating at only 12.5Hz with three token streams.

</details>

#### [ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion](https://arxiv.org/abs/2606.21888) · [📄 Read](papers/2026/2606.21888.md)

**Jeongsoo Choi, Ji-Hoon Kim, Shujie Hu, Joon Son Chung** · 2026-06-20

<details>
<summary>Abstract</summary>

Neural speech codecs efficiently compress speech and have become a foundation for speech generation, but they are typically learned as holistic representations that intertwine linguistic content, speaker identity, and prosody. While this design is effective for zero-shot voice cloning, it hinders downstream tasks that require prosody preservation or transfer, such as voice conversion. To address this, we introduce ProsoCodec, a prosody-oriented speech codec that models prosody as a conditional residual rather than as a disentangled stream. Specifically, by conditioning both the encoder and decoder on text and speaker embeddings as prefix tokens, the discrete bottleneck is encouraged to capture prosodic variation not explained by content and speaker. To further preserve prosody, we use the low-frequency mel band and train the model on paired same-speaker utterances. Experiments on voice conversion show improved prosody preservation and reduced source-timbre leakage.

</details>

#### [An Evaluation Framework for Text-to-Speech Voice Reconstruction](https://arxiv.org/abs/2606.21343) · [📄 Read](papers/2026/2606.21343.md)

**Ariadna Sanchez, Christoph Minixhofer, Korin Richmond, Ondrej Klejch et al.** · 2026-06-19

<details>
<summary>Abstract</summary>

Voice reconstruction using Text-to-Speech (TTS) offers a communication method for people with speech disorders, which aims to retain their speaker identity while improving intelligibility. Previous work generally relies on Mean Opinion Score (MOS) to evaluate naturalness and speaker similarity, but this has limited sensitivity and reliability. We propose an evaluation framework with subjective and objective components. Subjectively, we evaluate perceived intelligibility and speaker identity using Best Worst Scaling (BWS) with situational framing. Objectively, we demonstrate that standard measures fail to predict reconstruction success for highly unintelligible speakers, so we introduce a novel dual-reference distributional measure to assess the trade-off between intelligibility and speaker identity. By evaluating the output of 17 zero-shot TTS systems for 193 speakers, we show that our framework provides a reliable and task-aligned approach for assessing voice reconstruction.

</details>

#### [Backdoor Attacks on Speech Emotion Recognition via TTS-Generated Poisoning](https://arxiv.org/abs/2606.21052) · [📄 Read](papers/2026/2606.21052.md)

**Yongbin Huang, Xihao Xie, Jia Zhang** · 2026-06-19

<details>
<summary>Abstract</summary>

Speech Emotion Recognition (SER) systems increasingly leverage self-supervised acoustic representations, yet their vulnerability to training-time attacks remains largely underexplored. This paper presents the first systematic study of poisoning-based backdoor attacks on SER, with a focus on threats enabled by text-to-speech (TTS) generated audio. We introduce a stealthy, low-energy acoustic trigger that can be embedded imperceptibly into both natural and synthetic speech, enabling scalable and consistent poisoning. Our experiments demonstrate that SER models can be reliably compromised with high attack success rates under low poisoning ratios, while maintaining near-clean performance on benign inputs. We further show that backdoor patterns exhibit strong cross-model transferability and that self-supervised representations are particularly susceptible to learning these triggers. These findings reveal that TTS technology dramatically lowers the barrier to effective backdoor attacks, exposing critical vulnerabilities in modern SER pipelines and motivating the urgent need for dedicated defenses.

</details>

#### [SDP-Codec: A Speaker-Decoupled Speech Codec with Pitch Injection for Low-Bitrate Coding and Zero-Shot Voice Conversion](https://arxiv.org/abs/2606.21157) · [📄 Read](papers/2026/2606.21157.md)

**Hounsu Kim, Juhan Nam** · 2026-06-19

<details>
<summary>Abstract</summary>

Speaker-decoupled speech codecs can reduce bitrate by separating global speaker attributes from local content and prosody, while supporting voice conversion. Existing speaker-decoupled codecs face a trade-off: methods that explicitly suppress speaker leakage often rely on multi-stage or auxiliary training, whereas simpler designs can leave residual speaker information in local tokens. We propose SDP-Codec, a speaker-decoupled, pitch-injected codec trained with a single-stage optimization pipeline. SDP-Codec derives local tokens from continuous pre-quantization features of a pretrained self-supervised encoder and injects normalized F0 via a pitch encoder-decoder with global-conditioned denormalization and soft-label pitch reconstruction objective. Across 16 kHz and 24 kHz settings, SDP-Codec achieves competitive reconstruction and strong zero-shot voice conversion at comparable bitrates, with the lowest speaker-probing accuracy among compared systems, suggesting reduced speaker leakage.

</details>

#### [LambdaMark: Semantic Audio Watermarking for Robustness and Radioactivity](https://arxiv.org/abs/2606.21365) · [📄 Read](papers/2026/2606.21365.md)

**Kexin Li, Xiao Hu, Ilya Grishchenko, David Lie** · 2026-06-19

<details>
<summary>Abstract</summary>

Recent advances in generative audio have made voice cloning increasingly effortless, enabling voice fraud, impersonation, and other forms of unauthorized use. A common attack finetunes a speech generation model on recordings of a target speaker, allowing the model to synthesize speech in that speaker's voice. Audio watermarking offers a promising defense by embedding detectable signals into audio. A practical watermark must satisfy two key properties: robustness and radioactivity. Existing audio watermarking methods typically embed signals into low-level representations, such as waveforms or spectrograms, which makes them vulnerable to signal-level manipulations and limits their transfer to downstream models. We introduce LambdaMark -- the first generic radioactive watermarking scheme. Unlike all previous approaches, LambdaMark achieves generic radioactivity by embedding multi-bit watermark information into semantic audio latent representations. Our watermarks have semantic interpretation and are thus more likely to be learned by a downstream model through finetuning. LambdaMark includes a lightweight watermark encoder to inject multi-bit message-dependent perturbations into semantic audio representations and a decoder to detect watermark presence and recover the embedded bit information. Encoder and decoder are trained using a custom multi-component loss that preserves fidelity of the watermarked audio, increases bit-level recovery rate, and improves robustness against common distortions and adversarial removal attempts. Experiments show that LambdaMark achieves near-perfect robustness under common distortions. LambdaMark is also the only watermark that is robust against all evaluated removal attacks. Furthermore, LambdaMark exhibits general and robust radioactivity and remains robust to distortions and adversarial removal attacks even on the generated outputs of those finetuned models.

</details>

</details>
<!-- PAPERS_TABLE_END -->
