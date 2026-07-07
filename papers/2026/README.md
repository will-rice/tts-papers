# 2026

390 papers in this year.

### [ProPS: Prompted Profile Synthesis for Natural Language-Conditioned Speaker Embedding Distributions](2607.05276.md)
**Thomas Thebaud, Junhyeok Lee, Laureano Moro-Velazquez, Jesus Villalba Lopez et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

Speaker embeddings, or x-vectors, are widely used to represent speaker identity and speaker-related attributes, but existing embedding extractors are typically descriptive rather than generative: they map an observed speech segment to an x-vector, which is then used for downstream applications. We introduce ProPS, Prompted Profile Synthesis, a framework for generating distributions of speaker embeddings conditioned on natural language prompts such as "a thirties male speaker with an Indian accent". ProPS converts human-written profile descriptions into sentence embeddings and uses a mixture density network trained on a large-scale dataset to predict a Gaussian mixture model in the x-vector space. The model is trained by maximizing the likelihood that real speaker embeddings match the requested profile, and its generated distributions are evaluated by negative log-likelihood on held-out x-vectors and by attribute classification accuracies on sampled synthetic x-vectors. Experiments show that ProPS produces profile-conditioned distributions and generates x-vectors that preserve requested speaker attributes such as age, gender, accent, and prosodic characteristics. This design enables controllable speaker-profile synthesis for speech generation systems like Text-To-Speech (TTS) or Voice Conversion (VC) while anchoring generated distributions in observed speaker-embedding structure.

</details>

### [Streaming Neural Speech Codecs through Time-Invariant Representations](2607.05250.md)
**Kélian Estève, Salima Mhdaffar, Mickael Rouvier, Richard Dufour et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

Neural speech codecs are increasingly used as intermediate representations in codec-based speech generation systems. TiCodec introduces a factorized representation that separates time-varying speech content from time-invariant information through a Time-Invariant Representation Extraction (TIRE) module, potentially reducing the amount of information that must be modeled at the frame-level. In this work, we investigate the nature of the information captured by TIRE representations and their suitability for low-latency speech processing. Using a series of probing tasks, we analyze the influence of the encoder layer and show that intermediate layers capture complementary speaker- and environment-related information while containing little linguistic content. We further study several segment selection strategies for TIRE training and demonstrate that cross-file sampling improves the robustness of invariant representations. Based on these findings, we propose Dual-TIRE, a multi-level architecture that exploits the complementarity of different encoder layers and improves speech reconstruction quality and speaker similarity. Finally, we evaluate TiCodec in a streaming inference setting using successive 660ms processing blocks. Results show that streaming operation can be achieved without significant degradation in reconstruction performance, highlighting the potential of factorized neural codec representations for future low-latency speech generation systems.

</details>

### [Towards Digital Preservation of Efik: TTS for a Low-Resource African Language](2607.04515.md)
**Offiong Bassey Edet, Emmanuel Oyo-Ita, Archibong Okon Archibong, David Effanga Bassey et al.** · 2026-07-05

<details>
<summary>Abstract</summary>

Efik, a tonal language spoken by about 3 million second language speakers and 1.5 million native speakers in Southeastern Nigeria, remains underrepresented in speech synthesis research. We present the first documented end-to-end text-to-speech study for Efik, introducing a curated single speaker corpus of 2,632 utterances totaling three hours and a comparative evaluation of four neural models (VITS, MMS-TTS, SpeechT5, and Orpheus-TTS) under low resource conditions. Native speakers evaluated the systems using MOS, Nat-MOS, and A-MOS. MMS-TTS achieved the highest MOS of 3.80 +/- 0.63 and produced more stable long form speech, though tonal errors persisted. Other models showed greater tonal and prosodic inconsistencies. These results provide a reproducible baseline and highlight the need for larger corpora and tone aware modeling for tonal African languages.

</details>

### [DELTA-TTS: Adapting Autoregressive Model into Diffusion Language Model for Text-to-Speech](2607.04140.md)
**Junwon Moon, Seungbeom Kim, Yejin Lee, Hoseong Ahn et al.** · 2026-07-05

<details>
<summary>Abstract</summary>

Autoregressive (AR) text-to-speech (TTS) models generate discrete speech tokens sequentially, which makes inference slow and can degrade robustness by propagating local errors and hallucinations. This limitation stems from their left-to-right AR commitment: each token must be determined before future speech-token context is available. However, such ordering is not an inherent requirement for TTS, as the full input text is available before synthesis. In this paper, we introduce DELTA-TTS, a lightweight LoRA-based adaptation framework that converts a pretrained AR TTS model into a discrete diffusion language model (dLLM) for confidence-ordered speech-token decoding. To better capture the local structure of speech, DELTA-TTS incorporates a convolution module that injects local acoustic context, together with a $1/t$-weighted training objective and a time-shifted inference schedule that defer low-confidence positions to later steps. Trained on only $585$ hours of LibriTTS, DELTA-TTS achieves a $\textbf{1.75}\%$ WER on Seed-TTS test-en, outperforming its AR backbone while generating tokens $\textbf{3.3}\times$ faster. Further analysis shows that DELTA-TTS produces sharper text--speech alignment, increases overall decoding confidence, and mitigates hallucinations observed in AR generation.

</details>

### [TRACE-EVC: Text-Guided Relative Affective Control for Zero-Shot Emotional Voice Conversion](2607.03666.md)
**Zihan Zhang, Shreeram Suresh Chandra, Zongyang Du, Xiutian Zhao et al.** · 2026-07-04

<details>
<summary>Abstract</summary>

Traditional emotional voice conversion (EVC) conditions generation on explicit target emotions like labels or references, defining the target affective state but omitting the direction or nature of the transition. We introduce instruction-guided relative emotional voice conversion, a task where natural-language instructions specify source-conditioned affective transformations (e.g., "make the speech slightly calmer" or "sound noticeably more confident") instead of fixed targets. To support this task, we construct TRACE-Instruct, a dataset of relative emotion instructions covering categorical transitions, intensity modifications, and open-ended affective changes. We propose TRACE-EVC, a zero-shot framework built around Emo-Compass, a module that models each conversion as a source-anchored rectified flow. Rather than conditioning on an explicit target, it predicts the direction and degree of the affective change. Experiments demonstrate that TRACE-EVC accurately follows relative emotion instructions while preserving speaker identity, linguistic content, and speech quality, and remains competitive with conventional EVC systems on standard categorical emotion conversion.

</details>

### [VisionAId: An Offline-First Multimodal Android Assistant for People with Visual Impairment, Featuring Personalized Object Retrieval](2607.02371.md)
**Cristian-Gabriel Florea, Stelian Spînu** · 2026-07-02

<details>
<summary>Abstract</summary>

Over 285 million people worldwide live with a visual impairment, for whom everyday tasks such as avoiding obstacles, locating personal belongings, recognizing familiar faces, or handling cash remain persistent obstacles to personal autonomy. Existing assistive applications are typically limited to recognizing predefined categories, depend heavily on cloud connectivity, or require dedicated hardware. We present VisionAId, an Android application that turns a commodity smartphone into a real-time visual assistant. The system integrates six on-device deep learning models (metric monocular depth estimation, instance segmentation, visual and facial embeddings, face detection, and a custom banknote detector) running entirely through ONNX Runtime, with an optional cloud large language model (Google Gemini Flash) used only for narrative scene description and automatic object labeling. A distinctive contribution is a few-shot pipeline for personal objects: the user photographs an object from several angles, and the system later locates that specific instance in the environment, guiding the user toward it with augmented-reality markers, spatial audio, and distance-proportional haptics. All feedback is multimodal (Romanian speech synthesis, voice commands, vibration). On a reference device (Samsung Galaxy S21 Ultra), INT8 quantization reduces depth latency from ~1200 ms to ~491 ms, the custom banknote detector reaches an mAP@50 of 0.986, and metric depth is calibrated to below 1 cm of error within 3 m.

</details>

### [LuxSQA: Ask Me in Luxembourgish with TTS-Augmented Spoken Question Answering](2607.02763.md)
**Nina Hosseini-Kivanani, Marco Matassoni, Alessio Brutti** · 2026-07-02

<details>
<summary>Abstract</summary>

Spoken Question Answering (SQA) remains largely focused on high-resource languages and carefully recorded speech, limiting the reach of speech-LLM methods in low-resource settings. This paper investigates whether text-to-speech (TTS) can provide task-specific training data for Luxembourgish SQA without requiring a large human-recorded QA corpus. Starting from existing text-based QA resources, we translate questions into Luxembourgish, synthesize spoken questions with multiple TTS systems, and pair them with textual answers. We train a parameter-efficient SLAM-style architecture that connects a frozen Whisper encoder to frozen multilingual LLM backends through a learned projector and LoRA adapters. We compare MMS-TTS, Qwen3-TTS, and OmniVoice variants, including single-source corpora of about 48k questions and a 4TTS multi-source mix of approximately 230k questions. Evaluation on LLAMA-LB-Test with two real Luxembourgish speaker conditions shows that multi-source and voice-design-based synthetic training configurations yield the strongest SQA performance. The results also show that no-reference TTS quality scores do not monotonically predict downstream QA performance, indicating that synthetic speech must be evaluated as task-specific training data rather than only as natural-sounding audio.

</details>

### [GRAFT: Grafted Reference Audio for Fine-grained Pronunciation in Zero-shot Text-to-Speech](2607.02633.md)
**Antonis Asonitis, Francesco Verdini, Aref Farhadipour, Vijeta Avijeet et al.** · 2026-07-02

<details>
<summary>Abstract</summary>

We present GRAFT, a per-word pronunciation conditioning mechanism for text-to-speech neural codec language modeling. Existing systems reach high intelligibility and naturalness but inherit the ambiguity of text and mispronounce rare proper nouns, loanwords and technical terms. Even phoneme-conditioned models offer no direct acoustic handle for per-word pronunciation. GRAFT controls the pronunciation of a chosen word from a short spoken sample of it, encoded with the model's own speech tokenizer and bound to the word's position in the prompt. Voice conversion during training-data construction disentangles the hint speaker from the target speaker, so the hint may come from any voice while the output stays in the target voice. In a blind English listening study, human raters rank GRAFT first by a clear margin, judging its rendering of the difficult word closest to a reference recording of that word. On a five-language objective benchmark, GRAFT reduces target-word phoneme error rate by 22-39% over the identical text-only backbone and outperforms competitive open-source zero-shot systems, both phoneme- and text-conditioned, on target-word pronunciation, while preserving speaker similarity and naturalness.

</details>

### [A Geometric Perspective on Composable Emotion Steering in Text-to-Speech Models](2607.00946.md)
**Siyi Wang, James Bailey, Ting Dang** · 2026-07-01

<details>
<summary>Abstract</summary>

While prior work has explored emotion control in hybrid text-to-speech systems, the geometric properties of these modules, and their implications for steerability, remain poorly understood. We present the first comparative study of speech language model (SLM) and conditional flow-matching (CFM) modules as activation steering sites for mixed emotion speech synthesis. We first characterize emotion representations using linear probing and local intrinsic dimensionality (LID), and then evaluate single-site and joint steering for mixed-emotion synthesis. Our results show that SLM offers a clean, low-dimensional emotion-specific subspace with strong speaker--emotion disentanglement, while CFM exhibitspoor cross-speaker generalization due to speaker--emotion entanglement. Joint steering increases emotion intensity but degrades proportional control and speech quality on in-distribution data. These findings provide practical guidance for multi-site activation steering in hybrid TTS systems and highlight the importance of representation geometry in controllable speech generation.

</details>

### [Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis](2607.00363.md)
**Zuda Yu, Qianhui Xu, Ting Chen, Junhui Zhang et al.** · 2026-07-01

<details>
<summary>Abstract</summary>

Flow Matching (FM) has emerged as a powerful paradigm for speech generation but remains constrained by high inference latency and timbre leakage. To address these bottlenecks, we propose a unified guidance framework that enhances generation efficiency and robustness through two complementary strategies. On the data front, we introduce Data-guidance via heterogeneous augmentation, encouraging the model to disentangle linguistic content from acoustic residue. In parallel, we propose an enhanced Model-guidance mechanism that synergizes trajectory rectification with a novel intrinsic guidance objective. This approach distills conditional knowledge into network weights and straightens inference trajectory path, thereby eliminating Classifier-Free Guidance (CFG) overhead. Experiments demonstrate that our framework accelerates inference by nearly three times while effectively improving speaker similarity compared to state-of-the-art baselines.

</details>

### [LuxEmo: Expressive Text-to-Speech Corpus for Luxembourgish](2606.31947.md)
**Nina Hosseini-Kivanani, Sandipana Dowerah** · 2026-06-30

<details>
<summary>Abstract</summary>

State-of-the-art speech datasets predominantly focus on widely spoken languages, often overlooking low-resource languages such as Luxembourgish, which remain underrepresented in speech technology research. In this work, we introduce LuxEmo, a 21-hour conversational expressive speech corpus for Luxembourgish with 4 emotion categories. LuxEmo is derived from Radio Télévision Luxembourg (RTL) youth broadcasts, using automated detection followed by human validation. We propose a semi-automatic curation workflow combining voice activity detection, denoising, language identification, LuxASR-based segmentation, automatic emotion prediction, lexical cues, and targeted human review. Additionally, we benchmark five expressive TTS systems covering German-based cross-lingual transfer, multilingual Luxembourgish support, Luxembourgish adaptation, and non-parametric prosody transfer. Performance is evaluated using both objective metrics and human evaluation.

</details>

### [Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation](2606.31729.md)
**Dominika Woszczyk, Andreas Triantafyllopoulos, Jura Miniota, Éva Székely et al.** · 2026-06-30

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) evaluation is an open challenge. While the primary target was "naturalness," recent fidelity gains shifted focus toward "appropriateness" and whether speech is correct for its context. In this work, we examine how perception changes when the expected downstream use varies. We measure the appropriateness and human-likeness of five SOTA TTS systems across five domains: AI assistant, reader, actor, animated character, and spontaneous speaker. Results show appropriateness varies across domains independently of naturalness. While systems shine at reading, expressive domains remain challenging, and optimizing for one can degrade others. Furthermore, naturalness scores tend to penalize stylized speech while rewarding spontaneity. Finally, our study also highlights blind spots in one-size-fits-all evaluation metrics across more expressive domains. We demonstrate that TTS performance is not "solved" but depends on the target domain, requiring context-aware evaluation.

</details>

### [Beyond Cross-Reconstruction: Probing-Based Disentanglement Evaluation for Acoustic Teleportation Codecs](2606.31365.md)
**Philipp Grundhuber, Emanuël A. P. Habets** · 2026-06-30

<details>
<summary>Abstract</summary>

Some neural audio codecs disentangle speech into latent subspaces encoding content, speaker identity, and acoustics, enabling acoustic teleportation and voice conversion. Existing evaluations rely on cross-reconstruction quality, which cannot reliably detect leakage across partitions. We extend a probing based framework to assess disentanglement by regressing room-acoustic parameters (reverberation time, clarity, and direct-to-reverberant ratio) and classifying speaker identity, using the gap between intended and unintended partitions as the disentanglement measure. Applied to an acoustic teleportation codec, we find speaker identity is largely confined to its partition, while acoustics leak into the speech embeddings due to the training objective. Acoustic embeddings blindly estimate room parameters within 0.02 s of supervised baselines, indicating physically meaningful structure emerges without explicit supervision.

</details>

### [Preserving Speech-to-Text LLM Capabilities in Speech-to-Speech Generation](2606.30944.md)
**Yuxuan Hu, Heng Lu, Ruchao Fan, Yao Qian et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Strong speech-to-text (S2T) LLMs already provide robust speech perception and text reasoning, but adding speech-to-speech (S2S) output is challenging: fine-tuning the backbone can degrade the original S2T performance, while attaching a downstream talker reintroduces a serial text-to-speech bottleneck. We present PRIME-Speech, a frozen-backbone S2S conversion framework that trains only speech-generation modules. PRIME-Speech synchronizes a causal audio post-decoder with intermediate hidden states of the frozen backbone, so codec tokens are generated from the model's evolving reasoning trajectory rather than from completed text chunks. The post-decoder uses mixed hidden-state, text, and audio-history conditioning, and a training-time packing strategy with turn-level audio KV-cache and position reset stabilizes multi-turn spoken interaction without additional multi-turn S2S training data. Multi-token prediction further reduces the effective codec prediction rate and improves first-audio latency without modifying the reasoning path. Across speech translation, spoken QA, speech understanding, and multi-turn dialogue, PRIME-Speech preserves the S2T behavior of the frozen backbone while producing accurate, low-WER spoken responses.

</details>

### [DialogPII: A multilingual dataset of synthetic dialog transcripts to detect personal information](2606.30312.md)
**Roland Roller, Vera Czehmann, Derya Erman, Luke Flanagan et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Conversational data collected in domains such as healthcare or social sciences is a valuable resource for research and automated analysis. However, responsible data sharing requires the detection and removal of personally identifiable and sensitive information to protect individual privacy. To support the development and evaluation of automatic de-identification systems, we present DialogPII, a multilingual dataset of synthetic dialogs and speech-derived transcripts for personal information detection. DialogPII covers eight interaction scenarios (emergency calls, medical anamnesis interviews, therapy sessions, insurance communication, customer support, clinical interviews regarding an AI-supported dashboard, police reports, and group therapy discussions), 19 entity types, and 11 languages (English, Arabic, Finnish, French, German, Hindi, Italian, Polish, Portuguese, Spanish, and Turkish). Dialogs were generated semi-automatically using large language models, manually curated for plausibility and diversity, and localized to country- and city-specific contexts. All dialogs were additionally converted to speech via text-to-speech synthesis, transcribed with Whisper, and annotated through automatic projection and manual correction, yielding aligned written and speech-derived resources across all languages. We further release baseline multilingual named entity recognition models and provide technical validation through inter-annotator agreement analysis, translation quality evaluation, annotation projection assessment, and benchmark experiments with transformer-based sequence labeling models.

</details>

### [FacePlex: Full-Duplex Joint Speech-Facial Motion Generation for Conversational Avatars](2606.30145.md)
**Habin Lim, Jae-Ho Lee, Hah Min Lew, Ji-Su Kang et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Natural face-to-face conversation requires real-time speech generation together with synchronized facial motion. Existing systems only partially address this problem: speech-only full-duplex models can generate speech in real time but do not produce facial motion, while audio-driven facial motion models animate a face from already available audio rather than jointly generating speech and motion online. To bridge this gap, we first formalize full-duplex joint speech-facial motion generation, where speech tokens and facial motion tokens are produced together every step. Building on this formulation, we propose FacePlex, a unified streaming framework with two key components. First, Rolling Flow Matching adapts flow matching to online motion generation by committing new motion frames at each streaming step. Second, Rolling Cross-Attention couples the streaming audio queue with the motion queue, allowing speech and facial motion to condition each other as generation progresses. Through extensive experiments, ablation studies, and a user study, we show that FacePlex enables full-duplex joint speech-facial motion generation under online streaming constraints, while achieving stronger lip-sync quality and motion fidelity than audio-driven facial motion baselines.

</details>

### [VeRe-Flow: Guiding Flow Matching toward Clean Speech via Velocity Contrastive Regularization and Representation Alignment for Noise-Robust Bandwidth Expansion](2606.29450.md)
**Sujin Koo, Sangyoon Kim, Ji Sub Um, Hoirin Kim** · 2026-06-28

<details>
<summary>Abstract</summary>

Noise-robust bandwidth expansion aims to reconstruct high-fidelity wideband speech from noisy low-resolution inputs. While flow matching has shown strong performance in speech generation, accurately recovering clean speech from noisy inputs remains challenging due to the ambiguity of velocity estimation under noise. In this work, we propose VeRe-Flow, a clean-guided flow matching framework that introduces multi-level clean supervision to guide the generative process toward clean speech. At the velocity level, we introduce velocity contrastive regularization, which attracts the predicted velocity toward the clean trajectory while repelling it from noisy trajectories. At the representation level, we incorporate representation alignment that aligns intermediate features with clean self-supervised learning representations. The results demonstrate that the proposed method achieves the lowest LSD and highest DNSMOS OVRL among all baselines, and the highest MOS among generative baselines.

</details>

### [HPRO: Hierarchical Progressive Reward Optimization via Preference Extraction for Emotional Text-to-Speech](2606.28249.md)
**Sihang Nie, Xiaofen Xing, Rui Xing, Haoming Li et al.** · 2026-06-26

<details>
<summary>Abstract</summary>

Recently, Large Language Model (LLM)-based Text-to-Speech (TTS) models have achieved remarkable naturalness. However, the standard Supervised Fine-Tuning paradigm often converges to statistically averaged prosody, limiting emotional expressiveness. While preference-driven optimization offers a promising alternative, existing approaches suffer from two structural mismatches: information conflict, where content and emotion in a shared latent space produce conflicting gradients, leading to reward hacking and semantic degradation; and scale gap, where sparse sentence-level rewards struggle to guide dense frame-level generation. To overcome these challenges, we propose HPRO, a hierarchical progressive reward optimization framework. Within HPRO, we introduce the HD-Emo codec as a novel differentiable reward model to resolve the information conflict. It extracts speech into distinct content and style preference tokens, structurally isolating emotional optimization from semantic content. Building upon this structured preference space, HPRO bridges the scale gap by progressively aligning frame-, word- and sentence-level objectives. Experiments demonstrate that HPRO significantly enhances emotional expressiveness, while effectively preserving linguistic intelligibility. The code and audio samples are publicly available at https://xxh333.github.io/hpro-demo/.

</details>

### [Closing the Quality Gap in Low-Resource Text-to-Speech: LoRA Fine-Tuning of VoxCPM2 for Khmer and Korean](2606.26618.md)
**Phannet Pov, Sovandara Chhoun, Hyun Woo Park, Wan-Sup Cho et al.** · 2026-06-25

<details>
<summary>Abstract</summary>

Large pretrained text-to-speech (TTS) models sound almost human for well-resourced languages, but much worse for languages that are rare in their training data. We study this quality gap for Khmer and Korean using VoxCPM2, a 2.4B-parameter, tokenizer-free TTS model that joins a MiniCPM-4 language-model backbone with a flow-matching diffusion decoder. We build one shared, language-tagged corpus of about 26 hours and adapt VoxCPM2 with a single Low-Rank Adaptation (LoRA) adapter, trained on both languages at once and added to both the language model and the decoder. The adapter is zero-initialized, so training starts exactly at the original (zero-shot) model. In native-speaker listening tests, the Khmer Mean Opinion Score (MOS) rises from 3.85 to 4.23 with the best adapter (rank 64), a highly significant gain (paired Wilcoxon test, p<0.001), while training only 0.19 to 3.03 percent of the parameters. The automatic loss and the human ratings, however, disagree on the best rank: validation loss is lowest at rank 128, yet MOS peaks at rank 64. The same adapter brings no gain for Korean, a language the base model already handles well, and at a high rank it even degrades quality. Adaptation therefore helps mainly where the base model is genuinely weak.

</details>

### [VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation](2606.26534.md)
**Tianxin Xie, Chenxing Li, Dong Yu, Li Liu** · 2026-06-25

<details>
<summary>Abstract</summary>

Recently, zero-shot text-to-speech (TTS) has enabled high-fidelity and expressive speech synthesis, but it often fails to imitate unseen speaking styles from uncommon scenarios (e.g., crosstalk, dialects). Moreover, fine-tuning pretrained models requires large, high-quality datasets, limiting rapid personalization. We propose VoiceTTA, a reinforcement learning-based test-time adaptation (TTA) method that improves voice imitation of pretrained zero-shot TTS models. VoiceTTA introduces two style rewards based on coefficient-of-variation differences of F0 and energy, combined with speaker similarity and intelligibility (WER from a pretrained Whisper model), and optimizes learnable prefixes via group relative preference optimization (GRPO) in a flow matching-based model at inference time. Extensive experiments demonstrate substantial improvements on uncommon speech prompts, outperforming state-of-the-art baselines. Audio samples are available at https://voicetta.pages.dev/

</details>

### [Joint Residual Reweighting for Classifier Free Guidance in Flow-Matching Zero-Shot TTS](2606.25672.md)
**Runwu Shi, Yujin Wang, Hongjin Song, Chunxiang Jin** · 2026-06-24

<details>
<summary>Abstract</summary>

Classifier-free guidance (CFG) is widely used in flow-matching-based zero-shot text-to-speech (TTS), where generation is typically controlled by two conditions: the target text and a prompt speech signal. Standard CFG strengthens these conditions jointly, while recent branch-selective guidance methods attempt to enhance text or speaker conditioning separately, often leading to a trade-off between text correctness and speaker similarity. In this paper, we revisit the CFG under independently masked text and speech-prompt conditions, and decompose the guidance field into text, speaker, and joint residuals. We show that conventional speaker-selective guidance entangles the speaker residual with the joint residual, which may disturb text-related generation. Based on this observation, we propose joint residual reweighting, which independently controls the speaker and joint residuals within the standard CFG framework. Experiments on F5-TTS and CosyVoice2 show that the proposed method improves speaker similarity while maintaining competitive text correctness, demonstrating the usefulness of the joint residual for balancing speaker fidelity and text accuracy in zero-shot TTS.

</details>

### [Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS](2606.25424.md)
**Sandipan Dhar, Nirmesh J. Shah, Ashishkumar P. Gudmalwar, Pankaj Wasnik** · 2026-06-24

<details>
<summary>Abstract</summary>

Diffusion-based text-to-speech (TTS) models have achieved significant improvements in speech quality. However, modeling sharp prosodic transitions and rapid pitch variations in expressive speech remains challenging. Existing diffusion-based TTS decoders commonly utilize periodic nonlinearities such as Snake activation function to capture harmonic structures, but this activation funcation provides limited adaptability when modeling abrupt amplitude and frequency variations. In this paper, we investigate the role of oscillatory inductive bias in diffusion-based TTS decoders and introduce an adaptive oscillatory nonlinearity that enables controllable periodic modulation while maintaining signal stability through a linear bypass component. We refer the resulting TTS system as OscillaTTS. Experiments on the LJSpeech and Emotional Speech Dataset show consistent improvements across objective and subjective evaluations, indicating improved modeling of expressive prosodic dynamics.

</details>

### [CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations](2606.25403.md)
**Ram Annamdevula, Ankit Tatawat, Ashishkumar P. Gudmalwar, Nirmesh J. Shah et al.** · 2026-06-24

<details>
<summary>Abstract</summary>

Accent conversion and controllability remain fundamental challenges in cross-lingual text-to-speech (TTS), particularly for low-resource and phonetically diverse Indic languages. While recent large language model (LLM)-based TTS systems exhibit strong cross-lingual generalization, they provide limited explicit control over accent characteristics and intensity. In this paper, we propose CrossAccentTTS, a framework that enables both accent control and conversion while preserving speaker identity. Specifically, we introduce an Accent Intensity Controller (AIC) that injects weighted language embeddings into the accent subspace, allowing smooth interpolation between accents and fine-grained modulation of accent strength at inference time. Experiments on the Indic Multilingual and L2-arctic datasets shows that CrossAccent-TTS achieves precise control of accent intensity, outperforming strong baselines in accent similarity and controllability by maintaining speaker similarity and naturalness.

</details>

### [Sarashina2.2-TTS: Tackling Kanji Polyphony in Japanese Speech Generation via Data Scaling and Targeted Data Synthesis](2606.25369.md)
**Lianbo Liu, Shiao Zhu, Kai Washizaki, Reo Yoneyama et al.** · 2026-06-24

<details>
<summary>Abstract</summary>

While large language model (LLM)-based text-to-speech (TTS) systems have achieved high-quality speech synthesis, most existing systems focus on English and Chinese. Japanese, however, remains under-explored, and its unique linguistic challenges, such as widespread context-dependent kanji polyphony, have yet to be adequately tackled. Here we introduce Sarashina2.2-TTS (https://github.com/sbintuitions/sarashina2.2-tts), a Japanese-centric LLM-TTS system that tackles these challenges through a dual approach: data strategy and evaluation methodology. First, we scale training to approximately 361k hours of speech, incorporating a balanced mix of Japanese and English data. Furthermore, we design a targeted data augmentation pipeline covering all 2,136 Joyo (regular-use) kanji designated by Japan's Agency for Cultural Affairs to efficiently address kanji polyphony disambiguation. Second, we introduce the Joyo Kanji Yomi Benchmark (https://github.com/sbintuitions/JoyoKanji-Yomi-Benchmark), covering all 2,136 Joyo kanji and their 4,378 readings. Alongside this benchmark, we propose Kana-CER, a metric that compares synthesized speech against reference readings in the kana space, eliminating orthographic variations to directly measure pronunciation correctness. Experiments demonstrate that our targeted data augmentation significantly improves reading accuracy. Overall, Sarashina2.2-TTS achieves state-of-the-art kanji-level reading accuracy and matches top baselines on general sentence-level pronunciation, while delivering the highest speaker similarity in zero-shot Japanese speech synthesis. Furthermore, cross-lingual evaluation reveals that Sarashina2.2-TTS is the only system that maintains stable Japanese pronunciation regardless of the prompt language, confirming that our balanced training approach improves cross-lingual robustness.

</details>

### [CN-NewsTTS Bench: a target-level automatic benchmark for raw-input Chinese news TTS pronunciation](2606.24714.md)
**Shijun Luo** · 2026-06-23

<details>
<summary>Abstract</summary>

Chinese news text contains dense written forms such as scores, hyphenated model names, ranges, unit symbols, percentages, English abbreviations, and mixed Chinese-Latin-digit names. These forms are frequent in real listening workflows, and a text-to-speech (TTS) system can preserve the written string while changing the spoken meaning. We introduce CN-NewsTTS Bench v0.1, an open target-level benchmark for evaluating whether Chinese news TTS products pronounce such targets correctly from raw text, without user-side rules, LLM rewriting, SSML hints, or manual edits. The release contains a 200-record development set, an 800-record public test set, 992 public auto-evaluable targets, fixed transcripts from a three-ASR ensemble, an automatic target scorer, and initial results for seven product TTS systems. We additionally report ASR-route diagnostics, ASR-subset ablations, category-level results, confidence intervals, and provider configuration metadata. The best system reaches 0.879 strict accuracy, while several systems remain below 0.60.

</details>

### [ZONOS2 Technical Report](2606.24320.md)
**Gabriel Clark, Sofian Mejjoute, Mohamed Osman, George Close et al.** · 2026-06-23

<details>
<summary>Abstract</summary>

We present ZONOS2 8B, our latest TTS model, which achieves state-of-the-art naturalness, prosody, and voice cloning fidelity. We improve upon Zonos-v0.1 across scale, data, and training recipe. We scale the model from 1.6B to 8B total parameters (900M active) with a novel mixture-of-experts (MoE) backbone, improving inference latency and throughput. We expand our training corpus from 200K to over 6M hours using a new data processing pipeline, and we simplify our post-training and conditioning recipes to improve naturalness and voice cloning fidelity. We evaluate ZONOS2 8B on quality, speaker similarity, WER, and ZTTS1-Eval, our novel TTS benchmark, where it performs competitively with state-of-the-art systems while maintaining good streaming latency. We release our model weights and example inference code under an Apache 2.0 license on GitHub and Hugging Face.

</details>

### [On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models](2606.23285.md)
**Shunsuke Kando, Wataru Nakata, Shinnosuke Takamichi, Yusuke Miyao** · 2026-06-22

<details>
<summary>Abstract</summary>

Generative Spoken Language Modeling (GSLM) enables text-free speech modeling by training language models (LMs) using discrete speech representations instead of textual transcription. In this paper, we investigate the performance of GSLM on speech synthesis and continuation using discrete speech representations with varying bitrates. We segment speech representations with fixed widths and train K-means models in multiple cluster sizes, resulting in various bitrate settings. We demonstrate that intelligible and natural speech can be synthesized at lower bitrate settings than the baseline. Furthermore, speech continuation quality remains stable at lower bitrates across multiple metrics, suggesting that the conventional GSLM setting may be redundant for effective speech generation. Although LLM-based metrics show higher correlation with human subjective score than conventional metrics, it remains low, highlighting the need for more stable automatic evaluation methods.

</details>

### [FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech](2606.23190.md)
**Haoxu Wang, Biao Tian, Weiqing Li, Xiang Lv et al.** · 2026-06-22

<details>
<summary>Abstract</summary>

Existing Reinforcement Learning (RL) research for Text-to-Speech (TTS) focuses on large language models (LLMs), leaving Flow-Matching (FM) under-explored. We present FlowTTS-GRPO, an online RL framework for FM-based TTS. By converting ordinary differential equation (ODE) trajectories into stochastic differential equation (SDE) paths, our method enables direct fine-tuning of open-source FM models without auxiliary models. We show that a weighted reward combination converges faster than a probabilistic scheme, and identify three practical optimizations: omitting classifier-free guidance (CFG) during training accelerates convergence; synthesizing hard cases improves robustness; and applying RL to the FM component enhances audio-detail metrics. Experiments on CosyVoice 3.0 and F5-TTS demonstrate objective and subjective preference gains in speaker similarity and perceptual quality, with F5-TTS also improving intelligibility.

</details>

### [Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS](2606.23176.md)
**Seymanur Akti, Alexander Waibel** · 2026-06-22

<details>
<summary>Abstract</summary>

Humans tend to speak louder and clearer in challenging environments, such as noisy conditions or when addressing hearingimpaired listeners, which is called Lombard effect. To simulate this behavior in speech synthesis systems, we introduce a flow-matching based text-to-speech (TTS) model trained with vocal effort and articulation pseudo-labels. The proposed model achieves continuous and disentangled control of vocal effort and articulation, while also enabling word-level emphasis for clarifying specific segments of an utterance. Experimental results show that these control mechanisms effectively improve clarityrelated acoustic features. Furthermore, speech-in-noise experiments demonstrate that our model successfully simulates the intelligibility gains of human clear speech in noisy conditions.

</details>

### [Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis](2606.22811.md)
**Jinchuan Tian, Haoran Wang, Siddhant Arora, Takashi Maekaku et al.** · 2026-06-22

<details>
<summary>Abstract</summary>

Classical TTS systems typically rely on rigid input formats and predefined metadata slots, limiting their ability to fulfill flexible user requirements. This paper introduces Bagpiper-TTS, a universal speech synthesis system that deals with diverse natural language user requests. Given a natural language prompt, Bagpiper-TTS first reasons over the users' intent to derive a rich caption, i.e., a comprehensive textual blueprint encompassing both transcription and nuanced metadata. Subsequently, this caption guides the synthesis of the target speech. Our model inherently supports a broad spectrum of tasks besides classical TTS applications, including multi-talker, intent-to-speech, role-play synthesis, singing voice synthesis, and more. Experimental results demonstrate that Bagpiper-TTS achieves an 1.7% Word Error Rate (WER) on the Seed-TTS-Eval benchmark and match the performance of dedicated models in both LLM-as-a-judge and human subjective evaluations across multiple applications.

</details>

### [Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study](2606.22009.md)
**Tomoki Koriyama** · 2026-06-20

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion is essential for controllable and robust text-to-speech, and large language models (LLMs), with broad linguistic knowledge, offer a promising approach. We benchmarked over 30 LLMs on Japanese G2P, comparing them with conventional morphological analyzers on 3000 manually annotated sentences. We evaluated two prompting strategies: a parse mode, where the LLM performs morphological analysis followed by rule-based kana conversion, and a direct mode, where the LLM directly predicts kana readings. The results show that model size, version, and Japanese-specialized training are key factors, with the best LLMs achieving kana character error rate below 0.52\% vs. the best conventional tool (1.03\%). Parse mode outperforms direct mode for most models, as rule-based post-processing relieves the LLM of handling complex pronunciation rules. We also show that feeding LLM-predicted kana into a kana-input TTS yields better pronunciation than end-to-end TTS.

</details>

### [ISCSLP 2026 CoT-TTS Challenge: Chain-of-Thought Reasoning for Context-Aware Text-to-Speech](2606.21933.md)
**Wei Xue, Junlan Feng, Shilei Zhang, Yue Wang et al.** · 2026-06-20

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) have greatly improved speech naturalness, speaker similarity, and controllability. However, most existing controllable TTS systems still rely on explicit user-provided style prompts, making it difficult to automatically determine how a sentence should be spoken in long and complex conversational scenarios. This proposal introduces the ISCSLP 2026 CoT-TTS Challenge, which aims to evaluate whether a system can infer the intended speaking manner from contextual information and generate speech consistent with both the reasoning output and the surrounding scene. The challenge contains two tracks: text-context-aware CoT-TTS and audio-context-aware CoT-TTS. We construct a large-scale bilingual training set from speech-rich media and provide carefully filtered evaluation data for leaderboard comparison. Each system is required to output both a chain-of-thought reasoning analysis and the generated speech waveform. The official evaluation combines objective metrics, multimodal LLM-based evaluation, and human subjective assessment. To facilitate reproducibility, we provide inference code together with a fine-tuning recipe for a 0.6B Qwen3-based model trained via a three-stage strategy. This challenge is expected to support research on context understanding, chain-of-thought reasoning, and expressive speech generation for applications such as film dubbing, audiobook production, virtual characters, and spoken dialogue agents. Further information about the associated challenge is available at:https://iscslp2026-cot-tts.github.io/challenge-website/

</details>

### [Streaming T5-based Text-to-Speech Synthesis with Limited Lookahead](2606.21882.md)
**Muyang Du, Jason Roche, Junjie Lai** · 2026-06-20

<details>
<summary>Abstract</summary>

Streaming text-to-speech synthesis in cascaded LLM-TTS systems still faces latency challenges as most TTS models require full context before initiating generation. We present S5-TTS, a streaming variant of T5-TTS that enables low-latency, word-by-word incremental speech synthesis through encoder-decoder language modeling and monotonic alignment learning. S5-TTS begins generating speech immediately after receiving the first few words, substantially reducing end-to-end response latency. To maintain quality under limited lookahead, we introduce a lookahead-causal masking mechanism with Conv-based auxiliary attention that preserves intelligibility and speaker similarity, and employ interleaved multi-source distillation to further restore naturalness. Experiments show that S5-TTS achieves comparable quality to full-context T5-TTS, supports zero-shot synthesis with high speaker similarity, and significantly reduces end-to-end latency for practical conversational AI systems.

</details>

### [AugCodec: A Low-Bitrate Disentangled Neural Speech Codec via Data Augmentation](2606.21893.md)
**Dongmei Wang, Xiaohang Sun, Yang Liu, Fanjie Kong et al.** · 2026-06-20

<details>
<summary>Abstract</summary>

We propose AugCodec, a low-bitrate disentangled neural speech codec that leverages data augmentation to decompose speech into three distinct components: semantic, speaker, and prosody tokens. Specifically, we employ tailored augmenta tion strategies to transform speech into distinct variants, each serving as input for extracting tokens that preserve the target attribute while suppressing others. This disentanglement strategy enables substantial reduction in token rate. Further more, we introduce an augmentation loss that aligns semantic encoder outputs between source and voice-converted speech, encouraging speaker-agnostic embeddings while mitigating the acoustic mismatch induced by voice conversion. Experiments on LibriSpeech test-clean demonstrate that AugCodec significantly outperforms state-of-the-art methods in both reconstruction quality and disentanglement, while operating at only 12.5Hz with three token streams.

</details>

### [ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion](2606.21888.md)
**Jeongsoo Choi, Ji-Hoon Kim, Shujie Hu, Joon Son Chung** · 2026-06-20

<details>
<summary>Abstract</summary>

Neural speech codecs efficiently compress speech and have become a foundation for speech generation, but they are typically learned as holistic representations that intertwine linguistic content, speaker identity, and prosody. While this design is effective for zero-shot voice cloning, it hinders downstream tasks that require prosody preservation or transfer, such as voice conversion. To address this, we introduce ProsoCodec, a prosody-oriented speech codec that models prosody as a conditional residual rather than as a disentangled stream. Specifically, by conditioning both the encoder and decoder on text and speaker embeddings as prefix tokens, the discrete bottleneck is encouraged to capture prosodic variation not explained by content and speaker. To further preserve prosody, we use the low-frequency mel band and train the model on paired same-speaker utterances. Experiments on voice conversion show improved prosody preservation and reduced source-timbre leakage.

</details>

### [An Evaluation Framework for Text-to-Speech Voice Reconstruction](2606.21343.md)
**Ariadna Sanchez, Christoph Minixhofer, Korin Richmond, Ondrej Klejch et al.** · 2026-06-19

<details>
<summary>Abstract</summary>

Voice reconstruction using Text-to-Speech (TTS) offers a communication method for people with speech disorders, which aims to retain their speaker identity while improving intelligibility. Previous work generally relies on Mean Opinion Score (MOS) to evaluate naturalness and speaker similarity, but this has limited sensitivity and reliability. We propose an evaluation framework with subjective and objective components. Subjectively, we evaluate perceived intelligibility and speaker identity using Best Worst Scaling (BWS) with situational framing. Objectively, we demonstrate that standard measures fail to predict reconstruction success for highly unintelligible speakers, so we introduce a novel dual-reference distributional measure to assess the trade-off between intelligibility and speaker identity. By evaluating the output of 17 zero-shot TTS systems for 193 speakers, we show that our framework provides a reliable and task-aligned approach for assessing voice reconstruction.

</details>

### [Backdoor Attacks on Speech Emotion Recognition via TTS-Generated Poisoning](2606.21052.md)
**Yongbin Huang, Xihao Xie, Jia Zhang** · 2026-06-19

<details>
<summary>Abstract</summary>

Speech Emotion Recognition (SER) systems increasingly leverage self-supervised acoustic representations, yet their vulnerability to training-time attacks remains largely underexplored. This paper presents the first systematic study of poisoning-based backdoor attacks on SER, with a focus on threats enabled by text-to-speech (TTS) generated audio. We introduce a stealthy, low-energy acoustic trigger that can be embedded imperceptibly into both natural and synthetic speech, enabling scalable and consistent poisoning. Our experiments demonstrate that SER models can be reliably compromised with high attack success rates under low poisoning ratios, while maintaining near-clean performance on benign inputs. We further show that backdoor patterns exhibit strong cross-model transferability and that self-supervised representations are particularly susceptible to learning these triggers. These findings reveal that TTS technology dramatically lowers the barrier to effective backdoor attacks, exposing critical vulnerabilities in modern SER pipelines and motivating the urgent need for dedicated defenses.

</details>

### [SDP-Codec: A Speaker-Decoupled Speech Codec with Pitch Injection for Low-Bitrate Coding and Zero-Shot Voice Conversion](2606.21157.md)
**Hounsu Kim, Juhan Nam** · 2026-06-19

<details>
<summary>Abstract</summary>

Speaker-decoupled speech codecs can reduce bitrate by separating global speaker attributes from local content and prosody, while supporting voice conversion. Existing speaker-decoupled codecs face a trade-off: methods that explicitly suppress speaker leakage often rely on multi-stage or auxiliary training, whereas simpler designs can leave residual speaker information in local tokens. We propose SDP-Codec, a speaker-decoupled, pitch-injected codec trained with a single-stage optimization pipeline. SDP-Codec derives local tokens from continuous pre-quantization features of a pretrained self-supervised encoder and injects normalized F0 via a pitch encoder-decoder with global-conditioned denormalization and soft-label pitch reconstruction objective. Across 16 kHz and 24 kHz settings, SDP-Codec achieves competitive reconstruction and strong zero-shot voice conversion at comparable bitrates, with the lowest speaker-probing accuracy among compared systems, suggesting reduced speaker leakage.

</details>

### [LambdaMark: Semantic Audio Watermarking for Robustness and Radioactivity](2606.21365.md)
**Kexin Li, Xiao Hu, Ilya Grishchenko, David Lie** · 2026-06-19

<details>
<summary>Abstract</summary>

Recent advances in generative audio have made voice cloning increasingly effortless, enabling voice fraud, impersonation, and other forms of unauthorized use. A common attack finetunes a speech generation model on recordings of a target speaker, allowing the model to synthesize speech in that speaker's voice. Audio watermarking offers a promising defense by embedding detectable signals into audio. A practical watermark must satisfy two key properties: robustness and radioactivity. Existing audio watermarking methods typically embed signals into low-level representations, such as waveforms or spectrograms, which makes them vulnerable to signal-level manipulations and limits their transfer to downstream models. We introduce LambdaMark -- the first generic radioactive watermarking scheme. Unlike all previous approaches, LambdaMark achieves generic radioactivity by embedding multi-bit watermark information into semantic audio latent representations. Our watermarks have semantic interpretation and are thus more likely to be learned by a downstream model through finetuning. LambdaMark includes a lightweight watermark encoder to inject multi-bit message-dependent perturbations into semantic audio representations and a decoder to detect watermark presence and recover the embedded bit information. Encoder and decoder are trained using a custom multi-component loss that preserves fidelity of the watermarked audio, increases bit-level recovery rate, and improves robustness against common distortions and adversarial removal attempts. Experiments show that LambdaMark achieves near-perfect robustness under common distortions. LambdaMark is also the only watermark that is robust against all evaluated removal attacks. Furthermore, LambdaMark exhibits general and robust radioactivity and remains robust to distortions and adversarial removal attacks even on the generated outputs of those finetuned models.

</details>

### [How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech](2606.20532.md)
**Nityanand Mathur, Hamees Sayed, Wasim Madha, Apoorv Singh et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

Style-captioned text-to-speech systems use natural language to control voice characteristics, but how individual words influence acoustic output remains unclear. Understanding this is critical for diagnosing failure modes and improving controllability in expressive TTS. We propose cross-attention attribution for speech diffusion models, adapting the DAAM framework to the speech domain for the first time, and apply it to CapSpeech-TTS. Our method extracts per-token heatmaps across 25 layers and 24 ODE steps. We analyze 3,600 (style caption, text transcript) combinations comprising 120 style captions conditioning the generation of 30 text transcripts each, revealing how caption tokens shape waveforms. Results show: (1) style tokens have lower temporal variance than content/function tokens, confirming global conditioning; (2) style attention correlates with F0 and energy; (3) style conditioning peaks in early steps and deep layers; (4) attention entropy reaches its minimum at layer 17, co-occurring with the style importance peak, indicating maximal network selectivity at the most style-critical stage. This is the first study of how natural language influences cross-attention in speech diffusion models

</details>

### [FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS](2606.20518.md)
**Harshit Singh, Ayush Pratap Singh, Nityanand Mathur** · 2026-06-18

<details>
<summary>Abstract</summary>

Flow-matching text-to-speech systems achieve remarkable zero-shot quality but remain static after deployment: pronunciation errors on out-of-vocabulary proper nouns persist unless the model is retrained. We introduce FlowEdit, a life-long adaptation framework for frozen flow-matching TTS that learns pronunciation corrections as latent conditioning edits rather than weight updates. When corrective feedback is provided, FlowEdit optimizes a token-level perturbation in the text embedding space, then stores the correction in a Modern Hopfield Network serving as content-addressable episodic memory. At inference, corrections are retrieved via soft attention with a similarity gate, enabling fuzzy morphological matching. On our curated benchmark of 312 multilingual proper nouns across 18 language families, FlowEdit reduces target-word Phoneme Error Rate by 92.7% relative to the zero-shot baseline while maintaining identical general-speech quality. Corrections complete in approximately 15 seconds on a single GPU.

</details>

### [Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning](2606.20266.md)
**SooHwan Eom, Hee Suk Yoon, Eunseop Yoon, Mark Hasegawa-Johnson et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

Recent flow-matching text-to-speech (TTS) models, such as F5-TTS, rely on a reference transcript at inference time, obtained from an external ASR system. This dependency makes zero-shot TTS brittle for accented or dysarthric speakers, precisely the scenarios where it is most needed. Moreover, we find that text-based reference conditioning can propagate atypical acoustic patterns from atypical speech into synthesis, even when ground-truth transcripts are available. To address this, we propose RTFree-F5, which replaces the reference transcript with continuous self-supervised speech representations mapped into F5-TTS's text-conditioning space via a lightweight adapter, while reusing the pretrained checkpoint. On dysarthric speech, RTFree-F5 reduces WER from 24.6% to 10.4%, surpassing even the ground-truth reference transcript baselines, while improving naturalness and remaining competitive on standard benchmarks without requiring any reference transcript.

</details>

### [PASQA: Pitch-Accent-Focused Speech Quality Assessment Model Trained on Synthetic Speech with Accent Errors](2606.20137.md)
**Masaya Kawamura, Yuma Shirahata, Kentaro Mitsui, Reo Shimizu** · 2026-06-18

<details>
<summary>Abstract</summary>

Existing mean opinion score (MOS) prediction models typically predict utterance-level naturalness MOS and can be insensitive to localized pitch-accent errors. We propose Pitch-Accent-focused Speech Quality Assessment (PASQA), which explicitly targets pitch-accent correctness. To train our model, we construct a controlled Japanese accent-error dataset by changing accent patterns using an accent-controllable text-to-speech system, and compute a pseudo accent-quality score from the accent-error rate. PASQA builds on self-supervised representations and employs mora-conditioned fusion, ranking loss, an auxiliary accent-error localization task, and speaker-invariant training. Experiments show that conventional models fail to preserve the ordering by accent-error severity, whereas PASQA achieves high ordering accuracy on both seen and unseen speakers. Further, PASQA shows stronger agreement with human accent-correctness judgments. The code is available at https://github.com/lycorp-jp/PASQA.

</details>

### [Investigating Human-Model Discrepancies in Speech Quality Assessment via Acoustic and Prosodic Perturbations](2606.19951.md)
**Masato Takagi, Masaya Kawamura, Reo Shimizu, Yuma Shirahata** · 2026-06-18

<details>
<summary>Abstract</summary>

Mean opinion score (MOS) prediction models are widely used as proxy metrics in text-to-speech (TTS) research, yet their ability to capture quality differences beyond acoustic fidelity remains unclear. We investigate this via controlled perturbations on speech: acoustic degradation, prosodic errors, and manipulation of speaker-specific characteristics such as pitch and speaking rate. We obtained MOS predictions for these speech samples from both human listeners and the model, and analyzed the differences in their perceptual characteristics. Results show that most models track acoustic degradation well, while all are insensitive to prosodic errors despite large subjective score drops. For speaker characteristics, models exhibit a double dissociation: strong mean fundamental frequency (F0) biases absent in human ratings, yet insensitivity to speaking rate and F0 variability that humans notice. These findings highlight limitations of scalar MOS prediction beyond acoustic fidelity.

</details>

### [Exploring Pre-training Benefits on Phoneme Addition through Fine-tuning in Speech Synthesis](2606.19792.md)
**Masato Murata, Koichi Miyazaki, Tomoki Koriyama, Tomoki Toda** · 2026-06-18

<details>
<summary>Abstract</summary>

Transfer learning is widely used for low-resource text-to-speech. When the target corpus contains phonemes unseen in pre-training, the model must expand its phoneme inventory during fine-tuning; we call the process "phoneme addition." However, it remains unclear whether the pre-trained ability to generate seen phonemes contributes to this process. This study investigates phoneme addition in two settings: (1) a simulation setup using LLM-generated phoneme-controlled corpora that enables investigation without considering confounding factors, and (2) a real-speech cross-lingual transfer setup (English to Japanese) to validate whether the findings hold in practice. Experiments in both settings showed that while fine-tuning achieved higher naturalness than training from scratch, it required as much or more data to achieve comparable PER for new phonemes. These results indicate that pre-training mainly contributes to naturalness improvement, but offers limited benefit for phoneme addition.

</details>

### [Repurposing a Speech Classifier for Guided Diffusion-Based Speech Generation](2606.20457.md)
**Rostislav Makarov, Timo Gerkmann** · 2026-06-18

<details>
<summary>Abstract</summary>

Classifier guidance is a way to control diffusion generation by using a noise-conditioned classifier to steer the sampling process toward a target class. One drawback of classifier guidance is that it requires two separately trained models: a classifier and a diffusion model. We therefore study a more compact alternative in which a conventionally trained speech classifier is repurposed as the backbone for diffusion generation. Starting from a frozen noise-conditioned classifier in log-Mel space, we attach a lightweight subnetwork that reuses intermediate classifier representations and train only this subnetwork under a Denoising Score Matching objective. Our work shows that a pretrained classifier can be repurposed for conditional generation, providing an appealing bridge between discriminative modeling and conditional speech synthesis resulting in high speech quality within a single-backbone model, with reduced memory footprint and computational cost.

</details>

### [Interpreting Content and Speaker Characteristics in Factorised Self-Supervised Subspaces](2606.19974.md)
**Kyle Janse van Rensburg, Herman Kamper** · 2026-06-18

<details>
<summary>Abstract</summary>

Self-supervised speech features encode both content and speaker information. Recent work introduced an SVD-based factorisation that decomposes these features into a shared content matrix capturing temporal variation and speaker-specific transformations capturing static speaker characteristics. However, how information is organised within these components remains unclear. In this paper, we investigate how the dimensions of WavLM-factorised content and speaker subspaces correlate with speech characteristics such as pitch, intensity, and voicing. We find that leading dimensions in the content space primarily capture intensity, higher-order formants, and voicing, while pitch is encoded in a later dimension. In contrast, the highest-variance speaker dimension is strongly associated with pitch and gender, with later dimensions capturing high-frequency variation. Intervention experiments show that manipulating these dimensions enables targeted control of speech characteristics for speech synthesis. Furthermore, modifying the content and speaker representations jointly provides fine-grained control over characteristics such as pitch and intensity.

</details>

### [Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization](2606.20218.md)
**Yudong Li, Zihao Fang, Junwen Qiu, Ruihai Jing et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

Streaming zero-shot voice conversion struggles to disentangle timbre from linguistic content without degrading utility or inflating latency. Current methods rely on information bottleneck (IB) or speaker perturbation. While IB filters out timbre, it discards prosody, forcing models to explicitly inject features like fundamental frequency. This often requires buffering future frames, creating algorithmic lookahead latency. On the other hand, existing perturbation methods largely overlook the crucial trade-off between timbre leakage and utility preservation. Recognizing this neglected trade-off, we find that the inherent objective of Speaker Anonymization (SA) aligns well with balancing these factors. Thus, we introduce SA as a novel perturbation mechanism to explicitly mitigate timbre leakage while retaining prosodic utility. Crucially, SA's robust representations significantly alleviate the generator's reliance on future context, enabling our strictly causal, zero-lookahead network. Audio samples are available at https://amphionteam.github.io/Zero-VC-demo/.

</details>

### [PhysDrift: Bridging the Embodiment Gap in Humanoid Co-Speech Motion Generation](2606.19935.md)
**Zhangzhao Liang, Xiaofen Xing, Mingyue Yang, Wenlve Zhou et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

Humanoid robots require co-speech motions that are not only expressive and speech-aligned, but also physically executable under embodiment constraints. Existing co-speech generation pipelines are predominantly human-centric: motions are first generated in human-body representations such as SMPL-X and subsequently retargeted to humanoid robots. In this work, we identify a fundamental embodiment gap in this paradigm, where the mismatch between human motion manifolds and humanoid embodiment constraints disrupts embodiment consistency during motion transfer and physical execution. Through extensive analysis, we show that although retargeting can preserve coarse motion semantics, it significantly compresses motion diversity and weakens prosody-motion synchronization, limiting expressive humanoid behaviors. To address this problem, we first propose IK-EER, a prosody-preserving humanoid motion curation framework that jointly optimizes kinematic feasibility and speech-motion temporal alignment during retargeting. Building upon the curated robot-native motion dataset, we further introduce PhysDrift, an embodiment-aware co-speech motion generation framework that directly predicts executable humanoid joint trajectories from speech without relying on intermediate human-body representations. Unlike conventional human-centric pipelines, PhysDrift maintains embodiment consistency throughout both training and inference while incorporating physical regularization to stabilize robot motion dynamics. Extensive experiments and real-world humanoid deployment demonstrate that embodiment-aware robot-native generation substantially improves speech-motion alignment, physical plausibility, motion smoothness, inference efficiency, and real-time interaction capability.

</details>

### [FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech](2606.19209.md)
**Shuoyi Zhou, Yixuan Zhou, Peiji Yang, Yifan Hu et al.** · 2026-06-17

<details>
<summary>Abstract</summary>

Controllable text-to-speech (TTS) has become a key research focus. However, methods based on either reference speech or text descriptions lack flexibility and precise control, and recent joint approaches remain loosely coupled, with speech modeling timbre and text controlling global style. We propose FineCombo-TTS, a unified framework for speech synthesis grounded in reference speech and guided by text descriptions, enabling flexible and precise control over acoustic attributes. Instead of explicit attribute disentanglement, we learn a unified acoustic representation and introduce a Conditional Flow Matching (CFM)-based Speech Variance Predictor to model fine-grained reference-to-target transformations guided by text descriptions. To support relative attribute control, we construct FineEdit, a structured paired dataset that explicitly encodes source-to-target attribute variations. Experiments demonstrate that our approach achieves flexible, precise, and expressive controllable TTS.

</details>

### [Augmenting Dysarthric Speech Severity Assessment with MOS Supervision](2606.18645.md)
**Kaimeng Jia, Minzhu Tu, Zengrui Jin, Siyin Wang et al.** · 2026-06-17

<details>
<summary>Abstract</summary>

Dysarthria is a speech disorder marked by reduced intelligibility and communicative effectiveness. Automatic utterance-level assessment of dysarthric speech can support scalable speech monitoring and therapy-related analysis. Yet training such systems is bottlenecked by the scarcity of clinically annotated dysarthric speech. This work proposes to augment dysarthric speech assessment using data from speech synthesis evaluations, specifically human-annotated utterances with Mean Opinion Score (MOS) labels from the QualiSpeech corpus. Experiments show that fine-tuning on speech synthesis assessment data consistently improves performance on both intelligibility and naturalness prediction, while joint training yields gains primarily on naturalness. These results suggest that synthesis artifacts and dysarthric speech share perceptual commonalities, and speech synthesis evaluation corpora offer a practical augmentation source that reduces reliance on scarce clinical annotations.

</details>

### [Generating Natural and Expressive Robot Gestures through Iterative Reinforcement Learning with Human Feedback using LLMs](2606.18747.md)
**Chris Lee, Flora Salim, Benjamin Tag, Francisco Cruz** · 2026-06-17

<details>
<summary>Abstract</summary>

Expressive gestures are essential for natural and effective communication, complementing speech when verbal cues alone are insufficient (e.g., pointing). For social robots such as the humanoid Pepper, producing natural and expressive movements is critical for improving human-robot interaction (HRI) and long-term acceptance. However, generating gestures remains challenging due to reliance on expert-authored animations, resulting in rigid behaviors that are impractical for dynamic and diverse environments. Alternatively, machine learning approaches often struggle to capture perceived naturalness, becoming increasingly challenging with more degrees of freedom. Consequently, producing expressive robot gestures requires a system that can adapt to the environment while adhering to social norms and physical constraints. Recent advances in large language models (LLMs) enable dynamic code generation, offering new opportunities for runtime gesture synthesis from natural language. In this paper, we integrate ChatGPT into the humanoid robot Pepper to generate co-speech gestures aligned with conversational output. While this baseline enables flexible gesture generation, the resulting motions are often perceived as stiff and unnatural. To address this limitation, we introduce an iterative reinforcement learning with human feedback (RLHF) system that finetunes gesture generation based on user evaluations, leveraging an iterative user study to compare Pepper's generated gestures. Our results show that RLHF improved the LLM's co-speech generative capabilities, producing more expressive, relevant and fluid movements.

</details>

### [GRIDEX: Grid-Grounded Forensic Explanations for Deepfake Spectrogram Analysis](2606.18738.md)
**Thi Ngan Ha Do, Tingmin Wu, Alsharif Abuadbba, Kristen Moore** · 2026-06-17

<details>
<summary>Abstract</summary>

The advancement of speech generation technologies has made artificial speech increasingly realistic. Although modern classification models can achieve high accuracy when it comes to deepfake detection, they do not produce evidences such as indicating where spoof cues appear in the spectrogram and what they imply acoustically, limiting their usefulness in forensic settings. Manual analysis of full spectrograms is resource-intensive, so evidence should narrow attention to the most diagnostic regions. Moreover, existing explainability methods have limited capabilities in connecting contextual attributes to localized evidence, making explanations harder to verify. To overcome this limitation, we propose GRIDEX, a pipeline that, when given a deepfake spectrogram, generates forensic explanations of its anomalies. The pipeline (i) selects top-K anomalous regions in the spectrogram and (ii) produces an explanation for each anomaly. The explanations follow a schema of categorical acoustic fields, including temporal, spectral, phonetic information and interpretation text. To our knowledge, this is the first framework to generate structured forensic explanations using regional grounding for deepfake spectrograms. GRIDEX is trained with a two-stage learning paradigm that combines supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO). Experiments on our dataset show improved artifact localization and explanation quality over strong vision-language model (VLM) baselines. The dataset and code will be released upon publication.

</details>

### [MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data](2606.18485.md)
**Subhankar Ghosh, Jason Li, Paarth Neekhara, Shehzeen Hussain et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Neural Text-to-Speech (TTS) systems achieve remarkable quality on short utterances but long-form speech generation shows prosodic drift, speaker inconsistencies and sentence boundary artifacts. Existing approaches either compress sequences, increase context length or naively concatenate independently synthesized chunks. We present an inference-time approach called MagpieTTS-LF that enables MagpieTTS to produce coherent long-form speech without model retraining. Our method introduces three key innovations: (1) soft attention priors to guide monotonic alignment while preserving past and future context; (2) a stateful inference algorithm that maintains context across sentence chunks, ensuring prosodic continuity; (3) history-aware text encoding that uses past text for discourse-level prosodic planning. Experiments on long texts show significant improvements in long-range intelligibility, prosodic coherence, speaker consistency, and boundary naturalness compared to other baselines.

</details>

### [Reliable Neural-Codec Text-to-Speech by ASR Self-Verification and Distillation: Near-Zero Catastrophic Failures Across Models and Codecs](2606.18323.md)
**Ali Asaria, Tony Salomone, Deep Gandhi** · 2026-06-16

<details>
<summary>Abstract</summary>

Open autoregressive neural-codec text-to-speech (TTS) models sound excellent on typical inputs yet suffer stochastic catastrophic failures: on a meaningful fraction of utterances they emit silence, terminate early, or collapse into repetitive or hallucinated content. We show this failure mode is cheap to remove. Under a single format-robust metric (a catastrophic-failure rate via an ASR round-trip), best-of-N ASR self-verification drives failures to near-zero: no observed failures remain by N=2 on a standard corpus (LibriSpeech) and by N=4 on a hard prompt set. This is not an artifact of one model: the reduction replicates across four open codec-TTS systems and three neural codecs (XCodec2, SNAC, Mimi), reaching the near-zero floor by N=2 on three of the four. We then make the fix free at inference time by distilling the self-verified behaviour into the model, which recovers much of the robustness in single-shot decoding, closing ~52-58% of the failure mass on hard inputs at no test-time cost. The distillation gain concentrates where it is needed (hard inputs); on already-reliable prose there is no headroom and no detectable change. A controlled comparison adds a clean negative: offline direct preference optimization (DPO/IPO) does not beat plain supervised distillation, and an online iterative variant is promising but not statistically separable at our evaluation size. We report honestly the one model that resists (a larger Llasa where scale did not obviously help) and a rare-word capability ceiling that no self-distillation method overcomes

</details>

### [One-Step Token-to-Waveform Generation with MeanFlow in Latent Space](2606.18072.md)
**Zheqi Dai, Guangyan Zhang, Zhen Ye, Jingyu Li et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Neural audio codecs are central to modern LLM-based Text-to-Speech (TTS) and multimodal systems. As low-bitrate semantic codecs gain prominence, the Token-to-Waveform (Token2Wav) decoder becomes a bottleneck determining both perceptual quality and system efficiency. Conventional multi-step flow-matching decoders offer superior quality but suffer from high inference latency due to iterative sampling, creating a severe quality-speed trade-off. In this paper, we propose a novel Token2Wav architecture that overcomes this limitation by applying MeanFlow in a highly compressed latent space. By modeling the average velocity rather than the instantaneous velocity field, MeanFlow enables true one-step generation. Operating in the latent domain mitigates the memory and stability issues of waveform-level flows, yielding up to a 17$\times$ improvement in Real-Time Factor (RTF) compared to multi-step baselines with negligible quality degradation. Furthermore, we introduce refinement strategies that mitigate latent mismatch, including decoder-only fine-tuning with the MeanFlow generator frozen and end-to-end joint fine-tuning, improving fidelity without increasing inference-time cost. Code and demo are publicly available.

</details>

### [Mind Companion: An Embodied Conversational Agent for Process-Based Psychotherapy](2606.17789.md)
**Sofie Kamber, Lukas Diebold, Pascal Riachi, Stella Brogna et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Access to evidence-based psychotherapy remains limited worldwide, with long waitlists even in high-income regions. Recent advances in large language models (LLMs) offer potential for scalable mental health support when designed with clinical oversight and safety mechanisms. We present Mind Companion, an LLM-based embodied conversational agent integrating multi-layered psychological analysis with process-based therapy principles. The system performs real-time analysis of client statements across fact extraction, psychological flexibility process detection, emotion recognition, and safety monitoring. Analysis results are stored for supervising clinicians to inform therapeutic planning. Response generation incorporates retrieval-augmented generation from evidence-based therapeutic literature and context-aware prompting. Responses are delivered through an embodied avatar with synchronized speech synthesis and animation. We evaluated three LLM configurations (GPT-4.1-mini, GPT-5.2, Claude Sonnet 4.5) against therapist responses from real therapy sessions using automated LLM-judge assessment and expert evaluation with 11 professional psychotherapists. GPT-5.2 achieved higher ratings than human therapist responses across understanding, interpersonal effectiveness, collaboration, and therapeutic alignment in both evaluations, demonstrating the feasibility of LLM-based conversational agents as tools to complement clinical care.

</details>

### [PhASE-Flow: Phonetic-Conditioned Acoustic Flow Matching in SSL Representation Domain for Speech Enhancement](2606.17806.md)
**Jun Gao, Xiaobin Rong, Yu Sun, Dahan Wang et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Flow matching (FM) enables high-fidelity generation, while self-supervised learning (SSL) speech models provide hierarchical representations spanning acoustic and phonetic levels. However, existing FM-based speech enhancement (SE) methods operate primarily in the spectral domain, treating SSL features only as external conditions rather than modeling directly in the SSL latent space. To fully exploit the structural richness of SSL representations, we propose PhASE-Flow, an FM-based SE framework that operates entirely in the SSL space. It models the conditional distribution of clean acoustic representations given phonetic ones, reconstructing the waveform via a neural vocoder. Experiments show that PhASE-Flow outperforms state-of-the-art baselines in perceptual quality and intelligibility. Notably, it achieves competitive performance with only four sampling steps, enabling highly efficient inference. Audio demos are available at https://anonymous.4open.science/w/phase-flow_demo-E6E1/.

</details>

### [CraBERT: Efficient Phoneme Encoder Pre-Training via Cascade Fusion of Subword Representations for Text-to-Speech](2606.16668.md)
**Dong Yang, Yuki Saito, Wataru Nakata, Hiroshi Saruwatari** · 2026-06-15

<details>
<summary>Abstract</summary>

This paper introduces CraBERT, a pre-trained phoneme encoder (PPEnc) designed for efficient pre-training in text-to-speech (TTS). CraBERT employs a cascade-fusion architecture and a subword-phoneme alignment algorithm to integrate representations from a pre-trained subword-level BERT into a phoneme-level BERT. This design provides prior word- and sentence-level information, reducing the amount of pre-training required by the phoneme encoder. Subjective listening evaluations show that CraBERT achieves MOS values comparable to existing PPEncs after approximately one epoch of pre-training, whereas the baselines in our comparison are pre-trained for approximately ten epochs. These results demonstrate that CraBERT can efficiently learn representations suitable for improving the perceived naturalness and prosody of synthesized speech.

</details>

### [Joycent: Diffusion-based Accent TTS without Accented Phone Prediction](2606.16417.md)
**Xintong Wang, Ye Wang** · 2026-06-15

<details>
<summary>Abstract</summary>

Accent text-to-speech (TTS) aims to synthesize speech with target accents. Existing accent TTS systems typically rely on a two-stage pipeline that first converts standard phone sequences into accented phone sequences and then synthesizes accented speech. However, such approaches suffer from error accumulation and require paired standard-accented phone sequence data, which is often limited in practice. Moreover, text-based accented phone representations are insufficient to model acoustic accent characteristics such as prosody and rhythm. In this work, we propose Joycent, a diffusion-based accent TTS model that synthesizes accented speech directly from standard phone sequences and speech references without accented phone prediction. Joycent integrates accent and speaker representations through conditional layer normalization (CLN) in the text encoder. We introduce WhisAID, a Mandarin accent identification model trained on accented Mandarin speech to extract accent representations. Experimental results show that Joycent improves accentedness while preserving speaker identity compared with baseline systems. We release our code and demos at: https://github.com/oshindow/Joycent-code.

</details>

### [Probing Low Frame Rate Degradation in Neural Audio Codecs](2606.16969.md)
**Alex Gichamba, Moise Busogi** · 2026-06-15

<details>
<summary>Abstract</summary>

Low frame rates in neural audio codecs are attractive for autoregressive speech synthesis, where the generation cost scales linearly with the sequence length. Recent work has demonstrated that codecs can operate at 12.5 Hz and below, but the mechanisms underlying low frame rate degradation remain insufficiently understood. We investigate these mechanisms through a controlled frame rate ablation. We reproduce a quality cliff at 6.25 Hz reported in previous works and evaluate candidate explanations: phonemic collisions and codebook saturation, neither of which shows evidence of a fundamental barrier. The cliff is instead caused by suboptimal training configuration: fixed clip duration during training yields too few tokens at low frame rates, starving the decoder of inter-token context. Once corrected, WER degrades smoothly with phonemic load down to 3.1 Hz and 1.6 Hz, suggesting the inference-time efficiency gains of low frame rate codecs are more accessible than previously assumed.

</details>

### [Vibrato Expression Control for Singing Voice Conversion with Improving Independent Control](2606.17126.md)
**Joon-Seung Choi, Dong-Min Byun, Seong-Whan Lee** · 2026-06-15

<details>
<summary>Abstract</summary>

Singing style is a crucial aspect of a natural and expressive singing voice. Singers utilize singing styles to convey the feeling or emotion of the songs. Several works have been proposed to control singing style for making the more expressive singing voice. Recently, VibE-SVC successfully controls vibrato by predicting high-frequency F0 contour. In this paper, we introduce a singing voice conversion framework, called VibE-SVC2, to improve singing style conversion performance and controllability. The model offers control over two types of singing styles: a pitch style and a timbre style. For the pitch style, to resolve the pitch-energy entanglement issue that is unresolved in our previous work, we introduce a novel Energy Style Converter to address remaining style information in the energy contour. In addition, we propose a Zero-shot Pitch Style Converter, which mimics the pitch style of reference audio. To expand the controllability of the model, we propose vibrato rate scaling that is an independent control of vibrato extent, which is unavailable in VibE-SVC. For the timbre style, we extend the model to handle a variety of phonation styles. However, addressing specific styles such as vocal fry poses a challenge, as conventional F0 extraction often fails due to their inherent subharmonic characteristics, which degrades the conversion quality. To address this, we propose a novel Subharmonic Correction algorithm to refine the F0 contour for more natural timbre conversion. Through comprehensive objective and subjective evaluations, we demonstrate that VibE-SVC2 provides fine-grained, independent control over two types of singing styles, outperforming existing methods.

</details>

### [Robust Spoofed Speech Detection via Temporal Pyramid Modeling](2606.16837.md)
**Mahtab Masoudi Nezhad, Nima Karimian** · 2026-06-15

<details>
<summary>Abstract</summary>

Spoofed speech detection is increasingly challenged by realistic synthesis, voice conversion, and replay attacks, with cross-dataset generalization remaining a major limitation. This work we propose a Temporal Pyramid Adapter that utilize parallel temporal convolutions with varying receptive fields to capture multi-scale spoofing cues, ranging from local artifacts to global prosodic irregularities. We also integrated self-supervised XLS-R representations combined with front-end adapters, including Mel, Sinc, and a Temporal Pyramid design for multi-scale temporal modeling. The proposed model is evaluated cross multiple benchmark including ASVspoof 2017, ASVspoof 2021 (DF/LA), PartialSpoof, DiffSSD, and multilingual HQ-MPSD datasets. Experimental results demonstrate that Temporal Pyramid model obtained AUC of 99.24% and a EER of 3.87% on the PartialSpoof database, which is significantly outperforming the base model and several SOTA baseline such as LCNN-BLSTM (9.87% EER) and TRACE (8.08% EER). Additionally, multilingual evaluations confirm that while spoofing artifact are independent from language. While self-supervised representations improve robustness, performance degrades under domain and language shifts, highlighting the need for better adaptation and calibration strategies.

</details>

### [Dynamic Prosody Prediction in LLM-based TTS for Improving Speaker Similarity](2606.15267.md)
**Zhenwei Mou, Liping Chen, Yajun Hu, Zhen-Hua Ling et al.** · 2026-06-13

<details>
<summary>Abstract</summary>

Personalized text-to-speech (TTS) aims to clone the target speaker in the synthesized speech, imitating both the voice and speaking style. Current large language model (LLM)-based TTS methods ignore the style-specific prosodic patterns in generated speech, resulting in deficient style learning and thus limiting speaker similarity in synthesized speech. To this end, we investigate the prosody learning conditioned on the synthesized speech, and propose to predict the prosody of the current syllable based on previously predicted speech. Experimental results obtained on three datasets demonstrated the efficacy of the proposed dynamic prosody prediction method in enhancing the prosody learning capability, thereby improving the speaker similarity of the generated speech. Audio samples are available at https://muzw.github.io/dynapros/.

</details>

### [DuraMark: Duration-Embedded Watermarking in LLM-based TTS](2606.15264.md)
**Zhenwei Mou, Weili Jiang, Liping Chen, Zhen-Hua Ling et al.** · 2026-06-13

<details>
<summary>Abstract</summary>

Large language model (LLM)-based text-to-speech (TTS) models have achieved remarkable voice cloning capabilities, raising concerns about potential deepfake misuse. Speech watermarking mitigates this by embedding traceable information into generated speech. Mainstream watermarking methods operate at the signal level (waveform or spectrogram), rendering the watermark vulnerable to generative attacks (e.g., neural codec and vocoder). To address this, we propose DuraMark, a robust information-level watermarking framework. It utilizes syllable duration editing to achieve watermark embedding. Specifically, DuraMark integrates a duration-controllable LLM-based TTS model to edit syllable durations during synthesis, coupled with a duration extractor to extract these durations for detection. Experiments demonstrate DuraMark's superior robustness against generative attacks, significantly outperforming signal-level baselines. Audio samples are available at https://muzw.github.io/duramark_demo/.

</details>

### [VoxWatermark: A Large-Scale Benchmark for Audio Watermark Detection under Perturbations](2606.15187.md)
**Farnaz Sedaghati, Yuxi Wang, Zicheng Weng, Wei Rao** · 2026-06-13

<details>
<summary>Abstract</summary>

With the rapid deployment of speech generation systems in open environments, providing verifiable source attribution and copyright accountability for audio content has become critical. A gap in current research is the lack of a unified benchmark that systematically compares different watermark injection methods under realistic distribution shifts. To address this, we build VoxWatermark by applying 10 watermarking methods (4 neural and 6 traditional) with unified injection and annotation on multilingual, multi-source corpora, and introducing no-box, black-box, and white-box perturbations to simulate real recording and transmission conditions. Based on this benchmark, we propose AudioWMD as a robust baseline detector for large-scale, multi-method, cross-distribution settings. Results show that injection-method diversity and distribution shifts affect detection stability, while validating the effectiveness and scalability of AudioWMD. Dataset and code are publicly available.

</details>

### [Mask, Sample, Revise: A Revisable CTMC Inference Stack for Guided Discrete Flow Matching Text-to-Speech](2606.13989.md)
**Alef Iury Siqueira Ferreira, Lucas Rafael Stefanel Gris, Luiz Fernando de Araújo Vidal, Frederico Santos de Oliveira et al.** · 2026-06-12

<details>
<summary>Abstract</summary>

Recent alignment-free non-autoregressive (NAR) text-to-speech (TTS) models formulate synthesis as a conditional infilling task, bypassing explicit duration predictors and external aligners. When speech is represented with neural codec tokens, the infilling problem becomes discrete, making Discrete Flow Matching (DFM), a Continuous-Time Markov Chain (CTMC) framework for discrete generation, a natural fit. However, inference-time control for stable low-step conditional infilling remains underexplored. We propose Mask, Sample, Revise, an inference-time CTMC stack for alignment-free DFM-TTS. The stack combines predictor-free guidance to strengthen text conditioning, prompt-matched conditional coupling to align the probability path with the acoustic prompt, and SC-ReMask, a schedule-constrained remasking mechanism that introduces token-to-mask transitions so early de-masking decisions can be revised. These components require no post-hoc fine-tuning and operate in a single tau-leaping sampler. Controlled ablations show that this stack improves intelligibility and robustness in the low-NFE prompted setting, outperforming unguided and guidance-only samplers with substantially more steps.

</details>

### [Unsupervised Approaches for Global Prosodic Embedding Extraction](2606.14004.md)
**Martin Meza, Luciana Ferrer, Pablo Riera** · 2026-06-12

<details>
<summary>Abstract</summary>

Prosody is central to oral communication, conveying information like the emotional state of the speaker and cues needed for meaning disambiguation. Many self-supervised models of speech produce embeddings that encode prosodic as well as linguistic, and speaker information. This entanglement of information is problematic in scenarios where prosody is the main distinguishing factor while other factors may vary between training and deployment; in such cases, a purely prosodic representation would be more robust. Such representation could also be used for analyzing the role of prosody in a given task or as input to speech synthesis systems. In this work, we propose a variety of approaches for producing global prosodic embeddings based on auto-encoder models of pitch and energy. We develop a benchmark for assessing the performance of these representations, showing that our embeddings provide competitive or superior performance under challenging conditions, compared to various alternatives.

</details>

### [From Self-Supervised Speech Models to Mixture-of-Experts for Robust Anti-Spoofing](2606.14639.md)
**Hugo Daumain, Driss Matrouf, Khaled Khelif, Mickael Rouvier** · 2026-06-12

<details>
<summary>Abstract</summary>

Recent advances in speech generation have significantly improved the naturalness of synthetic speech, making spoofing detection increasingly challenging. A key limitation of current anti-spoofing systems is their limited robustness to unseen synthesis methods. In this work, we transform a self-supervised speech representation model into a Mixture-of-Experts (MoE) architecture to improve generalization. Feed-forward blocks in selected encoder layers are replaced by multiple expert networks controlled by a layer-wise gating mechanism, allowing experts to capture complementary acoustic patterns while preserving the representations learned during self-supervised pretraining. We further analyze the architectural choices affecting the performance of this MoE conversion and investigate the activation behavior of the experts. The proposed approach is evaluated on 14 spoofing datasets and reduces the macro EER from 5.46% to 4.81%, corresponding to 11.9% relative improvement over the baseline.

</details>

### [An Empirical Study on Learning Latent Representations for Emotional Speech Synthesis](2606.14922.md)
**Vinh Dang Quang, Huy Ngo Quang** · 2026-06-12

<details>
<summary>Abstract</summary>

For the last couple of years, the field of speech synthesis has improved dramatically thanks to deep learning. There are more and more deep learning-based TTS systems developed to make it possible to produce voices with high intelligibility and naturalness. Meanwhile, controlling the expressiveness is yet a big deal, generating speech in different styles or manners has received a lot of attention from community recently. This paper aims to give our solutions to deal with the task emotional speech synthesis (ESS) at VLSP 2022 which allows to generate humanlike natural-sounding voice from a given input text with desired emotional expression. By integrating speaker embedding, prosody bottleneck into FastSpeech 2, our systems can promisingly generate emotional speech of a single speaker (Sub-task 1), transfer speaking styles from another speaker to the target speaker with neutral non-expressive data while retaining the target speaker's identity (Sub-task 2).

</details>

### [From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation](2606.13630.md)
**Pedro Correa, Olivier Perrotin, Samir Sadok, Paula Costa et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

The choice of speech representation is critical in speech-driven 3D facial animation. Representations differ in what they encode: SSL features emphasize segmental and semantic cues, neural codecs yield latents optimized for acoustic reconstruction, and ASR-style objectives produce label-based spaces. We evaluate four speech representation families for 3D facial synthesis, comparing their facial reconstruction quality across two facial decoders using objective metrics and a perceptual evaluation. We additionally conduct probing analyses that relate tokenized representations to phonetic units and to articulatory deformations. We found that encoding phonetic classes is beneficial for accurate facial animation prediction on both semantic and label-based representations with comparable facial animation quality. From the latter, we introduce an Audio Visual Text-to-Speech (AVTTS) pipeline that leverages, as a shared space, discrete representations to decode speech and 3D facial motion.

</details>

### [TimeLens: On-Device Artifact Recognition with Retrieval-Augmented Question Answering for the Grand Egyptian Museum](2606.13267.md)
**Rawan Hesham, Ali Ashraf, Amr Ahmed, Malak Alaa et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

TimeLens is an AI-powered bilingual mobile guide for the Grand Egyptian Museum (GEM). Pointing a phone at an exhibit, a visitor sees the artifact recognized in real time and can ask follow-up questions answered in English or Arabic. The work addresses three problems specific to in-gallery deployment: fine-grained visual similarity among 51 catalogued artifacts (many near-identical Ramesside statues), the gap between curated training data and handheld camera conditions, and the risk of an AI guide stating unsupported historical facts. Two engineering contributions are reported. First, an on-device artifact detector was developed through a data-quality-driven iteration study -- from foundation-model auto-annotation (YOLO-World), through spatial label-cleaning rules, to a fully hand-annotated dataset -- isolating label quality as the decisive factor: the final YOLOv8n model resolves every previously failing class while remaining a 5.97 MB TensorFlow Lite asset that runs in real time on a mid-range phone (mAP@0.5 = 0.995, mAP@0.5:0.95 = 0.924). Second, a bilingual Retrieval-Augmented Generation (RAG) guide, grounded in a 108-record ChromaDB knowledge base, was benchmarked across seven candidate language models, with Gemma 4 E2B (Q4 K M) selected; ten targeted optimizations reduce end-to-end latency from over 30 s to approximately 10 s. Both subsystems are integrated in a production Flutter application with bilingual interface, museum location gating, and text-to-speech support.

</details>

### [Emo-LiPO: Listwise Preference Optimization for Fine-Grained Emotion Intensity Control in LLM-based Text-to-Speech](2606.13006.md)
**Yihang Lin, Li Zhou, Congwei Cao, Dongchu Xie et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

Large language model (LLM)-based text-to-speech (TTS) systems enable prompt-conditioned emotional control but struggle with fine-grained emotion intensity due to the semantic -- acoustic gap between text and speech. To address this challenge, we formulate emotion intensity control in LLM-based TTS as a learning-to-rank problem and propose Emo-LiPO, a listwise preference optimization framework that aligns prompt-conditioned speech generation with relative emotion intensity expressed in text. Emo-LiPO explicitly models global intensity ordering within each emotion under fixed transcripts, enabling more faithful and continuous emotional expression. We further construct ESD-plus, a multi-speaker dataset with explicit emotion intensity variations, to support fine-grained emotion modeling and evaluation. Experiments on ESD-plus demonstrate that Emo-LiPO significantly improves emotion accuracy and intensity controllability over both supervised- and DPO-based LLM TTS baselines, with particularly pronounced gains at high intensity levels.

</details>

### [PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue](2606.12902.md)
**Wen Zhang, Xiaocui Yang, Zhuoyue Gao, Shi Feng et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

Empathetic spoken dialogue systems require not only semantically appropriate responses but also emotionally aligned prosodic expression. However, cascade pipelines often discard acoustic cues during speech-to-text conversion, while end-to-end speech models lack interpretable control over emotion and knowledge integration. To address these challenges, we propose PRISM, a multi-agent framework for empathetic spoken dialogue that decouples speech perception, response generation, and speech synthesis into coordinated components. PRISM introduces a prosody-to-language translation mechanism to stabilize large language model reasoning and enables on-demand invocation of external knowledge tools for empathetic dialogue generation. Experimental results demonstrate that PRISM achieves consistent improvements in empathy, prosodic appropriateness, and text response generation quality across objective and subjective metrics. Our code is available at: https://github.com/Bxzfrm/PRISM.

</details>

### [Vocal Identity Under Siege by AI Voice Cloning Technologies](2606.12812.md)
**Jyh-An Lee, Xuan Sun** · 2026-06-11

<details>
<summary>Abstract</summary>

The advent of sophisticated AI-driven voice cloning has brought to the fore critical legal and ethical challenges regarding the protection of vocal identity. Prompted by recent controversies - including the striking resemblance between OpenAI's ChatGPT-4o voice and that of Scarlett Johansson - this article examines how generative AI technologies undermine the unique value of the human voice and further complicate the legal questions surrounding personality right. Through a comparative analysis, the paper evaluates three principal legal frameworks: the right of publicity, personality rights, and the personal data protection right. Each framework - rooted in different legal traditions o offers distinct strengths and limitations in addressing the threats posed by AI-generated voice cloning. By analysing these doctrines' scope, remedies, and posthumous protections, the study offers a foundation for understanding how existing legal approaches may be applied to the evolving challenges of vocal identity in the era of generative AI.

</details>

### [M*: A Modular, Extensible, Serving System for Multimodal Models](2606.12688.md)
**Atindra Jha, Naomi Sagan, Keisuke Kamahori, Irmak Sivgin et al.** · 2026-06-10

<details>
<summary>Abstract</summary>

We are entering a new era of composite model architectures that integrate diverse components such as vision encoders, language backbones, diffusion and flow heads, audio codecs, action generators, and world-model predictors. Such architectures underpin a broad class of multimodal models, including unified multimodal models, omni models, speech-language models, vision-language-action policies, and world models. However, existing model serving frameworks were built on narrow assumptions about model structure, making them ill-suited to accommodate this new architectural diversity. Here we present M*, a universal serving system for efficient serving of composite AI models. M* represents models as dataflow graphs, processing requests spanning diverse modalities and tasks as traversals over these graphs. The core insight is a modular abstraction that supports arbitrary composition of model components, flexible placement onto a physical cluster, and model-agnostic optimizations within a distributed runtime. We call this abstraction the Walk Graph and show how it can concisely capture composite models from a broad range of families. We instantiate M* on representative models and find that it achieves, on average, 20% lower end-to-end latency than vLLM-Omni for text-to-image workloads on BAGEL, while delivering up to 2.9x lower real-time factor and 2.7x higher throughput for text-to-speech workloads on Qwen3-Omni. M* also outperforms the V-JEPA 2-AC rollout baseline for robotic planning by up to 12.5x. Thus, our work paves the road towards more efficient serving of complex models with minimal developer effort.

</details>

### [UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction](2606.11681.md)
**Sangmin Lee, Eekgyun Ahn, Woongjib Choi, Hong-Goo Kang** · 2026-06-10

<details>
<summary>Abstract</summary>

We propose UR-BERT, a Romanized transcription-based text-to-speech (TTS) encoder for massively multilingual TTS systems. Conventional grapheme-to-phoneme (G2P)-based approaches are limited to around 100 languages due to the availability of reliable G2P resources. In contrast, UR-BERT scales to 495 languages by unifying diverse writing systems into a shared Romanization representation. To further enhance phonetic fidelity and text-speech alignment, we introduce a speech token prediction objective during training, which encourages the encoder to learn speech-aware phonetic representations in a data-efficient manner. Experiments show that TTS systems built on UR-BERT consistently outperform recent text encoder baselines across a wide range of languages and resource conditions, and demonstrate strong generalization to unseen languages.

</details>

### [SARA: A Dual-Stream VAE for High-Fidelity Speech Generation via Integrating Semantic and Acoustic Representations](2606.11611.md)
**Peijie Chen, Wenhao Guan, Weijie Wu, Kaidi Wang et al.** · 2026-06-10

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) relies on robust speech representations. However, current speech tokenizers face a fundamental trade-off: acoustic codecs preserve high-fidelity audio but lack linguistic constraints, causing content errors during generation, whereas semantic tokens from self-supervised learning (SSL) models ensure precise text alignment but discard some acoustic information. To bridge this gap, we propose SARA, a dual-stream VAE that directly fuses a frozen SSL semantic anchor with a dedicated residual acoustic encoder. This effectively mitigates the dilemma, creating an efficient and compact latent space without relying on complex regularizers. SARA achieves superior reconstruction quality over strong baselines. Furthermore, in downstream zero-shot TTS tasks, it yields highly natural and expressive synthesis quality, and maintains robust generation performance even under accelerated inference, offering a favorable trade-off between synthesis speed and computational cost.

</details>

### [Anchoring the Unknown: Open-Set Model Attribution via Proxy-Anchor Learning](2606.10758.md)
**Cristian-Teodor Neamtu, Serban Mihalache, Stefan Smeu, Dan Oneata et al.** · 2026-06-09

<details>
<summary>Abstract</summary>

The proliferation of text-to-speech (TTS) systems capable of generating realistic synthetic speech poses growing challenges for audio forensics. While binary deepfake detection has received considerable attention, source tracing (i.e., identifying which TTS system produced a given audio sample) remains underexplored, particularly in open-set scenarios where unknown systems may be encountered. We propose a metric learning framework based on the Proxy-Anchor loss function that operates on Wav2Vec2-BERT embeddings to learn a discriminative embedding space for TTS source attribution and out-of-distribution (OOD) detection of unseen systems. We evaluate it on the MLAAD v9 dataset spanning 140 TTS systems across 51 languages, and introduce an architecture merging strategy that groups TTS system versions into unified classes, reducing inter-class confusion. Our system achieves 99.76% accuracy on 110 in-distribution classes and a False Positive Rate (FPR@95) as low as 2.04% for OOD detection. Also, for a fair comparison against the current state of the art, we further evaluate it on the MLAAD v5 official dataset splits, improving the OOD accuracy by almost doubling it. These results demonstrate that Proxy-Anchor metric learning, combined with architecture-aware class design and post-hoc OOD scoring, provides an effective framework for forensic TTS source tracing in both closed-set and open-set settings.

</details>

### [SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space](2606.10317.md)
**Tomoya Tanabu, Hiroshi Nishijima, Daisuke Saito, Nobuaki Minematsu** · 2026-06-09

<details>
<summary>Abstract</summary>

We introduce SSL-GMMVC, an interpretable voice conversion method in self-supervised speech space. The method models paired source-target features with a Gaussian mixture model and performs conversion as a posterior-weighted sum of affine transforms. This yields locally linear transformations that adapt to heterogeneous feature-space structure while remaining analytically tractable. Through objective and subjective evaluations, we show that SSL-GMMVC improves speaker similarity with comparable intelligibility and naturalness, and that even a constrained covariance variant surpasses a deep learning baseline as the number of mixture components increases. Further analyses link component selection to phonetic structure and reveal interpretable scaling and rotation in the learned transforms. These findings highlight SSL-GMMVC as an effective, analyzable framework for voice conversion.

</details>

### [Interpreting and Steering a Text-to-Speech Language Model with Sparse Autoencoders](2606.10029.md)
**Nikita Koriagin, Georgii Aparin, Nikita Balagansky, Daniil Gavrilov** · 2026-06-08

<details>
<summary>Abstract</summary>

Language models increasingly serve as the backbone of text-to-speech (TTS) systems, yet we understand little about the representations they build when text and generated speech tokens share a single residual stream. We train BatchTopK sparse autoencoders on the LM backbone of CosyVoice3 and introduce a modality-aware auto-interp pipeline that labels each feature from where it fires-text-prefix context, 1-second speech clips, or both. The recovered features are interpretable, spanning phonemes, laughter, accent prompts and speaker gender. Steering through the SAE latent space shows these features are causal rather than merely descriptive: targeted interventions raise laughter probability from 0.02 to 0.79, flip perceived speaker gender, and control speech rate while preserving spoken content. SAE features thus serve both as interpretability objects and as control directions for TTS synthesis.

</details>

### [What Makes Synthetic Speech Sound Sarcastic? A Prosody-Controlled Perception Study](2606.09717.md)
**Zhu Li, Shekhar Nayak, Matt Coler** · 2026-06-08

<details>
<summary>Abstract</summary>

Prosody plays a central role in sarcasm perception, yet previous studies have relied on naturally produced speech that lacks fine-grained control over individual acoustic dimensions. As prosodic cues co-vary in natural data, isolating their independent contributions remains challenging. We introduce a controlled framework using neural text-to-speech (TTS) with prompt-based prosodic conditioning to manipulate speech rate, pitch variation, and loudness. An orthogonal stimulus set was constructed to enable causal testing of prosodic cue effects. Human listeners rated sarcasm and naturalness, and their judgments were compared with predictions from a foundation model capable of processing audio input. Results show that loudness primarily drives human sarcasm perception, whereas the model assigns greater weight to speech rate, leading to distinct cue-weighting patterns. This study shows how controllable neural TTS enables investigation of prosodic cue weighting in speech perception.

</details>

### [Optimality of FSQ Tokens for Continuous Diffusion for Categorical Data with Application to Text-to-Speech](2606.09962.md)
**Vadim Popov, Wenju Gu, Tasnima Sadekova, Georgii Aparin et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Continuous diffusion for categorical data is a framework belonging to the diffusion family and aiming at generating discrete data. The scientific interest to such models has been constantly increasing these days because researchers try to achieve a challenging goal of finding reasonable alternatives to autoregressive large language models. In this paper, we study the properties of the structure of the latent space corresponding to discrete tokens expressed in terms of Kullback-Leibler divergence on diffusion path measures and accuracy of the correct token prediction by the optimally trained diffusion model. We find that FSQ tokenization scheme has the latent space structure with the properties that make it best suited for continuous diffusion for categorical data as verified through rigorous theoretical analysis and numerical experiments. To validate our findings in real-life scenario, we train several text-to-speech diffusion models having speech tokens as intermediate acoustic features, and show that the one based on FSQ tokens indeed performs the best, and, moreover, it outperforms its strong LLM-based counterpart, at the same time being significantly smaller and faster.

</details>

### [OpenBibleTTS: Large-Scale Speech Resources and TTS Models for Low-Resource Languages](2606.09553.md)
**David Guzmán, Luel Hagos Beyene, Jesujoba Oluwadara Alabi, Yejin Jeon et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Recent advances in neural text-to-speech (TTS) and multilingual speech generation have substantially improved synthetic speech quality, yet these gains remain unevenly distributed across the world's languages. Existing models are still dominated by a small set of high-resource languages, while many studies of low-resource TTS are simulated on artificially downsampled high-resource corpora that do not reflect the orthographic variation and limited phonetic coverage encountered in genuinely underrepresented settings. As such, we introduce OpenBibleTTS, which is a large-scale benchmark for low-resource speech synthesis spanning 37 underrepresented languages. Moreover, a systematic comparison of various TTS architectures and large-scale speech generation models is conducted across in-domain Biblical text and out-of-domain material. Results show that no single system dominates across languages and metrics: Gemini-TTS achieves the highest listener ratings on most evaluated languages, but monolingual EveryVoice models trained on OpenBibleTTS remain strongest for intelligibility and are preferred in several African languages, while open from-scratch systems degrade sharply on out-of-domain text, revealing a persistent gap between broad multilingual coverage and reliable synthesis quality in underserved linguistic communities. We complement automatic evaluation with subjective human judgments, and open-source all processed datasets, alignments, and trained models to support future low-resource TTS research.

</details>

### [NüshuVoice: Reviving the Voice of Endangered Nüshu with Pitch-Aware Text-to-Speech](2606.09295.md)
**Hongkun Yang, Xinhui Yi, Xiyan Zhao, Yibo Meng et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Nüshu is an endangered phonetic script historically used by women in Jiangyong County, southern Hunan, China. While existing computational studies of Nüshu mainly focus on textual digitization and visual recognition, the acoustic reconstruction of its authentic pronunciation remains largely unexplored. Building a Nüshu text-to-speech (TTS) system is particularly challenging because available recordings are extremely limited and mostly consist of isolated syllable-level pronunciations rather than natural sentence-level utterances. In this work, we introduce NüshuVoice, the first TTS benchmark for Nüshu. We construct a sentence-level Nüshu text-to-audio dataset that aligns standardized Unicode Nüshu text, phonetic transcriptions, standard Chinese translations, and archival recordings. To synthesize speech under this extreme low-resource setting, we propose Nüshu-PitchVITS, an F0-conditioned VITS framework that leverages Nüshu's five-level pitch notation as an explicit prosodic inductive bias. Experimental results show that Nüshu-PitchVITS outperforms strong TTS baselines in spectral fidelity, pitch reconstruction, and human-rated intelligibility. We publicly release the dataset and code at: https://anonymous.4open.science/r/Nvshu-TTS-2EB6.

</details>

### [End-to-End Training for Discrete Token LLM based TTS System](2606.09234.md)
**Changfeng Gao, Yong Ren, Jun Yuan, Ye Bai et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Recent state-of-the-art (SOTA) text-to-speech (TTS) systems typically adopt a cascaded pipeline consisting of a speech tokenizer, an autoregressive large language model (LLM), and a diffusion based flow-matching (FM) model, with these components trained independently. In this paper, we propose a fully end-to-end (E2E) optimization framework that unifies the training of the speech tokenizer, LLM, FM model, and an additional reward model (RM). Specifically, we first jointly optimize the tokenizer using multi-task objectives derived from reconstruction for FM, next-token prediction for LLM, and multi recognition task for RM. This joint training encourages the discrete speech token space to capture acoustically and semantically salient information that is better tailored to TTS. We then further optimize the LLM using downstream reconstruction and recognition by FM and RM, which reduces inference-time mismatch and steers the LLM toward more preferred generations. Experimental results show that our E2E framework consistently outperforms cascaded baselines. On the Seed-TTS-Eval benchmark, our system achieves a word error rate (WER) of 0.78% and 1.56%, a new SOTA result with a 0.6B-parameter LLM and 0.5B-parameter FM model. These results validate that holistic E2E optimization is critical for improving discrete-token-based TTS systems with a much simpler training pipeline.

</details>

### [FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation](2606.09141.md)
**Hanke Xie, Xiaming Ren, Dake Guo, Ruonan You et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Recent progress in speech dialogue systems requires Text-to-Speech (TTS) models to be faster and more responsive. Modern speech dialogue systems impose two primary requirements on TTS models: low latency and support for streaming inputs and outputs. However, most existing single-codebook LLM-based TTS methods rely on multi-stage pipelines that lack native streaming capabilities. These systems typically suffer from high end-to-end latency due to slow autoregressive prediction and multi-step flow matching. To address these limitations, we propose FlashTTS, an open-source and low-latency streaming TTS framework. FlashTTS introduces a lagged multi-track architecture that natively processes streaming text and speech inputs, thereby eliminating the need for sentence-level buffering. To accelerate acoustic generation, we integrate parallel Multi-Token Prediction (MTP) with an X-pred mean flow matching decoder. This configuration achieves high-fidelity token-to-mel generation in exactly two function evaluations (2-NFE). By jointly optimizing input processing and decoding efficiency, FlashTTS offers a practical foundation for real-time speech dialogue systems. Experiments show that FlashTTS substantially reduces First-Packet Latency to 325ms compared to robust streaming baselines, all while preserving strong zero-shot voice cloning and cross-lingual intelligibility. Speech samples are available. The model code and checkpoints will be released as open source.

</details>

### [HoliDubber: Holistic Video Dubbing for Complex Acoustic Scenes via Text-Guided Audio Synthesis](2606.09098.md)
**Wenhao Guan, Yifan Duan, Junxi Liu, Yu Gu et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Video dubbing is a cornerstone of multimedia content creation, aiming to synthesize synchronized acoustic sequences for visual streams. While Text-to-Speech (TTS) and Text-to-Audio (TTA) generation have each achieved remarkable progress, existing dubbing systems remain confined to isolated speech synthesis without incorporating sound effects and ambient audio, forcing practitioners to rely on fragmented workflows and laborious manual post-mixing. To address this limitation, we present HoliDubber, a holistic video dubbing framework that moves beyond speech-only generation by enabling the joint synthesis of speech and sound effects from a single text prompt. Specifically, HoliDubber adopts a patch-based autoregressive diffusion transformer architecture, where a causal language model autoregressively models aggregated patch embeddings to capture global temporal structure, and a Diffusion Transformer decoder generates high-fidelity continuous tokens within each patch, following a divide-and-conquer strategy. To achieve cross-modal alignment, visual features are encoded into patch-level representations and fused with audio patches via cross-attention, enabling the model to ground speech generation in the speaker's visual articulation dynamics. In addition, we introduce HoliDub-Bench, a benchmark curated from established datasets with synchronized video-text-audio triplets designed for holistic dubbing evaluation. Extensive experiments demonstrate that HoliDubber significantly outperforms existing methods across multiple benchmarks in speech quality, synchronization, and speaker similarity. Furthermore, results on HoliDub-Bench validate the effectiveness of joint speech-and-sound generation, establishing a new paradigm for holistic video dubbing in complex acoustic scenes. \footnote{The demo page of the project is https://holidubber.github.io}

</details>

### [BareWave: Waveform-Native Flow-Matching Text-to-Speech](2606.09048.md)
**Wei Fan, Chao-Hong Tan, Qian Chen, Wen Wang et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Removing intermediate representations and separately trained decoding stages has become an important direction in generative modeling. In text-to-speech, however, high-quality systems are still commonly built through an intermediate acoustic representation before waveform synthesis. In this work, we present BareWave, a fully waveform-native framework for direct text-to-wave generation in flow-matching TTS. We consider this setting to raise three training challenges: raw-waveform modeling lacks a strong pretrained representational scaffold, different stages of training benefit from different noise schedules, and data-space perceptual objectives do not automatically share the temporal structure of the velocity-space flow objective. As a result, direct waveform training is hard to optimize efficiently, hard to push toward a strong final operating point with a fixed recipe, and hard to integrate effective perceptual refinement. Guided by this view, we develop a direct text-to-wave training framework that combines training-time representation alignment, staged noise scheduling, and velocity-aware perceptual alignment (VAPA), while preserving a single waveform-native inference path without pretrained components at test time. Experiments on zero-shot voice cloning show that strong intelligibility, speaker similarity, and naturalness can be achieved under a fully waveform-native inference path, supporting waveform-native flow-matching TTS as a practical direction. Project page with audio demos is available at https://barewave.github.io/.

</details>

### [TLDR: Compressing Audio Tokens for Efficient Autoregressive Text-to-Speech](2606.09019.md)
**Yejin Lee, Junwon Moon, Hyoeun Kim, Hyunjin Choi et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Codec-based autoregressive (AR) speech language models have achieved strong text-to-speech (TTS) quality by modeling speech as sequences of discrete audio tokens with large pretrained backbones. However, this token-level formulation creates a structural efficiency bottleneck: speech-token sequences are much longer than text sequences, requiring the AR backbone to perform causal computation at every token position and maintain a KV cache that grows with the sequence length. We introduce TLDR, a patch-based autoregressive framework that accelerates codec-based AR-TTS by shifting the causal modeling from token-level speech sequences to patch-level sequences. TLDR groups consecutive codec tokens into compact latent patches using a lightweight compressor, models the resulting shorter patch sequence with a frozen pretrained AR-TTS backbone adapted by LoRA, and reconstructs fine-grained speech tokens within each patch using a speaker-conditioned extractor. With a patch size of 4, TLDR achieves a 1.8x inference speedup over the baseline AR-TTS model and reduces global KV-cache memory by up to 75%. Experimental results indicate that patch-level global causal modeling can be a practical way to reduce the inference cost of pretrained codec-based AR-TTS systems without replacing the existing modules.

</details>

### [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](2606.09667.md)
**Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.

</details>

### [MeanVC 2: Robust Low-Latency Streaming Zero-Shot Voice Conversion](2606.09050.md)
**Guobin Ma, Yuxuan Xia, Yuepeng Jiang, Dake Guo et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Streaming zero-shot voice conversion (VC) has become increasingly popular due to its potential for real-time applications. The recently proposed MeanVC achieves lightweight streaming zero-shot VC, but it has several limitations: its chunk-wise autoregressive denoising doubles the effective training sequence length, conversion quality degrades under small-chunk settings, and its timbre encoder directly relies on reference mel-spectrograms, making it sensitive to reference audio quality. To address these limitations we propose MeanVC 2. We introduce future-receptive chunking (FRC), which explicitly schedules past and future receptive fields across diffusion transformer decoder layers and removes clean-chunk teacher forcing. By incorporating bounded future context, FRC enables stable conversion with a 40 ms chunk size. We further introduce a universal timbre token encoder, which constructs a timbre representation from a global speaker embedding and retrieves fine-grained timbre cues via cross-attention, improving robustness to low-quality references and enhancing zero-shot speaker similarity. Experimental results show that MeanVC 2 significantly outperforms MeanVC, while reducing latency from 211 ms to 110 ms. Audio samples are publicly available. The source code will be publicly released.

</details>

### [EmoInstruct-TTS: Dual-Path Instruction-Guided Emotional Speech Synthesis](2606.20650.md)
**Minghui Wu, Ganjun Liu, Zikun Fang, Ting Meng et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Instruction-based controllable speech synthesis enables users to specify emotions through natural language. However, existing approaches often rely on coarse emotion labels and lack explicit modeling of fine-grained intensity. We propose EmoInstruct-TTS, a dual-path instruction-guided framework for emotional speech synthesis. We introduce Emotion2embed, a supervised semantic-acoustic emotion embedding covering 48 emotional states, including fine-grained categories and intensity levels. To infer embeddings from free-form instructions, we design an Instruction-Conditioned Emotion Flow Model (ICE-Flow) that generates acoustically grounded emotion representations. The inferred embeddings are integrated into an LLM-based synthesis pipeline to provide explicit emotional control while preserving semantic planning. Experiments show improved emotional controllability and speech naturalness over strong baselines.

</details>

### [Audio-Oscar: A Multi-Agent System for Complex Audio Scene Generation, Orchestration, and Refinement](2606.07397.md)
**Yifan Duan, Qixiang Xu, Hengtao Wu, Zhanxun Liu et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

In recent years, audio generation has made significant progress in tasks such as text-to-speech (TTS), text-to-audio (TTA) and text-to-music (TTM). However, generating long-form and controllable audio from complex audio scene descriptions remains a significant challenge, as such scenes often require coordinated speech, sound effects, music, songs, temporal structure, and post-production. In this work, we introduce \textbf{Audio-Oscar}, a multi-agent framework for generating audio from complex descriptions. Audio-Oscar coordinates a set of specialist agents, each responsible for a different aspect of the audio scene, including character modeling and voice design, speech generation, fine-grained timeline planning, model selection, non-speech generation, and audio post-production. Audio-Oscar further incorporates feedback-driven refinement. In addition, to address the lack of suitable benchmarks for evaluating audio generation from complex audio scene descriptions, we construct \textbf{ASG-Bench}, an Audio Scene Generation Benchmark containing both scene descriptions paired with reference audio and text-only scene descriptions. Each scene is annotated with target audio events and temporal statements to evaluate whether the generated audio faithfully realizes the required scene content and temporal structure. Experimental results show that Audio-Oscar can effectively generate audio that matches complex scene descriptions. Project samples are available at https://audiooscar.github.io/. Our code is available at https://github.com/ziye26/Audio-Oscar.

</details>

### [KIT's Submission to Cross-Lingual Voice Cloning in IWSLT 2026](2606.07240.md)
**Seymanur Akti, Alexander Waibel** · 2026-06-05

<details>
<summary>Abstract</summary>

Cross-lingual voice cloning aims to generate speech in a target language while preserving speaker identity from a source-language reference. This task is central to speech translation and is the focus of the IWSLT 2026 Cross-Lingual Voice Cloning track. A key challenge is maintaining intelligibility and naturalness in the presence of accent variation and domain-specific vocabulary. We build on a multilingual text-to-speech model, FishAudio-S2-Pro, and introduce language tag prompting to improve language control and reduce accent leakage. We further apply reinforcement learning (RL) fine-tuning for task adaptation and observe improvements in intelligibility. Finally, we propose a reference-conditioned lexical matching method that improves pronunciation of domain-specific terms when lexical overlap is present. Results show that language prompting provides the largest gains, while lexical matching yields consistent improvements on matched subsets.

</details>

### [dots.tts Technical Report](2606.07080.md)
**Shi Lian, Changtao Li, Bohan Li, Hankun Wang et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

We present dots.tts, a 2B-parameter continuous autoregressive text-to-speech (TTS) foundation model that models speech in a continuous latent space. Compared with existing continuous autoregressive models, our key innovations are threefold. First, we train an AudioVAE with multiple objectives to build a semantically structured and prediction-friendly continuous speech space. Second, we use full-history conditioning in the flow-matching head to preserve long-range consistency and reduce drift during generation. Third, we apply reward-free self-corrective post-training to the flow-matching head to further improve robustness and acoustic quality. After being trained on a large-scale multilingual corpus, dots.tts achieves the best average performance on Seed-TTS-Eval, with WERs of 0.94%/1.30%/6.60% and SIM scores of 81.0/77.1/79.5 on the zh/en/zh-hard test sets, respectively. Across other benchmarks, dots.tts also consistently demonstrates open-source state-of-the-art performance, exhibiting strong generation stability, voice cloning ability, and emotional expressiveness. For efficient inference, we further apply CFG-aware MeanFlow distillation, enabling low-latency speech generation with first-packet latencies of 85/54 ms in output streaming and dual-streaming modes, respectively. To facilitate reproducible research and practical deployment, we release the training and inference code, together with the pretrained, post-trained, and MeanFlow-distilled checkpoints, under the Apache 2.0 license.

</details>

### [Leveraging Soft Distributions of SSL-Derived Discrete Speech Tokens for Downstream Inference](2606.06806.md)
**Kentaro Onda, Satoru Fukayama, Daisuke Saito, Nobuaki Minematsu** · 2026-06-05

<details>
<summary>Abstract</summary>

Discrete speech tokens obtained from self-supervised learning (SSL) models provide efficient data compression while maintaining strong performance, and have been widely used as intermediate representations in various tasks. However, discretization inevitably causes information loss, leading to degraded performance compared with continuous SSL features. In this work, we propose to apply soft token assignment only during downstream inference. This approach preserves the efficiency of hard discretization during training while enhancing the expressiveness of the tokens at inference. The proposed method outperforms conventional hard assignment on both ASR and speech synthesis tasks, and exhibits particularly strong generalizability to out-of-domain data. For ASR of non-native speech, it even surpasses models using continuous SSL features. Moreover, analysis of the resulting representations shows they align more accurately with phonemes compared with conventional hard assignment.

</details>

### [Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation](2606.07015.md)
**Ziyu Zhang, Chunyu Qiang, Xiaopeng Wang, Yuxin Guo et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

While song generation and singing voice conversion (SVC) have evolved significantly, they have long been developed isolated: the former lacks zero-shot speaker cloning, while the latter overlooks vocal-accompaniment synergy. To bridge this gap, we propose UniSinger, the first end-to-end framework unifying speaker cloning song generation and accompaniment co-generation SVC. Building on the multimodal diffusion transformer, we construct a unified speaker embedding space transferring speaker representation from SVC to song generation, endowing fine-grained cross-task timbre control. To mitigate multi-task optimization conflicts, we design a curriculum learning strategy using task-specific modality masking to guide the model to gradually master the generative mechanisms among semantic content, vocal timbre, and accompaniment. Experiments show state-of-the-art performance on both tasks and realizes complementary benefits, offering new possibilities for intelligent music production.

</details>

### [VoxCPM2 Technical Report](2606.06928.md)
**Yixuan Zhou, Guoyang Zeng, Xin Liu, Xiang Li et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

We present VoxCPM2, a https://info.arxiv.org/help/prep#abstractsfully open-source multilingual and controllable speech generation foundation model that extends the hierarchical diffusion-autoregressive modeling paradigm of VoxCPM. VoxCPM2 advances the framework in three key dimensions: (i) capability, by unifying 30 languages, 9 Chinese dialects, natural-language voice design, style-controllable voice cloning, and high-fidelity continuation cloning within a single backbone; (ii) quality, through an asymmetric AudioVAE that encodes at 16 kHz and reconstructs at 48 kHz, enabling implicit super-resolution with high encoding efficiency; and (iii) scale, by jointly scaling the model to 2B parameters and the training data to over 2 million hours of multilingual speech. To support these diverse capabilities within one model, we introduce a unified sequence organization that expresses all generation modes through different arrangements of the same input building blocks, allowing joint training under a single set of parameters and objective. VoxCPM2 achieves state-of-the-art or competitive performance on public zero-shot and instruction-following TTS benchmarks. On our internal 30-language evaluation set, it attains an average WER of 1.68%. These results demonstrate that hierarchical continuous-latent modeling, without relying on any external discrete speech tokenizer, offers a viable and powerful foundation for large-scale multilingual and controllable speech generation. The model weights, fine-tuning code, and inference tools are publicly released under the Apache 2.0 license to foster community research and development.

</details>

### [Mitigating Proxy-to-Wild Domain Gap in Deepfake Speech](2606.07494.md)
**Xuanjun Chen, Yun-Shing Wu, Wei-Chung Lu, Claire Lin et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

Recent neural audio codec-based speech generation (CodecFake) produces highly realistic audio, posing a challenge to existing deepfake countermeasure models. While using codec resynthesized speech (CoRS) as proxy data improves performance, it often suffers from limited generalization. We propose Domain-Shift Feature Augmentation (DSFA), which simulates "in-the-wild" variations by transforming deterministic feature statistics into stochastic distributions during fine-tuning. To evaluate generalization, we further introduce Codec-based Speech Generation Extension Evaluation (CoSG ExtEval) dataset, a more challenging extension of the CoSG Eval (from CodecFake+) dataset, featuring 40 unseen generative models and long-form audio. Experimental results demonstrate that combining a post-trained SSL backbone with DSFA effectively narrows the proxy-to-wild domain gap. This approach achieves state-of-the-art performance across diverse CodecFake attacks in both CoSG Eval and CoSG ExtEval.

</details>

### [Pixel-TTS: Image based Text Rendering for Robust Text-to-Speech](2606.14750.md)
**Adarsh Arigala, Arjun Gangwar, S Umesh, Yova Kementchedjhieva** · 2026-06-05

<details>
<summary>Abstract</summary>

Recent advances in pixel-based text modeling show that representing text as images enables models to exploit visual cues for language understanding. Grounding text in its visual form allows structurally similar characters with different Unicode encodings to produce similar embeddings, benefiting cross-lingual and zero-shot scenarios. Conventional text-based approaches treat each character independently, limiting generalization to unseen characters and requiring embedding expansion during cross-lingual adaptation. We propose Pixel-TTS, the first framework for visually grounded speech synthesis. It renders text as images and projects them through a 2D convolutional layer to generate embeddings. This design eliminates embedding matrix expansion during fine-tuning while improving robustness to unseen characters and orthographic variations. Extensive experiments show Pixel-TTS achieves competitive performance with strong baselines, faster convergence and robust zero-shot generalization.

</details>

### [GLASS: GRPO-Trained LoRA for Acoustic Style Steering in Zero-Shot Text-to-Speech](2606.05889.md)
**Jaehoon Kang, Yejin Lee, Kyuhong Shim** · 2026-06-04

<details>
<summary>Abstract</summary>

We propose GLASS, a framework for composable acoustic style control in zero-shot autoregressive text-to-speech (TTS) that learns controls from post-generation rewards rather than style labels. In zero-shot TTS, a speaker prompt often entangles speaker identity with prosodic attributes such as speaking rate and pitch, making it difficult to change style without changing the prompt itself. GLASS instead treats each acoustic attribute as a reward-defined control direction. For each control axis, GLASS freezes the TTS backbone and trains one lightweight LoRA adapter with Group Relative Policy Optimization (GRPO), using speech-token length and mean F0 as style rewards and WER as an intelligibility anchor. Because each control is represented as a LoRA weight update, independently trained adapters can be swapped, interpolated, and composed through linear LoRA arithmetic without retraining the backbone. Experiments on speaking rate and pitch control show targeted style shifts while preserving naturalness, speaker similarity, and intelligibility, and demonstrate smooth interpolation and multi-axis composition across independently trained adapters.

</details>

### [UniVoice: A Unified Model for Speech and Singing Voice Generation](2606.05852.md)
**Junjie Zheng, Huixin Xue, Shihong Ren, Chaofan Ding et al.** · 2026-06-04

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) and singing voice synthesis (SVS) both aim to generate human vocal audio from symbolic inputs, but they impose different requirements on the generation process. Speech generation relies on flexible, language-driven prosody, whereas singing generation requires explicit melody control and accurate rhythmic alignment. This mismatch makes it challenging to train a single model that can generate both natural speech and controllable singing, since melody-related conditions should strongly constrain singing but should not restrict speech prosody. We present UniVoice, a unified speech and singing voice generation framework based on conditional flow matching. Instead of using a single undifferentiated conditioning representation, UniVoice factorizes the condition into content, melody, and timbre, which are encoded by modality-appropriate encoders and consumed by a shared Diffusion Transformer (DiT) backbone. For singing, the melody condition is represented by MIDI note sequences; for speech, it is replaced with a learned null melody token, allowing the model to infer prosody from linguistic and acoustic context. This design preserves explicit melody control for singing while avoiding the need to impose melody constraints on speech. We further analyze the null melody token as an approximation to melody marginalization in the conditional flow. Trained on 30k hours of speech and 35k hours of singing data, UniVoice achieves a speech PER of 5.26\%, comparable to dedicated TTS systems such as F5-TTS (5.21\%) and CosyVoice3 (5.30\%). On singing generation, UniVoice achieves a PER of 16.22\%, outperforming the unified baseline Vevo1.5 (24.72\%).

</details>

### [Multilingual Multi-Speaker Unit Vocoders: A Systematic Analysis of Discrete Speech Representations](2606.06740.md)
**Naman Kothari, Arjun Gangwar, Adarsh Arigala, S Umesh** · 2026-06-04

<details>
<summary>Abstract</summary>

Discrete speech units obtained via k-means clustering of self supervised embeddings entangle phonetic, speaker, and language information, causing speaker mixing and cross-lingual interference in multilingual multi-speaker speech generation. Despite growing use in Audio LLMs and speech to speech systems, unit vocoders remain underexplored. We analyze a BigVGAN based unit vocoder, across four Indian languages. We study the interaction between cluster size and conditioning strategies using WER, speaker similarity, and unit level metrics. Results show that cluster size governs intelligibility by improving phonetic discriminability, while explicit speaker conditioning is indispensable for preventing identity collapse. Language supervision yields further gains mainly at lower cluster sizes where units remain ambiguous. Our analysis shows similar phonemes across languages collapse to the same cluster IDs at smaller inventories, with larger clusters progressively separating them.

</details>

### [Task-Vector Arithmetic for Emotional Expressivity Control in Language-Model-Based Text-to-Speech](2606.05367.md)
**Daniel Oliveira de Brito, Arnaldo Candido Junior** · 2026-06-03

<details>
<summary>Abstract</summary>

We investigate whether task-vector arithmetic, successful for cross-speaker emotional intensity control in modular text-to-speech (TTS), transfers to large-scale TTS systems built on language-model backbones with in-context learning (LM-TTS). Through a systematic elimination study over four progressively narrower operands on Qwen3-TTS-12Hz-1.7B - model weights via LoRA fine-tuning, continuous codec embeddings, discrete codec tokens, and the speaker embedding (x-vector) produced by an ECAPA-TDNN encoder jointly trained with the synthesis backbone - we localize the dominant carrier of emotional prosody to the x-vector. Building on this finding, we propose a training-free method based on centroid arithmetic in x-vector space: an emotion direction $τ= \mathbb{E}_i[x(s_i,\text{emo})] -\mathbb{E}_i[x(s_i,\text{neutral})]$ applied to an unseen target speaker as $x_{\text{new}} = x(\text{target},\text{neutral}) + α\cdotτ$. Using ESD (English) as the $τ$ source and emoUERJ (Brazilian Portuguese) as a cross-lingual ground-truth target, we observe average gains of $+0.29$ in emotion2vec cosine over the ICL baseline on English held-out speakers and $+0.09$ on Brazilian Portuguese held-out speakers, while largely preserving identity (WavLM SECS $\gtrsim 0.88$ for the multi-speaker $τ$ variant) and intelligibility (WER $\approx 0$ in PT-BR). These results offer initial evidence that the reported incompatibility of centroid-arithmetic style control with token-based TTS architectures may be circumvented when the arithmetic operates on the speaker embedding.

</details>

### [FoeGlass: Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors](2606.05101.md)
**Sepehr Dehdashtian, Jacob H Seidman, Vishnu N Boddeti, Gaurav Bharaj** · 2026-06-03

<details>
<summary>Abstract</summary>

Audio deepfake detection (ADD) models are critical for countering the malicious use of text-to-speech (TTS) models. Evaluating and strengthening ADD models requires developing datasets that span the space of generated audio and highlight high-error regions. Existing dataset development strategies face two challenges: (i) manual collection, and (ii) inefficient discovery of blind spots in the ADD models. To address these challenges, we propose FoeGlass, the first black-box automated red-teaming method for ADDs, which effectively discovers ADD failure modes in the space of generated audio underexplored by state-of-the-art deepfake benchmarks. FoeGlass uses the in-context learning capabilities of an LLM to explore the input space of a TTS model, generating audio samples that fool the target ADD using only black-box access to all components. By using a carefully designed context based on diversity measurements, FoeGlass mitigates the common problem of mode collapse in automated red-teaming systems. Empirical evaluations on several open-source ADD and TTS models demonstrate that data generated from FoeGlass substantially improves the false negative rates over unconditional sampling baselines and recent spoofing datasets by up to 94%, while requiring no manual supervision. Furthermore, we show that the attacks generated by FoeGlass are transferable across different target ADDs, demonstrating its broad applicability and ease of use for the automated red teaming of ADD systems. Finally, fine-tuning ADD models on FoeGlass-generated samples notably enhances the robustness of the detectors (up 41%).

</details>

### [CleanCodec: Efficient and Robust Speech Tokenization via Perceptually Guided Encoding](2606.04418.md)
**Eugene Kwek, Feng Liu, Rui Zhang, Wenpeng Yin** · 2026-06-03

<details>
<summary>Abstract</summary>

Neural audio codecs are a key component of speech processing pipelines, compressing audio into discrete tokens for downstream modeling. However, existing codecs struggle to balance reconstruction quality with token efficiency, often encoding perceptually irrelevant information such as background noise and recording artifacts at the expense of linguistically and acoustically meaningful content. We reframe audio tokenization as a selective information bottleneck problem and propose CleanCodec, a denoising audio codec which learns to encode only perceptually important features and discard imperceptible information. At just 12.5 tokens per second, CleanCodec achieves state-of-the-art tokenization efficiency, substantially outperforming existing codecs in speaker similarity and speech intelligibility. Evaluations on downstream text-to-speech and voice conversion tasks further demonstrate improved performance and up to 17x faster inference, highlighting significant efficiency gains.

</details>

### [WavTTS: Towards High-Quality Zero-Shot TTS via Direct Raw Waveform Modeling](2606.03455.md)
**Wenxi Chen, Dongya Jia, Yushen Chen, Zhikang Niu et al.** · 2026-06-02

<details>
<summary>Abstract</summary>

Recently, diffusion models operating on VAE latents or mel-spectrograms have become the dominant paradigm for zero-shot TTS. Although these compressed representations improve generation efficiency, they inevitably suffer from information loss and non-end-to-end training. Theoretically, directly modeling raw waveforms circumvents these issues; however, this direction remains underexplored and is often deemed difficult due to the extremely long sequence length of audio signals. To overcome this, we propose WavTTS, the first raw waveform generative TTS model that substantially narrows the gap with latent-space generative models. Built upon the flow matching with Diffusion Transformer (DiT), WavTTS directly models speech waveforms via a simple patchification strategy, while integrating multi-scale mel-spectrogram supervision to provide perceptual guidance during training. Furthermore, we investigate the impact of prediction targets and noise scheduling in waveform diffusion, and develop an effective schedule design to improve generation quality. Evaluations on open-source benchmarks demonstrate that WavTTS closely approaches the performance of current state-of-the-art latent generative zero-shot TTS models, while substantially outperforming previous end-to-end speech generation models. Our findings demonstrate the feasibility of scaling diffusion-based TTS directly in the waveform space, opening a new direction for end-to-end speech generation.

</details>

### [Advancing Electrolaryngeal Speech Enhancement Through Speech-Text Representation Learning](2606.01905.md)
**Ding Ma, Jinyi Mi, Fengji Li, Lester Phillip Violeta et al.** · 2026-06-01

<details>
<summary>Abstract</summary>

Objective: laryngectomees depend on an electromechanical device to generate electrolaryngeal (EL) speech. Compared with normal speech, EL speech suffers from severe distortion, limited phonetic variation, unnatural prosody, and temporal shifts, degrading naturalness and intelligibility. Although sequence-to-sequence (seq2seq) voice conversion (VC) based EL-speech-to-normal-speech conversion (EL2SP) is promising, substantial mismatches between EL and normal speech inevitably cause cumulative mapping errors that limit performance. To address this, we describe a novel representation learning framework integrating speech and text representations to improve mapping and reconstruction quality within a seq2seq VC model. Methods: our methodology comprises two main stages: 1) representation integration and learning, and 2) reconstruction training. A network capable of incorporating auxiliary text information is first constructed with pretrained modules to learn speech--text-based integrated representations. Then, an autoencoder-style reconstruction strategy finalizes EL2SP model to inherit these representations without increasing model complexity. We introduce three fusion strategies including middle-, input-, and hybrid-level fusion strategies that progressively enhance learning. Moreover, besides standard seq2seq VC objectives, an additional reconstruction loss on the integrated representation is introduced to refine representation transfer. Results: experiments under different EL2SP datasets consistently demonstrate that our methods, combined with data augmentations, outperform baselines relying solely on speech representations. Furthermore, progressive improvements with system design depth validate the effectiveness of our methods. Significance: the proposed methods provide an extensible and practical methodology for EL speech enhancement and assistive communication technologies.

</details>

### [UniVocal: Unified Speech-Singing Code-Switching Synthesis](2606.01677.md)
**Yufei Shi, Qian Chen, Wen Wang, Xiangang Li et al.** · 2026-06-01

<details>
<summary>Abstract</summary>

We propose UniVocal, a unified framework that implicitly infers vocal modes from text context to pioneer Speech-Singing Code-Switching (SCS) Synthesis - a task where transitions are autonomously driven by textual semantics, akin to seamless human language blending. Unlike single-mode generation or systems relying on switching-control tags, our proposed UniVocal implicitly infers vocal modes solely from text context. To achieve this, we employ a data-efficient two-stage curriculum learning strategy that progressively trains a competitive TTS system to acquire the desired SCS capability. Addressing data scarcity, we introduce a scalable pipeline to synthesize diverse code-switching data that is both semantically and acoustically natural, alongside a new multi-scenario benchmark, SCSBench. To address limitations of semantic tokenizers in capturing acoustic details, we also introduce refined cent token and Chain-of-Thought (CoT) generation for planning prosody before content generation, effectively enhancing empathetic speech generation and singing melody. Experimental results demonstrate that UniVocal achieves state-of-the-art performance on SCSBench while maintaining competitive performance on regular speech and singing tasks. Audio samples are available at https://project-univocal-demo.github.io/demo/. The code and dataset are released at https://github.com/FunAudioLLM/FunResearch/tree/main/UniVocal.

</details>

### [Sparse Autoencoders for Interpretable Emotion Control in Text-to-Speech](2606.01479.md)
**Hongfei Du, Jiacheng Shi, Sidi Lu, Gang Zhou et al.** · 2026-05-31

<details>
<summary>Abstract</summary>

Integrating large language models (LLMs) into text-to-speech (TTS) systems has improved speech expressiveness, yet interpretable emotional control remains challenging. Existing approaches primarily rely on external conditioning or global activation steering, offering limited insight into the internal representations underlying emotional control. In this work, we analyze emotion-related variation in the semantic hidden states of LLM-based TTS models using sparse autoencoders (SAEs) to identify sparse latent features. Our analysis shows that emotional variation is distributed across multiple sparse latent features, while intervening on a small subset enables interpretable emotion control. Building on this observation, we introduce a feature-level intervention framework for bidirectional emotion induction and suppression without modifying backbone parameters. We further show that distinct latent features are associated with specific acoustic attributes (e.g., pitch), suggesting that emotional expression arises from coordinated latent contributions rather than a single global shift. Empirically, steering these sparse latent features achieves comparable or superior emotion induction and suppression performance relative to global steering and existing TTS baselines.

</details>

### [Local Diagnostics of Continuous Normalizing Flow for Out-of-Distribution Detection](2606.00684.md)
**Xinwei Cao, Mengxuan Lu, Torbjørn Svendsen, Giampiero Salvi** · 2026-05-30

<details>
<summary>Abstract</summary>

We address the problem of out-of-distribution (OOD) detection for target observations embedded in a subspace of the high dimensional data space. Using continuous normalizing flows (CNFs), we propose a Lagrangian sub-flow (LSF) framework designed to isolate and estimate the density for the relevant components in the representation and using the remaining components as context. Through experimentation with models for speech synthesis, we show that CNFs, similarly to other deep generative models (DGMs), are susceptible to the "likelihood paradox", where high likelihood is erroneously assigned to OOD samples. This is attributed to the inductive bias of DGMs that prioritize low-level structural details over high-level semantic coherence. To mitigate this phenomenon, we propose a number of geometric diagnostic signals based on the velocity field over the sub-flow trajectory. Based on these signals, we design metrics for the challenging task of zero-shot phoneme-level mispronunciation detection. Finally, we demonstrate the superiority of these metrics compared to likelihood-based methods on a real-world mispronunciation detection benchmark.

</details>

### [UNISON: A Unified Sound Generation and Editing Framework via Deep LLM Fusion](2605.31530.md)
**Zhaoqing Li, Haoning Xu, Jingran Su, Yaofang Liu et al.** · 2026-05-29

<details>
<summary>Abstract</summary>

We present UNISON, a latent diffusion framework that unifies speech generation, sound generation, and audio editing within a single model. A single model handles text-to-audio, text-to-speech, zero-shot speaker cloning, mixed speech-and-sound generation, scene-level audio editing, speech-in-scene editing, and timed temporal composition, all of which share a single set of weights. Our architecture features two core designs: (1) Layer-wise deep LLM fusion, which injects hidden states from uniformly sampled layers of a frozen MLLM into corresponding MM-DiT blocks via learned projections, providing depth-matched semantic conditioning that improves instruction following over single-layer baselines; and (2) a unified multi-task architecture where task identity is encoded solely by a channel-wise mask and source audio is provided through VAE-encoded channel concatenation. Training is stabilized by an online GPU-side multi-task data synthesis pipeline with task-homogeneous batching and a two-stage curriculum. With 621M--732M trainable parameters, UNISON achieves results competitive with or exceeding task-specialist models across evaluated domains, while being roughly $4\times$ smaller than comparable unified systems.

</details>

### [SwanVoice: Expressive Long-Form Zero-Shot Speech Synthesis for Both Monologue and Dialogue](2605.30993.md)
**Ruiqi Li, Yu Zhang, Changhao Pan, Ke Lei et al.** · 2026-05-29

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) has improved substantially for single-speaker synthesis, yet expressive long-form multi-speaker dialogue remains difficult. A common workaround is to synthesize each turn with a monologue TTS model and stitch the outputs together. This adds inference cost and often breaks acoustic consistency, conversational coherence, and affective continuity across turns. Recent dialogue TTS systems have begun to address this setting, but they still struggle to keep expressive coherence, controllable speaker switching, and monologue quality at the same time. We present SwanData-Speech and SwanVoice. SwanData-Speech builds monologue and dialogue corpora from in-the-wild audio, using Swan Forced Aligner for pause-aware word-level alignment and RobustMegaTTS3 for pronunciation-hard cases. Built on these data, SwanVoice is a zero-shot TTS model for 1--4 speakers, combining a 25 Hz VAE, raw-text conditioning with pause-aware symbols and pinyin substitution, and a flow-matching DiT with speaker-turn conditioning. Training starts from monologue speech, moves through mixed and real dialogue data, and then uses DiffusionNFT post-training with phone-level and speaker-similarity rewards. On SwanBench-Speech, SwanVoice obtains higher richness and hierarchy scores than all evaluated open-source baselines in both monologue and dialogue settings, while content accuracy remains the main limitation. Audio demos are available at https://swanaigc.github.io//#swanvoice.

</details>

### [ImmersiveTTS: Environment-Aware Text-to-Speech with Multimodal Diffusion Transformer and Domain-Specific Representation Alignment](2605.30965.md)
**Jun-Hak Yun, Seung-Bin Kim, Seong-Whan Lee** · 2026-05-29

<details>
<summary>Abstract</summary>

Recent advancements in text-guided audio generation have yielded promising results in diverse domains, including sound effects, speech, and music. However, jointly generating speech with environmental audio remains challenging due to the inherent disparities in their acoustic patterns and temporal dynamics. We propose ImmersiveTTS, an environment-aware text-to-speech (TTS) model that generates natural speech seamlessly integrated within environmental contexts by explicitly modeling cross-modal interactions. Our model builds on a multimodal diffusion transformer and fuses transcript-aligned speech latent with text-conditioned environmental context via joint attention. To enhance semantic consistency, we introduce a domain-specific representation alignment objective tailored to environment-aware TTS, leveraging complementary self-supervised representations from speech and audio encoders. Experimental results show that ImmersiveTTS achieves higher naturalness, intelligibility, and audio fidelity than existing approaches across objective metrics and human listening tests.

</details>

### [Chatterbox-Flash: Prior-Calibrated Block Diffusion for Streaming Zero-Shot TTS](2605.30748.md)
**Deokjin Seo, Gangin Park, Kihyun Nam** · 2026-05-29

<details>
<summary>Abstract</summary>

We present Chatterbox-Flash, a zero-shot text-to-speech model obtained by fine-tuning a pretrained autoregressive TTS decoder into a block-diffusion decoder, enabling parallel token generation within each block while retaining block-by-block streaming. We find that naively transferring mainstream block-diffusion decoding to discrete speech tokens degrades quality, as a long-tail token distribution biases parallel position selection toward a few high-frequency tokens. To mitigate this without architectural modification, we introduce two inference-time techniques: prior-calibrated scoring, which subtracts the block-level marginal token distribution, and an early-decoding schedule, which adaptively terminates iteration based on calibrated confidence. On standard zero-shot TTS benchmarks, Chatterbox-Flash attains high-fidelity synthesis comparable to strong autoregressive and non-autoregressive baselines, while supporting streaming inference with time-to-first-packet on par with streaming AR systems and substantially lower real-time factor. Code and audio samples are available at https://github.com/resemble-ai/chatterbox-flash.

</details>

### [MindVoice: Reconstructing Intelligible Speech from Non-invasive Neural Signals with Pretrained Priors](2605.31173.md)
**Guangyin Bao, Taiping Zeng, Jianfeng Feng, Xiangyang Xue** · 2026-05-29

<details>
<summary>Abstract</summary>

Reconstructing continuous speech from non-invasive neural recordings is a fundamental problem for probing human auditory perception and building safe, scalable speech brain-computer interfaces. Despite recent progress, intelligible reconstruction remains elusive, as non-invasive recordings are inherently noisy, spatially blurred, and only partially preserve information about perceived speech. Existing methods directly map neural activity to entangled speech representations before synthesizing waveforms with neural vocoders, resulting in spectral-similar but unintelligible results. To overcome these limitations, we introduce MindVoice, a neuro-to-speech reconstruction framework that uses pretrained models to compensate for the incomplete semantic and acoustic information in neural recordings. MindVoice disentangles reconstruction into two complementary pathways: one recovers high-level semantic content, while the other estimates fine-grained acoustic attributes. These inferred representations are then fused with powerful speech generation models and in-context voice cloning to synthesize natural and intelligible utterances. Extensive experiments on EEG and MEG demonstrate that MindVoice substantially outperforms existing methods on various metrics. These results show that pretrained priors provide a principled way to bridge the gap between noisy neural recordings and natural speech, highlighting a promising attempt for auditory neuroscience research and non-invasive speech brain-computer interfaces.

</details>

### [UniAudio-Token: Empowering Semantic Speech Tokenizers with General Audio Perception](2605.31521.md)
**Yuhan Song, Linhao Zhang, Aiwei Liu, Chuhan Wu et al.** · 2026-05-29

<details>
<summary>Abstract</summary>

Semantic speech tokenizers have become a widely used interface for Audio-LLMs, owing to their compact single-codebook design and strong linguistic alignment. However, their focus on linguistic abstraction induces acoustic blindness, limiting their applicability beyond speech-centric tasks. We propose UniAudio-Token, a framework that empowers semantic tokenizers with general audio perception without compromising speech ability. Instead of altering the semantic paradigm, UniAudio-Token mitigates its information loss through two key innovations: (1) Semantic-Acoustic Primitives (SAP) provide structured supervision by decomposing audio into linguistic content, vocal attributes, and auditory-scene primitives; and (2) Semantic-Acoustic Equilibrium (SAE) introduces a content-aware gating mechanism that adaptively restores fine-grained acoustic details from shallow layers. Extensive evaluations show that UniAudio-Token learns comprehensive universal representations while preserving high-fidelity speech generation. When integrated with downstream LLMs, it outperforms all single-codebook baseline tokenizers on both understanding and generation tasks, effectively serving as a unified audio interface. We publicly release all our code, including training and inference scripts, together with the model checkpoints at https://github.com/Tencent/Universal_Audio_Tokenizer.

</details>

### [MELD: Mel-Spectrogram-Based Speech Language Modeling with Discrete Latent Variables](2605.29859.md)
**Sung-Lin Yeh, Wei Zhou, Gil Keren, Duc Le et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

Recent speech language models rely on encoders that are optimized separately from autoregressive models. Since these encoders are unaware of the downstream objectives, the extracted representations may not be optimal for downstream tasks. To address this limitation, we introduce a discrete latent variable model on mel spectrograms that jointly optimizes the encoder and the speech language model. Joint optimization not only brings improvements over codec-based and other mel-spectrogram-based baselines on zero-shot Text-to-Speech (TTS) and Speech-to-Text (STT) tasks, but also effectively alleviates common issues in autoregressive mel-spectrogram modeling, such as prolonged silence generation and word omissions.

</details>

### [HoliTok:A Coutinuous Holistic Tokenization with Robust Dual Capabilities of Speech Generation and Understanding](2605.29948.md)
**Bohan Li, Shi Lian, Hankun Wang, Yiwei Guo et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

Unified speech foundation models require a holistic tokenization space that is both learnable by language models and decodable into high-quality waveforms. Existing speech tokenizers, however, often fail to satisfy these requirements simultaneously, leading to increased architectural complexity and more involved training designs. We propose HoliTok, a continuous Holistic speech Tokenization model designed for unified generation-understanding modeling. HoliTok encodes 48~kHz speech into a compact 25~Hz sequence of 128-dimensional latents. It is trained with a progressive strategy that jointly preserves signal-level fidelity, incorporates semantic information, and maintains strong latent learnability. Based on this tokenization, we build a unified AR+DiT model for speech synthesis and recognition, where the same latent sequence supports both generation-specific and unified generation-understanding tasks. Experiments show that HoliTok achieves competitive reconstruction fidelity, improves generative learnability for high-quality and controllable synthesis, and, among the evaluated representations, is the only one that operates robustly in our unified generation-understanding architecture without additional optimization tricks. These results suggest that HoliTok serves as an effective speech tokenizer and a foundational representation interface for unified spoken language modeling. The code is available at: https://github.com/bovod-sjtu/HoliTok.

</details>

### [Why We Need Speech to Evaluate Speech Translation](2605.28227.md)
**Maike Züfle, Danni Liu, Vilém Zouhar, Jan Niehues** · 2026-05-27

<details>
<summary>Abstract</summary>

Speech translation models are increasingly capable of preserving speech-specific information (e.g., speaker gender, prosody, and emphasis), yet evaluation metrics remain blind to such phenomena. We meta-evaluate both text- and speech-based quality estimation metrics on two contrastive datasets targeting gender agreement and prosody, and find that both fall short, even when given direct access to the speech signal. We then train SpeechCOMET, a family of quality estimation models with speech encoders, and evaluate a state-of-the-art SpeechLLM as a judge. Both match or exceed text-based COMET on standard quality estimation, but neither consistently assesses speech-specific phenomena. We identify three causes: (1) speech-specific features are not reliably preserved in current encoders, (2) models tend to ignore the speech source signal, and (3) quality estimation training data contains too few relevant examples. We release all models and code, and argue that progress requires dedicated speech-specific training data and models that genuinely condition on speech.

</details>

### [Comprehensive Benchmarking of Long-Form Speech Generation in Diverse Scenarios](2605.28618.md)
**Changhao Pan, Rui Yang, Han Wang, Zhuan Zhou et al.** · 2026-05-27

<details>
<summary>Abstract</summary>

Recent advances in speech generation have enabled high-fidelity synthesis, yet systematic evaluation of models under long-context conditions remains largely underexplored. A comprehensive evaluation benchmark for long-form speech is indispensable for two reasons: 1) existing test scenarios are often confined to limited domains, creating a significant gap with the diverse downstream applications; 2) existing metrics overlook critical long-text factors such as consistency and coherence, failing to generalize reliably. To this end, we propose Swanbench-Speech, a comprehensive benchmark that decomposes long-form speech quality into specific, disentangled dimensions. SwanBench-Speech has three key properties. 1) Rich speech scenarios: Focusing on long-form speech generation and dialog generation, SwanBench-Speech covers acoustics, semantics, and expressiveness challenges, and consists of 1,101 samples spanning 17 common speech scenarios; 2) Comprehensive evaluation dimensions: Along the acoustics, semantics, and expressiveness axes, SwanBench-Speech defines an automated evaluation protocol with seven metrics to provide a comprehensive, accurate, and standardized assessment; 3) Valuable Insights: Through extensive experiments, we reveal that current models still struggle in highly expressive scenarios and exhibit a notable gap in consistency and hierarchy compared to real recordings.

</details>

### [PilotTTS: A Disciplined Modular Recipe for Competitive Speech Synthesis](2605.27258.md)
**Bowen Li, Shaotong Guo, Zhen Wang, Yang Xiang et al.** · 2026-05-26

<details>
<summary>Abstract</summary>

Building state-of-the-art text-to-speech (TTS) systems typically demands millions of hours of proprietary data and complex multi-stage architectures, creating substantial barriers for resource-constrained research teams. In this report, we present PilotTTS, a lightweight autoregressive TTS system that achieves competitive performance through minimalist architecture and rigorous data engineering. PilotTTS is trained on only 200K hours of data processed entirely with open-source tools. Specifically, our contributions are: (1) a reproducible multi-stage data processing pipeline covering quality assessment, label annotation, and filtering, and (2) a compact model architecture that employs Q-Former-based conditioning to decouple speaker identity from speaking style via cross-sample paired training. Within a unified framework, PilotTTS supports zero-shot voice cloning, emotion synthesis (11 categories), paralinguistic synthesis (4 categories), and Chinese dialect synthesis (14 dialects). On the Seed-TTS Eval benchmark, PilotTTS achieves the lowest WER of 1.50% on test-en, a CER of 0.87% on test-zh, and the highest speaker similarity on both test sets (0.862 and 0.815), outperforming systems trained on significantly larger datasets. We release the complete data pipeline recipe, pretrained weights, and code at https://github.com/AMAPVOICE/PilotTTS.

</details>

### [Learning When to Think While Listening in Large Audio-Language Models](2605.27190.md)
**Zhiyuan Song, Weici Zhao, Yang Xiao, Suhao Yu et al.** · 2026-05-26

<details>
<summary>Abstract</summary>

Recent advances in Large Audio-Language Models (LALMs) have made real-time, streaming spoken interaction increasingly practical. In this setting, reasoning quality and responsiveness are tightly coupled: delaying reasoning until the speech endpoint can improve answer quality but moves deliberation into user-visible response delay, while answering too early risks committing before decisive evidence arrives. We introduce a learnable wait-think-answer control formulation for LALMs. Motivated by the incremental nature of human conversation, the controller decides under partial audio evidence when to wait, when to externalize a compact reasoning update, and when to answer. Using Qwen2.5-Omni-7B as the base model, we construct aligned wait-think-answer traces from spoken reasoning data, train the controller with supervised fine-tuning (SFT), and then apply Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO). The reward combines answer correctness, action validity, update timing, latency synchronization, reasoning quality, and chain consistency, optimizing the complete wait-think-answer trajectory and not the final answer alone. On a six-task synthetic spoken reasoning question answering (SRQA) benchmark, the six-reward DAPO controller improves the row-weighted accuracy from 67.6% to 70.3% while reducing post-endpoint final-think length by 14% under the same Qwen deployment harness. On a 186-item human-recorded Real Audio Bench, a transfer check beyond text-to-speech (TTS)-rendered speech, the controller family remains functional: SFT achieves the strongest accuracy, while the six-reward DAPO controller is the only learned variant whose final-think length falls below the base. These results suggest that a streaming model should learn when to make intermediate reasoning explicit during the audio stream.

</details>

### [PashtoTTS-Bench: automated screening for low-resource non-Latin-script text-to-speech](2605.26978.md)
**Hanif Rahman** · 2026-05-26

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) evaluation for low-resource non-Latin-script languages can fail when it relies on a single ASR round-trip word error rate (WER). A system may produce no audio, speak a neighbouring language, preserve target script text only in an ASR transcript, or sound unnatural to native listeners. We introduce INSV (Intelligibility, Naturalness, Script fidelity, and Verification), a reporting framework that separates these cases. This paper reports INSV-A, the automated screening subset: synthesis completion, ASR WER/CER, transcript Script Fidelity Rate, and audio language identification. Native MOS and phonetic annotation are specified but not claimed in this release. We instantiate INSV-A as PashtoTTS-Bench, a dated benchmark for Pashto TTS. The April-May 2026 run evaluates Edge GulNawaz, Edge Latifa, OmniVoice clone, OmniVoice auto, and an Urdu negative control on 200 FLEURS and 200 filtered Common Voice 24 prompts. Under the independent omniASR_CTC_300M_v2, OmniVoice auto has the lowest WER (24.1% FLEURS, 27.4% CV24), followed by Edge GulNawaz (32.8%, 39.5%), Edge Latifa (35.6%, 47.7%), and OmniVoice clone (45.4%, 34.8%). WER below the natural-speech baseline reflects clean synthetic audio and should not be read as better than native speech. Whisper Large V3 returns 0.0% Pashto labels on checked Pashto TTS audio, while MMS-LID-4017 and SpeechBrain VoxLingua107 separate Pashto outputs from the Urdu control. The release provides provider metadata, per-sentence scores, LID audits, failure logs, and scripts for adding systems.

</details>

### [Can We Hear from Events? Generating Speech from Event Camera](2605.26672.md)
**Jingping Fang, Lin Chen, Chenyang Xu, Tong Zhao et al.** · 2026-05-26

<details>
<summary>Abstract</summary>

Traditional RGB-based speech generation faces Temporal Granularity Mismatch since fixed camera exposure times inevitably blur the high-frequency articulatory transients essential for rendering emotional speech. To break this ceiling, we propose EventSpeech as a novel text-conditioned framework pioneering the use of neuromorphic events for expressive speech generation, since these microsecond-precise events naturally align with acoustic waveform dynamics. Our architecture integrates a dedicated Event Encoder to model sparse neuromorphic events alongside a multi-scale Audio Encoder featuring a Hierarchical Wavelet Contextualizer (HWC). A bidirectional alignment mechanism seamlessly synchronizes linguistic content and visual dynamics with dense acoustic features. Furthermore, we construct EVT-SPK as the first benchmark comprising large-scale synthetic data and real-world recordings from specialized neuromorphic hardware. Extensive evaluations demonstrate that EventSpeech significantly outperforms current baselines by preserving fine-grained emotions and resisting motion blur to establish a new paradigm for multimodal speech generation. Code and demo are available at https://xrfang-0102.github.io/EventSpeechWeb/.

</details>

### [Do Audio LLMs Listen or Read? Analyzing and Mitigating Paralinguistic Failures with VoxParadox](2605.27772.md)
**Jiacheng Pang, Ashutosh Chaubey, Mohammad Soleymani** · 2026-05-26

<details>
<summary>Abstract</summary>

Audio large language models (Audio LLMs) demonstrate strong performance on speech understanding tasks, yet their ability to understand paralinguistic information remains limited. To systematically quantify this issue, we introduce VoxParadox, an adversarial benchmark with 2,000 verified examples, spanning 10 paralinguistic tasks, created with controlled speech synthesis to intentionally mismatch transcript claims and speaking style, enabling direct measurement of speech paralinguistic understanding. Evaluation of a diverse set of Audio LLMs reveals consistently low accuracy on acoustic ground truth and a strong tendency to follow language-implied (incorrect) answers. To understand the cause of this gap, we perform layer-wise probing and find that (i) paralinguistic cues can degrade in deeper encoder layers and at the encoder--LLM interface, and (ii) even when such cues are available in audio tokens, the language model frequently ignores them. To address these problems, we propose Prompt-Conditioned Layer Mixer (PCLM), which adaptively combines information from multiple audio layers based on the input prompt, and pair it with Direct Preference Optimization (DPO) to explicitly prefer acoustically supported options over language-implied alternatives. These methods substantially improve Audio LLM paralinguistic understanding, improving Audio Flamingo 3 from 17.40% to 65.20% on VoxParadox, and from 37.74% to 54.78% on MMSU paralinguistic subset. Our project page is available at https://voxparadox.github.io/.

</details>

### [Continual Speaker Identity Unlearning with Minimal Interference](2605.25962.md)
**Jinju Kim, Yunsung Kang, Gyeong-Moon Park, Jong Hwan Ko** · 2026-05-25

<details>
<summary>Abstract</summary>

Machine unlearning removes designated concepts or knowledge from pre-trained models. Recent work has extended this paradigm to speaker identity unlearning in zero-shot text-to-speech (ZS-TTS), the task of selectively erasing a model's ability to replicate a speaker's voice. Existing methods, however, quietly assume all unlearning requests arrive at once; an unrealistic assumption, since privacy-motivated removals arrive sequentially over time. We show this assumption breaks state-of-the-art methods: unlearning each new speaker fully revives previously unlearned speakers, reintroducing the very privacy risk unlearning was meant to eliminate. We present Cumulative ORThogonal Identity Suppression (CORTIS), the first framework for continual speaker identity unlearning in ZS-TTS that requires no access to previously-unlearned speaker data. CORTIS combines Fisher-information-based parameter masking, which localizes updates to speaker-relevant weights, with orthogonal projection against subspaces spanned by prior unlearning updates. With VoiceBox, CORTIS unlearns each requested speaker while keeping previously unlearned speakers forgotten across long request sequences, substantially outperforming sequential application of prior methods. The demo is available at https://cumulativeortis.github.io/ .

</details>

### [CosyEdit2: Speech-Editing-Oriented Reinforcement Learning Unlocks Better Zero-Shot TTS](2605.25930.md)
**Junyang Chen, Yuhang Jia, Hui Wang, Jiaming Zhou et al.** · 2026-05-25

<details>
<summary>Abstract</summary>

Speech editing and zero-shot Text-to-Speech (TTS) share a similar generative foundation conditioned on speech prompts, yet speech editing demands far stricter local acoustic consistency with surrounding unedited content. While prior work has shown that Supervised Fine-Tuning (SFT) enables TTS models to acquire functional editing capability, this approach remains fundamentally bottlenecked by imperfect paired editing data and coarse-grained optimization signals. To address these limitations, we propose CosyEdit2, a speech editing model built on a two-stage post-training framework that progresses from supervised editing initialization to editing-oriented Group Relative Policy Optimization (GRPO) over target-speech-free data. Extensive experiments demonstrate that CosyEdit2 not only substantially advances speech editing performance, but also unlocks better zero-shot TTS capability, revealing a deeper mutual relationship between the two tasks. Audio samples are available at https://cjy1018.github.io/CosyEdit2.

</details>

### [Toward Natural Emotional Text-To-Speech System with Fine-Grained Non-Verbal Expression Control](2605.25504.md)
**Wangzixi Zhou, Bagus Tris Atmaja, Sakriani Sakti** · 2026-05-25

<details>
<summary>Abstract</summary>

While current emotional Text-to-Speech (TTS) models have successfully controlled verbal prosody, they often ignore non-verbal vocalizations (NVs), which are essential for authentic human emotion. Although some non-verbal datasets have recently emerged, they often lack high-quality, fine-grained annotations, which restricts a model's ability to precisely control NV generation. To address this limitation, we propose a novel approach for fine-grained non-verbal expression synthesis. We curate and reprocess female NV utterances from the EARS corpus, develop a new annotation scheme using tags to encode NV types, frequencies, and durations, and build an emotional TTS benchmark to demonstrate its effectiveness. Our evaluation shows that while our NV approach leads to minor trade-offs in perceived naturalness, it significantly improves expressiveness (eMOS 4.20) and emotional recognition accuracy (78.8%). Emotion-specific analysis further reveals that NV cues are highly effective for high-arousal emotions like happy (82.5%) and fear (82.7%), and almost perfectly convey sadness (98.3%).

</details>

### [WaveNeXt 2: ConvNeXt-Based Fast Neural Vocoders With Residual Denoising and Sub-Modeling for GAN and Diffusion Models](2605.25506.md)
**Wangzixi Zhou, Takuma Okamoto, Yamato Ohtani, Sakriani Sakti et al.** · 2026-05-25

<details>
<summary>Abstract</summary>

Most neural vocoders are limited to one type: either GAN or diffusion-based. While state-of-the-art models like Vocos and WaveNeXt use powerful ConvNeXt-based generators, they have only been used in GAN frameworks and have limited performance in multi-speaker settings. Moreover, diffusion models, despite training faster than GANs, have slow CPU inference. In this paper, we introduce WaveNeXt 2, a unified ConvNeXt-based framework compatible with both GAN and diffusion vocoders. Its core innovation is residual denoising and sub-modeling, where each sub-model progressively refines the waveform. Experimental results in the multi-speaker dataset demonstrate the effectiveness of our approach: (1) GAN-WaveNeXt 2 is much faster than HiFi-GAN and WaveFit, and (2) Diff-WaveNeXt 2 also delivers much faster inference and competitive synthesis quality compared with FastDiff with 4 steps. The Diff-WaveNeXt 2 is very training-efficient, training in only 32 hours, making it ideal for resource-constrained applications.

</details>

### [FC-TTS: Style and Timbre Control in Zero-Shot Text-to-Speech with Disentangled Speech Representations](2605.24618.md)
**Yoonhyung Lee, Hyunsin Park, Jinhwan Park, Jinkyu Lee** · 2026-05-23

<details>
<summary>Abstract</summary>

Recent advances in zero-shot text-to-speech (TTS) have enabled accurate imitation of reference speech in terms of both speaking style and speaker timbre. However, achieving disentangled control over these aspects from separate references remains a challenging task. Several studies have proposed disentangled speech representations that decompose speech into interpretable attributes (e.g., timbre, prosody, and content), providing a promising foundation for TTS with attribute control from separate references. Yet, how to effectively integrate such representations into TTS systems to achieve independent and precise control remains underexplored. In this paper, we present FC-TTS, a zero-shot TTS framework that enables disentangled control of style and timbre by conditioning on two distinct reference utterances. Unlike existing systems that inherit limitations from those pre-trained disentangled representations, FC-TTS introduces key design strategies, including architectural choices, training framework, and auxiliary training objectives, which improve the reliability of attribute separation and dual-reference control. Experiments show that FC-TTS achieves high-fidelity synthesis and competitive zero-shot naturalness, while uniquely supporting consistent and independent manipulation of style and timbre. Audio samples are available at https://qualcomm-ai-research.github.io/fc-tts

</details>

### [Natural Yet Challenging to Detect: Robust In-the-Wild TTS through EMA and Dual-Scoring Prompt Selection -- Submission for WildSpoof 2026 TTS Track](2605.23859.md)
**Renhe Sun, Jiayi Zhou, Haolin He, Yueying Feng et al.** · 2026-05-22

<details>
<summary>Abstract</summary>

In this technical report, we describe our submission for the WildSpoof Challenge TTS Track: Text-to-Speech with In-the-Wild Data. We introduce F5-TTS-DPS, a model built upon the F5-TTS architecture. Our approach integrates Exponential Moving Average (EMA) into supervised fine-tuning to stabilize training and improve generalization. To enhance synthesis fidelity, we leverage large language models (LLMs) and large audio language models (LALMs) for dual-scoring prompt selection, filtering reference audio and text prompts to ensure quality while addressing alignment issues in noisy datasets. Experimental evaluation demonstrates that F5-TTS-DPS achieves strong performance with UTMOS of 3.20 and speaker similarity of 0.51 on the development set. More importantly, our model achieves the best a-DCF scores of 0.1582, 0.5233, and 0.2562 across three advanced SASV systems among all submissions, indicating our synthesized speech is the most difficult to detect and exhibits the highest degree of naturalness and authenticity. Combined with competitive WER performance, these results validate the effectiveness of our approach in generating natural-sounding speech with strong spoofing capabilities.

</details>

### [UniSRM: A Unified Speech Reward Model for Reasoning-Based Fine-grained Assessment](2605.23261.md)
**Yuanyuan Wang, Dongchao Yang, Yayue Deng, Zhiyong Wu et al.** · 2026-05-22

<details>
<summary>Abstract</summary>

Evaluating speech generation still relies heavily on human judgments, such as Mean Opinion Score (MOS), which are expensive, subjective, and difficult to reproduce at scale. While a few recent studies have begun to explore AudioLLM-based judge models, existing efforts typically target only a narrow set of scenarios (e.g., utterance-level quality or single-turn dialogue) and provide limited coverage of diverse speech generation tasks and evaluation dimensions. In this work, we propose UniSRM, a unified speech reward model that can support multi-dimensional, interpretable reward signals with reliable reasoning. To support training and evaluation, we introduce UniSRM-Data and UniSRM-Bench, covering speech evaluation tasks from utterance-level quality to context-level coherence. Based on this dataset, we present the unified speech reward model, UniSRM, with a two-stage pipeline that enables reasoning-based fine-grained assessment. Furthermore, we introduce Reasoning-Consistent Rewards to improve the reliability of the reasoning process. Experiments show that UniSRM delivers more reliable and human-aligned judgments across a broad range of speech evaluation tasks, offering a practical foundation for scalable and unified evaluation of speech quality.

</details>

### [Do Factual Recall Mechanisms Carry over from Text to Speech in Multimodal Language Models?](2605.22170.md)
**Luca Modica, Filip Landin, Mehrdad Farahani, Livia Qian et al.** · 2026-05-21

<details>
<summary>Abstract</summary>

In recent years, several Speech Language Models (SLMs) that represent speech and written text jointly have been presented. The question then emerges about how model-internal mechanisms are similar and different when operating in the two modalities. We focus on how these systems encode, store, and retrieve factual knowledge, which has previously been investigated for text-only models. To investigate mechanisms behind the storage and recall of factual association in SLMs, we leverage Causal Mediation Analysis, a technique previously applied to text-based models. Initial results using SpiritLM, a multimodal model integrating discrete speech tokens reveal discrepancies between text-to-text and speech-to-text results, suggesting that the emergent mechanisms for factual recall are only partially carried over from the text to the speech modality. These results advance our understanding of how internal mechanisms encode factual associations in SLMs while contributing insights for improving speech-enabled AI systems.

</details>

### [RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching](2605.22083.md)
**Jinhyeok Yang, Hyeongju Kim, Yechan Yu, Joon Byun et al.** · 2026-05-21

<details>
<summary>Abstract</summary>

While flow-matching text-to-speech (TTS) achieves strong zero-shot speaker similarity and naturalness, it remains susceptible to content fidelity issues, particularly skip and repeat errors from imperfect alignment. We propose RobustSpeechFlow, a training strategy that improves alignment robustness by extending contrastive flow matching with length-preserving repeat and skip latent augmentations. Requiring no external aligners or preference data, our method directly penalizes realistic failure modes and readily integrates into existing pipelines. On Seed-TTS-eval, it reduces the word error rate (WER) from 1.44 to 1.38 using only 0.06B parameters. On our ZERO500 benchmark, it delivers consistent intelligibility improvements across diverse speaker and prosody conditions; at NFE=24, it reduces English character error rate (CER) from 0.48\% to 0.35\% and Korean CER from 0.81\% to 0.57\%. Audio samples: https://robustspeechflow.github.io/

</details>

### [Eroding Trust in Real Speech: A Large-Scale Study of Human Audio Deepfake Perception](2605.26136.md)
**Nicolas M. Müller, Wei Herng Choong** · 2026-05-21

<details>
<summary>Abstract</summary>

Audio deepfakes have improved rapidly recently, yet their effect on human trust in real speech remains unstudied. We present the largest listening study on audio deepfake perception to date, collecting 35,532 judgments from 1,768 participants across 138 text-to-speech and voice conversion systems. Our central finding is a skepticism shift: compared to a 2021 baseline, human accuracy on fake samples barely changed (72.9% to 71.2%), but accuracy on real samples dropped from 72.7% to 64.1%. Participants are not worse at detecting synthesis artifacts; rather, they increasingly distrust authentic speech. Samples generated by commercial and autoregressive language model systems proved hardest to detect (61.3 - 65.9%), while those from traditional seq2seq and flow-matching models remain easier to spot (75.4 - 76.8%). An ML detector that served as a reference point maintained over 94.5% accuracy across all conditions. Our results suggest that the primary threat posed by modern deepfakes may not be mere deception, but the erosion of trust in genuine audio.

</details>

### [Raon-OpenTTS: Open Models and Data for Robust Text-to-Speech](2605.20830.md)
**Semin Kim, Seungjun Chung, Taehong Moon, Sangheon Lee et al.** · 2026-05-20

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) models show impressive speech naturalness and quality, yet the role of large-scale open data in driving this progress remains underexplored. In this work, we introduce Raon-OpenTTS, an open TTS model that performs competitively with state-of-the-art closed-data TTS models, and Raon-OpenTTS-Pool, a large-scale open dataset for reproducible TTS training. Raon-OpenTTS-Pool consists of 615K hours of 240M speech segments aggregated from publicly available English speech corpora and web-sourced recordings. With a model-based filtering pipeline applied to Raon-OpenTTS-Pool, we derive Raon-OpenTTS-Core, a curated, high-quality subset of 510K hours and 194M speech segments. Using Raon-OpenTTS-Core, we train Raon-OpenTTS, a series of diffusion transformer (DiT)-based TTS models from 0.3B to 1B parameters. On multiple benchmarks, Raon-OpenTTS-1B shows comparable performance to state-of-the-art models such as Qwen3-TTS and CosyVoice 3, which are trained on several million hours of proprietary speech data. Notably, on Seed-TTS-Eval, Raon-OpenTTS-1B achieves a word error rate (WER) of 1.78% and a speaker similarity (SIM) of 0.749, ranking second on WER and first on SIM among recent open-weight TTS baselines. On CV3-Hard-EN, Raon-OpenTTS-1B achieves a WER of 6.15% and a SIM of 0.775, ranking first on both metrics. Furthermore, to support robust evaluation, we introduce Raon-OpenTTS-Eval, a structured benchmark for assessing TTS robustness across diverse acoustic conditions including clean, noisy, in-the-wild, and expressive speech. On Raon-OpenTTS-Eval, Raon-OpenTTS-1B achieves the best average WER and SIM among all evaluated models, and the second-best human preference, as measured by comparative mean opinion score (CMOS). Our data pool, filtering pipeline, training code, and checkpoints are publicly available at https://github.com/krafton-ai/RAON-OpenTTS.

</details>

### [Evaluating Speech Articulation Synthesis with Articulatory Phoneme Recognition](2605.20920.md)
**Vinicius Ribeiro, Yves Laprie** · 2026-05-20

<details>
<summary>Abstract</summary>

Recent advances in machine learning and the availability of articulatory datasets allow vocal tract synthesis to be conditioned on phonetic sequences, a primary task of articulatory speech synthesis. However, quality assessment needs a better definition. Generally, ranking generative models is tricky due to subjectivity. However, articulatory synthesis has the additional difficulty of requiring specialized knowledge in vocal tract anatomy and acoustics. To address this problem, this paper proposes to evaluate speech articulation synthesis using phoneme recognition as a proxy. Our hypothesis is that phoneme recognition using articulatory features better captures nuances in phoneme production, such as correct places of articulation, which traditional metrics (e.g., point-wise distance metrics) do not. We train a neural network with acoustic and articulatory features extracted from a single-speaker RT-MRI dataset. Then, we compare the recognition performance when testing the model with different synthetic articulatory features. Our results show that our articulatory feature set is phonetically rich and helps exploring additional dimensions on speech articulation synthesis.

</details>

### [Thinking-while-speaking: A Controlled, Interleaved Reasoning Method for Real-Time Speech Generation](2605.20946.md)
**Xuan Du, Qiangyu Yan, Wenshuo Li, Borui Jiang et al.** · 2026-05-20

<details>
<summary>Abstract</summary>

The thinking-while-speaking paradigm aims to make AI communication more human. A key challenge is maintaining fluent speech while performing deep reasoning. Our method, InterRS, tackles this by inserting reasoning steps only during natural speech generation. This requires high-quality data where reasoning and speech are precisely aligned, and the length ratio are under controlled. We introduce a novel pipeline to generate such seamlessly interleaved audio data. To train our model, we combine interleaved SFT with refined data and reinforcement learning with two new rewards: a TA-Balance Reward to manage timing and thinking-answer ratio, and a Linguistic Quality Reward to refine expression. Experiments show our approach achieves 13% better performance on mathmatical and logic benchmarks while generating instant response like a spoken-language instruct model which outputs fast CoT response. Furthermore, our method generates more natural and fluent answers than prior methods.

</details>

### [DUET: Unified Dual-Space Emotion Control for Diffusion and Flow-Matching Driven Text-to-Speech](2606.00066.md)
**Xu Zhang, Longbing Cao, Zhangkai Wu** · 2026-05-20

<details>
<summary>Abstract</summary>

Diffusion and flow-matching based text-to-speech (TTS) models excel in naturalness but often lack explicit emotion control, as emotional signals remain entangled with speaker identity. We discover that emotion embedding emerges as a linearly decodable direction of frozen hidden states, nearly orthogonal to the direction embedding speaker identity. This inspires a plug-and-play framework DUET for emotion control over pretrained diffusion and flow-matching based TTS models. During generation, DUET unifies dual-space control to achieve fine-grained emotion intervention in a single per-step update: hidden space steering shifts generation along the target emotion direction, while mel-space guidance refines spectral details through gradients backpropagated from a differentiable vocoder. We validate DUET on five architecturally diverse pretrained TTS backbones across three datasets, where it outperforms 10 supervised state-of-the-art emotional TTS baselines across paradigms and achieves the highest human-rated emotion appropriateness. To further showcase its qualitative behavior, we deploy DUET on an Ameca humanoid robot, where it produces richly expressive emotional speech on the humanoid, demonstrating the strong potential for plug-and-play affective interaction for embodied agents.

</details>

### [Generative AI and Copyright Infringement: A Legal-Technical Analysis of AI Music Generation Systems Under 17 U.S.C. Title 17](2606.26111.md)
**Zuhaib Hussain Butt** · 2026-05-20

<details>
<summary>Abstract</summary>

Generative artificial intelligence (GenAI) has enabled users to synthesize music with text prompts, combining copyrighted lyrics, AI-composed melodies, and synthetic vocals that imitate real artists. This paper examines the legal and technical dimensions of AI-based music creation (e.g., Google Gemini's music tools) under U.S. copyright law. We analyze whether a user who inputs one artist's protected lyrics into a GenAI system, directs it to use another artist's voice or style, publishes the resulting song, and monetizes it violates 17 U.S.C. Section 106's exclusive rights [3]. The analysis integrates Title 17 doctrine (rights of reproduction, derivative works, distribution), 17 U.S.C. Section 114's narrow sound recording protection [4], and the new voice-cloning laws emerging at the state level [20]. We argue that unauthorized lyric copying poses a high risk of infringement of the musical composition, whereas mere AI-generated voice imitation typically falls outside federal sound recording protection and instead implicates state publicity rights [12], [13]. Recent cases and legislation (Concord v. Anthropic [10]; Kadrey v. Meta [11]; Lehrman v. Lovo [12]; Tennessee's "ELVIS Act" [20]; UMG v. Uncharted Labs [14]; etc.) illustrate this split. We map AI technical components (prompt encoding, latent diffusion, neural vocoders, speaker embeddings) to legal risks and identify a regulatory gap: federal law robustly protects lyrics and melody but currently provides limited remedies for synthesized vocal likeness [22], [23]. The paper concludes with policy suggestions for clearer rules on AI music creation.

</details>

### [Bridging the Gap: Converting Read Text to Conversational Dialogue](2605.18001.md)
**Parshav Singla, Agnik Banerjee, Aaditya Arora, Shruti Aggarwal et al.** · 2026-05-18

<details>
<summary>Abstract</summary>

In recent advancements within speech processing, converting read speech to conversational speech has gained significant attention. The primary challenge in this domain is maintaining naturalness and intelligibility while minimizing computational overhead for real-time applications. Traditional read speech often lacks the nuanced prosodic variation essential for natural conversational interactions, posing challenges for applications in virtual assistants, customer service, and language learning tools. This paper introduces a novel approach, Prosodic Adjustment with Conversational Context (PACC), aimed at converting read speech into natural conversational speech used in various modern applications. PACC utilizes advanced deep neural networks to analyze and modify prosodic features such as intonation, stress, and rhythm. Unlike conventional methods, our approach uses High-Fidelity Generative Adversarial Networks (HiFi-GAN) for speech synthesis. Our experimental results demonstrate significant improvements in speech conversion, enhancing naturalness and achieving better model accuracy with additional training on speech datasets. This research establishes new benchmarks in speech conversion tasks and Mean Opinion Score (MOS) evaluation for testing model accuracy, and we show that our approach can be successfully extended to other speech conversion applications.

</details>

### [Taming Audio VAEs via Target-KL Regularization](2605.17085.md)
**Prem Seetharaman, Rithesh Kumar** · 2026-05-16

<details>
<summary>Abstract</summary>

Latent diffusion models have emerged as the dominant paradigm for many generation tasks including audio generation such as text-to-audio, text-to-music and text-to-speech. A key component of latent diffusion is an autoencoder (VAE) that compresses high-dimensional signals into a low frame rate continuous representation that is conducive for downstream prediction. Regularizing these VAEs is challenging, as there is a trade-off between over-regularized (poor output quality) and under-regularized (difficult to predict) latent representations. We propose a framework for studying this trade-off through compression and train Audio VAEs at specific bitrates via target-KL regularization. This allows direct comparison to well-studied discrete neural audio codec models, and the construction of rate-distortion curves for audio VAEs. We evaluate the impact of target-KL regularization on text-to-sound generation and find that sweeping compression rates is helpful in identifying the optimal generation setting.

</details>

### [SemaVoice: Semantic-Aware Continuous Autoregressive Speech Synthesis](2605.16964.md)
**Huimeng Wang, Hui Lu, Jiajun Deng, Haoning Xu et al.** · 2026-05-16

<details>
<summary>Abstract</summary>

Continuous autoregressive speech synthesis has recently emerged as a promising direction for zero-shot text-to-speech (TTS). However, existing methods still suffer from a fundamental mismatch between semantic-prosodic modeling and reconstruction-driven continuous speech representations. This mismatch causes TTS models to focus excessively on low-level acoustic textures at the expense of high-level semantic coherence, further exacerbating error accumulation in autoregressive generation. To address this challenge, we propose SemaVoice, a semantic-aware continuous autoregressive framework for high-fidelity zero-shot TTS. SemaVoice introduces a Speech Foundation Model (SFM) guided alignment mechanism that refines continuous speech representations to better capture both local semantic consistency and global structural relationships. These representations condition a patch-wise diffusion head within the autoregressive framework for high-quality speech synthesis. Experimental results on the Seed-TTS benchmark show that SemaVoice achieves an English WER of 1.71\% and remains highly competitive with state-of-the-art open-source systems in both objective and subjective evaluations. The effectiveness of SFM guided alignment is further confirmed by significant improvements under varying representation granularities with a fixed information-rate constraint.

</details>

### [Voice "Cloning" is Style Transfer](2605.16578.md)
**Kaitlyn Zhou, Federico Bianchi, Martijn Bartelds, Anna Pot et al.** · 2026-05-15

<details>
<summary>Abstract</summary>

Artificially generated speech is increasingly embedded in everyday life. Voice cloning in particular enables applications where identity preservation is important, such as completing a recording, dubbing in a new language, or preserving the voices of individuals with speech loss. However, in our work, we find that despite the term, voice cloning does not faithfully ''clone'' an individual's voice. Instead, we find that widely-used voice cloning models systematically apply style transfer to source voices. As rated by human annotators, cloned voices are perceived as more authoritative, warm, customer-service-like, and human-like compared to their sources. Human annotators also report greater trust in cloned voices than source voices, and a greater willingness to disclose sensitive personal information to them. Our work furthermore shows that voice cloning leads to homogenization of speaker characteristics, as measured by reduced variance in accent, speaking rate, and the audio embedding space. Together, our results highlight a new set of limitations and risks of voice cloning technology and their potential impact on human behavior.

</details>

### [From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents](2605.15104.md)
**Md Tahmid Rahman Laskar, Xue-Yong Fu, Seyyed Saeed Sarfjoo, Quinten McNamara et al.** · 2026-05-14

<details>
<summary>Abstract</summary>

Voice agents increasingly require reliable tool use from speech, whereas prominent tool-calling benchmarks remain text-based. We study whether verified text benchmarks can be converted into controlled audio-based tool calling evaluations without re-annotating the tool schema and gold labels. Our dataset-agnostic framework uses text-to-speech, speaker variation, and environmental noise to create paired text-audio instances while preserving the original dataset annotations. Based on extensive evaluation of 7 omni-modal models on audio-converted versions of Confetti and When2Call, our framework demonstrates that the performance is strongly model- and task-dependent: Gemini-3.1-Flash-Live obtains the highest Confetti score (70.4), whereas GPT-Realtime-1.5 performs best on When2Call (71.9). On Confetti, the text-to-voice gap ranges from 1.8 points for Qwen3-Omni to 4.8 points for GPT-Realtime-1.5. A targeted analysis of failure cases demonstrates that degradations most often reflect misunderstandings of argument values in the speech. Considering real-world deployment scenarios, we further report text-only results, an ambiguity-based reformulation stress test, and a reference-free LLM-as-judge protocol validated against human preferences. Notably, we find that open-source Qwen3 judges with at least 8B parameters exceed 80% agreement with proprietary judges, supporting privacy-preserving evaluation. Overall, our framework provides a verifiable and reproducible first-stage diagnostic that complements purpose-built audio corpora.

</details>

### [AgentSteerTTS: A Multi-Agent Closed-Loop Framework for Composite-Instruction Text-to-Speech](2605.17583.md)
**Bin Kang, Shaoguo Wen, Yang Fan, Shunlong Wu et al.** · 2026-05-14

<details>
<summary>Abstract</summary>

While existing text-to-speech (TTS) models exhibit high expressiveness, fine-grained control over composite instructions remains challenging due to the structural mismatch between discrete textual intents and continuous acoustic realizations. Inspired by human cognitive decoupling, we introduce AgentSteerTTS, a multi-agent closed-loop framework designed for intent-faithful expressive control of composite instructions. First, in our framework, an adversarial disentanglement agent mitigates speaker-emotion leakage by learning separable identity and emotion-prosody subspaces with leakage-suppressing regularization. Next, a Dual-Stream Anchoring Controller grounds abstract intents using a large-scale acoustic prototype library: a Retrieval Agent selects expressive anchors, while a Synthesis Agent fuses them into continuous control vectors via gated attention. Finally, a Fast-Slow Feedback Agent refines output intensity through latent gradient correction and resolves semantic-acoustic mismatches using high-level perceptual critique. Experiments on a composite-instruction benchmark and public test sets show that AgentSteerTTS yields consistent and significant improvements to the baselines, demonstrating the effectiveness of the proposed method.

</details>

### [AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling](2605.11866.md)
**Yiming Ren, Xuenan Xu, Ziyang Zhang, Wen Wu et al.** · 2026-05-12

<details>
<summary>Abstract</summary>

Despite advances in text and visual generation, creating coherent long-form audio narratives remains challenging. Existing frameworks often exhibit limitations such as mismatched character settings with voice performance, insufficient self-correction mechanisms, and limited human interactivity. To address these challenges, we propose AuDirector, a self-reflective closed-loop multi-agent framework. Specifically, it involves an Identity-Aware Pre-production mechanism that transforms narrative texts into character profiles and utterance-level emotional instructions to retrieve suitable voice candidates and guide expressive speech synthesis, thereby promoting context-aligned voice adaptation. To enhance quality, a Collaborative Synthesis and Correction module introduces a closed-loop self-correction mechanism to systematically audit and regenerate defective audio components. Furthermore, a Human-Guided Interactive Refinement module facilitates user control by interpreting natural language feedback to interactively refine the underlying scripts. Experiments demonstrate that AuDirector achieves superior performance compared to state-of-the-art baselines in structural coherence, emotional expressiveness, and acoustic fidelity. Audio samples can be found at https://anonymous-itsh.github.io/.

</details>

### [Poly-SVC: Polyphony-Aware Singing Voice Conversion with Harmonic Modeling](2605.12310.md)
**Chen Geng, Meng Chen, Ruohua Zhou, Ruolan Liu et al.** · 2026-05-12

<details>
<summary>Abstract</summary>

Singing Voice Conversion (SVC) aims to transform a source singing voice into a target singer while preserving lyrics and melody. Most existing SVC methods depend on F0 extractors to capture the lead melody from clean vocals. However, no existing method can reliably extract clean vocals from accompanied recordings without leaving residual harmonies behind. In this paper, we innovatively propose Poly-SVC, a zero-shot, cross-lingual singing voice conversion system designed to process residual harmonies. Poly-SVC is composed of three key components: a Constant-Q Transform (CQT)-based pitch extractor to preserve both the lead melody and residual harmony, a random sampler to reduce interference information from the CQT and a diffusion decoder based on Conditional Flow Matching (CFM) that fuses pitch, content, and timbre features into natural-sounding polyphonic outputs. Experiments demonstrate that Poly-SVC surpasses the baseline models in naturalness, timbre similarity and harmony reconstruction across both harmony-rich and single-melody recordings.

</details>

### [AffectCodec: Emotion-Preserving Neural Speech Codec for Expressive Speech Modeling](2605.11098.md)
**Jiacheng Shi, Hongfei Du, Xinyuan Song, Y. Alicia Hong et al.** · 2026-05-11

<details>
<summary>Abstract</summary>

Neural speech codecs provide discrete representations for speech language models, but emotional cues are often degraded during quantization. Existing codecs mainly optimize acoustic reconstruction, leaving emotion expressiveness insufficiently modeled at the representation level. We propose an emotion-guided neural speech codec that explicitly preserves emotional information while maintaining semantic fidelity and prosodic naturalness. Our framework combines emotion-semantic guided latent modulation, relation-preserving emotional-semantic distillation, and emotion-weighted semantic alignment to retain emotionally salient cues under compression. Extensive evaluations across speech reconstruction, emotion recognition, and downstream text-to-speech generation demonstrate improved emotion consistency and perceptual quality without sacrificing content accuracy.

</details>

### [A Survey of Automated Presentation Coaching: Systems, Methods, and Open Challenges](2606.27380.md)
**Wen Liang, Li Siyan, Zackary Rackauckas, Julia Hirschberg** · 2026-05-11

<details>
<summary>Abstract</summary>

Automated coaching for oral presentations sits at the intersection of computer-assisted pronunciation training (CAPT), prosody modeling, and speech synthesis, yet no prior work has systematically surveyed and compared existing systems along these dimensions. This survey reviews and categorizes automated presentation coaching systems, spanning pronunciation tutors, fluency and prosody coaches, multimodal trainers, and conference Q&A practice tools. We introduce a five-dimensional task taxonomy - covering segmental pronunciation, lexical stress, suprasegmental prosody, pacing, and content faithfulness - and explicitly map surveyed systems onto it to reveal coverage gaps. We further review the core technical methods these systems employ: TTS-based exemplar generation and diagnostic methods for pronunciation, prosody, and fluency assessment. Key open challenges include the scarcity of annotated presentation corpora, achieving accent-fair feedback across diverse L1 backgrounds, and delivering low-latency diagnostics for real-time rehearsal.

</details>

### [Exploring Token-Space Manipulation in Latent Audio Tokenizers](2605.11192.md)
**Francesco Paissan, Luca Della Libera, Mirco Ravanelli, Cem Subakan** · 2026-05-11

<details>
<summary>Abstract</summary>

Neural audio codecs provide compact discrete representations for speech generation and manipulation. However, most codecs organize tokens as frame-level sequences, making it difficult to study or intervene on global factors of variation. In this work, we propose the Latent Audio Tokenizer for Token-space Editing (LATTE) that appends a fixed set of learnable latent tokens to the audio feature sequence and retains only these tokens for quantization and decoding. This design produces a compact, non-temporally aligned bottleneck in which each token can aggregate global information across the full utterance. We show that the resulting tokenizer preserves competitive reconstruction quality in low-bitrate speech coding settings while enabling simple token-space interventions. In particular, we find that swapping selected latent token positions between utterances can modify global attributes, such as speaker identity and background noise, and we evaluate these interventions on voice conversion and denoising tasks. Our results suggest that compact latent audio tokenizers can support controllable audio manipulation without supervision in task-specific editing models.

</details>

### [Kinetic-Optimal Scheduling with Moment Correction for Metric-Induced Discrete Flow Matching in Zero-Shot Text-to-Speech](2605.09386.md)
**Dong Yang, Yiyi Cai, Haoyu Zhang, Yuki Saito et al.** · 2026-05-10

<details>
<summary>Abstract</summary>

Metric-induced discrete flow matching (MI-DFM) exploits token-latent geometry for discrete generation, but its practical use is limited by two issues: heuristic schedulers requiring hyperparameter search, and finite-step path-tracking error from its first-order continuous-time Markov chain (CTMC) solver. We address both issues. First, we derive a kinetic-optimal scheduler for prescribed scalar-parameterized probability paths, and instantiate it for MI-DFM as a training-free numerical schedule that traverses the path at constant Fisher-Rao speed. Second, we introduce a finite-step moment correction that adjusts the jump probability while preserving the CTMC jump destination distribution. We validate the resulting method, GibbsTTS, on codec-based zero-shot text-to-speech (TTS). Under controlled comparisons with a unified architecture and large-scale dataset, GibbsTTS achieves the best objective naturalness and is preferred in subjective evaluations over masked discrete generative baselines. Additionally, in comparison with the evaluated state-of-the-art TTS systems, GibbsTTS shows strong speaker similarity, achieving the highest similarity on three of four test sets and ranking second on the fourth. Project page: https://ydqmkkx.github.io/GibbsTTSProject

</details>

### [Minimizing Modality Gap from the Input Side: Your Speech LLM Can Be a Prosody-Aware Text LLM](2605.05927.md)
**Wenqian Cui, Xiao-Hui Li, Daxin Tan, Qiyong Zheng et al.** · 2026-05-07

<details>
<summary>Abstract</summary>

Speech large language models (SLMs) are typically built from text large language model (TLM) checkpoints, yet they still suffer from a substantial modality gap. Prior work has mainly attempted to reduce this gap from the output side by making speech generation more text-like, but the gap remains. We argue that the key remaining bottleneck lies on the input side. We propose TextPro-SLM, an SLM that makes spoken input more closely resemble that of a prosody-aware text LLM. TextPro-SLM combines WhisperPro, a unified speech encoder that produces synchronized text tokens and prosody embeddings, with an LLM backbone trained to preserve the semantic capabilities of the original TLM while learning paralinguistic understanding. Experiments show that TextPro-SLM achieves the lowest modality gap among leading SLMs at both 3B and 7B scales, while also delivering strong overall performance on paralinguistic understanding tasks. These gains are achieved with only roughly 1,000 hours of LLM training audio, suggesting that reducing the modality gap from the input side is both effective and data-efficient.

</details>

### [X-Voice: Enabling Everyone to Speak 30 Languages via Zero-Shot Cross-Lingual Voice Cloning](2605.05611.md)
**Rixi Xu, Qingyu Liu, Haitao Li, Yushen Chen et al.** · 2026-05-07

<details>
<summary>Abstract</summary>

In this paper, we present X-Voice, a 0.4B multilingual zero-shot voice cloning model that clones arbitrary voices and enables everyone to speak 30 languages. X-Voice is trained on a 420K-hour multilingual corpus using the International Phonetic Alphabet (IPA) as a unified representation. To eliminate the reliance on prompt text without complex preprocessing like forced alignment, we design a two-stage training paradigm. In Stage 1, we establish X-Voice$_{\text{s1}}$ through standard conditional flow-matching training and use it to synthesize 10K hours of speaker-consistent segments as audio prompts. In Stage 2, we fine-tune on these audio pairs with prompt text masked to derive X-Voice$_{\text{s2}}$, which enables zero-shot voice cloning without requiring transcripts of audio prompts. Architecturally, we extend F5-TTS by implementing a dual-level injection of language identifiers and decoupling and scheduling of Classifier-Free Guidance to facilitate multilingual speech synthesis. Subjective and objective evaluation results demonstrate that X-Voice outperforms existing flow-matching based multilingual systems like LEMAS-TTS and achieves zero-shot cross-lingual cloning capabilities comparable to billion-scale models such as Qwen3-TTS. To facilitate research transparency and community advancement, we open-source all related resources.

</details>

### [WavCube: Unifying Speech Representation for Understanding and Generation via Semantic-Acoustic Joint Modeling](2605.06407.md)
**Guanrou Yang, Tian Tan, Qian Chen, Zhikang Niu et al.** · 2026-05-07

<details>
<summary>Abstract</summary>

Integrating speech understanding and generation is a pivotal step toward building unified speech models. However, the different representations required for these two tasks currently pose significant compatibility challenges. Typically, semantics-oriented features are learned from self-supervised learning (SSL), and acoustic-oriented features from reconstruction. Such fragmented representations hinder the realization of truly unified speech systems. We present WavCube, a compact continuous latent derived from an SSL speech encoder that simultaneously supports speech understanding, reconstruction, and generation. WavCube employs a two-stage training scheme. Stage 1 trains a semantic bottleneck to filter off-manifold redundancy that makes raw SSL features intractable for diffusion. Stage 2 injects fine-grained acoustic details via end-to-end reconstruction, while a semantic anchoring loss ensures the representation remains grounded within its original semantic manifold. Comprehensive experiments show that WavCube closely approaches WavLM performance on SUPERB despite an 8x dimensional compression, attains reconstruction quality on par with existing acoustic representations, delivers state-of-the-art zero-shot TTS performance with markedly faster training convergence, and excels in speech enhancement, separation, and voice conversion tasks on the SUPERB-SG benchmark. Systematic ablations reveal that WavCube's two-stage recipe resolves two intrinsic flaws of SSL features for generative modeling, paving the way for future unified speech systems. Codes and checkpoints are available at https://github.com/yanghaha0908/WavCube.

</details>

### [MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model](2605.03937.md)
**Jingyao Gong** · 2026-05-05

<details>
<summary>Abstract</summary>

MiniMind-O is an open 0.1B-scale omni model built on the MiniMind language model. It accepts text, speech, and image inputs, and returns both text and streaming speech. The release includes model code, checkpoints, and the main Parquet training datasets for text-to-audio, image-to-text, and audio-to-audio training, making the complete interaction loop directly inspectable. The model uses a full MiniMind backbone as the Thinker and an independent four-layer Talker made from MiniMind blocks. Frozen SenseVoice-Small and SigLIP2 encoders provide speech and image features, which are mapped by lightweight MLP projectors and injected at modality-placeholder positions. The Talker reads a middle-layer Thinker state together with an autoregressive eight-layer Mimi-code buffer. Speaker control is handled by a dedicated speaker token, right-aligned reference codec prompts, and precomputed CAM++ speaker embeddings, so voice conditioning remains part of the audio-code context rather than a separate TTS module. With a 768-dimensional Talker, the dense and MoE variants reach average CERs of 0.0897 and 0.0900 in Thinker--Talker consistency evaluation, with overall voice-cloning similarities of 0.5995 and 0.5937. Beyond reporting a working system, the paper identifies three scale-critical design choices for small omni models: middle-layer semantic bridging, a released multimodal sequence format, and a parameter-efficient eight-codebook interface.

</details>

### [Tibetan-TTS:Low-Resource Tibetan Speech Synthesis with Large Model Adaptation](2605.02496.md)
**Jiaxu He, Chao Wang, Jie Lian, Yuqing Cai et al.** · 2026-05-04

<details>
<summary>Abstract</summary>

Tibetan text-to-speech (TTS) has long been challenged by scarce speech resources, significant dialectal variation, and the complex mapping between written text and spoken pronunciation. To address these issues, this work presents, to the best of our knowledge, the first large-model-based Tibetan TTS system in the industry, built upon a large speech synthesis model developed by Xingchen AGI Lab. The proposed system integrates data quality enhancement, Tibetan-oriented text representation and tokenizer adaptation, and cross-lingual adaptive training for low-resource Tibetan speech synthesis. Experimental results show that the system can generate stable, natural, and intelligible Tibetan speech under low-resource conditions. In subjective evaluation, the MOS scores of the syllable-level and BPE-based systems reach 4.28 and 4.35, while their pronunciation accuracies reach 97.6% and 96.6%, respectively, outperforming an external commercial Tibetan TTS interface. These results demonstrate that combining a large-model backbone with Tibetan-oriented text representation adaptation and cross-lingual adaptive training enables highly usable low-resource Tibetan speech synthesis, and also provides a technical foundation for future unified multi-dialect Tibetan speech synthesis.

</details>

### [Toward Fine-Grained Speech Inpainting Forensics:A Dataset, Method, and Metric for Multi-Region Tampering Localization](2605.02223.md)
**Tung Vu, Yen Nguyen, Hai Nguyen, Cuong Pham et al.** · 2026-05-04

<details>
<summary>Abstract</summary>

Recent advances in voice cloning and text-to-speech synthesis have made partial speech manipulation - where an adversary replaces a few words within an utterance to alter its meaning while preserving the speaker's identity - an increasingly realistic threat. Existing audio deepfake detection benchmarks focus on utterance-level binary classification or single-region tampering, leaving a critical gap in detecting and localizing multiple inpainted segments whose count is unknown a priori. We address this gap with three contributions. First, we introduce MIST (Multiregion Inpainting Speech Tampering), a large-scale multilingual dataset spanning 6 languages with 1-3 independently inpainted word-level segments per utterance, generated via LLM-guided semantic replacement and neural voice cloning, with fake content constituting only 2-7% of each utterance. Second, we propose ISA (Iterative Segment Analysis), a backbone-agnostic framework that performs coarse-to-fine sliding-window classification with gap-tolerant region proposal and boundary refinement to recover all tampered regions without prior knowledge of their count. Third, we define SF1@tau, a segment-level F1 metric based on temporal IoU matching that jointly evaluates region count accuracy and localization precision. Zero-shot evaluation reveals that partial inpainting at word granularity remains unsolved by existing deepfake detectors: utterance-level classifiers trained on fully synthesized speech assign near zero fake probability to MIST utterances where only 2-7% of content is manipulated. ISA consistently outperforms non-iterative baselines in this challenging setting, and the dataset, code, and evaluation toolkit are publicly released.

</details>

### [Phoneme-Level Deepfake Detection Across Emotional Conditions Using Self-Supervised Embeddings](2605.03079.md)
**Vamshi Nallaguntla, Shruti Kshirsagar, Anderson R. Avila** · 2026-05-04

<details>
<summary>Abstract</summary>

Recent advances in emotional voice conversion (EVC) have enabled the generation of expressive synthetic speech, raising new concerns in audio deepfake detection. Existing approaches treat speech as a homogeneous signal and largely overlook its internal phonetic structure, limiting their interpretability in emotionally conditioned settings. In this work, we propose a phoneme-level framework to analyze emotionally manipulated synthetic speech using real and EVC-generated speech under matched emotional conditions with shared transcripts, phoneme-aligned TextGrids, and WavLM-based embeddings. Our results show that phoneme behavior varies across categories, with complex vowels and fricatives exhibiting higher divergence while simpler phonemes remain more stable. Phonemes with larger distributional differences are also found to be more easily detected, consistently across multiple emotions and synthesis systems. These findings demonstrate that phoneme-level analysis is an effective and interpretable approach for detecting emotionally manipulated synthetic speech.

</details>

### [Low-Cost Detection of Degraded Voice Clones via Source-Output Acoustic Consistency](2605.08165.md)
**Jana Shokr, Minos Papadopoulos, Jeremy Cooperstock, Pavo Orepic** · 2026-05-04

<details>
<summary>Abstract</summary>

Recent advances in generative speech have increased the need for automatic detection of obviously failed synthetic outputs. This is particularly important in clinical settings such as AVATAR therapy, in which schizophrenia patients engage with a computer-generated representation of their hallucinated voices and degraded synthesis may disrupt immersion and therapeutic engagement. We investigate whether low-dimensional, interpretable source-output acoustic features can provide a lightweight first-pass detector of degraded voice-cloning outputs. Motivated by source-filter models of speech, we first test median fundamental frequency (f0) as a source-related consistency measure, and compare it with vocal tract length (VTL) as a filter-related measure and Harmonics-to-Noise Ratio (HNR) as a noise-related descriptor. Human-labeled voice-cloning samples generated with two vocoder families, WaveRNN (n=54) and HiFi-GAN (n=40), were evaluated using an asymmetric thresholding procedure in the input-output feature space. For WaveRNN, f0 and HNR both achieved 85.2% accuracy, outperforming VTL (64.8%). For HiFi-GAN, HNR achieved 80.0% accuracy, followed by f0 at 77.5% and VTL at 67.5%. Sample-level overlap and spectrographic inspection showed that f0 and HNR capture partly distinct failure patterns, rather than providing redundant rankings of the same samples. These results show that simple source-output acoustic consistency measures can provide useful first-pass detection of degraded voice clones, and support the use of interpretable threshold-based screening in applications where failed synthetic speech must be rejected quickly.

</details>

### [MelShield: Robust Mel-Domain Audio Watermarking for Provenance Attribution of AI Generated Synthesized Speech](2605.01515.md)
**Yutong Jin, Qi Li, Lingshuang Liu, Jianbing Ni** · 2026-05-02

<details>
<summary>Abstract</summary>

In this paper, we propose MelShield, a robust, in-generation, keyed audio watermarking framework that embeds identifiable signals into AI-generated audio for copyright protection and reliable attribution. Specifically, MelShield operates in the Mel-spectrogram domain during the generation process, targeting intermediate acoustic representations in Mel-conditioned pipelines for text-to-speech (TTS) generation. The core idea is to treat the intermediate Mel-spectrogram as the host signal and embed a short binary payload via low-energy, keyed spread-spectrum perturbations distributed across carefully selected time-frequency regions prior to waveform synthesis. By performing watermarking before vocoder inference, MelShield remains plug-and-play for Mel-conditioned TTS architectures and does not require modification or retraining of the underlying TTS generation vocoder, such as DiffWave and HiFi-GAN. Moreover, the multi-user keyed construction enables scalable user-specific attribution, while the keyed verification mechanism limits unauthorized decoding, thereby reducing the risk of large-scale extractor probing and adversarial analysis. Extensive experiments on DiffWave and HiFi-GAN demonstrate that MelShield achieves reliable watermark extraction, approaching 100\% bit accuracy, even under signal distortions, e.g., compression and additive noise, while preserving high perceptual audio quality.

</details>

### [LASE: Language-Adversarial Speaker Encoding for Indic Cross-Script Identity Preservation](2605.00777.md)
**Venkata Pushpak Teja Menta** · 2026-05-01

<details>
<summary>Abstract</summary>

A speaker encoder used in multilingual voice cloning should treat the same speaker identically regardless of which script the audio was uttered in. Off-the-shelf encoders do not, and the failure is accent-conditional. On a 1043-pair Western-accented voice corpus across English, Hindi, Telugu, and Tamil, WavLM-base-plus-sv loses 0.082 absolute cosine similarity when the same voice changes script and ECAPA-TDNN loses 0.105. On a 1369-pair Indian-accented voice corpus, the gap shrinks to 0.006 (WavLM-SV) and 0.044 (ECAPA-TDNN). The leak is largest where it matters most for cross-script TTS: when a system projects a non-Indic-trained voice into Indic scripts. We present LASE (Language-Adversarial Speaker Encoder), a small projection head over frozen WavLM-base-plus trained with two losses: a supervised contrastive loss over voice identity, and a gradient-reversal cross-entropy against a 4-language classifier that pushes the embedding to be language-uninformative while remaining speaker-informative. Trained on 1118 quality-gated cross-script pairs synthesised from 8 commercial multilingual voices, LASE's residual gap is consistent with zero on both corpora (Delta = 0.013 Western, Delta = 0.026 Indian; both bootstrap 95% CIs include zero) and amplifies the cross-script-vs-floor margin 2.4-2.7x over both baselines. An ECAPA+GRL ablation shows the GRL objective improves either backbone but the WavLM choice contributes too. In synthetic multi-speaker diarisation, LASE matches ECAPA-TDNN on cross-script speaker recall (0.788 vs 0.789) with ~100x less training data. We release the r1 checkpoint, both corpora, and the bootstrap recipe.

</details>

### [SPARCLE: SPeaker-aware Aligned Representations via Contrastive Language Embeddings](2607.01238.md)
**Priyam Mazumdar, Yurii Halychanskyi, Steven Guo, Mark Hasegawa-Johnson et al.** · 2026-05-01

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis have shifted from phoneme representations to direct grapheme modeling. While phonemes address the one-to-many mapping between text and acoustics, they rely on grapheme-to-phoneme (G2P) systems that fail to capture speaker-specific acoustic variation. Prior work demonstrates that grapheme-based models outperform phoneme-based systems at scale, but not in low-resource settings. In this paper, we propose SPARCLE, a speaker-aware grapheme representation model that enriches characters with their precise acoustic realizations. SPARCLE is trained with a contrastive objective to align graphemes with corresponding Wav2Vec2 acoustic representations while conditioned on speaker identity. The resulting model serves as a replacement to G2P systems for downstream text-to-speech (TTS) tasks. We demonstrate that SPARCLE improves generation quality, reducing word error rates by half in extreme low-resource settings compared to standard grapheme-based models.

</details>

### [JaiTTS: A Thai Voice Cloning Model](2604.27607.md)
**Jullajak Karnjanaekarin, Pontakorn Trakuekul, Narongkorn Panitsrisit, Sumana Sumanakul et al.** · 2026-04-30

<details>
<summary>Abstract</summary>

We present JaiTTS-v1.0, a state-of-the-art Thai voice cloning text-to-speech model built through continual training on a large Thai-centric speech corpus. The model architecture is adapted from VoxCPM, a tokenizer-free autoregressive TTS model. JaiTTS-v1.0 directly processes numerals and Thai-English code-switching, which is very common in realistic settings, without explicit text normalization. We test the models on short-duration speech generation and long-duration speech generation, which reflects many real-world use cases. JaiTTS-v1.0 achieves a state-of-the-art CER of 1.94\%, surpassing the human ground truth of 1.98% for short-duration tasks while performing on par with human ground truth for long-duration tasks. In human judgment evaluations, our model wins 283 of 400 pairwise comparisons against commercial flagships, with only 58 losses.

</details>

### [MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction](2604.27393.md)
**Junbo Cui, Bokai Xu, Chongyi Wang, Tianyu Yu et al.** · 2026-04-30

<details>
<summary>Abstract</summary>

Recent progress in multimodal large language models (MLLMs) has brought AI capabilities from static offline data processing to real-time streaming interaction, yet they still remain far from human-level multimodal interaction. The key bottlenecks are no longer modality coverage or latency alone, but the interaction paradigm itself. First, perception and response are still separated into alternating phases, preventing models from incorporating new inputs for timely adjustment during generation. Second, most current models remain reactive, responding only to explicit user requests instead of acting proactively in the evolving multimodal environment. We present MiniCPM-o 4.5, our latest effort towards human-like multimodal interaction, which mitigates these gaps by real-time full-duplex omni-modal interaction. It can see, listen, and speak simultaneously in real-time, while also exhibiting proactive behaviors such as issuing reminders or comments based on its continuous understanding of the live scene. The key technique behind MiniCPM-o 4.5 is Omni-Flow, a unified streaming framework that aligns omni-modal inputs and outputs along a shared temporal axis. This formulation converts conventional turn-based interaction into a full-duplex, time-aligned process, enabling simultaneous perception and response and allowing proactive behavior to arise within the same framework. With a total of 9B parameters, MiniCPM-o 4.5 approaches Gemini 2.5 Flash in vision-language capabilities, delivering state-of-the-art open-source performance at its scale. It also surpasses Qwen3-Omni-30B-A3B in omni-modal understanding and delivers better speech generation, with significantly higher computation efficiency. Driven by its efficient architecture design and inference optimization, the model can perform real-time full-duplex omni-modal interaction on edge devices with less than 12GB RAM cost.

</details>

### [CANVAS: Captioning Art with Narrative Visual-Audio AI Systems](2606.09846.md)
**Vignesh Nagarajan** · 2026-04-30

<details>
<summary>Abstract</summary>

Visual art remains largely inaccessible to blind and low-vision (BLV) audiences due to brief or absent alt-text, which rarely conveys the sensory, spatial, or emotional qualities of an artwork. This study presents an automated workflow that generates multi-sensory art descriptions and synchronized audio narration using large language models and text-to-speech services. The system, orchestrated through Zapier, converts uploaded images into rich narrative captions without human intervention, enabling rapid, scalable production of accessible media. Quantitative evaluation across 50 artworks shows that AI-generated descriptions contain significantly higher lexical diversity, adjective density, and narrative detail than baseline captions, while maintaining comparable readability levels. Statistical tests (t-tests, ANOVA) confirm meaningful differences in richness and length, and the full pipeline produces text-plus-audio outputs in under 20 seconds per image at a cost below $0.05. Findings demonstrate that automated captioning can bridge gaps in museum and digital-collection accessibility, with implications for broader public engagement. Future work can incorporate user studies with BLV participants to assess comprehension, preference, and optimal levels of interpretive language.

</details>

### [EmoTransCap: Dataset and Pipeline for Emotion Transition-Aware Speech Captioning in Discourses](2604.26417.md)
**Shuhao Xu, Yifan Hu, Jingjing Wu, Zhihao Du et al.** · 2026-04-29

<details>
<summary>Abstract</summary>

Emotion perception and adaptive expression are fundamental capabilities in human-agent interaction. While recent advances in speech emotion captioning (SEC) have improved fine-grained emotional modeling, existing systems remain limited to static, single-emotion characterization within isolated sentences, neglecting dynamic emotional transitions at the discourse level. To address this gap, we propose Emotion Transition-Aware Speech Captioning (EmoTransCap), a paradigm that integrates temporal emotion dynamics with discourse-level speech description. To construct a dataset rich in emotion transitions while enabling scalable expansion, we design an automated pipeline for dataset creation. This is the first large-scale dataset explicitly designed to capture discourse-level emotion transitions. To generate semantically rich descriptions, we incorporate acoustic attributes and temporal cues from discourse-level speech. Our Multi-Task Emotion Transition Recognition (MTETR) model performs joint emotion transition detection and diarization. Leveraging the semantic analysis capabilities of LLMs, we produce two annotation versions: descriptive and instruction-oriented. These data and annotations offer a valuable resource for advancing emotion perception and emotional expressiveness. The dataset enables speech captions that capture emotional transitions, facilitating temporal-dynamic and fine-grained emotion understanding. We also introduce a controllable, transition-aware emotional speech synthesis system at the discourse level, enhancing anthropomorphic emotional expressiveness and supporting emotionally intelligent conversational agents.

</details>

### [The False Resonance: A Critical Examination of Emotion Embedding Similarity for Speech Generation Evaluation](2604.26347.md)
**Yun-Shao Tsai, Yi-Cheng Lin, Huang-Cheng Chou, Tzu-Wen Hsu et al.** · 2026-04-29

<details>
<summary>Abstract</summary>

Objective metrics for emotional expressiveness are vital for speech generation, particularly in expressive synthesis and voice conversion requiring emotional prosody transfer. To quantify this, the field widely relies on emotion similarity between reference and generated samples. This approach computes cosine similarity of embeddings from encoders like emotion2vec, assuming they capture affective cues despite linguistic and speaker variations. We challenge this assumption through controlled adversarial tasks and human alignment tests. Despite high classification accuracy, these latent spaces are unsuitable for zero-shot similarity evaluation. Representational limitations cause linguistic and speaker interference to overshadow emotional features, degrading discriminative ability. Consequently, the metric misaligns with human perception. This acoustic vulnerability reveals it rewards acoustic mimicry over genuine emotional synthesis.

</details>

### [PSP: An Interpretable Per-Dimension Accent Benchmark for Indic Text-to-Speech](2604.25476.md)
**Venkata Pushpak Teja Menta** · 2026-04-28

<details>
<summary>Abstract</summary>

Standard text-to-speech (TTS) evaluation measures intelligibility (WER, CER) and overall naturalness (MOS, UTMOS) but does not quantify accent. A synthesiser may score well on all four yet sound non-native on features that are phonemic in the target language. For Indic languages, these features include retroflex articulation, aspiration, vowel length, and the Tamil retroflex approximant (letter zha). We present PSP, the Phoneme Substitution Profile, an interpretable, per-phonological-dimension accent benchmark for Indic TTS. PSP decomposes accent into six complementary dimensions: retroflex collapse rate (RR), aspiration fidelity (AF), vowel-length fidelity (LF), Tamil-zha fidelity (ZF), Frechet Audio Distance (FAD), and prosodic signature divergence (PSD). The first four are measured via forced alignment plus native-speaker-centroid acoustic probes over Wav2Vec2-XLS-R layer-9 embeddings; the latter two are corpus-level distributional distances. In this v1 we benchmark four commercial and open-source systems (ElevenLabs v3, Cartesia Sonic-3, Sarvam Bulbul, Indic Parler-TTS) on Hindi, Telugu, and Tamil pilot sets, with a fifth system (Praxy Voice) included on all three languages, plus an R5->R6 case study on Telugu. Three findings: (i) retroflex collapse grows monotonically with phonological difficulty Hindi < Telugu < Tamil (~1%, ~40%, ~68%); (ii) PSP ordering diverges from WER ordering -- commercial WER-leaders do not uniformly lead on retroflex or prosodic fidelity; (iii) no single system is Pareto-optimal across all six dimensions. We release native reference centroids (500 clips per language), 1000-clip embeddings for FAD, 500-clip prosodic feature matrices for PSD, 300-utterance golden sets per language, scoring code under MIT, and centroids under CC-BY. Formal MOS-correlation is deferred to v2; v1 reports five internal-consistency signals plus a native-audio sanity check.

</details>

### [Robust Accent Identification via Voice Conversion and Non-Timbral Embeddings](2604.25332.md)
**Rayane Bakari, Olivier Le Blouch, Nicolas Gengembre, Nicholas Evans** · 2026-04-28

<details>
<summary>Abstract</summary>

Automatic accent identification (AID) remains a challenging task due to the complex variability of accents, the entanglement of accent cues with speaker traits, and the scarcity of reliable accentlabelled data. To address these challenges, we propose a speaker augmentation strategy using voice conversion (VC), with which we generate additional training data by converting original training utterances into different speaker voices while preserving accentual cues. For this purpose, we select two recent VC systems and evaluate their capability to preserve accent. Alternatively, we also explore the use of non-timbral embeddings in AID, for their ability to convey accent information among other non timbral cues. The effectiveness of both methods is demonstrated on the GenAID benchmark, achieving a new state-of-the-art F1-score of 0.66, compared to the previous score of 0.55. Beyond AID, we show that non-timbral embeddings enable accent-controlled Text-to-Speech, producing high-fidelity speech with accurate accent transfer.

</details>

### [One Voice, Many Tongues: Cross-Lingual Voice Cloning for Scientific Speech](2604.26136.md)
**Amanuel Gizachew Abebe, Yasmin Moslem** · 2026-04-28

<details>
<summary>Abstract</summary>

Preserving a speaker's voice identity while generating speech in a different language remains a fundamental challenge in spoken language technology, particularly in specialized domains such as scientific communication. In this paper, we address this challenge through our system submission to the International Conference on Spoken Language Translation (IWSLT 2026), the Cross-Lingual Voice Cloning shared task. First, we evaluate several state-of-the-art voice cloning models for cross-lingual speech generation of scientific texts in Arabic, Chinese, and French. Then, we build voice cloning systems based on the OmniVoice foundation model. We employ data augmentation via multi-model ensemble distillation from the ACL 60/60 corpus. We investigate the effect of using this synthetic data for fine-tuning, demonstrating consistent improvements in intelligibility (WER and CER) across languages while preserving speaker similarity.

</details>

### [AMAVA: Adaptive Motion-Aware Video-to-Audio Framework for Visually-Impaired Assistance](2604.23909.md)
**Benjamin Klein, Kazi Ruslan Rahman, Sanchita Ghose** · 2026-04-26

<details>
<summary>Abstract</summary>

Navigational aids for blind and low vision individuals struggle conveying dynamic real-world environments, leading to cognitive overload from continuous, undifferentiated feedback. We present AMAVA, a novel real-time video-to-audio framework that converts mobile device video into contextually relevant sound effects or text-to-speech descriptions. We propose a motion-aware pipeline using a lightweight AI classification model to distinguish between low and high-movement scenes followed by a real-time text-to-audio synthesis pipeline to enhance environmental perception more efficiently. In static environments, AMAVA generates spoken audio scene descriptions for situational awareness. In high-movement situations, it prioritizes safety by delivering sound cues, such as spoken hazard alerts and environmental sound effects. These audio outputs are produced by a decoder-only transformer-based vision-language model with mixture-of-experts and cross-modal attention for visual understanding, in conjunction with neural text-to-speech and natural sound synthesis networks. The proposed framework uses prompt-based caching and category-specific throttling to avoid auditory clutter and minimize latency. We present a comprehensive evaluation of the system, including a real-time navigation study comparing a white cane alone versus with AMAVA, that shows a significant increase in user confidence and perceived safety.

</details>

### [Talking Slide Avatars: Open-Source Multimodal Communication Approach for Teaching](2604.23703.md)
**Xinxing Wu** · 2026-04-26

<details>
<summary>Abstract</summary>

Slide-based teaching is widely used in higher education, yet in online, hybrid, and asynchronous contexts, slides often lose the instructor presence, narrative continuity, and expressive framing that help learners connect with content. Full lecture video can partly restore these qualities, but it is time-consuming to record, revise, and reuse. This study addresses that pedagogical and production challenge by presenting a practice-based analysis of an open-source workflow for creating talking slide avatars for slide-based teaching. The workflow integrates OpenVoice for text-to-speech generation and voice cloning with Ditto-TalkingHead for audio-driven talking-image synthesis, enabling instructors to transform a script and a static portrait into a short narrated video that can be embedded in slide decks or HTML-based lecture materials. Rather than treating this workflow merely as a technical solution, the study frames talking slide avatars as multimodal communication artifacts at the intersection of digital pedagogy, aesthetic education, and art-technology practice. Using a practice-based implementation and analytic reflection approach, the study documents the production pipeline, examines its communicative and aesthetic affordances, and proposes practical guidelines for script length, image selection, pacing, disclosure, accessibility, and ethical use. The study makes three primary contributions: it presents an educator-oriented open-source production model, reframes talking avatars as an educational communication design problem, and proposes a responsible pathway for incorporating generative synthetic media into teaching. It concludes that short, transparent, and carefully designed avatars can humanize slide-based instruction while providing a reusable communicative layer for introductions, transitions, reminders, and recaps across online, hybrid, and asynchronous learning environments.

</details>

### [RTCFake: Speech Deepfake Detection in Real-Time Communication](2604.23742.md)
**Jun Xue, Zhuolin Yi, Yihuan Huang, Yanzhen Ren et al.** · 2026-04-26

<details>
<summary>Abstract</summary>

With the rapid advancement of speech generation technologies, the threat posed by speech deepfakes in real-time communication (RTC) scenarios has intensified. However, existing detection studies mainly focus on offline simulations and struggle to cope with the complex distortions introduced during RTC transmission, including unknown speech enhancement processes (e.g., noise suppression) and codec compression. To address this challenge, we present the first large-scale speech deepfake dataset tailored for RTC scenarios, termed \textit{RTCFake}, totaling approximately 600 hours. The dataset is constructed by transmitting speech through multiple mainstream social media and conferencing platforms (e.g., Zoom), enabling precise pairing between offline and online speech. In addition, we propose a phoneme-guided consistency learning (PCL) strategy that enforces models to learn platform-invariant semantic structural representations. In this paper, the RTCFake dataset is divided into training, development, and evaluation sets. The evaluation set further includes both unseen RTC platforms and unseen complex noise conditions, thereby providing a more realistic and challenging evaluation benchmark for speech deepfake detection. Furthermore, the proposed PCL strategy achieves significant improvements in both cross-platform generalization and noise robustness, offering an effective and generalizable modeling paradigm. The \textit{RTCFake} dataset is provided in the {https://huggingface.co/datasets/JunXueTech/RTCFake}.

</details>

### [TTS-PRISM: A Perceptual Reasoning and Interpretable Speech Model for Fine-Grained Diagnosis](2604.22225.md)
**Xi Wang, Jie Wang, Xingchen Song, Baijun Song et al.** · 2026-04-24

<details>
<summary>Abstract</summary>

While generative text-to-speech (TTS) models approach human-level quality, monolithic metrics fail to diagnose fine-grained acoustic artifacts or explain perceptual collapse. To address this, we propose TTS-PRISM, a multi-dimensional diagnostic framework for Mandarin. First, we establish a 12-dimensional schema spanning stability to advanced expressiveness. Second, we design a targeted synthesis pipeline with adversarial perturbations and expert anchors to build a high-quality diagnostic dataset. Third, schema-driven instruction tuning embeds explicit scoring criteria and reasoning into an efficient end-to-end model. Experiments on a 1,600-sample Gold Test Set show TTS-PRISM outperforms generalist models in human alignment. Profiling six TTS paradigms establishes intuitive diagnostic flags that reveal fine-grained capability differences. TTS-PRISM is open-source, with code and checkpoints at https://github.com/xiaomi-research/tts-prism.

</details>

### [UniSonate: A Unified Model for Speech, Music, and Sound Effect Generation with Text Instructions](2604.22209.md)
**Chunyu Qiang, Xiaopeng Wang, Kang Yin, Yuzhe Liang et al.** · 2026-04-24

<details>
<summary>Abstract</summary>

Generative audio modeling has largely been fragmented into specialized tasks, text-to-speech (TTS), text-to-music (TTM), and text-to-audio (TTA), each operating under heterogeneous control paradigms. Unifying these modalities remains a fundamental challenge due to the intrinsic dissonance between structured semantic representations (speech/music) and unstructured acoustic textures (sound effects). In this paper, we introduce UniSonate, a unified flow-matching framework capable of synthesizing speech, music, and sound effects through a standardized, reference-free natural language instruction interface. To reconcile structural disparities, we propose a novel dynamic token injection mechanism that projects unstructured environmental sounds into a structured temporal latent space, enabling precise duration control within a phoneme-driven Multimodal Diffusion Transformer (MM-DiT). Coupled with a multi-stage curriculum learning strategy, this approach effectively mitigates cross-modal optimization conflicts. Extensive experiments demonstrate that UniSonate achieves state-of-the-art performance in instruction-based TTS (WER 1.47%) and TTM (SongEval Coherence 3.18), while maintaining competitive fidelity in TTA. Crucially, we observe positive transfer, where joint training on diverse audio data significantly enhances structural coherence and prosodic expressiveness compared to single-task baselines. Audio samples are available at https://qiangchunyu.github.io/UniSonate/.

</details>

### [Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages](2604.21481.md)
**Srija Anand, Ashwin Sankar, Ishvinder Sethi, Aaditya Pareek et al.** · 2026-04-23

<details>
<summary>Abstract</summary>

Crowdsourced pairwise evaluation has emerged as a scalable approach for assessing foundation models. However, applying it to Text to Speech(TTS) introduces high variance due to linguistic diversity and multidimensional nature of speech perception. We present a controlled multidimensional pairwise evaluation framework for multilingual TTS that combines linguistic control with perceptually grounded annotation. Using 5K+ native and code-mixed sentences across 10 Indic languages, we evaluate 7 state-of-the-art TTS systems and collect over 120K pairwise comparisons from over 1900 native raters. In addition to overall preference, raters provide judgments across 6 perceptual dimensions: intelligibility, expressiveness, voice quality, liveliness, noise, and hallucinations. Using Bradley-Terry modeling, we construct a multilingual leaderboard, interpret human preference using SHAP analysis and analyze leaderboard reliability alongside model strengths and trade-offs across perceptual dimensions.

</details>

### [MAGIC-TTS: Fine-Grained Controllable Speech Synthesis with Explicit Local Duration and Pause Control](2604.21164.md)
**Jialong Mai, Xiaofen Xing, Xiangmin Xu** · 2026-04-23

<details>
<summary>Abstract</summary>

Fine-grained local timing control is still absent from modern text-to-speech systems: existing approaches typically provide only utterance-level duration or global speaking-rate control, while precise token-level timing manipulation remains unavailable. To the best of our knowledge, MAGIC-TTS is the first TTS model with explicit local timing control over token-level content duration and pause. MAGIC-TTS is enabled by explicit token-level duration conditioning, carefully prepared high-confidence duration supervision, and training mechanisms that correct zero-value bias and make the model robust to missing local controls. On our timing-control benchmark, MAGIC-TTS substantially improves token-level duration and pause following over spontaneous synthesis. Even when no timing control is provided, MAGIC-TTS maintains natural high-quality synthesis. We further evaluate practical local editing with a scenario-based benchmark covering navigation guidance, guided reading, and accessibility-oriented code reading. In this setting, MAGIC-TTS realizes a reproducible uniform-timing baseline and then moves the edited regions toward the requested local targets with low mean bias. These results show that explicit fine-grained controllability can be implemented effectively in a high-quality TTS system and can support realistic local timing-editing applications.

</details>

### [SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation](2604.20842.md)
**Ruohan Liu, Shukang Yin, Tao Wang, Dong Zhang et al.** · 2026-04-22

<details>
<summary>Abstract</summary>

Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.

</details>

### [Text-To-Speech with Chain-of-Details: modeling temporal dynamics in speech generation](2604.19330.md)
**Jianbo Ma, Richard Cartwright** · 2026-04-21

<details>
<summary>Abstract</summary>

Recent advances in Text-To-Speech (TTS) synthesis have seen the popularity of multi-stage approaches that first predict semantic tokens and then generate acoustic tokens. In this paper, we extend the coarse-to-fine generation paradigm to the temporal domain and introduce Chain-of-Details (CoD), a novel framework that explicitly models temporal coarse-to-fine dynamics in speech generation using a cascaded architecture. Our method progressively refines temporal details across multiple stages, with each stage targeting a specific temporal granularity. All temporal detail predictions are performed using a shared decoder, enabling efficient parameter utilization across different temporal resolutions. Notably, we observe that the lowest detail level naturally performs phonetic planning without the need for an explicit phoneme duration predictor. We evaluate our method on several datasets and compare it against several baselines. Experimental results show that CoD achieves competitive performance with significantly fewer parameters than existing approaches. Our findings demonstrate that explicit modeling of temporal dynamics with the CoD framework leads to more natural speech synthesis.

</details>

### [Voice Mapping of Text-to-Speech Systems: A Metric-Based Approach for Voice Quality Assessment](2605.00861.md)
**Huanchen Cai, Sten Ternström** · 2026-04-21

<details>
<summary>Abstract</summary>

This study investigates voice mapping as an evaluation framework for text-to-speech (TTS) synthesis quality. The study analyzes six TTS models, including historical and recent ones. The metrics are crest factor, spectrum balance, and cepstral peak prominence (CPPs). We investigated 6 influential TTS models: Merlin, Tacotron 2, Transformer TTS, FastSpeech 2, Glow-TTS, and VITS. The results demonstrate that voice range serves as a primary indicator of model capability, with VITS showing the largest range among tested models. Glow-TTS exhibited superior performance in soft phonation, indicated by higher spectrum balance, despite limited voice range. The results showed that the CPPs values between 7-8 dB indicate natural voice quality, while with CPPs exceeding 10 dB, the speech tends to sound robotic. These findings underscore the need for voice mapping to evaluate vocal effort, and capture how TTS systems handle voice dynamic and expressiveness.

</details>

### [Self-EmoQ: Plutchik-Guided Value-based Planning to Drive Streaming Emotional TTS](2606.09837.md)
**Yue Zhao, Hongyan Li, Yong Chen, Luo Ji** · 2026-04-21

<details>
<summary>Abstract</summary>

Emotional interaction is increasingly crucial for conversational AI, yet current systems lack a self-emotion determination mechanism to drive the streaming text-to-speech (TTS) synthesis. We propose an emotion-planning framework that determines the emotion prior to the textual generation, grounding the downstream emotional TTS in a streaming manner. The framework is implemented by a plug-and-play LLM module, initialized from pretrained LLMs, and trained by reinforcement learning (RL) with emotions as the actions. A hybrid reward is employed which combines imitation signals with theory-driven scoring, in which the theory of Plutchik's wheel of emotions is adopted. By experiments on DailyDialog, EmoryNLP, IMEOCAP, and MELD, our method outperforms prompting and finetuning baselines on both emotion determination and response quality. We finally implement an entire streaming pipeline for real-time deployment, with the speech quality confirming the framework's emotional alignment, contextual coherence, and expressive fluency. Codes, cases, and demos are available in https://sixingdeguo.github.io/EmoQ-page/.

</details>

### [MINT-Bench: A Comprehensive Multilingual Benchmark for Instruction-Following Text-to-Speech](2604.17958.md)
**Huakang Chen, Jingbin Hu, Liumeng Xue, Qirui Zhan et al.** · 2026-04-20

<details>
<summary>Abstract</summary>

Instruction-following text-to-speech (TTS) has emerged as an important capability for controllable and expressive speech generation, yet its evaluation remains underdeveloped due to limited benchmark coverage, weak diagnostic granularity, and insufficient multilingual support. We present \textbf{MINT-Bench}, a comprehensive multilingual benchmark for instruction-following TTS. MINT-Bench is built upon a hierarchical multi-axis taxonomy, a scalable multi-stage data construction pipeline, and a hierarchical hybrid evaluation protocol that jointly assesses content consistency, instruction following, and perceptual quality. Experiments across ten languages show that current systems remain far from solved: frontier commercial systems lead overall, while leading open-source models become highly competitive and can even outperform commercial counterparts in localized settings such as Chinese. The benchmark further reveals that harder compositional and paralinguistic controls remain major bottlenecks for current systems. We release MINT-Bench together with the data construction and evaluation toolkit to support future research on controllable, multilingual, and diagnostically grounded TTS evaluation. The leaderboard and demo are available at https://longwaytog0.github.io/MINT-Bench/

</details>

### [HCFD: A Benchmark for Audio Deepfake Detection in Healthcare](2604.17642.md)
**Mohd Mujtaba Akhtar, Girish, Muskaan Singh** · 2026-04-19

<details>
<summary>Abstract</summary>

In this study, we present Healthcare Codec-Fake Detection (HCFD), a new task for detecting codec-fakes under pathological speech conditions. We intentionally focus on codec based synthetic speech in this work, since neural codec decoding forms a core building block in modern speech generation pipelines. First, we release Healthcare CodecFake, the first pathology-aware dataset containing paired real and NAC-synthesized speech across multipl clinical conditions and codec families. Our evaluations show that SOTA codec-fake detectors trained primarily on healthy speech perform poorly on Healthcare CodecFake, highlighting the need for HCFD-specific models. Second, we demonstrate that PaSST outperforms existing speech-based models for HCFD, benefiting from its patch-based spectro-temporal representation. Finally, we propose PHOENIX-Mamba, a geometry-aware framework that models codec-fakes as multiple self-discovered modes in hyperbolic space and achieves the strongest performance on HCFD across clinical conditions and codecs. Experiments on HCFK show that PHOENIX-Mamba (PaSST) achieves the best overall performance, reaching 97.04 Acc on E-Dep, 96.73 on E-Alz, and 96.57 on E-Dys, while maintaining strong results on Chinese with 94.41 (Dep), 94.40 (Alz), and 93.20 (Dys). This geometry-aware formulation enables self-discovered clustering of heterogeneous codec-fake modes in hyperbolic space, facilitating robust discrimination under pathological speech variability. PHOENIX-Mamba achieves topmost performance on the HCFD task across clinical conditions and codecs.

</details>

### [AST: Adaptive, Seamless, and Training-Free Precise Speech Editing](2604.16056.md)
**Sihan Lv, Yechen Jin, Zhen Li, Jintao Chen et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Text-based speech editing aims to modify specific segments while preserving speaker identity and acoustic context. Existing methods rely on task-specific training, which incurs high data costs and struggles with temporal fidelity in unedited regions. Meanwhile, adapting Text-to-Speech (TTS) models often faces a trade-off between editing quality and consistency. To address these issues, we propose AST, an Adaptive, Seamless, and Training-free precise speech editing framework. Leveraging a pre-trained autoregressive TTS model, AST introduces Latent Recomposition to selectively stitch preserved source segments with newly synthesized targets. Furthermore, AST extends this latent manipulation to enable precise style editing for specific speech segments. To prevent artifacts at these edit boundaries, the framework incorporates Adaptive Weak Fact Guidance (AWFG). AWFG dynamically modulates a mel-space guidance signal, enforcing structural constraints only where necessary without disrupting the generative manifold. To fill the gap of publicly accessible benchmarks, we introduce LibriSpeech-Edit, a new and larger speech editing dataset. As existing metrics poorly evaluate temporal consistency in unedited regions, we propose Word-level Dynamic Time Warping (WDTW). Extensive experiments demonstrate that AST resolves the controllability-quality trade-off without extra training. Compared to the previous most temporally consistent baseline, AST improves consistency while reducing Word Error Rate by nearly 70%. Moreover, applying AST to a foundation TTS model reduces WDTW by 27%, achieving state-of-the-art speaker preservation and temporal fidelity.

</details>

### [Qwen3.5-Omni Technical Report](2604.15804.md)
**Qwen Team** · 2026-04-17

<details>
<summary>Abstract</summary>

In this work, we present Qwen3.5-Omni, the latest advancement in the Qwen-Omni model family. Representing a significant evolution over its predecessor, Qwen3.5-Omni scales to hundreds of billions of parameters and supports a 256k context length. By leveraging a massive dataset comprising heterogeneous text-vision pairs and over 100 million hours of audio-visual content, the model demonstrates robust omni-modality capabilities. Qwen3.5-Omni-plus achieves SOTA results across 215 audio and audio-visual understanding, reasoning, and interaction subtasks and benchmarks, surpassing Gemini-3.1 Pro in key audio tasks and matching it in comprehensive audio-visual understanding. Architecturally, Qwen3.5-Omni employs a Hybrid Attention Mixture-of-Experts (MoE) framework for both Thinker and Talker, enabling efficient long-sequence inference. The model facilitates sophisticated interaction, supporting over 10 hours of audio understanding and 400 seconds of 720P video (at 1 FPS). To address the inherent instability and unnaturalness in streaming speech synthesis, often caused by encoding efficiency discrepancies between text and speech tokenizers, we introduce ARIA. ARIA dynamically aligns text and speech units, significantly enhancing the stability and prosody of conversational speech with minimal latency impact. Furthermore, Qwen3.5-Omni expands linguistic boundaries, supporting multilingual understanding and speech generation across 10 languages with human-like emotional nuance. Finally, Qwen3.5-Omni exhibits superior audio-visual grounding capabilities, generating script-level structured captions with precise temporal synchronization and automated scene segmentation. Remarkably, we observed the emergence of a new capability in omnimodal models: directly performing coding based on audio-visual instructions, which we call Audio-Visual Vibe Coding.

</details>

### [NVBench: A Benchmark for Speech Synthesis with Non-Verbal Vocalizations](2604.16211.md)
**Liumeng Xue, Weizhen Bian, Jiahao Pan, Wenxuan Wang et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Non-verbal vocalizations (NVVs) like laugh, sigh, and sob are essential for human-like speech, yet standardized evaluation remains limited in jointly assessing whether systems can generate the intended NVVs, place them correctly, and keep them salient without harming speech. We present Non-verbal Vocalization Benchmark (NVBench), a bilingual (English/Chinese) benchmark that evaluates speech synthesis with NVVs. NVBench pairs a unified 45-type taxonomy with a curated bilingual dataset and introduces a multi-axis protocol that separates general speech naturalness and quality from NVV-specific controllability, placement, and salience. We benchmark 15 TTS systems using objective metrics, listening tests, and an LLM-based multi-rater evaluation. Results reveal that NVVs controllability often decouples from quality, while low-SNR oral cues and long-duration affective NVVs remain persistent bottlenecks. NVBench enables fair cross-system comparison across diverse control interfaces under a unified, standardized framework.

</details>

### [Hierarchical Codec Diffusion for Video-to-Speech Generation](2604.15923.md)
**Jiaxin Ye, Gaoxiang Cong, Chenhui Wang, Xin-Cheng Wen et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Video-to-Speech (VTS) generation aims to synthesize speech from a silent video without auditory signals. However, existing VTS methods disregard the hierarchical nature of speech, which spans coarse speaker-aware semantics to fine-grained prosodic details. This oversight hinders direct alignment between visual and speech features at specific hierarchical levels during property matching. In this paper, leveraging the hierarchical structure of Residual Vector Quantization (RVQ)-based codec, we propose HiCoDiT, a novel Hierarchical Codec Diffusion Transformer that exploits the inherent hierarchy of discrete speech tokens to achieve strong audio-visual alignment. Specifically, since lower-level tokens encode coarse speaker-aware semantics and higher-level tokens capture fine-grained prosody, HiCoDiT employs low-level and high-level blocks to generate tokens at different levels. The low-level blocks condition on lip-synchronized motion and facial identity to capture speaker-aware content, while the high-level blocks use facial expression to modulate prosodic dynamics. Finally, to enable more effective coarse-to-fine conditioning, we propose a dual-scale adaptive instance layer normalization that jointly captures global vocal style through channel-wise normalization and local prosody dynamics through temporal-wise normalization. Extensive experiments demonstrate that HiCoDiT outperforms baselines in fidelity and expressiveness, highlighting the potential of discrete modelling for VTS. The code and speech demo are both available at https://github.com/Jiaxin-Ye/HiCoDiT.

</details>

### [Audio2Tool: Speak, Call, Act -- A Dataset for Benchmarking Speech Tool Use](2604.22821.md)
**Ramit Pahwa, Apoorva Beedu, Parivesh Priye, Rutu Gandhi et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Voice assistants increasingly rely on Speech Language Models (SpeechLMs) to interpret spoken queries and execute complex tasks, yet existing benchmarks lack domain breadth, acoustic diversity, and compositional reasoning complexity to evaluate tool-calling performance. We introduce Audio2Tool, a large-scale dataset comprising approximately 30,000 queries designed to assess tool-calling capabilities of SpeechLMs across three primary domains: Smart Car, Smart Home, and Wearables. Our benchmark features a multi-tier complexity hierarchy, ranging from simple direct commands to complex multi-intent and needle-in-a-haystack extraction to isolate distinct failure modes. To ensure realism, we employ zero-shot voice cloning text-to-speech synthesis and diverse noise profiles to simulate in-the-wild conditions. Evaluations of state-of-the-art SpeechLMs and ASR-LLM pipelines show strong performance on simple commands but significant degradation under compositional and acoustic challenges. Code and dataset are publicly available on the project page: https://audio2tool.github.io/.

</details>

### [UniPASE: A Generative Model for Universal Speech Enhancement with High Fidelity and Low Hallucinations](2604.14606.md)
**Xiaobin Rong, Zheng Wang, Yushi Wang, Jun Gao et al.** · 2026-04-16

<details>
<summary>Abstract</summary>

Universal speech enhancement (USE) aims to restore speech signals from diverse distortions across multiple sampling rates. We propose UniPASE, an extension of the low-hallucination PASE framework tailored for USE. At its core is DeWavLM-Omni, a unified representation-level enhancement module fine-tuned from WavLM via knowledge distillation on a large-scale supervised multi-distortion dataset. This module directly converts degraded waveforms into clean and linguistically faithful phonetic representations, ensuring robust enhancement with minimal linguistic hallucination. Based on these enhanced phonetic representations, an Adapter generates enhanced acoustic representations containing rich acoustic details, which a neural Vocoder uses to reconstruct corresponding high-fidelity 16-kHz waveforms. A PostNet then converts the waveforms to 48~kHz before resampling them to their original rates, enabling seamless handling of inputs and outputs at multiple sampling rates. Experimental results on several evaluation datasets, covering sub-tasks and full tasks, demonstrate that UniPASE achieves superior or competitive performance compared with existing state-of-the-art models. The proposed model also serves as the backbone of our submission to the URGENT 2026 Challenge, which achieved 1st place in the objective evaluation. The source code and audio demos are available at https://github.com/xiaobin-rong/unipase/.

</details>

### [WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training](2604.14932.md)
**Yifu Chen, Shengpeng Ji, Qian Chen, Tianle Liang et al.** · 2026-04-16

<details>
<summary>Abstract</summary>

End-to-end spoken dialogue models have garnered significant attention because they offer a higher potential ceiling in expressiveness and perceptual ability than cascaded systems. However, the intelligence and expressiveness of current open-source spoken dialogue models often remain below expectations. Motivated by the success of online reinforcement learning(RL) in other domains, one might attempt to directly apply preference optimization to spoken dialogue models, yet this transfer is non-trivial. We analyze these obstacles from the perspectives of reward modeling and rollout sampling, focusing on how sparse preference supervision interacts with dense speech generation under shared-parameter updates. Based on the analysis, we propose a modality-aware adaptive post-training recipe that makes RL practical for spoken dialogue: it constrains preference updates to the semantic channel and improves acoustic behavior via explicit anchoring, while dynamically regulating their mixture from rollout statistics to avoid unreliable preference gradients. We evaluate the method across multiple spoken dialogue benchmarks and representative architectures, and observe consistent improvements in semantic quality and speech expressiveness.

</details>

### [Giving Voice to the Constitution: Low-Resource Text-to-Speech for Quechua and Spanish Using a Bilingual Legal Corpus](2604.13288.md)
**John E. Ortega, Rodolfo Zevallos, Fabricio Carraro** · 2026-04-14

<details>
<summary>Abstract</summary>

We present a unified pipeline for synthesizing high-quality Quechua and Spanish speech for the Peruvian Constitution using three state-of-the-art text-to-speech (TTS) architectures: XTTS v2, F5-TTS, and DiFlow-TTS. Our models are trained on independent Spanish and Quechua speech datasets with heterogeneous sizes and recording conditions, and leverage bilingual and multilingual TTS capabilities to improve synthesis quality in both languages. By exploiting cross-lingual transfer, our framework mitigates data scarcity in Quechua while preserving naturalness in Spanish. We release trained checkpoints, inference code, and synthesized audio for each constitutional article, providing a reusable resource for speech technologies in indigenous and multilingual contexts. This work contributes to the development of inclusive TTS systems for political and legal content in low-resource settings.

</details>

### [An Ultra-Low Latency, End-to-End Streaming Speech Synthesis Architecture via Block-Wise Generation and Depth-Wise Codec Decoding](2604.12438.md)
**Tianhui Su, Tien-Ping Tan, Salima Mdhaffar, Yannick Estève et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Real-time speech synthesis requires balancing inference latency and acoustic fidelity for interactive applications. Conventional continuous text-to-speech pipelines require computationally intensive neural vocoders to reconstruct phase information, creating a significant streaming bottleneck. Furthermore, regression-based acoustic modeling frequently induces spectral over-smoothing artifacts. To address these limitations, this paper proposes a novel end-to-end non-autoregressive architecture optimized for ultra-low latency block-wise generation, directly modeling the highly compressed discrete latent space of the Mimi neural audio codec. Integrating a modified FastSpeech 2 backbone with a progressive depth-wise sequential decoding strategy, the architecture dynamically conditions 32 layers of residual vector quantization codes. This mechanism resolves phonetic alignment degradation and manages the complexity of high-fidelity discrete representations without temporal autoregressive overhead. Experimental evaluations on English and Malay datasets validate its language-independent deployment capability. Compared to conventional continuous regression models, the proposed architecture demonstrates quantitative improvements in fundamental voicing accuracy and mitigates high-frequency spectral degradation. It achieves ultra-low latency inference, translating to a 10.6-fold absolute acceleration over conventional cascaded pipelines. Crucially, the system achieves an average time-to-first-byte latency of 48.99 milliseconds, falling significantly below the human perception threshold for real-time interactive streaming. These results firmly establish the proposed architecture as a highly optimized solution for deploying real-time streaming speech interfaces.

</details>

### [X-VC: Zero-shot Streaming Voice Conversion in Codec Space](2604.12456.md)
**Qixi Zheng, Yuxiang Zhao, Tianrui Wang, Wenxi Chen et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) aims to convert a source utterance into the voice of an unseen target speaker while preserving its linguistic content. Although recent systems have improved conversion quality, building zero-shot VC systems for interactive scenarios remains challenging because high-fidelity speaker transfer and low-latency streaming inference are difficult to achieve simultaneously. In this work, we present X-VC, a zero-shot streaming VC system that performs one-step conversion in the latent space of a pretrained neural codec. X-VC uses a dual-conditioning acoustic converter that jointly models source codec latents and frame-level acoustic conditions derived from target reference speech, while injecting utterance-level target speaker information through adaptive normalization. To reduce the mismatch between training and inference, we train the model with generated paired data and a role-assignment strategy that combines standard, reconstruction, and reversed modes. For streaming inference, we further adopt a chunkwise inference scheme with overlap smoothing that is aligned with the segment-based training paradigm of the codec. Experiments on Seed-TTS-Eval show that X-VC achieves the best streaming WER in both English and Chinese, strong speaker similarity in same-language and cross-lingual settings, and substantially lower offline real-time factor than the compared baselines. These results suggest that codec-space one-step conversion is a practical approach for building high-quality low-latency zero-shot VC systems. Audio samples are available at https://x-vc.github.io. Our code and checkpoints will also be released.

</details>

### [On the Distillation Loss Functions of Speech VAE for Unified Reconstruction, Understanding, and Generation](2604.12383.md)
**Changhao Cheng, Wei Wang, Wangyou Zhang, Dongya Jia et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Continuous speech representations based on Variational Autoencoders (VAEs) have emerged as a promising alternative to traditional spectrogram or discrete token based features for speech generation and reconstruction. Recent research has tried to enrich the structural information in VAE latent representations by aligning with self-supervised learning (SSL) features, aiming for better generation performance. However, it remains unclear whether the widely-used alignment approach based on time-axis distillation is optimal when considering more tasks. To address this problem, this paper systematically explores different alignment approaches and analyzes their impact on the performances over three axes: reconstruction, understanding, and generation. We investigate various design choices in the distillation loss. Extensive experiments show that the joint-marginal alignment approach with adaptive weighting can achieve the best overall performance while allowing for a controllable balance.

</details>

### [CoSyncDiT: Cognitive Synchronous Diffusion Transformer for Movie Dubbing](2604.12292.md)
**Gaoxiang Cong, Liang Li, Jiaxin Ye, Zhedong Zhang et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Movie dubbing aims to synthesize speech that preserves the vocal identity of a reference audio while synchronizing with the lip movements in a target video. Existing methods fail to achieve precise lip-sync and lack naturalness due to explicit alignment at the duration level. While implicit alignment solutions have emerged, they remain susceptible to interference from the reference audio, triggering timbre and pronunciation degradation in in-the-wild scenarios. In this paper, we propose a novel flow matching-based movie dubbing framework driven by the Cognitive Synchronous Diffusion Transformer (CoSync-DiT), inspired by the cognitive process of professional actors. This architecture progressively guides the noise-to-speech generative trajectory by executing acoustic style adapting, fine-grained visual calibrating, and time-aware context aligning. Furthermore, we design the Joint Semantic and Alignment Regularization (JSAR) mechanism to simultaneously constrain frame-level temporal consistency on the contextual outputs and semantic consistency on the flow hidden states, ensuring robust alignment. Extensive experiments on both standard benchmarks and challenging in-the-wild dubbing benchmarks demonstrate that our method achieves the state-of-the-art performance across multiple metrics.

</details>

### [Saar-Voice: A Multi-Speaker Saarbrücken Dialect Speech Corpus](2604.11803.md)
**Lena S. Oberkircher, Jesujoba O. Alabi, Dietrich Klakow, Jürgen Trouvain** · 2026-04-13

<details>
<summary>Abstract</summary>

Natural language processing (NLP) and speech technologies have made significant progress in recent years; however, they remain largely focused on standardized language varieties. Dialects, despite their cultural significance and widespread use, are underrepresented in linguistic resources and computational models, resulting in performance disparities. To address this gap, we introduce Saar-Voice, a six-hour speech corpus for the Saarbrücken dialect of German. The dataset was created by first collecting text through digitized books and locally sourced materials. A subset of this text was recorded by nine speakers, and we conducted analyses on both the textual and speech components to assess the dataset's characteristics and quality. We discuss methodological challenges related to orthographic and speaker variation, and explore grapheme-to-phoneme (G2P) conversion. The resulting corpus provides aligned textual and audio representations. This serves as a foundation for future research on dialect-aware text-to-speech (TTS), particularly in low-resource scenarios, including zero-shot and few-shot model adaptation.

</details>

### [StreamMark: A Deep Learning-Based Semi-Fragile Audio Watermarking for Proactive Deepfake Detection](2604.11917.md)
**Zhentao Liu, Milos Cernak** · 2026-04-13

<details>
<summary>Abstract</summary>

The rapid advancement of generative AI has made it increasingly challenging to distinguish between deepfake audio and authentic human speech. To overcome the limitations of passive detection methods, we propose StreamMark, a novel deep learning-based, semi-fragile audio watermarking system. StreamMark is designed to be robust against benign audio conversions that preserve semantic meaning (e.g., compression, noise) while remaining fragile to malicious, semantics-altering manipulations (e.g., voice conversion, speech editing). Our method introduces a complex-domain embedding technique within a unique Encoder-Distortion-Decoder architecture, trained explicitly to differentiate between these two classes of transformations. Comprehensive benchmarks demonstrate that StreamMark achieves high imperceptibility (SNR 24.16 dB, PESQ 4.20), is resilient to real-world distortions like Opus encoding, and exhibits principled fragility against a suite of deepfake attacks, with message recovery accuracy dropping to chance levels (~50%), while remaining robust to benign AI-based style transfers (ACC >98%).

</details>

### [Bridging What the Model Thinks and How It Speaks: Self-Aware Speech Language Models for Expressive Speech Generation](2604.11424.md)
**Kuang Wang, Lai Wei, Qibing Bai, Ping Lin et al.** · 2026-04-13

<details>
<summary>Abstract</summary>

Speech Language Models (SLMs) exhibit strong semantic understanding, yet their generated speech often sounds flat and fails to convey expressive intent, undermining user engagement. We term this mismatch the semantic understanding-acoustic realization gap. We attribute this gap to two key deficiencies: (1) intent transmission failure, where SLMs fail to provide the stable utterance-level intent needed for expressive delivery; and (2) realization-unaware training, where no feedback signal verifies whether acoustic outputs faithfully reflect intended expression. To address these issues, we propose SA-SLM (Self-Aware Speech Language Model), built on the principle that the model should be aware of what it thinks during generation and how it speaks during training. SA-SLM addresses this gap through two core contributions: (1) Intent-Aware Bridging, which uses a Variational Information Bottleneck (VIB) objective to translate the model's internal semantics into temporally smooth expressive intent, making speech generation aware of what the model intends to express; and (2) Realization-Aware Alignment, which repurposes the model as its own critic to verify and align acoustic realization with intended expressive intent via rubric-based feedback. Trained on only 800 hours of expressive speech data, our 3B parameter SA-SLM surpasses all open-source baselines and comes within 0.08 points of GPT-4o-Audio in overall expressiveness on the EchoMind benchmark.

</details>

### [Knowing What to Stress: A Discourse-Conditioned Text-to-Speech Benchmark](2604.10580.md)
**Arnon Turetzky, Avihu Dekel, Hagai Aronowitz, Ron Hoory et al.** · 2026-04-12

<details>
<summary>Abstract</summary>

Spoken meaning often depends not only on what is said, but also on which word is emphasized. The same sentence can convey correction, contrast, or clarification depending on where emphasis falls. Although modern text-to-speech (TTS) systems generate expressive speech, it remains unclear whether they infer contextually appropriate stress from discourse alone. To address this gap, we present Context-Aware Stress TTS (CAST), a benchmark for evaluating context-conditioned word-level stress in TTS. Items are defined as contrastive context pairs: identical sentences paired with distinct contexts requiring different stressed words. We evaluate state-of-the-art systems and find a consistent gap: text-only language models reliably recover the intended stress from context, yet TTS systems frequently fail to realize it in speech. We release the benchmark, evaluation framework, construction pipeline and a synthetic corpus to support future work on context-aware speech synthesis.

</details>

### [Sign-to-Speech Prosody Transfer via Sign Reconstruction-based GAN](2604.10413.md)
**Toranosuke Manabe, Yuto Shibata, Shinnosuke Takamichi, Yoshimitsu Aoki** · 2026-04-12

<details>
<summary>Abstract</summary>

Deep learning models have improved sign language-to-text translation and made it easier for non-signers to understand signed messages. When the goal is spoken communication, a naive approach is to convert signed messages into text and then synthesize speech via Text-to-Speech (TTS). However, this two-stage pipeline inevitably treat text as a bottleneck representation, causing the loss of rich non-verbal information originally conveyed in the signing. To address this limitation, we propose a novel task, \emph{Sign-to-Speech Prosody Transfer}, which aims to capture the global prosodic nuances expressed in sign language and directly integrate them into synthesized speech. A major challenge is that aligning sign and speech requires expert knowledge, making annotation extremely costly and preventing the construction of large parallel corpora. To overcome this, we introduce \emph{SignRecGAN}, a scalable training framework that leverages unimodal datasets without cross-modal annotations through adversarial learning and reconstruction losses. Furthermore, we propose \emph{S2PFormer}, a new model architecture that preserves the expressive power of existing TTS models while enabling the injection of sign-derived prosody into the synthesized speech. Extensive experiments demonstrate that the proposed method can synthesize speech that faithfully reflects the emotional content of sign language, thereby opening new possibilities for more natural sign language communication. Our code will be available upon acceptance.

</details>

### [PS-TTS: Phonetic Synchronization in Text-to-Speech for Achieving Natural Automated Dubbing](2604.09111.md)
**Changi Hong, Yoonah Song, Hwayoung Park, Chaewoon Bang et al.** · 2026-04-10

<details>
<summary>Abstract</summary>

Recently, artificial intelligence-based dubbing technology has advanced, enabling automated dubbing (AD) to convert the source speech of a video into target speech in different languages. However, natural AD still faces synchronization challenges such as duration and lip-synchronization (lip-sync), which are crucial for preserving the viewer experience. Therefore, this paper proposes a synchronization method for AD processes that paraphrases translated text, comprising two steps: isochrony for timing constraints and phonetic synchronization (PS) to preserve lip-sync. First, we achieve isochrony by paraphrasing the translated text with a language model, ensuring the target speech duration matches that of the source speech. Second, we introduce PS, which employs dynamic time warping (DTW) with local costs of vowel distances measured from training data so that the target text composes vowels with pronunciations similar to source vowels. Third, we extend this approach to PSComet, which jointly considers semantic and phonetic similarity to preserve meaning better. The proposed methods are incorporated into text-to-speech systems, PS-TTS and PS-Comet TTS. The performance evaluation using Korean and English lip-reading datasets and a voice-actor dubbing dataset demonstrates that both systems outperform TTS without PS on several objective metrics and outperform voice actors in Korean-to-English and English-to-Korean dubbing. We extend the experiments to French, testing all pairs among these languages to evaluate cross-linguistic applicability. Across all language pairs, PS-Comet performed best, balancing lip-sync accuracy with semantic preservation, confirming that PS-Comet achieves more accurate lip-sync with semantic preservation than PS alone.

</details>

### [DDSP-QbE++: Improving Speech Quality for Speech Anonymisation for Atypical Speech](2604.09246.md)
**Suhita Ghosh, Yamini Sinha, Sebastian Stober** · 2026-04-10

<details>
<summary>Abstract</summary>

Differentiable Digital Signal Processing (DDSP) pipelines for voice conversion rely on subtractive synthesis, where a periodic excitation signal is shaped by a learned spectral envelope to reconstruct the target voice. In DDSP-QbE, the excitation is generated via phase accumulation, producing a sawtooth-like waveform whose abrupt discontinuities introduce aliasing artefacts that manifest perceptually as buzziness and spectral distortion, particularly at higher fundamental frequencies. We propose two targeted improvements to the excitation stage of the DDSP-QbE subtractive synthesizer. First, we incorporate explicit voicing detection to gate the harmonic excitation, suppressing the periodic component in unvoiced regions and replacing it with filtered noise, thereby avoiding aliased harmonic content where it is most perceptually disruptive. Second, we apply Polynomial Band-Limited Step (PolyBLEP) correction to the phase-accumulated oscillator, substituting the hard waveform discontinuity at each phase wrap with a smooth polynomial residual that cancels alias-generating components without oversampling or spectral truncation. Together, these modifications yield a cleaner harmonic roll-off, reduced high-frequency artefacts, and improved perceptual naturalness, as measured by MOS. The proposed approach is lightweight, differentiable, and integrates seamlessly into the existing DDSP-QbE training pipeline with no additional learnable parameters.

</details>

### [Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models](2605.27383.md)
**Yizhong Geng, Yanliang Li, Jinghan Yang, Tianhan Jiang et al.** · 2026-04-10

<details>
<summary>Abstract</summary>

Spoken Language Models (SLMs) have emerged as a promising paradigm for speech synthesis by bypassing explicit grapheme-to-phoneme pipelines. However, their effectiveness in low-resource languages remains fundamentally limited by the scarcity of transcribed speech. In practice, synthetic data has become the primary strategy for scaling SLMs in such settings, providing reliable phonetic supervision when real data is insufficient. In this work, we show that this reliance introduces a fundamental trade-off, which we term the Stability-Expressivity Gap: while synthetic data improves phonetic accuracy, it progressively suppresses prosodic variability, ultimately leading to a collapse of expressivity (Synthetic Erosion). To bridge this gap, we propose two self-alignment frameworks. Disentanglement-Guided Self-Alignment (DGSA) recovers expressivity for complex languages by exploiting prosody-timbre separation. For regimes where authentic references are exceptionally limited, Temperature-Driven Self-Critique (TDSC) stabilizes generation through automated exploration and filtering. Our approach outperforms strong commercial systems, including ElevenLabs and Gemini Pro, and enables the first zero-shot voice cloning capability for Lao.

</details>

### [Enhancing Conversational TTS with Cascaded Prompting and ICL-Based Online Reinforcement Learning](2604.08709.md)
**Zhicheng Ouyang, Seong-Gyun Leem, Bach Viet Do, Haibin Wu et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Conversational AI has made significant progress, yet generating expressive and controllable text-to-speech (TTS) remains challenging. Specifically, controlling fine-grained voice styles and emotions is notoriously difficult and typically requires massive amounts of heavily annotated training data. To overcome this data bottleneck, we present a scalable, data-efficient cascaded framework that pairs textual style tokens with human-curated, high-quality audio prompts. This approach enables single-shot adaptation to fine-grained speaking styles and character voices. In the context of TTS, this audio prompting acts as In-Context Learning (ICL), guiding the model's prosody and timbre without requiring massive parameter updates or large-scale retraining. To further enhance generation quality and mitigate hallucinations, we introduce a novel ICL-based online reinforcement learning (RL) strategy. This strategy directly optimizes the autoregressive prosody model using subjective aesthetic rewards while being constrained by Connectionist Temporal Classification (CTC) alignment to preserve intelligibility. Comprehensive human perception evaluations demonstrate significant improvements in both the naturalness and expressivity of the synthesized speech, establishing the efficacy of our ICL-based online RL approach.

</details>

### [CapTalk: Unified Voice Design for Single-Utterance and Dialogue Speech Generation](2604.08363.md)
**Xiaosu Su, Zihan Sun, Peilei Jia, Jun Gao** · 2026-04-09

<details>
<summary>Abstract</summary>

Voice design from natural language descriptions is emerging as a new task in text-to-speech multimodal generation, aiming to synthesize speech with target timbre and speaking style without relying on reference audio. However, existing methods mainly focus on single-utterance generation, leaving conversational voice design largely unexplored. In this work, we extend voice design to dialogue, enabling better target speaker modeling and turn-level expressive control in natural conversational settings. We propose CapTalk, a unified caption-conditioned text-audio autoregressive framework for both single-utterance and dialogue voice design. CapTalk uses utterance-level captions for single-utterance voice design and speaker-level captions for dialogue speaker modeling, and further introduces a CoT control sequence in dialogue to explicitly plan turn-level dynamic attributes. To resolve the conflict between stable timbre preservation and context-adaptive expression, we propose a hierarchical variational conditioning module with an utterance-level speaker encoder to better balance stable timbre preservation and context-adaptive expression. This enables timbre reuse while keeping expression adaptive to the current utterance and, in dialogue, the surrounding context. We also build a comprehensive evaluation protocol for both single-utterance and dialogue settings. Experiments show that CapTalk achieves state-of-the-art performance on a single-utterance voice design benchmark and delivers better expression controllability and contextual appropriateness in multi-turn dialogue. Audio samples are available at: https://anonymous.4open.science/api/repo/Captalk-D601/file/index.html.

</details>

### [Cross-Modal Emotion Transfer for Emotion Editing in Talking Face Video](2604.07786.md)
**Chanhyuk Choi, Taesoo Kim, Donggyu Lee, Siyeol Jung et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Talking face generation has gained significant attention as a core application of generative models. To enhance the expressiveness and realism of synthesized videos, emotion editing in talking face video plays a crucial role. However, existing approaches often limit expressive flexibility and struggle to generate extended emotions. Label-based methods represent emotions with discrete categories, which fail to capture a wide range of emotions. Audio-based methods can leverage emotionally rich speech signals - and even benefit from expressive text-to-speech (TTS) synthesis - but they fail to express the target emotions because emotions and linguistic contents are entangled in emotional speeches. Images-based methods, on the other hand, rely on target reference images to guide emotion transfer, yet they require high-quality frontal views and face challenges in acquiring reference data for extended emotions (e.g., sarcasm). To address these limitations, we propose Cross-Modal Emotion Transfer (C-MET), a novel approach that generates facial expressions based on speeches by modeling emotion semantic vectors between speech and visual feature spaces. C-MET leverages a large-scale pretrained audio encoder and a disentangled facial expression encoder to learn emotion semantic vectors that represent the difference between two different emotional embeddings across modalities. Extensive experiments on the MEAD and CREMA-D datasets demonstrate that our method improves emotion accuracy by 14% over state-of-the-art methods, while generating expressive talking face videos - even for unseen extended emotions. Code, checkpoint, and demo are available at https://chanhyeok-choi.github.io/C-MET/

</details>

### [AT-ADD: All-Type Audio Deepfake Detection Challenge Evaluation Plan](2604.08184.md)
**Yuankun Xie, Haonan Cheng, Jiayi Zhou, Xiaoxuan Guo et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

The rapid advancement of Audio Large Language Models (ALLMs) has enabled cost-effective, high-fidelity generation and manipulation of both speech and non-speech audio, including sound effects, singing voices, and music. While these capabilities foster creativity and content production, they also introduce significant security and trust challenges, as realistic audio deepfakes can now be generated and disseminated at scale. Existing audio deepfake detection (ADD) countermeasures (CMs) and benchmarks, however, remain largely speech-centric, often relying on speech-specific artifacts and exhibiting limited robustness to real-world distortions, as well as restricted generalization to heterogeneous audio types and emerging spoofing techniques. To address these gaps, we propose the All-Type Audio Deepfake Detection (AT-ADD) Grand Challenge for ACM Multimedia 2026, designed to bridge controlled academic evaluation with practical multimedia forensics. AT-ADD comprises two tracks: (1) Robust Speech Deepfake Detection, which evaluates detectors under real-world scenarios and against unseen, state-of-the-art speech generation methods; and (2) All-Type Audio Deepfake Detection, which extends detection beyond speech to diverse, unknown audio types and promotes type-agnostic generalization across speech, sound, singing, and music. By providing standardized datasets, rigorous evaluation protocols, and reproducible baselines, AT-ADD aims to accelerate the development of robust and generalizable audio forensic technologies, supporting secure communication, reliable media verification, and responsible governance in an era of pervasive synthetic audio.

</details>

### [Unlocking Fine-Grained and Within-Utterance Speaking Style Control in Prompt-Based Text-to-Speech Models](2605.27376.md)
**Jaehoon Kang, Yejin Lee, Yoonji Park, Kyuhong Shim** · 2026-04-09

<details>
<summary>Abstract</summary>

While prompt-based text-to-speech (TTS) models enable natural language-driven speaking style control, they often provide limited fine-grained control and apply a single global style across an utterance. This restricts practical use cases that require continuous style attribute interpolation across utterances and time-varying style transitions within a single utterance. In this paper, we propose novel techniques to achieve both capabilities in existing prompt-based TTS models. For inter-utterance style interpolation, we compute direction vectors between contrastive style prompts in the embedding space and perform simple interpolation, enabling smooth transitions between style characteristics. For intra-utterance style transition, we first identify a strong attention bias toward early tokens in autoregressive TTS decoders, causing the initial audio realization to dominate subsequent generation. To mitigate this effect, we introduce KV-cache swapping and sliding-window attention masking. Experiments demonstrate that our proposed inter-utterance interpolation achieves a 99-100% success rate in gender conversion, up to 36 Hz pitch variation, and up to 1.6 syllables-per-second speed change. Our intra-utterance transition maintains a speaker similarity of 0.81-0.91 and achieves perceptual smoothness scores of 3.48-4.48.

</details>

### [Lexical Tone is Hard to Quantize: Probing Discrete Speech Units in Mandarin and Yorùbá](2604.07467.md)
**Opeyemi Osakuade, Simon King** · 2026-04-08

<details>
<summary>Abstract</summary>

Discrete speech units (DSUs) are derived by quantising representations from models trained using self-supervised learning (SSL). They are a popular representation for a wide variety of spoken language tasks, including those where prosody matters. DSUs are especially convenient for tasks where text and speech are jointly modelled, such as text-to-speech and multimodal dialogue systems. But we have found that DSUs encode suprasegmental information less reliably than segmental structure, which we demonstrate in this work using lexical tone, though this limitation likely extends to other suprasegmental features such as prosody. Our investigations using the tone languages Mandarin and Yorùbá show that the SSL latent representations themselves do encode tone, yet DSUs obtained using quantisation tend to prioritise phonetic structure, which makes lexical tone less reliably encoded. This remains true for a variety of quantisation methods, not only the most common, K-means. We conclude that current DSU quantisation strategies have limitations for suprasegmental features, which suggests a need for new, tone-aware (or prosody-aware) techniques in speech representation learning. We point towards a potential form of the solution by performing K-means clustering once to encode phonetic information, then again on the residual representation, which better encodes lexical tone.

</details>

### [In-Context Learning in Speech Language Models: Analyzing the Role of Acoustic Features, Linguistic Structure, and Induction Heads](2604.06356.md)
**Charlotte Pouw, Hosein Mohebbi, Afra Alishahi, Willem Zuidema** · 2026-04-07

<details>
<summary>Abstract</summary>

In-Context Learning (ICL) has been extensively studied in text-only Language Models, but remains largely unexplored in the speech domain. Here, we investigate how linguistic and acoustic features affect ICL in Speech Language Models. We focus on the Text-to-Speech (TTS) task, which allows us to analyze ICL from two angles: (1) how accurately the model infers the task from the demonstrations (i.e., generating the correct spoken content), and (2) to what extent the model mimics the acoustic characteristics of the demonstration speech in its output. We find that speaking rate strongly affects ICL performance and is also mimicked in the output, whereas pitch range and intensity have little impact on performance and are not consistently reproduced. Finally, we investigate the role of induction heads in speech-based ICL and show that these heads play a causal role: ablating the top-k induction heads completely removes the model's ICL ability, mirroring findings from text-based ICL.

</details>

### [A Novel Automatic Framework for Speaker Drift Detection in Synthesized Speech](2604.06327.md)
**Jia-Hong Huang, Seulgi Kim, Yi Chieh Liu, Yixian Shen et al.** · 2026-04-07

<details>
<summary>Abstract</summary>

Recent diffusion-based text-to-speech (TTS) models achieve high naturalness and expressiveness, yet often suffer from speaker drift, a subtle, gradual shift in perceived speaker identity within a single utterance. This underexplored phenomenon undermines the coherence of synthetic speech, especially in long-form or interactive settings. We introduce the first automatic framework for detecting speaker drift by formulating it as a binary classification task over utterance-level speaker consistency. Our method computes cosine similarity across overlapping segments of synthesized speech and prompts large language models (LLMs) with structured representations to assess drift. We provide theoretical guarantees for cosine-based drift detection and demonstrate that speaker embeddings exhibit meaningful geometric clustering on the unit sphere. To support evaluation, we construct a high-quality synthetic benchmark with human-validated speaker drift annotations. Experiments with multiple state-of-the-art LLMs confirm the viability of this embedding-to-reasoning pipeline. Our work establishes speaker drift as a standalone research problem and bridges geometric signal analysis with LLM-based perceptual reasoning in modern TTS.

</details>

### [Controllable Singing Style Conversion with Boundary-Aware Information Bottleneck](2604.05526.md)
**Zhetao Hu, Yiquan Zhou, Wenyu Wang, Zhiyu Wu et al.** · 2026-04-07

<details>
<summary>Abstract</summary>

This paper presents the submission of the S4 team to the Singing Voice Conversion Challenge 2025 (SVCC2025)-a novel singing style conversion system that advances fine-grained style conversion and control within in-domain settings. To address the critical challenges of style leakage, dynamic rendering, and high-fidelity generation with limited data, we introduce three key innovations: a boundary-aware Whisper bottleneck that pools phoneme-span representations to suppress residual source style while preserving linguistic content; an explicit frame-level technique matrix, enhanced by targeted F0 processing during inference, for stable and distinct dynamic style rendering; and a perceptually motivated high-frequency band completion strategy that leverages an auxiliary standard 48kHz SVC model to augment the high-frequency spectrum, thereby overcoming data scarcity without overfitting. In the official SVCC2025 subjective evaluation, our system achieves the best naturalness performance among all submissions while maintaining competitive results in speaker similarity and technique control, despite using significantly less extra singing data than other top-performing systems. Audio samples are available online.

</details>

### [Subspace Control: Turning Constrained Model Steering into Controllable Spectral Optimization](2604.04231.md)
**Yancheng Huang, Changsheng Wang, Chongyu Fan, Yicheng Lang et al.** · 2026-04-05

<details>
<summary>Abstract</summary>

Foundation models, such as large language models (LLMs), are powerful but often require customization before deployment to satisfy practical constraints such as safety, privacy, and task-specific requirements, leading to "constrained" optimization problems for model steering and adaptation. However, solving such problems remains largely underexplored and is particularly challenging due to interference between the primary objective and constraint objectives during optimization. In this paper, we propose a subspace control framework for constrained model training. Specifically, (i) we first analyze, from a model merging perspective, how spectral cross-task interference arises and show that it can be resolved via a one-shot solution that orthogonalizes the merged subspace; (ii) we establish a connection between this solution and gradient orthogonalization in the spectral optimizer Muon; and (iii) building on these insights, we introduce SIFT (spectral interference-free training), which leverages a localization scheme to selectively intervene during optimization, enabling controllable updates that mitigate objective-constraint conflicts. We evaluate SIFT across four representative applications: (a) machine unlearning, (b) safety alignment, (c) text-to-speech adaptation, and (d) hallucination mitigation. Compared to both control-based and control-free baselines, SIFT consistently achieves substantial and robust performance improvements across all tasks. Code is available at https://github.com/OPTML-Group/SIFT.

</details>

### [GAP-URGENet: A Generative-Predictive Fusion Framework for Universal Speech Enhancement](2604.01832.md)
**Xiaobin Rong, Yushi Wang, Zheng Wang, Jing Lu** · 2026-04-02

<details>
<summary>Abstract</summary>

We introduce GAP-URGENet, a generative-predictive fusion framework developed for Track 1 of the ICASSP 2026 URGENT Challenge. The system integrates a generative branch, which performs full-stack speech restoration in a self-supervised representation domain and reconstructs the waveform via a neural vocoder, along with a predictive branch that performs spectrogram-domain enhancement, providing complementary cues. Outputs from both branches are fused by a post-processing module, which also performs bandwidth extension to generate the enhanced waveform at 48 kHz, later downsampled to the original sampling rate. This generative-predictive fusion improves robustness and perceptual quality, achieving top performance in the blind-test phase and ranking 1st in the objective evaluation. Audio examples are available at https://xiaobin-rong.github.io/gap-urgenet_demo.

</details>

### [T5Gemma-TTS Technical Report](2604.01760.md)
**Chihiro Arata, Kiyoshi Kurihara** · 2026-04-02

<details>
<summary>Abstract</summary>

Autoregressive neural codec language models have shown strong zero-shot voice cloning ability, but decoder-only architectures treat input text as a prefix that competes with the growing audio sequence for positional capacity, weakening text conditioning over long utterances. We present T5Gemma-TTS, an encoder-decoder codec language model that maintains persistent text conditioning by routing bidirectional text representations through cross-attention at every decoder layer. Built on the T5Gemma pretrained encoder-decoder backbone (2B encoder + 2B decoder; 4B parameters), it inherits rich linguistic knowledge without phoneme conversion and processes text directly at the subword level. To improve duration control, we introduce Progress-Monitoring Rotary Position Embedding (PM-RoPE) in all 26 cross-attention layers, injecting normalized progress signals that help the decoder track target speech length. Trained on 170,000 hours of multilingual speech in English, Chinese, and Japanese, T5Gemma-TTS achieves a statistically significant speaker-similarity gain on Japanese over XTTSv2 (0.677 vs. 0.622; non-overlapping 95% confidence intervals) and the highest numerical Korean speaker similarity (0.747) despite Korean not being included in training, although this margin over XTTSv2 (0.741) is not statistically conclusive. It also attains the lowest numerical Japanese character error rate among five baselines (0.126), though this ranking should be interpreted cautiously because of partial confidence-interval overlap with Kokoro. English results on LibriSpeech should be viewed as an upper-bound estimate because LibriHeavy is a superset of LibriSpeech. Using the same checkpoint, disabling PM-RoPE at inference causes near-complete synthesis failure: CER degrades from 0.129 to 0.982 and duration accuracy drops from 79% to 46%. Code and weights are available at https://github.com/Aratako/T5Gemma-TTS.

</details>

### [Acoustic and perceptual differences between standard and accented Chinese speech and their voice clones](2604.01562.md)
**Tianle Yang, Chengzhe Sun, Phil Rose, Siwei Lyu** · 2026-04-02

<details>
<summary>Abstract</summary>

Voice cloning is often evaluated in terms of overall quality, but less is known about accent preservation and its perceptual consequences. We compare standard and heavily accented Mandarin speech and their voice clones using a combined computational and perceptual design. Embedding-based analyses show no reliable accented-standard difference in original-clone distances across systems. In the perception study, clones are rated as more similar to their originals for standard than for accented speakers, and intelligibility increases from original to clone, with a larger gain for accented speech. These results show that accent variation can shape perceived identity match and intelligibility in voice cloning even when it is not reflected in an off-the-shelf speaker-embedding distance, and they motivate evaluating speaker identity preservation and accent preservation as separable dimensions.

</details>

### [OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models](2604.00688.md)
**Han Zhu, Lingxuan Ye, Wei Kang, Zengwei Yao et al.** · 2026-04-01

<details>
<summary>Abstract</summary>

We present OmniVoice, a massive multilingual zero-shot text-to-speech (TTS) model that scales to over 600 languages. At its core is a novel diffusion language model-style discrete non-autoregressive (NAR) architecture. Unlike conventional discrete NAR models that suffer from performance bottlenecks in complex two-stage (text-to-semantic-to-acoustic) pipelines, OmniVoice directly maps text to multi-codebook acoustic tokens. This simplified approach is facilitated by two key technical innovations: (1) a full-codebook random masking strategy for efficient training, and (2) initialization from a pre-trained LLM to ensure superior intelligibility. By leveraging a 581k-hour multilingual dataset curated entirely from open-source data, OmniVoice achieves the broadest language coverage to date and delivers state-of-the-art performance across Chinese, English, and diverse multilingual benchmarks. Our code and pre-trained models are publicly available at https://github.com/k2-fsa/OmniVoice.

</details>

### [MambaVoiceCloning: Efficient and Expressive Text-to-Speech via State-Space Modeling and Diffusion Control](2604.00292.md)
**Sahil Kumar, Namrataben Patel, Honggang Wang, Youshan Zhang** · 2026-03-31

<details>
<summary>Abstract</summary>

MambaVoiceCloning (MVC) asks whether the conditioning path of diffusion-based TTS can be made fully SSM-only at inference, removing all attention and explicit RNN-style recurrence layers across text, rhythm, and prosody, while preserving or improving quality under controlled conditions. MVC combines a gated bidirectional Mamba text encoder, a Temporal Bi-Mamba supervised by a lightweight alignment teacher discarded after training, and an Expressive Mamba with AdaLN modulation, yielding linear-time O(T) conditioning with bounded activation memory and practical finite look-ahead streaming. Unlike prior Mamba-TTS systems that remain hybrid at inference, MVC removes attention-based duration and style modules under a fixed StyleTTS2 mel-diffusion-vocoder backbone. Trained on LJSpeech/LibriTTS and evaluated on VCTK, CSS10 (ES/DE/FR), and long-form Gutenberg passages, MVC achieves modest but statistically reliable gains over StyleTTS2, VITS, and Mamba-attention hybrids in MOS/CMOS, F0 RMSE, MCD, and WER, while reducing encoder parameters to 21M and improving throughput by 1.6x. Diffusion remains the dominant latency source, but SSM-only conditioning improves memory footprint, stability, and deployability.

</details>

### [Covertly improving intelligibility with data-driven adaptations of speech timing](2603.30032.md)
**Paige Tuttösí, Angelica Lim, H. Henny Yeung, Yue Wang et al.** · 2026-03-31

<details>
<summary>Abstract</summary>

Human talkers often address listeners with language-comprehension challenges, such as hard-of-hearing or non-native adults, by globally slowing down their speech. However, it remains unclear whether this strategy actually makes speech more intelligible. Here, we take advantage of recent advancements in machine-generated speech allowing more precise control of speech rate in order to systematically examine how targeted speech-rate adjustments may improve comprehension. We first use reverse-correlation experiments to show that the temporal influence of speech rate prior to a target vowel contrast (ex. the tense-lax distinction) in fact manifests in a scissor-like pattern, with opposite effects in early versus late context windows; this pattern is remarkably stable both within individuals and across native L1-English listeners and L2-English listeners with French, Mandarin, and Japanese L1s. Second, we show that this speech rate structure not only facilitates L2 listeners' comprehension of the target vowel contrast, but that native listeners also rely on this pattern in challenging acoustic conditions. Finally, we build a data-driven text-to-speech algorithm that replicates this temporal structure on novel speech sequences. Across a variety of sentences and vowel contrasts, listeners remained unaware that such targeted slowing improved word comprehension. Strikingly, participants instead judged the common strategy of global slowing as clearer, even though it actually increased comprehension errors. Together, these results show that targeted adjustments to speech rate significantly aid intelligibility under challenging conditions, while often going unnoticed. More generally, this paper provides a data-driven methodology to improve the accessibility of machine-generated speech which can be extended to other aspects of speech comprehension and a wide variety of listeners and environments.

</details>

### [LongCat-AudioDiT: High-Fidelity Diffusion Text-to-Speech in the Waveform Latent Space](2603.29339.md)
**Detai Xin, Shujie Hu, Chengzuo Yang, Chen Huang et al.** · 2026-03-31

<details>
<summary>Abstract</summary>

We present LongCat-AudioDiT, a novel, non-autoregressive diffusion-based text-to-speech (TTS) model that achieves state-of-the-art (SOTA) performance. Unlike previous methods that rely on intermediate acoustic representations such as mel-spectrograms, the core innovation of LongCat-AudioDiT lies in operating directly within the waveform latent space. This approach effectively mitigates compounding errors and drastically simplifies the TTS pipeline, requiring only a waveform variational autoencoder (Wav-VAE) and a diffusion backbone. Furthermore, we introduce two critical improvements to the inference process: first, we identify and rectify a long-standing training-inference mismatch; second, we replace traditional classifier-free guidance with adaptive projection guidance to elevate generation quality. Experimental results demonstrate that, despite the absence of complex multi-stage training pipelines or high-quality human-annotated datasets, LongCat-AudioDiT achieves SOTA zero-shot voice cloning performance on the Seed benchmark while maintaining competitive intelligibility. Specifically, our largest variant, LongCat-AudioDiT-3.5B, outperforms the previous SOTA model (Seed-TTS), improving the speaker similarity (SIM) scores from 0.809 to 0.818 on Seed-ZH, and from 0.776 to 0.797 on Seed-Hard. Finally, through comprehensive ablation studies and systematic analysis, we validate the effectiveness of our proposed modules. Notably, we investigate the interplay between the Wav-VAE and the TTS backbone, revealing the counterintuitive finding that superior reconstruction fidelity in the Wav-VAE does not necessarily lead to better overall TTS performance. Code and model weights are released to foster further research within the speech community.

</details>

### [From Natural Alignment to Conditional Controllability in Multimodal Dialogue](2603.29162.md)
**Zeyu Jin, Songtao Zhou, Haoyu Wang, Minghao Tian et al.** · 2026-03-31

<details>
<summary>Abstract</summary>

The recent advancement of Artificial Intelligence Generated Content (AIGC) has led to significant strides in modeling human interaction, particularly in the context of multimodal dialogue. While current methods impressively generate realistic dialogue in isolated modalities like speech or vision, challenges remain in controllable Multimodal Dialogue Generation (MDG). This paper focuses on the natural alignment between speech, vision, and text in human interaction, aiming for expressive dialogue generation through multimodal conditional control. To address the insufficient richness and diversity of dialogue expressiveness in existing datasets, we introduce a novel multimodal dialogue annotation pipeline to curate dialogues from movies and TV series with fine-grained annotations in interactional characteristics. The resulting MM-Dia dataset (360+ hours, 54,700 dialogues) facilitates explicitly controlled MDG, specifically through style-controllable dialogue speech synthesis. In parallel, MM-Dia-Bench (309 highly expressive dialogues with visible single-/dual-speaker scenes) serves as a rigorous testbed for implicit cross-modal MDG control, evaluating audio-visual style consistency across modalities. Extensive experiments demonstrate that training on MM-Dia significantly enhances fine-grained controllability, while evaluations on MM-Dia-Bench reveal limitations in current frameworks to replicate the nuanced expressiveness of human interaction. These findings provides new insights and challenges for multimodal conditional dialogue generation.

</details>

### [Evaluating Generalization and Robustness in Russian Anti-Spoofing: The RuASD Initiative](2604.02374.md)
**Ksenia Lysikova, Kirill Borodin, Kirill Borodin** · 2026-03-31

<details>
<summary>Abstract</summary>

RuASD (Russian AntiSpoofing Dataset) is a dedicated, reproducible benchmark for Russian-language speech anti-spoofing designed to evaluate both in-domain discrimination and robustness to deployment-style distribution shifts. It combines a large spoof subset synthesized using 37 modern Russian-capable TTS and voice-cloning systems with a bona fide subset curated from multiple heterogeneous open Russian speech corpora, enabling systematic evaluation across diverse data sources. To emulate typical dissemination and channel effects in a controlled and reproducible manner, RuASD includes configurable simulations of platform and transmission distortions, including room reverberation, additive noise/music, and a range of speech-codec transcodings implemented via a unified processing chain. We benchmark a diverse set of publicly available anti-spoofing countermeasures spanning lightweight supervised architectures, graph-attention models, SSL-based detectors, and large-scale pretrained systems, and report reference results on both clean and simulated conditions to characterize robustness under realistic perturbation pipelines. The dataset is publickly available at \href{https://huggingface.co/datasets/MTUCI/RuASD}{\underline{Hugging Face}} and \href{https://modelscope.cn/datasets/lab260/RuASD}{\underline{ModelScope}}.

</details>

### [MOSS-VoiceGenerator: Create Realistic Voices with Natural Language Descriptions](2603.28086.md)
**Kexin Huang, Liwei Fan, Botian Jiang, Yaozhou Jiang et al.** · 2026-03-30

<details>
<summary>Abstract</summary>

Voice design from natural language aims to generate speaker timbres directly from free-form textual descriptions, allowing users to create voices tailored to specific roles, personalities, and emotions. Such controllable voice creation benefits a wide range of downstream applications-including storytelling, game dubbing, role-play agents, and conversational assistants, making it a significant task for modern Text-to-Speech models. However, existing models are largely trained on carefully recorded studio data, which produces speech that is clean and well-articulated, yet lacks the lived-in qualities of real human voices. To address these limitations, we present MOSS-VoiceGenerator, an open-source instruction-driven voice generation model that creates new timbres directly from natural language prompts. Motivated by the hypothesis that exposure to real-world acoustic variation produces more perceptually natural voices, we train on large-scale expressive speech data sourced from cinematic content. Subjective preference studies demonstrate its superiority in overall performance, instruction-following, and naturalness compared to other voice design models.

</details>

### [Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](2603.28554.md)
**Athos Georgiou** · 2026-03-30

<details>
<summary>Abstract</summary>

Visual document understanding typically requires separate retrieval and generation models, doubling memory and system complexity. We present Hydra, a dual-head approach that provides both ColBERT-style late-interaction retrieval and autoregressive generation from a single vision-language model (VLM). A single LoRA adapter, trained only for retrieval, is toggled at inference: enabling it produces multi-vector embeddings; disabling it recovers the base model's generation quality -- byte-identical outputs in 100% of 10,500 greedy and stochastic samples, with max delta-ANLS = 0.0044 across 15,301 samples on four VQA benchmarks (three informative; ChartQA is near-zero for both models under greedy decoding) when compared against an independent base-model pipeline. We identify three engineering requirements (attention-mode restoration, lm_head preservation, KV-cache-aware decoding) whose omission silently breaks generation despite correct weight recovery. On ViDoRe V1, Hydra (4B) is within 1 percentage point of a controlled single-head baseline in a single training run, with higher aggregate scores on V2 and V3 that are concentrated on a subset of tasks; multi-seed experiments are needed to confirm these trends. The single-model design reduces peak GPU memory by 41%, though adapter switching introduces throughput overhead under concurrent serving loads. An ablation shows that GritLM-style joint training provides no benefit within the LoRA-based (r=16) training regime. A proof-of-concept extension to Qwen2.5-Omni-3B demonstrates that the mechanism generalizes to audio retrieval and video embedding, with speech generation.

</details>

### [VoxAnchor: Grounding Speech Authenticity in Throat Vibration via mmWave Radar](2603.27562.md)
**Mingda Han, Huanqi Yang, Chaoqun Li, Wenhao Li et al.** · 2026-03-29

<details>
<summary>Abstract</summary>

Rapid advances in speech synthesis and audio editing have made realistic forgeries increasingly accessible, yet existing detection methods remain vulnerable to tampering or depend on visual/wearable sensors. In this paper, we present VoxAnchor, a system that physically grounds audio authentication in vocal dynamics by leveraging the inherent coherence between speech acoustics and radar-sensed throat vibrations. VoxAnchor uses contactless millimeter-wave radar to capture fine-grained throat vibrations that are tightly coupled with human speech production, establishing a hard-to-forge anchor rooted in human physiology. The design comprises three main components: (1) a cross-modal frame-work that uses modality-specific encoders and contrastive learning to detect subtle mismatches at word granularity; (2) a phase-aware pipeline that extracts physically consistent, temporally faithful throat vibrations; and (3) a dual-stage strategy that combines signal-level onset detection and semantic-level coherence to align asynchronous radar and audio streams. Unlike liveness detection, which only confirms whether speech occurred, VoxAnchor verifies what was spoken through word-level content consistency, exposing localized edits that preserve identity and global authenticity cues. Extensive evaluations show that VoxAnchor achieves robust, fine-grained detection across diverse forgeries (editing, splicing, replay, deepfake) and conditions, with an overall EER of 0.017, low latency, and modest computational cost.

</details>

### [LLaDA-TTS: Unifying Speech Synthesis and Zero-Shot Editing via Masked Diffusion Modeling](2603.26364.md)
**Xiaoyu Fan, Huizhi Xie, Wei Zou, Yunzhang Chen** · 2026-03-27

<details>
<summary>Abstract</summary>

Large language model (LLM)-based text-to-speech (TTS) systems achieve remarkable naturalness via autoregressive (AR) decoding, but require N sequential steps to generate N speech tokens. We present LLaDA-TTS, which replaces the AR LLM with a masked diffusion model that completes generation in a fixed number of parallel steps, decoupling inference latency from sequence length. Remarkably, using only 50 hours of fine-tuning data, we successfully transfer a pretrained AR checkpoint to the masked diffusion paradigm via bidirectional attention. At 64 steps, LLaDA-TTS achieves 0.98% CER (zh) and 1.96% WER (en) on Seed-TTS-Eval, matching the original CosyVoice 3 baseline performance while delivering a 2x LLM-stage speedup--a notable acceleration achieved despite the absence of KV cache, an optimization the AR baseline heavily relies on. Beyond acceleration, the bidirectional architecture naturally enables zero-shot speech editing--including word-level insertion, deletion, and substitution--without any additional training. Theoretically, we prove that AR-pretrained weights are near-optimal for bidirectional masked prediction under the locality property of acoustic tokens, explaining this rapid convergence. This general method modifies only the attention mask and objective, applying seamlessly to any LLM-based AR TTS system. Code and audio samples will be available at https://deft-piroshki-b652b5.netlify.app/.

</details>

### [PHONOS: PHOnetic Neutralization for Online Streaming Applications](2603.27001.md)
**Waris Quamer, Mu-Ruei Tseng, Ghady Nasrallah, Ricardo Gutierrez-Osuna** · 2026-03-27

<details>
<summary>Abstract</summary>

Speaker anonymization (SA) systems modify timbre while leaving regional or non-native accents intact, which is problematic because accents can narrow the anonymity set. To address this issue, we present PHONOS, a streaming module for real-time SA that neutralizes non-native accent to sound native-like. Our approach pre-generates golden speaker utterances that preserve source timbre and rhythm but replace foreign segmentals with native ones using silence-aware DTW alignment and zero-shot voice conversion. These utterances supervise a causal accent translator that maps non-native content tokens to native equivalents with at most 40ms look-ahead, trained using joint cross-entropy and CTC losses. Our evaluations show an 81% reduction in non-native accent confidence, with listening-test ratings consistent with this shift, and reduced speaker linkability as accent-neutralized utterances move away from the original speaker in embedding space while having latency under 241 ms on single GPU.

</details>

### [Voxtral TTS](2603.25551.md)
**Alexander H. Liu, Alexis Tacnet, Andy Ehrenberg, Andy Lo et al.** · 2026-03-26

<details>
<summary>Abstract</summary>

We introduce Voxtral TTS, an expressive multilingual text-to-speech model that generates natural speech from as little as 3 seconds of reference audio. Voxtral TTS adopts a hybrid architecture that combines auto-regressive generation of semantic speech tokens with flow-matching for acoustic tokens. These tokens are encoded and decoded with Voxtral Codec, a speech tokenizer trained from scratch with a hybrid VQ-FSQ quantization scheme. In human evaluations conducted by native speakers, Voxtral TTS is preferred for multilingual voice cloning due to its naturalness and expressivity, achieving a 68.4\% win rate over ElevenLabs Flash v2.5. We release the model weights under a CC BY-NC license.

</details>

### [OmniACBench: A Benchmark for Evaluating Context-Grounded Acoustic Control in Omni-Modal Models](2603.23938.md)
**Seunghee Kim, Bumkyu Park, Kyudan Jung, Joosung Lee et al.** · 2026-03-25

<details>
<summary>Abstract</summary>

Most testbeds for omni-modal models assess multimodal understanding via textual outputs, leaving it unclear whether these models can properly speak their answers. To study this, we introduce OmniACBench, a benchmark for evaluating context-grounded acoustic control in omni-modal models. Given a spoken instruction, a text script, and an image, a model must read the script aloud with an appropriate tone and manner. OmniACBench comprises 3,559 verified instances covering six acoustic features: speech rate, phonation, pronunciation, emotion, global accent, and timbre. Extensive experiments on eight models reveal their limitations in the proposed setting, despite their strong performance on prior textual-output evaluations. Our analyses show that the main bottleneck lies not in processing individual modalities, but in integrating multimodal context for faithful speech generation. Moreover, we identify three common failure modes-weak direct control, failed implicit inference, and failed multimodal grounding-providing insights for developing models that can verbalize responses effectively.

</details>

### [Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation](2603.24430.md)
**Shengfan Shen, Di Wu, Xingchen Song, Dinghao Zhou et al.** · 2026-03-25

<details>
<summary>Abstract</summary>

Reliable evaluation of modern zero-shot text-to-speech (TTS) models remains challenging. Subjective tests are costly and hard to reproduce, while objective metrics often saturate, failing to distinguish SOTA systems. To address this, we propose Iterate to Differentiate (I2D), an evaluation framework that recursively synthesizes speech using the model's own outputs as references. Higher-quality models exhibit greater resilience to the distributional shift induced by iterative synthesis, resulting in slower performance degradation. I2D exploits this differential degradation to amplify performance gaps and reveal robustness. By aggregating objective metrics across iterations, I2D improves discriminability and alignment with human judgments, increasing system-level SRCC from 0.118 to 0.464 for UTMOSv2. Experiments on 11 models across Chinese, English, and emotion datasets demonstrate that I2D enables more reliable automated evaluation for zero-shot TTS.

</details>

### [How Open is Open TTS? A Practical Evaluation of Open Source TTS Tools](2603.24116.md)
**Teodora Răgman, Adrian Bogdan Stânea, Horia Cucu, Adriana Stan** · 2026-03-25

<details>
<summary>Abstract</summary>

Open-source text-to-speech (TTS) frameworks have emerged as highly adaptable platforms for developing speech synthesis systems across a wide range of languages. However, their applicability is not uniform -- particularly when the target language is under-resourced or when computational resources are constrained. In this study, we systematically assess the feasibility of building novel TTS models using four widely adopted open-source architectures: FastPitch, VITS, Grad-TTS, and Matcha-TTS. Our evaluation spans multiple dimensions, including qualitative aspects such as ease of installation, dataset preparation, and hardware requirements, as well as quantitative assessments of synthesis quality for Romanian. We employ both objective metrics and subjective listening tests to evaluate intelligibility, speaker similarity, and naturalness of the generated speech. The results reveal significant challenges in tool chain setup, data preprocessing, and computational efficiency, which can hinder adoption in low-resource contexts. By grounding the analysis in reproducible protocols and accessible evaluation criteria, this work aims to inform best practices and promote more inclusive, language-diverse TTS development. All information needed to reproduce this study (i.e. code and data) are available in our git repository: https://gitlab.com/opentts_ragman/OpenTTS

</details>

### [Joint Modeling and KAFusion Feature Fusion for Prosody-Controllable Speech Synthesis](s2:26916f3a9c4b5470adbacacbbe23ea1b69234e52.md)
**Dongfeng Ye, Lin Jiang, Nianxin Ni, Wei Wan** · 2026-03-25

<details>
<summary>Abstract</summary>

To address the limited expressiveness in current speech synthesis caused by coarse-grained prosody modeling and simplistic feature fusion strategies, a joint prosody modeling framework and a nonlinear fusion method named KAFusion are proposed, based on the Kolmogorov–Arnold (KA) representation theorem. The joint modeling integrates pitch and energy as prosodic priors with text encodings to jointly guide duration prediction, enabling explicit control over speech rate and tone. During feature fusion, KAFusion facilitates nonlinear interactions among features through its nested inner and outer functions. Information entropy serves as the quantitative metric, and both theoretical and experimental results demonstrate the fusion module’s efficacy in suppressing redundancy while preserving task-critical content. Evaluations on the AISHELL3 dataset show a 5.8% improvement in MOS over the baseline. Ablation studies further validate the effectiveness of the proposed components, where KAFusion achieves an output entropy of 3.47, which is 18.4% higher than that of linear fusion (2.93) and indicates richer information content.

</details>

### [Rewriting TTS Inference Economics: Lightning V2 on Tenstorrent Achieves 4x Lower Cost Than NVIDIA L40S](2604.03279.md)
**Ranjith M. S., Akshat Mandloi, Sudarshan Kamath** · 2026-03-24

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) models are significantly more numerically fragile than Large Language Models (LLMs) due to their continuous waveform generation and perceptual sensitivity to small numerical perturbations. While aggressive precision reduction techniques such as BlockFloat8 (BFP8) and low-fidelity (LoFi) compute have been widely adopted in language models, applying similar strategies to TTS systems often results in audible artifacts, phase instability, and spectral distortion. In this work, we present Lightning V2, a production-grade TTS model co-optimized for Tenstorrent hardware. Through precision-aware architectural design and hardware-software co-optimization, we achieve over 95% LoFi computational fidelity and more than 80% BlockFloat8 deployment without measurable degradation in audio quality. Leveraging Tenstorrent's Network-on-Chip (NoC), distributed SRAM, and deterministic execution model, we reduce memory movement and redundant weight fetches, enabling efficient low-precision inference. Compared to an NVIDIA L40S baseline, Lightning V2 achieves approximately 4x lower on-prem accelerator cost at equivalent throughput, while maintaining production audio fidelity. Our results demonstrate that precision co-design, combined with hardware-aware optimization, can fundamentally reshape the economics of real-time speech inference.

</details>

### [SelfTTS: cross-speaker style transfer through explicit embedding disentanglement and self-refinement using self-augmentation](2603.22252.md)
**Lucas H. Ueda, João G. T. Lima, Pedro R. Corrêa, Flávio O. Simões et al.** · 2026-03-23

<details>
<summary>Abstract</summary>

This paper presents SelfTTS, a text-to-speech (TTS) model designed for cross-speaker style transfer that eliminates the need for external pre-trained speaker or emotion encoders. The architecture achieves emotional expressivity in neutral speakers through an explicit disentanglement strategy utilizing Gradient Reversal Layers (GRL) combined with cosine similarity loss to decouple speaker and emotion information. We introduce Multi Positive Contrastive Learning (MPCL) to induce clustered representations of speaker and emotion embeddings based on their respective labels. Furthermore, SelfTTS employs a self-refinement strategy via Self-Augmentation, exploiting the model's voice conversion capabilities to enhance the naturalness of synthesized speech. Experimental results demonstrate that SelfTTS achieves superior emotional naturalness (eMOS) and robust stability in target timbre and emotion compared to state-of-the-art baselines.

</details>

### [The Binding Effect: Analyzing How Multi-Dimensional Cues Form Gender Bias in Instruction TTS](2603.20743.md)
**Kuan-Yu Chen, Yi-Cheng Lin, Po-Chung Hsieh, Huang-Cheng Chou et al.** · 2026-03-21

<details>
<summary>Abstract</summary>

Current bias evaluations in Instruction Text-to-Speech (ITTS) often rely on univariate testing, overlooking the compositional structure of social cues. In this work, we investigate gender bias by modeling prompts as combinations of Social Status, Career stereotypes, and Persona descriptors. Analyzing open-source ITTS models, we uncover systematic interaction effects where social dimensions modulate one another, creating complex bias patterns missed by univariate baselines. Crucially, our findings indicate that these biases extend beyond surface-level artifacts, demonstrating strong associations with the semantic priors of pre-trained text encoders and the skewed distributions inherent in training data. We further demonstrate that generic diversity prompting is insufficient to override these entrenched patterns, underscoring the need for compositional analysis to diagnose latent risks in generative speech.

</details>

### [SNAP: Speaker Nulling for Artifact Projection in Speech Deepfake Detection](2603.20686.md)
**Kyudan Jung, Jihwan Kim, Minwoo Lee, Soyoon Kim et al.** · 2026-03-21

<details>
<summary>Abstract</summary>

Recent advancements in text-to-speech technologies enable generating high-fidelity synthetic speech nearly indistinguishable from real human voices. While recent studies show the efficacy of self-supervised learning-based speech encoders for deepfake detection, these models struggle to generalize across unseen speakers. Our quantitative analysis suggests these encoder representations are substantially influenced by speaker information, causing detectors to exploit speaker-specific correlations rather than artifact-related cues. We call this phenomenon speaker entanglement. To mitigate this reliance, we introduce SNAP, a speaker-nulling framework. We estimate a speaker subspace and apply orthogonal projection to suppress speaker-dependent components, isolating synthesis artifacts within the residual features. By reducing speaker entanglement, SNAP encourages detectors to focus on artifact-related patterns, leading to state-of-the-art performance.

</details>

### [Gesture2Speech: How Far Can Hand Movements Shape Expressive Speech?](2603.19831.md)
**Lokesh Kumar, Nirmesh Shah, Ashishkumar P. Gudmalwar, Pankaj Wasnik** · 2026-03-20

<details>
<summary>Abstract</summary>

Human communication seamlessly integrates speech and bodily motion, where hand gestures naturally complement vocal prosody to express intent, emotion, and emphasis. While recent text-to-speech (TTS) systems have begun incorporating multimodal cues such as facial expressions or lip movements, the role of hand gestures in shaping prosody remains largely underexplored. We propose a novel multimodal TTS framework, Gesture2Speech, that leverages visual gesture cues to modulate prosody in synthesized speech. Motivated by the observation that confident and expressive speakers coordinate gestures with vocal prosody, we introduce a multimodal Mixture-of-Experts (MoE) architecture that dynamically fuses linguistic content and gesture features within a dedicated style extraction module. The fused representation conditions an LLM-based speech decoder, enabling prosodic modulation that is temporally aligned with hand movements. We further design a gesture-speech alignment loss that explicitly models their temporal correspondence to ensure fine-grained synchrony between gestures and prosodic contours. Evaluations on the PATS dataset show that Gesture2Speech outperforms state-of-the-art baselines in both speech naturalness and gesture-speech synchrony. To the best of our knowledge, this is the first work to utilize hand gesture cues for prosody control in neural speech synthesis. Demo samples are available at https://research.sri-media-analysis.com/aaai26-beeu-gesture2speech/

</details>

### [Borderless Long Speech Synthesis](2603.19798.md)
**Xingchen Song, Di Wu, Dinghao Zhou, Pengyu Cheng et al.** · 2026-03-20

<details>
<summary>Abstract</summary>

Most existing text-to-speech (TTS) systems either synthesize speech sentence by sentence and stitch the results together, or drive synthesis from plain-text dialogues alone. Both approaches leave models with little understanding of global context or paralinguistic cues, making it hard to capture real-world phenomena such as multi-speaker interactions (interruptions, overlapping speech), evolving emotional arcs, and varied acoustic environments. We introduce the Borderless Long Speech Synthesis framework for agent-centric, borderless long audio synthesis. Rather than targeting a single narrow task, the system is designed as a unified capability set spanning VoiceDesigner, multi-speaker synthesis, Instruct TTS, and long-form text synthesis. On the data side, we propose a "Labeling over filtering/cleaning" strategy and design a top-down, multi-level annotation schema we call Global-Sentence-Token. On the model side, we adopt a backbone with a continuous tokenizer and add Chain-of-Thought (CoT) reasoning together with Dimension Dropout, both of which markedly improve instruction following under complex conditions. We further show that the system is Native Agentic by design: the hierarchical annotation doubles as a Structured Semantic Interface between the LLM Agent and the synthesis engine, creating a layered control protocol stack that spans from scene semantics down to phonetic detail. Text thereby becomes an information-complete, wide-band control channel, enabling a front-end LLM to convert inputs of any modality into structured generation commands, extending the paradigm from Text2Speech to borderless long speech synthesis.

</details>

### [MOSS-TTSD: Text to Spoken Dialogue Generation](2603.19739.md)
**Yuqian Zhang, Donghua Yu, Zhengyuan Lin, Botian Jiang et al.** · 2026-03-20

<details>
<summary>Abstract</summary>

Spoken dialogue generation is crucial for applications like podcasts, dynamic commentary, and entertainment content, but poses significant challenges compared to single-utterance text-to-speech (TTS). Key requirements include accurate turn-taking, cross-turn acoustic consistency, and long-form stability, which current models often fail to address due to a lack of dialogue context modeling. To bridge this gap, we present MOSS-TTSD, a spoken dialogue synthesis model designed for expressive, multi-party conversational speech across multiple languages. With enhanced long-context modeling, MOSS-TTSD generates long-form spoken conversations from dialogue scripts with explicit speaker tags, supporting up to 60 minutes of single-pass synthesis, multi-party dialogue with up to 5 speakers, and zero-shot voice cloning from a short reference audio clip. The model supports various mainstream languages, including English and Chinese, and is adapted to several long-form scenarios. Additionally, to address limitations of existing evaluation methods, we propose TTSD-eval, an objective evaluation framework based on forced alignment that measures speaker attribution accuracy and speaker similarity without relying on speaker diarization tools. Both objective and subjective evaluation results show that MOSS-TTSD surpasses strong open-source and proprietary baselines in dialogue synthesis.

</details>

### [MT-BCTTS: An End-to-End Mandarin-Tibetan Bilingual and Code-switching Speech Synthesis Method](s2:4e32d2681bacb4e04c00efb4600f23ddef1816d9.md)
**Fei Chen, Weizhao Zhang** · 2026-03-20

<details>
<summary>Abstract</summary>

With the growing demand for multilingual communication, bilingual and code-switching speech synthesis has emerged as a significant research direction in natural language processing. Although previous studies have achieved considerable progress in mainstream languages, existing speech synthesis systems still face challenges in cross-lingual modeling and the coupling of speaker and language features when dealing with lowresource languages combined with mainstream languages, such as Mandarin and Tibetan. To address these challenges, this paper proposes MT-BCTTS, an end-to-end speech synthesis model designed for Mandarin-Tibetan bilingual and code-switching tasks. Based on the VITS framework, the model enhances language modeling capabilities and language feature representation by incorporating language embeddings and the CINO pre-trained model for minority languages. Additionally, an LSTM-based speaker style encoder is introduced to extract speaker characteristics from training data. Furthermore, an orthogonal loss function is introduced to constrain language and speaker features, achieving further decoupling between them. Experimental results demonstrate that the proposed model outperforms the baseline systems in both subjective and objective evaluations, generating Mandarin and Tibetan speech with relatively high naturalness while enabling code-switching.

</details>

### [From Seeing it to Experiencing it: Interactive Evaluation of Intersectional Voice Bias in Human-AI Speech Interaction](2604.13067.md)
**Shree Harsha Bokkahalli Satish, Maria Teleki, Christoph Minixhofer, Ondrej Klejch et al.** · 2026-03-19

<details>
<summary>Abstract</summary>

SpeechLLMs process spoken language directly from audio, but accent and vocal identity cues can lead to biased behaviour. Current bias evaluations often miss how such bias manifests in end-to-end speech interactions and how users experience it. We distinguish quality-of-service disparities (e.g., off-topic or low-effort responses) from content-level bias in coherent outputs, and examine intersectional effects of accent and perceived gender. In this work, we explore a two-part evaluation approach: (1) a controlled test cohort spanning six accents and two gender presentations, analysed with judge-free prompt-response metrics, and (2) an interactive study design using voice conversion to let users experience identical content through different vocal identities. Across two studies (Interactive, N=24; Observational, N=19), we find that voice conversion increases trust and acceptability for benign responses and encourages perspective-taking, while automated analysis in search of quality-of-service disparities, reveals {accent x gender} disparities in alignment and verbosity across SpeechLLMs. These results highlight voice conversion for probing and experiencing intersectional voice bias while our evaluation suite provides richer bias evaluations for spoken conversational AI.

</details>

### [MOSS-TTS Technical Report](2603.18090.md)
**Yitian Gong, Botian Jiang, Yiwei Zhao, Yucheng Yuan et al.** · 2026-03-18

<details>
<summary>Abstract</summary>

This technical report presents MOSS-TTS, a speech generation foundation model built on a scalable recipe: discrete audio tokens, autoregressive modeling, and large-scale pretraining. Built on MOSS-Audio-Tokenizer, a causal Transformer tokenizer that compresses 24 kHz audio to 12.5 fps with variable-bitrate RVQ and unified semantic-acoustic representations, we release two complementary generators: MOSS-TTS, which emphasizes structural simplicity, scalability, and long-context/control-oriented deployment, and MOSS-TTS-Local-Transformer, which introduces a frame-local autoregressive module for higher modeling efficiency, stronger speaker preservation, and a shorter time to first audio. Across multilingual and open-domain settings, MOSS-TTS supports zero-shot voice cloning, token-level duration control, phoneme-/pinyin-level pronunciation control, smooth code-switching, and stable long-form generation. This report summarizes the design, training recipe, and empirical characteristics of the released models.

</details>

### [Neuron-Level Emotion Control in Speech-Generative Large Audio-Language Models](2603.17231.md)
**Xiutian Zhao, Ismail Rasim Ulgen, Philipp Koehn, Björn Schuller et al.** · 2026-03-18

<details>
<summary>Abstract</summary>

Large audio-language models (LALMs) can produce expressive speech, yet reliable emotion control remains elusive: conversions often miss the target affect and may degrade linguistic fidelity through refusals, hallucinations, or paraphrase. We present, to our knowledge, the first neuron-level study of emotion control in speech-generative LALMs and demonstrate that compact emotion-sensitive neurons (ESNs) are causally actionable, enabling training-free emotion steering at inference time. ESNs are identified via success-filtered activation aggregation enforcing both emotion realization and content preservation. Across three LALMs (Qwen2.5-Omni-7B, MiniCPM-o 4.5, Kimi-Audio), ESN interventions yield emotion-specific gains that generalize to unseen speakers and are supported by automatic and human evaluation. Controllability depends on selector design, mask sparsity, filtering, and intervention strength. Our results establish a mechanistic framework for training-free emotion control in speech generation.

</details>

### [CAST-TTS: A Simple Cross-Attention Framework for Unified Timbre Control in TTS](2603.16280.md)
**Zihao Zheng, Wen Wu, Chao Zhang, Mengyue Wu et al.** · 2026-03-17

<details>
<summary>Abstract</summary>

Current Text-to-Speech (TTS) systems typically use separate models for speech-prompted and text-prompted timbre control. While unifying both control signals into a single model is desirable, the challenge of cross-modal alignment often results in overly complex architectures and training objective. To address this challenge, we propose CAST-TTS, a simple yet effective framework for unified timbre control. Features are extracted from speech prompts and text prompts using pre-trained encoders. The multi-stage training strategy efficiently aligns the speech and projected text representations within a shared embedding space. A single cross-attention mechanism then allows the model to use either of these representations to control the timbre. Extensive experiments validate that the unified cross-attention mechanism is critical for achieving high-quality synthesis. CAST-TTS achieves performance comparable to specialized single-input models while operating within a unified architecture. The demo page can be accessed at https://HiRookie9.github.io/CAST-TTS-Page.

</details>

### [On the Emotion Understanding of Synthesized Speech](2603.16483.md)
**Yuan Ge, Haishu Zhao, Aokai Hao, Junxiang Zhang et al.** · 2026-03-17

<details>
<summary>Abstract</summary>

Emotion is a core paralinguistic feature in voice interaction. It is widely believed that emotion understanding models learn fundamental representations that transfer to synthesized speech, making emotion understanding results a plausible reward or evaluation metric for assessing emotional expressiveness in speech synthesis. In this work, we critically examine this assumption by systematically evaluating Speech Emotion Recognition (SER) on synthesized speech across datasets, discriminative and generative SER models, and diverse synthesis models. We find that current SER models can not generalize to synthesized speech, largely because speech token prediction during synthesis induces a representation mismatch between synthesized and human speech. Moreover, generative Speech Language Models (SLMs) tend to infer emotion from textual semantics while ignoring paralinguistic cues. Overall, our findings suggest that existing SER models often exploit non-robust shortcuts rather than capturing fundamental features, and paralinguistic understanding in SLMs remains challenging.

</details>

### [Neural networks for Text-to-Speech evaluation](2604.08562.md)
**Ilya Trofimenko, David Kocharyan, Aleksandr Zaitsev, Pavel Repnikov et al.** · 2026-03-17

<details>
<summary>Abstract</summary>

Ensuring that Text-to-Speech (TTS) systems deliver human-perceived quality at scale is a central challenge for modern speech technologies. Human subjective evaluation protocols such as Mean Opinion Score (MOS) and Side-by-Side (SBS) comparisons remain the de facto gold standards, yet they are expensive, slow, and sensitive to pervasive assessor biases. This study addresses these barriers by formulating, and implementing a suite of novel neural models designed to approximate expert judgments in both relative (SBS) and absolute (MOS) settings. For relative assessment, we propose NeuralSBS, a HuBERT-backed model achieving 73.7% accuracy (on SOMOS dataset). For absolute assessment, we introduce enhancements to MOSNet using custom sequence-length batching, as well as WhisperBert, a multimodal stacking ensemble that combines Whisper audio features and BERT textual embeddings via weak learners. Our best MOS models achieve a Root Mean Square Error (RMSE) of ~0.40, significantly outperforming the human inter-rater RMSE baseline of 0.62. Furthermore, our ablation studies reveal that naively fusing text via cross-attention can degrade performance, highlighting the effectiveness of ensemble-based stacking over direct latent fusion. We additionally report negative results with SpeechLM-based architectures and zero-shot LLM evaluators (Qwen2-Audio, Gemini 2.5 flash preview), reinforcing the necessity of dedicated metric learning frameworks.

</details>

### [WAND: Windowed Attention and Knowledge Distillation for Efficient Autoregressive Text-to-Speech Models](2604.08558.md)
**Hanna Lee, Tan Dat Nguyen, Jaehoon Kang, Kyuhong Shim** · 2026-03-17

<details>
<summary>Abstract</summary>

Recent decoder-only autoregressive text-to-speech (AR-TTS) models produce high-fidelity speech, but their memory and compute costs scale quadratically with sequence length due to full self-attention. In this paper, we propose WAND, Windowed Attention and Knowledge Distillation, a framework that adapts pretrained AR-TTS models to operate with constant computational and memory complexity. WAND separates the attention mechanism into two: persistent global attention over conditioning tokens and local sliding-window attention over generated tokens. To stabilize fine-tuning, we employ a curriculum learning strategy that progressively tightens the attention window. We further utilize knowledge distillation from a full-attention teacher to recover high-fidelity synthesis quality with high data efficiency. Evaluated on three modern AR-TTS models, WAND preserves the original quality while achieving up to 66.2% KV cache memory reduction and length-invariant, near-constant per-step latency.

</details>

### [NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation](2603.15352.md)
**Qinke Ni, Huan Liao, Dekun Chen, Yuxiang Wang et al.** · 2026-03-16

<details>
<summary>Abstract</summary>

While recent text-to-speech (TTS) systems increasingly integrate nonverbal vocalizations (NVs), their evaluations lack standardized metrics and reliable ground-truth references. To bridge this gap, we propose NV-Bench, the first benchmark grounded in a functional taxonomy that treats NVs as communicative acts rather than acoustic artifacts. NV-Bench comprises 1,651 multi-lingual, in-the-wild utterances with paired human reference audio, balanced across 14 NV categories. We introduce a dual-dimensional evaluation protocol: (1) Instruction Alignment, utilizing the proposed paralinguistic character error rate (PCER) to assess controllability, (2) Acoustic Fidelity, measuring the distributional gap to real recordings to assess acoustic realism. We evaluate diverse TTS models and develop two baselines. Experimental results demonstrate a strong correlation between our objective metrics and human perception, establishing NV-Bench as a standardized evaluation framework.

</details>

### [PhonemeDF: A Synthetic Speech Dataset for Audio Deepfake Detection and Naturalness Evaluation](2603.15037.md)
**Vamshi Nallaguntla, Aishwarya Fursule, Shruti Kshirsagar, Anderson R. Avila** · 2026-03-16

<details>
<summary>Abstract</summary>

The growing sophistication of speech generated by Artificial Intelligence (AI) has introduced new challenges in audio deepfake detection. Text-to-speech (TTS) and voice conversion (VC) technologies can create highly convincing synthetic speech with naturalness and intelligibility. This poses serious threats to voice biometric security and to systems designed to combat the spread of spoken misinformation, where synthetic voices may be used to disseminate false or malicious content. While interest in AI-generated speech has increased, resources for evaluating naturalness at the phoneme level remain limited. In this work, we address this gap by presenting the Phoneme-Level DeepFake dataset (PhonemeDF), comprising parallel real and synthetic speech segmented at the phoneme level. Real speech samples are derived from a subset of LibriSpeech, while synthetic samples are generated using four TTS and three VC systems. For each system, phoneme-aligned TextGrid files are obtained using the Montreal Forced Aligner (MFA). We compute the Kullback-Leibler divergence (KLD) between real and synthetic phoneme distributions to quantify fidelity and establish a ranking based on similarity to natural speech. Our findings show a clear correlation between the KLD of real and synthetic phoneme distributions and the performance of classifiers trained to distinguish them, suggesting that KLD can serve as an indicator of the most discriminative phonemes for deepfake detection.

</details>

### [WhispSynth: Scaling Multilingual Whisper Corpus through Real Data Curation and A Novel Pitch-free Generative Framework](2603.14853.md)
**Tianyi Tan, Jiaxin Ye, Yuanming Zhang, Xiaohuai Le et al.** · 2026-03-16

<details>
<summary>Abstract</summary>

Whisper generation is constrained by the difficulty of data collection. Because whispered speech has low acoustic amplitude, high-fidelity recording is challenging. In this paper, we introduce WhispSynth, a large-scale multilingual corpus constructed via a novel high-fidelity generative framework. Specifically, we propose a pipeline integrating Differentiable Digital Signal Processing (DDSP)-based pitch-free method with Text-to-Speech (TTS) models. This framework refines a comprehensive collection of resources, including our newly constructed WhispNJU dataset, into 118 hours of high-fidelity whispered speech from 479 speakers. Unlike standard synthetic or noisy real data, our data engine faithfully preserves source vocal timbre and linguistic content while ensuring acoustic consistency, providing a robust foundation for text-to-whisper research. Experimental results demonstrate that WhispSynth exhibits significantly higher quality than existing corpora. Moreover, our CosyWhisper, tuned with WhispSynth, achieves speech naturalness on par with ground-truth samples. The official implementation and related resources are available at https://github.com/tan90xx/cosywhisper.

</details>

### [CodecMOS-Accent: A MOS Benchmark of Resynthesized and TTS Speech from Neural Codecs Across English Accents](2603.14328.md)
**Wen-Chin Huang, Nicholas Sanders, Erica Cooper** · 2026-03-15

<details>
<summary>Abstract</summary>

We present the CodecMOS-Accent dataset, a mean opinion score (MOS) benchmark designed to evaluate neural audio codec (NAC) models and the large language model (LLM)-based text-to-speech (TTS) models trained upon them, especially across non-standard speech like accented speech. The dataset comprises 4,000 codec resynthesis and TTS samples from 24 systems, featuring 32 speakers spanning ten accents. A large-scale subjective test was conducted to collect 19,600 annotations from 25 listeners across three dimensions: naturalness, speaker similarity, and accent similarity. This dataset does not only represent an up-to-date study of recent speech synthesis system performance but reveals insights including a tight relationship between speaker and accent similarity, the predictive power of objective metrics, and a perceptual bias when listeners share the same accent with the speaker. This dataset is expected to foster research on more human-centric evaluation for NAC and accented TTS.

</details>

### [DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization](2603.14267.md)
**Ngoc-Son Nguyen, Thanh V. T. Tran, Jeongsoo Choi, Hieu-Nghia Huynh-Nguyen et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Video dubbing has broad applications in filmmaking, multimedia creation, and assistive speech technology. Existing approaches either train directly on limited dubbing datasets or adopt a two-stage pipeline that adapts pre-trained text-to-speech (TTS) models, which often struggle to produce expressive prosody, rich acoustic characteristics, and precise synchronization. To address these issues, we propose DiFlowDubber with a novel two-stage training framework that effectively transfers knowledge from a pre-trained TTS model to video-driven dubbing, with a discrete flow matching generative backbone. Specifically, we design a FaPro module that captures global prosody and stylistic cues from facial expressions and leverages this information to guide the modeling of subsequent speech attributes. To ensure precise speech-lip synchronization, we introduce a Synchronizer module that bridges the modality gap among text, video, and speech, thereby improving cross-modal alignment and generating speech that is temporally synchronized with lip movements. Experiments on two primary benchmark datasets demonstrate that DiFlowDubber outperforms previous methods across multiple metrics.

</details>

### [Affectron: Emotional Speech Synthesis with Affective and Contextually Aligned Nonverbal Vocalizations](2603.14432.md)
**Deok-Hyeon Cho, Hyung-Seok Oh, Seung-Bin Kim, Seong-Whan Lee** · 2026-03-15

<details>
<summary>Abstract</summary>

Nonverbal vocalizations (NVs), such as laughter and sighs, are central to the expression of affective cues in emotional speech synthesis. However, learning diverse and contextually aligned NVs remains challenging in open settings due to limited NV data and the lack of explicit supervision. Motivated by this challenge, we propose Affectron as a framework for affective and contextually aligned NV generation. Built on a small-scale open and decoupled corpus, Affectron introduces an NV-augmented training strategy that expands the distribution of NV types and insertion locations. We further incorporate NV structural masking into a speech backbone pre-trained on purely verbal speech to enable diverse and natural NV synthesis. Experimental results demonstrate that Affectron produces more expressive and diverse NVs than baseline systems while preserving the naturalness of the verbal speech stream.

</details>

### [The Voice Behind the Words: Quantifying Intersectional Bias in SpeechLLMs](2603.16941.md)
**Shree Harsha Bokkahalli Satish, Christoph Minixhofer, Maria Teleki, James Caverlee et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Speech Large Language Models (SpeechLLMs) process spoken input directly, retaining cues such as accent and perceived gender that were previously removed in cascaded pipelines. This introduces speaker identity dependent variation in responses. We present a large-scale intersectional evaluation of accent and gender bias in three SpeechLLMs using 2,880 controlled interactions across six English accents and two gender presentations, keeping linguistic content constant through voice cloning. Using pointwise LLM-judge ratings, pairwise comparisons, and Best-Worst Scaling with human validation, we detect consistent disparities. Eastern European-accented speech receives lower helpfulness scores, particularly for female-presenting voices. The bias is implicit: responses remain polite but differ in helpfulness. While LLM judges capture the directional trend of these biases, human evaluators exhibit significantly higher sensitivity, uncovering sharper intersectional disparities.

</details>

### [What Counts as Real? Speech Restoration and Voice Quality Conversion Pose New Challenges to Deepfake Detection](2603.14033.md)
**Shree Harsha Bokkahalli Satish, Harm Lameris, Joakim Gustafson, Éva Székely** · 2026-03-14

<details>
<summary>Abstract</summary>

Audio anti-spoofing systems are typically formulated as binary classifiers distinguishing bona fide from spoofed speech. This assumption fails under layered generative processing, where benign transformations introduce distributional shifts that are misclassified as spoofing. We show that phonation-modifying voice conversion and speech restoration are treated as out-of-distribution despite preserving speaker authenticity. Using a multi-class setup separating bona fide, converted, spoofed, and converted-spoofed speech, we analyse model behaviour through self-supervised learning (SSL) embeddings and acoustic correlates. The benign transformations induce a drift in the SSL space, compressing bona fide and spoofed speech and reducing classifier separability. Reformulating anti-spoofing as a multi-class problem improves robustness to benign shifts while preserving spoof detection, suggesting binary systems model the distribution of raw speech rather than authenticity itself.

</details>

### [Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization](2603.12565.md)
**Mengjie Zhao, Lianbo Liu, Yusuke Fujita, Hao Shi et al.** · 2026-03-13

<details>
<summary>Abstract</summary>

SpeechLLMs typically combine ASR-trained encoders with text-based LLM backbones, leading them to inherit written-style output patterns unsuitable for text-to-speech synthesis. This mismatch is particularly pronounced in Japanese, where spoken and written registers differ substantially in politeness markers, sentence-final particles, and syntactic complexity. We propose a preference-based alignment approach to adapt Japanese SpeechLLMs for speech-worthy outputs: text that is concise, conversational, and readily synthesized as natural speech. To rigorously evaluate this task, we introduce SpokenElyza, a benchmark for Japanese speech-worthiness derived from ELYZA-tasks-100 with auditory verification by native experts. Experiments show that our approach achieves substantial improvement on SpokenElyza while largely preserving performance on the original written-style evaluation. We will release SpokenElyza to support future research on Japanese spoken dialog systems.

</details>

### [DAST: A Dual-Stream Voice Anonymization Attacker with Staged Training](2603.12840.md)
**Ridwan Arefeen, Xiaoxiao Miao, Rong Tong, Aik Beng Ng et al.** · 2026-03-13

<details>
<summary>Abstract</summary>

Voice anonymization masks vocal traits while preserving linguistic content, which may still leak speaker-specific patterns. To assess and strengthen privacy evaluation, we propose a dual-stream attacker that fuses spectral and self-supervised learning features via parallel encoders with a three-stage training strategy. Stage I establishes foundational speaker-discriminative representations. Stage II leverages the shared identity-transformation characteristics of voice conversion and anonymization, exposing the model to diverse converted speech to build cross-system robustness. Stage III provides lightweight adaptation to target anonymized data. Results on the VoicePrivacy Attacker Challenge (VPAC) dataset demonstrate that Stage II is the primary driver of generalization, enabling strong attacking performance on unseen anonymization datasets. With Stage III, fine-tuning on only 10\% of the target anonymization dataset surpasses current state-of-the-art attackers in terms of EER.

</details>

### [VoXtream2: Full-stream TTS with dynamic speaking rate control](2603.13518.md)
**Nikita Torgashov, Gustav Eje Henter, Gabriel Skantze** · 2026-03-13

<details>
<summary>Abstract</summary>

Full-stream text-to-speech (TTS) for interactive systems must start speaking with minimal delay while remaining controllable as text arrives incrementally. We present VoXtream2, a zero-shot full-stream TTS model with dynamic speaking-rate control that can be updated mid-utterance on the fly. VoXtream2 combines a distribution matching mechanism over duration states with classifier-free guidance across conditioning signals to improve controllability and synthesis quality. Prompt-text masking enables textless audio prompting, removing the need for prompt transcription. Across standard zero-shot benchmarks and a dedicated speaking-rate test set, VoXtream2 achieves competitive objective and subjective results against public baselines despite a smaller model and less training data. In full-stream mode, it runs 4 times faster than real time with 74 ms first-packet latency on a consumer GPU.

</details>

### [Causal Prosody Mediation for Text-to-Speech:Counterfactual Training of Duration, Pitch, and Energy in FastSpeech2](2603.11683.md)
**Suvendu Sekhar Mohanty et.al.** · 2026-03-12

<details>
<summary>Abstract</summary>

We propose a novel causal prosody mediation framework for expressive text-to-speech (TTS) synthesis. Our approach augments the FastSpeech2 architecture with explicit emotion conditioning and introduces counterfactual training objectives to disentangle emotional prosody from linguistic content. By formulating a structural causal model of how text (content), emotion, and speaker jointly influence prosody (duration, pitch, energy) and ultimately the speech waveform, we derive two complementary loss terms: an Indirect Path Constraint (IPC) to enforce that emotion affects speech only through prosody, and a Counterfactual Prosody Constraint (CPC) to encourage distinct prosody patterns for different emotions. The resulting model is trained on multi-speaker emotional corpora (LibriTTS, EmoV-DB, VCTK) with a combined objective that includes standard spectrogram reconstruction and variance prediction losses alongside our causal losses. In evaluations on expressive speech synthesis, our method achieves significantly improved prosody manipulation and emotion rendering, with higher mean opinion scores (MOS) and emotion accuracy than baseline FastSpeech2 variants. We also observe better intelligibility (low WER) and speaker consistency when transferring emotions across speakers. Extensive ablations confirm that the causal objectives successfully separate prosody attribution, yielding an interpretable model that allows controlled counterfactual prosody editing (e.g. "same utterance, different emotion") without compromising naturalness. We discuss the implications for identifiability in prosody modeling and outline limitations such as the assumption that emotion effects are fully captured by pitch, duration, and energy. Our work demonstrates how integrating causal learning principles into TTS can improve controllability and expressiveness in generated speech.

</details>

### [RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis](2603.11678.md)
**Yongjoon Lee et.al.** · 2026-03-12

<details>
<summary>Abstract</summary>

We propose Relativistic Adversarial Feedback (RAF), a novel training objective for GAN vocoders that improves in-domain fidelity and generalization to unseen scenarios. Although modern GAN vocoders employ advanced architectures, their training objectives often fail to promote generalizable representations. RAF addresses this problem by leveraging speech self-supervised learning models to assist discriminators in evaluating sample quality, encouraging the generator to learn richer representations. Furthermore, we utilize relativistic pairing for real and fake waveforms to improve the modeling of the training data distribution. Experiments across multiple datasets show consistent gains in both objective and subjective metrics on GAN-based vocoders. Importantly, the RAF-trained BigVGAN-base outperforms the LSGAN-trained BigVGAN in perceptual quality using only 12\% of the parameters. Comparative studies further confirm the effectiveness of RAF as a training framework for GAN vocoders.

</details>

### [Probabilistic Verification of Voice Anti-Spoofing Models](2603.10713.md)
**Evgeny Kushnir et.al.** · 2026-03-12

<details>
<summary>Abstract</summary>

Recent advances in generative models have amplified the risk of malicious misuse of speech synthesis technologies, enabling adversaries to impersonate target speakers and access sensitive resources. Although speech deepfake detection has progressed rapidly, most existing countermeasures lack formal robustness guarantees or fail to generalize to unseen generation techniques. We propose PV-VASM, a probabilistic framework for verifying the robustness of voice anti-spoofing models (VASMs). PV-VASM estimates the probability of misclassification under text-to-speech (TTS), voice cloning (VC), and parametric signal transformations. The approach is model-agnostic and enables robustness verification against unseen speech synthesis techniques and input perturbations. We derive a theoretical upper bound on the error probability and validate the method across diverse experimental settings, demonstrating its effectiveness as a practical robustness verification tool.

</details>

### [TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling](2603.12350.md)
**Liang-Hsuan Tseng, Hung-yi Lee** · 2026-03-12

<details>
<summary>Abstract</summary>

Text-speech joint spoken language modeling (SLM) aims at natural and intelligent speech-based interactions, but developing such a system may suffer from modality mismatch: speech unit sequences are much longer than text tokens. Prior work reduces this gap with text-aligned tokenization and embedding (TASTE), producing speech tokens that align in lengths with their textual counterparts. However, the dependence on an external ASR system and the use of a non-causal decoder limits streaming use. To address this limitation, we propose TASTE-S, a streamable extension of TASTE suitable for real-time usage. TASTE-S integrates a CTC-based ASR module into the encoder for instant dual-modality encoding. We also redesign the unit decoder to enable on-the-fly decoding. With joint training, we show that TASTE-S matches TASTE's performance while significantly reducing latency. Further investigations reveal that TASTE-S remains robust to transcriptions and enables long-form encoding and decoding.

</details>

### [MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis](2603.12342.md)
**Tan Dat Nguyen, Sangmin Bae, Joon Son Chung, Ji-Hoon Kim** · 2026-03-12

<details>
<summary>Abstract</summary>

Despite the remarkable quality of LLM-based text-to-speech systems, their reliance on autoregressive Transformers leads to quadratic computational complexity, which severely limits practical applications. Linear-time alternatives, notably Mamba, offer a potential remedy; however, they often sacrifice the global context essential for expressive synthesis. In this paper, we propose MamTra, an interleaved Mamba-Transformer framework designed to leverage the advantages of Mamba's efficiency and Transformers' modeling capability. We also introduce novel knowledge transfer strategies to distill insights from a pretrained Transformer into our hybrid architecture, thereby bypassing the prohibitive costs of training from scratch. Systematic experiments identify the optimal hybrid configuration, and demonstrate that MamTra reduces inference VRAM usage by up to 34% without compromising speech fidelity - even trained on only 2% of the original training dataset. Audio samples are available at https://mamtratts.github.io.

</details>

### [Toward Complex-Valued Neural Networks for Waveform Generation](2603.11589.md)
**Hyung-Seok Oh, Deok-Hyeon Cho, Seung-Bin Kim, Seong-Whan Lee** · 2026-03-12

<details>
<summary>Abstract</summary>

Neural vocoders have recently advanced waveform generation, yielding natural and expressive audio. Among these approaches, iSTFT-based vocoders have recently gained attention. They predict a complex-valued spectrogram and then synthesize the waveform via iSTFT, thereby avoiding learned upsampling stages that can increase computational cost. However, current approaches use real-valued networks that process the real and imaginary parts independently. This separation limits their ability to capture the inherent structure of complex spectrograms. We present ComVo, a Complex-valued neural Vocoder whose generator and discriminator use native complex arithmetic. This enables an adversarial training framework that provides structured feedback in complex-valued representations. To guide phase transformations in a structured manner, we introduce phase quantization, which discretizes phase values and regularizes the training process. Finally, we propose a block-matrix computation scheme to improve training efficiency by reducing redundant operations. Experiments demonstrate that ComVo achieves higher synthesis quality than comparable real-valued baselines, and that its block-matrix scheme reduces training time by 25%. Audio samples and code are available at https://hs-oh-prml.github.io/ComVo/.

</details>

### [Vocal prosody and listening comprehension in advanced Arabic L2 learners: A mixed-methods study with comparative insights from English L2 pedagogy](s2:9b8483e5d54c7a11f81d15366e190162ecb7477c.md)
**D. Boulaares** · 2026-03-12

<details>
<summary>Abstract</summary>

This study investigates how prosodic parameters – speech rate, pausing, intonation contour, pitch range (F0 span), and monotony – shape listening comprehension among advanced learners of Arabic (CEFR B2–C1). Drawing on triangulated evidence from semi-structured instructor interviews ( n = 6), a learner survey ( n = 52), and a curriculum-embedded audit of textbook audio, the analysis integrates exploratory inferential statistics with acoustic-phonetic profiling in Praat (words-per-minute, pause metrics, F0 range, intensity). Convergent results identify fast, weakly segmented speech as the principal barrier to comprehension, with flattened or atypical intonation attenuating discourse-pragmatic signalling that listeners rely on for parsing and prediction. Relative to widely reported EAP benchmarks, the Arabic instructional materials examined exhibit slower delivery and narrower F0 spans, a pattern that risks limited ecological validity and potential under-preparation for authentic input. The findings refine bottom-up/top-down accounts and cognitive-load explanations by demonstrating that prosodic chunking – via tempo and temporal segmentation – mediates processing even at advanced proficiency. Pedagogically, the study motivates staged exposure to authentic-speed Arabic, explicit prosody-for-listening instruction (e.g. guided shadowing, cue tracking, and pause-aware transcription), and CEFR-aligned assessment targeting prosodic inference. Acoustic and statistical patterns jointly foreground speed and pausing as high-impact levers for instruction and materials design in Arabic second language (L2) listening.

</details>

### [When Fine-Tuning Fails and when it Generalises: Role of Data Diversity and Mixed Training in LLM-based TTS](2603.10904.md)
**Anupam Purwar et.al.** · 2026-03-11

<details>
<summary>Abstract</summary>

Large language models are increasingly adopted as semantic backbones for neural text-to-speech systems. However, frozen LLM representations are insufficient for modeling speaker specific acoustic and perceptual characteristics. Our experiments involving fine tuning of the Language Model backbone of TTS show promise in improving the voice consistency and Signal to Noise ratio SNR in voice cloning task. Across multiple speakers LoRA finetuning consistently outperforms the non-finetuned base Qwen-0.5B model across three complementary dimensions of speech quality. First, perceptual quality improves significantly with DNS-MOS gains of up to 0.42 points for speakers whose training data exhibits sufficient acoustic variability. Second, speaker fidelity improves for all evaluated speakers with consistent increases in voice similarity indicating that LoRA effectively adapts speaker identity representations without degrading linguistic modeling. Third, signal level quality improves in most cases with signal to noise ratio increasing by as much as 34 percent. Crucially these improvements are strongly governed by the characteristics of the training data. Speakers with high variability in acoustic energy and perceptual quality achieve simultaneous gains in DNS-MOS voice similarity and SNR. Overall this work establishes that LoRA finetuning is not merely a parameter efficient optimization technique but an effective mechanism for better speaker level adaptation in compact LLM-based TTS systems. When supported by sufficiently diverse training data LoRA adapted Qwen-0.5B consistently surpasses its frozen base model in perceptual quality speaker similarity with low latency using GGUF model hosted in quantized form.

</details>

### [Fish Audio S2 Technical Report](2603.08823.md)
**Shijia Liao et.al.** · 2026-03-11

<details>
<summary>Abstract</summary>

We introduce Fish Audio S2, an open-sourced text-to-speech system featuring multi-speaker, multi-turn generation, and, most importantly, instruction-following control via natural-language descriptions. To scale training, we develop a multi-stage training recipe together with a staged data pipeline covering video captioning and speech captioning, voice-quality assessment, and reward modeling. To push the frontier of open-source TTS, we release our model weights, fine-tuning code, and an SGLang-based inference engine. The inference engine is production-ready for streaming, achieving an RTF of 0.195 and a time-to-first-audio below 100 ms.Our code and weights are available on GitHub (https://github.com/fishaudio/fish-speech) and Hugging Face (https://huggingface.co/fishaudio/s2-pro). We highly encourage readers to visit https://fish.audio to try custom voices.

</details>

### [Speech-Omni-Lite: Portable Speech Interfaces for Vision-Language Models](2603.09627.md)
**Dehua Tao et.al.** · 2026-03-10

<details>
<summary>Abstract</summary>

While large-scale omni-models have demonstrated impressive capabilities across various modalities, their strong performance heavily relies on massive multimodal data and incurs substantial computational costs. This work introduces Speech-Omni-Lite, a cost-efficient framework for extending pre-trained Visual-Language (VL) backbones with speech understanding and generation capabilities, while fully preserving the backbones' vision-language performance. Specifically, the VL backbone is equipped with two lightweight, trainable plug-and-play modules, a speech projector and a speech token generator, while keeping the VL backbone fully frozen. To mitigate the scarcity of spoken QA corpora, a low-cost data construction strategy is proposed to generate Question-Text Answer-Text-Speech (QTATS) data from existing ASR speech-text pairs, facilitating effective speech generation training. Experimental results show that, even with only thousands of hours of speech training data, Speech-Omni-Lite achieves excellent spoken QA performance, which is comparable to omni-models trained on millions of hours of speech data. Furthermore, the learned speech modules exhibit strong transferability across VL backbones.

</details>

### [SPAR-K: Scheduled Periodic Alternating Early Exit for Spoken Language Models](2603.09215.md)
**Hsiao-Ying Huang et.al.** · 2026-03-10

<details>
<summary>Abstract</summary>

Interleaved spoken language models (SLMs) alternately generate text and speech tokens, but decoding at full transformer depth for every step becomes costly, especially due to long speech sequences. We propose SPAR-K, a modality-aware early exit framework designed to accelerate interleaved SLM inference while preserving perceptual quality. SPAR-K introduces a speech alternating-depth schedule: most speech positions exit at a fixed intermediate layer, while periodic full-depth "refresh" steps mitigate distribution shift due to early exit. We evaluate our framework using Step-Audio-2-mini and GLM-4-Voice across four datasets spanning reasoning, factual QA, and dialogue tasks, measuring performance in terms of ASR transcription accuracy and perceptual quality. Experimental results demonstrate that SPAR-K largely preserves question-answering accuracy with a maximum accuracy drop of 0.82\% while reducing average speech decoding depth by up to 11\% on Step-Audio-2-mini and 5\% on GLM-4-Voice, both with negligible changes in MOS and WER and no auxiliary computation overhead. We further demonstrate that confidence-based early exit strategies, widely used in text LLMs, are suboptimal for SLMs, highlighting that the unique statistical nature of speech tokens necessitates a specialized early exit design.

</details>

### [Emotion-Aware Prefix: Towards Explicit Emotion Control in Voice Conversion Models](2603.09120.md)
**Haoyuan Yang, Mu Yang, Jiamin Xie, Szu-Jui Chen et al.** · 2026-03-10

<details>
<summary>Abstract</summary>

Recent advances in zero-shot voice conversion have exhibited potential in emotion control, yet the performance is suboptimal or inconsistent due to their limited expressive capacity. We propose Emotion-Aware Prefix for explicit emotion control in a two-stage voice conversion backbone. We significantly improve emotion conversion performance, doubling the baseline Emotion Conversion Accuracy (ECA) from 42.40% to 85.50% while maintaining linguistic integrity and speech quality, without compromising speaker identity. Our ablation study suggests that a joint control of both sequence modulation and acoustic realization is essential to synthesize distinct emotions. Furthermore, comparative analysis verifies the generalizability of proposed method, while it provides insights on the role of acoustic decoupling in maintaining speaker identity.

</details>

### [Universal Speech Content Factorization](2603.08977.md)
**Henry Li Xinyuan et.al.** · 2026-03-09

<details>
<summary>Abstract</summary>

We propose Universal Speech Content Factorization (USCF), a simple and invertible linear method for extracting a low-rank speech representation in which speaker timbre is suppressed while phonetic content is preserved. USCF extends Speech Content Factorization, a closed-set voice conversion (VC) method, to an open-set setting by learning a universal speech-to-content mapping via least-squares optimization and deriving speaker-specific transformations from only a few seconds of target speech. We show through embedding analysis that USCF effectively removes speaker-dependent variation. As a zero-shot VC system, USCF achieves competitive intelligibility, naturalness, and speaker similarity compared to methods that require substantially more target-speaker data or additional neural training. Finally, we demonstrate that as a training-efficient timbre-disentangled speech feature, USCF features can serve as the acoustic representation for training timbre-prompted text-to-speech models. Speech samples and code are publicly available.

</details>

### [Scalable Neural Vocoder from Range-Null Space Decomposition](2603.08574.md)
**Andong Li, Tong Lei, Zhihang Sun, Rilin Chen et al.** · 2026-03-09

<details>
<summary>Abstract</summary>

Although deep neural networks have facilitated significant progress of neural vocoders in recent years, they usually suffer from intrinsic challenges like opaque modeling, inflexible retraining under different input configurations, and parameter-performance trade-off. These inherent hurdles can heavily impede the development of this field. To resolve these problems, in this paper, we propose a novel neural vocoder in the time-frequency (T-F) domain. Specifically, we bridge the connection between the classical range-null decomposition (RND) theory and the vocoder task, where the reconstruction of the target spectrogram is formulated into the superimposition between range-space and null-space. The former aims to project the representation in the original mel-domain into the target linear-scale domain, and the latter can be instantiated via neural networks to further infill the spectral details. To fully leverage the spectrum prior, an elaborate dual-path framework is devised, where the spectrum is hierarchically encoded and decoded, and the cross- and narrow-band modules are leveraged for effectively modeling along sub-band and time dimensions. To enable inference under various configurations, we propose a simple yet effective strategy, which transforms the multi-condition adaption in the inference stage into the data augmentation in the training stage. Comprehensive experiments are conducted on various benchmarks. Quantitative and qualitative results show that while enjoying lightweight network structure and scalable inference paradigm, the proposed framework achieves state-ofthe-art performance among existing advanced methods. Code is available at https://github.com/Andong-Li-speech/RNDVoC.

</details>

### [Targeted Speaker Poisoning Framework in Zero-Shot Text-to-Speech](2603.07551.md)
**Thanapat Trachu et.al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Zero-shot Text-to-Speech (TTS) voice cloning poses severe privacy risks, demanding the removal of specific speaker identities from trained TTS models. Conventional machine unlearning is insufficient in this context, as zero-shot TTS can dynamically reconstruct voices from just reference prompts. We formalize this task as Speech Generation Speaker Poisoning (SGSP), in which we modify trained models to prevent the generation of specific identities while preserving utility for other speakers. We evaluate inference-time filtering and parameter-modification baselines across 1, 15, and 100 forgotten speakers. Performance is assessed through the trade-off between utility (WER) and privacy, quantified using AUC and Forget Speaker Similarity (FSSIM). We achieve strong privacy for up to 15 speakers but reveal scalability limits at 100 speakers due to increased identity overlap. Our study thus introduces a novel problem and evaluation framework toward further advances in generative voice privacy.

</details>

### [Learning-free L2-Accented Speech Generation using Phonological Rules](2603.07550.md)
**Thanathai Lertpetchpun et.al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Accent plays a crucial role in speaker identity and inclusivity in speech technologies. Existing accented text-to-speech (TTS) systems either require large-scale accented datasets or lack fine-grained phoneme-level controllability. We propose a accented TTS framework that combines phonological rules with a multilingual TTS model. The rules are applied to phoneme sequences to transform accent at the phoneme level while preserving intelligibility. The method requires no accented training data and enables explicit phoneme-level accent manipulation. We design rule sets for Spanish- and Indian-accented English, modeling systematic differences in consonants, vowels, and syllable structure arising from phonotactic constraints. We analyze the trade-off between phoneme-level duration alignment and accent as realized in speech timing. Experimental results demonstrate effective accent shift while maintaining speech quality.

</details>

### [Accent Vector: Controllable Accent Manipulation for Multilingual TTS Without Accented Data](2603.07534.md)
**Thanathai Lertpetchpun et.al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Accent is an integral part of society, reflecting multiculturalism and shaping how individuals express identity. The majority of English speakers are non-native (L2) speakers, yet current Text-To-Speech (TTS) systems primarily model American-accented English due limited accented data. We propose \textit{Accent Vector}, a controllable representation that enables accent manipulation in multilingual TTS without requiring accented training data. \textit{Accent Vector} is derived by fine-tuning a TTS system on native speech of a different language (i.e. non-English) and computing task vectors capturing accent characteristics (i.e. in English). By scaling and interpolating the vector, we achieve fine-grained control over accent strength and generate mixed-accent speech. In addition, it generalizes beyond English, enabling accent control across multiple languages. Objective and human evaluations confirm the effectiveness of Accent Vector for fine-grained and compositional accent control.

</details>

### [Bolbosh: Script-Aware Flow Matching for Kashmiri Text-to-Speech](2603.07513.md)
**Tajamul Ashraf et.al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Kashmiri is spoken by around 7 million people but remains critically underserved in speech technology, despite its official status and rich linguistic heritage. The lack of robust Text-to-Speech (TTS) systems limits digital accessibility and inclusive human-computer interaction for native speakers. In this work, we present the first dedicated open-source neural TTS system designed for Kashmiri. We show that zero-shot multilingual baselines trained for Indic languages fail to produce intelligible speech, achieving a Mean Opinion Score (MOS) of only 1.86, largely due to inadequate modeling of Perso-Arabic diacritics and language-specific phonotactics. To address these limitations, we propose Bolbosh, a supervised cross-lingual adaptation strategy based on Optimal Transport Conditional Flow Matching (OT-CFM) within the Matcha-TTS framework. This enables stable alignment under limited paired data. We further introduce a three-stage acoustic enhancement pipeline consisting of dereverberation, silence trimming, and loudness normalization to unify heterogeneous speech sources and stabilize alignment learning. The model vocabulary is expanded to explicitly encode Kashmiri graphemes, preserving fine-grained vowel distinctions. Our system achieves a MOS of 3.63 and a Mel-Cepstral Distortion (MCD) of 3.73, substantially outperforming multilingual baselines and establishing a new benchmark for Kashmiri speech synthesis. Our results demonstrate that script-aware and supervised flow-based adaptation are critical for low-resource TTS in diacritic-sensitive languages. Code and data are available at: https://github.com/gaash-lab/Bolbosh.

</details>

### [Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision](2603.07025.md)
**Shreyas Gopal, Donghang Wu, Ashutosh Anshul, Yeo Yue Heng et al.** · 2026-03-07

<details>
<summary>Abstract</summary>

Speech Large Language Models (LLMs) that understand and follow instructions in many languages are useful for real-world interaction, but are difficult to train with supervised fine-tuning, requiring large, task-specific speech corpora. While recent distillation-based approaches train performant English-only Speech LLMs using only annotated ASR data by aligning text and speech using only a lightweight projector, these models under-perform when scaled to multilingual settings due to language interference in the shared projector. We address this by introducing language-aware distillation using a query bank and a gating network that selects or mixes query tokens using a Q-Former projector. Our approach shows gains of 14% over matched multilingual distillation baselines on instruction following. We further synthesize Audio-MLQA, a multilingual spoken QA benchmark built on MLQA with high-quality TTS questions. Our best model improves over existing Speech LLM baselines by 32% on Audio-MLQA.

</details>

### [Fast and Flexible Audio Bandwidth Extension via Vocos](2603.07285.md)
**Yatharth Sharma** · 2026-03-07

<details>
<summary>Abstract</summary>

We propose a Vocos-based bandwidth extension model that enhances audio at 8-48 kHz by generating missing high-frequency content. Inputs are resampled to 48 kHz and processed by a neural vocoder backbone, enabling a single network to support arbitrary upsampling ratios. A lightweight Linkwitz-Riley-inspired refiner merges the original low band with the generated high frequencies via a smooth crossover. On validation, the model achieves competitive log-spectral distance while running at a real-time factor of 0.0001 on an NVIDIA A100 GPU and 0.0053 on an 8-core CPU, demonstrating practical, high-quality BWE at extreme throughput.

</details>

### [Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input](2603.06444.md)
**Changsong Liu et.al.** · 2026-03-06

### [Activation Steering for Accent-Neutralized Zero-Shot Text-To-Speech](2603.05977.md)
**Mu Yang et.al.** · 2026-03-06

### [StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](2603.05800.md)
**Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri et al.** · 2026-03-06

<details>
<summary>Abstract</summary>

Advances in multi-modal generative models are enabling new applications, from storytelling to automated media synthesis. Most current workloads generate simple outputs (e.g., image generation from a prompt) in batch mode, often requiring several seconds even for basic results. Serving real-time multi-modal workflows at scale is costly and complex, requiring efficient coordination of diverse models (each with unique resource needs) across language, audio, image, and video, all under strict latency and resource constraints. We tackle these challenges through the lens of real-time podcast video generation, integrating LLMs, text-to-speech, and video-audio generation. To meet tight SLOs, we design an adaptive, modular serving system, StreamWise, that dynamically manages quality (e.g., resolution, sharpness), model/content parallelism, and resource-aware scheduling. We leverage heterogeneous hardware to maximize responsiveness and efficiency. For example, the system can lower video resolution and allocate more resources to early scenes. We quantify the trade-offs between latency, cost, and quality. The cheapest setup generates a 10-minute podcast video on A100 GPUs in 1.4 hours (8.4x slower than the real-time) for less than \$25. StreamWise enables high-quality real-time streaming with a sub-second startup delay under $45.

</details>

### [Is it Me? Toward Self-Extension to AI Avatars in Virtual Reality](2603.06030.md)
**Jieying Zhang, Steeven Villa, Abdallah El Ali** · 2026-03-06

<details>
<summary>Abstract</summary>

Advances in generative AI, speech synthesis, and embodied avatars enable systems that not only assist communication, but can act as proxies on users' behalf. Prior work in HCI has largely focused on systems as external tools, with less attention paid to the experiential consequences of users' speech and actions becoming assimilated with AI-generated output. We introduce the design and implementation of ProxyMe, a work-in-progress VR prototype that allows users to embody an avatar whose voice and spoken content are modified by an AI system. By combining avatar-based embodiment, voice cloning, and AI-mediated speech augmentation, ProxyMe invites the exploration of avatar self-extension: situations in which AI-modified communication is experienced as part of one's own expressive behavior. We chart out research challenges and envisioned scenarios, with a focus on how varying degrees of delegation and steerability can influence perceived agency, authorship, and self-identification.

</details>

### [How Well Do Current Speech Deepfake Detection Methods Generalize to the Real World?](2603.05852.md)
**Daixian Li, Jun Xue, Yanzhen Ren, Zhuolin Yi et al.** · 2026-03-06

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis and voice conversion have greatly improved the naturalness and authenticity of generated audio. Meanwhile, evolving encoding, compression, and transmission mechanisms on social media platforms further obscure deepfake artifacts. These factors complicate reliable detection in real-world environments, underscoring the need for representative evaluation benchmarks. To this end, we introduce ML-ITW (Multilingual In-The-Wild), a multilingual dataset covering 14 languages, seven major platforms, and 180 public figures, totaling 28.39 hours of audio. We evaluate three detection paradigms: end-to-end neural models, self-supervised feature-based (SSL) methods, and audio large language models (Audio LLMs). Experimental results reveal significant performance degradation across diverse languages and real-world acoustic conditions, highlighting the limited generalization ability of existing detectors in practical scenarios. The ML-ITW dataset is publicly available.

</details>

### [Conformer-iVITS: Efficient End-to-End Speech Synthesis with Convolution-Augmented Variational Inference](s2:e89826961ab2794549bd25463ea602e78c2ead33.md)
**Longtao Huang, Jiangtao Wang** · 2026-03-06

### [WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation](2603.05299.md)
**Luca Della Libera et.al.** · 2026-03-05

### [MSpoofTTS: Multi-Resolution Spoof-Guided Inference for Discrete Speech Synthesis](2603.05373.md)
**Junchuan Zhao, Minh Duc Vu, Ye Wang** · 2026-03-05

<details>
<summary>Abstract</summary>

Neural codec language models enable high-quality discrete speech synthesis, yet their inference remains vulnerable to token-level artifacts and distributional drift that degrade perceptual realism. Rather than relying on preference optimization or retraining, we propose MSpoof-TTS, a training-free inference framework that improves zero-shot synthesis through multi-resolution spoof guidance. We introduce a Multi-Resolution Token-based Spoof Detection framework that evaluates codec sequences at different temporal granularities to detect locally inconsistent or unnatural patterns. We then integrate the spoof detectors into a hierarchical decoding strategy, progressively pruning low-quality candidates and re-ranking hypotheses. This discriminator-guided generation enhances robustness without modifying model parameters. Experiments validate the effectiveness of our framework for robust and high-quality codec-based speech generation. Audio samples and code are available.

</details>

### [ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis](2603.04219.md)
**Youngwon Choi et.al.** · 2026-03-04

### [VietNormalizer: An Open-Source, Dependency-Free Python Library for Vietnamese Text Normalization in TTS and NLP Applications](2603.04145.md)
**Hung Vu Nguyen, Loan Do, Thanh Ngoc Nguyen, Ushik Shrestha Khwakhali et al.** · 2026-03-04

<details>
<summary>Abstract</summary>

We present VietNormalizer1, an open-source, zero-dependency Python library for Vietnamese text normalization targeting Text-to-Speech (TTS) and Natural Language Processing (NLP) applications. Vietnamese text normalization is a critical yet underserved preprocessing step: real-world Vietnamese text is densely populated with non-standard words (NSWs), including numbers, dates, times, currency amounts, percentages, acronyms, and foreign-language terms, all of which must be converted to fully pronounceable Vietnamese words before TTS synthesis or downstream language processing. Existing Vietnamese normalization tools either require heavy neural dependencies while covering only a narrow subset of NSW classes, or are embedded within larger NLP toolkits without standalone installability. VietNormalizer addresses these gaps through a unified, rule-based pipeline that: (1) converts arbitrary integers, decimals, and large numbers to Vietnamese words; (2) normalizes dates and times to their spoken Vietnamese forms; (3) handles VND and USD currency amounts; (4) expands percentages; (5) resolves acronyms via a customizable CSV dictionary; (6) transliterates non-Vietnamese loanwords and foreign terms to Vietnamese phonetic approximations; and (7) performs Unicode normalization and emoji/special-character removal. All regular expression patterns are pre-compiled at initialization, enabling high-throughput batch processing with minimal memory overhead and no GPU or external API dependency. The library is installable via pip install vietnormalizer, available on PyPI and GitHub at https://github.com/nghimestudio/vietnormalizer, and released under the MIT license. We discuss the design decisions, limitations of existing approaches, and the generalizability of the rule-based normalization paradigm to other low-resource tonal and agglutinative languages.

</details>

### [UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](2603.01418.md)
**Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin et al.** · 2026-03-02

<details>
<summary>Abstract</summary>

While state-of-the-art audio-video generation models like Veo3 and Sora2 demonstrate remarkable capabilities, their closed-source nature makes their architectures and training paradigms inaccessible. To bridge this gap in accessibility and performance, we introduce UniTalking, a unified, end-to-end diffusion framework for generating high-fidelity speech and lip-synchronized video. At its core, our framework employs Multi-Modal Transformer Blocks to explicitly model the fine-grained temporal correspondence between audio and video latent tokens via a shared self-attention mechanism. By leveraging powerful priors from a pre-trained video generation model, our framework ensures state-of-the-art visual fidelity while enabling efficient training. Furthermore, UniTalking incorporates a personalized voice cloning capability, allowing the generation of speech in a target style from a brief audio reference. Qualitative and quantitative results demonstrate that our method produces highly realistic talking portraits, achieving superior performance over existing open-source approaches in lip-sync accuracy, audio naturalness, and overall perceptual quality.

</details>

### [S-VoCAL: A Dataset and Evaluation Framework for Inferring Speaking Voice Character Attributes in Literature](2603.00958.md)
**Abigail Berthe-Pardo, Gaspard Michel, Elena V. Epure, Christophe Cerisara** · 2026-03-01

<details>
<summary>Abstract</summary>

With recent advances in Text-to-Speech (TTS) systems, synthetic audiobook narration has seen increased interest, reaching unprecedented levels of naturalness. However, larger gaps remain in synthetic narration systems' ability to impersonate fictional characters, and convey complex emotions or prosody. A promising direction to enhance character identification is the assignment of plausible voices to each fictional characters in a book. This step typically requires complex inference of attributes in book-length contexts, such as a character's age, gender, origin or physical health, which in turns requires dedicated benchmark datasets to evaluate extraction systems' performances. We present S-VoCAL (Speaking Voice Character Attributes in Literature), the first dataset and evaluation framework dedicated to evaluate the inference of voice-related fictional character attributes. S-VoCAL entails 8 attributes grounded in sociophonetic studies, and 952 character-book pairs derived from Project Gutenberg. Its evaluation framework addresses the particularities of each attribute, and includes a novel similarity metric based on recent Large Language Models embeddings. We demonstrate the applicability of S-VoCAL by applying a simple Retrieval-Augmented Generation (RAG) pipeline to the task of inferring character attributes. Our results suggest that the RAG pipeline reliably infers attributes such as Age or Gender, but struggles on others such as Origin or Physical Health. The dataset and evaluation code are available at https://github.com/AbigailBerthe/S-VoCAL .

</details>

### [TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment](2602.23068.md)
**Trung Dang, Sharath Rao, Ananya Gupta, Christopher Gagne et al.** · 2026-02-26

<details>
<summary>Abstract</summary>

Modern Text-to-Speech (TTS) systems increasingly leverage Large Language Model (LLM) architectures to achieve scalable, high-fidelity, zero-shot generation. However, these systems typically rely on fixed-frame-rate acoustic tokenization, resulting in speech sequences that are significantly longer than, and asynchronous with their corresponding text. Beyond computational inefficiency, this sequence length disparity often triggers hallucinations in TTS and amplifies the modality gap in spoken language modeling (SLM). In this paper, we propose a novel tokenization scheme that establishes one-to-one synchronization between continuous acoustic features and text tokens, enabling unified, single-stream modeling within an LLM. We demonstrate that these synchronous tokens maintain high-fidelity audio reconstruction and can be effectively modeled in a latent space by a large language model with a flow matching head. Moreover, the ability to seamlessly toggle speech modality within the context enables text-only guidance--a technique that blends logits from text-only and text-speech modes to flexibly bridge the gap toward text-only LLM intelligence. Experimental results indicate that our approach achieves performance competitive with state-of-the-art TTS and SLM systems while virtually eliminating content hallucinations and preserving linguistic integrity, all at a significantly reduced inference cost.

</details>

### [Discourse-Aware Dual-Track Streaming Response for Low-Latency Spoken Dialogue Systems](2602.23266.md)
**Siyuan Liu, Jiahui Xu, Feng Jiang, Kuang Wang et al.** · 2026-02-26

<details>
<summary>Abstract</summary>

Achieving human-like responsiveness is a critical yet challenging goal for cascaded spoken dialogue systems. Conventional ASR-LLM-TTS pipelines follow a strictly sequential paradigm, requiring complete transcription and full reasoning before speech synthesis can begin, which results in high response latency. We propose the Discourse-Aware Dual-Track Streaming Response (DDTSR) framework, a low-latency architecture that enables listen-while-thinking and speak-while-thinking. DDTSR is built upon three key mechanisms: (1) connective-guided small-large model synergy, where an auxiliary small model generates minimal-committal discourse connectives while a large model performs knowledge-intensive reasoning in parallel; (2) streaming-based cross-modal collaboration, which dynamically overlaps ASR, LLM inference, and TTS to advance the earliest speakable moment; and (3) curriculum-learning-based discourse continuity enhancement, which maintains coherence and logical consistency between early responses and subsequent reasoning outputs. Experiments on two spoken dialogue benchmarks demonstrate that DDTSR reduces response latency by 19%-51% while preserving discourse quality. Further analysis shows that DDTSR functions as a plug-and-play module compatible with diverse LLM backbones, and remains robust across varying utterance lengths, indicating strong practicality and scalability for real-time spoken interaction.

</details>

### [Scalable Multilingual Multimodal Machine Translation with Speech-Text Fusion](2602.21646.md)
**Yexing Du, Youcheng Pan, Zekun Wang, Zheng Chu et al.** · 2026-02-25

<details>
<summary>Abstract</summary>

Multimodal Large Language Models (MLLMs) have achieved notable success in enhancing translation performance by integrating multimodal information. However, existing research primarily focuses on image-guided methods, whose applicability is constrained by the scarcity of multilingual image-text pairs. The speech modality overcomes this limitation due to its natural alignment with text and the abundance of existing speech datasets, which enable scalable language coverage. In this paper, we propose a Speech-guided Machine Translation (SMT) framework that integrates speech and text as fused inputs into an MLLM to improve translation quality. To mitigate reliance on low-resource data, we introduce a Self-Evolution Mechanism. The core components of this framework include a text-to-speech model, responsible for generating synthetic speech, and an MLLM capable of classifying synthetic speech samples and iteratively optimizing itself using positive samples. Experimental results demonstrate that our framework surpasses all existing methods on the Multi30K multimodal machine translation benchmark, achieving new state-of-the-art results. Furthermore, on general machine translation datasets, particularly the FLORES-200, it achieves average state-of-the-art performance in 108 translation directions. Ablation studies on CoVoST-2 confirms that differences between synthetic and authentic speech have negligible impact on translation quality. The code and models are released at https://github.com/yxduir/LLM-SRT.

</details>

### [The Design Space of Tri-Modal Masked Diffusion Models](2602.21472.md)
**Louis Bethune, Victor Turrisi, Bruno Kacper Mlodozeniec, Pau Rodriguez Lopez et al.** · 2026-02-25

<details>
<summary>Abstract</summary>

Discrete diffusion models have emerged as strong alternatives to autoregressive language models, with recent work initializing and fine-tuning a base unimodal model for bimodal generation. Diverging from previous approaches, we introduce the first tri-modal masked diffusion model pretrained from scratch on text, image-text, and audio-text data. We systematically analyze multimodal scaling laws, modality mixing ratios, noise schedules, and batch-size effects, and we provide optimized inference sampling defaults. Our batch-size analysis yields a novel stochastic differential equation (SDE)-based reparameterization that eliminates the need for tuning the optimal batch size as reported in recent work. This reparameterization decouples the physical batch size, often chosen based on compute constraints (GPU saturation, FLOP efficiency, wall-clock time), from the logical batch size, chosen to balance gradient variance during stochastic optimization. Finally, we pretrain a preliminary 3B-parameter tri-modal model on 6.4T tokens, demonstrating the capabilities of a unified design and achieving strong results in text generation, text-to-image tasks, and text-to-speech tasks. Our work represents the largest-scale systematic open study of multimodal discrete diffusion models conducted to date, providing insights into scaling behaviors across multiple modalities.

</details>

### [CTC-TTS: LLM-based dual-streaming text-to-speech with CTC alignment](2602.19574.md)
**Hanwen Liu et.al.** · 2026-02-23

### [Can You Tell It's AI? Human Perception of Synthetic Voices in Vishing Scenarios](2602.20061.md)
**Zoha Hayat Bhatti, Bakhtawar Ahtisham, Seemal Tausif, Niklas George et al.** · 2026-02-23

<details>
<summary>Abstract</summary>

Large Language Models and commercial speech synthesis systems now enable highly realistic AI-generated voice scams (vishing), raising urgent concerns about deception at scale. Yet it remains unclear whether individuals can reliably distinguish AI-generated speech from human-recorded voices in realistic scam contexts and what perceptual strategies underlie their judgments. We conducted a controlled online study in which 22 participants evaluated 16 vishing-style audio clips (8 AI-generated, 8 human-recorded) and classified each as human or AI while reporting confidence. Participants performed poorly: mean accuracy was 37.5%, below chance in a binary classification task. At the stimulus level, misclassification was bidirectional: 75% of AI-generated clips were majority-labeled as human, while 62.5% of human-recorded clips were majority-labeled as AI. Signal Detection Theory analysis revealed near-zero discriminability (d' approx 0), indicating inability to reliably distinguish synthetic from human voices rather than simple response bias. Qualitative analysis of 315 coded excerpts revealed reliance on paralinguistic and emotional heuristics, including pauses, filler words, vocal variability, cadence, and emotional expressiveness. However, these surface-level cues traditionally associated with human authenticity were frequently replicated by AI-generated samples. Misclassifications were often accompanied by moderate to high confidence, suggesting perceptual miscalibration rather than uncertainty. Together, our findings demonstrate that authenticity judgments based on vocal heuristics are unreliable in contemporary vishing scenarios. We discuss implications for security interventions, user education, and AI-mediated deception mitigation.

</details>

### [Advances in GRPO for Generation Models: A Survey](2603.06623.md)
**Zexiang Liu, Xianglong He, Yangguang Li** · 2026-02-21

<details>
<summary>Abstract</summary>

Large-scale flow matching models have achieved strong performance across generative tasks such as text-to-image, video, 3D, and speech synthesis. However, aligning their outputs with human preferences and task-specific objectives remains challenging. Flow-GRPO extends Group Relative Policy Optimization (GRPO) to generation models, enabling stable reinforcement learning alignment for generative systems. Since its introduction, Flow-GRPO has triggered rapid research growth, spanning methodological refinements and diverse application domains. This survey provides a comprehensive review of Flow-GRPO and its subsequent developments. We organize existing work along two primary dimensions. First, we analyze methodological advances beyond the original framework, including reward signal design, credit assignment, sampling efficiency, diversity preservation, reward hacking mitigation, and reward model construction. Second, we examine extensions of GRPO-based alignment across generative paradigms and modalities, including text-to-image, video generation, image editing, speech and audio, 3D modeling, embodied vision-language-action systems, unified multimodal models, autoregressive and masked diffusion models, and restoration tasks. By synthesizing theoretical insights and practical adaptations, this survey highlights Flow-GRPO as a general alignment framework for modern generative models and outlines key open challenges for scalable and robust reinforcement-based generation.

</details>

### [MeanVoiceFlow: One-step Nonparallel Voice Conversion with Mean Flows](2602.18104.md)
**Takuhiro Kaneko, Hirokazu Kameoka, Kou Tanaka, Yuto Kondo** · 2026-02-20

<details>
<summary>Abstract</summary>

In voice conversion (VC) applications, diffusion and flow-matching models have exhibited exceptional speech quality and speaker similarity performances. However, they are limited by slow conversion owing to their iterative inference. Consequently, we propose MeanVoiceFlow, a novel one-step nonparallel VC model based on mean flows, which can be trained from scratch without requiring pretraining or distillation. Unlike conventional flow matching that uses instantaneous velocity, mean flows employ average velocity to more accurately compute the time integral along the inference path in a single step. However, training the average velocity requires its derivative to compute the target velocity, which can cause instability. Therefore, we introduce a structural margin reconstruction loss as a zero-input constraint, which moderately regularizes the input-output behavior of the model without harmful statistical averaging. Furthermore, we propose conditional diffused-input training in which a mixture of noise and source data is used as input to the model during both training and inference. This enables the model to effectively leverage source information while maintaining consistency between training and inference. Experimental results validate the effectiveness of these techniques and demonstrate that MeanVoiceFlow achieves performance comparable to that of previous multi-step and distillation-based models, even when trained from scratch. Audio samples are available at https://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/meanvoiceflow/.

</details>

### [CC-G2PnP: Streaming Grapheme-to-Phoneme and prosody with Conformer-CTC for unsegmented languages](2602.17157.md)
**Yuma Shirahata, Ryuichi Yamamoto** · 2026-02-19

<details>
<summary>Abstract</summary>

We propose CC-G2PnP, a streaming grapheme-to-phoneme and prosody (G2PnP) model to connect large language model and text-to-speech in a streaming manner. CC-G2PnP is based on Conformer-CTC architecture. Specifically, the input grapheme tokens are processed chunk by chunk, which enables streaming inference of phonemic and prosodic (PnP) labels. By guaranteeing minimal look-ahead size to each input token, the proposed model can consider future context in each token, which leads to stable PnP label prediction. Unlike previous streaming methods that depend on explicit word boundaries, the CTC decoder in CC-G2PnP effectively learns the alignment between graphemes and phonemes during training, making it applicable to unsegmented languages. Experiments on a Japanese dataset, which has no explicit word boundaries, show that CC-G2PnP significantly outperforms the baseline streaming G2PnP model in the accuracy of PnP label prediction.

</details>

### [How to Label Resynthesized Audio: The Dual Role of Neural Audio Codecs in Audio Deepfake Detection](2602.16343.md)
**Yixuan Xiao et.al.** · 2026-02-18

### [LLM-to-Speech: A Synthetic Data Pipeline for Training Dialectal Text-to-Speech Models](2602.15675.md)
**Ahmed Khaled Khamis et.al.** · 2026-02-17

### [UniTAF: A Modular Framework for Joint Text-to-Speech and Audio-to-Face Modeling](2602.15651.md)
**Qiangong Zhou, Nagasaka Tomohiro** · 2026-02-17

<details>
<summary>Abstract</summary>

This work considers merging two independent models, TTS and A2F, into a unified model to enable internal feature transfer, thereby improving the consistency between audio and facial expressions generated from text. We also discuss the extension of the emotion control mechanism from TTS to the joint model. This work does not aim to showcase generation quality; instead, from a system design perspective, it validates the feasibility of reusing intermediate representations from TTS for joint modeling of speech and facial expressions, and provides engineering practice references for subsequent speech expression co-design. The project code has been open source at: https://github.com/GoldenFishes/UniTAF

</details>

### [Probing Human Articulatory Constraints in End-to-End TTS with Reverse and Mismatched Speech-Text Directions](2602.14664.md)
**Parth Khadse et.al.** · 2026-02-16

### [GSRM: Generative Speech Reward Model for Speech RLHF](2602.13891.md)
**Maohao Shen, Tejas Jayashankar, Osama Hanna, Naoyuki Kanda et al.** · 2026-02-14

<details>
<summary>Abstract</summary>

Recent advances in speech language models, such as GPT-4o Voice Mode and Gemini Live, have demonstrated promising speech generation capabilities. Nevertheless, the aesthetic naturalness of the synthesized audio still lags behind that of human speech. Enhancing generation quality requires a reliable evaluator of speech naturalness. However, existing naturalness evaluators typically regress raw audio to scalar scores, offering limited interpretability of the evaluation and moreover fail to generalize to speech across different taxonomies. Inspired by recent advances in generative reward modeling, we propose the Generative Speech Reward Model (GSRM), a reasoning-centric reward model tailored for speech. The GSRM is trained to decompose speech naturalness evaluation into an interpretable acoustic feature extraction stage followed by feature-grounded chain-of-thought reasoning, enabling explainable judgments. To achieve this, we curated a large-scale human feedback dataset comprising 31k expert ratings and an out-of-domain benchmark of real-world user-assistant speech interactions. Experiments show that GSRM substantially outperforms existing speech naturalness predictors, achieving model-human correlation of naturalness score prediction that approaches human inter-rater consistency. We further show how GSRM can improve the naturalness of speech LLM generations by serving as an effective verifier for online RLHF.

</details>

### [SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis](2602.11477.md)
**Yifan Liang et.al.** · 2026-02-12

### [Calliope: A TTS-based Narrated E-book Creator Ensuring Exact Synchronization, Privacy, and Layout Fidelity](2602.10735.md)
**Hugo L. Hammer, Vajira Thambawita, Pål Halvorsen** · 2026-02-11

<details>
<summary>Abstract</summary>

A narrated e-book combines synchronized audio with digital text, highlighting the currently spoken word or sentence during playback. This format supports early literacy and assists individuals with reading challenges, while also allowing general readers to seamlessly switch between reading and listening. With the emergence of natural-sounding neural Text-to-Speech (TTS) technology, several commercial services have been developed to leverage these technology for converting standard text e-books into high-quality narrated e-books. However, no open-source solutions currently exist to perform this task. In this paper, we present Calliope, an open-source framework designed to fill this gap. Our method leverages state-of-the-art open-source TTS to convert a text e-book into a narrated e-book in the EPUB 3 Media Overlay format. The method offers several innovative steps: audio timestamps are captured directly during TTS, ensuring exact synchronization between narration and text highlighting; the publisher's original typography, styling, and embedded media are strictly preserved; and the entire pipeline operates offline. This offline capability eliminates recurring API costs, mitigates privacy concerns, and avoids copyright compliance issues associated with cloud-based services. The framework currently supports the state-of-the-art open-source TTS systems XTTS-v2 and Chatterbox. A potential alternative approach involves first generating narration via TTS and subsequently synchronizing it with the text using forced alignment. However, while our method ensures exact synchronization, our experiments show that forced alignment introduces drift between the audio and text highlighting significant enough to degrade the reading experience. Source code and usage instructions are available at https://github.com/hugohammer/TTS-Narrated-Ebook-Creator.git.

</details>

### [Emotion-Coherent Speech Data Augmentation and Self-Supervised Contrastive Style Training for Enhancing Kids's Story Speech Synthesis](2602.10164.md)
**Raymond Chung et.al.** · 2026-02-10

### [Covo-Audio Technical Report](2602.09823.md)
**Wenfu Wang, Chenxing Li, Liqiang Zhang, Yiyang Zhao et al.** · 2026-02-10

<details>
<summary>Abstract</summary>

In this work, we present Covo-Audio, a 7B-parameter end-to-end LALM that directly processes continuous audio inputs and generates audio outputs within a single unified architecture. Through large-scale curated pretraining and targeted post-training, Covo-Audio achieves state-of-the-art or competitive performance among models of comparable scale across a broad spectrum of tasks, including speech-text modeling, spoken dialogue, speech understanding, audio understanding, and full-duplex voice interaction. Extensive evaluations demonstrate that the pretrained foundation model exhibits strong speech-text comprehension and semantic reasoning capabilities on multiple benchmarks, outperforming representative open-source models of comparable scale. Furthermore, Covo-Audio-Chat, the dialogue-oriented variant, demonstrates strong spoken conversational abilities, including understanding, contextual reasoning, instruction following, and generating contextually appropriate and empathetic responses, validating its applicability to real-world conversational assistant scenarios. Covo-Audio-Chat-FD, the evolved full-duplex model, achieves substantially superior performance on both spoken dialogue capabilities and full-duplex interaction behaviors, demonstrating its competence in practical robustness. To mitigate the high cost of deploying end-to-end LALMs for natural conversational systems, we propose an intelligence-speaker decoupling strategy that separates dialogue intelligence from voice rendering, enabling flexible voice customization with minimal text-to-speech (TTS) data while preserving dialogue performance. Overall, our results highlight the strong potential of 7B-scale models to integrate sophisticated audio intelligence with high-level semantic reasoning, and suggest a scalable path toward more capable and versatile LALMs.

</details>

### [TVTSyn: Content-Synchronous Time-Varying Timbre for Streaming Voice Conversion and Anonymization](2602.09389.md)
**Waris Quamer, Mu-Ruei Tseng, Ghady Nasrallah, Ricardo Gutierrez-Osuna** · 2026-02-10

<details>
<summary>Abstract</summary>

Real-time voice conversion and speaker anonymization require causal, low-latency synthesis without sacrificing intelligibility or naturalness. Current systems have a core representational mismatch: content is time-varying, while speaker identity is injected as a static global embedding. We introduce a streamable speech synthesizer that aligns the temporal granularity of identity and content via a content-synchronous, time-varying timbre (TVT) representation. A Global Timbre Memory expands a global timbre instance into multiple compact facets; frame-level content attends to this memory, a gate regulates variation, and spherical interpolation preserves identity geometry while enabling smooth local changes. In addition, a factorized vector-quantized bottleneck regularizes content to reduce residual speaker leakage. The resulting system is streamable end-to-end, with <80 ms GPU latency. Experiments show improvements in naturalness, speaker transfer, and anonymization compared to SOTA streaming baselines, establishing TVT as a scalable approach for privacy-preserving and expressive speech synthesis under strict latency budgets.

</details>

### [SoulX-Singer: Towards High-Quality Zero-Shot Singing Voice Synthesis](2602.07803.md)
**Jiale Qian et.al.** · 2026-02-08

### [Zero-Shot TTS With Enhanced Audio Prompts: Bsc Submission For The 2026 Wildspoof Challenge TTS Track](2602.05770.md)
**Jose Giraldo et.al.** · 2026-02-05

### [Wave-Trainer-Fit: Neural Vocoder with Trainable Prior and Fixed-Point Iteration towards High-Quality Speech Generation from SSL features](2602.05443.md)
**Hien Ohnaka et.al.** · 2026-02-05

### [ARCHI-TTS: A flow-matching-based Text-to-Speech Model with Self-supervised Semantic Aligner and Accelerated Inference](2602.05207.md)
**Chunyat Wu et.al.** · 2026-02-05

### [PFluxTTS: Hybrid Flow-Matching TTS with Robust Cross-Lingual Voice Cloning and Inference-Time Model Fusion](2602.04160.md)
**Vikentii Pankov et.al.** · 2026-02-04

### [HoliAntiSpoof: Audio LLM for Holistic Speech Anti-Spoofing](2602.04535.md)
**Xuenan Xu, Yiming Ren, Liwei Liu, Wen Wu et al.** · 2026-02-04

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis and editing have made speech spoofing increasingly challenging. However, most existing methods treat spoofing as binary classification, overlooking that diverse spoofing techniques manipulate multiple, coupled speech attributes and their semantic effects. In this paper, we introduce HoliAntiSpoof, the first audio large language model (ALLM) framework for holistic speech anti-spoofing analysis. HoliAntiSpoof reformulates spoofing analysis as a unified text generation task, enabling joint reasoning over spoofing methods, affected speech attributes, and their semantic impacts. To support semantic-level analysis, we introduce DailyTalkEdit, a new anti-spoofing benchmark that simulates realistic conversational manipulations and provides annotations of semantic influence. Extensive experiments demonstrate that HoliAntiSpoof outperforms conventional baselines across multiple settings, while preliminary results show that in-context learning further improves out-of-domain generalization. These findings indicate that ALLMs not only enhance speech spoofing detection performance but also enable interpretable analysis of spoofing behaviors and their semantic effects, pointing towards more trustworthy and explainable speech security. Data and code are publicly available.

</details>

### [CoCoEmo: Composable and Controllable Human-Like Emotional TTS via Activation Steering](2602.03420.md)
**Siyi Wang, Shihong Tan, Siyi Liu, Hong Jia et al.** · 2026-02-03

<details>
<summary>Abstract</summary>

Emotional expression in human speech is nuanced and compositional, often involving multiple, sometimes conflicting, affective cues that may diverge from linguistic content. In contrast, most expressive text-to-speech systems enforce a single utterance-level emotion, collapsing affective diversity and suppressing mixed or text-emotion-misaligned expression. While activation steering via latent direction vectors offers a promising solution, it remains unclear whether emotion representations are linearly steerable in TTS, where steering should be applied within hybrid TTS architectures, and how such complex emotion behaviors should be evaluated. This paper presents the first systematic analysis of activation steering for emotional control in hybrid TTS models, introducing a quantitative, controllable steering framework, and multi-rater evaluation protocols that enable composable mixed-emotion synthesis and reliable text-emotion mismatch synthesis. Our results demonstrate, for the first time, that emotional prosody and expressive variability are primarily synthesized by the TTS language module instead of the flow-matching module, and also provide a lightweight steering approach for generating natural, human-like emotional speech.

</details>

### [DSFlow: Dual Supervision and Step-Aware Architecture for One-Step Flow Matching Speech Synthesis](2602.09041.md)
**Bin Lin, Peng Yang, Chao Yan, Xiaochen Liu et al.** · 2026-02-03

<details>
<summary>Abstract</summary>

Flow-matching models have enabled high-quality text-to-speech synthesis, but their iterative sampling process during inference incurs substantial computational cost. Although distillation is widely used to reduce the number of inference steps, existing methods often suffer from process variance due to endpoint error accumulation. Moreover, directly reusing continuous-time architectures for discrete, fixed-step generation introduces structural parameter inefficiencies. To address these challenges, we introduce DSFlow, a modular distillation framework for few-step and one-step synthesis. DSFlow reformulates generation as a discrete prediction task and explicitly adapts the student model to the target inference regime. It improves training stability through a dual supervision strategy that combines endpoint matching with deterministic mean-velocity alignment, enforcing consistent generation trajectories across inference steps. In addition, DSFlow improves parameter efficiency by replacing continuous-time timestep conditioning with lightweight step-aware tokens, aligning model capacity with the significantly reduced timestep space of the discrete task. Extensive experiments across diverse flow-based text-to-speech architectures demonstrate that DSFlow consistently outperforms standard distillation approaches, achieving strong few-step and one-step synthesis quality while reducing model parameters and inference cost.

</details>

### [LipSody: Lip-to-Speech Synthesis with Enhanced Prosody Consistency](2602.01908.md)
**Jaejun Lee, Yoori Oh, Kyogu Lee** · 2026-02-02

<details>
<summary>Abstract</summary>

Lip-to-speech synthesis aims to generate speech audio directly from silent facial video by reconstructing linguistic content from lip movements, providing valuable applications in situations where audio signals are unavailable or degraded. While recent diffusion-based models such as LipVoicer have demonstrated impressive performance in reconstructing linguistic content, they often lack prosodic consistency. In this work, we propose LipSody, a lip-to-speech framework enhanced for prosody consistency. LipSody introduces a prosody-guiding strategy that leverages three complementary cues: speaker identity extracted from facial images, linguistic content derived from lip movements, and emotional context inferred from face video. Experimental results demonstrate that LipSody substantially improves prosody-related metrics, including global and local pitch deviations, energy consistency, and speaker similarity, compared to prior approaches.

</details>

### [VividVoice: A Unified Framework for Scene-Aware Visually-Driven Speech Synthesis](2602.02591.md)
**Chengyuan Ma, Jiawei Jin, Ruijie Xiong, Chunxiang Jin et al.** · 2026-02-01

<details>
<summary>Abstract</summary>

We introduce and define a novel task-Scene-Aware Visually-Driven Speech Synthesis, aimed at addressing the limitations of existing speech generation models in creating immersive auditory experiences that align with the real physical world. To tackle the two core challenges of data scarcity and modality decoupling, we propose VividVoice, a unified generative framework. First, we constructed a large-scale, high-quality hybrid multimodal dataset, Vivid-210K, which, through an innovative programmatic pipeline, establishes a strong correlation between visual scenes, speaker identity, and audio for the first time. Second, we designed a core alignment module, D-MSVA, which leverages a decoupled memory bank architecture and a cross-modal hybrid supervision strategy to achieve fine-grained alignment from visual scenes to timbre and environmental acoustic features. Both subjective and objective experimental results provide strong evidence that VividVoice significantly outperforms existing baseline models in terms of audio fidelity, content clarity, and multimodal consistency. Our demo is available at https://chengyuann.github.io/VividVoice/.

</details>

### [HierCon: Hierarchical Contrastive Attention for Audio Deepfake Detection](2602.01032.md)
**Zhili Nicholas Liang, Soyeon Caren Han, Qizhou Wang, Christopher Leckie** · 2026-02-01

<details>
<summary>Abstract</summary>

Audio deepfakes generated by modern TTS and voice conversion systems are increasingly difficult to distinguish from real speech, raising serious risks for security and online trust. While state-of-the-art self-supervised models provide rich multi-layer representations, existing detectors treat layers independently and overlook temporal and hierarchical dependencies critical for identifying synthetic artefacts. We propose HierCon, a hierarchical layer attention framework combined with margin-based contrastive learning that models dependencies across temporal frames, neighbouring layers, and layer groups, while encouraging domain-invariant embeddings. Evaluated on ASVspoof 2021 DF and In-the-Wild datasets, our method achieves state-of-the-art performance (1.93% and 6.87% EER), improving over independent layer weighting by 36.6% and 22.5% respectively. The results and attention visualisations confirm that hierarchical modelling enhances generalisation to cross-domain generation techniques and recording conditions.

</details>

### [Edit Content, Preserve Acoustics: Imperceptible Text-Based Speech Editing via Self-Consistency Rewards](2602.00560.md)
**Yong Ren, Jiangyan Yi, Jianhua Tao, Tao Wang et al.** · 2026-01-31

<details>
<summary>Abstract</summary>

Imperceptible text-based speech editing modifies spoken content through transcript manipulation while preserving acoustic continuity. Prior acoustic-space approaches suffer from content-style entanglement, causing unstable generation and boundary artifacts. We introduce a framework guided by the principle of "Edit Content, Preserve Acoustics". Editing is conducted in a stable semantic space, while acoustic realization is handled by a Flow Matching decoder. To ensure perceptual consistency, we propose Self-Consistency Rewards Group Relative Policy Optimization, which leverages a pre-trained Text-to-Speech model as an implicit critic, together with intelligibility and duration constraints. Experiments demonstrate consistent improvements over state-of-the-art autoregressive and non-autoregressive baselines in intelligibility, robustness, and perceptual quality.

</details>

### [RVCBench: Benchmarking the Robustness of Voice Cloning Across Modern Audio Generation Models](2602.00443.md)
**Ruinan Jin, Xinting Liao, Hanlin Yu, Deval Pandya et al.** · 2026-01-31

<details>
<summary>Abstract</summary>

Modern voice cloning, also known as zero-shot text-to-speech (TTS), can synthesize speech that closely matches a target speaker from only seconds of reference audio, enabling applications such as personalized speech interfaces and dubbing. In practice, these systems often face noisy reference audio, imperfect text prompts, multilingual and long-form generation, post-processing, and adversarial perturbations, all of which can weaken robustness. Despite rapid progress in codec-token language models and diffusion-based TTS, robustness under realistic deployment shifts remains underexplored. This paper introduces RVCBench, a comprehensive dataset and benchmark for evaluating robustness in voice cloning. RVCBench provides task-aligned tests covering controlled text-audio pairing, multilingual and long-form scenarios, expressive prompts, post-processing conditions, and passive or proactive audio perturbations. Across 18 robustness evaluations, 225 speakers, and 14,370 utterances, RVCBench supports unified evaluation of input sensitivity, generation stability, output resilience, perturbation robustness, speaker similarity, and deepfake detectability. We evaluate 18 representative open-source voice cloning models and reveal systematic vulnerabilities in content consistency, speaker similarity, long-form stability, post-processing resilience, adversarial robustness, and detector-facing separability. We release the code and dataset to support reproducible evaluation and future research on robust voice cloning, speech synthesis, and audio generation. Code: https://github.com/Nanboy-Ronan/RVCBench. Dataset: https://huggingface.co/datasets/Nanboy/RVCBench.

</details>

### [Multi-Speaker Conversational Audio Deepfake: Taxonomy, Dataset and Pilot Study](2602.00295.md)
**Alabi Ahmed, Vandana Janeja, Sanjay Purushotham** · 2026-01-30

<details>
<summary>Abstract</summary>

The rapid advances in text-to-speech (TTS) technologies have made audio deepfakes increasingly realistic and accessible, raising significant security and trust concerns. While existing research has largely focused on detecting single-speaker audio deepfakes, real-world malicious applications with multi-speaker conversational settings is also emerging as a major underexplored threat. To address this gap, we propose a conceptual taxonomy of multi-speaker conversational audio deepfakes, distinguishing between partial manipulations (one or multiple speakers altered) and full manipulations (entire conversations synthesized). As a first step, we introduce a new Multi-speaker Conversational Audio Deepfakes Dataset (MsCADD) of 2,830 audio clips containing real and fully synthetic two-speaker conversations, generated using VITS and SoundStorm-based NotebookLM models to simulate natural dialogue with variations in speaker gender, and conversational spontaneity. MsCADD is limited to text-to-speech (TTS) types of deepfake. We benchmark three neural baseline models; LFCC-LCNN, RawNet2, and Wav2Vec 2.0 on this dataset and report performance in terms of F1 score, accuracy, true positive rate (TPR), and true negative rate (TNR). Results show that these baseline models provided a useful benchmark, however, the results also highlight that there is a significant gap in multi-speaker deepfake research in reliably detecting synthetic voices under varied conversational dynamics. Our dataset and benchmarks provide a foundation for future research on deepfake detection in conversational scenarios, which is a highly underexplored area of research but also a major area of threat to trustworthy information in audio settings. The MsCADD dataset is publicly available to support reproducibility and benchmarking by the research community.

</details>

### [Now You Hear Me: Audio Narrative Attacks Against Large Audio-Language Models](2601.23255.md)
**Ye Yu, Haibo Jin, Yaoning Yu, Jun Zhuang et al.** · 2026-01-30

<details>
<summary>Abstract</summary>

Large audio-language models increasingly operate on raw speech inputs, enabling more seamless integration across domains such as voice assistants, education, and clinical triage. This transition, however, introduces a distinct class of vulnerabilities that remain largely uncharacterized. We examine the security implications of this modality shift by designing a text-to-audio jailbreak that embeds disallowed directives within a narrative-style audio stream. The attack leverages an advanced instruction-following text-to-speech (TTS) model to exploit structural and acoustic properties, thereby circumventing safety mechanisms primarily calibrated for text. When delivered through synthetic speech, the narrative format elicits restricted outputs from state-of-the-art models, including Gemini 2.0 Flash, achieving a 98.26% success rate that substantially exceeds text-only baselines. These results highlight the need for safety frameworks that jointly reason over linguistic and paralinguistic representations, particularly as speech-based interfaces become more prevalent.

</details>

### [EmoShift: Lightweight Activation Steering for Enhanced Emotion-Aware Speech Synthesis](2601.22873.md)
**Li Zhou, Hao Jiang, Junjie Li, Tianrui Wang et al.** · 2026-01-30

<details>
<summary>Abstract</summary>

Achieving precise and controllable emotional expression is crucial for producing natural and context-appropriate speech in text-to-speech (TTS) synthesis. However, many emotion-aware TTS systems, including large language model (LLM)-based designs, rely on scaling fixed emotion embeddings or external guidance, limiting their ability to model emotion-specific latent characteristics. To address this gap, we present EmoShift, a lightweight activation-steering framework incorporating a EmoSteer layer, which learns a steering vector for each target emotion in the output embedding space to capture its latent offset and maintain stable, appropriate expression across utterances and categories. With only 10M trainable parameters,less than 1/30 of full fine-tuning, EmoShift outperforms zero-shot and fully fine-tuned baselines in objective and subjective evaluations, enhancing emotional expressiveness while preserving naturalness and speaker similarity. Further analysis confirms the proposed EmoSteer layer's effectiveness and reveals its potential for controllable emotional intensity in speech synthesis.

</details>

### [Evaluating and Rewarding LALMs for Expressive Role-Play TTS via Mean Continuation Log-Probability](2601.22661.md)
**Yong Ren, Jingbei Li, Haiyang Sun, Yujie Chen et al.** · 2026-01-30

<details>
<summary>Abstract</summary>

Recent advances in Large Audio Language Models (LALMs) have extended Text-to-Speech (TTS) to interactive role-play scenarios, which demand high expressiveness and strict adherence to role-play instructions. However, existing models struggle to maintain stylistic consistency with character profiles and scene descriptions across multi-turn dialogues. A critical bottleneck is the lack of objective metrics for quantifying speaking style. To bridge this gap, we propose Mean Continuation Log-Probability (MCLP) as both an evaluation metric and a reward signal, validated on LALM-based Role-Play TTS (RP-TTS) tasks. MCLP leverages the in-context learning capability of pretrained LALMs to measure the likelihood of ground-truth speech tokens conditioned on a contextual history consisting of the transcript, generated speech, and repeated transcript, serving as a proxy for stylistic continuity. Furthermore, we employ MCLP as a reinforcement learning reward to enhance the style alignment between generated speech and role-play instructions. To support this task, we construct a large-scale RP-TTS dataset with rich scene and character annotations. Experiments demonstrate that MCLP is well aligned with human judgments of stylistic consistency and serves as an effective reward for improving RP-TTS, leading to consistent gains in both objective metrics and subjective evaluations. Our code is publicly available at https://github.com/y-ren16/MCLP.

</details>

### [Speech Quality-Based Localization of Low-Quality Speech and Text-to-Speech Synthesis Artefacts](2601.21886.md)
**Michael Kuhlmann, Alexander Werning, Thilo von Neumann, Reinhold Haeb-Umbach** · 2026-01-29

<details>
<summary>Abstract</summary>

A large number of works view the automatic assessment of speech from an utterance- or system-level perspective. While such approaches are good in judging overall quality, they cannot adequately explain why a certain score was assigned to an utterance. frame-level scores can provide better interpretability, but models predicting them are harder to tune and regularize since no strong targets are available during training. In this work, we show that utterance-level speech quality predictors can be regularized with a segment-based consistency constraint which notably reduces frame-level stochasticity. We then demonstrate two applications involving frame-level scores: The partial spoof scenario and the detection of synthesis artefacts in two state-of-the-art text-to-speech systems. For the latter, we perform listening tests and confirm that listeners rate segments to be of poor quality more often in the set defined by low frame-level scores than in a random control set.

</details>

### [Audio Deepfake Detection in the Age of Advanced Text-to-Speech models](2601.20510.md)
**Robin Singh et.al.** · 2026-01-28

### [Erasing Your Voice Before It's Heard: Training-free Speaker Unlearning for Zero-shot Text-to-Speech](2601.20481.md)
**Myungjin Lee et.al.** · 2026-01-28

### [ASR for Affective Speech: Investigating Impact of Emotion and Speech Generative Strategy](2601.20319.md)
**Ya-Tse Wu et.al.** · 2026-01-28

### [Unit-Based Agent for Semi-Cascaded Full-Duplex Dialogue Systems](2601.20230.md)
**Haoyuan Yu, Yuxuan Chen, Minjie Cai** · 2026-01-28

<details>
<summary>Abstract</summary>

Full-duplex voice interaction is crucial for natural human computer interaction. We present a framework that decomposes complex dialogue into minimal conversational units, enabling the system to process each unit independently and predict when to transit to the next. This framework is instantiated as a semi-cascaded full-duplex dialogue system built around a multimodal large language model, supported by auxiliary modules such as voice activity detection (VAD) and text-to-speech (TTS) synthesis. The resulting system operates in a train-free, plug-and-play manner. Experiments on the HumDial dataset demonstrate the effectiveness of our framework, which ranks second among all teams on the test set of the Human-like Spoken Dialogue Systems Challenge (Track 2: Full-Duplex Interaction). Code is available at the GitHub repository https://github.com/yu-haoyuan/fd-badcat.

</details>

### [Self Voice Conversion as an Attack against Neural Audio Watermarking](2601.20432.md)
**Yigitcan Özer, Wanying Ge, Zhe Zhang, Xin Wang et al.** · 2026-01-28

<details>
<summary>Abstract</summary>

Audio watermarking embeds auxiliary information into speech while maintaining speaker identity, linguistic content, and perceptual quality. Although recent advances in neural and digital signal processing-based watermarking methods have improved imperceptibility and embedding capacity, robustness is still primarily assessed against conventional distortions such as compression, additive noise, and resampling. However, the rise of deep learning-based attacks introduces novel and significant threats to watermark security. In this work, we investigate self voice conversion as a universal, content-preserving attack against audio watermarking systems. Self voice conversion remaps a speaker's voice to the same identity while altering acoustic characteristics through a voice conversion model. We demonstrate that this attack severely degrades the reliability of state-of-the-art watermarking approaches and highlight its implications for the security of modern audio watermarking techniques.

</details>

### [End-to-End Speech Synthesis of Financial Statements via Multi-Task Learning](s2:0d742bd7ebb73d463630d07fcf6023c1f3c66465.md)
**Kandi Kranthi Kumar, R. Mishra** · 2026-01-28

<details>
<summary>Abstract</summary>

With the emergence of end-to-end neural networks, e.g., Tacotron and Tacotron-2 systems, the progress of speech synthesis systems has been truly remarkable. These models, however, have been found to fail when used in domain-specific applications, such as the narration of financial reports or earnings statements, to be capable of ensuring coherence, prosodic phrasing, and clarity in numerical and monetary statements. This paper contains a critical review and a new application of Multi-Task Learning (MTL) to Tacotron-based TTS systems, including improving prosody, intelligibility, and expressiveness of long-form financial text. We combine knowledge of the main works and suggest an integrated framework of MTL-Tacotron2, which combines the idea of phrase-break prediction and the concept of the spectral refinement of the wavelets. The method is more natural and numerically accurate, as confirmed by objective and subjective measures based on SPGISpeech and curated financial data.

</details>

### [T-Mimi: A Transformer-based Mimi Decoder for Real-Time On-Phone TTS](2601.20094.md)
**Haibin Wu et.al.** · 2026-01-27

### [Phonological Tokenizer: Prosody-Aware Phonetic Token via Multi-Objective Fine-Tuning with Differentiable K-Means](2601.19781.md)
**Kentaro Onda et.al.** · 2026-01-27

### [Rethinking Discrete Speech Representation Tokens for Accent Generation](2601.19786.md)
**Jinzuomu Zhong, Yi Wang, Korin Richmond, Peter Bell** · 2026-01-27

<details>
<summary>Abstract</summary>

Discrete Speech Representation Tokens (DSRTs) have become a foundational component in speech generation. While prior work has extensively studied phonetic and speaker information in DSRTs, how accent information is encoded in DSRTs remains largely unexplored. In this paper, we present the first systematic investigation of accent information in DSRTs. We propose a unified evaluation framework that measures both accessibility of accent information via a novel Accent ABX task and recoverability via cross-accent Voice Conversion (VC) resynthesis. Using this framework, we analyse DSRTs derived from several widely used speech representations. Our results reveal that: (1) choice of layers has the most significant impact on retaining accent information, (2) accent information is substantially reduced by ASR supervision; (3) naive codebook size reduction cannot effectively disentangle accent from phonetic and speaker information.

</details>

### [Neural Multi-Speaker Voice Cloning for Nepali in Low-Resource Settings](2601.18694.md)
**Aayush M. Shrestha et.al.** · 2026-01-26

### [UrgentMOS: Unified Multi-Metric and Preference Learning for Robust Speech Quality Assessment](2601.18438.md)
**Wei Wang, Wangyou Zhang, Chenda Li, Jiahe Wang et al.** · 2026-01-26

<details>
<summary>Abstract</summary>

Automatic speech quality assessment has become increasingly important as modern speech generation systems continue to advance, while human listening tests remain costly, time-consuming, and difficult to scale. Most existing learning-based assessment models rely primarily on scarce human-annotated mean opinion score (MOS) data, which limits robustness and generalization, especially when training across heterogeneous datasets. In this work, we propose UrgentMOS, a unified speech quality assessment framework that jointly learns from diverse objective and perceptual quality metrics, while explicitly tolerating the absence of arbitrary subsets of metrics during training. By leveraging complementary quality facets under heterogeneous supervision, UrgentMOS enables effective utilization of partially annotated data and improves robustness when trained on large-scale, multi-source datasets. Beyond absolute score prediction, UrgentMOS explicitly models pairwise quality preferences by directly predicting comparative MOS (CMOS), making it well suited for preference-based evaluation scenarios commonly adopted in system benchmarking. Extensive experiments across a wide range of speech quality datasets, including simulated distortions, speech enhancement, and speech synthesis, demonstrate that UrgentMOS consistently achieves state-of-the-art performance in both absolute and comparative evaluation settings.

</details>

### [OneVoice: One Model, Triple Scenarios-Towards Unified Zero-shot Voice Conversion](2601.18094.md)
**Zhichao Wang, Tao Li, Wenshuo Ge, Zihao Cui et al.** · 2026-01-26

<details>
<summary>Abstract</summary>

Recent progress of voice conversion~(VC) has achieved a new milestone in speaker cloning and linguistic preservation. But the field remains fragmented, relying on specialized models for linguistic-preserving, expressive, and singing scenarios. We propose OneVoice, a unified zero-shot framework capable of handling all three scenarios within a single model. OneVoice is built upon a continuous language model trained with VAE-free next-patch diffusion, ensuring high fidelity and efficient sequence modeling. Its core design for unification lies in a Mixture-of-Experts (MoE) designed to explicitly model shared conversion knowledge and scenario-specific expressivity. Expert selection is coordinated by a dual-path routing mechanism, including shared expert isolation and scenario-aware domain expert assignment with global-local cues. For precise conditioning, scenario-specific prosodic features are fused into each layer via a gated mechanism, allowing adaptive usage of prosody information. Furthermore, to enable the core idea and alleviate the imbalanced issue (abundant speech vs. scarce singing), we adopt a two-stage progressive training that includes foundational pre-training and scenario enhancement with LoRA-based domain experts. Experiments show that OneVoice matches or surpasses specialized models across all three scenarios, while verifying flexible control over scenarios and offering a fast decoding version as few as 2 steps. Audio samples are available on demo page.

</details>

### [AR-Omni: A Unified Autoregressive Model for Any-to-Any Generation](2601.17761.md)
**Dongjie Cheng, Ruifeng Yuan, Yongqi Li, Runyang You et al.** · 2026-01-25

<details>
<summary>Abstract</summary>

Real-world perception and interaction are inherently multimodal, encompassing not only language but also vision and speech, which motivates the development of "Omni" MLLMs that support both multimodal inputs and multimodal outputs. While a sequence of omni MLLMs has emerged, most existing systems still rely on additional expert components to achieve multimodal generation, limiting the simplicity of unified training and inference. Autoregressive (AR) modeling, with a single token stream, a single next-token objective, and a single decoder, is an elegant and scalable foundation in the text domain. Motivated by this, we present AR-Omni, a unified any-to-any model in the autoregressive paradigm without any expert decoders. AR-Omni supports autoregressive text and image generation, as well as streaming speech generation, all under a single Transformer decoder. We further address three practical issues in unified AR modeling: modality imbalance via task-aware loss reweighting, visual fidelity via a lightweight token-level perceptual alignment loss for image tokens, and stability-creativity trade-offs via a finite-state decoding mechanism. Empirically, AR-Omni achieves strong quality across three modalities while remaining real-time, achieving a 0.88 real-time factor for speech generation.

</details>

### [SonoEdit: Null-Space Constrained Knowledge Editing for Pronunciation Correction in LLM-Based TTS](2601.17086.md)
**Ayush Pratap Singh et.al.** · 2026-01-23

### [Timbre-Aware LLM-based Direct Speech-to-Speech Translation Extendable to Multiple Language Pairs](2601.16023.md)
**Lalaram Arya et.al.** · 2026-01-22

### [DeepASMR: LLM-Based Zero-Shot ASMR Speech Generation for Anyone of Any Voice](2601.15596.md)
**Leying Zhang et.al.** · 2026-01-22

### [Qwen3-TTS Technical Report](2601.15621.md)
**Hangrui Hu, Xinfa Zhu, Ting He, Dake Guo et al.** · 2026-01-22

<details>
<summary>Abstract</summary>

In this report, we present the Qwen3-TTS series, a family of advanced multilingual, controllable, robust, and streaming text-to-speech models. Qwen3-TTS supports state-of-the-art 3-second voice cloning and description-based control, allowing both the creation of entirely novel voices and fine-grained manipulation over the output speech. Trained on over 5 million hours of speech data spanning 10 languages, Qwen3-TTS adopts a dual-track LM architecture for real-time synthesis, coupled with two speech tokenizers: 1) Qwen-TTS-Tokenizer-25Hz is a single-codebook codec emphasizing semantic content, which offers seamlessly integration with Qwen-Audio and enables streaming waveform reconstruction via a block-wise DiT. 2) Qwen-TTS-Tokenizer-12Hz achieves extreme bitrate reduction and ultra-low-latency streaming, enabling immediate first-packet emission ($97\,\mathrm{ms}$) through its 12.5 Hz, 16-layer multi-codebook design and a lightweight causal ConvNet. Extensive experiments indicate state-of-the-art performance across diverse objective and subjective benchmark (e.g., TTS multilingual test set, InstructTTSEval, and our long speech test set). To facilitate community research and development, we release both tokenizers and models under the Apache 2.0 license.

</details>

### [Prosody-Guided Harmonic Attention for Phase-Coherent Neural Vocoding in the Complex Spectrum](2601.14472.md)
**Mohammed Salah Al-Radhi et.al.** · 2026-01-20

### [Quantifying Speaker Embedding Phonological Rule Interactions in Accented Speech Synthesis](2601.14417.md)
**Thanathai Lertpetchpun et.al.** · 2026-01-20

### [Synthetic Singers: A Review of Deep-Learning-based Singing Voice Synthesis Approaches](2601.13910.md)
**Changhao Pan et.al.** · 2026-01-20

### [Habibi: Laying the Open-Source Foundation of Unified-Dialectal Arabic Speech Synthesis](2601.13802.md)
**Yushen Chen, Junzhe Liu, Yujie Tu, Zhikang Niu et al.** · 2026-01-20

<details>
<summary>Abstract</summary>

Arabic spans over 30 spoken varieties, yet no open-source text-to-speech system unifies them. Key barriers include substantial cross-dialect lexical and phonological divergence, scarce synthesis-grade data, and the absence of a standardized multi-dialect evaluation benchmark. We present Habibi, a unified-dialectal Arabic TTS framework that addresses all three. Through a multi-step curation pipeline, we repurpose open-source ASR corpora into TTS training data covering 12+ regional dialects. A linguistically-informed curriculum learning strategy - progressing from Modern Standard Arabic to dialectal data - enables robust zero-shot synthesis without text diacritization. We further release the first standardized multi-dialect Arabic TTS benchmark, comprising over 11,000 utterances across 7 dialect subsets with manually verified transcripts. On this benchmark, our unified model matches or surpasses per-dialect specialized models. Both automatic metrics and human evaluations confirm that Habibi is highly competitive with ElevenLabs' Eleven v3 (alpha) in intelligibility, speaker similarity, and naturalness. Extensive ablations (~8,000 H100 GPU hours, 30+ configurations) validate each design choice. We open-source all checkpoints, training and inference code, and benchmark data - the first such release for multi-dialect Arabic TTS - at https://SWivid.github.io/Habibi/ .

</details>

### [GOMPSNR: Reflourish the Signal-to-Noise Ratio Metric for Audio Generation Tasks](2601.13758.md)
**Lingling Dai, Andong Li, Cheng Chi, Yifan Liang et al.** · 2026-01-20

<details>
<summary>Abstract</summary>

In the field of audio generation, signal-to-noise ratio (SNR) has long served as an objective metric for evaluating audio quality. Nevertheless, recent studies have shown that SNR and its variants are not always highly correlated with human perception, prompting us to raise the questions: Why does SNR fail in measuring audio quality? And how to improve its reliability as an objective metric? In this paper, we identify the inadequate measurement of phase distance as a pivotal factor and propose to reformulate SNR with specially designed phase-distance terms, yielding an improved metric named GOMPSNR. We further extend the newly proposed formulation to derive two novel categories of loss function, corresponding to magnitude-guided phase refinement and joint magnitude-phase optimization, respectively. Besides, extensive experiments are conducted for an optimal combination of different loss functions. Experimental results on advanced neural vocoders demonstrate that our proposed GOMPSNR exhibits more reliable error measurement than SNR. Meanwhile, our proposed loss functions yield substantial improvements in model performance, and our wellchosen combination of different loss functions further optimizes the overall model capability.

</details>

### [Stream-Voice-Anon: Enhancing Utility of Real-Time Speaker Anonymization via Neural Audio Codec and Language Models](2601.13948.md)
**Nikita Kuzmin, Songting Liu, Kong Aik Lee, Eng Siong Chng** · 2026-01-20

<details>
<summary>Abstract</summary>

Protecting speaker identity is crucial for online voice applications, yet streaming speaker anonymization (SA) remains underexplored. Recent research has demonstrated that neural audio codec (NAC) provides superior speaker feature disentanglement and linguistic fidelity. NAC can also be used with causal language models (LM) to enhance linguistic fidelity and prompt control for streaming tasks. However, existing NAC-based online LM systems are designed for voice conversion (VC) rather than anonymization, lacking the techniques required for privacy protection. Building on these advances, we present Stream-Voice-Anon, which adapts modern causal LM-based NAC architectures specifically for streaming SA by integrating anonymization techniques. Our anonymization approach incorporates pseudo-speaker representation sampling, a speaker embedding mixing and diverse prompt selection strategies for LM conditioning that leverage the disentanglement properties of quantized content codes to prevent speaker information leakage. Additionally, we compare dynamic and fixed delay configurations to explore latency-privacy trade-offs in real-time scenarios. Under the VoicePrivacy 2024 Challenge protocol, Stream-Voice-Anon achieves substantial improvements in intelligibility (up to 46% relative WER reduction) and emotion preservation (up to 28% UAR relative) compared to the previous state-of-the-art streaming method DarkStream while maintaining comparable latency (180ms vs 200ms) and privacy protection against lazy-informed attackers, though showing 15% relative degradation against semi-informed attackers.

</details>

### [S$^2$Voice: Style-Aware Autoregressive Modeling with Enhanced Conditioning for Singing Style Conversion](2601.13629.md)
**Ziqian Wang, Xianjun Xia, Chuanzeng Huang, Lei Xie** · 2026-01-20

<details>
<summary>Abstract</summary>

We present S$^2$Voice, the winning system of the Singing Voice Conversion Challenge (SVCC) 2025 for both the in-domain and zero-shot singing style conversion tracks. Built on the strong two-stage Vevo baseline, S$^2$Voice advances style control and robustness through several contributions. First, we integrate style embeddings into the autoregressive large language model (AR LLM) via a FiLM-style layer-norm conditioning and a style-aware cross-attention for enhanced fine-grained style modeling. Second, we introduce a global speaker embedding into the flow-matching transformer to improve timbre similarity. Third, we curate a large, high-quality singing corpus via an automated pipeline for web harvesting, vocal separation, and transcript refinement. Finally, we employ a multi-stage training strategy combining supervised fine-tuning (SFT) and direct preference optimization (DPO). Subjective listening tests confirm our system's superior performance: leading in style similarity and singer similarity for Task 1, and across naturalness, style similarity, and singer similarity for Task 2. Ablation studies demonstrate the effectiveness of our contributions in enhancing style fidelity, timbre preservation, and generalization. Audio samples are available~\footnote{https://honee-w.github.io/SVC-Challenge-Demo/}.

</details>

### [Lombard Speech Synthesis for Any Voice with Controllable Style Embeddings](2601.12966.md)
**Seymanur Akti et.al.** · 2026-01-19

### [Synthesizing the Virtual Advocate: A Multi-Persona Speech Generation Framework for Diverse Linguistic Jurisdictions in Indic Languages](2602.11172.md)
**Aniket Deroy** · 2026-01-19

<details>
<summary>Abstract</summary>

Legal advocacy requires a unique combination of authoritative tone, rhythmic pausing for emphasis, and emotional intelligence. This study investigates the performance of the Gemini 2.5 Flash TTS and Gemini 2.5 Pro TTS models in generating synthetic courtroom speeches across five Indic languages: Tamil, Telugu, Bengali, Hindi, and Gujarati. We propose a prompting framework that utilizes Gemini 2.5s native support for 5 languages and its context-aware pacing to produce distinct advocate personas. The evolution of Large Language Models (LLMs) has shifted the focus of TexttoSpeech (TTS) technology from basic intelligibility to context-aware, expressive synthesis. In the legal domain, synthetic speech must convey authority and a specific professional persona a task that becomes significantly more complex in the linguistically diverse landscape of India. The models exhibit a "monotone authority," excelling at procedural information delivery but struggling with the dynamic vocal modulation and emotive gravitas required for persuasive advocacy. Performance dips in Bengali and Gujarati further highlight phonological frontiers for future refinement. This research underscores the readiness of multilingual TTS for procedural legal tasks while identifying the remaining challenges in replicating the persuasive artistry of human legal discourse. The code is available at-https://github.com/naturenurtureelite/Synthesizing-the-Virtual-Advocate/tree/main

</details>

### [A Unified Neural Codec Language Model for Selective Editable Text to Speech Generation](2601.12480.md)
**Hanchen Pei et.al.** · 2026-01-18

### [ParaMETA: Towards Learning Disentangled Paralinguistic Speaking Styles Representations from Speech](2601.12289.md)
**Haowei Lou, Hye-young Paik, Wen Hu, Lina Yao** · 2026-01-18

<details>
<summary>Abstract</summary>

Learning representative embeddings for different types of speaking styles, such as emotion, age, and gender, is critical for both recognition tasks (e.g., cognitive computing and human-computer interaction) and generative tasks (e.g., style-controllable speech generation). In this work, we introduce ParaMETA, a unified and flexible framework for learning and controlling speaking styles directly from speech. Unlike existing methods that rely on single-task models or cross-modal alignment, ParaMETA learns disentangled, task-specific embeddings by projecting speech into dedicated subspaces for each type of style. This design reduces inter-task interference, mitigates negative transfer, and allows a single model to handle multiple paralinguistic tasks such as emotion, gender, age, and language classification. Beyond recognition, ParaMETA enables fine-grained style control in Text-To-Speech (TTS) generative models. It supports both speech- and text-based prompting and allows users to modify one speaking styles while preserving others. Extensive experiments demonstrate that ParaMETA outperforms strong baselines in classification accuracy and generates more natural and expressive speech, while maintaining a lightweight and efficient model suitable for real-world applications.

</details>

### [Confidence-based Filtering for Speech Dataset Curation with Generative Speech Enhancement Using Discrete Tokens](2601.12254.md)
**Kazuki Yamauchi, Masato Murata, Shogo Seki** · 2026-01-18

<details>
<summary>Abstract</summary>

Generative speech enhancement (GSE) models show great promise in producing high-quality clean speech from noisy inputs, enabling applications such as curating noisy text-to-speech (TTS) datasets into high-quality ones. However, GSE models are prone to hallucination errors, such as phoneme omissions and speaker inconsistency, which conventional error filtering based on non-intrusive speech quality metrics often fails to detect. To address this issue, we propose a non-intrusive method for filtering hallucination errors from discrete token-based GSE models. Our method leverages the log-probabilities of generated tokens as confidence scores to detect potential errors. Experimental results show that the confidence scores strongly correlate with a suite of intrusive SE metrics, and that our method effectively identifies hallucination errors missed by conventional filtering methods. Furthermore, we demonstrate the practical utility of our method: curating an in-the-wild TTS dataset with our confidence-based filtering improves the performance of subsequently trained TTS models.

</details>

### [FlashLabs Chroma 1.0: A Real-Time End-to-End Spoken Dialogue Model with Personalized Voice Cloning](2601.11141.md)
**Tanyu Chen et.al.** · 2026-01-16

### [ES4R: Speech Encoding Based on Prepositive Affective Modeling for Empathetic Response Generation](2601.16225.md)
**Zhuoyue Gao, Xiaohui Wang, Xiaocui Yang, Wen Zhang et al.** · 2026-01-16

<details>
<summary>Abstract</summary>

Empathetic speech dialogue requires not only understanding linguistic content but also perceiving rich paralinguistic information such as prosody, tone, and emotional intensity for affective understandings. Existing speech-to-speech large language models either rely on ASR transcription or use encoders to extract latent representations, often weakening affective information and contextual coherence in multi-turn dialogues. To address this, we propose \textbf{ES4R}, a framework for speech-based empathetic response generation. Our core innovation lies in explicitly modeling structured affective context before speech encoding, rather than relying on implicit learning by the encoder or explicit emotion supervision. Specifically, we introduce a dual-level attention mechanism to capture turn-level affective states and dialogue-level affective dynamics. The resulting affective representations are then integrated with textual semantics through speech-guided cross-modal attention to generate empathetic responses. For speech output, we employ energy-based strategy selection and style fusion to achieve empathetic speech synthesis. ES4R consistently outperforms strong baselines in both automatic and human evaluations and remains robust across different LLM backbones.

</details>

### [F-Actor: Controllable Conversational Behaviour in Full-Duplex Models](2601.11329.md)
**Maike Züfle, Ondrej Klejch, Nicholas Sanders, Jan Niehues et al.** · 2026-01-16

<details>
<summary>Abstract</summary>

Spoken conversational systems require more than accurate speech generation to have human-like conversations: to feel natural and engaging, they must produce conversational behaviour that adapts dynamically to the context. Current spoken conversational systems, however, rarely allow such customization, limiting their naturalness and usability. In this work, we present the first open, instruction-following full-duplex conversational speech model that can be trained efficiently under typical academic resource constraints. By keeping the audio encoder frozen and finetuning only the language model, our model requires just 2,000 hours of data, without relying on large-scale pretraining or multi-stage optimization. The model can follow explicit instructions to control speaker voice, conversation topic, conversational behaviour (e.g., backchanneling and interruptions), and dialogue initiation. We propose a single-stage training protocol and systematically analyze design choices. Both the model and training code is released to enable reproducible research on controllable full-duplex speech systems.

</details>

### [VoiceSculptor: Your Voice, Designed By You](2601.10629.md)
**Jingbin Hu, Huakang Chen, Linhan Ma, Dake Guo et al.** · 2026-01-15

<details>
<summary>Abstract</summary>

Despite rapid progress in text-to-speech (TTS), open-source systems still lack truly instruction-following, fine-grained control over core speech attributes (e.g., pitch, speaking rate, age, emotion, and style). We present VoiceSculptor, an open-source unified system that bridges this gap by integrating instruction-based voice design and high-fidelity voice cloning in a single framework. It generates controllable speaker timbre directly from natural-language descriptions, supports iterative refinement via Retrieval-Augmented Generation (RAG), and provides attribute-level edits across multiple dimensions. The designed voice is then rendered into a prompt waveform and fed into a cloning model to enable high-fidelity timbre transfer for downstream speech synthesis. VoiceSculptor achieves open-source state-of-the-art (SOTA) on InstructTTSEval-Zh, and is fully open-sourced, including code and pretrained models, to advance reproducible instruction-controlled TTS research.

</details>

### [PersonaPlex: Voice and Role Control for Full Duplex Conversational Speech Models](2602.06053.md)
**Rajarshi Roy, Jonathan Raiman, Sang-gil Lee, Teodor-Dumitru Ene et al.** · 2026-01-14

<details>
<summary>Abstract</summary>

Recent advances in duplex speech models have enabled natural, low-latency speech-to-speech interactions. However, existing models are restricted to a fixed role and voice, limiting their ability to support structured, role-driven real-world applications and personalized interactions. In this work, we introduce PersonaPlex, a duplex conversational speech model that incorporates hybrid system prompts, combining role conditioning with text prompts and voice cloning with speech samples. PersonaPlex is trained on a large-scale synthetic dataset of paired prompts and user-agent conversations, generated with open-source large language models (LLM) and text-to-speech (TTS) models. To evaluate role conditioning in real-world settings, we extend the Full-Duplex-Bench benchmark beyond a single assistant role to multi-role customer service scenarios. Experiments show that PersonaPlex achieves strong role-conditioned behavior, voice-conditioned speech, and natural conversational responsiveness, surpassing state-of-the-art duplex speech models and hybrid large language model-based speech systems in role adherence, speaker similarity, latency, and naturalness.

</details>

### [DSA-Tokenizer: Disentangled Semantic-Acoustic Tokenization via Flow Matching-based Hierarchical Fusion](2601.09239.md)
**Hanlin Zhang, Daxin Tan, Dehua Tao, Xiao Chen et al.** · 2026-01-14

<details>
<summary>Abstract</summary>

Speech tokenizers are a key building block of fully discrete Speech LLMs. Existing tokenizers either prioritize semantic encoding, fuse semantic content with acoustic style inseparably, or achieve incomplete semantic-acoustic disentanglement. To achieve better disentanglement, we propose DSA-Tokenizer, which explicitly disentangles speech into discrete semantic and acoustic tokens via distinct optimization constraints. Specifically, semantic tokens are supervised by ASR to capture linguistic content, while acoustic tokens focus on mel-spectrograms restoration to encode style. We further introduce a hierarchical Flow Matching decoder and a joint reconstruction-context inpainting training strategy, allowing the model to support both high-fidelity reconstruction and cross-utterance voice clone. To speed up inference, we distill the dit decoder to 4-step inference and improve synthesis quality with GAN fine-tuning. Experiments demonstrate that DSA-Tokenizer provides strong semantic-acoustic disentanglement, reliable controllable voice cloning, and efficient high-fidelity generation with low WER/CER. Moreover, our results suggest that disentangled tokenization provides a more effective interface for downstream large-model speech generation. Audio samples are avaialble at https://anonymous.4open.science/w/DSA_Tokenizer_demo/

</details>

### [Decoding Order Matters in Autoregressive Speech Synthesis](2601.08450.md)
**Minghui Zhao et.al.** · 2026-01-13

### [Detecting Mental Manipulation in Speech via Synthetic Multi-Speaker Dialogue](2601.08342.md)
**Run Chen, Wen Liang, Ziwei Gong, Lin Ai et al.** · 2026-01-13

<details>
<summary>Abstract</summary>

Mental manipulation, the strategic use of language to covertly influence or exploit others, is a newly emerging task in computational social reasoning. Prior work has focused exclusively on textual conversations, overlooking how manipulative tactics manifest in speech. We present the first study of mental manipulation detection in spoken dialogues, introducing a synthetic multi-speaker benchmark SPEECHMENTALMANIP that augments a text-based dataset with high-quality, voice-consistent Text-to-Speech rendered audio. Using few-shot large audio-language models and human annotation, we evaluate how modality affects detection accuracy and perception. Our results reveal that models exhibit high specificity but markedly lower recall on speech compared to text, suggesting sensitivity to missing acoustic or prosodic cues in training. Human raters show similar uncertainty in the audio setting, underscoring the inherent ambiguity of manipulative speech. Together, these findings highlight the need for modality-aware evaluation and safety alignment in multimodal dialogue systems.

</details>

### [ESDD2: Environment-Aware Speech and Sound Deepfake Detection Challenge Evaluation Plan](2601.07303.md)
**Xueping Zhang, Han Yin, Yang Xiao, Lin Zhang et al.** · 2026-01-12

<details>
<summary>Abstract</summary>

Audio recorded in real-world environments often contains a mixture of foreground speech and background environmental sounds. With rapid advances in text-to-speech, voice conversion, and other generation models, either component can now be modified independently. Such component-level manipulations are harder to detect, as the remaining unaltered component can mislead the systems designed for whole deepfake audio, and they often sound more natural to human listeners. To address this gap, we have proposed CompSpoofV2 dataset and a separation-enhanced joint learning framework. CompSpoofV2 is a large-scale curated dataset designed for component-level audio anti-spoofing, which contains over 250k audio samples, with a total duration of approximately 283 hours. Based on the CompSpoofV2 and the separation-enhanced joint learning framework, we launch the Environment-Aware Speech and Sound Deepfake Detection Challenge (ESDD2), focusing on component-level spoofing, where both speech and environmental sounds may be manipulated or synthesized, creating a more challenging and realistic detection scenario. The challenge will be held in conjunction with the IEEE International Conference on Multimedia and Expo 2026 (ICME 2026).

</details>

### [Bridging Attribution and Open-Set Detection using Graph-Augmented Instance Learning in Synthetic Speech](2601.07064.md)
**Mohd Mujtaba Akhtar, Girish, Farhan Sheth, Muskaan Singh** · 2026-01-11

<details>
<summary>Abstract</summary>

We propose a unified framework for not only attributing synthetic speech to its source but also for detecting speech generated by synthesizers that were not encountered during training. This requires methods that move beyond simple detection to support both detailed forensic analysis and open-set generalization. To address this, we introduce SIGNAL, a hybrid framework that combines speech foundation models (SFMs) with graph-based modeling and open-set-aware inference. Our framework integrates Graph Neural Networks (GNNs) and a k-Nearest Neighbor (KNN) classifier, allowing it to capture meaningful relationships between utterances and recognize speech that doesn`t belong to any known generator. It constructs a query-conditioned graph over generator class prototypes, enabling the GNN to reason over relationships among candidate generators, while the KNN branch supports open-set detection via confidence-based thresholding. We evaluate SIGNAL using the DiffSSD dataset, which offers a diverse mix of real speech and synthetic audio from both open-source and commercial diffusion-based TTS systems. To further assess generalization, we also test on the SingFake benchmark. Our results show that SIGNAL consistently improves performance across both tasks, with Mamba-based embeddings delivering especially strong results. To the best of our knowledge, this is the first study to unify graph-based learning and open-set detection for tracing synthetic speech back to its origin.

</details>

### [Lightweight Resolution-Aware Audio Deepfake Detection via Cross-Scale Attention and Consistency Learning](2601.06560.md)
**K. A. Shahriar** · 2026-01-10

<details>
<summary>Abstract</summary>

Audio deepfake detection has become increasingly challenging due to rapid advances in speech synthesis and voice conversion technologies, particularly under channel distortions, replay attacks, and real-world recording conditions. This paper proposes a resolution-aware audio deepfake detection framework that explicitly models and aligns multi-resolution spectral representations through cross-scale attention and consistency learning. Unlike conventional single-resolution or implicit feature-fusion approaches, the proposed method enforces agreement across complementary time--frequency scales. The proposed framework is evaluated on three representative benchmarks: ASVspoof 2019 (LA and PA), the Fake-or-Real (FoR) dataset, and the In-the-Wild Audio Deepfake dataset under a speaker-disjoint protocol. The method achieves near-perfect performance on ASVspoof LA (EER 0.16%), strong robustness on ASVspoof PA (EER 5.09%), FoR rerecorded audio (EER 4.54%), and in-the-wild deepfakes (AUC 0.98, EER 4.81%), significantly outperforming single-resolution and non-attention baselines under challenging conditions. The proposed model remains lightweight and efficient, requiring only 159k parameters and less than 1~GFLOP per inference, making it suitable for practical deployment. Comprehensive ablation studies confirm the critical contributions of cross-scale attention and consistency learning, while gradient-based interpretability analysis reveals that the model learns resolution-consistent and semantically meaningful spectral cues across diverse spoofing conditions. These results demonstrate that explicit cross-resolution modeling provides a principled, robust, and scalable foundation for next-generation audio deepfake detection systems.

</details>

### [A Framework for Low-Latency, LLM-driven Multimodal Interaction on the Pepper Robot](2603.21013.md)
**Erich Studerus, Vivienne Jia Zhong, Stephan Vonschallen** · 2026-01-09

<details>
<summary>Abstract</summary>

Despite recent advances in integrating Large Language Models (LLMs) into social robotics, two weaknesses persist. First, existing implementations on platforms like Pepper often rely on cascaded Speech-to-Text (STT)->LLM->Text-to-Speech (TTS) pipelines, resulting in high latency and the loss of paralinguistic information. Second, most implementations fail to fully leverage the LLM's capabilities for multimodal perception and agentic control. We present an open-source Android framework for the Pepper robot that addresses these limitations through two key innovations. First, we integrate end-to-end Speech-to-Speech (S2S) models to achieve low-latency interaction while preserving paralinguistic cues and enabling adaptive intonation. Second, we implement extensive Function Calling capabilities that elevate the LLM to an agentic planner, orchestrating robot actions (navigation, gaze control, tablet interaction) and integrating diverse multimodal feedback (vision, touch, system state). The framework runs on the robot's tablet but can also be built to run on regular Android smartphones or tablets, decoupling development from robot hardware. This work provides the HRI community with a practical, extensible platform for exploring advanced LLM-driven embodied interaction.

</details>

### [CosyEdit: Unlocking End-to-End Speech Editing Capability from Zero-Shot Text-to-Speech Models](2601.05329.md)
**Junyang Chen et.al.** · 2026-01-08

### [FlexiVoice: Enabling Flexible Style Control in Zero-Shot TTS with Natural Language Instructions](2601.04656.md)
**Dekun Chen et.al.** · 2026-01-08

### [ReStyle-TTS: Relative and Continuous Style Control for Zero-Shot Speech Synthesis](2601.03632.md)
**Haitao Li et.al.** · 2026-01-07

### [IndexTTS 2.5 Technical Report](2601.03888.md)
**Yunpei Li, Xun Zhou, Jinchao Wang, Lu Wang et al.** · 2026-01-07

<details>
<summary>Abstract</summary>

In prior work, we introduced IndexTTS 2, a zero-shot neural text-to-speech foundation model comprising two core components: a transformer-based Text-to-Semantic (T2S) module and a non-autoregressive Semantic-to-Mel (S2M) module, which together enable faithful emotion replication and establish the first autoregressive duration-controllable generative paradigm. Building upon this, we present IndexTTS 2.5, which significantly enhances multilingual coverage, inference speed, and overall synthesis quality through four key improvements: 1) Semantic Codec Compression: we reduce the semantic codec frame rate from 50 Hz to 25 Hz, halving sequence length and substantially lowering both training and inference costs; 2) Architectural Upgrade: we replace the U-DiT-based backbone of the S2M module with a more efficient Zipformer-based modeling architecture, achieving notable parameter reduction and faster mel-spectrogram generation; 3) Multilingual Extension: We propose three explicit cross-lingual modeling strategies, boundary-aware alignment, token-level concatenation, and instruction-guided generation, establishing practical design principles for zero-shot multilingual emotional TTS that supports Chinese, English, Japanese, and Spanish, and enables robust emotion transfer even without target-language emotional training data; 4) Reinforcement Learning Optimization: we apply GRPO in post-training of the T2S module, improving pronunciation accuracy and natrualness. Experiments show that IndexTTS 2.5 not only supports broader language coverage but also replicates emotional prosody in unseen languages under the same zero-shot setting. IndexTTS 2.5 achieves a 2.28 times improvement in RTF while maintaining comparable WER and speaker similarity to IndexTTS 2.

</details>

### [Domain Adaptation of the Pyannote Diarization Pipeline for Conversational Indonesian Audio](2601.03684.md)
**Muhammad Daffa'i Rafi Prasetyo, Ramadhan Andika Putra, Zaidan Naufal Ilmi, Kurniawati Azizah** · 2026-01-07

<details>
<summary>Abstract</summary>

This study presents a domain adaptation approach for speaker diarization targeting conversational Indonesian audio. We address the challenge of adapting an English-centric diarization pipeline to a low-resource language by employing synthetic data generation using neural Text-to-Speech technology. Experiments were conducted with varying training configurations, a small dataset (171 samples) and a large dataset containing 25 hours of synthetic speech. Results demonstrate that the baseline \texttt{pyannote/segmentation-3.0} model, trained on the AMI Corpus, achieves a Diarization Error Rate (DER) of 53.47\% when applied zero-shot to Indonesian. Domain adaptation significantly improves performance, with the small dataset models reducing DER to 34.31\% (1 epoch) and 34.81\% (2 epochs). The model trained on the 25-hour dataset achieves the best performance with a DER of 29.24\%, representing a 13.68\% absolute improvement over the baseline while maintaining 99.06\% Recall and 87.14\% F1-Score.

</details>

### [Lightweight and perceptually-guided voice conversion for electro-laryngeal speech](2601.03892.md)
**Benedikt Mayrhofer, Franz Pernkopf, Philipp Aichinger, Martin Hagmüller** · 2026-01-07

<details>
<summary>Abstract</summary>

Electro-laryngeal (EL) speech is characterized by constant pitch, limited prosody, and mechanical noise, reducing naturalness and intelligibility. We propose a lightweight adaptation of the state-of-the-art StreamVC framework to this setting by removing pitch and energy modules and combining self-supervised pretraining with supervised fine-tuning on parallel EL and healthy (HE) speech data, guided by perceptual and intelligibility losses. Objective and subjective evaluations across different loss configurations confirm their influence: the best model variant, based on WavLM features and human-feedback predictions (+WavLM+HF), drastically reduces character error rate (CER) of EL inputs, raises naturalness mean opinion score (nMOS) from 1.1 to 3.3, and consistently narrows the gap to HE ground-truth speech in all evaluated metrics. These findings demonstrate the feasibility of adapting lightweight voice conversion architectures to EL voice rehabilitation while also identifying prosody generation and intelligibility improvements as the main remaining bottlenecks.

</details>

### [SpeakerSleuth: Can Large Audio-Language Models Judge Speaker Consistency across Multi-turn Dialogues?](2601.04029.md)
**Jonggeun Lee, Junseong Pyo, Gyuhyeon Seo, Yohan Jo** · 2026-01-07

<details>
<summary>Abstract</summary>

Large Audio-Language Models (LALMs) as judges have emerged as a prominent approach for evaluating speech generation quality, yet their ability to assess speaker consistency across multi-turn dialogues remains unexplored. We present \textbf{SpeakerSleuth}, a benchmark evaluating whether LALMs can reliably judge speaker consistency across multi-turn dialogues through three tasks reflecting real-world requirements. We construct 1,818 human-verified evaluation instances across four diverse datasets spanning synthetic and real speech, with controlled acoustic difficulty. Evaluating twelve widely-used LALMs, we find that models struggle to reliably detect acoustic inconsistencies. For instance, given audio samples of the same speaker's turns, some models overpredict inconsistency, whereas others are overly lenient. Models further struggle to identify the exact turns that are problematic. When other interlocutors' turns are provided as textual context, performance degrades dramatically as models prioritize textual coherence over acoustic cues, failing to detect even obvious gender switches for a speaker. On the other hand, models perform substantially better in comparing and ranking acoustic variants, demonstrating inherent acoustic discrimination capabilities. These findings expose a significant bias in LALMs: they tend to prioritize text over acoustics, revealing fundamental modality imbalances that need to be addressed to build reliable audio-language judges. Our code and data are available at https://github.com/holi-lab/SpeakerSleuth.

</details>

### [Segment-Aware Conditioning for Training-Free Intra-Utterance Emotion and Duration Control in Text-to-Speech](2601.03170.md)
**Qifan Liang et.al.** · 2026-01-06

### [Tigrinya Number Verbalization: Rules, Algorithm, and Implementation](2601.03403.md)
**Fitsum Gaim, Issayas Tesfamariam** · 2026-01-06

<details>
<summary>Abstract</summary>

We present a systematic formalization of Tigrinya cardinal and ordinal number verbalization, addressing a gap in computational resources for the language. This work documents the canonical rules governing the expression of numerical values in spoken Tigrinya, including the conjunction system, scale words, and special cases for dates, times, and currency. We provide a formal algorithm for number-to-word conversion and release an open-source implementation. Evaluation of frontier large language models (LLMs) reveals significant gaps in their ability to accurately verbalize Tigrinya numbers, underscoring the need for explicit rule documentation. This work serves language modeling, speech synthesis, and accessibility applications targeting Tigrinya-speaking communities.

</details>

### [XLSR-MamBo: Scaling the Hybrid Mamba-Attention Backbone for Audio Deepfake Detection](2601.02944.md)
**Kwok-Ho Ng, Tingting Song, Yongdong Wu, Zhihua Xia** · 2026-01-06

<details>
<summary>Abstract</summary>

Advanced speech synthesis technologies have enabled highly realistic speech generation, posing security risks that motivate research into audio deepfake detection (ADD). While state space models (SSMs) offer linear complexity, pure causal SSMs architectures often struggle with the content-based retrieval required to capture global frequency-domain artifacts. To address this, we explore the scaling properties of hybrid architectures by proposing XLSR-MamBo, a modular framework integrating an XLSR front-end with synergistic Mamba-Attention backbones. We systematically evaluate four topological designs using advanced SSM variants, Mamba, Mamba2, Hydra, and Gated DeltaNet. Experimental results demonstrate that the MamBo-3-Hydra-N3 configuration achieves competitive performance compared to other state-of-the-art systems on the ASVspoof 2021 LA, DF, and In-the-Wild benchmarks. This performance benefits from Hydra's native bidirectional modeling, which captures holistic temporal dependencies more efficiently than the heuristic dual-branch strategies employed in prior works. Furthermore, evaluations on the DFADD dataset demonstrate robust generalization to unseen diffusion- and flow-matching-based synthesis methods. Crucially, our analysis reveals that scaling backbone depth effectively mitigates the performance variance and instability observed in shallower models. These results demonstrate the hybrid framework's ability to capture artifacts in spoofed speech signals, providing an effective method for ADD.

</details>

### [Vclip: Face-based Speaker Generation by Face-voice Association Learning](2601.02753.md)
**Yao Shi, Yunfei Xu, Hongbin Suo, Yulong Wan et al.** · 2026-01-06

<details>
<summary>Abstract</summary>

This paper discusses the task of face-based speech synthesis, a kind of personalized speech synthesis where the synthesized voices are constrained to perceptually match with a reference face image. Due to the lack of TTS-quality audio-visual corpora, previous approaches suffer from either low synthesis quality or domain mismatch induced by a knowledge transfer scheme. This paper proposes a new approach called Vclip that utilizes the facial-semantic knowledge of the CLIP encoder on noisy audio-visual data to learn the association between face and voice efficiently, achieving 89.63% cross-modal verification AUC score on Voxceleb testset. The proposed method then uses a retrieval-based strategy, combined with GMM-based speaker generation module for a downstream TTS system, to produce probable target speakers given reference images. Experimental results demonstrate that the proposed Vclip system in conjunction with the retrieval step can bridge the gap between face and voice features for face-based speech synthesis. And using the feedback information distilled from downstream TTS helps to synthesize voices that match closely with reference faces. Demos available at sos1sos2sixteen.github.io/vclip.

</details>

### [Towards Prosodically Informed Mizo TTS without Explicit Tone Markings](2601.02073.md)
**Abhijit Mohanta, Remruatpuii, Priyankoo Sarmah, Rohit Sinha et al.** · 2026-01-05

<details>
<summary>Abstract</summary>

This paper reports on the development of a text-to-speech (TTS) system for Mizo, a low-resource, tonal, and Tibeto-Burman language spoken primarily in the Indian state of Mizoram. The TTS was built with only 5.18 hours of data; however, in terms of subjective and objective evaluations, the outputs were considered perceptually acceptable and intelligible. A baseline model using Tacotron2 was built, and then, with the same data, another TTS model was built with VITS. In both subjective and objective evaluations, the VITS model outperformed the Tacotron2 model. In terms of tone synthesis, the VITS model showed significantly lower tone errors than the Tacotron2 model. The paper demonstrates that a non-autoregressive, end-to-end framework can achieve synthesis of acceptable perceptual quality and intelligibility.

</details>

### [MM-Sonate: Multimodal Controllable Audio-Video Generation with Zero-Shot Voice Cloning](2601.01568.md)
**Chunyu Qiang et.al.** · 2026-01-04

### [OV-InstructTTS: Towards Open-Vocabulary Instruct Text-to-Speech](2601.01459.md)
**Yong Ren, Jiangyan Yi, Jianhua Tao, Haiyang Sun et al.** · 2026-01-04

<details>
<summary>Abstract</summary>

Instruct Text-to-Speech (InstructTTS) leverages natural language descriptions as style prompts to guide speech synthesis. However, existing InstructTTS methods mainly rely on a direct combination of audio-related labels or their diverse rephrasings, making it difficult to handle flexible, high-level instructions. Such rigid control is insufficient for users such as content creators who wish to steer generation with descriptive instructions. To address these constraints, we introduce OV-InstructTTS, a new paradigm for open-vocabulary InstructTTS. We propose a comprehensive solution comprising a newly curated dataset, OV-Speech, and a novel reasoning-driven framework. The OV-Speech dataset pairs speech with open-vocabulary instructions, each augmented with a reasoning process that connects high-level instructions to acoustic features. The reasoning-driven framework infers emotional, acoustic, and paralinguistic information from open-vocabulary instructions before synthesizing speech. Evaluations show that this reasoning-driven approach significantly improves instruction-following fidelity and speech expressiveness. We believe this work can inspire the next user-friendly InstructTTS systems with stronger generalization and real-world applicability. The dataset and demos are publicly available on our project page.

</details>

### [LEMAS: Large A 150K-Hour Large-scale Extensible Multilingual Audio Suite with Generative Speech Models](2601.04233.md)
**Zhiyuan Zhao, Lijian Lin, Ye Zhu, Kai Xie et al.** · 2026-01-04

<details>
<summary>Abstract</summary>

We present the LEMAS-Dataset, which, to our knowledge, is currently the largest open-source multilingual speech corpus with word-level timestamps. Covering over 150,000 hours across 10 major languages, LEMAS-Dataset is constructed via a efficient data processing pipeline that ensures high-quality data and annotations. To validate the effectiveness of LEMAS-Dataset across diverse generative paradigms, we train two benchmark models with distinct architectures and task specializations on this dataset. LEMAS-TTS, built upon a non-autoregressive flow-matching framework, leverages the dataset's massive scale and linguistic diversity to achieve robust zero-shot multilingual synthesis. Our proposed accent-adversarial training and CTC loss mitigate cross-lingual accent issues, enhancing synthesis stability. Complementarily, LEMAS-Edit employs an autoregressive decoder-only architecture that formulates speech editing as a masked token infilling task. By exploiting precise word-level alignments to construct training masks and adopting adaptive decoding strategies, it achieves seamless, smooth-boundary speech editing with natural transitions. Experimental results demonstrate that models trained on LEMAS-Dataset deliver high-quality synthesis and editing performance, confirming the dataset's quality. We envision that this richly timestamp-annotated, fine-grained multilingual corpus will drive future advances in prompt-based speech generation systems.

</details>

### [Latent Flow Matching for Expressive Singing Voice Synthesis](2601.00217.md)
**Minhyeok Yun et.al.** · 2026-01-01

### [DepFlow: Disentangled Speech Generation to Mitigate Semantic Bias in Depression Detection](2601.00303.md)
**Yuxin Li, Xiangyu Zhang, Yifei Li, Zhiwei Guo et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Speech is a scalable and non-invasive biomarker for early mental health screening. However, widely used depression datasets like DAIC-WOZ exhibit strong coupling between linguistic sentiment and diagnostic labels, encouraging models to learn semantic shortcuts. As a result, model robustness may be compromised in real-world scenarios, such as Camouflaged Depression, where individuals maintain socially positive or neutral language despite underlying depressive states. To mitigate this semantic bias, we propose DepFlow, a three-stage depression-conditioned text-to-speech framework. First, a Depression Acoustic Encoder learns speaker- and content-invariant depression embeddings through adversarial training, achieving effective disentanglement while preserving depression discriminability (ROC-AUC: 0.693). Second, a flow-matching TTS model with FiLM modulation injects these embeddings into synthesis, enabling control over depressive severity while preserving content and speaker identity. Third, a prototype-based severity mapping mechanism provides smooth and interpretable manipulation across the depression continuum. Using DepFlow, we construct a Camouflage Depression-oriented Augmentation (CDoA) dataset that pairs depressed acoustic patterns with positive/neutral content from a sentiment-stratified text bank, creating acoustic-semantic mismatches underrepresented in natural data. Evaluated across three depression detection architectures, CDoA improves macro-F1 by 9%, 12%, and 5%, respectively, consistently outperforming conventional augmentation strategies in depression Detection. Beyond enhancing robustness, DepFlow provides a controllable synthesis platform for conversational systems and simulation-based evaluation, where real clinical data remains limited by ethical and coverage constraints.

</details>

### [Cro-MTVITS: An end-to-end cross-lingual speech synthesis model for Mandarin and multi-dialect Tibetan based on VITS](s2:6f240f3695e1b19b114a665d53e8723f41651c2e.md)
**Weizhao Zhang, Mengjuan Wang, Junzhi Li, Hongwu Yang** · 2026-01-01

### [Controllable End-to-End Neural Source–Filter Vocoder With Low-Dimensional Speech Parameters and Data Augmentation](s2:ebd7d6df8a917b7716e0ca404c47872751a23682.md)
**Sumiharu Kobayashi, Tetsuo Kosaka, Takashi Nose** · 2026-01-01

<details>
<summary>Abstract</summary>

Recent neural vocoders synthesize speech waveforms from high-dimensional spectrograms, making it difficult to control individual speech parameters such as F0 and formants. Neural formant synthesis (NF) has been proposed to control speech parameters by converting low-dimensional parameters into spectrograms that serve as input to a neural vocoder. However, the quality of the synthesized speech degrades because the generated spectral time series differs from the natural speech used to train the neural vocoder. In this study, we first propose E2E-NF and E2E-NF+ to improve the conventional NF vocoder by refining the training process with an end-to-end manner. Furthermore, to enhance the synthesis quality of E2E-NF+ during speech-parameter control, we propose E2E-SiFi-NF, which incorporates a source–filter structure, and we also investigate data augmentation. Experimental evaluations show that the source-filter-based method synthesizes speech with quality equal to or better than that of conventional approaches when controlling speech parameters. Additionally, data augmentation improved the robustness of F0 and formant controls. A demonstration of the proposed methods is available online at https://misumisumi.github.io/myprojects/end-to-end-neural-formant-synthesis

</details>

