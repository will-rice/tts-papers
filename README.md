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

_Showing the last 30 days (51 of 3376 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [PACodec: A Low-bitrate Neural Speech Codec with Parallel Additive Vector Quantization](https://arxiv.org/abs/2609.03363) · [📄 Read](papers/2026/2609.03363.md)

**Fei Liu, Yang Ai, Xiao-Hang Jiang, Zhen-Hua Ling** · 2026-09-03

<details>
<summary>Abstract</summary>

This paper proposes PACodec, a novel low-bitrate neural speech codec based on parallel additive vector quantization (PAVQ). Unlike the mainstream residual vector quantization (RVQ) used in most neural speech codecs, where vector quantizers (VQs) are sequentially dependent, the PAVQ strategy adopted in PACodec aggregates parallel quantization results to optimize bitrate usage. Specifically, the PAVQ adopts a "global-local-global" (GLG) design: the global encoded features are quantized in parallel by multiple independent VQs, each attending to a local component of the representation, and their outputs are aggregated through addition to yield the final global quantization result for decoding. Experimental results show that PACodec, as each VQ focuses only on local information, supports smaller codebooks and reduces bitrate by 30% compared with baselines at the same decoding quality, with only minor model complexity. Further analysis shows that, owing to the GLG framework of PAVQ, the proposed PACodec is disentanglement-friendly, and each independent VQ captures different aspects of speech, e.g., content, timbre, and acoustic details, suggesting potential for application to downstream tasks such as voice conversion.

</details>

#### [Building and Evaluating Fixed-Voice Thai TTS from Synthetic Speech](https://arxiv.org/abs/2609.03502) · [📄 Read](papers/2026/2609.03502.md)

**Kunat Pipatanakul, Potsawee Manakul, Warit Sirichotedumrong, Sittipong Sripaisarnmongkol et al.** · 2026-09-03

<details>
<summary>Abstract</summary>

In low-resource settings, deploying TTS typically requires choosing between a large voice-cloning model with costly inference or a compact fixed-voice system that requires a speaker-specific corpus. We study a third route: using a large voice-cloning model as a programmable data source to turn a short voice reference (e.g., 15 seconds) into a compact fixed-voice student trained entirely on synthetic speech. This setting makes pipeline design consequential: teacher errors become training targets, while filtering failed generations can reduce coverage of difficult texts. Thai further introduces challenges from ambiguous word boundaries, lexical tone, names and loanwords, numeric verbalization, and Thai-English code-switching. We study how text preparation, synthetic generation, quality filtering, rejection sampling, and frontend choices affect the resulting student, and where teacher limitations remain. We evaluate CER, Challenge-Set Keyword Accuracy, Prosody Pause Accuracy, speaker similarity, and speaking rate. The resulting 82M-parameter model, Wayu-Paxa-TTS-Edge, enables on-device Thai TTS without reference audio. It achieves 68.2% Challenge-Set Keyword Accuracy (85.5% of Gemini 3.1) and 91.4% pause precision, outperforming its OmniVoice teacher (89.9%) and reaching 94.8% of Gemini 3.1. It also achieves the lowest pause-placement error and intra-word pause rates among the three systems, and 3.7% and 1.1% CER on Thai and English, respectively. We open-source the model and evaluation framework for Thai TTS development.

</details>

#### [Deep Neural Compression for RIR-Characterized Acoustic Environments with Structure-Aware Constraints](https://arxiv.org/abs/2609.04085) · [📄 Read](papers/2026/2609.04085.md)

**Chen-Yuan Ning, Yang Ai, Hui-Peng Du, Xiao-Hang Jiang et al.** · 2026-09-03

<details>
<summary>Abstract</summary>

Room impulse responses (RIRs) characterize the acoustic environment of a room by capturing how sound propagates and decays within an enclosed space. In applications such as immersive audio rendering, accurate acoustic reconstruction often relies on spatially densely sampled RIRs. This consequently gives rise to a large volume of RIR data, imposing a substantial burden on storage. Although recent neural audio codecs provide an effective framework for low-bitrate compression, their training objectives are mainly tailored to speech and general audio, and are therefore not well aligned with the acoustic characteristics of RIRs. Therefore, we propose an EnCodec-based neural RIR compression method, which incorporates RIR structure-aware constraints at two levels. Specifically, at the RIR level, structure-aware constraints are imposed on the global decay behavior and local energy distribution of RIRs through energy decay curve (EDC) regularization and a short-time window energy constraint, while at the reverberant-speech level, reverberant-speech supervision is further introduced to constrain the consistency of the reverberant speech generated by the reconstructed RIRs. Experimental results show that, at a low bitrate of 375 bps, the proposed method achieves lower RIR reconstruction error and better reverberant-speech perceptual consistency than audio-oriented codecs.

</details>

#### [Ready to Speak: Aligning LLMs for TTS-Friendly Text Generation](https://arxiv.org/abs/2609.01246) · [📄 Read](papers/2026/2609.01246.md)

**Thibaut Thonet, Jos Rozen, Laurent Besacier** · 2026-09-01

<details>
<summary>Abstract</summary>

Current Large Language Models (LLMs) are primarily optimized for written text, often producing outputs that are grammatically correct and helpful yet poorly suited for spoken delivery via Text-to-Speech (TTS). In this work, we study how to make LLMs natively generate TTS-friendly text, which we frame as a preference alignment problem: instead of relying on downstream rewriting modules, we directly align LLMs to generate text optimized for spoken delivery. We introduce two preference datasets spanning different target domains, CORA and Recipe, which contain paired TTS-friendly and TTS-unfriendly responses. We further propose an evaluation suite combining a pattern-based heuristic metric, a TTS$\to$ASR evaluation pipeline, and a MUSHRA listening study with human judges. Our experiments compare the recently proposed Feature-aware Sampling and Tuning (FaST) framework -- leveraging interpretable features instead of a black-box reward model -- against an array of alignment baselines on the TTS-friendly generation task. Notably, we found that FaST achieves the best overall tradeoff between TTS-friendliness and helpfulness across various settings. We also identified a strong correlation between our different metrics, highlighting the ability to reliably assess TTS-friendliness via an efficient heuristic.

</details>

#### [Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech](https://arxiv.org/abs/2609.01016) · [📄 Read](papers/2026/2609.01016.md)

**Che Hyun Lee, Sangkwon Park, Donghun Kang, Dongwook Lee et al.** · 2026-09-01

<details>
<summary>Abstract</summary>

Current speech synthesis struggles with code-switching, which mixes a foreign language phrase into a primary language utterance, causing the phrase to be spoken with the primary language's accent rather than its native one. We propose Phrase-Localized Language-Contrastive Guidance (LCG), a training-free inference framework that restores a native accent to code-switched phrases in cross-lingual text-to-speech. LCG replaces the single language guidance applied across the whole utterance with a separate guidance for each region, so each part is guided by its own language. To choose where to apply this localized guidance, we propose a self-attention probing technique that finds the phrase boundaries without external alignments. Together, these components generate speech in which each region carries the accent of its own language, requiring no fine-tuning or auxiliary models. Across diverse language pairs, LCG robustly increases the nativeness of the code-switched phrase while suppressing accent leakage, and preserving overall speaker identity and naturalness.

</details>

#### [Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models](https://arxiv.org/abs/2609.01723) · [📄 Read](papers/2026/2609.01723.md)

**Kunlin Cai, Kaiyuan Zhang, Zihang Xiang, Jinghuai Zhang et al.** · 2026-09-01

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) foundation models are increasingly fine-tuned on private datasets to synthesize highly personalized voices, introducing severe privacy risks by exposing both biometric identities and sensitive speech content. Existing black-box membership inference attacks (MIAs) follow a two-stage pipeline of query generation and representation engineering, both of which face unique challenges when adapted to TTS. For query generation, dual conditioning on synthesis text and reference speech creates a large and underexplored query design space with no established criterion for identifying an effective query. For representation engineering, the multi-level speech characteristics and temporal variability of speech make low-level representations and direct comparisons inadequate for capturing membership signals. To address these challenges, we present the first black-box MIA framework explicitly tailored to TTS models at both the speaker and record levels. For query generation, we characterize the feasible query space and establish two criteria, scorable extent and memorization elicitation, for evaluating five representative queries, identifying recitation as the strongest. For representation engineering, we obtain multi-level speech representations from embedding models and temporally align the generated and target audio for fine-grained comparison. Evaluations across three state-of-the-art TTS models (CosyVoice2, F5-TTS, and XTTS-v2) fine-tuned on two benchmark datasets (VCTK and British Dialect) reveal severe privacy leakage: speaker-level AUC remains above 0.80 and approaches 1.0 in the strongest settings, while record-level AUC ranges from 0.80 to 0.90 and remains effective even in challenging scenarios where both members and non-members are of the same speakers. We further identify speech characteristics associated with disproportionate vulnerability to memorization.

</details>

#### [BiMTokenizer: Preserving Semantic-Acoustic Balance in Low-Bitrate Speech Tokenization via Bidirectional State-Space Modeling](https://arxiv.org/abs/2609.00562) · [📄 Read](papers/2026/2609.00562.md)

**Xin Zhang, Lin Li, Chuanbo Liu, Jianquan Liu et al.** · 2026-09-01

<details>
<summary>Abstract</summary>

Speech codecs serve as bridges between continuous speech signals and large language models, yet face an inherent conflict between acoustic fidelity and semantic preservation. To mitigate this conflict, recent works increasingly adopt dual-tower architectures to decouple semantic and acoustic modeling with separate encoders. However, these dual-tower designs incur substantial architectural overhead. To avoid such complexity, we revisit the single-tower paradigm and propose BiMTokenizer, a low-bitrate speech codec (around 1.1 kbps) combining a bidirectional state-space backbone with Residual Spherical Leech Quantization (RSLQ). The bidirectional backbone strengthens temporal modeling, while RSLQ offers a fixed, well-separated lattice bottleneck for robust semantic and acoustic tokenization without learned-codebook collapse. Experiments show that BiMTokenizer achieves superior acoustic reconstruction and the lowest WER among low-bitrate codec baselines across both clean and noisy environments, while using less than half the parameters of recent dual-tower baselines. Furthermore, its robust semantic representations yield strong performance on downstream speech understanding tasks, confirming that a well-designed single-tower codec can preserve the semantic-acoustic balance at low bitrates. The code and model weights are available at https://github.com/ZhangXinWhut/BiMTokenizer.

</details>

#### [When Does Predictor-Based RL Align with Human Perception? A Study of Subjective Rewards in Codec-Based Speech Language Models](https://arxiv.org/abs/2608.31035) · [📄 Read](papers/2026/2608.31035.md)

**Joonyong Park, Jerry Li** · 2026-08-31

<details>
<summary>Abstract</summary>

Codec-based text-to-speech (TTS) models make language-model post-training applicable to speech generation, but it remains unclear when learned perceptual predictors can serve as reinforcement learning rewards without losing alignment with human listeners. We study this question with Group Relative Policy Optimization (GRPO) using learned rewards for anime-like speaking style, naturalness, likability, and arousal. To prevent perceptual rewards from being optimized through transcript drift, we introduce a character error rate (CER) zone constraint and compare policy optimization with Best-of-$N$ reranking under the same reward gate. Across single-reward runs, each reward primarily improves its own target metric, showing that subjective predictors are not interchangeable quality surrogates. Multi-rater A/B tests further show uneven human transfer, while a reward-gap analysis separates average transfer from within-axis calibration: signed reward gaps significantly predict listener choices in the pooled analysis, whereas residual CER gaps do not, but per-axis calibration remains heterogeneous. Best-of-8 is a strong human-level baseline and is not clearly worse than GRPO perceptually, suggesting that GRPO should be viewed as amortizing reward-selected behavior into the policy rather than uniformly outperforming reranking. These results support analyzing subjective speech rewards as predictor-axis-base tuples and provide practical diagnostics for selecting rewards before multi-reward speech post-training.

</details>

#### [When Patients Cut In: Extending Clinical Conversational AI Safety to Interruptions](https://arxiv.org/abs/2608.29241) · [📄 Read](papers/2026/2608.29241.md)

**Zachary Ellis, Spencer Hazel, Adam Brandt, Yajie Vera He et al.** · 2026-08-29

<details>
<summary>Abstract</summary>

Clinical voice agents are now deployed in routine care, where real patients do not wait their turn: they interrupt. These systems typically use a cascaded architecture (speech-to-text -> LLM -> text-to-speech), so when a patient cuts the agent off mid-utterance, clinically required content can be lost even when the model handles cooperative transcripts well. Yet clinical conversational-AI benchmarks almost universally assume patients wait for the agent to finish, missing interruption-induced loss of required content. We present a transcript-based evaluation of interruption recovery, adapting conversation-analytic overlap categories into three operational types (recognitional, competitive, transitional sub-unit) and testing four deployment-oriented, non-reasoning LLM configurations across four cells spanning history-taking (information gathering) and FAQ (information provision), scored on whether the agent preserves the clinically required content. In the gathering cells, target-question failure varied across models; in the provision cells, where arms are directly comparable, failure rose for every model. Rankings differ across cells, and competitive FAQ interruption produced 30/30 provision-coverage failures for all four models (Wilson 95% CI: 88.6-100.0%; baseline 0/30 for three, 4/30 for Llama). A brief apology marker ("sorry to interrupt") shifts recovery by tens of percentage points, inconsistently across models, and for one it reduces recovery. Interruption robustness therefore cannot be a single score: evaluation must be content-grounded, reported per cell, and matched to the deployment's interruption profile.

</details>

#### [EmoSay: Artificial Intelligence-Driven Text-to-Emotional-Speech System for Affective Communication in Extended Reality](https://arxiv.org/abs/2608.26566) · [📄 Read](papers/2026/2608.26566.md)

**Sikiru Ademola Adewale, Sunday D. Ubur, Nikitha Donekal Chandrashekar, Onyeka Emebo et al.** · 2026-08-27

<details>
<summary>Abstract</summary>

While contemporary neural text-to-speech (TTS) systems have achieved high levels of intelligibility, they frequently lack the emotional nuance required for authentic affective communication. This limitation is particularly critical in Extended Reality (XR), where the absence of emotionally expressive audio can diminish user presence and spatial immersion. We present EmoSay, an Artificial Intelligence-driven Text-to-Emotional-Speech (TTES) system designed to bridge the semantic-affective gap in immersive environments. EmoSay modulates a neural synthesis pipeline using discrete emotional prompts, delivering the output through a Unity-based interface featuring high-fidelity spatialized audio. The system was evaluated through a comprehensive user study focusing on perception, engagement, and the subjective sense of empathy. Our results demonstrate that EmoSay significantly enhances the immersive experience, achieving a System Usability Scale (SUS) score of 74.76, indicating strong usability and seamless integration within the XR workflow. Subjective assessments reveal a high degree of perceived naturalness and a strong positive correlation between emotional expressiveness and user engagement. Regression analysis identifies vocal naturalness as the strongest of the tested predictors of user satisfaction, suggesting that EmoSay's affective prosody helps meet the heightened expectations for realism in immersive settings. This work contributes a scalable, affect-aware framework for inclusive XR design and demonstrates the role synthetic emotion can play in fostering human-computer rapport through voice-first interaction.

</details>

#### [Your Voice Cloning System is Secretly a Voice Anonymizer](https://arxiv.org/abs/2608.27360) · [📄 Read](papers/2026/2608.27360.md)

**Romolo Muletta, Felix Matthias Saaro, Mark Cieliebak, Jan Deriu** · 2026-08-27

<details>
<summary>Abstract</summary>

Speaker anonymization suppresses speaker-identifying attributes from speech while preserving linguistic content and quality. We propose repurposing XTTSv2, a multilingual voice cloning model trained on 27k hours of speech, for speaker anonymization without retraining. Our key insight is that XTTSv2's voice cloning capabilities preserve prosodic structure independently of speaker identity, enabling voice conversion by conditioning on a pseudo-speaker. We introduce an iterative refinement strategy that balances privacy and utility by maximizing a harmonic mean of speaker dissimilarity and intelligibility. Evaluated on seven European languages across CommonVoice and Multilingual LibriSpeech, our system achieves near-optimal privacy (EER $\approx$ 0.49), competitive intelligibility, and substantially better speech quality than dedicated anonymization baselines, while requiring no language-specific training. We release the code here: https://github.com/rm00cr/coqui-tts.

</details>

#### [HUG-VIS: A Multimodal Benchmark for Human-centered Understanding and Generation in Visual Intelligence](https://arxiv.org/abs/2608.26517) · [📄 Read](papers/2026/2608.26517.md)

**Fei Ma, Zebang Cheng, Minghui Li, Hongbo Xu et al.** · 2026-08-27

<details>
<summary>Abstract</summary>

Visual intelligence seeks to perceive, interpret, and synthesize the visual world and is central to modern computer vision. Human-centered visual intelligence is especially demanding because it studies people as expressive, socially situated subjects whose meaning is rarely conveyed by appearance alone. It couples vision with audio and language across four representative tasks: human emotion recognition, human video generation, human voice cloning, and human video matting. Yet existing resources remain task-specific, providing modalities and annotations for individual problems rather than a shared foundation coordinating understanding and generation. This limits multimodal signal use and broader research. We address this gap with HUG-VIS, a unified benchmark for Human-centered Understanding and Generation in Visual Intelligence. It contains 8,400 seated half-body videos of 30 professional actors, each performing the same 280 emotion-action-prompt assignments under a controlled Mandarin studio protocol, with synchronized video, audio, text, and alpha mattes. We evaluate diverse open- and closed-source models across the four tasks under a unified zero-shot protocol using automatic metrics, criterion-specific mean opinion scores, and multiple cross-task analyses. Results show that (i) linguistic content dominates current emotion recognition, while purely visual affect recognition is weakest; (ii) in video generation and voice cloning, automatic metrics and human judgment agree overall but differ in their top rankings, requiring joint reporting; (iii) boundary fidelity under motion is the main remaining obstacle for human matting; and (iv) task difficulty varies across emotions, models, and metrics, with notable cross-task correlations. The dataset and results are available at https://github.com/GML-MMGroup/HUG-VIS.

</details>

#### [CSAVocoder: A Causal Spatial Audio Vocoder Towards Real-Time Spatial Audio Generation](https://arxiv.org/abs/2608.25404) · [📄 Read](papers/2026/2608.25404.md)

**Zhiyuan Zhu, Han Wang, Wenxiang Guo, Yu Zhang et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Spatial audio vocoders are able to convert mel-spectrograms produced by generative models into spatial audio waveforms. Most neural vocoders are designed for monaural audio, and direct extensions to spatial audio can degrade spatial quality by ignoring inter-channel cues. We present CSAVocoder, a causal GAN-based spatial audio vocoder that jointly optimizes waveform fidelity and spatial rendering. Our framework introduces a Spatial Adaptor that fuses multi-channel mel-spectrograms with dynamic source-listener pose information, together with a spatial consistency discriminator that supervises inter-channel cues. To meet real-time requirements, we design a strictly causal, stateful generator that supports efficient streaming inference with constant memory overhead. Experiments on large-scale spatial audio datasets show that CSAVocoder improves spatial fidelity at competitive audio quality and real-time performance.

</details>

#### [InteractGesture: Progressive Chunk Guidance for Continuous Streaming Co-Speech Gesture Control](https://arxiv.org/abs/2608.25734) · [📄 Read](papers/2026/2608.25734.md)

**Ekkasit Pinyoanuntapong, Ajinkya Deogade, Paul Streli, Wenjing Zhang et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Co-speech gesture generation has made significant progress toward realistic full-body motion from speaker audio, yet existing models lack fine-grained spatial controllability of individual joints. To address this, we introduce \emph{InteractGesture}, a model-agnostic, inference-time method for spatially controllable gesture generation. \emph{InteractGesture} guides target latent estimates of a diffusion sampler through a differentiable RVQ-VAE decoder, backpropagating spatial control gradients to adjust motion latents during sampling. A primary challenge in streaming co-speech generation is chunk-wise dependency: standard sequential inference freezes prior chunks, preventing spatial constraints in future chunks from adjusting preceding trajectories and causing boundary inconsistencies. To overcome this limitation, we propose \emph{Progressive Chunk Guidance}, a chunk-window strategy that maintains an active set of editable chunk latents with staggered delays, enabling spatial constraints to propagate gradients backward across chunk boundaries during streaming generation. Experiments on the BEAT2 dataset show that \emph{InteractGesture} improves multi-joint spatial control while preserving overall gesture quality. Furthermore, our approach supports diverse applications, including sparse joint positioning, dense joint trajectory control, and directional pointing. Our project page is available at https://exitudio.github.io/interactgesture-page .

</details>

#### [OmniJudge or OmniBias? Diagnosing Multimodal Judges through Balanced, Decoupled Lenses](https://arxiv.org/abs/2608.24160) · [📄 Read](papers/2026/2608.24160.md)

**Guangzheng Hu, Ziyue Jiang, Weixu Qiao, Lixin Zhang et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

Multimodal understanding models that can jointly judge text-to-image (T2I), text-to-video (T2V) and text-to-speech (TTS) generation are increasingly used as "OmniJudges" for evaluation and automatic annotation. How reliably they understand what they score remains unclear, since existing benchmarks and training data tend to overemphasize positive examples and to conflate distinct failure modes, so a judge may score well without recognizing failures while its capability gaps stay hidden. Motivated by this, we introduce D3-Omni, a balanced and decoupled benchmark for diagnosing fine-grained multimodal understanding, covering 53 orthogonal binary dimensions (17/22/14) and 10,671 samples (3,526/1,998/5,147) across the three tasks. Rather than re-generating outputs, which may leak information across dimensions, we fix verified fully positive seeds and derive negatives through controlled prompt rewriting and atomic, dimension-isolating perturbations. The resulting D3 design is Dual-balanced, which helps alleviate negative-sample scarcity and per-dimension label imbalance; Decoupled, so that each error is attributable to a single capability; and Dynamic, steering construction toward under-represented regions of the label distribution as generative models improve.The suite reaches near 1:1 per-dimension parity and a uniform distribution over all total-score levels. Under this balanced view, even strong OmniJudges tend to struggle on modality-related dimensions, to confirm satisfied requirements far more reliably than they detect violated ones, and to treat nominally distinct attributes as largely a single decision, suggesting that aggregate accuracy may hide systematic blind spots that a balanced and decoupled lens can help expose and, in turn, address.

</details>

#### [FireRedAudio: A General-Purpose Audio Language Model with Decoupled Continuous Representations for Understanding and Generation](https://arxiv.org/abs/2608.24168) · [📄 Read](papers/2026/2608.24168.md)

**Junjie Li, Xuelong Geng, Kun Xie, Feiyu Shen et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

A unified audio model must recognize and understand linguistic, paralinguistic, and environmental information while supporting speech synthesis and editing. A key challenge is representation: understanding favors compact features suited to long-context modeling, whereas speech generation requires reconstructible features that preserve fine-grained acoustic detail. We introduce FireRedAudio, a general-purpose audio language model with a shared 9B-parameter LLM. To the best of our knowledge, it is the first publicly disclosed unified audio-language model to provide separate continuous input representations for understanding and generation within a single trainable autoregressive LLM. Audio to be recognized or analyzed is processed by a dedicated Audio Encoder, while speech inputs for generation use a RedAE-based pathway. The LLM directly generates text or conditions a flow-matching DiT to produce continuous acoustic latents. Through progressive multitask training, FireRedAudio supports ASR and audio understanding, with the latter extending to recordings of up to one hour, as well as zero-shot TTS, Instruct TTS, and semantic and acoustic speech editing. Its structured organization of long-form audio achieves second-level timestamp accuracy. Across comprehensive evaluations, FireRedAudio achieves competitive or leading performance in audio understanding and multilingual ASR, strong content accuracy and speaker preservation in zero-shot TTS, leading instruction following in Instruct TTS, and substantial improvements over Ming-UniAudio-Edit in both semantic and acoustic speech editing. These results demonstrate the viability of decoupled continuous input representations for unifying audio understanding and continuous-latent speech generation in a model of moderate scale. Our code is available at https://github.com/FireRedTeam/FireRedAudio.

</details>

#### [Speech-to-SOAP: End-to-End Summarization of Medical Dialogues: KIT@BeTraC 2026](https://arxiv.org/abs/2608.24327) · [📄 Read](papers/2026/2608.24327.md)

**Enes Yavuz Ugan, Fabian Retkowski, Yuka Ko, Thai-Binh Nguyen et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

With the advent of Large Language Models and its instruction following capabilities a promising application is the task of summarization. Within this domain of task the extractive sub-task of clinical protocolling has emerged as a topic of particular interest as it can significantly reduce the downtime and protocolling burden of health-care workers thus enabling them to focus on their core work helping humans. A further step towards automation is the direct generation of clinical notes from speech without intermediate transcripts, reducing processing time while preserving information such as coughing or other paralinguistic cues that may be lost in transcript-based systems. To this end, we present KIT's submission to this years BeTraC challenge in the lightweight track. Our main contribution is a scalable data augmentation pipeline that unifies heterogeneous medical dialogue datasets through synthetic speech generation and automatically generated SOAP supervision, enabling robust adaptation of a speech foundation model for end-to-end speech-to-SOAP generation.

</details>

#### [Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight](https://arxiv.org/abs/2608.24314) · [📄 Read](papers/2026/2608.24314.md)

**Anupam Purwar, Shashank Singh, Kritika Srivastava** · 2026-08-25

<details>
<summary>Abstract</summary>

Evaluating conversational voice agents at scale re- quires reliable assessment methods that capture both observ- able interaction quality and the contextual judgment typically provided by human evaluators. We investigate LLM-as-a-Judge evaluation by comparing human judgments with GPT-4.1 and GPT-5 on telecom and retail voice-agent conversations, across conversational quality and safety dimensions. The same interac- tions are scored under three evaluation configurations, p0, p1, and p2, to test whether automated judgments are sensitive to the evaluation setup and whether observed patterns generalize across configurations and judge models. Beyond aggregate agreement, we examine metric-level correlations, evaluator consistency, and systematic human-LLM disagreement to identify which conver- sational attributes can be judged reliably by automation and which remain sensitive to interpretation and context. Effective voice-agent evaluation is also shaped by pipeline-level factors such as speech generation, streaming, and error propagation across ASR, reasoning, and tool-calling stages, motivating our focus on comparing how human and LLM judges score the same interactions end to end. Our results show that LLM- based evaluation can serve as an effective component of large- scale voice-agent assessment, but that its reliability is metric- and configuration-dependent rather than uniform. This pro- vides an empirical framework for identifying which metrics suit automated evaluation and supports hybrid pipelines in which LLM judges handle scalable assessment while human evaluators remain engaged for metrics that demand contextual interpretation and higher-confidence judgment.

</details>

#### [EmoTra-TTS: Smooth Intra-Utterance Emotion Transitions for Speech Synthesis](https://arxiv.org/abs/2608.23791) · [📄 Read](papers/2026/2608.23791.md)

**Tianchi Liu, Zeyang Song, Tianrui Wang, Zhipeng Li et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

Psychological research on emotion dynamics has established that human affect is a continuous, evolving process: emotions rise, decay, and transition within seconds. Current emotional text-to-speech (TTS) systems, however, condition on a single discrete label or static embedding per utterance, fundamentally misaligning with the temporal nature of affect. While recent LLM-based TTS systems may implicitly vary prosody through text understanding, such variation is neither explicitly controllable nor precise enough for targeted intra-utterance transitions. We address three challenges: (1) a multi-pass flow blending pipeline synthesizes frame-aligned transition audio, circumventing the scarcity of natural intra-utterance transitions; (2) dual-stage Valence-Arousal-Dominance (VAD) conditioning guides prosodic planning in the LLM and acoustic realization in the flow decoder via frame-level VAD embeddings; (3) direction-magnitude decoupled injection structurally separates emotion direction from injection magnitude, preventing content degradation. EmoTra-TTS adds only +0.43% parameters with no latency overhead, achieves 30%-87% relative improvement on emotion transition quality, corroborated by 64.4%-79.5% overall win rates in pairwise preference tests against four SOTA baselines and two commercial systems.

</details>

#### [Interaction Effects Between Learner Characteristics and Dialogue Format in TTS Dialogue-Based Lessons](https://arxiv.org/abs/2608.20822) · [📄 Read](papers/2026/2608.20822.md)

**Fumie Watanabe, Tota Suko, Takashi Ishida, Yuko Kuma et al.** · 2026-08-21

<details>
<summary>Abstract</summary>

This study examined how learner characteristics affect motivation, learning outcomes, and overall evaluation in three types of dialogue-based lessons---(1) teacher--student, (2) student--student, and (3) teacher--teacher---generated using a large language model (LLM) and Text-to-Speech (TTS) technology. In particular, we focused on the interaction effects between dialogue format and learners' experiential learning style (the Concrete Experience factor, CE; and the factor of active experimentation through reflective observation and abstract conceptualization, RCE) and critical thinking disposition. Using a repeated-measures design with 222 first-year high school students, we analyzed the data with linear mixed-effects models. The results showed a significant interaction between learner characteristics and dialogue format for ARCS-based motivation. Specifically, the effect of the CE factor on motivation was more strongly positive in the teacher--teacher format than in the teacher--student format, whereas the positive effect of the RCE factor was relatively weaker in the teacher--teacher format. For learning outcomes, the interactions between dialogue format and both the CE and RCE factors showed a trend toward significance. No significant interaction emerged for overall evaluation; however, the overall evaluation of the teacher--teacher format was significantly lower than that of the teacher--student format, a pattern that diverged from the positive effect observed for motivation. These results suggest that dialogue format should be selected according to learner characteristics in TTS dialogue-based lessons. Because the effect sizes of the significant interactions were all small to medium, however, the findings of this study should be regarded as preliminary evidence for the design of personalized learning.

</details>

#### [DAMOS: Learning Distortion-Aware Speech Quality Assessment through Explicit Distortion Localization](https://arxiv.org/abs/2608.21176) · [📄 Read](papers/2026/2608.21176.md)

**Naiyuan Li, Li Dong, Diqun Yan** · 2026-08-21

<details>
<summary>Abstract</summary>

Automatic speech quality assessment aims to predict Mean Opinion Scores (MOS) consistent with human subjective perception and is essential for evaluating speech generation, enhancement, and communication systems. For speech signals, especially synthetic speech, distortions often occur locally, and overall perceptual quality is usually dominated by a small number of perceptually salient distortion regions. However, most existing methods are primarily optimized with utterance-level MOS, which provides only coarse-grained supervision and offer no explicit indication of where perceptually important distortions occur. To address this limitation, we introduce explicit distortion localization as auxiliary knowledge for speech quality assessment. We construct the first partially distorted speech dataset with frame-level distortion annotations and train a localization model to generate distortion cues. Building on these cues, we propose DAMOS, a distortion-aware speech quality assessment framework that integrates localization information into the MOS prediction pipeline. Experiments on multiple public benchmarks demonstrate that DAMOS consistently outperforms existing methods and exhibits strong cross-dataset generalization, validating the effectiveness of explicit distortion localization for speech quality assessment.

</details>

#### [Hear2Act: Benchmarking When Prosody Should Change What an Assistant Does](https://arxiv.org/abs/2608.19515) · [📄 Read](papers/2026/2608.19515.md)

**Xinyi Liu, Hooshang Nayyeri, Dilek Hakkani-Tur, Emine Yilmaz et al.** · 2026-08-21

<details>
<summary>Abstract</summary>

Prosodic cues can convey task-relevant information that alters the trajectory and outcome of a task-oriented dialogue, even when the words themselves remain unchanged. Yet existing benchmarks typically evaluate prosodic perception, response appropriateness, and task-oriented dialogue in isolation, making it difficult to test whether prosodic evidence changes downstream decisions. We introduce Hear2Act, a unified evaluation protocol for text and spoken assistants with 480 persona-grounded scenarios, hidden user concerns, and objectively verifiable outcomes. For each scenario, we keep the task and user needs fixed while varying whether the same concern is conveyed explicitly in words or primarily through prosody, and evaluate decisions under transcript, audio, and concern-state access. Using Hear2Act, we evaluate two audio-capable LLMs. Under Prosody-mediated feedback, adding audio to the transcript changes the average optimal-solution rate only from 14.6% to 15.3%. In contrast, when models infer the concern status from audio, represent it in text, and use it for next-action selection, the rate rises to 39.6%, close to 40.7% with the ground-truth state. This contrast, however, largely disappears under Explicit lexical feedback, where the concern is verbally mentioned in the utterance. Together, these results show that prosody matters when lexical evidence is insufficient, and that audio-capable LLMs can recover information from speech but do not reliably carry it into action without an explicit intermediate representation.

</details>

#### [Tracking the Trend in How Speech Synthesizers Deceive People](https://arxiv.org/abs/2608.19959) · [📄 Read](papers/2026/2608.19959.md)

**Milan Šalko, Anton Firc, Kamil Malinka, Vojtěch Staněk et al.** · 2026-08-20

<details>
<summary>Abstract</summary>

Advances in speech synthesis have made deepfake audio highly realistic. Earlier studies reported 70-80% human detection accuracy, but relied primarily on older synthesizers. We compare human detection for three selected voice synthesis tools released in 2019, 2022, and 2024 with 82 IT professionals, and benchmark humans against six pretrained detectors on the same material. For fully synthetic speech (full spoofs), the F1 score drops from about 90% for RTVC and YourTTS to 48% for ElevenLabs, although listeners were explicitly warned that deepfakes were present. For partial spoofing, where only one sentence of an utterance is altered, strict accuracy falls to 9%, and listeners classify the synthetic sentence as bona fide 77% of the time. Humans and detectors fail in complementary ways, and neither reliably localizes short manipulations. Additionally, listeners increasingly mislabel bona fide speech as fake, eroding trust in unmanipulated audio. These findings show that human perception alone is unreliable for the selected modern and partial-spoof conditions and motivate procedural verification, provenance, watermarking, and segment-level detection.

</details>

#### [Does Listening Matter? Backchanneling and Nodding in AI Clone](https://arxiv.org/abs/2608.19527) · [📄 Read](papers/2026/2608.19527.md)

**Koji Inoue, Kazushi Kato, Tatsuya Kawahara, Shunichi Kasahara** · 2026-08-20

<details>
<summary>Abstract</summary>

AI clones that imitate a specific person typically reproduce what the person says and how they sound, but not how they listen. We investigate whether adding multimodal listening behaviors gives such a clone more presence and authenticity. We integrated verbal backchannels and head nodding, driven by real-time prediction models, into an AI clone equipped with voice cloning and LLM-based responses. In a within-subjects study (N=35), adding these behaviors significantly improved the perceived attentiveness of the avatar, the sense of talking with the real person, and the feeling of co-presence. These results indicate that AI clone fidelity should extend beyond voice and response content to include interactive listening behavior.

</details>

#### [X2Streaming-TTS: Causal Token-Level Text-to-Speech from Streaming Text with Speech-State Inheritance](https://arxiv.org/abs/2608.18661) · [📄 Read](papers/2026/2608.18661.md)

**Rime Wen, Zehan Liu, Shawn Qin, Lights Shi et al.** · 2026-08-19

<details>
<summary>Abstract</summary>

Streaming text-to-speech is essential for low-latency spoken dialogue systems, yet many systems wait for sentence-level text and are therefore only pseudo-streaming. True token-level synthesis must generate speech from uncertain prefixes while maintaining perceptual continuity over an unbounded stream with bounded context. We present X2Streaming-TTS, a causal TTS framework that consumes asynchronously arriving text tokens and emits speech without accessing future input. To handle uncertain prefixes, we introduce causal commitment, which keeps ambiguous expressions provisional through uncertainty-aware buffering and performs capacity-adaptive, punctuation-aware segmentation. To preserve acoustic continuity, we further introduce causal speech-state inheritance, which carries the complete Code2Wav state and selected historical Talker states across segment boundaries. Together with an attention prior constraint, it blocks access to future positions while retaining bounded acoustic context. Experiments show that X2Streaming-TTS outperforms existing pseudo-streaming models on most subjective and objective metrics. Further analysis shows that causal commitment stabilizes online segmentation and reduces failures caused by insufficient context, while speech-state inheritance improves boundary continuity without degrading naturalness or speaker identity. X2Streaming-TTS thus achieves strict token-level synthesis with quality comparable to the evaluated offline baselines, a median time to first audio token (TTFT) of 15.8 ms for a single request, and a median TTFT of 260.8 ms at 128 concurrent requests. Our implementation is publicly available at https://github.com/X-Square-Robot/X2Streaming-TTS .

</details>

#### [Aslema at NADI 2026: Augmentation through Fewshot for SLU](https://arxiv.org/abs/2608.18689) · [📄 Read](papers/2026/2608.18689.md)

**Tajwaar Shafiq, Hunzalah Hassan Bhatti, Shammur Absar Chowdhury, Firoj Alam** · 2026-08-19

<details>
<summary>Abstract</summary>

We present Aslema, our system for NADI 2026 Shared Task 5, which consists of two subtasks: intent recognition and slot filling. We evaluate four omni LLMs in a zero-shot setting and compare them with fine-tuned models. Our results show that fine-tuning consistently outperforms zero-shot inference. We further explore synthetic data augmentation by using an LLM to generate culturally grounded Tunisian Derja utterances, followed by voice cloning to generate synthetic speech. Incorporating this synthetic data improves performance on both tasks. Our final submitted system, based on Qwen3-Omni-30B and trained with a mixture of original and synthetic data, achieves 86.8% intent accuracy and 34.7 WER on the devtest split. On the official test set it ranks 1st in slot filling (59.5 CoER) and 4th among 8 teams in intent recognition (66.1% accuracy). We release our experimental scripts and will soon share the synthetic dataset to support further research in this area.

</details>

#### [FireRedTTS3: Unified Speech Generation and Editing with Semantically Enriched Speech Representations](https://arxiv.org/abs/2608.17492) · [📄 Read](papers/2026/2608.17492.md)

**Feiyu Shen, Kun Xie, Yichen Wu, Ziqi Dai et al.** · 2026-08-18

<details>
<summary>Abstract</summary>

Recent continuous autoregressive TTS models operate directly on continuous speech representations, preserving rich acoustic details while leveraging the instruction-following capabilities of text LLMs. This paradigm opens new possibilities for voice cloning, instruction-controlled voice design, and speech editing, but remains susceptible to error accumulation during autoregressive generation. Existing solutions often require additional semantic modules, multi-stage tokenizer training pipelines, or complex autoregressive architectures. In this work, we propose FireRedTTS3, a simple yet effective speech generation and editing framework that mitigates error accumulation at the representation level. Specifically, we leverage a frozen Audio Encoder trained on diverse speech understanding tasks as a semantic teacher to regularize the audio feature space. This improves text-speech alignment and stabilizes autoregressive generation while keeping the overall system simple. FireRedTTS3 provides two variants: FireRedTTS3-Base for multilingual and multi-dialect zero-shot voice cloning, and FireRedTTS3-Instruct for unified voice cloning, instruction-controlled voice design, and speech editing. Experiments show that FireRedTTS3-Base achieves the best average speech intelligibility and speaker similarity among compared systems on Seed-TTS-Eval and MiniMax-MLS-Test, while FireRedTTS3-Instruct outperforms competing systems on InstructTTSEval and Ming-Freeform-Audio-Edit. These results demonstrate that semantically enriched continuous speech representations, combined with a simple architecture, enable stable, controllable, and high-fidelity speech generation and editing. Code and models are available at https://github.com/FireRedTeam/FireRedTTS3.

</details>

#### [Speaker-Normalized Semantic Speech Tokens via Iterative S2U-T2U Refinement](https://arxiv.org/abs/2608.16235) · [📄 Read](papers/2026/2608.16235.md)

**Hanlin Zhang, Daxin Tan, Dehua Tao, Chengxi Deng et al.** · 2026-08-17

<details>
<summary>Abstract</summary>

Semantic speech tokens should preserve linguistic content while suppressing speaker- and duration-dependent variation inherited from acoustic inputs. We propose Iterative Semantic Token Purification (ISTP), an alternating speech-to-unit (S2U) and text-to-unit (T2U) training procedure guided by text predictability. Starting from an initial S2U tokenizer, each iteration trains a T2U model on its deduplicated token sequences. The decoded T2U predictions then serve as connectionist temporal classification targets for a newly initialized S2U model, whose outputs supervise the next T2U model. This cycle progressively aligns the two token generators and biases the token space toward information recoverable from text. Experiments on Mandarin and English show substantially improved S2U--T2U agreement. Independently trained de-tokenizers further show that the refined S2U and T2U tokens retain sufficient content for high-intelligibility voice conversion and text-to-speech synthesis. In voice conversion, the generated speaking rate follows the reference more closely. The refined tokens also exhibit substantially improved cross-speaker consistency and reduced probe-recoverable speaker information.

</details>

#### [DuplexGen: Decoupling Content, Timing, and Acoustics for Synthetic Dialogue Speech](https://arxiv.org/abs/2608.16053) · [📄 Read](papers/2026/2608.16053.md)

**Pengcheng Wang, Sheng Li, Jiyi Li, Takahiro Shinozaki** · 2026-08-17

<details>
<summary>Abstract</summary>

Synthetic conversational speech has become an important resource for developing and evaluating conversational speech systems. However, existing dialogue synthesis pipelines typically generate dialogue content first and then insert interruptions, overlap, and backchannels using handcrafted markers or timing rules, making conversational timing prescribed rather than interaction-driven. We present DuplexGen, a dialogue synthesis framework that explicitly decouples content, timing, and acoustics. An LLM first generates the dialogue script, and then two full-duplex conversational models perform the script while listening to each other in real time. This allows conversational timing to emerge naturally while preserving the scripted content. Finally, a high-fidelity text-to-speech model re-renders the interaction without altering its timing. As a demonstration of the proposed framework, we construct a patient--clinician conversational speech corpus with construction-time annotations, including word timestamps, speaker activity, overlap regions, and interaction events. Experimental results show that the proposed framework produces conversational dynamics closer to real dialogue than conventional stitching-based synthesis.

</details>

#### [Iterative Self-Learning for Expressive Text-to-Speech Synthesis](https://arxiv.org/abs/2608.15910) · [📄 Read](papers/2026/2608.15910.md)

**Nicholas Sanders, Gustav Eje Henter, Simon King, Korin Richmond** · 2026-08-16

<details>
<summary>Abstract</summary>

Expressive text-to-speech (TTS) systems that use explicit conditioning labels provide direct and interpretable control over expressive attributes, in contrast to reference-based or prompting-based approaches, but require labeled data. Obtaining these labels at scale is costly and time-consuming, yet no prior semi-supervised framework addresses this specific bottleneck. Existing semi-supervised TTS methods instead target scarcity of paired speech-text data or transcriptions. To address the scarcity of expressive labels, we propose an Iterative Self-Learning (ISL) framework for expressive TTS, built on Invert-Classify, a classifier-free method that recovers discrete expressive labels by inverting a frozen generative model. The framework iteratively pseudo-labels unlabeled speech using the current model, retrains on the combined labeled and pseudo-labeled data, and repeats, progressively refining label quality and synthesis. We validate on two expressive tasks, word-level prominence and utterance-level emotion, across multiple low-resource data splits. We find that iterative refinement can improve pseudo-label accuracy over single-pass baselines. Furthermore, we observe that these improvements in pseudo-labeling of expressivity translate to gains in expressive label adherence and synthesis quality, confirmed by objective metrics and human listening tests. In the most data-scarce conditions, ISL-trained models outperform single-pass pseudo-labeling and further approach fully supervised performance, demonstrating that gradient-based ISL is an effective solution to expressive label scarcity in low-resource TTS.

</details>

#### [Adding Voice Cloning to Text-to-Audio-Video Models with a Single Zero-Initialised Layer](https://arxiv.org/abs/2608.15690) · [📄 Read](papers/2026/2608.15690.md)

**Ivan Mikheev, Viacheslav Vasilev, Anna Dmitrienko, Alexey Letunovskiy et al.** · 2026-08-16

<details>
<summary>Abstract</summary>

Text-to-audio-video (T2AV) generation models produce a video and its soundtrack from a textual description, but offer no control over whose voice speaks in the output. We show that a base T2AV model can be turned into a voice-cloning model by adding a single zero-initialized linear layer on top of its audio backbone, fine-tuning for a comparatively short training schedule, and conditioning on a short reference recording at inference time. The reference is injected through two complementary signals: its diffusion latents are prepended to the audio stream, and a global speaker embedding modulates token of the target audio. On a benchmark of 674 speaker-text pairs spanning 30 speakers we compare against five strong voice-cloning text-to-speech baselines: our enhanced 5B model attains the highest speaker-encoder cosine similarity (SECS) across three independent verification networks (ECAPA-TDNN, WavLM-SV, Resemblyzer), statistically significantly outperforming every baseline. A side product of the architecture is that the audio path can be evaluated without the video path at inference time, yielding a ~30x speed-up over the full audio-video diffusion loop while preserving the voice-cloning behaviour.

</details>

#### [A survey of AI-generated voices and their detection](https://arxiv.org/abs/2608.15411) · [📄 Read](papers/2026/2608.15411.md)

**Chengzhe Sun, Tianle Yang, Siwei Lyu** · 2026-08-15

<details>
<summary>Abstract</summary>

The ability of artificial intelligence (AI) models to generate highly realistic human voices has advanced rapidly. These technologies power accessibility tools, virtual assistants and creative applications, but they also enable harmful uses, including impersonation, fraud and disinformation. Recent incidents of voice cloning scams targeting businesses and political leaders underscore the urgent need for robust safeguards. Unlike image and video deepfakes, the detection of synthetic voices poses unique challenges due to the complexity of phonetics, prosody and auditory perception. This survey offers a comprehensive overview of AI voice generation and detection methods, encompassing both the technical foundations and the latest state-of-the-art advances. This study also identifies key open challenges, benchmark resources and future directions to make this survey useful for future researchers.

</details>

#### [Content Based Video Narration of Gameplay with Vision Language Models](https://arxiv.org/abs/2608.14016) · [📄 Read](papers/2026/2608.14016.md)

**Mathew Varghese** · 2026-08-14

<details>
<summary>Abstract</summary>

Live game commentary is scarce: it exists for professional esports broadcasts and almost nowhere else. We present a content-based video narration system that produces spoken, esports-style commentary for arbitrary gameplay recordings using a general-purpose vision-language model (VLM) and a text-to-speech back end, with no game-specific instrumentation, no engine telemetry, and no task-specific training. Three mechanisms carry the system. Temporal mosaic packing arranges nine uniformly sampled frames into a single 3x3 image, letting an image-native VLM reason about motion while consuming one image payload per segment instead of nine. Context-conditioned prompting replays the K most recent narrations as assistant-role history, suppressing the repetition that dominates per-segment captioning of static scenes. Duration-conditioned generation and elastic alignment constrain narration length in the prompt, then time-scale or symmetrically pad the synthesized audio so each utterance fills its segment slot exactly, giving frame-accurate muxing without a forced aligner. The implementation supports either cloud TTS or a 6-bit quantized 4B-parameter on-device TTS model on Apple silicon, making the speech stage fully local. We report a qualitative case study on real-time strategy footage, a cost model showing the mosaic reduces per-minute image payloads by 9x, and a candid account of observed failure modes - hallucinated game state, resolution loss from mosaicking, and prosody artifacts from time-scaling. We release the system as a reproducible baseline, with an evaluation protocol for the quantitative study a full version will report.

</details>

#### [S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling](https://arxiv.org/abs/2608.14029) · [📄 Read](papers/2026/2608.14029.md)

**Xueqi Wang, Zhigang Wang, Runqing Zhang, Zhenqi Jia et al.** · 2026-08-14

<details>
<summary>Abstract</summary>

Multimodal dialogue retrieval aims to retrieve dialogues from multimodal dialogue banks that are similar to a target dialogue in terms of both textual semantics and acoustic conversational styles. Such dialogue-level retrieval is crucial for many dialogue-related tasks, including Emotion Recognition in Conversation, Spoken Dialogue Systems, and Conversational Speech Synthesis, where external dialogue examples can provide valuable semantic and stylistic references. However, existing retrieval methods are still largely limited to utterance-level or unimodal matching, and often fail to capture the global semantic coherence and stylistic consistency of an entire dialogue. To address this gap, we propose S2Dialog, a unified framework for dialogue-level semantic-style retrieval from multimodal dialogue banks. Specifically, S2Dialog consists of a Dialogue-level Textual Retriever and a Dialogue-level Acoustic Retriever, which encode the textual and acoustic modalities of a dialogue into dialogue-level representations, respectively. To further enhance multimodal retrieval, we introduce Dialogue-level Textual-Acoustic Contrastive Learning, which aligns semantically and stylistically similar dialogues while distinguishing unrelated ones. Extensive experiments on the multimodal dialogue dataset DailyTalk demonstrate that S2Dialog achieves outstanding retrieval performance.

</details>

#### [FastThaiG2P: Lightning-fast Thai Grapheme-to-phoneme Conversion for Voice Agent Pipelines](https://arxiv.org/abs/2608.12814) · [📄 Read](papers/2026/2608.12814.md)

**Charin Polpanumas** · 2026-08-13

<details>
<summary>Abstract</summary>

FastThaiG2P provides sub-millisecond Thai grapheme-to-phoneme conversion for text-to-speech pipelines (International Phonetic Alphabet and Kokoro-TTS conventions) using a PyThaiNLP-tokenized, extensible dictionary and normalization rules for common Central Thai speech. The approach achieves an average latency of 0.15 ms per utterance on a benchmark of 27,242 synthetically generated utterances, of which 30\% is spent on tokenization, 12\% on normalization, and 58\% on out-of-vocabulary fallbacks (0.5\% OOV rate). To demonstrate its effectiveness, we used FastThaiG2P to phonemize Som-TTS, an open dataset containing 20 hours of grapheme-and-audio pairs, then trained an 82M-parameter StyleTTS 2 model based on a Kokoro-TTS recipe. The resulting model vocalizes intelligible Thai speech suitable for prototyping and development at 0.25 real-time factor (4x real-time) with ONNX inference on CPU.

</details>

#### [VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents](https://arxiv.org/abs/2608.13831) · [📄 Read](papers/2026/2608.13831.md)

**Edresson Casanova, Jaehyeon Kim, Mariana Graterol Fuenmayor, Shehzeen Hussain et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Spoken dialogue is a natural form of human--computer interaction, yet most speech language models remain limited to turn-based operation and lack real-time adaptability, such as user barge-in. Recent duplex speech-to-speech and speech-to-text models reduce latency by replacing multi-stage pipelines, but often compromise speech quality because accurate ASR, interruption handling, and high-fidelity synthesis must be optimized jointly. We propose VoiceChat-TTS, a low-latency, continuous, and streamable text-to-speech model for interactive agents. VoiceChat-TTS is driven directly by LLM text-token streams, supports explicit interruption via control tokens, and produces silence when no textual input is available. The model enables always-on, responsive speech generation while preserving modularity and high speech quality, and it supports mid-utterance interruptions without resetting the KV cache.

</details>

#### [MiDashengLM-Gen: Unified Audio Scene Generation via LLM-Driven Autoregressive Flow Matching](https://arxiv.org/abs/2608.11804) · [📄 Read](papers/2026/2608.11804.md)

**Xingwei Sun, Heinrich Dinkel, Gang Li, Jiahao Mei et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Generating coherent audio scenes that simultaneously blend speech, music, and sound effects remains a significant challenge. Current approaches typically rely on a disjointed pipeline where a frozen, decoupled text encoder feeds a separate audio decoder, limiting cross-modal optimization and leading to poor speech intelligibility. To overcome these limitations, we introduce MiDashengLM-Gen, an end-to-end framework that couples a pre-trained Large Language Model (LLM) with per-token conditional flow matching for autoregressive, variable-length mixed-audio scene generation. MiDashengLM-Gen represents a first approach for general text-to-audio generation with one end-to-end trained model. Empirical evaluations demonstrate that MiDashengLM-Gen drastically improves speech intelligibility over existing unified models. On the Seed-TTS benchmark, English Word Error Rate (WER) drops from 12.15% to 2.79%, approaching the performance of dedicated Text-to-Speech (TTS) systems (1.24%). Furthermore, the framework extends effectively to multilingual settings, yielding highly competitive multilingual WERs compared to existing baselines. Lastly, the model maintains competitive mixed-audio generation quality on the MECAT benchmark. Code and checkpoints are available at https://github.com/xiaomi-research/midashenglm-gen and https://huggingface.co/mispeech/midashenglm-gen, and the demo page is available at https://xingws.github.io/midashenglm-gen-demo/.

</details>

#### [Confucius4-TTS: Transcript-Free Cross-Lingual Zero-Shot TTS with a Learnable Speaker Encoder](https://arxiv.org/abs/2608.11650) · [📄 Read](papers/2026/2608.11650.md)

**Huaxuan Wang, Huimin Wang, Ruiyu Zhang, Yingjie Li et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Recent advances in zero-shot text-to-speech (TTS) have substantially improved speech quality and voice cloning fidelity. However, many zero-shot TTS systems still depend on audio prompt transcripts at inference time. This dependency limits cross-lingual voice cloning, since in-the-wild reference audio is often untranscribed. In this technical report, we present Confucius4-TTS, a multilingual zero-shot TTS system that supports 14 languages and performs both intra-lingual and cross-lingual reference cloning without requiring transcripts of audio prompts. Confucius4-TTS follows a two-stage architecture, consisting of text-to-semantic (T2S) and semantic-to-acoustic (S2A) modules. The LLM-based T2S module uses a learnable speaker encoder to extract timbre features from self-supervised speech representations, and the conditional flow-matching S2A module converts the predicted semantic tokens into mel-spectrograms. The same model also supports continuation cloning when a reference transcript is available. Confucius4-TTS is trained on large-scale multilingual speech data. It achieves high intelligibility and speaker similarity on public benchmarks. On the CV3-Eval cross-lingual benchmark, Confucius4-TTS obtains an average WER of 3.73% across six directions. On our internal cross-lingual set, it achieves the best average overall rank in human evaluation among recent open-source and commercial systems. We release code, model checkpoints, and demos at https://github.com/netease-youdao/Confucius4-TTS.

</details>

#### [Luna-TTS Family Technical Report](https://arxiv.org/abs/2608.11593) · [📄 Read](papers/2026/2608.11593.md)

**Feng Yin, Shuai Shi, Junjie Zheng, Kechenying Zhou et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Modern text-to-speech (TTS) is dominated by autoregressive (AR) codec language models, whose left-to-right decoding brings latency that grows with utterance length, error accumulation along the committed prefix, and an artificial generation order imposed on the Residual Vector Quantization (RVQ) token grid. We propose Luna-TTS Family, diffusion-language-model-based TTS systems pretrained on 1 million hours of speech across Chinese, English, Japanese, and Korean. The family is built by progressive adaptation of a pretrained AR text LLM, from causal to bidirectional and finally to block-causal attention, and comprises two variants sharing a single tokenizer, data pipeline, and 0.6B backbone lineage. Luna-TTS is fully non-autoregressive: it generates the entire RVQ token grid in a fixed number of parallel refinement steps, with zero-shot voice cloning and speech editing arising natively as infilling. Luna-TTS Realtime, derived by continual training, is autoregressive over blocks of 32 codec frames (1.28s) while denoising each block in parallel; it supports KV-cached blockwise generation and incremental audio delivery, achieving an end-to-end RTF of 0.0240 and 41.6 ms local first-block latency under the warmed serving protocol. An annealed fine-tuning stage adds explicit control over emotion and non-verbal vocalizations (NVVs), and a reinforcement-learning stage applies GRPO with policy ratios computed over the realized denoising trajectory. On Seed-TTS-Eval, Luna-TTS achieves the best results on all four metrics among compared open-source and commercial systems (0.73 CER / 79.7 SIM on test-zh, 1.49 WER / 76.8 SIM on test-en); on the harder in-the-wild CV3-Eval, it posts the lowest Mandarin and English error rates in our comparison. Against leading commercial systems, it achieves the best results on most objective, model-based, and human-rated metrics for NVV and emotion control.

</details>

#### [CookVoice: Unified Framework for Style Controllable Multi-Modal Human Voice Generation](https://arxiv.org/abs/2608.11590) · [📄 Read](papers/2026/2608.11590.md)

**Haowei Lou, Hye-Young Paik, Dai Jia, Kai Li et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Human voice generation has made rapid progress in speech generation, singing voice generation, voice cloning, and voice editing. However, most existing systems are designed for specific tasks and often rely on task-dependent architectures, control signals, or autoregressive decoding, limiting fine-grained controllability and inference efficiency. In this paper, we propose CookVoice, a unified framework for multimodal, multi-style, and multi-task human voice generation. CookVoice decomposes the human voice into three key factors: content, prosody, and style, enabling both speech and singing voice generation within a unified model. To achieve precise and flexible controllability, we design a flexible alignment strategy that maps text, style, and prosody control signals onto the frame-level of spectrogram. This design allows CookVoice to support a wide range of tasks, including text-to-speech, text-to-singing voice, style-controllable generation, voice mimicry, voice conversion, and voice editing. Experimental results show that CookVoice achieves generation quality comparable to existing Text-to-Speech and text-to-singing voice baselines, while providing stronger style and prosody controllability. Moreover, CookVoice achieves comparable performance to large-scale baselines with only 43.51 million parameters and efficient inference using as few as 4 ODE steps, making it a practical solution for real-world human voice generation applications. Demo page is available at https://haoweilou.github.io/CookVoice/.

</details>

#### [VoiceDesigner: Text-to-Voice Generation and Editing via Unified Diffusion Modeling and Data Augmentation](https://arxiv.org/abs/2608.13613) · [📄 Read](papers/2026/2608.13613.md)

**Jiarui Hai, Karan Thakkar, Ke Chen, Yunyun Wang et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Recent breakthroughs in generative models have made text-to-voice generation (TTV) possible, enabling the synthesis of speech directly from textual voice descriptions. However, existing systems face two key challenges. First, they struggle to generate a diverse range of voices, spanning real-world human speakers and fictional characters. Second, they lack robust and flexible voice editing capabilities, such as voice cloning and the ability to modify attributes like emotion and tone. In this paper, we propose VoiceDesigner, a unified framework for text-to-voice generation and editing that supports diverse and controllable voice design. To tackle the above challenges, we propose solutions from two perspectives. First, we develop a hybrid data pipeline that leverages digital signal processing techniques and speech generation models to construct a diverse voice dataset covering both real-world and fictional voices. Second, we introduce a diffusion transformer with architectural improvements to better handle complex conditioning and enhance multi-task performance, enabling unified voice generation and editing. Through subjective and objective evaluations, VoiceDesigner achieves superior prompt alignment with both voice descriptions and editing instructions, while maintaining competitive perceptual quality and voice usability compared to state-of-the-art TTV models.

</details>

#### [Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions](https://arxiv.org/abs/2608.09930) · [📄 Read](papers/2026/2608.09930.md)

**Oluwanifemi Bamgbose, Simon Rosen, Jash Shah, Lindsay Devon Brin et al.** · 2026-08-10

<details>
<summary>Abstract</summary>

Automated Text-to-Speech (TTS) evaluation methods (Mean Opinion Score (MOS) predictors and Audio Large Language Models (Audio-LLM) judges) are expected to reflect human perception, yet it is unclear how well they capture the distinct aspects of speech that listeners actually perceive. We deconstruct "naturalness" into a linguistically grounded annotation schema spanning 10 distinct perceptual dimensions, and use it to construct the first dimension-level meta-evaluation benchmark for TTS, comprising 860 utterances annotated by trained linguist raters. Results from benchmarking four MOS predictors and four Audio-LLM judges reveal that MOS predictors collapse onto acoustic signal quality, while Audio-LLM judges show selective, prompt-dependent detection that does not generalise across all dimensions. Neither class reliably captures a breadth of linguistically structured speech errors. Our dataset, annotation schema, and evaluation code are publicly released to support more targeted and interpretable TTS evaluation.

</details>

#### [MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection](https://arxiv.org/abs/2608.09593) · [📄 Read](papers/2026/2608.09593.md)

**Yanqiu Li, Yang Xiao, Jisheng Bai, Bin Chen et al.** · 2026-08-10

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis and audio generation have made high-fidelity acoustic forgery low-cost and difficult to attribute, enabling a realistic attack scenario in which speech and background audio are independently manipulated over otherwise authentic video. Yet existing research either focuses on visual manipulation, addresses speech detection in isolation, or conflates speech and non-speech audio as a single undifferentiated audio stream, overlooking the distinct forensic challenges posed by background audio. This conflation is consequential: the two acoustic components arise from fundamentally different generative mechanisms, exhibit distinct artifact profiles, and pose different challenges to detection systems. We introduce MADBench, the first benchmark that treats speech and environmental audio as distinct acoustic components, enabling component-aware evaluation of audio deepfake detection across independently manipulated forgery sources. We benchmark representative state-of-the-art detectors and multimodal large language models under a unified protocol. Our experiments reveal that environmental audio manipulation is more detectable than synthetic speech across general-purpose encoders, while existing pretrained detectors fail on both acoustic components, and manipulated environmental audio asymmetrically degrades speech deepfake detection, findings entirely invisible under the single-label paradigm of prior benchmarks. MADBench establishes a rigorous foundation for future research into robust, component-aware audio deepfake detection.

</details>

#### [CuteTTS: Efficient and High-Quality Speech Synthesis via Autoregressive Modeling of Continuous Latents](https://arxiv.org/abs/2608.08638) · [📄 Read](papers/2026/2608.08638.md)

**Yuqian Zhang, Yao Shi, Kexin Huang, Botian Jiang et al.** · 2026-08-09

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) now supports interactive assistants, personalized media, and accessibility tools. All TTS systems require faithful linguistic rendering, consistent speaker identity, and low-latency response. Yet compact streaming systems must preserve sufficient acoustic detail in a predictable low-rate latent sequence, while iterative diffusion sampling and classifier-free guidance multiply inference cost at every autoregressive step. To strike a balance between high-fidelity synthesis and low-latency inference, we present CuteTTS, a compact continuous-autoregressive TTS system. It combines semantically aligned causal VAE latents with patch-level autoregression, explicit speaker conditioning, and a bidirectional flow-matching head. We further introduce guidance-step distillation, which absorbs classifier-free guidance and multiple solver steps into a single interval-conditioned student. Evaluations on LibriSpeech and Seed-TTS-Eval demonstrate competitive intelligibility and speaker similarity in zero-shot voice cloning, while distillation lowers first-audio latency by 23.3% and real-time factor by 40.8% relative to the base model with comparable objective and subjective quality. These results provide a practical path toward continuous-autoregressive TTS that reconciles high-fidelity generation with the latency demands of real-time interaction.

</details>

#### [CtrlSpeech: Coarse-to-Fine Control for Expressive Speech Synthesis](https://arxiv.org/abs/2608.08362) · [📄 Read](papers/2026/2608.08362.md)

**Zhisheng Zheng, Xiaohang Sun, Zhu Liu, Caren Chen et al.** · 2026-08-08

<details>
<summary>Abstract</summary>

Recent Text-To-Speech (TTS) systems have achieved strong naturalness and zero-shot voice cloning performance, but fine-grained control of expressive speech at the word or phoneme level remains challenging. We propose CtrlSpeech, a controllable, expressive TTS framework with coarse-to-fine control. Built on the DiTAR architecture, CtrlSpeech combines global speaker conditioning with phone-aligned pitch, loudness, and duration signals, enabling localized prosodic control while preserving the target speaker's timbre. This design allows users to adjust expressive attributes at a fine temporal granularity, making speech refinement more flexible and controllable. Experimental results show that CtrlSpeech achieves competitive zero-shot TTS performance and improves controllability over expressive attributes, demonstrating its effectiveness for flexible and practical expressive speech synthesis.

</details>

#### [ReLMCodec: Designing Predictable Speech Tokens from Pre-Quantization Phoneme Structure](https://arxiv.org/abs/2608.08286) · [📄 Read](papers/2026/2608.08286.md)

**Zixiang Wan, Xusheng Yang, Zheng Wang, Peiji Yang** · 2026-08-08

<details>
<summary>Abstract</summary>

Neural speech codecs face a fundamental tension in the language-model era: tokens that support high-fidelity reconstruction are not necessarily easy for autoregressive models to predict. Our controlled analysis of diverse codec and self-supervised speech representations shows that clearer phoneme structure before discrete code assignment is consistently associated with easier autoregressive token prediction. Yet phoneme structure alone is insufficient for high-fidelity reconstruction, which also requires reconstruction-relevant acoustic detail. Guided by this observation, we introduce ReLMCodec, a low-bitrate single-codebook speech codec built upon a preserve--control--refine principle: it preserves the linguistic organization of frozen self-supervised learning (SSL) features at the quantizer input, controls reconstruction-driven drift through Pre-quantization Anchor-Preserving Adaptation (PAPA), and refines the quantized latent space with a training-only WavLM-Large L24 teacher to reduce phoneme-level token fragmentation. Together, these components allow acoustic detail to support waveform reconstruction while keeping the resulting token sequence predictable for autoregressive models. At 650 and 800 bps, ReLMCodec moves the empirical single-stream predictability--reconstruction frontier in our evaluations, with gains that carry over to downstream text-to-speech (TTS) synthesis in both intelligibility and speaker similarity.

</details>

#### [DialectS2S: End-to-End Speech Dialogue Modeling for Low-Resource Chinese Dialects](https://arxiv.org/abs/2608.08067) · [📄 Read](papers/2026/2608.08067.md)

**Yi Shu, Tianyu Peng, Yingzhuo Deng, Wen Yang et al.** · 2026-08-08

<details>
<summary>Abstract</summary>

Current end-to-end speech dialogue models are primarily optimized for mainstream languages and remain limited in low-resource dialect scenarios due to the scarcity of dialect speech data. Moreover, during dialect adaptation, the semantic representation space of speech dialogue models continuously evolves, while conventional speech supervision remains unchanged, leading to semantic inconsistency between hidden representations and speech targets and degrading speech stability and naturalness. To address these issues, we propose DialectS2S, an end-to-end speech dialogue model for Chinese dialects. We first develop a scalable dialect speech dialogue synthesis pipeline for efficient data construction. We further introduce a two-stage post-training strategy with self-aligned speech supervision, which aligns the semantic content of speech supervision with the evolved semantic representations of the model to improve dialect speech generation quality. Experimental results show that DialectS2S consistently outperforms existing baselines across multiple Chinese dialects in speech dialogue, achieving substantial improvements in dialect consistency, response quality, and speech intelligibility. Our work provides an efficient and scalable solution for end-to-end speech dialogue modeling in low-resource dialect scenarios. To facilitate future research and practical applications, we fully open-source the DialectS2S framework, including model checkpoints, training datasets, and fine-tuning code.

</details>

#### [SemBridge: Semantic Token Anchoring for Continuous-Latent Autoregressive Speech Generation](https://arxiv.org/abs/2608.07462) · [📄 Read](papers/2026/2608.07462.md)

**Hanke Xie, Haopeng Lin, Jiale Qian, Dake Guo et al.** · 2026-08-07

<details>
<summary>Abstract</summary>

Continuous-latent autoregressive speech generation has emerged as a promising alternative to discrete-token modeling by avoiding quantization loss and preserving richer acoustic information. However, continuous acoustic targets do not ex- pose linguistic structure as explicit token-level prediction tar- gets. Consequently, the autoregressive language model (LM) must acquire linguistic structure indirectly through acous- tic prediction, which can compromise the content fidelity of generated speech. We propose SemBridge, a training-only semantic-token anchoring framework for continuous-latent autoregressive speech generation. SemBridge uses discrete se- mantic tokens to directly supervise autoregressive LM states and employs a Semantic-Aligned Acoustic VAE to organize the continuous target space under the same semantic refer- ence. The semantic supervision is used only during train- ing, while inference remains entirely continuous. We evalu- ate SemBridge on zero-shot text-to-speech (TTS) and score- conditioned singing voice synthesis (SVS). Across multi- ple benchmarks, SemBridge improves content accuracy, as measured by word and character error rates (WER/CER), while maintaining competitive speaker similarity and percep- tual quality. Experimental results demonstrate that explicit semantic-token supervision for autoregressive state learning is an effective and general direction for continuous speech generation. Speech samples are available.1 The model code and checkpoints will be available at https://github.com/ASLP- lab/SemBridge

</details>

#### [MMAG: A Multi-Control Mixed Audio Generation Benchmark](https://arxiv.org/abs/2608.06900) · [📄 Read](papers/2026/2608.06900.md)

**Zihao Zheng, Xuenan Xu, Jiahao Mei, Yixuan Li et al.** · 2026-08-07

<details>
<summary>Abstract</summary>

Recent audio generation systems have progressed from single-modality synthesis to generating complex acoustic scenes containing speech, music, and sound effects. Therefore, evaluating these models requires assessing multiple interacting capabilities, including semantic fidelity, speaker consistency, and temporal control, yet existing benchmarks focus on isolated domains or coarse-grained descriptions. To address this gap, we introduce the Multi-control Mixed Audio Generation (MMAG) benchmark. MMAG contains approximately 4,000 manually verified audio clips with rich annotations covering speech content, speaker identity, music attributes, sound events, and temporal relationships, together with dedicated subsets for voice cloning and timestamp-conditioned generation. We further propose a systematic evaluation protocol that measures acoustic fidelity, speech quality, semantic alignment, and temporal accuracy. Benchmarking representative agentic orchestrators, unified audio-visual generation models, and native mixed-audio generators reveals substantial performance trade-offs across these capabilities, with no existing model performing consistently well. Our results highlight the remaining challenges of controllable mixed audio generation and establish MMAG as a comprehensive benchmark for future research.

</details>

#### [AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks](https://arxiv.org/abs/2608.05507) · [📄 Read](papers/2026/2608.05507.md)

**Aurosweta Mahapatra, Xiutian Zhao, Shreeram Suresh Chandra, Zihan Zhang et al.** · 2026-08-06

<details>
<summary>Abstract</summary>

Speech deepfake detection (SDD) systems achieve strong performance on conventional benchmarks; however, existing datasets provide limited coverage of emotionally expressive and recent large audio-language model (LALM)-based attacks. Existing emotional spoofing datasets are also limited in scale and attack diversity, typically covering only voice conversion (VC) or text-to-speech (TTS) attacks. We introduce AffectDF, the most comprehensive benchmark for emotionally expressive speech deepfakes, spanning TTS, VC, emotional VC, and LALM-based spoofing attacks across both acted and spontaneous emotional speech. AffectDF contains approximately 260 hours of speech generated using 21 spoofing attacks across five emotional states. We benchmark state-of-the-art SDD systems under conventional and emotional spoofing conditions, including LALM-based detectors evaluated with both inference-only prompting and supervised fine-tuning. Our experiments reveal severe robustness degradation when models trained on conventional benchmarks are evaluated on AffectDF, with several systems approaching near-random performance. Surprisingly, even large-scale emotional training does not consistently improve cross-domain robustness, indicating that current SDD systems fail to learn generalized spoof representations under emotional and prosodic variability. Robustness further varies substantially across emotional states, attack families, and acted vs spontaneous emotional speech conditions. These findings expose fundamental limitations of current SDD systems and establish AffectDF as a benchmark for developing more robust spoof detection models.

</details>

#### [LILAC: An Idempotent Neural Speech Codec](https://arxiv.org/abs/2608.05727) · [📄 Read](papers/2026/2608.05727.md)

**June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon** · 2026-08-06

<details>
<summary>Abstract</summary>

Neural Audio Codecs are widely adopted in speech generation and editing. However, existing neural audio codecs are not idempotent: across the paper's twelve baseline systems, every configuration tested rewrites, on average, at least 15% of its tokens in a single decode-re-encode pass. This poses a problem for utilizing Neural Audio Codecs as token interfaces in pipelines where re-encoding decoded outputs can occur. We present LILAC, a fully convolutional 24 kHz speech codec at 9.375 Hz and 0.75 kbit/s that is codec idempotent by construction; re-encoding the decoded audio of any valid token stream returns the identical stream. LILAC achieves idempotency while maintaining competitive quality, reaching UTMOS 4.14 and 4.24 on LibriSpeech and LibriTTS-R test sets, comparable to SOTA sub-1 kbit/s Neural Audio Codecs.

</details>

</details>
<!-- PAPERS_TABLE_END -->
