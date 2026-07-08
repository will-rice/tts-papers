# 2025

720 papers in this year.

### [Defense Against Synthetic Speech: Real-Time Detection of RVC Voice Conversion Attacks](2601.04227.md)
**Prajwal Chinchmalatpure, Suyash Chinchmalatpure, Siddharth Chavan** · 2025-12-31

<details>
<summary>Abstract</summary>

Generative audio technologies now enable highly realistic voice cloning and real-time voice conversion, increasing the risk of impersonation, fraud, and misinformation in communication channels such as phone and video calls. This study investigates real-time detection of AI-generated speech produced using Retrieval-based Voice Conversion (RVC), evaluated on the DEEP-VOICE dataset, which includes authentic and voice-converted speech samples from multiple well-known speakers. To simulate realistic conditions, deepfake generation is applied to isolated vocal components, followed by the reintroduction of background ambiance to suppress trivial artifacts and emphasize conversion-specific cues. We frame detection as a streaming classification task by dividing audio into one-second segments, extracting time-frequency and cepstral features, and training supervised machine learning models to classify each segment as real or voice-converted. The proposed system enables low-latency inference, supporting both segment-level decisions and call-level aggregation. Experimental results show that short-window acoustic features can reliably capture discriminative patterns associated with RVC speech, even in noisy backgrounds. These findings demonstrate the feasibility of practical, real-time deepfake speech detection and underscore the importance of evaluating under realistic audio mixing conditions for robust deployment.

</details>

### [AI4Reading: Chinese Audiobook Interpretation System Based on Multi-Agent Collaboration](2512.23300.md)
**Minjiang Huang, Jipeng Qiang, Yi Zhu, Chaowei Zhang et al.** · 2025-12-29

<details>
<summary>Abstract</summary>

Audiobook interpretations are attracting increasing attention, as they provide accessible and in-depth analyses of books that offer readers practical insights and intellectual inspiration. However, their manual creation process remains time-consuming and resource-intensive. To address this challenge, we propose AI4Reading, a multi-agent collaboration system leveraging large language models (LLMs) and speech synthesis technology to generate podcast, like audiobook interpretations. The system is designed to meet three key objectives: accurate content preservation, enhanced comprehensibility, and a logical narrative structure. To achieve these goals, we develop a framework composed of 11 specialized agents,including topic analysts, case analysts, editors, a narrator, and proofreaders that work in concert to explore themes, extract real world cases, refine content organization, and synthesize natural spoken language. By comparing expert interpretations with our system's output, the results show that although AI4Reading still has a gap in speech generation quality, the generated interpretative scripts are simpler and more accurate.

</details>

### [MiMo-Audio: Audio Language Models are Few-Shot Learners](2512.23808.md)
**Xiaomi LLM-Core Team, :, Dong Zhang, Gang Wang et al.** · 2025-12-29

<details>
<summary>Abstract</summary>

Existing audio language models typically rely on task-specific fine-tuning to accomplish particular audio tasks. In contrast, humans are able to generalize to new audio tasks with only a few examples or simple instructions. GPT-3 has shown that scaling next-token prediction pretraining enables strong generalization capabilities in text, and we believe this paradigm is equally applicable to the audio domain. By scaling MiMo-Audio's pretraining data to over one hundred million of hours, we observe the emergence of few-shot learning capabilities across a diverse set of audio tasks. We develop a systematic evaluation of these capabilities and find that MiMo-Audio-7B-Base achieves SOTA performance on both speech intelligence and audio understanding benchmarks among open-source models. Beyond standard metrics, MiMo-Audio-7B-Base generalizes to tasks absent from its training data, such as voice conversion, style transfer, and speech editing. MiMo-Audio-7B-Base also demonstrates powerful speech continuation capabilities, capable of generating highly realistic talk shows, recitations, livestreaming and debates. At the post-training stage, we curate a diverse instruction-tuning corpus and introduce thinking mechanisms into both audio understanding and generation. MiMo-Audio-7B-Instruct achieves open-source SOTA on audio understanding benchmarks (MMSU, MMAU, MMAR, MMAU-Pro), spoken dialogue benchmarks (Big Bench Audio, MultiChallenge Audio) and instruct-TTS evaluations, approaching or surpassing closed-source models. Model checkpoints and full evaluation suite are available at https://github.com/XiaomiMiMo/MiMo-Audio.

</details>

### [ManchuTTS: Towards High-Quality Manchu Speech Synthesis via Flow Matching and Hierarchical Text Representation](2512.22491.md)
**Suhua Wang et.al.** · 2025-12-27

### [Zero-Shot to Zero-Lies: Detecting Bengali Deepfake Audio through Transfer Learning](2512.21702.md)
**Most. Sharmin Sultana Samu, Md. Rakibul Islam, Md. Zahid Hossain, Md. Kamrozzaman Bhuiyan et al.** · 2025-12-25

<details>
<summary>Abstract</summary>

The rapid growth of speech synthesis and voice conversion systems has made deepfake audio a major security concern. Bengali deepfake detection remains largely unexplored. In this work, we study automatic detection of Bengali audio deepfakes using the BanglaFake dataset. We evaluate zeroshot inference with several pretrained models. These include Wav2Vec2-XLSR-53, Whisper, PANNsCNN14, WavLM and Audio Spectrogram Transformer. Zero-shot results show limited detection ability. The best model, Wav2Vec2-XLSR-53, achieves 53.80% accuracy, 56.60% AUC and 46.20% EER. We then f ine-tune multiple architectures for Bengali deepfake detection. These include Wav2Vec2-Base, LCNN, LCNN-Attention, ResNet18, ViT-B16 and CNN-BiLSTM. Fine-tuned models show strong performance gains. ResNet18 achieves the highest accuracy of 79.17%, F1 score of 79.12%, AUC of 84.37% and EER of 24.35%. Experimental results confirm that fine-tuning significantly improves performance over zero-shot inference. This study provides the first systematic benchmark of Bengali deepfake audio detection. It highlights the effectiveness of f ine-tuned deep learning models for this low-resource language.

</details>

### [Fun-Audio-Chat Technical Report](2512.20156.md)
**Tongyi Fun Team, Qian Chen, Luyao Cheng, Chong Deng et al.** · 2025-12-23

<details>
<summary>Abstract</summary>

Recent advancements in joint speech-text models show great potential for seamless voice interactions. However, existing models face critical challenges: temporal resolution mismatch between speech tokens (25Hz) and text tokens (~3Hz) dilutes semantic information, incurs high computational costs, and causes catastrophic forgetting of text LLM knowledge. We introduce Fun-Audio-Chat, a Large Audio Language Model addressing these limitations via two innovations from our previous work DrVoice. First, Dual-Resolution Speech Representations (DRSR): the Shared LLM processes audio at efficient 5Hz (via token grouping), while the Speech Refined Head generates high-quality tokens at 25Hz, balancing efficiency (~50% GPU reduction) and quality. Second, Core-Cocktail Training, a two-stage fine-tuning with intermediate merging that mitigates catastrophic forgetting. We then apply Multi-Task DPO Training to enhance robustness, audio understanding, instruction-following and voice empathy. This multi-stage post-training enables Fun-Audio-Chat to retain text LLM knowledge while gaining powerful audio understanding, reasoning, and generation. Unlike recent LALMs requiring large-scale audio-text pre-training, Fun-Audio-Chat leverages pre-trained models and extensive post-training. Fun-Audio-Chat 8B and MoE 30B-A3B achieve competitive performance on Speech-to-Text and Speech-to-Speech tasks, ranking top among similar-scale models on Spoken QA benchmarks. They also achieve competitive to superior performance on Audio Understanding, Speech Function Calling, Instruction-Following and Voice Empathy. We develop Fun-Audio-Chat-Duplex, a full-duplex variant with strong performance on Spoken QA and full-duplex interactions. We open-source Fun-Audio-Chat-8B with training and inference code, and provide an interactive demo, at https://github.com/FunAudioLLM/Fun-Audio-Chat .

</details>

### [Aliasing-Free Neural Audio Synthesis](2512.20211.md)
**Yicheng Gu, Junan Zhang, Chaoren Wang, Jerry Li et al.** · 2025-12-23

<details>
<summary>Abstract</summary>

In neural audio synthesis, neural vocoders and codecs are models that reconstruct waveforms from acoustic and latent representations, which are essential to the resulting audio quality. While current models are capable of generating perceptually natural speech, they still struggle with high-fidelity music and singing voice synthesis, as severe aliasing artifacts are introduced by non-linear activation functions and upsampling layers in existing architectures. Although various anti-aliasing techniques have been proposed in digital signal processing, their integration into neural vocoders and codecs remains under-explored. This paper incorporates differentiable anti-aliasing techniques into the activation and upsampling modules to bridge this gap, and thus presents Pupu-Vocoder and Pupu-Codec. We build a test signal benchmark to evaluate the anti-aliased modules, and validate our proposed models on speech, singing voice, music, and audio. Experimental results show that Pupu-Vocoder and Pupu-Codec outperform existing systems on singing voice, music, and audio, while achieving comparable performance on speech. Demos, codes, and checkpoints are available at: VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/.

</details>

### [QuarkAudio Technical Report](2512.20151.md)
**Chengwei Liu, Haoyin Yan, Shaofei Xue, Xiaotao Liang et al.** · 2025-12-23

<details>
<summary>Abstract</summary>

Many existing audio processing and generation models rely on task-specific architectures, resulting in fragmented development efforts and limited extensibility. It is therefore promising to design a unified framework capable of handling multiple tasks, while providing robust instruction and audio understanding and high-quality audio generation. This requires a compatible paradigm design, a powerful backbone, and a high-fidelity audio reconstruction module. To meet these requirements, this technical report introduces QuarkAudio, a decoder-only autoregressive (AR) LM-based generative framework that unifies multiple tasks. The framework includes a unified discrete audio tokenizer, H-Codec, which incorporates self-supervised learning (SSL) representations into the tokenization and reconstruction process. We further propose several improvements to H-Codec, such as a dynamic frame-rate mechanism and extending the audio sampling rate to 48 kHz. QuarkAudio unifies tasks by using task-specific conditional information as the conditioning sequence of the decoder-only LM, and predicting discrete target audio tokens in an AR manner. The framework supports a wide range of audio processing and generation tasks, including speech restoration (SR), target speaker extraction (TSE), speech separation (SS), voice conversion (VC), and language-queried audio source separation (LASS). In addition, we extend downstream tasks to universal free-form audio editing guided by natural language instructions (including speech semantic editing and audio event editing). Experimental results show that H-Codec achieves high-quality audio reconstruction with a low frame rate, improving both the efficiency and performance of downstream audio generation, and that QuarkAudio delivers competitive or comparable performance to state-of-the-art task-specific or multi-task systems across multiple tasks.

</details>

### [TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation](2512.20296.md)
**Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak, Joon Son Chung et al.** · 2025-12-23

<details>
<summary>Abstract</summary>

The objective of this paper is to jointly synthesize interactive videos and conversational speech from text and reference images. With the ultimate goal of building human-like conversational systems, recent studies have explored talking or listening head generation as well as conversational speech generation. However, these works are typically studied in isolation, overlooking the multimodal nature of human conversation, which involves tightly coupled audio-visual interactions. In this paper, we introduce TAVID, a unified framework that generates both interactive faces and conversational speech in a synchronized manner. TAVID integrates face and speech generation pipelines through two cross-modal mappers (i.e., a motion mapper and a speaker mapper), which enable bidirectional exchange of complementary information between the audio and visual modalities. We evaluate our system across four dimensions: talking face realism, listening head responsiveness, dyadic interaction fluency, and speech quality. Extensive experiments demonstrate the effectiveness of our approach across all these aspects.

</details>

### [JoyVoice: Long-Context Conditioning for Anthropomorphic Multi-Speaker Conversational Synthesis](2512.19090.md)
**Fan Yu, Tao Wang, You Wu, Lin Zhu et al.** · 2025-12-22

<details>
<summary>Abstract</summary>

Large speech generation models are evolving from single-speaker, short sentence synthesis to multi-speaker, long conversation geneartion. Current long-form speech generation models are predominately constrained to dyadic, turn-based interactions. To address this, we introduce JoyVoice, a novel anthropomorphic foundation model designed for flexible, boundary-free synthesis of up to eight speakers. Unlike conventional cascaded systems, JoyVoice employs a unified E2E-Transformer-DiT architecture that utilizes autoregressive hidden representations directly for diffusion inputs, enabling holistic end-to-end optimization. We further propose a MM-Tokenizer operating at a low bitrate of 12.5 Hz, which integrates multitask semantic and MMSE losses to effectively model both semantic and acoustic information. Additionally, the model incorporates robust text front-end processing via large-scale data perturbation. Experiments show that JoyVoice achieves state-of-the-art results in multilingual generation (Chinese, English, Japanese, Korean) and zero-shot voice cloning. JoyVoice achieves top-tier results on both the Seed-TTS-Eval Benchmark and multi-speaker long-form conversational voice cloning tasks, demonstrating superior audio quality and generalization. It achieves significant improvements in prosodic continuity for long-form speech, rhythm richness in multi-speaker conversations, paralinguistic naturalness, besides superior intelligibility. We encourage readers to listen to the demo at https://jea-speech.github.io/JoyVoice

</details>

### [Smark: A Watermark for Text-to-Speech Diffusion Models via Discrete Wavelet Transform](2512.18791.md)
**Yichuan Zhang et.al.** · 2025-12-21

### [Task Vector in TTS: Toward Emotionally Expressive Dialectal Speech Synthesis](2512.18699.md)
**Pengchao Feng, Yao Xiao, Ziyang Ma, Zhikang Niu et al.** · 2025-12-21

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) have yielded remarkable improvements in naturalness and intelligibility. Building on these achievements, research has increasingly shifted toward enhancing the expressiveness of generated speech, such as dialectal and emotional TTS. However, cross-style synthesis combining both dialect and emotion remains challenging and largely unexplored, mainly due to the scarcity of dialectal data with emotional labels. To address this, we propose Hierarchical Expressive Vector (HE-Vector), a two-stage method for Emotional Dialectal TTS. In the first stage, we construct different task vectors to model dialectal and emotional styles independently, and then enhance single-style synthesis by adjusting their weights, a method we refer to as Expressive Vector (E-Vector). For the second stage, we hierarchically integrate these vectors to achieve controllable emotionally expressive dialect synthesis without requiring jointly labeled data, corresponding to Hierarchical Expressive Vector (HE-Vector). Experimental results demonstrate that HE-Vectors achieve superior performance in dialect synthesis, and promising results in synthesizing emotionally expressive dialectal speech in a zero-shot setting.

</details>

### [Training Text-to-Speech Model with Purely Synthetic Data: Feasibility, Sensitivity, and Generalization Capability](2512.17356.md)
**Tingxiao Zhou et.al.** · 2025-12-19

### [Robust TTS Training via Self-Purifying Flow Matching for the WildSpoof 2026 TTS Track](2512.17293.md)
**June Young Yi et.al.** · 2025-12-19

### [DisCo-Speech: Controllable Zero-Shot Speech Generation with A Disentangled Speech Codec](2512.13251.md)
**Tao Li et.al.** · 2025-12-18

### [Pseudo-Cepstrum: Pitch Modification for Mel-Based Neural Vocoders](2512.16519.md)
**Nikolaos Ellinas, Alexandra Vioni, Panos Kakoulidis, Georgios Vamvoukakis et al.** · 2025-12-18

<details>
<summary>Abstract</summary>

This paper introduces a cepstrum-based pitch modification method that can be applied to any mel-spectrogram representation. As a result, this method is compatible with any mel-based vocoder without requiring any additional training or changes to the model. This is achieved by directly modifying the cepstrum feature space in order to shift the harmonic structure to the desired target. The spectrogram magnitude is computed via the pseudo-inverse mel transform, then converted to the cepstrum by applying DCT. In this domain, the cepstral peak is shifted without having to estimate its position and the modified mel is recomputed by applying IDCT and mel-filterbank. These pitch-shifted mel-spectrogram features can be converted to speech with any compatible vocoder. The proposed method is validated experimentally with objective and subjective metrics on various state-of-the-art neural vocoders as well as in comparison with traditional pitch modification methods.

</details>

### [Adapting Speech Language Model to Singing Voice Synthesis](2512.14657.md)
**Yiwen Zhao et.al.** · 2025-12-16

### [Robust Training of Singing Voice Synthesis Using Prior and Posterior Uncertainty](2512.14653.md)
**Yiwen Zhao et.al.** · 2025-12-16

### [GLM-TTS Technical Report](2512.14291.md)
**Jiayan Cui, Zhihan Yang, Naihan Li, Jiankun Tian et al.** · 2025-12-16

<details>
<summary>Abstract</summary>

This work proposes GLM-TTS, a production-level TTS system designed for efficiency, controllability, and high-fidelity speech generation. GLM-TTS follows a two-stage architecture, consisting of a text-to-token autoregressive model and a token-to-waveform diffusion model. With only 100k hours of training data, GLM-TTS achieves state-of-the-art performance on multiple open-source benchmarks. To meet production requirements, GLM-TTS improves speech quality through an optimized speech tokenizer with fundamental frequency constraints and a GRPO-based multi-reward reinforcement learning framework that jointly optimizes pronunciation, speaker similarity, and expressive prosody. In parallel, the system enables efficient and controllable deployment via parameter-efficient LoRA-based voice customization and a hybrid phoneme-text input scheme that provides precise pronunciation control. Our code is available at https://github.com/zai-org/GLM-TTS. Real-time speech synthesis demos are provided via Z.ai (audio.z.ai), the Zhipu Qingyan app/web (chatglm.cn).

</details>

### [A comparative study of generative models for child voice conversion](2512.12129.md)
**Protima Nomo Sudro, Anton Ragni, Thomas Hain** · 2025-12-13

<details>
<summary>Abstract</summary>

Generative models are a popular choice for adult-to-adult voice conversion (VC) because of their efficient way of modelling unlabelled data. To this point their usefulness in producing children speech and in particular adult to child VC has not been investigated. For adult to child VC, four generative models are compared: diffusion model, flow based model, variational autoencoders, and generative adversarial network. Results show that although converted speech outputs produce by those models appear plausible, they exhibit insufficient similarity with the target speaker characteristics. We introduce an efficient frequency warping technique that can be applied to the output of models, and which shows significant reduction of the mismatch between adult and child. The output of all the models are evaluated using both objective and subjective measures. In particular we compare specific speaker pairing using a unique corpus collected for dubbing of children speech.

</details>

### [F5-TTS-RO: Extending F5-TTS to Romanian TTS via Lightweight Input Adaptation](2512.12297.md)
**Radu-Gabriel Chivereanu, Tiberiu Boros** · 2025-12-13

<details>
<summary>Abstract</summary>

This work introduces a lightweight input-level adapter for the F5-TTS model that enables Romanian Language support. To preserve the existing capabilities of the model (voice cloning, English and Chinese support), we keep the original weights frozen, append a sub-network to the model and train it as an extension for the textual embedding matrix of the text encoder. For simplicity, we rely on ConvNeXt module implemented in F5-TTS to also model the co-dependencies between the new character-level embeddings. The module serves as a ``soft`` letter-to-sound layer, converting Romanian text into a continuous representation that the F5-TTS model uses to produce naturally sounding Romanian utterances. We evaluate the model with a pool of 20 human listeners across three tasks: (a) audio similarity between reference and generated speech, (b) pronunciation and naturalness and (c) Romanian-English code-switching. The results indicate that our approach maintains voice cloning capabilities and enables, to a certain extent, code-switching within the same utterance; however, residual English accent characteristics remain. We open-source our code and provide example audio samples at https://github.com/racai-ro/Ro-F5TTS.

</details>

### [DMP-TTS: Disentangled multi-modal Prompting for Controllable Text-to-Speech with Chained Guidance](2512.09504.md)
**Kang Yin, Chunyu Qiang, Sirui Zhao, Xiaopeng Wang et al.** · 2025-12-10

<details>
<summary>Abstract</summary>

Controllable text-to-speech (TTS) systems face significant challenges in achieving independent manipulation of speaker timbre and speaking style, often suffering from entanglement between these attributes. We present DMP-TTS, a latent Diffusion Transformer (DiT) framework with explicit disentanglement and multi-modal prompting. A CLAP-based style encoder (Style-CLAP) aligns cues from reference audio and descriptive text in a shared space and is trained with contrastive learning plus multi-task supervision on style attributes. For fine-grained control during inference, we introduce chained classifier-free guidance (cCFG) trained with hierarchical condition dropout, enabling independent adjustment of content, timbre, and style guidance strengths. Additionally, we employ Representation Alignment (REPA) to distill acoustic-semantic features from a pretrained Whisper model into intermediate DiT representations, stabilizing training and accelerating convergence. Experiments show that DMP-TTS delivers stronger style controllability than open-source baselines while maintaining competitive intelligibility and naturalness. Code and demos will be available at https://y61329697.github.io/DMP-TTS/.

</details>

### [Beyond Unified Models: A Service-Oriented Approach to Low Latency, Context Aware Phonemization for Real Time TTS](2512.08006.md)
**Mahta Fetrat, Donya Navabi, Zahra Dehghanian, Morteza Abolghasemi et al.** · 2025-12-08

<details>
<summary>Abstract</summary>

Lightweight, real-time text-to-speech systems are crucial for accessibility. However, the most efficient TTS models often rely on lightweight phonemizers that struggle with context-dependent challenges. In contrast, more advanced phonemizers with a deeper linguistic understanding typically incur high computational costs, which prevents real-time performance. This paper examines the trade-off between phonemization quality and inference speed in G2P-aided TTS systems, introducing a practical framework to bridge this gap. We propose lightweight strategies for context-aware phonemization and a service-oriented TTS architecture that executes these modules as independent services. This design decouples heavy context-aware components from the core TTS engine, effectively breaking the latency barrier and enabling real-time use of high-quality phonemization models. Experimental results confirm that the proposed system improves pronunciation soundness and linguistic accuracy while maintaining real-time responsiveness, making it well-suited for offline and end-device TTS applications.

</details>

### [Degrading Voice: A Comprehensive Overview of Robust Voice Conversion Through Input Manipulation](2512.06304.md)
**Xining Song, Zhihua Wei, Rui Wang, Haixiao Hu et al.** · 2025-12-06

<details>
<summary>Abstract</summary>

Identity, accent, style, and emotions are essential components of human speech. Voice conversion (VC) techniques process the speech signals of two input speakers and other modalities of auxiliary information such as prompts and emotion tags. It changes para-linguistic features from one to another, while maintaining linguistic contents. Recently, VC models have made rapid advancements in both generation quality and personalization capabilities. These developments have attracted considerable attention for diverse applications, including privacy preservation, voice-print reproduction for the deceased, and dysarthric speech recovery. However, these models only learn non-robust features due to the clean training data. Subsequently, it results in unsatisfactory performances when dealing with degraded input speech in real-world scenarios, including additional noise, reverberation, adversarial attacks, or even minor perturbation. Hence, it demands robust deployments, especially in real-world settings. Although latest researches attempt to find potential attacks and countermeasures for VC systems, there remains a significant gap in the comprehensive understanding of how robust the VC model is under input manipulation. here also raises many questions: For instance, to what extent do different forms of input degradation attacks alter the expected output of VC models? Is there potential for optimizing these attack and defense strategies? To answer these questions, we classify existing attack and defense methods from the perspective of input manipulation and evaluate the impact of degraded input speech across four dimensions, including intelligibility, naturalness, timbre similarity, and subjective perception. Finally, we outline open issues and future directions.

</details>

### [Simulating Life Paths with Digital Twins: AI-Generated Future Selves Influence Decision-Making and Expand Human Choice](2512.05397.md)
**Rachel Poonsiriwong, Chayapatr Archiwaranguprok, Constanze Albrecht, Peggy Yin et al.** · 2025-12-05

<details>
<summary>Abstract</summary>

Major life transitions demand high-stakes decisions, yet people often struggle to imagine how their future selves will live with the consequences. To support this limited capacity for mental time travel, we introduce AI-enabled digital twins that have ``lived through'' simulated life scenarios. Rather than predicting optimal outcomes, these simulations extend prospective cognition by making alternative futures vivid enough to support deliberation without assuming which path is best. We evaluate this idea in a randomized controlled study (N=192) using multimodal synthesis - facial age progression, voice cloning, and large language model dialogue - to create personalized avatars representing participants 30 years forward. Young adults 18 to 28 years old described pending binary decisions and were assigned to guided imagination or one of four avatar conditions: single-option, balanced dual-option, or expanded three-option with a system-generated novel alternative. Results showed asymmetric effects: single-sided avatars increased shifts toward the presented option, while balanced presentation produced movement toward both. Introducing a system-generated third option increased adoption of this new alternative compared to control, suggesting that AI-generated future selves can expand choice by surfacing paths that might otherwise go unnoticed. Participants rated evaluative reasoning and eudaimonic meaning-making as more important than emotional or visual vividness. Perceived persuasiveness and baseline agency predicted decision change. These findings advance understanding of AI-mediated episodic prospection and raise questions about autonomy in AI-augmented decisions.

</details>

### [YingMusic-Singer: Zero-shot Singing Voice Synthesis and Editing with Annotation-free Melody Guidance](2512.04779.md)
**Junjie Zheng et.al.** · 2025-12-04

### [M3-TTS: Multi-modal DiT Alignment & Mel-latent for Zero-shot High-fidelity Speech Synthesis](2512.04720.md)
**Xiaopeng Wang et.al.** · 2025-12-04

### [RRPO: Robust Reward Policy Optimization for LLM-based Emotional TTS](2512.04552.md)
**Cong Wang et.al.** · 2025-12-04

### [YingMusic-SVC: Real-World Robust Zero-Shot Singing Voice Conversion with Flow-GRPO and Singing-Specific Inductive Biases](2512.04793.md)
**Gongyu Chen, Xiaoyu Zhang, Zhenqiang Weng, Junjie Zheng et al.** · 2025-12-04

<details>
<summary>Abstract</summary>

Singing voice conversion (SVC) aims to render the target singer's timbre while preserving melody and lyrics. However, existing zero-shot SVC systems remain fragile in real songs due to harmony interference, F0 errors, and the lack of inductive biases for singing. We propose YingMusic-SVC, a robust zero-shot framework that unifies continuous pre-training, robust supervised fine-tuning, and Flow-GRPO reinforcement learning. Our model introduces a singing-trained RVC timbre shifter for timbre-content disentanglement, an F0-aware timbre adaptor for dynamic vocal expression, and an energy-balanced rectified flow matching loss to enhance high-frequency fidelity. Experiments on a graded multi-track benchmark show that YingMusic-SVC achieves consistent improvements over strong open-source baselines in timbre similarity, intelligibility, and perceptual naturalness, especially under accompanied and harmony-contaminated conditions, demonstrating its effectiveness for real-world SVC deployment.

</details>

### [Generative Multi-modal Feedback for Singing Voice Synthesis Evaluation](2512.02523.md)
**Xueyan Li et.al.** · 2025-12-02

### [Cross-Lingual Interleaving for Speech Language Models](2512.01865.md)
**Adel Moumen et.al.** · 2025-12-01

### [Arabic TTS with FastPitch: Reproducible Baselines, Adversarial Training, and Oversmoothing Analysis](2512.00937.md)
**Lars Nippert et.al.** · 2025-11-30

### [NeuroSense: A Computational AI Model for Continuous Psychological State Prediction](s2:1ab486621719cfbe74831d99f2676e757423aa22.md)
**Pushkar Sharma** · 2025-11-30

<details>
<summary>Abstract</summary>

An emerging interdisciplinary challenge in artificial intelligence, computational psychology, and neuroscience is the ongoing evaluation of human psychological states. Conventional mental-state assessments rely on clinical interviews and episodic, subjective self-reports, which are not flexible in real time. This paper presents NeuroSense, a computational AI framework that uses multimodal signals such as EEG, heart-rate variability (HRV), speech prosody, facial micro-expressions, linguistic sentiment, and contextual behavioral features to predict dynamic psychological states. A multimodal fusion pipeline comprising a Spatio-Temporal EEG Encoder, Physiological Dynamics Model, Affective Facial Transformer, Prosodic Emotional Encoder, and NLP-based Cognitive Load Estimator is integrated by NeuroSense. Continuous prediction using a hybrid deep learning framework is made possible by the convergence of these signals into a Unified Psychological State Vector (UPSV). High potential for real-time affect estimation, stress prediction, cognitive load modeling, and mental fatigue detection is demonstrated by experiments conducted on benchmark datasets. Future studies will investigate neuro-adaptive intelligent interfaces, wearable IoT integration, and federated learning.

</details>

### [STCTS: Generative Semantic Compression for Ultra-Low Bitrate Speech via Explicit Text-Prosody-Timbre Decomposition](2512.00451.md)
**Siyu Wang et.al.** · 2025-11-29

### [PURE Codec: Progressive Unfolding of Residual Entropy for Speech Codec Learning](2511.22687.md)
**Jiatong Shi et.al.** · 2025-11-27

### [GLA-Grad++: An Improved Griffin-Lim Guided Diffusion Model for Speech Synthesis](2511.22293.md)
**Teysir Baoueb et.al.** · 2025-11-27

### [VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task](2511.22229.md)
**Yuyue Wang et.al.** · 2025-11-27

### [Multi-Reward GRPO for Stable and Prosodic Single-Codebook TTS LLMs at Scale](2511.21270.md)
**Yicheng Zhong et.al.** · 2025-11-26

### [RosettaSpeech: Zero-Shot Speech-to-Speech Translation from Monolingual Data](2511.20974.md)
**Zhisheng Zheng et.al.** · 2025-11-26

### [CartoonSing: Unifying Human and Nonhuman Timbres in Singing Generation](2511.21045.md)
**Jionghao Han, Jiatong Shi, Zhuoyan Tao, Yuxun Tang et al.** · 2025-11-26

<details>
<summary>Abstract</summary>

Singing voice synthesis (SVS) and singing voice conversion (SVC) have achieved remarkable progress in generating natural-sounding human singing. However, existing systems are restricted to human timbres and have limited ability to synthesize voices outside the human range, which are increasingly demanded in creative applications such as video games, movies, and virtual characters. We introduce Non-Human Singing Generation (NHSG), covering non-human singing voice synthesis (NHSVS) and non-human singing voice conversion (NHSVC), as a novel machine learning task for generating musically coherent singing with non-human timbral characteristics. NHSG is particularly challenging due to the scarcity of non-human singing data, the lack of symbolic alignment, and the wide timbral gap between human and non-human voices. To address these challenges, we propose CartoonSing, a unified framework that integrates singing voice synthesis and conversion while bridging human and non-human singing generation. CartoonSing employs a two-stage pipeline: a score representation encoder trained with annotated human singing and a timbre-aware vocoder that reconstructs waveforms for both human and non-human audio. Experiments demonstrate that CartoonSing successfully generates non-human singing voices, generalizes to novel timbres, and extends conventional SVS and SVC toward creative, non-human singing generation.

</details>

### [Continual Audio Deepfake Detection via Universal Adversarial Perturbation](2511.19974.md)
**Wangjie Li, Lin Li, Qingyang Hong** · 2025-11-25

<details>
<summary>Abstract</summary>

The rapid advancement of speech synthesis and voice conversion technologies has raised significant security concerns in multimedia forensics. Although current detection models demonstrate impressive performance, they struggle to maintain effectiveness against constantly evolving deepfake attacks. Additionally, continually fine-tuning these models using historical training data incurs substantial computational and storage costs. To address these limitations, we propose a novel framework that incorporates Universal Adversarial Perturbation (UAP) into audio deepfake detection, enabling models to retain knowledge of historical spoofing distribution without direct access to past data. Our method integrates UAP seamlessly with pre-trained self-supervised audio models during fine-tuning. Extensive experiments validate the effectiveness of our approach, showcasing its potential as an efficient solution for continual learning in audio deepfake detection.

</details>

### [Evaluating Objective Speech Quality Metrics for Neural Audio Codecs](2511.19734.md)
**Luca A. Lanzendörfer et.al.** · 2025-11-24

### [SyncVoice: Towards Video Dubbing with Vision-Augmented Pretrained TTS Model](2512.05126.md)
**Kaidi Wang, Yi He, Wenhao Guan, Weijie Wu et al.** · 2025-11-23

<details>
<summary>Abstract</summary>

Video dubbing aims to generate high-fidelity speech that is precisely temporally aligned with the visual content. Existing methods still suffer from limitations in speech naturalness and audio-visual synchronization, and are limited to monolingual settings. To address these challenges, we propose SyncVoice, a vision-augmented video dubbing framework built upon a pretrained text-to-speech (TTS) model. By fine-tuning the TTS model on audio-visual data, we achieve strong audiovisual consistency. We propose a Dual Speaker Encoder to effectively mitigate inter-language interference in cross-lingual speech synthesis and explore the application of video dubbing in video translation scenarios. Experimental results show that SyncVoice achieves high-fidelity speech generation with strong synchronization performance, demonstrating its potential in video dubbing tasks.

</details>

### [InstructAudio: Unified speech and music generation with natural language instruction](2511.18487.md)
**Chunyu Qiang, Kang Yin, Xiaopeng Wang, Yuzhe Liang et al.** · 2025-11-23

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) and text-to-music (TTM) models face significant limitations in instruction-based control. TTS systems usually depend on reference audio for timbre, offer only limited text-level attribute control, and rarely support dialogue generation. TTM systems are constrained by input conditioning requirements that depend on expert knowledge annotations. The high heterogeneity of these input control conditions makes them difficult to joint modeling with speech synthesis. Despite sharing common acoustic modeling characteristics, these two tasks have long been developed independently, leaving open the challenge of achieving unified modeling through natural language instructions. We introduce InstructAudio, a unified framework that enables instruction-based (natural language descriptions) control of acoustic attributes including timbre (gender, age), paralinguistic (emotion, style, accent), and musical (genre, instrument, rhythm, atmosphere). It supports expressive speech, music, and dialogue generation in English and Chinese. The model employs joint and single diffusion transformer layers with a standardized instruction-phoneme input format, trained on 50K hours of speech and 20K hours of music data, enabling multi-task learning and cross-modal alignment. Fig. 1 visualizes performance comparisons with mainstream TTS and TTM models, demonstrating that InstructAudio achieves optimal results on most metrics. To our best knowledge, InstructAudio represents the first instruction-controlled framework unifying speech and music generation. Audio samples are available at: https://qiangchunyu.github.io/InstructAudio/

</details>

### [Codec2Vec: Self-Supervised Speech Representation Learning Using Neural Speech Codecs](2511.16639.md)
**Wei-Cheng Tseng et.al.** · 2025-11-20

### [SceneGuard: Training-Time Voice Protection with Scene-Consistent Audible Background Noise](2511.16114.md)
**Rui Sang, Yuxuan Liu** · 2025-11-20

<details>
<summary>Abstract</summary>

Voice cloning technology poses significant privacy threats by enabling unauthorized speech synthesis from limited audio samples. Existing defenses based on imperceptible adversarial perturbations are vulnerable to common audio preprocessing such as denoising and compression. We propose SceneGuard, a training-time voice protection method that applies scene-consistent audible background noise to speech recordings. Unlike imperceptible perturbations, SceneGuard leverages naturally occurring acoustic scenes (e.g., airport, street, park) to create protective noise that is contextually appropriate and robust to countermeasures. We evaluate SceneGuard on text-to-speech training attacks, demonstrating 5.5% speaker similarity degradation with extremely high statistical significance (p < 10^{-15}, Cohen's d = 2.18) while preserving 98.6% speech intelligibility (STOI = 0.986). Robustness evaluation shows that SceneGuard maintains or enhances protection under five common countermeasures including MP3 compression, spectral subtraction, lowpass filtering, and downsampling. Our results suggest that audible, scene-consistent noise provides a more robust alternative to imperceptible perturbations for training-time voice protection. The source code are available at: https://github.com/richael-sang/SceneGuard.

</details>

### [PresentCoach: Dual-Agent Presentation Coaching through Exemplars and Interactive Feedback](2511.15253.md)
**Sirui Chen, Jinsong Zhou, Xinli Xu, Xiaoyu Yang et al.** · 2025-11-19

<details>
<summary>Abstract</summary>

Effective presentation skills are essential in education, professional communication, and public speaking, yet learners often lack access to high-quality exemplars or personalized coaching. Existing AI tools typically provide isolated functionalities such as speech scoring or script generation without integrating reference modeling and interactive feedback into a cohesive learning experience. We introduce a dual-agent system that supports presentation practice through two complementary roles: the Ideal Presentation Agent and the Coach Agent. The Ideal Presentation Agent converts user-provided slides into model presentation videos by combining slide processing, visual-language analysis, narration script generation, personalized voice synthesis, and synchronized video assembly. The Coach Agent then evaluates user-recorded presentations against these exemplars, conducting multimodal speech analysis and delivering structured feedback in an Observation-Impact-Suggestion (OIS) format. To enhance the authenticity of the learning experience, the Coach Agent incorporates an Audience Agent, which simulates the perspective of a human listener and provides humanized feedback reflecting audience reactions and engagement. Together, these agents form a closed loop of observation, practice, and feedback. Implemented on a robust backend with multi-model integration, voice cloning, and error handling mechanisms, the system demonstrates how AI-driven agents can provide engaging, human-centered, and scalable support for presentation skill development in both educational and professional contexts.

</details>

### [Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech](2511.14824.md)
**Nam-Gyu Kim** · 2025-11-18

<details>
<summary>Abstract</summary>

Recent advances in expressive text-to-speech (TTS) have introduced diverse methods based on style embedding extracted from reference speech. However, synthesizing high-quality expressive speech remains challenging. We propose SpotlightTTS, which exclusively emphasizes style via voiced-aware style extraction and style direction adjustment. Voiced-aware style extraction focuses on voiced regions highly related to style while maintaining continuity across different speech regions to improve expressiveness. We adjust the direction of the extracted style for optimal integration into the TTS model, which improves speech quality. Experimental results demonstrate that Spotlight-TTS achieves superior performance compared to baseline models in terms of expressiveness, overall speech quality, and style transfer capability.

</details>

### [Towards Authentic Movie Dubbing with Retrieve-Augmented Director-Actor Interaction Learning](2511.14249.md)
**Rui Liu, Yuan Zhao, Zhenqi Jia** · 2025-11-18

<details>
<summary>Abstract</summary>

The automatic movie dubbing model generates vivid speech from given scripts, replicating a speaker's timbre from a brief timbre prompt while ensuring lip-sync with the silent video. Existing approaches simulate a simplified workflow where actors dub directly without preparation, overlooking the critical director-actor interaction. In contrast, authentic workflows involve a dynamic collaboration: directors actively engage with actors, guiding them to internalize the context cues, specifically emotion, before performance. To address this issue, we propose a new Retrieve-Augmented Director-Actor Interaction Learning scheme to achieve authentic movie dubbing, termed Authentic-Dubber, which contains three novel mechanisms: (1) We construct a multimodal Reference Footage library to simulate the learning footage provided by directors. Note that we integrate Large Language Models (LLMs) to achieve deep comprehension of emotional representations across multimodal signals. (2) To emulate how actors efficiently and comprehensively internalize director-provided footage during dubbing, we propose an Emotion-Similarity-based Retrieval-Augmentation strategy. This strategy retrieves the most relevant multimodal information that aligns with the target silent video. (3) We develop a Progressive Graph-based speech generation approach that incrementally incorporates the retrieved multimodal emotional knowledge, thereby simulating the actor's final dubbing process. The above mechanisms enable the Authentic-Dubber to faithfully replicate the authentic dubbing workflow, achieving comprehensive improvements in emotional expressiveness. Both subjective and objective evaluations on the V2C Animation benchmark dataset validate the effectiveness. The code and demos are available at https://github.com/AI-S2-Lab/Authentic-Dubber.

</details>

### [Improving Direct Persian-English Speech-to-Speech Translation with Discrete Units and Synthetic Parallel Data](2511.12690.md)
**Sina Rashidi, Hossein Sameti** · 2025-11-16

<details>
<summary>Abstract</summary>

Direct speech-to-speech translation (S2ST), in which all components are trained jointly, is an attractive alternative to cascaded systems because it offers a simpler pipeline and lower inference latency. However, direct S2ST models require large amounts of parallel speech data in the source and target languages, which are rarely available for low-resource languages such as Persian. This paper presents a direct S2ST system for translating Persian speech into English speech, as well as a pipeline for synthetic parallel Persian-English speech generation. The model comprises three components: (1) a conformer-based encoder, initialized from self-supervised pre-training, maps source speech to high-level acoustic representations; (2) a causal transformer decoder with relative position multi-head attention translates these representations into discrete target speech units; (3) a unit-based neural vocoder generates waveforms from the predicted discrete units. To mitigate the data scarcity problem, we construct a new Persian-English parallel speech corpus by translating Persian speech transcriptions into English using a large language model and then synthesizing the corresponding English speech with a state-of-the-art zero-shot text-to-speech system. The resulting corpus increases the amount of available parallel speech by roughly a factor of six. On the Persian-English portion of the CVSS corpus, the proposed model achieves improvement of 4.6 ASR BLEU with the synthetic data over direct baselines. These results indicate that combining self-supervised pre-training, discrete speech units, and synthetic parallel data is effective for improving direct S2ST in low-resource language pairs such as Persian-English

</details>

### [Hi-Reco: High-Fidelity Real-Time Conversational Digital Humans](2511.12662.md)
**Hongbin Huang, Junwei Li, Tianxin Xie, Zhuang Li et al.** · 2025-11-16

<details>
<summary>Abstract</summary>

High-fidelity digital humans are increasingly used in interactive applications, yet achieving both visual realism and real-time responsiveness remains a major challenge. We present a high-fidelity, real-time conversational digital human system that seamlessly combines a visually realistic 3D avatar, persona-driven expressive speech synthesis, and knowledge-grounded dialogue generation. To support natural and timely interaction, we introduce an asynchronous execution pipeline that coordinates multi-modal components with minimal latency. The system supports advanced features such as wake word detection, emotionally expressive prosody, and highly accurate, context-aware response generation. It leverages novel retrieval-augmented methods, including history augmentation to maintain conversational flow and intent-based routing for efficient knowledge access. Together, these components form an integrated system that enables responsive and believable digital humans, suitable for immersive applications in communication, education, and entertainment.

</details>

### [VoiceCraft-X: Unifying Multilingual, Voice-Cloning Speech Synthesis and Speech Editing](2511.12347.md)
**Zhisheng Zheng, Puyuan Peng, Anuj Diwan, Cong Phuoc Huynh et al.** · 2025-11-15

<details>
<summary>Abstract</summary>

We introduce VoiceCraft-X, an autoregressive neural codec language model which unifies multilingual speech editing and zero-shot Text-to-Speech (TTS) synthesis across 11 languages: English, Mandarin, Korean, Japanese, Spanish, French, German, Dutch, Italian, Portuguese, and Polish. VoiceCraft-X utilizes the Qwen3 large language model for phoneme-free cross-lingual text processing and a novel token reordering mechanism with time-aligned text and speech tokens to handle both tasks as a single sequence generation problem. The model generates high-quality, natural-sounding speech, seamlessly creating new audio or editing existing recordings within one framework. VoiceCraft-X shows robust performance in diverse linguistic settings, even with limited per-language data, underscoring the power of unified autoregressive approaches for advancing complex, real-world multilingual speech applications. Audio samples are available at https://zhishengzheng.com/voicecraft-x/.

</details>

### [MF-Speech: Achieving Fine-Grained and Compositional Control in Speech Generation via Factor Disentanglement](2511.12074.md)
**Xinyue Yu, Youqing Fang, Pingyu Wu, Guoyang Ye et al.** · 2025-11-15

<details>
<summary>Abstract</summary>

Generating expressive and controllable human speech is one of the core goals of generative artificial intelligence, but its progress has long been constrained by two fundamental challenges: the deep entanglement of speech factors and the coarse granularity of existing control mechanisms. To overcome these challenges, we have proposed a novel framework called MF-Speech, which consists of two core components: MF-SpeechEncoder and MF-SpeechGenerator. MF-SpeechEncoder acts as a factor purifier, adopting a multi-objective optimization strategy to decompose the original speech signal into highly pure and independent representations of content, timbre, and emotion. Subsequently, MF-SpeechGenerator functions as a conductor, achieving precise, composable and fine-grained control over these factors through dynamic fusion and Hierarchical Style Adaptive Normalization (HSAN). Experiments demonstrate that in the highly challenging multi-factor compositional speech generation task, MF-Speech significantly outperforms current state-of-the-art methods, achieving a lower word error rate (WER=4.67%), superior style control (SECS=0.5685, Corr=0.68), and the highest subjective evaluation scores(nMOS=3.96, sMOS_emotion=3.86, sMOS_style=3.78). Furthermore, the learned discrete factors exhibit strong transferability, demonstrating their significant potential as a general-purpose speech representation.

</details>

### [CLARITY: Contextual Linguistic Adaptation and Accent Retrieval for Dual-Bias Mitigation in Text-to-Speech Generation](2511.11104.md)
**Crystal Min Hui Poon et.al.** · 2025-11-14

### [Synthetic Voices, Real Threats: Evaluating Large Text-to-Speech Models in Generating Harmful Audio](2511.10913.md)
**Guangke Chen et.al.** · 2025-11-14

### [VocalNet-M2: Advancing Low-Latency Spoken Language Modeling via Integrated Multi-Codebook Tokenization and Multi-Token Prediction](2511.10232.md)
**Yuhao Wang et.al.** · 2025-11-13

### [Time-Layer Adaptive Alignment for Speaker Similarity in Flow-Matching Based Zero-Shot TTS](2511.09995.md)
**Haoyu Li et.al.** · 2025-11-13

### [Curved Worlds, Clear Boundaries: Generalizing Speech Deepfake Detection using Hyperbolic and Spherical Geometry Spaces](2511.10793.md)
**Farhan Sheth, Girish, Mohd Mujtaba Akhtar, Muskaan Singh** · 2025-11-13

<details>
<summary>Abstract</summary>

In this work, we address the challenge of generalizable audio deepfake detection (ADD) across diverse speech synthesis paradigms-including conventional text-to-speech (TTS) systems and modern diffusion or flow-matching (FM) based generators. Prior work has mostly targeted individual synthesis families and often fails to generalize across paradigms due to overfitting to generation-specific artifacts. We hypothesize that synthetic speech, irrespective of its generative origin, leaves behind shared structural distortions in the embedding space that can be aligned through geometry-aware modeling. To this end, we propose RHYME, a unified detection framework that fuses utterance-level embeddings from diverse pretrained speech encoders using non-Euclidean projections. RHYME maps representations into hyperbolic and spherical manifolds-where hyperbolic geometry excels at modeling hierarchical generator families, and spherical projections capture angular, energy-invariant cues such as periodic vocoder artifacts. The fused representation is obtained via Riemannian barycentric averaging, enabling synthesis-invariant alignment. RHYME outperforms individual PTMs and homogeneous fusion baselines, achieving top performance and setting new state-of-the-art in cross-paradigm ADD.

</details>

### [FabasedVC: Enhancing Voice Conversion with Text Modality Fusion and Phoneme-Level SSL Features](2511.10112.md)
**Wenyu Wang, Zhetao Hu, Yiquan Zhou, Jiacheng Xu et al.** · 2025-11-13

<details>
<summary>Abstract</summary>

In voice conversion (VC), it is crucial to preserve complete semantic information while accurately modeling the target speaker's timbre and prosody. This paper proposes FabasedVC to achieve VC with enhanced similarity in timbre, prosody, and duration to the target speaker, as well as improved content integrity. It is an end-to-end VITS-based VC system that integrates relevant textual modality information, phoneme-level self-supervised learning (SSL) features, and a duration predictor. Specifically, we employ a text feature encoder to encode attributes such as text, phonemes, tones and BERT features. We then process the frame-level SSL features into phoneme-level features using two methods: average pooling and attention mechanism based on each phoneme's duration. Moreover, a duration predictor is incorporated to better align the speech rate and prosody of the target speaker. Experimental results demonstrate that our method outperforms competing systems in terms of naturalness, similarity, and content integrity.

</details>

### [Do AI Voices Learn Social Nuances? A Case of Politeness and Speech Rate](2511.10693.md)
**Eyal Rabin, Zohar Elyoseph, Rotem Israel-Fishelson, Adi Dali et al.** · 2025-11-12

<details>
<summary>Abstract</summary>

Voice-based artificial intelligence is increasingly expected to adhere to human social conventions, but can it learn implicit cues that are not explicitly programmed? This study investigates whether state-of-the-art text-to-speech systems have internalized the human tendency to reduce speech rate to convey politeness - a non-obvious prosodic marker. We prompted 22 synthetic voices from two leading AI platforms (AI Studio and OpenAI) to read a fixed script under both "polite and formal" and "casual and informal" conditions and measured the resulting speech duration. Across both AI platforms, the polite prompt produced slower speech than the casual prompt with very large effect sizes, an effect that was statistically significant for all of AI Studio's voices and for a large majority of OpenAI's voices. These results demonstrate that AI can implicitly learn and replicate psychological nuances of human communication, highlighting its emerging role as a social actor capable of reinforcing human social norms.

</details>

### [SpeechJudge: Towards Human-Level Judgment for Speech Naturalness](2511.07931.md)
**Xueyao Zhang, Chaoren Wang, Huan Liao, Ziniu Li et al.** · 2025-11-11

<details>
<summary>Abstract</summary>

Aligning large generative models with human feedback is a critical challenge. In speech synthesis, this is particularly pronounced due to the lack of a large-scale human preference dataset, which hinders the development of models that truly align with human perception. To address this, we introduce SpeechJudge, a comprehensive suite comprising a dataset, a benchmark, and a reward model centered on naturalness--one of the most fundamental subjective metrics for speech synthesis. First, we present SpeechJudge-Data, a large-scale human feedback corpus of 99K speech pairs. The dataset is constructed using a diverse set of advanced zero-shot text-to-speech (TTS) models across diverse speech styles and multiple languages, with human annotations for both intelligibility and naturalness preference. From this, we establish SpeechJudge-Eval, a challenging benchmark for speech naturalness judgment. Our evaluation reveals that existing metrics and AudioLLMs struggle with this task; the leading model, Gemini-2.5-Flash, achieves less than 70% agreement with human judgment, highlighting a significant gap for improvement. To bridge this gap, we develop SpeechJudge-GRM, a generative reward model (GRM) based on Qwen2.5-Omni-7B. It is trained on SpeechJudge-Data via a two-stage post-training process: Supervised Fine-Tuning (SFT) with Chain-of-Thought rationales followed by Reinforcement Learning (RL) with GRPO on challenging cases. On the SpeechJudge-Eval benchmark, the proposed SpeechJudge-GRM demonstrates superior performance, achieving 77.2% accuracy (and 79.4% after inference-time scaling @10) compared to a classic Bradley-Terry reward model (72.7%). Furthermore, SpeechJudge-GRM can be also employed as a reward function during the post-training of speech generation models to facilitate their alignment with human preferences.

</details>

### [SynTTS-Commands: A Public Dataset for On-Device KWS via TTS-Synthesized Multilingual Speech](2511.07821.md)
**Lu Gan, Xi Li** · 2025-11-11

<details>
<summary>Abstract</summary>

The development of high-performance, on-device keyword spotting (KWS) systems for ultra-low-power hardware is critically constrained by the scarcity of specialized, multi-command training datasets. Traditional data collection through human recording is costly, slow, and lacks scalability. This paper introduces SYNTTS-COMMANDS, a novel, multilingual voice command dataset entirely generated using state-of-the-art Text-to-Speech (TTS) synthesis. By leveraging the CosyVoice 2 model and speaker embeddings from public corpora, we created a scalable collection of English and Chinese commands. Extensive benchmarking across a range of efficient acoustic models demonstrates that our synthetic dataset enables exceptional accuracy, achieving up to 99.5\% on English and 98\% on Chinese command recognition. These results robustly validate that synthetic speech can effectively replace human-recorded audio for training KWS classifiers. Our work directly addresses the data bottleneck in TinyML, providing a practical, scalable foundation for building private, low-latency, and energy-efficient voice interfaces on resource-constrained edge devices. The dataset and source code are publicly available at https://github.com/lugan113/SynTTS-Commands-Official.

</details>

### [HQ-SVC: Towards High-Quality Zero-Shot Singing Voice Conversion in Low-Resource Scenarios](2511.08496.md)
**Bingsong Bai, Yizhong Geng, Fengping Wang, Cong Wang et al.** · 2025-11-11

<details>
<summary>Abstract</summary>

Zero-shot singing voice conversion (SVC) transforms a source singer's timbre to an unseen target speaker's voice while preserving melodic content without fine-tuning. Existing methods model speaker timbre and vocal content separately, losing essential acoustic information that degrades output quality while requiring significant computational resources. To overcome these limitations, we propose HQ-SVC, an efficient framework for high-quality zero-shot SVC. HQ-SVC first extracts jointly content and speaker features using a decoupled codec. It then enhances fidelity through pitch and volume modeling, preserving critical acoustic information typically lost in separate modeling approaches, and progressively refines outputs via differentiable signal processing and diffusion techniques. Evaluations confirm HQ-SVC significantly outperforms state-of-the-art zero-shot SVC methods in conversion quality and efficiency. Beyond voice conversion, HQ-SVC achieves superior voice naturalness compared to specialized audio super-resolution methods while natively supporting voice super-resolution tasks.

</details>

### [ParliaBench: An Evaluation and Benchmarking Framework for LLM-Generated Parliamentary Speech](2511.08247.md)
**Marios Koniaris, Argyro Tsipi, Panayiotis Tsanakas** · 2025-11-11

<details>
<summary>Abstract</summary>

Parliamentary speech generation presents specific challenges for large language models beyond standard text generation tasks. Unlike general text generation, parliamentary speeches require not only linguistic quality but also political authenticity and ideological consistency. Current language models lack specialized training for parliamentary contexts, and existing evaluation methods focus on standard NLP metrics rather than political authenticity. To address this, we present ParliaBench, a benchmark for parliamentary speech generation. We constructed a dataset of speeches from UK Parliament to enable systematic model training. We introduce an evaluation framework combining computational metrics with LLM-as-a-judge assessments for measuring generation quality across three dimensions: linguistic quality, semantic coherence, and political authenticity. We propose two novel embedding-based metrics, Political Spectrum Alignment and Party Alignment, to quantify ideological positioning. We fine-tuned five large language models (LLMs), generated 28k speeches, and evaluated them using our framework, comparing baseline and fine-tuned models. Results show that fine-tuning produces statistically significant improvements across the majority of metrics and our novel metrics demonstrate strong discriminative power for political dimensions.

</details>

### [E2E-VGuard: Adversarial Prevention for Production LLM-based End-To-End Speech Synthesis](2511.07099.md)
**Zhisheng Zhang et.al.** · 2025-11-10

### [BridgeVoC: Revitalizing Neural Vocoder from a Restoration Perspective](2511.07116.md)
**Andong Li, Tong Lei, Rilin Chen, Kai Li et al.** · 2025-11-10

<details>
<summary>Abstract</summary>

This paper revisits the neural vocoder task through the lens of audio restoration and propose a novel diffusion vocoder called BridgeVoC. Specifically, by rank analysis, we compare the rank characteristics of Mel-spectrum with other common acoustic degradation factors, and cast the vocoder task as a specialized case of audio restoration, where the range-space spectral (RSS) surrogate of the target spectrum acts as the degraded input. Based on that, we introduce the Schrodinger bridge framework for diffusion modeling, which defines the RSS and target spectrum as dual endpoints of the stochastic generation trajectory. Further, to fully utilize the hierarchical prior of subbands in the time-frequency (T-F) domain, we elaborately devise a novel subband-aware convolutional diffusion network as the data predictor, where subbands are divided following an uneven strategy, and convolutional-style attention module is employed with large kernels for efficient T-F contextual modeling. To enable single-step inference, we propose an omnidirectional distillation loss to facilitate effective information transfer from the teacher model to the student model, and the performance is improved by combining target-related and bijective consistency losses. Comprehensive experiments are conducted on various benchmarks and out-of-distribution datasets. Quantitative and qualitative results show that while enjoying fewer parameters, lower computational cost, and competitive inference speed, the proposed BridgeVoC yields stateof-the-art performance over existing advanced GAN-, DDPMand flow-matching-based baselines with only 4 sampling steps. And consistent superiority is still achieved with single-step inference.

</details>

### [Generating Novel and Realistic Speakers for Voice Conversion](2511.07135.md)
**Meiying Melissa Chen, Zhenyu Wang, Zhiyao Duan** · 2025-11-10

<details>
<summary>Abstract</summary>

Voice conversion models modify timbre while preserving paralinguistic features, enabling applications like dubbing and identity protection. However, most VC systems require access to target utterances, limiting their use when target data is unavailable or when users desire conversion to entirely novel, unseen voices. To address this, we introduce a lightweight method SpeakerVAE to generate novel speakers for VC. Our approach uses a deep hierarchical variational autoencoder to model the speaker timbre space. By sampling from the trained model, we generate novel speaker representations for voice synthesis in a VC pipeline. The proposed method is a flexible plug-in module compatible with various VC models, without co-training or fine-tuning of the base VC system. We evaluated our approach with state-of-the-art VC models: FACodec and CosyVoice2. The results demonstrate that our method successfully generates novel, unseen speakers with quality comparable to that of the training speakers.

</details>

### [IDMap: A Pseudo-Speaker Generator Framework Based on Speaker Identity Index to Vector Mapping](2511.06246.md)
**Zeyan Liu, Liping Chen, Kong Aik Lee, Zhenhua Ling** · 2025-11-09

<details>
<summary>Abstract</summary>

Facilitated by the speech generation framework that disentangles speech into content, speaker, and prosody, voice anonymization is accomplished by substituting the original speaker embedding vector with that of a pseudo-speaker. In this framework, the pseudo-speaker generation forms a fundamental challenge. Current pseudo-speaker generation methods demonstrate limitations in the uniqueness of pseudo-speakers, consequently restricting their effectiveness in voice privacy protection. Besides, existing model-based methods suffer from heavy computation costs. Especially, in the large-scale scenario where a huge number of pseudo-speakers are generated, the limitations of uniqueness and computational inefficiency become more significant. To this end, this paper proposes a framework for pseudo-speaker generation, which establishes a mapping from speaker identity index to speaker vector in the feedforward architecture, termed IDMap. Specifically, the framework is specified into two models: IDMap-MLP and IDMap-Diff. Experiments were conducted on both small- and large-scale evaluation datasets. Small-scale evaluations on the LibriSpeech dataset validated the effectiveness of the proposed IDMap framework in enhancing the uniqueness of pseudo-speakers, thereby improving voice privacy protection, while at a reduced computational cost. Large-scale evaluations on the MLS and Common Voice datasets further justified the superiority of the IDMap framework regarding the stability of the voice privacy protection capability as the number of pseudo-speakers increased. Audio samples and open-source code can be found in https://github.com/VoicePrivacy/IDMap.

</details>

### [Synthesizing speech with selected perceptual voice qualities - A case study with creaky voice](2511.05143.md)
**Frederik Rautenberg, Fritz Seebauer, Jana Wiechmann, Michael Kuhlmann et al.** · 2025-11-07

<details>
<summary>Abstract</summary>

The control of perceptual voice qualities in a text-to-speech (TTS) system is of interest for applications where unmanipu- lated and manipulated speech probes can serve to illustrate pho- netic concepts that are otherwise difficult to grasp. Here, we show that a TTS system, that is augmented with a global speaker attribute manipulation block based on normalizing flows1 , is capable of correctly manipulating the non-persistent, localized quality of creaky voice, thus avoiding the necessity of a, typi- cally unreliable, frame-wise creak predictor. Subjective listen- ing tests confirm successful creak manipulation at a slightly re- duced MOS score compared to the original recording.

</details>

### [The Impact of Prosodic Segmentation on Speech Synthesis of Spontaneous Speech](2511.14779.md)
**Julio Cesar Galdino, Sidney Evaldo Leal, Leticia Gabriella De Souza, Rodrigo de Freitas Lima et al.** · 2025-11-06

<details>
<summary>Abstract</summary>

Spontaneous speech presents several challenges for speech synthesis, particularly in capturing the natural flow of conversation, including turn-taking, pauses, and disfluencies. Although speech synthesis systems have made significant progress in generating natural and intelligible speech, primarily through architectures that implicitly model prosodic features such as pitch, intensity, and duration, the construction of datasets with explicit prosodic segmentation and their impact on spontaneous speech synthesis remains largely unexplored. This paper evaluates the effects of manual and automatic prosodic segmentation annotations in Brazilian Portuguese on the quality of speech synthesized by a non-autoregressive model, FastSpeech 2. Experimental results show that training with prosodic segmentation produced slightly more intelligible and acoustically natural speech. While automatic segmentation tends to create more regular segments, manual prosodic segmentation introduces greater variability, which contributes to more natural prosody. Analysis of neutral declarative utterances showed that both training approaches reproduced the expected nuclear accent pattern, but the prosodic model aligned more closely with natural pre-nuclear contours. To support reproducibility and future research, all datasets, source codes, and trained models are publicly available under the CC BY-NC-ND 4.0 license.

</details>

### [PolyNorm: Few-Shot LLM-Based Text Normalization for Text-to-Speech](2511.03080.md)
**Michel Wong et.al.** · 2025-11-05

### [Step-Audio-EditX Technical Report](2511.03601.md)
**Chao Yan, Boyong Wu, Peng Yang, Pengfei Tan et al.** · 2025-11-05

<details>
<summary>Abstract</summary>

We present Step-Audio-EditX, the first open-source LLM-based audio model excelling at expressive and iterative audio editing encompassing emotion, speaking style, and paralinguistics alongside robust zero-shot text-to-speech (TTS) capabilities. Our core innovation lies in leveraging only large-margin synthetic data, which circumvents the need for embedding-based priors or auxiliary modules. This large-margin learning approach enables both iterative control and high expressivity across voices, and represents a fundamental pivot from the conventional focus on representation-level disentanglement. Evaluation results demonstrate that Step-Audio-EditX surpasses both MiniMax-2.6-hd and Doubao-Seed-TTS-2.0 in emotion editing and other fine-grained control tasks.

</details>

### [Principled Coarse-Grained Acceptance for Speculative Decoding in Speech](2511.13732.md)
**Moran Yanuka, Paul Dixon, Eyal Finkelshtein, Daniel Rotman et al.** · 2025-11-05

<details>
<summary>Abstract</summary>

Speculative decoding accelerates autoregressive speech generation by letting a fast draft model propose tokens that a larger target model verifies. However, for speech LLMs that generate acoustic tokens, exact token matching is overly restrictive: many discrete tokens are acoustically or semantically interchangeable, reducing acceptance rates and limiting speedups. We introduce Principled Coarse-Graining (PCG), which verifies proposals at the level of Acoustic Similarity Groups (ASGs) derived from the target model's embedding space. By splitting each token's probability mass across the overlapping groups that contain it, we define an overlap-aware coarse-grained distribution and perform rejection sampling on the resulting group variable. This yields an exactness guarantee at the group level while allowing the accepted draft token to stand in for any member of the group in practice. On LibriTTS, PCG increases acceptance and throughput relative to standard speculative decoding and prior speech-specific relaxations while maintaining intelligibility and speaker similarity. These results suggest acoustically aware, group-level acceptance as a simple and general way to accelerate speech token generation while maintaining speech quality.

</details>

### [Toward Objective and Interpretable Prosody Evaluation in Text-to-Speech: A Linguistically Motivated Approach](2511.02104.md)
**Cedric Chan, Jianjing Kuang** · 2025-11-03

<details>
<summary>Abstract</summary>

Prosody is essential for speech technology, shaping comprehension, naturalness, and expressiveness. However, current text-to-speech (TTS) systems still struggle to accurately capture human-like prosodic variation, in part because existing evaluation methods for prosody remain limited. Traditional metrics like Mean Opinion Score (MOS) are resource-intensive, inconsistent, and offer little insight into why a system sounds unnatural. This study introduces a linguistically informed, semi-automatic framework for evaluating TTS prosody through a two-tier architecture that mirrors human prosodic organization. The method uses quantitative linguistic criteria to evaluate synthesized speech against human speech corpora across multiple acoustic dimensions. By integrating discrete and continuous prosodic measures, it provides objective and interpretable metrics of both event placement and cue realization, while accounting for the natural variability observed across speakers and prosodic cues. Results show strong correlations with perceptual MOS ratings while revealing model-specific weaknesses that traditional perceptual tests alone cannot capture. This approach provides a principled path toward diagnosing, benchmarking, and ultimately improving the prosodic naturalness of next-generation TTS systems.

</details>

### [WhisperVC: Decoupled Cross-Domain Alignment and Speech Generation for Low-Resource Whisper-to-Normal Conversion](2511.01056.md)
**Dong Liu, Juan Liu, Wei Ju, Yao Tian et al.** · 2025-11-02

<details>
<summary>Abstract</summary>

Whispered speech lacks vocal-fold excitation, making intelligible conversion challenging. We propose WhisperVC, a three-stage framework for low-resource whisper-to-normal (W2N) conversion that decouples cross-domain alignment from speech generation. Stage 1 uses limited paired whisper-normal data with a content encoder and a Conformer-based variational autoencoder (VAE) with soft-DTW alignment to learn domain-invariant semantic representations. Stage 2, trained only on normal speech, employs a Length-Channel Aligner and a two-stage speaker-conditioned mel generator for timbre and prosody modeling. Stage 3 fine-tunes a HiFi-GAN vocoder for waveform synthesis. Experimental results on AISHELL6-Whisper show competitive quality (DNSMOS 3.07, UTMOS 2.83, CER 16.93%) and WavLM speaker similarity (0.95). The framework also supports privacy-preserving communication as well as non-vocal communication and a rehabilitation tool for post-surgical vocal-fold patients. Samples are available online.

</details>

### [Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication](2510.27247.md)
**Deok-Seon Kim, Seo-Hyun Lee, Kang Yin, Seong-Whan Lee** · 2025-10-31

<details>
<summary>Abstract</summary>

Brain-to-speech (BTS) systems represent a groundbreaking approach to human communication by enabling the direct transformation of neural activity into linguistic expressions. While recent non-invasive BTS studies have largely focused on decoding predefined words or sentences, achieving open-vocabulary neural communication comparable to natural human interaction requires decoding unconstrained speech. Additionally, effectively integrating diverse signals derived from speech is crucial for developing personalized and adaptive neural communication and rehabilitation solutions for patients. This study investigates the potential of speech synthesis for previously unseen sentences across various speech modes by leveraging phoneme-level information extracted from high-density electroencephalography (EEG) signals, both independently and in conjunction with electromyography (EMG) signals. Furthermore, we examine the properties affecting phoneme decoding accuracy during sentence reconstruction and offer neurophysiological insights to further enhance EEG decoding for more effective neural communication solutions. Our findings underscore the feasibility of biosignal-based sentence-level speech synthesis for reconstructing unseen sentences, highlighting a significant step toward developing open-vocabulary neural communication systems adapted to diverse patient needs and conditions. Additionally, this study provides meaningful insights into the development of communication and rehabilitation solutions utilizing EEG-based decoding technologies.

</details>

### [NaturalVoices: A Large-Scale, Spontaneous and Emotional Podcast Dataset for Voice Conversion](2511.00256.md)
**Zongyang Du, Shreeram Suresh Chandra, Ismail Rasim Ulgen, Aurosweta Mahapatra et al.** · 2025-10-31

<details>
<summary>Abstract</summary>

Everyday speech conveys far more than words, it reflects who we are, how we feel, and the circumstances surrounding our interactions. Yet, most existing speech datasets are acted, limited in scale, and fail to capture the expressive richness of real-life communication. With the rise of large neural networks, several large-scale speech corpora have emerged and been widely adopted across various speech processing tasks. However, the field of voice conversion (VC) still lacks large-scale, expressive, and real-life speech resources suitable for modeling natural prosody and emotion. To fill this gap, we release NaturalVoices (NV), the first large-scale spontaneous podcast dataset specifically designed for emotion-aware voice conversion. It comprises 5,049 hours of spontaneous podcast recordings with automatic annotations for emotion (categorical and attribute-based), speech quality, transcripts, speaker identity, and sound events. The dataset captures expressive emotional variation across thousands of speakers, diverse topics, and natural speaking styles. We also provide an open-source pipeline with modular annotation tools and flexible filtering, enabling researchers to construct customized subsets for a wide range of VC tasks. Experiments demonstrate that NaturalVoices supports the development of robust and generalizable VC models capable of producing natural, expressive speech, while revealing limitations of current architectures when applied to large-scale spontaneous data. These results suggest that NaturalVoices is both a valuable resource and a challenging benchmark for advancing the field of voice conversion. Dataset is available at: https://huggingface.co/JHU-SmileLab

</details>

### [UniTok-Audio: A Unified Audio Generation Framework via Generative Modeling on Discrete Codec Tokens](2510.26372.md)
**Chengwei Liu, Haoyin Yan, Shaofei Xue, Xiaotao Liang et al.** · 2025-10-30

<details>
<summary>Abstract</summary>

Generative modeling has recently achieved remarkable success across text, image, and audio domains, demonstrating powerful capabilities for unified representation learning. However, audio generation models still face challenges in terms of audio quality and generalization ability across tasks. This fragmentation results in redundant development efforts, inconsistent performance, and limited extensibility. To address these issues, we propose \textbf{UniTok-Audio}, a scalable and extensible framework for unified audio generation tasks. Specifically, 1) UniTok-Audio extracts continuous feature of conditions to generates discrete tokens of target audio in an autoregressive manner; 2) a special task identifier token unifies different learning patterns of multiple tasks in a single framework; 3) a dual-stream audio codec involving acoustic and semantic branch is developed for high-fidelity waveform reconstruction. Experimental results demonstrate that UniTok-Audio achieves competitive performance in comparation with state-of-the-art task-specific or multi-task systems across five time-aligned tasks: speech restoration, target speaker extraction, speech separation, voice conversion, and language-queried audio source separation. To foster future research, we will open-source our codebase. The demo page of our work can be found here: https://alibaba.github.io/unified-audio.

</details>

### [Explainable Disentanglement on Discrete Speech Representations for Noise-Robust ASR](2510.25150.md)
**Shreyas Gopal, Ashutosh Anshul, Haoyang Li, Yue Heng Yeo et al.** · 2025-10-29

<details>
<summary>Abstract</summary>

Discrete audio representations are gaining traction in speech modeling due to their interpretability and compatibility with large language models, but are not always optimized for noisy or real-world environments. Building on existing works that quantize Whisper embeddings for speech-to-unit modeling, we propose disentangling semantic speech content from background noise in the latent space. Our end-to-end model separates clean speech in the form of codebook tokens, while extracting interpretable noise vectors as quantization residue which are supervised via a lightweight classifier. We show that our approach improves alignment between clean/noisy speech and text, producing speech tokens that display a high degree of noiseinvariance, and improves ASR performance. Keeping Whisper frozen, we show an 82% reduction in error rate compared to Whisper, and 35% improvement over baseline methods on the VBDemand test set. Further analyses show that the learned token space generalizes well to both seen and unseen acoustic conditions.

</details>

### [Levée d'ambiguïtés par grammaires locales](2510.24530.md)
**Eric G. C. Laporte** · 2025-10-28

<details>
<summary>Abstract</summary>

Many words are ambiguous in terms of their part of speech (POS). However, when a word appears in a text, this ambiguity is generally much reduced. Disambiguating POS involves using context to reduce the number of POS associated with words, and is one of the main challenges of lexical tagging. The problem of labeling words by POS frequently arises in natural language processing, for example for spelling correction, grammar or style checking, expression recognition, text-to-speech conversion, text corpus analysis, etc. Lexical tagging systems are thus useful as an initial component of many natural language processing systems. A number of recent lexical tagging systems produce multiple solutions when the text is lexically ambiguous or the uniquely correct solution cannot be found. These contributions aim to guarantee a zero silence rate: the correct tag(s) for a word must never be discarded. This objective is unrealistic for systems that tag each word uniquely. This article concerns a lexical disambiguation method adapted to the objective of a zero silence rate and implemented in Silberztein's INTEX system (1993). We present here a formal description of this method. We show that to verify a local disambiguation grammar in this framework, it is not sufficient to consider the transducer paths separately: one needs to verify their interactions. Similarly, if a combination of multiple transducers is used, the result cannot be predicted by considering them in isolation. Furthermore, when examining the initial labeling of a text as produced by INTEX, ideas for disambiguation rules come spontaneously, but grammatical intuitions may turn out to be inaccurate, often due to an unforeseen construction or ambiguity. If a zero silence rate is targeted, local grammars must be carefully tested. This is where a detailed specification of what a grammar will do once applied to texts would be necessary.

</details>

### [Bayesian Speech Synthesizers Can Learn from Multiple Teachers](2510.24372.md)
**Ziyang Zhang, Yifan Gao, Xuenan Xu, Baoxiang Li et al.** · 2025-10-28

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) is inherently a "one-to-many" mapping characterized by intrinsic uncertainty, yet current paradigms often oversimplify it into a deterministic regression task. While continuous-valued autoregressive (AR) models have recently emerged as a promising alternative to discrete codec-based approaches, they typically rely on a fixed-variance prior, fundamentally constraining generation to a static point estimate that ignores the dynamic variability of natural speech. To bridge this gap, we propose BELLE (Bayesian evidential learning with language modelling), a framework that shifts from deterministic prediction to principled Bayesian inference without increasing model parameters or inference latency. By modeling the acoustic target as a Normal-Inverse-Gamma distribution, BELLE captures data-dependent aleatoric uncertainty. To enable accurate variance estimation on standard single-reference datasets, we introduce a "one-to-many" training strategy that leverages synthetic samples as a statistical support set, allowing the model to learn robust distributional properties rather than merely imitating teacher artifacts. Experiments demonstrate that BELLE, trained on only ~5k hours of data, outperforms leading open-source models trained on 50k hours (achieving a 25.8% relative WER reduction) and naturally supports high-quality streaming generation. Audio samples are available at https://belletts.github.io/Belle/.

</details>

### [Abjad AI at NADI 2025: CATT-Whisper: Multimodal Diacritic Restoration Using Text and Speech Representations](2510.24247.md)
**Ahmad Ghannam, Naif Alharthi, Faris Alasmary, Kholood Al Tabash et al.** · 2025-10-28

<details>
<summary>Abstract</summary>

In this work, we tackle the Diacritic Restoration (DR) task for Arabic dialectal sentences using a multimodal approach that combines both textual and speech information. We propose a model that represents the text modality using an encoder extracted from our own pre-trained model named CATT. The speech component is handled by the encoder module of the OpenAI Whisper base model. Our solution is designed following two integration strategies. The former consists of fusing the speech tokens with the input at an early stage, where the 1500 frames of the audio segment are averaged over 10 consecutive frames, resulting in 150 speech tokens. To ensure embedding compatibility, these averaged tokens are processed through a linear projection layer prior to merging them with the text tokens. Contextual encoding is guaranteed by the CATT encoder module. The latter strategy relies on cross-attention, where text and speech embeddings are fused. The cross-attention output is then fed to the CATT classification head for token-level diacritic prediction. To further improve model robustness, we randomly deactivate the speech input during training, allowing the model to perform well with or without speech. Our experiments show that the proposed approach achieves a word error rate (WER) of 0.25 and a character error rate (CER) of 0.9 on the development set. On the test set, our model achieved WER and CER scores of 0.55 and 0.13, respectively.

</details>

### [emg2speech: Synthesizing speech from electromyography using self-supervised speech models](2510.23969.md)
**Harshavardhana T. Gowda, Daniel C. Comstock, Lee M. Miller** · 2025-10-28

<details>
<summary>Abstract</summary>

We present a neuromuscular speech interface that translates electromyographic (EMG) signals recorded from orofacial muscles during speech articulation directly into audio. We find that self-supervised speech (S3) representations are strongly linearly related to the electrical power of muscle activity: a simple linear mapping predicts EMG power from S3 representations with a correlation of r = 0.85. In addition, EMG power vectors associated with distinct articulatory gestures form structured, separable clusters. Together, these observations suggest that S3 models implicitly encode articulatory mechanisms, as reflected in EMG activity. Leveraging this structure, we map EMG signals into the S3 representation space and synthesize speech, enabling end-to-end EMG-to-speech generation without explicit articulatory modeling or vocoder training. We demonstrate this system with a participant with amyotrophic lateral sclerosis (ALS), converting orofacial EMG recorded while she silently articulated speech into audio.

</details>

### [SoulX-Podcast: Towards Realistic Long-form Podcasts with Dialectal and Paralinguistic Diversity](2510.23541.md)
**Hanke Xie, Haopeng Lin, Wenxiao Cao, Dake Guo et al.** · 2025-10-27

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) synthesis have significantly improved speech expressiveness and naturalness. However, most existing systems are tailored for single-speaker synthesis and fall short in generating coherent multi-speaker conversational speech. This technical report presents SoulX-Podcast, a system designed for podcast-style multi-turn, multi-speaker dialogic speech generation, while also achieving state-of-the-art performance in conventional TTS tasks. To meet the higher naturalness demands of multi-turn spoken dialogue, SoulX-Podcast integrates a range of paralinguistic controls and supports both Mandarin and English, as well as several Chinese dialects, including Sichuanese, Henanese, and Cantonese, enabling more personalized podcast-style speech generation. Experimental results demonstrate that SoulX-Podcast can continuously produce over 90 minutes of conversation with stable speaker timbre and smooth speaker transitions. Moreover, speakers exhibit contextually adaptive prosody, reflecting natural rhythm and intonation changes as dialogues progress. Across multiple evaluation metrics, SoulX-Podcast achieves state-of-the-art performance in both monologue TTS and multi-turn conversational speech synthesis.

</details>

### [SFMS-ALR: Script-First Multilingual Speech Synthesis with Adaptive Locale Resolution](2510.25178.md)
**Dharma Teja Donepudi** · 2025-10-27

<details>
<summary>Abstract</summary>

Intra-sentence multilingual speech synthesis (code-switching TTS) remains a major challenge due to abrupt language shifts, varied scripts, and mismatched prosody between languages. Conventional TTS systems are typically monolingual and fail to produce natural, intelligible speech in mixed-language contexts. We introduce Script-First Multilingual Synthesis with Adaptive Locale Resolution (SFMS-ALR), an engine-agnostic framework for fluent, real-time code-switched speech generation. SFMS-ALR segments input text by Unicode script, applies adaptive language identification to determine each segment's language and locale, and normalizes prosody using sentiment-aware adjustments to preserve expressive continuity across languages. The algorithm generates a unified SSML representation with appropriate "lang" or "voice" spans and synthesizes the utterance in a single TTS request. Unlike end-to-end multilingual models, SFMS-ALR requires no retraining and integrates seamlessly with existing voices from Google, Apple, Amazon, and other providers. Comparative analysis with data-driven pipelines such as Unicom and Mask LID demonstrates SFMS-ALR's flexibility, interpretability, and immediate deployability. The framework establishes a modular baseline for high-quality, engine-independent multilingual TTS and outlines evaluation strategies for intelligibility, naturalness, and user preference.

</details>

### [UltraVoice: Scaling Fine-Grained Style-Controlled Speech Conversations for Spoken Dialogue Models](2510.22588.md)
**Wenming Tu, Guanrou Yang, Ruiqi Yan, Wenxi Chen et al.** · 2025-10-26

<details>
<summary>Abstract</summary>

Spoken dialogue models currently lack the ability for fine-grained speech style control, a critical capability for human-like interaction that is often overlooked in favor of purely functional capabilities like reasoning and question answering. To address this limitation, we introduce UltraVoice, the first large-scale speech dialogue dataset engineered for multiple fine-grained speech style control. Encompassing over 830 hours of speech dialogues, UltraVoice provides instructions across six key speech stylistic dimensions: emotion, speed, volume, accent, language, and composite styles. Fine-tuning leading models such as SLAM-Omni and VocalNet on UltraVoice significantly enhances their fine-grained speech stylistic controllability without degrading core conversational abilities. Specifically, our fine-tuned models achieve improvements of 29.12-42.33% in Mean Opinion Score (MOS) and 14.61-40.09 percentage points in Instruction Following Rate (IFR) on multi-dimensional control tasks designed in the UltraVoice. Moreover, on the URO-Bench benchmark, our fine-tuned models demonstrate substantial gains in core understanding, reasoning, and conversational abilities, with average improvements of +10.84% on the Basic setting and +7.87% on the Pro setting. Furthermore, the dataset's utility extends to training controllable Text-to-Speech (TTS) models, underscoring its high quality and broad applicability for expressive speech synthesis. The complete dataset and model checkpoints are available at: https://github.com/bigai-nlco/UltraVoice.

</details>

### [Ming-UniAudio: Speech LLM for Joint Understanding, Generation and Editing with Unified Representation](2511.05516.md)
**Canxiang Yan, Chunxiang Jin, Dawei Huang, Haibing Yu et al.** · 2025-10-26

<details>
<summary>Abstract</summary>

Existing speech models suffer from competing requirements on token representations by understanding and generation tasks. This discrepancy in representation prevents speech language models from performing instruction-based free-form editing. To solve this challenge, we introduce a novel framework that unifies speech understanding, generation, and editing. The core of our unified model is a unified continuous speech tokenizer MingTok-Audio, the first continuous tokenizer to effectively integrate semantic and acoustic features, which makes it suitable for both understanding and generation tasks. Based on this unified continuous audio tokenizer, we developed the speech language model Ming-UniAudio, which achieved a balance between generation and understanding capabilities. Ming-UniAudio sets new state-of-the-art (SOTA) records on 8 out of 12 metrics on the ContextASR benchmark. Notably, for Chinese voice cloning, it achieves a highly competitive Seed-TTS-WER of 0.95. Leveraging this foundational model, we further trained a dedicated speech editing model Ming-UniAudio-Edit, the first speech language model that enables universal, free-form speech editing guided solely by natural language instructions, handling both semantic and acoustic modifications without timestamp condition. To rigorously assess the editing capability and establish a foundation for future research, we introduce Ming-Freeform-Audio-Edit, the first comprehensive benchmark tailored for instruction-based free-form speech editing, featuring diverse scenarios and evaluation dimensions spanning semantic correctness, acoustic quality, and instruction alignment. We open-sourced the continuous audio tokenizer, the unified foundational model, and the free-form instruction-based editing model to facilitate the development of unified audio understanding, generation, and manipulation.

</details>

### [A Comprehensive Study of Neural Models for Arabic Text-to-Speech Synthesis](s2:d751b5be4693ab3a7373ea5a6343f5d460da9dc7.md)
**A. Ashraf, Abdelrahman Ramadan Fathi, Ali Adel Sayed Ahmed, Omar Tamer Mohammed Ameen Hassanin et al.** · 2025-10-25

<details>
<summary>Abstract</summary>

This paper presents a comprehensive study of neural models for Arabic Text-to-Speech (TTS) synthesis using only publicly available datasets. Given the scarcity of high-quality open source Arabic TTS systems and the importance of diacritics in conveying semantic meaning, we explore multiple deep learning approaches trained on the Arabic Speech Corpus [1] and the ClArTTS dataset [2]. We evaluate three spectrogram-generation models FastSpeech2 [3], FastPitch [4], and Mixer-TTS [5] alongside the HiFi-GAN vocoder [6]. Additionally, we investigate Spark-TTS [7], an end-to-end LLM-based model offering zero-shot voice cloning and controllable prosody. Our experiments show that FastPitch and Mixer-TTS generate high-quality speech even with limited data, while Spark-TTS achieves superior audio quality at the cost of longer inference. These results highlight the potential of open-source Arabic TTS and provide insight into trade-offs between traditional and end-to-end architectures.

</details>

### [StylePitcher: Generating Style-Following and Expressive Pitch Curves for Versatile Singing Tasks](2510.21685.md)
**Jingyue Huang, Qihui Yang, Fei Yueh Chen, Julian McAuley et al.** · 2025-10-24

<details>
<summary>Abstract</summary>

Existing pitch curve generators face two main challenges: they often neglect singer-specific expressiveness, reducing their ability to capture individual singing styles. And they are typically developed as auxiliary modules for specific tasks such as pitch correction, singing voice synthesis, or voice conversion, which restricts their generalization capability. We propose StylePitcher, a general-purpose pitch curve generator that learns singer style from reference audio while preserving alignment with the intended melody. Built upon a rectified flow matching architecture, StylePitcher flexibly incorporates symbolic music scores and pitch context as conditions for generation, and can seamlessly adapt to diverse singing tasks without retraining. Objective and subjective evaluations across various singing tasks demonstrate that StylePitcher improves style similarity and audio quality while maintaining pitch accuracy comparable to task-specific baselines.

</details>

### [Vox-Evaluator: Enhancing Stability and Fidelity for Zero-shot TTS with A Multi-Level Evaluator](2510.20210.md)
**Hualei Wang et.al.** · 2025-10-23

### [R2-SVC: Towards Real-World Robust and Expressive Zero-shot Singing Voice Conversion](2510.20677.md)
**Junjie Zheng, Gongyu Chen, Chaofan Ding, Zihao Chen** · 2025-10-23

<details>
<summary>Abstract</summary>

In real-world singing voice conversion (SVC) applications, environmental noise and the demand for expressive output pose significant challenges. Conventional methods, however, are typically designed without accounting for real deployment scenarios, as both training and inference usually rely on clean data. This mismatch hinders practical use, given the inevitable presence of diverse noise sources and artifacts from music separation. To tackle these issues, we propose R2-SVC, a robust and expressive SVC framework. First, we introduce simulation-based robustness enhancement through random fundamental frequency ($F_0$) perturbations and music separation artifact simulations (e.g., reverberation, echo), substantially improving performance under noisy conditions. Second, we enrich speaker representation using domain-specific singing data: alongside clean vocals, we incorporate DNSMOS-filtered separated vocals and public singing corpora, enabling the model to preserve speaker timbre while capturing singing style nuances. Third, we integrate the Neural Source-Filter (NSF) model to explicitly represent harmonic and noise components, enhancing the naturalness and controllability of converted singing. R2-SVC achieves state-of-the-art results on multiple SVC benchmarks under both clean and noisy conditions.

</details>

### [Style Attack Disguise: When Fonts Become a Camouflage for Adversarial Intent](2510.19641.md)
**Yangshijie Zhang, Xinda Wang, Jialin Liu, Wenqiang Wang et al.** · 2025-10-22

<details>
<summary>Abstract</summary>

With social media growth, users employ stylistic fonts and font-like emoji to express individuality, creating visually appealing text that remains human-readable. However, these fonts introduce hidden vulnerabilities in NLP models: while humans easily read stylistic text, models process these characters as distinct tokens, causing interference. We identify this human-model perception gap and propose a style-based attack, Style Attack Disguise (SAD). We design two sizes: light for query efficiency and strong for superior attack performance. Experiments on sentiment classification and machine translation across traditional models, LLMs, and commercial services demonstrate SAD's strong attack performance. We also show SAD's potential threats to multimodal tasks including text-to-image and text-to-speech generation.

</details>

### [EchoFake: A Replay-Aware Dataset for Practical Speech Deepfake Detection](2510.19414.md)
**Tong Zhang, Yihuan Huang, Yanzhen Ren** · 2025-10-22

<details>
<summary>Abstract</summary>

The growing prevalence of speech deepfakes has raised serious concerns, particularly in real-world scenarios such as telephone fraud and identity theft. While many anti-spoofing systems have demonstrated promising performance on lab-generated synthetic speech, they often fail when confronted with physical replay attacks-a common and low-cost form of attack used in practical settings. Our experiments show that models trained on existing datasets exhibit severe performance degradation, with average accuracy dropping to 59.6% when evaluated on replayed audio. To bridge this gap, we present EchoFake, a comprehensive dataset comprising more than 120 hours of audio from over 13,000 speakers, featuring both cutting-edge zero-shot text-to-speech (TTS) speech and physical replay recordings collected under varied devices and real-world environmental settings. Additionally, we evaluate three baseline detection models and show that models trained on EchoFake achieve lower average EERs across datasets, indicating better generalization. By introducing more practical challenges relevant to real-world deployment, EchoFake offers a more realistic foundation for advancing spoofing detection methods.

</details>

### [Which Evaluation for Which Model? A Taxonomy for Speech Model Assessment](2510.19509.md)
**Maureen de Seyssel, Eeshan Gunesh Dhekane** · 2025-10-22

<details>
<summary>Abstract</summary>

Speech foundation models have recently achieved remarkable capabilities across a wide range of tasks. However, their evaluation remains disjointed across tasks and model types. Different models excel at distinct aspects of speech processing and thus require different evaluation protocols. This paper proposes a unified taxonomy that addresses the question: Which evaluation is appropriate for which model? The taxonomy defines three orthogonal axes: the evaluation aspect being measured, the model capabilities required to attempt the task, and the task or protocol requirements needed to perform it. We classify a broad set of existing evaluations and benchmarks along these axes, spanning areas such as representation learning, speech generation, and interactive dialogue. By mapping each evaluation to the capabilities a model exposes (e.g., speech generation, real-time processing) and to its methodological demands (e.g., fine-tuning data, human judgment), the taxonomy provides a principled framework for aligning models with suitable evaluation methods. It also reveals systematic gaps, such as limited coverage of prosody, interaction, or reasoning, that highlight priorities for future benchmark design. Overall, this work offers a conceptual foundation and practical guide for selecting, interpreting, and extending evaluations of speech models.

</details>

### [A Study of Japanese Mixed Emotional Speech Synthesis Based on an End-to-End Emotional Speech Synthesis Model](s2:fcaea1eb0491ea7945cfc8b320d5b5b6ad13c4f7.md)
**Issei Sakata, Tetsuo Kosaka** · 2025-10-22

<details>
<summary>Abstract</summary>

In this study, we examined mixed emotion speech synthesis for Japanese using Emotional-VITS, an emotional speech synthesis model based on VITS, which is an end-to-end speech synthesis model. On the dataset of pretrained models, we compared models trained in two languages (Japanese and Chinese) and models trained only in Japanese. Regarding the quality of the synthesized speech, we confirmed that the model trained only in Japanese has higher naturalness than the model trained in Japanese and Chinese in both subjective and objective evaluation experiments, and that the input text is accurately synthesized. We also examined the emotional features used in speech synthesis and confirmed that the average of the emotional features of other speakers, other than the speaker to be synthesized, yields a higher emotion recognition rate than the average of the emotional features extracted from the target speech or the average of the emotional features of the speech of the speaker to be synthesized. Furthermore, it was found that even in mixed emotion speech synthesis, in which two types of emotions are mixed, the emotion recognized by the subject changes consistently depending on the mixing ratio, and it was found that emotions close to human sensation are possible.

</details>

### [BAANI: A 296M-Parameter Neural Vocoder for End-To-End Punjabi Speech Synthesis](s2:3222da1e420463570b5e63c1eefdd498d966e7ea.md)
**Siddharth Kumar, Nisarg Trivedi, Ravindrakumar M. Purohit, Hemant A. Patil** · 2025-10-22

<details>
<summary>Abstract</summary>

In this work, we present BAANI, a neural vocoder comprising 296 million parameters, designed for end-to-end speech synthesis (SS) in the Punjabi language. Recognizing the unique phonetic and prosodic characteristics of a low-resource and underrepresented Punjabi language, BAANI aims to enhance the naturalness and intelligibility of synthesized speech. The proposed model is trained on an IndicTTS Punjabi corpus and evaluated using an NVIDIA GTX 1080 GPU and an Intel Core i7 12th Gen CPU-powered system. We conducted a comparative analysis (e.g., subjective, objective, and quantitative metrics) with several state-of-the-art neural vocoders to validate the effectiveness of BAANI. It achieved 4.18 on the Mean Opinion Score (MOS). On the other side, from five different objective measures, all measures surpass the current SOTA models. Furthermore, BAANI generates 22.05 kHz speech with real-time factors (RTF) of $3.2 \times$ and $1.5 \times$ on the NVIDIA GTX 1080 GPU and the Intel Core i7-12700 CPU, respectively, demonstrating its practical deployment potential. Notably, the vocoder effectively preserves high-frequency harmonics and pitch (i.e., $F_{0}$) contours, aligning closely with the perceptual preferences of native Punjabi speakers.

</details>

### [KrishokBondhu: A Retrieval-Augmented Voice-Based Agricultural Advisory Call Center for Bengali Farmers](2510.18355.md)
**Mohd Ruhul Ameen, Akif Islam, Farjana Aktar, M. Saifuzzaman Rafat** · 2025-10-21

<details>
<summary>Abstract</summary>

In Bangladesh, many farmers still struggle to access timely, expert-level agricultural guidance. This paper presents KrishokBondhu, a voice-enabled, call-centre-integrated advisory platform built on a Retrieval-Augmented Generation (RAG) framework for Bengali-speaking farmers. The system combines agricultural handbooks, extension manuals, and NGO publications, processes them through an OCR-based pipeline, and indexes the curated content in a vector database for semantic retrieval. Through a phone-based interface, farmers can receive real-time, context-aware advice: speech-to-text converts the Bengali query, the RAG module retrieves relevant information, a large language model (Gemma 3-4B) generates a grounded response, and text-to-speech delivers the answer in spoken Bengali. In a pilot evaluation, KrishokBondhu produced high-quality responses for 72.7% of diverse agricultural queries. Compared to the KisanQRS benchmark, it achieved a composite score of 4.53 versus 3.13 on a 5-point scale, with a 44.7% improvement and especially large gains in contextual richness and completeness, while maintaining comparable relevance and technical specificity. Semantic-similarity analysis further showed a strong correlation between retrieved context and answer quality. KrishokBondhu demonstrates the feasibility of combining call-centre accessibility, multilingual voice interaction, and modern RAG techniques to deliver expert-level agricultural guidance to remote Bangladeshi farmers.

</details>

### [ParaStyleTTS: Toward Efficient and Robust Paralinguistic Style Control for Expressive Text-to-Speech Generation](2510.18308.md)
**Haowei Lou, Hye-Young Paik, Wen Hu, Lina Yao** · 2025-10-21

<details>
<summary>Abstract</summary>

Controlling speaking style in text-to-speech (TTS) systems has become a growing focus in both academia and industry. While many existing approaches rely on reference audio to guide style generation, such methods are often impractical due to privacy concerns and limited accessibility. More recently, large language models (LLMs) have been used to control speaking style through natural language prompts; however, their high computational cost, lack of interpretability, and sensitivity to prompt phrasing limit their applicability in real-time and resource-constrained environments. In this work, we propose ParaStyleTTS, a lightweight and interpretable TTS framework that enables expressive style control from text prompts alone. ParaStyleTTS features a novel two-level style adaptation architecture that separates prosodic and paralinguistic speech style modeling. It allows fine-grained and robust control over factors such as emotion, gender, and age. Unlike LLM-based methods, ParaStyleTTS maintains consistent style realization across varied prompt formulations and is well-suited for real-world applications, including on-device and low-resource deployment. Experimental results show that ParaStyleTTS generates high-quality speech with performance comparable to state-of-the-art LLM-based systems while being 30x faster, using 8x fewer parameters, and requiring 2.5x less CUDA memory. Moreover, ParaStyleTTS exhibits superior robustness and controllability over paralinguistic speaking styles, providing a practical and efficient solution for style-controllable text-to-speech generation. Demo can be found at https://parastyletts.github.io/ParaStyleTTS_Demo/. Code can be found at https://github.com/haoweilou/ParaStyleTTS.

</details>

### [U-Codec: Ultra Low Frame-rate Neural Speech Codec for Fast High-fidelity Speech Generation](2510.16718.md)
**Xusheng Yang et.al.** · 2025-10-19

### [SAC: Neural Speech Codec with Semantic-Acoustic Dual-Stream Quantization](2510.16841.md)
**Wenxi Chen, Xinsheng Wang, Ruiqi Yan, Yushen Chen et al.** · 2025-10-19

<details>
<summary>Abstract</summary>

Speech codecs that convert continuous speech signals into discrete tokens have become essential for speech language models. However, existing codecs struggle to balance high-quality reconstruction with semantically rich representations, limiting their effectiveness in both generative and understanding tasks. In this work, we propose SAC, a neural speech codec with semantic-acoustic dual-stream quantization. By disentangling semantic and acoustic modeling into two dedicated streams, SAC enables each to be optimized for its respective role. Comprehensive evaluations show that SAC achieves strong reconstruction performance across diverse bitrates under both clean and noisy conditions, with particularly high scores on UTMOS and WER, indicating superior naturalness and intelligibility. Moreover, SAC substantially surpasses prior codecs in semantic representation, approaching the level of continuous self-supervised embeddings. When used as a tokenizer for LLM-based text-to-speech, SAC enables a single-stage autoregressive (AR) TTS model that clearly outperforms state-of-the-art AR systems. Our disentanglement analysis further validates the effectiveness of the dual-stream design, offering new potential for controllable speech generation.

</details>

### [Edge-Based Speech Transcription and Synthesis for Kinyarwanda and Swahili Languages](2510.16497.md)
**Pacome Simon Mbonimpa, Diane Tuyizere, Azizuddin Ahmed Biyabani, Ozan K. Tonguz** · 2025-10-18

<details>
<summary>Abstract</summary>

This paper presents a novel framework for speech transcription and synthesis, leveraging edge-cloud parallelism to enhance processing speed and accessibility for Kinyarwanda and Swahili speakers. It addresses the scarcity of powerful language processing tools for these widely spoken languages in East African countries with limited technological infrastructure. The framework utilizes the Whisper and SpeechT5 pre-trained models to enable speech-to-text (STT) and text-to-speech (TTS) translation. The architecture uses a cascading mechanism that distributes the model inference workload between the edge device and the cloud, thereby reducing latency and resource usage, benefiting both ends. On the edge device, our approach achieves a memory usage compression of 9.5% for the SpeechT5 model and 14% for the Whisper model, with a maximum memory usage of 149 MB. Experimental results indicate that on a 1.7 GHz CPU edge device with a 1 MB/s network bandwidth, the system can process a 270-character text in less than a minute for both speech-to-text and text-to-speech transcription. Using real-world survey data from Kenya, it is shown that the cascaded edge-cloud architecture proposed could easily serve as an excellent platform for STT and TTS transcription with good accuracy and response time.

</details>

### [RLAIF-SPA: Optimizing LLM-based Emotional Speech Synthesis via RLAIF](2510.14628.md)
**Qing Yang et.al.** · 2025-10-16

### [TASLA: Text-Aligned Speech Tokens with Multiple Layer-Aggregation](2510.14934.md)
**Ming-Hao Hsu, Liang-Hsuan Tseng, Hung-yi Lee, Zhizheng Wu** · 2025-10-16

<details>
<summary>Abstract</summary>

We propose Text-Aligned Speech Tokens with Multiple Layer-Aggregation (TASLA), which is a text-aligned speech tokenization framework that aims to address the problem that under a low-frame-rate and text-aligned regime, single-source speech tokens may lose acoustic details during reconstruction. On the other hand, this paper further explains how different encoder layers collaborate to capture comprehensive acoustic features for tokenization. Previous work, TASTE, proposed the text-aligned speech tokenization framework, which is a LM-friendly architecture, but struggles to capture acoustic details. We address this trade-off with two components: Multi-Layer Dynamic Attention (MLDA), which lets each text position adaptively mix shallow/deep features from a frozen speech encoder, and Finite Scalar Quantization (FSQ), a simple per-dimension discretization with smooth optimization. At about 2.62 Hz (tokens/s), TASLA consistently improves prosody and achieves competitive quality over TASTE on in-domain (LibriSpeech) and OOD (EXPRESSO, Voxceleb) sets. We further demonstrate that dynamic layer mixing is correlated with spectral flux and explains why MLDA preserves prosody under a low frame rate with extreme feature compression.

</details>

### [DiSTAR: Diffusion over a Scalable Token Autoregressive Representation for Speech Generation](2510.12210.md)
**Yakun Song et.al.** · 2025-10-15

### [Closing the Gap Between Text and Speech Understanding in LLMs](2510.13632.md)
**Santiago Cuervo, Skyler Seto, Maureen de Seyssel, Richard He Bai et al.** · 2025-10-15

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) can be adapted to extend their text capabilities to speech inputs. However, these speech-adapted LLMs consistently underperform their text-based counterparts--and even cascaded pipelines--on language understanding tasks. We term this shortfall the text-speech understanding gap: the performance drop observed when a speech-adapted LLM processes spoken inputs relative to when the original text-based LLM processes the equivalent text. Recent approaches to narrowing this gap either rely on large-scale speech synthesis of text corpora, which is costly and heavily dependent on synthetic data, or on large-scale proprietary speech datasets, which are not reproducible. As a result, there remains a need for more data-efficient alternatives for closing the text-speech understanding gap. In this work, we analyze the gap as driven by two factors: (i) forgetting of text capabilities during adaptation, and (ii) cross-modal misalignment between speech and text. Based on this analysis, we introduce SALAD--Sample-efficient Alignment with Learning through Active selection and cross-modal Distillation--which combines cross-modal distillation with targeted synthetic data to improve alignment while mitigating forgetting. Applied to 3B and 7B LLMs, SALAD achieves competitive performance with a strong open-weight model across broad-domain benchmarks in knowledge, language understanding, and reasoning, while training on over an order of magnitude less speech data from public corpora.

</details>

### [Cross-modal Consistency Guidance for Robust Emotion Control in Auto-Regressive TTS Models](2510.13293.md)
**Yizhou Peng, Yukun Ma, Chong Zhang, Yi-Wen Chao et al.** · 2025-10-15

<details>
<summary>Abstract</summary>

While Text-to-Speech (TTS) systems enable emotional control via natural-language instructions, expressiveness, naturalness, and speech quality degrade when the target emotion conflicts with the textual semantics. We propose a Cross-modal Consistency Guided Classifier-Free Guidance (CCG-CFG) method with dynamic scales based on the degree of inconsistency between the text emotion and the explicit speech emotion, replacing the dropout condition with the text emotion. We also distill the CCG-CFG guidance signal using a hard-sample mining strategy, improving the TTS model's emotional alignment capability. Evaluations on five emotional corpora and two TTS benchmarks show that our approaches applied to CosyVoice2 achieve up to a 12% absolute improvement in emotion-recognition accuracy and a 10% relative improvement in subjective scores, outperforming baselines including HierSpeech++, Qwen3-TTS, and original CosyVoice2, while preserving intelligibility, naturalness, and high speech quality.

</details>

### [InteractiveOmni: A Unified Omni-modal Model for Audio-Visual Multi-turn Dialogue](2510.13747.md)
**Wenwen Tong, Hewei Guo, Dongchuan Ran, Jiangnan Chen et al.** · 2025-10-15

<details>
<summary>Abstract</summary>

We introduce InteractiveOmni, a unified and open-source omni-modal large language model for audio-visual multi-turn interaction, ranging from 4B to 8B parameters, designed to lead the field of lightweight models by offering comprehensive omni-modal understanding and speech generation capabilities. To achieve this, we integrate the vision encoder, audio encoder, large language model, and speech decoder into a unified model for understanding and generation tasks. We design a multi-stage training strategy to ensure robust cross-modal capabilities, including pre-training for omni-modal understanding, followed by post-training with speech conversation and audio-visual interaction. To enable human-like long-term conversational ability, we meticulously curate a multi-turn training dataset that enhances the model's ability to handle complex and multi-turn interactions. To effectively evaluate the multi-turn memory and speech interaction capabilities, we construct the multi-modal multi-turn memory benchmark and the multi-turn speech interaction benchmark. Experiments demonstrate that InteractiveOmni significantly outperforms leading open-source models and provides a more intelligent multi-turn audio-visual experience, particularly in its long-term memory capabilities. Notably, InteractiveOmni-4B is comparable to the much larger model like Qwen2.5-Omni-7B on general benchmarks, and it can retain 97% of the performance of the InteractiveOmni-8B while utilizing only 50% of the model size. Achieving state-of-the-art results against similarly sized models across image, audio, video understanding, and speech generation tasks, InteractiveOmni is an accessible, open-source foundation for next-generation intelligent interactive systems.

</details>

### [Continuous-Token Diffusion for Speaker-Referenced TTS in Multimodal LLMs](2510.12995.md)
**Xinlu He et.al.** · 2025-10-14

### [ParsVoice: A Large-Scale Multi-Speaker Persian Speech Corpus for Text-to-Speech Synthesis](2510.10774.md)
**Mohammad Javad Ranjbar Kalahroodi et.al.** · 2025-10-14

### [Understanding the Modality Gap: An Empirical Study on the Speech-Text Alignment Mechanism of Large Speech Language Models](2510.12116.md)
**Bajian Xiang, Shuaijiang Zhao, Tingwei Guo, Wei Zou** · 2025-10-14

<details>
<summary>Abstract</summary>

End-to-end Large Speech Language Models (LSLMs) have demonstrated impressive conversational generation abilities, yet consistently fall short of traditional pipeline systems on semantic understanding benchmarks. In this work, we reveal through systematic experimentation that although LSLMs lose some text input performance after speech-text alignment training, the performance gap between speech and text inputs is more pronounced, which we refer to as the modality gap. To understand this gap, we analyze both coarse- and fine-grained text and speech representations. At the coarse-grained level, representations of speech and text in deeper layers are found to be increasingly aligned in direction (cosine similarity), while concurrently diverging in magnitude (Euclidean distance). We further find that representation similarity is strongly correlated with the modality gap. At the fine-grained level, a spontaneous token-level alignment pattern between text and speech representations is observed. Based on this, we introduce the Alignment Path Score to quantify token-level alignment quality, which exhibits stronger correlation with the modality gap. Building on these insights, we design targeted interventions on critical tokens through angle projection and length normalization. These strategies demonstrate the potential to improve correctness for speech inputs. Our study provides the first systematic empirical analysis of the modality gap and alignment mechanisms in LSLMs, offering both theoretical and methodological guidance for future optimization.

</details>

### [VCTR: A Transformer-Based Model for Non-parallel Voice Conversion](2510.12964.md)
**Maharnab Saikia** · 2025-10-14

<details>
<summary>Abstract</summary>

Non-parallel voice conversion aims to convert voice from a source domain to a target domain without paired training data. Cycle-Consistent Generative Adversarial Networks (CycleGAN) and Variational Autoencoders (VAE) have been used for this task, but these models suffer from difficult training and unsatisfactory results. Later, Contrastive Voice Conversion (CVC) was introduced, utilizing a contrastive learning-based approach to address these issues. However, these methods use CNN-based generators, which can capture local semantics but lacks the ability to capture long-range dependencies necessary for global semantics. In this paper, we propose VCTR, an efficient method for non-parallel voice conversion that leverages the Hybrid Perception Block (HPB) and Dual Pruned Self-Attention (DPSA) along with a contrastive learning-based adversarial approach. The code can be found in https://github.com/Maharnab-Saikia/VCTR.

</details>

### [Beating Harmful Stereotypes Through Facts: RAG-based Counter-speech Generation](2510.12316.md)
**Greta Damo, Elena Cabrio, Serena Villata** · 2025-10-14

<details>
<summary>Abstract</summary>

Counter-speech generation is at the core of many expert activities, such as fact-checking and hate speech, to counter harmful content. Yet, existing work treats counter-speech generation as pure text generation task, mainly based on Large Language Models or NGO experts. These approaches show severe drawbacks due to the limited reliability and coherence in the generated countering text, and in scalability, respectively. To close this gap, we introduce a novel framework to model counter-speech generation as knowledge-wise text generation process. Our framework integrates advanced Retrieval-Augmented Generation (RAG) pipelines to ensure the generation of trustworthy counter-speech for 8 main target groups identified in the hate speech literature, including women, people of colour, persons with disabilities, migrants, Muslims, Jews, LGBT persons, and other. We built a knowledge base over the United Nations Digital Library, EUR-Lex and the EU Agency for Fundamental Rights, comprising a total of 32,792 texts. We use the MultiTarget-CONAN dataset to empirically assess the quality of the generated counter-speech, both through standard metrics (i.e., JudgeLM) and a human evaluation. Results show that our framework outperforms standard LLM baselines and competitive approach, on both assessments. The resulting framework and the knowledge base pave the way for studying trustworthy and sound counter-speech generation, in hate speech and beyond.

</details>

### [BridgeCode: A Dual Speech Representation Paradigm for Autoregressive Zero-Shot Text-to-Speech Synthesis](2510.11646.md)
**Jingyuan Xing et.al.** · 2025-10-13

### [Perturbation Self-Supervised Representations for Cross-Lingual Emotion TTS: Stage-Wise Modeling of Emotion and Speaker](2510.11124.md)
**Cheng Gong et.al.** · 2025-10-13

### [Gelina: Unified Speech and Gesture Synthesis via Interleaved Token Prediction](2510.12834.md)
**Téo Guichoux, Th'eodor Lemerle, Shivam Mehta, Jonas Beskow et al.** · 2025-10-13

<details>
<summary>Abstract</summary>

Human communication is multimodal, with speech and gestures tightly coupled, yet most computational methods for generating speech and gestures synthesize them sequentially, weakening synchrony and prosody alignment. We introduce Gelina, a unified framework that jointly synthesizes speech and co-speech gestures from text using interleaved token sequences in a discrete autoregressive backbone, with modality-specific decoders. Gelina supports multi-speaker and multi-style cloning and enables gesture-only synthesis from speech inputs. Subjective and objective evaluations demonstrate competitive speech quality and improved gesture generation over unimodal baselines.

</details>

### [MRSAudio: A Large-Scale Multimodal Recorded Spatial Audio Dataset with Refined Annotations](2510.10396.md)
**Wenxiang Guo, Changhao Pan, Zhiyuan Zhu, Xintong Hu et al.** · 2025-10-12

<details>
<summary>Abstract</summary>

Humans rely on multisensory integration to perceive spatial environments, where auditory cues enable sound source localization in three-dimensional space. Despite the critical role of spatial audio in immersive technologies such as VR/AR, most existing multimodal datasets provide only monaural audio, which limits the development of spatial audio generation and understanding. To address these challenges, we introduce MRSAudio, a large-scale multimodal spatial audio dataset designed to advance research in spatial audio understanding and generation. MRSAudio spans four distinct components: MRSLife, MRSSpeech, MRSMusic, and MRSSing, covering diverse real-world scenarios. The dataset includes synchronized binaural and ambisonic audio, exocentric and egocentric video, motion trajectories, and fine-grained annotations such as transcripts, phoneme boundaries, lyrics, scores, and prompts. To demonstrate the utility and versatility of MRSAudio, we establish five foundational tasks: audio spatialization, and spatial text to speech, spatial singing voice synthesis, spatial music generation and sound event localization and detection. Results show that MRSAudio enables high-quality spatial modeling and supports a broad range of spatial audio research. Demos and dataset access are available at https://mrsaudio.github.io.

</details>

### [Mind-Paced Speaking: A Dual-Brain Approach to Real-Time Reasoning in Spoken Language Models](2510.09592.md)
**Donghang Wu et.al.** · 2025-10-10

### [O_O-VC: Synthetic Data-Driven One-to-One Alignment for Any-to-Any Voice Conversion](2510.09061.md)
**Huu Tuong Tu et.al.** · 2025-10-10

### [DiTSinger: Scaling Singing Voice Synthesis with Diffusion Transformer and Implicit Alignment](2510.09016.md)
**Zongcai Du et.al.** · 2025-10-10

### [SynthVC: Leveraging Synthetic Data for End-to-End Low Latency Streaming Voice Conversion](2510.09245.md)
**Zhao Guo, Ziqian Ning, Guobin Ma, Lei Xie** · 2025-10-10

<details>
<summary>Abstract</summary>

Voice Conversion (VC) aims to modify a speaker's timbre while preserving linguistic content. While recent VC models achieve strong performance, most struggle in real-time streaming scenarios due to high latency, dependence on ASR modules, or complex speaker disentanglement, which often results in timbre leakage or degraded naturalness. We present SynthVC, a streaming end-to-end VC framework that directly learns speaker timbre transformation from synthetic parallel data generated by a pre-trained zero-shot VC model. This design eliminates the need for explicit content-speaker separation or recognition modules. Built upon a neural audio codec architecture, SynthVC supports low-latency streaming inference with high output fidelity. Experimental results show that SynthVC outperforms baseline streaming VC systems in both naturalness and speaker similarity, achieving an end-to-end latency of just 77.1 ms.

</details>

### [DialoSpeech: Dual-Speaker Dialogue Generation with LLM and Flow Matching](2510.08373.md)
**Hanke Xie, Dake Guo, Chengyou Wang, Yue Li et al.** · 2025-10-09

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) synthesis, particularly those leveraging large language models (LLMs), have significantly improved expressiveness and naturalness. However, generating human-like, interactive dialogue speech remains challenging. Current systems face limitations due to the scarcity of dual-track data and difficulties in achieving naturalness, contextual coherence, and interactional dynamics, such as turn-taking, overlapping speech, and speaker consistency, in multi-turn conversations. To address these challenges, we propose DialoSpeech, a dual-track architecture combining a large language model with Chunked Flow Matching for expressive, human-like dialogue speech synthesis. DialoSpeech generates natural multi-turn conversations with coherent speaker turns and natural overlaps, supporting both Chinese and English and cross-lingual speech synthesis. We introduce a data processing pipeline to construct dual-track dialogue datasets, facilitating scalable training and experimental validation. Experiments show that our model outperforms baselines, offering a solution for generating human-like spoken dialogues. Audio samples are available at https://tiamojames.github.io/DialoSpeech

</details>

### [IntMeanFlow: Few-step Speech Generation with Integral Velocity Distillation](2510.07979.md)
**Wei Wang, Rong Cao, Yi Guo, Zhengyang Chen et al.** · 2025-10-09

<details>
<summary>Abstract</summary>

Flow-based generative models have greatly improved text-to-speech (TTS) synthesis quality, but inference speed remains limited by the iterative sampling process and multiple function evaluations (NFE). The recent MeanFlow model accelerates generation by modeling average velocity instead of instantaneous velocity. However, its direct application to TTS encounters challenges, including GPU memory overhead from Jacobian-vector products (JVP) and training instability due to self-bootstrap processes. To address these issues, we introduce IntMeanFlow, a framework for few-step speech generation with integral velocity distillation. By approximating average velocity with the teacher's instantaneous velocity over a temporal interval, IntMeanFlow eliminates the need for JVPs and self-bootstrap, improving stability and reducing GPU memory usage. We also propose the Optimal Step Sampling Search (O3S) algorithm, which identifies the model-specific optimal sampling steps, improving speech synthesis without additional inference overhead. Experiments show that IntMeanFlow achieves 1-NFE inference for token-to-spectrogram and 3-NFE for text-to-spectrogram tasks while maintaining high-quality synthesis. Demo samples are available at https://vvwangvv.github.io/intmeanflow.

</details>

### [MeanVC: Lightweight and Streaming Zero-Shot Voice Conversion via Mean Flows](2510.08392.md)
**Guobin Ma, Jixun Yao, Ziqian Ning, Yuepeng Jiang et al.** · 2025-10-09

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) aims to transfer timbre from a source speaker to any unseen target speaker while preserving linguistic content. Growing application scenarios demand models with streaming inference capabilities. This has created a pressing need for models that are simultaneously fast, lightweight, and high-fidelity. However, existing streaming methods typically rely on either autoregressive (AR) or non-autoregressive (NAR) frameworks, which either require large parameter sizes to achieve strong performance or struggle to generalize to unseen speakers. In this study, we propose MeanVC, a lightweight and streaming zero-shot VC approach. MeanVC introduces a diffusion transformer with a chunk-wise autoregressive denoising strategy, combining the strengths of both AR and NAR paradigms for efficient streaming processing. By introducing mean flows, MeanVC regresses the average velocity field during training, enabling zero-shot VC with superior speech quality and speaker similarity in a single sampling step by directly mapping from the start to the endpoint of the flow trajectory. Additionally, we incorporate diffusion adversarial post-training to mitigate over-smoothing and further enhance speech quality. Experimental results demonstrate that MeanVC significantly outperforms existing zero-shot streaming VC systems, achieving superior conversion quality with higher efficiency and significantly fewer parameters. Audio demos and code are publicly available at https://aslp-lab.github.io/MeanVC.

</details>

### [VoiceAgentBench: Are Voice Assistants ready for agentic tasks?](2510.07978.md)
**Dhruv Jain, Harshit Shukla, Gautam Rajeev, Ashish Kulkarni et al.** · 2025-10-09

<details>
<summary>Abstract</summary>

Large scale Speech Language Models have enabled voice assistants capable of understanding natural spoken queries and performing complex tasks. However, existing speech benchmarks largely focus on isolated capabilities such as transcription or question answering and do not systematically evaluate agentic behavior or adversarial robustness. To address this, we introduce VoiceAgentBench, a comprehensive benchmark for evaluating SpeechLMs in realistic spoken agentic settings, comprising 6,000+ synthetic spoken queries spanning single-tool invocations, multi-tool workflows, multi-turn dialogue, and safety evaluations across English and six Indic languages. To ensure speaker diversity, we further simulate speaker variability using a novel sampling strategy that selects audios for TTS voice conversion based on speaker embeddings to maximize acoustic diversity. Our evaluation measures tool selection accuracy, structural consistency, and the correctness of tool invocations, including adversarial robustness. Across agentic tasks, ASR-LLM pipelines outperform end-to-end SpeechLMs, achieving up to 60.6% average parameter-filling accuracy on English, while SpeechLMs exhibit lower performance and sharper degradation on Indic languages. All models struggle in sequential workflows and safety evaluations, highlighting persistent limitations in tool orchestration, multilingual generalization, and safety robustness. VoiceAgentBench is publicly available on Hugging Face at https://huggingface.co/datasets/krutrim-ai-labs/VoiceAgentBench, and the codebase is released at https://github.com/ola-krutrim/VoiceAgentBench.

</details>

### [Making Machines Sound Sarcastic: LLM-Enhanced and Retrieval-Guided Sarcastic Speech Synthesis](2510.07096.md)
**Zhu Li et.al.** · 2025-10-08

### [Position: Towards Responsible Evaluation for Text-to-Speech](2510.06927.md)
**Yifan Yang, Hui Wang, Bing Han, Shujie Liu et al.** · 2025-10-08

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) technology have enabled systems to generate speech that is often indistinguishable from human speech, bringing benefits to accessibility, content creation, and human-computer interaction. However, current evaluation practices are increasingly inadequate for capturing the full range of capabilities, limitations, and societal impacts of modern TTS systems. This position paper introduces the concept of Responsible Evaluation and argues that it is essential and urgent for the next phase of TTS development, structured through three progressive levels: (1) ensuring the faithful and accurate reflection of a model's true capabilities and limitations, with more robust, discriminative, and comprehensive objective and subjective scoring methodologies; (2) enabling comparability, standardization, and transferability through standardized benchmarks, transparent reporting, and transferable evaluation metrics; and (3) assessing governance, fairness, and security concerns around data provenance, disparities, misuse, spoofing, and traceability. Through this concept, we critically examine current evaluation practices, identify systemic shortcomings, and propose actionable recommendations. We hope this concept will not only foster more reliable TTS technology but also guide its development toward ethically sound and societally beneficial applications.

</details>

### [Data-efficient Targeted Token-level Preference Optimization for LLM-based Text-to-Speech](2510.05799.md)
**Rikuto Kotoge et.al.** · 2025-10-07

### [ECTSpeech: Enhancing Efficient Speech Synthesis via Easy Consistency Tuning](2510.05984.md)
**Tao Zhu, Yinfeng Yu, Liejun Wang, Fuchun Sun et al.** · 2025-10-07

<details>
<summary>Abstract</summary>

Diffusion models have demonstrated remarkable performance in speech synthesis, but typically require multi-step sampling, resulting in low inference efficiency. Recent studies address this issue by distilling diffusion models into consistency models, enabling efficient one-step generation. However, these approaches introduce additional training costs and rely heavily on the performance of pre-trained teacher models. In this paper, we propose ECTSpeech, a simple and effective one-step speech synthesis framework that, for the first time, incorporates the Easy Consistency Tuning (ECT) strategy into speech synthesis. By progressively tightening consistency constraints on a pre-trained diffusion model, ECTSpeech achieves high-quality one-step generation while significantly reducing training complexity. In addition, we design a multi-scale gate module (MSGate) to enhance the denoiser's ability to fuse features at different scales. Experimental results on the LJSpeech dataset demonstrate that ECTSpeech achieves audio quality comparable to state-of-the-art methods under single-step sampling, while substantially reducing the model's training cost and complexity.

</details>

### [Sparse deepfake detection promotes better disentanglement](2510.05696.md)
**Antoine Teissier, Marie Tahon, Nicolas Dugué, Aghilas Sini** · 2025-10-07

<details>
<summary>Abstract</summary>

Due to the rapid progress of speech synthesis, deepfake detection has become a major concern in the speech processing community. Because it is a critical task, systems must not only be efficient and robust, but also provide interpretable explanations. Among the different approaches for explainability, we focus on the interpretation of latent representations. In such paper, we focus on the last layer of embeddings of AASIST, a deepfake detection architecture. We use a TopK activation inspired by SAEs on this layer to obtain sparse representations which are used in the decision process. We demonstrate that sparse deepfake detection can improve detection performance, with an EER of 23.36% on ASVSpoof5 test set, with 95% of sparsity. We then show that these representations provide better disentanglement, using completeness and modularity metrics based on mutual information. Notably, some attacks are directly encoded in the latent space.

</details>

### [Investigation of perception inconsistency in speaker embedding for asynchronous voice anonymization](2510.05718.md)
**Rui Wang, Liping Chen, Kong Aik Lee, Zhengpeng Zha et al.** · 2025-10-07

<details>
<summary>Abstract</summary>

Given the speech generation framework that represents the speaker attribute with an embedding vector, asynchronous voice anonymization can be achieved by modifying the speaker embedding derived from the original speech. However, the inconsistency between machine and human perceptions of the speaker attribute within the speaker embedding remains unexplored, limiting its performance in asynchronous voice anonymization. To this end, this study investigates this inconsistency via modifications to speaker embedding in the speech generation process. Experiments conducted on the FACodec and Diff-HierVC speech generation models discover a subspace whose removal alters machine perception while preserving its human perception of the speaker attribute in the generated speech. With these findings, an asynchronous voice anonymization is developed, achieving 100% human perception preservation rate while obscuring the machine perception. Audio samples can be found in https://voiceprivacy.github.io/speaker-embedding-eigen-decomposition/.

</details>

### [Teaching Machines to Speak Using Articulatory Control](2510.05619.md)
**Akshay Anand, Chenxu Guo, Cheol Jun Cho, Jiachen Lian et al.** · 2025-10-07

<details>
<summary>Abstract</summary>

Current speech production systems predominantly rely on large transformer models that operate as black boxes, providing little interpretability or grounding in the physical mechanisms of human speech. We address this limitation by proposing a new framework: speech generation through explicit articulatory control. This reframes speech as a motor control task similar to robotic manipulation. Our approach uses reinforcement learning to train a policy that directly controls the movements of vocal tract articulators, such as the tongue, lips, and jaw, to produce syllable-level speech. Specifically, we employ the Proximal Policy Optimization algorithm to learn optimal articulatory movements based on acoustic feedback provided by our audio perceiver, Sylber. The resulting articulatory trajectories are decoded into audio using SPARC, a pre-trained articulatory-to-speech decoder. We train this framework on six target syllables, and it demonstrates successful convergence, with similarity scores between the policy-generated audio and the target syllables exceeding 0.85. Accurate human transcription of the audio for syllables such as "please", "loot", and "cat" demonstrates the intelligibility of this framework.

</details>

### [Speak, Edit, Repeat: High-Fidelity Voice Editing and Zero-Shot TTS with Cross-Attentive Mamba](2510.04738.md)
**Baher Mohammad et.al.** · 2025-10-06

### [UniVoice: Unifying Autoregressive ASR and Flow-Matching based TTS with Large Language Models](2510.04593.md)
**Wenhao Guan et.al.** · 2025-10-06

### [Paper2Video: Automatic Video Generation from Scientific Papers](2510.05096.md)
**Zeyu Zhu, Kevin Qinghong Lin, Mike Zheng Shou** · 2025-10-06

<details>
<summary>Abstract</summary>

Academic presentation videos have become an essential medium for research communication, yet producing them remains highly labor-intensive, often requiring hours of slide design, recording, and editing for a short 2 to 10 minutes video. Unlike natural video, presentation video generation involves distinctive challenges: inputs from research papers, dense multi-modal information (text, figures, tables), and the need to coordinate multiple aligned channels such as slides, subtitles, speech, and human talker. To address these challenges, we introduce Paper2Video, the first benchmark of 101 research papers paired with author-created presentation videos, slides, and speaker metadata. We further design four tailored evaluation metrics--Meta Similarity, PresentArena, PresentQuiz, and IP Memory--to measure how videos convey the paper's information to the audience. Building on this foundation, we propose PaperTalker, the first multi-agent framework for academic presentation video generation. It integrates slide generation with effective layout refinement by a novel effective tree search visual choice, cursor grounding, subtitling, speech synthesis, and talking-head rendering, while parallelizing slide-wise generation for efficiency. Experiments on Paper2Video demonstrate that the presentation videos produced by our approach are more faithful and informative than existing baselines, establishing a practical step toward automated and ready-to-use academic video generation. Our dataset, agent, and code are available at https://github.com/showlab/Paper2Video.

</details>

### [GDiffuSE: Diffusion-based speech enhancement with noise model guidance](2510.04157.md)
**Efrayim Yanir, David Burshtein, Sharon Gannot** · 2025-10-05

<details>
<summary>Abstract</summary>

This paper introduces a novel speech enhancement (SE) approach based on a denoising diffusion probabilistic model (DDPM), termed Guided diffusion for speech enhancement (GDiffuSE). In contrast to conventional methods that directly map noisy speech to clean speech, our method employs a lightweight helper model to estimate the noise distribution, which is then incorporated into the diffusion denoising process via a guidance mechanism. This design improves robustness by enabling seamless adaptation to unseen noise types and by leveraging large-scale DDPMs originally trained for speech generation in the context of SE. We evaluate our approach on noisy signals obtained by adding noise samples from the BBC sound effects database to LibriSpeech utterances, showing consistent improvements over state-of-the-art baselines under mismatched noise conditions. Examples are available at our project webpage.

</details>

### [Flamed-TTS: Flow Matching Attention-Free Models for Efficient Generating and Dynamic Pacing Zero-shot Text-to-Speech](2510.02848.md)
**Hieu-Nghia Huynh-Nguyen et.al.** · 2025-10-03

### [Synthetic Audio Forensics Evaluation (SAFE) Challenge](2510.03387.md)
**Kirill Trapeznikov, Paul Cummer, Pranay Pherwani, Jai Aslam et al.** · 2025-10-03

<details>
<summary>Abstract</summary>

The increasing realism of synthetic speech generated by advanced text-to-speech (TTS) models, coupled with post-processing and laundering techniques, presents a significant challenge for audio forensic detection. In this paper, we introduce the SAFE (Synthetic Audio Forensics Evaluation) Challenge, a fully blind evaluation framework designed to benchmark detection models across progressively harder scenarios: raw synthetic speech, processed audio (e.g., compression, resampling), and laundered audio intended to evade forensic analysis. The SAFE challenge consisted of a total of 90 hours of audio and 21,000 audio samples split across 21 different real sources and 17 different TTS models and 3 tasks. We present the challenge, evaluation design and tasks, dataset details, and initial insights into the strengths and limitations of current approaches, offering a foundation for advancing synthetic audio detection research. More information is available at \href{https://stresearch.github.io/SAFE/}{https://stresearch.github.io/SAFE/}.

</details>

### [MOSS-Speech: Towards True Speech-to-Speech Models Without Text Guidance](2510.00499.md)
**Xingjian Zhao et.al.** · 2025-10-02

### [Emotional Text-To-Speech Based on Mutual-Information-Guided Emotion-Timbre Disentanglement](2510.01722.md)
**Jianing Yang, Sheng Li, Takahiro Shinozaki, Yuki Saito et al.** · 2025-10-02

<details>
<summary>Abstract</summary>

Current emotional Text-To-Speech (TTS) and style transfer methods rely on reference encoders to control global style or emotion vectors, but do not capture nuanced acoustic details of the reference speech. To this end, we propose a novel emotional TTS method that enables fine-grained phoneme-level emotion embedding prediction while disentangling intrinsic attributes of the reference speech. The proposed method employs a style disentanglement method to guide two feature extractors, reducing mutual information between timbre and emotion features, and effectively separating distinct style components from the reference speech. Experimental results demonstrate that our method outperforms baseline TTS systems in generating natural and emotionally rich speech. This work highlights the potential of disentangled and fine-grained representations in advancing the quality and flexibility of emotional TTS systems.

</details>

### [UniverSR: Unified and Versatile Audio Super-Resolution via Vocoder-Free Flow Matching](2510.00771.md)
**Woongjib Choi, Sangmin Lee, Hyungseob Lim, Hong-Goo Kang** · 2025-10-01

<details>
<summary>Abstract</summary>

In this paper, we present a vocoder-free framework for audio super-resolution that employs a flow matching generative model to capture the conditional distribution of complex-valued spectral coefficients. Unlike conventional two-stage diffusion-based approaches that predict a mel-spectrogram and then rely on a pre-trained neural vocoder to synthesize waveforms, our method directly reconstructs waveforms via the inverse Short-Time Fourier Transform (iSTFT), thereby eliminating the dependence on a separate vocoder. This design not only simplifies end-to-end optimization but also overcomes a critical bottleneck of two-stage pipelines, where the final audio quality is fundamentally constrained by vocoder performance. Experiments show that our model consistently produces high-fidelity 48 kHz audio across diverse upsampling factors, achieving state-of-the-art performance on both speech and general audio datasets.

</details>

### [From Scores to Preferences: Redefining MOS Benchmarking for Speech Quality Reward Modeling](2510.00743.md)
**Yifei Cao, Changhao Jiang, Jiabao Zhuang, Jiajun Sun et al.** · 2025-10-01

<details>
<summary>Abstract</summary>

Assessing the perceptual quality of synthetic speech is crucial for guiding the development and refinement of speech generation models. However, it has traditionally relied on human subjective ratings such as the Mean Opinion Score (MOS), which depend on manual annotations and often suffer from inconsistent rating standards and poor reproducibility. To address these limitations, we introduce MOS-RMBench, a unified benchmark that reformulates diverse MOS datasets into a preference-comparison setting, enabling rigorous evaluation across different datasets. Building on MOS-RMBench, we systematically construct and evaluate three paradigms for reward modeling: scalar reward models, semi-scalar reward models, and generative reward models (GRMs). Our experiments reveal three key findings: (1) scalar models achieve the strongest overall performance, consistently exceeding 74% accuracy; (2) most models perform considerably worse on synthetic speech than on human speech; and (3) all models struggle on pairs with very small MOS differences. To improve performance on these challenging pairs, we propose a MOS-aware GRM that incorporates an MOS-difference-based reward function, enabling the model to adaptively scale rewards according to the difficulty of each sample pair. Experimental results show that the MOS-aware GRM significantly improves fine-grained quality discrimination and narrows the gap with scalar models on the most challenging cases. We hope this work will establish both a benchmark and a methodological framework to foster more rigorous and scalable research in automatic speech quality assessment.

</details>

### [BatonVoice: An Operationalist Framework for Enhancing Controllable Speech Synthesis with Linguistic Intelligence from LLMs](2509.26514.md)
**Yue Wang et.al.** · 2025-09-30

### [HiStyle: Hierarchical Style Embedding Predictor for Text-Prompt-Guided Controllable Speech Synthesis](2509.25842.md)
**Ziyu Zhang et.al.** · 2025-09-30

### [Optimizing Speech Language Models for Acoustic Consistency](2509.26276.md)
**Morteza Rohanian, Michael Krauthammer** · 2025-09-30

<details>
<summary>Abstract</summary>

We study speech language models that incorporate semantic initialization and planning losses to achieve robust and consistent generation. Our approach initializes speech tokens with self-supervised features, applies a light alignment loss, and trains with thinning and auxiliary objectives that target robustness and content planning. We train three models: a 0.7B speech-only model, a 1.0B speech-only model, and a 1.0B interleaved model with both text and speech. Acoustic studies show that the speech-only models achieve the highest consistency across speaker, gender, sentiment, room, and background factors, surpassing larger systems. Interleaving improves lexical and syntactic probes and semantic--acoustic alignment but reduces consistency. Linear probes show that our initialization biases the model toward content structure while trading off prosody detail. These results show that LM-side design and training mix control the balance between acoustic stability and semantic grounding without changes to the tokenizer or runtime architecture. A demo and model weights are available for exploration.

</details>

### [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](2509.25670.md)
**Kang Yang, Yifan Liang, Fangkun Liu, Zhenping Xie et al.** · 2025-09-30

<details>
<summary>Abstract</summary>

Lip-to-speech (L2S) synthesis for Mandarin is a significant challenge, hindered by complex viseme-to-phoneme mappings and the critical role of lexical tones in intelligibility. To address this issue, we propose Lexical Tone-Aware Lip-to-Speech (LTA-L2S). To tackle viseme-to-phoneme complexity, our model adapts an English pre-trained audio-visual self-supervised learning (SSL) model via a cross-lingual transfer learning strategy. This strategy not only transfers universal knowledge learned from extensive English data to the Mandarin domain but also circumvents the prohibitive cost of training such a model from scratch. To specifically model lexical tones and enhance intelligibility, we further employ a flow-matching model to generate the F0 contour. This generation process is guided by ASR-fine-tuned SSL speech units, which contain crucial suprasegmental information. The overall speech quality is then elevated through a two-stage training paradigm, where a flow-matching postnet refines the coarse spectrogram from the first stage. Extensive experiments demonstrate that LTA-L2S significantly outperforms existing methods in both speech intelligibility and tonal accuracy.

</details>

### [Emotion-Aligned Generation in Diffusion Text to Speech Models via Preference-Guided Optimization](2509.25416.md)
**Jiacheng Shi et.al.** · 2025-09-29

### [VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning](2509.24650.md)
**Yixuan Zhou et.al.** · 2025-09-29

### [Word-Level Emotional Expression Control in Zero-Shot Text-to-Speech Synthesis](2509.24629.md)
**Tianrui Wang et.al.** · 2025-09-29

### [UniFlow-Audio: Unified Flow Matching for Audio Generation from Omni-Modalities](2509.24391.md)
**Xuenan Xu et.al.** · 2025-09-29

### [VSSFlow: Unifying Video-conditioned Sound and Speech Generation via Joint Learning](2509.24773.md)
**Xin Cheng, Yuyue Wang, Xihua Wang, Yihan Wu et al.** · 2025-09-29

<details>
<summary>Abstract</summary>

Video-conditioned audio generation, including Video-to-Sound (V2S) and Visual Text-to-Speech (VisualTTS), has traditionally been treated as distinct tasks, leaving the potential for a unified generative framework largely underexplored. In this paper, we bridge this gap with VSSFlow, a unified flow-matching framework that seamlessly solve both problems. To effectively handle multiple input signals within a Diffusion Transformer (DiT) architecture, we propose a disentangled condition aggregation mechanism leveraging distinct intrinsic properties of attention layers: cross-attention for semantic conditions, and self-attention for temporally-intensive conditions. Besides, contrary to the prevailing belief that joint training for the two tasks leads to performance degradation, we demonstrate that VSSFlow maintains superior performance during end-to-end joint learning process. Furthermore, we use a straightforward feature-level data synthesis method, demonstrating that our framework provides a robust foundation that easily adapts to joint sound and speech generation using synthetic data. Extensive experiments on V2S, VisualTTS and joint generation benchmarks show that VSSFlow effectively unifies these tasks and surpasses state-of-the-art domain-specific baselines, underscoring the critical potential of unified generative models. Project page: https://vasflow1.github.io/vasflow/

</details>

### [ISSE: An Instruction-Guided Speech Style Editing Dataset And Benchmark](2509.24570.md)
**Yun Chen, Qi Chen, Zheqi Dai, Arshdeep Singh et al.** · 2025-09-29

<details>
<summary>Abstract</summary>

Speech style editing refers to modifying the stylistic properties of speech while preserving its linguistic content and speaker identity. However, most existing approaches depend on explicit labels or reference audio, which limits both flexibility and scalability. More recent attempts to use natural language descriptions remain constrained by oversimplified instructions and coarse style control. To address these limitations, we introduce an Instruction-guided Speech Style Editing Dataset (ISSE). The dataset comprises nearly 400 hours of speech and over 100,000 source-target pairs, each aligned with diverse and detailed textual editing instructions. We also build a systematic instructed speech data generation pipeline leveraging large language model, expressive text-to-speech and voice conversion technologies to construct high-quality paired samples. Furthermore, we train an instruction-guided autoregressive speech model on ISSE and evaluate it in terms of instruction adherence, timbre preservation, and content consistency. Experimental results demonstrate that ISSE enables accurate, controllable, and generalizable speech style editing compared to other datasets. The project page of ISSE is available at https://ychenn1.github.io/ISSE/.

</details>

### [MGM-Omni: Scaling Omni LLMs to Personalized Long-Horizon Speech](2509.25131.md)
**Chengyao Wang, Zhisheng Zhong, Bohao Peng, Senqiao Yang et al.** · 2025-09-29

<details>
<summary>Abstract</summary>

We present MGM-Omni, a unified Omni LLM for omni-modal understanding and expressive, long-horizon speech generation. Unlike cascaded pipelines that isolate speech synthesis, MGM-Omni adopts a "brain-mouth" design with a dual-track, token-based architecture that cleanly decouples multimodal reasoning from real-time speech generation. This design enables efficient cross-modal interaction and low-latency, streaming speech generation. For understanding, a unified training strategy coupled with a dual audio encoder design enables long-form audio perception across diverse acoustic conditions. For generation, a chunk-based parallel decoding scheme narrows the text speech token-rate gap, accelerating inference and supporting streaming zero-shot voice cloning with stable timbre over extended durations. Compared to concurrent work, MGM-Omni achieves these capabilities with markedly data-efficient training. Extensive experiments demonstrate that MGM-Omni outperforms existing open source models in preserving timbre identity across extended sequences, producing natural and context-aware speech, and achieving superior long-form audio and omnimodal understanding. MGM-Omni establishes an efficient, end-to-end paradigm for omnimodal understanding and controllable, personalised long-horizon speech generation.

</details>

### [Generalizable Speech Deepfake Detection via Information Bottleneck Enhanced Adversarial Alignment](2509.23618.md)
**Pu Huang, Shouguang Wang, Siya Yao, Mengchu Zhou** · 2025-09-28

<details>
<summary>Abstract</summary>

Neural speech synthesis techniques have enabled highly realistic speech deepfakes, posing major security risks. Speech deepfake detection is challenging due to distribution shifts across spoofing methods and variability in speakers, channels, and recording conditions. We explore learning shared discriminative features as a path to robust detection and propose Information Bottleneck enhanced Confidence-Aware Adversarial Network (IB-CAAN). Confidence-guided adversarial alignment adaptively suppresses attack-specific artifacts without erasing discriminative cues, while the information bottleneck removes nuisance variability to preserve transferable features. Experiments on ASVspoof 2019/2021, ASVspoof 5, and In-the-Wild demonstrate that IB-CAAN consistently outperforms baseline and achieves state-of-the-art performance on many benchmarks.

</details>

### [BFA: Real-time Multilingual Text-to-speech Forced Alignment](2509.23147.md)
**Abdul Rehman, Jingyao Cai, Jian-Jun Zhang, Xiaosong Yang** · 2025-09-27

<details>
<summary>Abstract</summary>

We present Bournemouth Forced Aligner (BFA), a system that combines a Contextless Universal Phoneme Encoder (CUPE) with a connectionist temporal classification (CTC)based decoder. BFA introduces explicit modelling of inter-phoneme gaps and silences and hierarchical decoding strategies, enabling fine-grained boundary prediction. Evaluations on TIMIT and Buckeye corpora show that BFA achieves competitive recall relative to Montreal Forced Aligner at relaxed tolerance levels, while predicting both onset and offset boundaries for richer temporal structure. BFA processes speech up to 240x faster than MFA, enabling faster than real-time alignment. This combination of speed and silence-aware alignment opens opportunities for interactive speech applications previously constrained by slow aligners.

</details>

### [SRC-IT2: Speech Rate-Controllable Mongolian Emotional Speech Synthesis Based on Improved Tacotron2](s2:9fa4c9823383bb29fc49e9c604e88325934b2ca3.md)
**Qingdaoerji Ren, Qian Bo, Chao Zhou, Yatu Ji et al.** · 2025-09-27

<details>
<summary>Abstract</summary>

To address the challenges of slow synthesis speed, unstable quality, limited emotional expressiveness, and the lack of controllable speaking rate in Mongolian emotional speech synthesis, this paper proposes a speech Rate-Controllable Mongolian emotional speech synthesis model based on improved Tacotron2 (SRC-IT2). First, an end-to-end Mongolian speech synthesis module is constructed based on an improved Tacotron2 framework, incorporating the unique linguistic characteristics of the Mongolian script. The front-end processing is optimized accordingly, and a G2P-Seq2Seq model is employed to achieve accurate grapheme-to-phoneme conversion for Mongolian characters. Next, on top of the end-to-end synthesis framework, a joint text-audio emotion analysis module is integrated to effectively learn and represent emotional style features specific to Mongolian speech. Finally, a style encoder and speaking rate control variable are embedded into the acoustic modeling process, further enhancing Tacotron2’s ability to dynamically adjust the speaking rate during emotional speech generation. Experimental results demonstrate that the proposed model produces more natural-sounding speech with improved emotional expressiveness and enables effective real-time control over speaking rate in Mongolian emotional speech synthesis.

</details>

### [Semantic-VAE: Semantic-Alignment Latent Representation for Better Speech Synthesis](2509.22167.md)
**Zhikang Niu et.al.** · 2025-09-26

### [Comprehend and Talk: Text to Speech Synthesis via Dual Language Modeling](2509.22062.md)
**Junjie Cao et.al.** · 2025-09-26

### [SPADE: Structured Pruning and Adaptive Distillation for Efficient LLM-TTS](2509.20802.md)
**Tan Dat Nguyen et.al.** · 2025-09-26

### [Speaker Anonymisation for Speech-based Suicide Risk Detection](2509.22148.md)
**Ziyun Cui, Sike Jia, Yang Lin, Yinan Duan et al.** · 2025-09-26

<details>
<summary>Abstract</summary>

Adolescent suicide is a critical global health issue, and speech provides a cost-effective modality for automatic suicide risk detection. Given the vulnerable population, protecting speaker identity is particularly important, as speech itself can reveal personally identifiable information if the data is leaked or maliciously exploited. This work presents the first systematic study of speaker anonymisation for speech-based suicide risk detection. A broad range of anonymisation methods are investigated, including techniques based on traditional signal processing, neural voice conversion, and speech synthesis. A comprehensive evaluation framework is built to assess the trade-off between protecting speaker identity and preserving information essential for suicide risk detection. Results show that combining anonymisation methods that retain complementary information yields detection performance comparable to that of original speech, while achieving protection of speaker identity for vulnerable populations.

</details>

### [Measuring Prosody Diversity in Zero-Shot TTS: A New Metric, Benchmark, and Exploration](2509.19928.md)
**Yifan Yang et.al.** · 2025-09-25

### [UniSS: Unified Expressive Speech-to-Speech Translation with Your Voice](2509.21144.md)
**Sitong Cheng, Weizhen Bian, Xinsheng Wang, Ruibin Yuan et al.** · 2025-09-25

<details>
<summary>Abstract</summary>

The ultimate goal of expressive speech-to-speech translation (S2ST) is to accurately translate spoken content while preserving the speaker identity and emotional style. However, progress in this field is largely hindered by three key challenges: the scarcity of paired speech data that retains expressive styles, the complexity of multi-stage processing pipelines, and the limited transfer of translation capabilities from large language models (LLMs). In this work, we address these challenges by introducing UniSS, a novel single-stage framework for expressive S2ST. Our approach features carefully designed speech semantic and style modeling, enabling seamless integration with existing text-based LLM frameworks to develop a unified text-speech language model. To transfer translation capabilities from text to speech, we propose a cross-modal chain-of-thought prompting process that progressively aligns audio semantics with text and ensures style preservation in the decoded results. Furthermore, we construct and release a large-scale, high-quality expressive S2ST dataset, UniST, comprising 44.8k hours of data. Experimental results show that UniSS significantly outperforms previous methods in translation fidelity and speech quality while preserving voice, emotion, and duration consistency. Our work establishes a simpler and more effective paradigm for building the next generation of expressive S2ST systems. Audio samples are available at https://cmots.github.io/uniss-demo.

</details>

### [DiaMoE-TTS: A Unified IPA-Based Dialect TTS Framework with Mixture-of-Experts and Parameter-Efficient Zero-Shot Adaptation](2509.22727.md)
**Ziqi Chen, Gongyu Chen, Yihua Wang, Chaofan Ding et al.** · 2025-09-25

<details>
<summary>Abstract</summary>

Dialect speech embodies rich cultural and linguistic diversity, yet building text-to-speech (TTS) systems for dialects remains challenging due to scarce data, inconsistent orthographies, and complex phonetic variation. To address these issues, we present DiaMoE-TTS, a unified IPA-based framework that standardizes phonetic representations and resolves grapheme-to-phoneme ambiguities. Built upon the F5-TTS architecture, the system introduces a dialect-aware Mixture-of-Experts (MoE) to model phonological differences and employs parameter-efficient adaptation with Low-Rank Adaptors (LoRA) and Conditioning Adapters for rapid transfer to new dialects. Unlike approaches dependent on large-scale or proprietary resources, DiaMoE-TTS enables scalable, open-data-driven synthesis. Experiments demonstrate natural and expressive speech generation, achieving zero-shot performance on unseen dialects and specialized domains such as Peking Opera with only a few hours of data.

</details>

### [HuLA: Prosody-Aware Anti-Spoofing with Multi-Task Learning for Expressive and Emotional Synthetic Speech](2509.21676.md)
**Aurosweta Mahapatra, Ismail Rasim Ulgen, Berrak Sisman** · 2025-09-25

<details>
<summary>Abstract</summary>

Current anti-spoofing systems remain vulnerable to expressive and emotional synthetic speech, since they rarely leverage prosody as a discriminative cue. Prosody is central to human expressiveness and emotion, and humans instinctively use prosodic cues such as F0 patterns and voiced/unvoiced structure to distinguish natural from synthetic speech. In this paper, we propose HuLA, a two-stage prosody-aware multi-task learning framework for spoof detection. In Stage 1, a self-supervised learning (SSL) backbone is trained on real speech with auxiliary tasks of F0 prediction and voiced/unvoiced classification, enhancing its ability to capture natural prosodic variation similar to human perceptual learning. In Stage 2, the model is jointly optimized for spoof detection and prosody tasks on both real and synthetic data, leveraging prosodic awareness to detect mismatches between natural and expressive synthetic speech. Experiments show that HuLA consistently outperforms strong baselines on challenging out-of-domain dataset, including expressive, emotional, and cross-lingual attacks. These results demonstrate that explicit prosodic supervision, combined with SSL embeddings, substantially improves robustness against advanced synthetic speech attacks.

</details>

### [Eliminating stability hallucinations in llm-based tts models via attention guidance](2509.19852.md)
**ShiMing Wang et.al.** · 2025-09-24

### [Selective Classifier-free Guidance for Zero-shot Text-to-speech](2509.19668.md)
**John Zheng et.al.** · 2025-09-24

### [SpeechCT-CLIP: Distilling Text-Image Knowledge to Speech for Voice-Native Multimodal CT Analysis](2510.02322.md)
**Lukas Buess, Jan Geier, David Bani-Harouni, Chantal Pellegrini et al.** · 2025-09-24

<details>
<summary>Abstract</summary>

Spoken communication plays a central role in clinical workflows. In radiology, for example, most reports are created through dictation. Yet, nearly all medical AI systems rely exclusively on written text. In this work, we address this gap by exploring the feasibility of learning visual-language representations directly from spoken radiology reports. Specifically, we synthesize a large-scale dataset (Speech-RATE) of spoken radiology reports and train SpeechCT-CLIP, a contrastive model that aligns speech and 3D CT volumes in a shared representation space. While naive speech-based models underperform compared to text-trained counterparts, we show that knowledge distillation from a pretrained text-image CLIP model effectively transfers semantic alignment capabilities from text to speech, substantially narrowing this gap. Experiments demonstrate improved zero-shot classification F1 from 0.623 to 0.705, recovering 88% of the performance difference, and strong retrieval results without requiring text at inference. These findings highlight speech as a practical alternative to text in multimodal pretraining and open the door to voice-driven diagnostic support tools in clinical practice.

</details>

### [OLaPh: Optimal Language Phonemizer](2509.20086.md)
**Johannes Wirth** · 2025-09-24

<details>
<summary>Abstract</summary>

Phonemization is a critical component in text-to-speech synthesis. Traditional approaches rely on deterministic transformations and lexica, while neural methods offer potential for higher generalization on out-of-vocabulary (OOV) terms. We introduce OLaPh (Optimal Language Phonemizer), a hybrid framework that integrates extensive multilingual lexica with advanced NLP techniques and a statistical subword segmentation function. Evaluations on the WikiPron benchmark show OLaPh significantly outperforms established baselines in overall accuracy and maintains robustness on OOV data through advanced fallback mechanisms. To further explore neural generalization, we utilize the framework to synthesize a high-consistency training corpus for an instruction-tuned Large Language Model (LLM). While the deterministic framework remains more accurate overall, the LLM demonstrates strong generalization, matching or partly exceeding the framework's performance. This suggests that the LLM successfully internalized phonetic intuitions from the synthetic data that transcend the framework's capabilities. Together, these tools provide a comprehensive, open-source resource for multilingual grapheme-to-phoneme conversion (G2P) research.

</details>

### [Discrete Diffusion for Generative Modeling of Text-Aligned Speech Tokens](2509.20060.md)
**Pin-Jui Ku, He Huang, Jean-Marie Lemercier, Subham Sekhar Sahoo et al.** · 2025-09-24

<details>
<summary>Abstract</summary>

This paper introduces a discrete diffusion model (DDM) framework for text-aligned speech tokenization and reconstruction. By replacing the auto-regressive speech decoder with a discrete diffusion counterpart, our model achieves significantly better reconstruction quality, stronger ASR performance, and faster inference. We provide a comprehensive analysis of applying DDMs to speech reconstruction, examining sampler choices, inference steps, and robustness to length-scale estimation errors. Furthermore, we improve the original TASTE by systematically comparing vector quantization modules, showing that FSQ yields up to a 35% relative WER reduction and +0.14 UT-MOS improvement over RVQ for AR models, while also enhancing DDM performance. Our model generates speech in just 10 denoising steps and even supports single-step generation with only minor quality degradation.

</details>

### [PART: Progressive Alignment Representation Training for Multilingual Speech-To-Text with LLMs](2509.19745.md)
**Pei Zhang, Andong Chen, Xi Chen, Baosong Yang et al.** · 2025-09-24

<details>
<summary>Abstract</summary>

Large language models (LLMs) have expanded from text to speech, giving rise to Speech Large Models (SLMs) that support recognition, translation, and synthesis. A key challenge is aligning speech and text representations, which becomes harder in multilingual settings. Existing methods often freeze LLM parameters and train encoders on multilingual data, but this forces cross-language convergence and limits performance. We introduce Progressive Alignment Representation Training (PART), a multi-stage and multi-task framework that separates within-language from cross-language alignment. During cross-language training, LLM parameters are dynamically activated, and text-based tasks are later introduced to enhance multilingual understanding. Experiments on CommonVoice 15, Fleurs, Wenetspeech, and CoVoST2 show that PART surpasses conventional approaches, with analysis confirming its ability to balance language-specific distinctions and cross-language generalization. These results demonstrate PART's effectiveness and generality for multilingual speech modality alignment.

</details>

### [Objective Evaluation of Prosody and Intelligibility in Speech Synthesis via Conditional Prediction of Discrete Tokens](2509.20485.md)
**Ismail Rasim Ulgen, Zongyang Du, Junchen Lu, Philipp Koehn et al.** · 2025-09-24

<details>
<summary>Abstract</summary>

Objective evaluation of synthesized speech is critical for advancing speech generation systems, yet existing metrics for intelligibility and prosody remain limited in scope and weakly correlated with human perception. Word Error Rate (WER) provides only a coarse text-based measure of intelligibility, while F0-RMSE and related pitch-based metrics offer a narrow, reference-dependent view of prosody. To address these limitations, we propose TTScore, a targeted and reference-free evaluation framework based on conditional prediction of discrete speech tokens. TTScore employs two sequence-to-sequence predictors conditioned on input text: TTScore-int, which measures intelligibility through content tokens, and TTScore-pro, which evaluates prosody through prosody tokens. For each synthesized utterance, the predictors compute the likelihood of the corresponding token sequences, yielding interpretable scores that capture alignment with intended linguistic content and prosodic structure. Experiments on the SOMOS, VoiceMOS, and TTSArena benchmarks demonstrate that TTScore-int and TTScore-pro provide reliable, aspect-specific evaluation and achieve stronger correlations with human judgments of overall quality than existing intelligibility and prosody-focused metrics.

</details>

### [CoMelSinger: Discrete Token-Based Zero-Shot Singing Synthesis With Structured Melody Control and Guidance](2509.19883.md)
**Junchuan Zhao, Wei Zeng, Tianle Lyu, Ye Wang** · 2025-09-24

<details>
<summary>Abstract</summary>

Singing Voice Synthesis (SVS) aims to generate expressive vocal performances from structured musical inputs such as lyrics and pitch sequences. While recent progress in discrete codec-based speech synthesis has enabled zero-shot generation via in-context learning, directly extending these techniques to SVS remains non-trivial due to the requirement for precise melody control. In particular, prompt-based generation often introduces prosody leakage, where pitch information is inadvertently entangled within the timbre prompt, compromising controllability. We present CoMelSinger, a zero-shot SVS framework that enables structured and disentangled melody control within a discrete codec modeling paradigm. Built on the non-autoregressive MaskGCT architecture, CoMelSinger replaces conventional text inputs with lyric and pitch tokens, preserving in-context generalization while enhancing melody conditioning. To suppress prosody leakage, we propose a coarse-to-fine contrastive learning strategy that explicitly regularizes pitch redundancy between the acoustic prompt and melody input. Furthermore, we incorporate a lightweight encoder-only Singing Voice Transcription (SVT) module to align acoustic tokens with pitch and duration, offering fine-grained frame-level supervision. Experimental results demonstrate that CoMelSinger achieves notable improvements in pitch accuracy, timbre consistency, and zero-shot transferability over competitive baselines. Audio samples are available at https://danny-nus.github.io/CoMelSinger/.

</details>

### [Efficient Speech Watermarking for Speech Synthesis via Progressive Knowledge Distillation](2509.19812.md)
**Yang Cui, Peter Pan, Lei He, Sheng Zhao** · 2025-09-24

<details>
<summary>Abstract</summary>

With the rapid advancement of speech generative models, unauthorized voice cloning poses significant privacy and security risks. Speech watermarking offers a viable solution for tracing sources and preventing misuse. Current watermarking technologies fall mainly into two categories: DSP-based methods and deep learning-based methods. DSP-based methods are efficient but vulnerable to attacks, whereas deep learning-based methods offer robust protection at the expense of significantly higher computational cost. To improve the computational efficiency and enhance the robustness, we propose PKDMark, a lightweight deep learning-based speech watermarking method that leverages progressive knowledge distillation (PKD). Our approach proceeds in two stages: (1) training a high-performance teacher model using an invertible neural network-based architecture, and (2) transferring the teacher's capabilities to a compact student model through progressive knowledge distillation. This process reduces computational costs by 93.6% while maintaining high level of robust performance and imperceptibility. Experimental results demonstrate that our distilled model achieves an average detection F1 score of 99.6% with a PESQ of 4.30 in advanced distortions, enabling efficient speech watermarking for real-time speech synthesis applications.

</details>

### [Frame-Stacked Local Transformers For Efficient Multi-Codebook Speech Generation](2509.19592.md)
**Roy Fejgin et.al.** · 2025-09-23

### [Group Relative Policy Optimization for Text-to-Speech with Large Language Models](2509.18798.md)
**Chang Liu et.al.** · 2025-09-23

### [Explore the Reinforcement Learning for the LLM based ASR and TTS system](2509.18569.md)
**Changfeng Gao et.al.** · 2025-09-23

### [Direct Preference Optimization for Speech Autoregressive Diffusion Models](2509.18928.md)
**Zhijun Liu, Dongya Jia, Xiaoqiang Wang, Chenpeng Du et al.** · 2025-09-23

<details>
<summary>Abstract</summary>

Autoregressive diffusion models (ARDMs) have recently been applied to speech generation, achieving state-of-the-art (SOTA) performance in zero-shot text-to-speech. By autoregressively generating continuous speech tokens with next-token diffusion, these models offer a promising alternative to next-token prediction, avoiding the technical complexities associated with discrete speech tokenization. As a relatively new paradigm, research on reinforcement learning (RL)-based fine-tuning of speech ARDMs remains limited. In this paper, we propose Autoregressive Diffusion-Direct Preference Optimization (ARDM-DPO) to advance this research. By fine-tuning the recently proposed zero-shot text-to-speech model DiTAR with DPO, we achieve significant improvements in terms of speech expressiveness and robustness for long texts.

</details>

### [No Verifiable Reward for Prosody: Toward Preference-Guided Prosody Learning in TTS](2509.18531.md)
**Seungyoun Shin, Dongha Ahn, Jiwoo Kim, Sungwook Jeon** · 2025-09-23

<details>
<summary>Abstract</summary>

Recent work reports gains in neural text-to-speech (TTS) with Group Relative Policy Optimization (GRPO). However, in the absence of a verifiable reward for \textit{prosody}, GRPO trained on transcription-oriented signals (CER/NLL) lowers error rates yet collapses prosody into monotone, unnatural speech; adding speaker-similarity further destabilizes training and degrades CER. We address this with an \textit{iterative Direct Preference Optimization (DPO)} scheme that uses only a few hundred human-labeled preference pairs per round to directly optimize prosodic naturalness while regularizing to the current model. On \textbf{KoCC-TTS}, a curated dataset of authentic Korean call center interactions capturing task-oriented dialogues, our method attains the highest human preference (ELO) with competitive CER, outperforming GRPO and strong commercial baselines. These results suggest that when prosody cannot be rewarded automatically, \textit{human preference optimization} offers a practical and data-efficient path to natural and robust TTS. The demo page is available at \href{https://tts.ch.dev}

</details>

### [Rethinking the joint estimation of magnitude and phase for time-frequency domain neural vocoders](2509.18806.md)
**Lingling Dai, Andong Li, Tong Lei, Meng Yu et al.** · 2025-09-23

<details>
<summary>Abstract</summary>

Time-frequency (T-F) domain-based neural vocoders have shown promising results in synthesizing high-fidelity audio. Nevertheless, it remains unclear on the mechanism of effectively predicting magnitude and phase targets jointly. In this paper, we start from two representative T-F domain vocoders, namely Vocos and APNet2, which belong to the single-stream and dual-stream modes for magnitude and phase estimation, respectively. When evaluating their performance on a large-scale dataset, we accidentally observe severe performance collapse of APNet2. To stabilize its performance, in this paper, we introduce three simple yet effective strategies, each targeting the topological space, the source space, and the output space, respectively. Specifically, we modify the architectural topology for better information exchange in the topological space, introduce prior knowledge to facilitate the generation process in the source space, and optimize the backpropagation process for parameter updates with an improved output format in the output space. Experimental results demonstrate that our proposed method effectively facilitates the joint estimation of magnitude and phase in APNet2, thus bridging the performance disparities between the single-stream and dual-stream vocoders.

</details>

### [Exploring Ultra-Low-Dimensional End-to-End Neural Vocoder Using Primary Speech Parameters](s2:55c950d6d8a73fb043e9721c2c84cdafb88969d4.md)
**Sumiharu Kobayashi, Tetsuo Kosaka, Takashi Nose, Akinori Ito** · 2025-09-23

<details>
<summary>Abstract</summary>

This paper explores ultra-low-dimensional neural vocoders in an end-to-end manner. In our previous work, we proposed a controllable and high-fidelity end-to-end neural vocoder to improve the quality and controllability of speech synthesis. Nine parameters, including formants and fundamental frequency (F0), were used as the input of the vocoder. In this paper, we further examine reducing the number of parameters by focusing on primary speech parameters. The experimental results demonstrate that high-quality speech waveforms can be synthesized with low character error rate (CER) and speaker similarity using only four primary speech parameters.

</details>

### [Discrete-time diffusion-like models for speech synthesis](2509.18470.md)
**Xiaozhou Tan et.al.** · 2025-09-22

### [TMD-TTS: A Unified Tibetan Multi-Dialect Text-to-Speech Synthesis for Ü-Tsang, Amdo and Kham Speech Dataset Generation](2509.18060.md)
**Yutong Liu et.al.** · 2025-09-22

### [Nord-Parl-TTS: Finnish and Swedish TTS Dataset from Parliament Speech](2509.17988.md)
**Zirui Li et.al.** · 2025-09-22

### [Qwen3-Omni Technical Report](2509.17765.md)
**Jin Xu, Zhifang Guo, Hangrui Hu, Yunfei Chu et al.** · 2025-09-22

<details>
<summary>Abstract</summary>

We present Qwen3-Omni, a single multimodal model that, for the first time, maintains state-of-the-art performance across text, image, audio, and video without any degradation relative to single-modal counterparts. Qwen3-Omni matches the performance of same-sized single-modal models within the Qwen series and excels particularly on audio tasks. Across 36 audio and audio-visual benchmarks, Qwen3-Omni achieves open-source SOTA on 32 benchmarks and overall SOTA on 22, outperforming strong closed-source models such as Gemini-2.5-Pro, Seed-ASR, and GPT-4o-Transcribe. Qwen3-Omni adopts a Thinker-Talker MoE architecture that unifies perception and generation across text, images, audio, and video, yielding fluent text and natural real-time speech. It supports text interaction in 119 languages, speech understanding in 19 languages, and speech generation in 10 languages. To reduce first-packet latency in streaming synthesis, Talker autoregressively predicts discrete speech codecs using a multi-codebook scheme. Leveraging the representational capacity of these codebooks, we replace computationally intensive block-wise diffusion with a lightweight causal ConvNet, enabling streaming from the first codec frame. In cold-start settings, Qwen3-Omni achieves a theoretical end-to-end first-packet latency of 234 ms. To further strengthen multimodal reasoning, we introduce a Thinking model that explicitly reasons over inputs from any modality. Since the research community currently lacks a general-purpose audio captioning model, we fine-tuned Qwen3-Omni-30B-A3B to obtain Qwen3-Omni-30B-A3B-Captioner, which produces detailed, low-hallucination captions for arbitrary audio inputs. Qwen3-Omni-30B-A3B, Qwen3-Omni-30B-A3B-Thinking, and Qwen3-Omni-30B-A3B-Captioner are publicly released under the Apache 2.0 license.

</details>

### [Sidon: Fast and Robust Open-Source Multilingual Speech Restoration for Large-scale Dataset Cleansing](2509.17052.md)
**Wataru Nakata et.al.** · 2025-09-21

### [Bridging the gap between training and inference in LM-based TTS models](2509.17021.md)
**Ruonan Zhang et.al.** · 2025-09-21

### [MBCodec:Thorough disentangle for high-fidelity audio compression](2509.17006.md)
**Ruonan Zhang, Xiaoyang Hao, Yichen Han, Junjie Cao et al.** · 2025-09-21

<details>
<summary>Abstract</summary>

High-fidelity neural audio codecs in Text-to-speech (TTS) aim to compress speech signals into discrete representations for faithful reconstruction. However, prior approaches faced challenges in effectively disentangling acoustic and semantic information within tokens, leading to a lack of fine-grained details in synthesized speech. In this study, we propose MBCodec, a novel multi-codebook audio codec based on Residual Vector Quantization (RVQ) that learns a hierarchically structured representation. MBCodec leverages self-supervised semantic tokenization and audio subband features from the raw signals to construct a functionally-disentangled latent space. In order to encourage comprehensive learning across various layers of the codec embedding space, we introduce adaptive dropout depths to differentially train codebooks across layers, and employ a multi-channel pseudo-quadrature mirror filter (PQMF) during training. By thoroughly decoupling semantic and acoustic features, our method not only achieves near-lossless speech reconstruction but also enables a remarkable 170x compression of 24 kHz audio, resulting in a low bit rate of just 2.2 kbps. Experimental evaluations confirm its consistent and substantial outperformance of baselines across all evaluations.

</details>

### [MaskVCT: Masked Voice Codec Transformer for Zero-Shot Voice Conversion With Increased Controllability via Multiple Guidances](2509.17143.md)
**Junhyeok Lee, Helin Wang, Yaohan Guan, Thomas Thebaud et al.** · 2025-09-21

<details>
<summary>Abstract</summary>

We introduce MaskVCT, a zero-shot voice conversion (VC) model that offers multi-factor controllability through multiple classifier-free guidances (CFGs). While previous VC models rely on a fixed conditioning scheme, MaskVCT integrates diverse conditions in a single model. To further enhance robustness and control, the model can leverage continuous or quantized linguistic features to enhance intelligibility and speaker similarity, and can use or omit pitch contour to control prosody. These choices allow users to seamlessly balance speaker identity, linguistic content, and prosodic factors in a zero-shot VC setting. Extensive experiments demonstrate that MaskVCT achieves the best target speaker and accent similarities while obtaining competitive word and character error rates compared to existing baselines. Audio samples are available at https://maskvct.github.io/.

</details>

### [SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding](2509.14946.md)
**Bingsong Bai et.al.** · 2025-09-20

### [Beyond Global Emotion: Fine-Grained Emotional Speech Synthesis with Dynamic Word-Level Modulation](2509.20378.md)
**Sirui Wang, Andong Chen, Tiejun Zhao** · 2025-09-20

<details>
<summary>Abstract</summary>

Emotional text-to-speech (E-TTS) is central to creating natural and trustworthy human-computer interaction. Existing systems typically rely on sentence-level control through predefined labels, reference audio, or natural language prompts. While effective for global emotion expression, these approaches fail to capture dynamic shifts within a sentence. To address this limitation, we introduce Emo-FiLM, a fine-grained emotion modeling framework for LLM-based TTS. Emo-FiLM aligns frame-level features from emotion2vec to words to obtain word-level emotion annotations, and maps them through a Feature-wise Linear Modulation (FiLM) layer, enabling word-level emotion control by directly modulating text embeddings. To support evaluation, we construct the Fine-grained Emotion Dynamics Dataset (FEDD) with detailed annotations of emotional transitions. Experiments show that Emo-FiLM outperforms existing approaches on both global and fine-grained tasks, demonstrating its effectiveness and generality for expressive speech synthesis.

</details>

### [Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation](2509.16010.md)
**Qi Wang et.al.** · 2025-09-19

### [Deep Dubbing: End-to-End Auto-Audiobook System with Text-to-Timbre and Context-Aware Instruct-TTS](2509.15845.md)
**Ziqi Dai et.al.** · 2025-09-19

### [VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency](2509.15969.md)
**Nikita Torgashov, Gustav Eje Henter, Gabriel Skantze** · 2025-09-19

<details>
<summary>Abstract</summary>

We present VoXtream, a fully autoregressive, zero-shot streaming text-to-speech (TTS) system for real-time use that begins speaking from the first word. VoXtream directly maps incoming phonemes to audio tokens using a monotonic alignment scheme and a limited look-ahead that does not delay onset. Built around an incremental phoneme transformer, a temporal transformer predicting semantic and duration tokens, and a depth transformer producing acoustic tokens, VoXtream achieves, to our knowledge, the lowest initial delay among publicly available streaming TTS: 102 ms on GPU. Despite being trained on a mid-scale 9k-hour corpus, it matches or surpasses larger baselines on several metrics, while delivering competitive quality in both output- and full-streaming settings. Demo and code are available at https://herimor.github.io/voxtream.

</details>

### [LibriTTS-VI: A Public Corpus and Novel Methods for Efficient Voice Impression Control](2509.15626.md)
**Junki Ohmura, Yuki Ito, Emiru Tsunoo, Toshiyuki Sekiya et al.** · 2025-09-19

<details>
<summary>Abstract</summary>

Numerical voice impression (VI) control (e.g., scaling brightness) enables fine-grained control in text-to-speech (TTS). However, it faces two challenges: no public corpus and impression leakage, where reference audio biases synthesized voice away from the target VI. To address the first challenge, we introduce LibriTTS-VI, the first public VI corpus built on LibriTTS-R. For the second, we hypothesize a single reference causes leakage by entangling speaker identity and VI. To mitigate this, we propose 1) disentangled training with two utterances from the same speaker for speaker and VI conditioning, and 2) a reference-free method controlling the impression solely via target VI. Experimentally, our best method improves controllability: 11-dimensional VI mean squared error drops from 0.61 to 0.41 objectively and 1.15 to 0.92 subjectively. A comparison with a prompt-based TTS reveals imprecise numerical control and entanglement between VI and text semantics, which our methods overcome.

</details>

### [An Extensive Analysis of the Singing Voice Conversion Challenge 2025 Evaluation Results](2509.15629.md)
**Lester Phillip Violeta, Xueyao Zhang, Jiatong Shi, Yusuke Yasuda et al.** · 2025-09-19

<details>
<summary>Abstract</summary>

We present a thorough analysis of the findings of the latest iteration of the Singing Voice Conversion Challenge, a scientific event aiming to compare and understand different voice conversion systems in a controlled environment. Compared to previous iterations which solely focused on converting the singer identity, this year we also focused on converting the singing style of the singer. To create a controlled environment and thorough evaluations, we developed a new challenge database, introduced two tasks, open-sourced baselines, and conducted large-scale crowd-sourced listening tests and objective evaluations. The challenge was run for two months and in total we evaluated 33 different systems. The results of the large-scale crowd-sourced listening test showed that top systems had comparable singer identity scores to ground truth samples. However, modeling the singing style and consequently achieving high naturalness still remains a challenge in this task, primarily due to the difficulty in modeling dynamic information in breathy, glissando, and vibrato singing styles. Further analyses of the challenge also discuss the limitations of both the traditional similarity test and the dynamic preference test in evaluating singing style similarity. Moreover, calculating Spearman's rank correlation coefficient shows that dependent objective metrics such as chroma-alignment and non-match metrics such as speaker embeddings are the most correlated to subjective scores, but are still not at a level where it could be considered as a true replacement for subjective scores.

</details>

### [MELA-TTS: Joint transformer-diffusion model with representation alignment for speech synthesis](2509.14784.md)
**Keyu An et.al.** · 2025-09-18

### [Real-Time Streaming Mel Vocoding with Generative Flow Matching](2509.15085.md)
**Simon Welker, Tal Peer, Timo Gerkmann** · 2025-09-18

<details>
<summary>Abstract</summary>

The task of Mel vocoding, i.e., the inversion of a Mel magnitude spectrogram to an audio waveform, is still a key component in many text-to-speech (TTS) systems today. Based on generative flow matching, our prior work on generative STFT phase retrieval (DiffPhase), and the pseudoinverse operator of the Mel filterbank, we develop MelFlow, a streaming-capable generative Mel vocoder for speech sampled at 16 kHz with an algorithmic latency of only 32 ms and a total latency of 48 ms. We show real-time streaming capability at this latency not only in theory, but in practice on a consumer laptop GPU. Furthermore, we show that our model achieves substantially better PESQ and SI-SDR values compared to well-established not streaming-capable baselines for Mel vocoding including HiFi-GAN.

</details>

### [DAIEN-TTS: Disentangled Audio Infilling for Environment-Aware Text-to-Speech Synthesis](2509.14684.md)
**Ye-Xin Lu, Yu Gu, Kun Wei, Hui-Peng Du et al.** · 2025-09-18

<details>
<summary>Abstract</summary>

This paper presents DAIEN-TTS, a zero-shot text-to-speech (TTS) framework that enables ENvironment-aware synthesis through Disentangled Audio Infilling. By leveraging separate speaker and environment prompts, DAIEN-TTS allows independent control over the timbre and the background environment of the synthesized speech. Built upon F5-TTS, the proposed DAIEN-TTS first incorporates a pretrained speech-environment separation (SES) module to disentangle the environmental speech into mel-spectrograms of clean speech and environment audio. Two random span masks of varying lengths are then applied to both mel-spectrograms, which, together with the text embedding, serve as conditions for infilling the masked environmental mel-spectrogram, enabling the simultaneous continuation of personalized speech and time-varying environmental audio. To further enhance controllability during inference, we adopt dual classifier-free guidance (DCFG) for the speech and environment components and introduce a signal-to-noise ratio (SNR) adaptation strategy to align the synthesized speech with the environment prompt. Experimental results demonstrate that DAIEN-TTS generates environmental personalized speech with high naturalness, strong speaker similarity, and high environmental fidelity.

</details>

### [Stochastic Clock Attention for Aligning Continuous and Ordered Sequences](2509.14678.md)
**Hyungjoon Soh, Junghyo Jo** · 2025-09-18

<details>
<summary>Abstract</summary>

We formulate an attention mechanism for continuous and ordered sequences that explicitly functions as an alignment model, which serves as the core of many sequence-to-sequence tasks. Standard scaled dot-product attention relies on positional encodings and masks but does not enforce continuity or monotonicity, which are crucial for frame-synchronous targets. We propose learned nonnegative \emph{clocks} to source and target and model attention as the meeting probability of these clocks; a path-integral derivation yields a closed-form, Gaussian-like scoring rule with an intrinsic bias toward causal, smooth, near-diagonal alignments, without external positional regularizers. The framework supports two complementary regimes: normalized clocks for parallel decoding when a global length is available, and unnormalized clocks for autoregressive decoding -- both nearly-parameter-free, drop-in replacements. In a Transformer text-to-speech testbed, this construction produces more stable alignments and improved robustness to global time-scaling while matching or improving accuracy over scaled dot-product baselines. We hypothesize applicability to other continuous targets, including video and temporal signal modeling.

</details>

### [Emotion-Aware Speech Generation with Character-Specific Voices for Comics](2509.15253.md)
**Zhiwen Qian, Jinhua Liang, Huan Zhang** · 2025-09-18

<details>
<summary>Abstract</summary>

This paper presents an end-to-end pipeline for generating character-specific, emotion-aware speech from comics. The proposed system takes full comic volumes as input and produces speech aligned with each character's dialogue and emotional state. An image processing module performs character detection, text recognition, and emotion intensity recognition. A large language model performs dialogue attribution and emotion analysis by integrating visual information with the evolving plot context. Speech is synthesized through a text-to-speech model with distinct voice profiles tailored to each character and emotion. This work enables automated voiceover generation for comics, offering a step toward interactive and immersive comic reading experience.

</details>

### [Cross-Lingual F5-TTS: Towards Language-Agnostic Voice Cloning and Speech Synthesis](2509.14579.md)
**Qingyu Liu, Yushen Chen, Zhikang Niu, Chunhui Wang et al.** · 2025-09-18

<details>
<summary>Abstract</summary>

Flow-matching-based text-to-speech (TTS) models have shown high-quality speech synthesis. However, most current flow-matching-based TTS models still rely on reference transcripts corresponding to the audio prompt for synthesis. This dependency prevents cross-lingual voice cloning when audio prompt transcripts are unavailable, particularly for unseen languages. The key challenges for flow-matching-based TTS models to remove audio prompt transcripts are identifying word boundaries during training and determining appropriate duration during inference. In this paper, we introduce Cross-Lingual F5-TTS, a framework that enables cross-lingual voice cloning without audio prompt transcripts. Our method preprocesses audio prompts by forced alignment to obtain word boundaries, enabling direct synthesis from audio prompts while excluding transcripts during training. To address the duration modeling challenge, we train speaking rate predictors at different linguistic granularities to derive duration from speaker pace. Experiments show that our approach matches the performance of F5-TTS while enabling cross-lingual voice cloning.

</details>

### [FCPE: A Fast Context-based Pitch Estimation Model](2509.15140.md)
**Yuxin Luo, Ruoyi Zhang, Lu-Chuan Liu, Tianyu Li et al.** · 2025-09-18

<details>
<summary>Abstract</summary>

Pitch estimation (PE) in monophonic audio is crucial for MIDI transcription and singing voice conversion (SVC), but existing methods suffer significant performance degradation under noise. In this paper, we propose FCPE, a fast context-based pitch estimation model that employs a Lynx-Net architecture with depth-wise separable convolutions to effectively capture mel spectrogram features while maintaining low computational cost and robust noise tolerance. Experiments show that our method achieves 96.79\% Raw Pitch Accuracy (RPA) on the MIR-1K dataset, on par with the state-of-the-art methods. The Real-Time Factor (RTF) is 0.0062 on a single RTX 4090 GPU, which significantly outperforms existing algorithms in efficiency. Code is available at https://github.com/CNChTu/FCPE.

</details>

### [SpeechMLC: Speech Multi-label Classification](2509.14677.md)
**Miseul Kim, Seyun Um, Hyeonjin Cha, Hong-goo Kang** · 2025-09-18

<details>
<summary>Abstract</summary>

In this paper, we propose a multi-label classification framework to detect multiple speaking styles in a speech sample. Unlike previous studies that have primarily focused on identifying a single target style, our framework effectively captures various speaker characteristics within a unified structure, making it suitable for generalized human-computer interaction applications. The proposed framework integrates cross-attention mechanisms within a transformer decoder to extract salient features associated with each target label from the input speech. To mitigate the data imbalance inherent in multi-label speech datasets, we employ a data augmentation technique based on a speech generation model. We validate our model's effectiveness through multiple objective evaluations on seen and unseen corpora. In addition, we provide an analysis of the influence of human perception on classification accuracy by considering the impact of human labeling agreement on model performance.

</details>

### [Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation](2509.14632.md)
**Miseul Kim, Soo Jin Park, Kyungguen Byun, Hyeon-Kyeong Shin et al.** · 2025-09-18

<details>
<summary>Abstract</summary>

Speaker diarization systems often struggle with high intrinsic intra-speaker variability, such as shifts in emotion, health, or content. This can cause segments from the same speaker to be misclassified as different individuals, for example, when one raises their voice or speaks faster during conversation. To address this, we propose a style-controllable speech generation model that augments speech across diverse styles while preserving the target speaker's identity. The proposed system starts with diarized segments from a conventional diarizer. For each diarized segment, it generates augmented speech samples enriched with phonetic and stylistic diversity. And then, speaker embeddings from both the original and generated audio are blended to enhance the system's robustness in grouping segments with high intrinsic intra-speaker variability. We validate our approach on a simulated emotional speech dataset and the truncated AMI dataset, demonstrating significant improvements, with error rate reductions of 49% and 35% on each dataset, respectively.

</details>

### [Do You Hear What I Mean? Quantifying the Instruction-Perception Gap in Instruction-Guided Expressive Text-To-Speech Systems](2509.13989.md)
**Yi-Cheng Lin, Huang-Cheng Chou, Tzu-Chieh Wei, Kuan-Yu Chen et al.** · 2025-09-17

<details>
<summary>Abstract</summary>

Instruction-guided text-to-speech (ITTS) enables users to control speech generation through natural language prompts, offering a more intuitive interface than traditional TTS. However, the alignment between user style instructions and listener perception remains largely unexplored. This work first presents a perceptual analysis of ITTS controllability across two expressive dimensions (adverbs of degree and graded emotion intensity) and collects human ratings on speaker age and word-level emphasis attributes. To comprehensively reveal the instruction-perception gap, we provide a data collection with large-scale human evaluations, named Expressive VOice Control (E-VOC) corpus. Furthermore, we reveal that (1) gpt-4o-mini-tts is the most reliable ITTS model with great alignment between instruction and generated utterances across acoustic dimensions. (2) The 5 analyzed ITTS systems tend to generate Adult voices even when the instructions ask to use child or Elderly voices. (3) Fine-grained control remains a major challenge, indicating that most ITTS systems have substantial room for improvement in interpreting slightly different attribute instructions.

</details>

### [SpeechOp: Inference-Time Task Composition for Generative Speech Processing](2509.14298.md)
**Justin Lovelace, Rithesh Kumar, Jiaqi Su, Ke Chen et al.** · 2025-09-17

<details>
<summary>Abstract</summary>

While generative Text-to-Speech (TTS) systems leverage vast ``in-the-wild" data to achieve remarkable success, speech-to-speech processing tasks like enhancement face data limitations, which lead data-hungry generative approaches to distort speech content and speaker identity. To bridge this gap, we present SpeechOp, a multi-task latent diffusion model that transforms pre-trained TTS models into a universal speech processor capable of performing a wide range of speech tasks and composing them in novel ways at inference time. By adapting a pre-trained TTS model, SpeechOp inherits a rich understanding of natural speech, accelerating training and improving S2S task quality, while simultaneously enhancing core TTS performance. Finally, we introduce Implicit Task Composition (ITC), a novel pipeline where ASR-derived transcripts (e.g., from Whisper) guide SpeechOp's enhancement via our principled inference-time task composition. ITC achieves state-of-the-art content preservation by robustly combining web-scale speech understanding with SpeechOp's generative capabilities. Audio samples are available at https://justinlovelace.github.io/projects/speechop

</details>

### [A Distilled Low-Latency Neural Vocoder with Explicit Amplitude and Phase Prediction](2509.13667.md)
**Hui-Peng Du, Yang Ai, Zhen-Hua Ling** · 2025-09-17

<details>
<summary>Abstract</summary>

The majority of mainstream neural vocoders primarily focus on speech quality and generation speed, while overlooking latency, which is a critical factor in real-time applications. Excessive latency leads to noticeable delays in user interaction, severely degrading the user experience and rendering such systems impractical for real-time use. Therefore, this paper proposes DLL-APNet, a Distilled Low-Latency neural vocoder which first predicts the Amplitude and Phase spectra explicitly from input mel spectrogram and then reconstructs the speech waveform via inverse short-time Fourier transform (iSTFT). The DLL-APNet vocoder leverages causal convolutions to constrain the utilization of information to current and historical contexts, effectively minimizing latency. To mitigate speech quality degradation caused by causal constraints, a knowledge distillation strategy is proposed, where a pre-trained non-causal teacher vocoder guides intermediate feature generation of the causal student DLL-APNet vocoder. Experimental results demonstrate that the proposed DLL-APNet vocoder produces higher-quality speech than other causal vocoders, while requiring fewer computational resources. Furthermore, the proposed DLL-APNet vocoder achieves speech quality on par with mainstream non-causal neural vocoders, validating its ability to deliver both high perceptual quality and low latency.

</details>

### [MSR-Codec: A Low-Bitrate Multi-Stream Residual Codec for High-Fidelity Speech Generation with Information Disentanglement](2509.13068.md)
**Jingyu Li et.al.** · 2025-09-16

### [A Lightweight Pipeline for Noisy Speech Voice Cloning and Accurate Lip Sync Synthesis](2509.12831.md)
**Javeria Amir, Farwa Attaria, Mah Jabeen, Umara Noor et al.** · 2025-09-16

<details>
<summary>Abstract</summary>

Recent developments in voice cloning and talking head generation demonstrate impressive capabilities in synthesizing natural speech and realistic lip synchronization. Current methods typically require and are trained on large scale datasets and computationally intensive processes using clean studio recorded inputs that is infeasible in noisy or low resource environments. In this paper, we introduce a new modular pipeline comprising Tortoise text to speech. It is a transformer based latent diffusion model that can perform high fidelity zero shot voice cloning given only a few training samples. We use a lightweight generative adversarial network architecture for robust real time lip synchronization. The solution will contribute to many essential tasks concerning less reliance on massive pre training generation of emotionally expressive speech and lip synchronization in noisy and unconstrained scenarios. The modular structure of the pipeline allows an easy extension for future multi modal and text guided voice modulation and it could be used in real world systems.

</details>

### [Spiking Vocos: An Energy-Efficient Neural Vocoder](2509.13049.md)
**Yukun Chen, Zhaoxi Mu, Andong Li, Peilin Li et al.** · 2025-09-16

<details>
<summary>Abstract</summary>

Despite the remarkable progress in the synthesis speed and fidelity of neural vocoders, their high energy consumption remains a critical barrier to practical deployment on computationally restricted edge devices. Spiking Neural Networks (SNNs), widely recognized for their high energy efficiency due to their event-driven nature, offer a promising solution for low-resource scenarios. In this paper, we propose Spiking Vocos, a novel spiking neural vocoder with ultra-low energy consumption, built upon the efficient Vocos framework. To mitigate the inherent information bottleneck in SNNs, we design a Spiking ConvNeXt module to reduce Multiply-Accumulate (MAC) operations and incorporate an amplitude shortcut path to preserve crucial signal dynamics. Furthermore, to bridge the performance gap with its Artificial Neural Network (ANN) counterpart, we introduce a self-architectural distillation strategy to effectively transfer knowledge. A lightweight Temporal Shift Module is also integrated to enhance the model's ability to fuse information across the temporal dimension with negligible computational overhead. Experiments demonstrate that our model achieves performance comparable to its ANN counterpart, with UTMOS and PESQ scores of 3.74 and 3.45 respectively, while consuming only 14.7% of the energy. The source code is available at https://github.com/pymaster17/Spiking-Vocos.

</details>

### [Preservation of Language Understanding Capabilities in Speech-aware Large Language Models](2509.12171.md)
**Marek Kubis, Paweł Skórzewski, Iwona Christop, Mateusz Czyżnikiewicz et al.** · 2025-09-15

<details>
<summary>Abstract</summary>

The paper presents C3T (Cross-modal Capabilities Conservation Test), a new benchmark for assessing the performance of speech-aware large language models. The benchmark utilizes textual tasks and a voice cloning text-to-speech model to quantify the extent to which language understanding capabilities are preserved when the model is accessed via speech input. C3T quantifies the fairness of the model for different categories of speakers and its robustness across text and speech modalities.

</details>

### [SpeechWeave: Diverse Multilingual Synthetic Text & Audio Data Generation Pipeline for Training Text to Speech Models](2509.14270.md)
**Karan Dua, Puneet Mittal, Ranjeet Gupta, Hitesh Laxmichand Patel** · 2025-09-15

<details>
<summary>Abstract</summary>

High-quality Text-to-Speech (TTS) model training requires extensive and diverse text and speech data. It is challenging to procure such data from real sources due to issues of domain specificity, licensing, and scalability. Large language models (LLMs) can certainly generate textual data, but they create repetitive text with insufficient variation in the prompt during the generation process. Another important aspect in TTS training data is text normalization. Tools for normalization might occasionally introduce anomalies or overlook valuable patterns, and thus impact data quality. Furthermore, it is also impractical to rely on voice artists for large scale speech recording in commercial TTS systems with standardized voices. To address these challenges, we propose SpeechWeave, a synthetic speech data generation pipeline that is capable of automating the generation of multilingual, domain-specific datasets for training TTS models. Our experiments reveal that our pipeline generates data that is 10-48% more diverse than the baseline across various linguistic and phonetic metrics, along with speaker-standardized speech audio while generating approximately 97% correctly normalized text. Our approach enables scalable, high-quality data generation for TTS training, improving diversity, normalization, and voice consistency in the generated datasets.

</details>

### [Length-Aware Rotary Position Embedding for Text-Speech Alignment](2509.11084.md)
**Hyeongju Kim, Juheon Lee, Jinhyeok Yang, Jacob Morton** · 2025-09-14

<details>
<summary>Abstract</summary>

Many recent text-to-speech (TTS) systems are built on transformer architectures and employ cross-attention mechanisms for text-speech alignment. Within these systems, rotary position embedding (RoPE) is commonly used to encode positional information in text and speech representations. In this work, we introduce length-aware RoPE (LARoPE), a simple yet effective extension of RoPE that improves text-speech alignment. Unlike RoPE, which relies on absolute indices, LARoPE computes relative distances between query and key positions using length-normalized indices. Experimental results show that LARoPE consistently outperforms RoPE, offering faster loss convergence, more accurate text-speech alignment, and higher overall TTS quality. Furthermore, LARoPE demonstrates greater resilience to variations in utterance duration and maintains stable performance in extended speech generation up to 30 seconds, whereas RoPE suffers from notable degradation. Notably, our method achieves a state-of-the-art word error rate on a standard zero-shot TTS benchmark.

</details>

### [FuseCodec: Semantic-Contextual Fusion and Supervision for Neural Codecs](2509.11425.md)
**Md Mubtasim Ahasan, Rafat Hasan Khan, Tasnim Mohiuddin, Aman Chadha et al.** · 2025-09-14

<details>
<summary>Abstract</summary>

Speech tokenization enables discrete representation and facilitates speech language modeling. However, existing neural codecs capture low-level acoustic features, overlooking the semantic and contextual cues inherent to human speech. While recent efforts introduced semantic representations from self-supervised speech models or incorporated contextual representations from pre-trained language models, challenges remain in aligning and unifying the semantic and contextual representations. We introduce FuseCodec, which unifies acoustic, semantic, and contextual representations through strong cross-modal alignment and globally informed supervision. We propose three complementary techniques: (i) Latent Representation Fusion, integrating semantic and contextual features directly into the encoder latent space for robust and unified representation learning; (ii) Global Semantic-Contextual Supervision, supervising discrete tokens with globally pooled and broadcasted representations to enhance temporal consistency and cross-modal alignment; and (iii) Temporally Aligned Contextual Supervision, strengthening alignment by dynamically matching contextual and speech tokens within a local window for fine-grained token-level supervision. We further introduce FuseCodec-TTS, demonstrating our methodology's applicability to zero-shot speech synthesis. Empirically, FuseCodec achieves state-of-the-art performance in LibriSpeech, surpassing EnCodec, SpeechTokenizer, and DAC in transcription accuracy, perceptual quality, intelligibility, and speaker similarity. Results highlight the effectiveness of contextually and semantically guided tokenization for speech tokenization and downstream tasks. Code and pretrained models are available at https://github.com/mubtasimahasan/FuseCodec.

</details>

### [DiFlow-TTS: Discrete Flow Matching with Factorized Speech Tokens for Low-Latency Zero-Shot Text-To-Speech](2509.09631.md)
**Ngoc-Son Nguyen et.al.** · 2025-09-12

### [Towards Data Drift Monitoring for Speech Deepfake Detection in the context of MLOps](2509.10086.md)
**Xin Wang, Wanying Ge, Junichi Yamagishi** · 2025-09-12

<details>
<summary>Abstract</summary>

When being delivered in applications or services on the cloud, static speech deepfake detectors that are not updated will become vulnerable to newly created speech deepfake attacks. From the perspective of machine learning operations (MLOps), this paper tries to answer whether we can monitor new and unseen speech deepfake data that drifts away from a seen reference data set. We further ask, if drift is detected, whether we can fine-tune the detector using similarly drifted data, reduce the drift, and improve the detection performance. On a toy dataset and the large-scale MLAAD dataset, we show that the drift caused by new text-to-speech (TTS) attacks can be monitored using distances between the distributions of the new data and reference data. Furthermore, we demonstrate that fine-tuning the detector using data generated by the new TTS deepfakes can reduce the drift and the detection error rates.

</details>

### [DiTReducio: A Training-Free Acceleration for DiT-Based TTS via Progressive Calibration](2509.09748.md)
**Yanru Huo et.al.** · 2025-09-11

### [HISPASpoof: A New Dataset For Spanish Speech Forensics](2509.09155.md)
**Maria Risques, Kratika Bhagtani, Amit Kumar Singh Yadav, Edward J. Delp** · 2025-09-11

<details>
<summary>Abstract</summary>

Zero-shot Voice Cloning (VC) and Text-to-Speech (TTS) methods have advanced rapidly, enabling the generation of highly realistic synthetic speech and raising serious concerns about their misuse. While numerous detectors have been developed for English and Chinese, Spanish-spoken by over 600 million people worldwide-remains underrepresented in speech forensics. To address this gap, we introduce HISPASpoof, the first large-scale Spanish dataset designed for synthetic speech detection and attribution. It includes real speech from public corpora across six accents and synthetic speech generated with six zero-shot TTS systems. We evaluate five representative methods, showing that detectors trained on English fail to generalize to Spanish, while training on HISPASpoof substantially improves detection. We also evaluate synthetic speech attribution performance on HISPASpoof, i.e., identifying the generation method of synthetic speech. HISPASpoof thus provides a critical benchmark for advancing reliable and inclusive speech forensics in Spanish.

</details>

### [DeCodec: Rethinking Audio Codecs as Universal Disentangled Representation Learners](2509.09201.md)
**Xiaoxue Luo, Jinwei Huang, Runyan Yang, Yingying Gao et al.** · 2025-09-11

<details>
<summary>Abstract</summary>

Universal audio codecs learn entangled representations across audio types, whereas some specific codecs offer decoupled representations but are limited to speech. Real-world audio, however, often contains mixed speech and background sounds, and downstream tasks require selective access to these components. Therefore, we rethink the audio codec as a universal disentangled representation learner to enable controllable feature selection across different audio tasks. To this end, we introduce DeCodec, a novel neural codec that learns to decouple audio representations into orthogonal subspaces dedicated to speech and background sound, and within speech, representations are further decomposed into semantic and paralinguistic components. This hierarchical disentanglement allows flexible feature selection, making DeCodec a universal front-end for multiple audio applications. Technically, built upon a codec framework, DeCodec incorporates two key innovations: a subspace orthogonal projection module that factorizes the input into two decoupled orthogonal subspaces, and a representation swap training procedure that ensures these two subspaces are correlate to the speech and background sound, respectively. These allows parallel RVQs to quantize speech and background sound components independently. Furthermore, we employ semantic guidance to the speech RVQ to achieve semantic and paralinguistic decomposition. Experimental results show that DeCodec maintains advanced signal reconstruction while enabling new capabilities: superior speech enhancement and effective one-shot voice conversion on noisy speech via representation recombination, improved ASR robustness through clean semantic features, and controllable background sound preservation/suppression in TTS. Demo Page: https://luo404.github.io/DeCodecV2/

</details>

### [Accelerating Diffusion Transformer-Based Text-to-Speech with Transformer Layer Caching](2509.08696.md)
**Siratish Sakpiboonchit et.al.** · 2025-09-10

### [Joint Learning using Mixture-of-Expert-Based Representation for Enhanced Speech Generation and Robust Emotion Recognition](2509.08470.md)
**Jing-Tong Tzeng et.al.** · 2025-09-10

### [LatentVoiceGrad: Nonparallel Voice Conversion with Latent Diffusion/Flow-Matching Models](2509.08379.md)
**Hirokazu Kameoka, Takuhiro Kaneko, Kou Tanaka, Yuto Kondo** · 2025-09-10

<details>
<summary>Abstract</summary>

Previously, we introduced VoiceGrad, a nonparallel voice conversion (VC) technique enabling mel-spectrogram conversion from source to target speakers using a score-based diffusion model. The concept involves training a score network to predict the gradient of the log density of mel-spectrograms from various speakers. VC is executed by iteratively adjusting an input mel-spectrogram until resembling the target speaker's. However, challenges persist: audio quality needs improvement, and conversion is slower compared to modern VC methods designed to operate at very high speeds. To address these, we introduce latent diffusion models into VoiceGrad, proposing an improved version with reverse diffusion in the autoencoder bottleneck. Additionally, we propose using a flow matching model as an alternative to the diffusion model to further speed up the conversion process without compromising the conversion quality. Experimental results show enhanced speech quality and accelerated conversion compared to the original.

</details>

### [Deploying AI for Signal Processing education: Selected challenges and intriguing opportunities](2509.08950.md)
**Jarvis Haupt, Qin Lu, Yanning Shen, Jia Chen et al.** · 2025-09-10

<details>
<summary>Abstract</summary>

Powerful artificial intelligence (AI) tools that have emerged in recent years -- including large language models, automated coding assistants, and advanced image and speech generation technologies -- are the result of monumental human achievements. These breakthroughs reflect mastery across multiple technical disciplines and the resolution of significant technological challenges. However, some of the most profound challenges may still lie ahead. These challenges are not purely technical but pertain to the fair and responsible use of AI in ways that genuinely improve the global human condition. This article explores one promising application aligned with that vision: the use of AI tools to facilitate and enhance education, with a specific focus on signal processing (SP). It presents two interrelated perspectives: identifying and addressing technical limitations, and applying AI tools in practice to improve educational experiences. Primers are provided on several core technical issues that arise when using AI in educational settings, including how to ensure fairness and inclusivity, handle hallucinated outputs, and achieve efficient use of resources. These and other considerations -- such as transparency, explainability, and trustworthiness -- are illustrated through the development of an immersive, structured, and reliable "smart textbook." The article serves as a resource for researchers and educators seeking to advance AI's role in engineering education.

</details>

### [End-to-End Emotionally-Aware Speech Synthesis using Conditional GAN Frameworks](s2:2aebd2f1bddb209818bb94da592dd1cf800e8d99.md)
**G. Sajiv, N. Meenakshisundaram** · 2025-09-10

<details>
<summary>Abstract</summary>

The capacity to produce emotionally expressive speech is essential for improving the naturalness and relatability of human-computer interactions. Despite recent improvements in neural text-to-speech (TTS) systems that have markedly enhanced voice quality, the precise and continuous management of emotional expression continues to be a substantial challenge. This study presents a comprehensive emotionally-aware voice synthesis framework utilizing Conditional Generative Adversarial Networks (cGANs). Our paradigm incorporates emotion conditioning directly into the speech generating process, enabling dynamic manipulation of affective states across a continuous range. In contrast to traditional methods that depend on distinct emotion labels or external prosody modeling, our approach generates expressive speech by concurrently optimizing the generator and discriminator within an adversarial framework. Comprehensive studies on publicly accessible emotional speech datasets reveal that our system generates high-fidelity audio while adeptly capturing nuanced variations in emotional tone. Both subjective and objective assessments validate the superiority of our approach in producing speech that is emotionally nuanced and perceptually authentic. This research establishes the foundation for emotionally intelligent text-to-speech systems that adjust to user context and enhance communication across various applications.

</details>

### [Progressive Facial Granularity Aggregation with Bilateral Attribute-based Enhancement for Face-to-Speech Synthesis](2509.07376.md)
**Yejin Jeon, Youngjae Kim, Jihyun Lee, Hyounghun Kim et al.** · 2025-09-09

<details>
<summary>Abstract</summary>

For individuals who have experienced traumatic events such as strokes, speech may no longer be a viable means of communication. While text-to-speech (TTS) can be used as a communication aid since it generates synthetic speech, it fails to preserve the user's own voice. As such, face-to-voice (FTV) synthesis, which derives corresponding voices from facial images, provides a promising alternative. However, existing methods rely on pre-trained visual encoders, and finetune them to align with speech embeddings, which strips fine-grained information from facial inputs such as gender or ethnicity, despite their known correlation with vocal traits. Moreover, these pipelines are multi-stage, which requires separate training of multiple components, thus leading to training inefficiency. To address these limitations, we utilize fine-grained facial attribute modeling by decomposing facial images into non-overlapping segments and progressively integrating them into a multi-granular representation. This representation is further refined through multi-task learning of speaker attributes such as gender and ethnicity at both the visual and acoustic domains. Moreover, to improve alignment robustness, we adopt a multi-view training strategy by pairing various visual perspectives of a speaker in terms of different angles and lighting conditions, with identical speech recordings. Extensive subjective and objective evaluations confirm that our approach substantially enhances face-voice congruence and synthesis stability.

</details>

### [When Fine-Tuning is Not Enough: Lessons from HSAD on Hybrid and Adversarial Audio Spoof Detection](2509.07323.md)
**Bin Hu, Kunyang Huang, Daehan Kwak, Meng Xu et al.** · 2025-09-09

<details>
<summary>Abstract</summary>

The rapid advancement of AI has enabled highly realistic speech synthesis and voice cloning, posing serious risks to voice authentication, smart assistants, and telecom security. While most prior work frames spoof detection as a binary task, real-world attacks often involve hybrid utterances that mix genuine and synthetic speech, making detection substantially more challenging. To address this gap, we introduce the Hybrid Spoofed Audio Dataset (HSAD), a benchmark containing 1,248 clean and 41,044 degraded utterances across four classes: human, cloned, zero-shot AI-generated, and hybrid audio. Each sample is annotated with spoofing method, speaker identity, and degradation metadata to enable fine-grained analysis. We evaluate six transformer-based models, including spectrogram encoders (MIT-AST, MattyB95-AST) and self-supervised waveform models (Wav2Vec2, HuBERT). Results reveal critical lessons: pretrained models overgeneralize and collapse under hybrid conditions; spoof-specific fine-tuning improves separability but struggles with unseen compositions; and dataset-specific adaptation on HSAD yields large performance gains (AST greater than 97 percent and F1 score is approximately 99 percent), though residual errors persist for complex hybrids. These findings demonstrate that fine-tuning alone is not sufficient-robust hybrid-aware benchmarks like HSAD are essential to expose calibration failures, model biases, and factors affecting spoof detection in adversarial environments. HSAD thus provides both a dataset and an analytic framework for building resilient and trustworthy voice authentication systems.

</details>

### [VStyle: A Benchmark for Voice Style Adaptation with Spoken Instructions](2509.09716.md)
**Jun Zhan, Mingyang Han, Yuxuan Xie, Chen Wang et al.** · 2025-09-09

<details>
<summary>Abstract</summary>

Spoken language models (SLMs) have emerged as a unified paradigm for speech understanding and generation, enabling natural human machine interaction. However, while most progress has focused on semantic accuracy and instruction following, the ability of SLMs to adapt their speaking style based on spoken instructions has received limited attention. We introduce Voice Style Adaptation (VSA), a new task that examines whether SLMs can modify their speaking style, such as timbre, prosody, or persona following natural language spoken commands. To study this task, we present VStyle, a bilingual (Chinese & English) benchmark covering four categories of speech generation: acoustic attributes, natural language instruction, role play, and implicit empathy. We also introduce the Large Audio Language Model as a Judge (LALM as a Judge) framework, which progressively evaluates outputs along textual faithfulness, style adherence, and naturalness, ensuring reproducible and objective assessment. Experiments on commercial systems and open source SLMs demonstrate that current models face clear limitations in controllable style adaptation, highlighting both the novelty and challenge of this task. By releasing VStyle and its evaluation toolkit, we aim to provide the community with a foundation for advancing human centered spoken interaction. The dataset and code are publicly available at \href{https://junzhan2000.github.io/VStyle.github.io/}{project's homepage}.

</details>

### [Continuous Audio Language Models](2509.06926.md)
**Simon Rouard, Manu Orsini, Axel Roebel, Neil Zeghidour et al.** · 2025-09-08

<details>
<summary>Abstract</summary>

Audio Language Models (ALM) have emerged as the dominant paradigm for speech and music generation by representing audio as sequences of discrete tokens. Yet, unlike text tokens, which are invertible, audio tokens are extracted from lossy codecs with a limited bitrate. As a consequence, increasing audio quality requires generating more tokens, which imposes a trade-off between fidelity and computational cost. We address this issue by studying Continuous Audio Language Models (CALM). These models instantiate a large Transformer backbone that produces a contextual embedding at every timestep. This sequential information then conditions an MLP that generates the next continuous frame of an audio VAE through consistency modeling. By avoiding lossy compression, CALM achieves higher quality at lower computational cost than their discrete counterpart. Experiments on speech and music demonstrate improved efficiency and fidelity over state-of-the-art discrete audio language models, facilitating lightweight, high-quality audio generation. Samples are available at hf.co/spaces/kyutai/calm-samples. Finally, we release Pocket TTS, an open-source 100M-parameter text-to-speech model that can run faster than real time on a laptop CPU: github.com/kyutai-labs/pocket-tts.

</details>

### [Multimodal Fine-grained Context Interaction Graph Modeling for Conversational Speech Synthesis](2509.06074.md)
**Zhenqi Jia et.al.** · 2025-09-07

### [UniVerse-1: Unified Audio-Video Generation via Stitching of Experts](2509.06155.md)
**Duomin Wang, Wei Zuo, Aojie Li, Ling-Hao Chen et al.** · 2025-09-07

<details>
<summary>Abstract</summary>

We introduce UniVerse-1, a unified, Veo-3-like model capable of simultaneously generating coordinated audio and video. To enhance training efficiency, we bypass training from scratch and instead employ a stitching of experts (SoE) technique. This approach deeply fuses the corresponding blocks of pre-trained video and music generation experts models, thereby fully leveraging their foundational capabilities. To ensure accurate annotations and temporal alignment for both ambient sounds and speech with video content, we developed an online annotation pipeline that processes the required training data and generates labels during training process. This strategy circumvents the performance degradation often caused by misalignment text-based annotations. Through the synergy of these techniques, our model, after being finetuned on approximately 7,600 hours of audio-video data, produces results with well-coordinated audio-visuals for ambient sounds generation and strong alignment for speech generation. To systematically evaluate our proposed method, we introduce Verse-Bench, a new benchmark dataset. In an effort to advance research in audio-video generation and to close the performance gap with state-of-the-art models such as Veo3, we make our model and code publicly available. We hope this contribution will benefit the broader research community. Project page: https://dorniwang.github.io/UniVerse-1/.

</details>

### [LatinX: Aligning a Multilingual TTS Model with Direct Preference Optimization](2509.05863.md)
**Luis Felipe Chary, Miguel Arjona Ramirez** · 2025-09-06

<details>
<summary>Abstract</summary>

We present LatinX, a multilingual text-to-speech (TTS) model for cascaded speech-to-speech translation that preserves the source speaker's identity across languages. LatinX is a 12-layer decoder-only Transformer trained in three stages: (i) pre-training for text-to-audio mapping, (ii) supervised fine-tuning for zero-shot voice cloning, and (iii) alignment with Direct Preference Optimization (DPO) using automatically labeled pairs based on Word Error Rate (WER) and speaker-similarity metrics. Trained on English and Romance languages with emphasis on Portuguese, LatinX with DPO consistently reduces WER and improves objective similarity over the fine-tuned baseline. Human evaluations further indicate stronger perceived speaker similarity than a strong baseline (XTTSv2), revealing gaps between objective and subjective measures. We provide cross-lingual analyses and discuss balanced preference signals and lower-latency architectures as future work.

</details>

### [Open-Source Full-Duplex Conversational Datasets for Natural and Interactive Speech Synthesis](2509.04093.md)
**Zhitong Zhou et.al.** · 2025-09-04

### [LibriQuote: A Speech Dataset of Fictional Character Utterances for Expressive Zero-Shot Speech Synthesis](2509.04072.md)
**Gaspard Michel et.al.** · 2025-09-04

### [Say More with Less: Variable-Frame-Rate Speech Tokenization via Adaptive Clustering and Implicit Duration Coding](2509.04685.md)
**Rui-Chen Zheng, Wenrui Liu, Hui-Peng Du, Qinglin Zhang et al.** · 2025-09-04

<details>
<summary>Abstract</summary>

Existing speech tokenizers typically assign a fixed number of tokens per second, regardless of the varying information density or temporal fluctuations in the speech signal. This uniform token allocation mismatches the intrinsic structure of speech, where information is distributed unevenly over time. To address this, we propose VARSTok, a VAriable-frame-Rate Speech Tokenizer that adapts token allocation based on local feature similarity. VARSTok introduces two key innovations: (1) a temporal-aware density peak clustering algorithm that adaptively segments speech into variable-length units, and (2) a novel implicit duration coding scheme that embeds both content and temporal span into a single token index, eliminating the need for auxiliary duration predictors. Extensive experiments show that VARSTok significantly outperforms strong fixed-rate baselines. Notably, it achieves superior reconstruction naturalness while using up to 23% fewer tokens than a 40 Hz fixed-frame-rate baseline. VARSTok further yields lower word error rates and improved naturalness in zero-shot text-to-speech synthesis. To the best of our knowledge, this is the first work to demonstrate that a fully dynamic, variable-frame-rate acoustic speech tokenizer can be seamlessly integrated into downstream speech language models.

</details>

### [AUDETER: A Large-scale Dataset for Deepfake Audio Detection in Open Worlds](2509.04345.md)
**Qizhou Wang, Hanxun Huang, Guansong Pang, Sarah Erfani et al.** · 2025-09-04

<details>
<summary>Abstract</summary>

Speech synthesis systems can now produce highly realistic vocalisations that pose significant authenticity challenges. Despite substantial progress in deepfake detection models, their real-world effectiveness is often undermined by evolving distribution shifts between training and test data, driven by the complexity of human speech and the rapid evolution of synthesis systems. Existing datasets suffer from limited real speech diversity, insufficient coverage of recent synthesis systems, and heterogeneous mixtures of deepfake sources, which hinder systematic evaluation and open-world model training. To address these issues, we introduce AUDETER (AUdio DEepfake TEst Range), a large-scale and highly diverse deepfake audio dataset comprising over 4,500 hours of synthetic audio generated by 11 recent TTS models and 10 vocoders, totalling 3 million clips. We further observe that most existing detectors default to binary supervised training, which can induce negative transfer across synthesis sources when the training data contains highly diverse deepfake patterns, impacting overall generalisation. As a complementary contribution, we propose an effective curriculum-learning-based approach to mitigate this effect. Extensive experiments show that existing detection models struggle to generalise to novel deepfakes and human speech in AUDETER, whereas XLR-based detectors trained on AUDETER achieve strong cross-domain performance across multiple benchmarks, achieving an EER of 1.87% on In-the-Wild. AUDETER is available on GitHub.

</details>

### [Improving Perceptual Audio Aesthetic Assessment via Triplet Loss and Self-Supervised Embeddings](2509.03292.md)
**Dyah A. M. G. Wisnu, Ryandhimas E. Zezario, Stefano Rini, Hsin-Min Wang et al.** · 2025-09-03

<details>
<summary>Abstract</summary>

We present a system for automatic multi-axis perceptual quality prediction of generative audio, developed for Track 2 of the AudioMOS Challenge 2025. The task is to predict four Audio Aesthetic Scores--Production Quality, Production Complexity, Content Enjoyment, and Content Usefulness--for audio generated by text-to-speech (TTS), text-to-audio (TTA), and text-to-music (TTM) systems. A main challenge is the domain shift between natural training data and synthetic evaluation data. To address this, we combine BEATs, a pretrained transformer-based audio representation model, with a multi-branch long short-term memory (LSTM) predictor and use a triplet loss with buffer-based sampling to structure the embedding space by perceptual similarity. Our results show that this improves embedding discriminability and generalization, enabling domain-robust audio quality assessment without synthetic training data.

</details>

### [AIVA: An AI-based Virtual Companion for Emotion-aware Interaction](2509.03212.md)
**Chenxi Li** · 2025-09-03

<details>
<summary>Abstract</summary>

Recent advances in Large Language Models (LLMs) have significantly improved natural language understanding and generation, enhancing Human-Computer Interaction (HCI). However, LLMs are limited to unimodal text processing and lack the ability to interpret emotional cues from non-verbal signals, hindering more immersive and empathetic interactions. This work explores integrating multimodal sentiment perception into LLMs to create emotion-aware agents. We propose \ours, an AI-based virtual companion that captures multimodal sentiment cues, enabling emotionally aligned and animated HCI. \ours introduces a Multimodal Sentiment Perception Network (MSPN) using a cross-modal fusion transformer and supervised contrastive learning to provide emotional cues. Additionally, we develop an emotion-aware prompt engineering strategy for generating empathetic responses and integrate a Text-to-Speech (TTS) system and animated avatar module for expressive interactions. \ours provides a framework for emotion-aware agents with applications in companion robotics, social care, mental health, and human-centered AI.

</details>

### [Multi-level SSL Feature Gating for Audio Deepfake Detection](2509.03409.md)
**Hoan My Tran, Damien Lolive, Aghilas Sini, Arnaud Delhay et al.** · 2025-09-03

<details>
<summary>Abstract</summary>

Recent advancements in generative AI, particularly in speech synthesis, have enabled the generation of highly natural-sounding synthetic speech that closely mimics human voices. While these innovations hold promise for applications like assistive technologies, they also pose significant risks, including misuse for fraudulent activities, identity theft, and security threats. Current research on spoofing detection countermeasures remains limited by generalization to unseen deepfake attacks and languages. To address this, we propose a gating mechanism extracting relevant feature from the speech foundation XLS-R model as a front-end feature extractor. For downstream back-end classifier, we employ Multi-kernel gated Convolution (MultiConv) to capture both local and global speech artifacts. Additionally, we introduce Centered Kernel Alignment (CKA) as a similarity metric to enforce diversity in learned features across different MultiConv layers. By integrating CKA with our gating mechanism, we hypothesize that each component helps improving the learning of distinct synthetic speech patterns. Experimental results demonstrate that our approach achieves state-of-the-art performance on in-domain benchmarks while generalizing robustly to out-of-domain datasets, including multilingual speech samples. This underscores its potential as a versatile solution for detecting evolving speech deepfake threats.

</details>

### [FireRedTTS-2: Towards Long Conversational Speech Generation for Podcast and Chatbot](2509.02020.md)
**Kun Xie, Feiyu Shen, Junjie Li, Fenglong Xie et al.** · 2025-09-02

<details>
<summary>Abstract</summary>

Current dialogue generation approaches typically require the complete dialogue text before synthesis and produce a single, inseparable speech containing all voices, making them unsuitable for interactive chat; moreover, they suffer from unstable synthesis, inaccurate speaker transitions, and incoherent prosody. In this work, we present FireRedTTS-2, a long-form streaming TTS system for multi-speaker dialogue generation, delivering stable, natural speech with reliable speaker switching and context-aware prosody. A new 12.5Hz streaming speech tokenizer accelerates training and inference, extends maximum dialogue length, encodes richer semantics to stabilize text-to-token modeling and supports high-fidelity streaming generation for real-time applications. We adopt a text-speech interleaved format, concatenating speaker-labeled text with aligned speech tokens in chronological order, and model it with a dual-transformer: a large decoder-only transformer predicts tokens at the first layer, and a smaller one completes subsequent layers. Experimental results show that FireRedTTS-2 integrates seamlessly with chat frameworks and, with minimal fine-tuning, produces emotionally expressive speech guided by implicit contextual cues. In podcast generation, it surpasses existing systems including MoonCast, Zipvoice-Dialogue, and MOSS-TTSD in objective intelligibility, speaker-turn reliability, and perceived naturalness with context-consistent prosody. Our demos are available at https://fireredteam.github.io/demos/firered_tts_2.

</details>

### [MixedG2P-T5: G2P-free Speech Synthesis for Mixed-script texts using Speech Self-Supervised Learning and Language Model](2509.01391.md)
**Joonyong Park et.al.** · 2025-09-01

### [Efficient and Natural Tibetan Speech Synthesis via Gaussian Noise-Improved Monotonic Alignment Search and Lightweight iSTFT Multiband Decoder](s2:261ceb3853e1cc47a7b6e91dc66921e1228dc1e7.md)
**Shiqi Wu, Yue Zhao, Jing Yu, Xiaona Xu et al.** · 2025-09-01

<details>
<summary>Abstract</summary>

Although end-to-end speech synthesis technology has made significant progress in general domains, Tibetan speech synthesis still faces issues such as inaccurate alignment and unnatural synthesis due to its unique linguistic features and low-resource data sparsity. To address these challenges, this paper proposes the EnhancedTTS model, which incorporates a random duration predictor based on generative adversarial networks, a Gaussian noise-enhanced monotonic alignment search algorithm, and a Transformer block with residual connections to significantly improve the modeling accuracy of complex Tibetan syllable boundaries. Additionally, the model uses iSTFT and multi-band parallel strategies in the decoder to enhance inference speed. Furthermore, Tibetan character components are used as modeling units, providing a more accurate representation of Tibetan’s unique phonetic and structural features. To validate the e ff ectiveness of the proposed model, experiments were conducted using a Tibetan Amdo dialect dataset, and comparisons were made with the VITS and FastSpeech2 models. The results show significant breakthroughs in both speech quality and e ffi ciency. The MOS score reached 4.69, improving by 3.1% and 1.5% over VITS and FastSpeech2. Objective tests showed significant optimizations in RMSE and MCD, with inference speed increasing by 2-5 times. Ablation experiments further confirmed the e ff ectiveness of the key modules.

</details>

### [MPO: Multidimensional Preference Optimization for Language Model-based Text-to-Speech](2509.00685.md)
**Kangxiang Xia et.al.** · 2025-08-31

### [Speaker-Conditioned Phrase Break Prediction for Text-to-Speech with Phoneme-Level Pre-trained Language Model](2509.00675.md)
**Dong Yang, Yuki Saito, Takaaki Saeki, Tomoki Koriyama et al.** · 2025-08-31

<details>
<summary>Abstract</summary>

This paper advances phrase break prediction (also known as phrasing) in multi-speaker text-to-speech (TTS) systems. We integrate speaker-specific features by leveraging speaker embeddings to enhance the performance of the phrasing model. We further demonstrate that these speaker embeddings can capture speaker-related characteristics solely from the phrasing task. Besides, we explore the potential of pre-trained speaker embeddings for unseen speakers through a few-shot adaptation method. Furthermore, we pioneer the application of phoneme-level pre-trained language models to this TTS front-end task, which significantly boosts the accuracy of the phrasing model. Our methods are rigorously assessed through both objective and subjective evaluations, demonstrating their effectiveness.

</details>

### [Entropy-based Coarse and Compressed Semantic Speech Representation Learning](2509.00503.md)
**Jialong Zuo, Guangyan Zhang, Minghui Fang, Shengpeng Ji et al.** · 2025-08-30

<details>
<summary>Abstract</summary>

Discrete speech representation learning has recently attracted increasing interest in both acoustic and semantic modeling. Existing approaches typically encode 16 kHz waveforms into discrete tokens at a rate of 25 or 50 tokens per second. However, given that speech generally conveys only 2 to 5 words per second, such fine-grained tokenization introduces redundancy and hinders efficiency in downstream training and inference. Moreover, semantic speech representations at this frequency primarily capture phonetic-level information, while semantic understanding may not require such detailed token-level resolution. To address these limitations, we propose an entropy-based dynamic aggregation framework for learning compressed semantic speech representations. A speech language model is first pre-trained via next-token prediction on large-scale unlabeled data to capture frequent token patterns. Predictive entropy is then used to adaptively determine aggregation boundaries, followed by a cross-attention module that fuses information within each segment. By adjusting the entropy threshold, the granularity and compression ratio of the representations can be flexibly controlled. Experiments on ASR, speech-to-text translation, and voice conversion tasks demonstrate that the compressed representations perform on par with or better than dense token sequences, demonstrating the effectiveness of the proposed approach.

</details>

### [Talking Spell: A Wearable System Enabling Real-Time Anthropomorphic Voice Interaction with Everyday Objects](2509.02367.md)
**Xuetong Wang, Ching Christie Pang, Pan Hui** · 2025-08-28

<details>
<summary>Abstract</summary>

Virtual assistants (VAs) have become ubiquitous in daily life, integrated into smartphones and smart devices, sparking interest in AI companions that enhance user experiences and foster emotional connections. However, existing companions are often embedded in specific objects-such as glasses, home assistants, or dolls-requiring users to form emotional bonds with unfamiliar items, which can lead to reduced engagement and feelings of detachment. To address this, we introduce Talking Spell, a wearable system that empowers users to imbue any everyday object with speech and anthropomorphic personas through a user-centric radiative network. Leveraging advanced computer vision (e.g., YOLOv11 for object detection), large vision-language models (e.g., QWEN-VL for persona generation), speech-to-text and text-to-speech technologies, Talking Spell guides users through three stages of emotional connection: acquaintance, familiarization, and bonding. We validated our system through a user study involving 12 participants, utilizing Talking Spell to explore four interaction intentions: entertainment, companionship, utility, and creativity. The results demonstrate its effectiveness in fostering meaningful interactions and emotional significance with everyday objects. Our findings indicate that Talking Spell creates engaging and personalized experiences, as demonstrated through various devices, ranging from accessories to essential wearables.

</details>

### [Vocoder-Projected Feature Discriminator](2508.17874.md)
**Takuhiro Kaneko et.al.** · 2025-08-27

### [CLEAR: Continuous Latent Autoregressive Modeling for High-quality and Low-latency Speech Synthesis](2508.19098.md)
**Chun Yat Wu et.al.** · 2025-08-26

### [Unseen Speaker and Language Adaptation for Lightweight Text-To-Speech with Adapters](2508.18006.md)
**Alessio Falai et.al.** · 2025-08-25

### [EMO-Reasoning: Benchmarking Emotional Reasoning Capabilities in Spoken Dialogue Systems](2508.17623.md)
**Jingwen Liu, Kan Jen Cheng, Jiachen Lian, Akshay Anand et al.** · 2025-08-25

<details>
<summary>Abstract</summary>

Speech emotions play a crucial role in human-computer interaction, shaping engagement and context-aware communication. Despite recent advances in spoken dialogue systems, a holistic system for evaluating emotional reasoning is still lacking. To address this, we introduce EMO-Reasoning, a benchmark for assessing emotional coherence in dialogue systems. It leverages a curated dataset generated via text-to-speech to simulate diverse emotional states, overcoming the scarcity of emotional speech data. We further propose the Cross-turn Emotion Reasoning Score to assess the emotion transitions in multi-turn dialogues. Evaluating seven dialogue systems through continuous, categorical, and perceptual metrics, we show that our framework effectively detects emotional inconsistencies, providing insights for improving current dialogue systems. By releasing a systematic evaluation benchmark, we aim to advance emotion-aware spoken dialogue modeling toward more natural and adaptive interactions.

</details>

### [FasterVoiceGrad: Faster One-step Diffusion-Based Voice Conversion with Adversarial Diffusion Conversion Distillation](2508.17868.md)
**Takuhiro Kaneko, Hirokazu Kameoka, Kou Tanaka, Yuto Kondo** · 2025-08-25

<details>
<summary>Abstract</summary>

A diffusion-based voice conversion (VC) model (e.g., VoiceGrad) can achieve high speech quality and speaker similarity; however, its conversion process is slow owing to iterative sampling. FastVoiceGrad overcomes this limitation by distilling VoiceGrad into a one-step diffusion model. However, it still requires a computationally intensive content encoder to disentangle the speaker's identity and content, which slows conversion. Therefore, we propose FasterVoiceGrad, a novel one-step diffusion-based VC model obtained by simultaneously distilling a diffusion model and content encoder using adversarial diffusion conversion distillation (ADCD), where distillation is performed in the conversion process while leveraging adversarial and score distillation training. Experimental evaluations of one-shot VC demonstrated that FasterVoiceGrad achieves competitive VC performance compared to FastVoiceGrad, with 6.6-6.9 and 1.8 times faster speed on a GPU and CPU, respectively.

</details>

### [Improving French Synthetic Speech Quality via SSML Prosody Control](2508.17494.md)
**Nassima Ould Ouali, Awais Hussain Sani, Ruben Bueno, Jonah Dauvet et al.** · 2025-08-24

<details>
<summary>Abstract</summary>

Despite recent advances, synthetic voices often lack expressiveness due to limited prosody control in commercial text-to-speech (TTS) systems. We introduce the first end-to-end pipeline that inserts Speech Synthesis Markup Language (SSML) tags into French text to control pitch, speaking rate, volume, and pause duration. We employ a cascaded architecture with two QLoRA-fine-tuned Qwen 2.5-7B models: one predicts phrase-break positions and the other performs regression on prosodic targets, generating commercial TTS-compatible SSML markup. Evaluated on a 14-hour French podcast corpus, our method achieves 99.2% F1 for break placement and reduces mean absolute error on pitch, rate, and volume by 25-40% compared with prompting-only large language models (LLMs) and a BiLSTM baseline. In perceptual evaluation involving 18 participants across over 9 hours of synthesized audio, SSML-enhanced speech generated by our pipeline significantly improves naturalness, with the mean opinion score increasing from 3.20 to 3.87 (p < 0.005). Additionally, 15 of 18 listeners preferred our enhanced synthesis. These results demonstrate substantial progress in bridging the expressiveness gap between synthetic and natural French speech. Our code is publicly available at https://github.com/hi-paris/Prosody-Control-French-TTS.

</details>

### [Speech synthesis for Walloon, an under-resourced minority language](s2:b090a3a8f2743c2ed9cfbfcf2676edacceb924fc.md)
**Jose Felipe Espinosa Orjuela, Philippe Boula de Mareüil, Marc Evrard** · 2025-08-24

<details>
<summary>Abstract</summary>

This paper describes a text-to-speech synthesis system for Walloon, a Gallo-Romance language spoken in Belgium and part of France (in the Ardennes department). The system uses recordings of a translation of The Little Prince , read entirely by a male speaker (156 minutes) and, for the first chapters, a female speaker (18 minutes). The corpus was segmented into sentences and transcribed into phonemes by a rule-based grapheme-to-phoneme converter. The synthesis system is based on the Variational Inference with Adversarial Learning for End-to-End Text-to-Speech ( VITS ) architecture, and several models were trained in different conditions: with or without grapheme-to-phoneme conversion, using or not a fine-tuned model pre-trained on a French corpus. A perceptual evaluation campaign was conducted with Walloon speakers. Results suggest that the models resorting to French data are only preferred in the training condition with the 18-minute reduced corpus.

</details>

### [RephraseTTS: Dynamic Length Text based Speech Insertion with Speaker Style Transfer](2508.17031.md)
**Neeraj Matiyali, Siddharth Srivastava, Gaurav Sharma** · 2025-08-23

<details>
<summary>Abstract</summary>

We propose a method for the task of text-conditioned speech insertion, i.e. inserting a speech sample in an input speech sample, conditioned on the corresponding complete text transcript. An example use case of the task would be to update the speech audio when corrections are done on the corresponding text transcript. The proposed method follows a transformer-based non-autoregressive approach that allows speech insertions of variable lengths, which are dynamically determined during inference, based on the text transcript and tempo of the available partial input. It is capable of maintaining the speaker's voice characteristics, prosody and other spectral properties of the available speech input. Results from our experiments and user study on LibriTTS show that our method outperforms baselines based on an existing adaptive text to speech method. We also provide numerous qualitative results to appreciate the quality of the output from the proposed method.

</details>

### [TaDiCodec: Text-aware Diffusion Speech Tokenizer for Speech Language Modeling](2508.16790.md)
**Yuancheng Wang et.al.** · 2025-08-22

### [Seeing is Believing: Emotion-Aware Audio-Visual Language Modeling for Expressive Speech Generation](2508.16188.md)
**Weiting Tan et.al.** · 2025-08-22

### [From Signs to Speech: An End-to-End Conversational Platform for Deaf and Mute Individuals Using GRU and LLM Integration](s2:2c12e8eb7ed55081c3facd2c88692e4faa68a123.md)
**A. Chauhan, Abdulqadir Kayamkhani, Atharva Gujar, Mandar Gade et al.** · 2025-08-22

<details>
<summary>Abstract</summary>

Deaf and mute individuals are often disadvantaged in professional interview settings due to limited verbal communication, despite possessing relevant qualifications. This paper presents an AI-driven system designed to facilitate seamless bidirectional communication through real-time sign language recognition and speech synthesis. A custom dataset of ten technical signs, formulated through surveys in special education institutions were recorded using Mediapipe and OpenCV. A three-layer Gated Recurrent Unit (GRU) model achieved 97% training accuracy and 94% test accuracy, outperforming LSTM and BiGRU architectures. Dropout regularization was applied to mitigate overfitting. A locally hosted Ollama LLM model was employed to enhance grammatical accuracy of sign-to-text-to-voice outputs. The interface, developed using Streamlit, supports user interaction, while Firebase manages backend communication. Precision and recall values of 93 % and 92 % respectively demonstrate the system's reliability. This work proposes a deployable, inclusive solution aimed at improving accessibility and opportunity for deaf-mute individuals in professional environments.

</details>

### [Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets](2508.15442.md)
**Chenlin Liu, Minghui Fang, Patrick Zhang, Wei Zhou et al.** · 2025-08-21

<details>
<summary>Abstract</summary>

Language Model (LM)-based Text-to-Speech (TTS) systems often generate hallucinated speech that deviates from input text. Existing mitigation strategies either demand excessive training resources or introduce significant inference latency. In this paper, we propose GFlOwNet-guided distribution AlignmenT (GOAT) for LM-based TTS, a post-training framework that mitigates hallucinations without relying on massive resources or inference cost. Specifically, we first conduct an uncertainty analysis, revealing a strong positive correlation between hallucination and model uncertainty. Based on this, we reformulate TTS generation as a trajectory flow optimization problem and introduce an enhanced Subtrajectory Balance objective together with a sharpened internal reward as target distribution. We further integrate reward temperature decay and learning rate optimization for stability and performance balance. Extensive experiments show that GOAT reduce over 50% character error rates on challenging test cases and lowering uncertainty by up to 58%, demonstrating its strong generalization ability and effectiveness.

</details>

### [QvTAD: Differential Relative Attribute Learning for Voice Timbre Attribute Detection](2508.15931.md)
**Zhiyu Wu, Jingyi Fang, Yufei Tang, Yuanzhong Zheng et al.** · 2025-08-21

<details>
<summary>Abstract</summary>

Voice Timbre Attribute Detection (vTAD) plays a pivotal role in fine-grained timbre modeling for speech generation tasks. However, it remains challenging due to the inherently subjective nature of timbre descriptors and the severe label imbalance in existing datasets. In this work, we present QvTAD, a novel pairwise comparison framework based on differential attention, designed to enhance the modeling of perceptual timbre attributes. To address the label imbalance in the VCTK-RVA dataset, we introduce a graph-based data augmentation strategy that constructs a Directed Acyclic Graph and employs Disjoint-Set Union techniques to automatically mine unobserved utterance pairs with valid attribute comparisons. Our framework leverages speaker embeddings from a pretrained FACodec, and incorporates a Relative Timbre Shift-Aware Differential Attention module. This module explicitly models attribute-specific contrasts between paired utterances via differential denoising and contrast amplification mechanisms. Experimental results on the VCTK-RVA benchmark demonstrate that QvTAD achieves substantial improvements across multiple timbre descriptors, with particularly notable gains in cross-speaker generalization scenarios.

</details>

### [Any-to-any Speaker Attribute Perturbation for Asynchronous Voice Anonymization](2508.15565.md)
**Liping Chen, Chenyang Guo, Rui Wang, Kong Aik Lee et al.** · 2025-08-21

<details>
<summary>Abstract</summary>

Speaker attribute perturbation offers a feasible approach to asynchronous voice anonymization by employing adversarially perturbed speech as anonymized output. In order to enhance the identity unlinkability among anonymized utterances from the same original speaker, the targeted attack training strategy is usually applied to anonymize the utterances to a common designated speaker. However, this strategy may violate the privacy of the designated speaker who is an actual speaker. To mitigate this risk, this paper proposes an any-to-any training strategy. It is accomplished by defining a batch mean loss to anonymize the utterances from various speakers within a training mini-batch to a common pseudo-speaker, which is approximated as the average speaker in the mini-batch. Based on this, a speaker-adversarial speech generation model is proposed, incorporating the supervision from both the untargeted attack and the any-to-any strategies. The speaker attribute perturbations are generated and incorporated into the original speech to produce its anonymized version. The effectiveness of the proposed model was justified in asynchronous voice anonymization through experiments conducted on the VoxCeleb datasets. Additional experiments were carried out to explore the potential limitations of speaker-adversarial speech in voice privacy protection. With them, we aim to provide insights for future research on its protective efficacy against black-box speaker extractors \textcolor{black}{and adaptive attacks, as well as} generalization to out-of-domain datasets \textcolor{black}{and stability}. Audio samples and open-source code are published in https://github.com/VoicePrivacy/any-to-any-speaker-attribute-perturbation.

</details>

### [Improving Resource-Efficient Speech Enhancement via Neural Differentiable DSP Vocoder Refinement](2508.14709.md)
**Heitor R. Guimarães et.al.** · 2025-08-20

### [Long-Context Speech Synthesis with Context-Aware Memory](2508.14713.md)
**Zhipeng Li, Xiaofen Xing, Jingyuan Xing, Hangrui Hu et al.** · 2025-08-20

<details>
<summary>Abstract</summary>

In long-text speech synthesis, current approaches typically convert text to speech at the sentence-level and concatenate the results to form pseudo-paragraph-level speech. These methods overlook the contextual coherence of paragraphs, leading to reduced naturalness and inconsistencies in style and timbre across the long-form speech. To address these issues, we propose a Context-Aware Memory (CAM)-based long-context Text-to-Speech (TTS) model. The CAM block integrates and retrieves both long-term memory and local context details, enabling dynamic memory updates and transfers within long paragraphs to guide sentence-level speech synthesis. Furthermore, the prefix mask enhances the in-context learning ability by enabling bidirectional attention on prefix tokens while maintaining unidirectional generation. Experimental results demonstrate that the proposed method outperforms baseline and state-of-the-art long-context methods in terms of prosody expressiveness, coherence and context inference cost across paragraph-level speech.

</details>

### [Linear Preference Optimization: Decoupled Gradient Control via Absolute Regularization](2508.14947.md)
**Rui Wang, Qianguo Sun, Chao Song, Junlong Wu et al.** · 2025-08-20

<details>
<summary>Abstract</summary>

DPO (Direct Preference Optimization) has become a widely used offline preference optimization algorithm due to its simplicity and training stability. However, DPO is prone to overfitting and collapse. To address these challenges, we propose Linear Preference Optimization (LPO), a novel alignment framework featuring three key innovations. First, we introduce gradient decoupling by replacing the log-sigmoid function with an absolute difference loss, thereby isolating the optimization dynamics. Second, we improve stability through an offset constraint combined with a positive regularization term to preserve the chosen response quality. Third, we implement controllable rejection suppression using gradient separation with straightforward estimation and a tunable coefficient that linearly regulates the descent of the rejection probability. Through extensive experiments, we demonstrate that LPO consistently improves performance on various tasks, including general text tasks, math tasks, and text-to-speech (TTS) tasks. These results establish LPO as a robust and tunable paradigm for preference alignment, and we release the source code, models, and training data publicly.

</details>

### [DiffIER: Optimizing Diffusion Models with Iterative Error Reduction](2508.13628.md)
**Ao Chen, Lihe Ding, Tianfan Xue** · 2025-08-19

<details>
<summary>Abstract</summary>

Diffusion models have demonstrated remarkable capabilities in generating high-quality samples and enhancing performance across diverse domains through Classifier-Free Guidance (CFG). However, the quality of generated samples is highly sensitive to the selection of the guidance weight. In this work, we identify a critical ``training-inference gap'' and we argue that it is the presence of this gap that undermines the performance of conditional generation and renders outputs highly sensitive to the guidance weight. We quantify this gap by measuring the accumulated error during the inference stage and establish a correlation between the selection of guidance weight and minimizing this gap. Furthermore, to mitigate this gap, we propose DiffIER, an optimization-based method for high-quality generation. We demonstrate that the accumulated error can be effectively reduced by an iterative error minimization at each step during inference. By introducing this novel plug-and-play optimization framework, we enable the optimization of errors at every single inference step and enhance generation quality. Empirical results demonstrate that our proposed method outperforms baseline approaches in conditional generation tasks. Furthermore, the method achieves consistent success in text-to-image generation, image super-resolution, and text-to-speech generation, underscoring its versatility and potential for broad applications in future research.

</details>

### [Who Gets the Mic? Investigating Gender Bias in the Speaker Assignment of a Speech-LLM](2508.13603.md)
**Dariia Puhach, Amir H. Payberah, Éva Székely** · 2025-08-19

<details>
<summary>Abstract</summary>

Similar to text-based Large Language Models (LLMs), Speech-LLMs exhibit emergent abilities and context awareness. However, whether these similarities extend to gender bias remains an open question. This study proposes a methodology leveraging speaker assignment as an analytic tool for bias investigation. Unlike text-based models, which encode gendered associations implicitly, Speech-LLMs must produce a gendered voice, making speaker selection an explicit bias cue. We evaluate Bark, a Text-to-Speech (TTS) model, analyzing its default speaker assignments for textual prompts. If Bark's speaker selection systematically aligns with gendered associations, it may reveal patterns in its training data or model design. To test this, we construct two datasets: (i) Professions, containing gender-stereotyped occupations, and (ii) Gender-Colored Words, featuring gendered connotations. While Bark does not exhibit systematic bias, it demonstrates gender awareness and has some gender inclinations.

</details>

### [Real-Time Sign Language Gestures to Speech Transcription using Deep Learning](2508.12713.md)
**Brandone Fonya, Clarence Worrell** · 2025-08-18

<details>
<summary>Abstract</summary>

Communication barriers pose significant challenges for individuals with hearing and speech impairments, often limiting their ability to effectively interact in everyday environments. This project introduces a real-time assistive technology solution that leverages advanced deep learning techniques to translate sign language gestures into textual and audible speech. By employing convolution neural networks (CNN) trained on the Sign Language MNIST dataset, the system accurately classifies hand gestures captured live via webcam. Detected gestures are instantaneously translated into their corresponding meanings and transcribed into spoken language using text-to-speech synthesis, thus facilitating seamless communication. Comprehensive experiments demonstrate high model accuracy and robust real-time performance with some latency, highlighting the system's practical applicability as an accessible, reliable, and user-friendly tool for enhancing the autonomy and integration of sign language users in diverse social settings.

</details>

### [Integrating Feedback Loss from Bi-modal Sarcasm Detector for Sarcastic Speech Synthesis](2508.13028.md)
**Zhu Li, Yuqing Zhang, Xiyuan Gao, Devraj Raghuvanshi et al.** · 2025-08-18

<details>
<summary>Abstract</summary>

Sarcastic speech synthesis, which involves generating speech that effectively conveys sarcasm, is essential for enhancing natural interactions in applications such as entertainment and human-computer interaction. However, synthesizing sarcastic speech remains a challenge due to the nuanced prosody that characterizes sarcasm, as well as the limited availability of annotated sarcastic speech data. To address these challenges, this study introduces a novel approach that integrates feedback loss from a bi-modal sarcasm detection model into the TTS training process, enhancing the model's ability to capture and convey sarcasm. In addition, by leveraging transfer learning, a speech synthesis model pre-trained on read speech undergoes a two-stage fine-tuning process. First, it is fine-tuned on a diverse dataset encompassing various speech styles, including sarcastic speech. In the second stage, the model is further refined using a dataset focused specifically on sarcastic speech, enhancing its ability to generate sarcasm-aware speech. Objective and subjective evaluations demonstrate that our proposed methods improve the quality, naturalness, and sarcasm-awareness of synthesized speech.

</details>

### [Mini-Omni-Reasoner: Token-Level Thinking-in-Speaking in Large Speech Models](2508.15827.md)
**Zhifei Xie, Ziyang Ma, Zihang Liu, Kaiyu Pang et al.** · 2025-08-18

<details>
<summary>Abstract</summary>

Reasoning is essential for effective communication and decision-making. While recent advances in LLMs and MLLMs have shown that incorporating explicit reasoning significantly improves understanding and generalization, reasoning in LSMs remains in a nascent stage. Early efforts attempt to transfer the "Thinking-before-Speaking" paradigm from textual models to speech. However, this sequential formulation introduces notable latency, as spoken responses are delayed until reasoning is fully completed, impairing real-time interaction and communication efficiency. To address this, we propose Mini-Omni-Reasoner, a framework that enables reasoning within speech via a novel "Thinking-in-Speaking" formulation. Rather than completing reasoning before producing any verbal output, Mini-Omni-Reasoner interleaves silent reasoning tokens with spoken response tokens at the token level. This design allows continuous speech generation while embedding structured internal reasoning, leveraging the model's high-frequency token processing capability. Although interleaved, local semantic alignment is enforced to ensure that each response token is informed by its preceding reasoning. To support this framework, we introduce Spoken-Math-Problems-3M, a large-scale dataset tailored for interleaved reasoning and response. The dataset ensures that verbal tokens consistently follow relevant reasoning content, enabling accurate and efficient learning of speech-coupled reasoning. Built on a hierarchical Thinker-Talker architecture, Mini-Omni-Reasoner delivers fluent yet logically grounded spoken responses, maintaining both naturalness and precision. On the Spoken-MQA benchmark, it achieves a +19.1% gain in arithmetic reasoning and +6.4% in contextual understanding, with shorter outputs and zero decoding latency.

</details>

### [GST-BERT-TTS: Prosody Prediction Without Accentual Labels For Multi-Speaker TTS Using BERT With Global Style Tokens](s2:d7186392cf0f2aa8805be525ab20e8d4f5b13f0e.md)
**Tadashi Ogura, T. Okamoto, Yamato Ohtani, Erica Cooper et al.** · 2025-08-17

<details>
<summary>Abstract</summary>

Prosody prediction is crucial for pitch-accent languages like Japanese in text-to-speech (TTS) synthesis. Traditional meth-ods rely on accent labels, which are often incomplete and do not generalize well. BERT-based models, such as f o -BERT, enable fundamental frequency prediction without accent labels but have been limited to single-speaker TTS. We propose GST-BERT-TTS, a novel method for multi-speaker TTS that integrates speaker-specific style embeddings from global style to-kens (GST) into the token embeddings in BERT. The proposed method can realize speaker-aware fundamental frequency ( f o ) prediction in an accent label-free setting. Additionally, we extend f o -BERT to predict not only log f o but also energy and duration, improving speech expressiveness. Experiments using a Japanese multi-speaker TTS corpus demonstrate that GST-BERT-TTS improves the prosody prediction accuracy and synthesis quality compared with f o -BERT.

</details>

### [Multimodal Prosody Modeling: A Use Case for Multilingual Sentence Mode Prediction](s2:33b0d3c7985f02b394218321513d2546e59ee9b2.md)
**Bogdan Vlasenko, Mathew Magimai.-Doss** · 2025-08-17

<details>
<summary>Abstract</summary>

Prosody modeling has garnered significant attention from the speech processing community. Recent developments in multilingual latent spaces for representing linguistic and acoustic information have become a new trend in various research directions. Therefore, we decided to evaluate the ability of multilingual acoustic neural embeddings and knowledge-based features to preserve sentence-mode-related information at the supraseg-mental level. For linguistic information modeling, we selected neural embeddings based on word-and phoneme-level latent space representations. The experimental study was conducted using Italian, French, and German audiobook recordings, as well as emotional speech samples from EMO-DB. Both intra-and inter-language experimental protocols were used to assess classification performance for uni-and multimodal (early fusion approach) features. For comparison, we used a sentence mode prediction system built on top of automatically generated W HISPER -based transcripts.

</details>

### [ArticulateX: End-to-End Monolingual Speech Translation in Articulator Space](s2:594cdd0052587fcc5c872ea44e92a69382bacc18.md)
**Vishal Kumar, V. Abrol** · 2025-08-17

<details>
<summary>Abstract</summary>

We present ArticulateX, the first non-autoregressive direct speech-to-speech translation (S2ST) model that operates through an articulatory latent space, offering an efficient alternative to existing cascaded models. It consists of a direct speech-to-articulator encoder, a latent articulator-to-MelSpectrogram mapper, and a vocoder for high-fidelity speech synthesis. By leveraging articulatory representations, which are inherently language-agnostic, our model effectively captures speech dynamics, preserving speaker identity, prosody and expressiveness across languages. Unlike prior autoregressive models, ArticulateX eliminates the need for intermediate text, discrete units and/or complex self-supervised objectives, enabling faster inference, stable training, and improved translation quality. We demonstrate the efficacy of the proposed model in fr-en and de-en speech-to-speech translation on the CVSS dataset, achieving BLEU scores better or comparable to existing models.

</details>

### [FNH-TTS: Mixture-of-Experts Duration Modeling for Robust Neural Speech Synthesis](2508.12001.md)
**Qingliang Meng, Yuqing Deng, Wei Liang, Limei Yu et al.** · 2025-08-16

<details>
<summary>Abstract</summary>

Current non-autoregressive (NAR) text-to-speech (TTS) systems still struggle to model diverse and speaker-dependent duration variation. We further observe that richer duration variation can increase the synthesis difficulty of existing HiFi-GAN-based vocoders, leading to spectral artifacts and unstable time-frequency structures. To address these issues, we propose FNH-TTS, a VITS-based end-to-end TTS system with Mixture-of-Experts duration modeling and robust vocoder-side synthesis. Specifically, we introduce a Mixture-of-Experts Duration Predictor (MoE-DP) to capture diverse phoneme duration patterns and speaker-dependent speaking-rate characteristics. To convert richer duration variation into stable waveform generation, we further integrate a VOCOS-style vocoder with Collaborative Multi-Band and Sub-Band Discriminators. Experiments on LJSpeech, VCTK, and LibriTTS show that FNH-TTS achieves improved synthesis quality, duration-category accuracy, vocoder reconstruction quality, and inference efficiency. Further analysis shows that MoE-DP is the main source of improved duration modeling, while stronger vocoder-side components are necessary for robust synthesis under richer duration variation.

</details>

### [MultiAiTutor: Child-Friendly Educational Multilingual Speech Generation Tutor with LLMs](2508.08715.md)
**Xiaoxue Gao et.al.** · 2025-08-15

### [MoE-TTS: Enhancing Out-of-Domain Text Understanding for Description-based TTS via Mixture-of-Experts](2508.11326.md)
**Heyang Xue, Xuchen Song, Yu Tang, Jianyu Chen et al.** · 2025-08-15

<details>
<summary>Abstract</summary>

Description-based text-to-speech (TTS) models exhibit strong performance on in-domain text descriptions, i.e., those encountered during training. However, in real-world applications, the diverse range of user-generated descriptions inevitably introduces numerous out-of-domain inputs that challenge the text understanding capabilities of these systems. To address this issue, we propose MoE-TTS, a description-based TTS model designed to enhance the understanding of out-of-domain text descriptions. MoE-TTS employs a modality-based mixture-of-experts (MoE) approach to augment a pre-trained textual large language model (LLM) with a set of specialized weights adapted to the speech modality while maintaining the original LLM frozen during training. This approach allows MoE-TTS to effectively leverage the pre-trained knowledge and text understanding abilities of textual LLMs. Our experimental results indicate that: first, even the most advanced closed-source commercial products can be challenged by carefully designed out-of-domain description test sets; second, MoE-TTS achieves superior performance in generating speech that more accurately reflects the descriptions. We encourage readers to listen to the demos at https://welkinyang.github.io/MoE-TTS/.

</details>

### [EmoSSLSphere: Multilingual Emotional Speech Synthesis with Spherical Vectors and Discrete Speech Tokens](2508.11273.md)
**Joonyong Park, Kenichi Nakamura** · 2025-08-15

<details>
<summary>Abstract</summary>

This paper introduces EmoSSLSphere, a novel framework for multilingual emotional text-to-speech (TTS) synthesis that combines spherical emotion vectors with discrete token features derived from self-supervised learning (SSL). By encoding emotions in a continuous spherical coordinate space and leveraging SSL-based representations for semantic and acoustic modeling, EmoSSLSphere enables fine-grained emotional control, effective cross-lingual emotion transfer, and robust preservation of speaker identity. We evaluate EmoSSLSphere on English and Japanese corpora, demonstrating significant improvements in speech intelligibility, spectral fidelity, prosodic consistency, and overall synthesis quality. Subjective evaluations further confirm that our method outperforms baseline models in terms of naturalness and emotional expressiveness, underscoring its potential as a scalable solution for multilingual emotional TTS.

</details>

### [Benchmarking Prosody Encoding in Discrete Speech Tokens](2508.11224.md)
**Kentaro Onda, Satoru Fukayama, Daisuke Saito, Nobuaki Minematsu** · 2025-08-15

<details>
<summary>Abstract</summary>

Recently, discrete tokens derived from self-supervised learning (SSL) models via k-means clustering have been actively studied as pseudo-text in speech language models and as efficient intermediate representations for various tasks. However, these discrete tokens are typically learned in advance, separately from the training of language models or downstream tasks. As a result, choices related to discretization, such as the SSL model used or the number of clusters, must be made heuristically. In particular, speech language models are expected to understand and generate responses that reflect not only the semantic content but also prosodic features. Yet, there has been limited research on the ability of discrete tokens to capture prosodic information. To address this gap, this study conducts a comprehensive analysis focusing on prosodic encoding based on their sensitivity to the artificially modified prosody, aiming to provide practical guidelines for designing discrete tokens.

</details>

### [Facilitating Personalized TTS for Dysarthric Speakers Using Knowledge Anchoring and Curriculum Learning](2508.10412.md)
**Yejin Jeon, Solee Im, Youngjae Kim, Gary Geunbae Lee** · 2025-08-14

<details>
<summary>Abstract</summary>

Dysarthric speakers experience substantial communication challenges due to impaired motor control of the speech apparatus, which leads to reduced speech intelligibility. This creates significant obstacles in dataset curation since actual recording of long, articulate sentences for the objective of training personalized TTS models becomes infeasible. Thus, the limited availability of audio data, in addition to the articulation errors that are present within the audio, complicates personalized speech synthesis for target dysarthric speaker adaptation. To address this, we frame the issue as a domain transfer task and introduce a knowledge anchoring framework that leverages a teacher-student model, enhanced by curriculum learning through audio augmentation. Experimental results show that the proposed zero-shot multi-speaker TTS model effectively generates synthetic speech with markedly reduced articulation errors and high speaker fidelity, while maintaining prosodic naturalness.

</details>

### [Fake Speech Wild: Detecting Deepfake Speech on Social Media Platform](2508.10559.md)
**Yuankun Xie, Ruibo Fu, Xiaopeng Wang, Zhiyong Wang et al.** · 2025-08-14

<details>
<summary>Abstract</summary>

The rapid advancement of speech generation technology has led to the widespread proliferation of deepfake speech across social media platforms. While deepfake audio countermeasures (CMs) achieve promising results on public datasets, their performance degrades significantly in cross-domain scenarios. To advance CMs for real-world deepfake detection, we first propose the Fake Speech Wild (FSW) dataset, which includes 254 hours of real and deepfake audio from four different media platforms, focusing on social media. As CMs, we establish a benchmark using public datasets and advanced selfsupervised learning (SSL)-based CMs to evaluate current CMs in real-world scenarios. We also assess the effectiveness of data augmentation strategies in enhancing CM robustness for detecting deepfake speech on social media. Finally, by augmenting public datasets and incorporating the FSW training set, we significantly advanced real-world deepfake audio detection performance, achieving an average equal error rate (EER) of 3.54% across all evaluation sets.

</details>

### [$\text{M}^3\text{PDB}$ : A Multimodal, Multi-Label, Multilingual Prompt Database for Speech Generation](2508.09702.md)
**Boyu Zhu et.al.** · 2025-08-13

### [DualSpeechLM: Towards Unified Speech Understanding and Generation via Dual Speech Token Modeling with Large Language Models](2508.08961.md)
**Yuanyuan Wang et.al.** · 2025-08-13

### [UtterTune: LoRA-Based Target-Language Pronunciation Edit and Control in Multilingual Text-to-Speech](2508.09767.md)
**Shuhei Kato** · 2025-08-13

<details>
<summary>Abstract</summary>

We propose UtterTune, a lightweight adaptation method that fine-tunes a multilingual text-to-speech (TTS) system based on a large language model (LLM) architecture, designed to enhance the controllability of pronunciation in a target language while preserving performance in others. While LLM architectures have enabled TTS models to achieve remarkable naturalness, accurately modeling grapheme-to-phoneme (G2P) mapping and prosody remains challenging, especially when the model omits an explicit G2P module and directly processes minimally encoded text (e.g., byte-pair encoding). UtterTune leverages low-rank adaptation to enable the control of segmental pronunciation and pitch accent at the phoneme level for Japanese speech, the target language in this paper, while maintaining naturalness and speaker similarity in a zero-shot setting. Objective and subjective evaluations confirm its effectiveness.

</details>

### [Perturbed Public Voices (P$^{2}$V): A Dataset for Robust Audio Deepfake Detection](2508.10949.md)
**Chongyang Gao, Marco Postiglione, Isabel Gortner, Sarit Kraus et al.** · 2025-08-13

<details>
<summary>Abstract</summary>

Current audio deepfake detectors cannot be trusted. While they excel on controlled benchmarks, they fail when tested in the real world. We introduce Perturbed Public Voices (P$^{2}$V), an IRB-approved dataset capturing three critical aspects of malicious deepfakes: (1) identity-consistent transcripts via LLMs, (2) environmental and adversarial noise, and (3) state-of-the-art voice cloning (2020-2025). Experiments reveal alarming vulnerabilities of 22 recent audio deepfake detectors: models trained on current datasets lose 43% performance when tested on P$^{2}$V, with performance measured as the mean of F1 score on deepfake audio, AUC, and 1-EER. Simple adversarial perturbations induce up to 16% performance degradation, while advanced cloning techniques reduce detectability by 20-30%. In contrast, P$^{2}$V-trained models maintain robustness against these attacks while generalizing to existing datasets, establishing a new benchmark for robust audio deepfake detection. P$^{2}$V will be publicly released upon acceptance by a conference/journal.

</details>

### [QAMRO: Quality-aware Adaptive Margin Ranking Optimization for Human-aligned Assessment of Audio Generation Systems](2508.08957.md)
**Chien-Chun Wang, Kuan-Tang Huang, Cheng-Yeh Yang, Hung-Shin Lee et al.** · 2025-08-12

<details>
<summary>Abstract</summary>

Evaluating audio generation systems, including text-to-music (TTM), text-to-speech (TTS), and text-to-audio (TTA), remains challenging due to the subjective and multi-dimensional nature of human perception. Existing methods treat mean opinion score (MOS) prediction as a regression problem, but standard regression losses overlook the relativity of perceptual judgments. To address this limitation, we introduce QAMRO, a novel Quality-aware Adaptive Margin Ranking Optimization framework that seamlessly integrates regression objectives from different perspectives, aiming to highlight perceptual differences and prioritize accurate ratings. Our framework leverages pre-trained audio-text models such as CLAP and Audiobox-Aesthetics, and is trained exclusively on the official AudioMOS Challenge 2025 dataset. It demonstrates superior alignment with human evaluations across all dimensions, significantly outperforming robust baseline models.

</details>

### [Fine-grained Video Dubbing Duration Alignment with Segment Supervised Preference Optimization](2508.08550.md)
**Chaoqun Cui, Liangbin Huang, Shijing Wang, Zhe Tong et al.** · 2025-08-12

<details>
<summary>Abstract</summary>

Video dubbing aims to translate original speech in visual media programs from the source language to the target language, relying on neural machine translation and text-to-speech technologies. Due to varying information densities across languages, target speech often mismatches the source speech duration, causing audio-video synchronization issues that significantly impact viewer experience. In this study, we approach duration alignment in LLM-based video dubbing machine translation as a preference optimization problem. We propose the Segment Supervised Preference Optimization (SSPO) method, which employs a segment-wise sampling strategy and fine-grained loss to mitigate duration mismatches between source and target lines. Experimental results demonstrate that SSPO achieves superior performance in duration alignment tasks.

</details>

### [Fake-Mamba: Real-Time Speech Deepfake Detection Using Bidirectional Mamba as Self-Attention's Alternative](2508.09294.md)
**Xi Xuan, Zimo Zhu, Wenxin Zhang, Yi-Cheng Lin et al.** · 2025-08-12

<details>
<summary>Abstract</summary>

Advances in speech synthesis intensify security threats, motivating real-time deepfake detection research. We investigate whether bidirectional Mamba can serve as a competitive alternative to Self-Attention in detecting synthetic speech. Our solution, Fake-Mamba, integrates an XLSR front-end with bidirectional Mamba to capture both local and global artifacts. Our core innovation introduces three efficient encoders: TransBiMamba, ConBiMamba, and PN-BiMamba. Leveraging XLSR's rich linguistic representations, PN-BiMamba can effectively capture the subtle cues of synthetic speech. Evaluated on ASVspoof 21 LA, 21 DF, and In-The-Wild benchmarks, Fake-Mamba achieves 0.97%, 1.74%, and 5.85% EER, respectively, representing substantial relative gains over SOTA models XLSR-Conformer and XLSR-Mamba. The framework maintains real-time inference across utterance lengths, demonstrating strong generalization and practical viability. The code is available at https://github.com/xuanxixi/Fake-Mamba.

</details>

### [Is GAN Necessary for Mel-Spectrogram-based Neural Vocoder?](2508.07711.md)
**Hui-Peng Du et.al.** · 2025-08-11

### [Exploring Disentangled Neural Speech Codecs from Self-Supervised Representations](2508.08399.md)
**Ryo Aihara, Yoshiki Masuyama, Gordon Wichern, François G. Germain et al.** · 2025-08-11

<details>
<summary>Abstract</summary>

Neural audio codecs (NACs), which use neural networks to generate compact audio representations, have garnered interest for their applicability to many downstream tasks -- especially quantized codecs due to their compatibility with large language models. However, unlike text, speech conveys not only linguistic content but also rich paralinguistic features. Encoding these elements in an entangled fashion may be suboptimal, as it limits flexibility. For instance, voice conversion (VC) aims to convert speaker characteristics while preserving the original linguistic content, which requires a disentangled representation. Inspired by VC methods utilizing $k$-means quantization with self-supervised features to disentangle phonetic information, we develop a discrete NAC capable of structured disentanglement. Experimental evaluations show that our approach achieves reconstruction performance on par with conventional NACs that do not explicitly perform disentanglement, while also matching the effectiveness of conventional VC techniques.

</details>

### [Think Before You Talk: Enhancing Meaningful Dialogue Generation in Full-Duplex Speech Language Models with Planning-Inspired Text Guidance](2508.07375.md)
**Wenqian Cui et.al.** · 2025-08-10

### [KLASSify to Verify: Audio-Visual Deepfake Detection Using SSL-based Audio and Handcrafted Visual Features](2508.07337.md)
**Ivan Kukanov, Jun Wah Ng** · 2025-08-10

<details>
<summary>Abstract</summary>

The rapid development of audio-driven talking head generators and advanced Text-To-Speech (TTS) models has led to more sophisticated temporal deepfakes. These advances highlight the need for robust methods capable of detecting and localizing deepfakes, even under novel, unseen attack scenarios. Current state-of-the-art deepfake detectors, while accurate, are often computationally expensive and struggle to generalize to novel manipulation techniques. To address these challenges, we propose multimodal approaches for the AV-Deepfake1M 2025 challenge. For the visual modality, we leverage handcrafted features to improve interpretability and adaptability. For the audio modality, we adapt a self-supervised learning (SSL) backbone coupled with graph attention networks to capture rich audio representations, improving detection robustness. Our approach strikes a balance between performance and real-world deployment, focusing on resilience and potential interpretability. On the AV-Deepfake1M++ dataset, our multimodal system achieves AUC of 92.78% for deepfake classification task and IoU of 0.3536 for temporal localization using only the audio modality.

</details>

### [XEmoRAG: Cross-Lingual Emotion Transfer with Controllable Intensity Using Retrieval-Augmented Generation](2508.07302.md)
**Tianlun Zuo, Jingbin Hu, Yuke Li, Xinfa Zhu et al.** · 2025-08-10

<details>
<summary>Abstract</summary>

Zero-shot emotion transfer in cross-lingual speech synthesis refers to generating speech in a target language, where the emotion is expressed based on reference speech from a different source language. However, this task remains challenging due to the scarcity of parallel multilingual emotional corpora, the presence of foreign accent artifacts, and the difficulty of separating emotion from language-specific prosodic features. In this paper, we propose XEmoRAG, a novel framework to enable zero-shot emotion transfer from Chinese to Thai using a large language model (LLM)-based model, without relying on parallel emotional data. XEmoRAG extracts language-agnostic emotional embeddings from Chinese speech and retrieves emotionally matched Thai utterances from a curated emotional database, enabling controllable emotion transfer without explicit emotion labels. Additionally, a flow-matching alignment module minimizes pitch and duration mismatches, ensuring natural prosody. It also blends Chinese timbre into the Thai synthesis, enhancing rhythmic accuracy and emotional expression, while preserving speaker characteristics and emotional consistency. Experimental results show that XEmoRAG synthesizes expressive and natural Thai speech using only Chinese reference audio, without requiring explicit emotion labels. These results highlight XEmoRAG's capability to achieve flexible and low-resource emotional transfer across languages. Our demo is available at https://tlzuo-lesley.github.io/Demo-page/ .

</details>

### [Scalable Controllable Accented TTS](2508.07426.md)
**Henry Li Xinyuan, Zexin Cai, Ashi Garg, Kevin Duh et al.** · 2025-08-10

<details>
<summary>Abstract</summary>

We tackle the challenge of scaling accented TTS systems, expanding their capabilities to include much larger amounts of training data and a wider variety of accent labels, even for accents that are poorly represented or unlabeled in traditional TTS datasets. To achieve this, we employ two strategies: 1. Accent label discovery via a speech geolocation model, which automatically infers accent labels from raw speech data without relying solely on human annotation; 2. Timbre augmentation through kNN voice conversion to increase data diversity and model robustness. These strategies are validated on CommonVoice, where we fine-tune XTTS-v2 for accented TTS with accent labels discovered or enhanced using geolocation. We demonstrate that the resulting accented TTS model not only outperforms XTTS-v2 fine-tuned on self-reported accent labels in CommonVoice, but also existing accented TTS benchmarks.

</details>

### [Text to Speech System for Meitei Mayek Script](2508.06870.md)
**Gangular Singh Irengbam, Nirvash Singh Wahengbam, Lanthoiba Meitei Khumanthem, Paikhomba Oinam** · 2025-08-09

<details>
<summary>Abstract</summary>

This paper presents the development of a Text-to-Speech (TTS) system for the Manipuri language using the Meitei Mayek script. Leveraging Tacotron 2 and HiFi-GAN, we introduce a neural TTS architecture adapted to support tonal phonology and under-resourced linguistic environments. We develop a phoneme mapping for Meitei Mayek to ARPAbet, curate a single-speaker dataset, and demonstrate intelligible and natural speech synthesis, validated through subjective and objective metrics. This system lays the groundwork for linguistic preservation and technological inclusion of Manipuri.

</details>

### [Maestro-EVC: Controllable Emotional Voice Conversion Guided by References and Explicit Prosody](2508.06890.md)
**Jinsung Yoon, Wooyeol Jeong, Jio Gim, Young-Joo Suh** · 2025-08-09

<details>
<summary>Abstract</summary>

Emotional voice conversion (EVC) aims to modify the emotional style of speech while preserving its linguistic content. In practical EVC, controllability, the ability to independently control speaker identity and emotional style using distinct references, is crucial. However, existing methods often struggle to fully disentangle these attributes and lack the ability to model fine-grained emotional expressions such as temporal dynamics. We propose Maestro-EVC, a controllable EVC framework that enables independent control of content, speaker identity, and emotion by effectively disentangling each attribute from separate references. We further introduce a temporal emotion representation and an explicit prosody modeling with prosody augmentation to robustly capture and transfer the temporal dynamics of the target emotion, even under prosody-mismatched conditions. Experimental results confirm that Maestro-EVC achieves high-quality, controllable, and emotionally expressive speech synthesis.

</details>

### [ScamAgents: How AI Agents Can Simulate Human-Level Scam Calls](2508.06457.md)
**Sanket Badhe** · 2025-08-08

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated impressive fluency and reasoning capabilities, but their potential for misuse has raised growing concern. In this paper, we present ScamAgent, an autonomous multi-turn agent built on top of LLMs, capable of generating highly realistic scam call scripts that simulate real-world fraud scenarios. Unlike prior work focused on single-shot prompt misuse, ScamAgent maintains dialogue memory, adapts dynamically to simulated user responses, and employs deceptive persuasion strategies across conversational turns. We show that current LLM safety guardrails, including refusal mechanisms and content filters, are ineffective against such agent-based threats. Even models with strong prompt-level safeguards can be bypassed when prompts are decomposed, disguised, or delivered incrementally within an agent framework. We further demonstrate the transformation of scam scripts into lifelike voice calls using modern text-to-speech systems, completing a fully automated scam pipeline. Our findings highlight an urgent need for multi-turn safety auditing, agent-level control frameworks, and new methods to detect and disrupt conversational deception powered by generative AI.

</details>

### [Large Language Model Data Generation for Enhanced Intent Recognition in German Speech](2508.06277.md)
**Theresa Pekarek Rosin, Burak Can Kaplan, Stefan Wermter** · 2025-08-08

<details>
<summary>Abstract</summary>

Intent recognition (IR) for speech commands is essential for artificial intelligence (AI) assistant systems; however, most existing approaches are limited to short commands and are predominantly developed for English. This paper addresses these limitations by focusing on IR from speech by elderly German speakers. We propose a novel approach that combines an adapted Whisper ASR model, fine-tuned on elderly German speech (SVC-de), with Transformer-based language models trained on synthetic text datasets generated by three well-known large language models (LLMs): LeoLM, Llama3, and ChatGPT. To evaluate the robustness of our approach, we generate synthetic speech with a text-to-speech model and conduct extensive cross-dataset testing. Our results show that synthetic LLM-generated data significantly boosts classification performance and robustness to different speaking styles and unseen vocabulary. Notably, we find that LeoLM, a smaller, domain-specific 13B LLM, surpasses the much larger ChatGPT (175B) in dataset quality for German intent recognition. Our approach demonstrates that generative AI can effectively bridge data gaps in low-resource domains. We provide detailed documentation of our data generation and training process to ensure transparency and reproducibility.

</details>

### [Llasa+: Free Lunch for Accelerated and Streaming Llama-Based Speech Synthesis](2508.06262.md)
**Wenjie Tian, Xinfa Zhu, Hanke Xie, Zhen Ye et al.** · 2025-08-08

<details>
<summary>Abstract</summary>

Recent progress in text-to-speech (TTS) has achieved impressive naturalness and flexibility, especially with the development of large language model (LLM)-based approaches. However, existing autoregressive (AR) structures and large-scale models, such as Llasa, still face significant challenges in inference latency and streaming synthesis. To deal with the limitations, we introduce Llasa+, an accelerated and streaming TTS model built on Llasa. Specifically, to accelerate the generation process, we introduce two plug-and-play Multi-Token Prediction (MTP) modules following the frozen backbone. These modules allow the model to predict multiple tokens in one AR step. Additionally, to mitigate potential error propagation caused by inaccurate MTP, we design a novel verification algorithm that leverages the frozen backbone to validate the generated tokens, thus allowing Llasa+ to achieve speedup without sacrificing generation quality. Furthermore, we design a causal decoder that enables streaming speech reconstruction from tokens. Extensive experiments show that Llasa+ achieves a 1.48X speedup without sacrificing generation quality, despite being trained only on LibriTTS. Moreover, the MTP-and-verification framework can be applied to accelerate any LLM-based model. All codes and models are publicly available at https://github.com/ASLP-lab/LLaSA_Plus.

</details>

### [DAFMSVC: One-Shot Singing Voice Conversion with Dual Attention Mechanism and Flow Matching](2508.05978.md)
**Wei Chen, Binzhu Sha, Dan Luo, Jing Yang et al.** · 2025-08-08

<details>
<summary>Abstract</summary>

Singing Voice Conversion (SVC) transfers a source singer's timbre to a target while keeping melody and lyrics. The key challenge in any-to-any SVC is adapting unseen speaker timbres to source audio without quality degradation. Existing methods either face timbre leakage or fail to achieve satisfactory timbre similarity and quality in the generated audio. To address these challenges, we propose DAFMSVC, where the self-supervised learning (SSL) features from the source audio are replaced with the most similar SSL features from the target audio to prevent timbre leakage. It also incorporates a dual cross-attention mechanism for the adaptive fusion of speaker embeddings, melody, and linguistic content. Additionally, we introduce a flow matching module for high quality audio generation from the fused features. Experimental results show that DAFMSVC significantly enhances timbre similarity and naturalness, outperforming state-of-the-art methods in both subjective and objective evaluations.

</details>

### [Fairness in Dysarthric Speech Synthesis: Understanding Intrinsic Bias in Dysarthric Speech Cloning using F5-TTS](2508.05102.md)
**M Anuprabha, Krishna Gurugubelli, Anil Kumar Vuppala** · 2025-08-07

<details>
<summary>Abstract</summary>

Dysarthric speech poses significant challenges in developing assistive technologies, primarily due to the limited availability of data. Recent advances in neural speech synthesis, especially zero-shot voice cloning, facilitate synthetic speech generation for data augmentation; however, they may introduce biases towards dysarthric speech. In this paper, we investigate the effectiveness of state-of-the-art F5-TTS in cloning dysarthric speech using TORGO dataset, focusing on intelligibility, speaker similarity, and prosody preservation. We also analyze potential biases using fairness metrics like Disparate Impact and Parity Difference to assess disparities across dysarthric severity levels. Results show that F5-TTS exhibits a strong bias toward speech intelligibility over speaker and prosody preservation in dysarthric speech synthesis. Insights from this study can help integrate fairness-aware dysarthric speech synthesis, fostering the advancement of more inclusive speech technologies.

</details>

### [REF-VC: Robust, Expressive and Fast Zero-Shot Voice Conversion with Diffusion Transformers](2508.04996.md)
**Yuepeng Jiang, Ziqian Ning, Shuai Wang, Chengjia Wang et al.** · 2025-08-07

<details>
<summary>Abstract</summary>

In real-world voice conversion applications, environmental noise in source speech and user demands for expressive output pose critical challenges. Traditional ASR-based methods ensure noise robustness but suppress prosody richness, while SSL-based models improve expressiveness but suffer from timbre leakage and noise sensitivity. This paper proposes REF-VC, a noise-robust expressive voice conversion system. Key innovations include: (1) A random erasing strategy to mitigate the information redundancy inherent in SSL features, enhancing noise robustness and expressiveness; (2) Implicit alignment inspired by E2TTS to suppress non-essential feature reconstruction; (3) Integration of Shortcut Models to accelerate flow matching inference, significantly reducing to 4 steps. Experimental results demonstrate that REF-VC outperforms baselines such as Seed-VC in zero-shot scenarios on the noisy set, while also performing comparably to Seed-VC on the clean set. In addition, REF-VC can be compatible with singing voice conversion within one model.

</details>

### [A Scalable Pipeline for Enabling Non-Verbal Speech Generation and Understanding](2508.05385.md)
**Runchuan Ye, Yixuan Zhou, Renjie Yu, Zijian Lin et al.** · 2025-08-07

<details>
<summary>Abstract</summary>

Non-verbal Vocalizations (NVs), such as laughter and sighs, are vital for conveying emotion and intention in human speech, yet most existing speech systems neglect them, which severely compromises communicative richness and emotional intelligence. Existing methods for NVs acquisition are either costly and unscalable (relying on manual annotation/recording) or unnatural (relying on rule-based synthesis). To address these limitations, we propose a highly scalable automatic annotation framework to label non-verbal phenomena from natural speech, which is low-cost, easily extendable, and inherently diverse and natural. This framework leverages a unified detection model to accurately identify NVs in natural speech and integrates them with transcripts via temporal-semantic alignment method. Using this framework, we created and released \textbf{NonVerbalSpeech-38K}, a diverse, real-world dataset featuring 38,718 samples across 10 NV categories collected from in-the-wild media. Experimental results demonstrate that our dataset provides superior controllability for NVs generation and achieves comparable performance for NVs understanding.

</details>

### [Parallel GPT: Harmonizing the Independence and Interdependence of Acoustic and Semantic Information for Zero-Shot Text-to-Speech](2508.04141.md)
**Jingyuan Xing et.al.** · 2025-08-06

### [EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering](2508.03543.md)
**Tianxin Xie et.al.** · 2025-08-06

### [Toward Scalable Patient Safety Training: A Prototype for Root Cause Analysis Simulation With AI Virtual Avatars](2508.04904.md)
**Yuqi Hu, Qiwen Xiong, Zhenzhen Qin, Brandon Watanabe et al.** · 2025-08-06

<details>
<summary>Abstract</summary>

Patient safety training is essential for preparing healthcare professionals to identify, investigate, and prevent adverse events. However, conventional simulation-based approaches often require substantial faculty time, physical resources, and standardized facilitation. This paper presents a prototype AI-powered simulation platform designed to support more scalable patient safety training through root cause analysis (RCA). The system provides a Unity-based 3D simulation environment, which allows trainees to investigate an ICU adverse event by interviewing five virtual team members represented as AI-powered avatars. Each avatar is driven by a large language model (LLM) agent with role-specific knowledge and variable states of mind. Moreover, emotional text-to-speech and AI-supported facial and body animation enable more realistic and immersive interactions. After completing the simulation, trainees submit a written RCA report and receive rubric-guided formative and summative feedback automatically generated by an LLM-based assessment component. The prototype is built to support patient safety training for healthcare professionals, focusing on skills in communication, investigation, thinking, and analysis, with low recurring instructional burden. We describe the design of the platform, its core technical components, and an RCA case based on a published ICU scenario. This work demonstrates the feasibility of integrating generative AI into immersive simulation for scalable patient safety education.

</details>

### [UniTalker: Conversational Speech-Visual Synthesis](2508.04585.md)
**Yifan Hu, Rui Liu, Yi Ren, Xiang Yin et al.** · 2025-08-06

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis (CSS) is a key task in the user-agent interaction area, aiming to generate more expressive and empathetic speech for users. However, it is well-known that "listening" and "eye contact" play crucial roles in conveying emotions during real-world interpersonal communication. Existing CSS research is limited to perceiving only text and speech within the dialogue context, which restricts its effectiveness. Moreover, speech-only responses further constrain the interactive experience. To address these limitations, we introduce a Conversational Speech-Visual Synthesis (CSVS) task as an extension of traditional CSS. By leveraging multimodal dialogue context, it provides users with coherent audiovisual responses. To this end, we develop a CSVS system named UniTalker, which is a unified model that seamlessly integrates multimodal perception and multimodal rendering capabilities. Specifically, it leverages a large-scale language model to comprehensively understand multimodal cues in the dialogue context, including speaker, text, speech, and the talking-face animations. After that, it employs multi-task sequence prediction to first infer the target utterance's emotion and then generate empathetic speech and natural talking-face animations. To ensure that the generated speech-visual content remains consistent in terms of emotion, content, and duration, we introduce three key optimizations: 1) Designing a specialized neural landmark codec to tokenize and reconstruct facial expression sequences. 2) Proposing a bimodal speech-visual hard alignment decoding strategy. 3) Applying emotion-guided rendering during the generation stage. Comprehensive objective and subjective experiments demonstrate that our model synthesizes more empathetic speech and provides users with more natural and emotionally consistent talking-face animations.

</details>

### [Multilingual Source Tracing of Speech Deepfakes: A First Benchmark](2508.04143.md)
**Xi Xuan, Yang Xiao, Rohan Kumar Das, Tomi Kinnunen** · 2025-08-06

<details>
<summary>Abstract</summary>

Recent progress in generative AI has made it increasingly easy to create natural-sounding deepfake speech from just a few seconds of audio. While these tools support helpful applications, they also raise serious concerns by making it possible to generate convincing fake speech in many languages. Current research has largely focused on detecting fake speech, but little attention has been given to tracing the source models used to generate it. This paper introduces the first benchmark for multilingual speech deepfake source tracing, covering both mono- and cross-lingual scenarios. We comparatively investigate DSP- and SSL-based modeling; examine how SSL representations fine-tuned on different languages impact cross-lingual generalization performance; and evaluate generalization to unseen languages and speakers. Our findings offer the first comprehensive insights into the challenges of identifying speech generation models when training and inference languages differ. The dataset, protocol and code are available at https://github.com/xuanxixi/Multilingual-Source-Tracing.

</details>

### [Toward Low-Latency End-to-End Voice Agents for Telecommunications Using Streaming ASR, Quantized LLMs, and Real-Time TTS](2508.04721.md)
**Vignesh Ethiraj et.al.** · 2025-08-05

### [MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction](2508.03166.md)
**Mohammed Salah Al-Radhi et.al.** · 2025-08-05

### [Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback](2508.03123.md)
**Jingyi Chen et.al.** · 2025-08-05

### [MahaTTS: A Unified Framework for Multilingual Text-to-Speech Synthesis](2508.14049.md)
**Jaskaran Singh, Amartya Roy Chowdhury, Raghav Prabhakar, Varshul C. W** · 2025-08-05

<details>
<summary>Abstract</summary>

Current Text-to-Speech models pose a multilingual challenge, where most of the models traditionally focus on English and European languages, thereby hurting the potential to provide access to information to many more people. To address this gap, we introduce MahaTTS-v2 a Multilingual Multi-speaker Text-To-Speech (TTS) system that has excellent multilingual expressive capabilities in Indic languages. The model has been trained on around 20K hours of data specifically focused on Indian languages. Our approach leverages Wav2Vec2.0 tokens for semantic extraction, and a Language Model (LM) for text-to-semantic modeling. Additionally, we have used a Conditional Flow Model (CFM) for semantics to melspectogram generation. The experimental results indicate the effectiveness of the proposed approach over other frameworks. Our code is available at https://github.com/dubverse-ai/MahaTTSv2

</details>

### [SecoustiCodec: Cross-Modal Aligned Streaming Single-Codecbook Speech Codec](2508.02849.md)
**Chunyu Qiang, Haoyu Wang, Cheng Gong, Tianrui Wang et al.** · 2025-08-04

<details>
<summary>Abstract</summary>

Speech codecs serve as a crucial bridge in unifying speech and text language models. Existing codec methods face several challenges in semantic encoding, such as residual paralinguistic information (e.g., timbre, emotion), insufficient semantic completeness, limited reconstruction capability, and lack of support for streaming. To address these challenges, we propose SecoustiCodec, a cross-modal aligned low-bitrate streaming speech codec that disentangles semantic and paralinguistic information in a single-codebook space. To ensure semantic completeness and reconstruction fidelity, paralinguistic encoding is introduced to bridge the information gap between semantic and acoustic encoding. A semantic-only efficient quantization method based on VAE (Variational Autoencoder) and FSQ (Finite Scalar Quantization) is proposed. This approach alleviates the long-tail distribution problem of tokens while maintaining high codebook utilization. A semantic disentanglement method based on contrastive learning is proposed, which aligns text and speech in a joint multimodal frame-level space, effectively removing paralinguistic information from semantic encoding. An acoustic-constrained multi-stage optimization strategy is proposed to ensure robust and stable convergence. Figure~\ref{fig:pesq_kbps_below_2kbps} shows SecoustiCodec achieves SOTA (state-of-the-art) reconstruction quality (PESQ) of 1.77/2.58 at 0.27/1 kbps. The code and model weights for SecoustiCodec will be open-sourced upon the completion of the peer-review process. We've open-sourced SecoustiCodec's demo, code, and model weights.

</details>

### [SpeechRole: A Large-Scale Dataset and Benchmark for Evaluating Speech Role-Playing Agents](2508.02013.md)
**Changhao Jiang, Jiajun Sun, Yifei Cao, Jiabao Zhuang et al.** · 2025-08-04

<details>
<summary>Abstract</summary>

Speech is essential for realistic role-playing, yet existing work on role-playing agents largely centers on text, leaving Speech Role-Playing Agents (SRPAs) underexplored and without systematic evaluation. We introduce SpeechRole, a unified framework for developing and assessing SRPAs. SpeechRole-Data contains 98 roles and 111k speech-to-speech conversations with rich timbre and prosodic variation, providing large-scale resources for training SRPAs. SpeechRole-Eval offers a multidimensional benchmark that directly evaluates generated speech, preserving paralinguistic cues and measuring interaction ability, speech expressiveness, and role-playing fidelity. Experiments show that end-to-end SRPAs such as GPT-4o Audio achieve strong fluency and naturalness, but remain limited in prosody consistency and emotion appropriateness. In contrast, current open-source end-to-end models exhibit substantial performance gaps across multiple evaluation dimensions. Cascaded and end-to-end systems achieve comparable results in interaction ability and role-playing fidelity, suggesting that these aspects are still largely influenced by the underlying text-based language models. We release all data, code, and evaluation tools at https://github.com/yuhui1038/SpeechRole.

</details>

### [Marco-Voice Technical Report](2508.02038.md)
**Fengping Tian, Chenyang Lyu, Xuanfan Ni, Haoqin Sun et al.** · 2025-08-04

<details>
<summary>Abstract</summary>

This paper presents a multifunctional speech synthesis system that integrates voice cloning and emotion control speech synthesis within a unified framework. The goal of this work is to address longstanding challenges in achieving highly expressive, controllable, and natural speech generation that faithfully preserves speaker identity across diverse linguistic and emotional contexts. Our approach introduces an effective speaker-emotion disentanglement mechanism with in-batch contrastive learning, enabling independent manipulation of speaker identity and eemotional style, as well as rotational emotional embedding integration method for smooth emotion control. To support comprehensive training and evaluation, we construct CSEMOTIONS, a high-quality emotional speech dataset containing 10 hours of Mandarin speech from six professional speakers across seven emotional categories. Extensive experiments demonstrate that our system, Marco-Voice, achieves substantial improvements in both objective and subjective metrics. Comprehensive evaluations and analysis were conducted, results show that MarcoVoice delivers competitive performance in terms of speech clarity and emotional richness, representing a substantial advance in the field of expressive neural speech synthesis. Our code and dataset are publicly available at https://github.com/AIDC-AI/Marco-Voice and https://huggingface.co/datasets/AIDC-AI/CSEMOTIONS respectively.

</details>

### [Enhancing Spectrogram Realism in Singing Voice Synthesis via Explicit Bandwidth Extension Prior to Vocoder](2508.01796.md)
**Runxuan Yang et.al.** · 2025-08-03

### [Advancing Speech Quality Assessment Through Scientific Challenges and Open-source Activities](2508.00317.md)
**Wen-Chin Huang** · 2025-08-01

<details>
<summary>Abstract</summary>

Speech quality assessment (SQA) refers to the evaluation of speech quality, and developing an accurate automatic SQA method that reflects human perception has become increasingly important, in order to keep up with the generative AI boom. In recent years, SQA has progressed to a point that researchers started to faithfully use automatic SQA in research papers as a rigorous measurement of goodness for speech generation systems. We believe that the scientific challenges and open-source activities of late have stimulated the growth in this field. In this paper, we review recent challenges as well as open-source implementations and toolkits for SQA, and highlight the importance of maintaining such activities to facilitate the development of not only SQA itself but also generative AI for speech.

</details>

### [Next Tokens Denoising for Speech Synthesis](2507.22746.md)
**Yanqing Liu, Ruiqing Xue, Chong Zhang, Yufei Liu et al.** · 2025-07-30

<details>
<summary>Abstract</summary>

While diffusion and autoregressive (AR) models have significantly advanced generative modeling, they each present distinct limitations. AR models, which rely on causal attention, cannot exploit future context and suffer from slow generation speeds. Conversely, diffusion models struggle with key-value (KV) caching. To overcome these challenges, we introduce Dragon-FM, a novel text-to-speech (TTS) design that unifies AR and flow-matching. This model processes 48 kHz audio codec tokens in chunks at a compact rate of 12.5 tokens per second. This design enables AR modeling across chunks, ensuring global coherence, while parallel flow-matching within chunks facilitates fast iterative denoising. Thus, the model leverages KV-cache across chunks and utilizes bidirectional context within each chunk. Furthermore, it bridges continuous and discrete feature modeling, demonstrating that continuous AR flow-matching can predict discrete tokens with finite scalar quantizers. This efficient codec and fast chunk-autoregressive architecture also make the model highly effective for generating long-form content, such as podcasts. Experiments on podcast datasets demonstrate its capability to efficiently generate high-quality zero-shot podcasts.

</details>

### [Adaptive Duration Model for Text Speech Alignment](2507.22612.md)
**Junjie Cao** · 2025-07-30

<details>
<summary>Abstract</summary>

Speech-to-text alignment is a critical component of neural text to speech (TTS) models. Autoregressive TTS models typically use an attention mechanism to learn these alignments on-line, while non-autoregressive end to end TTS models rely on durations extracted from external sources. In this paper, we propose a novel duration prediction framework that can give promising phoneme-level duration distribution with given text. In our experiments, the proposed duration model has more precise prediction and adaptation ability to conditions, compared to previous baseline models. Specifically, it makes a considerable improvement on phoneme-level alignment accuracy and makes the performance of zero-shot TTS models more robust to the mismatch between prompt audio and input audio.

</details>

### [JWB-DH-V1: Benchmark for Joint Whole-Body Talking Avatar and Speech Generation Version 1](2507.20987.md)
**Xinhan Di et.al.** · 2025-07-29

### [SpeechFake: A Large-Scale Multilingual Speech Deepfake Dataset Incorporating Cutting-Edge Generation Methods](2507.21463.md)
**Wen Huang, Yanmei Gu, Zhiming Wang, Huijia Zhu et al.** · 2025-07-29

<details>
<summary>Abstract</summary>

As speech generation technology advances, the risk of misuse through deepfake audio has become a pressing concern, which underscores the critical need for robust detection systems. However, many existing speech deepfake datasets are limited in scale and diversity, making it challenging to train models that can generalize well to unseen deepfakes. To address these gaps, we introduce SpeechFake, a large-scale dataset designed specifically for speech deepfake detection. SpeechFake includes over 3 million deepfake samples, totaling more than 3,000 hours of audio, generated using 40 different speech synthesis tools. The dataset encompasses a wide range of generation techniques, including text-to-speech, voice conversion, and neural vocoder, incorporating the latest cutting-edge methods. It also provides multilingual support, spanning 46 languages. In this paper, we offer a detailed overview of the dataset's creation, composition, and statistics. We also present baseline results by training detection models on SpeechFake, demonstrating strong performance on both its own test sets and various unseen test sets. Additionally, we conduct experiments to rigorously explore how generation methods, language diversity, and speaker variation affect detection performance. We believe SpeechFake will be a valuable resource for advancing speech deepfake detection and developing more robust models for evolving generation techniques.

</details>

### [Intent Aware Context Retrieval for Multi-Turn Agricultural Question Answering](2508.03719.md)
**Abhay Vijayvargia, Ajay Nagpal, Kundeshwar Pundalik, Atharva Savarkar et al.** · 2025-07-28

<details>
<summary>Abstract</summary>

Indian farmers often lack timely, accessible, and language-friendly agricultural advice, especially in rural areas with low literacy. To address this gap in accessibility, this paper presents a novel AI-powered agricultural chatbot, Krishi Sathi, designed to support Indian farmers by providing personalized, easy-to-understand answers to their queries through both text and speech. The system's intelligence stems from an IFT model, subsequently refined through fine-tuning on Indian agricultural knowledge across three curated datasets. Unlike traditional chatbots that respond to one-off questions, Krishi Sathi follows a structured, multi-turn conversation flow to gradually collect the necessary details from the farmer, ensuring the query is fully understood before generating a response. Once the intent and context are extracted, the system performs Retrieval-Augmented Generation (RAG) by first fetching information from a curated agricultural database and then generating a tailored response using the IFT model. The chatbot supports both English and Hindi languages, with speech input and output features (via ASR and TTS) to make it accessible for users with low literacy or limited digital skills. This work demonstrates how combining intent-driven dialogue flows, instruction-tuned models, and retrieval-based generation can improve the quality and accessibility of digital agricultural support in India. This approach yielded strong results, with the system achieving a query response accuracy of 97.53%, 91.35% contextual relevance and personalization, and a query completion rate of 97.53%. The average response time remained under 6 seconds, ensuring timely support for users across both English and Hindi interactions.

</details>

### [AV-Deepfake1M++: A Large-Scale Audio-Visual Deepfake Benchmark with Real-World Perturbations](2507.20579.md)
**Zhixi Cai, Kartik Kuckreja, Shreya Ghosh, Akanksha Chuchra et al.** · 2025-07-28

<details>
<summary>Abstract</summary>

The rapid surge of text-to-speech and face-voice reenactment models makes video fabrication easier and highly realistic. To encounter this problem, we require datasets that rich in type of generation methods and perturbation strategy which is usually common for online videos. To this end, we propose AV-Deepfake1M++, an extension of the AV-Deepfake1M having 2 million video clips with diversified manipulation strategy and audio-visual perturbation. This paper includes the description of data generation strategies along with benchmarking of AV-Deepfake1M++ using state-of-the-art methods. We believe that this dataset will play a pivotal role in facilitating research in Deepfake domain. Based on this dataset, we host the 2025 1M-Deepfakes Detection Challenge. The challenge details, dataset and evaluation scripts are available online under a research-only license at https://deepfakes1m.github.io/2025.

</details>

### [Learning Neural Vocoder from Range-Null Space Decomposition](2507.20731.md)
**Andong Li, Tong Lei, Zhihang Sun, Rilin Chen et al.** · 2025-07-28

<details>
<summary>Abstract</summary>

Despite the rapid development of neural vocoders in recent years, they usually suffer from some intrinsic challenges like opaque modeling, and parameter-performance trade-off. In this study, we propose an innovative time-frequency (T-F) domain-based neural vocoder to resolve the above-mentioned challenges. To be specific, we bridge the connection between the classical signal range-null decomposition (RND) theory and vocoder task, and the reconstruction of target spectrogram can be decomposed into the superimposition between the range-space and null-space, where the former is enabled by a linear domain shift from the original mel-scale domain to the target linear-scale domain, and the latter is instantiated via a learnable network for further spectral detail generation. Accordingly, we propose a novel dual-path framework, where the spectrum is hierarchically encoded/decoded, and the cross- and narrow-band modules are elaborately devised for efficient sub-band and sequential modeling. Comprehensive experiments are conducted on the LJSpeech and LibriTTS benchmarks. Quantitative and qualitative results show that while enjoying lightweight network parameters, the proposed approach yields state-of-the-art performance among existing advanced methods. Our code and the pretrained model weights are available at https://github.com/Andong-Li-speech/RNDVoC.

</details>

### [Do Not Mimic My Voice: Speaker Identity Unlearning for Zero-Shot Text-to-Speech](2507.20140.md)
**Taesoo Kim et.al.** · 2025-07-27

### [Seed LiveInterpret 2.0: End-to-end Simultaneous Speech-to-speech Translation with Your Voice](2507.17527.md)
**Shanbo Cheng et.al.** · 2025-07-27

### [What Makes Code Generation Ethically Sourced?](2507.19743.md)
**Zhuolin Xu, Chenglin Li, Qiushi Li, Shin Hwei Tan** · 2025-07-26

<details>
<summary>Abstract</summary>

Several code generation models have been proposed to help reduce time and effort in solving software-related tasks. To ensure responsible AI, there are growing interests over various ethical issues (e.g., unclear licensing, privacy, fairness, and environment impact). These studies have the overarching goal of ensuring ethically sourced generation, which has gained growing attentions in speech synthesis and image generation. In this paper, we introduce the novel notion of Ethically Sourced Code Generation (ES-CodeGen) to refer to managing all processes involved in code generation model development from data collection to post-deployment via ethical and sustainable practices. To build a taxonomy of ES-CodeGen, we perform a two-phase literature review where we read 803 papers across various domains and specific to AI-based code generation. We identified 71 relevant papers with 10 initial dimensions of ES-CodeGen. To refine our dimensions and gain insights on consequences of ES-CodeGen, we surveyed 32 practitioners, which include six developers who submitted GitHub issues to opt-out from the Stack dataset (these impacted users have real-world experience of ethically sourcing issues in code generation models). The results lead to 11 dimensions of ES-CodeGen with a new dimension on code quality as practitioners have noted its importance. We also identified consequences, artifacts, and stages relevant to ES-CodeGen. Our post-survey reflection showed that most practitioners tend to ignore social-related dimensions despite their importance. Most practitioners either agreed or strongly agreed that our survey help improve their understanding of ES-CodeGen. Our study calls for attentions of various ethical issues towards ES-CodeGen.

</details>

### [GOAT-SLM: A Spoken Language Model with Paralinguistic and Speaker Characteristic Awareness](2507.18119.md)
**Hongjie Chen et.al.** · 2025-07-25

### [Synthetic Data Generation for Phrase Break Prediction with Large Language Model](2507.18044.md)
**Hoyeon Lee, Sejung Son, Ye-Eun Kang, Jong-Hwan Kim** · 2025-07-24

<details>
<summary>Abstract</summary>

Current approaches to phrase break prediction address crucial prosodic aspects of text-to-speech systems but heavily rely on vast human annotations from audio or text, incurring significant manual effort and cost. Inherent variability in the speech domain, driven by phonetic factors, further complicates acquiring consistent, high-quality data. Recently, large language models (LLMs) have shown success in addressing data challenges in NLP by generating tailored synthetic data while reducing manual annotation needs. Motivated by this, we explore leveraging LLM to generate synthetic phrase break annotations, addressing the challenges of both manual annotation and speech-related tasks by comparing with traditional annotations and assessing effectiveness across multiple languages. Our findings suggest that LLM-based synthetic data generation effectively mitigates data challenges in phrase break prediction and highlights the potential of LLMs as a viable solution for the speech domain.

</details>

### [TTS-1 Technical Report](2507.21138.md)
**Oleg Atamanenko, Anna Chalova, Joseph Coombes, Nikki Cope et al.** · 2025-07-22

<details>
<summary>Abstract</summary>

We introduce Inworld TTS-1, a set of two Transformer-based autoregressive text-to-speech (TTS) models. Our largest model, TTS-1-Max, has 8.8B parameters and is designed for utmost quality and expressiveness in demanding applications. TTS-1 is our most efficient model, with 1.6B parameters, built for real-time speech synthesis and on-device use cases. By scaling train-time compute and applying a sequential process of pre-training, fine-tuning, and RL-alignment of the speech-language model (SpeechLM) component, both models achieve state-of-the-art performance on a variety of benchmarks, demonstrating exceptional quality relying purely on in-context learning of the speaker's voice. Inworld TTS-1 and TTS-1-Max can generate high-resolution 48 kHz speech with low latency, and support 11 languages with fine-grained emotional control and non-verbal vocalizations through audio markups. We additionally open-source our training and modeling code under an MIT license.

</details>

### [SplitMeanFlow: Interval Splitting Consistency in Few-Step Generative Modeling](2507.16884.md)
**Yi Guo, Wei Wang, Zhihang Yuan, Rong Cao et al.** · 2025-07-22

<details>
<summary>Abstract</summary>

Generative models like Flow Matching have achieved state-of-the-art performance but are often hindered by a computationally expensive iterative sampling process. To address this, recent work has focused on few-step or one-step generation by learning the average velocity field, which directly maps noise to data. MeanFlow, a leading method in this area, learns this field by enforcing a differential identity that connects the average and instantaneous velocities. In this work, we argue that this differential formulation is a limiting special case of a more fundamental principle. We return to the first principles of average velocity and leverage the additivity property of definite integrals. This leads us to derive a novel, purely algebraic identity we term Interval Splitting Consistency. This identity establishes a self-referential relationship for the average velocity field across different time intervals without resorting to any differential operators. Based on this principle, we introduce SplitMeanFlow, a new training framework that enforces this algebraic consistency directly as a learning objective. We formally prove that the differential identity at the core of MeanFlow is recovered by taking the limit of our algebraic consistency as the interval split becomes infinitesimal. This establishes SplitMeanFlow as a direct and more general foundation for learning average velocity fields. From a practical standpoint, our algebraic approach is significantly more efficient, as it eliminates the need for JVP computations, resulting in simpler implementation, more stable training, and broader hardware compatibility. One-step and two-step SplitMeanFlow models have been successfully deployed in large-scale speech synthesis products (such as Doubao), achieving speedups of 20x.

</details>

### [Technical report: Impact of Duration Prediction on Speaker-specific TTS for Indian Languages](2507.16875.md)
**Isha Pandey, Pranav Gaikwad, Amruta Parulekar, Ganesh Ramakrishnan** · 2025-07-22

<details>
<summary>Abstract</summary>

High-quality speech generation for low-resource languages, such as many Indian languages, remains a significant challenge due to limited data and diverse linguistic structures. Duration prediction is a critical component in many speech generation pipelines, playing a key role in modeling prosody and speech rhythm. While some recent generative approaches choose to omit explicit duration modeling, often at the cost of longer training times. We retain and explore this module to better understand its impact in the linguistically rich and data-scarce landscape of India. We train a non-autoregressive Continuous Normalizing Flow (CNF) based speech model using publicly available Indian language data and evaluate multiple duration prediction strategies for zero-shot, speaker-specific generation. Our comparative analysis on speech-infilling tasks reveals nuanced trade-offs: infilling based predictors improve intelligibility in some languages, while speaker-prompted predictors better preserve speaker characteristics in others. These findings inform the design and selection of duration strategies tailored to specific languages and tasks, underscoring the continued value of interpretable components like duration prediction in adapting advanced generative architectures to low-resource, multilingual settings.

</details>

### [A2TTS: TTS for Low Resource Indian Languages](2507.15272.md)
**Ayush Singh Bhadoriya, Abhishek Nikunj Shinde, Isha Pandey, Ganesh Ramakrishnan** · 2025-07-21

<details>
<summary>Abstract</summary>

We present a speaker conditioned text-to-speech (TTS) system aimed at addressing challenges in generating speech for unseen speakers and supporting diverse Indian languages. Our method leverages a diffusion-based TTS architecture, where a speaker encoder extracts embeddings from short reference audio samples to condition the DDPM decoder for multispeaker generation. To further enhance prosody and naturalness, we employ a cross-attention based duration prediction mechanism that utilizes reference audio, enabling more accurate and speaker consistent timing. This results in speech that closely resembles the target speaker while improving duration modeling and overall expressiveness. Additionally, to improve zero-shot generation, we employed classifier free guidance, allowing the system to generate speech more near speech for unknown speakers. Using this approach, we trained language-specific speaker-conditioned models. Using the IndicSUPERB dataset for multiple Indian languages such as Bengali, Gujarati, Hindi, Marathi, Malayalam, Punjabi and Tamil.

</details>

### [DMOSpeech 2: Reinforcement Learning for Duration Prediction in Metric-Optimized Speech Synthesis](2507.14988.md)
**Yinghao Aaron Li et.al.** · 2025-07-20

### [Hear Your Code Fail, Voice-Assisted Debugging for Python](2507.15007.md)
**Sayed Mahbub Hasan Amiri, Md. Mainul Islam, Mohammad Shakhawat Hossen, Sayed Majhab Hasan Amiri et al.** · 2025-07-20

<details>
<summary>Abstract</summary>

This research introduces an innovative voice-assisted debugging plugin for Python that transforms silent runtime errors into actionable audible diagnostics. By implementing a global exception hook architecture with pyttsx3 text-to-speech conversion and Tkinter-based GUI visualization, the solution delivers multimodal error feedback through parallel auditory and visual channels. Empirical evaluation demonstrates 37% reduced cognitive load (p<0.01, n=50) compared to traditional stack-trace debugging, while enabling 78% faster error identification through vocalized exception classification and contextualization. The system achieves sub-1.2 second voice latency with under 18% CPU overhead during exception handling, vocalizing error types and consequences while displaying interactive tracebacks with documentation deep links. Criteria validate compatibility across Python 3.7+ environments on Windows, macOS, and Linux platforms. Needing only two lines of integration code, the plugin significantly boosts availability for aesthetically impaired designers and supports multitasking workflows through hands-free error medical diagnosis. Educational applications show particular promise, with pilot studies indicating 45% faster debugging skill acquisition among novice programmers. Future development will incorporate GPT-based repair suggestions and real-time multilingual translation to further advance auditory debugging paradigms. The solution represents a fundamental shift toward human-centric error diagnostics, bridging critical gaps in programming accessibility while establishing new standards for cognitive efficiency in software development workflows.

</details>

### [FastLongSpeech: Enhancing Large Speech-Language Models for Efficient Long-Speech Processing](2507.14815.md)
**Shoutao Guo, Shaolei Zhang, Qingkai Fang, Zhengrui Ma et al.** · 2025-07-20

<details>
<summary>Abstract</summary>

The rapid advancement of Large Language Models (LLMs) has spurred significant progress in Large Speech-Language Models (LSLMs), enhancing their capabilities in both speech understanding and generation. While existing LSLMs often concentrate on augmenting speech generation or tackling a diverse array of short-speech tasks, the efficient processing of long-form speech remains a critical yet underexplored challenge. This gap is primarily attributed to the scarcity of long-speech training datasets and the high computational costs associated with long sequences. To address these limitations, we introduce FastLongSpeech, a novel framework designed to extend LSLM capabilities for efficient long-speech processing without necessitating dedicated long-speech training data. FastLongSpeech incorporates an iterative fusion strategy that can compress excessively long-speech sequences into manageable lengths. To adapt LSLMs for long-speech inputs, it introduces a dynamic compression training approach, which exposes the model to short-speech sequences at varying compression ratios, thereby transferring the capabilities of LSLMs to long-speech tasks. To assess the long-speech capabilities of LSLMs, we develop a long-speech understanding benchmark called LongSpeech-Eval. Experiments show that our method exhibits strong performance in both long-speech and short-speech tasks, while greatly improving inference efficiency.

</details>

### [Conan: A Chunkwise Online Network for Zero-Shot Adaptive Voice Conversion](2507.14534.md)
**Yu Zhang, Baotong Tian, Zhiyao Duan** · 2025-07-19

<details>
<summary>Abstract</summary>

Zero-shot online voice conversion (VC) holds significant promise for real-time communications and entertainment. However, current VC models struggle to preserve semantic fidelity under real-time constraints, deliver natural-sounding conversions, and adapt effectively to unseen speaker characteristics. To address these challenges, we introduce Conan, a chunkwise online zero-shot voice conversion model that preserves the content of the source while matching the voice timbre and styles of reference speech. Conan comprises three core components: 1) a Stream Content Extractor that leverages Emformer for low-latency streaming content encoding; 2) an Adaptive Style Encoder that extracts fine-grained stylistic features from reference speech for enhanced style adaptation; 3) a Causal Shuffle Vocoder that implements a fully causal HiFiGAN using a pixel-shuffle mechanism. Experimental evaluations demonstrate that Conan outperforms baseline models in subjective and objective metrics. Audio samples can be found at https://aaronz345.github.io/ConanDemo.

</details>

### [A Data-Centric Framework for Addressing Phonetic and Prosodic Challenges in Russian Speech Generative Models](2507.13563.md)
**Kirill Borodin et.al.** · 2025-07-17

### [NonverbalTTS: A Public English Corpus of Text-Aligned Nonverbal Vocalizations with Emotion Annotations for Text-to-Speech](2507.13155.md)
**Maksim Borisov et.al.** · 2025-07-17

### [Intelligent Virtual Sonographer (IVS): Enhancing Physician-Robot-Patient Communication](2507.13052.md)
**Tianyu Song, Feng Li, Yuan Bi, Angelos Karlas et al.** · 2025-07-17

<details>
<summary>Abstract</summary>

The advancement and maturity of large language models (LLMs) and robotics have unlocked vast potential for human-computer interaction, particularly in the field of robotic ultrasound. While existing research primarily focuses on either patient-robot or physician-robot interaction, the role of an intelligent virtual sonographer (IVS) bridging physician-robot-patient communication remains underexplored. This work introduces a conversational virtual agent in Extended Reality (XR) that facilitates real-time interaction between physicians, a robotic ultrasound system(RUS), and patients. The IVS agent communicates with physicians in a professional manner while offering empathetic explanations and reassurance to patients. Furthermore, it actively controls the RUS by executing physician commands and transparently relays these actions to the patient. By integrating LLM-powered dialogue with speech-to-text, text-to-speech, and robotic control, our system enhances the efficiency, clarity, and accessibility of robotic ultrasound acquisition. This work constitutes a first step toward understanding how IVS can bridge communication gaps in physician-robot-patient interaction, providing more control and therefore trust into physician-robot interaction while improving patient experience and acceptance of robotic ultrasound.

</details>

### [Quantize More, Lose Less: Autoregressive Generation from Residually Quantized Speech Representations](2507.12197.md)
**Yichen Han, Xiaoyang Hao, Keming Chen, Weibo Xiong et al.** · 2025-07-16

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) synthesis has seen renewed progress under the discrete modeling paradigm. Existing autoregressive approaches often rely on single-codebook representations, which suffer from significant information loss. Even with post-hoc refinement techniques such as flow matching, these methods fail to recover fine-grained details (e.g., prosodic nuances, speaker-specific timbres), especially in challenging scenarios like singing voice or music synthesis. We propose QTTS, a novel TTS framework built upon our new audio codec, QDAC. The core innovation of QDAC lies in its end-to-end training of an ASR-based auto-regressive network with a GAN, which achieves superior semantic feature disentanglement for scalable, near-lossless compression. QTTS models these discrete codes using two innovative strategies: the Hierarchical Parallel architecture, which uses a dual-AR structure to model inter-codebook dependencies for higher-quality synthesis, and the Delay Multihead approach, which employs parallelized prediction with a fixed delay to accelerate inference speed. Our experiments demonstrate that the proposed framework achieves higher synthesis quality and better preserves expressive content compared to baseline. This suggests that scaling up compression via multi-codebook modeling is a promising direction for high-fidelity, general-purpose speech and audio generation.

</details>

### [EME-TTS: Unlocking the Emphasis and Emotion Link in Speech Synthesis](2507.12015.md)
**Haoxun Li, Leyuan Qu, Jiaxi Hu, Taihao Li** · 2025-07-16

<details>
<summary>Abstract</summary>

In recent years, emotional Text-to-Speech (TTS) synthesis and emphasis-controllable speech synthesis have advanced significantly. However, their interaction remains underexplored. We propose Emphasis Meets Emotion TTS (EME-TTS), a novel framework designed to address two key research questions: (1) how to effectively utilize emphasis to enhance the expressiveness of emotional speech, and (2) how to maintain the perceptual clarity and stability of target emphasis across different emotions. EME-TTS employs weakly supervised learning with emphasis pseudo-labels and variance-based emphasis features. Additionally, the proposed Emphasis Perception Enhancement (EPE) block enhances the interaction between emotional signals and emphasis positions. Experimental results show that EME-TTS, when combined with large language models for emphasis position prediction, enables more natural emotional speech synthesis while preserving stable and distinguishable target emphasis across emotions. Synthesized samples are available on-line.

</details>

### [Evaluating Speech-to-Text x LLM x Text-to-Speech Combinations for AI Interview Systems](2507.16835.md)
**Nima Yazdani et.al.** · 2025-07-15

### [P.808 Multilingual Speech Enhancement Testing: Approach and Results of URGENT 2025 Challenge](2507.11306.md)
**Marvin Sach, Yihui Fu, Kohei Saijo, Wangyou Zhang et al.** · 2025-07-15

<details>
<summary>Abstract</summary>

In speech quality estimation for speech enhancement (SE) systems, subjective listening tests so far are considered as the gold standard. This should be even more true considering the large influx of new generative or hybrid methods into the field, revealing issues of some objective metrics. Efforts such as the Interspeech 2025 URGENT Speech Enhancement Challenge also involving non-English datasets add the aspect of multilinguality to the testing procedure. In this paper, we provide a brief recap of the ITU-T P.808 crowdsourced subjective listening test method. A first novel contribution is our proposed process of localizing both text and audio components of Naderi and Cutler's implementation of crowdsourced subjective absolute category rating (ACR) listening tests involving text-to-speech (TTS). Further, we provide surprising analyses of and insights into URGENT Challenge results, tackling the reliability of (P.808) ACR subjective testing as gold standard in the age of generative AI. Particularly, it seems that for generative SE methods, subjective (ACR MOS) and objective (DNSMOS, NISQA) reference-free metrics should be accompanied by objective phone fidelity metrics to reliably detect hallucinations. Finally, we will soon release our localization scripts and methods for easy deployment for new multilingual speech enhancement subjective evaluations according to ITU-T P.808.

</details>

### [Pronunciation Deviation Analysis Through Voice Cloning and Acoustic Comparison](2507.10985.md)
**Andrew Valdivia, Yueming Zhang, Hailu Xu, Amir Ghasemkhani et al.** · 2025-07-15

<details>
<summary>Abstract</summary>

This paper presents a novel approach for detecting mispronunciations by analyzing deviations between a user's original speech and their voice-cloned counterpart with corrected pronunciation. We hypothesize that regions with maximal acoustic deviation between the original and cloned utterances indicate potential mispronunciations. Our method leverages recent advances in voice cloning to generate a synthetic version of the user's voice with proper pronunciation, then performs frame-by-frame comparisons to identify problematic segments. Experimental results demonstrate the effectiveness of this approach in pinpointing specific pronunciation errors without requiring predefined phonetic rules or extensive training data for each target language.

</details>

### [Fast Inference End-to-End Speech Synthesis with Style Diffusion](s2:b26e9b78deda6f13d36e5728a551191d9ab46b77.md)
**Hui Sun, Jiyeoun Song, Yi Jiang** · 2025-07-15

<details>
<summary>Abstract</summary>

In recent years, deep learning-based end-to-end Text-To-Speech (TTS) models have made significant progress in enhancing speech naturalness and fluency. However, existing Variational Inference Text-to-Speech (VITS) models still face challenges such as insufficient pitch modeling, inadequate contextual dependency capture, and low inference efficiency in the decoder. To address these issues, this paper proposes an improved TTS framework named Q-VITS. Q-VITS incorporates Rotary Position Embedding (RoPE) into the text encoder to enhance long-sequence modeling, adopts a frame-level prior modeling strategy to optimize one-to-many mappings, and designs a style extractor based on a diffusion model for controllable style rendering. Additionally, the proposed decoder ConfoGAN integrates explicit F0 modeling, Pseudo-Quadrature Mirror Filter (PQMF) multi-band synthesis and Conformer structure. The experimental results demonstrate that Q-VITS outperforms the VITS in terms of speech quality, pitch accuracy, and inference efficiency in both subjective Mean Opinion Score (MOS) and objective Mel-Cepstral Distortion (MCD) and Root Mean Square Error (RMSE) evaluations on a single-speaker dataset, achieving performance close to ground-truth audio. These improvements provide an effective solution for efficient and controllable speech synthesis.

</details>

### [An Empirical Evaluation of AI-Powered Non-Player Characters' Perceived Realism and Performance in Virtual Reality Environments](2507.10469.md)
**Mikko Korkiakoski, Saeid Sheikhi, Jesper Nyman, Jussi Saariniemi et al.** · 2025-07-14

<details>
<summary>Abstract</summary>

Advancements in artificial intelligence (AI) have significantly enhanced the realism and interactivity of non-player characters (NPCs) in virtual reality (VR), creating more engaging and believable user experiences. This paper evaluates AI-driven NPCs within a VR interrogation simulator, focusing on their perceived realism, usability, and system performance. The simulator features two AI-powered NPCs, a suspect, and a partner, using GPT-4 Turbo to engage participants in a scenario to determine the suspect's guilt or innocence. A user study with 18 participants assessed the system using the System Usability Scale (SUS), Game Experience Questionnaire (GEQ), and a Virtual Agent Believability Questionnaire, alongside latency measurements for speech-to-text (STT), text-to-speech (TTS), OpenAI GPT-4 Turbo, and overall (cycle) latency. Results showed an average cycle latency of 7 seconds, influenced by the increasing conversational context. Believability scored 6.67 out of 10, with high ratings in behavior, social relationships, and intelligence but moderate scores in emotion and personality. The system achieved a SUS score of 79.44, indicating good usability. These findings demonstrate the potential of large language models to improve NPC realism and interaction in VR while highlighting challenges in reducing system latency and enhancing emotional depth. This research contributes to the development of more sophisticated AI-driven NPCs, revealing the need for performance optimization to achieve increasingly immersive virtual experiences.

</details>

### [DualDub: Video-to-Soundtrack Generation via Joint Speech and Background Audio Synthesis](2507.10109.md)
**Wenjie Tian, Xinfa Zhu, Haohe Liu, Zhixian Zhao et al.** · 2025-07-14

<details>
<summary>Abstract</summary>

While recent video-to-audio (V2A) models can generate realistic background audio from visual input, they largely overlook speech, an essential part of many video soundtracks. This paper proposes a new task, video-to-soundtrack (V2ST) generation, which aims to jointly produce synchronized background audio and speech within a unified framework. To tackle V2ST, we introduce DualDub, a unified framework built on a multimodal language model that integrates a multimodal encoder, a cross-modal aligner, and dual decoding heads for simultaneous background audio and speech generation. Specifically, our proposed cross-modal aligner employs causal and non-causal attention mechanisms to improve synchronization and acoustic harmony. Besides, to handle data scarcity, we design a curriculum learning strategy that progressively builds the multimodal capability. Finally, we introduce DualBench, the first benchmark for V2ST evaluation with a carefully curated test set and comprehensive metrics. Experimental results demonstrate that DualDub achieves state-of-the-art performance, generating high-quality and well-synchronized soundtracks with both speech and background audio.

</details>

### [ZipVoice-Dialog: Non-Autoregressive Spoken Dialogue Generation with Flow Matching](2507.09318.md)
**Han Zhu et.al.** · 2025-07-12

### [Voice Conversion for Lombard Speaking Style with Implicit and Explicit Acoustic Feature Conditioning](2507.09310.md)
**Dominika Woszczyk, Manuel Sam Ribeiro, Thomas Merritt, Daniel Korzekwa** · 2025-07-12

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) systems in Lombard speaking style can improve the overall intelligibility of speech, useful for hearing loss and noisy conditions. However, training those models requires a large amount of data and the Lombard effect is challenging to record due to speaker and noise variability and tiring recording conditions. Voice conversion (VC) has been shown to be a useful augmentation technique to train TTS systems in the absence of recorded data from the target speaker in the target speaking style. In this paper, we are concerned with Lombard speaking style transfer. Our goal is to convert speaker identity while preserving the acoustic attributes that define the Lombard speaking style. We compare voice conversion models with implicit and explicit acoustic feature conditioning. We observe that our proposed implicit conditioning strategy achieves an intelligibility gain comparable to the model conditioned on explicit acoustic features, while also preserving speaker similarity.

</details>

### [ClaritySpeech: Dementia Obfuscation in Speech](2507.09282.md)
**Dominika Woszczyk, Ranya Aloufi, Soteris Demetriou** · 2025-07-12

<details>
<summary>Abstract</summary>

Dementia, a neurodegenerative disease, alters speech patterns, creating communication barriers and raising privacy concerns. Current speech technologies, such as automatic speech transcription (ASR), struggle with dementia and atypical speech, further challenging accessibility. This paper presents a novel dementia obfuscation in speech framework, ClaritySpeech, integrating ASR, text obfuscation, and zero-shot text-to-speech (TTS) to correct dementia-affected speech while preserving speaker identity in low-data environments without fine-tuning. Results show a 16% and 10% drop in mean F1 score across various adversarial settings and modalities (audio, text, fusion) for ADReSS and ADReSSo, respectively, maintaining 50% speaker similarity. We also find that our system improves WER (from 0.73 to 0.08 for ADReSS and 0.15 for ADReSSo) and speech quality from 1.65 to ~2.15, enhancing privacy and accessibility.

</details>

### [MIDI-VALLE: Improving Expressive Piano Performance Synthesis Through Neural Codec Language Modelling](2507.08530.md)
**Jingjing Tang et.al.** · 2025-07-11

### [Exploiting Leaderboards for Large-Scale Distribution of Malicious Models](2507.08983.md)
**Anshuman Suri, Harsh Chaudhari, Yuefeng Peng, Ali Naseh et al.** · 2025-07-11

<details>
<summary>Abstract</summary>

While poisoning attacks on machine learning models have been extensively studied, the mechanisms by which adversaries can distribute poisoned models at scale remain largely unexplored. In this paper, we shed light on how model leaderboards -- ranked platforms for model discovery and evaluation -- can serve as a powerful channel for adversaries for stealthy large-scale distribution of poisoned models. We present TrojanClimb, a general framework that enables injection of malicious behaviors while maintaining competitive leaderboard performance. We demonstrate its effectiveness across four diverse modalities: text-embedding, text-generation, text-to-speech and text-to-image, showing that adversaries can successfully achieve high leaderboard rankings while embedding arbitrary harmful functionalities, from backdoors to bias injection. Our findings reveal a significant vulnerability in the machine learning ecosystem, highlighting the urgent need to redesign leaderboard evaluation mechanisms to detect and filter malicious (e.g., poisoned) models, while exposing broader security implications for the machine learning community regarding the risks of adopting models from unverified sources.

</details>

### [Unlocking Speech Instruction Data Potential with Query Rewriting](2507.08603.md)
**Yonghua Hei, Yibo Yan, Shuliang Liu, Huiyu Zhou et al.** · 2025-07-11

<details>
<summary>Abstract</summary>

End-to-end Large Speech Language Models~(\textbf{LSLMs}) demonstrate strong potential in response latency and speech comprehension capabilities, showcasing general intelligence across speech understanding tasks. However, the ability to follow speech instructions has not been fully realized due to the lack of datasets and heavily biased training tasks. Leveraging the rich ASR datasets, previous approaches have used Large Language Models~(\textbf{LLMs}) to continue the linguistic information of speech to construct speech instruction datasets. Yet, due to the gap between LLM-generated results and real human responses, the continuation methods further amplify these shortcomings. Given the high costs of collecting and annotating speech instruction datasets by humans, using speech synthesis to construct large-scale speech instruction datasets has become a balanced and robust alternative. Although modern Text-To-Speech~(\textbf{TTS}) models have achieved near-human-level synthesis quality, it is challenging to appropriately convert out-of-distribution text instruction to speech due to the limitations of the training data distribution in TTS models. To address this issue, we propose a query rewriting framework with multi-LLM knowledge fusion, employing multiple agents to annotate and validate the synthesized speech, making it possible to construct high-quality speech instruction datasets without relying on human annotation. Experiments show that this method can transform text instructions into distributions more suitable for TTS models for speech synthesis through zero-shot rewriting, increasing data usability from 72\% to 93\%. It also demonstrates unique advantages in rewriting tasks that require complex knowledge and context-related abilities.

</details>

### [Active Learning for Text-to-Speech Synthesis with Informative Sample Collection](2507.08319.md)
**Kentaro Seki, Shinnosuke Takamichi, Takaaki Saeki, Hiroshi Saruwatari** · 2025-07-11

<details>
<summary>Abstract</summary>

The construction of high-quality datasets is a cornerstone of modern text-to-speech (TTS) systems. However, the increasing scale of available data poses significant challenges, including storage constraints. To address these issues, we propose a TTS corpus construction method based on active learning. Unlike traditional feed-forward and model-agnostic corpus construction approaches, our method iteratively alternates between data collection and model training, thereby focusing on acquiring data that is more informative for model improvement. This approach enables the construction of a data-efficient corpus. Experimental results demonstrate that the corpus constructed using our method enables higher-quality speech synthesis than corpora of the same size.

</details>

### [SemAlignVC: Enhancing zero-shot timbre conversion using semantic alignment](2507.09070.md)
**Shivam Mehta, Yingru Liu, Zhenyu Tang, Kainan Peng et al.** · 2025-07-11

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) synthesizes speech in a target speaker's voice while preserving linguistic and paralinguistic content. However, timbre leakage-where source speaker traits persist-remains a challenge, especially in neural codec and LLM-based VC, where quantized representations entangle speaker identity with content. We introduce SemAlignVC, an architecture designed to prevent timbre leakage using SemAlign, a novel method that aligns text and audio representations to ensure speaker-independent semantic encoding. This disentangled representation conditions an autoregressive transformer for high-fidelity conversion without explicit speaker embeddings. Experiments show SemAlignVC significantly reduces timbre leakage, outperforming baselines in speaker timbre similarity, intelligibility, and naturalness, making it a robust, privacy-preserving, and generalizable VC solution. Audio samples can be accessed at https://shivammehta25.github.io/SemAlignVC/

</details>

### [Detecting Deepfake Talking Heads from Facial Biometric Anomalies](2507.08917.md)
**Justin D. Norman, Hany Farid** · 2025-07-11

<details>
<summary>Abstract</summary>

The combination of highly realistic voice cloning, along with visually compelling avatar, face-swap, or lip-sync deepfake video generation, makes it relatively easy to create a video of anyone saying anything. Today, such deepfake impersonations are often used to power frauds, scams, and political disinformation. We propose a novel forensic machine learning technique for the detection of deepfake video impersonations that leverages unnatural patterns in facial biometrics. We evaluate this technique across a large dataset of deepfake techniques and impersonations, as well as assess its reliability to video laundering and its generalization to previously unseen video deepfake generators.

</details>

### [SecureSpeech: Prompt-based Speaker and Content Protection](2507.07799.md)
**Belinda Soh Hui Hui, Xiaoxiao Miao, Xin Wang** · 2025-07-10

<details>
<summary>Abstract</summary>

Given the increasing privacy concerns from identity theft and the re-identification of speakers through content in the speech field, this paper proposes a prompt-based speech generation pipeline that ensures dual anonymization of both speaker identity and spoken content. This is addressed through 1) generating a speaker identity unlinkable to the source speaker, controlled by descriptors, and 2) replacing sensitive content within the original text using a name entity recognition model and a large language model. The pipeline utilizes the anonymized speaker identity and text to generate high-fidelity, privacy-friendly speech via a text-to-speech synthesis model. Experimental results demonstrate an achievement of significant privacy protection while maintaining a decent level of content retention and audio quality. This paper also investigates the impact of varying speaker descriptions on the utility and privacy of generated speech to determine potential biases.

</details>

### [Animating Language Practice: Engagement with Stylized Conversational Agents in Japanese Learning](2507.06483.md)
**Zackary Rackauckas, Julia Hirschberg** · 2025-07-09

<details>
<summary>Abstract</summary>

We explore Jouzu, a Japanese language learning application that integrates large language models with anime-inspired conversational agents. Designed to address challenges learners face in practicing natural and expressive dialogue, Jouzu combines stylized character personas with expressive text-to-speech to create engaging conversational scenarios. We conducted a two-week in-the-wild deployment with 52 Japanese learners to examine how such stylized agents influence engagement and learner experience. Our findings show that participants interacted frequently and creatively, with advanced learners demonstrating greater use of expressive forms. Participants reported that the anime-inspired style made practice more enjoyable and encouraged experimenting with different registers. We discuss how stylization shapes willingness to engage, the role of affect in sustaining practice, and design opportunities for culturally grounded conversational AI in computer-assisted language learning (CALL). By framing our findings as an exploration of design and engagement, we highlight opportunities for generalization beyond Japanese contexts and contribute to international HCI scholarship.

</details>

### [Speech Tokenizer is Key to Consistent Representation](2507.06802.md)
**Wonjin Jung, Sungil Kang, Dong-Yeon Cho** · 2025-07-09

<details>
<summary>Abstract</summary>

Speech tokenization is crucial in digital speech processing, converting continuous speech signals into discrete units for various computational tasks. This paper introduces a novel speech tokenizer with broad applicability across downstream tasks. While recent advances in residual vector quantization (RVQ) have incorporated semantic elements, they often neglect critical acoustic features. We propose an advanced approach that simultaneously encodes both linguistic and acoustic information, preserving prosodic and emotional content. Our method significantly enhances speech representation fidelity across diverse applications. Empirical evaluations demonstrate its effectiveness in speech coding, voice conversion, emotion recognition, and multimodal language modeling, without requiring additional training. This versatility underscores its potential as a key tool for advancing AI-driven speech processing.

</details>

### [Differentiable Reward Optimization for LLM based TTS system](2507.05911.md)
**Changfeng Gao et.al.** · 2025-07-08

### [OpenS2S: Advancing Fully Open-Source End-to-End Empathetic Large Speech Language Model](2507.05177.md)
**Chen Wang et.al.** · 2025-07-08

### [SpeechAccentLLM: A Unified Framework for Foreign Accent Conversion and Text to Speech](2507.01348.md)
**Zhuangfei Cheng et.al.** · 2025-07-08

### [Speech Quality Assessment Model Based on Mixture of Experts: System-Level Performance Enhancement and Utterance-Level Challenge Analysis](2507.06116.md)
**Xintong Hu, Yixuan Chen, Rui Yang, Wenxiang Guo et al.** · 2025-07-08

<details>
<summary>Abstract</summary>

Automatic speech quality assessment plays a crucial role in the development of speech synthesis systems, but existing models exhibit significant performance variations across different granularity levels of prediction tasks. This paper proposes an enhanced MOS prediction system based on self-supervised learning speech models, incorporating a Mixture of Experts (MoE) classification head and utilizing synthetic data from multiple commercial generation models for data augmentation. Our method builds upon existing self-supervised models such as wav2vec2, designing a specialized MoE architecture to address different types of speech quality assessment tasks. We also collected a large-scale synthetic speech dataset encompassing the latest text-to-speech, speech conversion, and speech enhancement systems. However, despite the adoption of the MoE architecture and expanded dataset, the model's performance improvements in sentence-level prediction tasks remain limited. Our work reveals the limitations of current methods in handling sentence-level quality assessment, provides new technical pathways for the field of automatic speech quality assessment, and also delves into the fundamental causes of performance differences across different assessment granularities.

</details>

### [LAPS-Diff: A Diffusion-Based Framework for Singing Voice Synthesis With Language Aware Prosody-Style Guided Learning](2507.04966.md)
**Sandipan Dhar et.al.** · 2025-07-07

### [Multi-Step Prediction and Control of Hierarchical Emotion Distribution in Text-to-Speech Synthesis](2507.04598.md)
**Sho Inoue, Kun Zhou, Shuai Wang, Haizhou Li** · 2025-07-07

<details>
<summary>Abstract</summary>

We investigate hierarchical emotion distribution (ED) for achieving multi-level quantitative control of emotion rendering in text-to-speech synthesis (TTS). We introduce a novel multi-step hierarchical ED prediction module that quantifies emotion variance at the utterance, word, and phoneme levels. By predicting emotion variance in a multi-step manner, we leverage global emotional context to refine local emotional variations, thereby capturing the intrinsic hierarchical structure of speech emotion. Our approach is validated through its integration into a variance adaptor and an external module design compatible with various TTS systems. Both objective and subjective evaluations demonstrate that the proposed framework significantly enhances emotional expressiveness and enables precise control of emotion rendering across multiple speech granularities.

</details>

### [Fast-VGAN: Lightweight Voice Conversion with Explicit Control of F0 and Duration Parameters](2507.04817.md)
**Mathilde Abrassart, Nicolas Obin, Axel Roebel** · 2025-07-07

<details>
<summary>Abstract</summary>

Precise control over speech characteristics, such as pitch, duration, and speech rate, remains a significant challenge in the field of voice conversion. The ability to manipulate parameters like pitch and syllable rate is an important element for effective identity conversion, but can also be used independently for voice transformation, achieving goals that were historically addressed by vocoder-based methods. In this work, we explore a convolutional neural network-based approach that aims to provide means for modifying fundamental frequency (F0), phoneme sequences, intensity, and speaker identity. Rather than relying on disentanglement techniques, our model is explicitly conditioned on these factors to generate mel spectrograms, which are then converted into waveforms using a universal neural vocoder. Accordingly, during inference, F0 contours, phoneme sequences, and speaker embeddings can be freely adjusted, allowing for intuitively controlled voice transformations. We evaluate our approach on speaker conversion and expressive speech tasks using both perceptual and objective metrics. The results suggest that the proposed method offers substantial flexibility, while maintaining high intelligibility and speaker similarity.

</details>

### [TTS-CtrlNet: Time varying emotion aligned text-to-speech generation with ControlNet](2507.04349.md)
**Jaeseok Jeong, Yuna Lee, Mingi Kwon, Youngjung Uh** · 2025-07-06

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) have enabled natural speech synthesis, but fine-grained, time-varying emotion control remains challenging. Existing methods often allow only utterance-level control and require full model fine-tuning with a large emotion speech dataset, which can degrade performance. Inspired by adding conditional control to the existing model in ControlNet (Zhang et al, 2023), we propose the first ControlNet-based approach for controllable flow-matching TTS (TTS-CtrlNet), which freezes the original model and introduces a trainable copy of it to process additional conditions. We show that TTS-CtrlNet can boost the pretrained large TTS model by adding intuitive, scalable, and time-varying emotion control while inheriting the ability of the original model (e.g., zero-shot voice cloning & naturalness). Furthermore, we provide practical recipes for adding emotion control: 1) optimal architecture design choice with block analysis, 2) emotion-specific flow step, and 3) flexible control scale. Experiments show that ours can effectively add an emotion controller to existing TTS, and achieves state-of-the-art performance with emotion similarity scores: Emo-SIM and Aro-Val SIM. The project page is available at: https://curryjung.github.io/ttsctrlnet_project_page

</details>

### [Prosody Labeling with Phoneme-BERT and Speech Foundation Models](2507.03912.md)
**Tomoki Koriyama et.al.** · 2025-07-05

### [PresentAgent: Multimodal Agent for Presentation Video Generation](2507.04036.md)
**Jingwei Shi, Zeyu Zhang, Biao Wu, Yanjie Liang et al.** · 2025-07-05

<details>
<summary>Abstract</summary>

We present PresentAgent, a multimodal agent that transforms long-form documents into narrated presentation videos. While existing approaches are limited to generating static slides or text summaries, our method advances beyond these limitations by producing fully synchronized visual and spoken content that closely mimics human-style presentations. To achieve this integration, PresentAgent employs a modular pipeline that systematically segments the input document, plans and renders slide-style visual frames, generates contextual spoken narration with large language models and Text-to-Speech models, and seamlessly composes the final video with precise audio-visual alignment. Given the complexity of evaluating such multimodal outputs, we introduce PresentEval, a unified assessment framework powered by Vision-Language Models that comprehensively scores videos across three critical dimensions: content fidelity, visual clarity, and audience comprehension through prompt-based evaluation. Our experimental validation on a curated dataset of 30 document-presentation pairs demonstrates that PresentAgent approaches human-level quality across all evaluation metrics. These results highlight the significant potential of controllable multimodal agents in transforming static textual materials into dynamic, effective, and accessible presentation formats. Code will be available at https://github.com/AIGeeksGroup/PresentAgent.

</details>

### [RepeaTTS: Towards Feature Discovery through Repeated Fine-Tuning](2507.08012.md)
**Atli Sigurgeirsson, Simon King** · 2025-07-05

<details>
<summary>Abstract</summary>

A Prompt-based Text-To-Speech model allows a user to control different aspects of speech, such as speaking rate and perceived gender, through natural language instruction. Although user-friendly, such approaches are on one hand constrained: control is limited to acoustic features exposed to the model during training, and too flexible on the other: the same inputs yields uncontrollable variation that are reflected in the corpus statistics. We investigate a novel fine-tuning regime to address both of these issues at the same time by exploiting the uncontrollable variance of the model. Through principal component analysis of thousands of synthesised samples, we determine latent features that account for the highest proportion of the output variance and incorporate them as new labels for secondary fine-tuning. We evaluate the proposed methods on two models trained on an expressive Icelandic speech corpus, one with emotional disclosure and one without. In the case of the model without emotional disclosure, the method yields both continuous and discrete features that improve overall controllability of the model.

</details>

### [Traceable TTS: Toward Watermark-Free TTS with Strong Traceability](2507.03887.md)
**Yuxiang Zhao, Yunchong Xiao, Yushen Chen, Zhikang Niu et al.** · 2025-07-05

<details>
<summary>Abstract</summary>

Recent advances in Text-To-Speech (TTS) technology have enabled synthetic speech to mimic human voices with remarkable realism, raising significant security concerns. This underscores the need for traceable TTS models-systems capable of tracing their synthesized speech without compromising quality or security. However, existing methods predominantly rely on explicit watermarking on speech or on vocoder, which degrades speech quality and is vulnerable to spoofing. To address these limitations, we propose a novel framework for model attribution. Instead of embedding watermarks, we train the TTS model and discriminator using a joint training method that significantly improves traceability generalization while preserving-and even slightly improving-audio quality. This is the first work toward watermark-free TTS with strong traceability. To promote progress in related fields, we will release the code upon acceptance of the paper.

</details>

### [Improving Low-Resource Dialect Classification Using Retrieval-based Voice Conversion](2507.03641.md)
**Lea Fischbach, Akbar Karimi, Caroline Kleen, Alfred Lameli et al.** · 2025-07-04

<details>
<summary>Abstract</summary>

Deep learning models for dialect identification are often limited by the scarcity of dialectal data. To address this challenge, we propose to use Retrieval-based Voice Conversion (RVC) as an effective data augmentation method for a low-resource German dialect classification task. By converting audio samples to a uniform target speaker, RVC minimizes speaker-related variability, enabling models to focus on dialect-specific linguistic and phonetic features. Our experiments demonstrate that RVC enhances classification performance when utilized as a standalone augmentation method. Furthermore, combining RVC with other augmentation methods such as frequency masking and segment removal leads to additional performance gains, highlighting its potential for improving dialect classification in low-resource scenarios.

</details>

### [JoyTTS: LLM-based Spoken Chatbot With Voice Cloning](2507.02380.md)
**Fangru Zhou et.al.** · 2025-07-03

### [A conversational gesture synthesis system based on emotions and semantics](2507.03147.md)
**Thanh Hoang-Minh** · 2025-07-03

<details>
<summary>Abstract</summary>

Along with the explosion of large language models, improvements in speech synthesis, advancements in hardware, and the evolution of computer graphics, the current bottleneck in creating digital humans lies in generating character movements that correspond naturally to text or speech inputs. In this work, we present DeepGesture, a diffusion-based gesture synthesis framework for generating expressive co-speech gestures conditioned on multimodal signals - text, speech, emotion, and seed motion. Built upon the DiffuseStyleGesture model, DeepGesture introduces novel architectural enhancements that improve semantic alignment and emotional expressiveness in generated gestures. Specifically, we integrate fast text transcriptions as semantic conditioning and implement emotion-guided classifier-free diffusion to support controllable gesture generation across affective states. To visualize results, we implement a full rendering pipeline in Unity based on BVH output from the model. Evaluation on the ZeroEGGS dataset shows that DeepGesture produces gestures with improved human-likeness and contextual appropriateness. Our system supports interpolation between emotional states and demonstrates generalization to out-of-distribution speech, including synthetic voices - marking a step forward toward fully multimodal, emotionally aware digital humans.

</details>

### [De-AntiFake: Rethinking the Protective Perturbations Against Voice Cloning Attacks](2507.02606.md)
**Wei Fan, Kejiang Chen, Chang Liu, Weiming Zhang et al.** · 2025-07-03

<details>
<summary>Abstract</summary>

The rapid advancement of speech generation models has heightened privacy and security concerns related to voice cloning (VC). Recent studies have investigated disrupting unauthorized voice cloning by introducing adversarial perturbations. However, determined attackers can mitigate these protective perturbations and successfully execute VC. In this study, we conduct the first systematic evaluation of these protective perturbations against VC under realistic threat models that include perturbation purification. Our findings reveal that while existing purification methods can neutralize a considerable portion of the protective perturbations, they still lead to distortions in the feature space of VC models, which degrades the performance of VC. From this perspective, we propose a novel two-stage purification method: (1) Purify the perturbed speech; (2) Refine it using phoneme guidance to align it with the clean speech distribution. Experimental results demonstrate that our method outperforms state-of-the-art purification methods in disrupting VC defenses. Our study reveals the limitations of adversarial perturbation-based VC defenses and underscores the urgent need for more robust solutions to mitigate the security and privacy risks posed by VC. The code and audio samples are available at https://de-antifake.github.io.

</details>

### [A Dataset for Automatic Assessment of TTS Quality in Spanish](2507.01805.md)
**Alejandro Sosa Welford et.al.** · 2025-07-02

### [Pronunciation Editing for Finnish Speech using Phonetic Posteriorgrams](2507.02115.md)
**Zirui Li, Lauri Juvela, Mikko Kurimo** · 2025-07-02

<details>
<summary>Abstract</summary>

Synthesizing second-language (L2) speech is potentially highly valued for L2 language learning experience and feedback. However, due to the lack of L2 speech synthesis datasets, it is difficult to synthesize L2 speech for low-resourced languages. In this paper, we provide a practical solution for editing native speech to approximate L2 speech and present PPG2Speech, a diffusion-based multispeaker Phonetic-Posteriorgrams-to-Speech model that is capable of editing a single phoneme without text alignment. We use Matcha-TTS's flow-matching decoder as the backbone, transforming Phonetic Posteriorgrams (PPGs) to mel-spectrograms conditioned on external speaker embeddings and pitch. PPG2Speech strengthens the Matcha-TTS's flow-matching decoder with Classifier-free Guidance (CFG) and Sway Sampling. We also propose a new task-specific objective evaluation metric, the Phonetic Aligned Consistency (PAC), between the edited PPGs and the PPGs extracted from the synthetic speech for editing effects. We validate the effectiveness of our method on Finnish, a low-resourced, nearly phonetic language, using approximately 60 hours of data. We conduct objective and subjective evaluations of our approach to compare its naturalness, speaker similarity, and editing effectiveness with TTS-based editing. Our source code is published at https://github.com/aalto-speech/PPG2Speech.

</details>

### [Voice Conversion for Likability Control via Automated Rating of Speech Synthesis Corpora](2507.01356.md)
**Hitoshi Suda, Shinnosuke Takamichi, Satoru Fukayama** · 2025-07-02

<details>
<summary>Abstract</summary>

Perceived voice likability plays a crucial role in various social interactions, such as partner selection and advertising. A system that provides reference likable voice samples tailored to target audiences would enable users to adjust their speaking style and voice quality, facilitating smoother communication. To this end, we propose a voice conversion method that controls the likability of input speech while preserving both speaker identity and linguistic content. To improve training data scalability, we train a likability predictor on an existing voice likability dataset and employ it to automatically annotate a large speech synthesis corpus with likability ratings. Experimental evaluations reveal a significant correlation between the predictor's outputs and human-provided likability ratings. Subjective and objective evaluations further demonstrate that the proposed approach effectively controls voice likability while preserving both speaker identity and linguistic content.

</details>

### [QHARMA-GAN: Quasi-Harmonic Neural Vocoder based on Autoregressive Moving Average Model](2507.01611.md)
**Shaowen Chen, Tomoki Toda** · 2025-07-02

<details>
<summary>Abstract</summary>

Vocoders, encoding speech signals into acoustic features and allowing for speech signal reconstruction from them, have been studied for decades. Recently, the rise of deep learning has particularly driven the development of neural vocoders to generate high-quality speech signals. On the other hand, the existing end-to-end neural vocoders suffer from a black-box nature that blinds the speech production mechanism and the intrinsic structure of speech, resulting in the ambiguity of separately modeling source excitation and resonance characteristics and the loss of flexibly synthesizing or modifying speech with high quality. Moreover, their sequence-wise waveform generation usually requires complicated networks, leading to substantial time consumption. In this work, inspired by the quasi-harmonic model (QHM) that represents speech as sparse components, we combine the neural network and QHM synthesis process to propose a novel framework for the neural vocoder. Accordingly, speech signals can be encoded into autoregressive moving average (ARMA) functions to model the resonance characteristics, yielding accurate estimates of the amplitudes and phases of quasi-harmonics at any frequency. Subsequently, the speech can be resynthesized and arbitrarily modified in terms of pitch shifting and time stretching with high quality, whereas the time consumption and network size decrease. The experiments indicate that the proposed method leverages the strengths of QHM, the ARMA model, and neural networks, leading to the outperformance of our methods over other methods in terms of generation speed, synthesis quality, and modification flexibility.

</details>

### [StreamFlow: Streaming Flow Matching with Block-wise Guided Attention Mask for Speech Token Decoding](2506.23986.md)
**Dake Guo et.al.** · 2025-07-01

### [Multi-interaction TTS toward professional recording reproduction](2507.00808.md)
**Hiroki Kanagawa, Kenichi Fujita, Aya Watanabe, Yusuke Ijima** · 2025-07-01

<details>
<summary>Abstract</summary>

Voice directors often iteratively refine voice actors' performances by providing feedback to achieve the desired outcome. While this iterative feedback-based refinement process is important in actual recordings, it has been overlooked in text-to-speech synthesis (TTS). As a result, fine-grained style refinement after the initial synthesis is not possible, even though the synthesized speech often deviates from the user's intended style. To address this issue, we propose a TTS method with multi-step interaction that allows users to intuitively and rapidly refine synthesized speech. Our approach models the interaction between the TTS model and its user to emulate the relationship between voice actors and voice directors. Experiments show that the proposed model with its corresponding dataset enables iterative style refinements in accordance with users' directions, thus demonstrating its multi-interaction capability. Sample audios are available: https://ntt-hilab-gensp.github.io/ssw13multiinteractiontts/

</details>

### [MuteSwap: Visual-informed Silent Video Identity Conversion](2507.00498.md)
**Yifan Liu, Yu Fang, Zhouhan Lin** · 2025-07-01

<details>
<summary>Abstract</summary>

Conventional voice conversion modifies voice characteristics from a source speaker to a target speaker, relying on audio input from both sides. However, this process becomes infeasible when clean audio is unavailable, such as in silent videos or noisy environments. In this work, we focus on the task of Silent Face-based Voice Conversion (SFVC), which does voice conversion entirely from visual inputs. i.e., given images of a target speaker and a silent video of a source speaker containing lip motion, SFVC generates speech aligning the identity of the target speaker while preserving the speech content in the source silent video. As this task requires generating intelligible speech and converting identity using only visual cues, it is particularly challenging. To address this, we introduce MuteSwap, a novel framework that employs contrastive learning to align cross-modality identities and minimize mutual information to separate shared visual features. Experimental results show that MuteSwap achieves impressive performance in both speech synthesis and identity conversion, especially under noisy conditions where methods dependent on audio input fail to produce intelligible results, demonstrating both the effectiveness of our training approach and the feasibility of SFVC.

</details>

### [Investigating Stochastic Methods for Prosody Modeling in Speech Synthesis](2507.00227.md)
**Paul Mayer, Florian Lux, Alejandro Pérez-González-de-Martos, Angelina Elizarova et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

While generative methods have progressed rapidly in recent years, generating expressive prosody for an utterance remains a challenging task in text-to-speech synthesis. This is particularly true for systems that model prosody explicitly through parameters such as pitch, energy, and duration, which is commonly done for the sake of interpretability and controllability. In this work, we investigate the effectiveness of stochastic methods for this task, including Normalizing Flows, Conditional Flow Matching, and Rectified Flows. We compare these methods to a traditional deterministic baseline, as well as to real human realizations. Our extensive subjective and objective evaluations demonstrate that stochastic methods produce natural prosody on par with human speakers by capturing the variability inherent in human speech. Further, they open up additional controllability options by allowing the sampling temperature to be tuned.

</details>

### [JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching](2506.23552.md)
**Mingi Kwon, Joonghyuk Shin, Jaeseok Jung, Jaesik Park et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

The intrinsic link between facial motion and speech is often overlooked in generative modeling, where talking head synthesis and text-to-speech (TTS) are typically addressed as separate tasks. This paper introduces JAM-Flow, a unified framework to simultaneously synthesize and condition on both facial motion and speech. Our approach leverages flow matching and a novel Multi-Modal Diffusion Transformer (MM-DiT) architecture, integrating specialized Motion-DiT and Audio-DiT modules. These are coupled via selective joint attention layers and incorporate key architectural choices, such as temporally aligned positional embeddings and localized joint attention masking, to enable effective cross-modal interaction while preserving modality-specific strengths. Trained with an inpainting-style objective, JAM-Flow supports a wide array of conditioning inputs-including text, reference audio, and reference motion-facilitating tasks such as synchronized talking head generation from text, audio-driven animation, and much more, within a single, coherent model. JAM-Flow significantly advances multi-modal generative modeling by providing a practical solution for holistic audio-visual synthesis. project page: https://joonghyuk.com/jamflow-web

</details>

### [Collecting, Curating, and Annotating Good Quality Speech deepfake dataset for Famous Figures: Process and Challenges](2507.00324.md)
**Hashim Ali, Surya Subramani, Raksha Varahamurthy, Nithin Adupa et al.** · 2025-06-30

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis have introduced unprecedented challenges in maintaining voice authenticity, particularly concerning public figures who are frequent targets of impersonation attacks. This paper presents a comprehensive methodology for collecting, curating, and generating synthetic speech data for political figures and a detailed analysis of challenges encountered. We introduce a systematic approach incorporating an automated pipeline for collecting high-quality bonafide speech samples, featuring transcription-based segmentation that significantly improves synthetic speech quality. We experimented with various synthesis approaches; from single-speaker to zero-shot synthesis, and documented the evolution of our methodology. The resulting dataset comprises bonafide and synthetic speech samples from ten public figures, demonstrating superior quality with a NISQA-TTS naturalness score of 3.69 and the highest human misclassification rate of 61.9\%.

</details>

### [Efficient Interleaved Speech Modeling through Knowledge Distillation](2506.23670.md)
**Mohammadmahdi Nouriborji, Morteza Rohanian** · 2025-06-30

<details>
<summary>Abstract</summary>

Current speech language models exceed the size and latency constraints of many deployment environments. We build compact, expressive speech generation models through layer-aligned distillation, matching hidden states, attention maps, and softened logits to compress large multimodal transformers by 3x with minimal loss in performance. We introduce TinyWave, a family of 2B-parameter models for speech-to-speech and interleaved speech-text generation, trained on 50,000 hours of public audio. TinyWave supports (i) speech-only generation using phonetic or expressive tokens and (ii) mixed speech-text continuations. Evaluation on Libri-Light shows TinyWave within 1.4 normalized perplexity points of its teacher. Accuracy on spoken StoryCloze and SALMon reaches 93-97% of the teacher's performance, outperforming size-matched baselines. These models are optimized for deployment on commodity hardware, enabling applications in real-time conversational agents, assistive technologies, and low-resource environments. We release models, training code, and evaluation scripts to support reproducible research on compact, expressive speech generation.

</details>

### [You Sound a Little Tense: L2 Tailored Clear TTS Using Durational Vowel Properties](2506.23367.md)
**Paige Tuttösí, H. Henny Yeung, Yue Wang, Jean-Julien Aucouturier et al.** · 2025-06-29

<details>
<summary>Abstract</summary>

We present the first text-to-speech (TTS) system tailored to second language (L2) speakers. We use duration differences between American English tense (longer) and lax (shorter) vowels to create a "clarity mode" for Matcha-TTS. Our perception studies showed that French-L1, English-L2 listeners had fewer (at least 9.15%) transcription errors when using our clarity mode, and found it more encouraging and respectful than overall slowed down speech. Remarkably, listeners were not aware of these effects: despite the decreased word error rate in clarity mode, listeners still believed that slowing all target words was the most intelligible, suggesting that actual intelligibility does not correlate with perceived intelligibility. Additionally, we found that Whisper-ASR did not use the same cues as L2 speakers to differentiate difficult vowels and is not sufficient to assess the intelligibility of TTS systems for these individuals.

</details>

### [DiffSoundStream: Efficient Speech Tokenization via Diffusion Decoding](2506.22362.md)
**Yang Yang et.al.** · 2025-06-27

### [Robust and Efficient Autoregressive Speech Synthesis with Dynamic Chunk-wise Prediction Policy](2506.22023.md)
**Bohan Li et.al.** · 2025-06-27

### [Evaluating Pointing Gestures for Target Selection in Human-Robot Collaboration](2506.22116.md)
**Noora Sassali, Roel Pieters** · 2025-06-27

<details>
<summary>Abstract</summary>

Pointing gestures are a common interaction method used in Human-Robot Collaboration for various tasks, ranging from selecting targets to guiding industrial processes. This study introduces a method for localizing pointed targets within a planar workspace. The approach employs pose estimation, and a simple geometric model based on shoulder-wrist extension to extract gesturing data from an RGB-D stream. The study proposes a rigorous methodology and comprehensive analysis for evaluating pointing gestures and target selection in typical robotic tasks. In addition to evaluating tool accuracy, the tool is integrated into a proof-of-concept robotic system, which includes object detection, speech transcription, and speech synthesis to demonstrate the integration of multiple modalities in a collaborative application. Finally, a discussion over tool limitations and performance is provided to understand its role in multimodal robotic systems. All developments are available at: https://github.com/NMKsas/gesture_pointer.git.

</details>

### [SmoothSinger: A Conditional Diffusion Model for Singing Voice Synthesis with Multi-Resolution Architecture](2506.21478.md)
**Kehan Sui et.al.** · 2025-06-26

### [A Multi-Stage Framework for Multimodal Controllable Speech Synthesis](2506.20945.md)
**Rui Niu et.al.** · 2025-06-26

### [An Exploration of ECAPA-TDNN and x-vector Speaker Representations in Zero-shot Multi-speaker TTS](2506.20190.md)
**Marie Kunešová et.al.** · 2025-06-25

### [TTSDS2: Resources and Benchmark for Evaluating Human-Quality Text to Speech Systems](2506.19441.md)
**Christoph Minixhofer et.al.** · 2025-06-24

### [IndexTTS2: A Breakthrough in Emotionally Expressive and Duration-Controlled Auto-Regressive Zero-Shot Text-to-Speech](2506.21619.md)
**Siyi Zhou et.al.** · 2025-06-23

### [Selecting N-lowest scores for training MOS prediction models](2506.18326.md)
**Yuto Kondo, Hirokazu Kameoka, Kou Tanaka, Takuhiro Kaneko** · 2025-06-23

<details>
<summary>Abstract</summary>

The automatic speech quality assessment (SQA) has been extensively studied to predict the speech quality without time-consuming questionnaires. Recently, neural-based SQA models have been actively developed for speech samples produced by text-to-speech or voice conversion, with a primary focus on training mean opinion score (MOS) prediction models. The quality of each speech sample may not be consistent across the entire duration, and it remains unclear which segments of the speech receive the primary focus from humans when assigning subjective evaluation for MOS calculation. We hypothesize that when humans rate speech, they tend to assign more weight to low-quality speech segments, and the variance in ratings for each sample is mainly due to accidental assignment of higher scores when overlooking the poor quality speech segments. Motivated by the hypothesis, we analyze the VCC2018 and BVCC datasets. Based on the hypothesis, we propose the more reliable representative value N_low-MOS, the mean of the $N$-lowest opinion scores. Our experiments show that LCC and SRCC improve compared to regular MOS when employing N_low-MOS to MOSNet training. This result suggests that N_low-MOS is a more intrinsic representative value of subjective speech quality and makes MOSNet a better comparator of VC models.

</details>

### [Rethinking Mean Opinion Scores in Speech Quality Assessment: Aggregation through Quantized Distribution Fitting](2506.18307.md)
**Yuto Kondo, Hirokazu Kameoka, Kou Tanaka, Takuhiro Kaneko** · 2025-06-23

<details>
<summary>Abstract</summary>

Speech quality assessment (SQA) aims to evaluate the quality of speech samples without relying on time-consuming listener questionnaires. Recent efforts have focused on training neural-based SQA models to predict the mean opinion score (MOS) of speech samples produced by text-to-speech or voice conversion systems. This paper targets the enhancement of MOS prediction models' performance. We propose a novel score aggregation method to address the limitations of conventional annotations for MOS, which typically involve ratings on a scale from 1 to 5. Our method is based on the hypothesis that annotators internally consider continuous scores and then choose the nearest discrete rating. By modeling this process, we approximate the generative distribution of ratings by quantizing the latent continuous distribution. We then use the peak of this latent distribution, estimated through the loss between the quantized distribution and annotated ratings, as a new representative value instead of MOS. Experimental results demonstrate that substituting MOSNet's predicted target with this proposed value improves prediction performance.

</details>

### [JIS: A Speech Corpus of Japanese Idol Speakers with Various Speaking Styles](2506.18296.md)
**Yuto Kondo, Hirokazu Kameoka, Kou Tanaka, Takuhiro Kaneko** · 2025-06-23

<details>
<summary>Abstract</summary>

We construct Japanese Idol Speech Corpus (JIS) to advance research in speech generation AI, including text-to-speech synthesis (TTS) and voice conversion (VC). JIS will facilitate more rigorous evaluations of speaker similarity in TTS and VC systems since all speakers in JIS belong to a highly specific category: "young female live idols" in Japan, and each speaker is identified by a stage name, enabling researchers to recruit listeners familiar with these idols for listening experiments. With its unique speaker attributes, JIS will foster compelling research, including generating voices tailored to listener preferences-an area not yet widely studied. JIS will be distributed free of charge to promote research in speech generation AI, with usage restricted to non-commercial, basic research. We describe the construction of JIS, provide an overview of Japanese live idol culture to support effective and ethical use of JIS, and offer a basic analysis to guide application of JIS.

</details>

### [OpusLM: A Family of Open Unified Speech Language Models](2506.17611.md)
**Jinchuan Tian et.al.** · 2025-06-21

### [RapFlow-TTS: Rapid and High-Fidelity Text-to-Speech with Improved Consistency Flow Matching](2506.16741.md)
**Hyun Joon Park et.al.** · 2025-06-20

### [ZipVoice: Fast and High-Quality Zero-Shot Text-to-Speech with Flow Matching](2506.13053.md)
**Han Zhu et.al.** · 2025-06-20

### [V-CASS: Vision-context-aware Expressive Speech Synthesis for Enhancing User Understanding of Videos](2506.16716.md)
**Qixin Wang, Songtao Zhou, Zeyu Jin, Chenglin Guo et al.** · 2025-06-20

<details>
<summary>Abstract</summary>

Automatic video commentary systems are widely used on multimedia social media platforms to extract factual information about video content. However, current systems may overlook essential para-linguistic cues, including emotion and attitude, which are critical for fully conveying the meaning of visual content. The absence of these cues can limit user understanding or, in some cases, distort the video's original intent. Expressive speech effectively conveys these cues and enhances the user's comprehension of videos. Building on these insights, this paper explores the usage of vision-context-aware expressive speech in enhancing users' understanding of videos in video commentary systems. Firstly, our formatting study indicates that semantic-only speech can lead to ambiguity, and misaligned emotions between speech and visuals may distort content interpretation. To address this, we propose a method called vision-context-aware speech synthesis (V-CASS). It analyzes para-linguistic cues from visuals using a vision-language model and leverages a knowledge-infused language model to guide the expressive speech model in generating context-aligned speech. User studies show that V-CASS enhances emotional and attitudinal resonance, as well as user audio-visual understanding and engagement, with 74.68% of participants preferring the system. Finally, we explore the potential of our method in helping blind and low-vision users navigate web videos, improving universal accessibility.

</details>

### [InstructTTSEval: Benchmarking Complex Natural-Language Instruction Following in Text-to-Speech Systems](2506.16381.md)
**Kexin Huang et.al.** · 2025-06-19

### [Streaming Non-Autoregressive Model for Accent Conversion and Pronunciation Improvement](2506.16580.md)
**Tuan-Nam Nguyen, Ngoc-Quan Pham, Seymanur Akti, Alexander Waibel** · 2025-06-19

<details>
<summary>Abstract</summary>

We propose a first streaming accent conversion (AC) model that transforms non-native speech into a native-like accent while preserving speaker identity, prosody and improving pronunciation. Our approach enables stream processing by modifying a previous AC architecture with an Emformer encoder and an optimized inference mechanism. Additionally, we integrate a native text-to-speech (TTS) model to generate ideal ground-truth data for efficient training. Our streaming AC model achieves comparable performance to the top AC models while maintaining stable latency, making it the first AC system capable of streaming.

</details>

### [Optimizing Multilingual Text-To-Speech with Accents & Emotions](2506.16310.md)
**Pranav Pawar, Akshansh Dwivedi, Jenish Boricha, Himanshu Gohil et al.** · 2025-06-19

<details>
<summary>Abstract</summary>

State-of-the-art text-to-speech (TTS) systems realize high naturalness in monolingual environments, synthesizing speech with correct multilingual accents (especially for Indic languages) and context-relevant emotions still poses difficulty owing to cultural nuance discrepancies in current frameworks. This paper introduces a new TTS architecture integrating accent along with preserving transliteration with multi-scale emotion modelling, in particularly tuned for Hindi and Indian English accent. Our approach extends the Parler-TTS model by integrating A language-specific phoneme alignment hybrid encoder-decoder architecture, and culture-sensitive emotion embedding layers trained on native speaker corpora, as well as incorporating a dynamic accent code switching with residual vector quantization. Quantitative tests demonstrate 23.7% improvement in accent accuracy (Word Error Rate reduction from 15.4% to 11.8%) and 85.3% emotion recognition accuracy from native listeners, surpassing METTS and VECL-TTS baselines. The novelty of the system is that it can mix code in real time - generating statements such as "Namaste, let's talk about <Hindi phrase>" with uninterrupted accent shifts while preserving emotional consistency. Subjective evaluation with 200 users reported a mean opinion score (MOS) of 4.2/5 for cultural correctness, much better than existing multilingual systems (p<0.01). This research makes cross-lingual synthesis more feasible by showcasing scalable accent-emotion disentanglement, with direct application in South Asian EdTech and accessibility software.

</details>

### [Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching](2506.16127.md)
**Shoutrik Das, Nishant Singh, Arjun Gangwar, S Umesh** · 2025-06-19

<details>
<summary>Abstract</summary>

Dysarthria is a neurological disorder that significantly impairs speech intelligibility, often rendering affected individuals unable to communicate effectively. This necessitates the development of robust dysarthric-to-regular speech conversion techniques. In this work, we investigate the utility and limitations of self-supervised learning (SSL) features and their quantized representations as an alternative to mel-spectrograms for speech generation. Additionally, we explore methods to mitigate speaker variability by generating clean speech in a single-speaker voice using features extracted from WavLM. To this end, we propose a fully non-autoregressive approach that leverages Conditional Flow Matching (CFM) with Diffusion Transformers to learn a direct mapping from dysarthric to clean speech. Our findings highlight the effectiveness of discrete acoustic units in improving intelligibility while achieving faster convergence compared to traditional mel-spectrogram-based approaches.

</details>

### [TTSOps: A Closed-Loop Corpus Optimization Framework for Training Multi-Speaker TTS Models from Dark Data](2506.15614.md)
**Kentaro Seki et.al.** · 2025-06-18

### [Factorized RVQ-GAN For Disentangled Speech Tokenization](2506.15456.md)
**Sameer Khurana et.al.** · 2025-06-18

### [PredGen: Accelerated Inference of Large Language Models through Input-Time Speculation for Real-Time Speech Interaction](2506.15556.md)
**Shufan Li, Aditya Grover** · 2025-06-18

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are widely used in real-time voice chat applications, typically in combination with text-to-speech (TTS) systems to generate audio responses. However, their large size often leads to noticeable latency between the end of user input and the start of audio output, resulting in suboptimal user experiences. This latency is particularly evident when LLMs are deployed as single-user voice assistants on consumer-grade hardware with limited computing capacity. We discovered that this latency is primarily dominated by the time it takes for the LLMs to generate the first sentence, which is required as input by the TTS systems that synthesize audio responses on a sentence-by-sentence basis. To address this bottleneck, we propose Predictive Generation (PredGen), a novel framework that mitigates-or even eliminates-this delay through speculative decoding at input time. PredGen generates candidate responses while the user is still speaking, enabling the system to begin TTS processing with minimal delay. Simulated experiments on the Lmsys and MT-Bench datasets show that the proposed method can effectively reduce the latency by around 2x across a wide range of use cases, while incurring only minimal additional computation cost at input time-computation that would otherwise go unused.

</details>

### [EmojiVoice: Towards long-term controllable expressivity in robot speech](2506.15085.md)
**Paige Tuttösí, Shivam Mehta, Zachary Syvenky, Bermet Burkanova et al.** · 2025-06-18

<details>
<summary>Abstract</summary>

Humans vary their expressivity when speaking for extended periods to maintain engagement with their listener. Although social robots tend to be deployed with ``expressive'' joyful voices, they lack this long-term variation found in human speech. Foundation model text-to-speech systems are beginning to mimic the expressivity in human speech, but they are difficult to deploy offline on robots. We present EmojiVoice, a free, customizable text-to-speech (TTS) toolkit that allows social roboticists to build temporally variable, expressive speech on social robots. We introduce emoji-prompting to allow fine-grained control of expressivity on a phase level and use the lightweight Matcha-TTS backbone to generate speech in real-time. We explore three case studies: (1) a scripted conversation with a robot assistant, (2) a storytelling robot, and (3) an autonomous speech-to-speech interactive agent. We found that using varied emoji prompting improved the perception and expressivity of speech over a long period in a storytelling task, but expressive voice was not preferred in the assistant use case.

</details>

### [EmoNews: A Spoken Dialogue System for Expressive News Conversations](2506.13894.md)
**Ryuki Matsuura, Shikhar Bharadwaj, Jiarui Liu, Dhatchi Kunde Govindarajan** · 2025-06-16

<details>
<summary>Abstract</summary>

We develop a task-oriented spoken dialogue system (SDS) that regulates emotional speech based on contextual cues to enable more empathetic news conversations. Despite advancements in emotional text-to-speech (TTS) techniques, task-oriented emotional SDSs remain underexplored due to the compartmentalized nature of SDS and emotional TTS research, as well as the lack of standardized evaluation metrics for social goals. We address these challenges by developing an emotional SDS for news conversations that utilizes a large language model (LLM)-based sentiment analyzer to identify appropriate emotions and PromptTTS to synthesize context-appropriate emotional speech. We also propose subjective evaluation scale for emotional SDSs and judge the emotion regulation performance of the proposed and baseline systems. Experiments showed that our emotional SDS outperformed a baseline system in terms of the emotion regulation and engagement. These results suggest the critical role of speech emotion for more engaging conversations. All our source code is open-sourced at https://github.com/dhatchi711/espnet-emotional-news/tree/emo-sds/egs2/emo_news_sds/sds1

</details>

### [Multimodal Integration Challenges in Emotionally Expressive Child Avatars for Training Applications](2506.13477.md)
**Pegah Salehi, Sajad Amouei Sheshkal, Vajira Thambawita, Michael A. Riegler et al.** · 2025-06-16

<details>
<summary>Abstract</summary>

Dynamic facial emotion is essential for believable AI-generated avatars, yet most systems remain visually static, limiting their use in simulations like virtual training for investigative interviews with abused children. We present a real-time architecture combining Unreal Engine 5 MetaHuman rendering with NVIDIA Omniverse Audio2Face to generate facial expressions from vocal prosody in photorealistic child avatars. Due to limited TTS options, both avatars were voiced using young adult female models from two systems to better fit character profiles, introducing a voice-age mismatch. This confound may affect audiovisual alignment. We used a two-PC setup to decouple speech generation from GPU-intensive rendering, enabling low-latency interaction in desktop and VR. A between-subjects study (N=70) compared audio+visual vs. visual-only conditions as participants rated emotional clarity, facial realism, and empathy for avatars expressing joy, sadness, and anger. While emotions were generally recognized - especially sadness and joy - anger was harder to detect without audio, highlighting the role of voice in high-arousal expressions. Interestingly, silencing clips improved perceived realism by removing mismatches between voice and animation, especially when tone or age felt incongruent. These results emphasize the importance of audiovisual congruence: mismatched voice undermines expression, while a good match can enhance weaker visuals - posing challenges for emotionally coherent avatars in sensitive contexts.

</details>

### [StreamMel: Real-Time Zero-shot Text-to-Speech via Interleaved Continuous Autoregressive Modeling](2506.12570.md)
**Hui Wang et.al.** · 2025-06-14

### [Phonikud: Overcoming Phonetic Underspecification for Hebrew Text-To-Speech](2506.12311.md)
**Yakov Kolani, Maxim Melichov, Cobi Calev, Morris Alper** · 2025-06-14

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) for Modern Hebrew is challenged by the language's orthographic complexity, with existing solutions ignoring underspecified phonetic features such as stress. We present a framework for more phonetically accurate Hebrew TTS with four contributions: (1) Phonikud, an open-source Hebrew grapheme-to-phoneme (G2P) system that outputs fully-specified International Phonetic Alphabet (IPA) transcriptions, designed by augmenting a base diacritizer. (2) The ILSpeech corpus of paired Hebrew audio, text, and expert IPA annotations. (3) A benchmark for the previously unmeasured task of Hebrew G2P conversion. (4) Hebrew audio-to-IPA models capturing previously disregarded phonetic details for automatic TTS evaluation. Our results show that Phonikud more accurately predicts Hebrew phonemes than prior methods, and that small, local TTS models with phonetic input from Phonikud approach large proprietary systems. We release our code, data, and models at https://phonikud.github.io.

</details>

### [What Makes a Good Speech Tokenizer for LLM-Centric Speech Generation? A Systematic Study](2506.12537.md)
**Xiaoran Fan, Zhichao Sun, Yangfan Gao, Jingfei Xiong et al.** · 2025-06-14

<details>
<summary>Abstract</summary>

Speech-language models (SLMs) offer a promising path toward unifying speech and text understanding and generation. However, challenges remain in achieving effective cross-modal alignment and high-quality speech generation. In this work, we systematically investigate the role of speech tokenizer designs in LLM-centric SLMs, augmented by speech heads and speaker modeling. We compare coupled, semi-decoupled, and fully decoupled speech tokenizers under a fair SLM framework and find that decoupled tokenization significantly improves alignment and synthesis quality. To address the information density mismatch between speech and text, we introduce multi-token prediction (MTP) into SLMs, enabling each hidden state to decode multiple speech tokens. This leads to up to 12$\times$ faster decoding and a substantial drop in word error rate (from 6.07 to 3.01). Furthermore, we propose a speaker-aware generation paradigm and introduce RoleTriviaQA, a large-scale role-playing knowledge QA benchmark with diverse speaker identities. Experiments demonstrate that our methods enhance both knowledge understanding and speaker consistency.

</details>

### [Scheduled Interleaved Speech-Text Training for Speech-to-Speech Translation with LLMs](2506.10299.md)
**Hayato Futami et.al.** · 2025-06-12

### [RT-VC: Real-Time Zero-Shot Voice Conversion with Speech Articulatory Coding](2506.10289.md)
**Yisi Liu, Chenyang Wang, Hanjo Kim, Raniya Khan et al.** · 2025-06-12

<details>
<summary>Abstract</summary>

Voice conversion has emerged as a pivotal technology in numerous applications ranging from assistive communication to entertainment. In this paper, we present RT-VC, a zero-shot real-time voice conversion system that delivers ultra-low latency and high-quality performance. Our approach leverages an articulatory feature space to naturally disentangle content and speaker characteristics, facilitating more robust and interpretable voice transformations. Additionally, the integration of differentiable digital signal processing (DDSP) enables efficient vocoding directly from articulatory features, significantly reducing conversion latency. Experimental evaluations demonstrate that, while maintaining synthesis quality comparable to the current state-of-the-art (SOTA) method, RT-VC achieves a CPU latency of 61.4 ms, representing a 13.3\% reduction in latency.

</details>

### [S2ST-Omni: An Efficient and Scalable Multilingual Speech-to-Speech Translation Framework via Seamlessly Speech-Text Alignment and Streaming Speech Decoder](2506.11160.md)
**Yu Pan et.al.** · 2025-06-11

### [UmbraTTS: Adapting Text-to-Speech to Environmental Contexts with Flow Matching](2506.09874.md)
**Neta Glazer et.al.** · 2025-06-11

### [Ming-Omni: A Unified Multimodal Model for Perception and Generation](2506.09344.md)
**Inclusion AI, Biao Gong, Cheng Zou, Chuanyang Zheng et al.** · 2025-06-11

<details>
<summary>Abstract</summary>

We propose Ming-Omni, a unified multimodal model capable of processing images, text, audio, and video, while demonstrating strong proficiency in both speech and image generation. Ming-Omni employs dedicated encoders to extract tokens from different modalities, which are then processed by Ling, an MoE architecture equipped with newly proposed modality-specific routers. This design enables a single model to efficiently process and fuse multimodal inputs within a unified framework, thereby facilitating diverse tasks without requiring separate models, task-specific fine-tuning, or structural redesign. Importantly, Ming-Omni extends beyond conventional multimodal models by supporting audio and image generation. This is achieved through the integration of an advanced audio decoder for natural-sounding speech and Ming-Lite-Uni for high-quality image generation, which also allow the model to engage in context-aware chatting, perform text-to-speech conversion, and conduct versatile image editing. Our experimental results showcase Ming-Omni offers a powerful solution for unified perception and generation across all modalities. Notably, our proposed Ming-Omni is the first open-source model we are aware of to match GPT-4o in modality support, and we release all code and model weights to encourage further research and development in the community.

</details>

### [DrVoice: Parallel Speech-Text Voice Conversation Model via Dual-Resolution Speech Representations](2506.09349.md)
**Chao-Hong Tan, Qian Chen, Wen Wang, Chong Deng et al.** · 2025-06-11

<details>
<summary>Abstract</summary>

Recent studies on end-to-end (E2E) speech generation with large language models (LLMs) have attracted significant community attention, with multiple works extending text-based LLMs to generate discrete speech tokens. Existing E2E approaches primarily fall into two categories: (1) Methods that generate discrete speech tokens independently without incorporating them into the LLM's autoregressive process, resulting in text generation being unaware of concurrent speech synthesis. (2) Models that generate interleaved or parallel speech-text tokens through joint autoregressive modeling, enabling mutual modality awareness during generation. This paper presents DrVoice, a parallel speech-text voice conversation model based on joint autoregressive modeling, featuring dual-resolution speech representations. Notably, while current methods utilize mainly 12.5Hz input audio representation, our proposed dual-resolution mechanism reduces the input frequency for the LLM to 5Hz, significantly reducing computational cost and alleviating the frequency discrepancy between speech and text tokens and in turn better exploiting LLMs' capabilities. Experimental results demonstrate that DrVoice-7B establishes new state-of-the-art (SOTA) on prominent speech benchmarks including OpenAudioBench, VoiceBench, UltraEval-Audio and Big Bench Audio, making it a leading open-source speech foundation model in ~7B models.

</details>

### [Training-Free Voice Conversion with Factorized Optimal Transport](2506.09709.md)
**Alexander Lobashev, Assel Yermekova, Maria Larchenko** · 2025-06-11

<details>
<summary>Abstract</summary>

This paper introduces Factorized MKL-VC, a training-free modification for kNN-VC pipeline. In contrast with original pipeline, our algorithm performs high quality any-to-any cross-lingual voice conversion with only 5 second of reference audio. MKL-VC replaces kNN regression with a factorized optimal transport map in WavLM embedding subspaces, derived from Monge-Kantorovich Linear solution. Factorization addresses non-uniform variance across dimensions, ensuring effective feature transformation. Experiments on LibriSpeech and FLEURS datasets show MKL-VC significantly improves content preservation and robustness with short reference audio, outperforming kNN-VC. MKL-VC achieves performance comparable to FACodec, especially in cross-lingual voice conversion domain.

</details>

### [A Self-Refining Framework for Enhancing ASR Using TTS-Synthesized Data](2506.11130.md)
**Cheng-Kang Chou, Chan-Jan Hsu, Ho-Lam Chung, Liang-Hsuan Tseng et al.** · 2025-06-10

<details>
<summary>Abstract</summary>

We propose a self-refining framework that enhances ASR performance with only unlabeled datasets. The process starts with an existing ASR model generating pseudo-labels on unannotated speech, which are then used to train a high-fidelity text-to-speech (TTS) system. Then, synthesized speech text pairs are bootstrapped into the original ASR system, completing the closed-loop self-improvement cycle. We demonstrated the effectiveness of the framework on Taiwanese Mandarin speech. Leveraging 6,000 hours of unlabeled speech, a moderate amount of text data, and synthetic content from the AI models, we adapt Whisper-large-v2 into a specialized model, Twister. Twister reduces error rates by up to 20% on Mandarin and 50% on Mandarin-English code-switching benchmarks compared to Whisper. Results highlight the framework as a compelling alternative to pseudo-labeling self-distillation approaches and provides a practical pathway for improving ASR performance in low-resource or domain-specific settings.

</details>

### [UITron-Speech: Towards Automated GUI Agents Based on Speech Instructions](2506.11127.md)
**Wenkang Han, Zhixiong Zeng, Jing Huang, Shu Jiang et al.** · 2025-06-10

<details>
<summary>Abstract</summary>

Autonomous agents for Graphical User Interfaces (GUIs) are revolutionizing human-computer interaction, yet their reliance on text-based instructions imposes limitations on accessibility and convenience, particularly in hands-free scenarios. To address this issue, we propose replacing text with speech as the instruction input modality for GUI agents, and introduce UITron-Speech, which is the first end-to-end GUI agent capable of directly processing speech instructions and on-device screenshots to predict user actions. To tackle the problem of data scarcity, we synthesize high-quality speech instruction datasets using a random-speaker text-to-speech model. Additionally, we design a mixed-modality training strategy to mitigate the inherent modality imbalance in pre-trained foundation models. Furthermore, we conduct a statistical analysis of the distribution of GUI grounding prediction errors and propose a training-free two-step grounding refinement method to alleviate minor localization deviations. Extensive experiments on multiple benchmarks demonstrate that UITron-Speech achieves robust performance and superior adaptability, underscoring the feasibility and potential of speech-driven GUI agents for more accessible and intelligent human-computer interaction. Our code and datasets are available at https://github.com/UITron-hub/UITron-Speech.

</details>

### [Audio Generation Through Score-Based Generative Modeling: Design Principles and Implementation](2506.08457.md)
**Ge Zhu, Yutong Wen, Zhiyao Duan** · 2025-06-10

<details>
<summary>Abstract</summary>

Diffusion models have emerged as powerful deep generative techniques, producing high-quality and diverse samples in applications in various domains including audio. While existing reviews provide overviews, there remains limited in-depth discussion of these specific design choices. The audio diffusion model literature also lacks principled guidance for the implementation of these design choices and their comparisons for different applications. This survey provides a comprehensive review of diffusion model design with an emphasis on design principles for quality improvement and conditioning for audio applications. We adopt the score modeling perspective as a unifying framework that accommodates various interpretations, including recent approaches like flow matching. We systematically examine the training and sampling procedures of diffusion models, and audio applications through different conditioning mechanisms. To provide an integrated, unified codebase and to promote reproducible research and rapid prototyping, we introduce an open-source codebase (https://github.com/gzhu06/AudioDiffuser) that implements our reviewed framework for various audio applications. We demonstrate its capabilities through three case studies: audio generation, speech enhancement, and text-to-speech synthesis, with benchmark evaluations on standard datasets.

</details>

### [Step-Audio-AQAA: a Fully End-to-End Expressive Large Audio Language Model](2506.08967.md)
**Ailin Huang, Bingxin Li, Bruce Wang, Boyong Wu et al.** · 2025-06-10

<details>
<summary>Abstract</summary>

Large Audio-Language Models (LALMs) have significantly advanced intelligent human-computer interaction, yet their reliance on text-based outputs limits their ability to generate natural speech responses directly, hindering seamless audio interactions. To address this, we introduce Step-Audio-AQAA, a fully end-to-end LALM designed for Audio Query-Audio Answer (AQAA) tasks. The model integrates a dual-codebook audio tokenizer for linguistic and semantic feature extraction, a 130-billion-parameter backbone LLM and a neural vocoder for high-fidelity speech synthesis. Our post-training approach employs interleaved token-output of text and audio to enhance semantic coherence and combines Direct Preference Optimization (DPO) with model merge to improve performance. Evaluations on the StepEval-Audio-360 benchmark demonstrate that Step-Audio-AQAA excels especially in speech control, outperforming the state-of-art LALMs in key areas. This work contributes a promising solution for end-to-end LALMs and highlights the critical role of token-based vocoder in enhancing overall performance for AQAA tasks.

</details>

### [Pureformer-VC: Non-parallel Voice Conversion with Pure Stylized Transformer Blocks and Triplet Discriminative Training](2506.08348.md)
**Wenhan Yao, Fen Xiao, Xiarun Chen, Jia Liu et al.** · 2025-06-10

<details>
<summary>Abstract</summary>

As a foundational technology for intelligent human-computer interaction, voice conversion (VC) seeks to transform speech from any source timbre into any target timbre. Traditional voice conversion methods based on Generative Adversarial Networks (GANs) encounter significant challenges in precisely encoding diverse speech elements and effectively synthesising these elements into natural-sounding converted speech. To overcome these limitations, we introduce Pureformer-VC, an encoder-decoder framework that utilizes Conformer blocks to build a disentangled encoder and employs Zipformer blocks to create a style transfer decoder. We adopt a variational decoupled training approach to isolate speech components using a Variational Autoencoder (VAE), complemented by triplet discriminative training to enhance the speaker's discriminative capabilities. Furthermore, we incorporate the Attention Style Transfer Mechanism (ASTM) with Zipformer's shared weights to improve the style transfer performance in the decoder. We conducted experiments on two multi-speaker datasets. The experimental results demonstrate that the proposed model achieves comparable subjective evaluation scores while significantly enhancing objective metrics compared to existing approaches in many-to-many and many-to-one VC scenarios.

</details>

### [Voice Impression Control in Zero-Shot TTS](2506.05688.md)
**Keinichi Fujita et.al.** · 2025-06-09

### [Seeing Voices: Generating A-Roll Video from Audio with Mirage](2506.08279.md)
**Aditi Sundararaman, Amogh Adishesha, Andrew Jaegle, Dan Bigioi et al.** · 2025-06-09

<details>
<summary>Abstract</summary>

From professional filmmaking to user-generated content, creators and consumers have long recognized that the power of video depends on the harmonious integration of what we hear (the video's audio track) with what we see (the video's image sequence). Current approaches to video generation either ignore sound to focus on general-purpose but silent image sequence generation or address both visual and audio elements but focus on restricted application domains such as re-dubbing. We introduce Mirage, an audio-to-video foundation model that excels at generating realistic, expressive output imagery from scratch given an audio input. When integrated with existing methods for speech synthesis (text-to-speech, or TTS), Mirage results in compelling multimodal video. When trained on audio-video footage of people talking (A-roll) and conditioned on audio containing speech, Mirage generates video of people delivering a believable interpretation of the performance implicit in input audio. Our central technical contribution is a unified method for training self-attention-based audio-to-video generation models, either from scratch or given existing weights. This methodology allows Mirage to retain generality as an approach to audio-to-video generation while producing outputs of superior subjective quality to methods that incorporate audio-specific architectures or loss components specific to people, speech, or details of how images or audio are captured. We encourage readers to watch and listen to the results of Mirage for themselves (see paper and comments for links).

</details>

### [In This Environment, As That Speaker: A Text-Driven Framework for Multi-Attribute Speech Conversion](2506.07036.md)
**Jiawei Jin, Zhihan Yang, Yixuan Zhou, Zhiyong Wu** · 2025-06-08

<details>
<summary>Abstract</summary>

We propose TES-VC (Text-driven Environment and Speaker controllable Voice Conversion), a text-driven voice conversion framework with independent control of speaker timbre and environmental acoustics. TES-VC processes simultaneous text inputs for target voice and environment, accurately generating speech matching described timbre/environment while preserving source content. Trained on synthetic data with decoupled vocal/environment features via latent diffusion modeling, our method eliminates interference between attributes. The Retrieval-Based Timbre Control (RBTC) module enables precise manipulation using abstract descriptions without paired data. Experiments confirm TES-VC effectively generates contextually appropriate speech in both timbre and environment with high content retention and superior controllability which demonstrates its potential for widespread applications.

</details>

### [Towards Generalized Source Tracing for Codec-Based Deepfake Speech](2506.07294.md)
**Xuanjun Chen, I-Ming Lin, Lin Zhang, Haibin Wu et al.** · 2025-06-08

<details>
<summary>Abstract</summary>

Recent attempts at source tracing for codec-based deepfake speech (CodecFake), generated by neural audio codec-based speech generation (CoSG) models, have exhibited suboptimal performance. However, how to train source tracing models using simulated CoSG data while maintaining strong performance on real CoSG-generated audio remains an open challenge. In this paper, we show that models trained solely on codec-resynthesized data tend to overfit to non-speech regions and struggle to generalize to unseen content. To mitigate these challenges, we introduce the Semantic-Acoustic Source Tracing Network (SASTNet), which jointly leverages Whisper for semantic feature encoding and Wav2vec2 with AudioMAE for acoustic feature encoding. Our proposed SASTNet achieves state-of-the-art performance on the CoSG test set of the CodecFake+ dataset, demonstrating its effectiveness for reliable source tracing.

</details>

### [SynHate: Detecting Hate Speech in Synthetic Deepfake Audio](2506.06772.md)
**Rishabh Ranjan, Kishan Pipariya, Mayank Vatsa, Richa Singh** · 2025-06-07

<details>
<summary>Abstract</summary>

The rise of deepfake audio and hate speech, powered by advanced text-to-speech, threatens online safety. We present SynHate, the first multilingual dataset for detecting hate speech in synthetic audio, spanning 37 languages. SynHate uses a novel four-class scheme: Real-normal, Real-hate, Fake-normal, and Fake-hate. Built from MuTox and ADIMA datasets, it captures diverse hate speech patterns globally and in India. We evaluate five leading self-supervised models (Whisper-small/medium, XLS-R, AST, mHuBERT), finding notable performance differences by language, with Whisper-small performing best overall. Cross-dataset generalization remains a challenge. By releasing SynHate and baseline code, we aim to advance robust, culturally sensitive, and multilingual solutions against synthetic hate speech. The dataset is available at https://www.iab-rubric.org/resources.

</details>

### [CO-VADA: A Confidence-Oriented Voice Augmentation Debiasing Approach for Fair Speech Emotion Recognition](2506.06071.md)
**Yun-Shao Tsai, Yi-Cheng Lin, Huang-Cheng Chou, Hung-yi Lee** · 2025-06-06

<details>
<summary>Abstract</summary>

Bias in speech emotion recognition (SER) systems often stems from spurious correlations between speaker characteristics and emotional labels, leading to unfair predictions across demographic groups. Many existing debiasing methods require model-specific changes or demographic annotations, limiting their practical use. We present CO-VADA, a Confidence-Oriented Voice Augmentation Debiasing Approach that mitigates bias without modifying model architecture or relying on demographic information. CO-VADA identifies training samples that reflect bias patterns present in the training data and then applies voice conversion to alter irrelevant attributes and generate samples. These augmented samples introduce speaker variations that differ from dominant patterns in the data, guiding the model to focus more on emotion-relevant features. Our framework is compatible with various SER models and voice conversion tools, making it a scalable and practical solution for improving fairness in SER systems.

</details>

### [A Survey of Automatic Evaluation Methods on Text, Visual and Speech Generations](2506.10019.md)
**Tian Lan, Yang-Hao Zhou, Zi-Ao Ma, Fanshu Sun et al.** · 2025-06-06

<details>
<summary>Abstract</summary>

Recent advances in deep learning have significantly enhanced generative AI capabilities across text, images, and audio. However, automatically evaluating the quality of these generated outputs presents ongoing challenges. Although numerous automatic evaluation methods exist, current research lacks a systematic framework that comprehensively organizes these methods across text, visual, and audio modalities. To address this issue, we present a comprehensive review and a unified taxonomy of automatic evaluation methods for generated content across all three modalities; We identify five fundamental paradigms that characterize existing evaluation approaches across these domains. Our analysis begins by examining evaluation methods for text generation, where techniques are most mature. We then extend this framework to image and audio generation, demonstrating its broad applicability. Finally, we discuss promising directions for future research in cross-modal evaluation methodologies.

</details>

### [Audio-Aware Large Language Models as Judges for Speaking Styles](2506.05984.md)
**Cheng-Han Chiang, Xiaofei Wang, Chung-Ching Lin, Kevin Lin et al.** · 2025-06-06

<details>
<summary>Abstract</summary>

Audio-aware large language models (ALLMs) can understand the textual and non-textual information in the audio input. In this paper, we explore using ALLMs as an automatic judge to assess the speaking styles of speeches. We use ALLM judges to evaluate the speeches generated by SLMs on two tasks: voice style instruction following and role-playing. The speaking style we consider includes emotion, volume, speaking pace, word emphasis, pitch control, and non-verbal elements. We use four spoken language models (SLMs) to complete the two tasks and use humans and ALLMs to judge the SLMs' responses. We compare two ALLM judges, GPT-4o-audio and Gemini-2.5-pro, with human evaluation results and show that the agreement between Gemini and human judges is comparable to the agreement between human evaluators. These promising results show that ALLMs can be used as a judge to evaluate SLMs. Our results also reveal that current SLMs, even GPT-4o-audio, still have room for improvement in controlling the speaking style and generating natural dialogues.

</details>

### [Intelligibility of Text-to-Speech Systems for Mathematical Expressions](2506.11086.md)
**Sujoy Roychowdhury, H. G. Ranjani, Sumit Soman, Nishtha Paul et al.** · 2025-06-05

<details>
<summary>Abstract</summary>

There has been limited evaluation of advanced Text-to-Speech (TTS) models with Mathematical eXpressions (MX) as inputs. In this work, we design experiments to evaluate quality and intelligibility of five TTS models through listening and transcribing tests for various categories of MX. We use two Large Language Models (LLMs) to generate English pronunciation from LaTeX MX as TTS models cannot process LaTeX directly. We use Mean Opinion Score from user ratings and quantify intelligibility through transcription correctness using three metrics. We also compare listener preference of TTS outputs with respect to human expert rendition of same MX. Results establish that output of TTS models for MX is not necessarily intelligible, the gap in intelligibility varies across TTS models and MX category. For most categories, performance of TTS models is significantly worse than that of expert rendition. The effect of choice of LLM is limited. This establishes the need to improve TTS models for MX.

</details>

### [Grapheme-Coherent Phonemic and Prosodic Annotation of Speech by Implicit and Explicit Grapheme Conditioning](2506.04527.md)
**Hien Ohnaka, Yuma Shirahata, Byeongseon Park, Ryuichi Yamamoto** · 2025-06-05

<details>
<summary>Abstract</summary>

We propose a model to obtain phonemic and prosodic labels of speech that are coherent with graphemes. Unlike previous methods that simply fine-tune a pre-trained ASR model with the labels, the proposed model conditions the label generation on corresponding graphemes by two methods: 1) Add implicit grapheme conditioning through prompt encoder using pre-trained BERT features. 2) Explicitly prune the label hypotheses inconsistent with the grapheme during inference. These methods enable obtaining parallel data of speech, the labels, and graphemes, which is applicable to various downstream tasks such as text-to-speech and accent estimation from text. Experiments showed that the proposed method significantly improved the consistency between graphemes and the predicted labels. Further, experiments on accent estimation task confirmed that the created parallel data by the proposed method effectively improve the estimation accuracy.

</details>

### [Can we reconstruct a dysarthric voice with the large speech model Parler TTS?](2506.04397.md)
**Ariadna Sanchez et.al.** · 2025-06-04

### [Kinship in Speech: Leveraging Linguistic Relatedness for Zero-Shot TTS in Indian Languages](2506.03884.md)
**Utkarsh Pathak et.al.** · 2025-06-04

### [Comparative Analysis of Fast and High-Fidelity Neural Vocoders for Low-Latency Streaming Synthesis in Resource-Constrained Environments](2506.03554.md)
**Reo Yoneyama et.al.** · 2025-06-04

### [HiFiTTS-2: A Large-Scale High Bandwidth Speech Dataset](2506.04152.md)
**Ryan Langman, Xuesong Yang, Paarth Neekhara, Shehzeen Hussain et al.** · 2025-06-04

<details>
<summary>Abstract</summary>

This paper introduces HiFiTTS-2, a large-scale speech dataset designed for high-bandwidth speech synthesis. The dataset is derived from LibriVox audiobooks, and contains approximately 36.7k hours of English speech for 22.05 kHz training, and 31.7k hours for 44.1 kHz training. We present our data processing pipeline, including bandwidth estimation, segmentation, text preprocessing, and multi-speaker detection. The dataset is accompanied by detailed utterance and audiobook metadata generated by our pipeline, enabling researchers to apply data quality filters to adapt the dataset to various use cases. Experimental results demonstrate that our data pipeline and resulting dataset can facilitate the training of high-quality, zero-shot text-to-speech (TTS) models at high bandwidths.

</details>

### [UniCUE: Unified Recognition and Generation Framework for Chinese Cued Speech Video-to-Speech Generation](2506.04134.md)
**Jinting Wang, Shan Yang, Chenxing Li, Dong Yu et al.** · 2025-06-04

<details>
<summary>Abstract</summary>

Cued Speech (CS) enhances lipreading via hand coding, offering visual phonemic cues that support precise speech perception for the hearing-impaired. The task of CS Video-to-Speech generation (CSV2S) aims to convert CS videos into intelligible speech signals. Most existing research focuses on CS Recognition (CSR), which transcribes video content into text. Consequently, a common solution for CSV2S is to integrate CSR with a text-to-speech (TTS) system. However, this pipeline relies on text as an intermediate medium, which may lead to error propagation and temporal misalignment between speech and CS video dynamics. In contrast, directly generating audio speech from CS video (direct CSV2S) often suffers from the inherent multimodal complexity and the limited availability of CS data. To address these challenges, we propose UniCUE, the first unified framework for CSV2S that directly generates speech from CS videos without relying on intermediate text. The core innovation of UniCUE lies in integrating an understanding task (CSR) that provides fine-grained CS visual-semantic cues to guide speech generation. Specifically, UniCUE incorporates a pose-aware visual processor, a semantic alignment pool that enables precise visual-semantic mapping, and a VisioPhonetic adapter to bridge the understanding and generation tasks within a unified architecture. To support this framework, we construct UniCUE-HI, a large-scale Mandarin CS dataset containing 11282 videos from 14 cuers, including both hearing-impaired and normal-hearing individuals. Extensive experiments on this dataset demonstrate that UniCUE achieves state-of-the-art performance across multiple evaluation metrics.

</details>

### [A Novel Data Augmentation Approach for Automatic Speaking Assessment on Opinion Expressions](2506.04077.md)
**Chung-Chun Wang, Jhen-Ke Lin, Hao-Chien Lu, Hong-Yun Lin et al.** · 2025-06-04

<details>
<summary>Abstract</summary>

Automated speaking assessment (ASA) on opinion expressions is often hampered by the scarcity of labeled recordings, which restricts prompt diversity and undermines scoring reliability. To address this challenge, we propose a novel training paradigm that leverages a large language models (LLM) to generate diverse responses of a given proficiency level, converts responses into synthesized speech via speaker-aware text-to-speech synthesis, and employs a dynamic importance loss to adaptively reweight training instances based on feature distribution differences between synthesized and real speech. Subsequently, a multimodal large language model integrates aligned textual features with speech signals to predict proficiency scores directly. Experiments conducted on the LTTC dataset show that our approach outperforms methods relying on real data or conventional augmentation, effectively mitigating low-resource constraints and enabling ASA on opinion expressions with cross-modal information.

</details>

### [Mark My Words: A Robust Multilingual Model for Punctuation in Text and Speech Transcripts](2506.03793.md)
**Sidharth Pulipaka, Sparsh Jain, Ashwin Sankar, Raj Dabre** · 2025-06-04

<details>
<summary>Abstract</summary>

Punctuation plays a vital role in structuring meaning, yet current models often struggle to restore it accurately in transcripts of spontaneous speech, especially in the presence of disfluencies such as false starts and backtracking. These limitations hinder the performance of downstream tasks like translation, text to speech, summarization, etc. where sentence boundaries are critical for preserving quality. In this work, we introduce Cadence, a generalist punctuation restoration model adapted from a pretrained large language model. Cadence is designed to handle both clean written text and highly spontaneous spoken transcripts. It surpasses the previous state of the art in performance while expanding support from 14 to all 22 Indian languages and English. We conduct a comprehensive analysis of model behavior across punctuation types and language families, identifying persistent challenges under domain shift and with rare punctuation marks. Our findings demonstrate the efficacy of utilizing pretrained language models for multilingual punctuation restoration and highlight Cadence practical value for low resource NLP pipelines at scale.

</details>

### [BitTTS: Highly Compact Text-to-Speech Using 1.58-bit Quantization and Weight Indexing](2506.03515.md)
**Masaya Kawamura, Takuya Hasumi, Yuma Shirahata, Ryuichi Yamamoto** · 2025-06-04

<details>
<summary>Abstract</summary>

This paper proposes a highly compact, lightweight text-to-speech (TTS) model for on-device applications. To reduce the model size, the proposed model introduces two techniques. First, we introduce quantization-aware training (QAT), which quantizes model parameters during training to as low as 1.58-bit. In this case, most of 32-bit model parameters are quantized to ternary values {-1, 0, 1}. Second, we propose a method named weight indexing. In this method, we save a group of 1.58-bit weights as a single int8 index. This allows for efficient storage of model parameters, even on hardware that treats values in units of 8-bit. Experimental results demonstrate that the proposed method achieved 83 % reduction in model size, while outperforming the baseline of similar model size without quantization in synthesis quality.

</details>

### [Towards Better Disentanglement in Non-Autoregressive Zero-Shot Expressive Voice Conversion](2506.04013.md)
**Seymanur Akti, Tuan Nam Nguyen, Alexander Waibel** · 2025-06-04

<details>
<summary>Abstract</summary>

Expressive voice conversion aims to transfer both speaker identity and expressive attributes from a target speech to a given source speech. In this work, we improve over a self-supervised, non-autoregressive framework with a conditional variational autoencoder, focusing on reducing source timbre leakage and improving linguistic-acoustic disentanglement for better style transfer. To minimize style leakage, we use multilingual discrete speech units for content representation and reinforce embeddings with augmentation-based similarity loss and mix-style layer normalization. To enhance expressivity transfer, we incorporate local F0 information via cross-attention and extract style embeddings enriched with global pitch and energy features. Experiments show our model outperforms baselines in emotion and speaker similarity, demonstrating superior style adaptation and reduced source style leakage.

</details>

### [Controllable Text-to-Speech Synthesis with Masked-Autoencoded Style-Rich Representation](2506.02997.md)
**Yongqi Wang et.al.** · 2025-06-03

### [PartialEdit: Identifying Partial Deepfakes in the Era of Neural Speech Editing](2506.02958.md)
**You Zhang et.al.** · 2025-06-03

### [Prompt-Unseen-Emotion: Zero-shot Expressive Speech Synthesis with Prompt-LLM Contextual Knowledge for Mixed Emotions](2506.02742.md)
**Xiaoxue Gao et.al.** · 2025-06-03

### [Towards a Japanese Full-duplex Spoken Dialogue System](2506.02979.md)
**Atsumoto Ohashi, Shinya Iizuka, Jingjing Jiang, Ryuichiro Higashinaka** · 2025-06-03

<details>
<summary>Abstract</summary>

Full-duplex spoken dialogue systems, which can model simultaneous bidirectional features of human conversations such as speech overlaps and backchannels, have attracted significant attention recently. However, the study of full-duplex spoken dialogue systems for the Japanese language has been limited, and the research on their development in Japanese remains scarce. In this paper, we present the first publicly available full-duplex spoken dialogue model in Japanese, which is built upon Moshi, a full-duplex dialogue model in English. Our model is trained through a two-stage process: pre-training on a large-scale spoken dialogue data in Japanese, followed by fine-tuning on high-quality stereo spoken dialogue data. We further enhance the model's performance by incorporating synthetic dialogue data generated by a multi-stream text-to-speech system. Evaluation experiments demonstrate that the trained model outperforms Japanese baseline models in both naturalness and meaningfulness.

</details>

### [CapSpeech: Enabling Downstream Applications in Style-Captioned Text-to-Speech](2506.02863.md)
**Helin Wang, Jiarui Hai, Dading Chong, Karan Thakkar et al.** · 2025-06-03

<details>
<summary>Abstract</summary>

Recent advancements in generative artificial intelligence have significantly transformed the field of style-captioned text-to-speech synthesis (CapTTS). However, adapting CapTTS to real-world applications remains challenging due to the lack of standardized, comprehensive datasets and limited research on downstream tasks built upon CapTTS. To address these gaps, we introduce CapSpeech, a new benchmark designed for a series of CapTTS-related tasks, including style-captioned text-to-speech synthesis with sound events (CapTTS-SE), accent-captioned TTS (AccCapTTS), emotion-captioned TTS (EmoCapTTS), and text-to-speech synthesis for chat agent (AgentTTS). CapSpeech comprises over 10 million machine-annotated audio-caption pairs and nearly 0.36 million human-annotated audio-caption pairs. In addition, we introduce two new datasets collected and recorded by a professional voice actor and experienced audio engineers, specifically for the AgentTTS and CapTTS-SE tasks. Alongside the datasets, we conduct comprehensive experiments using both autoregressive and non-autoregressive models on CapSpeech. Our results demonstrate high-fidelity and highly intelligible speech synthesis across a diverse range of speaking styles. To the best of our knowledge, CapSpeech is the largest available dataset offering comprehensive annotations for CapTTS-related tasks. The experiments and findings further provide valuable insights into the challenges of developing CapTTS systems.

</details>

### [StarVC: A Unified Auto-Regressive Framework for Joint Text and Speech Generation in Voice Conversion](2506.02414.md)
**Fengjin Li, Jie Wang, Yadong Niu, Yongqing Wang et al.** · 2025-06-03

<details>
<summary>Abstract</summary>

Voice Conversion (VC) modifies speech to match a target speaker while preserving linguistic content. Traditional methods usually extract speaker information directly from speech while neglecting the explicit utilization of linguistic content. Since VC fundamentally involves disentangling speaker identity from linguistic content, leveraging structured semantic features could enhance conversion performance. However, previous attempts to incorporate semantic features into VC have shown limited effectiveness, motivating the integration of explicit text modeling. We propose StarVC, a unified autoregressive VC framework that first predicts text tokens before synthesizing acoustic features. The experiments demonstrate that StarVC outperforms conventional VC methods in preserving both linguistic content (i.e., WER and CER) and speaker characteristics (i.e., SECS and MOS). Audio demo can be found at: https://thuhcsi.github.io/StarVC/.

</details>

### [Trusted Fake Audio Detection Based on Dirichlet Distribution](2506.02401.md)
**Chi Ding, Junxiao Xue, Cong Wang, Hao Zhou** · 2025-06-03

<details>
<summary>Abstract</summary>

With the continuous development of deep learning-based speech conversion and speech synthesis technologies, the cybersecurity problem posed by fake audio has become increasingly serious. Previously proposed models for defending against fake audio have attained remarkable performance. However, they all fall short in modeling the trustworthiness of the decisions made by the models themselves. Based on this, we put forward a plausible fake audio detection approach based on the Dirichlet distribution with the aim of enhancing the reliability of fake audio detection. Specifically, we first generate evidence through a neural network. Uncertainty is then modeled using the Dirichlet distribution. By modeling the belief distribution with the parameters of the Dirichlet distribution, an estimate of uncertainty can be obtained for each decision. Finally, the predicted probabilities and corresponding uncertainty estimates are combined to form the final opinion. On the ASVspoof series dataset (i.e., ASVspoof 2019 LA, ASVspoof 2021 LA, and DF), we conduct a number of comparison experiments to verify the excellent performance of the proposed model in terms of accuracy, robustness, and trustworthiness.

</details>

### [SingaKids: A Multilingual Multimodal Dialogic Tutor for Language Learning](2506.02412.md)
**Zhengyuan Liu, Geyu Lin, Hui Li Tan, Huayun Zhang et al.** · 2025-06-03

<details>
<summary>Abstract</summary>

The integration of generative artificial intelligence into educational applications has enhanced personalized and interactive learning experiences, and it shows strong potential to promote young learners language acquisition. However, it is still challenging to ensure consistent and robust performance across different languages and cultural contexts, and kids-friendly design requires simplified instructions, engaging interactions, and age-appropriate scaffolding to maintain motivation and optimize learning outcomes. In this work, we introduce SingaKids, a dialogic tutor designed to facilitate language learning through picture description tasks. Our system integrates dense image captioning, multilingual dialogic interaction, speech understanding, and engaging speech generation to create an immersive learning environment in four languages: English, Mandarin, Malay, and Tamil. We further improve the system through multilingual pre-training, task-specific tuning, and scaffolding optimization. Empirical studies with elementary school students demonstrate that SingaKids provides effective dialogic teaching, benefiting learners at different performance levels.

</details>

### [Zero-Shot Text-to-Speech for Vietnamese](2506.01322.md)
**Thi Vu et.al.** · 2025-06-02

### [Zero-Shot Streaming Text to Speech Synthesis with Transducer and Auto-Regressive Modeling](2505.19669.md)
**Haiyang Sun et.al.** · 2025-06-02

### [SALF-MOS: Speaker Agnostic Latent Features Downsampled for MOS Prediction](2506.02082.md)
**Saurabh Agrawal, Raj Gohil, Gopal Kumar Agrawal, Vikram C M et al.** · 2025-06-02

<details>
<summary>Abstract</summary>

Speech quality assessment is a critical process in selecting text-to-speech synthesis (TTS) or voice conversion models. Evaluation of voice synthesis can be done using objective metrics or subjective metrics. Although there are many objective metrics like the Perceptual Evaluation of Speech Quality (PESQ), Perceptual Objective Listening Quality Assessment (POLQA) or Short-Time Objective Intelligibility (STOI) but none of them is feasible in selecting the best model. On the other hand subjective metric like Mean Opinion Score is highly reliable but it requires a lot of manual efforts and are time-consuming. To counter the issues in MOS Evaluation, we have developed a novel model, Speaker Agnostic Latent Features (SALF)-Mean Opinion Score (MOS) which is a small-sized, end-to-end, highly generalized and scalable model for predicting MOS score on a scale of 5. We use the sequences of convolutions and stack them to get the latent features of the audio samples to get the best state-of-the-art results based on mean squared error (MSE), Linear Concordance Correlation coefficient (LCC), Spearman Rank Correlation Coefficient (SRCC) and Kendall Rank Correlation Coefficient (KTAU).

</details>

### [LinearVC: Linear transformations of self-supervised features through the lens of voice conversion](2506.01510.md)
**Herman Kamper, Benjamin van Niekerk, Julian Zaïdi, Marc-André Carbonneau** · 2025-06-02

<details>
<summary>Abstract</summary>

We introduce LinearVC, a simple voice conversion method that sheds light on the structure of self-supervised representations. First, we show that simple linear transformations of self-supervised features effectively convert voices. Next, we probe the geometry of the feature space by constraining the set of allowed transformations. We find that just rotating the features is sufficient for high-quality voice conversion. This suggests that content information is embedded in a low-dimensional subspace which can be linearly transformed to produce a target voice. To validate this hypothesis, we finally propose a method that explicitly factorizes content and speaker information using singular value decomposition; the resulting linear projection with a rank of just 100 gives competitive conversion results. Our work has implications for both practical voice conversion and a broader understanding of self-supervised speech representations. Samples and code: https://www.kamperh.com/linearvc/.

</details>

### [Dhvani: A Weakly-supervised Phonemic Error Detection and Personalized Feedback System for Hindi](2506.02166.md)
**Arnav Rustagi, Satvik Bajpai, Nimrat Kaur, Siddharth Siddharth** · 2025-06-02

<details>
<summary>Abstract</summary>

Computer-Assisted Pronunciation Training (CAPT) has been extensively studied for English. However, there remains a critical gap in its application to Indian languages with a base of 1.5 billion speakers. Pronunciation tools tailored to Indian languages are strikingly lacking despite the fact that millions learn them every year. With over 600 million speakers and being the fourth most-spoken language worldwide, improving Hindi pronunciation is a vital first step toward addressing this gap. This paper proposes 1) Dhvani -- a novel CAPT system for Hindi, 2) synthetic speech generation for Hindi mispronunciations, and 3) a novel methodology for providing personalized feedback to learners. While the system often interacts with learners using Devanagari graphemes, its core analysis targets phonemic distinctions, leveraging Hindi's highly phonetic orthography to analyze mispronounced speech and provide targeted feedback.

</details>

### [Universal Preference-Score-based Pairwise Speech Quality Assessment](2506.01455.md)
**Yu-Fei Shi, Yang Ai, Zhen-Hua Ling** · 2025-06-02

<details>
<summary>Abstract</summary>

To compare the performance of two speech generation systems, one of the most effective approaches is estimating the preference score between their generated speech. This paper proposes a novel universal preference-score-based pairwise speech quality assessment (UPPSQA) model, aimed at predicting the preference score between paired speech samples to determine which one has better quality. The model first predicts the absolute mean opinion score (MOS) for the two speech samples separately, and then aggregates them into a relative preference score using a preference function. To address the scarcity of preference data, we also construct a new pairwise speech dataset based on a MOS dataset for experiments. Experimental results confirm that, whether in training scenarios with different data types and label conditions, or in both in-domain and out-of-domain test scenarios, the prediction accuracy of UPP-SQA outperforms that of the baseline models, demonstrating its universality.

</details>

### [DS-TTS: Zero-Shot Speaker Style Adaptation from Voice Clips via Dynamic Dual-Style Feature Modulation](2506.01020.md)
**Ming Meng et.al.** · 2025-06-01

### [Rhythm Controllable and Efficient Zero-Shot Voice Conversion via Shortcut Flow Matching](2506.01014.md)
**Jialong Zuo et.al.** · 2025-06-01

### [Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models](2506.00832.md)
**Kyowoon Lee, Artyom Stitsyuk, Gunu Jho, Inchul Hwang et al.** · 2025-06-01

<details>
<summary>Abstract</summary>

Recent advances in Text-to-Speech (TTS) have significantly improved speech naturalness, increasing the demand for precise prosody control and mispronunciation correction. Existing approaches for prosody manipulation often depend on specialized modules or additional training, limiting their capacity for post-hoc adjustments. Similarly, traditional mispronunciation correction relies on grapheme-to-phoneme dictionaries, making it less practical in low-resource settings. We introduce Counterfactual Activation Editing, a model-agnostic method that manipulates internal representations in a pre-trained TTS model to achieve post-hoc control of prosody and pronunciation. Experimental results show that our method effectively adjusts prosodic features and corrects mispronunciations while preserving synthesis quality. This opens the door to inference-time refinement of TTS outputs without retraining, bridging the gap between pre-trained TTS models and editable speech synthesis.

</details>

### [PseudoVC: Improving One-shot Voice Conversion with Pseudo Paired Data](2506.01039.md)
**Songjun Cao, Qinghua Wu, Jie Chen, Jin Li et al.** · 2025-06-01

<details>
<summary>Abstract</summary>

As parallel training data is scarce for one-shot voice conversion (VC) tasks, waveform reconstruction is typically performed by various VC systems. A typical one-shot VC system comprises a content encoder and a speaker encoder. However, two types of mismatches arise: one for the inputs to the content encoder during training and inference, and another for the inputs to the speaker encoder. To address these mismatches, we propose a novel VC training method called \textit{PseudoVC} in this paper. First, we introduce an innovative information perturbation approach named \textit{Pseudo Conversion} to tackle the first mismatch problem. This approach leverages pretrained VC models to convert the source utterance into a perturbed utterance, which is fed into the content encoder during training. Second, we propose an approach termed \textit{Speaker Sampling} to resolve the second mismatch problem, which will substitute the input to the speaker encoder by another utterance from the same speaker during training. Experimental results demonstrate that our proposed \textit{Pseudo Conversion} outperforms previous information perturbation methods, and the overall \textit{PseudoVC} method surpasses publicly available VC models. Audio examples are available.

</details>

### [ReFlow-VC: Zero-shot Voice Conversion Based on Rectified Flow and Speaker Feature Optimization](2506.01032.md)
**Pengyu Ren, Wenhao Guan, Kaidi Wang, Peijie Chen et al.** · 2025-06-01

<details>
<summary>Abstract</summary>

In recent years, diffusion-based generative models have demonstrated remarkable performance in speech conversion, including Denoising Diffusion Probabilistic Models (DDPM) and others. However, the advantages of these models come at the cost of requiring a large number of sampling steps. This limitation hinders their practical application in real-world scenarios. In this paper, we introduce ReFlow-VC, a novel high-fidelity speech conversion method based on rectified flow. Specifically, ReFlow-VC is an Ordinary Differential Equation (ODE) model that transforms a Gaussian distribution to the true Mel-spectrogram distribution along the most direct path. Furthermore, we propose a modeling approach that optimizes speaker features by utilizing both content and pitch information, allowing speaker features to reflect the properties of the current speech more accurately. Experimental results show that ReFlow-VC performs exceptionally well in small datasets and zero-shot scenarios.

</details>

### [CoVoMix2: Advancing Zero-Shot Dialogue Generation with Fully Non-Autoregressive Flow Matching](2506.00885.md)
**Leying Zhang, Yao Qian, Xiaofei Wang, Manthan Thakker et al.** · 2025-06-01

<details>
<summary>Abstract</summary>

Generating natural-sounding, multi-speaker dialogue is crucial for applications such as podcast creation, virtual agents, and multimedia content generation. However, existing systems struggle to maintain speaker consistency, model overlapping speech, and synthesize coherent conversations efficiently. In this paper, we introduce CoVoMix2, a fully non-autoregressive framework for zero-shot multi-talker dialogue generation. CoVoMix2 directly predicts mel-spectrograms from multi-stream transcriptions using a flow-matching-based generative model, eliminating the reliance on intermediate token representations. To better capture realistic conversational dynamics, we propose transcription-level speaker disentanglement, sentence-level alignment, and prompt-level random masking strategies. Our approach achieves state-of-the-art performance, outperforming strong baselines like MoonCast and Sesame in speech quality, speaker consistency, and inference speed. Notably, CoVoMix2 operates without requiring transcriptions for the prompt and supports controllable dialogue generation, including overlapping speech and precise timing control, demonstrating strong generalizability to real-world speech generation scenarios.

</details>

### [Speech Token Prediction via Compressed-to-fine Language Modeling for Speech Generation](2505.24496.md)
**Wenrui Liu et.al.** · 2025-05-30

### [DS-Codec: Dual-Stage Training with Mirror-to-NonMirror Architecture Switching for Speech Codec](2505.24314.md)
**Peijie Chen et.al.** · 2025-05-30

### [Accelerating Diffusion-based Text-to-Speech Model Training with Dual Modality Alignment](2505.19595.md)
**Jeongsoo Choi et.al.** · 2025-05-30

### [Verbal Werewolf: Engage Users with Verbalized Agentic Werewolf Game Framework](2506.00160.md)
**Qihui Fan, Wenbo Li, Enfu Nan, Yixiao Chen et al.** · 2025-05-30

<details>
<summary>Abstract</summary>

The growing popularity of social deduction games has created an increasing need for intelligent frameworks where humans can collaborate with AI agents, particularly in post-pandemic contexts with heightened psychological and social pressures. Social deduction games like Werewolf, traditionally played through verbal communication, present an ideal application for Large Language Models (LLMs) given their advanced reasoning and conversational capabilities. Prior studies have shown that LLMs can outperform humans in Werewolf games, but their reliance on external modules introduces latency that left their contribution in academic domain only, and omit such game should be user-facing. We propose \textbf{Verbal Werewolf}, a novel LLM-based Werewolf game system that optimizes two parallel pipelines: gameplay powered by state-of-the-art LLMs and a fine-tuned Text-to-Speech (TTS) module that brings text output to life. Our system operates in near real-time without external decision-making modules, leveraging the enhanced reasoning capabilities of modern LLMs like DeepSeek V3 to create a more engaging and anthropomorphic gaming experience that significantly improves user engagement compared to existing text-only frameworks.

</details>

### [Voice Conversion Improves Cross-Domain Robustness for Spoken Arabic Dialect Identification](2505.24713.md)
**Badr M. Abdullah, Matthew Baas, Bernd Möbius, Dietrich Klakow** · 2025-05-30

<details>
<summary>Abstract</summary>

Arabic dialect identification (ADI) systems are essential for large-scale data collection pipelines that enable the development of inclusive speech technologies for Arabic language varieties. However, the reliability of current ADI systems is limited by poor generalization to out-of-domain speech. In this paper, we present an effective approach based on voice conversion for training ADI models that achieves state-of-the-art performance and significantly improves robustness in cross-domain scenarios. Evaluated on a newly collected real-world test set spanning four different domains, our approach yields consistent improvements of up to +34.1% in accuracy across domains. Furthermore, we present an analysis of our approach and demonstrate that voice conversion helps mitigate the speaker bias in the ADI dataset. We release our robust ADI model and cross-domain evaluation dataset to support the development of inclusive speech technologies for Arabic.

</details>

### [When Humans Growl and Birds Speak: High-Fidelity Voice Conversion from Human to Animal and Designed Sounds](2505.24336.md)
**Minsu Kang, Seolhee Lee, Choonghyeon Lee, Namhyun Cho** · 2025-05-30

<details>
<summary>Abstract</summary>

Human to non-human voice conversion (H2NH-VC) transforms human speech into animal or designed vocalizations. Unlike prior studies focused on dog-sounds and 16 or 22.05kHz audio transformation, this work addresses a broader range of non-speech sounds, including natural sounds (lion-roars, birdsongs) and designed voice (synthetic growls). To accomodate generation of diverse non-speech sounds and 44.1kHz high-quality audio transformation, we introduce a preprocessing pipeline and an improved CVAE-based H2NH-VC model, both optimized for human and non-human voices. Experimental results showed that the proposed method outperformed baselines in quality, naturalness, and similarity MOS, achieving effective voice conversion across diverse non-human timbres. Demo samples are available at https://nc-ai.github.io/speech/publications/nonhuman-vc/

</details>

### [A Perception-Based L2 Speech Intelligibility Indicator: Leveraging a Rater's Shadowing and Sequence-to-sequence Voice Conversion](2505.24304.md)
**Haopeng Geng, Daisuke Saito, Nobuaki Minematsu** · 2025-05-30

<details>
<summary>Abstract</summary>

Evaluating L2 speech intelligibility is crucial for effective computer-assisted language learning (CALL). Conventional ASR-based methods often focus on native-likeness, which may fail to capture the actual intelligibility perceived by human listeners. In contrast, our work introduces a novel, perception based L2 speech intelligibility indicator that leverages a native rater's shadowing data within a sequence-to-sequence (seq2seq) voice conversion framework. By integrating an alignment mechanism and acoustic feature reconstruction, our approach simulates the auditory perception of native listeners, identifying segments in L2 speech that are likely to cause comprehension difficulties. Both objective and subjective evaluations indicate that our method aligns more closely with native judgments than traditional ASR-based metrics, offering a promising new direction for CALL systems in a global, multilingual contexts.

</details>

### [Discl-VC: Disentangled Discrete Tokens and In-Context Learning for Controllable Zero-Shot Voice Conversion](2505.24291.md)
**Kaidi Wang, Wenhao Guan, Ziyue Jiang, Hukai Huang et al.** · 2025-05-30

<details>
<summary>Abstract</summary>

Currently, zero-shot voice conversion systems are capable of synthesizing the voice of unseen speakers. However, most existing approaches struggle to accurately replicate the speaking style of the source speaker or mimic the distinctive speaking style of the target speaker, thereby limiting the controllability of voice conversion. In this work, we propose Discl-VC, a novel voice conversion framework that disentangles content and prosody information from self-supervised speech representations and synthesizes the target speaker's voice through in-context learning with a flow matching transformer. To enable precise control over the prosody of generated speech, we introduce a mask generative transformer that predicts discrete prosody tokens in a non-autoregressive manner based on prompts. Experimental results demonstrate the superior performance of Discl-VC in zero-shot voice conversion and its remarkable accuracy in prosody control for synthesized speech.

</details>

### [ARECHO: Autoregressive Evaluation via Chain-Based Hypothesis Optimization for Speech Multi-Metric Estimation](2505.24518.md)
**Jiatong Shi, Yifan Cheng, Bo-Hao Su, Hye-jin Shim et al.** · 2025-05-30

<details>
<summary>Abstract</summary>

Speech signal analysis poses significant challenges, particularly in tasks such as speech quality evaluation and profiling, where the goal is to predict multiple perceptual and objective metrics. For instance, metrics like PESQ (Perceptual Evaluation of Speech Quality), STOI (Short-Time Objective Intelligibility), and MOS (Mean Opinion Score) each capture different aspects of speech quality. However, these metrics often have different scales, assumptions, and dependencies, making joint estimation non-trivial. To address these issues, we introduce ARECHO (Autoregressive Evaluation via Chain-based Hypothesis Optimization), a chain-based, versatile evaluation system for speech assessment grounded in autoregressive dependency modeling. ARECHO is distinguished by three key innovations: (1) a comprehensive speech information tokenization pipeline; (2) a dynamic classifier chain that explicitly captures inter-metric dependencies; and (3) a two-step confidence-oriented decoding algorithm that enhances inference reliability. Experiments demonstrate that ARECHO significantly outperforms the baseline framework across diverse evaluation scenarios, including enhanced speech analysis, speech generation evaluation, and, noisy speech evaluation. Furthermore, its dynamic dependency modeling improves interpretability by capturing inter-metric relationships. Across tasks, ARECHO offers reference-free evaluation using its dynamic classifier chain to support subset queries (single or multiple metrics) and reduces error propagation via confidence-oriented decoding.

</details>

### [Can Emotion Fool Anti-spoofing?](2505.23962.md)
**Aurosweta Mahapatra, Ismail Rasim Ulgen, Abinay Reddy Naini, Carlos Busso et al.** · 2025-05-29

<details>
<summary>Abstract</summary>

Traditional anti-spoofing focuses on models and datasets built on synthetic speech with mostly neutral state, neglecting diverse emotional variations. As a result, their robustness against high-quality, emotionally expressive synthetic speech is uncertain. We address this by introducing EmoSpoof-TTS, a corpus of emotional text-to-speech samples. Our analysis shows existing anti-spoofing models struggle with emotional synthetic speech, exposing risks of emotion-targeted attacks. Even trained on emotional data, the models underperform due to limited focus on emotional aspect and show performance disparities across emotions. This highlights the need for emotion-focused anti-spoofing paradigm in both dataset and methodology. We propose GEM, a gated ensemble of emotion-specialized models with a speech emotion recognition gating network. GEM performs effectively across all emotions and neutral state, improving defenses against spoofing attacks. We release the EmoSpoof-TTS Dataset: https://emospoof-tts.github.io/Dataset/

</details>

### [Few-Shot Speech Deepfake Detection Adaptation with Gaussian Processes](2505.23619.md)
**Neta Glazer, David Chernin, Idan Achituve, Sharon Gannot et al.** · 2025-05-29

<details>
<summary>Abstract</summary>

Recent advancements in Text-to-Speech (TTS) models, particularly in voice cloning, have intensified the demand for adaptable and efficient deepfake detection methods. As TTS systems continue to evolve, detection models must be able to efficiently adapt to previously unseen generation models with minimal data. This paper introduces ADD-GP, a few-shot adaptive framework based on a Gaussian Process (GP) classifier for Audio Deepfake Detection (ADD). We show how the combination of a powerful deep embedding model with the Gaussian processes flexibility can achieve strong performance and adaptability. Additionally, we show this approach can also be used for personalized detection, with greater robustness to new TTS models and one-shot adaptability. To support our evaluation, a benchmark dataset is constructed for this task using new state-of-the-art voice cloning models.

</details>

### [EmergentTTS-Eval: Evaluating TTS Models on Complex Prosodic, Expressiveness, and Linguistic Challenges Using Model-as-a-Judge](2505.23009.md)
**Ruskin Raj Manku, Yuzhi Tang, Xingjian Shi, Mu Li et al.** · 2025-05-29

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) benchmarks often fail to capture how well models handle nuanced and semantically complex text. Building on $\textit{EmergentTTS}$, we introduce $\textit{EmergentTTS-Eval}$, a comprehensive benchmark covering six challenging TTS scenarios: emotions, paralinguistics, foreign words, syntactic complexity, complex pronunciation (e.g. URLs, formulas), and questions. Crucially, our framework automates both test-case generation and evaluation, making the benchmark easily extensible. Starting from a small set of human-written seed prompts, we iteratively extend them using LLMs to target specific structural, phonetic and prosodic challenges, resulting in 1,645 diverse test cases. Moreover, we employ a model-as-a-judge approach, using a Large Audio Language Model (LALM) to assess the speech across multiple dimensions such as expressed emotion, prosodic, intonational, and pronunciation accuracy. We evaluate state-of-the-art open-source and proprietary TTS systems, such as 11Labs, Deepgram, and OpenAI's 4o-mini-TTS, on EmergentTTS-Eval, demonstrating its ability to reveal fine-grained performance differences. Results show that the model-as-a-judge approach offers robust TTS assessment and a high correlation with human preferences. We open source the evaluation $\href{https://github.com/boson-ai/EmergentTTS-Eval-public}{code}$ and the $\href{https://huggingface.co/datasets/bosonai/EmergentTTS-Eval}{dataset}$.

</details>

### [LLM-Synth4KWS: Scalable Automatic Generation and Synthesis of Confusable Data for Custom Keyword Spotting](2505.22995.md)
**Pai Zhu, Quan Wang, Dhruuv Agarwal, Kurt Partridge** · 2025-05-29

<details>
<summary>Abstract</summary>

Custom keyword spotting (KWS) allows detecting user-defined spoken keywords from streaming audio. This is achieved by comparing the embeddings from voice enrollments and input audio. State-of-the-art custom KWS models are typically trained contrastively using utterances whose keywords are randomly sampled from training dataset. These KWS models often struggle with confusing keywords, such as "blue" versus "glue". This paper introduces an effective way to augment the training with confusable utterances where keywords are generated and grouped from large language models (LLMs), and speech signals are synthesized with diverse speaking styles from text-to-speech (TTS) engines. To better measure user experience on confusable KWS, we define a new northstar metric using the average area under DET curve from confusable groups (c-AUC). Featuring high scalability and zero labor cost, the proposed method improves AUC by 3.7% and c-AUC by 11.3% on the Speech Commands testing set.

</details>

### [Spoken question answering for visual queries](2505.23308.md)
**Nimrod Shabtay, Zvi Kons, Avihu Dekel, Hagai Aronowitz et al.** · 2025-05-29

<details>
<summary>Abstract</summary>

Question answering (QA) systems are designed to answer natural language questions. Visual QA (VQA) and Spoken QA (SQA) systems extend the textual QA system to accept visual and spoken input respectively. This work aims to create a system that enables user interaction through both speech and images. That is achieved through the fusion of text, speech, and image modalities to tackle the task of spoken VQA (SVQA). The resulting multi-modal model has textual, visual, and spoken inputs and can answer spoken questions on images. Training and evaluating SVQA models requires a dataset for all three modalities, but no such dataset currently exists. We address this problem by synthesizing VQA datasets using two zero-shot TTS models. Our initial findings indicate that a model trained only with synthesized speech nearly reaches the performance of the upper-bounding model trained on textual QAs. In addition, we show that the choice of the TTS model has a minor impact on accuracy.

</details>

### [SpeakBraille:Revolutionizing Braille with Speech Synthesis](s2:3e758b1ca5da92e30f74cdc783eb0a2144116b9e.md)
**Anitha Vasam, M. Nikitha, Dikonda Pavanikalyani** · 2025-05-29

<details>
<summary>Abstract</summary>

In an era of increasing technological advancement, accessibility remains a paramount concern. This project presents a robust and innovative solution for the visually impaired by harnessing the power of computer vision to seamlessly convert Braille into text and voice. The Braille to Text and Voice Conversion System (BTVCS) serves as a transformative tool that bridges the gap between tactile and auditory communication, empowering individuals with visual impairments to access written information independently. The core of the system lies in its ability to accurately recognize Braille characters through image processing and computer vision techniques. Utilizing state-of-the-art machine learning algorithms and deep neural networks, BTVCS interprets Braille patterns with precision, ensuring minimal error rates. The extracted Braille text is then seamlessly converted into natural language text, opening up a world of printed content to the visually impaired. Additionally, BTVCS features a robust text to- speech (TTS) engine that transforms the converted text into high quality, natural-sounding voice output. Users can select from a range of voices and settings to personalize their experience. This dynamic TTS capability extends beyond mere translation; it provides an immersive auditory experience that conveys tone, context, and emotion, making the content more engaging and informative

</details>

### [BinauralFlow: A Causal and Streamable Approach for High-Quality Binaural Speech Synthesis with Flow Matching Models](2505.22865.md)
**Susan Liang et.al.** · 2025-05-28

### [Tell me Habibi, is it Real or Fake?](2505.22581.md)
**Kartik Kuckreja, Parul Gupta, Injy Hamed, Thamar Solorio et al.** · 2025-05-28

<details>
<summary>Abstract</summary>

Deepfake generation methods are evolving fast, making fake media harder to detect and raising serious societal concerns. Most deepfake detection and dataset creation research focuses on monolingual content, often overlooking the challenges of multilingual and code-switched speech, where multiple languages are mixed within the same discourse. Code-switching, especially between Arabic and English, is common in the Arab world and is widely used in digital communication. This linguistic mixing poses extra challenges for deepfake detection, as it can confuse models trained mostly on monolingual data. To address this, we introduce \textbf{ArEnAV}, the first large-scale Arabic-English audio-visual deepfake dataset featuring intra-utterance code-switching, dialectal variation, and monolingual Arabic content. It \textbf{contains 387k videos and over 765 hours of real and fake videos}. Our dataset is generated using a novel pipeline integrating four Text-To-Speech and two lip-sync models, enabling comprehensive analysis of multilingual multimodal deepfake detection. We benchmark our dataset against existing monolingual and multilingual datasets, state-of-the-art deepfake detection models, and a human evaluation, highlighting its potential to advance deepfake research. The dataset can be accessed \href{https://huggingface.co/datasets/kartik060702/ArEnAV-Full}{here}.

</details>

### [A Linguistically Motivated Analysis of Intonational Phrasing in Text-to-Speech Systems: Revealing Gaps in Syntactic Sensitivity](2505.22236.md)
**Charlotte Pouw, Afra Alishahi, Willem Zuidema** · 2025-05-28

<details>
<summary>Abstract</summary>

We analyze the syntactic sensitivity of Text-to-Speech (TTS) systems using methods inspired by psycholinguistic research. Specifically, we focus on the generation of intonational phrase boundaries, which can often be predicted by identifying syntactic boundaries within a sentence. We find that TTS systems struggle to accurately generate intonational phrase boundaries in sentences where syntactic boundaries are ambiguous (e.g., garden path sentences or sentences with attachment ambiguity). In these cases, systems need superficial cues such as commas to place boundaries at the correct positions. In contrast, for sentences with simpler syntactic structures, we find that systems do incorporate syntactic cues beyond surface markers. Finally, we finetune models on sentences without commas at the syntactic boundary positions, encouraging them to focus on more subtle linguistic cues. Our findings indicate that this leads to more distinct intonation patterns that better reflect the underlying structure.

</details>

### [Speaking images. A novel framework for the automated self-description of artworks](2506.05368.md)
**Valentine Bernasconi, Gustavo Marfia** · 2025-05-28

<details>
<summary>Abstract</summary>

Recent breakthroughs in generative AI have opened the door to new research perspectives in the domain of art and cultural heritage, where a large number of artifacts have been digitized. There is a need for innovation to ease the access and highlight the content of digital collections. Such innovations develop into creative explorations of the digital image in relation to its malleability and contemporary interpretation, in confrontation to the original historical object. Based on the concept of the autonomous image, we propose a new framework towards the production of self-explaining cultural artifacts using open-source large-language, face detection, text-to-speech and audio-to-animation models. The goal is to start from a digitized artwork and to automatically assemble a short video of the latter where the main character animates to explain its content. The whole process questions cultural biases encapsulated in large-language models, the potential of digital images and deepfakes of artworks for educational purposes, along with concerns of the field of art history regarding such creative diversions.

</details>

### [ACE-Step: A Step Towards Music Generation Foundation Model](2506.00045.md)
**Junmin Gong, Sean Zhao, Sen Wang, Shengyuan Xu et al.** · 2025-05-28

<details>
<summary>Abstract</summary>

We introduce ACE-Step, a novel open-source foundation model for music generation that overcomes key limitations of existing approaches and achieves state-of-the-art performance through a holistic architectural design. Current methods face inherent trade-offs between generation speed, musical coherence, and controllability. For example, LLM-based models (e.g. Yue, SongGen) excel at lyric alignment but suffer from slow inference and structural artifacts. Diffusion models (e.g. DiffRhythm), on the other hand, enable faster synthesis but often lack long-range structural coherence. ACE-Step bridges this gap by integrating diffusion-based generation with Sana's Deep Compression AutoEncoder (DCAE) and a lightweight linear transformer. It also leverages MERT and m-hubert to align semantic representations (REPA) during training, allowing rapid convergence. As a result, our model synthesizes up to 4 minutes of music in just 20 seconds on an A100 GPU-15x faster than LLM-based baselines-while achieving superior musical coherence and lyric alignment across melody, harmony, and rhythm metrics. Moreover, ACE-Step preserves fine-grained acoustic details, enabling advanced control mechanisms such as voice cloning, lyric editing, remixing, and track generation (e.g. lyric2vocal, singing2accompaniment). Rather than building yet another end-to-end text-to-music pipeline, our vision is to establish a foundation model for music AI: a fast, general-purpose, efficient yet flexible architecture that makes it easy to train subtasks on top of it. This paves the way for the development of powerful tools that seamlessly integrate into the creative workflows of music artists, producers, and content creators. In short, our goal is to build a stable diffusion moment for music. The code, the model weights and the demo are available at: https://ace-step.github.io/.

</details>

### [Voice Adaptation for Swiss German](2505.22054.md)
**Samuel Stucki, Jan Deriu, Mark Cieliebak** · 2025-05-28

<details>
<summary>Abstract</summary>

This work investigates the performance of Voice Adaptation models for Swiss German dialects, i.e., translating Standard German text to Swiss German dialect speech. For this, we preprocess a large dataset of Swiss podcasts, which we automatically transcribe and annotate with dialect classes, yielding approximately 5000 hours of weakly labeled training material. We fine-tune the XTTSv2 model on this dataset and show that it achieves good scores in human and automated evaluations and can correctly render the desired dialect. Our work shows a step towards adapting Voice Cloning technology to underrepresented languages. The resulting model achieves CMOS scores of up to -0.28 and SMOS scores of 3.8.

</details>

### [CosyVoice 3: Towards In-the-wild Speech Generation via Scaling-up and Post-training](2505.17589.md)
**Zhihao Du et.al.** · 2025-05-27

### [OmniResponse: Online Multimodal Conversational Response Generation in Dyadic Interactions](2505.21724.md)
**Cheng Luo, Jianghui Wang, Bing Li, Siyang Song et al.** · 2025-05-27

<details>
<summary>Abstract</summary>

In this paper, we introduce Online Multimodal Conversational Response Generation (OMCRG), a novel task designed to produce synchronized verbal and non-verbal listener feedback online, based on the speaker's multimodal inputs. OMCRG captures natural dyadic interactions and introduces new challenges in aligning generated audio with listeners' facial responses. To tackle these challenges, we incorporate text as an intermediate modality to connect audio and facial responses. We propose OmniResponse, a Multimodal Large Language Model (MLLM) that autoregressively generates accurate multimodal listener responses. OmniResponse leverages a pretrained LLM enhanced with two core components: Chrono-Text Markup, which precisely timestamps generated text tokens, and TempoVoice, a controllable online text-to-speech (TTS) module that outputs speech synchronized with facial responses. To advance OMCRG research, we offer ResponseNet, a dataset of 696 detailed dyadic interactions featuring synchronized split-screen videos, multichannel audio, transcripts, and annotated facial behaviors. Comprehensive evaluations on ResponseNet demonstrate that OmniResponse outperforms baseline models in terms of semantic speech content, audio-visual synchronization, and generation quality. Our dataset, code, and models are publicly available.

</details>

### [Spotlight-TTS: Spotlighting the Style via Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech](2505.20868.md)
**Nam-Gyu Kim, Deok-Hyeon Cho, Seung-Bin Kim, Seong-Whan Lee** · 2025-05-27

<details>
<summary>Abstract</summary>

Recent advances in expressive text-to-speech (TTS) have introduced diverse methods based on style embedding extracted from reference speech. However, synthesizing high-quality expressive speech remains challenging. We propose Spotlight-TTS, which exclusively emphasizes style via voiced-aware style extraction and style direction adjustment. Voiced-aware style extraction focuses on voiced regions highly related to style while maintaining continuity across different speech regions to improve expressiveness. We adjust the direction of the extracted style for optimal integration into the TTS model, which improves speech quality. Experimental results demonstrate that Spotlight-TTS achieves superior performance compared to baseline models in terms of expressiveness, overall speech quality, and style transfer capability. Our audio samples are publicly available.

</details>

### [PromptEVC: Controllable Emotional Voice Conversion with Natural Language Prompts](2505.20678.md)
**Tianhua Qi, Shiyan Wang, Cheng Lu, Tengfei Song et al.** · 2025-05-27

<details>
<summary>Abstract</summary>

Controllable emotional voice conversion (EVC) aims to manipulate emotional expressions to increase the diversity of synthesized speech. Existing methods typically rely on predefined labels, reference audios, or prespecified factor values, often overlooking individual differences in emotion perception and expression. In this paper, we introduce PromptEVC that utilizes natural language prompts for precise and flexible emotion control. To bridge text descriptions with emotional speech, we propose emotion descriptor and prompt mapper to generate fine-grained emotion embeddings, trained jointly with reference embeddings. To enhance naturalness, we present a prosody modeling and control pipeline that adjusts the rhythm based on linguistic content and emotional cues. Additionally, a speaker encoder is incorporated to preserve identity. Experimental results demonstrate that PromptEVC outperforms state-of-the-art controllable EVC methods in emotion conversion, intensity control, mixed emotion synthesis, and prosody manipulation. Speech samples are available at https://jeremychee4.github.io/PromptEVC/.

</details>

### [VoiceMark: Zero-Shot Voice Cloning-Resistant Watermarking Approach Leveraging Speaker-Specific Latents](2505.21568.md)
**Haiyun Li, Zhiyong Wu, Xiaofeng Xie, Jingran Xie et al.** · 2025-05-27

<details>
<summary>Abstract</summary>

Voice cloning (VC)-resistant watermarking is an emerging technique for tracing and preventing unauthorized cloning. Existing methods effectively trace traditional VC models by training them on watermarked audio but fail in zero-shot VC scenarios, where models synthesize audio from an audio prompt without training. To address this, we propose VoiceMark, the first zero-shot VC-resistant watermarking method that leverages speaker-specific latents as the watermark carrier, allowing the watermark to transfer through the zero-shot VC process into the synthesized audio. Additionally, we introduce VC-simulated augmentations and VAD-based loss to enhance robustness against distortions. Experiments on multiple zero-shot VC models demonstrate that VoiceMark achieves over 95% accuracy in watermark detection after zero-shot VC synthesis, significantly outperforming existing methods, which only reach around 50%. See our code and demos at: https://huggingface.co/spaces/haiyunli/VoiceMark

</details>

### [Phir Hera Fairy: An English Fairytaler is a Strong Faker of Fluent Speech in Low-Resource Indian Languages](2505.20693.md)
**Praveen Srinivasa Varadhan, Srija Anand, Soma Siddhartha, Mitesh M. Khapra** · 2025-05-27

<details>
<summary>Abstract</summary>

What happens when an English Fairytaler is fine-tuned on Indian languages? We evaluate how the English F5-TTS model adapts to 11 Indian languages, measuring polyglot fluency, voice-cloning, style-cloning, and code-mixing. We compare: (i) training from scratch, (ii) fine-tuning English F5 on Indian data, and (iii) fine-tuning on both Indian and English data to prevent forgetting. Fine-tuning with only Indian data proves most effective and the resultant IN-F5 is a near-human polyglot; that enables speakers of one language (e.g., Odia) to fluently speak in another (e.g., Hindi). Our results show English pretraining aids low-resource TTS in reaching human parity. To aid progress in other low-resource languages, we study data-constrained setups and arrive at a compute optimal strategy. Finally, we show IN-F5 can synthesize unseen languages like Bhojpuri and Tulu using a human-in-the-loop approach for zero-resource TTS via synthetic data generation.

</details>

### [ArVoice: A Multi-Speaker Dataset for Arabic Speech Synthesis](2505.20506.md)
**Hawau Olamide Toyin et.al.** · 2025-05-26

### [Accelerating Flow-Matching-Based Text-to-Speech via Empirically Pruned Step Sampling](2505.19931.md)
**Qixi Zheng et.al.** · 2025-05-26

### [DiEmo-TTS: Disentangled Emotion Representations via Self-Supervised Distillation for Cross-Speaker Emotion Transfer in Text-to-Speech](2505.19687.md)
**Deok-Hyeon Cho et.al.** · 2025-05-26

### [GSA-TTS : Toward Zero-Shot Speech Synthesis based on Gradual Style Adaptor](2505.19384.md)
**Seokgi Lee et.al.** · 2025-05-26

### [VoiceStar: Robust Zero-Shot Autoregressive TTS with Duration Control and Extrapolation](2505.19462.md)
**Puyuan Peng, Shang-Wen Li, Abdelrahman Mohamed, David Harwath** · 2025-05-26

<details>
<summary>Abstract</summary>

We present VoiceStar, the first zero-shot TTS model that achieves both output duration control and extrapolation. VoiceStar is an autoregressive encoder-decoder neural codec language model, that leverages a novel Progress-Monitoring Rotary Position Embedding (PM-RoPE) and is trained with Continuation-Prompt Mixed (CPM) training. PM-RoPE enables the model to better align text and speech tokens, indicates the target duration for the generated speech, and also allows the model to generate speech waveforms much longer in duration than those seen during. CPM training also helps to mitigate the training/inference mismatch, and significantly improves the quality of the generated speech in terms of speaker similarity and intelligibility. VoiceStar outperforms or is on par with current state-of-the-art models on short-form benchmarks such as Librispeech and Seed-TTS, and significantly outperforms these models on long-form/extrapolation benchmarks (20-50s) in terms of intelligibility and naturalness. Code and models: https://github.com/jasonppy/VoiceStar. Audio samples: https://jasonppy.github.io/VoiceStar_web

</details>

### [CloneShield: A Framework for Universal Perturbation Against Zero-Shot Voice Cloning](2505.19119.md)
**Renyuan Li et.al.** · 2025-05-25

### [SpeakStream: Streaming Text-to-Speech with Interleaved Data](2505.19206.md)
**Richard He Bai, Zijin Gu, Tatiana Likhomanenko, Navdeep Jaitly** · 2025-05-25

<details>
<summary>Abstract</summary>

The latency bottleneck of traditional text-to-speech (TTS) systems fundamentally hinders the potential of streaming large language models (LLMs) in conversational AI. These TTS systems, typically trained and inferenced on complete utterances, introduce unacceptable delays, even with optimized inference speeds, when coupled with streaming LLM outputs. This is particularly problematic for creating responsive conversational agents where low first-token latency is critical. In this paper, we present SpeakStream, a streaming TTS system that generates audio incrementally from streaming text using a decoder-only architecture. SpeakStream is trained using a next-step prediction loss on interleaved text-speech data. During inference, it generates speech incrementally while absorbing streaming input text, making it particularly suitable for cascaded conversational AI agents where an LLM streams text to a TTS system. Our experiments demonstrate that SpeakStream achieves state-of-the-art latency results in terms of first-token latency while maintaining the quality of non-streaming TTS systems.

</details>

### [Revival with Voice: Multi-modal Controllable Text-to-Speech Synthesis](2505.18972.md)
**Minsu Kim, Pingchuan Ma, Honglie Chen, Stavros Petridis et al.** · 2025-05-25

<details>
<summary>Abstract</summary>

This paper explores multi-modal controllable Text-to-Speech Synthesis (TTS) where the voice can be generated from face image, and the characteristics of output speech (e.g., pace, noise level, distance, tone, place) can be controllable with natural text description. Specifically, we aim to mitigate the following three challenges in face-driven TTS systems. 1) To overcome the limited audio quality of audio-visual speech corpora, we propose a training method that additionally utilizes high-quality audio-only speech corpora. 2) To generate voices not only from real human faces but also from artistic portraits, we propose augmenting the input face image with stylization. 3) To consider one-to-many possibilities in face-to-voice mapping and ensure consistent voice generation at the same time, we propose to first employ sampling-based decoding and then use prompting with generated speech samples. Experimental results validate the proposed model's effectiveness in face-driven voice synthesis.

</details>

### [Eta-WavLM: Efficient Speaker Identity Removal in Self-Supervised Speech Representations Using a Simple Linear Equation](2505.19273.md)
**Giuseppe Ruggiero, Matteo Testa, Jurgen Van de Walle, Luigi Di Caro** · 2025-05-25

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has reduced the reliance on expensive labeling in speech technologies by learning meaningful representations from unannotated data. Since most SSL-based downstream tasks prioritize content information in speech, ideal representations should disentangle content from unwanted variations like speaker characteristics in the SSL representations. However, removing speaker information often degrades other speech components, and existing methods either fail to fully disentangle speaker identity or require resource-intensive models. In this paper, we propose a novel disentanglement method that linearly decomposes SSL representations into speaker-specific and speaker-independent components, effectively generating speaker disentangled representations. Comprehensive experiments show that our approach achieves speaker independence and as such, when applied to content-driven tasks such as voice conversion, our representations yield significant improvements over state-of-the-art methods.

</details>

### [MPE-TTS: Customized Emotion Zero-Shot Text-To-Speech Using Multi-Modal Prompt](2505.18453.md)
**Zhichao Wu et.al.** · 2025-05-24

### [Towards Emotionally Consistent Text-Based Speech Editing: Introducing EmoCorrector and The ECD-TSE Dataset](2505.20341.md)
**Rui Liu, Pu Gao, Jiatian Xi, Berrak Sisman et al.** · 2025-05-24

<details>
<summary>Abstract</summary>

Text-based speech editing (TSE) modifies speech using only text, eliminating re-recording. However, existing TSE methods, mainly focus on the content accuracy and acoustic consistency of synthetic speech segments, and often overlook the emotional shifts or inconsistency issues introduced by text changes. To address this issue, we propose EmoCorrector, a novel post-correction scheme for TSE. EmoCorrector leverages Retrieval-Augmented Generation (RAG) by extracting the edited text's emotional features, retrieving speech samples with matching emotions, and synthesizing speech that aligns with the desired emotion while preserving the speaker's identity and quality. To support the training and evaluation of emotional consistency modeling in TSE, we pioneer the benchmarking Emotion Correction Dataset for TSE (ECD-TSE). The prominent aspect of ECD-TSE is its inclusion of $<$text, speech$>$ paired data featuring diverse text variations and a range of emotional expressions. Subjective and objective experiments and comprehensive analysis on ECD-TSE confirm that EmoCorrector significantly enhances the expression of intended emotion while addressing emotion inconsistency limitations in current TSE methods. Code and audio examples are available at https://github.com/AI-S2-Lab/EmoCorrector.

</details>

### [RASMALAI: Resources for Adaptive Speech Modeling in Indian Languages with Accents and Intonations](2505.18609.md)
**Ashwin Sankar, Yoach Lacombe, Sherry Thomas, Praveen Srinivasa Varadhan et al.** · 2025-05-24

<details>
<summary>Abstract</summary>

We introduce RASMALAI, a large-scale speech dataset with rich text descriptions, designed to advance controllable and expressive text-to-speech (TTS) synthesis for 23 Indian languages and English. It comprises 13,000 hours of speech and 24 million text-description annotations with fine-grained attributes like speaker identity, accent, emotion, style, and background conditions. Using RASMALAI, we develop IndicParlerTTS, the first open-source, text-description-guided TTS for Indian languages. Systematic evaluation demonstrates its ability to generate high-quality speech for named speakers, reliably follow text descriptions and accurately synthesize specified attributes. Additionally, it effectively transfers expressive characteristics both within and across languages. IndicParlerTTS consistently achieves strong performance across these evaluations, setting a new standard for controllable multilingual expressive speech synthesis in Indian languages.

</details>

### [UniTTS: An end-to-end TTS system without decoupling of acoustic and semantic information](2505.17426.md)
**Rui Wang et.al.** · 2025-05-23

### [What You Read Isn't What You Hear: Linguistic Sensitivity in Deepfake Speech Detection](2505.17513.md)
**Binh Nguyen, Shuji Shi, Ryan Ofman, Thai Le** · 2025-05-23

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech technologies have enabled realistic voice generation, fueling audio-based deepfake attacks such as fraud and impersonation. While audio anti-spoofing systems are critical for detecting such threats, prior work has predominantly focused on acoustic-level perturbations, leaving the impact of linguistic variation largely unexplored. In this paper, we investigate the linguistic sensitivity of both open-source and commercial anti-spoofing detectors by introducing transcript-level adversarial attacks. Our extensive evaluation reveals that even minor linguistic perturbations can significantly degrade detection accuracy: attack success rates surpass 60% on several open-source detector-voice pairs, and notably one commercial detection accuracy drops from 100% on synthetic audio to just 32%. Through a comprehensive feature attribution analysis, we identify that both linguistic complexity and model-level audio embedding similarity contribute strongly to detector vulnerability. We further demonstrate the real-world risk via a case study replicating the Brad Pitt audio deepfake scam, using transcript adversarial attacks to completely bypass commercial detectors. These results highlight the need to move beyond purely acoustic defenses and account for linguistic variation in the design of robust anti-spoofing systems. All source code will be publicly available.

</details>

### [Benchmarking Expressive Japanese Character Text-to-Speech with VITS and Style-BERT-VITS2](2505.17320.md)
**Zackary Rackauckas et.al.** · 2025-05-22

### [Improving Noise Robustness of LLM-based Zero-shot TTS via Discrete Acoustic Token Denoising](2505.13830.md)
**Ye-Xin Lu et.al.** · 2025-05-22

### [EZ-VC: Easy Zero-shot Any-to-Any Voice Conversion](2505.16691.md)
**Advait Joglekar, Divyanshu Singh, Rooshil Rohit Bhatia, S. Umesh** · 2025-05-22

<details>
<summary>Abstract</summary>

Voice Conversion research in recent times has increasingly focused on improving the zero-shot capabilities of existing methods. Despite remarkable advancements, current architectures still tend to struggle in zero-shot cross-lingual settings. They are also often unable to generalize for speakers of unseen languages and accents. In this paper, we adopt a simple yet effective approach that combines discrete speech representations from self-supervised models with a non-autoregressive Diffusion-Transformer based conditional flow matching speech decoder. We show that this architecture allows us to train a voice-conversion model in a purely textless, self-supervised fashion. Our technique works without requiring multiple encoders to disentangle speech features. Our model also manages to excel in zero-shot cross-lingual settings even for unseen languages. For Demo: https://ez-vc.github.io/EZ-VC-Demo/

</details>

### [Beyond Face Swapping: A Diffusion-Based Digital Human Benchmark for Multimodal Deepfake Detection](2505.16512.md)
**Jiaxin Liu, Jia Wang, Saihui Hou, Min Ren et al.** · 2025-05-22

<details>
<summary>Abstract</summary>

In recent years, the explosive advancement of deepfake technology has posed a critical and escalating threat to public security: diffusion-based digital human generation. Unlike traditional face manipulation methods, such models can generate highly realistic videos with consistency via multimodal control signals. Their flexibility and covertness pose severe challenges to existing detection strategies. To bridge this gap, we introduce DigiFakeAV, the new large-scale multimodal digital human forgery dataset based on diffusion models. Leveraging five of the latest digital human generation methods and a voice cloning method, we systematically construct a dataset comprising 60,000 videos (8.4 million frames), covering multiple nationalities, skin tones, genders, and real-world scenarios, significantly enhancing data diversity and realism. User studies demonstrate that the misrecognition rate by participants for DigiFakeAV reaches as high as 68%. Moreover, the substantial performance degradation of existing detection models on our dataset further highlights its challenges. To address this problem, we propose DigiShield, an effective detection baseline based on spatiotemporal and cross-modal fusion. By jointly modeling the 3D spatiotemporal features of videos and the semantic-acoustic features of audio, DigiShield achieves state-of-the-art (SOTA) performance on the DigiFakeAV and shows strong generalization on other datasets.

</details>

### [MM-MovieDubber: Towards Multi-Modal Learning for Multi-Modal Movie Dubbing](2505.16279.md)
**Junjie Zheng, Zihao Chen, Chaofan Ding, Yunming Liang et al.** · 2025-05-22

<details>
<summary>Abstract</summary>

Current movie dubbing technology can produce the desired speech using a reference voice and input video, maintaining perfect synchronization with the visuals while effectively conveying the intended emotions. However, crucial aspects of movie dubbing, including adaptation to various dubbing styles, effective handling of dialogue, narration, and monologues, as well as consideration of subtle details such as speaker age and gender, remain insufficiently explored. To tackle these challenges, we introduce a multi-modal generative framework. First, it utilizes a multi-modal large vision-language model (VLM) to analyze visual inputs, enabling the recognition of dubbing types and fine-grained attributes. Second, it produces high-quality dubbing using large speech generation models, guided by multi-modal inputs. Additionally, a movie dubbing dataset with annotations for dubbing types and subtle details is constructed to enhance movie understanding and improve dubbing quality for the proposed multi-modal framework. Experimental results across multiple benchmark datasets show superior performance compared to state-of-the-art (SOTA) methods. In details, the LSE-D, SPK-SIM, EMO-SIM, and MCD exhibit improvements of up to 1.09%, 8.80%, 19.08%, and 18.74%, respectively.

</details>

### [Prosody-Adaptable Audio Codecs for Zero-Shot Voice Conversion via In-Context Learning](2505.15402.md)
**Junchuan Zhao et.al.** · 2025-05-21

### [Accelerating Autoregressive Speech Synthesis Inference With Speech Speculative Decoding](2505.15380.md)
**Zijian Lin et.al.** · 2025-05-21

### [MIKU-PAL: An Automated and Standardized Multi-Modal Method for Speech Paralinguistic and Affect Labeling](2505.15772.md)
**Yifan Cheng, Ruoyi Zhang, Jiatong Shi** · 2025-05-21

<details>
<summary>Abstract</summary>

Acquiring large-scale emotional speech data with strong consistency remains a challenge for speech synthesis. This paper presents MIKU-PAL, a fully automated multimodal pipeline for extracting high-consistency emotional speech from unlabeled video data. Leveraging face detection and tracking algorithms, we developed an automatic emotion analysis system using a multimodal large language model (MLLM). Our results demonstrate that MIKU-PAL can achieve human-level accuracy (68.5% on MELD) and superior consistency (0.93 Fleiss kappa score) while being much cheaper and faster than human annotation. With the high-quality, flexible, and consistent annotation from MIKU-PAL, we can annotate fine-grained speech emotion categories of up to 26 types, validated by human annotators with 83% rationality ratings. Based on our proposed system, we further released a fine-grained emotional speech dataset MIKU-EmoBench(131.2 hours) as a new benchmark for emotional text-to-speech and visual voice cloning.

</details>

### [Segmentation-Variant Codebooks for Preservation of Paralinguistic and Prosodic Information](2505.15667.md)
**Nicholas Sanders, Yuanchao Li, Korin Richmond, Simon King** · 2025-05-21

<details>
<summary>Abstract</summary>

Quantization in SSL speech models (e.g., HuBERT) improves compression and performance in tasks like language modeling, resynthesis, and text-to-speech but often discards prosodic and paralinguistic information (e.g., emotion, prominence). While increasing codebook size mitigates some loss, it inefficiently raises bitrates. We propose Segmentation-Variant Codebooks (SVCs), which quantize speech at distinct linguistic units (frame, phone, word, utterance), factorizing it into multiple streams of segment-specific discrete features. Our results show that SVCs are significantly more effective at preserving prosodic and paralinguistic information across probing tasks. Additionally, we find that pooling before rather than after discretization better retains segment-level information. Resynthesis experiments further confirm improved style realization and slightly improved quality while preserving intelligibility.

</details>

### [Audio Jailbreak: An Open Comprehensive Benchmark for Jailbreaking Large Audio-Language Models](2505.15406.md)
**Zirui Song, Qian Jiang, Mingxuan Cui, Mingzhe Li et al.** · 2025-05-21

<details>
<summary>Abstract</summary>

The rise of Large Audio Language Models (LAMs) brings both potential and risks, as their audio outputs may contain harmful or unethical content. However, current research lacks a systematic, quantitative evaluation of LAM safety especially against jailbreak attacks, which are challenging due to the temporal and semantic nature of speech. To bridge this gap, we introduce AJailBench, the first benchmark specifically designed to evaluate jailbreak vulnerabilities in LAMs. We begin by constructing AJailBench-Base, a dataset of 1,495 adversarial audio prompts spanning 10 policy-violating categories, converted from textual jailbreak attacks using realistic text to speech synthesis. Using this dataset, we evaluate several state-of-the-art LAMs and reveal that none exhibit consistent robustness across attacks. To further strengthen jailbreak testing and simulate more realistic attack conditions, we propose a method to generate dynamic adversarial variants. Our Audio Perturbation Toolkit (APT) applies targeted distortions across time, frequency, and amplitude domains. To preserve the original jailbreak intent, we enforce a semantic consistency constraint and employ Bayesian optimization to efficiently search for perturbations that are both subtle and highly effective. This results in AJailBench-APT, an extended dataset of optimized adversarial audio samples. Our findings demonstrate that even small, semantically preserved perturbations can significantly reduce the safety performance of leading LAMs, underscoring the need for more robust and semantically aware defense mechanisms.

</details>

### [P2VA: Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech](2505.17093.md)
**Yejin Lee, Jaehoon Kang, Kyuhong Shim** · 2025-05-21

<details>
<summary>Abstract</summary>

While persona-driven large language models (LLMs) and prompt-based text-to-speech (TTS) systems have advanced significantly, a usability gap arises when users attempt to generate voices matching their desired personas from implicit descriptions. Most users lack specialized knowledge to specify detailed voice attributes, which often leads TTS systems to misinterpret their expectations. To address these gaps, we introduce Persona-to-Voice-Attribute (P2VA), the first framework enabling voice generation automatically from persona descriptions. Our approach employs two strategies: P2VA-C for structured voice attributes, and P2VA-O for richer style descriptions. Evaluation shows our P2VA-C reduces WER by 5% and improves MOS by 0.33 points. To the best of our knowledge, P2VA is the first framework to establish a connection between persona and voice synthesis. In addition, we discover that current LLMs embed societal biases in voice attributes during the conversion process. Our experiments and findings further provide insights into the challenges of building persona-voice systems.

</details>

### [Voice-ENHANCE: Speech Restoration using a Diffusion-based Voice Conversion Framework](2505.15254.md)
**Kyungguen Byun, Jason Filos, Erik Visser, Sunkuk Moon** · 2025-05-21

<details>
<summary>Abstract</summary>

We propose a speech enhancement system that combines speaker-agnostic speech restoration with voice conversion (VC) to obtain a studio-level quality speech signal. While voice conversion models are typically used to change speaker characteristics, they can also serve as a means of speech restoration when the target speaker is the same as the source speaker. However, since VC models are vulnerable to noisy conditions, we have included a generative speech restoration (GSR) model at the front end of our proposed system. The GSR model performs noise suppression and restores speech damage incurred during that process without knowledge about the target speaker. The VC stage then uses guidance from clean speaker embeddings to further restore the output speech. By employing this two-stage approach, we have achieved speech quality objective metric scores comparable to state-of-the-art (SOTA) methods across multiple datasets.

</details>

### [Hybrid Audio Detection Using Fine-Tuned Audio Spectrogram Transformers: A Dataset-Driven Evaluation of Mixed AI-Human Speech](2505.15136.md)
**Kunyang Huang, Bin Hu** · 2025-05-21

<details>
<summary>Abstract</summary>

The rapid advancement of artificial intelligence (AI) has enabled sophisticated audio generation and voice cloning technologies, posing significant security risks for applications reliant on voice authentication. While existing datasets and models primarily focus on distinguishing between human and fully synthetic speech, real-world attacks often involve audio that combines both genuine and cloned segments. To address this gap, we construct a novel hybrid audio dataset incorporating human, AI-generated, cloned, and mixed audio samples. We further propose fine-tuned Audio Spectrogram Transformer (AST)-based models tailored for detecting these complex acoustic patterns. Extensive experiments demonstrate that our approach significantly outperforms existing baselines in mixed-audio detection, achieving 97\% classification accuracy. Our findings highlight the importance of hybrid datasets and tailored models in advancing the robustness of speech-based authentication systems.

</details>

### [Impact of Frame Rates on Speech Tokenizer: A Case Study on Mandarin and English](2505.17076.md)
**Haoyang Zhang et.al.** · 2025-05-20

### [TCSinger 2: Customizable Multilingual Zero-shot Singing Voice Synthesis](2505.14910.md)
**Yu Zhang et.al.** · 2025-05-20

### [FMSD-TTS: Few-shot Multi-Speaker Multi-Dialect Text-to-Speech Synthesis for Ü-Tsang, Amdo and Kham Speech Dataset Generation](2505.14351.md)
**Yutong Liu et.al.** · 2025-05-20

### [SeamlessEdit: Background Noise Aware Zero-Shot Speech Editing with in-Context Enhancement](2505.14066.md)
**Kuan-Yu Chen et.al.** · 2025-05-20

### [AudioJailbreak: Jailbreak Attacks against End-to-End Large Audio-Language Models](2505.14103.md)
**Guangke Chen, Fu Song, Zhe Zhao, Xiaojun Jia et al.** · 2025-05-20

<details>
<summary>Abstract</summary>

Jailbreak attacks to Large audio-language models (LALMs) are studied recently, but they exclusively focused on the attack scenario where the adversary can fully manipulate user prompts (named strong adversary) and limited in effectiveness, applicability, and practicability. In this work, we first conduct an extensive evaluation showing that advanced text jailbreak attacks cannot be easily ported to end-to-end LALMs via text-to-speech (TTS) techniques. We then propose AUDIOJAILBREAK, a novel audio jailbreak attack, featuring (1) asynchrony: the jailbreak audios do not need to align with user prompts in the time axis by crafting suffixal jailbreak audios; (2) universality: a single jailbreak perturbation is effective for different prompts by incorporating multiple prompts into the perturbation generation; (3) stealthiness: the malicious intent of jailbreak audios is concealed by proposing various intent concealment strategies; and (4) over-the-air robustness: the jailbreak audios remain effective when being played over the air by incorporating reverberation into the perturbation generation. In contrast, all prior audio jailbreak attacks cannot offer asynchrony, universality, stealthiness, and/or over-the-air robustness. Moreover, AUDIOJAILBREAK is also applicable to a more practical and broader attack scenario where the adversary cannot fully manipulate user prompts (named weak adversary). Extensive experiments with thus far the most LALMs demonstrate the high effectiveness of AUDIOJAILBREAK, in particular, it can jailbreak openAI's GPT-4o-Audio and bypass Meta's Llama-Guard-3 safeguard, in the weak adversary scenario. We highlight that our work peeks into the security implications of audio jailbreak attacks against LALMs, and realistically fosters improving their robustness, especially for the newly proposed weak adversary.

</details>

### [Pairwise Evaluation of Accent Similarity in Speech Synthesis](2505.14410.md)
**Jinzuomu Zhong, Suyuan Liu, Dan Wells, Korin Richmond** · 2025-05-20

<details>
<summary>Abstract</summary>

Despite growing interest in generating high-fidelity accents, evaluating accent similarity in speech synthesis has been underexplored. We aim to enhance both subjective and objective evaluation methods for accent similarity. Subjectively, we refine the XAB listening test by adding components that achieve higher statistical significance with fewer listeners and lower costs. Our method involves providing listeners with transcriptions, having them highlight perceived accent differences, and implementing meticulous screening for reliability. Objectively, we utilise pronunciation-related metrics, based on distances between vowel formants and phonetic posteriorgrams, to evaluate accent generation. Comparative experiments reveal that these metrics, alongside accent similarity, speaker similarity, and Mel Cepstral Distortion, can be used. Moreover, our findings underscore significant limitations of common metrics like Word Error Rate in assessing underrepresented accents.

</details>

### [Articulatory Feature Prediction from Surface EMG during Speech Production](2505.13814.md)
**Jihwan Lee, Kevin Huang, Kleanthis Avramidis, Simon Pistrosch et al.** · 2025-05-20

<details>
<summary>Abstract</summary>

We present a model for predicting articulatory features from surface electromyography (EMG) signals during speech production. The proposed model integrates convolutional layers and a Transformer block, followed by separate predictors for articulatory features. Our approach achieves a high prediction correlation of approximately 0.9 for most articulatory features. Furthermore, we demonstrate that these predicted articulatory features can be decoded into intelligible speech waveforms. To our knowledge, this is the first method to decode speech waveforms from surface EMG via articulatory features, offering a novel approach to EMG-based speech synthesis. Additionally, we analyze the relationship between EMG electrode placement and articulatory feature predictability, providing knowledge-driven insights for optimizing EMG electrode configurations. The source code and decoded speech samples are publicly available.

</details>

### [ClapFM-EVC: High-Fidelity and Flexible Emotional Voice Conversion with Dual Control from Natural Language and Speech](2505.13805.md)
**Yu Pan, Yanni Hu, Yuguang Yang, Jixun Yao et al.** · 2025-05-20

<details>
<summary>Abstract</summary>

Despite great advances, achieving high-fidelity emotional voice conversion (EVC) with flexible and interpretable control remains challenging. This paper introduces ClapFM-EVC, a novel EVC framework capable of generating high-quality converted speech driven by natural language prompts or reference speech with adjustable emotion intensity. We first propose EVC-CLAP, an emotional contrastive language-audio pre-training model, guided by natural language prompts and categorical labels, to extract and align fine-grained emotional elements across speech and text modalities. Then, a FuEncoder with an adaptive intensity gate is presented to seamless fuse emotional features with Phonetic PosteriorGrams from a pre-trained ASR model. To further improve emotion expressiveness and speech naturalness, we propose a flow matching model conditioned on these captured features to reconstruct Mel-spectrogram of source speech. Subjective and objective evaluations validate the effectiveness of ClapFM-EVC.

</details>

### [Efficient Speech Language Modeling via Energy Distance in Continuous Latent Space](2505.13181.md)
**Zhengrui Ma et.al.** · 2025-05-19

### [DualCodec: A Low-Frame-Rate, Semantically-Enhanced Neural Audio Codec for Speech Generation](2505.13000.md)
**Jiaqi Li et.al.** · 2025-05-19

### [Codec-Based Deepfake Source Tracing via Neural Audio Codec Taxonomy](2505.12994.md)
**Xuanjun Chen et.al.** · 2025-05-19

### [OZSpeech: One-step Zero-shot Speech Synthesis with Learned-Prior-Conditioned Flow Matching](2505.12800.md)
**Hieu-Nghia Huynh-Nguyen et.al.** · 2025-05-19

### [RoVo: Robust Voice Protection Against Unauthorized Speech Synthesis with Embedding-Level Perturbations](2505.12686.md)
**Seungmin Kim et.al.** · 2025-05-19

### [Chain-Talker: Chain Understanding and Rendering for Empathetic Conversational Speech Synthesis](2505.12597.md)
**Yifan Hu, Rui Liu, Yi Ren, Xiang Yin et al.** · 2025-05-19

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis (CSS) aims to align synthesized speech with the emotional and stylistic context of user-agent interactions to achieve empathy. Current generative CSS models face interpretability limitations due to insufficient emotional perception and redundant discrete speech coding. To address the above issues, we present Chain-Talker, a three-stage framework mimicking human cognition: Emotion Understanding derives context-aware emotion descriptors from dialogue history; Semantic Understanding generates compact semantic codes via serialized prediction; and Empathetic Rendering synthesizes expressive speech by integrating both components. To support emotion modeling, we develop CSS-EmCap, an LLM-driven automated pipeline for generating precise conversational speech emotion captions. Experiments on three benchmark datasets demonstrate that Chain-Talker produces more expressive and empathetic speech than existing methods, with CSS-EmCap contributing to reliable emotion modeling. The code and demos are available at: https://github.com/AI-S2-Lab/Chain-Talker.

</details>

### [Shallow Flow Matching for Coarse-to-Fine Text-to-Speech Synthesis](2505.12226.md)
**Dong Yang et.al.** · 2025-05-18

### [VoiceCloak: A Multi-Dimensional Defense Framework against Unauthorized Diffusion-based Voice Cloning](2505.12332.md)
**Qianyue Hu, Junyan Wu, Wei Lu, Xiangyang Luo** · 2025-05-18

<details>
<summary>Abstract</summary>

Diffusion Models (DMs) have achieved remarkable success in realistic voice cloning (VC), while they also increase the risk of malicious misuse. Existing proactive defenses designed for traditional VC models aim to disrupt the forgery process, but they have been proven incompatible with DMs due to the intricate generative mechanisms of diffusion. To bridge this gap, we introduce VoiceCloak, a multi-dimensional proactive defense framework with the goal of obfuscating speaker identity and degrading perceptual quality in potential unauthorized VC. To achieve these goals, we conduct a focused analysis to identify specific vulnerabilities within DMs, allowing VoiceCloak to disrupt the cloning process by introducing adversarial perturbations into the reference audio. Specifically, to obfuscate speaker identity, VoiceCloak first targets speaker identity by distorting representation learning embeddings to maximize identity variation, which is guided by auditory perception principles. Additionally, VoiceCloak disrupts crucial conditional guidance processes, particularly attention context, thereby preventing the alignment of vocal characteristics that are essential for achieving convincing cloning. Then, to address the second objective, VoiceCloak introduces score magnitude amplification to actively steer the reverse trajectory away from the generation of high-quality speech. Noise-guided semantic corruption is further employed to disrupt structural speech semantics captured by DMs, degrading output quality. Extensive experiments highlight VoiceCloak's outstanding defense success rate against unauthorized diffusion-based voice cloning. Audio samples of VoiceCloak are available at https://voice-cloak.github.io/VoiceCloak/.

</details>

### [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](2505.11391.md)
**Danilo de Oliveira et.al.** · 2025-05-16

### [Audio Turing Test: Benchmarking the Human-likeness of Large Language Model-based Text-to-Speech Systems in Chinese](2505.11200.md)
**Xihuai Wang et.al.** · 2025-05-16

### [BanglaFake: Constructing and Evaluating a Specialized Bengali Deepfake Audio Dataset](2505.10885.md)
**Istiaq Ahmed Fahad, Kamruzzaman Asif, Sifat Sikder** · 2025-05-16

<details>
<summary>Abstract</summary>

Deepfake audio detection is challenging for low-resource languages like Bengali due to limited datasets and subtle acoustic features. To address this, we introduce BangalFake, a Bengali Deepfake Audio Dataset with 12,260 real and 13,260 deepfake utterances. Synthetic speech is generated using SOTA Text-to-Speech (TTS) models, ensuring high naturalness and quality. We evaluate the dataset through both qualitative and quantitative analyses. Mean Opinion Score (MOS) from 30 native speakers shows Robust-MOS of 3.40 (naturalness) and 4.01 (intelligibility). t-SNE visualization of MFCCs highlights real vs. fake differentiation challenges. This dataset serves as a crucial resource for advancing deepfake detection in Bengali, addressing the limitations of low-resource language research.

</details>

### [UDDETTS: Unifying Discrete and Dimensional Emotions for Controllable Emotional Text-to-Speech](2505.10599.md)
**Jiaxuan Liu, Yang Xiang, Han Zhao, Xiangang Li et al.** · 2025-05-15

<details>
<summary>Abstract</summary>

Recent large language models (LLMs) have made great progress in the field of text-to-speech (TTS), but they still face major challenges in synthesizing fine-grained emotional speech in an interpretable manner. Traditional methods rely on discrete emotion labels to control emotion categories and intensities, which cannot capture the complexity and continuity of human emotional perception and expression. The lack of large-scale emotional speech datasets with balanced emotion distributions and fine-grained emotional annotations often causes overfitting in synthesis models and impedes effective emotion control. To address these issues, we propose UDDETTS, a universal LLM framework unifying discrete and dimensional emotions for controllable emotional TTS. This model introduces the interpretable Arousal-Dominance-Valence (ADV) space for dimensional emotion description and supports emotion control driven by either discrete emotion labels or nonlinearly quantified ADV values. Furthermore, a semi-supervised training strategy is designed to comprehensively utilize diverse speech datasets with different types of emotional annotations to train the UDDETTS. Experiments show that UDDETTS achieves linear emotion control along three interpretable dimensions, and exhibits superior end-to-end emotional speech synthesis capabilities. Code and demos are available at: https://anonymous.4open.science/w/UDDETTS.

</details>

### [DPN-GAN: Inducing Periodic Activations in Generative Adversarial Networks for High-Fidelity Audio Synthesis](2505.09091.md)
**Zeeshan Ahmad, Shudi Bao, Meng Chen** · 2025-05-14

<details>
<summary>Abstract</summary>

In recent years, generative adversarial networks (GANs) have made significant progress in generating audio sequences. However, these models typically rely on bandwidth-limited mel-spectrograms, which constrain the resolution of generated audio sequences, and lead to mode collapse during conditional generation. To address this issue, we propose Deformable Periodic Network based GAN (DPN-GAN), a novel GAN architecture that incorporates a kernel-based periodic ReLU activation function to induce periodic bias in audio generation. This innovative approach enhances the model's ability to capture and reproduce intricate audio patterns. In particular, our proposed model features a DPN module for multi-resolution generation utilizing deformable convolution operations, allowing for adaptive receptive fields that improve the quality and fidelity of the synthetic audio. Additionally, we enhance the discriminator network using deformable convolution to better distinguish between real and generated samples, further refining the audio quality. We trained two versions of the model: DPN-GAN small (38.67M parameters) and DPN-GAN large (124M parameters). For evaluation, we use five different datasets, covering both speech synthesis and music generation tasks, to demonstrate the efficiency of the DPN-GAN. The experimental results demonstrate that DPN-GAN delivers superior performance on both out-of-distribution and noisy data, showcasing its robustness and adaptability. Trained across various datasets, DPN-GAN outperforms state-of-the-art GAN architectures on standard evaluation metrics, and exhibits increased robustness in synthesized audio.

</details>

### [SingNet: Towards a Large-Scale, Diverse, and In-the-Wild Singing Voice Dataset](2505.09325.md)
**Yicheng Gu, Chaoren Wang, Junan Zhang, Xueyao Zhang et al.** · 2025-05-14

<details>
<summary>Abstract</summary>

The lack of a publicly-available large-scale and diverse dataset has long been a significant bottleneck for singing voice applications like Singing Voice Synthesis (SVS) and Singing Voice Conversion (SVC). To tackle this problem, we present SingNet, an extensive, diverse, and in-the-wild singing voice dataset. Specifically, we propose a data processing pipeline to extract ready-to-use training data from sample packs and songs on the internet, forming 3000 hours of singing voices in various languages and styles. Furthermore, to facilitate the use and demonstrate the effectiveness of SingNet, we pre-train and open-source various state-of-the-art (SOTA) models on Wav2vec2, BigVGAN, and NSF-HiFiGAN based on our collected singing voice data. We also conduct benchmark experiments on Automatic Lyric Transcription (ALT), Neural Vocoder, and Singing Voice Conversion (SVC). Audio demos are available at: https://singnet-dataset.github.io/.

</details>

### [Investigating self-supervised features for expressive, multilingual voice conversion](2505.08278.md)
**Álvaro Martín-Cortinas et.al.** · 2025-05-13

### [MiniMax-Speech: Intrinsic Zero-Shot Text-to-Speech with a Learnable Speaker Encoder](2505.07916.md)
**Bowen Zhang et.al.** · 2025-05-12

### [Lightweight End-to-end Text-to-speech Synthesis for low resource on-device applications](2505.07701.md)
**Biel Tura Vecino et.al.** · 2025-05-12

### [VTutor: An Animated Pedagogical Agent SDK that Provide Real Time Multi-Model Feedback](2505.06676.md)
**Eason Chen, Chenyu Lin, Yu-Kai Huang, Xinyi Tang et al.** · 2025-05-10

<details>
<summary>Abstract</summary>

Pedagogical Agents (PAs) show significant potential for boosting student engagement and learning outcomes by providing adaptive, on-demand support in educational contexts. However, existing PA solutions are often hampered by pre-scripted dialogue, unnatural animations, uncanny visual realism, and high development costs. To address these gaps, we introduce VTutor, an open-source SDK leveraging lightweight WebGL, Unity, and JavaScript frameworks. VTutor receives text outputs from a large language model (LLM), converts them into audio via text-to-speech, and then renders a real-time, lip-synced pedagogical agent (PA) for immediate, large-scale deployment on web-based learning platforms. By providing on-demand, personalized feedback, VTutor strengthens students' motivation and deepens their engagement with instructional material. Using an anime-like aesthetic, VTutor alleviates the uncanny valley effect, allowing learners to engage with expressive yet comfortably stylized characters. Our evaluation with 50 participants revealed that VTutor significantly outperforms the existing talking-head approaches (e.g., SadTalker) on perceived synchronization accuracy, naturalness, emotional expressiveness, and overall preference. As an open-source project, VTutor welcomes community-driven contributions - from novel character designs to specialized showcases of pedagogical agent applications - that fuel ongoing innovation in AI-enhanced education. By providing an accessible, customizable, and learner-centered PA solution, VTutor aims to elevate human-AI interaction experience in education fields, ultimately broadening the impact of AI in learning contexts. The demo link to VTutor is at https://vtutor-aied25.vercel.app.

</details>

### [Bridging the Gap: An Intermediate Language for Enhanced and Cost-Effective Grapheme-to-Phoneme Conversion with Homographs with Multiple Pronunciations Disambiguation](2505.06599.md)
**Abbas Bertina, Shahab Beirami, Hossein Biniazian, Elham Esmaeilnia et al.** · 2025-05-10

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion for Persian presents unique challenges due to its complex phonological features, particularly homographs and Ezafe, which exist in formal and informal language contexts. This paper introduces an intermediate language specifically designed for Persian language processing that addresses these challenges through a multi-faceted approach. Our methodology combines two key components: Large Language Model (LLM) prompting techniques and a specialized sequence-to-sequence machine transliteration architecture. We developed and implemented a systematic approach for constructing a comprehensive lexical database for homographs with multiple pronunciations disambiguation often termed polyphones, utilizing formal concept analysis for semantic differentiation. We train our model using two distinct datasets: the LLM-generated dataset for formal and informal Persian and the B-Plus podcasts for informal language variants. The experimental results demonstrate superior performance compared to existing state-of-the-art approaches, particularly in handling the complexities of Persian phoneme conversion. Our model significantly improves Phoneme Error Rate (PER) metrics, establishing a new benchmark for Persian G2P conversion accuracy. This work contributes to the growing research in low-resource language processing and provides a robust solution for Persian text-to-speech systems and demonstrating its applicability beyond Persian. Specifically, the approach can extend to languages with rich homographic phenomena such as Chinese and Arabic

</details>

### [Enhancing the Prediction of Episodes of Aggression in Patients with Dementia Using Audio-Based Detection: A Multimodal Late Fusion Approach with a Meta-Classifier](s2:6d512990d19501e485f20462ed01c3a9ca6d1826.md)
**Ioannis Galanakis, R. Soldatos, N. Karanikolas, Athanasios Voulodimos et al.** · 2025-05-10

<details>
<summary>Abstract</summary>

This study presents an enhancement in the prediction of aggressive outbursts in dementia patients from our previous work, by integrating audio-based violence detection into our previous visual-based aggressive body movement detections. By combining audio and visual information, we aim to further enhance the model’s capabilities and make it more suitable for real-world scenario applications. This current work utilizes an audio dataset, containing various audio segments capturing vocal expressions during aggressive and non-aggressive scenarios. Various noise-filtering techniques were performed on the audio files using Mel-frequency cepstral coefficients (MFCCs), frequency filtering, and speech prosody to extract clear information from the audio features. Furthermore, we perform a late fusion rule to merge the predictions of the two models into a unified trained meta-classifier to determine the further improvement of the model with the audio integrated into it with a higher aim for a more precise and multimodal approach in detecting and predicting aggressive outburst behavior in patients suffering from dementia. The analysis of the correlations in our multimodal approach suggests that the accuracy of the early detection models is improved, providing a novel proof of concept with the appropriate findings to advance the understanding of aggression prediction in clinical settings and offer more effective intervention tactics from caregivers.

</details>

### [FlexSpeech: Towards Stable, Controllable and Expressive Text-to-Speech](2505.05159.md)
**Linhan Ma, Dake Guo, He Wang, Jin Xu et al.** · 2025-05-08

<details>
<summary>Abstract</summary>

Current speech generation research can be categorized into two primary classes: non-autoregressive and autoregressive. The fundamental distinction between these approaches lies in the duration prediction strategy employed for predictable-length sequences. The NAR methods ensure stability in speech generation by explicitly and independently modeling the duration of each phonetic unit. Conversely, AR methods employ an autoregressive paradigm to predict the compressed speech token by implicitly modeling duration with Markov properties. Although this approach improves prosody, it does not provide the structural guarantees necessary for stability. To simultaneously address the issues of stability and naturalness in speech generation, we propose FlexSpeech, a stable, controllable, and expressive TTS model. The motivation behind FlexSpeech is to incorporate Markov dependencies and preference optimization directly on the duration predictor to boost its naturalness while maintaining explicit modeling of the phonetic units to ensure stability. Specifically, we decompose the speech generation task into two components: an AR duration predictor and a NAR acoustic model. The acoustic model is trained on a substantial amount of data to learn to render audio more stably, given reference audio prosody and phone durations. The duration predictor is optimized in a lightweight manner for different stylistic variations, thereby enabling rapid style transfer while maintaining a decoupled relationship with the specified speaker timbre. Experimental results demonstrate that our approach achieves SOTA stability and naturalness in zero-shot TTS. More importantly, when transferring to a specific stylistic domain, we can accomplish lightweight optimization of the duration module solely with about 100 data samples, without the need to adjust the acoustic model, thereby enabling rapid and stable style transfer.

</details>

### [A Multi-Agent AI Framework for Immersive Audiobook Production through Spatial Audio and Neural Narration](2505.04885.md)
**Shaja Arul Selvamani, Nia D'Souza Ganapathy** · 2025-05-08

<details>
<summary>Abstract</summary>

This research introduces an innovative AI-driven multi-agent framework specifically designed for creating immersive audiobooks. Leveraging neural text-to-speech synthesis with FastSpeech 2 and VALL-E for expressive narration and character-specific voices, the framework employs advanced language models to automatically interpret textual narratives and generate realistic spatial audio effects. These sound effects are dynamically synchronized with the storyline through sophisticated temporal integration methods, including Dynamic Time Warping (DTW) and recurrent neural networks (RNNs). Diffusion-based generative models combined with higher-order ambisonics (HOA) and scattering delay networks (SDN) enable highly realistic 3D soundscapes, substantially enhancing listener immersion and narrative realism. This technology significantly advances audiobook applications, providing richer experiences for educational content, storytelling platforms, and accessibility solutions for visually impaired audiences. Future work will address personalization, ethical management of synthesized voices, and integration with multi-sensory platforms.

</details>

### [Advancing Zero-shot Text-to-Speech Intelligibility across Diverse Domains via Preference Alignment](2505.04113.md)
**Xueyao Zhang et.al.** · 2025-05-07

### [Miipher-2: A Universal Speech Restoration Model for Million-Hour Scale Data Restoration](2505.04457.md)
**Shigeki Karita, Yuma Koizumi, Heiga Zen, Haruko Ishikawa et al.** · 2025-05-07

<details>
<summary>Abstract</summary>

Training data cleaning is a new application for generative model-based speech restoration (SR). This paper introduces Miipher-2, an SR model designed for million-hour scale data, for training data cleaning for large-scale generative models like large language models. Key challenges addressed include generalization to unseen languages, operation without explicit conditioning (e.g., text, speaker ID), and computational efficiency. Miipher-2 utilizes a frozen, pre-trained Universal Speech Model (USM), supporting over 300 languages, as a robust, conditioning-free feature extractor. To optimize efficiency and minimize memory, Miipher-2 incorporates parallel adapters for predicting clean USM features from noisy inputs and employs the WaveFit neural vocoder for waveform synthesis. These components were trained on 3,000 hours of multi-lingual, studio-quality recordings with augmented degradations, while USM parameters remained fixed. Experimental results demonstrate Miipher-2's superior or comparable performance to conventional SR models in word-error-rate, speaker similarity, and both objective and subjective sound quality scores across all tested languages. Miipher-2 operates efficiently on consumer-grade accelerators, achieving a real-time factor of 0.0078, enabling the processing of a million-hour speech dataset in approximately three days using only 100 such accelerators.

</details>

### [Discrete Optimal Transport and Voice Conversion](2505.04382.md)
**Anton Selitskiy, Maitreya Kocharekar** · 2025-05-07

<details>
<summary>Abstract</summary>

We propose kDOT, a discrete optimal transport (OT) framework for voice conversion (VC) operating in a pretrained speech embedding space. In contrast to the averaging strategies used in kNN-VC and SinkVC, and the independence assumption adopted in MKL, our method employs the barycentric projection of the discrete OT plan to construct a transport map between source and target speaker embedding distributions. We conduct a comprehensive ablation study over the number of transported embeddings and systematically analyze the impact of source and target utterance duration. Experiments on LibriSpeech demonstrate that OT with barycentric projection consistently improves distribution alignment and often outperforms averaging-based approaches in terms of WER, MOS, and FAD. Furthermore, we show that applying discrete OT as a post-processing step can transform spoofed speech into samples that are misclassified as bona fide by a state-of-the-art spoofing detector. This demonstrates the strong domain adaptation capability of OT in embedding space, while also revealing important security implications for spoof detection systems.

</details>

### [SonicRAG : High Fidelity Sound Effects Synthesis Based on Retrival Augmented Generation](2505.03244.md)
**Yu-Ren Guo, Wen-Kai Tai** · 2025-05-06

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have demonstrated remarkable capabilities in natural language processing (NLP) and multimodal learning, with successful applications in text generation and speech synthesis, enabling a deeper understanding and generation of multimodal content. In the field of sound effects (SFX) generation, LLMs have been leveraged to orchestrate multiple models for audio synthesis. However, due to the scarcity of annotated datasets, and the complexity of temproal modeling. current SFX generation techniques still fall short in achieving high-fidelity audio. To address these limitations, this paper introduces a novel framework that integrates LLMs with existing sound effect databases, allowing for the retrieval, recombination, and synthesis of audio based on user requirements. By leveraging this approach, we enhance the diversity and quality of generated sound effects while eliminating the need for additional recording costs, offering a flexible and efficient solution for sound design and application.

</details>

### [LLaMA-Omni2: LLM-based Real-time Spoken Chatbot with Autoregressive Streaming Speech Synthesis](2505.02625.md)
**Qingkai Fang et.al.** · 2025-05-05

### [Generating Narrated Lecture Videos from Slides with Synchronized Highlights](2505.02966.md)
**Alexander Holmberg** · 2025-05-05

<details>
<summary>Abstract</summary>

Turning static slides into engaging video lectures takes considerable time and effort, requiring presenters to record explanations and visually guide their audience through the material. We introduce an end-to-end system designed to automate this process entirely. Given a slide deck, this system synthesizes a video lecture featuring AI-generated narration synchronized precisely with dynamic visual highlights. These highlights automatically draw attention to the specific concept being discussed, much like an effective presenter would. The core technical contribution is a novel highlight alignment module. This module accurately maps spoken phrases to locations on a given slide using diverse strategies (e.g., Levenshtein distance, LLM-based semantic analysis) at selectable granularities (line or word level) and utilizes timestamp-providing Text-to-Speech (TTS) for timing synchronization. We demonstrate the system's effectiveness through a technical evaluation using a manually annotated slide dataset with 1000 samples, finding that LLM-based alignment achieves high location accuracy (F1 > 92%), significantly outperforming simpler methods, especially on complex, math-heavy content. Furthermore, the calculated generation cost averages under $1 per hour of video, offering potential savings of two orders of magnitude compared to conservative estimates of manual production costs. This combination of high accuracy and extremely low cost positions this approach as a practical and scalable tool for transforming static slides into effective, visually-guided video lectures.

</details>

### [Towards Flow-Matching-based TTS without Classifier-Free Guidance](2504.20334.md)
**Yuzhe Liang et.al.** · 2025-05-02

### [Voice Cloning: Comprehensive Survey](2505.00579.md)
**Hussam Azzuni, Abdulmotaleb El Saddik** · 2025-05-01

<details>
<summary>Abstract</summary>

Voice Cloning has rapidly advanced in today's digital world, with many researchers and corporations working to improve these algorithms for various applications. This article aims to establish a standardized terminology for voice cloning and explore its different variations. It will cover speaker adaptation as the fundamental concept and then delve deeper into topics such as few-shot, zero-shot, and multilingual TTS within that context. Finally, we will explore the evaluation metrics commonly used in voice cloning research and related datasets. This survey compiles the available voice cloning algorithms to encourage research toward its generation and detection to limit its misuse.

</details>

### [Sadeed: Advancing Arabic Diacritization Through Small Language Model](2504.21635.md)
**Zeina Aldallal, Sara Chrouf, Khalil Hennara, Mohamed Motaism Hamed et al.** · 2025-04-30

<details>
<summary>Abstract</summary>

Arabic text diacritization remains a persistent challenge in natural language processing due to the language's morphological richness. In this paper, we introduce Sadeed, a novel approach based on a fine-tuned decoder-only language model adapted from Kuwain 1.5B Hennara et al. [2025], a compact model originally trained on diverse Arabic corpora. Sadeed is fine-tuned on carefully curated, high-quality diacritized datasets, constructed through a rigorous data-cleaning and normalization pipeline. Despite utilizing modest computational resources, Sadeed achieves competitive results compared to proprietary large language models and outperforms traditional models trained on similar domains. Additionally, we highlight key limitations in current benchmarking practices for Arabic diacritization. To address these issues, we introduce SadeedDiac-25, a new benchmark designed to enable fairer and more comprehensive evaluation across diverse text genres and complexity levels. Together, Sadeed and SadeedDiac-25 provide a robust foundation for advancing Arabic NLP applications, including machine translation, text-to-speech, and language learning tools.

</details>

### [Towards Film-Making Production Dialogue, Narration, Monologue Adaptive Moving Dubbing Benchmarks](2505.01450.md)
**Chaoyi Wang, Junjie Zheng, Zihao Chen, Shiyu Xia et al.** · 2025-04-30

<details>
<summary>Abstract</summary>

Movie dubbing has advanced significantly, yet assessing the real-world effectiveness of these models remains challenging. A comprehensive evaluation benchmark is crucial for two key reasons: 1) Existing metrics fail to fully capture the complexities of dialogue, narration, monologue, and actor adaptability in movie dubbing. 2) A practical evaluation system should offer valuable insights to improve movie dubbing quality and advancement in film production. To this end, we introduce Talking Adaptive Dubbing Benchmarks (TA-Dubbing), designed to improve film production by adapting to dialogue, narration, monologue, and actors in movie dubbing. TA-Dubbing offers several key advantages: 1) Comprehensive Dimensions: TA-Dubbing covers a variety of dimensions of movie dubbing, incorporating metric evaluations for both movie understanding and speech generation. 2) Versatile Benchmarking: TA-Dubbing is designed to evaluate state-of-the-art movie dubbing models and advanced multi-modal large language models. 3) Full Open-Sourcing: We fully open-source TA-Dubbing at https://github.com/woka- 0a/DeepDubber- V1 including all video suits, evaluation methods, annotations. We also continuously integrate new movie dubbing models into the TA-Dubbing leaderboard at https://github.com/woka- 0a/DeepDubber-V1 to drive forward the field of movie dubbing.

</details>

### [AlignDiT: Multimodal Aligned Diffusion Transformer for Synchronized Speech Generation](2504.20629.md)
**Jeongsoo Choi et.al.** · 2025-04-29

### [ClonEval: An Open Voice Cloning Benchmark](2504.20581.md)
**Iwona Christop et.al.** · 2025-04-29

### [TriniMark: A Robust Generative Speech Watermarking Method for Trinity-Level Traceability](2504.20532.md)
**Yue Li, Weizhi Liu, Kaiqing Lin, Dongdong Lin et al.** · 2025-04-29

<details>
<summary>Abstract</summary>

Diffusion-based speech generation has achieved remarkable fidelity, increasing the risk of misuse and unauthorized redistribution. However, most existing generative speech watermarking methods are developed for GAN-based pipelines, and watermarking for diffusion-based speech generation remains comparatively underexplored. In addition, prior work often focuses on content-level provenance, while support for model-level and user-level attribution is less mature. We propose \textbf{TriniMark}, a diffusion-based generative speech watermarking framework that targets trinity-level traceability, i.e., the ability to associate a generated speech sample with (i) the embedded watermark message (content-level provenance), (ii) the source generative model (model-level attribution), and (iii) the end user who requested generation (user-level traceability). TriniMark uses a lightweight encoder to embed watermark bits into time-domain speech features and reconstruct the waveform, and a temporal-aware gated convolutional decoder for reliable bit recovery. We further introduce a waveform-guided fine-tuning strategy to transfer watermarking capability into a diffusion model. Finally, we incorporate variable-watermark training so that a single trained model can embed different watermark messages at inference time, enabling scalable user-level traceability. Experiments on speech datasets indicate that TriniMark maintains speech quality while improving robustness to common single and compound signal-processing attacks, and it supports high-capacity watermarking for large-scale traceability.

</details>

### [Generative Adversarial Network based Voice Conversion: Techniques, Challenges, and Recent Advancements](2504.19197.md)
**Sandipan Dhar et.al.** · 2025-04-27

### [Muyan-TTS: A Trainable Text-to-Speech Model Optimized for Podcast Scenarios with a $50K Budget](2504.19146.md)
**Xin Li et.al.** · 2025-04-27

### [Evolution and Perspectives of Speech Synthesis Technology: From Parametric Synthesis to the Era of Large Language Models](s2:0f9866fa4f9d5a62b1391553ad6efa6954ffed55.md)
**Yuhao Guo, Guanyu Li, Chenyu Xie, Qian Sun** · 2025-04-25

<details>
<summary>Abstract</summary>

Speech synthesis technology has evolved over six decades from rule-based to data-driven and now knowledge-driven approaches. This paper reviews its development, from early parametric methods (e.g., Formant, LPC) to modern Large Language Models (LLMs), highlighting key breakthroughs and paradigm shifts. Traditional methods relied on handcrafted acoustic rules, while deep learning (e.g., WaveNet, Tacotron) enabled end-to-end natural-sounding synthesis. Recently, LLMs like VALL-E and Voicebox have transformed speech generation into conditional language modeling, enhancing zero-shot cloning and cross-language synthesis. We propose a three-stage” division of this evolution and discuss three key features of speech synthesis in the LLM era: (1) joint text-to-speech modeling, (2) dynamic style control, and (3) adaptive generation with limited samples. Despite achieving near-human naturalness (MOS 4.5), current systems face challenges like high computational cost, insufficient emotional expressiveness, and security risks. Future trends include lightweight deployment, multimodal generation, and self-learning systems, with ethical guidelines needed to address deepfake risks.

</details>

### [EmoVoice: LLM-based Emotional Text-To-Speech Model with Freestyle Text Prompting](2504.12867.md)
**Guanrou Yang et.al.** · 2025-04-22

### [Affect Models Have Weak Generalizability to Atypical Speech](2504.16283.md)
**Jaya Narain, Amrit Romana, Vikramjit Mitra, Colin Lea et al.** · 2025-04-22

<details>
<summary>Abstract</summary>

Speech and voice conditions can alter the acoustic properties of speech, which could impact the performance of paralinguistic models for affect for people with atypical speech. We evaluate publicly available models for recognizing categorical and dimensional affect from speech on a dataset of atypical speech, comparing results to datasets of typical speech. We investigate three dimensions of speech atypicality: intelligibility, which is related to pronounciation; monopitch, which is related to prosody, and harshness, which is related to voice quality. We look at (1) distributional trends of categorical affect predictions within the dataset, (2) distributional comparisons of categorical affect predictions to similar datasets of typical speech, and (3) correlation strengths between text and speech predictions for spontaneous speech for valence and arousal. We find that the output of affect models is significantly impacted by the presence and degree of speech atypicalities. For instance, the percentage of speech predicted as sad is significantly higher for all types and grades of atypical speech when compared to similar typical speech datasets. In a preliminary investigation on improving robustness for atypical speech, we find that fine-tuning models on pseudo-labeled atypical speech data improves performance on atypical speech without impacting performance on typical speech. Our results emphasize the need for broader training and evaluation datasets for speech emotion models, and for modeling approaches that are robust to voice and speech differences.

</details>

### [A Multi-Agent Framework for Automated Qinqiang Opera Script Generation Using Large Language Models](2504.15552.md)
**Gengxian Cao, Fengyuan Li, Hong Duan, Ye Yang et al.** · 2025-04-22

<details>
<summary>Abstract</summary>

This paper introduces a novel multi-Agent framework that automates the end to end production of Qinqiang opera by integrating Large Language Models , visual generation, and Text to Speech synthesis. Three specialized agents collaborate in sequence: Agent1 uses an LLM to craft coherent, culturally grounded scripts;Agent2 employs visual generation models to render contextually accurate stage scenes; and Agent3 leverages TTS to produce synchronized, emotionally expressive vocal performances. In a case study on Dou E Yuan, the system achieved expert ratings of 3.8 for script fidelity, 3.5 for visual coherence, and 3.8 for speech accuracy-culminating in an overall score of 3.6, a 0.3 point improvement over a Single Agent baseline. Ablation experiments demonstrate that removing Agent2 or Agent3 leads to drops of 0.4 and 0.5 points, respectively, underscoring the value of modular collaboration. This work showcases how AI driven pipelines can streamline and scale the preservation of traditional performing arts, and points toward future enhancements in cross modal alignment, richer emotional nuance, and support for additional opera genres.

</details>

### [Quantifying Source Speaker Leakage in One-to-One Voice Conversion](2504.15822.md)
**Scott Wellington, Xuechen Liu, Junichi Yamagishi** · 2025-04-22

<details>
<summary>Abstract</summary>

Using a multi-accented corpus of parallel utterances for use with commercial speech devices, we present a case study to show that it is possible to quantify a degree of confidence about a source speaker's identity in the case of one-to-one voice conversion. Following voice conversion using a HiFi-GAN vocoder, we compare information leakage for a range speaker characteristics; assuming a "worst-case" white-box scenario, we quantify our confidence to perform inference and narrow the pool of likely source speakers, reinforcing the regulatory obligation and moral duty that providers of synthetic voices have to ensure the privacy of their speakers' data.

</details>

### [A Fast Acoustic Model Based on Multi-Scale Feature Fusion Module for Text-To-Speech Synthesis](s2:81f35613dc5e76a10ffe8cc761d7eec9e119a77b.md)
**Jin-Hyok Song, S. Jong, Thae-Myong Kim, Guk-Chol Kim et al.** · 2025-04-22

<details>
<summary>Abstract</summary>

In the end-to-end Text-to-speech synthesis, the ability of acoustic model has important effects on the quality of the speech generated. In the acoustic model, the encoder and decoder are critical components, and usually Transformer is used. The previous works have a lack of ability to model the essential features of speech signal, as they model fixed length of features. There is also limitation of slow inference speed of the acoustic model due to the characteristics of the transformer including the high-computational multi-head self-attention layer. This limits the application of TTS in the low performance of devices such as embedded devices or mobile phones. In this paper, we propose a novel acoustic model to model the different length of features and improve the speed of generating synthetic speech and naturalness as compared to the conventional Transformer structure. Through the experiment, we confirmed that the proposed method improves the naturalness of synthetic speech and operation speed in the low performance of devices.

</details>

### [SOLIDO: A Robust Watermarking Method for Speech Synthesis via Low-Rank Adaptation](2504.15035.md)
**Yue Li et.al.** · 2025-04-21

### [DialogueAgents: A Hybrid Agent-Based Speech Synthesis Framework for Multi-Party Dialogue](2504.14482.md)
**Xiang Li, Duyi Pan, Hongru Xiao, Jiale Han et al.** · 2025-04-20

<details>
<summary>Abstract</summary>

Speech synthesis is crucial for human-computer interaction, enabling natural and intuitive communication. However, existing datasets involve high construction costs due to manual annotation and suffer from limited character diversity, contextual scenarios, and emotional expressiveness. To address these issues, we propose DialogueAgents, a novel hybrid agent-based speech synthesis framework, which integrates three specialized agents -- a script writer, a speech synthesizer, and a dialogue critic -- to collaboratively generate dialogues. Grounded in a diverse character pool, the framework iteratively refines dialogue scripts and synthesizes speech based on speech review, boosting emotional expressiveness and paralinguistic features of the synthesized dialogues. Using DialogueAgent, we contribute MultiTalk, a bilingual, multi-party, multi-turn speech dialogue dataset covering diverse topics. Extensive experiments demonstrate the effectiveness of our framework and the high quality of the MultiTalk dataset. We release the dataset and code https://github.com/uirlx/DialogueAgents to facilitate future research on advanced speech synthesis models and customized data generation.

</details>

### [Collective Learning Mechanism based Optimal Transport Generative Adversarial Network for Non-parallel Voice Conversion](2504.13791.md)
**Sandipan Dhar et.al.** · 2025-04-18

### [Prosody Predictor based Diffusion Models Techniques for Enhanced Speech Synthesis](s2:0eda71a1d570363cd56bdda1ce43ca3afac974d6.md)
**Dr. K. Aruna Bhaskar, D. Lal, Dr. M. Bhaskar, S. Sushma et al.** · 2025-04-18

<details>
<summary>Abstract</summary>

A prosody predictor based on a diffusion model is crucial to the new zero shot approach of voice synthesis. Since diffusion models excel at capturing complicated distributions, they are perfect for simulating the complex patterns of prosody in speech. These models have recently attracted interest in a number of generative tasks. By repeatedly changing an initial chaotic input into an output that nearly matches the intended goal, a diffusion model acts by gradually refining the input. The diffusion model iteratively refines an initial rough estimate of the prosody pattern in the context of prosody prediction. To get realistic sounding speech, it is necessary to capture small prosody fluctuations in pitch, length, and loudness. This approach enables the model to do just that. Training on massive speech corpora teaches the diffusion model-based prosody predictor to mimic reference speech in its prosody pattern generation. During inference, the model makes use of the learnt prosody patterns to anticipate the target speech’s prosody, guaranteeing that the produced speech is expressive and authentic, even while the speaker is unseen.

</details>

### [Voice Conversion with Diverse Intonation using Conditional Variational Auto-Encoder](2504.12005.md)
**Soobin Suh, Dabi Ahn, Heewoong Park, Jonghun Park** · 2025-04-16

<details>
<summary>Abstract</summary>

Voice conversion is a task of synthesizing an utterance with target speaker's voice while maintaining linguistic information of the source utterance. While a speaker can produce varying utterances from a single script with different intonations, conventional voice conversion models were limited to producing only one result per source input. To overcome this limitation, we propose a novel approach for voice conversion with diverse intonations using conditional variational autoencoder (CVAE). Experiments have shown that the speaker's style feature can be mapped into a latent space with Gaussian distribution. We have also been able to convert voices with more diverse intonation by making the posterior of the latent space more complex with inverse autoregressive flow (IAF). As a result, the converted voice not only has a diversity of intonations, but also has better sound quality than the model without CVAE.

</details>

### [GOAT-TTS: LLM-based Text-To-Speech Generation Optimized via A Dual-Branch Architecture](2504.12339.md)
**Yaodong Song et.al.** · 2025-04-15

### [Generalized Audio Deepfake Detection Using Frame-level Latent Information Entropy](2504.10819.md)
**Botao Zhao, Zuheng Kang, Yayun He, Xiaoyang Qu et al.** · 2025-04-15

<details>
<summary>Abstract</summary>

Generalizability, the capacity of a robust model to perform effectively on unseen data, is crucial for audio deepfake detection due to the rapid evolution of text-to-speech (TTS) and voice conversion (VC) technologies. A promising approach to differentiate between bonafide and spoof samples lies in identifying intrinsic disparities to enhance model generalizability. From an information-theoretic perspective, we hypothesize the information content is one of the intrinsic differences: bonafide sample represents a dense, information-rich sampling of the real world, whereas spoof sample is typically derived from lower-dimensional, less informative representations. To implement this, we introduce frame-level latent information entropy detector(f-InfoED), a framework that extracts distinctive information entropy from latent representations at the frame level to identify audio deepfakes. Furthermore, we present AdaLAM, which extends large pre-trained audio models with trainable adapters for enhanced feature extraction. To facilitate comprehensive evaluation, the audio deepfake forensics 2024 (ADFF 2024) dataset was built by the latest TTS and VC methods. Extensive experiments demonstrate that our proposed approach achieves state-of-the-art performance and exhibits remarkable generalization capabilities. Further analytical studies confirms the efficacy of AdaLAM in extracting discriminative audio features and f-InfoED in leveraging latent entropy information for more generalized deepfake detection.

</details>

### [Pseudo-Autoregressive Neural Codec Language Models for Efficient Zero-Shot Text-to-Speech Synthesis](2504.10352.md)
**Yifan Yang et.al.** · 2025-04-14

### [AutoStyle-TTS: Retrieval-Augmented Generation based Automatic Style Matching Text-to-Speech Synthesis](2504.10309.md)
**Dan Luo, Chengyuan Ma, Weiqin Li, Jun Wang et al.** · 2025-04-14

<details>
<summary>Abstract</summary>

With the advancement of speech synthesis technology, users have higher expectations for the naturalness and expressiveness of synthesized speech. But previous research ignores the importance of prompt selection. This study proposes a text-to-speech (TTS) framework based on Retrieval-Augmented Generation (RAG) technology, which can dynamically adjust the speech style according to the text content to achieve more natural and vivid communication effects. We have constructed a speech style knowledge database containing high-quality speech samples in various contexts and developed a style matching scheme. This scheme uses embeddings, extracted by Llama, PER-LLM-Embedder,and Moka, to match with samples in the knowledge database, selecting the most appropriate speech style for synthesis. Furthermore, our empirical research validates the effectiveness of the proposed method. Our demo can be viewed at: https://thuhcsi.github.io/icme2025-AutoStyle-TTS

</details>

### [SafeSpeech: Robust and Universal Voice Protection Against Malicious Speech Synthesis](2504.09839.md)
**Zhisheng Zhang, Derui Wang, Qianyi Yang, Pengyang Huang et al.** · 2025-04-14

<details>
<summary>Abstract</summary>

Speech synthesis technology has brought great convenience, while the widespread usage of realistic deepfake audio has triggered hazards. Malicious adversaries may unauthorizedly collect victims' speeches and clone a similar voice for illegal exploitation (\textit{e.g.}, telecom fraud). However, the existing defense methods cannot effectively prevent deepfake exploitation and are vulnerable to robust training techniques. Therefore, a more effective and robust data protection method is urgently needed. In response, we propose a defensive framework, \textit{\textbf{SafeSpeech}}, which protects the users' audio before uploading by embedding imperceptible perturbations on original speeches to prevent high-quality synthetic speech. In SafeSpeech, we devise a robust and universal proactive protection technique, \textbf{S}peech \textbf{PE}rturbative \textbf{C}oncealment (\textbf{SPEC}), that leverages a surrogate model to generate universally applicable perturbation for generative synthetic models. Moreover, we optimize the human perception of embedded perturbation in terms of time and frequency domains. To evaluate our method comprehensively, we conduct extensive experiments across advanced models and datasets, both subjectively and objectively. Our experimental results demonstrate that SafeSpeech achieves state-of-the-art (SOTA) voice protection effectiveness and transferability and is highly robust against advanced adaptive adversaries. Moreover, SafeSpeech has real-time capability in real-world tests. The source code is available at \href{https://github.com/wxzyd123/SafeSpeech}{https://github.com/wxzyd123/SafeSpeech}.

</details>

### [AMNet: An Acoustic Model Network for Enhanced Mandarin Speech Synthesis](2504.09225.md)
**Yubing Cao, Yinfeng Yu, Yongming Li, Liejun Wang** · 2025-04-12

<details>
<summary>Abstract</summary>

This paper presents AMNet, an Acoustic Model Network designed to improve the performance of Mandarin speech synthesis by incorporating phrase structure annotation and local convolution modules. AMNet builds upon the FastSpeech 2 architecture while addressing the challenge of local context modeling, which is crucial for capturing intricate speech features such as pauses, stress, and intonation. By embedding a phrase structure parser into the model and introducing a local convolution module, AMNet enhances the model's sensitivity to local information. Additionally, AMNet decouples tonal characteristics from phonemes, providing explicit guidance for tone modeling, which improves tone accuracy and pronunciation. Experimental results demonstrate that AMNet outperforms baseline models in subjective and objective evaluations. The proposed model achieves superior Mean Opinion Scores (MOS), lower Mel Cepstral Distortion (MCD), and improved fundamental frequency fitting $F0 (R^2)$, confirming its ability to generate high-quality, natural, and expressive Mandarin speech.

</details>

### ["It's not a representation of me": Examining Accent Bias and Digital Exclusion in Synthetic AI Voice Services](2504.09346.md)
**Shira Michel, Sufi Kaur, Sarah Elizabeth Gillespie, Jeffrey Gleason et al.** · 2025-04-12

<details>
<summary>Abstract</summary>

Recent advances in artificial intelligence (AI) speech generation and voice cloning technologies have produced naturalistic speech and accurate voice replication, yet their influence on sociotechnical systems across diverse accents and linguistic traits is not fully understood. This study evaluates two synthetic AI voice services (Speechify and ElevenLabs) through a mixed methods approach using surveys and interviews to assess technical performance and uncover how users' lived experiences influence their perceptions of accent variations in these speech technologies. Our findings reveal technical performance disparities across five regional, English-language accents and demonstrate how current speech generation technologies may inadvertently reinforce linguistic privilege and accent-based discrimination, potentially creating new forms of digital exclusion. Overall, our study highlights the need for inclusive design and regulation by providing actionable insights for developers, policymakers, and organizations to ensure equitable and socially responsible AI speech technologies.

</details>

### [SIFT-50M: A Large-Scale Multilingual Dataset for Speech Instruction Fine-Tuning](2504.09081.md)
**Prabhat Pandey, Rupak Vignesh Swaminathan, K V Vijay Girish, Arunasish Sen et al.** · 2025-04-12

<details>
<summary>Abstract</summary>

We introduce SIFT (Speech Instruction Fine-Tuning), a 50M-example dataset designed for instruction fine-tuning and pre-training of speech-text large language models (LLMs). SIFT-50M is built from publicly available speech corpora, which collectively contain 14K hours of speech, and leverages LLMs along with off-the-shelf expert models. The dataset spans five languages, encompassing a diverse range of speech understanding as well as controllable speech generation instructions. Using SIFT-50M, we train SIFT-LLM, which outperforms existing speech-text LLMs on instruction-following benchmarks while achieving competitive performance on foundational speech tasks. To support further research, we also introduce EvalSIFT, a benchmark dataset specifically designed to evaluate the instruction-following capabilities of speech-text LLMs.

</details>

### [Generalized Multilingual Text-to-Speech Generation with Language-Aware Style Adaptation](2504.08274.md)
**Haowei Lou et.al.** · 2025-04-11

### [USM-VC: Mitigating Timbre Leakage with Universal Semantic Mapping Residual Block for Voice Conversion](2504.08524.md)
**Na Li, Chuke Wang, Yu Gu, Zhifeng Li** · 2025-04-11

<details>
<summary>Abstract</summary>

Voice conversion (VC) transforms source speech into a target voice by preserving the content. However, timbre information from the source speaker is inherently embedded in the content representations, causing significant timbre leakage and reducing similarity to the target speaker. To address this, we introduce a Universal Semantic Matching (USM) residual block to a content extractor. The residual block consists of two weighted branches: 1) universal semantic dictionary based Content Feature Re-expression (CFR) module, supplying timbre-free content representation. 2) skip connection to the original content layer, providing complementary fine-grained information. In the CFR module, each dictionary entry in the universal semantic dictionary represents a phoneme class, computed statistically using speech from multiple speakers, creating a stable, speaker-independent semantic set. We introduce a CFR method to obtain timbre-free content representations by expressing each content frame as a weighted linear combination of dictionary entries using corresponding phoneme posteriors as weights. Extensive experiments across various VC frameworks demonstrate that our approach effectively mitigates timbre leakage and significantly improves similarity to the target speaker.

</details>

### [StableVC: Style Controllable Zero-Shot Voice Conversion with Conditional Flow Matching](s2:6cf3630b618be023c348f4c2376c64d6471fcaa2.md)
**Jixun Yao, Yuguang Yang, Yu Pan, Ziqian Ning et al.** · 2025-04-11

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) aims to transfer the timbre from the source speaker to an arbitrary unseen speaker while preserving the original linguistic content. Despite recent advancements in zero-shot VC using language model-based or diffusion-based approaches, several challenges remain: 1) current approaches primarily focus on adapting timbre from unseen speakers and are unable to transfer style and timbre to different unseen speakers independently; 2) these approaches often suffer from slower inference speeds due to the autoregressive modeling methods or the need for numerous sampling steps; 3) the quality and similarity of the converted samples are still not fully satisfactory. To address these challenges, we propose a Style controllable zero-shot VC approach named StableVC, which aims to transfer timbre and style from source speech to different unseen target speakers. Specifically, we decompose speech into linguistic content, timbre, and style, and then employ a conditional flow matching module to reconstruct the high-quality mel-spectrogram based on these decomposed features. To effectively capture timbre and style in a zero-shot manner, we introduce a novel dual attention mechanism with an adaptive gate, rather than using conventional feature concatenation. With this non-autoregressive design, StableVC can efficiently capture the intricate timbre and style from different unseen speakers and generate high-quality speech significantly faster than real-time. Experiments demonstrate that our proposed StableVC outperforms state-of-the-art baseline systems in zero-shot VC and achieves flexible control over timbre and style from different unseen speakers. Moreover, StableVC offers approximately 25x and 1.65x faster sampling compared to autoregressive and diffusion-based baselines.

</details>

### [Empowering Global Voices: A Data-Efficient, Phoneme-Tone Adaptive Approach to High-Fidelity Speech Synthesis](2504.07858.md)
**Yizhong Geng et.al.** · 2025-04-10

### [SlimSpeech: Lightweight and Efficient Text-to-Speech with Slim Rectified Flow](2504.07776.md)
**Kaidi Wang, Wenhao Guan, Shenghui Lu, Jianglong Yao et al.** · 2025-04-10

<details>
<summary>Abstract</summary>

Recently, flow matching based speech synthesis has significantly enhanced the quality of synthesized speech while reducing the number of inference steps. In this paper, we introduce SlimSpeech, a lightweight and efficient speech synthesis system based on rectified flow. We have built upon the existing speech synthesis method utilizing the rectified flow model, modifying its structure to reduce parameters and serve as a teacher model. By refining the reflow operation, we directly derive a smaller model with a more straight sampling trajectory from the larger model, while utilizing distillation techniques to further enhance the model performance. Experimental results demonstrate that our proposed method, with significantly reduced model parameters, achieves comparable performance to larger models through one-step sampling.

</details>

### [F5R-TTS: Improving Flow-Matching based Text-to-Speech with Group Relative Policy Optimization](2504.02407.md)
**Xiaohui Sun et.al.** · 2025-04-09

### [TASTE: Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling](2504.07053.md)
**Liang-Hsuan Tseng, Yi-Chang Chen, Kuan-Yi Lee, Da-Shan Shiu et al.** · 2025-04-09

<details>
<summary>Abstract</summary>

Recent efforts target spoken language models (SLMs) that not only listen but also speak for more natural human-LLM interaction. Joint speech-text modeling is a promising direction to achieve this. However, the effectiveness of recent speech tokens for joint modeling remains underexplored. To address this, we introduce Text-Aligned Speech Tokenization and Embedding (TASTE), a method that directly addresses the modality gap by aligning speech token with the corresponding text transcription during the tokenization stage. We propose a method that can achieve this through a attention-based aggregation mechanism and with speech reconstruction as the training objective. We conduct extensive experiments and show that TASTE can preserve essential paralinguistic information while dramatically reducing the token sequence length. With TASTE, we perform straightforward joint spoken language modeling by using Low-Rank Adaptation on the pre-trained text LLM. Experimental results show that TASTE-based SLMs perform comparable to previous work on SALMON and StoryCloze; while significantly outperform other pre-trained SLMs on speech continuation across subjective and objective evaluations. To our knowledge, TASTE is the first end-to-end approach that utilizes a reconstruction objective to automatically learn a text-aligned speech tokenization and embedding suitable for spoken language modeling. Our demo, code, and model are available at https://mtkresearch.github.io/TASTE-SpokenLM.github.io.

</details>

### [AVENet: Disentangling Features by Approximating Average Features for Voice Conversion](2504.05833.md)
**Wenyu Wang, Yiquan Zhou, Jihua Zhu, Hongwu Ding et al.** · 2025-04-08

<details>
<summary>Abstract</summary>

Voice conversion (VC) has made progress in feature disentanglement, but it is still difficult to balance timbre and content information. This paper evaluates the pre-trained model features commonly used in voice conversion, and proposes an innovative method for disentangling speech feature representations. Specifically, we first propose an ideal content feature, referred to as the average feature, which is calculated by averaging the features within frame-level aligned parallel speech (FAPS) data. For generating FAPS data, we utilize a technique that involves freezing the duration predictor in a Text-to-Speech system and manipulating speaker embedding. To fit the average feature on traditional VC datasets, we then design the AVENet to take features as input and generate closely matching average features. Experiments are conducted on the performance of AVENet-extracted features within a VC system. The experimental results demonstrate its superiority over multiple current speech feature disentangling methods. These findings affirm the effectiveness of our disentanglement approach.

</details>

### [kNN-SVC: Robust Zero-Shot Singing Voice Conversion with Additive Synthesis and Concatenation Smoothness Optimization](2504.05686.md)
**Keren Shao, Ke Chen, Matthew Baas, Shlomo Dubnov** · 2025-04-08

<details>
<summary>Abstract</summary>

Robustness is critical in zero-shot singing voice conversion (SVC). This paper introduces two novel methods to strengthen the robustness of the kNN-VC framework for SVC. First, kNN-VC's core representation, WavLM, lacks harmonic emphasis, resulting in dull sounds and ringing artifacts. To address this, we leverage the bijection between WavLM, pitch contours, and spectrograms to perform additive synthesis, integrating the resulting waveform into the model to mitigate these issues. Second, kNN-VC overlooks concatenative smoothness, a key perceptual factor in SVC. To enhance smoothness, we propose a new distance metric that filters out unsuitable kNN candidates and optimize the summing weights of the candidates during inference. Although our techniques are built on the kNN-VC framework for implementation convenience, they are broadly applicable to general concatenative neural synthesis models. Experimental results validate the effectiveness of these modifications in achieving robust SVC. Demo: http://knnsvc.com Code: https://github.com/SmoothKen/knn-svc

</details>

### [P2Mark: Plug-and-play Parameter-intrinsic Watermarking for Neural Speech Generation](2504.05197.md)
**Yong Ren et.al.** · 2025-04-07

### [DistillW2N: A Lightweight One-Shot Whisper to Normal Voice Conversion Model Using Distillation of Self-Supervised Features](s2:f7373dc1c5db7ff86bde948a3ca7084092abb9f3.md)
**Tianyi Tan, Haoxin Ruan, Xin'an Chen, Kai-Jyun Chen et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

Whisper to Normal voice conversion (W2N) holds great promise for assistive communication and healthcare, making it an exciting area of research and development. Recent advancements in W2N are predominantly driven by self-supervised speech representation learning (SSL) techniques. While effective, SSL requires extensive parameters and high computational costs, making it impractical to be deployed in real-world applications. We propose DistillW2N, a lightweight one-shot W2N model. DistillW2N consists of a speech-to-unit (S2U) encoder, which seeks to close the gap between whispered and normal content units by distilling HuBERT-Soft representations from both normal speech and pseudo-whisper, and a unit-to-speech (U2S) decoder, which incorporates content units with timbre units by Style-Adaptive Layer Normalization (SALN) and leverages SoundStream decoder for lightweight high-quality speech synthesis. Moreover, we discover that the S2U encoder is able to learn from a VAD model to trim noise. Experiments show that DistillW2N significantly improves the intelligibility for whisper while preserving speaker similarity compared to prevailing SSL approaches. The resulting model demands only 10.91 M parameters and 1.63 GMACs per second and runs approximately 5 times faster than QuickVC. All samples and code are available at https://github.com/tan90xx/distillw2n.

</details>

### [Black-Box Adversarial Defense Against Voice Conversion Using Latent Space Perturbation](s2:e556e56e99168c738bfc262833e56976f415c364.md)
**Jie Gao, Haiyun Li, Zhisheng Zhang, Zhiyong Wu** · 2025-04-06

<details>
<summary>Abstract</summary>

Voice Conversion (VC) technologies have advanced significantly, enabling voice cloning with just a few seconds of audio, posing serious risks to privacy, property, and reputation. In response to these threats, adversarial defense methods protect users by adding imperceptible perturbations to the audio, making it harder for VC models to clone the original voice. However, current methods are effective in white-box scenarios but struggle in black-box settings where VC models' internal parameters and structures are unknown. To address this problem, we propose a black-box adversarial defense method that effectively adapts and defends against unknown VC models relies solely on black-box feedback. We introduce a latent perturbation model that compresses speech and generates initial perturbations to reduce the search space and ensure convergence for black-box optimization. We then apply evolution-based black-box optimization to refine the perturbations, improving defense performance against unknown VC models. Extensive experiments on state-of-the-art VC models demonstrate the adaptability and superior defense performance of our method in real-world black-box scenarios compared to other defence approaches. Demo is available at https://g-bety.github.io/advdense.

</details>

### [Mora-Level Prosody Prediction for Text-to-Speech Using Japanese BERT Without Accentual Labels](s2:21bb4265cdf1f917c55e6930eb0a983b1ea42360.md)
**Tadashi Ogura, T. Okamoto, Yamato Ohtani, Erica Cooper et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

In practical text-to-speech (TTS) for pitch accent languages, such as Japanese, high-fidelity synthesis with correct prosody requires not only a phoneme sequence but also accentual information. Although accentual information can be obtained from accent dictionaries, words not included in the dictionaries and accent sandhi are sometimes synthesized with incorrect prosody, and manual registration of huge amounts of accent data is costly. Additionally, previous machine learning-based data-driven accent information estimation approaches for TTS also require huge quantities of handcrafted accentual labels during training. This paper proposes a data-driven prosody prediction method for Japanese TTS that uses Japanese BERT and does not require any accentual labels during training. A Japanese TTS acoustic model with mora-level (katakana sequence) input is first trained and mora-level fundamental frequency values (fo), which directly correspond to the prosody, are extracted for the training data using forced alignment. Then, a pre-trained Japanese BERT is finetuned for the mora-level fo prediction task with word sequences including kanji and the corresponding katakana sequences as input and the mora-level fo extracted using forced alignment as the prediction target. During TTS inference, the mora-level fo sequence predicted by the finetuned Japanese BERT is input to the TTS acoustic model along with the katakana input, and correct prosodic synthesis can be realized thanks to this predicted fo sequence. Experimental results demonstrate that the proposed method can realize the same synthesis quality and higher accent correctness compared with conventional neural TTS models with accentual labels.

</details>

### [Factorized-VITS: Decoupling Prosody and Text in End-to-End Speech Synthesis without External or Secondary Aligner](s2:bcaf9448e14b750ba5f9eb47770a7aa3012515bf.md)
**Yining Liu, Alexander Waibel** · 2025-04-06

<details>
<summary>Abstract</summary>

We propose Factorized-VITS, an advanced end-to-end text-to-speech model that incorporates explicit text-side prosody modeling control into VITS while achieving a clean factorization of the audio prior hidden space into text and prosody subspaces. Unlike previous works that rely on external or secondary aligners, Factorized-VITS is the first work attempting to do on-the-fly alignment in the factorized text subspace without introducing extra parameters, which not only simplifies the training procedure but also enables the use of a more complex prosody prior. Our experiments demonstrate the accuracy and effectiveness of this approximation strategy. Furthermore, we implement an in-context learning joint predictor for pitch, energy, and duration, which offers a flexible streaming deployment option.

</details>

### [LEF-TTS: Lightweight and Efficient End-to-End Text-to-Speech Synthesis With Multi-Stream Generator](s2:6696db4d55250727c9bbd0433796d3c1a671cf1b.md)
**Yan Shi, Jin Shi, Minchuan Chen, Chenfeng Miao et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

Recently, the field of Text-to-speech synthesis has been predominantly characterized by end-to-end models, with the quality of speech generated by these models becoming increasingly comparable to that of human speech. In this work, we propose a Lightweight and Efficient Text-to-speech model, a fast end-to-end framework based on EfficientTTS 2 with fully differentiable. We utilize Fast Linear Attention with a Single Head instead of the standard stacked Transformer, which decreases computational complexity and reduces parameters. Additionally, we improve a network architecture ConvWaveNet to further decrease model parameters, and accelerate inference through a multi-stream inverse short-time Fourier Transform generator. These improvements significantly reduce model parameters and increase inference speed, thereby achieving the objectives of faster inference and lightweight modeling. Experimental results show that the proposed model achieves speech quality comparable to that of the baseline models, while also offering improved inference speed and reduced model size.

</details>

### [Universal Low-Resource Speech Synthesis Via Phoneme Fusion Coordinating Low-Rank Decomposition](s2:cdabdb1d602ab0c1e5d9fc45d76057db01f1d2a7.md)
**Yanliang Li, Zhengtao Yu, Linqin Wang, Shengxiang Gao et al.** · 2025-04-06

<details>
<summary>Abstract</summary>

Recent advancements in end-to-end text-to-speech models have made significant progress. However, these approaches based on high-resource languages, are inapplicable for low-resource languages, and existing low-resource speech synthesis methods are typically specific to single languages. Consequently, the pursuit of a universal methodology for low-resource speech synthesis emerges as a critical problem that requires immediate attention. Unlike previous works, we propose a novel and universal approach for multiple low-resource languages by leveraging phoneme fusion coordinating low-rank decomposition in a pre-trained multilingual model. Specifically, by establishing a multilingual phoneme dictionary through phoneme fusion and applying parameter freezing and matrix decomposition techniques for fine-tuning, the proposed method was extensively evaluated across four different languages, each utilizing approximately 3 hours of speech data. The experimental results demonstrate that the quality of the synthesized speech surpasses current mainstream methods for low-resource speech synthesis, achieving outcomes comparable to those trained with tens of hours of data. Audio samples are available at https://priankaan.github.io/Demo.github.io.

</details>

### [VocalNet: Speech LLM with Multi-Token Prediction for Faster and High-Quality Generation](2504.04060.md)
**Yuhao Wang, Heyang Liu, Ziyang Cheng, Ronghua Wu et al.** · 2025-04-05

<details>
<summary>Abstract</summary>

Speech large language models (LLMs) have emerged as a prominent research focus in speech processing. We introduce VocalNet-1B and VocalNet-8B, a series of high-performance, low-latency speech LLMs enabled by a scalable and model-agnostic training framework designed for real-time voice interaction. Central to our contribution is the first application of multi-token prediction (MTP) to speech LLMs. This approach represents a paradigm shift from standard next-token prediction (NTP), offering simultaneous improvements in generation speed and quality. Informed by analysis of MTP's effect on speech generation and experimental comparisons, we designed a straightforward and highly effective MTP implementation. Experiments demonstrate that VocalNet performs on par with mainstream Omni LLMs even with limited training data, and significantly surpasses existing open-source speech LLMs. To foster reproducibility and community advancement, all model weights, inference code, training data, and framework implementations have been made publicly available at https://github.com/SJTU-OmniAgent/VocalNet

</details>

### [RWKVTTS: Yet another TTS based on RWKV-7](2504.03289.md)
**Lin yueyu, Liu Xiao** · 2025-04-04

<details>
<summary>Abstract</summary>

Human-AI interaction thrives on intuitive and efficient interfaces, among which voice stands out as a particularly natural and accessible modality. Recent advancements in transformer-based text-to-speech (TTS) systems, such as Fish-Speech, CosyVoice, and MegaTTS 3, have delivered remarkable improvements in quality and realism, driving a significant evolution in the TTS domain. In this paper, we introduce RWKV-7 \cite{peng2025rwkv}, a cutting-edge RNN-based architecture tailored for TTS applications. Unlike traditional transformer models, RWKV-7 leverages the strengths of recurrent neural networks to achieve greater computational efficiency and scalability, while maintaining high-quality output. Our comprehensive benchmarks demonstrate that RWKV-7 outperforms transformer-based models across multiple key metrics, including synthesis speed, naturalness of speech, and resource efficiency. Furthermore, we explore its adaptability to diverse linguistic contexts and low-resource environments, showcasing its potential to democratize TTS technology. These findings position RWKV-7 as a powerful and innovative alternative, paving the way for more accessible and versatile voice synthesis solutions in real-world applications.Our code and weights are https://github.com/yynil/RWKVTTS, https://huggingface.co/spaces/RWKV-Red-Team

</details>

### [VoiceCraft-Dub: Automated Video Dubbing with Neural Codec Language Models](2504.02386.md)
**Kim Sung-Bin et.al.** · 2025-04-03

### [SVLA: A Unified Speech-Vision-Language Assistant with Multimodal Reasoning and Speech Generation](2503.24164.md)
**Ngoc Dung Huynh et.al.** · 2025-03-31

### [SpeechDialogueFactory: Generating High-Quality Speech Dialogue Data to Accelerate Your Speech-LLM Development](2503.23848.md)
**Minghan Wang, Ye Bai, Yuxia Wang, Thuy-Trang Vu et al.** · 2025-03-31

<details>
<summary>Abstract</summary>

High-quality speech dialogue datasets are crucial for Speech-LLM development, yet existing acquisition methods face significant limitations. Human recordings incur high costs and privacy concerns, while synthetic approaches often lack conversational authenticity. To address these challenges, we introduce \textsc{SpeechDialogueFactory}, a production-ready framework for generating natural speech dialogues efficiently. Our solution employs a comprehensive pipeline including metadata generation, dialogue scripting, paralinguistic-enriched utterance simulation, and natural speech synthesis with voice cloning. Additionally, the system provides an interactive UI for detailed sample inspection and a high-throughput batch synthesis mode. Evaluations show that dialogues generated by our system achieve a quality comparable to human recordings while significantly reducing production costs. We release our work as an open-source toolkit, alongside example datasets available in English and Chinese, empowering researchers and developers in Speech-LLM research and development.

</details>

### [Can Diffusion Models Disentangle? A Theoretical Perspective](2504.00220.md)
**Liming Wang, Muhammad Jehanzeb Mirza, Yishu Gong, Yuan Gong et al.** · 2025-03-31

<details>
<summary>Abstract</summary>

This paper presents a novel theoretical framework for understanding how diffusion models can learn disentangled representations. Within this framework, we establish identifiability conditions for general disentangled latent variable models, analyze training dynamics, and derive sample complexity bounds for disentangled latent subspace models. To validate our theory, we conduct disentanglement experiments across diverse tasks and modalities, including subspace recovery in latent subspace Gaussian mixture models, image colorization, image denoising, and voice conversion for speech classification. Additionally, our experiments show that training strategies inspired by our theory, such as style guidance regularization, consistently enhance disentanglement performance.

</details>

### [DeepDubber-V1: Towards High Quality and Dialogue, Narration, Monologue Adaptive Movie Dubbing Via Multi-Modal Chain-of-Thoughts Reasoning Guidance](2503.23660.md)
**Junjie Zheng, Zihao Chen, Chaofan Ding, Xinhan Di** · 2025-03-31

<details>
<summary>Abstract</summary>

Current movie dubbing technology can generate the desired voice from a given speech prompt, ensuring good synchronization between speech and visuals while accurately conveying the intended emotions. However, in movie dubbing, key aspects such as adapting to different dubbing styles, handling dialogue, narration, and monologue effectively, and understanding subtle details like the age and gender of speakers, have not been well studied. To address this challenge, we propose a framework of multi-modal large language model. First, it utilizes multimodal Chain-of-Thought (CoT) reasoning methods on visual inputs to understand dubbing styles and fine-grained attributes. Second, it generates high-quality dubbing through large speech generation models, guided by multimodal conditions. Additionally, we have developed a movie dubbing dataset with CoT annotations. The evaluation results demonstrate a performance improvement over state-of-the-art methods across multiple datasets. In particular, for the evaluation metrics, the SPK-SIM and EMO-SIM increases from 82.48% to 89.74%, 66.24% to 78.88% for dubbing setting 2.0 on V2C Animation dataset, LSE-D and MCD-SL decreases from 14.79 to 14.63, 5.24 to 4.74 for dubbing setting 2.0 on Grid dataset, SPK-SIM increases from 64.03 to 83.42 and WER decreases from 52.69% to 23.20% for initial reasoning setting on proposed CoT-Movie-Dubbing dataset in the comparison with the state-of-the art models.

</details>

### [Speculative End-Turn Detector for Efficient Speech Chatbot Assistant](2503.23439.md)
**Hyunjong Ok, Suho Yoo, Jaeho Lee** · 2025-03-30

<details>
<summary>Abstract</summary>

Spoken dialogue systems powered by large language models have demonstrated remarkable abilities in understanding human speech and generating appropriate spoken responses. However, these systems struggle with end-turn detection (ETD) -- the ability to distinguish between user turn completion and hesitation. This limitation often leads to premature or delayed responses, disrupting the flow of spoken conversations. In this paper, we introduce the ETD Dataset, the first public dataset for end-turn detection. The ETD dataset consists of both synthetic speech data generated with text-to-speech models and real-world speech data collected from web sources. We also propose SpeculativeETD, a novel collaborative inference framework that balances efficiency and accuracy to improve real-time ETD in resource-constrained environments. Our approach jointly employs a lightweight GRU-based model, which rapidly detects the non-speaking units in real-time on local devices, and a high-performance Wav2vec-based model running on the server to make a more challenging classification of distinguishing turn ends from mere pauses. Experiments demonstrate that the proposed SpeculativeETD significantly improves ETD accuracy while keeping the required computations low. Datasets and code will be available after the review.

</details>

### [SupertonicTTS: Towards Highly Efficient and Streamlined Text-to-Speech System](2503.23108.md)
**Hyeongju Kim, Jinhyeok Yang, Yechan Yu, Seunghun Ji et al.** · 2025-03-29

<details>
<summary>Abstract</summary>

We introduce SupertonicTTS, a novel text-to-speech (TTS) system designed for efficient and streamlined speech synthesis. SupertonicTTS comprises three components: a speech autoencoder for continuous latent representation, a text-to-latent module leveraging flow-matching for text-to-latent mapping, and an utterance-level duration predictor. To enable a lightweight architecture, we employ a low-dimensional latent space, temporal compression of latents, and ConvNeXt blocks. The TTS pipeline is further simplified by operating directly on raw character-level text and employing cross-attention for text-speech alignment, thus eliminating the need for grapheme-to-phoneme (G2P) modules and external aligners. In addition, we propose context-sharing batch expansion that accelerates loss convergence and stabilizes text-speech alignment with minimal memory and I/O overhead. Experimental results demonstrate that SupertonicTTS delivers performance comparable to contemporary zero-shot TTS models with only 44M parameters, while significantly reducing architectural complexity and computational cost. Audio samples are available at: https://supertonictts.github.io/.

</details>

### [DeepAudio-V1:Towards Multi-Modal Multi-Stage End-to-End Video to Speech and Audio Generation](2503.22265.md)
**Haomin Zhang et.al.** · 2025-03-28

### [Text-Driven Voice Conversion via Latent State-Space Modeling](2503.20999.md)
**Wen Li, Sofia Martinez, Priyanka Shah** · 2025-03-26

<details>
<summary>Abstract</summary>

Text-driven voice conversion allows customization of speaker characteristics and prosodic elements using textual descriptions. However, most existing methods rely heavily on direct text-to-speech training, limiting their flexibility in controlling nuanced style elements or timbral features. In this paper, we propose a novel \textbf{Latent State-Space} approach for text-driven voice conversion (\textbf{LSS-VC}). Our method treats each utterance as an evolving dynamical system in a continuous latent space. Drawing inspiration from mamba, which introduced a state-space model for efficient text-driven \emph{image} style transfer, we adapt a loosely related methodology for \emph{voice} style transformation. Specifically, we learn a voice latent manifold where style and content can be manipulated independently by textual style prompts. We propose an adaptive cross-modal fusion mechanism to inject style information into the voice latent representation, enabling interpretable and fine-grained control over speaker identity, speaking rate, and emphasis. Extensive experiments show that our approach significantly outperforms recent baselines in both subjective and objective quality metrics, while offering smoother transitions between styles, reduced artifacts, and more precise text-based style control.

</details>

### [FireRedTTS-1S: An Upgraded Streamable Foundation Text-to-Speech System](2503.20499.md)
**Hao-Han Guo, Yao Hu, Fei-Yu Shen, Xu Tang et al.** · 2025-03-26

<details>
<summary>Abstract</summary>

In this work, we upgrade FireRedTTS to a new version, FireRedTTS-1S, a high-quality streaming foundation text-to-speech system. FireRedTTS-1S achieves streaming speech generation via two steps: text-to-semantic decoding and semantic-to-acoustic decoding. In text-to-semantic decoding, a semantic-aware speech tokenizer converts the speech signal into semantic tokens, which can be synthesized from the text via a language model in an auto-regressive manner. Meanwhile, the semantic-to-acoustic decoding module simultaneously translates generated semantic tokens into the speech signal in a streaming way. We implement two approaches to achieve this module: 1) a chunk-wise streamable flow-matching approach, and 2) a multi-stream language model-based approach. They both present high-quality and streamable speech generation but differ in real-time factor (RTF) and latency. Specifically, flow-matching decoding can generate speech by chunks, presenting a lower RTF of 0.1 but a higher latency of 300ms. Instead, the multi-stream language model generates speech by frames in an autoregressive manner, presenting a higher RTF of 0.3 but a low latency of 150ms. In experiments on zero-shot voice cloning, the objective results validate FireRedTTS-1S as a high-quality foundation model with comparable intelligibility and speaker similarity over industrial baseline systems. Furthermore, the subjective score of FireRedTTS-1S highlights its impressive synthesis performance, achieving comparable quality to the ground-truth recordings. These results validate FireRedTTS-1S as a high-quality streaming foundation TTS system.

</details>

### [Dual Audio-Centric Modality Coupling for Talking Head Generation](2503.22728.md)
**Ao Fu, Ziqi Ni, Yi Zhou** · 2025-03-26

<details>
<summary>Abstract</summary>

The generation of audio-driven talking head videos is a key challenge in computer vision and graphics, with applications in virtual avatars and digital media. Traditional approaches often struggle with capturing the complex interaction between audio and facial dynamics, leading to lip synchronization and visual quality issues. In this paper, we propose a novel NeRF-based framework, Dual Audio-Centric Modality Coupling (DAMC), which effectively integrates content and dynamic features from audio inputs. By leveraging a dual encoder structure, DAMC captures semantic content through the Content-Aware Encoder and ensures precise visual synchronization through the Dynamic-Sync Encoder. These features are fused using a Cross-Synchronized Fusion Module (CSFM), enhancing content representation and lip synchronization. Extensive experiments show that our method outperforms existing state-of-the-art approaches in key metrics such as lip synchronization accuracy and image quality, demonstrating robust generalization across various audio inputs, including synthetic speech from text-to-speech (TTS) systems. Our results provide a promising solution for high-quality, audio-driven talking head generation and present a scalable approach for creating realistic talking heads.

</details>

### [Qwen2.5-Omni Technical Report](2503.20215.md)
**Jin Xu, Zhifang Guo, Jinzheng He, Hangrui Hu et al.** · 2025-03-26

<details>
<summary>Abstract</summary>

In this report, we present Qwen2.5-Omni, an end-to-end multimodal model designed to perceive diverse modalities, including text, images, audio, and video, while simultaneously generating text and natural speech responses in a streaming manner. To enable the streaming of multimodal information inputs, both audio and visual encoders utilize a block-wise processing approach. To synchronize the timestamps of video inputs with audio, we organize the audio and video sequentially in an interleaved manner and propose a novel position embedding approach, named TMRoPE(Time-aligned Multimodal RoPE). To concurrently generate text and speech while avoiding interference between the two modalities, we propose \textbf{Thinker-Talker} architecture. In this framework, Thinker functions as a large language model tasked with text generation, while Talker is a dual-track autoregressive model that directly utilizes the hidden representations from the Thinker to produce audio tokens as output. Both the Thinker and Talker models are designed to be trained and inferred in an end-to-end manner. For decoding audio tokens in a streaming manner, we introduce a sliding-window DiT that restricts the receptive field, aiming to reduce the initial package delay. Qwen2.5-Omni is comparable with the similarly sized Qwen2.5-VL and outperforms Qwen2-Audio. Furthermore, Qwen2.5-Omni achieves state-of-the-art performance on multimodal benchmarks like Omni-Bench. Notably, Qwen2.5-Omni's performance in end-to-end speech instruction following is comparable to its capabilities with text inputs, as evidenced by benchmarks such as MMLU and GSM8K. As for speech generation, Qwen2.5-Omni's streaming Talker outperforms most existing streaming and non-streaming alternatives in robustness and naturalness.

</details>

### [SoK: How Robust is Audio Watermarking in Generative AI models?](2503.19176.md)
**Yizhu Wen, Ashwin Innuganti, Aaron Bien Ramos, Hanqing Guo et al.** · 2025-03-24

<details>
<summary>Abstract</summary>

Audio watermarking is increasingly used to verify the provenance of AI-generated content, enabling applications such as detecting AI-generated speech, protecting music IP, and defending against voice cloning. To be effective, audio watermarks must resist removal attacks that distort signals to evade detection. While many schemes claim robustness, these claims are typically tested in isolation and against a limited set of attacks. A systematic evaluation against diverse removal attacks is lacking, hindering practical deployment. In this paper, we investigate whether recent watermarking schemes that claim robustness can withstand a broad range of removal attacks. First, we introduce a taxonomy covering 22 audio watermarking schemes. Next, we summarize their underlying technologies and potential vulnerabilities. We then present a large-scale empirical study to assess their robustness. To support this, we build an evaluation framework encompassing 22 types of removal attacks (109 configurations) including signal-level, physical-level, and AI-induced distortions. We reproduce 9 watermarking schemes using open-source code, identify 8 new highly effective attacks, and highlight 11 key findings that expose the fundamental limitations of these methods across 3 public datasets. Our results reveal that none of the surveyed schemes can withstand all tested distortions. This evaluation offers a comprehensive view of how current watermarking methods perform under real-world threats. Our demo and code are available at https://sokaudiowm.github.io/.

</details>

### [Your voice is your voice: Supporting Self-expression through Speech Generation and LLMs in Augmented and Alternative Communication](2503.17479.md)
**Yiwen Xu et.al.** · 2025-03-21

### [From Faces to Voices: Learning Hierarchical Representations for High-quality Video-to-Speech](2503.16956.md)
**Ji-Hoon Kim, Jeongsoo Choi, Jaehun Kim, Chaeyoung Jung et al.** · 2025-03-21

<details>
<summary>Abstract</summary>

The objective of this study is to generate high-quality speech from silent talking face videos, a task also known as video-to-speech synthesis. A significant challenge in video-to-speech synthesis lies in the substantial modality gap between silent video and multi-faceted speech. In this paper, we propose a novel video-to-speech system that effectively bridges this modality gap, significantly enhancing the quality of synthesized speech. This is achieved by learning of hierarchical representations from video to speech. Specifically, we gradually transform silent video into acoustic feature spaces through three sequential stages -- content, timbre, and prosody modeling. In each stage, we align visual factors -- lip movements, face identity, and facial expressions -- with corresponding acoustic counterparts to ensure the seamless transformation. Additionally, to generate realistic and coherent speech from the visual representations, we employ a flow matching model that estimates direct trajectories from a simple prior distribution to the target speech distribution. Extensive experiments demonstrate that our method achieves exceptional generation quality comparable to real utterances, outperforming existing methods by a significant margin.

</details>

### [WaveFM: A High-Fidelity and Efficient Vocoder Based on Flow Matching](2503.16689.md)
**Tianze Luo et.al.** · 2025-03-20

### [Shushing! Let's Imagine an Authentic Speech from the Silent Video](2503.14928.md)
**Jiaxin Ye, Hongming Shan** · 2025-03-19

<details>
<summary>Abstract</summary>

Vision-guided speech generation aims to produce authentic speech from facial appearance or lip motions without relying on auditory signals, offering significant potential for applications such as dubbing in filmmaking and assisting individuals with aphonia. Despite recent progress, existing methods struggle to achieve unified cross-modal alignment across semantics, timbre, and emotional prosody from visual cues, prompting us to propose Consistent Video-to-Speech (CV2S) as an extended task to enhance cross-modal consistency. To tackle emerging challenges, we introduce ImaginTalk, a novel cross-modal diffusion framework that generates faithful speech using only visual input, operating within a discrete space. Specifically, we propose a discrete lip aligner that predicts discrete speech tokens from lip videos to capture semantic information, while an error detector identifies misaligned tokens, which are subsequently refined through masked language modeling with BERT. To further enhance the expressiveness of the generated speech, we develop a style diffusion transformer equipped with a face-style adapter that adaptively customizes identity and prosody dynamics across both the channel and temporal dimensions while ensuring synchronization with lip-aware semantic features. Extensive experiments demonstrate that ImaginTalk can generate high-fidelity speech with more accurate semantic details and greater expressiveness in timbre and emotion compared to state-of-the-art baselines. Demos are shown at our project page: https://imagintalk.github.io.

</details>

### [MoonCast: High-Quality Zero-Shot Podcast Generation](2503.14345.md)
**Zeqian Ju, Dongchao Yang, Jianwei Yu, Kai Shen et al.** · 2025-03-18

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech synthesis have achieved notable success in generating high-quality short utterances for individual speakers. However, these systems still face challenges when extending their capabilities to long, multi-speaker, and spontaneous dialogues, typical of real-world scenarios such as podcasts. These limitations arise from two primary challenges: 1) long speech: podcasts typically span several minutes, exceeding the upper limit of most existing work; 2) spontaneity: podcasts are marked by their spontaneous, oral nature, which sharply contrasts with formal, written contexts; existing works often fall short in capturing this spontaneity. In this paper, we propose MoonCast, a solution for high-quality zero-shot podcast generation, aiming to synthesize natural podcast-style speech from text-only sources (e.g., stories, technical reports, news in TXT, PDF, or Web URL formats) using the voices of unseen speakers. To generate long audio, we adopt a long-context language model-based audio modeling approach utilizing large-scale long-context speech data. To enhance spontaneity, we utilize a podcast generation module to generate scripts with spontaneous details, which have been empirically shown to be as crucial as the text-to-speech modeling itself. Experiments demonstrate that MoonCast outperforms baselines, with particularly notable improvements in spontaneity and coherence.

</details>

### [InnerSelf: Designing Self-Deepfaked Voice for Emotional Well-being](2503.14257.md)
**Guang Dai, Pinhao Wang, Cheng Yao, Fangtian Ying** · 2025-03-18

<details>
<summary>Abstract</summary>

One's own voice is one of the most frequently heard voices. Studies found that hearing and talking to oneself have positive psychological effects. However, the design and implementation of self-voice for emotional regulation in HCI have yet to be explored. In this paper, we introduce InnerSelf, an innovative voice system based on speech synthesis technologies and the Large Language Model. It allows users to engage in supportive and empathic dialogue with their deepfake voice. By manipulating positive self-talk, our system aims to promote self-disclosure and regulation, reshaping negative thoughts and improving emotional well-being.

</details>

### [Universal Speech Token Learning via Low-Bitrate Neural Codec and Pretrained Representations](2503.12115.md)
**Xue Jiang et.al.** · 2025-03-15

### [MAVFlow: Preserving Paralinguistic Elements with Conditional Flow Matching for Zero-Shot AV2AV Multilingual Translation](2503.11026.md)
**Sungwoo Cho, Jeongsoo Choi, Sungnyun Kim, Se-Young Yun** · 2025-03-14

<details>
<summary>Abstract</summary>

Despite recent advances in text-to-speech (TTS) models, audio-visual-to-audio-visual (AV2AV) translation still faces a critical challenge: maintaining speaker consistency between the original and translated vocal and facial features. To address this issue, we propose a conditional flow matching (CFM) zero-shot audio-visual renderer that utilizes strong dual guidance from both audio and visual modalities. By leveraging multimodal guidance with CFM, our model robustly preserves speaker-specific characteristics and enhances zero-shot AV2AV translation abilities. For the audio modality, we enhance the CFM process by integrating robust speaker embeddings with x-vectors, which serve to bolster speaker consistency. Additionally, we convey emotional nuances to the face rendering module. The guidance provided by both audio and visual cues remains independent of semantic or linguistic content, allowing our renderer to effectively handle zero-shot translation tasks for monolingual speakers in different languages. We empirically demonstrate that the inclusion of high-quality mel-spectrograms conditioned on facial information not only enhances the quality of the synthesized speech but also positively influences facial generation, leading to overall performance improvements in LSE and FID score. Our code is available at https://github.com/Peter-SungwooCho/MAVFlow.

</details>

### [VocalEyes: Enhancing Environmental Perception for the Visually Impaired through Vision-Language Models and Distance-Aware Object Detection](2503.16488.md)
**Kunal Chavan, Keertan Balaji, Spoorti Barigidad, Samba Raju Chiluveru** · 2025-03-10

<details>
<summary>Abstract</summary>

With an increasing demand for assistive technologies that promote the independence and mobility of visually impaired people, this study suggests an innovative real-time system that gives audio descriptions of a user's surroundings to improve situational awareness. The system acquires live video input and processes it with a quantized and fine-tuned Florence-2 big model, adjusted to 4-bit accuracy for efficient operation on low-power edge devices such as the NVIDIA Jetson Orin Nano. By transforming the video signal into frames with a 5-frame latency, the model provides rapid and contextually pertinent descriptions of objects, pedestrians, and barriers, together with their estimated distances. The system employs Parler TTS Mini, a lightweight and adaptable Text-to-Speech (TTS) solution, for efficient audio feedback. It accommodates 34 distinct speaker types and enables customization of speech tone, pace, and style to suit user requirements. This study examines the quantization and fine-tuning techniques utilized to modify the Florence-2 model for this application, illustrating how the integration of a compact model architecture with a versatile TTS component improves real-time performance and user experience. The proposed system is assessed based on its accuracy, efficiency, and usefulness, providing a viable option to aid vision-impaired users in navigating their surroundings securely and successfully.

</details>

### [ProSE: Diffusion Priors for Speech Enhancement](2503.06375.md)
**Sonal Kumar, Sreyan Ghosh, Utkarsh Tyagi, Anton Jeran Ratnarajah et al.** · 2025-03-09

<details>
<summary>Abstract</summary>

Speech enhancement (SE) is the foundational task of enhancing the clarity and quality of speech in the presence of non-stationary additive noise. While deterministic deep learning models have been commonly employed for SE, recent research indicates that generative models, such as denoising diffusion probabilistic models (DDPMs), have shown promise. However, unlike speech generation, SE has a strong constraint in generating results in accordance with the underlying ground-truth signal. Additionally, for a wide variety of applications, SE systems need to be employed in real-time, and traditional diffusion models (DMs) requiring many iterations of a large model during inference are inefficient. To address these issues, we propose ProSE (diffusion-based Priors for SE), a novel methodology based on an alternative framework for applying diffusion models to SE. Specifically, we first apply DDPMs to generate priors in a latent space due to their powerful distribution mapping capabilities. The priors are then integrated into a transformer-based regression model for SE. The priors guide the regression model in the enhancement process. Since the diffusion process is applied to a compact latent space, the diffusion model takes fewer iterations than the traditional DM to obtain accurate estimations. Additionally, using a regression model for SE avoids the distortion issue caused by misaligned details generated by DMs. Our experiments show that ProSE achieves state-of-the-art performance on benchmark datasets with fewer computational costs.

</details>

### [Late Fusion and Multi-Level Fission Amplify Cross-Modal Transfer in Text-Speech LMs](2503.06211.md)
**Santiago Cuervo, Adel Moumen, Yanis Labrak, Sameer Khurana et al.** · 2025-03-08

<details>
<summary>Abstract</summary>

Text-Speech Language Models (TSLMs) -- language models trained to jointly process and generate text and speech -- are commonly trained through an early modality fusion/fission approach, in which both modalities are fed and predicted from a shared backbone via linear layers. We hypothesize that this approach limits cross-modal transfer by neglecting feature compositionality -- specifically, the finer-grained nature of speech representations compared to text -- preventing the emergence of a shared feature hierarchy within model layers. In this paper, we argue that this limitation can be addressed through late fusion and fission, with a fission process that accesses both high- and low-level features for speech generation. Our models implementing these principles, SmolTolk, rival or surpass state-of-the-art TSLMs trained with orders of magnitude more compute, and achieve significantly improved cross-modal performance relative to early fusion/fission baselines. Representation analyses further suggest that our method enhances the model's ability to abstract higher-level, more semantic features from speech, and leads to increasingly shared representation spaces across layers.

</details>

### [DiVISe: Direct Visual-Input Speech Synthesis Preserving Speaker Characteristics And Intelligibility](2503.05223.md)
**Yifan Liu, Yu Fang, Zhouhan Lin** · 2025-03-07

<details>
<summary>Abstract</summary>

Video-to-speech (V2S) synthesis, the task of generating speech directly from silent video input, is inherently more challenging than other speech synthesis tasks due to the need to accurately reconstruct both speech content and speaker characteristics from visual cues alone. Recently, audio-visual pre-training has eliminated the need for additional acoustic hints in V2S, which previous methods often relied on to ensure training convergence. However, even with pre-training, existing methods continue to face challenges in achieving a balance between acoustic intelligibility and the preservation of speaker-specific characteristics. We analyzed this limitation and were motivated to introduce DiVISe (Direct Visual-Input Speech Synthesis), an end-to-end V2S model that predicts Mel-spectrograms directly from video frames alone. Despite not taking any acoustic hints, DiVISe effectively preserves speaker characteristics in the generated audio, and achieves superior performance on both objective and subjective metrics across the LRS2 and LRS3 datasets. Our results demonstrate that DiVISe not only outperforms existing V2S models in acoustic intelligibility but also scales more effectively with increased data and model parameters. Code and weights can be found at https://github.com/PussyCat0700/DiVISe.

</details>

### [LLMVoX: Autoregressive Streaming Text-to-Speech Model for Any LLM](2503.04724.md)
**Sambal Shikhar et.al.** · 2025-03-06

### [Scaling Rich Style-Prompted Text-to-Speech Datasets](2503.04713.md)
**Anuj Diwan et.al.** · 2025-03-06

### [InSerter: Speech Instruction Following with Unsupervised Interleaved Pre-training](2503.02769.md)
**Dingdong Wang, Jin Xu, Ruihang Chu, Zhifang Guo et al.** · 2025-03-04

<details>
<summary>Abstract</summary>

Recent advancements in speech large language models (SpeechLLMs) have attracted considerable attention. Nonetheless, current methods exhibit suboptimal performance in adhering to speech instructions. Notably, the intelligence of models significantly diminishes when processing speech-form input as compared to direct text-form input. Prior work has attempted to mitigate this semantic inconsistency between speech and text representations through techniques such as representation and behavior alignment, which involve the meticulous design of data pairs during the post-training phase. In this paper, we introduce a simple and scalable training method called InSerter, which stands for Interleaved Speech-Text Representation Pre-training. InSerter is designed to pre-train large-scale unsupervised speech-text sequences, where the speech is synthesized from randomly selected segments of an extensive text corpus using text-to-speech conversion. Consequently, the model acquires the ability to generate textual continuations corresponding to the provided speech segments, obviating the need for intensive data design endeavors. To systematically evaluate speech instruction-following capabilities, we introduce SpeechInstructBench, the first comprehensive benchmark specifically designed for speech-oriented instruction-following tasks. Our proposed InSerter achieves SOTA performance in SpeechInstructBench and demonstrates superior or competitive results across diverse speech processing tasks.

</details>

### [Spark-TTS: An Efficient LLM-Based Text-to-Speech Model with Single-Stream Decoupled Speech Tokens](2503.01710.md)
**Xinsheng Wang et.al.** · 2025-03-03

### [Voice Cloning for Dysarthric Speech Synthesis: Addressing Data Scarcity in Speech-Language Pathology](2503.01266.md)
**Birger Moell, Fredrik Sand Aronsson** · 2025-03-03

<details>
<summary>Abstract</summary>

This study explores voice cloning to generate synthetic speech replicating the unique patterns of individuals with dysarthria. Using the TORGO dataset, we address data scarcity and privacy challenges in speech-language pathology. Our contributions include demonstrating that voice cloning preserves dysarthric speech characteristics, analyzing differences between real and synthetic data, and discussing implications for diagnostics, rehabilitation, and communication. We cloned voices from dysarthric and control speakers using a commercial platform, ensuring gender-matched synthetic voices. A licensed speech-language pathologist (SLP) evaluated a subset for dysarthria, speaker gender, and synthetic indicators. The SLP correctly identified dysarthria in all cases and speaker gender in 95% but misclassified 30% of synthetic samples as real, indicating high realism. Our results suggest synthetic speech effectively captures disordered characteristics and that voice cloning has advanced to produce high-quality data resembling real speech, even to trained professionals. This has critical implications for healthcare, where synthetic data can mitigate data scarcity, protect privacy, and enhance AI-driven diagnostics. By enabling the creation of diverse, high-quality speech datasets, voice cloning can improve generalizable models, personalize therapy, and advance assistive technologies for dysarthria. We publicly release our synthetic dataset to foster further research and collaboration, aiming to develop robust models that improve patient outcomes in speech-language pathology.

</details>

### [Language-agnostic, automated assessment of listeners' speech recall using large language models](2503.01045.md)
**Björn Herrmann** · 2025-03-02

<details>
<summary>Abstract</summary>

Speech-comprehension difficulties are common among older people. Standard speech tests do not fully capture such difficulties because the tests poorly resemble the context-rich, story-like nature of ongoing conversation and are typically available only in a country's dominant/official language (e.g., English), leading to inaccurate scores for native speakers of other languages. Assessments for naturalistic, story speech in multiple languages require accurate, time-efficient scoring. The current research leverages modern large language models (LLMs) in native English speakers and native speakers of 10 other languages to automate the generation of high-quality, spoken stories and scoring of speech recall in different languages. Participants listened to and freely recalled short stories (in quiet/clear and in babble noise) in their native language. LLM text-embeddings and LLM prompt engineering with semantic similarity analyses to score speech recall revealed sensitivity to known effects of temporal order, primacy/recency, and background noise, and high similarity of recall scores across languages. The work overcomes limitations associated with simple speech materials and testing of closed native-speaker groups because recall data of varying length and details can be mapped across languages with high accuracy. The full automation of speech generation and recall scoring provides an important step towards comprehension assessments of naturalistic speech with clinical applicability.

</details>

### [PodAgent: A Comprehensive Framework for Podcast Generation](2503.00455.md)
**Yujia Xiao, Lei He, Haohan Guo, Fenglong Xie et al.** · 2025-03-01

<details>
<summary>Abstract</summary>

Existing Existing automatic audio generation methods struggle to generate podcast-like audio programs effectively. The key challenges lie in in-depth content generation, appropriate and expressive voice production. This paper proposed PodAgent, a comprehensive framework for creating audio programs. PodAgent 1) generates informative topic-discussion content by designing a Host-Guest-Writer multi-agent collaboration system, 2) builds a voice pool for suitable voice-role matching and 3) utilizes LLM-enhanced speech synthesis method to generate expressive conversational speech. Given the absence of standardized evaluation criteria for podcast-like audio generation, we developed comprehensive assessment guidelines to effectively evaluate the model's performance. Experimental results demonstrate PodAgent's effectiveness, significantly surpassing direct GPT-4 generation in topic-discussion dialogue content, achieving an 87.4% voice-matching accuracy, and producing more expressive speech through LLM-guided synthesis. Demo page: https://podcast-agent.github.io/demo/. Source code: https://github.com/yujxx/PodAgent.

</details>

### [DiffCSS: Diverse and Expressive Conversational Speech Synthesis with Diffusion Models](2502.19924.md)
**Weihao wu et.al.** · 2025-02-27

### [Telephone Surveys Meet Conversational AI: Evaluating a LLM-Based Telephone Survey System at Scale](2502.20140.md)
**Max M. Lang, Sol Eskenazi** · 2025-02-27

<details>
<summary>Abstract</summary>

Telephone surveys remain a valuable tool for gathering insights but typically require substantial resources in training and coordinating human interviewers. This work presents an AI-driven telephone survey system integrating text-to-speech (TTS), a large language model (LLM), and speech-to-text (STT) that mimics the versatility of human-led interviews (full-duplex dialogues) at scale. We tested the system across two populations, a pilot study in the United States (n = 75) and a large-scale deployment in Peru (n = 2,739), inviting participants via web-based links and contacting them via direct phone calls. The AI agent successfully administered open-ended and closed-ended questions, handled basic clarifications, and dynamically navigated branching logic, allowing fast large-scale survey deployment without interviewer recruitment or training. Our findings demonstrate that while the AI system's probing for qualitative depth was more limited than human interviewers, overall data quality approached human-led standards for structured items. This study represents one of the first successful large-scale deployments of an LLM-based telephone interviewer in a real-world survey context. The AI-powered telephone survey system has the potential for expanding scalable, consistent data collecting across market research, social science, and public opinion studies, thus improving operational efficiency while maintaining appropriate data quality for research.

</details>

### [Speculative Decoding and Beyond: An In-Depth Survey of Techniques](2502.19732.md)
**Yunhai Hu, Zining Liu, Zhenyuan Dong, Tianfan Peng et al.** · 2025-02-27

<details>
<summary>Abstract</summary>

Sequential dependencies present a fundamental bottleneck in deploying large-scale autoregressive models, particularly for real-time applications. While traditional optimization approaches like pruning and quantization often compromise model quality, recent advances in generation-refinement frameworks demonstrate that this trade-off can be significantly mitigated. This survey presents a comprehensive taxonomy of generation-refinement frameworks, analyzing methods across autoregressive sequence tasks. We categorize methods based on their generation strategies (from simple n-gram prediction to sophisticated draft models) and refinement mechanisms (including single-pass verification and iterative approaches). Through systematic analysis of both algorithmic innovations and system-level implementations, we examine deployment strategies across computing environments and explore applications spanning text, images, and speech generation. This systematic examination of both theoretical frameworks and practical implementations provides a foundation for future research in efficient autoregressive decoding.

</details>

### [Sparse Alignment Enhanced Latent Diffusion Transformer for Zero-Shot Speech Synthesis](2502.18924.md)
**Ziyue Jiang et.al.** · 2025-02-26

### [Clip-TTS: Contrastive Text-content and Mel-spectrogram, A High-Quality Text-to-Speech Method based on Contextual Semantic Understanding](2502.18889.md)
**Tianyun Liu** · 2025-02-26

<details>
<summary>Abstract</summary>

Traditional text-to-speech (TTS) methods primarily focus on establishing a mapping between phonemes and mel-spectrograms. However, during the phoneme encoding stage, there is often a lack of real mel-spectrogram auxiliary information, which results in the encoding process lacking true semantic understanding. At the same time, traditional TTS systems often struggle to balance the inference speed of the model with the quality of the synthesized speech. Methods that generate high-quality synthesized speech tend to have slower inference speeds, while faster inference methods often sacrifice speech quality. In this paper, I propose Clip-TTS, a TTS method based on the Clip architecture. This method uses the Clip framework to establish a connection between text content and real mel-spectrograms during the text encoding stage, enabling the text encoder to directly learn the true semantics of the global context, thereby ensuring the quality of the synthesized speech. In terms of model architecture, I adopt the basic structure of Transformer, which allows Clip-TTS to achieve fast inference speeds. Experimental results show that on the LJSpeech and Baker datasets, the speech generated by Clip-TTS achieves state-of-the-art MOS scores, and it also performs excellently on multi-emotion datasets.Audio samples are available at: https://ltydd1314.github.io/.

</details>

### [Baichuan-Audio: A Unified Framework for End-to-End Speech Interaction](2502.17239.md)
**Tianpeng Li, Jun Liu, Tao Zhang, Yuanbo Fang et al.** · 2025-02-24

<details>
<summary>Abstract</summary>

We introduce Baichuan-Audio, an end-to-end audio large language model that seamlessly integrates audio understanding and generation. It features a text-guided aligned speech generation mechanism, enabling real-time speech interaction with both comprehension and generation capabilities. Baichuan-Audio leverages a pre-trained ASR model, followed by multi-codebook discretization of speech at a frame rate of 12.5 Hz. This multi-codebook setup ensures that speech tokens retain both semantic and acoustic information. To further enhance modeling, an independent audio head is employed to process audio tokens, effectively capturing their unique characteristics. To mitigate the loss of intelligence during pre-training and preserve the original capabilities of the LLM, we propose a two-stage pre-training strategy that maintains language understanding while enhancing audio modeling. Following alignment, the model excels in real-time speech-based conversation and exhibits outstanding question-answering capabilities, demonstrating its versatility and efficiency. The proposed model demonstrates superior performance in real-time spoken dialogue and exhibits strong question-answering abilities. Our code, model and training data are available at https://github.com/baichuan-inc/Baichuan-Audio

</details>

### [ESPnet-SpeechLM: An Open Speech Language Model Toolkit](2502.15218.md)
**Jinchuan Tian, Jiatong Shi, William Chen, Siddhant Arora et al.** · 2025-02-21

<details>
<summary>Abstract</summary>

We present ESPnet-SpeechLM, an open toolkit designed to democratize the development of speech language models (SpeechLMs) and voice-driven agentic applications. The toolkit standardizes speech processing tasks by framing them as universal sequential modeling problems, encompassing a cohesive workflow of data preprocessing, pre-training, inference, and task evaluation. With ESPnet-SpeechLM, users can easily define task templates and configure key settings, enabling seamless and streamlined SpeechLM development. The toolkit ensures flexibility, efficiency, and scalability by offering highly configurable modules for every stage of the workflow. To illustrate its capabilities, we provide multiple use cases demonstrating how competitive SpeechLMs can be constructed with ESPnet-SpeechLM, including a 1.7B-parameter model pre-trained on both text and speech tasks, across diverse benchmarks. The toolkit and its recipes are fully transparent and reproducible at: https://github.com/espnet/espnet/tree/speechlm.

</details>

### [High-Fidelity Music Vocoder using Neural Audio Codecs](2502.12759.md)
**Luca A. Lanzendörfer et.al.** · 2025-02-18

### [TechSinger: Technique Controllable Multilingual Singing Voice Synthesis via Flow Matching](2502.12572.md)
**Wenxiang Guo et.al.** · 2025-02-18

### [AV-Flow: Transforming Text to Audio-Visual Human-like Interactions](2502.13133.md)
**Aggelina Chatziagapi, Louis-Philippe Morency, Hongyu Gong, Michael Zollhoefer et al.** · 2025-02-18

<details>
<summary>Abstract</summary>

We introduce AV-Flow, an audio-visual generative model that animates photo-realistic 4D talking avatars given only text input. In contrast to prior work that assumes an existing speech signal, we synthesize speech and vision jointly. We demonstrate human-like speech synthesis, synchronized lip motion, lively facial expressions and head pose; all generated from just text characters. The core premise of our approach lies in the architecture of our two parallel diffusion transformers. Intermediate highway connections ensure communication between the audio and visual modalities, and thus, synchronized speech intonation and facial dynamics (e.g., eyebrow motion). Our model is trained with flow matching, leading to expressive results and fast inference. In case of dyadic conversations, AV-Flow produces an always-on avatar, that actively listens and reacts to the audio-visual input of a user. Through extensive experiments, we show that our method outperforms prior work, synthesizing natural-looking 4D talking avatars. Project page: https://aggelinacha.github.io/AV-Flow/

</details>

### [Playing with Voices: Tabletop Role-Playing Game Recordings as a Diarization Challenge](2502.12714.md)
**Lian Remme, Kevin Tang** · 2025-02-18

<details>
<summary>Abstract</summary>

This paper provides a proof of concept that audio of tabletop role-playing games (TTRPG) could serve as a challenge for diarization systems. TTRPGs are carried out mostly by conversation. Participants often alter their voices to indicate that they are talking as a fictional character. Audio processing systems are susceptible to voice conversion with or without technological assistance. TTRPG present a conversational phenomenon in which voice conversion is an inherent characteristic for an immersive gaming experience. This could make it more challenging for diarizers to pick the real speaker and determine that impersonating is just that. We present the creation of a small TTRPG audio dataset and compare it against the AMI and the ICSI corpus. The performance of two diarizers, pyannote.audio and wespeaker, were evaluated. We observed that TTRPGs' properties result in a higher confusion rate for both diarizers. Additionally, wespeaker strongly underestimates the number of speakers in the TTRPG audio files. We propose TTRPG audio as a promising challenge for diarization systems.

</details>

### [SongGen: A Single Stage Auto-regressive Transformer for Text-to-Song Generation](2502.13128.md)
**Zihan Liu, Shuangrui Ding, Zhixiong Zhang, Xiaoyi Dong et al.** · 2025-02-18

<details>
<summary>Abstract</summary>

Text-to-song generation, the task of creating vocals and accompaniment from textual inputs, poses significant challenges due to domain complexity and data scarcity. Existing approaches often employ multi-stage generation procedures, leading to cumbersome training and inference pipelines, as well as suboptimal overall generation quality due to error accumulation across stages. In this paper, we propose SongGen, a fully open-source, single-stage auto-regressive transformer designed for controllable song generation. The proposed model facilitates fine-grained control over diverse musical attributes, including lyrics and textual descriptions of instrumentation, genre, mood, and timbre, while also offering an optional three-second reference clip for voice cloning. Within a unified auto-regressive framework, SongGen supports two output modes: mixed mode, which generates a mixture of vocals and accompaniment directly, and dual-track mode, which synthesizes them separately for greater flexibility in downstream applications. We explore diverse token pattern strategies for each mode, leading to notable improvements and valuable insights. Furthermore, we design an automated data preprocessing pipeline with effective quality control. To foster community engagement and future research, we will release our model weights, training code, annotated data, and preprocessing pipeline. The code is available at https://github.com/LiuZH-19/SongGen.

</details>

### [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](2502.12002.md)
**Yifan Liang et.al.** · 2025-02-17

### [A Survey on Bridging EEG Signals and Generative AI: From Image and Text to Beyond](2502.12048.md)
**Shreya Shukla, Jose Torres, Akshaj Murhekar, Christina Liu et al.** · 2025-02-17

<details>
<summary>Abstract</summary>

Decoding neural activity into human-interpretable representations is a key research direction in brain-computer interfaces (BCIs) and computational neuroscience. Recent progress in machine learning and generative AI has driven growing interest in transforming non-invasive Electroencephalography (EEG) signals into images, text, and audio. This survey consolidates and analyzes developments across EEG-to-image synthesis, EEG-to-text generation, and EEG-to-audio reconstruction. We conducted a structured literature search across major databases (2017-2025), extracting key information on datasets, generative architectures (GANs, VAEs, transformers, diffusion models), EEG feature-encoding techniques, evaluation metrics, and the major challenges shaping current work in this area. Our review finds that EEG-to-image models predominantly employ encoder-decoder architectures built on GANs, VAEs, or diffusion models; EEG-to-text approaches increasingly leverage transformer-based language models for open-vocabulary decoding; and EEG-to-audio methods commonly map EEG signals to mel-spectrograms that are subsequently rendered into audio using neural vocoders. Despite promising advances, the field remains constrained by small and heterogeneous datasets, limited cross-subject generalization, and the absence of standardized benchmarks. By consolidating methodological trends and available datasets, this survey provides a foundational reference for advancing EEG-based generative AI and supporting reproducible research. We further highlight open-source datasets and baseline implementations to facilitate systematic benchmarking and accelerate progress in EEG-driven neural decoding.

</details>

### [Step-Audio: Unified Understanding and Generation in Intelligent Speech Interaction](2502.11946.md)
**Ailin Huang, Boyong Wu, Bruce Wang, Chao Yan et al.** · 2025-02-17

<details>
<summary>Abstract</summary>

Real-time speech interaction, serving as a fundamental interface for human-machine collaboration, holds immense potential. However, current open-source models face limitations such as high costs in voice data collection, weakness in dynamic control, and limited intelligence. To address these challenges, this paper introduces Step-Audio, the first production-ready open-source solution. Key contributions include: 1) a 130B-parameter unified speech-text multi-modal model that achieves unified understanding and generation, with the Step-Audio-Chat version open-sourced; 2) a generative speech data engine that establishes an affordable voice cloning framework and produces the open-sourced lightweight Step-Audio-TTS-3B model through distillation; 3) an instruction-driven fine control system enabling dynamic adjustments across dialects, emotions, singing, and RAP; 4) an enhanced cognitive architecture augmented with tool calling and role-playing abilities to manage complex tasks effectively. Based on our new StepEval-Audio-360 evaluation benchmark, Step-Audio achieves state-of-the-art performance in human evaluations, especially in terms of instruction following. On open-source benchmarks like LLaMA Question, shows 9.3% average performance improvement, demonstrating our commitment to advancing the development of open-source multi-modal language technologies. Our code and models are available at https://github.com/stepfun-ai/Step-Audio.

</details>

### [FELLE: Autoregressive Speech Synthesis with Token-Wise Coarse-to-Fine Flow Matching](2502.11128.md)
**Hui Wang et.al.** · 2025-02-16

### [SyncSpeech: Low-Latency and Efficient Dual-Stream Text-to-Speech based on Temporal Masked Transformer](2502.11094.md)
**Zhengyan Sheng et.al.** · 2025-02-16

### [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](2502.03930.md)
**Dongya Jia et.al.** · 2025-02-14

### [TokenSynth: A Token-based Neural Synthesizer for Instrument Cloning and Text-to-Instrument](2502.08939.md)
**Kyungsu Kim, Junghyun Koo, Sungho Lee, Haesun Joung et al.** · 2025-02-13

<details>
<summary>Abstract</summary>

Recent advancements in neural audio codecs have enabled the use of tokenized audio representations in various audio generation tasks, such as text-to-speech, text-to-audio, and text-to-music generation. Leveraging this approach, we propose TokenSynth, a novel neural synthesizer that utilizes a decoder-only transformer to generate desired audio tokens from MIDI tokens and CLAP (Contrastive Language-Audio Pretraining) embedding, which has timbre-related information. Our model is capable of performing instrument cloning, text-to-instrument synthesis, and text-guided timbre manipulation without any fine-tuning. This flexibility enables diverse sound design and intuitive timbre control. We evaluated the quality of the synthesized audio, the timbral similarity between synthesized and target audio/text, and synthesis accuracy (i.e., how accurately it follows the input MIDI) using objective measures. TokenSynth demonstrates the potential of leveraging advanced neural audio codecs and transformers to create powerful and versatile neural synthesizers. The source code, model weights, and audio demos are available at: https://github.com/KyungsuKim42/tokensynth

</details>

### [Advanced Zero-Shot Text-to-Speech for Background Removal and Preservation with Controllable Masked Speech Prediction](2502.07345.md)
**Leying Zhang et.al.** · 2025-02-11

### [LoRP-TTS: Low-Rank Personalized Text-To-Speech](2502.07562.md)
**Łukasz Bondaruk, Jakub Kubiak** · 2025-02-11

<details>
<summary>Abstract</summary>

Speech synthesis models convert written text into natural-sounding audio. While earlier models were limited to a single speaker, recent advancements have led to the development of zero-shot systems that generate realistic speech from a wide range of speakers using their voices as additional prompts. However, they still struggle with imitating non-studio-quality samples that differ significantly from the training datasets. In this work, we demonstrate that utilizing Low-Rank Adaptation (LoRA) allows us to successfully use even single recordings of spontaneous speech in noisy environments as prompts. This approach enhances speaker similarity by up to $30pp$ while preserving content and naturalness. It represents a significant step toward creating truly diverse speech corpora, that is crucial in all speech-related tasks.

</details>

### [Vevo: Controllable Zero-Shot Voice Imitation with Self-Supervised Disentanglement](2502.07243.md)
**Xueyao Zhang, Xiaohui Zhang, Kainan Peng, Zhenyu Tang et al.** · 2025-02-11

<details>
<summary>Abstract</summary>

The imitation of voice, targeted on specific speech attributes such as timbre and speaking style, is crucial in speech generation. However, existing methods rely heavily on annotated data, and struggle with effectively disentangling timbre and style, leading to challenges in achieving controllable generation, especially in zero-shot scenarios. To address these issues, we propose Vevo, a versatile zero-shot voice imitation framework with controllable timbre and style. Vevo operates in two core stages: (1) Content-Style Modeling: Given either text or speech's content tokens as input, we utilize an autoregressive transformer to generate the content-style tokens, which is prompted by a style reference; (2) Acoustic Modeling: Given the content-style tokens as input, we employ a flow-matching transformer to produce acoustic representations, which is prompted by a timbre reference. To obtain the content and content-style tokens of speech, we design a fully self-supervised approach that progressively decouples the timbre, style, and linguistic content of speech. Specifically, we adopt VQ-VAE as the tokenizer for the continuous hidden features of HuBERT. We treat the vocabulary size of the VQ-VAE codebook as the information bottleneck, and adjust it carefully to obtain the disentangled speech representations. Solely self-supervised trained on 60K hours of audiobook speech data, without any fine-tuning on style-specific corpora, Vevo matches or surpasses existing methods in accent and emotion conversion tasks. Additionally, Vevo's effectiveness in zero-shot voice conversion and text-to-speech tasks further demonstrates its strong generalization and versatility. Audio samples are available at https://versavoice.github.io.

</details>

### [Synthetic Audio Helps for Cognitive State Tasks](2502.06922.md)
**Adil Soubki, John Murzaku, Peter Zeng, Owen Rambow** · 2025-02-10

<details>
<summary>Abstract</summary>

The NLP community has broadly focused on text-only approaches of cognitive state tasks, but audio can provide vital missing cues through prosody. We posit that text-to-speech models learn to track aspects of cognitive state in order to produce naturalistic audio, and that the signal audio models implicitly identify is orthogonal to the information that language models exploit. We present Synthetic Audio Data fine-tuning (SAD), a framework where we show that 7 tasks related to cognitive state modeling benefit from multimodal training on both text and zero-shot synthetic audio data from an off-the-shelf TTS system. We show an improvement over the text-only modality when adding synthetic audio data to text-only corpora. Furthermore, on tasks and corpora that do contain gold audio, we show our SAD framework achieves competitive performance with text and synthetic audio compared to text and gold audio.

</details>

### [Recent Advances in Discrete Speech Tokens: A Review](2502.06490.md)
**Yiwei Guo, Zhihan Li, Hankun Wang, Bohan Li et al.** · 2025-02-10

<details>
<summary>Abstract</summary>

The rapid advancement of speech generation technologies in the era of large language models (LLMs) has established discrete speech tokens as a foundational paradigm for speech representation. These tokens, characterized by their discrete, compact, and concise nature, are not only advantageous for efficient transmission and storage, but also inherently compatible with the language modeling framework, enabling seamless integration of speech into text-dominated LLM architectures. Current research categorizes discrete speech tokens into two principal classes: acoustic tokens and semantic tokens, each of which has evolved into a rich research domain characterized by unique design philosophies and methodological approaches. This survey systematically synthesizes the existing taxonomy and recent innovations in discrete speech tokenization, conducts a critical examination of the strengths and limitations of each paradigm, and presents systematic experimental comparisons across token types. Furthermore, we identify persistent challenges in the field and propose potential research directions, aiming to offer actionable insights to inspire future advancements in the development and application of discrete speech tokens.

</details>

### [BnTTS: Few-Shot Speaker Adaptation in Low-Resource Setting](2502.05729.md)
**Mohammad Jahid Ibna Basher, Md Kowsher, Md Saiful Islam, Rabindra Nath Nandi et al.** · 2025-02-09

<details>
<summary>Abstract</summary>

This paper introduces BnTTS (Bangla Text-To-Speech), the first framework for Bangla speaker adaptation-based TTS, designed to bridge the gap in Bangla speech synthesis using minimal training data. Building upon the XTTS architecture, our approach integrates Bangla into a multilingual TTS pipeline, with modifications to account for the phonetic and linguistic characteristics of the language. We pre-train BnTTS on 3.85k hours of Bangla speech dataset with corresponding text labels and evaluate performance in both zero-shot and few-shot settings on our proposed test dataset. Empirical evaluations in few-shot settings show that BnTTS significantly improves the naturalness, intelligibility, and speaker fidelity of synthesized Bangla speech. Compared to state-of-the-art Bangla TTS systems, BnTTS exhibits superior performance in Subjective Mean Opinion Score (SMOS), Naturalness, and Clarity metrics.

</details>

### [Gender Bias in Instruction-Guided Speech Synthesis Models](2502.05649.md)
**Chun-Yi Kuan et.al.** · 2025-02-08

### [IndexTTS: An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech System](2502.05512.md)
**Wei Deng et.al.** · 2025-02-08

### [ShiftySpeech: A Large-Scale Synthetic Speech Dataset with Distribution Shifts](2502.05674.md)
**Ashi Garg, Zexin Cai, Lin Zhang, Henry Li Xinyuan et al.** · 2025-02-08

<details>
<summary>Abstract</summary>

The problem of synthetic speech detection has enjoyed considerable attention, with recent methods achieving low error rates across several established benchmarks. However, to what extent can low error rates on academic benchmarks translate to more realistic conditions? In practice, while the training set is fixed at one point in time, test-time conditions may exhibit distribution shifts relative to the training conditions, such as changes in speaker characteristics, emotional expressiveness, language and acoustic conditions, and the emergence of novel synthesis methods. Although some existing datasets target subsets of these distribution shifts, systematic analysis remains difficult due to inconsistencies between source data and synthesis systems across datasets. This difficulty is further exacerbated by the rapid development of new text-to-speech (TTS) and vocoder systems, which continually expand the diversity of synthetic speech. To enable systematic benchmarking of model performance under distribution shifts, we introduce ShiftySpeech, a large-scale benchmark comprising over 3,000 hours of synthetic speech across 7 source domains, 6 TTS systems, 12 vocoders, and 3 languages. ShiftySpeech is specifically designed to evaluate model generalization under controlled distribution shifts while ensuring broad coverage of modern synthetic speech generation techniques. It fills a key gap in current benchmarks by supporting fine-grained, controlled analysis of generalization robustness. All tested distribution shifts significantly degrade detection performance of state-of-the-art detection approaches based on self-supervised features. Overall, our findings suggest that reliance on synthetic speech detection methods in production environments should be carefully evaluated based on anticipated distribution shifts.

</details>

### [Enhancing Expressive Voice Conversion with Discrete Pitch-Conditioned Flow Matching Model](2502.05471.md)
**Jialong Zuo, Shengpeng Ji, Minghui Fang, Ziyue Jiang et al.** · 2025-02-08

<details>
<summary>Abstract</summary>

This paper introduces PFlow-VC, a conditional flow matching voice conversion model that leverages fine-grained discrete pitch tokens and target speaker prompt information for expressive voice conversion (VC). Previous VC works primarily focus on speaker conversion, with further exploration needed in enhancing expressiveness (such as prosody and emotion) for timbre conversion. Unlike previous methods, we adopt a simple and efficient approach to enhance the style expressiveness of voice conversion models. Specifically, we pretrain a self-supervised pitch VQVAE model to discretize speaker-irrelevant pitch information and leverage a masked pitch-conditioned flow matching model for Mel-spectrogram synthesis, which provides in-context pitch modeling capabilities for the speaker conversion model, effectively improving the voice style transfer capacity. Additionally, we improve timbre similarity by combining global timbre embeddings with time-varying timbre tokens. Experiments on unseen LibriTTS test-clean and emotional speech dataset ESD show the superiority of the PFlow-VC model in both timbre conversion and style transfer. Audio samples are available on the demo page https://speechai-demo.github.io/PFlow-VC/.

</details>

### [Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](2502.05236.md)
**Shehzeen Hussain et.al.** · 2025-02-07

### [Singing Voice Conversion with Accompaniment Using Self-Supervised Representation-Based Melody Features](2502.04722.md)
**Wei Chen, Binzhu Sha, Jing Yang, Zhuo Wang et al.** · 2025-02-07

<details>
<summary>Abstract</summary>

Melody preservation is crucial in singing voice conversion (SVC). However, in many scenarios, audio is often accompanied with background music (BGM), which can cause audio distortion and interfere with the extraction of melody and other key features, significantly degrading SVC performance. Previous methods have attempted to address this by using more robust neural network-based melody extractors, but their performance drops sharply in the presence of complex accompaniment. Other approaches involve performing source separation before conversion, but this often introduces noticeable artifacts, leading to a significant drop in conversion quality and increasing the user's operational costs. To address these issues, we introduce a novel SVC method that uses self-supervised representation-based melody features to improve melody modeling accuracy in the presence of BGM. In our experiments, we compare the effectiveness of different self-supervised learning (SSL) models for melody extraction and explore for the first time how SSL benefits the task of melody extraction. The experimental results demonstrate that our proposed SVC model significantly outperforms existing baseline methods in terms of melody accuracy and shows higher similarity and naturalness in both subjective and objective evaluations across noisy and clean audio environments.

</details>

### [Llasa: Scaling Train-Time and Inference-Time Compute for Llama-based Speech Synthesis](2502.04128.md)
**Zhen Ye, Xinfa Zhu, Chi-Min Chan, Xinsheng Wang et al.** · 2025-02-06

<details>
<summary>Abstract</summary>

Recent advances in text-based large language models (LLMs), particularly in the GPT series and the o1 model, have demonstrated the effectiveness of scaling both training-time and inference-time compute. However, current state-of-the-art TTS systems leveraging LLMs are often multi-stage, requiring separate models (e.g., diffusion models after LLM), complicating the decision of whether to scale a particular model during training or testing. This work makes the following contributions: First, we explore the scaling of train-time and inference-time compute for speech synthesis. Second, we propose a simple framework Llasa for speech synthesis that employs a single-layer vector quantizer (VQ) codec and a single Transformer architecture to fully align with standard LLMs such as Llama. Our experiments reveal that scaling train-time compute for Llasa consistently improves the naturalness of synthesized speech and enables the generation of more complex and accurate prosody patterns. Furthermore, from the perspective of scaling inference-time compute, we employ speech understanding models as verifiers during the search, finding that scaling inference-time compute shifts the sampling modes toward the preferences of specific verifiers, thereby improving emotional expressiveness, timbre consistency, and content accuracy. In addition, we released the checkpoint and training code for our TTS model (1B, 3B, 8B) and codec model publicly available.

</details>

### [GenVC: Self-Supervised Zero-Shot Voice Conversion](2502.04519.md)
**Zexin Cai, Henry Li Xinyuan, Ashi Garg, Leibny Paola García-Perera et al.** · 2025-02-06

<details>
<summary>Abstract</summary>

Most current zero-shot voice conversion methods rely on externally supervised components, particularly speaker encoders, for training. To explore alternatives that eliminate this dependency, this paper introduces GenVC, a novel framework that disentangles speaker identity and linguistic content from speech signals in a self-supervised manner. GenVC leverages speech tokenizers and an autoregressive, Transformer-based language model as its backbone for speech generation. This design supports large-scale training while enhancing both source speaker privacy protection and target speaker cloning fidelity. Experimental results demonstrate that GenVC achieves notably higher speaker similarity, with naturalness on par with leading zero-shot approaches. Moreover, due to its autoregressive formulation, GenVC introduces flexibility in temporal alignment, reducing the preservation of source prosody and speaker-specific traits, and making it highly effective for voice anonymization.

</details>

### [FocalCodec: Low-Bitrate Speech Coding via Focal Modulation Networks](2502.04465.md)
**Luca Della Libera, Francesco Paissan, Cem Subakan, Mirco Ravanelli** · 2025-02-06

<details>
<summary>Abstract</summary>

Large language models have revolutionized natural language processing through self-supervised pretraining on massive datasets. Inspired by this success, researchers have explored adapting these methods to speech by discretizing continuous audio into tokens using neural audio codecs. However, existing approaches face limitations, including high bitrates, the loss of either semantic or acoustic information, and the reliance on multi-codebook designs when trying to capture both, which increases architectural complexity for downstream tasks. To address these challenges, we introduce FocalCodec, an efficient low-bitrate codec based on focal modulation that utilizes a single binary codebook to compress speech between 0.16 and 0.65 kbps. FocalCodec delivers competitive performance in speech resynthesis and voice conversion at lower bitrates than the current state-of-the-art, while effectively handling multilingual speech and noisy environments. Evaluation on downstream tasks shows that FocalCodec successfully preserves sufficient semantic and acoustic information, while also being well-suited for generative modeling. Demo samples and code are available at https://lucadellalib.github.io/focalcodec-web/.

</details>

### [Metis: A Foundation Speech Generation Model with Masked Generative Pre-training](2502.03128.md)
**Yuancheng Wang et.al.** · 2025-02-05

### [Fine-grained Preference Optimization Improves Zero-shot Text-to-Speech](2502.02950.md)
**Jixun Yao et.al.** · 2025-02-05

### [High-Fidelity Simultaneous Speech-To-Speech Translation](2502.03382.md)
**Tom Labiausse, Laurent Mazaré, Edouard Grave, Patrick Pérez et al.** · 2025-02-05

<details>
<summary>Abstract</summary>

We introduce Hibiki, a decoder-only model for simultaneous speech translation. Hibiki leverages a multistream language model to synchronously process source and target speech, and jointly produces text and audio tokens to perform speech-to-text and speech-to-speech translation. We furthermore address the fundamental challenge of simultaneous interpretation, which unlike its consecutive counterpart, where one waits for the end of the source utterance to start translating, adapts its flow to accumulate just enough context to produce a correct translation in real-time, chunk by chunk. To do so, we introduce a weakly-supervised method that leverages the perplexity of an off-the-shelf text translation system to identify optimal delays on a per-word basis and create aligned synthetic data. After supervised training, Hibiki performs adaptive, simultaneous speech translation with vanilla temperature sampling. On a French-English simultaneous speech translation task, Hibiki demonstrates state-of-the-art performance in translation quality, speaker fidelity and naturalness. Moreover, the simplicity of its inference process makes it compatible with batched translation and even real-time on-device deployment. We provide examples as well as models and inference code.

</details>

### [Developing multilingual speech synthesis system for Ojibwe, Mi'kmaq, and Maliseet](2502.02703.md)
**Shenran Wang, Changbing Yang, Mike Parkhill, Chad Quinn et al.** · 2025-02-04

<details>
<summary>Abstract</summary>

We present lightweight flow matching multilingual text-to-speech (TTS) systems for Ojibwe, Mi'kmaq, and Maliseet, three Indigenous languages in North America. Our results show that training a multilingual TTS model on three typologically similar languages can improve the performance over monolingual models, especially when data are scarce. Attention-free architectures are highly competitive with self-attention architecture with higher memory efficiency. Our research not only advances technical development for the revitalization of low-resource languages but also highlights the cultural gap in human evaluation protocols, calling for a more community-centered approach to human evaluation.

</details>

### [Streaming Speaker Change Detection and Gender Classification for Transducer-Based Multi-Talker Speech Translation](2502.02683.md)
**Peidong Wang, Naoyuki Kanda, Jian Xue, Jinyu Li et al.** · 2025-02-04

<details>
<summary>Abstract</summary>

Streaming multi-talker speech translation is a task that involves not only generating accurate and fluent translations with low latency but also recognizing when a speaker change occurs and what the speaker's gender is. Speaker change information can be used to create audio prompts for a zero-shot text-to-speech system, and gender can help to select speaker profiles in a conventional text-to-speech model. We propose to tackle streaming speaker change detection and gender classification by incorporating speaker embeddings into a transducer-based streaming end-to-end speech translation model. Our experiments demonstrate that the proposed methods can achieve high accuracy for both speaker change detection and gender classification.

</details>

### [Continuous Autoregressive Modeling with Stochastic Monotonic Alignment for Speech Synthesis](2502.01084.md)
**Weiwei Lin et.al.** · 2025-02-03

### [Emotional Face-to-Speech](2502.01046.md)
**Jiaxin Ye, Boyuan Cao, Hongming Shan** · 2025-02-03

<details>
<summary>Abstract</summary>

How much can we infer about an emotional voice solely from an expressive face? This intriguing question holds great potential for applications such as virtual character dubbing and aiding individuals with expressive language disorders. Existing face-to-speech methods offer great promise in capturing identity characteristics but struggle to generate diverse vocal styles with emotional expression. In this paper, we explore a new task, termed emotional face-to-speech, aiming to synthesize emotional speech directly from expressive facial cues. To that end, we introduce DEmoFace, a novel generative framework that leverages a discrete diffusion transformer (DiT) with curriculum learning, built upon a multi-level neural audio codec. Specifically, we propose multimodal DiT blocks to dynamically align text and speech while tailoring vocal styles based on facial emotion and identity. To enhance training efficiency and generation quality, we further introduce a coarse-to-fine curriculum learning algorithm for multi-level token processing. In addition, we develop an enhanced predictor-free guidance to handle diverse conditioning scenarios, enabling multi-conditional generation and disentangling complex attributes effectively. Extensive experimental results demonstrate that DEmoFace generates more natural and consistent speech compared to baselines, even surpassing speech-driven methods. Demos are shown at https://demoface-ai.github.io/.

</details>

### [EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](2502.00654.md)
**Junuk Cha, Seongro Yoon, Valeriya Strizhkova, Francois Bremond et al.** · 2025-02-02

<details>
<summary>Abstract</summary>

3D Gaussian splatting-based talking head synthesis has recently gained attention for its ability to render high-fidelity images with real-time inference speed. However, since it is typically trained on only a short video that lacks the diversity in facial emotions, the resultant talking heads struggle to represent a wide range of emotions. To address this issue, we propose a lip-aligned emotional face generator and leverage it to train our EmoTalkingGaussian model. It is able to manipulate facial emotions conditioned on continuous emotion values (i.e., valence and arousal); while retaining synchronization of lip movements with input audio. Additionally, to achieve the accurate lip synchronization for in-the-wild audio, we introduce a self-supervised learning method that leverages a text-to-speech network and a visual-audio synchronization network. We experiment our EmoTalkingGaussian on publicly available videos and have obtained better results than state-of-the-arts in terms of image quality (measured in PSNR, SSIM, LPIPS), emotion expression (measured in V-RMSE, A-RMSE, V-SA, A-SA, Emotion Accuracy), and lip synchronization (measured in LMD, Sync-E, Sync-C), respectively.

</details>

### [BreezyVoice: Adapting TTS for Taiwanese Mandarin with Enhanced Polyphone Disambiguation -- Challenges and Insights](2501.17790.md)
**Chan-Jan Hsu, Yi-Cheng Lin, Chia-Chun Lin, Wei-Chih Chen et al.** · 2025-01-29

<details>
<summary>Abstract</summary>

We present BreezyVoice, a Text-to-Speech (TTS) system specifically adapted for Taiwanese Mandarin, highlighting phonetic control abilities to address the unique challenges of polyphone disambiguation in the language. Building upon CosyVoice, we incorporate a $S^{3}$ tokenizer, a large language model (LLM), an optimal-transport conditional flow matching model (OT-CFM), and a grapheme to phoneme prediction model, to generate realistic speech that closely mimics human utterances. Our evaluation demonstrates BreezyVoice's superior performance in both general and code-switching contexts, highlighting its robustness and effectiveness in generating high-fidelity speech. Additionally, we address the challenges of generalizability in modeling long-tail speakers and polyphone disambiguation. Our approach significantly enhances performance and offers valuable insights into the workings of neural codec TTS systems.

</details>

### [VoicePrompter: Robust Zero-Shot Voice Conversion with Voice Prompt and Conditional Flow Matching](2501.17612.md)
**Ha-Yeong Choi, Jaehan Park** · 2025-01-29

<details>
<summary>Abstract</summary>

Despite remarkable advancements in recent voice conversion (VC) systems, enhancing speaker similarity in zero-shot scenarios remains challenging. This challenge arises from the difficulty of generalizing and adapting speaker characteristics in speech within zero-shot environments, which is further complicated by mismatch between the training and inference processes. To address these challenges, we propose VoicePrompter, a robust zero-shot VC model that leverages in-context learning with voice prompts. VoicePrompter is composed of (1) a factorization method that disentangles speech components and (2) a DiT-based conditional flow matching (CFM) decoder that conditions on these factorized features and voice prompts. Additionally, (3) latent mixup is used to enhance in-context learning by combining various speaker features. This approach improves speaker similarity and naturalness in zero-shot VC by applying mixup to latent representations. Experimental results demonstrate that VoicePrompter outperforms existing zero-shot VC systems in terms of speaker similarity, speech intelligibility, and audio quality. Our demo is available at \url{https://hayeong0.github.io/VoicePrompter-demo/}.

</details>

### [CSEval: Towards Automated, Multi-Dimensional, and Reference-Free Counterspeech Evaluation using Auto-Calibrated LLMs](2501.17581.md)
**Amey Hengle, Aswini Kumar, Anil Bandhakavi, Tanmoy Chakraborty** · 2025-01-29

<details>
<summary>Abstract</summary>

Counterspeech has emerged as a popular and effective strategy for combating online hate speech, sparking growing research interest in automating its generation using language models. However, the field still lacks standardised evaluation protocols and reliable automated evaluation metrics that align with human judgement. Current automatic evaluation methods, primarily based on similarity metrics, do not effectively capture the complex and independent attributes of counterspeech quality, such as contextual relevance, aggressiveness, or argumentative coherence. This has led to an increased dependency on labor-intensive human evaluations to assess automated counter-speech generation methods. To address these challenges, we introduce CSEval, a novel dataset and framework for evaluating counterspeech quality across four dimensions: contextual-relevance, aggressiveness, argument-coherence, and suitableness. Furthermore, we propose Auto-Calibrated COT for Counterspeech Evaluation (Auto-CSEval), a prompt-based method with auto-calibrated chain-of-thoughts (CoT) for scoring counterspeech using large language models. Our experiments show that Auto-CSEval outperforms traditional metrics like ROUGE, METEOR, and BertScore in correlating with human judgement, indicating a significant improvement in automated counterspeech evaluation.

</details>

### [Compact Neural TTS Voices for Accessibility](2501.17332.md)
**Kunal Jain et.al.** · 2025-01-28

### [Emilia: A Large-Scale, Extensive, Multilingual, and Diverse Dataset for Speech Generation](2501.15907.md)
**Haorui He et.al.** · 2025-01-27

### [Overview of the Amphion Toolkit (v0.2)](2501.15442.md)
**Jiaqi Li, Xueyao Zhang, Yuancheng Wang, Haorui He et al.** · 2025-01-26

<details>
<summary>Abstract</summary>

Amphion is an open-source toolkit for Audio, Music, and Speech Generation, designed to lower the entry barrier for junior researchers and engineers in these fields. It provides a versatile framework that supports a variety of generation tasks and models. In this report, we introduce Amphion v0.2, the second major release developed in 2024. This release features a 100K-hour open-source multilingual dataset, a robust data preparation pipeline, and novel models for tasks such as text-to-speech, audio coding, and voice conversion. Furthermore, the report includes multiple tutorials that guide users through the functionalities and usage of the newly released models.

</details>

### [Stepback: Enhanced Disentanglement for Voice Conversion via Multi-Task Learning](2501.15613.md)
**Qian Yang, Calbert Graham** · 2025-01-26

<details>
<summary>Abstract</summary>

Voice conversion (VC) modifies voice characteristics while preserving linguistic content. This paper presents the Stepback network, a novel model for converting speaker identity using non-parallel data. Unlike traditional VC methods that rely on parallel data, our approach leverages deep learning techniques to enhance disentanglement completion and linguistic content preservation. The Stepback network incorporates a dual flow of different domain data inputs and uses constraints with self-destructive amendments to optimize the content encoder. Extensive experiments show that our model significantly improves VC performance, reducing training costs while achieving high-quality voice conversion. The Stepback network's design offers a promising solution for advanced voice conversion tasks.

</details>

### [Characteristic-Specific Partial Fine-Tuning for Efficient Emotion and Speaker Adaptation in Codec Language Text-to-Speech Models](2501.14273.md)
**Tianrui Wang et.al.** · 2025-01-24

### [Generalizable Audio Deepfake Detection via Latent Space Refinement and Augmentation](2501.14240.md)
**Wen Huang, Yanmei Gu, Zhiming Wang, Huijia Zhu et al.** · 2025-01-24

<details>
<summary>Abstract</summary>

Advances in speech synthesis technologies, like text-to-speech (TTS) and voice conversion (VC), have made detecting deepfake speech increasingly challenging. Spoofing countermeasures often struggle to generalize effectively, particularly when faced with unseen attacks. To address this, we propose a novel strategy that integrates Latent Space Refinement (LSR) and Latent Space Augmentation (LSA) to improve the generalization of deepfake detection systems. LSR introduces multiple learnable prototypes for the spoof class, refining the latent space to better capture the intricate variations within spoofed data. LSA further diversifies spoofed data representations by applying augmentation techniques directly in the latent space, enabling the model to learn a broader range of spoofing patterns. We evaluated our approach on four representative datasets, i.e. ASVspoof 2019 LA, ASVspoof 2021 LA and DF, and In-The-Wild. The results show that LSR and LSA perform well individually, and their integration achieves competitive results, matching or surpassing current state-of-the-art methods.

</details>

### [Deepfake Technology Unveiled: The Commoditization of AI and Its Impact on Digital Trust](2506.07363.md)
**Claudiu Popa, Rex Pallath, Liam Cunningham, Hewad Tahiri et al.** · 2025-01-24

<details>
<summary>Abstract</summary>

Deepfake Technology Unveiled: The Commoditization of AI and Its Impact on Digital Trust. With the increasing accessibility of generative AI, tools for voice cloning, face-swapping, and synthetic media creation have advanced significantly, lowering both financial and technical barriers for their use. While these technologies present innovative opportunities, their rapid growth raises concerns about trust, privacy, and security. This white paper explores the implications of deepfake technology, analyzing its role in enabling fraud, misinformation, and the erosion of authenticity in multimedia. Using cost-effective, easy to use tools such as Runway, Rope, and ElevenLabs, we explore how realistic deepfakes can be created with limited resources, demonstrating the risks posed to individuals and organizations alike. By analyzing the technical and ethical challenges of deepfake mitigation and detection, we emphasize the urgent need for regulatory frameworks, public awareness, and collaborative efforts to maintain trust in digital media.

</details>

### [Everyone-Can-Sing: Zero-Shot Singing Voice Synthesis and Conversion with Speech Reference](2501.13870.md)
**Shuqi Dai et.al.** · 2025-01-23

### [Generative Data Augmentation Challenge: Zero-Shot Speech Synthesis for Personalized Speech Enhancement](2501.13372.md)
**Jae-Sung Bae et.al.** · 2025-01-23

### [Neural Vocoders as Speech Enhancers](2501.13465.md)
**Andong Li, Zhihang Sun, Fengyuan Hao, Xiaodong Li et al.** · 2025-01-23

<details>
<summary>Abstract</summary>

Speech enhancement (SE) and neural vocoding are traditionally viewed as separate tasks. In this work, we observe them under a common thread: the rank behavior of these processes. This observation prompts two key questions: \textit{Can a model designed for one task's rank degradation be adapted for the other?} and \textit{Is it possible to address both tasks using a unified model?} Our empirical findings demonstrate that existing speech enhancement models can be successfully trained to perform vocoding tasks, and a single model, when jointly trained, can effectively handle both tasks with performance comparable to separately trained models. These results suggest that speech enhancement and neural vocoding can be unified under a broader framework of speech restoration. Code: https://github.com/Andong-Li-speech/Neural-Vocoders-as-Speech-Enhancers.

</details>

### [Why disentanglement-based speaker anonymization systems fail at preserving emotions?](2501.13000.md)
**Ünal Ege Gaznepoglu, Nils Peters** · 2025-01-22

<details>
<summary>Abstract</summary>

Disentanglement-based speaker anonymization involves decomposing speech into a semantically meaningful representation, altering the speaker embedding, and resynthesizing a waveform using a neural vocoder. State-of-the-art systems of this kind are known to remove emotion information. Possible reasons include mode collapse in GAN-based vocoders, unintended modeling and modification of emotions through speaker embeddings, or excessive sanitization of the intermediate representation. In this paper, we conduct a comprehensive evaluation of a state-of-the-art speaker anonymization system to understand the underlying causes. We conclude that the main reason is the lack of emotion-related information in the intermediate representation. The speaker embeddings also have a high impact, if they are learned in a generative context. The vocoder's out-of-distribution performance has a smaller impact. Additionally, we discovered that synthesis artifacts increase spectral kurtosis, biasing emotion recognition evaluation towards classifying utterances as angry. Therefore, we conclude that reporting unweighted average recall alone for emotion recognition performance is suboptimal.

</details>

### [A Non-autoregressive Model for Joint STT and TTS](2501.09104.md)
**Vishal Sunder et.al.** · 2025-01-20

### [Towards Lightweight and Stable Zero-shot TTS with Self-distilled Representation Disentanglement](2501.08566.md)
**Qianniu Chen et.al.** · 2025-01-15

### [Speech Synthesis along Perceptual Voice Quality Dimensions](2501.08791.md)
**Frederik Rautenberg, Michael Kuhlmann, Fritz Seebauer, Jana Wiechmann et al.** · 2025-01-15

<details>
<summary>Abstract</summary>

While expressive speech synthesis or voice conversion systems mainly focus on controlling or manipulating abstract prosodic characteristics of speech, such as emotion or accent, we here address the control of perceptual voice qualities (PVQs) recognized by phonetic experts, which are speech properties at a lower level of abstraction. The ability to manipulate PVQs can be a valuable tool for teaching speech pathologists in training or voice actors. In this paper, we integrate a Conditional Continuous-Normalizing-Flow-based method into a Text-to-Speech system to modify perceptual voice attributes on a continuous scale. Unlike previous approaches, our system avoids direct manipulation of acoustic correlates and instead learns from examples. We demonstrate the system's capability by manipulating four voice qualities: Roughness, breathiness, resonance and weight. Phonetic experts evaluated these modifications, both for seen and unseen speaker conditions. The results highlight both the system's strengths and areas for improvement.

</details>

### [AI-Powered Assistive Technologies for Visual Impairment](2503.15494.md)
**Prudhvi Naayini, Praveen Kumar Myakala, Chiranjeevi Bura, Anil Kumar Jonnalagadda et al.** · 2025-01-14

<details>
<summary>Abstract</summary>

Artificial Intelligence (AI) is revolutionizing assistive technologies. It offers innovative solutions to enhance the quality of life for individuals with visual impairments. This review examines the development, applications, and impact of AI-powered tools in key domains, such as computer vision, natural language processing (NLP), and wearable devices. Specific advancements include object recognition for identifying everyday items, scene description for understanding surroundings, and NLP-driven text-to-speech systems for accessing digital information. Assistive technologies like smart glasses, smartphone applications, and AI-enabled navigation aids are discussed, demonstrating their ability to support independent travel, facilitate social interaction, and increase access to education and employment opportunities. The integration of deep learning models, multimodal interfaces, and real-time data processing has transformed the functionality and usability of these tools, fostering inclusivity and empowerment. This article also addresses critical challenges, including ethical considerations, affordability, and adaptability in diverse environments. Future directions highlight the need for interdisciplinary collaboration to refine these technologies, ensuring equitable access and sustainable innovation. By providing a comprehensive overview, this review underscores AI's transformative potential in promoting independence, enhancing accessibility, and fostering social inclusion for visually impaired individuals.

</details>

### [CodecFake+: Codec-Based Resynthesized Data as a Proxy for Detecting CodecFake Speech](2501.08238.md)
**Xuanjun Chen, Jiawei Du, Haibin Wu, Lin Zhang et al.** · 2025-01-14

<details>
<summary>Abstract</summary>

With the rapid advancement of neural audio codecs, codec-based speech generation (CoSG) systems have become highly powerful. Unfortunately, CoSG also enables the creation of highly realistic deepfake speech, making it easier to mimic an individual's voice and spread misinformation. We refer to this emerging deepfake speech generated by CoSG systems as CodecFake. Detecting such CodecFake is an urgent challenge, yet most existing systems primarily focus on detecting fake speech generated by traditional speech synthesis models. In this paper, we introduce CodecFake+, a large-scale dataset designed to advance CodecFake detection. To our knowledge, CodecFake+ is the largest dataset encompassing the most diverse range of codec architectures. The training set is generated through re-synthesis using 31 publicly available open-source codec models, while the evaluation set includes web-sourced data from 17 advanced CoSG models. We also propose a comprehensive taxonomy that categorizes codecs by their root components: vector quantizer, auxiliary objectives, and decoder types. Our proposed dataset and taxonomy enable detailed analysis at multiple levels to discern the key factors for successful CodecFake detection. At the individual codec level, we validate the effectiveness of using codec re-synthesized speech (CoRS) as training data for large-scale CodecFake detection. At the taxonomy level, we show that detection performance is strongest when the re-synthesis model incorporates disentanglement auxiliary objectives or a frequency-domain decoder. Furthermore, from the perspective of using all the CoRS training data, we show that our proposed taxonomy can be used to select better training data for improving detection performance. Overall, we envision that CodecFake+ will be a valuable resource for both general and fine-grained exploration to develop better anti-spoofing models against CodecFake.

</details>

### [MathReader : Text-to-Speech for Mathematical Documents](2501.07088.md)
**Sieun Hyeon, Kyudan Jung, Nam-Joon Kim, Hyun Gon Ryu et al.** · 2025-01-13

<details>
<summary>Abstract</summary>

TTS (Text-to-Speech) document reader from Microsoft, Adobe, Apple, and OpenAI have been serviced worldwide. They provide relatively good TTS results for general plain text, but sometimes skip contents or provide unsatisfactory results for mathematical expressions. This is because most modern academic papers are written in LaTeX, and when LaTeX formulas are compiled, they are rendered as distinctive text forms within the document. However, traditional TTS document readers output only the text as it is recognized, without considering the mathematical meaning of the formulas. To address this issue, we propose MathReader, which effectively integrates OCR, a fine-tuned T5 model, and TTS. MathReader demonstrated a lower Word Error Rate (WER) than existing TTS document readers, such as Microsoft Edge and Adobe Acrobat, when processing documents containing mathematical formulas. MathReader reduced the WER from 0.510 to 0.281 compared to Microsoft Edge, and from 0.617 to 0.281 compared to Adobe Acrobat. This will significantly contribute to alleviating the inconvenience faced by users who want to listen to documents, especially those who are visually impaired. The code is available at https://github.com/hyeonsieun/MathReader.

</details>

### [Exploring the encoding of linguistic representations in the Fully-Connected Layer of generative CNNs for Speech](2501.07726.md)
**Bruno Ferenc Šegedin, Gasper Beguš** · 2025-01-13

<details>
<summary>Abstract</summary>

Interpretability work on the convolutional layers of CNNs has primarily focused on computer vision, but some studies also explore correspondences between the latent space and the output in the audio domain. However, it has not been thoroughly examined how acoustic and linguistic information is represented in the fully connected (FC) layer that bridges the latent space and convolutional layers. The current study presents the first exploration of how the FC layer of CNNs for speech synthesis encodes linguistically relevant information. We propose two techniques for exploration of the fully connected layer. In Experiment 1, we use weight matrices as inputs into convolutional layers. In Experiment 2, we manipulate the FC layer to explore how symbolic-like representations are encoded in CNNs. We leverage the fact that the FC layer outputs a feature map and that variable-specific weight matrices are temporally structured to (1) demonstrate how the distribution of learned weights varies between latent variables in systematic ways and (2) demonstrate how manipulating the FC layer while holding constant subsequent model parameters affects the output. We ultimately present an FC manipulation that can output a single segment. Using this technique, we show that lexically specific latent codes in generative CNNs (ciwGAN) have shared lexically invariant sublexical representations in the FC-layer weights, showing that ciwGAN encodes lexical information in a linguistically principled manner.

</details>

### [Retrieval-Augmented Dialogue Knowledge Aggregation for Expressive Conversational Speech Synthesis](2501.06467.md)
**Rui Liu, Zhenqi Jia, Feilong Bao, Haizhou Li** · 2025-01-11

<details>
<summary>Abstract</summary>

Conversational speech synthesis (CSS) aims to take the current dialogue (CD) history as a reference to synthesize expressive speech that aligns with the conversational style. Unlike CD, stored dialogue (SD) contains preserved dialogue fragments from earlier stages of user-agent interaction, which include style expression knowledge relevant to scenarios similar to those in CD. Note that this knowledge plays a significant role in enabling the agent to synthesize expressive conversational speech that generates empathetic feedback. However, prior research has overlooked this aspect. To address this issue, we propose a novel Retrieval-Augmented Dialogue Knowledge Aggregation scheme for expressive CSS, termed RADKA-CSS, which includes three main components: 1) To effectively retrieve dialogues from SD that are similar to CD in terms of both semantic and style. First, we build a stored dialogue semantic-style database (SDSSD) which includes the text and audio samples. Then, we design a multi-attribute retrieval scheme to match the dialogue semantic and style vectors of the CD with the stored dialogue semantic and style vectors in the SDSSD, retrieving the most similar dialogues. 2) To effectively utilize the style knowledge from CD and SD, we propose adopting the multi-granularity graph structure to encode the dialogue and introducing a multi-source style knowledge aggregation mechanism. 3) Finally, the aggregated style knowledge are fed into the speech synthesizer to help the agent synthesize expressive speech that aligns with the conversational style. We conducted a comprehensive and in-depth experiment based on the DailyTalk dataset, which is a benchmarking dataset for the CSS task. Both objective and subjective evaluations demonstrate that RADKA-CSS outperforms baseline models in expressiveness rendering. Code and audio samples can be found at: https://github.com/Coder-jzq/RADKA-CSS.

</details>

### [Unispeaker: A Unified Approach for Multimodality-driven Speaker Generation](2501.06394.md)
**Zhengyan Sheng, Zhihao Du, Heng Lu, Shiliang Zhang et al.** · 2025-01-11

<details>
<summary>Abstract</summary>

Recent advancements in personalized speech generation have brought synthetic speech increasingly close to the realism of target speakers' recordings, yet multimodal speaker generation remains on the rise. This paper introduces UniSpeaker, a unified approach for multimodality-driven speaker generation. Specifically, we propose a unified voice aggregator based on KV-Former, applying soft contrastive loss to map diverse voice description modalities into a shared voice space, ensuring that the generated voice aligns more closely with the input descriptions. To evaluate multimodality-driven voice control, we build the first multimodality-based voice control (MVC) benchmark, focusing on voice suitability, voice diversity, and speech quality. UniSpeaker is evaluated across five tasks using the MVC benchmark, and the experimental results demonstrate that UniSpeaker outperforms previous modality-specific models. Speech samples are available at \url{https://UniSpeaker.github.io}.

</details>

### [TTS-Transducer: End-to-End Speech Synthesis with Neural Transducer](2501.06320.md)
**Vladimir Bataev et.al.** · 2025-01-10

### [Low-Resource Text-to-Speech Synthesis Using Noise-Augmented Training of ForwardTacotron](2501.05976.md)
**Kishor Kayyar Lakshminarayana et.al.** · 2025-01-10

### [MARS6: A Small and Robust Hierarchical-Codec Text-to-Speech Model](2501.05787.md)
**Matthew Baas et.al.** · 2025-01-10

### [MinMo: A Multimodal Large Language Model for Seamless Voice Interaction](2501.06282.md)
**Qian Chen, Yafeng Chen, Yanni Chen, Mengzhe Chen et al.** · 2025-01-10

<details>
<summary>Abstract</summary>

Recent advancements in large language models (LLMs) and multimodal speech-text models have laid the groundwork for seamless voice interactions, enabling real-time, natural, and human-like conversations. Previous models for voice interactions are categorized as native and aligned. Native models integrate speech and text processing in one framework but struggle with issues like differing sequence lengths and insufficient pre-training. Aligned models maintain text LLM capabilities but are often limited by small datasets and a narrow focus on speech tasks. In this work, we introduce MinMo, a Multimodal Large Language Model with approximately 8B parameters for seamless voice interaction. We address the main limitations of prior aligned multimodal models. We train MinMo through multiple stages of speech-to-text alignment, text-to-speech alignment, speech-to-speech alignment, and duplex interaction alignment, on 1.4 million hours of diverse speech data and a broad range of speech tasks. After the multi-stage training, MinMo achieves state-of-the-art performance across various benchmarks for voice comprehension and generation while maintaining the capabilities of text LLMs, and also facilitates full-duplex conversation, that is, simultaneous two-way communication between the user and the system. Moreover, we propose a novel and simple voice decoder that outperforms prior models in voice generation. The enhanced instruction-following capabilities of MinMo supports controlling speech generation based on user instructions, with various nuances including emotions, dialects, and speaking rates, and mimicking specific voices. For MinMo, the speech-to-text latency is approximately 100ms, full-duplex latency is approximately 600ms in theory and 800ms in practice. The MinMo project web page is https://funaudiollm.github.io/minmo, and the code and models will be released soon.

</details>

### [PROEMO: Prompt-Driven Text-to-Speech Synthesis Based on Emotion and Intensity Control](2501.06276.md)
**Shaozuo Zhang, Ambuj Mehrish, Yingting Li, Soujanya Poria** · 2025-01-10

<details>
<summary>Abstract</summary>

Speech synthesis has significantly advanced from statistical methods to deep neural network architectures, leading to various text-to-speech (TTS) models that closely mimic human speech patterns. However, capturing nuances such as emotion and style in speech synthesis is challenging. To address this challenge, we introduce an approach centered on prompt-based emotion control. The proposed architecture incorporates emotion and intensity control across multi-speakers. Furthermore, we leverage large language models (LLMs) to manipulate speech prosody while preserving linguistic content. Using embedding emotional cues, regulating intensity levels, and guiding prosodic variations with prompts, our approach infuses synthesized speech with human-like expressiveness and variability. Lastly, we demonstrate the effectiveness of our approach through a systematic exploration of the control mechanisms mentioned above.

</details>

### [JELLY: Joint Emotion Recognition and Context Reasoning with LLMs for Conversational Speech Synthesis](2501.04904.md)
**Jun-Hyeok Cha et.al.** · 2025-01-09

### [OpenOmni: Large Language Models Pivot Zero-shot Omnimodal Alignment across Language with Real-time Self-Aware Emotional Speech Synthesis](2501.04561.md)
**Run Luo et.al.** · 2025-01-09

### [FreeSVC: Towards Zero-shot Multilingual Singing Voice Conversion](2501.05586.md)
**Alef Iury Siqueira Ferreira, Lucas Rafael Gris, Augusto Seben da Rosa, Frederico Santos de Oliveira et al.** · 2025-01-09

<details>
<summary>Abstract</summary>

This work presents FreeSVC, a promising multilingual singing voice conversion approach that leverages an enhanced VITS model with Speaker-invariant Clustering (SPIN) for better content representation and the State-of-the-Art (SOTA) speaker encoder ECAPA2. FreeSVC incorporates trainable language embeddings to handle multiple languages and employs an advanced speaker encoder to disentangle speaker characteristics from linguistic content. Designed for zero-shot learning, FreeSVC enables cross-lingual singing voice conversion without extensive language-specific training. We demonstrate that a multilingual content extractor is crucial for optimal cross-language conversion. Our source code and models are publicly available.

</details>

### [Cued Speech Generation Leveraging a Pre-trained Audiovisual Text-to-Speech Model](2501.04799.md)
**Sanjana Sankar et.al.** · 2025-01-08

### [DrawSpeech: Expressive Speech Synthesis Using Prosodic Sketches as Control Conditions](2501.04256.md)
**Weidong Chen, Shan Yang, Guangzhi Li, Xixin Wu** · 2025-01-08

<details>
<summary>Abstract</summary>

Controlling text-to-speech (TTS) systems to synthesize speech with the prosodic characteristics expected by users has attracted much attention. To achieve controllability, current studies focus on two main directions: (1) using reference speech as prosody prompt to guide speech synthesis, and (2) using natural language descriptions to control the generation process. However, finding reference speech that exactly contains the prosody that users want to synthesize takes a lot of effort. Description-based guidance in TTS systems can only determine the overall prosody, which has difficulty in achieving fine-grained prosody control over the synthesized speech. In this paper, we propose DrawSpeech, a sketch-conditioned diffusion model capable of generating speech based on any prosody sketches drawn by users. Specifically, the prosody sketches are fed to DrawSpeech to provide a rough indication of the expected prosody trends. DrawSpeech then recovers the detailed pitch and energy contours based on the coarse sketches and synthesizes the desired speech. Experimental results show that DrawSpeech can generate speech with a wide variety of prosody and can precisely control the fine-grained prosody in a user-friendly manner. Our implementation and audio samples are publicly available.

</details>

### [FleSpeech: Flexibly Controllable Speech Generation with Various Prompts](2501.04644.md)
**Hanzhao Li, Yuke Li, Xinsheng Wang, Jingbin Hu et al.** · 2025-01-08

<details>
<summary>Abstract</summary>

Controllable speech generation methods typically rely on single or fixed prompts, hindering creativity and flexibility. These limitations make it difficult to meet specific user needs in certain scenarios, such as adjusting the style while preserving a selected speaker's timbre, or choosing a style and generating a voice that matches a character's visual appearance. To overcome these challenges, we propose \textit{FleSpeech}, a novel multi-stage speech generation framework that allows for more flexible manipulation of speech attributes by integrating various forms of control. FleSpeech employs a multimodal prompt encoder that processes and unifies different text, audio, and visual prompts into a cohesive representation. This approach enhances the adaptability of speech synthesis and supports creative and precise control over the generated speech. Additionally, we develop a data collection pipeline for multimodal datasets to facilitate further research and applications in this field. Comprehensive subjective and objective experiments demonstrate the effectiveness of FleSpeech. Audio samples are available at https://kkksuper.github.io/FleSpeech/

</details>

### [ZSVC: Zero-shot Style Voice Conversion with Disentangled Latent Diffusion Models and Adversarial Training](2501.04416.md)
**Xinfa Zhu, Lei He, Yujia Xiao, Xi Wang et al.** · 2025-01-08

<details>
<summary>Abstract</summary>

Style voice conversion aims to transform the speaking style of source speech into a desired style while keeping the original speaker's identity. However, previous style voice conversion approaches primarily focus on well-defined domains such as emotional aspects, limiting their practical applications. In this study, we present ZSVC, a novel Zero-shot Style Voice Conversion approach that utilizes a speech codec and a latent diffusion model with speech prompting mechanism to facilitate in-context learning for speaking style conversion. To disentangle speaking style and speaker timbre, we introduce information bottleneck to filter speaking style in the source speech and employ Uncertainty Modeling Adaptive Instance Normalization (UMAdaIN) to perturb the speaker timbre in the style prompt. Moreover, we propose a novel adversarial training strategy to enhance in-context learning and improve style similarity. Experiments conducted on 44,000 hours of speech data demonstrate the superior performance of ZSVC in generating speech with diverse speaking styles in zero-shot scenarios.

</details>

### [Finding A Voice: Exploring the Potential of African American Dialect and Voice Generation for Chatbots](2501.03441.md)
**Sarah E. Finch, Ellie S. Paek, Ikseon Choi, Jinho D. Choi** · 2025-01-07

<details>
<summary>Abstract</summary>

As chatbots become integral to daily life, personalizing systems is key for fostering trust, engagement, and inclusivity. This study examines how linguistic similarity affects chatbot performance, focusing on integrating African American English (AAE) into virtual agents to better serve the African American community. We develop text-based and spoken chatbots using large language models and text-to-speech technology, then evaluate them with AAE speakers against standard English chatbots. Our results show that while text-based AAE chatbots often underperform, spoken chatbots benefit from an African American voice and AAE elements, improving performance and preference. These findings underscore the complexities of linguistic personalization and the dynamics between text and speech modalities, highlighting technological limitations that affect chatbots' AA speech generation and pointing to promising future research directions.

</details>

### [NeuroIncept Decoder for High-Fidelity Speech Reconstruction from Neural Activity](2501.03757.md)
**Owais Mujtaba Khanday, José L. Pérez-Córdoba, Mohd Yaqub Mir, Ashfaq Ahmad Najar et al.** · 2025-01-07

<details>
<summary>Abstract</summary>

This paper introduces a novel algorithm designed for speech synthesis from neural activity recordings obtained using invasive electroencephalography (EEG) techniques. The proposed system offers a promising communication solution for individuals with severe speech impairments. Central to our approach is the integration of time-frequency features in the high-gamma band computed from EEG recordings with an advanced NeuroIncept Decoder architecture. This neural network architecture combines Convolutional Neural Networks (CNNs) and Gated Recurrent Units (GRUs) to reconstruct audio spectrograms from neural patterns. Our model demonstrates robust mean correlation coefficients between predicted and actual spectrograms, though inter-subject variability indicates distinct neural processing mechanisms among participants. Overall, our study highlights the potential of neural decoding techniques to restore communicative abilities in individuals with speech disorders and paves the way for future advancements in brain-computer interface technologies.

</details>

### [Generating and Detecting Various Types of Fake Image and Audio Content: A Review of Modern Deep Learning Technologies and Tools](2501.06227.md)
**Arash Dehghani, Hossein Saberi** · 2025-01-07

<details>
<summary>Abstract</summary>

This paper reviews the state-of-the-art in deepfake generation and detection, focusing on modern deep learning technologies and tools based on the latest scientific advancements. The rise of deepfakes, leveraging techniques like Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs), Diffusion models and other generative models, presents significant threats to privacy, security, and democracy. This fake media can deceive individuals, discredit real people and organizations, facilitate blackmail, and even threaten the integrity of legal, political, and social systems. Therefore, finding appropriate solutions to counter the potential threats posed by this technology is essential. We explore various deepfake methods, including face swapping, voice conversion, reenactment and lip synchronization, highlighting their applications in both benign and malicious contexts. The review critically examines the ongoing "arms race" between deepfake generation and detection, analyzing the challenges in identifying manipulated contents. By examining current methods and highlighting future research directions, this paper contributes to a crucial understanding of this rapidly evolving field and the urgent need for robust detection strategies to counter the misuse of this powerful technology. While focusing primarily on audio, image, and video domains, this study allows the reader to easily grasp the latest advancements in deepfake generation and detection.

</details>

### [SYKI-SVC: Advancing Singing Voice Conversion with Post-Processing Innovations and an Open-Source Professional Testset](2501.02953.md)
**Yiquan Zhou, Wenyu Wang, Hongwu Ding, Jiacheng Xu et al.** · 2025-01-06

<details>
<summary>Abstract</summary>

Singing voice conversion aims to transform a source singing voice into that of a target singer while preserving the original lyrics, melody, and various vocal techniques. In this paper, we propose a high-fidelity singing voice conversion system. Our system builds upon the SVCC T02 framework and consists of three key components: a feature extractor, a voice converter, and a post-processor. The feature extractor utilizes the ContentVec and Whisper models to derive F0 contours and extract speaker-independent linguistic features from the input singing voice. The voice converter then integrates the extracted timbre, F0, and linguistic content to synthesize the target speaker's waveform. The post-processor augments high-frequency information directly from the source through simple and effective signal processing to enhance audio quality. Due to the lack of a standardized professional dataset for evaluating expressive singing conversion systems, we have created and made publicly available a specialized test set. Comparative evaluations demonstrate that our system achieves a remarkably high level of naturalness, and further analysis confirms the efficacy of our proposed system design.

</details>

### [CycleFlow: Leveraging Cycle Consistency in Flow Matching for Speaker Style Adaptation](2501.01861.md)
**Ziqi Liang, Xulong Zhang, Chang Liu, Xiaoyang Qu et al.** · 2025-01-03

<details>
<summary>Abstract</summary>

Voice Conversion (VC) aims to convert the style of a source speaker, such as timbre and pitch, to the style of any target speaker while preserving the linguistic content. However, the ground truth of the converted speech does not exist in a non-parallel VC scenario, which induces the train-inference mismatch problem. Moreover, existing methods still have an inaccurate pitch and low speaker adaptation quality, there is a significant disparity in pitch between the source and target speaker style domains. As a result, the models tend to generate speech with hoarseness, posing challenges in achieving high-quality voice conversion. In this study, we propose CycleFlow, a novel VC approach that leverages cycle consistency in conditional flow matching (CFM) for speaker timbre adaptation training on non-parallel data. Furthermore, we design a Dual-CFM based on VoiceCFM and PitchCFM to generate speech and improve speaker pitch adaptation quality. Experiments show that our method can significantly improve speaker similarity, generating natural and higher-quality speech.

</details>

### [Controlling your Attributes in Voice](2501.01674.md)
**Xuyuan Li, Zengqiang Shang. Li Wang, Pengyuan Zhang** · 2025-01-03

<details>
<summary>Abstract</summary>

Attribute control in generative tasks aims to modify personal attributes, such as age and gender while preserving the identity information in the source sample. Although significant progress has been made in controlling facial attributes in image generation, similar approaches for speech generation remain largely unexplored. This letter proposes a novel method for controlling speaker attributes in speech without parallel data. Our approach consists of two main components: a GAN-based speaker representation variational autoencoder that extracts speaker identity and attributes from speaker vector, and a two-stage voice conversion model that captures the natural expression of speaker attributes in speech. Experimental results show that our proposed method not only achieves attribute control at the speaker representation level but also enables manipulation of the speaker age and gender at the speech level while preserving speech quality and speaker identity.

</details>

### [RingFormer: A Neural Vocoder with Ring Attention and Convolution-Augmented Transformer](2501.01182.md)
**Seongho Hong et.al.** · 2025-01-02

### [Disambiguation of Chinese Polyphones in an End-to-End Framework with Semantic Features Extracted by Pre-trained BERT](2501.01102.md)
**Dongyang Dai, Zhiyong Wu, Shiyin Kang, Xixin Wu et al.** · 2025-01-02

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion serves as an essential component in Chinese Mandarin text-to-speech (TTS) system, where polyphone disambiguation is the core issue. In this paper, we propose an end-to-end framework to predict the pronunciation of a polyphonic character, which accepts sentence containing polyphonic character as input in the form of Chinese character sequence without the necessity of any preprocessing. The proposed method consists of a pre-trained bidirectional encoder representations from Transformers (BERT) model and a neural network (NN) based classifier. The pre-trained BERT model extracts semantic features from a raw Chinese character sequence and the NN based classifier predicts the polyphonic character's pronunciation according to BERT output. In out experiments, we implemented three classifiers, a fully-connected network based classifier, a long short-term memory (LSTM) network based classifier and a Transformer block based classifier. The experimental results compared with the baseline approach based on LSTM demonstrate that, the pre-trained model extracts effective semantic features, which greatly enhances the performance of polyphone disambiguation. In addition, we also explored the impact of contextual information on polyphone disambiguation.

</details>

### [FaceSpeak: Expressive and High-Quality Speech Synthesis from Human Portraits of Different Styles](2501.03181.md)
**Tian-Hao Zhang, Jiawei Zhang, Jun Wang, Xinyuan Qian et al.** · 2025-01-02

<details>
<summary>Abstract</summary>

Humans can perceive speakers' characteristics (e.g., identity, gender, personality and emotion) by their appearance, which are generally aligned to their voice style. Recently, vision-driven Text-to-speech (TTS) scholars grounded their investigations on real-person faces, thereby restricting effective speech synthesis from applying to vast potential usage scenarios with diverse characters and image styles. To solve this issue, we introduce a novel FaceSpeak approach. It extracts salient identity characteristics and emotional representations from a wide variety of image styles. Meanwhile, it mitigates the extraneous information (e.g., background, clothing, and hair color, etc.), resulting in synthesized speech closely aligned with a character's persona. Furthermore, to overcome the scarcity of multi-modal TTS data, we have devised an innovative dataset, namely Expressive Multi-Modal TTS, which is diligently curated and annotated to facilitate research in this domain. The experimental results demonstrate our proposed FaceSpeak can generate portrait-aligned voice with satisfactory naturalness and quality.

</details>

### [AdaptVC: High Quality Voice Conversion with Adaptive Learning](2501.01347.md)
**Jaehun Kim, Ji-Hoon Kim, Yeunju Choi, Tan Dat Nguyen et al.** · 2025-01-02

<details>
<summary>Abstract</summary>

The goal of voice conversion is to transform the speech of a source speaker to sound like that of a reference speaker while preserving the original content. A key challenge is to extract disentangled linguistic content from the source and voice style from the reference. While existing approaches leverage various methods to isolate the two, a generalization still requires further attention, especially for robustness in zero-shot scenarios. In this paper, we achieve successful disentanglement of content and speaker features by tuning self-supervised speech features with adapters. The adapters are trained to dynamically encode nuanced features from rich self-supervised features, and the decoder fuses them to produce speech that accurately resembles the reference with minimal loss of content. Moreover, we leverage a conditional flow matching decoder with cross-attention speaker conditioning to further boost the synthesis quality and efficiency. Subjective and objective evaluations in a zero-shot scenario demonstrate that the proposed method outperforms existing models in speech quality and similarity to the reference speech.

</details>

### [Context-Aware Lexical Stress Prediction and Phonemization for Ukrainian TTS Systems](s2:e427d1adccfd47f322ae7ae1e83fce2164d86e15.md)
**Anastasiia Senyk, M. Lukianchuk, V. Robeiko, Yurii Paniv** · 2025-01-01

<details>
<summary>Abstract</summary>

Text preprocessing is a fundamental component of high-quality speech synthesis. This work presents a novel rule-based phonemizer combined with a sentence-level lexical stress prediction model to improve phonetic accuracy and prosody prediction in the text-to-speech pipelines. We also introduce a new benchmark dataset with annotated stress patterns designed for evaluating lexical stress prediction systems at the sentence level. Experimental results demonstrate that the proposed phonemizer achieves a 1.23% word error rate on a manually constructed pronunciation dataset, while the lexical stress prediction pipeline shows results close to dictionary-based methods, outperforming existing neural network solutions.

</details>

### [TM-SPEECH: END-TO-END TEXT TO SPEECH BASED ON INTEGRATING TRANSFORMER AND MAMBA](s2:dd62b9638086e422581f60e24e5b39d67f2eebe8.md)
**Long Wang** · 2025-01-01

<details>
<summary>Abstract</summary>

Text-to-speech synthesis is the process of converting natural language text into speech. In recent years, deep learning has made significant strides in this field. Although the Transformer model is effective at capturing dependencies, its attention mechanism’s quadratic complexity results in longer training times and increased costs. Recent advancements in state-space models SSMs have demonstrated impressive performance in modeling long-range dependencies due to their sub-quadratic complexity. Mamba, a notable example of SSMs, exhibits linear time complexity and excels in tasks involving long sequences, similar to those in natural language. In this paper, we propose TM-Speech, which integrates Mamba for modeling long-range dependencies and Transformer for capturing short-range dependencies, thereby reducing model training costs. Comparative experiments show that TM-Speech is almost 2× smaller and 3× faster than FastSpeech2 during training, while also achieving superior inferred audio quality. The code is available at https: github.com Apolarity886 TMSpeech.

</details>

### [Retraining-Free Pruning Text-to-Speech Synthesis Model for Speaker Cloning](s2:ea15b2537406e4900a0eeb7069f352227f169394.md)
**Ali Raheem Mandeel, Tamara Z. Fadhil, Mohammed Hamzah Alsalihi, M. Al-Radhi et al.** · 2025-01-01

<details>
<summary>Abstract</summary>

End-to-end text-to-speech (TTS) synthesis models can produce highly natural speech by drawing on large-scale pretraining with extensive datasets and subsequent adaptation to specific target speakers, such as voice cloning. However, as model sizes grow with increasingly comprehensive pretraining, fine-tuning all parameters for each speaker becomes both computationally demanding and resource-intensive. In this study, we adapted Pruning by Weights and Activations (Wanda), a technique initially developed for large language models, to reduce the parameter footprint of pretrained TTS models for voice cloning. Wanda leverages a simple yet effective metric to prune redundant parameters by multiplying weight magnitudes by input activation norms. It does not require post-retraining to preserve the synthesized speech quality and allows for efficient adaptation to cloned voices. Our proposed pruning TTS method uses two pruning schemes, structured Wanda (removes all units, such as neurons, filters, or channels) and unstructured Wanda (removes weights or individual connections based on magnitude or significance scores). Subjective and objective evaluations showed that the pruned TTS model exhibited promising results and was comparable to the baseline TTS model (non-pruned) at the one-quarter pruning level. Our proposed pruned TTS model subjectively achieved only a relatively small decline in naturalness of approximately 4.3% in a sparsity of one-quarter with the structured Wanda and 23% in moderate pruning levels of one-half using the unstructured Wanda. The findings demonstrate that our approach yields lightweight TTS models deployed efficiently to address the scalability challenges in modern speech synthesis systems. The outcome of this study supports the development of personalized TTS systems with potential applications for communication aids for individuals with speech disorders.

</details>

