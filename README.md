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

_Showing the last 30 days (53 of 3324 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [Towards Real-world Environment-aware Zero-shot Text-to-speech Synthesis via Disentangled Audio Infilling](https://arxiv.org/abs/2608.03011) · [📄 Read](papers/2026/2608.03011.md)

**Ye-Xin Lu, Xin Wang, Yang Ai, Hui-Peng Du et al.** · 2026-08-04

<details>
<summary>Abstract</summary>

Recent zero-shot text-to-speech (TTS) systems achieve remarkable naturalness and speaker similarity but typically require high-quality speaker prompts and either strip away or entangle the acoustic environment with speaker characteristics, limiting their real-world applicability. We present an extended DAIEN-TTS, an environment-aware zero-shot TTS framework that disentangles and jointly models speech, background noise, and reverberation, enabling independent control over timbre and acoustic environment through separate speaker and environment prompts. Built upon the flow-matching-based F5-TTS, it uses a speech-environment separation module to decompose environmental speech into speech, noise, and reverberation components, which are injected into the Diffusion Transformer for environment-aware generation. Training uses simulated data constructed by mixing clean speech with noise and room impulse responses, together with a cross-speaker conditioning strategy that suppresses speaker information leakage from the environment branch. When real-world data are available, the system can be further fine-tuned to bridge the simulated-to-real domain gap.At inference, a triple classifier-free guidance mechanism enables fine-grained control over speech, noise, and reverberation, and a signal-to-noise-ratio adaptation strategy aligns the synthesized speech with the environment prompt. Experiments on simulated and real-world test sets show that DAIEN-TTS generates environmental personalized speech with high naturalness, strong speaker similarity, and faithful noise and reverberation reproduction, while offering controllability beyond prior environment-aware TTS systems.

</details>

#### [GROW: Group-Relative Advantage-Weighted On-Policy Reinforcement Learning of Autoregressive-Diffusion Text-to-Speech model](https://arxiv.org/abs/2608.03215)

**Guanrou Yang, Tian Tan, Qian Chen, Ziyang Ma et al.** · 2026-08-04

<details>
<summary>Abstract</summary>

Reinforcement learning for flow-matching text-to-speech is complicated by deterministic ODE sampling: trajectory-level policy-gradient methods typically convert the ODE into an SDE and track per-step likelihood ratios, introducing stochastic perturbations and substantial overhead. We propose GROW, a group-relative advantage-weighted on-policy RL method that acts directly on the standard flow-matching objective. For each prompt, GROW samples a group of on-policy utterances, separately standardizes intelligibility and speaker-similarity rewards within the group, and combines them to reweight flow-matching regression. A Wasserstein-2 velocity penalty anchors the updated model to a frozen pretrained reference. A group-mean reward baseline is introduced to convert reward weighting into advantage weighting. For strong pretrained TTS models with concentrated rewards, positive exponential weighting is dominated by reward-agnostic self-imitation, whereas a zero-mean signed advantage preserves effective within-group credit assignment. Instantiated on DiTAR and evaluated on LibriSpeech and Seed-TTS EN/ZH, GROW reduces average WER from 2.016 to 1.558 and raises speaker similarity from 0.676 to 0.715 while keeping UTMOS. With 10-NFE training rollouts and 32-NFE evaluation, GROW retains comparable performance while training 2.9x faster than 32-NFE DiTAR-GRPO. We will open-source complete GROW codes, faithful DiTAR reproduction, and all model checkpoints.

</details>

#### [Towards More Expressive Spoken LLMs: Fine-Grained Intent Benchmarking and Acoustic-Lexical Decoupled Policy Optimization](https://arxiv.org/abs/2608.03054)

**Xiang Lin, Tian-Hao Zhang, Chunfeng Wang, Zhou Pan et al.** · 2026-08-04

<details>
<summary>Abstract</summary>

Spoken emotional dialogue requires a model to understand a user's spoken input and generate a response that is both semantically appropriate and emotionally expressive. This is challenging because communicative intent may be stated explicitly in lexical content or conveyed more implicitly through paralinguistic cues, which can complement or diverge from the words themselves. However, two limitations constrain progress in this area: the scarcity of benchmarks that distinguish these intent expressions, and the lack of reinforcement learning objectives that jointly account for response quality and emotional expression. To address the lack of suitable benchmarks, we introduce ParaIntent, a Chinese benchmark comprising 14 intent categories with balanced explicit and implicit samples, together with a multidimensional evaluation protocol covering intent fulfillment, response quality, and emotional expression. For policy optimization, existing approaches either use a shared objective for text and speech or apply reinforcement learning to only one modality, leaving modality-specific learning signals entangled within policy optimization. Motivated by this, we propose Acoustic-Lexical Decoupled Policy Optimization (ALPO), which computes independent textual and acoustic advantages and routes them to the corresponding text and speech tokens within a unified rollout. Under identical reward functions and training budgets, ALPO improves over standard GRPO on most automatic metrics and achieves the best subjective results among the fine-tuned variants, with particularly clear gains in emotional expressiveness on both the synthetic and human-recorded test sets.

</details>

#### [Embodied Empathy: A Multimodal AR and LLM-Powered System for Self-Attachment Psychotherapy with Self-Initiated Humour](https://arxiv.org/abs/2608.02283) · [📄 Read](papers/2026/2608.02283.md)

**Xinyan Ye, Gwyneth Phang, Anandha Gopalan, Abbas Edalat** · 2026-08-03

<details>
<summary>Abstract</summary>

The growing global demand for mental health support increasingly exceeds the supply of qualified practitioners, creating an urgent need for scalable digital interventions that can deliver meaningful emotional connection. In response, we present a novel multimodal application that operationalises the Self-Initiated Humour Protocol (SIHP) within a Self-Attachment Technique (SAT) framework. Our mobile application integrates customisable 3D childhood avatars, augmented reality, and an LLM-driven virtual therapist capable of automated emotion mirroring. An eight-day user study (N=16) indicates the system's feasibility and improvements in self-reported mood. Results show that personalised avatars and text-to-speech output strengthen emotional bonding and perceived empathy. Although emotion mirroring boosts engagement, its effectiveness depends heavily on classification accuracy and animation intensity. Moreover, findings indicate a shift in user expectations--from reactive chatbots to proactive conversational facilitators. We conclude with design implications for leveraging AI and AR to cultivate embodied empathy in digital mental health tools.

</details>

#### [Domain-Specific Evaluation of Text-to-Speech Systems: A Multi-Metric Benchmarking Study](https://arxiv.org/abs/2608.02235) · [📄 Read](papers/2026/2608.02235.md)

**Ali Jafar, Amal Sarmad, Shifa Yousaf, Maryam Bashir** · 2026-08-03

<details>
<summary>Abstract</summary>

Recent advances in neural text-to-speech (TTS) systems have substantially improved speech naturalness and intelligibility across many languages. However, comprehensive evaluation methodologies that jointly assess perceptual quality, speaker similarity, and acoustic fidelity across diverse speech domains remain limited, particularly for low-resource and underrepresented languages. This paper presents a reproducible, multi-metric benchmarking framework for systematic evaluation of modern TTS systems through domain-specific analysis. The proposed framework integrates complementary subjective and objective evaluation protocols and is demonstrated through a comprehensive case study on a representative low-resource language spanning four speech domains: Formal, Conversational, Literary/Storytelling, and Emotional. Four state-of-the-art TTS systems -- Indic-Parler-TTS, MMS-TTS, Microsoft Edge TTS, and Google Gemini TTS -- are evaluated using MUSHRA listening tests, ABX discrimination tests, speaker similarity scoring with Resemblyzer, and acoustic analyses based on mel-cepstral distortion (MCD) and F0 RMSE over 960 audio pairs. Results reveal substantial variation in TTS performance across speech domains, with emotional speech consistently presenting the greatest synthesis challenge (mean MCD 12.03 dB; mean F0 RMSE 889 cents), while conversational speech achieves the highest overall acoustic fidelity. Beyond the empirical findings, this work provides a reproducible evaluation framework, publicly releasing evaluation scripts, result tables, and executable Colab notebooks to support standardized benchmarking and future research on TTS evaluation for low-resource languages.

</details>

#### [SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zero-Shot Tasks](https://arxiv.org/abs/2608.02023) · [📄 Read](papers/2026/2608.02023.md)

**Yu Zhang, Ruiqi Li, Changhao Pan, Ke Lei et al.** · 2026-08-03

<details>
<summary>Abstract</summary>

Speech and audio generation is often needed in animation dubbing, audio drama, movies, advertising, games, podcasts, and short-video production. In these scenarios, creators may need to design voices without reference recordings, control speaker styles with natural language, support acoustic scenes with environments and audio effects, and later reuse the designed voices. Therefore, it is important to support multi-speaker speech and audio generation for both instruct and zero-shot tasks. The instruct task requires a caption of the environment, speaker styles, and fine-grained content, while the zero-shot task uses reference audio together with the same fine-grained content. We address these tasks from both the data and model sides. First, we propose SwanData-Caption, which cleans raw speech and audio data, adds targeted synthetic coverage, and annotates diverse and accurate multi-level captions. Then, we propose SwanTale, a multi-speaker expressive speech and audio generation model that supports both zero-shot and instruct tasks. We introduce SwanVAE to support high-quality multi-audio-modality generation. Then, we adopt reward-conditioned quality control and Engram conditioning, along with Unified MoE for multi-task and multi-audio-modality modeling. In addition, we use curriculum learning and GRPO post-training to let the model progressively learn and strengthen its capabilities. Experimental results show that SwanTale leads on multiple key zero-shot and instruct metrics, achieves the best expressiveness scores in both tasks, and supports complex instruct generation involving multi-speaker speech and audio. Demos can be found at https://swanaigc.github.io/\#swantale.

</details>

#### [Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces](https://arxiv.org/abs/2608.00998) · [📄 Read](papers/2026/2608.00998.md)

**Wangzixi Zhou, Bagus Tris Atmaja, Sakriani Sakti** · 2026-08-02

<details>
<summary>Abstract</summary>

The rise of conversational AI has increased interest in emotional Text-to-Speech (TTS). Most systems rely on discrete emotion labels, which fail to capture the nuanced nature of human affect. Recent models employ dimensional representations such as Russell's arousal-valence (A-V) model, offering finer control. However, emotional perception varies across individuals and cultures, which may cause mismatches between modeled and perceived emotions. We propose a personalized and culturally adaptive emotional TTS framework that performs interactive optimization of individualized A-V perception spaces using an Interactive Genetic Algorithm. By adapting emotion representations to each listener, the system produces speech with more perceptually aligned emotional expression than models using averaged A-V values. Evaluations with Japanese, Chinese, and Indonesian participants highlight the importance of personalization and cultural adaptation for moving beyond one-size-fits-all emotional TTS.

</details>

#### [JoyAI-Talker: Full-Duplex Speech Interactive Large Model Built for Empathetic Voice Agents](https://arxiv.org/abs/2608.01119) · [📄 Read](papers/2026/2608.01119.md)

**Yinhao Bai, Jinming Chen, Yafeng Chen, Wei Deng et al.** · 2026-08-02

<details>
<summary>Abstract</summary>

We present JoyAI-Talker, a full-duplex speech dialogue system that delivers robust foundation model capabilities while empowering empathetic interaction and voice agent intelligence. JoyAI-Talker adopts a modular Thinker-Talker architecture and further implements a unified speech-text joint training pipeline to mitigate the common "cognitive degradation" bottleneck, thereby largely preserving the model's core textual reasoning, STEM, and logical capabilities while extending them to speech-based interaction. For expressive speech synthesis, the Talker module employs a text-controllable generation paradigm that enables natural-language instructions to flexibly control vocal attributes and localized paralinguistic events, such as laughter and sighs, supporting more expressive and fine-grained speech responses. To enhance conversational empathy, we introduce the Persona-Adaptive Empathetic Response (PAER) framework. PAER employs a hierarchical cognitive pipeline to extract non-verbal speaker cues, such as gender, age, and emotional state, from raw input audio, incorporate them into the Thinker's CoT reasoning, and generate context-adaptive responses that align semantically appropriate text with fine-grained control over utterance-level expressiveness and localized paralinguistic events, including sighs, speaking rate, and volume. We further integrate Joy-Duplex, a state-driven, plug-and-play full-duplex framework that functions as an efficient gating engine for real-time turn control. Extensive evaluations show that JoyAI-Talker achieves highly competitive performance on foundational T2T and S2T benchmarks. In full-duplex evaluation, the system reaches a high response rate of 0.88 under user interruptions while maintaining an extremely low false-trigger rate under background speech, demonstrating its readiness for fluid and natural speech dialogue.

</details>

#### [dots.tts.edit: Precisely Controlled Speech Editing with a Continuous Autoregressive Model](https://arxiv.org/abs/2608.02673) · [📄 Read](papers/2026/2608.02673.md)

**Hankun Wang, Bohan Li, Shi Lian, Xiaoyu Gu et al.** · 2026-08-02

<details>
<summary>Abstract</summary>

Speech editing for content creation requires precise control over both what an edit should do and where it should apply. Free-form natural language provides a flexible interface for expressing edit requests, but its ambiguity may leave the intended operation, parameters, or target region underspecified. We study a precise and explicit interface for speech editing: a transcript-grounded structural edit instruction with XML-style tags explicitly specifies typed operations and localizes them to transcript spans or boundaries. This semantic timeline avoids explicit timestamp alignment and provides an externally inspectable contract for compositional edits. We instantiate the interface in dots.tts.edit, an editor adapted from the continuous autoregressive dots.tts foundation model. Four representative speech-creation controls cover lexical content, affective expression, pitch and speaking-rate delivery, and temporal phrasing through text, emotion, prosody, and pause editing. Task-specific data pipelines construct operation- and scope-controlled pairs while retaining source-derived context outside each target region. We further introduce doteBench, a bilingual evaluation suite that measures precise instruction following, local preservation, and audio quality across the four controls and their composition. Experiments show leading overall instruction following and local preservation across its five editing categories, while audio quality remains comparable to existing open-source systems. Across three Seed-TTS-Eval shards, the model shows negligible differences from the base model in zero-shot TTS recognition error rate and speaker similarity. The code and model will be released soon.

</details>

#### [REIMU: Efficient Heterogeneous Hierarchical Reasoning for SSL-Based Speech Deepfake Detection](https://arxiv.org/abs/2608.00857) · [📄 Read](papers/2026/2608.00857.md)

**Kwok-Ho Ng, Tingting Song, Bingwen Feng, Peiya Li** · 2026-08-01

<details>
<summary>Abstract</summary>

The increasing realism of speech generated by text-to-speech and voice conversion systems poses growing challenges to media integrity and voice authentication. Self-supervised learning (SSL) has substantially advanced speech deepfake detection, where downstream backbones conventionally process SSL representations through a single forward pass. This work investigates the practical effectiveness of recurrent hierarchical reasoning for this task. We term this controlled study REIMU and systematically compare conventional single-pass backbones, weight-shared recurrence, homogeneous HRM, and heterogeneous HRM across four Base-scale SSL frontends. We further examine heterogeneous high- and low-level modules that combine self-attention with linear attention. Experiments on the ASVspoof 2019 and 2021 evaluation sets show that recurrence and hierarchical decomposition do not inherently improve detection, whereas heterogeneous operator assignment provides a more competitive configuration. Notably, the heterogeneous design remains competitive while using 10.8\% fewer downstream parameters than the matched baseline, demonstrating its potential for parameter-efficient speech deepfake detection.

</details>

#### [Experience-Calibrated Contrastive Decoding for Mitigating Hallucinations in LM-Based Text-to-Speech](https://arxiv.org/abs/2608.00722) · [📄 Read](papers/2026/2608.00722.md)

**Chenlin Liu, Minghui Fang, Zhonghao Bi, Zekai Su et al.** · 2026-08-01

<details>
<summary>Abstract</summary>

Language model-based text-to-speech (LM-based TTS) remains vulnerable to speech hallucinations that deviate from the target text. Existing mitigation mainly relies on architectural changes or additional training, while decoding-time control remains underexplored. We present a conditional information view that distinguishes text-derived alignment information from experience information supplied by acoustic context and learned speech regularities. We hypothesize that an important class of hallucinations begins when alignment support is insufficiently reflected in the selected token at a vulnerable transition. Using predictions from the same speech LM with and without text conditions, we propose Experience-Calibrated Contrastive Decoding (ECCD), a training-free method that strengthens alignment support while preserving useful experience information. ECCD preserves the original expert distribution, applies only positive alignment enhancement, and calibrates its strength using set-level experience compatibility. Across four models, ECCD reduces WER/CER by up to 55.6% in all SeedTTS-Eval settings and 24 of 25 multilingual CV3-Eval settings. A listening test yields a CMOS gain of $+0.644$ while retaining strong speaker similarity. Further analysis shows that alignment influence and decision-level gain vary within linguistic units and are lower at first-error boundaries than at matched correct boundaries. Overall, these extensive experiments and analyses identify conditional information control as a promising decoding-time direction for mitigating speech hallucination.

</details>

#### [AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context Spectral Infilling](https://arxiv.org/abs/2608.00572) · [📄 Read](papers/2026/2608.00572.md)

**Junchuan Zhao, Minh Duc Vu, Bowen Zhang, Ye Wang** · 2026-08-01

<details>
<summary>Abstract</summary>

Bandwidth extension (BWE) aims to recover missing high-frequency content from band-limited speech. Existing methods often formulate BWE as a fixed or predefined bandwidth conversion problem, potentially requiring cutoff-specific models or retraining when the input bandwidth changes. This assumption limits their applicability to practical scenarios where speech may arrive with diverse cutoff frequencies. We propose AnyBand, a unified BWE framework that recasts bandwidth extension as in-context spectral infilling. Motivated by prompt-based zero-shot speech generation, AnyBand conditions high-frequency generation on the observed low-frequency spectrum, using the available band as a frequency-domain prompt that conveys content, speaker, prosodic, and spectral-envelope cues. This formulation enables a single model to perform cutoff-conditioned generation over a continuous range of input bandwidths. AnyBand is trained with missing-band conditional flow matching and an Easy-to-Balanced cutoff curriculum over continuously sampled cutoff frequencies. To better exploit the spectral prompt, we introduce a frequency-aware Diffusion Transformer that models cross-frequency interactions and long-range temporal dependencies, followed by a physically motivated multi-view adversarial refinement stage to enhance spectral realism, envelope coherence, and harmonic consistency. Experiments on multiple datasets and bandwidth settings show that AnyBand consistently improves spectral reconstruction over existing baselines while achieving competitive perceptual quality across both standard and irregular input cutoffs. Audio samples are available.

</details>

#### [Beyond Prompt Adherence: Auditing Attribute-Level Voice Control in Speech Generation](https://arxiv.org/abs/2608.00545) · [📄 Read](papers/2026/2608.00545.md)

**Xianhao Zhou, Jianghao Wu** · 2026-08-01

<details>
<summary>Abstract</summary>

Natural-language descriptions have become a flexible interface for controlling generated speech. Existing evaluations largely assess whether an output matches a prompt, but prompt matching alone does not reveal whether characteristics outside the intended change remain stable. We examine this distinction through a controlled paired audit of three speech-generation systems: CosyVoice3, VoxCPM2, and Fish-Speech-S2. The evaluation contains 5,940 outputs spanning six reference speakers, ten texts, three random seeds, and eleven conditions. Using acoustic, prosodic, content, and speaker measurements, we find that responses in the expected target direction are frequently accompanied by changes outside descriptor-specific signal-level target sets. This pattern remains among outputs whose target response exceeds baseline seed variation, and the accompanying changes differ substantially across systems. We further introduce VoDER-Cal, a training-free candidate selector that retains sufficiently strong target responses while favoring smaller off-target deviations. A three-candidate pool raises the joint success rate from 4.8% under single-sample direct generation to approximately 14% for all candidate-selection policies. Within the matched three-candidate budget, VoDER-Cal reduces held-out off-target deviation from 0.344 under target-only selection to 0.276 and improves listener-rated preservation. Preservation-sensitive evaluation therefore complements prompt-adherence evaluation, while candidate reranking offers a practical inference-time improvement. Code, configuration files, and analysis scripts are available at https://github.com/intelland/VoDER

</details>

#### [Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens](https://arxiv.org/abs/2607.29363) · [📄 Read](papers/2026/2607.29363.md)

**Yi Luo, Rongzhi Gu, Jixun Yao** · 2026-07-31

<details>
<summary>Abstract</summary>

Balancing sequence length, representational capacity, and long-horizon stability is a central problem in autoregressive (AR) speech and audio generation. Representations with higher frame rates or greater capacity can preserve more signal detail, but they also make streaming generation more vulnerable to distribution drift and AR error accumulation. Conversely, shorter and more compressed representations simplify AR modeling, but their limited bandwidth may discard important components and constrain the upper bound of reconstruction fidelity and generation quality. We ask whether a low-frame-rate, high-dimensional, high-bandwidth continuous representation can be co-designed with a streaming generation framework to support robust high-fidelity reconstruction, strong single-token predictability, and superior long-horizon stability. We decompose this goal into two coupled problems: what geometric and statistical properties a high-dimensional representation space should have, and how an AR continuous-token generator should be structured to resist error accumulation. Accordingly, we propose Locodec, a locally encoded codec that shapes its representation space to improve the interpolatability of a lower-dimensional core manifold and the identifiability of the native high-dimensional coordinates, thereby improving the predictability of high-dimensional high-bandwidth tokens. We also propose MP-ELD, a single-token AR flow-matching framework that uses multi-path information routing and residual classifier-free guidance to mitigate error accumulation. Experiments with 8-Hz, 768-dimensional tokens show that our design preserves reconstruction quality, improves single-token predictability, achieves competitive WER, and maintains stable long-form synthesis, without using external SSL/ASR models, pretrained text language models, or post-training stages.

</details>

#### [Teffic-Audio: Tell Fact from Fiction](https://arxiv.org/abs/2607.28351) · [📄 Read](papers/2026/2607.28351.md)

**Wan Lin, Li Wang, Jindong Wang, Kunyu Feng et al.** · 2026-07-30

<details>
<summary>Abstract</summary>

Speech deepfake detection has expanded in scope with increasingly heterogeneous spoofing mechanisms, including speech synthesis, voice conversion, vocoder reconstruction, and neural-codec resynthesis. The resulting spoofing artifacts can be further shaped by variability in source speech, recording environments, and transmission channels. This variability makes robust generalization across heterogeneous conditions a central requirement for practical detection systems. This report presents Teffic-Audio, a general speech deepfake detection system designed for comprehensive evaluation environment. Teffic-Audio adopts a straightforward detector architecture consisting of a Conformer-based speech encoder, multi-head attentive statistics pooling, and a binary classifier. Rather than relying on additional architectural complexity, the system improves generalization through its training recipe, which integrates multi-source data, attack- and source-balanced sampling, and diverse audio augmentation. Trained only with open-source data, Teffic-Audio achieves a pooled EER of 1.454% on the 14 test sets of Speech-DF-Arena, outperforming all currently public systems on the leaderboard. It also obtains the lowest EER on five individual test sets and shows a favorable performance-complexity trade-off compared with larger leading systems. Overall, Teffic-Audio provides a strong and practical reference system for general speech deepfake detection.

</details>

#### [CrowdioSet and PaRIRset: Two Datasets Towards Live Music Source Separation](https://arxiv.org/abs/2607.27828) · [📄 Read](papers/2026/2607.27828.md)

**Enric Gusó, Xavier Serra** · 2026-07-30

<details>
<summary>Abstract</summary>

Most Music Source Separation (MSS) models do not generalize well to live music recordings because they are trained on studio recordings alone, disregarding the venue acoustics, the speaker system's response and audience noise. We propose to bridge this gap by providing and training a model on two novel datasets. First, we present CrowdioSet: a noise dataset comprising 4800 real ambience tracks from Freesound and synthetic sing-alongs for the vocals in MUSDB18 and MOISESDB datasets, generated from zero-shot singing voice conversions. CrowdioSet enables effective audio denoising for live recordings, resulting in superior separation both in objective and subjective evaluations. Second, we introduce PaRIRset, a stereo impulse response dataset captured across 40 professional concert venues using a microphone array. Our results show that adding PaRIRset RIRs increases the performance of a MSS model compared to using real RIRs from Speech Enhancement tasks alone. We make the examples, code, model weights, PaRIRset, and CrowdioSet freely available to the public.

</details>

#### [Cloned Voices, Real Consequences: Evaluating Bias in Political Deepfake Detection for Electoral Integrity in Brazil](https://arxiv.org/abs/2607.28770) · [📄 Read](papers/2026/2607.28770.md)

**Lucas Rafael Stefanel Gris, Daniel Casanova, Frederico Santos De Oliveira, Alef Iury Ferreira et al.** · 2026-07-30

<details>
<summary>Abstract</summary>

Recent advances in generative artificial intelligence have made it easier to fabricate statements and amplify political disinformation during elections. We introduce ParlaSpoof-BR, an audio deepfake dataset derived from recordings of the Brazilian Chamber of Deputies and expanded with synthetic utterances from diverse text-to-speech and voice conversion models. Using ParlaSpoof-BR, we benchmark state-of-the-art audio deepfake detectors, examine their ability to generalize to Brazilian Portuguese political speech, and investigate potential biases in their predictions. Our analysis reveals that current systems struggle to provide consistent decisions across the diversity represented in the dataset, with methodological factors (synthesis model choice, manipulation extent) dominating over demographic disparities. ParlaSpoof-BR provides a domain-specific benchmark for studying audio deepfake detection in a socially consequential and underrepresented setting, supporting the development of more robust detection systems for electoral integrity in Brazil.

</details>

#### [Zero-Shot Face-to-Speech Synthesis via Latent Space Adaptation of a Style-Diffusion TTS Model](https://arxiv.org/abs/2607.26742) · [📄 Read](papers/2026/2607.26742.md)

**Carlos Muñoz-Romero, Jose A. Gonzalez-Lopez** · 2026-07-29

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) clones a voice from a short audio prompt, but this reliance on reference audio is a barrier when only visual information is available, e.g. for historical figures or video-game characters. In this work, we propose a Face-to-Speech (F2S) framework that predicts a plausible voice from a static facial image. A lightweight Face Adapter, together with soft-tuning of the face encoder's upper blocks, aligns face-recognition features with the style space of a frozen StyleTTS 2 model, kept frozen during training. We evaluate on held-out identities from LRS3, a large-scale audiovisual corpus of English TED-talk videos. The synthesized speech is highly natural (UTMOS 3.7-4.0, matching or exceeding the 3.61 of ground truth), face-to-voice retrieval is consistently above chance, and the generated voice is consistent with the target speaker. Without any retraining, an English-trained adapter also produces fluent Spanish speech, indicating that the face-to-style mapping is largely language-agnostic.

</details>

#### [Extracting Voice Styles from Frozen TTS Models via Gradient-Based Inverse Optimization](https://arxiv.org/abs/2607.25351) · [📄 Read](papers/2026/2607.25351.md)

**Gyeongmin Kim** · 2026-07-28

<details>
<summary>Abstract</summary>

Some text-to-speech systems ship a synthesis model and preset style vectors but not the reference encoder that turns audio into such a vector. The model still accepts a style vector; a user with a voice of their own cannot produce one. We solve for that input directly, inverting the released pipeline by gradient descent: every weight stays frozen and only the style vector is optimized, against time-pooled WavLM statistics of one recording. Because the objective discards the time axis, the synthesized text may differ from the recording, so no transcript and no alignment are needed. On 154 speakers from two corpora, ECAPA-TDNN similarity rises from 0.132 to 0.413 and ResNet from 0.099 to 0.401, improving for every speaker; a verifier at its equal-error point accepts 53% of the recovered voices as the target, against 1% for the presets they start from.

</details>

#### [Qwen-Audio-3.0-TTS: Freely Controllable and Highly Robust Speech Synthesis with Multi-Stage Training Paradigm](https://arxiv.org/abs/2607.23938) · [📄 Read](papers/2026/2607.23938.md)

**Bajian Xiang, Cheng Wen, Han Zhao, Hao Wang et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

In this report, we present Qwen-Audio-3.0-TTS, a production-oriented speech synthesis system that jointly advances content consistency, speaker similarity, prosodic naturalness, audio quality, controllability, multilingual coverage, efficiency, and robustness. It combines a 12.5~Hz low-frame-rate speech tokenizer for reduced inference latency with a five-stage progressive training paradigm for coordinated language model (LM) and flow-matching model (FM) optimization. The model provides production-level control through free-style natural-language instructions and fine-grained inline tags, while supporting 16 languages, 20 Chinese dialect regions, one-pass long-form synthesis up to 3 minutes, and robust generation from noisy, reverberant, or unclear reference speech. Across SEED-TTS-Eval, CV3-Eval, instruction-following, long-form, and acoustic-robustness evaluations, Qwen-Audio-3.0-TTS achieves state-of-the-art performance on many reported dimensions or the strongest aggregate results. It also ranks first on the independent Artificial Analysis Text-to-Speech Leaderboard. These results establish Qwen-Audio-3.0-TTS as a strong foundation for production-level speech synthesis.

</details>

#### [Let Me Look at You: Advanced Facial Expression Modeling for Conversational Speech Synthesis](https://arxiv.org/abs/2607.24430) · [📄 Read](papers/2026/2607.24430.md)

**Yifan Hu, Shuwei He, Rui Liu, Haizhou Li** · 2026-07-27

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis is a fundamental component of human-computer interaction, aiming to generate contextually appropriate, expressive, and empathetic speech. However, facial expressions encode subtle and rich affective cues that are crucial for empathetic speech interaction, whereas existing approaches often overlook this important modality. In addition, the lack of large-scale natural conversational datasets with both speech and visual modalities also limits the development of visual affect understanding in conversational settings.To address these limitations, we propose FacialTalker, a facial-expression-aware CSS framework built upon a large language model backbone. To efficiently encode facial expressions, we propose AUTokenizer, a single-codebook visual tokenizer that discretizes each frame-level facial expression into a compact token, trained with supervision from combinations of facial Action Units. We further introduce a dual direct preference optimization (DualDPO) strategy, which extends the DPO by jointly imposing preference constraints on both visual and speech token sequences, to enhance the model's understanding of facial expressions and speech semantics in multimodal conversational contexts. Moreover, we construct VSDD-1K, a large-scale multimodal dialogue dataset collected through a fully automated pipeline from real-world Internet conversations, comprising over 1,033 hours of synchronized speaker videos and speech, with more than 85\% of frames containing valid faces. Extensive objective and subjective experiments demonstrate that FacialTalker consistently outperforms strong baselines in facial-expression perception and speech synthesis quality, generating speech that is more natural, expressive, and better aligned with the conversational context. The results also validate the effectiveness of our training strategy and dataset construction pipeline.

</details>

#### [Leveraging Gradient Reversal Loss and Multitask Learning for Datasets-Aware Audio Deepfake Detection](https://arxiv.org/abs/2607.23961) · [📄 Read](papers/2026/2607.23961.md)

**Mingrui Liang, Thomas Thebaud, Lukasz Wojciak, Laureano Moro Velazquez et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis and voice conversion, which pose threats to security and privacy, have underscored the need for deepfake detection technology. Although existing detection systems achieve strong performance on individual datasets, they often fail to generalize across diverse datasets. Prior methods for improving generalization, including data augmentation, adversarial training on auxiliary factors such as language or codec types, and Mixture-of-Experts (MoE), are limited by predefined augmentation coverage, difficulties in obtaining auxiliary factors, and substantial model complexity. In this work, we propose a practical dataset-aware framework for deepfake detection. Our method targets heterogeneous datasets for which auxiliary annotations such as language, codec, or spoofing method may not be consistently available. We therefore rely only on dataset identity as a naturally available supervisory signal for multitask (MT) and gradient reversal layer (GRL) training, allowing the model to investigate both dataset-aware multitask supervision and adversarial suppression of dataset-specific information. We conduct experiments following the 2025 Speech DeepFake Arena benchmark protocol, evaluating our model across multiple evaluation datasets and reporting aggregate performance in terms of Equal Error Rate (EER), including Average EER and Pooled EER. Compared with the baseline, MT reduces Average EER by 13.14% relatively, while GRL reduces Pooled EER by 5.32% relatively. These results demonstrate that our method can improve aggregate detection performance across heterogeneous evaluation datasets, offering a practical solution for deploying reliable deepfake detection systems on diverse and unseen real-world data.

</details>

#### [Revisiting Vocos: That Phasiness Business in Time-Frequency Neural Vocoding](https://arxiv.org/abs/2607.24323) · [📄 Read](papers/2026/2607.24323.md)

**Ünal Ege Gaznepoğlu, Frank Zalkow, Mohammad Joshaghani, Emanuël A. P. Habets et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

Recently, time-frequency neural vocoders have been approaching the state-of-the-art quality of time-domain neural vocoders. Vocos is a notable example due to its efficiency, but its audio quality lags behind the time-domain vocoders and the reasons remain debated. Thus, in this study, we revisit Vocos from a phase reconstruction perspective. First, we quantify the gap between time-domain and time-frequency domain vocoders using bandlimited mel spectrograms as inputs. Later, via an ablation study, we verify the Vocos architecture is effective for magnitude modeling, but less so for phase. We then adapt the Vocos backbone to predict phase differences, a precursor for phase reconstruction, and identify 1D convolutional layers are hindering their accurate prediction. Our findings indicate that future research needs to focus on inductive biases that allow the architecture to better model the time-frequency structure of speech signals, without sacrificing the support for arbitrary input representations.

</details>

#### [Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers](https://arxiv.org/abs/2607.23811) · [📄 Read](papers/2026/2607.23811.md)

**Dongseong Hwang, Prasanth Yadla, Kaan Elgin, Shifas Padinjaru Veettil et al.** · 2026-07-26

<details>
<summary>Abstract</summary>

Siri Expressive Voices synthesize rich, configurable speech in real time and entirely on device, powered by AFM 3 Core Advanced, Apple's most powerful on-device foundation model. This work presents the memory-efficient audio synthesis architecture behind that capability: a detokenizer that converts the semantic audio tokens emitted by the foundation model into high-fidelity audio within the tight compute and memory budget of the Apple Matrix Coprocessor (AMX). We convert semantic audio tokens to a residual vector quantization (RVQ) representation with a three-component design, a streaming encoder, a temporal decoder, and a depth decoder, that systematically decouples temporal and depth processing. A single reusable depth decoder with Diffusion Transformer (DiT)-style stage conditioning generates all RVQ levels autoregressively, replacing the dedicated per-level decoders of prior multi-decoder architectures, while causal sliding window attention with fixed-window key-value caching yields constant memory complexity independent of sequence length. Deployed on the AMX, the detokenizer sustains roughly 10 ms per generation step, about 16x faster than real time, with a peak runtime memory of only 21 MB and 329 MB of on-device assets, enabling continuous streaming synthesis of 20-320 seconds of audio. This constant, small footprint replaces the linear and quadratic memory scaling of conventional transformer- and GAN-based approaches. Ablation studies validate the key architectural components, and audio quality assessment confirms that the architecture maintains synthesis fidelity while achieving efficiency gains over existing methods. Operating at a 1-billion-parameter activation size within AFM 3 Core Advanced, it improves Mean Opinion Score by +0.28 overall (4.15 vs. 3.87) and by +0.42 on conversational speech (4.24 vs. 3.82) over the prior on-device text-to-speech system.

</details>

#### [Expose Your Disguise: Recovering Source Speaker Identity From Voice Conversion](https://arxiv.org/abs/2607.23650) · [📄 Read](papers/2026/2607.23650.md)

**Hanlei Zhang, Zhongming Ma, Mingyang Zhang, Tengfei Liu et al.** · 2026-07-26

<details>
<summary>Abstract</summary>

Voice conversion (VC) poses a significant threat to biometric security by allowing attackers to impersonate target speakers. In forensic contexts, recovering the source speaker's identity from converted audio is vital for narrowing the field of suspects. To address this, we propose TRIDENT, a retracing framework designed to restore a source speaker's original identity from a converted audio sample. TRIDENT utilizes a three-pronged architecture consisting of a primary extractor and two auxiliary branches. The first auxiliary branch identifies the underlying voice conversion mechanism. This design acknowledges that even if the exact conversion strategy is unknown, a high-performance model adopted by the attacker is typically a derivative or variant of established mainstream ones. The second auxiliary branch extracts a latent representation of the target speaker, facilitating the isolation of target-specific traits from the composite converted audio sample. Finally, the main extractor leverages insights from both auxiliary branches to decouple confounding factors and distill a highly discriminative representation of the source speaker's identity. Experimental results demonstrate that TRIDENT achieves an accuracy as high as 90.99% against 7 state-of-the-art voice conversion methods. Furthermore, TRIDENT maintains robust performance under challenging conditions, including telephony channels, unseen languages, and adaptive scenarios.

</details>

#### [Singlish, Can or Not? Fine-Tuning and Evaluating Zero-Shot TTS for Singapore English](https://arxiv.org/abs/2607.23027) · [📄 Read](papers/2026/2607.23027.md)

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

</details>
<!-- PAPERS_TABLE_END -->
