# tts-papers

A curated, automatically-updated collection of papers on **text-to-speech synthesis**, neural vocoders, voice conversion, voice cloning, prosody, and related topics — starting from the Tacotron/WaveNet era (2017) and growing every week.

## How it works

* Papers are sourced from [arXiv](https://arxiv.org/) via its public API.
* A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs every **Monday at 06:00 UTC** to pull papers submitted in the previous week.
* The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Running locally

```bash
# Incremental fetch (last 8 days)
python scripts/fetch_papers.py

# Full historical fetch (everything since 2017-01-01)
python scripts/fetch_papers.py --full

# Custom window
python scripts/fetch_papers.py --days 30
```

No third-party dependencies are required — the script uses only the Python standard library.

## Triggering a manual update

Open the **Actions** tab → **Fetch TTS Papers** → **Run workflow**.  
Select *full = true* to back-fill from 2017, or leave it as *false* for an incremental update.

## Search terms

The following keyword queries are used against arXiv title and abstract fields:

`text to speech` · `text-to-speech` · `speech synthesis` · `neural text to speech` · `neural vocoder` · `voice conversion` · `voice cloning` · `speech generation` · `acoustic model speech` · `prosody prediction` · `expressive speech synthesis` · `zero-shot TTS` · `end-to-end speech synthesis` · `diffusion speech synthesis`

## Papers

<!-- PAPERS_TABLE_START -->
### 2026

#### [How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech](https://arxiv.org/abs/2606.20532)
**Nityanand Mathur, Hamees Sayed, Wasim Madha, Apoorv Singh et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

Style-captioned text-to-speech systems use natural language to control voice characteristics, but how individual words influence acoustic output remains unclear. Understanding this is critical for diagnosing failure modes and improving controllability in expressive TTS. We propose cross-attention attribution for speech diffusion models, adapting the DAAM framework to the speech domain for the first time, and apply it to CapSpeech-TTS. Our method extracts per-token heatmaps across 25 layers and 24 ODE steps. We analyze 3,600 (style caption, text transcript) combinations comprising 120 style captions conditioning the generation of 30 text transcripts each, revealing how caption tokens shape waveforms. Results show: (1) style tokens have lower temporal variance than content/function tokens, confirming global conditioning; (2) style attention correlates with F0 and energy; (3) style conditioning peaks in early steps and deep layers; (4) attention entropy reaches its minimum at layer 17, co-occurring with the style importance peak, indicating maximal network selectivity at the most style-critical stage. This is the first study of how natural language influences cross-attention in speech diffusion models

</details>

#### [FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS](https://arxiv.org/abs/2606.20518)
**Harshit Singh, Ayush Pratap Singh, Nityanand Mathur** · 2026-06-18

<details>
<summary>Abstract</summary>

Flow-matching text-to-speech systems achieve remarkable zero-shot quality but remain static after deployment: pronunciation errors on out-of-vocabulary proper nouns persist unless the model is retrained. We introduce FlowEdit, a life-long adaptation framework for frozen flow-matching TTS that learns pronunciation corrections as latent conditioning edits rather than weight updates. When corrective feedback is provided, FlowEdit optimizes a token-level perturbation in the text embedding space, then stores the correction in a Modern Hopfield Network serving as content-addressable episodic memory. At inference, corrections are retrieved via soft attention with a similarity gate, enabling fuzzy morphological matching. On our curated benchmark of 312 multilingual proper nouns across 18 language families, FlowEdit reduces target-word Phoneme Error Rate by 92.7% relative to the zero-shot baseline while maintaining identical general-speech quality. Corrections complete in approximately 15 seconds on a single GPU.

</details>

#### [Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning](https://arxiv.org/abs/2606.20266)
**SooHwan Eom, Hee Suk Yoon, Eunseop Yoon, Mark Hasegawa-Johnson et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

Recent flow-matching text-to-speech (TTS) models, such as F5-TTS, rely on a reference transcript at inference time, obtained from an external ASR system. This dependency makes zero-shot TTS brittle for accented or dysarthric speakers, precisely the scenarios where it is most needed. Moreover, we find that text-based reference conditioning can propagate atypical acoustic patterns from atypical speech into synthesis, even when ground-truth transcripts are available. To address this, we propose RTFree-F5, which replaces the reference transcript with continuous self-supervised speech representations mapped into F5-TTS's text-conditioning space via a lightweight adapter, while reusing the pretrained checkpoint. On dysarthric speech, RTFree-F5 reduces WER from 24.6% to 10.4%, surpassing even the ground-truth reference transcript baselines, while improving naturalness and remaining competitive on standard benchmarks without requiring any reference transcript.

</details>

#### [PASQA: Pitch-Accent-Focused Speech Quality Assessment Model Trained on Synthetic Speech with Accent Errors](https://arxiv.org/abs/2606.20137)
**Masaya Kawamura, Yuma Shirahata, Kentaro Mitsui, Reo Shimizu** · 2026-06-18

<details>
<summary>Abstract</summary>

Existing mean opinion score (MOS) prediction models typically predict utterance-level naturalness MOS and can be insensitive to localized pitch-accent errors. We propose Pitch-Accent-focused Speech Quality Assessment (PASQA), which explicitly targets pitch-accent correctness. To train our model, we construct a controlled Japanese accent-error dataset by changing accent patterns using an accent-controllable text-to-speech system, and compute a pseudo accent-quality score from the accent-error rate. PASQA builds on self-supervised representations and employs mora-conditioned fusion, ranking loss, an auxiliary accent-error localization task, and speaker-invariant training. Experiments show that conventional models fail to preserve the ordering by accent-error severity, whereas PASQA achieves high ordering accuracy on both seen and unseen speakers. Further, PASQA shows stronger agreement with human accent-correctness judgments. The code is available at https://github.com/lycorp-jp/PASQA.

</details>

#### [Investigating Human-Model Discrepancies in Speech Quality Assessment via Acoustic and Prosodic Perturbations](https://arxiv.org/abs/2606.19951)
**Masato Takagi, Masaya Kawamura, Reo Shimizu, Yuma Shirahata** · 2026-06-18

<details>
<summary>Abstract</summary>

Mean opinion score (MOS) prediction models are widely used as proxy metrics in text-to-speech (TTS) research, yet their ability to capture quality differences beyond acoustic fidelity remains unclear. We investigate this via controlled perturbations on speech: acoustic degradation, prosodic errors, and manipulation of speaker-specific characteristics such as pitch and speaking rate. We obtained MOS predictions for these speech samples from both human listeners and the model, and analyzed the differences in their perceptual characteristics. Results show that most models track acoustic degradation well, while all are insensitive to prosodic errors despite large subjective score drops. For speaker characteristics, models exhibit a double dissociation: strong mean fundamental frequency (F0) biases absent in human ratings, yet insensitivity to speaking rate and F0 variability that humans notice. These findings highlight limitations of scalar MOS prediction beyond acoustic fidelity.

</details>

#### [Exploring Pre-training Benefits on Phoneme Addition through Fine-tuning in Speech Synthesis](https://arxiv.org/abs/2606.19792)
**Masato Murata, Koichi Miyazaki, Tomoki Koriyama, Tomoki Toda** · 2026-06-18

<details>
<summary>Abstract</summary>

Transfer learning is widely used for low-resource text-to-speech. When the target corpus contains phonemes unseen in pre-training, the model must expand its phoneme inventory during fine-tuning; we call the process "phoneme addition." However, it remains unclear whether the pre-trained ability to generate seen phonemes contributes to this process. This study investigates phoneme addition in two settings: (1) a simulation setup using LLM-generated phoneme-controlled corpora that enables investigation without considering confounding factors, and (2) a real-speech cross-lingual transfer setup (English to Japanese) to validate whether the findings hold in practice. Experiments in both settings showed that while fine-tuning achieved higher naturalness than training from scratch, it required as much or more data to achieve comparable PER for new phonemes. These results indicate that pre-training mainly contributes to naturalness improvement, but offers limited benefit for phoneme addition.

</details>

#### [Repurposing a Speech Classifier for Guided Diffusion-Based Speech Generation](https://arxiv.org/abs/2606.20457)
**Rostislav Makarov, Timo Gerkmann** · 2026-06-18

<details>
<summary>Abstract</summary>

Classifier guidance is a way to control diffusion generation by using a noise-conditioned classifier to steer the sampling process toward a target class. One drawback of classifier guidance is that it requires two separately trained models: a classifier and a diffusion model. We therefore study a more compact alternative in which a conventionally trained speech classifier is repurposed as the backbone for diffusion generation. Starting from a frozen noise-conditioned classifier in log-Mel space, we attach a lightweight subnetwork that reuses intermediate classifier representations and train only this subnetwork under a Denoising Score Matching objective. Our work shows that a pretrained classifier can be repurposed for conditional generation, providing an appealing bridge between discriminative modeling and conditional speech synthesis resulting in high speech quality within a single-backbone model, with reduced memory footprint and computational cost.

</details>

#### [Interpreting Content and Speaker Characteristics in Factorised Self-Supervised Subspaces](https://arxiv.org/abs/2606.19974)
**Kyle Janse van Rensburg, Herman Kamper** · 2026-06-18

<details>
<summary>Abstract</summary>

Self-supervised speech features encode both content and speaker information. Recent work introduced an SVD-based factorisation that decomposes these features into a shared content matrix capturing temporal variation and speaker-specific transformations capturing static speaker characteristics. However, how information is organised within these components remains unclear. In this paper, we investigate how the dimensions of WavLM-factorised content and speaker subspaces correlate with speech characteristics such as pitch, intensity, and voicing. We find that leading dimensions in the content space primarily capture intensity, higher-order formants, and voicing, while pitch is encoded in a later dimension. In contrast, the highest-variance speaker dimension is strongly associated with pitch and gender, with later dimensions capturing high-frequency variation. Intervention experiments show that manipulating these dimensions enables targeted control of speech characteristics for speech synthesis. Furthermore, modifying the content and speaker representations jointly provides fine-grained control over characteristics such as pitch and intensity.

</details>

#### [Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization](https://arxiv.org/abs/2606.20218)
**Yudong Li, Zihao Fang, Junwen Qiu, Ruihai Jing et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

Streaming zero-shot voice conversion struggles to disentangle timbre from linguistic content without degrading utility or inflating latency. Current methods rely on information bottleneck (IB) or speaker perturbation. While IB filters out timbre, it discards prosody, forcing models to explicitly inject features like fundamental frequency. This often requires buffering future frames, creating algorithmic lookahead latency. On the other hand, existing perturbation methods largely overlook the crucial trade-off between timbre leakage and utility preservation. Recognizing this neglected trade-off, we find that the inherent objective of Speaker Anonymization (SA) aligns well with balancing these factors. Thus, we introduce SA as a novel perturbation mechanism to explicitly mitigate timbre leakage while retaining prosodic utility. Crucially, SA's robust representations significantly alleviate the generator's reliance on future context, enabling our strictly causal, zero-lookahead network. Audio samples are available at https://amphionteam.github.io/Zero-VC-demo/.

</details>

#### [PhysDrift: Bridging the Embodiment Gap in Humanoid Co-Speech Motion Generation](https://arxiv.org/abs/2606.19935)
**Zhangzhao Liang, Xiaofen Xing, Mingyue Yang, Wenlve Zhou et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

Humanoid robots require co-speech motions that are not only expressive and speech-aligned, but also physically executable under embodiment constraints. Existing co-speech generation pipelines are predominantly human-centric: motions are first generated in human-body representations such as SMPL-X and subsequently retargeted to humanoid robots. In this work, we identify a fundamental embodiment gap in this paradigm, where the mismatch between human motion manifolds and humanoid embodiment constraints disrupts embodiment consistency during motion transfer and physical execution. Through extensive analysis, we show that although retargeting can preserve coarse motion semantics, it significantly compresses motion diversity and weakens prosody-motion synchronization, limiting expressive humanoid behaviors. To address this problem, we first propose IK-EER, a prosody-preserving humanoid motion curation framework that jointly optimizes kinematic feasibility and speech-motion temporal alignment during retargeting. Building upon the curated robot-native motion dataset, we further introduce PhysDrift, an embodiment-aware co-speech motion generation framework that directly predicts executable humanoid joint trajectories from speech without relying on intermediate human-body representations. Unlike conventional human-centric pipelines, PhysDrift maintains embodiment consistency throughout both training and inference while incorporating physical regularization to stabilize robot motion dynamics. Extensive experiments and real-world humanoid deployment demonstrate that embodiment-aware robot-native generation substantially improves speech-motion alignment, physical plausibility, motion smoothness, inference efficiency, and real-time interaction capability.

</details>

#### [FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech](https://arxiv.org/abs/2606.19209)
**Shuoyi Zhou, Yixuan Zhou, Peiji Yang, Yifan Hu et al.** · 2026-06-17

<details>
<summary>Abstract</summary>

Controllable text-to-speech (TTS) has become a key research focus. However, methods based on either reference speech or text descriptions lack flexibility and precise control, and recent joint approaches remain loosely coupled, with speech modeling timbre and text controlling global style. We propose FineCombo-TTS, a unified framework for speech synthesis grounded in reference speech and guided by text descriptions, enabling flexible and precise control over acoustic attributes. Instead of explicit attribute disentanglement, we learn a unified acoustic representation and introduce a Conditional Flow Matching (CFM)-based Speech Variance Predictor to model fine-grained reference-to-target transformations guided by text descriptions. To support relative attribute control, we construct FineEdit, a structured paired dataset that explicitly encodes source-to-target attribute variations. Experiments demonstrate that our approach achieves flexible, precise, and expressive controllable TTS.

</details>

#### [Augmenting Dysarthric Speech Severity Assessment with MOS Supervision](https://arxiv.org/abs/2606.18645)
**Kaimeng Jia, Minzhu Tu, Zengrui Jin, Siyin Wang et al.** · 2026-06-17

<details>
<summary>Abstract</summary>

Dysarthria is a speech disorder marked by reduced intelligibility and communicative effectiveness. Automatic utterance-level assessment of dysarthric speech can support scalable speech monitoring and therapy-related analysis. Yet training such systems is bottlenecked by the scarcity of clinically annotated dysarthric speech. This work proposes to augment dysarthric speech assessment using data from speech synthesis evaluations, specifically human-annotated utterances with Mean Opinion Score (MOS) labels from the QualiSpeech corpus. Experiments show that fine-tuning on speech synthesis assessment data consistently improves performance on both intelligibility and naturalness prediction, while joint training yields gains primarily on naturalness. These results suggest that synthesis artifacts and dysarthric speech share perceptual commonalities, and speech synthesis evaluation corpora offer a practical augmentation source that reduces reliance on scarce clinical annotations.

</details>

#### [Generating Natural and Expressive Robot Gestures through Iterative Reinforcement Learning with Human Feedback using LLMs](https://arxiv.org/abs/2606.18747)
**Chris Lee, Flora Salim, Benjamin Tag, Francisco Cruz** · 2026-06-17

<details>
<summary>Abstract</summary>

Expressive gestures are essential for natural and effective communication, complementing speech when verbal cues alone are insufficient (e.g., pointing). For social robots such as the humanoid Pepper, producing natural and expressive movements is critical for improving human-robot interaction (HRI) and long-term acceptance. However, generating gestures remains challenging due to reliance on expert-authored animations, resulting in rigid behaviors that are impractical for dynamic and diverse environments. Alternatively, machine learning approaches often struggle to capture perceived naturalness, becoming increasingly challenging with more degrees of freedom. Consequently, producing expressive robot gestures requires a system that can adapt to the environment while adhering to social norms and physical constraints. Recent advances in large language models (LLMs) enable dynamic code generation, offering new opportunities for runtime gesture synthesis from natural language. In this paper, we integrate ChatGPT into the humanoid robot Pepper to generate co-speech gestures aligned with conversational output. While this baseline enables flexible gesture generation, the resulting motions are often perceived as stiff and unnatural. To address this limitation, we introduce an iterative reinforcement learning with human feedback (RLHF) system that finetunes gesture generation based on user evaluations, leveraging an iterative user study to compare Pepper's generated gestures. Our results show that RLHF improved the LLM's co-speech generative capabilities, producing more expressive, relevant and fluid movements.

</details>

#### [GRIDEX: Grid-Grounded Forensic Explanations for Deepfake Spectrogram Analysis](https://arxiv.org/abs/2606.18738)
**Thi Ngan Ha Do, Tingmin Wu, Alsharif Abuadbba, Kristen Moore** · 2026-06-17

<details>
<summary>Abstract</summary>

The advancement of speech generation technologies has made artificial speech increasingly realistic. Although modern classification models can achieve high accuracy when it comes to deepfake detection, they do not produce evidences such as indicating where spoof cues appear in the spectrogram and what they imply acoustically, limiting their usefulness in forensic settings. Manual analysis of full spectrograms is resource-intensive, so evidence should narrow attention to the most diagnostic regions. Moreover, existing explainability methods have limited capabilities in connecting contextual attributes to localized evidence, making explanations harder to verify. To overcome this limitation, we propose GRIDEX, a pipeline that, when given a deepfake spectrogram, generates forensic explanations of its anomalies. The pipeline (i) selects top-K anomalous regions in the spectrogram and (ii) produces an explanation for each anomaly. The explanations follow a schema of categorical acoustic fields, including temporal, spectral, phonetic information and interpretation text. To our knowledge, this is the first framework to generate structured forensic explanations using regional grounding for deepfake spectrograms. GRIDEX is trained with a two-stage learning paradigm that combines supervised fine-tuning (SFT) with Group Relative Policy Optimization (GRPO). Experiments on our dataset show improved artifact localization and explanation quality over strong vision-language model (VLM) baselines. The dataset and code will be released upon publication.

</details>

#### [MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data](https://arxiv.org/abs/2606.18485)
**Subhankar Ghosh, Jason Li, Paarth Neekhara, Shehzeen Hussain et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Neural Text-to-Speech (TTS) systems achieve remarkable quality on short utterances but long-form speech generation shows prosodic drift, speaker inconsistencies and sentence boundary artifacts. Existing approaches either compress sequences, increase context length or naively concatenate independently synthesized chunks. We present an inference-time approach called MagpieTTS-LF that enables MagpieTTS to produce coherent long-form speech without model retraining. Our method introduces three key innovations: (1) soft attention priors to guide monotonic alignment while preserving past and future context; (2) a stateful inference algorithm that maintains context across sentence chunks, ensuring prosodic continuity; (3) history-aware text encoding that uses past text for discourse-level prosodic planning. Experiments on long texts show significant improvements in long-range intelligibility, prosodic coherence, speaker consistency, and boundary naturalness compared to other baselines.

</details>

#### [Reliable Neural-Codec Text-to-Speech by ASR Self-Verification and Distillation: Near-Zero Catastrophic Failures Across Models and Codecs](https://arxiv.org/abs/2606.18323)
**Ali Asaria, Tony Salomone, Deep Gandhi** · 2026-06-16

<details>
<summary>Abstract</summary>

Open autoregressive neural-codec text-to-speech (TTS) models sound excellent on typical inputs yet suffer stochastic catastrophic failures: on a meaningful fraction of utterances they emit silence, terminate early, or collapse into repetitive or hallucinated content. We show this failure mode is cheap to remove. Under a single format-robust metric (a catastrophic-failure rate via an ASR round-trip), best-of-N ASR self-verification drives failures to near-zero: no observed failures remain by N=2 on a standard corpus (LibriSpeech) and by N=4 on a hard prompt set. This is not an artifact of one model: the reduction replicates across four open codec-TTS systems and three neural codecs (XCodec2, SNAC, Mimi), reaching the near-zero floor by N=2 on three of the four. We then make the fix free at inference time by distilling the self-verified behaviour into the model, which recovers much of the robustness in single-shot decoding, closing ~52-58% of the failure mass on hard inputs at no test-time cost. The distillation gain concentrates where it is needed (hard inputs); on already-reliable prose there is no headroom and no detectable change. A controlled comparison adds a clean negative: offline direct preference optimization (DPO/IPO) does not beat plain supervised distillation, and an online iterative variant is promising but not statistically separable at our evaluation size. We report honestly the one model that resists (a larger Llasa where scale did not obviously help) and a rare-word capability ceiling that no self-distillation method overcomes

</details>

#### [One-Step Token-to-Waveform Generation with MeanFlow in Latent Space](https://arxiv.org/abs/2606.18072)
**Zheqi Dai, Guangyan Zhang, Zhen Ye, Jingyu Li et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Neural audio codecs are central to modern LLM-based Text-to-Speech (TTS) and multimodal systems. As low-bitrate semantic codecs gain prominence, the Token-to-Waveform (Token2Wav) decoder becomes a bottleneck determining both perceptual quality and system efficiency. Conventional multi-step flow-matching decoders offer superior quality but suffer from high inference latency due to iterative sampling, creating a severe quality-speed trade-off. In this paper, we propose a novel Token2Wav architecture that overcomes this limitation by applying MeanFlow in a highly compressed latent space. By modeling the average velocity rather than the instantaneous velocity field, MeanFlow enables true one-step generation. Operating in the latent domain mitigates the memory and stability issues of waveform-level flows, yielding up to a 17$\times$ improvement in Real-Time Factor (RTF) compared to multi-step baselines with negligible quality degradation. Furthermore, we introduce refinement strategies that mitigate latent mismatch, including decoder-only fine-tuning with the MeanFlow generator frozen and end-to-end joint fine-tuning, improving fidelity without increasing inference-time cost. Code and demo are publicly available.

</details>

#### [Mind Companion: An Embodied Conversational Agent for Process-Based Psychotherapy](https://arxiv.org/abs/2606.17789)
**Sofie Kamber, Lukas Diebold, Pascal Riachi, Stella Brogna et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Access to evidence-based psychotherapy remains limited worldwide, with long waitlists even in high-income regions. Recent advances in large language models (LLMs) offer potential for scalable mental health support when designed with clinical oversight and safety mechanisms. We present Mind Companion, an LLM-based embodied conversational agent integrating multi-layered psychological analysis with process-based therapy principles. The system performs real-time analysis of client statements across fact extraction, psychological flexibility process detection, emotion recognition, and safety monitoring. Analysis results are stored for supervising clinicians to inform therapeutic planning. Response generation incorporates retrieval-augmented generation from evidence-based therapeutic literature and context-aware prompting. Responses are delivered through an embodied avatar with synchronized speech synthesis and animation. We evaluated three LLM configurations (GPT-4.1-mini, GPT-5.2, Claude Sonnet 4.5) against therapist responses from real therapy sessions using automated LLM-judge assessment and expert evaluation with 11 professional psychotherapists. GPT-5.2 achieved higher ratings than human therapist responses across understanding, interpersonal effectiveness, collaboration, and therapeutic alignment in both evaluations, demonstrating the feasibility of LLM-based conversational agents as tools to complement clinical care.

</details>

#### [PhASE-Flow: Phonetic-Conditioned Acoustic Flow Matching in SSL Representation Domain for Speech Enhancement](https://arxiv.org/abs/2606.17806)
**Jun Gao, Xiaobin Rong, Yu Sun, Dahan Wang et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Flow matching (FM) enables high-fidelity generation, while self-supervised learning (SSL) speech models provide hierarchical representations spanning acoustic and phonetic levels. However, existing FM-based speech enhancement (SE) methods operate primarily in the spectral domain, treating SSL features only as external conditions rather than modeling directly in the SSL latent space. To fully exploit the structural richness of SSL representations, we propose PhASE-Flow, an FM-based SE framework that operates entirely in the SSL space. It models the conditional distribution of clean acoustic representations given phonetic ones, reconstructing the waveform via a neural vocoder. Experiments show that PhASE-Flow outperforms state-of-the-art baselines in perceptual quality and intelligibility. Notably, it achieves competitive performance with only four sampling steps, enabling highly efficient inference. Audio demos are available at https://anonymous.4open.science/w/phase-flow_demo-E6E1/.

</details>

#### [Data-Driven Decoding of Russell's Circumplex Model of Affect](https://arxiv.org/abs/2606.16843)
**Amdjed Belaref, Samir Sadok, Zineb Noumir, Renaud Seguier** · 2026-06-15

<details>
<summary>Abstract</summary>

Affective computing increasingly relies on deep learning to represent emotions, yet latent spaces often remain opaque, high-dimensional black boxes. This paper investigates whether Transformers' embeddings recover the geometric regularities of Russell's circumplex model. We unify two complementary experiments testing the hypothesis that, after training models on text and speech, their resulting latent spaces encode a topology consistent with valence-arousal and reproduce human-like neighborhood relations. Specifically, we evaluate deep representations extracted from Transformer-based text (RoBERTa) and speech (wav2vec 2.0) encoders, along with a multimodal Transformer fusion architecture, across naturalistic datasets like MSP-Podcast and controlled LLM-generated stimuli. Our analysis reveals that multimodal fusion of text and audio yields perfect topological alignment with Russell's primary emotion ordering. Furthermore, in a zero-shot setting using generic text embeddings, projected fine-grained emotion terms fall close to their established human-mapped coordinates. Our contribution is a novel, data-driven framework for validating emotion models, demonstrating that Russell's circumplex structure is intrinsically encoded in the embeddings of these modalities rather than being solely an artifact of human labeling, thereby bridging the gap between psychological theory and representation learning.

</details>

#### [CraBERT: Efficient Phoneme Encoder Pre-Training via Cascade Fusion of Subword Representations for Text-to-Speech](https://arxiv.org/abs/2606.16668)
**Dong Yang, Yuki Saito, Wataru Nakata, Hiroshi Saruwatari** · 2026-06-15

<details>
<summary>Abstract</summary>

This paper introduces CraBERT, a pre-trained phoneme encoder (PPEnc) designed for efficient pre-training in text-to-speech (TTS). CraBERT employs a cascade-fusion architecture and a subword-phoneme alignment algorithm to integrate representations from a pre-trained subword-level BERT into a phoneme-level BERT. This design provides prior word- and sentence-level information, reducing the amount of pre-training required by the phoneme encoder. Subjective listening evaluations show that CraBERT achieves MOS values comparable to existing PPEncs after approximately one epoch of pre-training, whereas the baselines in our comparison are pre-trained for approximately ten epochs. These results demonstrate that CraBERT can efficiently learn representations suitable for improving the perceived naturalness and prosody of synthesized speech.

</details>

#### [Joycent: Diffusion-based Accent TTS without Accented Phone Prediction](https://arxiv.org/abs/2606.16417)
**Xintong Wang, Ye Wang** · 2026-06-15

<details>
<summary>Abstract</summary>

Accent text-to-speech (TTS) aims to synthesize speech with target accents. Existing accent TTS systems typically rely on a two-stage pipeline that first converts standard phone sequences into accented phone sequences and then synthesizes accented speech. However, such approaches suffer from error accumulation and require paired standard-accented phone sequence data, which is often limited in practice. Moreover, text-based accented phone representations are insufficient to model acoustic accent characteristics such as prosody and rhythm. In this work, we propose Joycent, a diffusion-based accent TTS model that synthesizes accented speech directly from standard phone sequences and speech references without accented phone prediction. Joycent integrates accent and speaker representations through conditional layer normalization (CLN) in the text encoder. We introduce WhisAID, a Mandarin accent identification model trained on accented Mandarin speech to extract accent representations. Experimental results show that Joycent improves accentedness while preserving speaker identity compared with baseline systems. We release our code and demos at: https://github.com/oshindow/Joycent-code.

</details>

#### [Probing Low Frame Rate Degradation in Neural Audio Codecs](https://arxiv.org/abs/2606.16969)
**Alex Gichamba, Moise Busogi** · 2026-06-15

<details>
<summary>Abstract</summary>

Low frame rates in neural audio codecs are attractive for autoregressive speech synthesis, where the generation cost scales linearly with the sequence length. Recent work has demonstrated that codecs can operate at 12.5 Hz and below, but the mechanisms underlying low frame rate degradation remain insufficiently understood. We investigate these mechanisms through a controlled frame rate ablation. We reproduce a quality cliff at 6.25 Hz reported in previous works and evaluate candidate explanations: phonemic collisions and codebook saturation, neither of which shows evidence of a fundamental barrier. The cliff is instead caused by suboptimal training configuration: fixed clip duration during training yields too few tokens at low frame rates, starving the decoder of inter-token context. Once corrected, WER degrades smoothly with phonemic load down to 3.1 Hz and 1.6 Hz, suggesting the inference-time efficiency gains of low frame rate codecs are more accessible than previously assumed.

</details>

#### [Vibrato Expression Control for Singing Voice Conversion with Improving Independent Control](https://arxiv.org/abs/2606.17126)
**Joon-Seung Choi, Dong-Min Byun, Seong-Whan Lee** · 2026-06-15

<details>
<summary>Abstract</summary>

Singing style is a crucial aspect of a natural and expressive singing voice. Singers utilize singing styles to convey the feeling or emotion of the songs. Several works have been proposed to control singing style for making the more expressive singing voice. Recently, VibE-SVC successfully controls vibrato by predicting high-frequency F0 contour. In this paper, we introduce a singing voice conversion framework, called VibE-SVC2, to improve singing style conversion performance and controllability. The model offers control over two types of singing styles: a pitch style and a timbre style. For the pitch style, to resolve the pitch-energy entanglement issue that is unresolved in our previous work, we introduce a novel Energy Style Converter to address remaining style information in the energy contour. In addition, we propose a Zero-shot Pitch Style Converter, which mimics the pitch style of reference audio. To expand the controllability of the model, we propose vibrato rate scaling that is an independent control of vibrato extent, which is unavailable in VibE-SVC. For the timbre style, we extend the model to handle a variety of phonation styles. However, addressing specific styles such as vocal fry poses a challenge, as conventional F0 extraction often fails due to their inherent subharmonic characteristics, which degrades the conversion quality. To address this, we propose a novel Subharmonic Correction algorithm to refine the F0 contour for more natural timbre conversion. Through comprehensive objective and subjective evaluations, we demonstrate that VibE-SVC2 provides fine-grained, independent control over two types of singing styles, outperforming existing methods.

</details>

#### [Robust Spoofed Speech Detection via Temporal Pyramid Modeling](https://arxiv.org/abs/2606.16837)
**Mahtab Masoudi Nezhad, Nima Karimian** · 2026-06-15

<details>
<summary>Abstract</summary>

Spoofed speech detection is increasingly challenged by realistic synthesis, voice conversion, and replay attacks, with cross-dataset generalization remaining a major limitation. This work we propose a Temporal Pyramid Adapter that utilize parallel temporal convolutions with varying receptive fields to capture multi-scale spoofing cues, ranging from local artifacts to global prosodic irregularities. We also integrated self-supervised XLS-R representations combined with front-end adapters, including Mel, Sinc, and a Temporal Pyramid design for multi-scale temporal modeling. The proposed model is evaluated cross multiple benchmark including ASVspoof 2017, ASVspoof 2021 (DF/LA), PartialSpoof, DiffSSD, and multilingual HQ-MPSD datasets. Experimental results demonstrate that Temporal Pyramid model obtained AUC of 99.24% and a EER of 3.87% on the PartialSpoof database, which is significantly outperforming the base model and several SOTA baseline such as LCNN-BLSTM (9.87% EER) and TRACE (8.08% EER). Additionally, multilingual evaluations confirm that while spoofing artifact are independent from language. While self-supervised representations improve robustness, performance degrades under domain and language shifts, highlighting the need for better adaptation and calibration strategies.

</details>

#### [Mask, Sample, Revise: A Revisable CTMC Inference Stack for Guided Discrete Flow Matching Text-to-Speech](https://arxiv.org/abs/2606.13989)
**Alef Iury Siqueira Ferreira, Lucas Rafael Stefanel Gris, Luiz Fernando de Araújo Vidal, Frederico Santos de Oliveira et al.** · 2026-06-12

<details>
<summary>Abstract</summary>

Recent alignment-free non-autoregressive (NAR) text-to-speech (TTS) models formulate synthesis as a conditional infilling task, bypassing explicit duration predictors and external aligners. When speech is represented with neural codec tokens, the infilling problem becomes discrete, making Discrete Flow Matching (DFM), a Continuous-Time Markov Chain (CTMC) framework for discrete generation, a natural fit. However, inference-time control for stable low-step conditional infilling remains underexplored. We propose Mask, Sample, Revise, an inference-time CTMC stack for alignment-free DFM-TTS. The stack combines predictor-free guidance to strengthen text conditioning, prompt-matched conditional coupling to align the probability path with the acoustic prompt, and SC-ReMask, a schedule-constrained remasking mechanism that introduces token-to-mask transitions so early de-masking decisions can be revised. These components require no post-hoc fine-tuning and operate in a single tau-leaping sampler. Controlled ablations show that this stack improves intelligibility and robustness in the low-NFE prompted setting, outperforming unguided and guidance-only samplers with substantially more steps.

</details>

#### [Unsupervised Approaches for Global Prosodic Embedding Extraction](https://arxiv.org/abs/2606.14004)
**Martin Meza, Luciana Ferrer, Pablo Riera** · 2026-06-12

<details>
<summary>Abstract</summary>

Prosody is central to oral communication, conveying information like the emotional state of the speaker and cues needed for meaning disambiguation. Many self-supervised models of speech produce embeddings that encode prosodic as well as linguistic, and speaker information. This entanglement of information is problematic in scenarios where prosody is the main distinguishing factor while other factors may vary between training and deployment; in such cases, a purely prosodic representation would be more robust. Such representation could also be used for analyzing the role of prosody in a given task or as input to speech synthesis systems. In this work, we propose a variety of approaches for producing global prosodic embeddings based on auto-encoder models of pitch and energy. We develop a benchmark for assessing the performance of these representations, showing that our embeddings provide competitive or superior performance under challenging conditions, compared to various alternatives.

</details>

#### [From Self-Supervised Speech Models to Mixture-of-Experts for Robust Anti-Spoofing](https://arxiv.org/abs/2606.14639)
**Hugo Daumain, Driss Matrouf, Khaled Khelif, Mickael Rouvier** · 2026-06-12

<details>
<summary>Abstract</summary>

Recent advances in speech generation have significantly improved the naturalness of synthetic speech, making spoofing detection increasingly challenging. A key limitation of current anti-spoofing systems is their limited robustness to unseen synthesis methods. In this work, we transform a self-supervised speech representation model into a Mixture-of-Experts (MoE) architecture to improve generalization. Feed-forward blocks in selected encoder layers are replaced by multiple expert networks controlled by a layer-wise gating mechanism, allowing experts to capture complementary acoustic patterns while preserving the representations learned during self-supervised pretraining. We further analyze the architectural choices affecting the performance of this MoE conversion and investigate the activation behavior of the experts. The proposed approach is evaluated on 14 spoofing datasets and reduces the macro EER from 5.46% to 4.81%, corresponding to 11.9% relative improvement over the baseline.

</details>

#### [From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation](https://arxiv.org/abs/2606.13630)
**Pedro Correa, Olivier Perrotin, Samir Sadok, Paula Costa et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

The choice of speech representation is critical in speech-driven 3D facial animation. Representations differ in what they encode: SSL features emphasize segmental and semantic cues, neural codecs yield latents optimized for acoustic reconstruction, and ASR-style objectives produce label-based spaces. We evaluate four speech representation families for 3D facial synthesis, comparing their facial reconstruction quality across two facial decoders using objective metrics and a perceptual evaluation. We additionally conduct probing analyses that relate tokenized representations to phonetic units and to articulatory deformations. We found that encoding phonetic classes is beneficial for accurate facial animation prediction on both semantic and label-based representations with comparable facial animation quality. From the latter, we introduce an Audio Visual Text-to-Speech (AVTTS) pipeline that leverages, as a shared space, discrete representations to decode speech and 3D facial motion.

</details>

#### [TimeLens: On-Device Artifact Recognition with Retrieval-Augmented Question Answering for the Grand Egyptian Museum](https://arxiv.org/abs/2606.13267)
**Rawan Hesham, Ali Ashraf, Amr Ahmed, Malak Alaa et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

TimeLens is an AI-powered bilingual mobile guide for the Grand Egyptian Museum (GEM). Pointing a phone at an exhibit, a visitor sees the artifact recognized in real time and can ask follow-up questions answered in English or Arabic. The work addresses three problems specific to in-gallery deployment: fine-grained visual similarity among 51 catalogued artifacts (many near-identical Ramesside statues), the gap between curated training data and handheld camera conditions, and the risk of an AI guide stating unsupported historical facts. Two engineering contributions are reported. First, an on-device artifact detector was developed through a data-quality-driven iteration study -- from foundation-model auto-annotation (YOLO-World), through spatial label-cleaning rules, to a fully hand-annotated dataset -- isolating label quality as the decisive factor: the final YOLOv8n model resolves every previously failing class while remaining a 5.97 MB TensorFlow Lite asset that runs in real time on a mid-range phone (mAP@0.5 = 0.995, mAP@0.5:0.95 = 0.924). Second, a bilingual Retrieval-Augmented Generation (RAG) guide, grounded in a 108-record ChromaDB knowledge base, was benchmarked across seven candidate language models, with Gemma 4 E2B (Q4 K M) selected; ten targeted optimizations reduce end-to-end latency from over 30 s to approximately 10 s. Both subsystems are integrated in a production Flutter application with bilingual interface, museum location gating, and text-to-speech support.

</details>

#### [Emo-LiPO: Listwise Preference Optimization for Fine-Grained Emotion Intensity Control in LLM-based Text-to-Speech](https://arxiv.org/abs/2606.13006)
**Yihang Lin, Li Zhou, Congwei Cao, Dongchu Xie et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

Large language model (LLM)-based text-to-speech (TTS) systems enable prompt-conditioned emotional control but struggle with fine-grained emotion intensity due to the semantic -- acoustic gap between text and speech. To address this challenge, we formulate emotion intensity control in LLM-based TTS as a learning-to-rank problem and propose Emo-LiPO, a listwise preference optimization framework that aligns prompt-conditioned speech generation with relative emotion intensity expressed in text. Emo-LiPO explicitly models global intensity ordering within each emotion under fixed transcripts, enabling more faithful and continuous emotional expression. We further construct ESD-plus, a multi-speaker dataset with explicit emotion intensity variations, to support fine-grained emotion modeling and evaluation. Experiments on ESD-plus demonstrate that Emo-LiPO significantly improves emotion accuracy and intensity controllability over both supervised- and DPO-based LLM TTS baselines, with particularly pronounced gains at high intensity levels.

</details>

#### [PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue](https://arxiv.org/abs/2606.12902)
**Wen Zhang, Xiaocui Yang, Zhuoyue Gao, Shi Feng et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

Empathetic spoken dialogue systems require not only semantically appropriate responses but also emotionally aligned prosodic expression. However, cascade pipelines often discard acoustic cues during speech-to-text conversion, while end-to-end speech models lack interpretable control over emotion and knowledge integration. To address these challenges, we propose PRISM, a multi-agent framework for empathetic spoken dialogue that decouples speech perception, response generation, and speech synthesis into coordinated components. PRISM introduces a prosody-to-language translation mechanism to stabilize large language model reasoning and enables on-demand invocation of external knowledge tools for empathetic dialogue generation. Experimental results demonstrate that PRISM achieves consistent improvements in empathy, prosodic appropriateness, and text response generation quality across objective and subjective metrics. Our code is available at: https://github.com/Bxzfrm/PRISM.

</details>

#### [Vocal Identity Under Siege by AI Voice Cloning Technologies](https://arxiv.org/abs/2606.12812)
**Jyh-An Lee, Xuan Sun** · 2026-06-11

<details>
<summary>Abstract</summary>

The advent of sophisticated AI-driven voice cloning has brought to the fore critical legal and ethical challenges regarding the protection of vocal identity. Prompted by recent controversies - including the striking resemblance between OpenAI's ChatGPT-4o voice and that of Scarlett Johansson - this article examines how generative AI technologies undermine the unique value of the human voice and further complicate the legal questions surrounding personality right. Through a comparative analysis, the paper evaluates three principal legal frameworks: the right of publicity, personality rights, and the personal data protection right. Each framework - rooted in different legal traditions o offers distinct strengths and limitations in addressing the threats posed by AI-generated voice cloning. By analysing these doctrines' scope, remedies, and posthumous protections, the study offers a foundation for understanding how existing legal approaches may be applied to the evolving challenges of vocal identity in the era of generative AI.

</details>

#### [M*: A Modular, Extensible, Serving System for Multimodal Models](https://arxiv.org/abs/2606.12688)
**Atindra Jha, Naomi Sagan, Keisuke Kamahori, Irmak Sivgin et al.** · 2026-06-10

<details>
<summary>Abstract</summary>

We are entering a new era of composite model architectures that integrate diverse components such as vision encoders, language backbones, diffusion and flow heads, audio codecs, action generators, and world-model predictors. Such architectures underpin a broad class of multimodal models, including unified multimodal models, omni models, speech-language models, vision-language-action policies, and world models. However, existing model serving frameworks were built on narrow assumptions about model structure, making them ill-suited to accommodate this new architectural diversity. Here we present M*, a universal serving system for efficient serving of composite AI models. M* represents models as dataflow graphs, processing requests spanning diverse modalities and tasks as traversals over these graphs. The core insight is a modular abstraction that supports arbitrary composition of model components, flexible placement onto a physical cluster, and model-agnostic optimizations within a distributed runtime. We call this abstraction the Walk Graph and show how it can concisely capture composite models from a broad range of families. We instantiate M* on representative models and find that it achieves, on average, 20% lower end-to-end latency than vLLM-Omni for text-to-image workloads on BAGEL, while delivering up to 2.9x lower real-time factor and 2.7x higher throughput for text-to-speech workloads on Qwen3-Omni. M* also outperforms the V-JEPA 2-AC rollout baseline for robotic planning by up to 12.5x. Thus, our work paves the road towards more efficient serving of complex models with minimal developer effort.

</details>

#### [UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction](https://arxiv.org/abs/2606.11681)
**Sangmin Lee, Eekgyun Ahn, Woongjib Choi, Hong-Goo Kang** · 2026-06-10

<details>
<summary>Abstract</summary>

We propose UR-BERT, a Romanized transcription-based text-to-speech (TTS) encoder for massively multilingual TTS systems. Conventional grapheme-to-phoneme (G2P)-based approaches are limited to around 100 languages due to the availability of reliable G2P resources. In contrast, UR-BERT scales to 495 languages by unifying diverse writing systems into a shared Romanization representation. To further enhance phonetic fidelity and text-speech alignment, we introduce a speech token prediction objective during training, which encourages the encoder to learn speech-aware phonetic representations in a data-efficient manner. Experiments show that TTS systems built on UR-BERT consistently outperform recent text encoder baselines across a wide range of languages and resource conditions, and demonstrate strong generalization to unseen languages.

</details>

#### [SARA: A Dual-Stream VAE for High-Fidelity Speech Generation via Integrating Semantic and Acoustic Representations](https://arxiv.org/abs/2606.11611)
**Peijie Chen, Wenhao Guan, Weijie Wu, Kaidi Wang et al.** · 2026-06-10

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) relies on robust speech representations. However, current speech tokenizers face a fundamental trade-off: acoustic codecs preserve high-fidelity audio but lack linguistic constraints, causing content errors during generation, whereas semantic tokens from self-supervised learning (SSL) models ensure precise text alignment but discard some acoustic information. To bridge this gap, we propose SARA, a dual-stream VAE that directly fuses a frozen SSL semantic anchor with a dedicated residual acoustic encoder. This effectively mitigates the dilemma, creating an efficient and compact latent space without relying on complex regularizers. SARA achieves superior reconstruction quality over strong baselines. Furthermore, in downstream zero-shot TTS tasks, it yields highly natural and expressive synthesis quality, and maintains robust generation performance even under accelerated inference, offering a favorable trade-off between synthesis speed and computational cost.

</details>

#### [Anchoring the Unknown: Open-Set Model Attribution via Proxy-Anchor Learning](https://arxiv.org/abs/2606.10758)
**Cristian-Teodor Neamtu, Serban Mihalache, Stefan Smeu, Dan Oneata et al.** · 2026-06-09

<details>
<summary>Abstract</summary>

The proliferation of text-to-speech (TTS) systems capable of generating realistic synthetic speech poses growing challenges for audio forensics. While binary deepfake detection has received considerable attention, source tracing (i.e., identifying which TTS system produced a given audio sample) remains underexplored, particularly in open-set scenarios where unknown systems may be encountered. We propose a metric learning framework based on the Proxy-Anchor loss function that operates on Wav2Vec2-BERT embeddings to learn a discriminative embedding space for TTS source attribution and out-of-distribution (OOD) detection of unseen systems. We evaluate it on the MLAAD v9 dataset spanning 140 TTS systems across 51 languages, and introduce an architecture merging strategy that groups TTS system versions into unified classes, reducing inter-class confusion. Our system achieves 99.76% accuracy on 110 in-distribution classes and a False Positive Rate (FPR@95) as low as 2.04% for OOD detection. Also, for a fair comparison against the current state of the art, we further evaluate it on the MLAAD v5 official dataset splits, improving the OOD accuracy by almost doubling it. These results demonstrate that Proxy-Anchor metric learning, combined with architecture-aware class design and post-hoc OOD scoring, provides an effective framework for forensic TTS source tracing in both closed-set and open-set settings.

</details>

#### [SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space](https://arxiv.org/abs/2606.10317)
**Tomoya Tanabu, Hiroshi Nishijima, Daisuke Saito, Nobuaki Minematsu** · 2026-06-09

<details>
<summary>Abstract</summary>

We introduce SSL-GMMVC, an interpretable voice conversion method in self-supervised speech space. The method models paired source-target features with a Gaussian mixture model and performs conversion as a posterior-weighted sum of affine transforms. This yields locally linear transformations that adapt to heterogeneous feature-space structure while remaining analytically tractable. Through objective and subjective evaluations, we show that SSL-GMMVC improves speaker similarity with comparable intelligibility and naturalness, and that even a constrained covariance variant surpasses a deep learning baseline as the number of mixture components increases. Further analyses link component selection to phonetic structure and reveal interpretable scaling and rotation in the learned transforms. These findings highlight SSL-GMMVC as an effective, analyzable framework for voice conversion.

</details>

#### [Interpreting and Steering a Text-to-Speech Language Model with Sparse Autoencoders](https://arxiv.org/abs/2606.10029)
**Nikita Koriagin, Georgii Aparin, Nikita Balagansky, Daniil Gavrilov** · 2026-06-08

<details>
<summary>Abstract</summary>

Language models increasingly serve as the backbone of text-to-speech (TTS) systems, yet we understand little about the representations they build when text and generated speech tokens share a single residual stream. We train BatchTopK sparse autoencoders on the LM backbone of CosyVoice3 and introduce a modality-aware auto-interp pipeline that labels each feature from where it fires-text-prefix context, 1-second speech clips, or both. The recovered features are interpretable, spanning phonemes, laughter, accent prompts and speaker gender. Steering through the SAE latent space shows these features are causal rather than merely descriptive: targeted interventions raise laughter probability from 0.02 to 0.79, flip perceived speaker gender, and control speech rate while preserving spoken content. SAE features thus serve both as interpretability objects and as control directions for TTS synthesis.

</details>

#### [What Makes Synthetic Speech Sound Sarcastic? A Prosody-Controlled Perception Study](https://arxiv.org/abs/2606.09717)
**Zhu Li, Shekhar Nayak, Matt Coler** · 2026-06-08

<details>
<summary>Abstract</summary>

Prosody plays a central role in sarcasm perception, yet previous studies have relied on naturally produced speech that lacks fine-grained control over individual acoustic dimensions. As prosodic cues co-vary in natural data, isolating their independent contributions remains challenging. We introduce a controlled framework using neural text-to-speech (TTS) with prompt-based prosodic conditioning to manipulate speech rate, pitch variation, and loudness. An orthogonal stimulus set was constructed to enable causal testing of prosodic cue effects. Human listeners rated sarcasm and naturalness, and their judgments were compared with predictions from a foundation model capable of processing audio input. Results show that loudness primarily drives human sarcasm perception, whereas the model assigns greater weight to speech rate, leading to distinct cue-weighting patterns. This study shows how controllable neural TTS enables investigation of prosodic cue weighting in speech perception.

</details>

#### [Optimality of FSQ Tokens for Continuous Diffusion for Categorical Data with Application to Text-to-Speech](https://arxiv.org/abs/2606.09962)
**Vadim Popov, Wenju Gu, Tasnima Sadekova, Georgii Aparin et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Continuous diffusion for categorical data is a framework belonging to the diffusion family and aiming at generating discrete data. The scientific interest to such models has been constantly increasing these days because researchers try to achieve a challenging goal of finding reasonable alternatives to autoregressive large language models. In this paper, we study the properties of the structure of the latent space corresponding to discrete tokens expressed in terms of Kullback-Leibler divergence on diffusion path measures and accuracy of the correct token prediction by the optimally trained diffusion model. We find that FSQ tokenization scheme has the latent space structure with the properties that make it best suited for continuous diffusion for categorical data as verified through rigorous theoretical analysis and numerical experiments. To validate our findings in real-life scenario, we train several text-to-speech diffusion models having speech tokens as intermediate acoustic features, and show that the one based on FSQ tokens indeed performs the best, and, moreover, it outperforms its strong LLM-based counterpart, at the same time being significantly smaller and faster.

</details>

#### [OpenBibleTTS: Large-Scale Speech Resources and TTS Models for Low-Resource Languages](https://arxiv.org/abs/2606.09553)
**David Guzmán, Luel Hagos Beyene, Jesujoba Oluwadara Alabi, Yejin Jeon et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Recent advances in neural text-to-speech (TTS) and multilingual speech generation have substantially improved synthetic speech quality, yet these gains remain unevenly distributed across the world's languages. Existing models are still dominated by a small set of high-resource languages, while many studies of low-resource TTS are simulated on artificially downsampled high-resource corpora that do not reflect the orthographic variation and limited phonetic coverage encountered in genuinely underrepresented settings. As such, we introduce OpenBibleTTS, which is a large-scale benchmark for low-resource speech synthesis spanning 37 underrepresented languages. Moreover, a systematic comparison of various TTS architectures and large-scale speech generation models is conducted across in-domain Biblical text and out-of-domain material. Results show that no single system dominates across languages and metrics: Gemini-TTS achieves the highest listener ratings on most evaluated languages, but monolingual EveryVoice models trained on OpenBibleTTS remain strongest for intelligibility and are preferred in several African languages, while open from-scratch systems degrade sharply on out-of-domain text, revealing a persistent gap between broad multilingual coverage and reliable synthesis quality in underserved linguistic communities. We complement automatic evaluation with subjective human judgments, and open-source all processed datasets, alignments, and trained models to support future low-resource TTS research.

</details>

#### [NüshuVoice: Reviving the Voice of Endangered Nüshu with Pitch-Aware Text-to-Speech](https://arxiv.org/abs/2606.09295)
**Hongkun Yang, Xinhui Yi, Xiyan Zhao, Yibo Meng et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Nüshu is an endangered phonetic script historically used by women in Jiangyong County, southern Hunan, China. While existing computational studies of Nüshu mainly focus on textual digitization and visual recognition, the acoustic reconstruction of its authentic pronunciation remains largely unexplored. Building a Nüshu text-to-speech (TTS) system is particularly challenging because available recordings are extremely limited and mostly consist of isolated syllable-level pronunciations rather than natural sentence-level utterances. In this work, we introduce NüshuVoice, the first TTS benchmark for Nüshu. We construct a sentence-level Nüshu text-to-audio dataset that aligns standardized Unicode Nüshu text, phonetic transcriptions, standard Chinese translations, and archival recordings. To synthesize speech under this extreme low-resource setting, we propose Nüshu-PitchVITS, an F0-conditioned VITS framework that leverages Nüshu's five-level pitch notation as an explicit prosodic inductive bias. Experimental results show that Nüshu-PitchVITS outperforms strong TTS baselines in spectral fidelity, pitch reconstruction, and human-rated intelligibility. We publicly release the dataset and code at: https://anonymous.4open.science/r/Nvshu-TTS-2EB6.

</details>

#### [End-to-End Training for Discrete Token LLM based TTS System](https://arxiv.org/abs/2606.09234)
**Changfeng Gao, Yong Ren, Jun Yuan, Ye Bai et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Recent state-of-the-art (SOTA) text-to-speech (TTS) systems typically adopt a cascaded pipeline consisting of a speech tokenizer, an autoregressive large language model (LLM), and a diffusion based flow-matching (FM) model, with these components trained independently. In this paper, we propose a fully end-to-end (E2E) optimization framework that unifies the training of the speech tokenizer, LLM, FM model, and an additional reward model (RM). Specifically, we first jointly optimize the tokenizer using multi-task objectives derived from reconstruction for FM, next-token prediction for LLM, and multi recognition task for RM. This joint training encourages the discrete speech token space to capture acoustically and semantically salient information that is better tailored to TTS. We then further optimize the LLM using downstream reconstruction and recognition by FM and RM, which reduces inference-time mismatch and steers the LLM toward more preferred generations. Experimental results show that our E2E framework consistently outperforms cascaded baselines. On the Seed-TTS-Eval benchmark, our system achieves a word error rate (WER) of 0.78% and 1.56%, a new SOTA result with a 0.6B-parameter LLM and 0.5B-parameter FM model. These results validate that holistic E2E optimization is critical for improving discrete-token-based TTS systems with a much simpler training pipeline.

</details>

#### [DuplexOmni: Real-Time Listening, Seeing, Thinking, and Speaking for Full-Duplex Interaction](https://arxiv.org/abs/2606.09186)
**Muye Huang, Lingling Zhang, Xingyu Yu, Lei Shi et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Human interaction is continuous, multimodal, and full-duplex by nature. Although recent omni models have made substantial progress in unified speech, vision, and text modeling, combining seamless real-time interaction with complex reasoning and tool use remains challenging. We present DuplexOmni, a method for real-time multimodal full-duplex interaction. DuplexOmni separates model capability into an interaction layer and a thinking layer, which collaborate asynchronously in parallel. The interaction layer is implemented by the DuplexOmni model, an end-to-end system that processes streaming audio and video inputs while generating text and speech responses in real time. The thinking layer is a pluggable module that provides complex reasoning and tool-use capabilities. To support this method, we further develop a Writer-Director pipeline for constructing continuous-interaction training data. Experiments show that DuplexOmni achieves strong performance on multiple public benchmarks and exhibits natural full-duplex interaction ability.

</details>

#### [FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation](https://arxiv.org/abs/2606.09141)
**Hanke Xie, Xiaming Ren, Dake Guo, Ruonan You et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Recent progress in speech dialogue systems requires Text-to-Speech (TTS) models to be faster and more responsive. Modern speech dialogue systems impose two primary requirements on TTS models: low latency and support for streaming inputs and outputs. However, most existing single-codebook LLM-based TTS methods rely on multi-stage pipelines that lack native streaming capabilities. These systems typically suffer from high end-to-end latency due to slow autoregressive prediction and multi-step flow matching. To address these limitations, we propose FlashTTS, an open-source and low-latency streaming TTS framework. FlashTTS introduces a lagged multi-track architecture that natively processes streaming text and speech inputs, thereby eliminating the need for sentence-level buffering. To accelerate acoustic generation, we integrate parallel Multi-Token Prediction (MTP) with an X-pred mean flow matching decoder. This configuration achieves high-fidelity token-to-mel generation in exactly two function evaluations (2-NFE). By jointly optimizing input processing and decoding efficiency, FlashTTS offers a practical foundation for real-time speech dialogue systems. Experiments show that FlashTTS substantially reduces First-Packet Latency to 325ms compared to robust streaming baselines, all while preserving strong zero-shot voice cloning and cross-lingual intelligibility. Speech samples are available. The model code and checkpoints will be released as open source.

</details>

#### [HoliDubber: Holistic Video Dubbing for Complex Acoustic Scenes via Text-Guided Audio Synthesis](https://arxiv.org/abs/2606.09098)
**Wenhao Guan, Yifan Duan, Junxi Liu, Yu Gu et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Video dubbing is a cornerstone of multimedia content creation, aiming to synthesize synchronized acoustic sequences for visual streams. While Text-to-Speech (TTS) and Text-to-Audio (TTA) generation have each achieved remarkable progress, existing dubbing systems remain confined to isolated speech synthesis without incorporating sound effects and ambient audio, forcing practitioners to rely on fragmented workflows and laborious manual post-mixing. To address this limitation, we present HoliDubber, a holistic video dubbing framework that moves beyond speech-only generation by enabling the joint synthesis of speech and sound effects from a single text prompt. Specifically, HoliDubber adopts a patch-based autoregressive diffusion transformer architecture, where a causal language model autoregressively models aggregated patch embeddings to capture global temporal structure, and a Diffusion Transformer decoder generates high-fidelity continuous tokens within each patch, following a divide-and-conquer strategy. To achieve cross-modal alignment, visual features are encoded into patch-level representations and fused with audio patches via cross-attention, enabling the model to ground speech generation in the speaker's visual articulation dynamics. In addition, we introduce HoliDub-Bench, a benchmark curated from established datasets with synchronized video-text-audio triplets designed for holistic dubbing evaluation. Extensive experiments demonstrate that HoliDubber significantly outperforms existing methods across multiple benchmarks in speech quality, synchronization, and speaker similarity. Furthermore, results on HoliDub-Bench validate the effectiveness of joint speech-and-sound generation, establishing a new paradigm for holistic video dubbing in complex acoustic scenes. \footnote{The demo page of the project is https://holidubber.github.io}

</details>

#### [BareWave: Waveform-Native Flow-Matching Text-to-Speech](https://arxiv.org/abs/2606.09048)
**Wei Fan, Chao-Hong Tan, Qian Chen, Wen Wang et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Removing intermediate representations and separately trained decoding stages has become an important direction in generative modeling. In text-to-speech, however, high-quality systems are still commonly built through an intermediate acoustic representation before waveform synthesis. In this work, we present BareWave, a fully waveform-native framework for direct text-to-wave generation in flow-matching TTS. We consider this setting to raise three training challenges: raw-waveform modeling lacks a strong pretrained representational scaffold, different stages of training benefit from different noise schedules, and data-space perceptual objectives do not automatically share the temporal structure of the velocity-space flow objective. As a result, direct waveform training is hard to optimize efficiently, hard to push toward a strong final operating point with a fixed recipe, and hard to integrate effective perceptual refinement. Guided by this view, we develop a direct text-to-wave training framework that combines training-time representation alignment, staged noise scheduling, and velocity-aware perceptual alignment (VAPA), while preserving a single waveform-native inference path without pretrained components at test time. Experiments on zero-shot voice cloning show that strong intelligibility, speaker similarity, and naturalness can be achieved under a fully waveform-native inference path, supporting waveform-native flow-matching TTS as a practical direction. Project page with audio demos is available at https://barewave.github.io/.

</details>

#### [TLDR: Compressing Audio Tokens for Efficient Autoregressive Text-to-Speech](https://arxiv.org/abs/2606.09019)
**Yejin Lee, Junwon Moon, Hyoeun Kim, Hyunjin Choi et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Codec-based autoregressive (AR) speech language models have achieved strong text-to-speech (TTS) quality by modeling speech as sequences of discrete audio tokens with large pretrained backbones. However, this token-level formulation creates a structural efficiency bottleneck: speech-token sequences are much longer than text sequences, requiring the AR backbone to perform causal computation at every token position and maintain a KV cache that grows with the sequence length. We introduce TLDR, a patch-based autoregressive framework that accelerates codec-based AR-TTS by shifting the causal modeling from token-level speech sequences to patch-level sequences. TLDR groups consecutive codec tokens into compact latent patches using a lightweight compressor, models the resulting shorter patch sequence with a frozen pretrained AR-TTS backbone adapted by LoRA, and reconstructs fine-grained speech tokens within each patch using a speaker-conditioned extractor. With a patch size of 4, TLDR achieves a 1.8x inference speedup over the baseline AR-TTS model and reduces global KV-cache memory by up to 75%. Experimental results indicate that patch-level global causal modeling can be a practical way to reduce the inference cost of pretrained codec-based AR-TTS systems without replacing the existing modules.

</details>

#### [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](https://arxiv.org/abs/2606.09667)
**Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.

</details>

#### [MeanVC 2: Robust Low-Latency Streaming Zero-Shot Voice Conversion](https://arxiv.org/abs/2606.09050)
**Guobin Ma, Yuxuan Xia, Yuepeng Jiang, Dake Guo et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Streaming zero-shot voice conversion (VC) has become increasingly popular due to its potential for real-time applications. The recently proposed MeanVC achieves lightweight streaming zero-shot VC, but it has several limitations: its chunk-wise autoregressive denoising doubles the effective training sequence length, conversion quality degrades under small-chunk settings, and its timbre encoder directly relies on reference mel-spectrograms, making it sensitive to reference audio quality. To address these limitations we propose MeanVC 2. We introduce future-receptive chunking (FRC), which explicitly schedules past and future receptive fields across diffusion transformer decoder layers and removes clean-chunk teacher forcing. By incorporating bounded future context, FRC enables stable conversion with a 40 ms chunk size. We further introduce a universal timbre token encoder, which constructs a timbre representation from a global speaker embedding and retrieves fine-grained timbre cues via cross-attention, improving robustness to low-quality references and enhancing zero-shot speaker similarity. Experimental results show that MeanVC 2 significantly outperforms MeanVC, while reducing latency from 211 ms to 110 ms. Audio samples are publicly available. The source code will be publicly released.

</details>

#### [Audio-Oscar: A Multi-Agent System for Complex Audio Scene Generation, Orchestration, and Refinement](https://arxiv.org/abs/2606.07397)
**Yifan Duan, Qixiang Xu, Hengtao Wu, Zhanxun Liu et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

In recent years, audio generation has made significant progress in tasks such as text-to-speech (TTS), text-to-audio (TTA) and text-to-music (TTM). However, generating long-form and controllable audio from complex audio scene descriptions remains a significant challenge, as such scenes often require coordinated speech, sound effects, music, songs, temporal structure, and post-production. In this work, we introduce \textbf{Audio-Oscar}, a multi-agent framework for generating audio from complex descriptions. Audio-Oscar coordinates a set of specialist agents, each responsible for a different aspect of the audio scene, including character modeling and voice design, speech generation, fine-grained timeline planning, model selection, non-speech generation, and audio post-production. Audio-Oscar further incorporates feedback-driven refinement. In addition, to address the lack of suitable benchmarks for evaluating audio generation from complex audio scene descriptions, we construct \textbf{ASG-Bench}, an Audio Scene Generation Benchmark containing both scene descriptions paired with reference audio and text-only scene descriptions. Each scene is annotated with target audio events and temporal statements to evaluate whether the generated audio faithfully realizes the required scene content and temporal structure. Experimental results show that Audio-Oscar can effectively generate audio that matches complex scene descriptions. Project samples are available at https://audiooscar.github.io/. Our code is available at https://github.com/ziye26/Audio-Oscar.

</details>

#### [KIT's Submission to Cross-Lingual Voice Cloning in IWSLT 2026](https://arxiv.org/abs/2606.07240)
**Seymanur Akti, Alexander Waibel** · 2026-06-05

<details>
<summary>Abstract</summary>

Cross-lingual voice cloning aims to generate speech in a target language while preserving speaker identity from a source-language reference. This task is central to speech translation and is the focus of the IWSLT 2026 Cross-Lingual Voice Cloning track. A key challenge is maintaining intelligibility and naturalness in the presence of accent variation and domain-specific vocabulary. We build on a multilingual text-to-speech model, FishAudio-S2-Pro, and introduce language tag prompting to improve language control and reduce accent leakage. We further apply reinforcement learning (RL) fine-tuning for task adaptation and observe improvements in intelligibility. Finally, we propose a reference-conditioned lexical matching method that improves pronunciation of domain-specific terms when lexical overlap is present. Results show that language prompting provides the largest gains, while lexical matching yields consistent improvements on matched subsets.

</details>

#### [dots.tts Technical Report](https://arxiv.org/abs/2606.07080)
**Shi Lian, Changtao Li, Bohan Li, Hankun Wang et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

We present dots.tts, a 2B-parameter continuous autoregressive text-to-speech (TTS) foundation model that models speech in a continuous latent space. Compared with existing continuous autoregressive models, our key innovations are threefold. First, we train an AudioVAE with multiple objectives to build a semantically structured and prediction-friendly continuous speech space. Second, we use full-history conditioning in the flow-matching head to preserve long-range consistency and reduce drift during generation. Third, we apply reward-free self-corrective post-training to the flow-matching head to further improve robustness and acoustic quality. After being trained on a large-scale multilingual corpus, dots.tts achieves the best average performance on Seed-TTS-Eval, with WERs of 0.94%/1.30%/6.60% and SIM scores of 81.0/77.1/79.5 on the zh/en/zh-hard test sets, respectively. Across other benchmarks, dots.tts also consistently demonstrates open-source state-of-the-art performance, exhibiting strong generation stability, voice cloning ability, and emotional expressiveness. For efficient inference, we further apply CFG-aware MeanFlow distillation, enabling low-latency speech generation with first-packet latencies of 85/54 ms in output streaming and dual-streaming modes, respectively. To facilitate reproducible research and practical deployment, we release the training and inference code, together with the pretrained, post-trained, and MeanFlow-distilled checkpoints, under the Apache 2.0 license.

</details>

#### [Leveraging Soft Distributions of SSL-Derived Discrete Speech Tokens for Downstream Inference](https://arxiv.org/abs/2606.06806)
**Kentaro Onda, Satoru Fukayama, Daisuke Saito, Nobuaki Minematsu** · 2026-06-05

<details>
<summary>Abstract</summary>

Discrete speech tokens obtained from self-supervised learning (SSL) models provide efficient data compression while maintaining strong performance, and have been widely used as intermediate representations in various tasks. However, discretization inevitably causes information loss, leading to degraded performance compared with continuous SSL features. In this work, we propose to apply soft token assignment only during downstream inference. This approach preserves the efficiency of hard discretization during training while enhancing the expressiveness of the tokens at inference. The proposed method outperforms conventional hard assignment on both ASR and speech synthesis tasks, and exhibits particularly strong generalizability to out-of-domain data. For ASR of non-native speech, it even surpasses models using continuous SSL features. Moreover, analysis of the resulting representations shows they align more accurately with phonemes compared with conventional hard assignment.

</details>

#### [Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation](https://arxiv.org/abs/2606.07015)
**Ziyu Zhang, Chunyu Qiang, Xiaopeng Wang, Yuxin Guo et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

While song generation and singing voice conversion (SVC) have evolved significantly, they have long been developed isolated: the former lacks zero-shot speaker cloning, while the latter overlooks vocal-accompaniment synergy. To bridge this gap, we propose UniSinger, the first end-to-end framework unifying speaker cloning song generation and accompaniment co-generation SVC. Building on the multimodal diffusion transformer, we construct a unified speaker embedding space transferring speaker representation from SVC to song generation, endowing fine-grained cross-task timbre control. To mitigate multi-task optimization conflicts, we design a curriculum learning strategy using task-specific modality masking to guide the model to gradually master the generative mechanisms among semantic content, vocal timbre, and accompaniment. Experiments show state-of-the-art performance on both tasks and realizes complementary benefits, offering new possibilities for intelligent music production.

</details>

#### [VoxCPM2 Technical Report](https://arxiv.org/abs/2606.06928)
**Yixuan Zhou, Guoyang Zeng, Xin Liu, Xiang Li et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

We present VoxCPM2, a https://info.arxiv.org/help/prep#abstractsfully open-source multilingual and controllable speech generation foundation model that extends the hierarchical diffusion-autoregressive modeling paradigm of VoxCPM. VoxCPM2 advances the framework in three key dimensions: (i) capability, by unifying 30 languages, 9 Chinese dialects, natural-language voice design, style-controllable voice cloning, and high-fidelity continuation cloning within a single backbone; (ii) quality, through an asymmetric AudioVAE that encodes at 16 kHz and reconstructs at 48 kHz, enabling implicit super-resolution with high encoding efficiency; and (iii) scale, by jointly scaling the model to 2B parameters and the training data to over 2 million hours of multilingual speech. To support these diverse capabilities within one model, we introduce a unified sequence organization that expresses all generation modes through different arrangements of the same input building blocks, allowing joint training under a single set of parameters and objective. VoxCPM2 achieves state-of-the-art or competitive performance on public zero-shot and instruction-following TTS benchmarks. On our internal 30-language evaluation set, it attains an average WER of 1.68%. These results demonstrate that hierarchical continuous-latent modeling, without relying on any external discrete speech tokenizer, offers a viable and powerful foundation for large-scale multilingual and controllable speech generation. The model weights, fine-tuning code, and inference tools are publicly released under the Apache 2.0 license to foster community research and development.

</details>

#### [Mitigating Proxy-to-Wild Domain Gap in Deepfake Speech](https://arxiv.org/abs/2606.07494)
**Xuanjun Chen, Yun-Shing Wu, Wei-Chung Lu, Claire Lin et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

Recent neural audio codec-based speech generation (CodecFake) produces highly realistic audio, posing a challenge to existing deepfake countermeasure models. While using codec resynthesized speech (CoRS) as proxy data improves performance, it often suffers from limited generalization. We propose Domain-Shift Feature Augmentation (DSFA), which simulates "in-the-wild" variations by transforming deterministic feature statistics into stochastic distributions during fine-tuning. To evaluate generalization, we further introduce Codec-based Speech Generation Extension Evaluation (CoSG ExtEval) dataset, a more challenging extension of the CoSG Eval (from CodecFake+) dataset, featuring 40 unseen generative models and long-form audio. Experimental results demonstrate that combining a post-trained SSL backbone with DSFA effectively narrows the proxy-to-wild domain gap. This approach achieves state-of-the-art performance across diverse CodecFake attacks in both CoSG Eval and CoSG ExtEval.

</details>

#### [GLASS: GRPO-Trained LoRA for Acoustic Style Steering in Zero-Shot Text-to-Speech](https://arxiv.org/abs/2606.05889)
**Jaehoon Kang, Yejin Lee, Kyuhong Shim** · 2026-06-04

<details>
<summary>Abstract</summary>

We propose GLASS, a framework for composable acoustic style control in zero-shot autoregressive text-to-speech (TTS) that learns controls from post-generation rewards rather than style labels. In zero-shot TTS, a speaker prompt often entangles speaker identity with prosodic attributes such as speaking rate and pitch, making it difficult to change style without changing the prompt itself. GLASS instead treats each acoustic attribute as a reward-defined control direction. For each control axis, GLASS freezes the TTS backbone and trains one lightweight LoRA adapter with Group Relative Policy Optimization (GRPO), using speech-token length and mean F0 as style rewards and WER as an intelligibility anchor. Because each control is represented as a LoRA weight update, independently trained adapters can be swapped, interpolated, and composed through linear LoRA arithmetic without retraining the backbone. Experiments on speaking rate and pitch control show targeted style shifts while preserving naturalness, speaker similarity, and intelligibility, and demonstrate smooth interpolation and multi-axis composition across independently trained adapters.

</details>

#### [UniVoice: A Unified Model for Speech and Singing Voice Generation](https://arxiv.org/abs/2606.05852)
**Junjie Zheng, Huixin Xue, Shihong Ren, Chaofan Ding et al.** · 2026-06-04

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) and singing voice synthesis (SVS) both aim to generate human vocal audio from symbolic inputs, but they impose different requirements on the generation process. Speech generation relies on flexible, language-driven prosody, whereas singing generation requires explicit melody control and accurate rhythmic alignment. This mismatch makes it challenging to train a single model that can generate both natural speech and controllable singing, since melody-related conditions should strongly constrain singing but should not restrict speech prosody. We present UniVoice, a unified speech and singing voice generation framework based on conditional flow matching. Instead of using a single undifferentiated conditioning representation, UniVoice factorizes the condition into content, melody, and timbre, which are encoded by modality-appropriate encoders and consumed by a shared Diffusion Transformer (DiT) backbone. For singing, the melody condition is represented by MIDI note sequences; for speech, it is replaced with a learned null melody token, allowing the model to infer prosody from linguistic and acoustic context. This design preserves explicit melody control for singing while avoiding the need to impose melody constraints on speech. We further analyze the null melody token as an approximation to melody marginalization in the conditional flow. Trained on 30k hours of speech and 35k hours of singing data, UniVoice achieves a speech PER of 5.26\%, comparable to dedicated TTS systems such as F5-TTS (5.21\%) and CosyVoice3 (5.30\%). On singing generation, UniVoice achieves a PER of 16.22\%, outperforming the unified baseline Vevo1.5 (24.72\%).

</details>

#### [Multilingual Multi-Speaker Unit Vocoders: A Systematic Analysis of Discrete Speech Representations](https://arxiv.org/abs/2606.06740)
**Naman Kothari, Arjun Gangwar, Adarsh Arigala, S Umesh** · 2026-06-04

<details>
<summary>Abstract</summary>

Discrete speech units obtained via k-means clustering of self supervised embeddings entangle phonetic, speaker, and language information, causing speaker mixing and cross-lingual interference in multilingual multi-speaker speech generation. Despite growing use in Audio LLMs and speech to speech systems, unit vocoders remain underexplored. We analyze a BigVGAN based unit vocoder, across four Indian languages. We study the interaction between cluster size and conditioning strategies using WER, speaker similarity, and unit level metrics. Results show that cluster size governs intelligibility by improving phonetic discriminability, while explicit speaker conditioning is indispensable for preventing identity collapse. Language supervision yields further gains mainly at lower cluster sizes where units remain ambiguous. Our analysis shows similar phonemes across languages collapse to the same cluster IDs at smaller inventories, with larger clusters progressively separating them.

</details>

#### [Task-Vector Arithmetic for Emotional Expressivity Control in Language-Model-Based Text-to-Speech](https://arxiv.org/abs/2606.05367)
**Daniel Oliveira de Brito, Arnaldo Candido Junior** · 2026-06-03

<details>
<summary>Abstract</summary>

We investigate whether task-vector arithmetic, successful for cross-speaker emotional intensity control in modular text-to-speech (TTS), transfers to large-scale TTS systems built on language-model backbones with in-context learning (LM-TTS). Through a systematic elimination study over four progressively narrower operands on Qwen3-TTS-12Hz-1.7B - model weights via LoRA fine-tuning, continuous codec embeddings, discrete codec tokens, and the speaker embedding (x-vector) produced by an ECAPA-TDNN encoder jointly trained with the synthesis backbone - we localize the dominant carrier of emotional prosody to the x-vector. Building on this finding, we propose a training-free method based on centroid arithmetic in x-vector space: an emotion direction $τ= \mathbb{E}_i[x(s_i,\text{emo})] -\mathbb{E}_i[x(s_i,\text{neutral})]$ applied to an unseen target speaker as $x_{\text{new}} = x(\text{target},\text{neutral}) + α\cdotτ$. Using ESD (English) as the $τ$ source and emoUERJ (Brazilian Portuguese) as a cross-lingual ground-truth target, we observe average gains of $+0.29$ in emotion2vec cosine over the ICL baseline on English held-out speakers and $+0.09$ on Brazilian Portuguese held-out speakers, while largely preserving identity (WavLM SECS $\gtrsim 0.88$ for the multi-speaker $τ$ variant) and intelligibility (WER $\approx 0$ in PT-BR). These results offer initial evidence that the reported incompatibility of centroid-arithmetic style control with token-based TTS architectures may be circumvented when the arithmetic operates on the speaker embedding.

</details>

#### [FoeGlass: Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors](https://arxiv.org/abs/2606.05101)
**Sepehr Dehdashtian, Jacob H Seidman, Vishnu N Boddeti, Gaurav Bharaj** · 2026-06-03

<details>
<summary>Abstract</summary>

Audio deepfake detection (ADD) models are critical for countering the malicious use of text-to-speech (TTS) models. Evaluating and strengthening ADD models requires developing datasets that span the space of generated audio and highlight high-error regions. Existing dataset development strategies face two challenges: (i) manual collection, and (ii) inefficient discovery of blind spots in the ADD models. To address these challenges, we propose FoeGlass, the first black-box automated red-teaming method for ADDs, which effectively discovers ADD failure modes in the space of generated audio underexplored by state-of-the-art deepfake benchmarks. FoeGlass uses the in-context learning capabilities of an LLM to explore the input space of a TTS model, generating audio samples that fool the target ADD using only black-box access to all components. By using a carefully designed context based on diversity measurements, FoeGlass mitigates the common problem of mode collapse in automated red-teaming systems. Empirical evaluations on several open-source ADD and TTS models demonstrate that data generated from FoeGlass substantially improves the false negative rates over unconditional sampling baselines and recent spoofing datasets by up to 94%, while requiring no manual supervision. Furthermore, we show that the attacks generated by FoeGlass are transferable across different target ADDs, demonstrating its broad applicability and ease of use for the automated red teaming of ADD systems. Finally, fine-tuning ADD models on FoeGlass-generated samples notably enhances the robustness of the detectors (up 41%).

</details>

#### [CleanCodec: Efficient and Robust Speech Tokenization via Perceptually Guided Encoding](https://arxiv.org/abs/2606.04418)
**Eugene Kwek, Feng Liu, Rui Zhang, Wenpeng Yin** · 2026-06-03

<details>
<summary>Abstract</summary>

Neural audio codecs are a key component of speech processing pipelines, compressing audio into discrete tokens for downstream modeling. However, existing codecs struggle to balance reconstruction quality with token efficiency, often encoding perceptually irrelevant information such as background noise and recording artifacts at the expense of linguistically and acoustically meaningful content. We reframe audio tokenization as a selective information bottleneck problem and propose CleanCodec, a denoising audio codec which learns to encode only perceptually important features and discard imperceptible information. At just 12.5 tokens per second, CleanCodec achieves state-of-the-art tokenization efficiency, substantially outperforming existing codecs in speaker similarity and speech intelligibility. Evaluations on downstream text-to-speech and voice conversion tasks further demonstrate improved performance and up to 17x faster inference, highlighting significant efficiency gains.

</details>

#### [WavTTS: Towards High-Quality Zero-Shot TTS via Direct Raw Waveform Modeling](https://arxiv.org/abs/2606.03455)
**Wenxi Chen, Dongya Jia, Yushen Chen, Zhikang Niu et al.** · 2026-06-02

<details>
<summary>Abstract</summary>

Recently, diffusion models operating on VAE latents or mel-spectrograms have become the dominant paradigm for zero-shot TTS. Although these compressed representations improve generation efficiency, they inevitably suffer from information loss and non-end-to-end training. Theoretically, directly modeling raw waveforms circumvents these issues; however, this direction remains underexplored and is often deemed difficult due to the extremely long sequence length of audio signals. To overcome this, we propose WavTTS, the first raw waveform generative TTS model that substantially narrows the gap with latent-space generative models. Built upon the flow matching with Diffusion Transformer (DiT), WavTTS directly models speech waveforms via a simple patchification strategy, while integrating multi-scale mel-spectrogram supervision to provide perceptual guidance during training. Furthermore, we investigate the impact of prediction targets and noise scheduling in waveform diffusion, and develop an effective schedule design to improve generation quality. Evaluations on open-source benchmarks demonstrate that WavTTS closely approaches the performance of current state-of-the-art latent generative zero-shot TTS models, while substantially outperforming previous end-to-end speech generation models. Our findings demonstrate the feasibility of scaling diffusion-based TTS directly in the waveform space, opening a new direction for end-to-end speech generation.

</details>

#### [Advancing Electrolaryngeal Speech Enhancement Through Speech-Text Representation Learning](https://arxiv.org/abs/2606.01905)
**Ding Ma, Jinyi Mi, Fengji Li, Lester Phillip Violeta et al.** · 2026-06-01

<details>
<summary>Abstract</summary>

Objective: laryngectomees depend on an electromechanical device to generate electrolaryngeal (EL) speech. Compared with normal speech, EL speech suffers from severe distortion, limited phonetic variation, unnatural prosody, and temporal shifts, degrading naturalness and intelligibility. Although sequence-to-sequence (seq2seq) voice conversion (VC) based EL-speech-to-normal-speech conversion (EL2SP) is promising, substantial mismatches between EL and normal speech inevitably cause cumulative mapping errors that limit performance. To address this, we describe a novel representation learning framework integrating speech and text representations to improve mapping and reconstruction quality within a seq2seq VC model. Methods: our methodology comprises two main stages: 1) representation integration and learning, and 2) reconstruction training. A network capable of incorporating auxiliary text information is first constructed with pretrained modules to learn speech--text-based integrated representations. Then, an autoencoder-style reconstruction strategy finalizes EL2SP model to inherit these representations without increasing model complexity. We introduce three fusion strategies including middle-, input-, and hybrid-level fusion strategies that progressively enhance learning. Moreover, besides standard seq2seq VC objectives, an additional reconstruction loss on the integrated representation is introduced to refine representation transfer. Results: experiments under different EL2SP datasets consistently demonstrate that our methods, combined with data augmentations, outperform baselines relying solely on speech representations. Furthermore, progressive improvements with system design depth validate the effectiveness of our methods. Significance: the proposed methods provide an extensible and practical methodology for EL speech enhancement and assistive communication technologies.

</details>

#### [UniVocal: Unified Speech-Singing Code-Switching Synthesis](https://arxiv.org/abs/2606.01677)
**Yufei Shi, Qian Chen, Wen Wang, Xiangang Li et al.** · 2026-06-01

<details>
<summary>Abstract</summary>

We propose UniVocal, a unified framework that implicitly infers vocal modes from text context to pioneer Speech-Singing Code-Switching (SCS) Synthesis - a task where transitions are autonomously driven by textual semantics, akin to seamless human language blending. Unlike single-mode generation or systems relying on switching-control tags, our proposed UniVocal implicitly infers vocal modes solely from text context. To achieve this, we employ a data-efficient two-stage curriculum learning strategy that progressively trains a competitive TTS system to acquire the desired SCS capability. Addressing data scarcity, we introduce a scalable pipeline to synthesize diverse code-switching data that is both semantically and acoustically natural, alongside a new multi-scenario benchmark, SCSBench. To address limitations of semantic tokenizers in capturing acoustic details, we also introduce refined cent token and Chain-of-Thought (CoT) generation for planning prosody before content generation, effectively enhancing empathetic speech generation and singing melody. Experimental results demonstrate that UniVocal achieves state-of-the-art performance on SCSBench while maintaining competitive performance on regular speech and singing tasks. Audio samples are available at https://project-univocal-demo.github.io/demo/. The code and dataset are released at https://github.com/FunAudioLLM/FunResearch/tree/main/UniVocal.

</details>

#### [Sparse Autoencoders for Interpretable Emotion Control in Text-to-Speech](https://arxiv.org/abs/2606.01479)
**Hongfei Du, Jiacheng Shi, Sidi Lu, Gang Zhou et al.** · 2026-05-31

<details>
<summary>Abstract</summary>

Integrating large language models (LLMs) into text-to-speech (TTS) systems has improved speech expressiveness, yet interpretable emotional control remains challenging. Existing approaches primarily rely on external conditioning or global activation steering, offering limited insight into the internal representations underlying emotional control. In this work, we analyze emotion-related variation in the semantic hidden states of LLM-based TTS models using sparse autoencoders (SAEs) to identify sparse latent features. Our analysis shows that emotional variation is distributed across multiple sparse latent features, while intervening on a small subset enables interpretable emotion control. Building on this observation, we introduce a feature-level intervention framework for bidirectional emotion induction and suppression without modifying backbone parameters. We further show that distinct latent features are associated with specific acoustic attributes (e.g., pitch), suggesting that emotional expression arises from coordinated latent contributions rather than a single global shift. Empirically, steering these sparse latent features achieves comparable or superior emotion induction and suppression performance relative to global steering and existing TTS baselines.

</details>

#### [UNISON: A Unified Sound Generation and Editing Framework via Deep LLM Fusion](https://arxiv.org/abs/2605.31530)
**Zhaoqing Li, Haoning Xu, Jingran Su, Yaofang Liu et al.** · 2026-05-29

<details>
<summary>Abstract</summary>

We present UNISON, a latent diffusion framework that unifies speech generation, sound generation, and audio editing within a single model. A single model handles text-to-audio, text-to-speech, zero-shot speaker cloning, mixed speech-and-sound generation, scene-level audio editing, speech-in-scene editing, and timed temporal composition, all of which share a single set of weights. Our architecture features two core designs: (1) Layer-wise deep LLM fusion, which injects hidden states from uniformly sampled layers of a frozen MLLM into corresponding MM-DiT blocks via learned projections, providing depth-matched semantic conditioning that improves instruction following over single-layer baselines; and (2) a unified multi-task architecture where task identity is encoded solely by a channel-wise mask and source audio is provided through VAE-encoded channel concatenation. Training is stabilized by an online GPU-side multi-task data synthesis pipeline with task-homogeneous batching and a two-stage curriculum. With 621M--732M trainable parameters, UNISON achieves results competitive with or exceeding task-specialist models across evaluated domains, while being roughly $4\times$ smaller than comparable unified systems.

</details>

#### [SwanVoice: Expressive Long-Form Zero-Shot Speech Synthesis for Both Monologue and Dialogue](https://arxiv.org/abs/2605.30993)
**Ruiqi Li, Yu Zhang, Changhao Pan, Ke Lei et al.** · 2026-05-29

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) has improved substantially for single-speaker synthesis, yet expressive long-form multi-speaker dialogue remains difficult. A common workaround is to synthesize each turn with a monologue TTS model and stitch the outputs together. This adds inference cost and often breaks acoustic consistency, conversational coherence, and affective continuity across turns. Recent dialogue TTS systems have begun to address this setting, but they still struggle to keep expressive coherence, controllable speaker switching, and monologue quality at the same time. We present SwanData-Speech and SwanVoice. SwanData-Speech builds monologue and dialogue corpora from in-the-wild audio, using Swan Forced Aligner for pause-aware word-level alignment and RobustMegaTTS3 for pronunciation-hard cases. Built on these data, SwanVoice is a zero-shot TTS model for 1--4 speakers, combining a 25 Hz VAE, raw-text conditioning with pause-aware symbols and pinyin substitution, and a flow-matching DiT with speaker-turn conditioning. Training starts from monologue speech, moves through mixed and real dialogue data, and then uses DiffusionNFT post-training with phone-level and speaker-similarity rewards. On SwanBench-Speech, SwanVoice obtains higher richness and hierarchy scores than all evaluated open-source baselines in both monologue and dialogue settings, while content accuracy remains the main limitation. Audio demos are available at https://swanaigc.github.io//#swanvoice.

</details>

#### [ImmersiveTTS: Environment-Aware Text-to-Speech with Multimodal Diffusion Transformer and Domain-Specific Representation Alignment](https://arxiv.org/abs/2605.30965)
**Jun-Hak Yun, Seung-Bin Kim, Seong-Whan Lee** · 2026-05-29

<details>
<summary>Abstract</summary>

Recent advancements in text-guided audio generation have yielded promising results in diverse domains, including sound effects, speech, and music. However, jointly generating speech with environmental audio remains challenging due to the inherent disparities in their acoustic patterns and temporal dynamics. We propose ImmersiveTTS, an environment-aware text-to-speech (TTS) model that generates natural speech seamlessly integrated within environmental contexts by explicitly modeling cross-modal interactions. Our model builds on a multimodal diffusion transformer and fuses transcript-aligned speech latent with text-conditioned environmental context via joint attention. To enhance semantic consistency, we introduce a domain-specific representation alignment objective tailored to environment-aware TTS, leveraging complementary self-supervised representations from speech and audio encoders. Experimental results show that ImmersiveTTS achieves higher naturalness, intelligibility, and audio fidelity than existing approaches across objective metrics and human listening tests.

</details>

#### [Chatterbox-Flash: Prior-Calibrated Block Diffusion for Streaming Zero-Shot TTS](https://arxiv.org/abs/2605.30748)
**Deokjin Seo, Gangin Park, Kihyun Nam** · 2026-05-29

<details>
<summary>Abstract</summary>

We present Chatterbox-Flash, a zero-shot text-to-speech model obtained by fine-tuning a pretrained autoregressive TTS decoder into a block-diffusion decoder, enabling parallel token generation within each block while retaining block-by-block streaming. We find that naively transferring mainstream block-diffusion decoding to discrete speech tokens degrades quality, as a long-tail token distribution biases parallel position selection toward a few high-frequency tokens. To mitigate this without architectural modification, we introduce two inference-time techniques: prior-calibrated scoring, which subtracts the block-level marginal token distribution, and an early-decoding schedule, which adaptively terminates iteration based on calibrated confidence. On standard zero-shot TTS benchmarks, Chatterbox-Flash attains high-fidelity synthesis comparable to strong autoregressive and non-autoregressive baselines, while supporting streaming inference with time-to-first-packet on par with streaming AR systems and substantially lower real-time factor. Code and audio samples are available at https://github.com/resemble-ai/chatterbox-flash.

</details>

#### [MindVoice: Reconstructing Intelligible Speech from Non-invasive Neural Signals with Pretrained Priors](https://arxiv.org/abs/2605.31173)
**Guangyin Bao, Taiping Zeng, Jianfeng Feng, Xiangyang Xue** · 2026-05-29

<details>
<summary>Abstract</summary>

Reconstructing continuous speech from non-invasive neural recordings is a fundamental problem for probing human auditory perception and building safe, scalable speech brain-computer interfaces. Despite recent progress, intelligible reconstruction remains elusive, as non-invasive recordings are inherently noisy, spatially blurred, and only partially preserve information about perceived speech. Existing methods directly map neural activity to entangled speech representations before synthesizing waveforms with neural vocoders, resulting in spectral-similar but unintelligible results. To overcome these limitations, we introduce MindVoice, a neuro-to-speech reconstruction framework that uses pretrained models to compensate for the incomplete semantic and acoustic information in neural recordings. MindVoice disentangles reconstruction into two complementary pathways: one recovers high-level semantic content, while the other estimates fine-grained acoustic attributes. These inferred representations are then fused with powerful speech generation models and in-context voice cloning to synthesize natural and intelligible utterances. Extensive experiments on EEG and MEG demonstrate that MindVoice substantially outperforms existing methods on various metrics. These results show that pretrained priors provide a principled way to bridge the gap between noisy neural recordings and natural speech, highlighting a promising attempt for auditory neuroscience research and non-invasive speech brain-computer interfaces.

</details>

#### [UniAudio-Token: Empowering Semantic Speech Tokenizers with General Audio Perception](https://arxiv.org/abs/2605.31521)
**Yuhan Song, Linhao Zhang, Aiwei Liu, Chuhan Wu et al.** · 2026-05-29

<details>
<summary>Abstract</summary>

Semantic speech tokenizers have become a widely used interface for Audio-LLMs, owing to their compact single-codebook design and strong linguistic alignment. However, their focus on linguistic abstraction induces acoustic blindness, limiting their applicability beyond speech-centric tasks. We propose UniAudio-Token, a framework that empowers semantic tokenizers with general audio perception without compromising speech ability. Instead of altering the semantic paradigm, UniAudio-Token mitigates its information loss through two key innovations: (1) Semantic-Acoustic Primitives (SAP) provide structured supervision by decomposing audio into linguistic content, vocal attributes, and auditory-scene primitives; and (2) Semantic-Acoustic Equilibrium (SAE) introduces a content-aware gating mechanism that adaptively restores fine-grained acoustic details from shallow layers. Extensive evaluations show that UniAudio-Token learns comprehensive universal representations while preserving high-fidelity speech generation. When integrated with downstream LLMs, it outperforms all single-codebook baseline tokenizers on both understanding and generation tasks, effectively serving as a unified audio interface. We publicly release all our code, including training and inference scripts, together with the model checkpoints at https://github.com/Tencent/Universal_Audio_Tokenizer.

</details>

#### [MELD: Mel-Spectrogram-Based Speech Language Modeling with Discrete Latent Variables](https://arxiv.org/abs/2605.29859)
**Sung-Lin Yeh, Wei Zhou, Gil Keren, Duc Le et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

Recent speech language models rely on encoders that are optimized separately from autoregressive models. Since these encoders are unaware of the downstream objectives, the extracted representations may not be optimal for downstream tasks. To address this limitation, we introduce a discrete latent variable model on mel spectrograms that jointly optimizes the encoder and the speech language model. Joint optimization not only brings improvements over codec-based and other mel-spectrogram-based baselines on zero-shot Text-to-Speech (TTS) and Speech-to-Text (STT) tasks, but also effectively alleviates common issues in autoregressive mel-spectrogram modeling, such as prolonged silence generation and word omissions.

</details>

#### [HoliTok:A Coutinuous Holistic Tokenization with Robust Dual Capabilities of Speech Generation and Understanding](https://arxiv.org/abs/2605.29948)
**Bohan Li, Shi Lian, Hankun Wang, Yiwei Guo et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

Unified speech foundation models require a holistic tokenization space that is both learnable by language models and decodable into high-quality waveforms. Existing speech tokenizers, however, often fail to satisfy these requirements simultaneously, leading to increased architectural complexity and more involved training designs. We propose HoliTok, a continuous Holistic speech Tokenization model designed for unified generation-understanding modeling. HoliTok encodes 48~kHz speech into a compact 25~Hz sequence of 128-dimensional latents. It is trained with a progressive strategy that jointly preserves signal-level fidelity, incorporates semantic information, and maintains strong latent learnability. Based on this tokenization, we build a unified AR+DiT model for speech synthesis and recognition, where the same latent sequence supports both generation-specific and unified generation-understanding tasks. Experiments show that HoliTok achieves competitive reconstruction fidelity, improves generative learnability for high-quality and controllable synthesis, and, among the evaluated representations, is the only one that operates robustly in our unified generation-understanding architecture without additional optimization tricks. These results suggest that HoliTok serves as an effective speech tokenizer and a foundational representation interface for unified spoken language modeling. The code is available at: https://github.com/bovod-sjtu/HoliTok.

</details>

#### [Why We Need Speech to Evaluate Speech Translation](https://arxiv.org/abs/2605.28227)
**Maike Züfle, Danni Liu, Vilém Zouhar, Jan Niehues** · 2026-05-27

<details>
<summary>Abstract</summary>

Speech translation models are increasingly capable of preserving speech-specific information (e.g., speaker gender, prosody, and emphasis), yet evaluation metrics remain blind to such phenomena. We meta-evaluate both text- and speech-based quality estimation metrics on two contrastive datasets targeting gender agreement and prosody, and find that both fall short, even when given direct access to the speech signal. We then train SpeechCOMET, a family of quality estimation models with speech encoders, and evaluate a state-of-the-art SpeechLLM as a judge. Both match or exceed text-based COMET on standard quality estimation, but neither consistently assesses speech-specific phenomena. We identify three causes: (1) speech-specific features are not reliably preserved in current encoders, (2) models tend to ignore the speech source signal, and (3) quality estimation training data contains too few relevant examples. We release all models and code, and argue that progress requires dedicated speech-specific training data and models that genuinely condition on speech.

</details>

#### [Comprehensive Benchmarking of Long-Form Speech Generation in Diverse Scenarios](https://arxiv.org/abs/2605.28618)
**Changhao Pan, Rui Yang, Han Wang, Zhuan Zhou et al.** · 2026-05-27

<details>
<summary>Abstract</summary>

Recent advances in speech generation have enabled high-fidelity synthesis, yet systematic evaluation of models under long-context conditions remains largely underexplored. A comprehensive evaluation benchmark for long-form speech is indispensable for two reasons: 1) existing test scenarios are often confined to limited domains, creating a significant gap with the diverse downstream applications; 2) existing metrics overlook critical long-text factors such as consistency and coherence, failing to generalize reliably. To this end, we propose Swanbench-Speech, a comprehensive benchmark that decomposes long-form speech quality into specific, disentangled dimensions. SwanBench-Speech has three key properties. 1) Rich speech scenarios: Focusing on long-form speech generation and dialog generation, SwanBench-Speech covers acoustics, semantics, and expressiveness challenges, and consists of 1,101 samples spanning 17 common speech scenarios; 2) Comprehensive evaluation dimensions: Along the acoustics, semantics, and expressiveness axes, SwanBench-Speech defines an automated evaluation protocol with seven metrics to provide a comprehensive, accurate, and standardized assessment; 3) Valuable Insights: Through extensive experiments, we reveal that current models still struggle in highly expressive scenarios and exhibit a notable gap in consistency and hierarchy compared to real recordings.

</details>

#### [PilotTTS: A Disciplined Modular Recipe for Competitive Speech Synthesis](https://arxiv.org/abs/2605.27258)
**Bowen Li, Shaotong Guo, Zhen Wang, Yang Xiang et al.** · 2026-05-26

<details>
<summary>Abstract</summary>

Building state-of-the-art text-to-speech (TTS) systems typically demands millions of hours of proprietary data and complex multi-stage architectures, creating substantial barriers for resource-constrained research teams. In this report, we present PilotTTS, a lightweight autoregressive TTS system that achieves competitive performance through minimalist architecture and rigorous data engineering. PilotTTS is trained on only 200K hours of data processed entirely with open-source tools. Specifically, our contributions are: (1) a reproducible multi-stage data processing pipeline covering quality assessment, label annotation, and filtering, and (2) a compact model architecture that employs Q-Former-based conditioning to decouple speaker identity from speaking style via cross-sample paired training. Within a unified framework, PilotTTS supports zero-shot voice cloning, emotion synthesis (11 categories), paralinguistic synthesis (4 categories), and Chinese dialect synthesis (14 dialects). On the Seed-TTS Eval benchmark, PilotTTS achieves the lowest WER of 1.50% on test-en, a CER of 0.87% on test-zh, and the highest speaker similarity on both test sets (0.862 and 0.815), outperforming systems trained on significantly larger datasets. We release the complete data pipeline recipe, pretrained weights, and code at https://github.com/AMAPVOICE/PilotTTS.

</details>

#### [Learning When to Think While Listening in Large Audio-Language Models](https://arxiv.org/abs/2605.27190)
**Zhiyuan Song, Weici Zhao, Yang Xiao, Suhao Yu et al.** · 2026-05-26

<details>
<summary>Abstract</summary>

Recent advances in Large Audio-Language Models (LALMs) have made real-time, streaming spoken interaction increasingly practical. In this setting, reasoning quality and responsiveness are tightly coupled: delaying reasoning until the speech endpoint can improve answer quality but moves deliberation into user-visible response delay, while answering too early risks committing before decisive evidence arrives. We introduce a learnable wait-think-answer control formulation for LALMs. Motivated by the incremental nature of human conversation, the controller decides under partial audio evidence when to wait, when to externalize a compact reasoning update, and when to answer. Using Qwen2.5-Omni-7B as the base model, we construct aligned wait-think-answer traces from spoken reasoning data, train the controller with supervised fine-tuning (SFT), and then apply Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO). The reward combines answer correctness, action validity, update timing, latency synchronization, reasoning quality, and chain consistency, optimizing the complete wait-think-answer trajectory and not the final answer alone. On a six-task synthetic spoken reasoning question answering (SRQA) benchmark, the six-reward DAPO controller improves the row-weighted accuracy from 67.6% to 70.3% while reducing post-endpoint final-think length by 14% under the same Qwen deployment harness. On a 186-item human-recorded Real Audio Bench, a transfer check beyond text-to-speech (TTS)-rendered speech, the controller family remains functional: SFT achieves the strongest accuracy, while the six-reward DAPO controller is the only learned variant whose final-think length falls below the base. These results suggest that a streaming model should learn when to make intermediate reasoning explicit during the audio stream.

</details>

#### [PashtoTTS-Bench: automated screening for low-resource non-Latin-script text-to-speech](https://arxiv.org/abs/2605.26978)
**Hanif Rahman** · 2026-05-26

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) evaluation for low-resource non-Latin-script languages can fail when it relies on a single ASR round-trip word error rate (WER). A system may produce no audio, speak a neighbouring language, preserve target script text only in an ASR transcript, or sound unnatural to native listeners. We introduce INSV (Intelligibility, Naturalness, Script fidelity, and Verification), a reporting framework that separates these cases. This paper reports INSV-A, the automated screening subset: synthesis completion, ASR WER/CER, transcript Script Fidelity Rate, and audio language identification. Native MOS and phonetic annotation are specified but not claimed in this release. We instantiate INSV-A as PashtoTTS-Bench, a dated benchmark for Pashto TTS. The April-May 2026 run evaluates Edge GulNawaz, Edge Latifa, OmniVoice clone, OmniVoice auto, and an Urdu negative control on 200 FLEURS and 200 filtered Common Voice 24 prompts. Under the independent omniASR_CTC_300M_v2, OmniVoice auto has the lowest WER (24.1% FLEURS, 27.4% CV24), followed by Edge GulNawaz (32.8%, 39.5%), Edge Latifa (35.6%, 47.7%), and OmniVoice clone (45.4%, 34.8%). WER below the natural-speech baseline reflects clean synthetic audio and should not be read as better than native speech. Whisper Large V3 returns 0.0% Pashto labels on checked Pashto TTS audio, while MMS-LID-4017 and SpeechBrain VoxLingua107 separate Pashto outputs from the Urdu control. The release provides provider metadata, per-sentence scores, LID audits, failure logs, and scripts for adding systems.

</details>

#### [Can We Hear from Events? Generating Speech from Event Camera](https://arxiv.org/abs/2605.26672)
**Jingping Fang, Lin Chen, Chenyang Xu, Tong Zhao et al.** · 2026-05-26

<details>
<summary>Abstract</summary>

Traditional RGB-based speech generation faces Temporal Granularity Mismatch since fixed camera exposure times inevitably blur the high-frequency articulatory transients essential for rendering emotional speech. To break this ceiling, we propose EventSpeech as a novel text-conditioned framework pioneering the use of neuromorphic events for expressive speech generation, since these microsecond-precise events naturally align with acoustic waveform dynamics. Our architecture integrates a dedicated Event Encoder to model sparse neuromorphic events alongside a multi-scale Audio Encoder featuring a Hierarchical Wavelet Contextualizer (HWC). A bidirectional alignment mechanism seamlessly synchronizes linguistic content and visual dynamics with dense acoustic features. Furthermore, we construct EVT-SPK as the first benchmark comprising large-scale synthetic data and real-world recordings from specialized neuromorphic hardware. Extensive evaluations demonstrate that EventSpeech significantly outperforms current baselines by preserving fine-grained emotions and resisting motion blur to establish a new paradigm for multimodal speech generation. Code and demo are available at https://xrfang-0102.github.io/EventSpeechWeb/.

</details>

#### [Continual Speaker Identity Unlearning with Minimal Interference](https://arxiv.org/abs/2605.25962)
**Jinju Kim, Yunsung Kang, Gyeong-Moon Park, Jong Hwan Ko** · 2026-05-25

<details>
<summary>Abstract</summary>

Machine unlearning removes designated concepts or knowledge from pre-trained models. Recent work has extended this paradigm to speaker identity unlearning in zero-shot text-to-speech (ZS-TTS), the task of selectively erasing a model's ability to replicate a speaker's voice. Existing methods, however, quietly assume all unlearning requests arrive at once; an unrealistic assumption, since privacy-motivated removals arrive sequentially over time. We show this assumption breaks state-of-the-art methods: unlearning each new speaker fully revives previously unlearned speakers, reintroducing the very privacy risk unlearning was meant to eliminate. We present Cumulative ORThogonal Identity Suppression (CORTIS), the first framework for continual speaker identity unlearning in ZS-TTS that requires no access to previously-unlearned speaker data. CORTIS combines Fisher-information-based parameter masking, which localizes updates to speaker-relevant weights, with orthogonal projection against subspaces spanned by prior unlearning updates. With VoiceBox, CORTIS unlearns each requested speaker while keeping previously unlearned speakers forgotten across long request sequences, substantially outperforming sequential application of prior methods. The demo is available at https://cumulativeortis.github.io/ .

</details>

#### [CosyEdit2: Speech-Editing-Oriented Reinforcement Learning Unlocks Better Zero-Shot TTS](https://arxiv.org/abs/2605.25930)
**Junyang Chen, Yuhang Jia, Hui Wang, Jiaming Zhou et al.** · 2026-05-25

<details>
<summary>Abstract</summary>

Speech editing and zero-shot Text-to-Speech (TTS) share a similar generative foundation conditioned on speech prompts, yet speech editing demands far stricter local acoustic consistency with surrounding unedited content. While prior work has shown that Supervised Fine-Tuning (SFT) enables TTS models to acquire functional editing capability, this approach remains fundamentally bottlenecked by imperfect paired editing data and coarse-grained optimization signals. To address these limitations, we propose CosyEdit2, a speech editing model built on a two-stage post-training framework that progresses from supervised editing initialization to editing-oriented Group Relative Policy Optimization (GRPO) over target-speech-free data. Extensive experiments demonstrate that CosyEdit2 not only substantially advances speech editing performance, but also unlocks better zero-shot TTS capability, revealing a deeper mutual relationship between the two tasks. Audio samples are available at https://cjy1018.github.io/CosyEdit2.

</details>

#### [Thaka at KSAA-2026 Task 2: Regularized Fine-Tuning for Arabic Speech Diacritization](https://arxiv.org/abs/2605.25928)
**Meshal Alamr, Hassan Alqaeri, Abdullah Aldahlawi** · 2026-05-25

<details>
<summary>Abstract</summary>

We describe the winning system for Task 2 of the KSAA-2026 Shared Task on Arabic Speech Dictation with Automatic Diacritization. The task requires producing fully diacritized Arabic text from speech audio and undiacritized transcripts, with only 2,327 training samples available and no external data permitted. Our system fine-tunes CATT-Whisper, a character-level multimodal model combining a pretrained CATT text encoder with a frozen Whisper speech encoder. The key to our approach is training regularization: R-Drop consistency regularization, Optuna-optimized hyperparameters with high weight decay, and Focal Loss. At inference, we average 200 stochastic forward passes across four model checkpoints using Monte Carlo Dropout at the softmax probability level. The system achieves 23.26% WER on the primary leaderboard metric (with case endings, including no-diacritic positions), placing 1st among all participants.

</details>

#### [Toward Natural Emotional Text-To-Speech System with Fine-Grained Non-Verbal Expression Control](https://arxiv.org/abs/2605.25504)
**Wangzixi Zhou, Bagus Tris Atmaja, Sakriani Sakti** · 2026-05-25

<details>
<summary>Abstract</summary>

While current emotional Text-to-Speech (TTS) models have successfully controlled verbal prosody, they often ignore non-verbal vocalizations (NVs), which are essential for authentic human emotion. Although some non-verbal datasets have recently emerged, they often lack high-quality, fine-grained annotations, which restricts a model's ability to precisely control NV generation. To address this limitation, we propose a novel approach for fine-grained non-verbal expression synthesis. We curate and reprocess female NV utterances from the EARS corpus, develop a new annotation scheme using tags to encode NV types, frequencies, and durations, and build an emotional TTS benchmark to demonstrate its effectiveness. Our evaluation shows that while our NV approach leads to minor trade-offs in perceived naturalness, it significantly improves expressiveness (eMOS 4.20) and emotional recognition accuracy (78.8%). Emotion-specific analysis further reveals that NV cues are highly effective for high-arousal emotions like happy (82.5%) and fear (82.7%), and almost perfectly convey sadness (98.3%).

</details>

#### [Natural Yet Challenging to Detect: Robust In-the-Wild TTS through EMA and Dual-Scoring Prompt Selection -- Submission for WildSpoof 2026 TTS Track](https://arxiv.org/abs/2605.23859)
**Renhe Sun, Jiayi Zhou, Haolin He, Yueying Feng et al.** · 2026-05-22

<details>
<summary>Abstract</summary>

In this technical report, we describe our submission for the WildSpoof Challenge TTS Track: Text-to-Speech with In-the-Wild Data. We introduce F5-TTS-DPS, a model built upon the F5-TTS architecture. Our approach integrates Exponential Moving Average (EMA) into supervised fine-tuning to stabilize training and improve generalization. To enhance synthesis fidelity, we leverage large language models (LLMs) and large audio language models (LALMs) for dual-scoring prompt selection, filtering reference audio and text prompts to ensure quality while addressing alignment issues in noisy datasets. Experimental evaluation demonstrates that F5-TTS-DPS achieves strong performance with UTMOS of 3.20 and speaker similarity of 0.51 on the development set. More importantly, our model achieves the best a-DCF scores of 0.1582, 0.5233, and 0.2562 across three advanced SASV systems among all submissions, indicating our synthesized speech is the most difficult to detect and exhibits the highest degree of naturalness and authenticity. Combined with competitive WER performance, these results validate the effectiveness of our approach in generating natural-sounding speech with strong spoofing capabilities.

</details>

#### [Word-Level Modeling with Alignment-Aware Acoustic Fusion for Text-Assisted Intelligibility Prediction in Listeners with Hearing Loss](https://arxiv.org/abs/2605.23604)
**Kazushi Nakazawa** · 2026-05-22

<details>
<summary>Abstract</summary>

We address text-assisted speech intelligibility prediction for hearing-impaired listeners in CPC3. Although the target is a sentence-level percentage, it is determined by reference-word recognition outcomes. We formulate prediction as reference-conditioned word-level correctness modeling: a frozen Whisper encoder analyzes degraded speech, a teacher-forced decoder conditions on the canonical transcript, and sentence intelligibility is obtained by averaging predicted correctness probabilities over valid reference words. To complement transcript-conditioned decoder states, we add a word-aligned local acoustic branch based on character-level cross-attention alignment and an utterance-level global acoustic branch for calibration. On the official evaluation set, the decoder baseline obtains RMSE 24.92 and correlation 0.795, while joint fusion improves to incorrect-word F1 0.778, MCC 0.626, correlation 0.806, and RMSE 24.39. A similar trend with Whisper medium suggests that the gain comes from prediction granularity and alignment-aware fusion.

</details>

#### [UniSRM: A Unified Speech Reward Model for Reasoning-Based Fine-grained Assessment](https://arxiv.org/abs/2605.23261)
**Yuanyuan Wang, Dongchao Yang, Yayue Deng, Zhiyong Wu et al.** · 2026-05-22

<details>
<summary>Abstract</summary>

Evaluating speech generation still relies heavily on human judgments, such as Mean Opinion Score (MOS), which are expensive, subjective, and difficult to reproduce at scale. While a few recent studies have begun to explore AudioLLM-based judge models, existing efforts typically target only a narrow set of scenarios (e.g., utterance-level quality or single-turn dialogue) and provide limited coverage of diverse speech generation tasks and evaluation dimensions. In this work, we propose UniSRM, a unified speech reward model that can support multi-dimensional, interpretable reward signals with reliable reasoning. To support training and evaluation, we introduce UniSRM-Data and UniSRM-Bench, covering speech evaluation tasks from utterance-level quality to context-level coherence. Based on this dataset, we present the unified speech reward model, UniSRM, with a two-stage pipeline that enables reasoning-based fine-grained assessment. Furthermore, we introduce Reasoning-Consistent Rewards to improve the reliability of the reasoning process. Experiments show that UniSRM delivers more reliable and human-aligned judgments across a broad range of speech evaluation tasks, offering a practical foundation for scalable and unified evaluation of speech quality.

</details>

#### [Do Factual Recall Mechanisms Carry over from Text to Speech in Multimodal Language Models?](https://arxiv.org/abs/2605.22170)
**Luca Modica, Filip Landin, Mehrdad Farahani, Livia Qian et al.** · 2026-05-21

<details>
<summary>Abstract</summary>

In recent years, several Speech Language Models (SLMs) that represent speech and written text jointly have been presented. The question then emerges about how model-internal mechanisms are similar and different when operating in the two modalities. We focus on how these systems encode, store, and retrieve factual knowledge, which has previously been investigated for text-only models. To investigate mechanisms behind the storage and recall of factual association in SLMs, we leverage Causal Mediation Analysis, a technique previously applied to text-based models. Initial results using SpiritLM, a multimodal model integrating discrete speech tokens reveal discrepancies between text-to-text and speech-to-text results, suggesting that the emergent mechanisms for factual recall are only partially carried over from the text to the speech modality. These results advance our understanding of how internal mechanisms encode factual associations in SLMs while contributing insights for improving speech-enabled AI systems.

</details>

#### [RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching](https://arxiv.org/abs/2605.22083)
**Jinhyeok Yang, Hyeongju Kim, Yechan Yu, Joon Byun et al.** · 2026-05-21

<details>
<summary>Abstract</summary>

While flow-matching text-to-speech (TTS) achieves strong zero-shot speaker similarity and naturalness, it remains susceptible to content fidelity issues, particularly skip and repeat errors from imperfect alignment. We propose RobustSpeechFlow, a training strategy that improves alignment robustness by extending contrastive flow matching with length-preserving repeat and skip latent augmentations. Requiring no external aligners or preference data, our method directly penalizes realistic failure modes and readily integrates into existing pipelines. On Seed-TTS-eval, it reduces the word error rate (WER) from 1.44 to 1.38 using only 0.06B parameters. On our ZERO500 benchmark, it delivers consistent intelligibility improvements across diverse speaker and prosody conditions; at NFE=24, it reduces English character error rate (CER) from 0.48\% to 0.35\% and Korean CER from 0.81\% to 0.57\%. Audio samples: https://robustspeechflow.github.io/

</details>

#### [Raon-OpenTTS: Open Models and Data for Robust Text-to-Speech](https://arxiv.org/abs/2605.20830)
**Semin Kim, Seungjun Chung, Taehong Moon, Sangheon Lee et al.** · 2026-05-20

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) models show impressive speech naturalness and quality, yet the role of large-scale open data in driving this progress remains underexplored. In this work, we introduce Raon-OpenTTS, an open TTS model that performs competitively with state-of-the-art closed-data TTS models, and Raon-OpenTTS-Pool, a large-scale open dataset for reproducible TTS training. Raon-OpenTTS-Pool consists of 615K hours of 240M speech segments aggregated from publicly available English speech corpora and web-sourced recordings. With a model-based filtering pipeline applied to Raon-OpenTTS-Pool, we derive Raon-OpenTTS-Core, a curated, high-quality subset of 510K hours and 194M speech segments. Using Raon-OpenTTS-Core, we train Raon-OpenTTS, a series of diffusion transformer (DiT)-based TTS models from 0.3B to 1B parameters. On multiple benchmarks, Raon-OpenTTS-1B shows comparable performance to state-of-the-art models such as Qwen3-TTS and CosyVoice 3, which are trained on several million hours of proprietary speech data. Notably, on Seed-TTS-Eval, Raon-OpenTTS-1B achieves a word error rate (WER) of 1.78% and a speaker similarity (SIM) of 0.749, ranking second on WER and first on SIM among recent open-weight TTS baselines. On CV3-Hard-EN, Raon-OpenTTS-1B achieves a WER of 6.15% and a SIM of 0.775, ranking first on both metrics. Furthermore, to support robust evaluation, we introduce Raon-OpenTTS-Eval, a structured benchmark for assessing TTS robustness across diverse acoustic conditions including clean, noisy, in-the-wild, and expressive speech. On Raon-OpenTTS-Eval, Raon-OpenTTS-1B achieves the best average WER and SIM among all evaluated models, and the second-best human preference, as measured by comparative mean opinion score (CMOS). Our data pool, filtering pipeline, training code, and checkpoints are publicly available at https://github.com/krafton-ai/RAON-OpenTTS.

</details>

#### [Evaluating Speech Articulation Synthesis with Articulatory Phoneme Recognition](https://arxiv.org/abs/2605.20920)
**Vinicius Ribeiro, Yves Laprie** · 2026-05-20

<details>
<summary>Abstract</summary>

Recent advances in machine learning and the availability of articulatory datasets allow vocal tract synthesis to be conditioned on phonetic sequences, a primary task of articulatory speech synthesis. However, quality assessment needs a better definition. Generally, ranking generative models is tricky due to subjectivity. However, articulatory synthesis has the additional difficulty of requiring specialized knowledge in vocal tract anatomy and acoustics. To address this problem, this paper proposes to evaluate speech articulation synthesis using phoneme recognition as a proxy. Our hypothesis is that phoneme recognition using articulatory features better captures nuances in phoneme production, such as correct places of articulation, which traditional metrics (e.g., point-wise distance metrics) do not. We train a neural network with acoustic and articulatory features extracted from a single-speaker RT-MRI dataset. Then, we compare the recognition performance when testing the model with different synthetic articulatory features. Our results show that our articulatory feature set is phonetically rich and helps exploring additional dimensions on speech articulation synthesis.

</details>

#### [Thinking-while-speaking: A Controlled, Interleaved Reasoning Method for Real-Time Speech Generation](https://arxiv.org/abs/2605.20946)
**Xuan Du, Qiangyu Yan, Wenshuo Li, Borui Jiang et al.** · 2026-05-20

<details>
<summary>Abstract</summary>

The thinking-while-speaking paradigm aims to make AI communication more human. A key challenge is maintaining fluent speech while performing deep reasoning. Our method, InterRS, tackles this by inserting reasoning steps only during natural speech generation. This requires high-quality data where reasoning and speech are precisely aligned, and the length ratio are under controlled. We introduce a novel pipeline to generate such seamlessly interleaved audio data. To train our model, we combine interleaved SFT with refined data and reinforcement learning with two new rewards: a TA-Balance Reward to manage timing and thinking-answer ratio, and a Linguistic Quality Reward to refine expression. Experiments show our approach achieves 13% better performance on mathmatical and logic benchmarks while generating instant response like a spoken-language instruct model which outputs fast CoT response. Furthermore, our method generates more natural and fluent answers than prior methods.

</details>

#### [Bridging the Gap: Converting Read Text to Conversational Dialogue](https://arxiv.org/abs/2605.18001)
**Parshav Singla, Agnik Banerjee, Aaditya Arora, Shruti Aggarwal et al.** · 2026-05-18

<details>
<summary>Abstract</summary>

In recent advancements within speech processing, converting read speech to conversational speech has gained significant attention. The primary challenge in this domain is maintaining naturalness and intelligibility while minimizing computational overhead for real-time applications. Traditional read speech often lacks the nuanced prosodic variation essential for natural conversational interactions, posing challenges for applications in virtual assistants, customer service, and language learning tools. This paper introduces a novel approach, Prosodic Adjustment with Conversational Context (PACC), aimed at converting read speech into natural conversational speech used in various modern applications. PACC utilizes advanced deep neural networks to analyze and modify prosodic features such as intonation, stress, and rhythm. Unlike conventional methods, our approach uses High-Fidelity Generative Adversarial Networks (HiFi-GAN) for speech synthesis. Our experimental results demonstrate significant improvements in speech conversion, enhancing naturalness and achieving better model accuracy with additional training on speech datasets. This research establishes new benchmarks in speech conversion tasks and Mean Opinion Score (MOS) evaluation for testing model accuracy, and we show that our approach can be successfully extended to other speech conversion applications.

</details>

#### [Linked Multi-Model Data on Russian Domestic and Foreign Policy Speeches](https://arxiv.org/abs/2605.15886)
**Daria Blinova, Gayathri Emuru, Rakesh Emuru, Kushagradheer Shridheer Srivastava et al.** · 2026-05-15

<details>
<summary>Abstract</summary>

This paper introduces a dataset of interlinked multimodal political communications from the Russian government, addressing persistent deficiencies in the availability of social text- and image-based data for authoritarian politics contexts. The dataset comprises two large corpora of official speeches delivered by senior actors within the Kremlin and the Russian Ministry of Foreign Affairs over multiple decades. For each speech, we provide Russian- and English-language texts, associated images and captions where available, and harmonized metadata including (e.g.) dates, speakers, (geo)locations, and official government content tags. Unique identifiers link images to speeches and align Russian and English versions of the same communication texts. We further augment these linked datasets with validated topical annotations for both speech texts and speech images, which are generated via transformer-based multimodal topic modeling and refined by a Russian politics expert. The resulting data resources support multimodal, multilingual, temporal, and/or spatial analyses of (authoritarian) political communication and offer a valuable testbed for social science research and large language model (LLM) applications in political domains.

</details>

#### [From Text to Voice: A Reproducible and Verifiable Framework for Evaluating Tool Calling LLM Agents](https://arxiv.org/abs/2605.15104)
**Md Tahmid Rahman Laskar, Xue-Yong Fu, Seyyed Saeed Sarfjoo, Quinten McNamara et al.** · 2026-05-14

<details>
<summary>Abstract</summary>

Voice agents increasingly require reliable tool use from speech, whereas prominent tool-calling benchmarks remain text-based. We study whether verified text benchmarks can be converted into controlled audio-based tool calling evaluations without re-annotating the tool schema and gold labels. Our dataset-agnostic framework uses text-to-speech, speaker variation, and environmental noise to create paired text-audio instances while preserving the original dataset annotations. Based on extensive evaluation of 7 omni-modal models on audio-converted versions of Confetti and When2Call, our framework demonstrates that the performance is strongly model- and task-dependent: Gemini-3.1-Flash-Live obtains the highest Confetti score (70.4), whereas GPT-Realtime-1.5 performs best on When2Call (71.9). On Confetti, the text-to-voice gap ranges from 1.8 points for Qwen3-Omni to 4.8 points for GPT-Realtime-1.5. A targeted analysis of failure cases demonstrates that degradations most often reflect misunderstandings of argument values in the speech. Considering real-world deployment scenarios, we further report text-only results, an ambiguity-based reformulation stress test, and a reference-free LLM-as-judge protocol validated against human preferences. Notably, we find that open-source Qwen3 judges with at least 8B parameters exceed 80% agreement with proprietary judges, supporting privacy-preserving evaluation. Overall, our framework provides a verifiable and reproducible first-stage diagnostic that complements purpose-built audio corpora.

</details>

#### [Exploiting Pre-trained Encoder-Decoder Transformers for Sequence-to-Sequence Constituent Parsing](https://arxiv.org/abs/2605.13373)
**Daniel Fernández-González, Cristina Outeiriño Cid** · 2026-05-13

<details>
<summary>Abstract</summary>

To achieve deep natural language understanding, syntactic constituent parsing plays a crucial role and is widely required by many artificial intelligence systems for processing both text and speech. A recent approach involves using standard sequence-to-sequence models to handle constituent parsing as a machine translation problem, moving away from traditional task-specific parsers. These models are typically initialized with pre-trained encoder-only language models like BERT or RoBERTa. However, the use of pre-trained encoder-decoder language models for constituency parsing has not been thoroughly explored. To bridge this gap, we extend the sequence-to-sequence framework by investigating parsers built on pre-trained encoder-decoder architectures, including BART, mBART, and T5. We fine-tune them to generate linearized parse trees and extensively evaluate them on different linearization strategies across both continuous treebanks and more complex discontinuous benchmarks. Our results demonstrate that our approach outperforms all prior sequence-to-sequence models and performs competitively with leading task-specific constituent parsers on continuous constituent parsing.

</details>

#### [The Deepfakes We Missed: We Built Detectors for a Threat That Didn't Arrive](https://arxiv.org/abs/2605.12075)
**Shaina Raza** · 2026-05-12

<details>
<summary>Abstract</summary>

Nearly a decade of Machine Learning (ML) research on deepfake detection has been organized around a threat model inherited from 2017--2019, revolving around face-swap and talking-head manipulation of public figures, motivated by concerns about large-scale misinformation and video-evidence fraud. This position paper argues that the threat the field prepared for did not arrive, and the threats that did arrive are substantially different. An accounting of deepfake incidents in 2022--2026 shows that the dominant observed harms are peer-generated Non-Consensual Intimate Imagery (NCII), voice-clone scam calls targeting families and finance workers, and emotional-manipulation fraud. The predicted large-scale public-figure deepfake catastrophe did not materialize during the 2024 global information environment despite extensive preparation. Meanwhile, research effort, benchmarks, and detection methods remain concentrated on the inherited threat model. The central claim of this paper is that this misalignment is now the dominant bottleneck on real-world deepfake defense, not model capability. We argue the ML research community should substantially rebalance its research agenda toward the harm categories that are actually growing. We support this position with empirical accounting of research effort and harm distribution, identify the structural reasons the misalignment persists, and outline three concrete technical research agendas for the under-defended harm categories.

</details>

#### [AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling](https://arxiv.org/abs/2605.11866)
**Yiming Ren, Xuenan Xu, Ziyang Zhang, Wen Wu et al.** · 2026-05-12

<details>
<summary>Abstract</summary>

Despite advances in text and visual generation, creating coherent long-form audio narratives remains challenging. Existing frameworks often exhibit limitations such as mismatched character settings with voice performance, insufficient self-correction mechanisms, and limited human interactivity. To address these challenges, we propose AuDirector, a self-reflective closed-loop multi-agent framework. Specifically, it involves an Identity-Aware Pre-production mechanism that transforms narrative texts into character profiles and utterance-level emotional instructions to retrieve suitable voice candidates and guide expressive speech synthesis, thereby promoting context-aligned voice adaptation. To enhance quality, a Collaborative Synthesis and Correction module introduces a closed-loop self-correction mechanism to systematically audit and regenerate defective audio components. Furthermore, a Human-Guided Interactive Refinement module facilitates user control by interpreting natural language feedback to interactively refine the underlying scripts. Experiments demonstrate that AuDirector achieves superior performance compared to state-of-the-art baselines in structural coherence, emotional expressiveness, and acoustic fidelity. Audio samples can be found at https://anonymous-itsh.github.io/.

</details>

#### [AffectCodec: Emotion-Preserving Neural Speech Codec for Expressive Speech Modeling](https://arxiv.org/abs/2605.11098)
**Jiacheng Shi, Hongfei Du, Xinyuan Song, Y. Alicia Hong et al.** · 2026-05-11

<details>
<summary>Abstract</summary>

Neural speech codecs provide discrete representations for speech language models, but emotional cues are often degraded during quantization. Existing codecs mainly optimize acoustic reconstruction, leaving emotion expressiveness insufficiently modeled at the representation level. We propose an emotion-guided neural speech codec that explicitly preserves emotional information while maintaining semantic fidelity and prosodic naturalness. Our framework combines emotion-semantic guided latent modulation, relation-preserving emotional-semantic distillation, and emotion-weighted semantic alignment to retain emotionally salient cues under compression. Extensive evaluations across speech reconstruction, emotion recognition, and downstream text-to-speech generation demonstrate improved emotion consistency and perceptual quality without sacrificing content accuracy.

</details>

#### [Kinetic-Optimal Scheduling with Moment Correction for Metric-Induced Discrete Flow Matching in Zero-Shot Text-to-Speech](https://arxiv.org/abs/2605.09386)
**Dong Yang, Yiyi Cai, Haoyu Zhang, Yuki Saito et al.** · 2026-05-10

<details>
<summary>Abstract</summary>

Metric-induced discrete flow matching (MI-DFM) exploits token-latent geometry for discrete generation, but its practical use is limited by two issues: heuristic schedulers requiring hyperparameter search, and finite-step path-tracking error from its first-order continuous-time Markov chain (CTMC) solver. We address both issues. First, we derive a kinetic-optimal scheduler for prescribed scalar-parameterized probability paths, and instantiate it for MI-DFM as a training-free numerical schedule that traverses the path at constant Fisher-Rao speed. Second, we introduce a finite-step moment correction that adjusts the jump probability while preserving the CTMC jump destination distribution. We validate the resulting method, GibbsTTS, on codec-based zero-shot text-to-speech (TTS). Under controlled comparisons with a unified architecture and large-scale dataset, GibbsTTS achieves the best objective naturalness and is preferred in subjective evaluations over masked discrete generative baselines. Additionally, in comparison with the evaluated state-of-the-art TTS systems, GibbsTTS shows strong speaker similarity, achieving the highest similarity on three of four test sets and ranking second on the fourth. Project page: https://ydqmkkx.github.io/GibbsTTSProject

</details>

#### [Minimizing Modality Gap from the Input Side: Your Speech LLM Can Be a Prosody-Aware Text LLM](https://arxiv.org/abs/2605.05927)
**Wenqian Cui, Xiao-Hui Li, Daxin Tan, Qiyong Zheng et al.** · 2026-05-07

<details>
<summary>Abstract</summary>

Speech large language models (SLMs) are typically built from text large language model (TLM) checkpoints, yet they still suffer from a substantial modality gap. Prior work has mainly attempted to reduce this gap from the output side by making speech generation more text-like, but the gap remains. We argue that the key remaining bottleneck lies on the input side. We propose TextPro-SLM, an SLM that makes spoken input more closely resemble that of a prosody-aware text LLM. TextPro-SLM combines WhisperPro, a unified speech encoder that produces synchronized text tokens and prosody embeddings, with an LLM backbone trained to preserve the semantic capabilities of the original TLM while learning paralinguistic understanding. Experiments show that TextPro-SLM achieves the lowest modality gap among leading SLMs at both 3B and 7B scales, while also delivering strong overall performance on paralinguistic understanding tasks. These gains are achieved with only roughly 1,000 hours of LLM training audio, suggesting that reducing the modality gap from the input side is both effective and data-efficient.

</details>

#### [Tibetan-TTS:Low-Resource Tibetan Speech Synthesis with Large Model Adaptation](https://arxiv.org/abs/2605.02496)
**Jiaxu He, Chao Wang, Jie Lian, Yuqing Cai et al.** · 2026-05-04

<details>
<summary>Abstract</summary>

Tibetan text-to-speech (TTS) has long been challenged by scarce speech resources, significant dialectal variation, and the complex mapping between written text and spoken pronunciation. To address these issues, this work presents, to the best of our knowledge, the first large-model-based Tibetan TTS system in the industry, built upon a large speech synthesis model developed by Xingchen AGI Lab. The proposed system integrates data quality enhancement, Tibetan-oriented text representation and tokenizer adaptation, and cross-lingual adaptive training for low-resource Tibetan speech synthesis. Experimental results show that the system can generate stable, natural, and intelligible Tibetan speech under low-resource conditions. In subjective evaluation, the MOS scores of the syllable-level and BPE-based systems reach 4.28 and 4.35, while their pronunciation accuracies reach 97.6% and 96.6%, respectively, outperforming an external commercial Tibetan TTS interface. These results demonstrate that combining a large-model backbone with Tibetan-oriented text representation adaptation and cross-lingual adaptive training enables highly usable low-resource Tibetan speech synthesis, and also provides a technical foundation for future unified multi-dialect Tibetan speech synthesis.

</details>

#### [Toward Fine-Grained Speech Inpainting Forensics:A Dataset, Method, and Metric for Multi-Region Tampering Localization](https://arxiv.org/abs/2605.02223)
**Tung Vu, Yen Nguyen, Hai Nguyen, Cuong Pham et al.** · 2026-05-04

<details>
<summary>Abstract</summary>

Recent advances in voice cloning and text-to-speech synthesis have made partial speech manipulation - where an adversary replaces a few words within an utterance to alter its meaning while preserving the speaker's identity - an increasingly realistic threat. Existing audio deepfake detection benchmarks focus on utterance-level binary classification or single-region tampering, leaving a critical gap in detecting and localizing multiple inpainted segments whose count is unknown a priori. We address this gap with three contributions. First, we introduce MIST (Multiregion Inpainting Speech Tampering), a large-scale multilingual dataset spanning 6 languages with 1-3 independently inpainted word-level segments per utterance, generated via LLM-guided semantic replacement and neural voice cloning, with fake content constituting only 2-7% of each utterance. Second, we propose ISA (Iterative Segment Analysis), a backbone-agnostic framework that performs coarse-to-fine sliding-window classification with gap-tolerant region proposal and boundary refinement to recover all tampered regions without prior knowledge of their count. Third, we define SF1@tau, a segment-level F1 metric based on temporal IoU matching that jointly evaluates region count accuracy and localization precision. Zero-shot evaluation reveals that partial inpainting at word granularity remains unsolved by existing deepfake detectors: utterance-level classifiers trained on fully synthesized speech assign near zero fake probability to MIST utterances where only 2-7% of content is manipulated. ISA consistently outperforms non-iterative baselines in this challenging setting, and the dataset, code, and evaluation toolkit are publicly released.

</details>

#### [Beyond Decodability: Reconstructing Language Model Representations with an Encoding Probe](https://arxiv.org/abs/2605.00607)
**Gaofei Shen, Martijn Bentum, Tom Lentz, Afra Alishahi et al.** · 2026-05-01

<details>
<summary>Abstract</summary>

Probing is widely used to study which features can be decoded from language model representations. However, the common decoding probe approach has two limitations that we aim to solve with our new encoding probe approach: contributions of different features to model representations cannot be directly compared, and feature correlations can affect probing results. We present an Encoding Probe that reverses this direction and reconstructs internal representations of models using interpretable features. We evaluate this method on text and speech transformer models, using feature sets spanning acoustics, phonetics, syntax, lexicon, and speaker identity. Our results suggest that speaker-related effects vary strongly across different training objectives and datasets, while syntactic and lexical features contribute independently to reconstruction. These results show that the Encoding Probe provides a complementary perspective on interpreting model representations beyond decodability.

</details>

#### [LASE: Language-Adversarial Speaker Encoding for Indic Cross-Script Identity Preservation](https://arxiv.org/abs/2605.00777)
**Venkata Pushpak Teja Menta** · 2026-05-01

<details>
<summary>Abstract</summary>

A speaker encoder used in multilingual voice cloning should treat the same speaker identically regardless of which script the audio was uttered in. Off-the-shelf encoders do not, and the failure is accent-conditional. On a 1043-pair Western-accented voice corpus across English, Hindi, Telugu, and Tamil, WavLM-base-plus-sv loses 0.082 absolute cosine similarity when the same voice changes script and ECAPA-TDNN loses 0.105. On a 1369-pair Indian-accented voice corpus, the gap shrinks to 0.006 (WavLM-SV) and 0.044 (ECAPA-TDNN). The leak is largest where it matters most for cross-script TTS: when a system projects a non-Indic-trained voice into Indic scripts. We present LASE (Language-Adversarial Speaker Encoder), a small projection head over frozen WavLM-base-plus trained with two losses: a supervised contrastive loss over voice identity, and a gradient-reversal cross-entropy against a 4-language classifier that pushes the embedding to be language-uninformative while remaining speaker-informative. Trained on 1118 quality-gated cross-script pairs synthesised from 8 commercial multilingual voices, LASE's residual gap is consistent with zero on both corpora (Delta = 0.013 Western, Delta = 0.026 Indian; both bootstrap 95% CIs include zero) and amplifies the cross-script-vs-floor margin 2.4-2.7x over both baselines. An ECAPA+GRL ablation shows the GRL objective improves either backbone but the WavLM choice contributes too. In synthetic multi-speaker diarisation, LASE matches ECAPA-TDNN on cross-script speaker recall (0.788 vs 0.789) with ~100x less training data. We release the r1 checkpoint, both corpora, and the bootstrap recipe.

</details>

#### [JaiTTS: A Thai Voice Cloning Model](https://arxiv.org/abs/2604.27607)
**Jullajak Karnjanaekarin, Pontakorn Trakuekul, Narongkorn Panitsrisit, Sumana Sumanakul et al.** · 2026-04-30

<details>
<summary>Abstract</summary>

We present JaiTTS-v1.0, a state-of-the-art Thai voice cloning text-to-speech model built through continual training on a large Thai-centric speech corpus. The model architecture is adapted from VoxCPM, a tokenizer-free autoregressive TTS model. JaiTTS-v1.0 directly processes numerals and Thai-English code-switching, which is very common in realistic settings, without explicit text normalization. We test the models on short-duration speech generation and long-duration speech generation, which reflects many real-world use cases. JaiTTS-v1.0 achieves a state-of-the-art CER of 1.94\%, surpassing the human ground truth of 1.98% for short-duration tasks while performing on par with human ground truth for long-duration tasks. In human judgment evaluations, our model wins 283 of 400 pairwise comparisons against commercial flagships, with only 58 losses.

</details>

#### [MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction](https://arxiv.org/abs/2604.27393)
**Junbo Cui, Bokai Xu, Chongyi Wang, Tianyu Yu et al.** · 2026-04-30

<details>
<summary>Abstract</summary>

Recent progress in multimodal large language models (MLLMs) has brought AI capabilities from static offline data processing to real-time streaming interaction, yet they still remain far from human-level multimodal interaction. The key bottlenecks are no longer modality coverage or latency alone, but the interaction paradigm itself. First, perception and response are still separated into alternating phases, preventing models from incorporating new inputs for timely adjustment during generation. Second, most current models remain reactive, responding only to explicit user requests instead of acting proactively in the evolving multimodal environment. We present MiniCPM-o 4.5, our latest effort towards human-like multimodal interaction, which mitigates these gaps by real-time full-duplex omni-modal interaction. It can see, listen, and speak simultaneously in real-time, while also exhibiting proactive behaviors such as issuing reminders or comments based on its continuous understanding of the live scene. The key technique behind MiniCPM-o 4.5 is Omni-Flow, a unified streaming framework that aligns omni-modal inputs and outputs along a shared temporal axis. This formulation converts conventional turn-based interaction into a full-duplex, time-aligned process, enabling simultaneous perception and response and allowing proactive behavior to arise within the same framework. With a total of 9B parameters, MiniCPM-o 4.5 approaches Gemini 2.5 Flash in vision-language capabilities, delivering state-of-the-art open-source performance at its scale. It also surpasses Qwen3-Omni-30B-A3B in omni-modal understanding and delivers better speech generation, with significantly higher computation efficiency. Driven by its efficient architecture design and inference optimization, the model can perform real-time full-duplex omni-modal interaction on edge devices with less than 12GB RAM cost.

</details>

#### [Targeted Linguistic Analysis of Sign Language Models with Minimal Translation Pairs](https://arxiv.org/abs/2604.27232)
**Serpil Karabüklü, Kanishka Misra, Shester Gueuwou, Diane Brentari et al.** · 2026-04-29

<details>
<summary>Abstract</summary>

Models of sign language have historically lagged behind those for spoken language (text and speech). Recent work has greatly improved their performance on tasks like sign language translation and isolated sign recognition. However, it remains unclear to what extent existing models capture various linguistic phenomena of sign language, and how well they use cues from the multiple articulators used in sign language (hands, upper body, face). We introduce a new benchmark dataset for American Sign Language, ASL Minimal Translation Pairs (ASL-MTP), divided into multiple types of sign language phenomena and corresponding minimal pairs of translations, for performing such linguistic analyses. As a case study, we use ASL-MTP to analyze a state-of-the-art ASL-to-English translation model. We conduct a targeted analysis of the model by ablating various input cues during training and inference and evaluating on the phenomena in ASL-MTP. Our results show that, while the model performs above chance level on most of the phenomena, it relies strongly on manual cues while often missing crucial non-manual cues.

</details>

#### [EmoTransCap: Dataset and Pipeline for Emotion Transition-Aware Speech Captioning in Discourses](https://arxiv.org/abs/2604.26417)
**Shuhao Xu, Yifan Hu, Jingjing Wu, Zhihao Du et al.** · 2026-04-29

<details>
<summary>Abstract</summary>

Emotion perception and adaptive expression are fundamental capabilities in human-agent interaction. While recent advances in speech emotion captioning (SEC) have improved fine-grained emotional modeling, existing systems remain limited to static, single-emotion characterization within isolated sentences, neglecting dynamic emotional transitions at the discourse level. To address this gap, we propose Emotion Transition-Aware Speech Captioning (EmoTransCap), a paradigm that integrates temporal emotion dynamics with discourse-level speech description. To construct a dataset rich in emotion transitions while enabling scalable expansion, we design an automated pipeline for dataset creation. This is the first large-scale dataset explicitly designed to capture discourse-level emotion transitions. To generate semantically rich descriptions, we incorporate acoustic attributes and temporal cues from discourse-level speech. Our Multi-Task Emotion Transition Recognition (MTETR) model performs joint emotion transition detection and diarization. Leveraging the semantic analysis capabilities of LLMs, we produce two annotation versions: descriptive and instruction-oriented. These data and annotations offer a valuable resource for advancing emotion perception and emotional expressiveness. The dataset enables speech captions that capture emotional transitions, facilitating temporal-dynamic and fine-grained emotion understanding. We also introduce a controllable, transition-aware emotional speech synthesis system at the discourse level, enhancing anthropomorphic emotional expressiveness and supporting emotionally intelligent conversational agents.

</details>

#### [The False Resonance: A Critical Examination of Emotion Embedding Similarity for Speech Generation Evaluation](https://arxiv.org/abs/2604.26347)
**Yun-Shao Tsai, Yi-Cheng Lin, Huang-Cheng Chou, Tzu-Wen Hsu et al.** · 2026-04-29

<details>
<summary>Abstract</summary>

Objective metrics for emotional expressiveness are vital for speech generation, particularly in expressive synthesis and voice conversion requiring emotional prosody transfer. To quantify this, the field widely relies on emotion similarity between reference and generated samples. This approach computes cosine similarity of embeddings from encoders like emotion2vec, assuming they capture affective cues despite linguistic and speaker variations. We challenge this assumption through controlled adversarial tasks and human alignment tests. Despite high classification accuracy, these latent spaces are unsuitable for zero-shot similarity evaluation. Representational limitations cause linguistic and speaker interference to overshadow emotional features, degrading discriminative ability. Consequently, the metric misaligns with human perception. This acoustic vulnerability reveals it rewards acoustic mimicry over genuine emotional synthesis.

</details>

#### [PSP: An Interpretable Per-Dimension Accent Benchmark for Indic Text-to-Speech](https://arxiv.org/abs/2604.25476)
**Venkata Pushpak Teja Menta** · 2026-04-28

<details>
<summary>Abstract</summary>

Standard text-to-speech (TTS) evaluation measures intelligibility (WER, CER) and overall naturalness (MOS, UTMOS) but does not quantify accent. A synthesiser may score well on all four yet sound non-native on features that are phonemic in the target language. For Indic languages, these features include retroflex articulation, aspiration, vowel length, and the Tamil retroflex approximant (letter zha). We present PSP, the Phoneme Substitution Profile, an interpretable, per-phonological-dimension accent benchmark for Indic TTS. PSP decomposes accent into six complementary dimensions: retroflex collapse rate (RR), aspiration fidelity (AF), vowel-length fidelity (LF), Tamil-zha fidelity (ZF), Frechet Audio Distance (FAD), and prosodic signature divergence (PSD). The first four are measured via forced alignment plus native-speaker-centroid acoustic probes over Wav2Vec2-XLS-R layer-9 embeddings; the latter two are corpus-level distributional distances. In this v1 we benchmark four commercial and open-source systems (ElevenLabs v3, Cartesia Sonic-3, Sarvam Bulbul, Indic Parler-TTS) on Hindi, Telugu, and Tamil pilot sets, with a fifth system (Praxy Voice) included on all three languages, plus an R5->R6 case study on Telugu. Three findings: (i) retroflex collapse grows monotonically with phonological difficulty Hindi < Telugu < Tamil (~1%, ~40%, ~68%); (ii) PSP ordering diverges from WER ordering -- commercial WER-leaders do not uniformly lead on retroflex or prosodic fidelity; (iii) no single system is Pareto-optimal across all six dimensions. We release native reference centroids (500 clips per language), 1000-clip embeddings for FAD, 500-clip prosodic feature matrices for PSD, 300-utterance golden sets per language, scoring code under MIT, and centroids under CC-BY. Formal MOS-correlation is deferred to v2; v1 reports five internal-consistency signals plus a native-audio sanity check.

</details>

#### [Robust Accent Identification via Voice Conversion and Non-Timbral Embeddings](https://arxiv.org/abs/2604.25332)
**Rayane Bakari, Olivier Le Blouch, Nicolas Gengembre, Nicholas Evans** · 2026-04-28

<details>
<summary>Abstract</summary>

Automatic accent identification (AID) remains a challenging task due to the complex variability of accents, the entanglement of accent cues with speaker traits, and the scarcity of reliable accentlabelled data. To address these challenges, we propose a speaker augmentation strategy using voice conversion (VC), with which we generate additional training data by converting original training utterances into different speaker voices while preserving accentual cues. For this purpose, we select two recent VC systems and evaluate their capability to preserve accent. Alternatively, we also explore the use of non-timbral embeddings in AID, for their ability to convey accent information among other non timbral cues. The effectiveness of both methods is demonstrated on the GenAID benchmark, achieving a new state-of-the-art F1-score of 0.66, compared to the previous score of 0.55. Beyond AID, we show that non-timbral embeddings enable accent-controlled Text-to-Speech, producing high-fidelity speech with accurate accent transfer.

</details>

#### [One Voice, Many Tongues: Cross-Lingual Voice Cloning for Scientific Speech](https://arxiv.org/abs/2604.26136)
**Amanuel Gizachew Abebe, Yasmin Moslem** · 2026-04-28

<details>
<summary>Abstract</summary>

Preserving a speaker's voice identity while generating speech in a different language remains a fundamental challenge in spoken language technology, particularly in specialized domains such as scientific communication. In this paper, we address this challenge through our system submission to the International Conference on Spoken Language Translation (IWSLT 2026), the Cross-Lingual Voice Cloning shared task. First, we evaluate several state-of-the-art voice cloning models for cross-lingual speech generation of scientific texts in Arabic, Chinese, and French. Then, we build voice cloning systems based on the OmniVoice foundation model. We employ data augmentation via multi-model ensemble distillation from the ACL 60/60 corpus. We investigate the effect of using this synthetic data for fine-tuning, demonstrating consistent improvements in intelligibility (WER and CER) across languages while preserving speaker similarity.

</details>

#### [AMAVA: Adaptive Motion-Aware Video-to-Audio Framework for Visually-Impaired Assistance](https://arxiv.org/abs/2604.23909)
**Benjamin Klein, Kazi Ruslan Rahman, Sanchita Ghose** · 2026-04-26

<details>
<summary>Abstract</summary>

Navigational aids for blind and low vision individuals struggle conveying dynamic real-world environments, leading to cognitive overload from continuous, undifferentiated feedback. We present AMAVA, a novel real-time video-to-audio framework that converts mobile device video into contextually relevant sound effects or text-to-speech descriptions. We propose a motion-aware pipeline using a lightweight AI classification model to distinguish between low and high-movement scenes followed by a real-time text-to-audio synthesis pipeline to enhance environmental perception more efficiently. In static environments, AMAVA generates spoken audio scene descriptions for situational awareness. In high-movement situations, it prioritizes safety by delivering sound cues, such as spoken hazard alerts and environmental sound effects. These audio outputs are produced by a decoder-only transformer-based vision-language model with mixture-of-experts and cross-modal attention for visual understanding, in conjunction with neural text-to-speech and natural sound synthesis networks. The proposed framework uses prompt-based caching and category-specific throttling to avoid auditory clutter and minimize latency. We present a comprehensive evaluation of the system, including a real-time navigation study comparing a white cane alone versus with AMAVA, that shows a significant increase in user confidence and perceived safety.

</details>

#### [Talking Slide Avatars: Open-Source Multimodal Communication Approach for Teaching](https://arxiv.org/abs/2604.23703)
**Xinxing Wu** · 2026-04-26

<details>
<summary>Abstract</summary>

Slide-based teaching is widely used in higher education, yet in online, hybrid, and asynchronous contexts, slides often lose the instructor presence, narrative continuity, and expressive framing that help learners connect with content. Full lecture video can partly restore these qualities, but it is time-consuming to record, revise, and reuse. This study addresses that pedagogical and production challenge by presenting a practice-based analysis of an open-source workflow for creating talking slide avatars for slide-based teaching. The workflow integrates OpenVoice for text-to-speech generation and voice cloning with Ditto-TalkingHead for audio-driven talking-image synthesis, enabling instructors to transform a script and a static portrait into a short narrated video that can be embedded in slide decks or HTML-based lecture materials. Rather than treating this workflow merely as a technical solution, the study frames talking slide avatars as multimodal communication artifacts at the intersection of digital pedagogy, aesthetic education, and art-technology practice. Using a practice-based implementation and analytic reflection approach, the study documents the production pipeline, examines its communicative and aesthetic affordances, and proposes practical guidelines for script length, image selection, pacing, disclosure, accessibility, and ethical use. The study makes three primary contributions: it presents an educator-oriented open-source production model, reframes talking avatars as an educational communication design problem, and proposes a responsible pathway for incorporating generative synthetic media into teaching. It concludes that short, transparent, and carefully designed avatars can humanize slide-based instruction while providing a reusable communicative layer for introductions, transitions, reminders, and recaps across online, hybrid, and asynchronous learning environments.

</details>

#### [RTCFake: Speech Deepfake Detection in Real-Time Communication](https://arxiv.org/abs/2604.23742)
**Jun Xue, Zhuolin Yi, Yihuan Huang, Yanzhen Ren et al.** · 2026-04-26

<details>
<summary>Abstract</summary>

With the rapid advancement of speech generation technologies, the threat posed by speech deepfakes in real-time communication (RTC) scenarios has intensified. However, existing detection studies mainly focus on offline simulations and struggle to cope with the complex distortions introduced during RTC transmission, including unknown speech enhancement processes (e.g., noise suppression) and codec compression. To address this challenge, we present the first large-scale speech deepfake dataset tailored for RTC scenarios, termed \textit{RTCFake}, totaling approximately 600 hours. The dataset is constructed by transmitting speech through multiple mainstream social media and conferencing platforms (e.g., Zoom), enabling precise pairing between offline and online speech. In addition, we propose a phoneme-guided consistency learning (PCL) strategy that enforces models to learn platform-invariant semantic structural representations. In this paper, the RTCFake dataset is divided into training, development, and evaluation sets. The evaluation set further includes both unseen RTC platforms and unseen complex noise conditions, thereby providing a more realistic and challenging evaluation benchmark for speech deepfake detection. Furthermore, the proposed PCL strategy achieves significant improvements in both cross-platform generalization and noise robustness, offering an effective and generalizable modeling paradigm. The \textit{RTCFake} dataset is provided in the {https://huggingface.co/datasets/JunXueTech/RTCFake}.

</details>

#### [TTS-PRISM: A Perceptual Reasoning and Interpretable Speech Model for Fine-Grained Diagnosis](https://arxiv.org/abs/2604.22225)
**Xi Wang, Jie Wang, Xingchen Song, Baijun Song et al.** · 2026-04-24

<details>
<summary>Abstract</summary>

While generative text-to-speech (TTS) models approach human-level quality, monolithic metrics fail to diagnose fine-grained acoustic artifacts or explain perceptual collapse. To address this, we propose TTS-PRISM, a multi-dimensional diagnostic framework for Mandarin. First, we establish a 12-dimensional schema spanning stability to advanced expressiveness. Second, we design a targeted synthesis pipeline with adversarial perturbations and expert anchors to build a high-quality diagnostic dataset. Third, schema-driven instruction tuning embeds explicit scoring criteria and reasoning into an efficient end-to-end model. Experiments on a 1,600-sample Gold Test Set show TTS-PRISM outperforms generalist models in human alignment. Profiling six TTS paradigms establishes intuitive diagnostic flags that reveal fine-grained capability differences. TTS-PRISM is open-source, with code and checkpoints at https://github.com/xiaomi-research/tts-prism.

</details>

#### [UniSonate: A Unified Model for Speech, Music, and Sound Effect Generation with Text Instructions](https://arxiv.org/abs/2604.22209)
**Chunyu Qiang, Xiaopeng Wang, Kang Yin, Yuzhe Liang et al.** · 2026-04-24

<details>
<summary>Abstract</summary>

Generative audio modeling has largely been fragmented into specialized tasks, text-to-speech (TTS), text-to-music (TTM), and text-to-audio (TTA), each operating under heterogeneous control paradigms. Unifying these modalities remains a fundamental challenge due to the intrinsic dissonance between structured semantic representations (speech/music) and unstructured acoustic textures (sound effects). In this paper, we introduce UniSonate, a unified flow-matching framework capable of synthesizing speech, music, and sound effects through a standardized, reference-free natural language instruction interface. To reconcile structural disparities, we propose a novel dynamic token injection mechanism that projects unstructured environmental sounds into a structured temporal latent space, enabling precise duration control within a phoneme-driven Multimodal Diffusion Transformer (MM-DiT). Coupled with a multi-stage curriculum learning strategy, this approach effectively mitigates cross-modal optimization conflicts. Extensive experiments demonstrate that UniSonate achieves state-of-the-art performance in instruction-based TTS (WER 1.47%) and TTM (SongEval Coherence 3.18), while maintaining competitive fidelity in TTA. Crucially, we observe positive transfer, where joint training on diverse audio data significantly enhances structural coherence and prosodic expressiveness compared to single-task baselines. Audio samples are available at https://qiangchunyu.github.io/UniSonate/.

</details>

#### [Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages](https://arxiv.org/abs/2604.21481)
**Srija Anand, Ashwin Sankar, Ishvinder Sethi, Aaditya Pareek et al.** · 2026-04-23

<details>
<summary>Abstract</summary>

Crowdsourced pairwise evaluation has emerged as a scalable approach for assessing foundation models. However, applying it to Text to Speech(TTS) introduces high variance due to linguistic diversity and multidimensional nature of speech perception. We present a controlled multidimensional pairwise evaluation framework for multilingual TTS that combines linguistic control with perceptually grounded annotation. Using 5K+ native and code-mixed sentences across 10 Indic languages, we evaluate 7 state-of-the-art TTS systems and collect over 120K pairwise comparisons from over 1900 native raters. In addition to overall preference, raters provide judgments across 6 perceptual dimensions: intelligibility, expressiveness, voice quality, liveliness, noise, and hallucinations. Using Bradley-Terry modeling, we construct a multilingual leaderboard, interpret human preference using SHAP analysis and analyze leaderboard reliability alongside model strengths and trade-offs across perceptual dimensions.

</details>

#### [MAGIC-TTS: Fine-Grained Controllable Speech Synthesis with Explicit Local Duration and Pause Control](https://arxiv.org/abs/2604.21164)
**Jialong Mai, Xiaofen Xing, Xiangmin Xu** · 2026-04-23

<details>
<summary>Abstract</summary>

Fine-grained local timing control is still absent from modern text-to-speech systems: existing approaches typically provide only utterance-level duration or global speaking-rate control, while precise token-level timing manipulation remains unavailable. To the best of our knowledge, MAGIC-TTS is the first TTS model with explicit local timing control over token-level content duration and pause. MAGIC-TTS is enabled by explicit token-level duration conditioning, carefully prepared high-confidence duration supervision, and training mechanisms that correct zero-value bias and make the model robust to missing local controls. On our timing-control benchmark, MAGIC-TTS substantially improves token-level duration and pause following over spontaneous synthesis. Even when no timing control is provided, MAGIC-TTS maintains natural high-quality synthesis. We further evaluate practical local editing with a scenario-based benchmark covering navigation guidance, guided reading, and accessibility-oriented code reading. In this setting, MAGIC-TTS realizes a reproducible uniform-timing baseline and then moves the edited regions toward the requested local targets with low mean bias. These results show that explicit fine-grained controllability can be implemented effectively in a high-quality TTS system and can support realistic local timing-editing applications.

</details>

#### [SpeechParaling-Bench: A Comprehensive Benchmark for Paralinguistic-Aware Speech Generation](https://arxiv.org/abs/2604.20842)
**Ruohan Liu, Shukang Yin, Tao Wang, Dong Zhang et al.** · 2026-04-22

<details>
<summary>Abstract</summary>

Paralinguistic cues are essential for natural human-computer interaction, yet their evaluation in Large Audio-Language Models (LALMs) remains limited by coarse feature coverage and the inherent subjectivity of assessment. To address these challenges, we introduce SpeechParaling-Bench, a comprehensive benchmark for paralinguistic-aware speech generation. It expands existing coverage from fewer than 50 to over 100 fine-grained features, supported by more than 1,000 English-Chinese parallel speech queries, and is organized into three progressively challenging tasks: fine-grained control, intra-utterance variation, and context-aware adaptation. To enable reliable evaluation, we further develop a pairwise comparison pipeline, in which candidate responses are evaluated against a fixed baseline by an LALM-based judge. By framing evaluation as relative preference rather than absolute scoring, this approach mitigates subjectivity and yields more stable and scalable assessments without costly human annotation. Extensive experiments reveal substantial limitations in current LALMs. Even leading proprietary models struggle with comprehensive static control and dynamic modulation of paralinguistic features, while failure to correctly interpret paralinguistic cues accounts for 43.3% of errors in situational dialogue. These findings underscore the need for more robust paralinguistic modeling toward human-aligned voice assistants.

</details>

#### [Text-To-Speech with Chain-of-Details: modeling temporal dynamics in speech generation](https://arxiv.org/abs/2604.19330)
**Jianbo Ma, Richard Cartwright** · 2026-04-21

<details>
<summary>Abstract</summary>

Recent advances in Text-To-Speech (TTS) synthesis have seen the popularity of multi-stage approaches that first predict semantic tokens and then generate acoustic tokens. In this paper, we extend the coarse-to-fine generation paradigm to the temporal domain and introduce Chain-of-Details (CoD), a novel framework that explicitly models temporal coarse-to-fine dynamics in speech generation using a cascaded architecture. Our method progressively refines temporal details across multiple stages, with each stage targeting a specific temporal granularity. All temporal detail predictions are performed using a shared decoder, enabling efficient parameter utilization across different temporal resolutions. Notably, we observe that the lowest detail level naturally performs phonetic planning without the need for an explicit phoneme duration predictor. We evaluate our method on several datasets and compare it against several baselines. Experimental results show that CoD achieves competitive performance with significantly fewer parameters than existing approaches. Our findings demonstrate that explicit modeling of temporal dynamics with the CoD framework leads to more natural speech synthesis.

</details>

#### [MINT-Bench: A Comprehensive Multilingual Benchmark for Instruction-Following Text-to-Speech](https://arxiv.org/abs/2604.17958)
**Huakang Chen, Jingbin Hu, Liumeng Xue, Qirui Zhan et al.** · 2026-04-20

<details>
<summary>Abstract</summary>

Instruction-following text-to-speech (TTS) has emerged as an important capability for controllable and expressive speech generation, yet its evaluation remains underdeveloped due to limited benchmark coverage, weak diagnostic granularity, and insufficient multilingual support. We present \textbf{MINT-Bench}, a comprehensive multilingual benchmark for instruction-following TTS. MINT-Bench is built upon a hierarchical multi-axis taxonomy, a scalable multi-stage data construction pipeline, and a hierarchical hybrid evaluation protocol that jointly assesses content consistency, instruction following, and perceptual quality. Experiments across ten languages show that current systems remain far from solved: frontier commercial systems lead overall, while leading open-source models become highly competitive and can even outperform commercial counterparts in localized settings such as Chinese. The benchmark further reveals that harder compositional and paralinguistic controls remain major bottlenecks for current systems. We release MINT-Bench together with the data construction and evaluation toolkit to support future research on controllable, multilingual, and diagnostically grounded TTS evaluation. The leaderboard and demo are available at https://longwaytog0.github.io/MINT-Bench/

</details>

#### [HCFD: A Benchmark for Audio Deepfake Detection in Healthcare](https://arxiv.org/abs/2604.17642)
**Mohd Mujtaba Akhtar, Girish, Muskaan Singh** · 2026-04-19

<details>
<summary>Abstract</summary>

In this study, we present Healthcare Codec-Fake Detection (HCFD), a new task for detecting codec-fakes under pathological speech conditions. We intentionally focus on codec based synthetic speech in this work, since neural codec decoding forms a core building block in modern speech generation pipelines. First, we release Healthcare CodecFake, the first pathology-aware dataset containing paired real and NAC-synthesized speech across multipl clinical conditions and codec families. Our evaluations show that SOTA codec-fake detectors trained primarily on healthy speech perform poorly on Healthcare CodecFake, highlighting the need for HCFD-specific models. Second, we demonstrate that PaSST outperforms existing speech-based models for HCFD, benefiting from its patch-based spectro-temporal representation. Finally, we propose PHOENIX-Mamba, a geometry-aware framework that models codec-fakes as multiple self-discovered modes in hyperbolic space and achieves the strongest performance on HCFD across clinical conditions and codecs. Experiments on HCFK show that PHOENIX-Mamba (PaSST) achieves the best overall performance, reaching 97.04 Acc on E-Dep, 96.73 on E-Alz, and 96.57 on E-Dys, while maintaining strong results on Chinese with 94.41 (Dep), 94.40 (Alz), and 93.20 (Dys). This geometry-aware formulation enables self-discovered clustering of heterogeneous codec-fake modes in hyperbolic space, facilitating robust discrimination under pathological speech variability. PHOENIX-Mamba achieves topmost performance on the HCFD task across clinical conditions and codecs.

</details>

#### [AST: Adaptive, Seamless, and Training-Free Precise Speech Editing](https://arxiv.org/abs/2604.16056)
**Sihan Lv, Yechen Jin, Zhen Li, Jintao Chen et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Text-based speech editing aims to modify specific segments while preserving speaker identity and acoustic context. Existing methods rely on task-specific training, which incurs high data costs and struggles with temporal fidelity in unedited regions. Meanwhile, adapting Text-to-Speech (TTS) models often faces a trade-off between editing quality and consistency. To address these issues, we propose AST, an Adaptive, Seamless, and Training-free precise speech editing framework. Leveraging a pre-trained autoregressive TTS model, AST introduces Latent Recomposition to selectively stitch preserved source segments with newly synthesized targets. Furthermore, AST extends this latent manipulation to enable precise style editing for specific speech segments. To prevent artifacts at these edit boundaries, the framework incorporates Adaptive Weak Fact Guidance (AWFG). AWFG dynamically modulates a mel-space guidance signal, enforcing structural constraints only where necessary without disrupting the generative manifold. To fill the gap of publicly accessible benchmarks, we introduce LibriSpeech-Edit, a new and larger speech editing dataset. As existing metrics poorly evaluate temporal consistency in unedited regions, we propose Word-level Dynamic Time Warping (WDTW). Extensive experiments demonstrate that AST resolves the controllability-quality trade-off without extra training. Compared to the previous most temporally consistent baseline, AST improves consistency while reducing Word Error Rate by nearly 70%. Moreover, applying AST to a foundation TTS model reduces WDTW by 27%, achieving state-of-the-art speaker preservation and temporal fidelity.

</details>

#### [Qwen3.5-Omni Technical Report](https://arxiv.org/abs/2604.15804)
**Qwen Team** · 2026-04-17

<details>
<summary>Abstract</summary>

In this work, we present Qwen3.5-Omni, the latest advancement in the Qwen-Omni model family. Representing a significant evolution over its predecessor, Qwen3.5-Omni scales to hundreds of billions of parameters and supports a 256k context length. By leveraging a massive dataset comprising heterogeneous text-vision pairs and over 100 million hours of audio-visual content, the model demonstrates robust omni-modality capabilities. Qwen3.5-Omni-plus achieves SOTA results across 215 audio and audio-visual understanding, reasoning, and interaction subtasks and benchmarks, surpassing Gemini-3.1 Pro in key audio tasks and matching it in comprehensive audio-visual understanding. Architecturally, Qwen3.5-Omni employs a Hybrid Attention Mixture-of-Experts (MoE) framework for both Thinker and Talker, enabling efficient long-sequence inference. The model facilitates sophisticated interaction, supporting over 10 hours of audio understanding and 400 seconds of 720P video (at 1 FPS). To address the inherent instability and unnaturalness in streaming speech synthesis, often caused by encoding efficiency discrepancies between text and speech tokenizers, we introduce ARIA. ARIA dynamically aligns text and speech units, significantly enhancing the stability and prosody of conversational speech with minimal latency impact. Furthermore, Qwen3.5-Omni expands linguistic boundaries, supporting multilingual understanding and speech generation across 10 languages with human-like emotional nuance. Finally, Qwen3.5-Omni exhibits superior audio-visual grounding capabilities, generating script-level structured captions with precise temporal synchronization and automated scene segmentation. Remarkably, we observed the emergence of a new capability in omnimodal models: directly performing coding based on audio-visual instructions, which we call Audio-Visual Vibe Coding.

</details>

#### [NVBench: A Benchmark for Speech Synthesis with Non-Verbal Vocalizations](https://arxiv.org/abs/2604.16211)
**Liumeng Xue, Weizhen Bian, Jiahao Pan, Wenxuan Wang et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Non-verbal vocalizations (NVVs) like laugh, sigh, and sob are essential for human-like speech, yet standardized evaluation remains limited in jointly assessing whether systems can generate the intended NVVs, place them correctly, and keep them salient without harming speech. We present Non-verbal Vocalization Benchmark (NVBench), a bilingual (English/Chinese) benchmark that evaluates speech synthesis with NVVs. NVBench pairs a unified 45-type taxonomy with a curated bilingual dataset and introduces a multi-axis protocol that separates general speech naturalness and quality from NVV-specific controllability, placement, and salience. We benchmark 15 TTS systems using objective metrics, listening tests, and an LLM-based multi-rater evaluation. Results reveal that NVVs controllability often decouples from quality, while low-SNR oral cues and long-duration affective NVVs remain persistent bottlenecks. NVBench enables fair cross-system comparison across diverse control interfaces under a unified, standardized framework.

</details>

#### [Hierarchical Codec Diffusion for Video-to-Speech Generation](https://arxiv.org/abs/2604.15923)
**Jiaxin Ye, Gaoxiang Cong, Chenhui Wang, Xin-Cheng Wen et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Video-to-Speech (VTS) generation aims to synthesize speech from a silent video without auditory signals. However, existing VTS methods disregard the hierarchical nature of speech, which spans coarse speaker-aware semantics to fine-grained prosodic details. This oversight hinders direct alignment between visual and speech features at specific hierarchical levels during property matching. In this paper, leveraging the hierarchical structure of Residual Vector Quantization (RVQ)-based codec, we propose HiCoDiT, a novel Hierarchical Codec Diffusion Transformer that exploits the inherent hierarchy of discrete speech tokens to achieve strong audio-visual alignment. Specifically, since lower-level tokens encode coarse speaker-aware semantics and higher-level tokens capture fine-grained prosody, HiCoDiT employs low-level and high-level blocks to generate tokens at different levels. The low-level blocks condition on lip-synchronized motion and facial identity to capture speaker-aware content, while the high-level blocks use facial expression to modulate prosodic dynamics. Finally, to enable more effective coarse-to-fine conditioning, we propose a dual-scale adaptive instance layer normalization that jointly captures global vocal style through channel-wise normalization and local prosody dynamics through temporal-wise normalization. Extensive experiments demonstrate that HiCoDiT outperforms baselines in fidelity and expressiveness, highlighting the potential of discrete modelling for VTS. The code and speech demo are both available at https://github.com/Jiaxin-Ye/HiCoDiT.

</details>

#### [UniPASE: A Generative Model for Universal Speech Enhancement with High Fidelity and Low Hallucinations](https://arxiv.org/abs/2604.14606)
**Xiaobin Rong, Zheng Wang, Yushi Wang, Jun Gao et al.** · 2026-04-16

<details>
<summary>Abstract</summary>

Universal speech enhancement (USE) aims to restore speech signals from diverse distortions across multiple sampling rates. We propose UniPASE, an extension of the low-hallucination PASE framework tailored for USE. At its core is DeWavLM-Omni, a unified representation-level enhancement module fine-tuned from WavLM via knowledge distillation on a large-scale supervised multi-distortion dataset. This module directly converts degraded waveforms into clean and linguistically faithful phonetic representations, ensuring robust enhancement with minimal linguistic hallucination. Based on these enhanced phonetic representations, an Adapter generates enhanced acoustic representations containing rich acoustic details, which a neural Vocoder uses to reconstruct corresponding high-fidelity 16-kHz waveforms. A PostNet then converts the waveforms to 48~kHz before resampling them to their original rates, enabling seamless handling of inputs and outputs at multiple sampling rates. Experimental results on several evaluation datasets, covering sub-tasks and full tasks, demonstrate that UniPASE achieves superior or competitive performance compared with existing state-of-the-art models. The proposed model also serves as the backbone of our submission to the URGENT 2026 Challenge, which achieved 1st place in the objective evaluation. The source code and audio demos are available at https://github.com/xiaobin-rong/unipase/.

</details>

#### [WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training](https://arxiv.org/abs/2604.14932)
**Yifu Chen, Shengpeng Ji, Qian Chen, Tianle Liang et al.** · 2026-04-16

<details>
<summary>Abstract</summary>

End-to-end spoken dialogue models have garnered significant attention because they offer a higher potential ceiling in expressiveness and perceptual ability than cascaded systems. However, the intelligence and expressiveness of current open-source spoken dialogue models often remain below expectations. Motivated by the success of online reinforcement learning(RL) in other domains, one might attempt to directly apply preference optimization to spoken dialogue models, yet this transfer is non-trivial. We analyze these obstacles from the perspectives of reward modeling and rollout sampling, focusing on how sparse preference supervision interacts with dense speech generation under shared-parameter updates. Based on the analysis, we propose a modality-aware adaptive post-training recipe that makes RL practical for spoken dialogue: it constrains preference updates to the semantic channel and improves acoustic behavior via explicit anchoring, while dynamically regulating their mixture from rollout statistics to avoid unreliable preference gradients. We evaluate the method across multiple spoken dialogue benchmarks and representative architectures, and observe consistent improvements in semantic quality and speech expressiveness.

</details>

#### [Giving Voice to the Constitution: Low-Resource Text-to-Speech for Quechua and Spanish Using a Bilingual Legal Corpus](https://arxiv.org/abs/2604.13288)
**John E. Ortega, Rodolfo Zevallos, Fabricio Carraro** · 2026-04-14

<details>
<summary>Abstract</summary>

We present a unified pipeline for synthesizing high-quality Quechua and Spanish speech for the Peruvian Constitution using three state-of-the-art text-to-speech (TTS) architectures: XTTS v2, F5-TTS, and DiFlow-TTS. Our models are trained on independent Spanish and Quechua speech datasets with heterogeneous sizes and recording conditions, and leverage bilingual and multilingual TTS capabilities to improve synthesis quality in both languages. By exploiting cross-lingual transfer, our framework mitigates data scarcity in Quechua while preserving naturalness in Spanish. We release trained checkpoints, inference code, and synthesized audio for each constitutional article, providing a reusable resource for speech technologies in indigenous and multilingual contexts. This work contributes to the development of inclusive TTS systems for political and legal content in low-resource settings.

</details>

#### [An Ultra-Low Latency, End-to-End Streaming Speech Synthesis Architecture via Block-Wise Generation and Depth-Wise Codec Decoding](https://arxiv.org/abs/2604.12438)
**Tianhui Su, Tien-Ping Tan, Salima Mdhaffar, Yannick Estève et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Real-time speech synthesis requires balancing inference latency and acoustic fidelity for interactive applications. Conventional continuous text-to-speech pipelines require computationally intensive neural vocoders to reconstruct phase information, creating a significant streaming bottleneck. Furthermore, regression-based acoustic modeling frequently induces spectral over-smoothing artifacts. To address these limitations, this paper proposes a novel end-to-end non-autoregressive architecture optimized for ultra-low latency block-wise generation, directly modeling the highly compressed discrete latent space of the Mimi neural audio codec. Integrating a modified FastSpeech 2 backbone with a progressive depth-wise sequential decoding strategy, the architecture dynamically conditions 32 layers of residual vector quantization codes. This mechanism resolves phonetic alignment degradation and manages the complexity of high-fidelity discrete representations without temporal autoregressive overhead. Experimental evaluations on English and Malay datasets validate its language-independent deployment capability. Compared to conventional continuous regression models, the proposed architecture demonstrates quantitative improvements in fundamental voicing accuracy and mitigates high-frequency spectral degradation. It achieves ultra-low latency inference, translating to a 10.6-fold absolute acceleration over conventional cascaded pipelines. Crucially, the system achieves an average time-to-first-byte latency of 48.99 milliseconds, falling significantly below the human perception threshold for real-time interactive streaming. These results firmly establish the proposed architecture as a highly optimized solution for deploying real-time streaming speech interfaces.

</details>

#### [X-VC: Zero-shot Streaming Voice Conversion in Codec Space](https://arxiv.org/abs/2604.12456)
**Qixi Zheng, Yuxiang Zhao, Tianrui Wang, Wenxi Chen et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) aims to convert a source utterance into the voice of an unseen target speaker while preserving its linguistic content. Although recent systems have improved conversion quality, building zero-shot VC systems for interactive scenarios remains challenging because high-fidelity speaker transfer and low-latency streaming inference are difficult to achieve simultaneously. In this work, we present X-VC, a zero-shot streaming VC system that performs one-step conversion in the latent space of a pretrained neural codec. X-VC uses a dual-conditioning acoustic converter that jointly models source codec latents and frame-level acoustic conditions derived from target reference speech, while injecting utterance-level target speaker information through adaptive normalization. To reduce the mismatch between training and inference, we train the model with generated paired data and a role-assignment strategy that combines standard, reconstruction, and reversed modes. For streaming inference, we further adopt a chunkwise inference scheme with overlap smoothing that is aligned with the segment-based training paradigm of the codec. Experiments on Seed-TTS-Eval show that X-VC achieves the best streaming WER in both English and Chinese, strong speaker similarity in same-language and cross-lingual settings, and substantially lower offline real-time factor than the compared baselines. These results suggest that codec-space one-step conversion is a practical approach for building high-quality low-latency zero-shot VC systems. Audio samples are available at https://x-vc.github.io. Our code and checkpoints will also be released.

</details>

#### [On the Distillation Loss Functions of Speech VAE for Unified Reconstruction, Understanding, and Generation](https://arxiv.org/abs/2604.12383)
**Changhao Cheng, Wei Wang, Wangyou Zhang, Dongya Jia et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Continuous speech representations based on Variational Autoencoders (VAEs) have emerged as a promising alternative to traditional spectrogram or discrete token based features for speech generation and reconstruction. Recent research has tried to enrich the structural information in VAE latent representations by aligning with self-supervised learning (SSL) features, aiming for better generation performance. However, it remains unclear whether the widely-used alignment approach based on time-axis distillation is optimal when considering more tasks. To address this problem, this paper systematically explores different alignment approaches and analyzes their impact on the performances over three axes: reconstruction, understanding, and generation. We investigate various design choices in the distillation loss. Extensive experiments show that the joint-marginal alignment approach with adaptive weighting can achieve the best overall performance while allowing for a controllable balance.

</details>

#### [CoSyncDiT: Cognitive Synchronous Diffusion Transformer for Movie Dubbing](https://arxiv.org/abs/2604.12292)
**Gaoxiang Cong, Liang Li, Jiaxin Ye, Zhedong Zhang et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Movie dubbing aims to synthesize speech that preserves the vocal identity of a reference audio while synchronizing with the lip movements in a target video. Existing methods fail to achieve precise lip-sync and lack naturalness due to explicit alignment at the duration level. While implicit alignment solutions have emerged, they remain susceptible to interference from the reference audio, triggering timbre and pronunciation degradation in in-the-wild scenarios. In this paper, we propose a novel flow matching-based movie dubbing framework driven by the Cognitive Synchronous Diffusion Transformer (CoSync-DiT), inspired by the cognitive process of professional actors. This architecture progressively guides the noise-to-speech generative trajectory by executing acoustic style adapting, fine-grained visual calibrating, and time-aware context aligning. Furthermore, we design the Joint Semantic and Alignment Regularization (JSAR) mechanism to simultaneously constrain frame-level temporal consistency on the contextual outputs and semantic consistency on the flow hidden states, ensuring robust alignment. Extensive experiments on both standard benchmarks and challenging in-the-wild dubbing benchmarks demonstrate that our method achieves the state-of-the-art performance across multiple metrics.

</details>

#### [Saar-Voice: A Multi-Speaker Saarbrücken Dialect Speech Corpus](https://arxiv.org/abs/2604.11803)
**Lena S. Oberkircher, Jesujoba O. Alabi, Dietrich Klakow, Jürgen Trouvain** · 2026-04-13

<details>
<summary>Abstract</summary>

Natural language processing (NLP) and speech technologies have made significant progress in recent years; however, they remain largely focused on standardized language varieties. Dialects, despite their cultural significance and widespread use, are underrepresented in linguistic resources and computational models, resulting in performance disparities. To address this gap, we introduce Saar-Voice, a six-hour speech corpus for the Saarbrücken dialect of German. The dataset was created by first collecting text through digitized books and locally sourced materials. A subset of this text was recorded by nine speakers, and we conducted analyses on both the textual and speech components to assess the dataset's characteristics and quality. We discuss methodological challenges related to orthographic and speaker variation, and explore grapheme-to-phoneme (G2P) conversion. The resulting corpus provides aligned textual and audio representations. This serves as a foundation for future research on dialect-aware text-to-speech (TTS), particularly in low-resource scenarios, including zero-shot and few-shot model adaptation.

</details>

#### [StreamMark: A Deep Learning-Based Semi-Fragile Audio Watermarking for Proactive Deepfake Detection](https://arxiv.org/abs/2604.11917)
**Zhentao Liu, Milos Cernak** · 2026-04-13

<details>
<summary>Abstract</summary>

The rapid advancement of generative AI has made it increasingly challenging to distinguish between deepfake audio and authentic human speech. To overcome the limitations of passive detection methods, we propose StreamMark, a novel deep learning-based, semi-fragile audio watermarking system. StreamMark is designed to be robust against benign audio conversions that preserve semantic meaning (e.g., compression, noise) while remaining fragile to malicious, semantics-altering manipulations (e.g., voice conversion, speech editing). Our method introduces a complex-domain embedding technique within a unique Encoder-Distortion-Decoder architecture, trained explicitly to differentiate between these two classes of transformations. Comprehensive benchmarks demonstrate that StreamMark achieves high imperceptibility (SNR 24.16 dB, PESQ 4.20), is resilient to real-world distortions like Opus encoding, and exhibits principled fragility against a suite of deepfake attacks, with message recovery accuracy dropping to chance levels (~50%), while remaining robust to benign AI-based style transfers (ACC >98%).

</details>

#### [Bridging What the Model Thinks and How It Speaks: Self-Aware Speech Language Models for Expressive Speech Generation](https://arxiv.org/abs/2604.11424)
**Kuang Wang, Lai Wei, Qibing Bai, Ping Lin et al.** · 2026-04-13

<details>
<summary>Abstract</summary>

Speech Language Models (SLMs) exhibit strong semantic understanding, yet their generated speech often sounds flat and fails to convey expressive intent, undermining user engagement. We term this mismatch the semantic understanding-acoustic realization gap. We attribute this gap to two key deficiencies: (1) intent transmission failure, where SLMs fail to provide the stable utterance-level intent needed for expressive delivery; and (2) realization-unaware training, where no feedback signal verifies whether acoustic outputs faithfully reflect intended expression. To address these issues, we propose SA-SLM (Self-Aware Speech Language Model), built on the principle that the model should be aware of what it thinks during generation and how it speaks during training. SA-SLM addresses this gap through two core contributions: (1) Intent-Aware Bridging, which uses a Variational Information Bottleneck (VIB) objective to translate the model's internal semantics into temporally smooth expressive intent, making speech generation aware of what the model intends to express; and (2) Realization-Aware Alignment, which repurposes the model as its own critic to verify and align acoustic realization with intended expressive intent via rubric-based feedback. Trained on only 800 hours of expressive speech data, our 3B parameter SA-SLM surpasses all open-source baselines and comes within 0.08 points of GPT-4o-Audio in overall expressiveness on the EchoMind benchmark.

</details>

#### [Knowing What to Stress: A Discourse-Conditioned Text-to-Speech Benchmark](https://arxiv.org/abs/2604.10580)
**Arnon Turetzky, Avihu Dekel, Hagai Aronowitz, Ron Hoory et al.** · 2026-04-12

<details>
<summary>Abstract</summary>

Spoken meaning often depends not only on what is said, but also on which word is emphasized. The same sentence can convey correction, contrast, or clarification depending on where emphasis falls. Although modern text-to-speech (TTS) systems generate expressive speech, it remains unclear whether they infer contextually appropriate stress from discourse alone. To address this gap, we present Context-Aware Stress TTS (CAST), a benchmark for evaluating context-conditioned word-level stress in TTS. Items are defined as contrastive context pairs: identical sentences paired with distinct contexts requiring different stressed words. We evaluate state-of-the-art systems and find a consistent gap: text-only language models reliably recover the intended stress from context, yet TTS systems frequently fail to realize it in speech. We release the benchmark, evaluation framework, construction pipeline and a synthetic corpus to support future work on context-aware speech synthesis.

</details>

#### [Sign-to-Speech Prosody Transfer via Sign Reconstruction-based GAN](https://arxiv.org/abs/2604.10413)
**Toranosuke Manabe, Yuto Shibata, Shinnosuke Takamichi, Yoshimitsu Aoki** · 2026-04-12

<details>
<summary>Abstract</summary>

Deep learning models have improved sign language-to-text translation and made it easier for non-signers to understand signed messages. When the goal is spoken communication, a naive approach is to convert signed messages into text and then synthesize speech via Text-to-Speech (TTS). However, this two-stage pipeline inevitably treat text as a bottleneck representation, causing the loss of rich non-verbal information originally conveyed in the signing. To address this limitation, we propose a novel task, \emph{Sign-to-Speech Prosody Transfer}, which aims to capture the global prosodic nuances expressed in sign language and directly integrate them into synthesized speech. A major challenge is that aligning sign and speech requires expert knowledge, making annotation extremely costly and preventing the construction of large parallel corpora. To overcome this, we introduce \emph{SignRecGAN}, a scalable training framework that leverages unimodal datasets without cross-modal annotations through adversarial learning and reconstruction losses. Furthermore, we propose \emph{S2PFormer}, a new model architecture that preserves the expressive power of existing TTS models while enabling the injection of sign-derived prosody into the synthesized speech. Extensive experiments demonstrate that the proposed method can synthesize speech that faithfully reflects the emotional content of sign language, thereby opening new possibilities for more natural sign language communication. Our code will be available upon acceptance.

</details>

#### [PS-TTS: Phonetic Synchronization in Text-to-Speech for Achieving Natural Automated Dubbing](https://arxiv.org/abs/2604.09111)
**Changi Hong, Yoonah Song, Hwayoung Park, Chaewoon Bang et al.** · 2026-04-10

<details>
<summary>Abstract</summary>

Recently, artificial intelligence-based dubbing technology has advanced, enabling automated dubbing (AD) to convert the source speech of a video into target speech in different languages. However, natural AD still faces synchronization challenges such as duration and lip-synchronization (lip-sync), which are crucial for preserving the viewer experience. Therefore, this paper proposes a synchronization method for AD processes that paraphrases translated text, comprising two steps: isochrony for timing constraints and phonetic synchronization (PS) to preserve lip-sync. First, we achieve isochrony by paraphrasing the translated text with a language model, ensuring the target speech duration matches that of the source speech. Second, we introduce PS, which employs dynamic time warping (DTW) with local costs of vowel distances measured from training data so that the target text composes vowels with pronunciations similar to source vowels. Third, we extend this approach to PSComet, which jointly considers semantic and phonetic similarity to preserve meaning better. The proposed methods are incorporated into text-to-speech systems, PS-TTS and PS-Comet TTS. The performance evaluation using Korean and English lip-reading datasets and a voice-actor dubbing dataset demonstrates that both systems outperform TTS without PS on several objective metrics and outperform voice actors in Korean-to-English and English-to-Korean dubbing. We extend the experiments to French, testing all pairs among these languages to evaluate cross-linguistic applicability. Across all language pairs, PS-Comet performed best, balancing lip-sync accuracy with semantic preservation, confirming that PS-Comet achieves more accurate lip-sync with semantic preservation than PS alone.

</details>

#### [DDSP-QbE++: Improving Speech Quality for Speech Anonymisation for Atypical Speech](https://arxiv.org/abs/2604.09246)
**Suhita Ghosh, Yamini Sinha, Sebastian Stober** · 2026-04-10

<details>
<summary>Abstract</summary>

Differentiable Digital Signal Processing (DDSP) pipelines for voice conversion rely on subtractive synthesis, where a periodic excitation signal is shaped by a learned spectral envelope to reconstruct the target voice. In DDSP-QbE, the excitation is generated via phase accumulation, producing a sawtooth-like waveform whose abrupt discontinuities introduce aliasing artefacts that manifest perceptually as buzziness and spectral distortion, particularly at higher fundamental frequencies. We propose two targeted improvements to the excitation stage of the DDSP-QbE subtractive synthesizer. First, we incorporate explicit voicing detection to gate the harmonic excitation, suppressing the periodic component in unvoiced regions and replacing it with filtered noise, thereby avoiding aliased harmonic content where it is most perceptually disruptive. Second, we apply Polynomial Band-Limited Step (PolyBLEP) correction to the phase-accumulated oscillator, substituting the hard waveform discontinuity at each phase wrap with a smooth polynomial residual that cancels alias-generating components without oversampling or spectral truncation. Together, these modifications yield a cleaner harmonic roll-off, reduced high-frequency artefacts, and improved perceptual naturalness, as measured by MOS. The proposed approach is lightweight, differentiable, and integrates seamlessly into the existing DDSP-QbE training pipeline with no additional learnable parameters.

</details>

#### [AudioGuard: Toward Comprehensive Audio Safety Protection Across Diverse Threat Models](https://arxiv.org/abs/2604.08867)
**Mintong Kang, Chen Fang, Bo Li** · 2026-04-10

<details>
<summary>Abstract</summary>

Audio has rapidly become a primary interface for foundation models, powering real-time voice assistants. Ensuring safety in audio systems is inherently more complex than just "unsafe text spoken aloud": real-world risks can hinge on audio-native harmful sound events, speaker attributes (e.g., child voice), impersonation/voice-cloning misuse, and voice-content compositional harms, such as child voice plus sexual content. The nature of audio makes it challenging to develop comprehensive benchmarks or guardrails against this unique risk landscape. To close this gap, we conduct large-scale red teaming on audio systems, systematically uncover vulnerabilities in audio, and develop a comprehensive, policy-grounded audio risk taxonomy and AudioSafetyBench, the first policy-based audio safety benchmark across diverse threat models. AudioSafetyBench supports diverse languages, suspicious voices (e.g., celebrity/impersonation and child voice), risky voice-content combinations, and non-speech sound events. To defend against these threats, we propose AudioGuard, a unified guardrail consisting of 1) SoundGuard for waveform-level audio-native detection and 2) ContentGuard for policy-grounded semantic protection. Extensive experiments on AudioSafetyBench and four complementary benchmarks show that AudioGuard consistently improves guardrail accuracy over strong audio-LLM-based baselines with substantially lower latency.

</details>

#### [Enhancing Conversational TTS with Cascaded Prompting and ICL-Based Online Reinforcement Learning](https://arxiv.org/abs/2604.08709)
**Zhicheng Ouyang, Seong-Gyun Leem, Bach Viet Do, Haibin Wu et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Conversational AI has made significant progress, yet generating expressive and controllable text-to-speech (TTS) remains challenging. Specifically, controlling fine-grained voice styles and emotions is notoriously difficult and typically requires massive amounts of heavily annotated training data. To overcome this data bottleneck, we present a scalable, data-efficient cascaded framework that pairs textual style tokens with human-curated, high-quality audio prompts. This approach enables single-shot adaptation to fine-grained speaking styles and character voices. In the context of TTS, this audio prompting acts as In-Context Learning (ICL), guiding the model's prosody and timbre without requiring massive parameter updates or large-scale retraining. To further enhance generation quality and mitigate hallucinations, we introduce a novel ICL-based online reinforcement learning (RL) strategy. This strategy directly optimizes the autoregressive prosody model using subjective aesthetic rewards while being constrained by Connectionist Temporal Classification (CTC) alignment to preserve intelligibility. Comprehensive human perception evaluations demonstrate significant improvements in both the naturalness and expressivity of the synthesized speech, establishing the efficacy of our ICL-based online RL approach.

</details>

#### [AVGen-Bench: A Task-Driven Benchmark for Multi-Granular Evaluation of Text-to-Audio-Video Generation](https://arxiv.org/abs/2604.08540)
**Ziwei Zhou, Zeyuan Lai, Rui Wang, Yifan Yang et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Text-to-Audio-Video (T2AV) generation is rapidly becoming a core interface for media creation, yet its evaluation remains fragmented. Existing benchmarks largely assess audio and video in isolation or rely on coarse embedding similarity, failing to capture the fine-grained joint correctness required by realistic prompts. We introduce AVGen-Bench, a task-driven benchmark for T2AV generation featuring high-quality prompts across 11 real-world categories. To support comprehensive assessment, we propose a multi-granular evaluation framework that combines lightweight specialist models with Multimodal Large Language Models (MLLMs), enabling evaluation from perceptual quality to fine-grained semantic controllability. Our evaluation reveals a pronounced gap between strong audio-visual aesthetics and weak semantic reliability, including persistent failures in text rendering, speech coherence, physical reasoning, and a universal breakdown in musical pitch control. Code and benchmark resources are available at http://aka.ms/avgenbench.

</details>

#### [CapTalk: Unified Voice Design for Single-Utterance and Dialogue Speech Generation](https://arxiv.org/abs/2604.08363)
**Xiaosu Su, Zihan Sun, Peilei Jia, Jun Gao** · 2026-04-09

<details>
<summary>Abstract</summary>

Voice design from natural language descriptions is emerging as a new task in text-to-speech multimodal generation, aiming to synthesize speech with target timbre and speaking style without relying on reference audio. However, existing methods mainly focus on single-utterance generation, leaving conversational voice design largely unexplored. In this work, we extend voice design to dialogue, enabling better target speaker modeling and turn-level expressive control in natural conversational settings. We propose CapTalk, a unified caption-conditioned text-audio autoregressive framework for both single-utterance and dialogue voice design. CapTalk uses utterance-level captions for single-utterance voice design and speaker-level captions for dialogue speaker modeling, and further introduces a CoT control sequence in dialogue to explicitly plan turn-level dynamic attributes. To resolve the conflict between stable timbre preservation and context-adaptive expression, we propose a hierarchical variational conditioning module with an utterance-level speaker encoder to better balance stable timbre preservation and context-adaptive expression. This enables timbre reuse while keeping expression adaptive to the current utterance and, in dialogue, the surrounding context. We also build a comprehensive evaluation protocol for both single-utterance and dialogue settings. Experiments show that CapTalk achieves state-of-the-art performance on a single-utterance voice design benchmark and delivers better expression controllability and contextual appropriateness in multi-turn dialogue. Audio samples are available at: https://anonymous.4open.science/api/repo/Captalk-D601/file/index.html.

</details>

#### [Cross-Modal Emotion Transfer for Emotion Editing in Talking Face Video](https://arxiv.org/abs/2604.07786)
**Chanhyuk Choi, Taesoo Kim, Donggyu Lee, Siyeol Jung et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Talking face generation has gained significant attention as a core application of generative models. To enhance the expressiveness and realism of synthesized videos, emotion editing in talking face video plays a crucial role. However, existing approaches often limit expressive flexibility and struggle to generate extended emotions. Label-based methods represent emotions with discrete categories, which fail to capture a wide range of emotions. Audio-based methods can leverage emotionally rich speech signals - and even benefit from expressive text-to-speech (TTS) synthesis - but they fail to express the target emotions because emotions and linguistic contents are entangled in emotional speeches. Images-based methods, on the other hand, rely on target reference images to guide emotion transfer, yet they require high-quality frontal views and face challenges in acquiring reference data for extended emotions (e.g., sarcasm). To address these limitations, we propose Cross-Modal Emotion Transfer (C-MET), a novel approach that generates facial expressions based on speeches by modeling emotion semantic vectors between speech and visual feature spaces. C-MET leverages a large-scale pretrained audio encoder and a disentangled facial expression encoder to learn emotion semantic vectors that represent the difference between two different emotional embeddings across modalities. Extensive experiments on the MEAD and CREMA-D datasets demonstrate that our method improves emotion accuracy by 14% over state-of-the-art methods, while generating expressive talking face videos - even for unseen extended emotions. Code, checkpoint, and demo are available at https://chanhyeok-choi.github.io/C-MET/

</details>

#### [AT-ADD: All-Type Audio Deepfake Detection Challenge Evaluation Plan](https://arxiv.org/abs/2604.08184)
**Yuankun Xie, Haonan Cheng, Jiayi Zhou, Xiaoxuan Guo et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

The rapid advancement of Audio Large Language Models (ALLMs) has enabled cost-effective, high-fidelity generation and manipulation of both speech and non-speech audio, including sound effects, singing voices, and music. While these capabilities foster creativity and content production, they also introduce significant security and trust challenges, as realistic audio deepfakes can now be generated and disseminated at scale. Existing audio deepfake detection (ADD) countermeasures (CMs) and benchmarks, however, remain largely speech-centric, often relying on speech-specific artifacts and exhibiting limited robustness to real-world distortions, as well as restricted generalization to heterogeneous audio types and emerging spoofing techniques. To address these gaps, we propose the All-Type Audio Deepfake Detection (AT-ADD) Grand Challenge for ACM Multimedia 2026, designed to bridge controlled academic evaluation with practical multimedia forensics. AT-ADD comprises two tracks: (1) Robust Speech Deepfake Detection, which evaluates detectors under real-world scenarios and against unseen, state-of-the-art speech generation methods; and (2) All-Type Audio Deepfake Detection, which extends detection beyond speech to diverse, unknown audio types and promotes type-agnostic generalization across speech, sound, singing, and music. By providing standardized datasets, rigorous evaluation protocols, and reproducible baselines, AT-ADD aims to accelerate the development of robust and generalizable audio forensic technologies, supporting secure communication, reliable media verification, and responsible governance in an era of pervasive synthetic audio.

</details>

#### [Lexical Tone is Hard to Quantize: Probing Discrete Speech Units in Mandarin and Yorùbá](https://arxiv.org/abs/2604.07467)
**Opeyemi Osakuade, Simon King** · 2026-04-08

<details>
<summary>Abstract</summary>

Discrete speech units (DSUs) are derived by quantising representations from models trained using self-supervised learning (SSL). They are a popular representation for a wide variety of spoken language tasks, including those where prosody matters. DSUs are especially convenient for tasks where text and speech are jointly modelled, such as text-to-speech and multimodal dialogue systems. But we have found that DSUs encode suprasegmental information less reliably than segmental structure, which we demonstrate in this work using lexical tone, though this limitation likely extends to other suprasegmental features such as prosody. Our investigations using the tone languages Mandarin and Yorùbá show that the SSL latent representations themselves do encode tone, yet DSUs obtained using quantisation tend to prioritise phonetic structure, which makes lexical tone less reliably encoded. This remains true for a variety of quantisation methods, not only the most common, K-means. We conclude that current DSU quantisation strategies have limitations for suprasegmental features, which suggests a need for new, tone-aware (or prosody-aware) techniques in speech representation learning. We point towards a potential form of the solution by performing K-means clustering once to encode phonetic information, then again on the residual representation, which better encodes lexical tone.

</details>

#### [In-Context Learning in Speech Language Models: Analyzing the Role of Acoustic Features, Linguistic Structure, and Induction Heads](https://arxiv.org/abs/2604.06356)
**Charlotte Pouw, Hosein Mohebbi, Afra Alishahi, Willem Zuidema** · 2026-04-07

<details>
<summary>Abstract</summary>

In-Context Learning (ICL) has been extensively studied in text-only Language Models, but remains largely unexplored in the speech domain. Here, we investigate how linguistic and acoustic features affect ICL in Speech Language Models. We focus on the Text-to-Speech (TTS) task, which allows us to analyze ICL from two angles: (1) how accurately the model infers the task from the demonstrations (i.e., generating the correct spoken content), and (2) to what extent the model mimics the acoustic characteristics of the demonstration speech in its output. We find that speaking rate strongly affects ICL performance and is also mimicked in the output, whereas pitch range and intensity have little impact on performance and are not consistently reproduced. Finally, we investigate the role of induction heads in speech-based ICL and show that these heads play a causal role: ablating the top-k induction heads completely removes the model's ICL ability, mirroring findings from text-based ICL.

</details>

#### [A Novel Automatic Framework for Speaker Drift Detection in Synthesized Speech](https://arxiv.org/abs/2604.06327)
**Jia-Hong Huang, Seulgi Kim, Yi Chieh Liu, Yixian Shen et al.** · 2026-04-07

<details>
<summary>Abstract</summary>

Recent diffusion-based text-to-speech (TTS) models achieve high naturalness and expressiveness, yet often suffer from speaker drift, a subtle, gradual shift in perceived speaker identity within a single utterance. This underexplored phenomenon undermines the coherence of synthetic speech, especially in long-form or interactive settings. We introduce the first automatic framework for detecting speaker drift by formulating it as a binary classification task over utterance-level speaker consistency. Our method computes cosine similarity across overlapping segments of synthesized speech and prompts large language models (LLMs) with structured representations to assess drift. We provide theoretical guarantees for cosine-based drift detection and demonstrate that speaker embeddings exhibit meaningful geometric clustering on the unit sphere. To support evaluation, we construct a high-quality synthetic benchmark with human-validated speaker drift annotations. Experiments with multiple state-of-the-art LLMs confirm the viability of this embedding-to-reasoning pipeline. Our work establishes speaker drift as a standalone research problem and bridges geometric signal analysis with LLM-based perceptual reasoning in modern TTS.

</details>

#### [Controllable Singing Style Conversion with Boundary-Aware Information Bottleneck](https://arxiv.org/abs/2604.05526)
**Zhetao Hu, Yiquan Zhou, Wenyu Wang, Zhiyu Wu et al.** · 2026-04-07

<details>
<summary>Abstract</summary>

This paper presents the submission of the S4 team to the Singing Voice Conversion Challenge 2025 (SVCC2025)-a novel singing style conversion system that advances fine-grained style conversion and control within in-domain settings. To address the critical challenges of style leakage, dynamic rendering, and high-fidelity generation with limited data, we introduce three key innovations: a boundary-aware Whisper bottleneck that pools phoneme-span representations to suppress residual source style while preserving linguistic content; an explicit frame-level technique matrix, enhanced by targeted F0 processing during inference, for stable and distinct dynamic style rendering; and a perceptually motivated high-frequency band completion strategy that leverages an auxiliary standard 48kHz SVC model to augment the high-frequency spectrum, thereby overcoming data scarcity without overfitting. In the official SVCC2025 subjective evaluation, our system achieves the best naturalness performance among all submissions while maintaining competitive results in speaker similarity and technique control, despite using significantly less extra singing data than other top-performing systems. Audio samples are available online.

</details>

#### [ClickAIXR: On-Device Multimodal Vision-Language Interaction with Real-World Objects in Extended Reality](https://arxiv.org/abs/2604.04905)
**Dawar Khan, Alexandre Kouyoumdjian, Xinyu Liu, Omar Mena et al.** · 2026-04-06

<details>
<summary>Abstract</summary>

We present ClickAIXR, a novel on-device framework for multimodal vision-language interaction with objects in extended reality (XR). Unlike prior systems that rely on cloud-based AI (e.g., ChatGPT) or gaze-based selection (e.g., GazePointAR), ClickAIXR integrates an on-device vision-language model (VLM) with a controller-based object selection paradigm, enabling users to precisely click on real-world objects in XR. Once selected, the object image is processed locally by the VLM to answer natural language questions through both text and speech. This object-centered interaction reduces ambiguity inherent in gaze- or voice-only interfaces and improves transparency by performing all inference on-device, addressing concerns around privacy and latency. We implemented ClickAIXR in the Magic Leap SDK (C API) with ONNX-based local VLM inference. We conducted a user study comparing ClickAIXR with Gemini 2.5 Flash and ChatGPT 5, evaluating usability, trust, and user satisfaction. Results show that latency is moderate and user experience is acceptable. Our findings demonstrate the potential of click-based object selection combined with on-device AI to advance trustworthy, privacy-preserving XR interactions. The source code and supplementary materials are available at: nanovis.org/ClickAIXR.html

</details>

#### [Subspace Control: Turning Constrained Model Steering into Controllable Spectral Optimization](https://arxiv.org/abs/2604.04231)
**Yancheng Huang, Changsheng Wang, Chongyu Fan, Yicheng Lang et al.** · 2026-04-05

<details>
<summary>Abstract</summary>

Foundation models, such as large language models (LLMs), are powerful but often require customization before deployment to satisfy practical constraints such as safety, privacy, and task-specific requirements, leading to "constrained" optimization problems for model steering and adaptation. However, solving such problems remains largely underexplored and is particularly challenging due to interference between the primary objective and constraint objectives during optimization. In this paper, we propose a subspace control framework for constrained model training. Specifically, (i) we first analyze, from a model merging perspective, how spectral cross-task interference arises and show that it can be resolved via a one-shot solution that orthogonalizes the merged subspace; (ii) we establish a connection between this solution and gradient orthogonalization in the spectral optimizer Muon; and (iii) building on these insights, we introduce SIFT (spectral interference-free training), which leverages a localization scheme to selectively intervene during optimization, enabling controllable updates that mitigate objective-constraint conflicts. We evaluate SIFT across four representative applications: (a) machine unlearning, (b) safety alignment, (c) text-to-speech adaptation, and (d) hallucination mitigation. Compared to both control-based and control-free baselines, SIFT consistently achieves substantial and robust performance improvements across all tasks. Code is available at https://github.com/OPTML-Group/SIFT.

</details>

#### [GAP-URGENet: A Generative-Predictive Fusion Framework for Universal Speech Enhancement](https://arxiv.org/abs/2604.01832)
**Xiaobin Rong, Yushi Wang, Zheng Wang, Jing Lu** · 2026-04-02

<details>
<summary>Abstract</summary>

We introduce GAP-URGENet, a generative-predictive fusion framework developed for Track 1 of the ICASSP 2026 URGENT Challenge. The system integrates a generative branch, which performs full-stack speech restoration in a self-supervised representation domain and reconstructs the waveform via a neural vocoder, along with a predictive branch that performs spectrogram-domain enhancement, providing complementary cues. Outputs from both branches are fused by a post-processing module, which also performs bandwidth extension to generate the enhanced waveform at 48 kHz, later downsampled to the original sampling rate. This generative-predictive fusion improves robustness and perceptual quality, achieving top performance in the blind-test phase and ranking 1st in the objective evaluation. Audio examples are available at https://xiaobin-rong.github.io/gap-urgenet_demo.

</details>

#### [T5Gemma-TTS Technical Report](https://arxiv.org/abs/2604.01760)
**Chihiro Arata, Kiyoshi Kurihara** · 2026-04-02

<details>
<summary>Abstract</summary>

Autoregressive neural codec language models have shown strong zero-shot voice cloning ability, but decoder-only architectures treat input text as a prefix that competes with the growing audio sequence for positional capacity, weakening text conditioning over long utterances. We present T5Gemma-TTS, an encoder-decoder codec language model that maintains persistent text conditioning by routing bidirectional text representations through cross-attention at every decoder layer. Built on the T5Gemma pretrained encoder-decoder backbone (2B encoder + 2B decoder; 4B parameters), it inherits rich linguistic knowledge without phoneme conversion and processes text directly at the subword level. To improve duration control, we introduce Progress-Monitoring Rotary Position Embedding (PM-RoPE) in all 26 cross-attention layers, injecting normalized progress signals that help the decoder track target speech length. Trained on 170,000 hours of multilingual speech in English, Chinese, and Japanese, T5Gemma-TTS achieves a statistically significant speaker-similarity gain on Japanese over XTTSv2 (0.677 vs. 0.622; non-overlapping 95% confidence intervals) and the highest numerical Korean speaker similarity (0.747) despite Korean not being included in training, although this margin over XTTSv2 (0.741) is not statistically conclusive. It also attains the lowest numerical Japanese character error rate among five baselines (0.126), though this ranking should be interpreted cautiously because of partial confidence-interval overlap with Kokoro. English results on LibriSpeech should be viewed as an upper-bound estimate because LibriHeavy is a superset of LibriSpeech. Using the same checkpoint, disabling PM-RoPE at inference causes near-complete synthesis failure: CER degrades from 0.129 to 0.982 and duration accuracy drops from 79% to 46%. Code and weights are available at https://github.com/Aratako/T5Gemma-TTS.

</details>

#### [Acoustic and perceptual differences between standard and accented Chinese speech and their voice clones](https://arxiv.org/abs/2604.01562)
**Tianle Yang, Chengzhe Sun, Phil Rose, Siwei Lyu** · 2026-04-02

<details>
<summary>Abstract</summary>

Voice cloning is often evaluated in terms of overall quality, but less is known about accent preservation and its perceptual consequences. We compare standard and heavily accented Mandarin speech and their voice clones using a combined computational and perceptual design. Embedding-based analyses show no reliable accented-standard difference in original-clone distances across systems. In the perception study, clones are rated as more similar to their originals for standard than for accented speakers, and intelligibility increases from original to clone, with a larger gain for accented speech. These results show that accent variation can shape perceived identity match and intelligibility in voice cloning even when it is not reflected in an off-the-shelf speaker-embedding distance, and they motivate evaluating speaker identity preservation and accent preservation as separable dimensions.

</details>

#### [OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models](https://arxiv.org/abs/2604.00688)
**Han Zhu, Lingxuan Ye, Wei Kang, Zengwei Yao et al.** · 2026-04-01

<details>
<summary>Abstract</summary>

We present OmniVoice, a massive multilingual zero-shot text-to-speech (TTS) model that scales to over 600 languages. At its core is a novel diffusion language model-style discrete non-autoregressive (NAR) architecture. Unlike conventional discrete NAR models that suffer from performance bottlenecks in complex two-stage (text-to-semantic-to-acoustic) pipelines, OmniVoice directly maps text to multi-codebook acoustic tokens. This simplified approach is facilitated by two key technical innovations: (1) a full-codebook random masking strategy for efficient training, and (2) initialization from a pre-trained LLM to ensure superior intelligibility. By leveraging a 581k-hour multilingual dataset curated entirely from open-source data, OmniVoice achieves the broadest language coverage to date and delivers state-of-the-art performance across Chinese, English, and diverse multilingual benchmarks. Our code and pre-trained models are publicly available at https://github.com/k2-fsa/OmniVoice.

</details>

#### [MambaVoiceCloning: Efficient and Expressive Text-to-Speech via State-Space Modeling and Diffusion Control](https://arxiv.org/abs/2604.00292)
**Sahil Kumar, Namrataben Patel, Honggang Wang, Youshan Zhang** · 2026-03-31

<details>
<summary>Abstract</summary>

MambaVoiceCloning (MVC) asks whether the conditioning path of diffusion-based TTS can be made fully SSM-only at inference, removing all attention and explicit RNN-style recurrence layers across text, rhythm, and prosody, while preserving or improving quality under controlled conditions. MVC combines a gated bidirectional Mamba text encoder, a Temporal Bi-Mamba supervised by a lightweight alignment teacher discarded after training, and an Expressive Mamba with AdaLN modulation, yielding linear-time O(T) conditioning with bounded activation memory and practical finite look-ahead streaming. Unlike prior Mamba-TTS systems that remain hybrid at inference, MVC removes attention-based duration and style modules under a fixed StyleTTS2 mel-diffusion-vocoder backbone. Trained on LJSpeech/LibriTTS and evaluated on VCTK, CSS10 (ES/DE/FR), and long-form Gutenberg passages, MVC achieves modest but statistically reliable gains over StyleTTS2, VITS, and Mamba-attention hybrids in MOS/CMOS, F0 RMSE, MCD, and WER, while reducing encoder parameters to 21M and improving throughput by 1.6x. Diffusion remains the dominant latency source, but SSM-only conditioning improves memory footprint, stability, and deployability.

</details>

#### [Covertly improving intelligibility with data-driven adaptations of speech timing](https://arxiv.org/abs/2603.30032)
**Paige Tuttösí, Angelica Lim, H. Henny Yeung, Yue Wang et al.** · 2026-03-31

<details>
<summary>Abstract</summary>

Human talkers often address listeners with language-comprehension challenges, such as hard-of-hearing or non-native adults, by globally slowing down their speech. However, it remains unclear whether this strategy actually makes speech more intelligible. Here, we take advantage of recent advancements in machine-generated speech allowing more precise control of speech rate in order to systematically examine how targeted speech-rate adjustments may improve comprehension. We first use reverse-correlation experiments to show that the temporal influence of speech rate prior to a target vowel contrast (ex. the tense-lax distinction) in fact manifests in a scissor-like pattern, with opposite effects in early versus late context windows; this pattern is remarkably stable both within individuals and across native L1-English listeners and L2-English listeners with French, Mandarin, and Japanese L1s. Second, we show that this speech rate structure not only facilitates L2 listeners' comprehension of the target vowel contrast, but that native listeners also rely on this pattern in challenging acoustic conditions. Finally, we build a data-driven text-to-speech algorithm that replicates this temporal structure on novel speech sequences. Across a variety of sentences and vowel contrasts, listeners remained unaware that such targeted slowing improved word comprehension. Strikingly, participants instead judged the common strategy of global slowing as clearer, even though it actually increased comprehension errors. Together, these results show that targeted adjustments to speech rate significantly aid intelligibility under challenging conditions, while often going unnoticed. More generally, this paper provides a data-driven methodology to improve the accessibility of machine-generated speech which can be extended to other aspects of speech comprehension and a wide variety of listeners and environments.

</details>

#### [LongCat-AudioDiT: High-Fidelity Diffusion Text-to-Speech in the Waveform Latent Space](https://arxiv.org/abs/2603.29339)
**Detai Xin, Shujie Hu, Chengzuo Yang, Chen Huang et al.** · 2026-03-31

<details>
<summary>Abstract</summary>

We present LongCat-AudioDiT, a novel, non-autoregressive diffusion-based text-to-speech (TTS) model that achieves state-of-the-art (SOTA) performance. Unlike previous methods that rely on intermediate acoustic representations such as mel-spectrograms, the core innovation of LongCat-AudioDiT lies in operating directly within the waveform latent space. This approach effectively mitigates compounding errors and drastically simplifies the TTS pipeline, requiring only a waveform variational autoencoder (Wav-VAE) and a diffusion backbone. Furthermore, we introduce two critical improvements to the inference process: first, we identify and rectify a long-standing training-inference mismatch; second, we replace traditional classifier-free guidance with adaptive projection guidance to elevate generation quality. Experimental results demonstrate that, despite the absence of complex multi-stage training pipelines or high-quality human-annotated datasets, LongCat-AudioDiT achieves SOTA zero-shot voice cloning performance on the Seed benchmark while maintaining competitive intelligibility. Specifically, our largest variant, LongCat-AudioDiT-3.5B, outperforms the previous SOTA model (Seed-TTS), improving the speaker similarity (SIM) scores from 0.809 to 0.818 on Seed-ZH, and from 0.776 to 0.797 on Seed-Hard. Finally, through comprehensive ablation studies and systematic analysis, we validate the effectiveness of our proposed modules. Notably, we investigate the interplay between the Wav-VAE and the TTS backbone, revealing the counterintuitive finding that superior reconstruction fidelity in the Wav-VAE does not necessarily lead to better overall TTS performance. Code and model weights are released to foster further research within the speech community.

</details>

#### [From Natural Alignment to Conditional Controllability in Multimodal Dialogue](https://arxiv.org/abs/2603.29162)
**Zeyu Jin, Songtao Zhou, Haoyu Wang, Minghao Tian et al.** · 2026-03-31

<details>
<summary>Abstract</summary>

The recent advancement of Artificial Intelligence Generated Content (AIGC) has led to significant strides in modeling human interaction, particularly in the context of multimodal dialogue. While current methods impressively generate realistic dialogue in isolated modalities like speech or vision, challenges remain in controllable Multimodal Dialogue Generation (MDG). This paper focuses on the natural alignment between speech, vision, and text in human interaction, aiming for expressive dialogue generation through multimodal conditional control. To address the insufficient richness and diversity of dialogue expressiveness in existing datasets, we introduce a novel multimodal dialogue annotation pipeline to curate dialogues from movies and TV series with fine-grained annotations in interactional characteristics. The resulting MM-Dia dataset (360+ hours, 54,700 dialogues) facilitates explicitly controlled MDG, specifically through style-controllable dialogue speech synthesis. In parallel, MM-Dia-Bench (309 highly expressive dialogues with visible single-/dual-speaker scenes) serves as a rigorous testbed for implicit cross-modal MDG control, evaluating audio-visual style consistency across modalities. Extensive experiments demonstrate that training on MM-Dia significantly enhances fine-grained controllability, while evaluations on MM-Dia-Bench reveal limitations in current frameworks to replicate the nuanced expressiveness of human interaction. These findings provides new insights and challenges for multimodal conditional dialogue generation.

</details>

#### [Evaluating Generalization and Robustness in Russian Anti-Spoofing: The RuASD Initiative](https://arxiv.org/abs/2604.02374)
**Ksenia Lysikova, Kirill Borodin, Kirill Borodin** · 2026-03-31

<details>
<summary>Abstract</summary>

RuASD (Russian AntiSpoofing Dataset) is a dedicated, reproducible benchmark for Russian-language speech anti-spoofing designed to evaluate both in-domain discrimination and robustness to deployment-style distribution shifts. It combines a large spoof subset synthesized using 37 modern Russian-capable TTS and voice-cloning systems with a bona fide subset curated from multiple heterogeneous open Russian speech corpora, enabling systematic evaluation across diverse data sources. To emulate typical dissemination and channel effects in a controlled and reproducible manner, RuASD includes configurable simulations of platform and transmission distortions, including room reverberation, additive noise/music, and a range of speech-codec transcodings implemented via a unified processing chain. We benchmark a diverse set of publicly available anti-spoofing countermeasures spanning lightweight supervised architectures, graph-attention models, SSL-based detectors, and large-scale pretrained systems, and report reference results on both clean and simulated conditions to characterize robustness under realistic perturbation pipelines. The dataset is publickly available at \href{https://huggingface.co/datasets/MTUCI/RuASD}{\underline{Hugging Face}} and \href{https://modelscope.cn/datasets/lab260/RuASD}{\underline{ModelScope}}.

</details>

#### [MOSS-VoiceGenerator: Create Realistic Voices with Natural Language Descriptions](https://arxiv.org/abs/2603.28086)
**Kexin Huang, Liwei Fan, Botian Jiang, Yaozhou Jiang et al.** · 2026-03-30

<details>
<summary>Abstract</summary>

Voice design from natural language aims to generate speaker timbres directly from free-form textual descriptions, allowing users to create voices tailored to specific roles, personalities, and emotions. Such controllable voice creation benefits a wide range of downstream applications-including storytelling, game dubbing, role-play agents, and conversational assistants, making it a significant task for modern Text-to-Speech models. However, existing models are largely trained on carefully recorded studio data, which produces speech that is clean and well-articulated, yet lacks the lived-in qualities of real human voices. To address these limitations, we present MOSS-VoiceGenerator, an open-source instruction-driven voice generation model that creates new timbres directly from natural language prompts. Motivated by the hypothesis that exposure to real-world acoustic variation produces more perceptually natural voices, we train on large-scale expressive speech data sourced from cinematic content. Subjective preference studies demonstrate its superiority in overall performance, instruction-following, and naturalness compared to other voice design models.

</details>

#### [Hydra: Unifying Document Retrieval and Generation in a Single Vision-Language Model](https://arxiv.org/abs/2603.28554)
**Athos Georgiou** · 2026-03-30

<details>
<summary>Abstract</summary>

Visual document understanding typically requires separate retrieval and generation models, doubling memory and system complexity. We present Hydra, a dual-head approach that provides both ColBERT-style late-interaction retrieval and autoregressive generation from a single vision-language model (VLM). A single LoRA adapter, trained only for retrieval, is toggled at inference: enabling it produces multi-vector embeddings; disabling it recovers the base model's generation quality -- byte-identical outputs in 100% of 10,500 greedy and stochastic samples, with max delta-ANLS = 0.0044 across 15,301 samples on four VQA benchmarks (three informative; ChartQA is near-zero for both models under greedy decoding) when compared against an independent base-model pipeline. We identify three engineering requirements (attention-mode restoration, lm_head preservation, KV-cache-aware decoding) whose omission silently breaks generation despite correct weight recovery. On ViDoRe V1, Hydra (4B) is within 1 percentage point of a controlled single-head baseline in a single training run, with higher aggregate scores on V2 and V3 that are concentrated on a subset of tasks; multi-seed experiments are needed to confirm these trends. The single-model design reduces peak GPU memory by 41%, though adapter switching introduces throughput overhead under concurrent serving loads. An ablation shows that GritLM-style joint training provides no benefit within the LoRA-based (r=16) training regime. A proof-of-concept extension to Qwen2.5-Omni-3B demonstrates that the mechanism generalizes to audio retrieval and video embedding, with speech generation.

</details>

#### [VoxAnchor: Grounding Speech Authenticity in Throat Vibration via mmWave Radar](https://arxiv.org/abs/2603.27562)
**Mingda Han, Huanqi Yang, Chaoqun Li, Wenhao Li et al.** · 2026-03-29

<details>
<summary>Abstract</summary>

Rapid advances in speech synthesis and audio editing have made realistic forgeries increasingly accessible, yet existing detection methods remain vulnerable to tampering or depend on visual/wearable sensors. In this paper, we present VoxAnchor, a system that physically grounds audio authentication in vocal dynamics by leveraging the inherent coherence between speech acoustics and radar-sensed throat vibrations. VoxAnchor uses contactless millimeter-wave radar to capture fine-grained throat vibrations that are tightly coupled with human speech production, establishing a hard-to-forge anchor rooted in human physiology. The design comprises three main components: (1) a cross-modal frame-work that uses modality-specific encoders and contrastive learning to detect subtle mismatches at word granularity; (2) a phase-aware pipeline that extracts physically consistent, temporally faithful throat vibrations; and (3) a dual-stage strategy that combines signal-level onset detection and semantic-level coherence to align asynchronous radar and audio streams. Unlike liveness detection, which only confirms whether speech occurred, VoxAnchor verifies what was spoken through word-level content consistency, exposing localized edits that preserve identity and global authenticity cues. Extensive evaluations show that VoxAnchor achieves robust, fine-grained detection across diverse forgeries (editing, splicing, replay, deepfake) and conditions, with an overall EER of 0.017, low latency, and modest computational cost.

</details>

#### [Voxtral TTS](https://arxiv.org/abs/2603.25551)
**Alexander H. Liu, Alexis Tacnet, Andy Ehrenberg, Andy Lo et al.** · 2026-03-26

<details>
<summary>Abstract</summary>

We introduce Voxtral TTS, an expressive multilingual text-to-speech model that generates natural speech from as little as 3 seconds of reference audio. Voxtral TTS adopts a hybrid architecture that combines auto-regressive generation of semantic speech tokens with flow-matching for acoustic tokens. These tokens are encoded and decoded with Voxtral Codec, a speech tokenizer trained from scratch with a hybrid VQ-FSQ quantization scheme. In human evaluations conducted by native speakers, Voxtral TTS is preferred for multilingual voice cloning due to its naturalness and expressivity, achieving a 68.4\% win rate over ElevenLabs Flash v2.5. We release the model weights under a CC BY-NC license.

</details>

#### [OmniACBench: A Benchmark for Evaluating Context-Grounded Acoustic Control in Omni-Modal Models](https://arxiv.org/abs/2603.23938)
**Seunghee Kim, Bumkyu Park, Kyudan Jung, Joosung Lee et al.** · 2026-03-25

<details>
<summary>Abstract</summary>

Most testbeds for omni-modal models assess multimodal understanding via textual outputs, leaving it unclear whether these models can properly speak their answers. To study this, we introduce OmniACBench, a benchmark for evaluating context-grounded acoustic control in omni-modal models. Given a spoken instruction, a text script, and an image, a model must read the script aloud with an appropriate tone and manner. OmniACBench comprises 3,559 verified instances covering six acoustic features: speech rate, phonation, pronunciation, emotion, global accent, and timbre. Extensive experiments on eight models reveal their limitations in the proposed setting, despite their strong performance on prior textual-output evaluations. Our analyses show that the main bottleneck lies not in processing individual modalities, but in integrating multimodal context for faithful speech generation. Moreover, we identify three common failure modes-weak direct control, failed implicit inference, and failed multimodal grounding-providing insights for developing models that can verbalize responses effectively.

</details>

#### [Gesture2Speech: How Far Can Hand Movements Shape Expressive Speech?](https://arxiv.org/abs/2603.19831)
**Lokesh Kumar, Nirmesh Shah, Ashishkumar P. Gudmalwar, Pankaj Wasnik** · 2026-03-20

<details>
<summary>Abstract</summary>

Human communication seamlessly integrates speech and bodily motion, where hand gestures naturally complement vocal prosody to express intent, emotion, and emphasis. While recent text-to-speech (TTS) systems have begun incorporating multimodal cues such as facial expressions or lip movements, the role of hand gestures in shaping prosody remains largely underexplored. We propose a novel multimodal TTS framework, Gesture2Speech, that leverages visual gesture cues to modulate prosody in synthesized speech. Motivated by the observation that confident and expressive speakers coordinate gestures with vocal prosody, we introduce a multimodal Mixture-of-Experts (MoE) architecture that dynamically fuses linguistic content and gesture features within a dedicated style extraction module. The fused representation conditions an LLM-based speech decoder, enabling prosodic modulation that is temporally aligned with hand movements. We further design a gesture-speech alignment loss that explicitly models their temporal correspondence to ensure fine-grained synchrony between gestures and prosodic contours. Evaluations on the PATS dataset show that Gesture2Speech outperforms state-of-the-art baselines in both speech naturalness and gesture-speech synchrony. To the best of our knowledge, this is the first work to utilize hand gesture cues for prosody control in neural speech synthesis. Demo samples are available at https://research.sri-media-analysis.com/aaai26-beeu-gesture2speech/

</details>

#### [Borderless Long Speech Synthesis](https://arxiv.org/abs/2603.19798)
**Xingchen Song, Di Wu, Dinghao Zhou, Pengyu Cheng et al.** · 2026-03-20

<details>
<summary>Abstract</summary>

Most existing text-to-speech (TTS) systems either synthesize speech sentence by sentence and stitch the results together, or drive synthesis from plain-text dialogues alone. Both approaches leave models with little understanding of global context or paralinguistic cues, making it hard to capture real-world phenomena such as multi-speaker interactions (interruptions, overlapping speech), evolving emotional arcs, and varied acoustic environments. We introduce the Borderless Long Speech Synthesis framework for agent-centric, borderless long audio synthesis. Rather than targeting a single narrow task, the system is designed as a unified capability set spanning VoiceDesigner, multi-speaker synthesis, Instruct TTS, and long-form text synthesis. On the data side, we propose a "Labeling over filtering/cleaning" strategy and design a top-down, multi-level annotation schema we call Global-Sentence-Token. On the model side, we adopt a backbone with a continuous tokenizer and add Chain-of-Thought (CoT) reasoning together with Dimension Dropout, both of which markedly improve instruction following under complex conditions. We further show that the system is Native Agentic by design: the hierarchical annotation doubles as a Structured Semantic Interface between the LLM Agent and the synthesis engine, creating a layered control protocol stack that spans from scene semantics down to phonetic detail. Text thereby becomes an information-complete, wide-band control channel, enabling a front-end LLM to convert inputs of any modality into structured generation commands, extending the paradigm from Text2Speech to borderless long speech synthesis.

</details>

#### [MOSS-TTSD: Text to Spoken Dialogue Generation](https://arxiv.org/abs/2603.19739)
**Yuqian Zhang, Donghua Yu, Zhengyuan Lin, Botian Jiang et al.** · 2026-03-20

<details>
<summary>Abstract</summary>

Spoken dialogue generation is crucial for applications like podcasts, dynamic commentary, and entertainment content, but poses significant challenges compared to single-utterance text-to-speech (TTS). Key requirements include accurate turn-taking, cross-turn acoustic consistency, and long-form stability, which current models often fail to address due to a lack of dialogue context modeling. To bridge this gap, we present MOSS-TTSD, a spoken dialogue synthesis model designed for expressive, multi-party conversational speech across multiple languages. With enhanced long-context modeling, MOSS-TTSD generates long-form spoken conversations from dialogue scripts with explicit speaker tags, supporting up to 60 minutes of single-pass synthesis, multi-party dialogue with up to 5 speakers, and zero-shot voice cloning from a short reference audio clip. The model supports various mainstream languages, including English and Chinese, and is adapted to several long-form scenarios. Additionally, to address limitations of existing evaluation methods, we propose TTSD-eval, an objective evaluation framework based on forced alignment that measures speaker attribution accuracy and speaker similarity without relying on speaker diarization tools. Both objective and subjective evaluation results show that MOSS-TTSD surpasses strong open-source and proprietary baselines in dialogue synthesis.

</details>

#### [MOSS-TTS Technical Report](https://arxiv.org/abs/2603.18090)
**Yitian Gong, Botian Jiang, Yiwei Zhao, Yucheng Yuan et al.** · 2026-03-18

<details>
<summary>Abstract</summary>

This technical report presents MOSS-TTS, a speech generation foundation model built on a scalable recipe: discrete audio tokens, autoregressive modeling, and large-scale pretraining. Built on MOSS-Audio-Tokenizer, a causal Transformer tokenizer that compresses 24 kHz audio to 12.5 fps with variable-bitrate RVQ and unified semantic-acoustic representations, we release two complementary generators: MOSS-TTS, which emphasizes structural simplicity, scalability, and long-context/control-oriented deployment, and MOSS-TTS-Local-Transformer, which introduces a frame-local autoregressive module for higher modeling efficiency, stronger speaker preservation, and a shorter time to first audio. Across multilingual and open-domain settings, MOSS-TTS supports zero-shot voice cloning, token-level duration control, phoneme-/pinyin-level pronunciation control, smooth code-switching, and stable long-form generation. This report summarizes the design, training recipe, and empirical characteristics of the released models.

</details>

#### [Neuron-Level Emotion Control in Speech-Generative Large Audio-Language Models](https://arxiv.org/abs/2603.17231)
**Xiutian Zhao, Ismail Rasim Ulgen, Philipp Koehn, Björn Schuller et al.** · 2026-03-18

<details>
<summary>Abstract</summary>

Large audio-language models (LALMs) can produce expressive speech, yet reliable emotion control remains elusive: conversions often miss the target affect and may degrade linguistic fidelity through refusals, hallucinations, or paraphrase. We present, to our knowledge, the first neuron-level study of emotion control in speech-generative LALMs and demonstrate that compact emotion-sensitive neurons (ESNs) are causally actionable, enabling training-free emotion steering at inference time. ESNs are identified via success-filtered activation aggregation enforcing both emotion realization and content preservation. Across three LALMs (Qwen2.5-Omni-7B, MiniCPM-o 4.5, Kimi-Audio), ESN interventions yield emotion-specific gains that generalize to unseen speakers and are supported by automatic and human evaluation. Controllability depends on selector design, mask sparsity, filtering, and intervention strength. Our results establish a mechanistic framework for training-free emotion control in speech generation.

</details>

#### [Omnilingual SONAR: Cross-Lingual and Cross-Modal Sentence Embeddings Bridging Massively Multilingual Text and Speech](https://arxiv.org/abs/2603.16606)
**Omnilingual SONAR Team, João Maria Janeiro, Pere-Lluís Huguet Cabot, Ioannis Tsiamas et al.** · 2026-03-17

<details>
<summary>Abstract</summary>

Cross-lingual sentence encoders typically cover only a few hundred languages and often trade downstream quality for stronger alignment, limiting their adoption. We introduce OmniSONAR, a new family of omnilingual, cross-lingual and cross-modal sentence embedding models that natively embed text, speech, code, and mathematical expressions in a single semantic space, while delivering state-of-the-art downstream performance at the scale of thousands of languages, from high-resource to extremely low-resource varieties. To reach this scale without representation collapse, we use progressive training. We first learn a strong foundational space for 200 languages with an LLM-initialized encoder-decoder, combining token-level decoding with a novel split-softmax contrastive loss and synthetic hard negatives. Building on this foundation, we expand to several thousands language varieties via a two-stage teacher-student encoder distillation framework. Finally, we demonstrate the cross-modal extensibility of this space by seamlessly mapping 177 spoken languages into it. OmniSONAR halves cross-lingual similarity search error on the 200-language FLORES dataset and reduces error by a factor of 15 on the 1,560-language BIBLE benchmark. It also enables strong translation, outperforming NLLB-3B on multilingual benchmarks and exceeding prior models (including much larger LLMs) by 15 chrF++ points on 1,560 languages into English BIBLE translation. OmniSONAR also performs strongly on MTEB and XLCoST. For speech, OmniSONAR achieves a 43% lower similarity-search error and reaches 97% of SeamlessM4T speech-to-text quality, despite being zero-shot for translation (trained only on ASR data). Finally, by training an encoder-decoder LM, Spectrum, exclusively on English text processing OmniSONAR embedding sequences, we unlock high-performance transfer to thousands of languages and speech for complex downstream tasks.

</details>

#### [CAST-TTS: A Simple Cross-Attention Framework for Unified Timbre Control in TTS](https://arxiv.org/abs/2603.16280)
**Zihao Zheng, Wen Wu, Chao Zhang, Mengyue Wu et al.** · 2026-03-17

<details>
<summary>Abstract</summary>

Current Text-to-Speech (TTS) systems typically use separate models for speech-prompted and text-prompted timbre control. While unifying both control signals into a single model is desirable, the challenge of cross-modal alignment often results in overly complex architectures and training objective. To address this challenge, we propose CAST-TTS, a simple yet effective framework for unified timbre control. Features are extracted from speech prompts and text prompts using pre-trained encoders. The multi-stage training strategy efficiently aligns the speech and projected text representations within a shared embedding space. A single cross-attention mechanism then allows the model to use either of these representations to control the timbre. Extensive experiments validate that the unified cross-attention mechanism is critical for achieving high-quality synthesis. CAST-TTS achieves performance comparable to specialized single-input models while operating within a unified architecture. The demo page can be accessed at https://HiRookie9.github.io/CAST-TTS-Page.

</details>

#### [On the Emotion Understanding of Synthesized Speech](https://arxiv.org/abs/2603.16483)
**Yuan Ge, Haishu Zhao, Aokai Hao, Junxiang Zhang et al.** · 2026-03-17

<details>
<summary>Abstract</summary>

Emotion is a core paralinguistic feature in voice interaction. It is widely believed that emotion understanding models learn fundamental representations that transfer to synthesized speech, making emotion understanding results a plausible reward or evaluation metric for assessing emotional expressiveness in speech synthesis. In this work, we critically examine this assumption by systematically evaluating Speech Emotion Recognition (SER) on synthesized speech across datasets, discriminative and generative SER models, and diverse synthesis models. We find that current SER models can not generalize to synthesized speech, largely because speech token prediction during synthesis induces a representation mismatch between synthesized and human speech. Moreover, generative Speech Language Models (SLMs) tend to infer emotion from textual semantics while ignoring paralinguistic cues. Overall, our findings suggest that existing SER models often exploit non-robust shortcuts rather than capturing fundamental features, and paralinguistic understanding in SLMs remains challenging.

</details>

#### [NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation](https://arxiv.org/abs/2603.15352)
**Qinke Ni, Huan Liao, Dekun Chen, Yuxiang Wang et al.** · 2026-03-16

<details>
<summary>Abstract</summary>

While recent text-to-speech (TTS) systems increasingly integrate nonverbal vocalizations (NVs), their evaluations lack standardized metrics and reliable ground-truth references. To bridge this gap, we propose NV-Bench, the first benchmark grounded in a functional taxonomy that treats NVs as communicative acts rather than acoustic artifacts. NV-Bench comprises 1,651 multi-lingual, in-the-wild utterances with paired human reference audio, balanced across 14 NV categories. We introduce a dual-dimensional evaluation protocol: (1) Instruction Alignment, utilizing the proposed paralinguistic character error rate (PCER) to assess controllability, (2) Acoustic Fidelity, measuring the distributional gap to real recordings to assess acoustic realism. We evaluate diverse TTS models and develop two baselines. Experimental results demonstrate a strong correlation between our objective metrics and human perception, establishing NV-Bench as a standardized evaluation framework.

</details>

#### [PhonemeDF: A Synthetic Speech Dataset for Audio Deepfake Detection and Naturalness Evaluation](https://arxiv.org/abs/2603.15037)
**Vamshi Nallaguntla, Aishwarya Fursule, Shruti Kshirsagar, Anderson R. Avila** · 2026-03-16

<details>
<summary>Abstract</summary>

The growing sophistication of speech generated by Artificial Intelligence (AI) has introduced new challenges in audio deepfake detection. Text-to-speech (TTS) and voice conversion (VC) technologies can create highly convincing synthetic speech with naturalness and intelligibility. This poses serious threats to voice biometric security and to systems designed to combat the spread of spoken misinformation, where synthetic voices may be used to disseminate false or malicious content. While interest in AI-generated speech has increased, resources for evaluating naturalness at the phoneme level remain limited. In this work, we address this gap by presenting the Phoneme-Level DeepFake dataset (PhonemeDF), comprising parallel real and synthetic speech segmented at the phoneme level. Real speech samples are derived from a subset of LibriSpeech, while synthetic samples are generated using four TTS and three VC systems. For each system, phoneme-aligned TextGrid files are obtained using the Montreal Forced Aligner (MFA). We compute the Kullback-Leibler divergence (KLD) between real and synthetic phoneme distributions to quantify fidelity and establish a ranking based on similarity to natural speech. Our findings show a clear correlation between the KLD of real and synthetic phoneme distributions and the performance of classifiers trained to distinguish them, suggesting that KLD can serve as an indicator of the most discriminative phonemes for deepfake detection.

</details>

#### [WhispSynth: Scaling Multilingual Whisper Corpus through Real Data Curation and A Novel Pitch-free Generative Framework](https://arxiv.org/abs/2603.14853)
**Tianyi Tan, Jiaxin Ye, Yuanming Zhang, Xiaohuai Le et al.** · 2026-03-16

<details>
<summary>Abstract</summary>

Whisper generation is constrained by the difficulty of data collection. Because whispered speech has low acoustic amplitude, high-fidelity recording is challenging. In this paper, we introduce WhispSynth, a large-scale multilingual corpus constructed via a novel high-fidelity generative framework. Specifically, we propose a pipeline integrating Differentiable Digital Signal Processing (DDSP)-based pitch-free method with Text-to-Speech (TTS) models. This framework refines a comprehensive collection of resources, including our newly constructed WhispNJU dataset, into 118 hours of high-fidelity whispered speech from 479 speakers. Unlike standard synthetic or noisy real data, our data engine faithfully preserves source vocal timbre and linguistic content while ensuring acoustic consistency, providing a robust foundation for text-to-whisper research. Experimental results demonstrate that WhispSynth exhibits significantly higher quality than existing corpora. Moreover, our CosyWhisper, tuned with WhispSynth, achieves speech naturalness on par with ground-truth samples. The official implementation and related resources are available at https://github.com/tan90xx/cosywhisper.

</details>

#### [CodecMOS-Accent: A MOS Benchmark of Resynthesized and TTS Speech from Neural Codecs Across English Accents](https://arxiv.org/abs/2603.14328)
**Wen-Chin Huang, Nicholas Sanders, Erica Cooper** · 2026-03-15

<details>
<summary>Abstract</summary>

We present the CodecMOS-Accent dataset, a mean opinion score (MOS) benchmark designed to evaluate neural audio codec (NAC) models and the large language model (LLM)-based text-to-speech (TTS) models trained upon them, especially across non-standard speech like accented speech. The dataset comprises 4,000 codec resynthesis and TTS samples from 24 systems, featuring 32 speakers spanning ten accents. A large-scale subjective test was conducted to collect 19,600 annotations from 25 listeners across three dimensions: naturalness, speaker similarity, and accent similarity. This dataset does not only represent an up-to-date study of recent speech synthesis system performance but reveals insights including a tight relationship between speaker and accent similarity, the predictive power of objective metrics, and a perceptual bias when listeners share the same accent with the speaker. This dataset is expected to foster research on more human-centric evaluation for NAC and accented TTS.

</details>

#### [DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization](https://arxiv.org/abs/2603.14267)
**Ngoc-Son Nguyen, Thanh V. T. Tran, Jeongsoo Choi, Hieu-Nghia Huynh-Nguyen et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Video dubbing has broad applications in filmmaking, multimedia creation, and assistive speech technology. Existing approaches either train directly on limited dubbing datasets or adopt a two-stage pipeline that adapts pre-trained text-to-speech (TTS) models, which often struggle to produce expressive prosody, rich acoustic characteristics, and precise synchronization. To address these issues, we propose DiFlowDubber with a novel two-stage training framework that effectively transfers knowledge from a pre-trained TTS model to video-driven dubbing, with a discrete flow matching generative backbone. Specifically, we design a FaPro module that captures global prosody and stylistic cues from facial expressions and leverages this information to guide the modeling of subsequent speech attributes. To ensure precise speech-lip synchronization, we introduce a Synchronizer module that bridges the modality gap among text, video, and speech, thereby improving cross-modal alignment and generating speech that is temporally synchronized with lip movements. Experiments on two primary benchmark datasets demonstrate that DiFlowDubber outperforms previous methods across multiple metrics.

</details>

#### [Affectron: Emotional Speech Synthesis with Affective and Contextually Aligned Nonverbal Vocalizations](https://arxiv.org/abs/2603.14432)
**Deok-Hyeon Cho, Hyung-Seok Oh, Seung-Bin Kim, Seong-Whan Lee** · 2026-03-15

<details>
<summary>Abstract</summary>

Nonverbal vocalizations (NVs), such as laughter and sighs, are central to the expression of affective cues in emotional speech synthesis. However, learning diverse and contextually aligned NVs remains challenging in open settings due to limited NV data and the lack of explicit supervision. Motivated by this challenge, we propose Affectron as a framework for affective and contextually aligned NV generation. Built on a small-scale open and decoupled corpus, Affectron introduces an NV-augmented training strategy that expands the distribution of NV types and insertion locations. We further incorporate NV structural masking into a speech backbone pre-trained on purely verbal speech to enable diverse and natural NV synthesis. Experimental results demonstrate that Affectron produces more expressive and diverse NVs than baseline systems while preserving the naturalness of the verbal speech stream.

</details>

#### [The Voice Behind the Words: Quantifying Intersectional Bias in SpeechLLMs](https://arxiv.org/abs/2603.16941)
**Shree Harsha Bokkahalli Satish, Christoph Minixhofer, Maria Teleki, James Caverlee et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Speech Large Language Models (SpeechLLMs) process spoken input directly, retaining cues such as accent and perceived gender that were previously removed in cascaded pipelines. This introduces speaker identity dependent variation in responses. We present a large-scale intersectional evaluation of accent and gender bias in three SpeechLLMs using 2,880 controlled interactions across six English accents and two gender presentations, keeping linguistic content constant through voice cloning. Using pointwise LLM-judge ratings, pairwise comparisons, and Best-Worst Scaling with human validation, we detect consistent disparities. Eastern European-accented speech receives lower helpfulness scores, particularly for female-presenting voices. The bias is implicit: responses remain polite but differ in helpfulness. While LLM judges capture the directional trend of these biases, human evaluators exhibit significantly higher sensitivity, uncovering sharper intersectional disparities.

</details>

#### [Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization](https://arxiv.org/abs/2603.12565)
**Mengjie Zhao, Lianbo Liu, Yusuke Fujita, Hao Shi et al.** · 2026-03-13

<details>
<summary>Abstract</summary>

SpeechLLMs typically combine ASR-trained encoders with text-based LLM backbones, leading them to inherit written-style output patterns unsuitable for text-to-speech synthesis. This mismatch is particularly pronounced in Japanese, where spoken and written registers differ substantially in politeness markers, sentence-final particles, and syntactic complexity. We propose a preference-based alignment approach to adapt Japanese SpeechLLMs for speech-worthy outputs: text that is concise, conversational, and readily synthesized as natural speech. To rigorously evaluate this task, we introduce SpokenElyza, a benchmark for Japanese speech-worthiness derived from ELYZA-tasks-100 with auditory verification by native experts. Experiments show that our approach achieves substantial improvement on SpokenElyza while largely preserving performance on the original written-style evaluation. We will release SpokenElyza to support future research on Japanese spoken dialog systems.

</details>

#### [DAST: A Dual-Stream Voice Anonymization Attacker with Staged Training](https://arxiv.org/abs/2603.12840)
**Ridwan Arefeen, Xiaoxiao Miao, Rong Tong, Aik Beng Ng et al.** · 2026-03-13

<details>
<summary>Abstract</summary>

Voice anonymization masks vocal traits while preserving linguistic content, which may still leak speaker-specific patterns. To assess and strengthen privacy evaluation, we propose a dual-stream attacker that fuses spectral and self-supervised learning features via parallel encoders with a three-stage training strategy. Stage I establishes foundational speaker-discriminative representations. Stage II leverages the shared identity-transformation characteristics of voice conversion and anonymization, exposing the model to diverse converted speech to build cross-system robustness. Stage III provides lightweight adaptation to target anonymized data. Results on the VoicePrivacy Attacker Challenge (VPAC) dataset demonstrate that Stage II is the primary driver of generalization, enabling strong attacking performance on unseen anonymization datasets. With Stage III, fine-tuning on only 10\% of the target anonymization dataset surpasses current state-of-the-art attackers in terms of EER.

</details>

#### [Causal Prosody Mediation for Text-to-Speech:Counterfactual Training of Duration, Pitch, and Energy in FastSpeech2](https://arxiv.org/abs/2603.11683)
**Suvendu Sekhar Mohanty et.al.** · 2026-03-12

<details>
<summary>Abstract</summary>

We propose a novel causal prosody mediation framework for expressive text-to-speech (TTS) synthesis. Our approach augments the FastSpeech2 architecture with explicit emotion conditioning and introduces counterfactual training objectives to disentangle emotional prosody from linguistic content. By formulating a structural causal model of how text (content), emotion, and speaker jointly influence prosody (duration, pitch, energy) and ultimately the speech waveform, we derive two complementary loss terms: an Indirect Path Constraint (IPC) to enforce that emotion affects speech only through prosody, and a Counterfactual Prosody Constraint (CPC) to encourage distinct prosody patterns for different emotions. The resulting model is trained on multi-speaker emotional corpora (LibriTTS, EmoV-DB, VCTK) with a combined objective that includes standard spectrogram reconstruction and variance prediction losses alongside our causal losses. In evaluations on expressive speech synthesis, our method achieves significantly improved prosody manipulation and emotion rendering, with higher mean opinion scores (MOS) and emotion accuracy than baseline FastSpeech2 variants. We also observe better intelligibility (low WER) and speaker consistency when transferring emotions across speakers. Extensive ablations confirm that the causal objectives successfully separate prosody attribution, yielding an interpretable model that allows controlled counterfactual prosody editing (e.g. "same utterance, different emotion") without compromising naturalness. We discuss the implications for identifiability in prosody modeling and outline limitations such as the assumption that emotion effects are fully captured by pitch, duration, and energy. Our work demonstrates how integrating causal learning principles into TTS can improve controllability and expressiveness in generated speech.

</details>

#### [RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis](https://arxiv.org/abs/2603.11678)
**Yongjoon Lee et.al.** · 2026-03-12

<details>
<summary>Abstract</summary>

We propose Relativistic Adversarial Feedback (RAF), a novel training objective for GAN vocoders that improves in-domain fidelity and generalization to unseen scenarios. Although modern GAN vocoders employ advanced architectures, their training objectives often fail to promote generalizable representations. RAF addresses this problem by leveraging speech self-supervised learning models to assist discriminators in evaluating sample quality, encouraging the generator to learn richer representations. Furthermore, we utilize relativistic pairing for real and fake waveforms to improve the modeling of the training data distribution. Experiments across multiple datasets show consistent gains in both objective and subjective metrics on GAN-based vocoders. Importantly, the RAF-trained BigVGAN-base outperforms the LSGAN-trained BigVGAN in perceptual quality using only 12\% of the parameters. Comparative studies further confirm the effectiveness of RAF as a training framework for GAN vocoders.

</details>

#### [Probabilistic Verification of Voice Anti-Spoofing Models](https://arxiv.org/abs/2603.10713)
**Evgeny Kushnir et.al.** · 2026-03-12

<details>
<summary>Abstract</summary>

Recent advances in generative models have amplified the risk of malicious misuse of speech synthesis technologies, enabling adversaries to impersonate target speakers and access sensitive resources. Although speech deepfake detection has progressed rapidly, most existing countermeasures lack formal robustness guarantees or fail to generalize to unseen generation techniques. We propose PV-VASM, a probabilistic framework for verifying the robustness of voice anti-spoofing models (VASMs). PV-VASM estimates the probability of misclassification under text-to-speech (TTS), voice cloning (VC), and parametric signal transformations. The approach is model-agnostic and enables robustness verification against unseen speech synthesis techniques and input perturbations. We derive a theoretical upper bound on the error probability and validate the method across diverse experimental settings, demonstrating its effectiveness as a practical robustness verification tool.

</details>

#### [TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling](https://arxiv.org/abs/2603.12350)
**Liang-Hsuan Tseng, Hung-yi Lee** · 2026-03-12

<details>
<summary>Abstract</summary>

Text-speech joint spoken language modeling (SLM) aims at natural and intelligent speech-based interactions, but developing such a system may suffer from modality mismatch: speech unit sequences are much longer than text tokens. Prior work reduces this gap with text-aligned tokenization and embedding (TASTE), producing speech tokens that align in lengths with their textual counterparts. However, the dependence on an external ASR system and the use of a non-causal decoder limits streaming use. To address this limitation, we propose TASTE-S, a streamable extension of TASTE suitable for real-time usage. TASTE-S integrates a CTC-based ASR module into the encoder for instant dual-modality encoding. We also redesign the unit decoder to enable on-the-fly decoding. With joint training, we show that TASTE-S matches TASTE's performance while significantly reducing latency. Further investigations reveal that TASTE-S remains robust to transcriptions and enables long-form encoding and decoding.

</details>

#### [MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis](https://arxiv.org/abs/2603.12342)
**Tan Dat Nguyen, Sangmin Bae, Joon Son Chung, Ji-Hoon Kim** · 2026-03-12

<details>
<summary>Abstract</summary>

Despite the remarkable quality of LLM-based text-to-speech systems, their reliance on autoregressive Transformers leads to quadratic computational complexity, which severely limits practical applications. Linear-time alternatives, notably Mamba, offer a potential remedy; however, they often sacrifice the global context essential for expressive synthesis. In this paper, we propose MamTra, an interleaved Mamba-Transformer framework designed to leverage the advantages of Mamba's efficiency and Transformers' modeling capability. We also introduce novel knowledge transfer strategies to distill insights from a pretrained Transformer into our hybrid architecture, thereby bypassing the prohibitive costs of training from scratch. Systematic experiments identify the optimal hybrid configuration, and demonstrate that MamTra reduces inference VRAM usage by up to 34% without compromising speech fidelity - even trained on only 2% of the original training dataset. Audio samples are available at https://mamtratts.github.io.

</details>

#### [Toward Complex-Valued Neural Networks for Waveform Generation](https://arxiv.org/abs/2603.11589)
**Hyung-Seok Oh, Deok-Hyeon Cho, Seung-Bin Kim, Seong-Whan Lee** · 2026-03-12

<details>
<summary>Abstract</summary>

Neural vocoders have recently advanced waveform generation, yielding natural and expressive audio. Among these approaches, iSTFT-based vocoders have recently gained attention. They predict a complex-valued spectrogram and then synthesize the waveform via iSTFT, thereby avoiding learned upsampling stages that can increase computational cost. However, current approaches use real-valued networks that process the real and imaginary parts independently. This separation limits their ability to capture the inherent structure of complex spectrograms. We present ComVo, a Complex-valued neural Vocoder whose generator and discriminator use native complex arithmetic. This enables an adversarial training framework that provides structured feedback in complex-valued representations. To guide phase transformations in a structured manner, we introduce phase quantization, which discretizes phase values and regularizes the training process. Finally, we propose a block-matrix computation scheme to improve training efficiency by reducing redundant operations. Experiments demonstrate that ComVo achieves higher synthesis quality than comparable real-valued baselines, and that its block-matrix scheme reduces training time by 25%. Audio samples and code are available at https://hs-oh-prml.github.io/ComVo/.

</details>

#### [RadEar: A Self-Supervised RF Backscatter System for Voice Eavesdropping and Separation](https://arxiv.org/abs/2603.12446)
**Qijun Wang, Peihao Yan, Chunqi Qian, Huacheng Zeng** · 2026-03-12

<details>
<summary>Abstract</summary>

Eavesdropping on voice conversations presents a growing threat to personal privacy and information security. In this paper, we present RadEar, a novel RF backscatter-based system designed to enable covert voice eavesdropping through walls. RadEar consists of two key components: (i) a batteryless RF backscatter tag covertly deployed inside the target space, and (ii) an RF reader located outside the room that performs signal demodulation, voice separation, and denoising. The tag features a compact, dual-resonator design that achieves energy-efficient frequency modulation for continuous voice eavesdropping while mitigating self-interference by separating excitation and reflection frequencies. To overcome the challenges of weak signal reception and overlapping speech, the RF reader employs self-supervised learning models for voice separation and denoising, trained using a remix-based objective without requiring ground-truth labels. We fabricate and evaluate RadEar in real-world scenarios, demonstrating its ability to recover and separate human speech with high fidelity under practical constraints.

</details>

#### [When Fine-Tuning Fails and when it Generalises: Role of Data Diversity and Mixed Training in LLM-based TTS](https://arxiv.org/abs/2603.10904)
**Anupam Purwar et.al.** · 2026-03-11

<details>
<summary>Abstract</summary>

Large language models are increasingly adopted as semantic backbones for neural text-to-speech systems. However, frozen LLM representations are insufficient for modeling speaker specific acoustic and perceptual characteristics. Our experiments involving fine tuning of the Language Model backbone of TTS show promise in improving the voice consistency and Signal to Noise ratio SNR in voice cloning task. Across multiple speakers LoRA finetuning consistently outperforms the non-finetuned base Qwen-0.5B model across three complementary dimensions of speech quality. First, perceptual quality improves significantly with DNS-MOS gains of up to 0.42 points for speakers whose training data exhibits sufficient acoustic variability. Second, speaker fidelity improves for all evaluated speakers with consistent increases in voice similarity indicating that LoRA effectively adapts speaker identity representations without degrading linguistic modeling. Third, signal level quality improves in most cases with signal to noise ratio increasing by as much as 34 percent. Crucially these improvements are strongly governed by the characteristics of the training data. Speakers with high variability in acoustic energy and perceptual quality achieve simultaneous gains in DNS-MOS voice similarity and SNR. Overall this work establishes that LoRA finetuning is not merely a parameter efficient optimization technique but an effective mechanism for better speaker level adaptation in compact LLM-based TTS systems. When supported by sufficiently diverse training data LoRA adapted Qwen-0.5B consistently surpasses its frozen base model in perceptual quality speaker similarity with low latency using GGUF model hosted in quantized form.

</details>

#### [Fish Audio S2 Technical Report](https://arxiv.org/abs/2603.08823)
**Shijia Liao et.al.** · 2026-03-11

<details>
<summary>Abstract</summary>

We introduce Fish Audio S2, an open-sourced text-to-speech system featuring multi-speaker, multi-turn generation, and, most importantly, instruction-following control via natural-language descriptions. To scale training, we develop a multi-stage training recipe together with a staged data pipeline covering video captioning and speech captioning, voice-quality assessment, and reward modeling. To push the frontier of open-source TTS, we release our model weights, fine-tuning code, and an SGLang-based inference engine. The inference engine is production-ready for streaming, achieving an RTF of 0.195 and a time-to-first-audio below 100 ms.Our code and weights are available on GitHub (https://github.com/fishaudio/fish-speech) and Hugging Face (https://huggingface.co/fishaudio/s2-pro). We highly encourage readers to visit https://fish.audio to try custom voices.

</details>

#### [NasoVoce: A Nose-Mounted Low-Audibility Speech Interface for Always-Available Speech Interaction](https://arxiv.org/abs/2603.10324)
**Jun Rekimoto, Yu Nishimura, Bojian Yang** · 2026-03-11

<details>
<summary>Abstract</summary>

Silent and whispered speech offer promise for always-available voice interaction with AI, yet existing methods struggle to balance vocabulary size, wearability, silence, and noise robustness. We present NasoVoce, a nose-bridge-mounted interface that integrates a microphone and a vibration sensor. Positioned at the nasal pads of smart glasses, it unobtrusively captures both acoustic and vibration signals. The nasal bridge, close to the mouth, allows access to bone- and skin-conducted speech and enables reliable capture of low-volume utterances such as whispered speech. While the microphone captures high-quality audio, it is highly sensitive to environmental noise. Conversely, the vibration sensor is robust to noise but yields lower signal quality. By fusing these complementary inputs, NasoVoce generates high-quality speech robust against interference. Evaluation with Whisper Large-v2, PESQ, STOI, and MUSHRA ratings confirms improved recognition and quality. NasoVoce demonstrates the feasibility of a practical interface for always-available, continuous, and discreet AI voice conversations.

</details>

#### [MUGEN: Evaluating and Improving Multi-audio Understanding of Large Audio-Language Models](https://arxiv.org/abs/2603.09714)
**Chih-Kai Yang et.al.** · 2026-03-10

<details>
<summary>Abstract</summary>

While multi-audio understanding is critical for large audio-language models (LALMs), it remains underexplored. We introduce MUGEN, a comprehensive benchmark evaluating this capability across speech, general audio, and music. Our experiments reveal consistent weaknesses in multi-audio settings, and performance degrades sharply as the number of concurrent audio inputs increases, identifying input scaling as a fundamental bottleneck. We further investigate training-free strategies and observe that Audio-Permutational Self-Consistency, which diversifies the order of audio candidates, helps models form more robust aggregated predictions, yielding up to 6.28% accuracy gains. Combining this permutation strategy with Chain-of-Thought further improves performance to 6.74%. These results expose blind spots in current LALMs and provide a foundation for evaluating complex auditory comprehension.

</details>

#### [Speech-Omni-Lite: Portable Speech Interfaces for Vision-Language Models](https://arxiv.org/abs/2603.09627)
**Dehua Tao et.al.** · 2026-03-10

<details>
<summary>Abstract</summary>

While large-scale omni-models have demonstrated impressive capabilities across various modalities, their strong performance heavily relies on massive multimodal data and incurs substantial computational costs. This work introduces Speech-Omni-Lite, a cost-efficient framework for extending pre-trained Visual-Language (VL) backbones with speech understanding and generation capabilities, while fully preserving the backbones' vision-language performance. Specifically, the VL backbone is equipped with two lightweight, trainable plug-and-play modules, a speech projector and a speech token generator, while keeping the VL backbone fully frozen. To mitigate the scarcity of spoken QA corpora, a low-cost data construction strategy is proposed to generate Question-Text Answer-Text-Speech (QTATS) data from existing ASR speech-text pairs, facilitating effective speech generation training. Experimental results show that, even with only thousands of hours of speech training data, Speech-Omni-Lite achieves excellent spoken QA performance, which is comparable to omni-models trained on millions of hours of speech data. Furthermore, the learned speech modules exhibit strong transferability across VL backbones.

</details>

#### [SPAR-K: Scheduled Periodic Alternating Early Exit for Spoken Language Models](https://arxiv.org/abs/2603.09215)
**Hsiao-Ying Huang et.al.** · 2026-03-10

<details>
<summary>Abstract</summary>

Interleaved spoken language models (SLMs) alternately generate text and speech tokens, but decoding at full transformer depth for every step becomes costly, especially due to long speech sequences. We propose SPAR-K, a modality-aware early exit framework designed to accelerate interleaved SLM inference while preserving perceptual quality. SPAR-K introduces a speech alternating-depth schedule: most speech positions exit at a fixed intermediate layer, while periodic full-depth "refresh" steps mitigate distribution shift due to early exit. We evaluate our framework using Step-Audio-2-mini and GLM-4-Voice across four datasets spanning reasoning, factual QA, and dialogue tasks, measuring performance in terms of ASR transcription accuracy and perceptual quality. Experimental results demonstrate that SPAR-K largely preserves question-answering accuracy with a maximum accuracy drop of 0.82\% while reducing average speech decoding depth by up to 11\% on Step-Audio-2-mini and 5\% on GLM-4-Voice, both with negligible changes in MOS and WER and no auxiliary computation overhead. We further demonstrate that confidence-based early exit strategies, widely used in text LLMs, are suboptimal for SLMs, highlighting that the unique statistical nature of speech tokens necessitates a specialized early exit design.

</details>

#### [Emotion-Aware Prefix: Towards Explicit Emotion Control in Voice Conversion Models](https://arxiv.org/abs/2603.09120)
**Haoyuan Yang, Mu Yang, Jiamin Xie, Szu-Jui Chen et al.** · 2026-03-10

<details>
<summary>Abstract</summary>

Recent advances in zero-shot voice conversion have exhibited potential in emotion control, yet the performance is suboptimal or inconsistent due to their limited expressive capacity. We propose Emotion-Aware Prefix for explicit emotion control in a two-stage voice conversion backbone. We significantly improve emotion conversion performance, doubling the baseline Emotion Conversion Accuracy (ECA) from 42.40% to 85.50% while maintaining linguistic integrity and speech quality, without compromising speaker identity. Our ablation study suggests that a joint control of both sequence modulation and acoustic realization is essential to synthesize distinct emotions. Furthermore, comparative analysis verifies the generalizability of proposed method, while it provides insights on the role of acoustic decoupling in maintaining speaker identity.

</details>

#### [ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256)
**Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf et al.** · 2026-03-10

<details>
<summary>Abstract</summary>

Existing video personalization methods preserve visual likeness but treat video and audio separately. Without access to the visual scene, audio models cannot synchronize sounds with on-screen actions; and because classical voice-cloning models condition only on a reference recording, a text prompt cannot redirect speaking style or acoustic environment. We propose ID-LoRA (Identity-Driven In-Context LoRA), which jointly generates a subject's appearance and voice in a single model, letting a text prompt, a reference image, and a short audio clip govern both modalities together. ID-LoRA adapts the LTX-2 joint audio-video diffusion backbone via parameter-efficient In-Context LoRA and, to our knowledge, is the first method to personalize visual appearance and voice in a single generative pass. Two challenges arise. Reference and generation tokens share the same positional-encoding space, making them hard to distinguish; we address this with negative temporal positions, placing reference tokens in a disjoint RoPE region while preserving their internal temporal structure. Speaker characteristics also tend to be diluted during denoising; we introduce identity guidance, a classifier-free guidance variant that amplifies speaker-specific features by contrasting predictions with and without the reference signal. In human preference studies, ID-LoRA is preferred over Kling 2.6 Pro by 73% of annotators for voice similarity and 65% for speaking style. On cross-environment settings, speaker similarity improves by 24% over Kling, with the gap widening as conditions diverge. A preliminary user study further suggests that joint generation provides a useful inductive bias for physically grounded sound synthesis. ID-LoRA achieves these results with only ~3K training pairs on a single GPU. Code, models, and data will be released.

</details>

#### [Universal Speech Content Factorization](https://arxiv.org/abs/2603.08977)
**Henry Li Xinyuan et.al.** · 2026-03-09

<details>
<summary>Abstract</summary>

We propose Universal Speech Content Factorization (USCF), a simple and invertible linear method for extracting a low-rank speech representation in which speaker timbre is suppressed while phonetic content is preserved. USCF extends Speech Content Factorization, a closed-set voice conversion (VC) method, to an open-set setting by learning a universal speech-to-content mapping via least-squares optimization and deriving speaker-specific transformations from only a few seconds of target speech. We show through embedding analysis that USCF effectively removes speaker-dependent variation. As a zero-shot VC system, USCF achieves competitive intelligibility, naturalness, and speaker similarity compared to methods that require substantially more target-speaker data or additional neural training. Finally, we demonstrate that as a training-efficient timbre-disentangled speech feature, USCF features can serve as the acoustic representation for training timbre-prompted text-to-speech models. Speech samples and code are publicly available.

</details>

#### [Using Multimodal and Language-Agnostic Sentence Embeddings for Abstractive Summarization](https://arxiv.org/abs/2603.08282)
**Chaimae Chellaf et.al.** · 2026-03-09

<details>
<summary>Abstract</summary>

Abstractive summarization aims to generate concise summaries by creating new sentences, allowing for flexible rephrasing. However, this approach can be vulnerable to inaccuracies, particularly `hallucinations' where the model introduces non-existent information. In this paper, we leverage the use of multimodal and multilingual sentence embeddings derived from pretrained models such as LaBSE, SONAR, and BGE-M3, and feed them into a modified BART-based French model. A Named Entity Injection mechanism that appends tokenized named entities to the decoder input is introduced, in order to improve the factual consistency of the generated summary. Our novel framework, SBARThez, is applicable to both text and speech inputs and supports cross-lingual summarization; it shows competitive performance relative to token-level baselines, especially for low-resource languages, while generating more concise and abstract summaries.

</details>

#### [Scalable Neural Vocoder from Range-Null Space Decomposition](https://arxiv.org/abs/2603.08574)
**Andong Li, Tong Lei, Zhihang Sun, Rilin Chen et al.** · 2026-03-09

<details>
<summary>Abstract</summary>

Although deep neural networks have facilitated significant progress of neural vocoders in recent years, they usually suffer from intrinsic challenges like opaque modeling, inflexible retraining under different input configurations, and parameter-performance trade-off. These inherent hurdles can heavily impede the development of this field. To resolve these problems, in this paper, we propose a novel neural vocoder in the time-frequency (T-F) domain. Specifically, we bridge the connection between the classical range-null decomposition (RND) theory and the vocoder task, where the reconstruction of the target spectrogram is formulated into the superimposition between range-space and null-space. The former aims to project the representation in the original mel-domain into the target linear-scale domain, and the latter can be instantiated via neural networks to further infill the spectral details. To fully leverage the spectrum prior, an elaborate dual-path framework is devised, where the spectrum is hierarchically encoded and decoded, and the cross- and narrow-band modules are leveraged for effectively modeling along sub-band and time dimensions. To enable inference under various configurations, we propose a simple yet effective strategy, which transforms the multi-condition adaption in the inference stage into the data augmentation in the training stage. Comprehensive experiments are conducted on various benchmarks. Quantitative and qualitative results show that while enjoying lightweight network structure and scalable inference paradigm, the proposed framework achieves state-ofthe-art performance among existing advanced methods. Code is available at https://github.com/Andong-Li-speech/RNDVoC.

</details>

#### [Targeted Speaker Poisoning Framework in Zero-Shot Text-to-Speech](https://arxiv.org/abs/2603.07551)
**Thanapat Trachu et.al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Zero-shot Text-to-Speech (TTS) voice cloning poses severe privacy risks, demanding the removal of specific speaker identities from trained TTS models. Conventional machine unlearning is insufficient in this context, as zero-shot TTS can dynamically reconstruct voices from just reference prompts. We formalize this task as Speech Generation Speaker Poisoning (SGSP), in which we modify trained models to prevent the generation of specific identities while preserving utility for other speakers. We evaluate inference-time filtering and parameter-modification baselines across 1, 15, and 100 forgotten speakers. Performance is assessed through the trade-off between utility (WER) and privacy, quantified using AUC and Forget Speaker Similarity (FSSIM). We achieve strong privacy for up to 15 speakers but reveal scalability limits at 100 speakers due to increased identity overlap. Our study thus introduces a novel problem and evaluation framework toward further advances in generative voice privacy.

</details>

#### [Learning-free L2-Accented Speech Generation using Phonological Rules](https://arxiv.org/abs/2603.07550)
**Thanathai Lertpetchpun et.al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Accent plays a crucial role in speaker identity and inclusivity in speech technologies. Existing accented text-to-speech (TTS) systems either require large-scale accented datasets or lack fine-grained phoneme-level controllability. We propose a accented TTS framework that combines phonological rules with a multilingual TTS model. The rules are applied to phoneme sequences to transform accent at the phoneme level while preserving intelligibility. The method requires no accented training data and enables explicit phoneme-level accent manipulation. We design rule sets for Spanish- and Indian-accented English, modeling systematic differences in consonants, vowels, and syllable structure arising from phonotactic constraints. We analyze the trade-off between phoneme-level duration alignment and accent as realized in speech timing. Experimental results demonstrate effective accent shift while maintaining speech quality.

</details>

#### [Accent Vector: Controllable Accent Manipulation for Multilingual TTS Without Accented Data](https://arxiv.org/abs/2603.07534)
**Thanathai Lertpetchpun et.al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Accent is an integral part of society, reflecting multiculturalism and shaping how individuals express identity. The majority of English speakers are non-native (L2) speakers, yet current Text-To-Speech (TTS) systems primarily model American-accented English due limited accented data. We propose \textit{Accent Vector}, a controllable representation that enables accent manipulation in multilingual TTS without requiring accented training data. \textit{Accent Vector} is derived by fine-tuning a TTS system on native speech of a different language (i.e. non-English) and computing task vectors capturing accent characteristics (i.e. in English). By scaling and interpolating the vector, we achieve fine-grained control over accent strength and generate mixed-accent speech. In addition, it generalizes beyond English, enabling accent control across multiple languages. Objective and human evaluations confirm the effectiveness of Accent Vector for fine-grained and compositional accent control.

</details>

#### [Bolbosh: Script-Aware Flow Matching for Kashmiri Text-to-Speech](https://arxiv.org/abs/2603.07513)
**Tajamul Ashraf et.al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Kashmiri is spoken by around 7 million people but remains critically underserved in speech technology, despite its official status and rich linguistic heritage. The lack of robust Text-to-Speech (TTS) systems limits digital accessibility and inclusive human-computer interaction for native speakers. In this work, we present the first dedicated open-source neural TTS system designed for Kashmiri. We show that zero-shot multilingual baselines trained for Indic languages fail to produce intelligible speech, achieving a Mean Opinion Score (MOS) of only 1.86, largely due to inadequate modeling of Perso-Arabic diacritics and language-specific phonotactics. To address these limitations, we propose Bolbosh, a supervised cross-lingual adaptation strategy based on Optimal Transport Conditional Flow Matching (OT-CFM) within the Matcha-TTS framework. This enables stable alignment under limited paired data. We further introduce a three-stage acoustic enhancement pipeline consisting of dereverberation, silence trimming, and loudness normalization to unify heterogeneous speech sources and stabilize alignment learning. The model vocabulary is expanded to explicitly encode Kashmiri graphemes, preserving fine-grained vowel distinctions. Our system achieves a MOS of 3.63 and a Mel-Cepstral Distortion (MCD) of 3.73, substantially outperforming multilingual baselines and establishing a new benchmark for Kashmiri speech synthesis. Our results demonstrate that script-aware and supervised flow-based adaptation are critical for low-resource TTS in diacritic-sensitive languages. Code and data are available at: https://github.com/gaash-lab/Bolbosh.

</details>

#### [The Talking Robot: Distortion-Robust Acoustic Models for Robot-Robot Communication](https://arxiv.org/abs/2603.07072)
**Hanlong Li et.al.** · 2026-03-07


#### [Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision](https://arxiv.org/abs/2603.07025)
**Shreyas Gopal et.al.** · 2026-03-07


#### [Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input](https://arxiv.org/abs/2603.06444)
**Changsong Liu et.al.** · 2026-03-06


#### [Is it Me? Toward Self-Extension to AI Avatars in Virtual Reality](https://arxiv.org/abs/2603.06030)
**Jieying Zhang et.al.** · 2026-03-06


#### [Activation Steering for Accent-Neutralized Zero-Shot Text-To-Speech](https://arxiv.org/abs/2603.05977)
**Mu Yang et.al.** · 2026-03-06


#### [How Well Do Current Speech Deepfake Detection Methods Generalize to the Real World?](https://arxiv.org/abs/2603.05852)
**Daixian Li et.al.** · 2026-03-06


#### [StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800)
**Haoran Qiu et.al.** · 2026-03-06


#### [Let's Talk, Not Type: An Oral-First Multi-Agent Architecture for Guaraní](https://arxiv.org/abs/2603.05743)
**Samantha Adorno et.al.** · 2026-03-05


#### [Hierarchical Decoding for Discrete Speech Synthesis with Multi-Resolution Spoof Detection](https://arxiv.org/abs/2603.05373)
**Junchuan Zhao et.al.** · 2026-03-05


#### [WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation](https://arxiv.org/abs/2603.05299)
**Luca Della Libera et.al.** · 2026-03-05


#### [Measuring the Redundancy of Decoder Layers in SpeechLLMs](https://arxiv.org/abs/2603.05121)
**Adel Moumen et.al.** · 2026-03-05


#### [ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis](https://arxiv.org/abs/2603.04219)
**Youngwon Choi et.al.** · 2026-03-04


#### [VietNormalizer: An Open-Source, Dependency-Free Python Library for Vietnamese Text Normalization in TTS and NLP Applications](https://arxiv.org/abs/2603.04145)
**Hung Vu Nguyen et.al.** · 2026-03-04


#### [Scalable Multilingual Multimodal Machine Translation with Speech-Text Fusion](https://arxiv.org/abs/2602.21646)
**Yexing Du et.al.** · 2026-03-03


#### [More Data, Fewer Diacritics: Scaling Arabic TTS](https://arxiv.org/abs/2603.01622)
**Ahmed Musleh et.al.** · 2026-03-02


#### [End-to-End Simultaneous Dysarthric Speech Reconstruction with Frame-Level Adaptor and Multiple Wait-k Knowledge Distillation](https://arxiv.org/abs/2603.01382)
**Minghui Wu et.al.** · 2026-03-02


#### [DARS: Dysarthria-Aware Rhythm-Style Synthesis for ASR Enhancement](https://arxiv.org/abs/2603.01369)
**Minghui Wu et.al.** · 2026-03-02


#### [S-VoCAL: A Dataset and Evaluation Framework for Inferring Speaking Voice Character Attributes in Literature](https://arxiv.org/abs/2603.00958)
**Abigail Berthe-Pardo et.al.** · 2026-03-01


#### [Deepfake Word Detection by Next-token Prediction using Fine-tuned Whisper](https://arxiv.org/abs/2602.22658)
**Hoan My Tran et.al.** · 2026-02-28


#### [Discourse-Aware Dual-Track Streaming Response for Low-Latency Spoken Dialogue Systems](https://arxiv.org/abs/2602.23266)
**Siyuan Liu et.al.** · 2026-02-26


#### [TADA: A Generative Framework for Speech Modeling via Text-Acoustic Dual Alignment](https://arxiv.org/abs/2602.23068)
**Trung Dang et.al.** · 2026-02-26


#### [Giving Meaning to Movements: Challenges and Opportunities in Expanding Communication by Pairing Unaided AAC with Speech Generated Messages](https://arxiv.org/abs/2602.22131)
**Imran Kabir et.al.** · 2026-02-25


#### [The Design Space of Tri-Modal Masked Diffusion Models](https://arxiv.org/abs/2602.21472)
**Louis Bethune et.al.** · 2026-02-25


#### [MIDI-Informed Singing Accompaniment Generation in a Compositional Song Pipeline](https://arxiv.org/abs/2602.22029)
**Fang-Duo Tsai et.al.** · 2026-02-24


#### [Can You Tell It's AI? Human Perception of Synthetic Voices in Vishing Scenarios](https://arxiv.org/abs/2602.20061)
**Zoha Hayat Bhatti et.al.** · 2026-02-23


#### [CTC-TTS: LLM-based dual-streaming text-to-speech with CTC alignment](https://arxiv.org/abs/2602.19574)
**Hanwen Liu et.al.** · 2026-02-23


#### [CC-G2PnP: Streaming Grapheme-to-Phoneme and prosody with Conformer-CTC for unsegmented languages](https://arxiv.org/abs/2602.17157)
**Yuma Shirahata et.al.** · 2026-02-19


#### [How to Label Resynthesized Audio: The Dual Role of Neural Audio Codecs in Audio Deepfake Detection](https://arxiv.org/abs/2602.16343)
**Yixuan Xiao et.al.** · 2026-02-18


#### [LLM-to-Speech: A Synthetic Data Pipeline for Training Dialectal Text-to-Speech Models](https://arxiv.org/abs/2602.15675)
**Ahmed Khaled Khamis et.al.** · 2026-02-17


#### [UniTAF: A Modular Framework for Joint Text-to-Speech and Audio-to-Face Modeling](https://arxiv.org/abs/2602.15651)
**Qiangong Zhou et.al.** · 2026-02-17


#### [Disentangling Pitch and Creak for Speaker Identity Preservation in Speech Synthesis](https://arxiv.org/abs/2602.14686)
**Frederik Rautenberg et.al.** · 2026-02-16


#### [Probing Human Articulatory Constraints in End-to-End TTS with Reverse and Mismatched Speech-Text Directions](https://arxiv.org/abs/2602.14664)
**Parth Khadse et.al.** · 2026-02-16


#### ["Sorry, I Didn't Catch That": How Speech Models Miss What Matters Most](https://arxiv.org/abs/2602.12249)
**Kaitlyn Zhou et.al.** · 2026-02-16


#### [GSRM: Generative Speech Reward Model for Speech RLHF](https://arxiv.org/abs/2602.13891)
**Maohao Shen et.al.** · 2026-02-14


#### [Learning Vocal-Tract Area and Radiation with a Physics-Informed Webster Model](https://arxiv.org/abs/2602.13834)
**Minhui Lu et.al.** · 2026-02-14


#### [PISHYAR: A Socially Intelligent Smart Cane for Indoor Social Navigation and Multimodal Human-Robot Interaction for Visually Impaired People](https://arxiv.org/abs/2602.12597)
**Mahdi Haghighat Joo et.al.** · 2026-02-13


#### [When Audio-LLMs Don't Listen: A Cross-Linguistic Study of Modality Arbitration](https://arxiv.org/abs/2602.11488)
**Jayadev Billa et.al.** · 2026-02-12


#### [SLD-L2S: Hierarchical Subspace Latent Diffusion for High-Fidelity Lip to Speech Synthesis](https://arxiv.org/abs/2602.11477)
**Yifan Liang et.al.** · 2026-02-12


#### [Calliope: A TTS-based Narrated E-book Creator Ensuring Exact Synchronization, Privacy, and Layout Fidelity](https://arxiv.org/abs/2602.10735)
**Hugo L. Hammer et.al.** · 2026-02-11


#### [Emotion-Coherent Speech Data Augmentation and Self-Supervised Contrastive Style Training for Enhancing Kids's Story Speech Synthesis](https://arxiv.org/abs/2602.10164)
**Raymond Chung et.al.** · 2026-02-10


#### [Covo-Audio Technical Report](https://arxiv.org/abs/2602.09823)
**Wenfu Wang et.al.** · 2026-02-10


#### [TVTSyn: Content-Synchronous Time-Varying Timbre for Streaming Voice Conversion and Anonymization](https://arxiv.org/abs/2602.09389)
**Waris Quamer et.al.** · 2026-02-10


#### [Prototype-Based Disentanglement for Controllable Dysarthric Speech Synthesis](https://arxiv.org/abs/2602.08696)
**Haoshen Wang et.al.** · 2026-02-09


#### [Tutti: Expressive Multi-Singer Synthesis via Structure-Level Timbre Control and Vocal Texture Modeling](https://arxiv.org/abs/2602.08233)
**Jiatao Chen et.al.** · 2026-02-09


#### [SoulX-Singer: Towards High-Quality Zero-Shot Singing Voice Synthesis](https://arxiv.org/abs/2602.07803)
**Jiale Qian et.al.** · 2026-02-08


#### [Zero-Shot TTS With Enhanced Audio Prompts: Bsc Submission For The 2026 Wildspoof Challenge TTS Track](https://arxiv.org/abs/2602.05770)
**Jose Giraldo et.al.** · 2026-02-05


#### [Wave-Trainer-Fit: Neural Vocoder with Trainable Prior and Fixed-Point Iteration towards High-Quality Speech Generation from SSL features](https://arxiv.org/abs/2602.05443)
**Hien Ohnaka et.al.** · 2026-02-05


#### [ARCHI-TTS: A flow-matching-based Text-to-Speech Model with Self-supervised Semantic Aligner and Accelerated Inference](https://arxiv.org/abs/2602.05207)
**Chunyat Wu et.al.** · 2026-02-05


#### [HoliAntiSpoof: Audio LLM for Holistic Speech Anti-Spoofing](https://arxiv.org/abs/2602.04535)
**Xuenan Xu et.al.** · 2026-02-04


#### [PFluxTTS: Hybrid Flow-Matching TTS with Robust Cross-Lingual Voice Cloning and Inference-Time Model Fusion](https://arxiv.org/abs/2602.04160)
**Vikentii Pankov et.al.** · 2026-02-04


#### [WAXAL: A Large-Scale Multilingual African Language Speech Corpus](https://arxiv.org/abs/2602.02734)
**Abdoulaye Diack et.al.** · 2026-02-04


#### [CoCoEmo: Composable and Controllable Human-Like Emotional TTS via Activation Steering](https://arxiv.org/abs/2602.03420)
**Siyi Wang et.al.** · 2026-02-03


#### [LipSody: Lip-to-Speech Synthesis with Enhanced Prosody Consistency](https://arxiv.org/abs/2602.01908)
**Jaejun Lee et.al.** · 2026-02-02


#### [VividVoice: A Unified Framework for Scene-Aware Visually-Driven Speech Synthesis](https://arxiv.org/abs/2602.02591)
**Chengyuan Ma et.al.** · 2026-02-01


#### [EmoAra: Emotion-Preserving English Speech Transcription and Cross-Lingual Translation with Arabic Text-to-Speech](https://arxiv.org/abs/2602.01170)
**Besher Hassan et.al.** · 2026-02-01


#### [Bias in the Ear of the Listener: Assessing Sensitivity in Audio Language Models Across Linguistic, Demographic, and Positional Variations](https://arxiv.org/abs/2602.01030)
**Sheng-Lun Wei et.al.** · 2026-02-01


#### [Edit Content, Preserve Acoustics: Imperceptible Text-Based Speech Editing via Self-Consistency Rewards](https://arxiv.org/abs/2602.00560)
**Yong Ren et.al.** · 2026-01-31


#### [Multi-Speaker Conversational Audio Deepfake: Taxonomy, Dataset and Pilot Study](https://arxiv.org/abs/2602.00295)
**Alabi Ahmed et.al.** · 2026-01-30


#### [Now You Hear Me: Audio Narrative Attacks Against Large Audio-Language Models](https://arxiv.org/abs/2601.23255)
**Ye Yu et.al.** · 2026-01-30


#### [EmoShift: Lightweight Activation Steering for Enhanced Emotion-Aware Speech Synthesis](https://arxiv.org/abs/2601.22873)
**Li Zhou et.al.** · 2026-01-30


#### [Evaluating and Rewarding LALMs for Expressive Role-Play TTS via Mean Continuation Log-Probability](https://arxiv.org/abs/2601.22661)
**Yong Ren et.al.** · 2026-01-30


#### [Speech Quality-Based Localization of Low-Quality Speech and Text-to-Speech Synthesis Artefacts](https://arxiv.org/abs/2601.21886)
**Michael Kuhlmann et.al.** · 2026-01-29


#### [Unit-Based Agent for Semi-Cascaded Full-Duplex Dialogue Systems](https://arxiv.org/abs/2601.20230)
**Haoyuan Yu et.al.** · 2026-01-29


#### [Audio Deepfake Detection in the Age of Advanced Text-to-Speech models](https://arxiv.org/abs/2601.20510)
**Robin Singh et.al.** · 2026-01-28


#### [Erasing Your Voice Before It's Heard: Training-free Speaker Unlearning for Zero-shot Text-to-Speech](https://arxiv.org/abs/2601.20481)
**Myungjin Lee et.al.** · 2026-01-28


#### [ASR for Affective Speech: Investigating Impact of Emotion and Speech Generative Strategy](https://arxiv.org/abs/2601.20319)
**Ya-Tse Wu et.al.** · 2026-01-28


#### [T-Mimi: A Transformer-based Mimi Decoder for Real-Time On-Phone TTS](https://arxiv.org/abs/2601.20094)
**Haibin Wu et.al.** · 2026-01-27


#### [Rethinking Discrete Speech Representation Tokens for Accent Generation](https://arxiv.org/abs/2601.19786)
**Jinzuomu Zhong et.al.** · 2026-01-27


#### [Phonological Tokenizer: Prosody-Aware Phonetic Token via Multi-Objective Fine-Tuning with Differentiable K-Means](https://arxiv.org/abs/2601.19781)
**Kentaro Onda et.al.** · 2026-01-27


#### [Neural Multi-Speaker Voice Cloning for Nepali in Low-Resource Settings](https://arxiv.org/abs/2601.18694)
**Aayush M. Shrestha et.al.** · 2026-01-26


#### [UrgentMOS: Unified Multi-Metric and Preference Learning for Robust Speech Quality Assessment](https://arxiv.org/abs/2601.18438)
**Wei Wang et.al.** · 2026-01-26


#### [Quran-MD: A Fine-Grained Multilingual Multimodal Dataset of the Quran](https://arxiv.org/abs/2601.17880)
**Muhammad Umar Salman et.al.** · 2026-01-25


#### [AR-Omni: A Unified Autoregressive Model for Any-to-Any Generation](https://arxiv.org/abs/2601.17761)
**Dongjie Cheng et.al.** · 2026-01-25


#### [SonoEdit: Null-Space Constrained Knowledge Editing for Pronunciation Correction in LLM-Based TTS](https://arxiv.org/abs/2601.17086)
**Ayush Pratap Singh et.al.** · 2026-01-23


#### [Timbre-Aware LLM-based Direct Speech-to-Speech Translation Extendable to Multiple Language Pairs](https://arxiv.org/abs/2601.16023)
**Lalaram Arya et.al.** · 2026-01-22


#### [Qwen3-TTS Technical Report](https://arxiv.org/abs/2601.15621)
**Hangrui Hu et.al.** · 2026-01-22


#### [DeepASMR: LLM-Based Zero-Shot ASMR Speech Generation for Anyone of Any Voice](https://arxiv.org/abs/2601.15596)
**Leying Zhang et.al.** · 2026-01-22


#### [Prosody-Guided Harmonic Attention for Phase-Coherent Neural Vocoding in the Complex Spectrum](https://arxiv.org/abs/2601.14472)
**Mohammed Salah Al-Radhi et.al.** · 2026-01-20


#### [Quantifying Speaker Embedding Phonological Rule Interactions in Accented Speech Synthesis](https://arxiv.org/abs/2601.14417)
**Thanathai Lertpetchpun et.al.** · 2026-01-20


#### [Synthetic Singers: A Review of Deep-Learning-based Singing Voice Synthesis Approaches](https://arxiv.org/abs/2601.13910)
**Changhao Pan et.al.** · 2026-01-20


#### [Habibi: Laying the Open-Source Foundation of Unified-Dialectal Arabic Speech Synthesis](https://arxiv.org/abs/2601.13802)
**Yushen Chen et.al.** · 2026-01-20


#### [HoverAI: An Embodied Aerial Agent for Natural Human-Drone Interaction](https://arxiv.org/abs/2601.13801)
**Yuhua Jin et.al.** · 2026-01-20


#### [Lombard Speech Synthesis for Any Voice with Controllable Style Embeddings](https://arxiv.org/abs/2601.12966)
**Seymanur Akti et.al.** · 2026-01-19


#### [A Unified Neural Codec Language Model for Selective Editable Text to Speech Generation](https://arxiv.org/abs/2601.12480)
**Hanchen Pei et.al.** · 2026-01-18


#### [ParaMETA: Towards Learning Disentangled Paralinguistic Speaking Styles Representations from Speech](https://arxiv.org/abs/2601.12289)
**Haowei Lou et.al.** · 2026-01-18


#### [Confidence-based Filtering for Speech Dataset Curation with Generative Speech Enhancement Using Discrete Tokens](https://arxiv.org/abs/2601.12254)
**Kazuki Yamauchi et.al.** · 2026-01-18


#### [F-Actor: Controllable Conversational Behaviour in Full-Duplex Models](https://arxiv.org/abs/2601.11329)
**Maike Züfle et.al.** · 2026-01-16


#### [FlashLabs Chroma 1.0: A Real-Time End-to-End Spoken Dialogue Model with Personalized Voice Cloning](https://arxiv.org/abs/2601.11141)
**Tanyu Chen et.al.** · 2026-01-16


#### [WenetSpeech-Wu: Datasets, Benchmarks, and Models for a Unified Chinese Wu Dialect Speech Processing Ecosystem](https://arxiv.org/abs/2601.11027)
**Chengyou Wang et.al.** · 2026-01-16


#### [VoiceSculptor: Your Voice, Designed By You](https://arxiv.org/abs/2601.10629)
**Jingbin Hu et.al.** · 2026-01-15


#### [DSA-Tokenizer: Disentangled Semantic-Acoustic Tokenization via Flow Matching-based Hierarchical Fusion](https://arxiv.org/abs/2601.09239)
**Hanlin Zhang et.al.** · 2026-01-15


#### [ESDD2: Environment-Aware Speech and Sound Deepfake Detection Challenge Evaluation Plan](https://arxiv.org/abs/2601.07303)
**Xueping Zhang et.al.** · 2026-01-15


#### [Afri-MCQA: Multimodal Cultural Question Answering for African Languages](https://arxiv.org/abs/2601.05699)
**Atnafu Lambebo Tonja et.al.** · 2026-01-14


#### [Decoding Order Matters in Autoregressive Speech Synthesis](https://arxiv.org/abs/2601.08450)
**Minghui Zhao et.al.** · 2026-01-13


#### [Detecting Mental Manipulation in Speech via Synthetic Multi-Speaker Dialogue](https://arxiv.org/abs/2601.08342)
**Run Chen et.al.** · 2026-01-13


#### [FOCAL: A Novel Benchmarking Technique for Multi-modal Agents](https://arxiv.org/abs/2601.07367)
**Aditya Choudhary et.al.** · 2026-01-12


#### [Bridging Attribution and Open-Set Detection using Graph-Augmented Instance Learning in Synthetic Speech](https://arxiv.org/abs/2601.07064)
**Mohd Mujtaba Akhtar et.al.** · 2026-01-11


#### [Lightweight Resolution-Aware Audio Deepfake Detection via Cross-Scale Attention and Consistency Learning](https://arxiv.org/abs/2601.06560)
**K. A. Shahriar et.al.** · 2026-01-10


#### [Pantagruel: Unified Self-Supervised Encoders for French Text and Speech](https://arxiv.org/abs/2601.05911)
**Phuong-Hang Le et.al.** · 2026-01-09


#### [SPAM: Style Prompt Adherence Metric for Prompt-based TTS](https://arxiv.org/abs/2601.05554)
**Chanhee Cho et.al.** · 2026-01-09


#### [IndexTTS 2.5 Technical Report](https://arxiv.org/abs/2601.03888)
**Yunpei Li et.al.** · 2026-01-09


#### [CosyEdit: Unlocking End-to-End Speech Editing Capability from Zero-Shot Text-to-Speech Models](https://arxiv.org/abs/2601.05329)
**Junyang Chen et.al.** · 2026-01-08


#### [FlexiVoice: Enabling Flexible Style Control in Zero-Shot TTS with Natural Language Instructions](https://arxiv.org/abs/2601.04656)
**Dekun Chen et.al.** · 2026-01-08


#### [SpeakerSleuth: Evaluating Large Audio-Language Models as Judges for Multi-turn Speaker Consistency](https://arxiv.org/abs/2601.04029)
**Jonggeun Lee et.al.** · 2026-01-07


#### [Domain Adaptation of the Pyannote Diarization Pipeline for Conversational Indonesian Audio](https://arxiv.org/abs/2601.03684)
**Muhammad Daffa'i Rafi Prasetyo et.al.** · 2026-01-07


#### [ReStyle-TTS: Relative and Continuous Style Control for Zero-Shot Speech Synthesis](https://arxiv.org/abs/2601.03632)
**Haitao Li et.al.** · 2026-01-07


#### [Tigrinya Number Verbalization: Rules, Algorithm, and Implementation](https://arxiv.org/abs/2601.03403)
**Fitsum Gaim et.al.** · 2026-01-06


#### [Segment-Aware Conditioning for Training-Free Intra-Utterance Emotion and Duration Control in Text-to-Speech](https://arxiv.org/abs/2601.03170)
**Qifan Liang et.al.** · 2026-01-06


#### [XLSR-MamBo: Scaling the Hybrid Mamba-Attention Backbone for Audio Deepfake Detection](https://arxiv.org/abs/2601.02944)
**Kwok-Ho Ng et.al.** · 2026-01-06


#### [Vulnerabilities of Audio-Based Biometric Authentication Systems Against Deepfake Speech Synthesis](https://arxiv.org/abs/2601.02914)
**Mengze Hong et.al.** · 2026-01-06


#### [Vclip: Face-based Speaker Generation by Face-voice Association Learning](https://arxiv.org/abs/2601.02753)
**Yao Shi et.al.** · 2026-01-06


#### [VocalBridge: Latent Diffusion-Bridge Purification for Defeating Perturbation-Based Voiceprint Defenses](https://arxiv.org/abs/2601.02444)
**Maryam Abbasihafshejani et.al.** · 2026-01-05


#### [Towards Prosodically Informed Mizo TTS without Explicit Tone Markings](https://arxiv.org/abs/2601.02073)
**Abhijit Mohanta et.al.** · 2026-01-05


#### [MM-Sonate: Multimodal Controllable Audio-Video Generation with Zero-Shot Voice Cloning](https://arxiv.org/abs/2601.01568)
**Chunyu Qiang et.al.** · 2026-01-04


#### [OV-InstructTTS: Towards Open-Vocabulary Instruct Text-to-Speech](https://arxiv.org/abs/2601.01459)
**Yong Ren et.al.** · 2026-01-04


#### [DepFlow: Disentangled Speech Generation to Mitigate Semantic Bias in Depression Detection](https://arxiv.org/abs/2601.00303)
**Yuxin Li et.al.** · 2026-01-01


#### [Latent Flow Matching for Expressive Singing Voice Synthesis](https://arxiv.org/abs/2601.00217)
**Minhyeok Yun et.al.** · 2026-01-01



### 2025

#### [Fun-Audio-Chat Technical Report](https://arxiv.org/abs/2512.20156)
**Tongyi Fun Team et.al.** · 2025-12-30


#### [AI4Reading: Chinese Audiobook Interpretation System Based on Multi-Agent Collaboration](https://arxiv.org/abs/2512.23300)
**Minjiang Huang et.al.** · 2025-12-29


#### [ManchuTTS: Towards High-Quality Manchu Speech Synthesis via Flow Matching and Hierarchical Text Representation](https://arxiv.org/abs/2512.22491)
**Suhua Wang et.al.** · 2025-12-27


#### [Zero-Shot to Zero-Lies: Detecting Bengali Deepfake Audio through Transfer Learning](https://arxiv.org/abs/2512.21702)
**Most. Sharmin Sultana Samu et.al.** · 2025-12-25


#### [Hearing to Translate: The Effectiveness of Speech Modality Integration into LLMs](https://arxiv.org/abs/2512.16378)
**Sara Papi et.al.** · 2025-12-24


#### [TAVID: Text-Driven Audio-Visual Interactive Dialogue Generation](https://arxiv.org/abs/2512.20296)
**Ji-Hoon Kim et.al.** · 2025-12-23


#### [JoyVoice: Long-Context Conditioning for Anthropomorphic Multi-Speaker Conversational Synthesis](https://arxiv.org/abs/2512.19090)
**Fan Yu et.al.** · 2025-12-22


#### [Smark: A Watermark for Text-to-Speech Diffusion Models via Discrete Wavelet Transform](https://arxiv.org/abs/2512.18791)
**Yichuan Zhang et.al.** · 2025-12-21


#### [Task Vector in TTS: Toward Emotionally Expressive Dialectal Speech Synthesis](https://arxiv.org/abs/2512.18699)
**Pengchao Feng et.al.** · 2025-12-21


#### [Training Text-to-Speech Model with Purely Synthetic Data: Feasibility, Sensitivity, and Generalization Capability](https://arxiv.org/abs/2512.17356)
**Tingxiao Zhou et.al.** · 2025-12-19


#### [Robust TTS Training via Self-Purifying Flow Matching for the WildSpoof 2026 TTS Track](https://arxiv.org/abs/2512.17293)
**June Young Yi et.al.** · 2025-12-19


#### [A stylometric analysis of speaker attribution from speech transcripts](https://arxiv.org/abs/2512.13667)
**Cristina Aggazzotti et.al.** · 2025-12-18


#### [DisCo-Speech: Controllable Zero-Shot Speech Generation with A Disentangled Speech Codec](https://arxiv.org/abs/2512.13251)
**Tao Li et.al.** · 2025-12-18


#### [Adapting Speech Language Model to Singing Voice Synthesis](https://arxiv.org/abs/2512.14657)
**Yiwen Zhao et.al.** · 2025-12-16


#### [Robust Training of Singing Voice Synthesis Using Prior and Posterior Uncertainty](https://arxiv.org/abs/2512.14653)
**Yiwen Zhao et.al.** · 2025-12-16


#### [GLM-TTS Technical Report](https://arxiv.org/abs/2512.14291)
**Jiayan Cui et.al.** · 2025-12-16


#### [CompanionCast: A Multi-Agent Conversational AI Framework with Spatial Audio for Social Co-Viewing Experiences](https://arxiv.org/abs/2512.10918)
**Yiyang Wang et.al.** · 2025-12-11


#### [DMP-TTS: Disentangled multi-modal Prompting for Controllable Text-to-Speech with Chained Guidance](https://arxiv.org/abs/2512.09504)
**Kang Yin et.al.** · 2025-12-10


#### [LG Uplus System with Multi-Speaker IDs and Discriminator-based Sub-Judges for the WildSpoof Challenge](https://arxiv.org/abs/2512.09000)
**Jinyoung Park et.al.** · 2025-12-09


#### [Beyond Unified Models: A Service-Oriented Approach to Low Latency, Context Aware Phonemization for Real Time TTS](https://arxiv.org/abs/2512.08006)
**Mahta Fetrat et.al.** · 2025-12-08


#### [MultiAPI Spoof: A Multi-API Dataset and Local-Attention Network for Speech Anti-spoofing Detection](https://arxiv.org/abs/2512.07352)
**Xueping Zhang et.al.** · 2025-12-08


#### [Sanvaad: A Multimodal Accessibility Framework for ISL Recognition and Voice-Based Interaction](https://arxiv.org/abs/2512.06485)
**Kush Revankar et.al.** · 2025-12-06


#### [SEA-SafeguardBench: Evaluating AI Safety in SEA Languages and Cultures](https://arxiv.org/abs/2512.05501)
**Panuthep Tasawong et.al.** · 2025-12-05


#### [Simulating Life Paths with Digital Twins: AI-Generated Future Selves Influence Decision-Making and Expand Human Choice](https://arxiv.org/abs/2512.05397)
**Rachel Poonsiriwong et.al.** · 2025-12-05


#### [HiPPO: Exploring A Novel Hierarchical Pronunciation Assessment Approach for Spoken Languages](https://arxiv.org/abs/2512.04964)
**Bi-Cheng Yan et.al.** · 2025-12-04


#### [TripleC Learning and Lightweight Speech Enhancement for Multi-Condition Target Speech Extraction](https://arxiv.org/abs/2512.04945)
**Ziling Huang et.al.** · 2025-12-04


#### [YingMusic-Singer: Zero-shot Singing Voice Synthesis and Editing with Annotation-free Melody Guidance](https://arxiv.org/abs/2512.04779)
**Junjie Zheng et.al.** · 2025-12-04


#### [Measuring the Unspoken: A Disentanglement Model and Benchmark for Psychological Analysis in the Wild](https://arxiv.org/abs/2512.04728)
**Yigui Feng et.al.** · 2025-12-04


#### [M3-TTS: Multi-modal DiT Alignment & Mel-latent for Zero-shot High-fidelity Speech Synthesis](https://arxiv.org/abs/2512.04720)
**Xiaopeng Wang et.al.** · 2025-12-04


#### [Large Speech Model Enabled Semantic Communication](https://arxiv.org/abs/2512.04711)
**Yun Tian et.al.** · 2025-12-04


#### [Limit cycles for speech](https://arxiv.org/abs/2512.04642)
**Adamantios I. Gafos et.al.** · 2025-12-04


#### [RRPO: Robust Reward Policy Optimization for LLM-based Emotional TTS](https://arxiv.org/abs/2512.04552)
**Cong Wang et.al.** · 2025-12-04


#### [Multi-Loss Learning for Speech Emotion Recognition with Energy-Adaptive Mixup and Frame-Level Attention](https://arxiv.org/abs/2512.04551)
**Cong Wang et.al.** · 2025-12-04


#### [Head, posture, and full-body gestures in interactive communication](https://arxiv.org/abs/2512.03636)
**Ľuboš Hládek et.al.** · 2025-12-03


#### [A Convolutional Framework for Mapping Imagined Auditory MEG into Listened Brain Responses](https://arxiv.org/abs/2512.03458)
**Maryam Maghsoudi et.al.** · 2025-12-03


#### [Comparing Unsupervised and Supervised Semantic Speech Tokens: A Case Study of Child ASR](https://arxiv.org/abs/2512.03301)
**Mohan Shi et.al.** · 2025-12-02


#### [How to DP-fy Your Data: A Practical Guide to Generating Synthetic Data With Differential Privacy](https://arxiv.org/abs/2512.03238)
**Natalia Ponomareva et.al.** · 2025-12-02


#### [MAViD: A Multimodal Framework for Audio-Visual Dialogue Understanding and Generation](https://arxiv.org/abs/2512.03034)
**Youxin Pang et.al.** · 2025-12-02


#### [Perceptual evaluation of Acoustic Level of Detail in Virtual Acoustic Environments](https://arxiv.org/abs/2512.02891)
**Stefan Fichna et.al.** · 2025-12-02


#### [BOOM: Beyond Only One Modality KIT's Multimodal Multilingual Lecture Companion](https://arxiv.org/abs/2512.02817)
**Sai Koneru et.al.** · 2025-12-02


#### [Reasoning-Aware Multimodal Fusion for Hateful Video Detection](https://arxiv.org/abs/2512.02743)
**Shuonan Yang et.al.** · 2025-12-02


#### [Hear What Matters! Text-conditioned Selective Video-to-Audio Generation](https://arxiv.org/abs/2512.02650)
**Junwon Lee et.al.** · 2025-12-02


#### [Spoken Conversational Agents with Large Language Models](https://arxiv.org/abs/2512.02593)
**Chao-Han Huck Yang et.al.** · 2025-12-02


#### [Co-speech Gesture Video Generation via Motion-Based Graph Retrieval](https://arxiv.org/abs/2512.02576)
**Yafei Song et.al.** · 2025-12-02


#### [Generative Multi-modal Feedback for Singing Voice Synthesis Evaluation](https://arxiv.org/abs/2512.02523)
**Xueyan Li et.al.** · 2025-12-02


#### [VibOmni: Towards Scalable Bone-conduction Speech Enhancement on Earables](https://arxiv.org/abs/2512.02515)
**Lixing He et.al.** · 2025-12-02


#### [Swivuriso: The South African Next Voices Multilingual Speech Dataset](https://arxiv.org/abs/2512.02201)
**Vukosi Marivatee et.al.** · 2025-12-01


#### [Cross-Lingual Interleaving for Speech Language Models](https://arxiv.org/abs/2512.01865)
**Adel Moumen et.al.** · 2025-12-01


#### [MAC-SLU: Multi-Intent Automotive Cabin Spoken Language Understanding Benchmark](https://arxiv.org/abs/2512.01603)
**Yuezhang Peng et.al.** · 2025-12-01


#### [MCAT: Scaling Many-to-Many Speech-to-Text Translation with MLLMs to 70 Languages](https://arxiv.org/abs/2512.01512)
**Yexing Du et.al.** · 2025-12-01


#### [Model-Based Clustering of Functional Data Via Random Projection Ensembles](https://arxiv.org/abs/2512.01450)
**Matteo Mori et.al.** · 2025-12-01


#### [EvalTalker: Learning to Evaluate Real-Portrait-Driven Multi-Subject Talking Humans](https://arxiv.org/abs/2512.01340)
**Yingjie Zhou et.al.** · 2025-12-01


#### [fMRI2GES: Co-speech Gesture Reconstruction from fMRI Signal with Dual Brain Decoding Alignment](https://arxiv.org/abs/2512.01189)
**Chunzheng Zhu et.al.** · 2025-12-01


#### [Supporting Productivity Skill Development in College Students through Social Robot Coaching: A Proof-of-Concept](https://arxiv.org/abs/2512.01105)
**Himanshi Lalwani et.al.** · 2025-11-30


#### [Arabic TTS with FastPitch: Reproducible Baselines, Adversarial Training, and Oversmoothing Analysis](https://arxiv.org/abs/2512.00937)
**Lars Nippert et.al.** · 2025-11-30


#### [STCTS: Generative Semantic Compression for Ultra-Low Bitrate Speech via Explicit Text-Prosody-Timbre Decomposition](https://arxiv.org/abs/2512.00451)
**Siyu Wang et.al.** · 2025-11-29


#### [OmniFusion: Simultaneous Multilingual Multimodal Translations via Modular Fusion](https://arxiv.org/abs/2512.00234)
**Sai Koneru et.al.** · 2025-11-28


#### [CoordSpeaker: Exploiting Gesture Captioning for Coordinated Caption-Empowered Co-Speech Gesture Generation](https://arxiv.org/abs/2511.22863)
**Fengyi Fang et.al.** · 2025-11-28


#### [Modeling Romanized Hindi and Bengali: Dataset Creation and Multilingual LLM Integration](https://arxiv.org/abs/2511.22769)
**Kanchon Gharami et.al.** · 2025-11-27


#### [PURE Codec: Progressive Unfolding of Residual Entropy for Speech Codec Learning](https://arxiv.org/abs/2511.22687)
**Jiatong Shi et.al.** · 2025-11-27


#### [Joint Speech and Text Training for LLM-Based End-to-End Spoken Dialogue State Tracking](https://arxiv.org/abs/2511.22503)
**Katia Vendrame et.al.** · 2025-11-27


#### [GLA-Grad++: An Improved Griffin-Lim Guided Diffusion Model for Speech Synthesis](https://arxiv.org/abs/2511.22293)
**Teysir Baoueb et.al.** · 2025-11-27


#### [VSpeechLM: A Visual Speech Language Model for Visual Text-to-Speech Task](https://arxiv.org/abs/2511.22229)
**Yuyue Wang et.al.** · 2025-11-27


#### [Layover or Direct Flight: Rethinking Audio-Guided Image Segmentation](https://arxiv.org/abs/2511.22025)
**Joel Alberto Santos et.al.** · 2025-11-27


#### [Advancing Marine Bioacoustics with Deep Generative Models: A Hybrid Augmentation Strategy for Southern Resident Killer Whale Detection](https://arxiv.org/abs/2511.21872)
**Bruno Padovese et.al.** · 2025-11-26


#### [Voice, Bias, and Coreference: An Interpretability Study of Gender in Speech Translation](https://arxiv.org/abs/2511.21517)
**Lina Conti et.al.** · 2025-11-26


#### [TSGM: Regular and Irregular Time-series Generation using Score-based Generative Models](https://arxiv.org/abs/2511.21335)
**Haksoo Lim et.al.** · 2025-11-26


#### [Acoustic neural networks: Identifying design principles and exploring physical feasibility](https://arxiv.org/abs/2511.21313)
**Ivan Kalthoff et.al.** · 2025-11-26


#### [Multi-Reward GRPO for Stable and Prosodic Single-Codebook TTS LLMs at Scale](https://arxiv.org/abs/2511.21270)
**Yicheng Zhong et.al.** · 2025-11-26


#### [CartoonSing: Unifying Human and Nonhuman Timbres in Singing Generation](https://arxiv.org/abs/2511.21045)
**Jionghao Han et.al.** · 2025-11-26


#### [RosettaSpeech: Zero-Shot Speech-to-Speech Translation from Monolingual Data](https://arxiv.org/abs/2511.20974)
**Zhisheng Zheng et.al.** · 2025-11-26


#### [Towards Audio Token Compression in Large Audio Language Models](https://arxiv.org/abs/2511.20973)
**Saurabhchand Bhati et.al.** · 2025-11-26


#### [SingingSDS: A Singing-Capable Spoken Dialogue System for Conversational Roleplay Applications](https://arxiv.org/abs/2511.20972)
**Jionghao Han et.al.** · 2025-11-26


#### [Continual Audio Deepfake Detection via Universal Adversarial Perturbation](https://arxiv.org/abs/2511.19974)
**Wangjie Li et.al.** · 2025-11-25


#### [Towards Edge General Intelligence: Knowledge Distillation for Mobile Agentic AI](https://arxiv.org/abs/2511.19947)
**Yuxuan Wu et.al.** · 2025-11-25


#### [It Hears, It Sees too: Multi-Modal LLM for Depression Detection By Integrating Visual Understanding into Audio Language Models](https://arxiv.org/abs/2511.19877)
**Xiangyu Zhao et.al.** · 2025-11-25


#### [PrismAudio: Decomposed Chain-of-Thoughts and Multi-dimensional Rewards for Video-to-Audio Generation](https://arxiv.org/abs/2511.18833)
**Huadai Liu et.al.** · 2025-11-25


#### [Evaluating Objective Speech Quality Metrics for Neural Audio Codecs](https://arxiv.org/abs/2511.19734)
**Luca A. Lanzendörfer et.al.** · 2025-11-24


#### [A Layered Protocol Architecture for the Internet of Agents](https://arxiv.org/abs/2511.19699)
**Charles Fleming et.al.** · 2025-11-24


#### [Dynamic Multi-Species Bird Soundscape Generation with Acoustic Patterning and 3D Spatialization](https://arxiv.org/abs/2511.19275)
**Ellie L. Zhang et.al.** · 2025-11-24


#### [Context-Aware Whisper for Arabic ASR Under Linguistic Varieties](https://arxiv.org/abs/2511.18774)
**Bashar Talafha et.al.** · 2025-11-24


#### [AIRHILT: A Human-in-the-Loop Testbed for Multimodal Conflict Detection in Aviation](https://arxiv.org/abs/2511.18718)
**Omar Garib et.al.** · 2025-11-24


#### [The Locally Deployable Virtual Doctor: LLM Based Human Interface for Automated Anamnesis and Database Conversion](https://arxiv.org/abs/2511.18632)
**Jan Benedikt Ruhland et.al.** · 2025-11-23


#### [InstructAudio: Unified speech and music generation with natural language instruction](https://arxiv.org/abs/2511.18487)
**Chunyu Qiang et.al.** · 2025-11-23


#### [A Multimodal Conversational Agent for Tabular Data Analysis](https://arxiv.org/abs/2511.18405)
**Mohammad Nour Al Awad et.al.** · 2025-11-23


#### [Gradient Masters at BLP-2025 Task 1: Advancing Low-Resource NLP for Bengali using Ensemble-Based Adversarial Training for Hate Speech Detection](https://arxiv.org/abs/2511.18324)
**Syed Mohaiminul Hoque et.al.** · 2025-11-23


#### [MultiDiffNet: A Multi-Objective Diffusion Framework for Generalizable Brain Decoding](https://arxiv.org/abs/2511.18294)
**Mengchun Zhang et.al.** · 2025-11-23


#### [A superpersuasive autonomous policy debating system](https://arxiv.org/abs/2511.17854)
**Allen Roush et.al.** · 2025-11-22


#### [Enhancing Quranic Learning: A Multimodal Deep Learning Approach for Arabic Phoneme Recognition](https://arxiv.org/abs/2511.17477)
**Ayhan Kucukmanisa et.al.** · 2025-11-21


#### [AI in Music and Sound: Pedagogical Reflections, Post-Structuralist Approaches and Creative Outcomes in Seminar Practice](https://arxiv.org/abs/2511.17425)
**Guilherme Coelho et.al.** · 2025-11-21


#### [Robot Confirmation Generation and Action Planning Using Long-context Q-Former Integrated with Multimodal LLM](https://arxiv.org/abs/2511.17335)
**Chiori Hori et.al.** · 2025-11-21


#### [Investigating self-supervised representations for audio-visual deepfake detection](https://arxiv.org/abs/2511.17181)
**Dragos-Alexandru Boldisor et.al.** · 2025-11-21


#### [WER is Unaware: Assessing How ASR Errors Distort Clinical Understanding in Patient Facing Dialogue](https://arxiv.org/abs/2511.16544)
**Zachary Ellis et.al.** · 2025-11-21


#### [Revisiting Audio-language Pretraining for Learning General-purpose Audio Representation](https://arxiv.org/abs/2511.16757)
**Wei-Cheng Tseng et.al.** · 2025-11-20


#### [Codec2Vec: Self-Supervised Speech Representation Learning Using Neural Speech Codecs](https://arxiv.org/abs/2511.16639)
**Wei-Cheng Tseng et.al.** · 2025-11-20


#### [SceneGuard: Training-Time Voice Protection with Scene-Consistent Audible Background Noise](https://arxiv.org/abs/2511.16114)
**Rui Sang et.al.** · 2025-11-20


#### [Step-Audio-R1 Technical Report](https://arxiv.org/abs/2511.15848)
**Fei Tian et.al.** · 2025-11-19


#### [A Generalized Weighted Overlap-Add (WOLA) Filter Bank for Improved Subband System Identification](https://arxiv.org/abs/2511.15766)
**Mohit Sharma et.al.** · 2025-11-19


#### [PresentCoach: Dual-Agent Presentation Coaching through Exemplars and Interactive Feedback](https://arxiv.org/abs/2511.15253)
**Sirui Chen et.al.** · 2025-11-19


#### [Auden-Voice: General-Purpose Voice Encoder for Speech and Language Understanding](https://arxiv.org/abs/2511.15145)
**Mingyue Huo et.al.** · 2025-11-19


#### [Aligning Generative Music AI with Human Preferences: Methods and Challenges](https://arxiv.org/abs/2511.15038)
**Dorien Herremans et.al.** · 2025-11-19


#### [Quality-Controlled Multimodal Emotion Recognition in Conversations with Identity-Based Transfer Learning and MAMBA Fusion](https://arxiv.org/abs/2511.14969)
**Zanxu Wang et.al.** · 2025-11-18


#### [PolyKAN: Efficient Fused GPU Operators for Polynomial Kolmogorov-Arnold Network Variants](https://arxiv.org/abs/2511.14852)
**Mingkun Yu et.al.** · 2025-11-18


#### [Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech](https://arxiv.org/abs/2511.14824)
**Nam-Gyu Kim et.al.** · 2025-11-18


#### [Ground Truth Generation for Multilingual Historical NLP using LLMs](https://arxiv.org/abs/2511.14688)
**Clovis Gladstone et.al.** · 2025-11-18


#### [TTA: Transcribe, Translate and Alignment for Cross-lingual Speech Representation](https://arxiv.org/abs/2511.14410)
**Wei Liu et.al.** · 2025-11-18


#### [AfriSpeech-MultiBench: A Verticalized Multidomain Multicountry Benchmark Suite for African Accented English ASR](https://arxiv.org/abs/2511.14255)
**Gabrial Zencha Ashungafac et.al.** · 2025-11-18


#### [Towards Authentic Movie Dubbing with Retrieve-Augmented Director-Actor Interaction Learning](https://arxiv.org/abs/2511.14249)
**Rui Liu et.al.** · 2025-11-18


#### [StreamingTalker: Audio-driven 3D Facial Animation with Autoregressive Diffusion Model](https://arxiv.org/abs/2511.14223)
**Yifan Yang et.al.** · 2025-11-18


#### [FxSearcher: gradient-free text-driven audio transformation](https://arxiv.org/abs/2511.14138)
**Hojoon Ki et.al.** · 2025-11-18


#### [Human-centric Maintenance Process Through Integration of AI, Speech, and AR](https://arxiv.org/abs/2511.13918)
**Parul Khanna et.al.** · 2025-11-17


#### [Passive Dementia Screening via Facial Temporal Micro-Dynamics Analysis of In-the-Wild Talking-Head Video](https://arxiv.org/abs/2511.13802)
**Filippo Cenacchi. Longbing Cao et.al.** · 2025-11-17


#### [PASE: Leveraging the Phonological Prior of WavLM for Low-Hallucination Generative Speech Enhancement](https://arxiv.org/abs/2511.13300)
**Xiaobin Rong et.al.** · 2025-11-17


#### [Computational Measurement of Political Positions: A Review of Text-Based Ideal Point Estimation Algorithms](https://arxiv.org/abs/2511.13238)
**Patrick Parschan et.al.** · 2025-11-17


#### [FoleyBench: A Benchmark For Video-to-Audio Models](https://arxiv.org/abs/2511.13219)
**Satvik Dixit et.al.** · 2025-11-17


#### [Distinguishing Repetition Disfluency from Morphological Reduplication in Bangla ASR Transcripts: A Novel Corpus and Benchmarking Analysis](https://arxiv.org/abs/2511.13159)
**Zaara Zabeen Arpa et.al.** · 2025-11-17


#### [A Smart-Glasses for Emergency Medical Services via Multimodal Multitask Learning](https://arxiv.org/abs/2511.13078)
**Liuyi Jin et.al.** · 2025-11-17


#### [CalibrateMix: Guided-Mixup Calibration of Image Semi-Supervised Models](https://arxiv.org/abs/2511.12964)
**Mehrab Mustafy Rahman et.al.** · 2025-11-17


#### [Improving Direct Persian-English Speech-to-Speech Translation with Discrete Units and Synthetic Parallel Data](https://arxiv.org/abs/2511.12690)
**Sina Rashidi et.al.** · 2025-11-16


#### [Hi-Reco: High-Fidelity Real-Time Conversational Digital Humans](https://arxiv.org/abs/2511.12662)
**Hongbin Huang et.al.** · 2025-11-16


#### [Uni-MoE-2.0-Omni: Scaling Language-Centric Omnimodal Large Model with Advanced MoE, Training and Data](https://arxiv.org/abs/2511.12609)
**Yunxin Li et.al.** · 2025-11-16


#### [DenseAnnotate: Enabling Scalable Dense Caption Collection for Images and 3D Scenes via Spoken Descriptions](https://arxiv.org/abs/2511.12452)
**Xiaoyu Lin et.al.** · 2025-11-16


#### [Proactive Hearing Assistants that Isolate Egocentric Conversations](https://arxiv.org/abs/2511.11473)
**Guilin Hu et.al.** · 2025-11-14


#### [Language-Aided State Estimation](https://arxiv.org/abs/2511.11285)
**Yuki Miyoshi et.al.** · 2025-11-14


#### [Analysing Personal Attacks in U.S. Presidential Debates](https://arxiv.org/abs/2511.11108)
**Ruban Goyal et.al.** · 2025-11-14


#### [CLARITY: Contextual Linguistic Adaptation and Accent Retrieval for Dual-Bias Mitigation in Text-to-Speech Generation](https://arxiv.org/abs/2511.11104)
**Crystal Min Hui Poon et.al.** · 2025-11-14


#### [CAT-Net: A Cross-Attention Tone Network for Cross-Subject EEG-EMG Fusion Tone Decoding](https://arxiv.org/abs/2511.10935)
**Yifan Zhuang et.al.** · 2025-11-14


#### [Synthetic Voices, Real Threats: Evaluating Large Text-to-Speech Models in Generating Harmful Audio](https://arxiv.org/abs/2511.10913)
**Guangke Chen et.al.** · 2025-11-14


#### [Curved Worlds, Clear Boundaries: Generalizing Speech Deepfake Detection using Hyperbolic and Spherical Geometry Spaces](https://arxiv.org/abs/2511.10793)
**Farhan Sheth et.al.** · 2025-11-13


#### [Towards Attribution of Generators and Emotional Manipulation in Cross-Lingual Synthetic Speech using Geometric Learning](https://arxiv.org/abs/2511.10790)
**Girish et.al.** · 2025-11-13


#### [Music Flamingo: Scaling Music Understanding in Audio Language Models](https://arxiv.org/abs/2511.10289)
**Sreyan Ghosh et.al.** · 2025-11-13


#### [VocalNet-M2: Advancing Low-Latency Spoken Language Modeling via Integrated Multi-Codebook Tokenization and Multi-Token Prediction](https://arxiv.org/abs/2511.10232)
**Yuhao Wang et.al.** · 2025-11-13


#### [Speech-Audio Compositional Attacks on Multimodal LLMs and Their Mitigation with SALMONN-Guard](https://arxiv.org/abs/2511.10222)
**Yudong Yang et.al.** · 2025-11-13


#### [Towards Leveraging Sequential Structure in Animal Vocalizations](https://arxiv.org/abs/2511.10190)
**Eklavya Sarkar et.al.** · 2025-11-13


#### [FabasedVC: Enhancing Voice Conversion with Text Modality Fusion and Phoneme-Level SSL Features](https://arxiv.org/abs/2511.10112)
**Wenyu Wang et.al.** · 2025-11-13


#### [Mitigating Error Accumulation in Co-Speech Motion Generation via Global Rotation Diffusion and Multi-Level Constraints](https://arxiv.org/abs/2511.10076)
**Xiangyue Zhang et.al.** · 2025-11-13


#### [Time-Layer Adaptive Alignment for Speaker Similarity in Flow-Matching Based Zero-Shot TTS](https://arxiv.org/abs/2511.09995)
**Haoyu Li et.al.** · 2025-11-13


#### [MINDS: A Cross-cultural Dialogue Corpus for Social Norm Classification and Adherence Detection](https://arxiv.org/abs/2511.09918)
**Pritish Sahu et.al.** · 2025-11-13


#### [End-to-end Contrastive Language-Speech Pretraining Model For Long-form Spoken Question Answering](https://arxiv.org/abs/2511.09282)
**Jiliang Hu et.al.** · 2025-11-12


#### [Generating Novel and Realistic Speakers for Voice Conversion](https://arxiv.org/abs/2511.07135)
**Meiying Melissa Chen et.al.** · 2025-11-10


#### [E2E-VGuard: Adversarial Prevention for Production LLM-based End-To-End Speech Synthesis](https://arxiv.org/abs/2511.07099)
**Zhisheng Zhang et.al.** · 2025-11-10


#### [IDMap: A Pseudo-Speaker Generator Framework Based on Speaker Identity Index to Vector Mapping](https://arxiv.org/abs/2511.06246)
**Zeyan Liu et.al.** · 2025-11-09


#### [Synthesizing speech with selected perceptual voice qualities - A case study with creaky voice](https://arxiv.org/abs/2511.05143)
**Frederik Rautenberg et.al.** · 2025-11-07


#### [Step-Audio-EditX Technical Report](https://arxiv.org/abs/2511.03601)
**Chao Yan et.al.** · 2025-11-05


#### [PolyNorm: Few-Shot LLM-Based Text Normalization for Text-to-Speech](https://arxiv.org/abs/2511.03080)
**Michel Wong et.al.** · 2025-11-05


#### [Augmenting Open-Vocabulary Dysarthric Speech Assessment with Human Perceptual Supervision](https://arxiv.org/abs/2511.02270)
**Kaimeng Jia et.al.** · 2025-11-04


#### [Toward Objective and Interpretable Prosody Evaluation in Text-to-Speech: A Linguistically Motivated Approach](https://arxiv.org/abs/2511.02104)
**Cedric Chan et.al.** · 2025-11-03


#### [Reconstructing Unseen Sentences from Speech-related Biosignals for Open-vocabulary Neural Communication](https://arxiv.org/abs/2510.27247)
**Deok-Seon Kim et.al.** · 2025-10-31


#### [Levée d'ambiguïtés par grammaires locales](https://arxiv.org/abs/2510.24530)
**Eric G. C. Laporte et.al.** · 2025-10-28


#### [Bayesian Speech synthesizers Can Learn from Multiple Teachers](https://arxiv.org/abs/2510.24372)
**Ziyang Zhang et.al.** · 2025-10-28


#### [emg2speech: synthesizing speech from electromyography using self-supervised speech models](https://arxiv.org/abs/2510.23969)
**Harshavardhana T. Gowda et.al.** · 2025-10-28


#### [SoulX-Podcast: Towards Realistic Long-form Podcasts with Dialectal and Paralinguistic Diversity](https://arxiv.org/abs/2510.23541)
**Hanke Xie et.al.** · 2025-10-28


#### [SFMS-ALR: Script-First Multilingual Speech Synthesis with Adaptive Locale Resolution](https://arxiv.org/abs/2510.25178)
**Dharma Teja Donepudi et.al.** · 2025-10-27


#### [UltraVoice: Scaling Fine-Grained Style-Controlled Speech Conversations for Spoken Dialogue Models](https://arxiv.org/abs/2510.22588)
**Wenming Tu et.al.** · 2025-10-26


#### [StylePitcher: Generating Style-Following and Expressive Pitch Curves for Versatile Singing Tasks](https://arxiv.org/abs/2510.21685)
**Jingyue Huang et.al.** · 2025-10-24


#### [Vox-Evaluator: Enhancing Stability and Fidelity for Zero-shot TTS with A Multi-Level Evaluator](https://arxiv.org/abs/2510.20210)
**Hualei Wang et.al.** · 2025-10-23


#### [SpeechAgent: An End-to-End Mobile Infrastructure for Speech Impairment Assistance](https://arxiv.org/abs/2510.20113)
**Haowei Lou et.al.** · 2025-10-23


#### [Style Attack Disguise: When Fonts Become a Camouflage for Adversarial Intent](https://arxiv.org/abs/2510.19641)
**Yangshijie Zhang et.al.** · 2025-10-22


#### [Which Evaluation for Which Model? A Taxonomy for Speech Model Assessment](https://arxiv.org/abs/2510.19509)
**Maureen de Seyssel et.al.** · 2025-10-22


#### [EchoFake: A Replay-Aware Dataset for Practical Speech Deepfake Detection](https://arxiv.org/abs/2510.19414)
**Tong Zhang et.al.** · 2025-10-22


#### [VoiceMorph: How AI Voice Morphing Reveals the Boundaries of Auditory Self-Recognition](https://arxiv.org/abs/2510.16192)
**Kye Shimizu et.al.** · 2025-10-22


#### [StutterZero and StutterFormer: End-to-End Speech Conversion for Stuttering Transcription and Correction](https://arxiv.org/abs/2510.18938)
**Qianheng Xu et.al.** · 2025-10-21


#### [KrishokBondhu: A Retrieval-Augmented Voice-Based Agricultural Advisory Call Center for Bengali Farmers](https://arxiv.org/abs/2510.18355)
**Mohd Ruhul Ameen et.al.** · 2025-10-21


#### [ParaStyleTTS: Toward Efficient and Robust Paralinguistic Style Control for Expressive Text-to-Speech Generation](https://arxiv.org/abs/2510.18308)
**Haowei Lou et.al.** · 2025-10-21


#### [U-Codec: Ultra Low Frame-rate Neural Speech Codec for Fast High-fidelity Speech Generation](https://arxiv.org/abs/2510.16718)
**Xusheng Yang et.al.** · 2025-10-19


#### [Edge-Based Speech Transcription and Synthesis for Kinyarwanda and Swahili Languages](https://arxiv.org/abs/2510.16497)
**Pacome Simon Mbonimpa et.al.** · 2025-10-18


#### [RLAIF-SPA: Optimizing LLM-based Emotional Speech Synthesis via RLAIF](https://arxiv.org/abs/2510.14628)
**Qing Yang et.al.** · 2025-10-16


#### [InteractiveOmni: A Unified Omni-modal Model for Audio-Visual Multi-turn Dialogue](https://arxiv.org/abs/2510.13747)
**Wenwen Tong et.al.** · 2025-10-15


#### [Closing the Gap Between Text and Speech Understanding in LLMs](https://arxiv.org/abs/2510.13632)
**Santiago Cuervo et.al.** · 2025-10-15


#### [Mismatch Aware Guidance for Robust Emotion Control in Auto-Regressive TTS Models](https://arxiv.org/abs/2510.13293)
**Yizhou Peng et.al.** · 2025-10-15


#### [DiSTAR: Diffusion over a Scalable Token Autoregressive Representation for Speech Generation](https://arxiv.org/abs/2510.12210)
**Yakun Song et.al.** · 2025-10-15


#### [Continuous-Token Diffusion for Speaker-Referenced TTS in Multimodal LLMs](https://arxiv.org/abs/2510.12995)
**Xinlu He et.al.** · 2025-10-14


#### [Beating Harmful Stereotypes Through Facts: RAG-based Counter-speech Generation](https://arxiv.org/abs/2510.12316)
**Greta Damo et.al.** · 2025-10-14


#### [ParsVoice: A Large-Scale Multi-Speaker Persian Speech Corpus for Text-to-Speech Synthesis](https://arxiv.org/abs/2510.10774)
**Mohammad Javad Ranjbar Kalahroodi et.al.** · 2025-10-14


#### [MRSAudio: A Large-Scale Multimodal Recorded Spatial Audio Dataset with Refined Annotations](https://arxiv.org/abs/2510.10396)
**Wenxiang Guo et.al.** · 2025-10-14


#### [BridgeCode: A Dual Speech Representation Paradigm for Autoregressive Zero-Shot Text-to-Speech Synthesis](https://arxiv.org/abs/2510.11646)
**Jingyuan Xing et.al.** · 2025-10-13


#### [Perturbation Self-Supervised Representations for Cross-Lingual Emotion TTS: Stage-Wise Modeling of Emotion and Speaker](https://arxiv.org/abs/2510.11124)
**Cheng Gong et.al.** · 2025-10-13


#### [Mind-Paced Speaking: A Dual-Brain Approach to Real-Time Reasoning in Spoken Language Models](https://arxiv.org/abs/2510.09592)
**Donghang Wu et.al.** · 2025-10-10


#### [O_O-VC: Synthetic Data-Driven One-to-One Alignment for Any-to-Any Voice Conversion](https://arxiv.org/abs/2510.09061)
**Huu Tuong Tu et.al.** · 2025-10-10


#### [DiTSinger: Scaling Singing Voice Synthesis with Diffusion Transformer and Implicit Alignment](https://arxiv.org/abs/2510.09016)
**Zongcai Du et.al.** · 2025-10-10


#### [DialoSpeech: Dual-Speaker Dialogue Generation with LLM and Flow Matching](https://arxiv.org/abs/2510.08373)
**Hanke Xie et.al.** · 2025-10-09


#### [IntMeanFlow: Few-step Speech Generation with Integral Velocity Distillation](https://arxiv.org/abs/2510.07979)
**Wei Wang et.al.** · 2025-10-09


#### [Making Machines Sound Sarcastic: LLM-Enhanced and Retrieval-Guided Sarcastic Speech Synthesis](https://arxiv.org/abs/2510.07096)
**Zhu Li et.al.** · 2025-10-08


#### [Towards Responsible Evaluation for Text-to-Speech](https://arxiv.org/abs/2510.06927)
**Yifan Yang et.al.** · 2025-10-08


#### [XLSR-Kanformer: A KAN-Intergrated model for Synthetic Speech Detection](https://arxiv.org/abs/2510.06706)
**Phuong Tuan Dat et.al.** · 2025-10-08


#### [ECTSpeech: Enhancing Efficient Speech Synthesis via Easy Consistency Tuning](https://arxiv.org/abs/2510.05984)
**Tao Zhu et.al.** · 2025-10-07


#### [Data-efficient Targeted Token-level Preference Optimization for LLM-based Text-to-Speech](https://arxiv.org/abs/2510.05799)
**Rikuto Kotoge et.al.** · 2025-10-07


#### [Investigation of perception inconsistency in speaker embedding for asynchronous voice anonymization](https://arxiv.org/abs/2510.05718)
**Rui Wang et.al.** · 2025-10-07


#### [Sparse deepfake detection promotes better disentanglement](https://arxiv.org/abs/2510.05696)
**Antoine Teissier et.al.** · 2025-10-07


#### [Teaching Machines to Speak Using Articulatory Control](https://arxiv.org/abs/2510.05619)
**Akshay Anand et.al.** · 2025-10-07


#### [Synthetic Audio Forensics Evaluation (SAFE) Challenge](https://arxiv.org/abs/2510.03387)
**Kirill Trapeznikov et.al.** · 2025-10-07


#### [Paper2Video: Automatic Video Generation from Scientific Papers](https://arxiv.org/abs/2510.05096)
**Zeyu Zhu et.al.** · 2025-10-06


#### [Speak, Edit, Repeat: High-Fidelity Voice Editing and Zero-Shot TTS with Cross-Attentive Mamba](https://arxiv.org/abs/2510.04738)
**Baher Mohammad et.al.** · 2025-10-06


#### [UniVoice: Unifying Autoregressive ASR and Flow-Matching based TTS with Large Language Models](https://arxiv.org/abs/2510.04593)
**Wenhao Guan et.al.** · 2025-10-06


#### [GDiffuSE: Diffusion-based speech enhancement with noise model guidance](https://arxiv.org/abs/2510.04157)
**Efrayim Yanir et.al.** · 2025-10-05


#### [A Multilingual Framework for Dysarthria: Detection, Severity Classification, Speech-to-Text, and Clean Speech Generation](https://arxiv.org/abs/2510.03986)
**Ananya Raghu et.al.** · 2025-10-05


#### [Flamed-TTS: Flow Matching Attention-Free Models for Efficient Generating and Dynamic Pacing Zero-shot Text-to-Speech](https://arxiv.org/abs/2510.02848)
**Hieu-Nghia Huynh-Nguyen et.al.** · 2025-10-03


#### [Emotional Text-To-Speech Based on Mutual-Information-Guided Emotion-Timbre Disentanglement](https://arxiv.org/abs/2510.01722)
**Jianing Yang et.al.** · 2025-10-02


#### [MOSS-Speech: Towards True Speech-to-Speech Models Without Text Guidance](https://arxiv.org/abs/2510.00499)
**Xingjian Zhao et.al.** · 2025-10-02


#### [From Scores to Preferences: Redefining MOS Benchmarking for Speech Quality Reward Modeling](https://arxiv.org/abs/2510.00743)
**Yifei Cao et.al.** · 2025-10-01


#### [BatonVoice: An Operationalist Framework for Enhancing Controllable Speech Synthesis with Linguistic Intelligence from LLMs](https://arxiv.org/abs/2509.26514)
**Yue Wang et.al.** · 2025-09-30


#### [HiStyle: Hierarchical Style Embedding Predictor for Text-Prompt-Guided Controllable Speech Synthesis](https://arxiv.org/abs/2509.25842)
**Ziyu Zhang et.al.** · 2025-09-30


#### [LTA-L2S: Lexical Tone-Aware Lip-to-Speech Synthesis for Mandarin with Cross-Lingual Transfer Learning](https://arxiv.org/abs/2509.25670)
**Kang Yang et.al.** · 2025-09-30


#### [VSSFlow: Unifying Video-conditioned Sound and Speech Generation via Joint Learning](https://arxiv.org/abs/2509.24773)
**Xin Cheng et.al.** · 2025-09-30


#### [Emotion-Aligned Generation in Diffusion Text to Speech Models via Preference-Guided Optimization](https://arxiv.org/abs/2509.25416)
**Jiacheng Shi et.al.** · 2025-09-29


#### [MGM-Omni: Scaling Omni LLMs to Personalized Long-Horizon Speech](https://arxiv.org/abs/2509.25131)
**Chengyao Wang et.al.** · 2025-09-29


#### [VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning](https://arxiv.org/abs/2509.24650)
**Yixuan Zhou et.al.** · 2025-09-29


#### [Word-Level Emotional Expression Control in Zero-Shot Text-to-Speech Synthesis](https://arxiv.org/abs/2509.24629)
**Tianrui Wang et.al.** · 2025-09-29


#### [ISSE: An Instruction-Guided Speech Style Editing Dataset And Benchmark](https://arxiv.org/abs/2509.24570)
**Yun Chen et.al.** · 2025-09-29


#### [UniFlow-Audio: Unified Flow Matching for Audio Generation from Omni-Modalities](https://arxiv.org/abs/2509.24391)
**Xuenan Xu et.al.** · 2025-09-29


#### [Generalizable Speech Deepfake Detection via Information Bottleneck Enhanced Adversarial Alignment](https://arxiv.org/abs/2509.23618)
**Pu Huang et.al.** · 2025-09-28


#### [BFA: Real-time Multilingual Text-to-speech Forced Alignment](https://arxiv.org/abs/2509.23147)
**Abdul Rehman et.al.** · 2025-09-27


#### [i-LAVA: Insights on Low Latency Voice-2-Voice Architecture for Agents](https://arxiv.org/abs/2509.20971)
**Anupam Purwar et.al.** · 2025-09-27


#### [ArFake: A Multi-Dialect Benchmark and Baselines for Arabic Spoof-Speech Detection](https://arxiv.org/abs/2509.22808)
**Mohamed Maged et.al.** · 2025-09-26


#### [Semantic-VAE: Semantic-Alignment Latent Representation for Better Speech Synthesis](https://arxiv.org/abs/2509.22167)
**Zhikang Niu et.al.** · 2025-09-26


#### [Speaker Anonymisation for Speech-based Suicide Risk Detection](https://arxiv.org/abs/2509.22148)
**Ziyun Cui et.al.** · 2025-09-26


#### [Comprehend and Talk: Text to Speech Synthesis via Dual Language Modeling](https://arxiv.org/abs/2509.22062)
**Junjie Cao et.al.** · 2025-09-26


#### [Align2Speak: Improving TTS for Low Resource Languages via ASR-Guided Online Preference Optimization](https://arxiv.org/abs/2509.21718)
**Shehzeen Hussain et.al.** · 2025-09-26


#### [SPADE: Structured Pruning and Adaptive Distillation for Efficient LLM-TTS](https://arxiv.org/abs/2509.20802)
**Tan Dat Nguyen et.al.** · 2025-09-26


#### [UniSS: Unified Expressive Speech-to-Speech Translation with Your Voice](https://arxiv.org/abs/2509.21144)
**Sitong Cheng et.al.** · 2025-09-25


#### [Measuring Prosody Diversity in Zero-Shot TTS: A New Metric, Benchmark, and Exploration](https://arxiv.org/abs/2509.19928)
**Yifan Yang et.al.** · 2025-09-25


#### [Objective Evaluation of Prosody and Intelligibility in Speech Synthesis via Conditional Prediction of Discrete Tokens](https://arxiv.org/abs/2509.20485)
**Ismail Rasim Ulgen et.al.** · 2025-09-24


#### [OLaPh: Optimal Language Phonemizer](https://arxiv.org/abs/2509.20086)
**Johannes Wirth et.al.** · 2025-09-24


#### [CoMelSinger: Discrete Token-Based Zero-Shot Singing Synthesis With Structured Melody Control and Guidance](https://arxiv.org/abs/2509.19883)
**Junchuan Zhao et.al.** · 2025-09-24


#### [Eliminating stability hallucinations in llm-based tts models via attention guidance](https://arxiv.org/abs/2509.19852)
**ShiMing Wang et.al.** · 2025-09-24


#### [Efficient Speech Watermarking for Speech Synthesis via Progressive Knowledge Distillation](https://arxiv.org/abs/2509.19812)
**Yang Cui et.al.** · 2025-09-24


#### [PART: Progressive Alignment Representation Training for Multilingual Speech-To-Text with LLMs](https://arxiv.org/abs/2509.19745)
**Pei Zhang et.al.** · 2025-09-24


#### [Selective Classifier-free Guidance for Zero-shot Text-to-speech](https://arxiv.org/abs/2509.19668)
**John Zheng et.al.** · 2025-09-24


#### [Frame-Stacked Local Transformers For Efficient Multi-Codebook Speech Generation](https://arxiv.org/abs/2509.19592)
**Roy Fejgin et.al.** · 2025-09-23


#### [HD-PPT: Hierarchical Decoding of Content- and Prompt-Preference Tokens for Instruction-based TTS](https://arxiv.org/abs/2509.19001)
**Sihang Nie et.al.** · 2025-09-23


#### [Direct Preference Optimization for Speech Autoregressive Diffusion Models](https://arxiv.org/abs/2509.18928)
**Zhijun Liu et.al.** · 2025-09-23


#### [Group Relative Policy Optimization for Text-to-Speech with Large Language Models](https://arxiv.org/abs/2509.18798)
**Chang Liu et.al.** · 2025-09-23


#### [Explore the Reinforcement Learning for the LLM based ASR and TTS system](https://arxiv.org/abs/2509.18569)
**Changfeng Gao et.al.** · 2025-09-23


#### [No Verifiable Reward for Prosody: Toward Preference-Guided Prosody Learning in TTS](https://arxiv.org/abs/2509.18531)
**Seungyoun Shin et.al.** · 2025-09-23


#### [Discrete-time diffusion-like models for speech synthesis](https://arxiv.org/abs/2509.18470)
**Xiaozhou Tan et.al.** · 2025-09-22


#### [TMD-TTS: A Unified Tibetan Multi-Dialect Text-to-Speech Synthesis for Ü-Tsang, Amdo and Kham Speech Dataset Generation](https://arxiv.org/abs/2509.18060)
**Yutong Liu et.al.** · 2025-09-22


#### [Nord-Parl-TTS: Finnish and Swedish TTS Dataset from Parliament Speech](https://arxiv.org/abs/2509.17988)
**Zirui Li et.al.** · 2025-09-22


#### [Qwen3-Omni Technical Report](https://arxiv.org/abs/2509.17765)
**Jin Xu et.al.** · 2025-09-22


#### [Audiobook-CC: Controllable Long-context Speech Generation for Multicast Audiobook](https://arxiv.org/abs/2509.17516)
**Min Liu et.al.** · 2025-09-22


#### [Sidon: Fast and Robust Open-Source Multilingual Speech Restoration for Large-scale Dataset Cleansing](https://arxiv.org/abs/2509.17052)
**Wataru Nakata et.al.** · 2025-09-21


#### [Bridging the gap between training and inference in LM-based TTS models](https://arxiv.org/abs/2509.17021)
**Ruonan Zhang et.al.** · 2025-09-21


#### [MBCodec:Thorough disentangle for high-fidelity audio compression](https://arxiv.org/abs/2509.17006)
**Ruonan Zhang et.al.** · 2025-09-21


#### [SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding](https://arxiv.org/abs/2509.14946)
**Bingsong Bai et.al.** · 2025-09-20


#### [Fed-PISA: Federated Voice Cloning via Personalized Identity-Style Adaptation](https://arxiv.org/abs/2509.16010)
**Qi Wang et.al.** · 2025-09-19


#### [VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency](https://arxiv.org/abs/2509.15969)
**Nikita Torgashov et.al.** · 2025-09-19


#### [Deep Dubbing: End-to-End Auto-Audiobook System with Text-to-Timbre and Context-Aware Instruct-TTS](https://arxiv.org/abs/2509.15845)
**Ziqi Dai et.al.** · 2025-09-19


#### [LibriTTS-VI: A Public Corpus and Novel Methods for Efficient Voice Impression Control](https://arxiv.org/abs/2509.15626)
**Junki Ohmura et.al.** · 2025-09-19


#### [Beyond Video-to-SFX: Video to Audio Synthesis with Environmentally Aware Speech](https://arxiv.org/abs/2509.15492)
**Xinlei Niu et.al.** · 2025-09-19


#### [A Novel Semantic Compression Approach for Ultra-low Bandwidth Voice Communication](https://arxiv.org/abs/2509.15462)
**Ryan Collette et.al.** · 2025-09-18


#### [Frustratingly Easy Data Augmentation for Low-Resource ASR](https://arxiv.org/abs/2509.15373)
**Katsumi Ibaraki et.al.** · 2025-09-18


#### [Real-Time Streaming Mel Vocoding with Generative Flow Matching](https://arxiv.org/abs/2509.15085)
**Simon Welker et.al.** · 2025-09-18


#### [MELA-TTS: Joint transformer-diffusion model with representation alignment for speech synthesis](https://arxiv.org/abs/2509.14784)
**Keyu An et.al.** · 2025-09-18


#### [DAIEN-TTS: Disentangled Audio Infilling for Environment-Aware Text-to-Speech Synthesis](https://arxiv.org/abs/2509.14684)
**Ye-Xin Lu et.al.** · 2025-09-18


#### [Stochastic Clock Attention for Aligning Continuous and Ordered Sequences](https://arxiv.org/abs/2509.14678)
**Hyungjoon Soh et.al.** · 2025-09-18


#### [SpeechMLC: Speech Multi-label Classification](https://arxiv.org/abs/2509.14677)
**Miseul Kim et.al.** · 2025-09-18


#### [Mitigating Intra-Speaker Variability in Diarization with Style-Controllable Speech Augmentation](https://arxiv.org/abs/2509.14632)
**Miseul Kim et.al.** · 2025-09-18


#### [Cross-Lingual F5-TTS: Towards Language-Agnostic Voice Cloning and Speech Synthesis](https://arxiv.org/abs/2509.14579)
**Qingyu Liu et.al.** · 2025-09-18


#### [Do You Hear What I Mean? Quantifying the Instruction-Perception Gap in Instruction-Guided Expressive Text-To-Speech Systems](https://arxiv.org/abs/2509.13989)
**Yi-Cheng Lin et.al.** · 2025-09-18


#### [CS-FLEURS: A Massively Multilingual and Code-Switched Speech Dataset](https://arxiv.org/abs/2509.14161)
**Brian Yan et.al.** · 2025-09-17


#### [MSR-Codec: A Low-Bitrate Multi-Stream Residual Codec for High-Fidelity Speech Generation with Information Disentanglement](https://arxiv.org/abs/2509.13068)
**Jingyu Li et.al.** · 2025-09-16


#### [A Lightweight Pipeline for Noisy Speech Voice Cloning and Accurate Lip Sync Synthesis](https://arxiv.org/abs/2509.12831)
**Javeria Amir et.al.** · 2025-09-16


#### [Preservation of Language Understanding Capabilities in Speech-aware Large Language Models](https://arxiv.org/abs/2509.12171)
**Marek Kubis et.al.** · 2025-09-15


#### [FuseCodec: Semantic-Contextual Fusion and Supervision for Neural Codecs](https://arxiv.org/abs/2509.11425)
**Md Mubtasim Ahasan et.al.** · 2025-09-14


#### [Length-Aware Rotary Position Embedding for Text-Speech Alignment](https://arxiv.org/abs/2509.11084)
**Hyeongju Kim et.al.** · 2025-09-14


#### [Towards Data Drift Monitoring for Speech Deepfake Detection in the context of MLOps](https://arxiv.org/abs/2509.10086)
**Xin Wang et.al.** · 2025-09-12


#### [DiFlow-TTS: Discrete Flow Matching with Factorized Speech Tokens for Low-Latency Zero-Shot Text-To-Speech](https://arxiv.org/abs/2509.09631)
**Ngoc-Son Nguyen et.al.** · 2025-09-12


#### [DiTReducio: A Training-Free Acceleration for DiT-Based TTS via Progressive Calibration](https://arxiv.org/abs/2509.09748)
**Yanru Huo et.al.** · 2025-09-11


#### [HISPASpoof: A New Dataset For Spanish Speech Forensics](https://arxiv.org/abs/2509.09155)
**Maria Risques et.al.** · 2025-09-11


#### [Deploying AI for Signal Processing education: Selected challenges and intriguing opportunities](https://arxiv.org/abs/2509.08950)
**Jarvis Haupt et.al.** · 2025-09-10


#### [Streaming Sequence-to-Sequence Learning with Delayed Streams Modeling](https://arxiv.org/abs/2509.08753)
**Neil Zeghidour et.al.** · 2025-09-10


#### [Accelerating Diffusion Transformer-Based Text-to-Speech with Transformer Layer Caching](https://arxiv.org/abs/2509.08696)
**Siratish Sakpiboonchit et.al.** · 2025-09-10


#### [Joint Learning using Mixture-of-Expert-Based Representation for Enhanced Speech Generation and Robust Emotion Recognition](https://arxiv.org/abs/2509.08470)
**Jing-Tong Tzeng et.al.** · 2025-09-10


#### [VStyle: A Benchmark for Voice Style Adaptation with Spoken Instructions](https://arxiv.org/abs/2509.09716)
**Jun Zhan et.al.** · 2025-09-09


#### [Progressive Facial Granularity Aggregation with Bilateral Attribute-based Enhancement for Face-to-Speech Synthesis](https://arxiv.org/abs/2509.07376)
**Yejin Jeon et.al.** · 2025-09-09


#### [When Fine-Tuning is Not Enough: Lessons from HSAD on Hybrid and Adversarial Audio Spoof Detection](https://arxiv.org/abs/2509.07323)
**Bin Hu et.al.** · 2025-09-09


#### [Speaker Privacy and Security in the Big Data Era: Protection and Defense against Deepfake](https://arxiv.org/abs/2509.06361)
**Liping Chen et.al.** · 2025-09-09


#### [Controllable Singing Voice Synthesis using Phoneme-Level Energy Sequence](https://arxiv.org/abs/2509.07038)
**Yerin Ryu et.al.** · 2025-09-08


#### [ParCzech4Speech: A New Speech Corpus Derived from Czech Parliamentary Data](https://arxiv.org/abs/2509.06675)
**Vladislav Stankov et.al.** · 2025-09-08


#### [UniVerse-1: Unified Audio-Video Generation via Stitching of Experts](https://arxiv.org/abs/2509.06155)
**Duomin Wang et.al.** · 2025-09-07


#### [Multimodal Fine-grained Context Interaction Graph Modeling for Conversational Speech Synthesis](https://arxiv.org/abs/2509.06074)
**Zhenqi Jia et.al.** · 2025-09-07


#### [LatinX: Aligning a Multilingual TTS Model with Direct Preference Optimization](https://arxiv.org/abs/2509.05863)
**Luis Felipe Chary et.al.** · 2025-09-06


#### [Cloning a Conversational Voice AI Agent from Call\,Recording Datasets for Telesales](https://arxiv.org/abs/2509.04871)
**Krittanon Kaewtawee et.al.** · 2025-09-05


#### [Say More with Less: Variable-Frame-Rate Speech Tokenization via Adaptive Clustering and Implicit Duration Coding](https://arxiv.org/abs/2509.04685)
**Rui-Chen Zheng et.al.** · 2025-09-04


#### [DarkStream: real-time speech anonymization with low latency](https://arxiv.org/abs/2509.04667)
**Waris Quamer et.al.** · 2025-09-04


#### [AUDETER: A Large-scale Dataset for Deepfake Audio Detection in Open Worlds](https://arxiv.org/abs/2509.04345)
**Qizhou Wang et.al.** · 2025-09-04


#### [Open-Source Full-Duplex Conversational Datasets for Natural and Interactive Speech Synthesis](https://arxiv.org/abs/2509.04093)
**Zhitong Zhou et.al.** · 2025-09-04


#### [LibriQuote: A Speech Dataset of Fictional Character Utterances for Expressive Zero-Shot Speech Synthesis](https://arxiv.org/abs/2509.04072)
**Gaspard Michel et.al.** · 2025-09-04


#### [FireRedTTS-2: Towards Long Conversational Speech Generation for Podcast and Chatbot](https://arxiv.org/abs/2509.02020)
**Kun Xie et.al.** · 2025-09-04


#### [Multi-level SSL Feature Gating for Audio Deepfake Detection](https://arxiv.org/abs/2509.03409)
**Hoan My Tran et.al.** · 2025-09-03


#### [LatPhon: Lightweight Multilingual G2P for Romance Languages and English](https://arxiv.org/abs/2509.03300)
**Luis Felipe Chary et.al.** · 2025-09-03


#### [Improving Perceptual Audio Aesthetic Assessment via Triplet Loss and Self-Supervised Embeddings](https://arxiv.org/abs/2509.03292)
**Dyah A. M. G. Wisnu et.al.** · 2025-09-03


#### [AIVA: An AI-based Virtual Companion for Emotion-aware Interaction](https://arxiv.org/abs/2509.03212)
**Chenxi Li et.al.** · 2025-09-03


#### [Zero-shot Context Biasing with Trie-based Decoding using Synthetic Multi-Pronunciation](https://arxiv.org/abs/2508.17796)
**Changsong Liu et.al.** · 2025-09-02


#### [MixedG2P-T5: G2P-free Speech Synthesis for Mixed-script texts using Speech Self-Supervised Learning and Language Model](https://arxiv.org/abs/2509.01391)
**Joonyong Park et.al.** · 2025-09-01


#### [The AudioMOS Challenge 2025](https://arxiv.org/abs/2509.01336)
**Wen-Chin Huang et.al.** · 2025-09-01


#### [An AI-Based Shopping Assistant System to Support the Visually Impaired](https://arxiv.org/abs/2509.01246)
**Larissa R. de S. Shibata et.al.** · 2025-09-01


#### [SimulMEGA: MoE Routers are Advanced Policy Makers for Simultaneous Speech Translation](https://arxiv.org/abs/2509.01200)
**Chenyang Le et.al.** · 2025-09-01


#### [MPO: Multidimensional Preference Optimization for Language Model-based Text-to-Speech](https://arxiv.org/abs/2509.00685)
**Kangxiang Xia et.al.** · 2025-08-31


#### [MoTAS: MoE-Guided Feature Selection from TTS-Augmented Speech for Enhanced Multimodal Alzheimer's Early Screening](https://arxiv.org/abs/2508.20513)
**Yongqi Shao et.al.** · 2025-08-28


#### [Vocoder-Projected Feature Discriminator](https://arxiv.org/abs/2508.17874)
**Takuhiro Kaneko et.al.** · 2025-08-27


#### [Interpolating Speaker Identities in Embedding Space for Data Expansion](https://arxiv.org/abs/2508.19210)
**Tianchi Liu et.al.** · 2025-08-26


#### [CLEAR: Continuous Latent Autoregressive Modeling for High-quality and Low-latency Speech Synthesis](https://arxiv.org/abs/2508.19098)
**Chun Yat Wu et.al.** · 2025-08-26


#### [EMO-Reasoning: Benchmarking Emotional Reasoning Capabilities in Spoken Dialogue Systems](https://arxiv.org/abs/2508.17623)
**Jingwen Liu et.al.** · 2025-08-26


#### [Unseen Speaker and Language Adaptation for Lightweight Text-To-Speech with Adapters](https://arxiv.org/abs/2508.18006)
**Alessio Falai et.al.** · 2025-08-25


#### [ClearMask: Noise-Free and Naturalness-Preserving Protection Against Voice Deepfake Attacks](https://arxiv.org/abs/2508.17660)
**Yuanda Wang et.al.** · 2025-08-25


#### [Improving French Synthetic Speech Quality via SSML Prosody Control](https://arxiv.org/abs/2508.17494)
**Nassima Ould Ouali et.al.** · 2025-08-24


#### [Mitigating Hallucinations in LM-Based TTS Models via Distribution Alignment Using GFlowNets](https://arxiv.org/abs/2508.15442)
**Chenlin Liu et.al.** · 2025-08-24


#### [RephraseTTS: Dynamic Length Text based Speech Insertion with Speaker Style Transfer](https://arxiv.org/abs/2508.17031)
**Neeraj Matiyali et.al.** · 2025-08-23


#### [WildSpoof Challenge Evaluation Plan](https://arxiv.org/abs/2508.16858)
**Yihan Wu et.al.** · 2025-08-23


#### [TaDiCodec: Text-aware Diffusion Speech Tokenizer for Speech Language Modeling](https://arxiv.org/abs/2508.16790)
**Yuancheng Wang et.al.** · 2025-08-22


#### [Seeing is Believing: Emotion-Aware Audio-Visual Language Modeling for Expressive Speech Generation](https://arxiv.org/abs/2508.16188)
**Weiting Tan et.al.** · 2025-08-22


#### [QvTAD: Differential Relative Attribute Learning for Voice Timbre Attribute Detection](https://arxiv.org/abs/2508.15931)
**Zhiyu Wu et.al.** · 2025-08-21


#### [Any-to-any Speaker Attribute Perturbation for Asynchronous Voice Anonymization](https://arxiv.org/abs/2508.15565)
**Liping Chen et.al.** · 2025-08-21


#### [UniCoM: A Universal Code-Switching Speech Generator](https://arxiv.org/abs/2508.15244)
**Sangmin Lee et.al.** · 2025-08-21


#### [Linear Preference Optimization: Decoupled Gradient Control via Absolute Regularization](https://arxiv.org/abs/2508.14947)
**Rui Wang et.al.** · 2025-08-20


#### [Long-Context Speech Synthesis with Context-Aware Memory](https://arxiv.org/abs/2508.14713)
**Zhipeng Li et.al.** · 2025-08-20


#### [Improving Resource-Efficient Speech Enhancement via Neural Differentiable DSP Vocoder Refinement](https://arxiv.org/abs/2508.14709)
**Heitor R. Guimarães et.al.** · 2025-08-20


#### [DiffIER: Optimizing Diffusion Models with Iterative Error Reduction](https://arxiv.org/abs/2508.13628)
**Ao Chen et.al.** · 2025-08-20


#### [Who Gets the Mic? Investigating Gender Bias in the Speaker Assignment of a Speech-LLM](https://arxiv.org/abs/2508.13603)
**Dariia Puhach et.al.** · 2025-08-19


#### [FNH-TTS: A Fast, Natural, and Human-Like Speech Synthesis System with advanced prosodic modeling based on Mixture of Experts](https://arxiv.org/abs/2508.12001)
**Qingliang Meng et.al.** · 2025-08-19


#### [A Surveillance Based Interactive Robot](https://arxiv.org/abs/2508.13319)
**Kshitij Kavimandan et.al.** · 2025-08-18


#### [Integrating Feedback Loss from Bi-modal Sarcasm Detector for Sarcastic Speech Synthesis](https://arxiv.org/abs/2508.13028)
**Zhu Li et.al.** · 2025-08-18


#### [Real-Time Sign Language Gestures to Speech Transcription using Deep Learning](https://arxiv.org/abs/2508.12713)
**Brandone Fonya et.al.** · 2025-08-18


#### [SimInterview: Transforming Business Education through Large Language Model-Based Simulated Multilingual Interview Training System](https://arxiv.org/abs/2508.11873)
**Truong Thanh Hung Nguyen et.al.** · 2025-08-16


#### [MoE-TTS: Enhancing Out-of-Domain Text Understanding for Description-based TTS via Mixture-of-Experts](https://arxiv.org/abs/2508.11326)
**Heyang Xue et.al.** · 2025-08-15


#### [EmoSSLSphere: Multilingual Emotional Speech Synthesis with Spherical Vectors and Discrete Speech Tokens](https://arxiv.org/abs/2508.11273)
**Joonyong Park et.al.** · 2025-08-15


#### [Training-Free Multimodal Large Language Model Orchestration](https://arxiv.org/abs/2508.10016)
**Tianyu Xie et.al.** · 2025-08-15


#### [MultiAiTutor: Child-Friendly Educational Multilingual Speech Generation Tutor with LLMs](https://arxiv.org/abs/2508.08715)
**Xiaoxue Gao et.al.** · 2025-08-15


#### [Fairness in Dysarthric Speech Synthesis: Understanding Intrinsic Bias in Dysarthric Speech Cloning using F5-TTS](https://arxiv.org/abs/2508.05102)
**M Anuprabha et.al.** · 2025-08-15


#### [Fake Speech Wild: Detecting Deepfake Speech on Social Media Platform](https://arxiv.org/abs/2508.10559)
**Yuankun Xie et.al.** · 2025-08-14


#### [Facilitating Personalized TTS for Dysarthric Speakers Using Knowledge Anchoring and Curriculum Learning](https://arxiv.org/abs/2508.10412)
**Yejin Jeon et.al.** · 2025-08-14


#### [Towards Frame-level Quality Predictions of Synthetic Speech](https://arxiv.org/abs/2508.10374)
**Michael Kuhlmann et.al.** · 2025-08-14


#### [Marco-Voice Technical Report](https://arxiv.org/abs/2508.02038)
**Fengping Tian et.al.** · 2025-08-14


#### [Analysis of Domain Shift across ASR Architectures via TTS-Enabled Separation of Target Domain and Acoustic Conditions](https://arxiv.org/abs/2508.09868)
**Tina Raissi et.al.** · 2025-08-13


#### [UtterTune: LoRA-Based Target-Language Pronunciation Edit and Control in Multilingual Text-to-Speech](https://arxiv.org/abs/2508.09767)
**Shuhei Kato et.al.** · 2025-08-13


#### [$\text{M}^3\text{PDB}$ : A Multimodal, Multi-Label, Multilingual Prompt Database for Speech Generation](https://arxiv.org/abs/2508.09702)
**Boyu Zhu et.al.** · 2025-08-13


#### [DualSpeechLM: Towards Unified Speech Understanding and Generation via Dual Speech Token Modeling with Large Language Models](https://arxiv.org/abs/2508.08961)
**Yuanyuan Wang et.al.** · 2025-08-13


#### [Fake-Mamba: Real-Time Speech Deepfake Detection Using Bidirectional Mamba as Self-Attention's Alternative](https://arxiv.org/abs/2508.09294)
**Xi Xuan et.al.** · 2025-08-12


#### [QAMRO: Quality-aware Adaptive Margin Ranking Optimization for Human-aligned Assessment of Audio Generation Systems](https://arxiv.org/abs/2508.08957)
**Chien-Chun Wang et.al.** · 2025-08-12


#### [Fine-grained Video Dubbing Duration Alignment with Segment Supervised Preference Optimization](https://arxiv.org/abs/2508.08550)
**Chaoqun Cui et.al.** · 2025-08-12


#### [XEmoRAG: Cross-Lingual Emotion Transfer with Controllable Intensity Using Retrieval-Augmented Generation](https://arxiv.org/abs/2508.07302)
**Tianlun Zuo et.al.** · 2025-08-12


#### [Is GAN Necessary for Mel-Spectrogram-based Neural Vocoder?](https://arxiv.org/abs/2508.07711)
**Hui-Peng Du et.al.** · 2025-08-11


#### [Think Before You Talk: Enhancing Meaningful Dialogue Generation in Full-Duplex Speech Language Models with Planning-Inspired Text Guidance](https://arxiv.org/abs/2508.07375)
**Wenqian Cui et.al.** · 2025-08-10


#### [KLASSify to Verify: Audio-Visual Deepfake Detection Using SSL-based Audio and Handcrafted Visual Features](https://arxiv.org/abs/2508.07337)
**Ivan Kukanov et.al.** · 2025-08-10


#### [Maestro-EVC: Controllable Emotional Voice Conversion Guided by References and Explicit Prosody](https://arxiv.org/abs/2508.06890)
**Jinsung Yoon et.al.** · 2025-08-09


#### [Text to Speech System for Meitei Mayek Script](https://arxiv.org/abs/2508.06870)
**Gangular Singh Irengbam et.al.** · 2025-08-09


#### [LLMCARE: Alzheimer's Detection via Transformer Models Enhanced by LLM-Generated Synthetic Data](https://arxiv.org/abs/2508.10027)
**Ali Zolnour et.al.** · 2025-08-08


#### [ScamAgents: How AI Agents Can Simulate Human-Level Scam Calls](https://arxiv.org/abs/2508.06457)
**Sanket Badhe et.al.** · 2025-08-08


#### [Improved Dysarthric Speech to Text Conversion via TTS Personalization](https://arxiv.org/abs/2508.06391)
**Péter Mihajlik et.al.** · 2025-08-08


#### [Large Language Model Data Generation for Enhanced Intent Recognition in German Speech](https://arxiv.org/abs/2508.06277)
**Theresa Pekarek Rosin et.al.** · 2025-08-08


#### [Llasa+: Free Lunch for Accelerated and Streaming Llama-Based Speech Synthesis](https://arxiv.org/abs/2508.06262)
**Wenjie Tian et.al.** · 2025-08-08


#### [A Scalable Pipeline for Enabling Non-Verbal Speech Generation and Understanding](https://arxiv.org/abs/2508.05385)
**Runchuan Ye et.al.** · 2025-08-07


#### [UniTalker: Conversational Speech-Visual Synthesis](https://arxiv.org/abs/2508.04585)
**Yifan Hu et.al.** · 2025-08-07


#### [Root Cause Analysis Training for Healthcare Professionals With AI-Powered Virtual Simulation: A Proof-of-Concept](https://arxiv.org/abs/2508.04904)
**Yuqi Hu et.al.** · 2025-08-06


#### [NVSpeech: An Integrated and Scalable Pipeline for Human-Like Speech Modeling with Paralinguistic Vocalizations](https://arxiv.org/abs/2508.04195)
**Huan Liao et.al.** · 2025-08-06


#### [Multilingual Source Tracing of Speech Deepfakes: A First Benchmark](https://arxiv.org/abs/2508.04143)
**Xi Xuan et.al.** · 2025-08-06


#### [Parallel GPT: Harmonizing the Independence and Interdependence of Acoustic and Semantic Information for Zero-Shot Text-to-Speech](https://arxiv.org/abs/2508.04141)
**Jingyuan Xing et.al.** · 2025-08-06


#### [EmoSteer-TTS: Fine-Grained and Training-Free Emotion-Controllable Text-to-Speech via Activation Steering](https://arxiv.org/abs/2508.03543)
**Tianxin Xie et.al.** · 2025-08-06


#### [Toward Low-Latency End-to-End Voice Agents for Telecommunications Using Streaming ASR, Quantized LLMs, and Real-Time TTS](https://arxiv.org/abs/2508.04721)
**Vignesh Ethiraj et.al.** · 2025-08-05


#### [MiSTR: Multi-Modal iEEG-to-Speech Synthesis with Transformer-Based Prosody Prediction and Neural Phase Reconstruction](https://arxiv.org/abs/2508.03166)
**Mohammed Salah Al-Radhi et.al.** · 2025-08-05


#### [Fine-Tuning Text-to-Speech Diffusion Models Using Reinforcement Learning with Human Feedback](https://arxiv.org/abs/2508.03123)
**Jingyi Chen et.al.** · 2025-08-05


#### [Enhancing Spectrogram Realism in Singing Voice Synthesis via Explicit Bandwidth Extension Prior to Vocoder](https://arxiv.org/abs/2508.01796)
**Runxuan Yang et.al.** · 2025-08-03


#### [Voxlect: A Speech Foundation Model Benchmark for Modeling Dialects and Regional Languages Around the Globe](https://arxiv.org/abs/2508.01691)
**Tiantian Feng et.al.** · 2025-08-03


#### [Advancing Speech Quality Assessment Through Scientific Challenges and Open-source Activities](https://arxiv.org/abs/2508.00317)
**Wen-Chin Huang et.al.** · 2025-08-01


#### [Next Tokens Denoising for Speech Synthesis](https://arxiv.org/abs/2507.22746)
**Yanqing Liu et.al.** · 2025-08-01


#### [Adaptive Duration Model for Text Speech Alignment](https://arxiv.org/abs/2507.22612)
**Junjie Cao et.al.** · 2025-07-30


#### [SpeechFake: A Large-Scale Multilingual Speech Deepfake Dataset Incorporating Cutting-Edge Generation Methods](https://arxiv.org/abs/2507.21463)
**Wen Huang et.al.** · 2025-07-29


#### [JWB-DH-V1: Benchmark for Joint Whole-Body Talking Avatar and Speech Generation Version 1](https://arxiv.org/abs/2507.20987)
**Xinhan Di et.al.** · 2025-07-29


#### [AV-Deepfake1M++: A Large-Scale Audio-Visual Deepfake Benchmark with Real-World Perturbations](https://arxiv.org/abs/2507.20579)
**Zhixi Cai et.al.** · 2025-07-28


#### [Do Not Mimic My Voice: Speaker Identity Unlearning for Zero-Shot Text-to-Speech](https://arxiv.org/abs/2507.20140)
**Taesoo Kim et.al.** · 2025-07-27


#### [Seed LiveInterpret 2.0: End-to-end Simultaneous Speech-to-speech Translation with Your Voice](https://arxiv.org/abs/2507.17527)
**Shanbo Cheng et.al.** · 2025-07-27


#### [Defining ethically sourced code generation](https://arxiv.org/abs/2507.19743)
**Zhuolin Xu et.al.** · 2025-07-26


#### [GOAT-SLM: A Spoken Language Model with Paralinguistic and Speaker Characteristic Awareness](https://arxiv.org/abs/2507.18119)
**Hongjie Chen et.al.** · 2025-07-25


#### [P.808 Multilingual Speech Enhancement Testing: Approach and Results of URGENT 2025 Challenge](https://arxiv.org/abs/2507.11306)
**Marvin Sach et.al.** · 2025-07-25


#### [Synthetic Data Generation for Phrase Break Prediction with Large Language Model](https://arxiv.org/abs/2507.18044)
**Hoyeon Lee et.al.** · 2025-07-24


#### [WaveVerify: A Novel Audio Watermarking Framework for Media Authentication and Combatting Deepfakes](https://arxiv.org/abs/2507.21150)
**Aditya Pujari et.al.** · 2025-07-23


#### [AI Telephone Surveying: Automating Quantitative Data Collection with an AI Interviewer](https://arxiv.org/abs/2507.17718)
**Danny D. Leybzon et.al.** · 2025-07-23


#### [BoSS: Beyond-Semantic Speech](https://arxiv.org/abs/2507.17563)
**Qing Wang et.al.** · 2025-07-23


#### [TTS-1 Technical Report](https://arxiv.org/abs/2507.21138)
**Oleg Atamanenko et.al.** · 2025-07-22


#### [SplitMeanFlow: Interval Splitting Consistency in Few-Step Generative Modeling](https://arxiv.org/abs/2507.16884)
**Yi Guo et.al.** · 2025-07-22


#### [Technical report: Impact of Duration Prediction on Speaker-specific TTS for Indian Languages](https://arxiv.org/abs/2507.16875)
**Isha Pandey et.al.** · 2025-07-22


#### [Hear Your Code Fail, Voice-Assisted Debugging for Python](https://arxiv.org/abs/2507.15007)
**Sayed Mahbub Hasan Amiri et.al.** · 2025-07-22


#### [A2TTS: TTS for Low Resource Indian Languages](https://arxiv.org/abs/2507.15272)
**Ayush Singh Bhadoriya et.al.** · 2025-07-21


#### [EchoVoices: Preserving Generational Voices and Memories for Seniors and Children](https://arxiv.org/abs/2507.15221)
**Haiying Xu et.al.** · 2025-07-21


#### [DMOSpeech 2: Reinforcement Learning for Duration Prediction in Metric-Optimized Speech Synthesis](https://arxiv.org/abs/2507.14988)
**Yinghao Aaron Li et.al.** · 2025-07-20


#### [FastLongSpeech: Enhancing Large Speech-Language Models for Efficient Long-Speech Processing](https://arxiv.org/abs/2507.14815)
**Shoutao Guo et.al.** · 2025-07-20


#### [A Data-Centric Framework for Addressing Phonetic and Prosodic Challenges in Russian Speech Generative Models](https://arxiv.org/abs/2507.13563)
**Kirill Borodin et.al.** · 2025-07-17


#### [NonverbalTTS: A Public English Corpus of Text-Aligned Nonverbal Vocalizations with Emotion Annotations for Text-to-Speech](https://arxiv.org/abs/2507.13155)
**Maksim Borisov et.al.** · 2025-07-17


#### [Intelligent Virtual Sonographer (IVS): Enhancing Physician-Robot-Patient Communication](https://arxiv.org/abs/2507.13052)
**Tianyu Song et.al.** · 2025-07-17


#### [Enkidu: Universal Frequential Perturbation for Real-Time Audio Privacy Protection against Voice Deepfakes](https://arxiv.org/abs/2507.12932)
**Zhou Feng et.al.** · 2025-07-17


#### [Quantize More, Lose Less: Autoregressive Generation from Residually Quantized Speech Representations](https://arxiv.org/abs/2507.12197)
**Yichen Han et.al.** · 2025-07-16


#### [EME-TTS: Unlocking the Emphasis and Emotion Link in Speech Synthesis](https://arxiv.org/abs/2507.12015)
**Haoxun Li et.al.** · 2025-07-16


#### [Evaluating Speech-to-Text x LLM x Text-to-Speech Combinations for AI Interview Systems](https://arxiv.org/abs/2507.16835)
**Nima Yazdani et.al.** · 2025-07-15


#### [Towards Scalable AASIST: Refining Graph Attention for Speech Deepfake Detection](https://arxiv.org/abs/2507.11777)
**Ivan Viakhirev et.al.** · 2025-07-15


#### [An Empirical Evaluation of AI-Powered Non-Player Characters' Perceived Realism and Performance in Virtual Reality Environments](https://arxiv.org/abs/2507.10469)
**Mikko Korkiakoski et.al.** · 2025-07-14


#### [DualDub: Video-to-Soundtrack Generation via Joint Speech and Background Audio Synthesis](https://arxiv.org/abs/2507.10109)
**Wenjie Tian et.al.** · 2025-07-14


#### [DeepGesture: A conversational gesture synthesis system based on emotions and semantics](https://arxiv.org/abs/2507.03147)
**Thanh Hoang-Minh et.al.** · 2025-07-14


#### [ZipVoice-Dialog: Non-Autoregressive Spoken Dialogue Generation with Flow Matching](https://arxiv.org/abs/2507.09318)
**Han Zhu et.al.** · 2025-07-12


#### [Voice Conversion for Lombard Speaking Style with Implicit and Explicit Acoustic Feature Conditioning](https://arxiv.org/abs/2507.09310)
**Dominika Woszczyk et.al.** · 2025-07-12


#### [ClaritySpeech: Dementia Obfuscation in Speech](https://arxiv.org/abs/2507.09282)
**Dominika Woszczyk et.al.** · 2025-07-12


#### [SemAlignVC: Enhancing zero-shot timbre conversion using semantic alignment](https://arxiv.org/abs/2507.09070)
**Shivam Mehta et.al.** · 2025-07-11


#### [Exploiting Leaderboards for Large-Scale Distribution of Malicious Models](https://arxiv.org/abs/2507.08983)
**Anshuman Suri et.al.** · 2025-07-11


#### [Unlocking Speech Instruction Data Potential with Query Rewriting](https://arxiv.org/abs/2507.08603)
**Yonghua Hei et.al.** · 2025-07-11


#### [MIDI-VALLE: Improving Expressive Piano Performance Synthesis Through Neural Codec Language Modelling](https://arxiv.org/abs/2507.08530)
**Jingjing Tang et.al.** · 2025-07-11


#### [Active Learning for Text-to-Speech Synthesis with Informative Sample Collection](https://arxiv.org/abs/2507.08319)
**Kentaro Seki et.al.** · 2025-07-11


#### [SecureSpeech: Prompt-based Speaker and Content Protection](https://arxiv.org/abs/2507.07799)
**Belinda Soh Hui Hui et.al.** · 2025-07-10


#### [STARS: A Unified Framework for Singing Transcription, Alignment, and Refined Style Annotation](https://arxiv.org/abs/2507.06670)
**Wenxiang Guo et.al.** · 2025-07-09


#### [Learning Japanese with Jouzu: Interaction Outcomes with Stylized Dialogue Fictional Agents](https://arxiv.org/abs/2507.06483)
**Zackary Rackauckas et.al.** · 2025-07-09


#### [Speech Quality Assessment Model Based on Mixture of Experts: System-Level Performance Enhancement and Utterance-Level Challenge Analysis](https://arxiv.org/abs/2507.06116)
**Xintong Hu et.al.** · 2025-07-08


#### [Differentiable Reward Optimization for LLM based TTS system](https://arxiv.org/abs/2507.05911)
**Changfeng Gao et.al.** · 2025-07-08


#### [OpenS2S: Advancing Fully Open-Source End-to-End Empathetic Large Speech Language Model](https://arxiv.org/abs/2507.05177)
**Chen Wang et.al.** · 2025-07-08


#### [SpeechAccentLLM: A Unified Framework for Foreign Accent Conversion and Text to Speech](https://arxiv.org/abs/2507.01348)
**Zhuangfei Cheng et.al.** · 2025-07-08


#### [LAPS-Diff: A Diffusion-Based Framework for Singing Voice Synthesis With Language Aware Prosody-Style Guided Learning](https://arxiv.org/abs/2507.04966)
**Sandipan Dhar et.al.** · 2025-07-07


#### [Multi-Step Prediction and Control of Hierarchical Emotion Distribution in Text-to-Speech Synthesis](https://arxiv.org/abs/2507.04598)
**Sho Inoue et.al.** · 2025-07-07


#### [A Hybrid Machine Learning Framework for Optimizing Crop Selection via Agronomic and Economic Forecasting](https://arxiv.org/abs/2507.08832)
**Niranjan Mallikarjun Sindhur et.al.** · 2025-07-06


#### [TTS-CtrlNet: Time varying emotion aligned text-to-speech generation with ControlNet](https://arxiv.org/abs/2507.04349)
**Jaeseok Jeong et.al.** · 2025-07-06


#### [RepeaTTS: Towards Feature Discovery through Repeated Fine-Tuning](https://arxiv.org/abs/2507.08012)
**Atli Sigurgeirsson et.al.** · 2025-07-05


#### [PresentAgent: Multimodal Agent for Presentation Video Generation](https://arxiv.org/abs/2507.04036)
**Jingwei Shi et.al.** · 2025-07-05


#### [Prosody Labeling with Phoneme-BERT and Speech Foundation Models](https://arxiv.org/abs/2507.03912)
**Tomoki Koriyama et.al.** · 2025-07-05


#### [Traceable TTS: Toward Watermark-Free TTS with Strong Traceability](https://arxiv.org/abs/2507.03887)
**Yuxiang Zhao et.al.** · 2025-07-05


#### [Pronunciation Editing for Finnish Speech using Phonetic Posteriorgrams](https://arxiv.org/abs/2507.02115)
**Zirui Li et.al.** · 2025-07-04


#### [De-AntiFake: Rethinking the Protective Perturbations Against Voice Cloning Attacks](https://arxiv.org/abs/2507.02606)
**Wei Fan et.al.** · 2025-07-03


#### [Open-Source System for Multilingual Translation and Cloned Speech Synthesis](https://arxiv.org/abs/2507.02530)
**Mateo Cámara et.al.** · 2025-07-03


#### [JoyTTS: LLM-based Spoken Chatbot With Voice Cloning](https://arxiv.org/abs/2507.02380)
**Fangru Zhou et.al.** · 2025-07-03


#### [Analyzing and Improving Speaker Similarity Assessment for Speech Synthesis](https://arxiv.org/abs/2507.02176)
**Marc-André Carbonneau et.al.** · 2025-07-02


#### [A Dataset for Automatic Assessment of TTS Quality in Spanish](https://arxiv.org/abs/2507.01805)
**Alejandro Sosa Welford et.al.** · 2025-07-02


#### [Voice Conversion for Likability Control via Automated Rating of Speech Synthesis Corpora](https://arxiv.org/abs/2507.01356)
**Hitoshi Suda et.al.** · 2025-07-02


#### [Multi-interaction TTS toward professional recording reproduction](https://arxiv.org/abs/2507.00808)
**Hiroki Kanagawa et.al.** · 2025-07-02


#### [MuteSwap: Silent Face-based Voice Conversion](https://arxiv.org/abs/2507.00498)
**Yifan Liu et.al.** · 2025-07-01


#### [StreamFlow: Streaming Flow Matching with Block-wise Guided Attention Mask for Speech Token Decoding](https://arxiv.org/abs/2506.23986)
**Dake Guo et.al.** · 2025-07-01


#### [Collecting, Curating, and Annotating Good Quality Speech deepfake dataset for Famous Figures: Process and Challenges](https://arxiv.org/abs/2507.00324)
**Hashim Ali et.al.** · 2025-06-30


#### [Investigating Stochastic Methods for Prosody Modeling in Speech Synthesis](https://arxiv.org/abs/2507.00227)
**Paul Mayer et.al.** · 2025-06-30


#### [Efficient Interleaved Speech Modeling through Knowledge Distillation](https://arxiv.org/abs/2506.23670)
**Mohammadmahdi Nouriborji et.al.** · 2025-06-30


#### [JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching](https://arxiv.org/abs/2506.23552)
**Mingi Kwon et.al.** · 2025-06-30


#### [You Sound a Little Tense: L2 Tailored Clear TTS Using Durational Vowel Properties](https://arxiv.org/abs/2506.23367)
**Paige Tuttösí et.al.** · 2025-06-29


#### [DiffSoundStream: Efficient Speech Tokenization via Diffusion Decoding](https://arxiv.org/abs/2506.22362)
**Yang Yang et.al.** · 2025-06-27


#### [Evaluating Pointing Gestures for Target Selection in Human-Robot Collaboration](https://arxiv.org/abs/2506.22116)
**Noora Sassali et.al.** · 2025-06-27


#### [Robust and Efficient Autoregressive Speech Synthesis with Dynamic Chunk-wise Prediction Policy](https://arxiv.org/abs/2506.22023)
**Bohan Li et.al.** · 2025-06-27


#### [SmoothSinger: A Conditional Diffusion Model for Singing Voice Synthesis with Multi-Resolution Architecture](https://arxiv.org/abs/2506.21478)
**Kehan Sui et.al.** · 2025-06-26


#### [A Multi-Stage Framework for Multimodal Controllable Speech Synthesis](https://arxiv.org/abs/2506.20945)
**Rui Niu et.al.** · 2025-06-26


#### [An Exploration of ECAPA-TDNN and x-vector Speaker Representations in Zero-shot Multi-speaker TTS](https://arxiv.org/abs/2506.20190)
**Marie Kunešová et.al.** · 2025-06-25


#### [SLEEPING-DISCO 9M: A large-scale pre-training dataset for generative music modeling](https://arxiv.org/abs/2506.14293)
**Tawsif Ahmed et.al.** · 2025-06-25


#### [TTSDS2: Resources and Benchmark for Evaluating Human-Quality Text to Speech Systems](https://arxiv.org/abs/2506.19441)
**Christoph Minixhofer et.al.** · 2025-06-24


#### [IndexTTS2: A Breakthrough in Emotionally Expressive and Duration-Controlled Auto-Regressive Zero-Shot Text-to-Speech](https://arxiv.org/abs/2506.21619)
**Siyi Zhou et.al.** · 2025-06-23


#### [Selecting N-lowest scores for training MOS prediction models](https://arxiv.org/abs/2506.18326)
**Yuto Kondo et.al.** · 2025-06-23


#### [Rethinking Mean Opinion Scores in Speech Quality Assessment: Aggregation through Quantized Distribution Fitting](https://arxiv.org/abs/2506.18307)
**Yuto Kondo et.al.** · 2025-06-23


#### [JIS: A Speech Corpus of Japanese Idol Speakers with Various Speaking Styles](https://arxiv.org/abs/2506.18296)
**Yuto Kondo et.al.** · 2025-06-23


#### [OpusLM: A Family of Open Unified Speech Language Models](https://arxiv.org/abs/2506.17611)
**Jinchuan Tian et.al.** · 2025-06-21


#### [RapFlow-TTS: Rapid and High-Fidelity Text-to-Speech with Improved Consistency Flow Matching](https://arxiv.org/abs/2506.16741)
**Hyun Joon Park et.al.** · 2025-06-20


#### [LM-SPT: LM-Aligned Semantic Distillation for Speech Tokenization](https://arxiv.org/abs/2506.16738)
**Daejin Jo et.al.** · 2025-06-20


#### [V-CASS: Vision-context-aware Expressive Speech Synthesis for Enhancing User Understanding of Videos](https://arxiv.org/abs/2506.16716)
**Qixin Wang et.al.** · 2025-06-20


#### [ZipVoice: Fast and High-Quality Zero-Shot Text-to-Speech with Flow Matching](https://arxiv.org/abs/2506.13053)
**Han Zhu et.al.** · 2025-06-20


#### [Streaming Non-Autoregressive Model for Accent Conversion and Pronunciation Improvement](https://arxiv.org/abs/2506.16580)
**Tuan-Nam Nguyen et.al.** · 2025-06-19


#### [InstructTTSEval: Benchmarking Complex Natural-Language Instruction Following in Text-to-Speech Systems](https://arxiv.org/abs/2506.16381)
**Kexin Huang et.al.** · 2025-06-19


#### [Optimizing Multilingual Text-To-Speech with Accents & Emotions](https://arxiv.org/abs/2506.16310)
**Pranav Pawar et.al.** · 2025-06-19


#### [Improved Intelligibility of Dysarthric Speech using Conditional Flow Matching](https://arxiv.org/abs/2506.16127)
**Shoutrik Das et.al.** · 2025-06-19


#### [VS-Singer: Vision-Guided Stereo Singing Voice Synthesis with Consistency Schrödinger Bridge](https://arxiv.org/abs/2506.16020)
**Zijing Zhao et.al.** · 2025-06-19


#### [TTSOps: A Closed-Loop Corpus Optimization Framework for Training Multi-Speaker TTS Models from Dark Data](https://arxiv.org/abs/2506.15614)
**Kentaro Seki et.al.** · 2025-06-18


#### [PredGen: Accelerated Inference of Large Language Models through Input-Time Speculation for Real-Time Speech Interaction](https://arxiv.org/abs/2506.15556)
**Shufan Li et.al.** · 2025-06-18


#### [Factorized RVQ-GAN For Disentangled Speech Tokenization](https://arxiv.org/abs/2506.15456)
**Sameer Khurana et.al.** · 2025-06-18


#### [EmojiVoice: Towards long-term controllable expressivity in robot speech](https://arxiv.org/abs/2506.15085)
**Paige Tuttösí et.al.** · 2025-06-18


#### [An accurate and revised version of optical character recognition-based speech synthesis using LabVIEW](https://arxiv.org/abs/2506.15029)
**Prateek Mehta et.al.** · 2025-06-18


#### [Pushing the Performance of Synthetic Speech Detection with Kolmogorov-Arnold Networks and Self-Supervised Learning Models](https://arxiv.org/abs/2506.14153)
**Tuan Dat Phuong et.al.** · 2025-06-17


#### [EmoNews: A Spoken Dialogue System for Expressive News Conversations](https://arxiv.org/abs/2506.13894)
**Ryuki Matsuura et.al.** · 2025-06-16


#### [From Flat to Feeling: A Feasibility and Impact Study on Dynamic Facial Emotions in AI-Generated Avatars](https://arxiv.org/abs/2506.13477)
**Pegah Salehi et.al.** · 2025-06-16


#### [A Self-Refining Framework for Enhancing ASR Using TTS-Synthesized Data](https://arxiv.org/abs/2506.11130)
**Cheng-Kang Chou et.al.** · 2025-06-16


#### [EmoNet-Voice: A Fine-Grained, Expert-Verified Benchmark for Speech Emotion Detection](https://arxiv.org/abs/2506.09827)
**Christoph Schuhmann et.al.** · 2025-06-15


#### [StreamMel: Real-Time Zero-shot Text-to-Speech via Interleaved Continuous Autoregressive Modeling](https://arxiv.org/abs/2506.12570)
**Hui Wang et.al.** · 2025-06-14


#### [Speech-Language Models with Decoupled Tokenizers and Multi-Token Prediction](https://arxiv.org/abs/2506.12537)
**Xiaoran Fan et.al.** · 2025-06-14


#### [Phonikud: Hebrew Grapheme-to-Phoneme Conversion for Real-Time Text-to-Speech](https://arxiv.org/abs/2506.12311)
**Yakov Kolani et.al.** · 2025-06-14


#### [Step-Audio-AQAA: a Fully End-to-End Expressive Large Audio Language Model](https://arxiv.org/abs/2506.08967)
**Ailin Huang et.al.** · 2025-06-13


#### [Scheduled Interleaved Speech-Text Training for Speech-to-Speech Translation with LLMs](https://arxiv.org/abs/2506.10299)
**Hayato Futami et.al.** · 2025-06-12


#### [S2ST-Omni: An Efficient and Scalable Multilingual Speech-to-Speech Translation Framework via Seamlessly Speech-Text Alignment and Streaming Speech Decoder](https://arxiv.org/abs/2506.11160)
**Yu Pan et.al.** · 2025-06-11


#### [UmbraTTS: Adapting Text-to-Speech to Environmental Contexts with Flow Matching](https://arxiv.org/abs/2506.09874)
**Neta Glazer et.al.** · 2025-06-11


#### [OmniDRCA: Parallel Speech-Text Foundation Model via Dual-Resolution Speech Representations and Contrastive Alignment](https://arxiv.org/abs/2506.09349)
**Chao-Hong Tan et.al.** · 2025-06-11


#### [Ming-Omni: A Unified Multimodal Model for Perception and Generation](https://arxiv.org/abs/2506.09344)
**Inclusion AI et.al.** · 2025-06-11


#### [GUIRoboTron-Speech: Towards Automated GUI Agents Based on Speech Instructions](https://arxiv.org/abs/2506.11127)
**Wenkang Han et.al.** · 2025-06-10


#### [ASRJam: Human-Friendly AI Speech Jamming to Prevent Automated Phone Scams](https://arxiv.org/abs/2506.11125)
**Freddie Grabovski et.al.** · 2025-06-10


#### [A Review on Score-based Generative Models for Audio Applications](https://arxiv.org/abs/2506.08457)
**Ge Zhu et.al.** · 2025-06-10


#### [Towards Generalized Source Tracing for Codec-Based Deepfake Speech](https://arxiv.org/abs/2506.07294)
**Xuanjun Chen et.al.** · 2025-06-10


#### [Seeing Voices: Generating A-Roll Video from Audio with Mirage](https://arxiv.org/abs/2506.08279)
**Aditi Sundararaman et.al.** · 2025-06-09


#### [Transcript-Prompted Whisper with Dictionary-Enhanced Decoding for Japanese Speech Annotation](https://arxiv.org/abs/2506.07646)
**Rui Hu et.al.** · 2025-06-09


#### [Voice Impression Control in Zero-Shot TTS](https://arxiv.org/abs/2506.05688)
**Keinichi Fujita et.al.** · 2025-06-09


#### [SynHate: Detecting Hate Speech in Synthetic Deepfake Audio](https://arxiv.org/abs/2506.06772)
**Rishabh Ranjan et.al.** · 2025-06-07


#### [A Survey of Automatic Evaluation Methods on Text, Visual and Speech Generations](https://arxiv.org/abs/2506.10019)
**Tian Lan et.al.** · 2025-06-06


#### [Audio-Aware Large Language Models as Judges for Speaking Styles](https://arxiv.org/abs/2506.05984)
**Cheng-Han Chiang et.al.** · 2025-06-06


#### [Intelligibility of Text-to-Speech Systems for Mathematical Expressions](https://arxiv.org/abs/2506.11086)
**Sujoy Roychowdhury et.al.** · 2025-06-05


#### [Grapheme-Coherent Phonemic and Prosodic Annotation of Speech by Implicit and Explicit Grapheme Conditioning](https://arxiv.org/abs/2506.04527)
**Hien Ohnaka et.al.** · 2025-06-05


#### [Can we reconstruct a dysarthric voice with the large speech model Parler TTS?](https://arxiv.org/abs/2506.04397)
**Ariadna Sanchez et.al.** · 2025-06-04


#### [HiFiTTS-2: A Large-Scale High Bandwidth Speech Dataset](https://arxiv.org/abs/2506.04152)
**Ryan Langman et.al.** · 2025-06-04


#### [UniCUE: Unified Recognition and Generation Framework for Chinese Cued Speech Video-to-Speech Generation](https://arxiv.org/abs/2506.04134)
**Jinting Wang et.al.** · 2025-06-04


#### [A Novel Data Augmentation Approach for Automatic Speaking Assessment on Opinion Expressions](https://arxiv.org/abs/2506.04077)
**Chung-Chun Wang et.al.** · 2025-06-04


#### [Kinship in Speech: Leveraging Linguistic Relatedness for Zero-Shot TTS in Indian Languages](https://arxiv.org/abs/2506.03884)
**Utkarsh Pathak et.al.** · 2025-06-04


#### [Mark My Words: A Robust Multilingual Model for Punctuation in Text and Speech Transcripts](https://arxiv.org/abs/2506.03793)
**Sidharth Pulipaka et.al.** · 2025-06-04


#### [Comparative Analysis of Fast and High-Fidelity Neural Vocoders for Low-Latency Streaming Synthesis in Resource-Constrained Environments](https://arxiv.org/abs/2506.03554)
**Reo Yoneyama et.al.** · 2025-06-04


#### [BitTTS: Highly Compact Text-to-Speech Using 1.58-bit Quantization and Weight Indexing](https://arxiv.org/abs/2506.03515)
**Masaya Kawamura et.al.** · 2025-06-04


#### [Controllable Text-to-Speech Synthesis with Masked-Autoencoded Style-Rich Representation](https://arxiv.org/abs/2506.02997)
**Yongqi Wang et.al.** · 2025-06-03


#### [Towards a Japanese Full-duplex Spoken Dialogue System](https://arxiv.org/abs/2506.02979)
**Atsumoto Ohashi et.al.** · 2025-06-03


#### [PartialEdit: Identifying Partial Deepfakes in the Era of Neural Speech Editing](https://arxiv.org/abs/2506.02958)
**You Zhang et.al.** · 2025-06-03


#### [CapSpeech: Enabling Downstream Applications in Style-Captioned Text-to-Speech](https://arxiv.org/abs/2506.02863)
**Helin Wang et.al.** · 2025-06-03


#### [Prompt-Unseen-Emotion: Zero-shot Expressive Speech Synthesis with Prompt-LLM Contextual Knowledge for Mixed Emotions](https://arxiv.org/abs/2506.02742)
**Xiaoxue Gao et.al.** · 2025-06-03


#### [StarVC: A Unified Auto-Regressive Framework for Joint Text and Speech Generation in Voice Conversion](https://arxiv.org/abs/2506.02414)
**Fengjin Li et.al.** · 2025-06-03


#### [SingaKids: A Multilingual Multimodal Dialogic Tutor for Language Learning](https://arxiv.org/abs/2506.02412)
**Zhengyuan Liu et.al.** · 2025-06-03


#### [Trusted Fake Audio Detection Based on Dirichlet Distribution](https://arxiv.org/abs/2506.02401)
**Chi Ding et.al.** · 2025-06-03


#### [Dhvani: A Weakly-supervised Phonemic Error Detection and Personalized Feedback System for Hindi](https://arxiv.org/abs/2506.02166)
**Arnav Rustagi et.al.** · 2025-06-02


#### [SALF-MOS: Speaker Agnostic Latent Features Downsampled for MOS Prediction](https://arxiv.org/abs/2506.02082)
**Saurabh Agrawal et.al.** · 2025-06-02


#### [Universal Preference-Score-based Pairwise Speech Quality Assessment](https://arxiv.org/abs/2506.01455)
**Yu-Fei Shi et.al.** · 2025-06-02


#### [Speech-to-Speech Translation Pipelines for Conversations in Low-Resource Languages](https://arxiv.org/abs/2506.01406)
**Andrei Popescu-Belis et.al.** · 2025-06-02


#### [Zero-Shot Text-to-Speech for Vietnamese](https://arxiv.org/abs/2506.01322)
**Thi Vu et.al.** · 2025-06-02


#### [CleanS2S: Single-file Framework for Proactive Speech-to-Speech Interaction](https://arxiv.org/abs/2506.01268)
**Yudong Lu et.al.** · 2025-06-02


#### [WCTC-Biasing: Retraining-free Contextual Biasing ASR with Wildcard CTC-based Keyword Spotting and Inter-layer Biasing](https://arxiv.org/abs/2506.01263)
**Yu Nakagome et.al.** · 2025-06-02


#### [Zero-Shot Streaming Text to Speech Synthesis with Transducer and Auto-Regressive Modeling](https://arxiv.org/abs/2505.19669)
**Haiyang Sun et.al.** · 2025-06-02


#### [Source Tracing of Synthetic Speech Systems Through Paralinguistic Pre-Trained Representations](https://arxiv.org/abs/2506.01157)
**Girish et.al.** · 2025-06-01


#### [DS-TTS: Zero-Shot Speaker Style Adaptation from Voice Clips via Dynamic Dual-Style Feature Modulation](https://arxiv.org/abs/2506.01020)
**Ming Meng et.al.** · 2025-06-01


#### [Rhythm Controllable and Efficient Zero-Shot Voice Conversion via Shortcut Flow Matching](https://arxiv.org/abs/2506.01014)
**Jialong Zuo et.al.** · 2025-06-01


#### [CoVoMix2: Advancing Zero-Shot Dialogue Generation with Fully Non-Autoregressive Flow Matching](https://arxiv.org/abs/2506.00885)
**Leying Zhang et.al.** · 2025-06-01


#### [Counterfactual Activation Editing for Post-hoc Prosody and Mispronunciation Correction in TTS Models](https://arxiv.org/abs/2506.00832)
**Kyowoon Lee et.al.** · 2025-06-01


#### [ARECHO: Autoregressive Evaluation via Chain-Based Hypothesis Optimization for Speech Multi-Metric Estimation](https://arxiv.org/abs/2505.24518)
**Jiatong Shi et.al.** · 2025-05-30


#### [Speech Token Prediction via Compressed-to-fine Language Modeling for Speech Generation](https://arxiv.org/abs/2505.24496)
**Wenrui Liu et.al.** · 2025-05-30


#### [DS-Codec: Dual-Stage Training with Mirror-to-NonMirror Architecture Switching for Speech Codec](https://arxiv.org/abs/2505.24314)
**Peijie Chen et.al.** · 2025-05-30


#### [Accelerating Diffusion-based Text-to-Speech Model Training with Dual Modality Alignment](https://arxiv.org/abs/2505.19595)
**Jeongsoo Choi et.al.** · 2025-05-30


#### [Can Emotion Fool Anti-spoofing?](https://arxiv.org/abs/2505.23962)
**Aurosweta Mahapatra et.al.** · 2025-05-29


#### [Few-Shot Speech Deepfake Detection Adaptation with Gaussian Processes](https://arxiv.org/abs/2505.23619)
**Neta Glazer et.al.** · 2025-05-29


#### [EmergentTTS-Eval: Evaluating TTS Models on Complex Prosodic, Expressiveness, and Linguistic Challenges Using Model-as-a-Judge](https://arxiv.org/abs/2505.23009)
**Ruskin Raj Manku et.al.** · 2025-05-29


#### [LLM-Synth4KWS: Scalable Automatic Generation and Synthesis of Confusable Data for Custom Keyword Spotting](https://arxiv.org/abs/2505.22995)
**Pai Zhu et.al.** · 2025-05-29


#### [BinauralFlow: A Causal and Streamable Approach for High-Quality Binaural Speech Synthesis with Flow Matching Models](https://arxiv.org/abs/2505.22865)
**Susan Liang et.al.** · 2025-05-28


#### [Tell me Habibi, is it Real or Fake?](https://arxiv.org/abs/2505.22581)
**Kartik Kuckreja et.al.** · 2025-05-28


#### [A Linguistically Motivated Analysis of Intonational Phrasing in Text-to-Speech Systems: Revealing Gaps in Syntactic Sensitivity](https://arxiv.org/abs/2505.22236)
**Charlotte Pouw et.al.** · 2025-05-28


#### [Spotlight-TTS: Spotlighting the Style via Voiced-Aware Style Extraction and Style Direction Adjustment for Expressive Text-to-Speech](https://arxiv.org/abs/2505.20868)
**Nam-Gyu Kim et.al.** · 2025-05-27


#### [RASMALAI: Resources for Adaptive Speech Modeling in Indian Languages with Accents and Intonations](https://arxiv.org/abs/2505.18609)
**Ashwin Sankar et.al.** · 2025-05-27


#### [CosyVoice 3: Towards In-the-wild Speech Generation via Scaling-up and Post-training](https://arxiv.org/abs/2505.17589)
**Zhihao Du et.al.** · 2025-05-27


#### [ArVoice: A Multi-Speaker Dataset for Arabic Speech Synthesis](https://arxiv.org/abs/2505.20506)
**Hawau Olamide Toyin et.al.** · 2025-05-26


#### [Accelerating Flow-Matching-Based Text-to-Speech via Empirically Pruned Step Sampling](https://arxiv.org/abs/2505.19931)
**Qixi Zheng et.al.** · 2025-05-26


#### [DiEmo-TTS: Disentangled Emotion Representations via Self-Supervised Distillation for Cross-Speaker Emotion Transfer in Text-to-Speech](https://arxiv.org/abs/2505.19687)
**Deok-Hyeon Cho et.al.** · 2025-05-26


#### [KIT's Low-resource Speech Translation Systems for IWSLT2025: System Enhancement with Synthetic Data and Model Regularization](https://arxiv.org/abs/2505.19679)
**Zhaolin Li et.al.** · 2025-05-26


#### [GSA-TTS : Toward Zero-Shot Speech Synthesis based on Gradual Style Adaptor](https://arxiv.org/abs/2505.19384)
**Seokgi Lee et.al.** · 2025-05-26


#### [SpeakStream: Streaming Text-to-Speech with Interleaved Data](https://arxiv.org/abs/2505.19206)
**Richard He Bai et.al.** · 2025-05-25


#### [CloneShield: A Framework for Universal Perturbation Against Zero-Shot Voice Cloning](https://arxiv.org/abs/2505.19119)
**Renyuan Li et.al.** · 2025-05-25


#### [Revival with Voice: Multi-modal Controllable Text-to-Speech Synthesis](https://arxiv.org/abs/2505.18972)
**Minsu Kim et.al.** · 2025-05-25


#### [MPE-TTS: Customized Emotion Zero-Shot Text-To-Speech Using Multi-Modal Prompt](https://arxiv.org/abs/2505.18453)
**Zhichao Wu et.al.** · 2025-05-24


#### [What You Read Isn't What You Hear: Linguistic Sensitivity in Deepfake Speech Detection](https://arxiv.org/abs/2505.17513)
**Binh Nguyen et.al.** · 2025-05-23


#### [UniTTS: An end-to-end TTS system without decoupling of acoustic and semantic information](https://arxiv.org/abs/2505.17426)
**Rui Wang et.al.** · 2025-05-23


#### [Speechless: Speech Instruction Training Without Speech for Low Resource Languages](https://arxiv.org/abs/2505.17417)
**Alan Dao et.al.** · 2025-05-23


#### [U-SAM: An audio language Model for Unified Speech, Audio, and Music Understanding](https://arxiv.org/abs/2505.13880)
**Ziqian Wang et.al.** · 2025-05-23


#### [Benchmarking Expressive Japanese Character Text-to-Speech with VITS and Style-BERT-VITS2](https://arxiv.org/abs/2505.17320)
**Zackary Rackauckas et.al.** · 2025-05-22


#### [MM-MovieDubber: Towards Multi-Modal Learning for Multi-Modal Movie Dubbing](https://arxiv.org/abs/2505.16279)
**Junjie Zheng et.al.** · 2025-05-22


#### [Improving Noise Robustness of LLM-based Zero-shot TTS via Discrete Acoustic Token Denoising](https://arxiv.org/abs/2505.13830)
**Ye-Xin Lu et.al.** · 2025-05-22


#### [Voicing Personas: Rewriting Persona Descriptions into Style Prompts for Controllable Text-to-Speech](https://arxiv.org/abs/2505.17093)
**Yejin Lee et.al.** · 2025-05-21


#### [MIKU-PAL: An Automated and Standardized Multi-Modal Method for Speech Paralinguistic and Affect Labeling](https://arxiv.org/abs/2505.15772)
**Yifan Cheng et.al.** · 2025-05-21


#### [Segmentation-Variant Codebooks for Preservation of Paralinguistic and Prosodic Information](https://arxiv.org/abs/2505.15667)
**Nicholas Sanders et.al.** · 2025-05-21


#### [Audio Jailbreak: An Open Comprehensive Benchmark for Jailbreaking Large Audio-Language Models](https://arxiv.org/abs/2505.15406)
**Zirui Song et.al.** · 2025-05-21


#### [Prosody-Adaptable Audio Codecs for Zero-Shot Voice Conversion via In-Context Learning](https://arxiv.org/abs/2505.15402)
**Junchuan Zhao et.al.** · 2025-05-21


#### [Accelerating Autoregressive Speech Synthesis Inference With Speech Speculative Decoding](https://arxiv.org/abs/2505.15380)
**Zijian Lin et.al.** · 2025-05-21


#### [AudioJailbreak: Jailbreak Attacks against End-to-End Large Audio-Language Models](https://arxiv.org/abs/2505.14103)
**Guangke Chen et.al.** · 2025-05-21


#### [Impact of Frame Rates on Speech Tokenizer: A Case Study on Mandarin and English](https://arxiv.org/abs/2505.17076)
**Haoyang Zhang et.al.** · 2025-05-20


#### [TCSinger 2: Customizable Multilingual Zero-shot Singing Voice Synthesis](https://arxiv.org/abs/2505.14910)
**Yu Zhang et.al.** · 2025-05-20


#### [Vox-Profile: A Speech Foundation Model Benchmark for Characterizing Diverse Speaker and Speech Traits](https://arxiv.org/abs/2505.14648)
**Tiantian Feng et.al.** · 2025-05-20


#### [Pairwise Evaluation of Accent Similarity in Speech Synthesis](https://arxiv.org/abs/2505.14410)
**Jinzuomu Zhong et.al.** · 2025-05-20


#### [FMSD-TTS: Few-shot Multi-Speaker Multi-Dialect Text-to-Speech Synthesis for Ü-Tsang, Amdo and Kham Speech Dataset Generation](https://arxiv.org/abs/2505.14351)
**Yutong Liu et.al.** · 2025-05-20


#### [SeamlessEdit: Background Noise Aware Zero-Shot Speech Editing with in-Context Enhancement](https://arxiv.org/abs/2505.14066)
**Kuan-Yu Chen et.al.** · 2025-05-20


#### [Articulatory Feature Prediction from Surface EMG during Speech Production](https://arxiv.org/abs/2505.13814)
**Jihwan Lee et.al.** · 2025-05-20


#### [Efficient Speech Language Modeling via Energy Distance in Continuous Latent Space](https://arxiv.org/abs/2505.13181)
**Zhengrui Ma et.al.** · 2025-05-19


#### [DualCodec: A Low-Frame-Rate, Semantically-Enhanced Neural Audio Codec for Speech Generation](https://arxiv.org/abs/2505.13000)
**Jiaqi Li et.al.** · 2025-05-19


#### [Codec-Based Deepfake Source Tracing via Neural Audio Codec Taxonomy](https://arxiv.org/abs/2505.12994)
**Xuanjun Chen et.al.** · 2025-05-19


#### [OZSpeech: One-step Zero-shot Speech Synthesis with Learned-Prior-Conditioned Flow Matching](https://arxiv.org/abs/2505.12800)
**Hieu-Nghia Huynh-Nguyen et.al.** · 2025-05-19


#### [RoVo: Robust Voice Protection Against Unauthorized Speech Synthesis with Embedding-Level Perturbations](https://arxiv.org/abs/2505.12686)
**Seungmin Kim et.al.** · 2025-05-19


#### [Chain-Talker: Chain Understanding and Rendering for Empathetic Conversational Speech Synthesis](https://arxiv.org/abs/2505.12597)
**Yifan Hu et.al.** · 2025-05-19


#### [Shallow Flow Matching for Coarse-to-Fine Text-to-Speech Synthesis](https://arxiv.org/abs/2505.12226)
**Dong Yang et.al.** · 2025-05-18


#### [LipDiffuser: Lip-to-Speech Generation with Conditional Diffusion Models](https://arxiv.org/abs/2505.11391)
**Danilo de Oliveira et.al.** · 2025-05-16


#### [Audio Turing Test: Benchmarking the Human-likeness of Large Language Model-based Text-to-Speech Systems in Chinese](https://arxiv.org/abs/2505.11200)
**Xihuai Wang et.al.** · 2025-05-16


#### [BanglaFake: Constructing and Evaluating a Specialized Bengali Deepfake Audio Dataset](https://arxiv.org/abs/2505.10885)
**Istiaq Ahmed Fahad et.al.** · 2025-05-16


#### [UDDETTS: Unifying Discrete and Dimensional Emotions for Controllable Emotional Text-to-Speech](https://arxiv.org/abs/2505.10599)
**Jiaxuan Liu et.al.** · 2025-05-15


#### [FlexSpeech: Towards Stable, Controllable and Expressive Text-to-Speech](https://arxiv.org/abs/2505.05159)
**Linhan Ma et.al.** · 2025-05-15


#### [SingNet: Towards a Large-Scale, Diverse, and In-the-Wild Singing Voice Dataset](https://arxiv.org/abs/2505.09325)
**Yicheng Gu et.al.** · 2025-05-14


#### [DPN-GAN: Inducing Periodic Activations in Generative Adversarial Networks for High-Fidelity Audio Synthesis](https://arxiv.org/abs/2505.09091)
**Zeeshan Ahmad et.al.** · 2025-05-14


#### [Investigating self-supervised features for expressive, multilingual voice conversion](https://arxiv.org/abs/2505.08278)
**Álvaro Martín-Cortinas et.al.** · 2025-05-13


#### [SonicRAG : High Fidelity Sound Effects Synthesis Based on Retrival Augmented Generation](https://arxiv.org/abs/2505.03244)
**Yu-Ren Guo et.al.** · 2025-05-13


#### [MiniMax-Speech: Intrinsic Zero-Shot Text-to-Speech with a Learnable Speaker Encoder](https://arxiv.org/abs/2505.07916)
**Bowen Zhang et.al.** · 2025-05-12


#### [Lightweight End-to-end Text-to-speech Synthesis for low resource on-device applications](https://arxiv.org/abs/2505.07701)
**Biel Tura Vecino et.al.** · 2025-05-12


#### [VTutor: An Animated Pedagogical Agent SDK that Provide Real Time Multi-Model Feedback](https://arxiv.org/abs/2505.06676)
**Eason Chen et.al.** · 2025-05-10


#### [Bridging the Gap: An Intermediate Language for Enhanced and Cost-Effective Grapheme-to-Phoneme Conversion with Homographs with Multiple Pronunciations Disambiguation](https://arxiv.org/abs/2505.06599)
**Abbas Bertina et.al.** · 2025-05-10


#### [Teochew-Wild: The First In-the-wild Teochew Dataset with Orthographic Annotations](https://arxiv.org/abs/2505.05056)
**Linrong Pan et.al.** · 2025-05-08


#### [A Multi-Agent AI Framework for Immersive Audiobook Production through Spatial Audio and Neural Narration](https://arxiv.org/abs/2505.04885)
**Shaja Arul Selvamani et.al.** · 2025-05-08


#### [Advancing Zero-shot Text-to-Speech Intelligibility across Diverse Domains via Preference Alignment](https://arxiv.org/abs/2505.04113)
**Xueyao Zhang et.al.** · 2025-05-07


#### [VITA-Audio: Fast Interleaved Cross-Modal Token Generation for Efficient Large Speech-Language Model](https://arxiv.org/abs/2505.03739)
**Zuwei Long et.al.** · 2025-05-06


#### [Generating Narrated Lecture Videos from Slides with Synchronized Highlights](https://arxiv.org/abs/2505.02966)
**Alexander Holmberg et.al.** · 2025-05-05


#### [Voila: Voice-Language Foundation Models for Real-Time Autonomous Interaction and Voice Role-Play](https://arxiv.org/abs/2505.02707)
**Yemin Shi et.al.** · 2025-05-05


#### [LLaMA-Omni2: LLM-based Real-time Spoken Chatbot with Autoregressive Streaming Speech Synthesis](https://arxiv.org/abs/2505.02625)
**Qingkai Fang et.al.** · 2025-05-05


#### [Towards Flow-Matching-based TTS without Classifier-Free Guidance](https://arxiv.org/abs/2504.20334)
**Yuzhe Liang et.al.** · 2025-05-02


#### [Towards Film-Making Production Dialogue, Narration, Monologue Adaptive Moving Dubbing Benchmarks](https://arxiv.org/abs/2505.01450)
**Chaoyi Wang et.al.** · 2025-04-30


#### [Sadeed: Advancing Arabic Diacritization Through Small Language Model](https://arxiv.org/abs/2504.21635)
**Zeina Aldallal et.al.** · 2025-04-30


#### [AlignDiT: Multimodal Aligned Diffusion Transformer for Synchronized Speech Generation](https://arxiv.org/abs/2504.20629)
**Jeongsoo Choi et.al.** · 2025-04-29


#### [ClonEval: An Open Voice Cloning Benchmark](https://arxiv.org/abs/2504.20581)
**Iwona Christop et.al.** · 2025-04-29


#### [Generative Adversarial Network based Voice Conversion: Techniques, Challenges, and Recent Advancements](https://arxiv.org/abs/2504.19197)
**Sandipan Dhar et.al.** · 2025-04-27


#### [Muyan-TTS: A Trainable Text-to-Speech Model Optimized for Podcast Scenarios with a $50K Budget](https://arxiv.org/abs/2504.19146)
**Xin Li et.al.** · 2025-04-27


#### [FADEL: Uncertainty-aware Fake Audio Detection with Evidential Deep Learning](https://arxiv.org/abs/2504.15663)
**Ju Yeon Kang et.al.** · 2025-04-22


#### [A Multi-Agent Framework for Automated Qinqiang Opera Script Generation Using Large Language Models](https://arxiv.org/abs/2504.15552)
**Gengxian Cao et.al.** · 2025-04-22


#### [EmoVoice: LLM-based Emotional Text-To-Speech Model with Freestyle Text Prompting](https://arxiv.org/abs/2504.12867)
**Guanrou Yang et.al.** · 2025-04-22


#### [SOLIDO: A Robust Watermarking Method for Speech Synthesis via Low-Rank Adaptation](https://arxiv.org/abs/2504.15035)
**Yue Li et.al.** · 2025-04-21


#### [DialogueAgents: A Hybrid Agent-Based Speech Synthesis Framework for Multi-Party Dialogue](https://arxiv.org/abs/2504.14482)
**Xiang Li et.al.** · 2025-04-20


#### [ChatNekoHacker: Real-Time Fan Engagement with Conversational Agents](https://arxiv.org/abs/2504.13793)
**Takuya Sera et.al.** · 2025-04-18


#### [Collective Learning Mechanism based Optimal Transport Generative Adversarial Network for Non-parallel Voice Conversion](https://arxiv.org/abs/2504.13791)
**Sandipan Dhar et.al.** · 2025-04-18


#### [SIFT-50M: A Large-Scale Multilingual Dataset for Speech Instruction Fine-Tuning](https://arxiv.org/abs/2504.09081)
**Prabhat Pandey et.al.** · 2025-04-17


#### [GOAT-TTS: LLM-based Text-To-Speech Generation Optimized via A Dual-Branch Architecture](https://arxiv.org/abs/2504.12339)
**Yaodong Song et.al.** · 2025-04-15


#### [Dopamine Audiobook: A Training-free MLLM Agent for Emotional and Human-like Audiobook Generation](https://arxiv.org/abs/2504.11002)
**Yan Rong et.al.** · 2025-04-15


#### [Generalized Audio Deepfake Detection Using Frame-level Latent Information Entropy](https://arxiv.org/abs/2504.10819)
**Botao Zhao et.al.** · 2025-04-15


#### [Pseudo-Autoregressive Neural Codec Language Models for Efficient Zero-Shot Text-to-Speech Synthesis](https://arxiv.org/abs/2504.10352)
**Yifan Yang et.al.** · 2025-04-14


#### [AutoStyle-TTS: Retrieval-Augmented Generation based Automatic Style Matching Text-to-Speech Synthesis](https://arxiv.org/abs/2504.10309)
**Dan Luo et.al.** · 2025-04-14


#### [SafeSpeech: Robust and Universal Voice Protection Against Malicious Speech Synthesis](https://arxiv.org/abs/2504.09839)
**Zhisheng Zhang et.al.** · 2025-04-14


#### ["It's not a representation of me": Examining Accent Bias and Digital Exclusion in Synthetic AI Voice Services](https://arxiv.org/abs/2504.09346)
**Shira Michel et.al.** · 2025-04-12


#### [AMNet: An Acoustic Model Network for Enhanced Mandarin Speech Synthesis](https://arxiv.org/abs/2504.09225)
**Yubing Cao et.al.** · 2025-04-12


#### [Generalized Multilingual Text-to-Speech Generation with Language-Aware Style Adaptation](https://arxiv.org/abs/2504.08274)
**Haowei Lou et.al.** · 2025-04-11


#### [Empowering Global Voices: A Data-Efficient, Phoneme-Tone Adaptive Approach to High-Fidelity Speech Synthesis](https://arxiv.org/abs/2504.07858)
**Yizhong Geng et.al.** · 2025-04-10


#### [SlimSpeech: Lightweight and Efficient Text-to-Speech with Slim Rectified Flow](https://arxiv.org/abs/2504.07776)
**Kaidi Wang et.al.** · 2025-04-10


#### [F5R-TTS: Improving Flow-Matching based Text-to-Speech with Group Relative Policy Optimization](https://arxiv.org/abs/2504.02407)
**Xiaohui Sun et.al.** · 2025-04-09


#### [AVENet: Disentangling Features by Approximating Average Features for Voice Conversion](https://arxiv.org/abs/2504.05833)
**Wenyu Wang et.al.** · 2025-04-08


#### [P2Mark: Plug-and-play Parameter-intrinsic Watermarking for Neural Speech Generation](https://arxiv.org/abs/2504.05197)
**Yong Ren et.al.** · 2025-04-07


#### [SpeakEasy: Enhancing Text-to-Speech Interactions for Expressive Content Creation](https://arxiv.org/abs/2504.05106)
**Stephen Brade et.al.** · 2025-04-07


#### [RWKVTTS: Yet another TTS based on RWKV-7](https://arxiv.org/abs/2504.03289)
**Lin yueyu et.al.** · 2025-04-04


#### [VoiceCraft-Dub: Automated Video Dubbing with Neural Codec Language Models](https://arxiv.org/abs/2504.02386)
**Kim Sung-Bin et.al.** · 2025-04-03


#### [TeleAntiFraud-28k: An Audio-Text Slow-Thinking Dataset for Telecom Fraud Detection](https://arxiv.org/abs/2503.24115)
**Zhiming Ma et.al.** · 2025-04-02


#### [SVLA: A Unified Speech-Vision-Language Assistant with Multimodal Reasoning and Speech Generation](https://arxiv.org/abs/2503.24164)
**Ngoc Dung Huynh et.al.** · 2025-03-31


#### [SpeechDialogueFactory: Generating High-Quality Speech Dialogue Data to Accelerate Your Speech-LLM Development](https://arxiv.org/abs/2503.23848)
**Minghan Wang et.al.** · 2025-03-31


#### [DeepDubber-V1: Towards High Quality and Dialogue, Narration, Monologue Adaptive Movie Dubbing Via Multi-Modal Chain-of-Thoughts Reasoning Guidance](https://arxiv.org/abs/2503.23660)
**Junjie Zheng et.al.** · 2025-03-31


#### [Speculative End-Turn Detector for Efficient Speech Chatbot Assistant](https://arxiv.org/abs/2503.23439)
**Hyunjong Ok et.al.** · 2025-03-30


#### [SupertonicTTS: Towards Highly Scalable and Efficient Text-to-Speech System](https://arxiv.org/abs/2503.23108)
**Hyeongju Kim et.al.** · 2025-03-29


#### [Cross-Technology Generalization in Synthesized Speech Detection: Evaluating AST Models with Modern Voice Generators](https://arxiv.org/abs/2503.22503)
**Andrew Ustinov et.al.** · 2025-03-28


#### [DeepAudio-V1:Towards Multi-Modal Multi-Stage End-to-End Video to Speech and Audio Generation](https://arxiv.org/abs/2503.22265)
**Haomin Zhang et.al.** · 2025-03-28


#### [FireRedTTS-1S: An Upgraded Streamable Foundation Text-to-Speech System](https://arxiv.org/abs/2503.20499)
**Hao-Han Guo et.al.** · 2025-03-28


#### [Dual Audio-Centric Modality Coupling for Talking Head Generation](https://arxiv.org/abs/2503.22728)
**Ao Fu et.al.** · 2025-03-26


#### [Text-Driven Voice Conversion via Latent State-Space Modeling](https://arxiv.org/abs/2503.20999)
**Wen Li et.al.** · 2025-03-26


#### [Qwen2.5-Omni Technical Report](https://arxiv.org/abs/2503.20215)
**Jin Xu et.al.** · 2025-03-26


#### [InnerSelf: Designing Self-Deepfaked Voice for Emotional Well-being](https://arxiv.org/abs/2503.14257)
**Guang Dai et.al.** · 2025-03-26


#### [Measuring the Robustness of Audio Deepfake Detectors](https://arxiv.org/abs/2503.17577)
**Xiang Li et.al.** · 2025-03-21


#### [Your voice is your voice: Supporting Self-expression through Speech Generation and LLMs in Augmented and Alternative Communication](https://arxiv.org/abs/2503.17479)
**Yiwen Xu et.al.** · 2025-03-21


#### [From Faces to Voices: Learning Hierarchical Representations for High-quality Video-to-Speech](https://arxiv.org/abs/2503.16956)
**Ji-Hoon Kim et.al.** · 2025-03-21


#### [WaveFM: A High-Fidelity and Efficient Vocoder Based on Flow Matching](https://arxiv.org/abs/2503.16689)
**Tianze Luo et.al.** · 2025-03-20


#### [Shushing! Let's Imagine an Authentic Speech from the Silent Video](https://arxiv.org/abs/2503.14928)
**Jiaxin Ye et.al.** · 2025-03-19


#### [MoonCast: High-Quality Zero-Shot Podcast Generation](https://arxiv.org/abs/2503.14345)
**Zeqian Ju et.al.** · 2025-03-19


#### [Universal Speech Token Learning via Low-Bitrate Neural Codec and Pretrained Representations](https://arxiv.org/abs/2503.12115)
**Xue Jiang et.al.** · 2025-03-15


#### [MAVFlow: Preserving Paralinguistic Elements with Conditional Flow Matching for Zero-Shot AV2AV Multilingual Translation](https://arxiv.org/abs/2503.11026)
**Sungwoo Cho et.al.** · 2025-03-14


#### [Proceedings of the ISCA/ITG Workshop on Diversity in Large Speech and Language Models](https://arxiv.org/abs/2503.10298)
**Sebastian Möller et.al.** · 2025-03-14


#### [Telephone Surveys Meet Conversational AI: Evaluating a LLM-Based Telephone Survey System at Scale](https://arxiv.org/abs/2502.20140)
**Max M. Lang et.al.** · 2025-03-12


#### [An Exhaustive Evaluation of TTS- and VC-based Data Augmentation for ASR](https://arxiv.org/abs/2503.08954)
**Sewade Ogun et.al.** · 2025-03-11


#### [VocalEyes: Enhancing Environmental Perception for the Visually Impaired through Vision-Language Models and Distance-Aware Object Detection](https://arxiv.org/abs/2503.16488)
**Kunal Chavan et.al.** · 2025-03-10


#### [ProSE: Diffusion Priors for Speech Enhancement](https://arxiv.org/abs/2503.06375)
**Sonal Kumar et.al.** · 2025-03-09


#### [Clip-TTS: Contrastive Text-content and Mel-spectrogram, A High-Quality Text-to-Speech Method based on Contextual Semantic Understanding](https://arxiv.org/abs/2502.18889)
**Tianyun Liu et.al.** · 2025-03-08


#### [DiVISe: Direct Visual-Input Speech Synthesis Preserving Speaker Characteristics And Intelligibility](https://arxiv.org/abs/2503.05223)
**Yifan Liu et.al.** · 2025-03-07


#### [LLMVoX: Autoregressive Streaming Text-to-Speech Model for Any LLM](https://arxiv.org/abs/2503.04724)
**Sambal Shikhar et.al.** · 2025-03-06


#### [Scaling Rich Style-Prompted Text-to-Speech Datasets](https://arxiv.org/abs/2503.04713)
**Anuj Diwan et.al.** · 2025-03-06


#### [Good practices for evaluation of synthesized speech](https://arxiv.org/abs/2503.03250)
**Erica Cooper et.al.** · 2025-03-05


#### [InSerter: Speech Instruction Following with Unsupervised Interleaved Pre-training](https://arxiv.org/abs/2503.02769)
**Dingdong Wang et.al.** · 2025-03-04


#### [Speculative Decoding and Beyond: An In-Depth Survey of Techniques](https://arxiv.org/abs/2502.19732)
**Yunhai Hu et.al.** · 2025-03-04


#### [Direct Speech to Speech Translation: A Review](https://arxiv.org/abs/2503.04799)
**Mohammad Sarim et.al.** · 2025-03-03


#### [Spark-TTS: An Efficient LLM-Based Text-to-Speech Model with Single-Stream Decoupled Speech Tokens](https://arxiv.org/abs/2503.01710)
**Xinsheng Wang et.al.** · 2025-03-03


#### [Voice Cloning for Dysarthric Speech Synthesis: Addressing Data Scarcity in Speech-Language Pathology](https://arxiv.org/abs/2503.01266)
**Birger Moell et.al.** · 2025-03-03


#### [Language-agnostic, automated assessment of listeners' speech recall using large language models](https://arxiv.org/abs/2503.01045)
**Björn Herrmann et.al.** · 2025-03-02


#### [UniWav: Towards Unified Pre-training for Speech Representation Learning and Generation](https://arxiv.org/abs/2503.00733)
**Alexander H. Liu et.al.** · 2025-03-02


#### [ASVspoof 5: Design, Collection and Validation of Resources for Spoofing, Deepfake, and Adversarial Attack Detection Using Crowdsourced Speech](https://arxiv.org/abs/2502.08857)
**Xin Wang et.al.** · 2025-03-02


#### [PodAgent: A Comprehensive Framework for Podcast Generation](https://arxiv.org/abs/2503.00455)
**Yujia Xiao et.al.** · 2025-03-01


#### [DiffCSS: Diverse and Expressive Conversational Speech Synthesis with Diffusion Models](https://arxiv.org/abs/2502.19924)
**Weihao wu et.al.** · 2025-02-27


#### [Sparse Alignment Enhanced Latent Diffusion Transformer for Zero-Shot Speech Synthesis](https://arxiv.org/abs/2502.18924)
**Ziyue Jiang et.al.** · 2025-02-26


#### [Baichuan-Audio: A Unified Framework for End-to-End Speech Interaction](https://arxiv.org/abs/2502.17239)
**Tianpeng Li et.al.** · 2025-02-24


#### [Balancing Speech Understanding and Generation Using Continual Pre-training for Codec-based Speech LLM](https://arxiv.org/abs/2502.16897)
**Jiatong Shi et.al.** · 2025-02-24


#### [Speech to Speech Translation with Translatotron: A State of the Art Review](https://arxiv.org/abs/2502.05980)
**Jules R. Kala et.al.** · 2025-02-19


#### [AV-Flow: Transforming Text to Audio-Visual Human-like Interactions](https://arxiv.org/abs/2502.13133)
**Aggelina Chatziagapi et.al.** · 2025-02-18


#### [High-Fidelity Music Vocoder using Neural Audio Codecs](https://arxiv.org/abs/2502.12759)
**Luca A. Lanzendörfer et.al.** · 2025-02-18


#### [TechSinger: Technique Controllable Multilingual Singing Voice Synthesis via Flow Matching](https://arxiv.org/abs/2502.12572)
**Wenxiang Guo et.al.** · 2025-02-18


#### [A Survey on Bridging EEG Signals and Generative AI: From Image and Text to Beyond](https://arxiv.org/abs/2502.12048)
**Shreya Shukla et.al.** · 2025-02-18


#### [NaturalL2S: End-to-End High-quality Multispeaker Lip-to-Speech Synthesis with Differential Digital Signal Processing](https://arxiv.org/abs/2502.12002)
**Yifan Liang et.al.** · 2025-02-17


#### [FELLE: Autoregressive Speech Synthesis with Token-Wise Coarse-to-Fine Flow Matching](https://arxiv.org/abs/2502.11128)
**Hui Wang et.al.** · 2025-02-16


#### [SyncSpeech: Low-Latency and Efficient Dual-Stream Text-to-Speech based on Temporal Masked Transformer](https://arxiv.org/abs/2502.11094)
**Zhengyan Sheng et.al.** · 2025-02-16


#### [Recent Advances in Discrete Speech Tokens: A Review](https://arxiv.org/abs/2502.06490)
**Yiwei Guo et.al.** · 2025-02-16


#### [VocalCrypt: Novel Active Defense Against Deepfake Voice Based on Masking Effect](https://arxiv.org/abs/2502.10329)
**Qingyuan Fei et.al.** · 2025-02-14


#### [DiTAR: Diffusion Transformer Autoregressive Modeling for Speech Generation](https://arxiv.org/abs/2502.03930)
**Dongya Jia et.al.** · 2025-02-14


#### [TokenSynth: A Token-based Neural Synthesizer for Instrument Cloning and Text-to-Instrument](https://arxiv.org/abs/2502.08939)
**Kyungsu Kim et.al.** · 2025-02-13


#### [Ola: Pushing the Frontiers of Omni-Modal Language Model with Progressive Modality Alignment](https://arxiv.org/abs/2502.04328)
**Zuyan Liu et.al.** · 2025-02-12


#### [LoRP-TTS: Low-Rank Personalized Text-To-Speech](https://arxiv.org/abs/2502.07562)
**Łukasz Bondaruk et.al.** · 2025-02-11


#### [Advanced Zero-Shot Text-to-Speech for Background Removal and Preservation with Controllable Masked Speech Prediction](https://arxiv.org/abs/2502.07345)
**Leying Zhang et.al.** · 2025-02-11


#### [Vevo: Controllable Zero-Shot Voice Imitation with Self-Supervised Disentanglement](https://arxiv.org/abs/2502.07243)
**Xueyao Zhang et.al.** · 2025-02-11


#### [Synthetic Audio Helps for Cognitive State Tasks](https://arxiv.org/abs/2502.06922)
**Adil Soubki et.al.** · 2025-02-10


#### [Non-invasive electromyographic speech neuroprosthesis: a geometric perspective](https://arxiv.org/abs/2502.05762)
**Harshavardhana T. Gowda et.al.** · 2025-02-09


#### [BnTTS: Few-Shot Speaker Adaptation in Low-Resource Setting](https://arxiv.org/abs/2502.05729)
**Mohammad Jahid Ibna Basher et.al.** · 2025-02-09


#### [CSEval: Towards Automated, Multi-Dimensional, and Reference-Free Counterspeech Evaluation using Auto-Calibrated LLMs](https://arxiv.org/abs/2501.17581)
**Amey Hengle et.al.** · 2025-02-09


#### [Gender Bias in Instruction-Guided Speech Synthesis Models](https://arxiv.org/abs/2502.05649)
**Chun-Yi Kuan et.al.** · 2025-02-08


#### [IndexTTS: An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech System](https://arxiv.org/abs/2502.05512)
**Wei Deng et.al.** · 2025-02-08


#### [Koel-TTS: Enhancing LLM based Speech Generation with Preference Alignment and Classifier Free Guidance](https://arxiv.org/abs/2502.05236)
**Shehzeen Hussain et.al.** · 2025-02-07


#### [Llasa: Scaling Train-Time and Inference-Time Compute for Llama-based Speech Synthesis](https://arxiv.org/abs/2502.04128)
**Zhen Ye et.al.** · 2025-02-06


#### [Metis: A Foundation Speech Generation Model with Masked Generative Pre-training](https://arxiv.org/abs/2502.03128)
**Yuancheng Wang et.al.** · 2025-02-05


#### [Fine-grained Preference Optimization Improves Zero-shot Text-to-Speech](https://arxiv.org/abs/2502.02950)
**Jixun Yao et.al.** · 2025-02-05


#### [Developing multilingual speech synthesis system for Ojibwe, Mi'kmaq, and Maliseet](https://arxiv.org/abs/2502.02703)
**Shenran Wang et.al.** · 2025-02-04


#### [Streaming Speaker Change Detection and Gender Classification for Transducer-Based Multi-Talker Speech Translation](https://arxiv.org/abs/2502.02683)
**Peidong Wang et.al.** · 2025-02-04


#### [Continuous Autoregressive Modeling with Stochastic Monotonic Alignment for Speech Synthesis](https://arxiv.org/abs/2502.01084)
**Weiwei Lin et.al.** · 2025-02-03


#### [EmoTalkingGaussian: Continuous Emotion-conditioned Talking Head Synthesis](https://arxiv.org/abs/2502.00654)
**Junuk Cha et.al.** · 2025-02-02


#### [VisualSpeech: Enhance Prosody with Visual Context in TTS](https://arxiv.org/abs/2501.19258)
**Shumin Que et.al.** · 2025-01-31


#### [BreezyVoice: Adapting TTS for Taiwanese Mandarin with Enhanced Polyphone Disambiguation -- Challenges and Insights](https://arxiv.org/abs/2501.17790)
**Chan-Jan Hsu et.al.** · 2025-01-29


#### [Compact Neural TTS Voices for Accessibility](https://arxiv.org/abs/2501.17332)
**Kunal Jain et.al.** · 2025-01-28


#### [Emilia: A Large-Scale, Extensive, Multilingual, and Diverse Dataset for Speech Generation](https://arxiv.org/abs/2501.15907)
**Haorui He et.al.** · 2025-01-27


#### [Overview of the Amphion Toolkit (v0.2)](https://arxiv.org/abs/2501.15442)
**Jiaqi Li et.al.** · 2025-01-26


#### [Characteristic-Specific Partial Fine-Tuning for Efficient Emotion and Speaker Adaptation in Codec Language Text-to-Speech Models](https://arxiv.org/abs/2501.14273)
**Tianrui Wang et.al.** · 2025-01-24


#### [Generalizable Audio Deepfake Detection via Latent Space Refinement and Augmentation](https://arxiv.org/abs/2501.14240)
**Wen Huang et.al.** · 2025-01-24


#### [LoCoML: A Framework for Real-World ML Inference Pipelines](https://arxiv.org/abs/2501.14165)
**Kritin Maddireddy et.al.** · 2025-01-24


#### [Everyone-Can-Sing: Zero-Shot Singing Voice Synthesis and Conversion with Speech Reference](https://arxiv.org/abs/2501.13870)
**Shuqi Dai et.al.** · 2025-01-23


#### [Generative Data Augmentation Challenge: Zero-Shot Speech Synthesis for Personalized Speech Enhancement](https://arxiv.org/abs/2501.13372)
**Jae-Sung Bae et.al.** · 2025-01-23


#### [A Non-autoregressive Model for Joint STT and TTS](https://arxiv.org/abs/2501.09104)
**Vishal Sunder et.al.** · 2025-01-20


#### [MathReader : Text-to-Speech for Mathematical Documents](https://arxiv.org/abs/2501.07088)
**Sieun Hyeon et.al.** · 2025-01-19


#### [Speech Synthesis along Perceptual Voice Quality Dimensions](https://arxiv.org/abs/2501.08791)
**Frederik Rautenberg et.al.** · 2025-01-15


#### [Towards Lightweight and Stable Zero-shot TTS with Self-distilled Representation Disentanglement](https://arxiv.org/abs/2501.08566)
**Qianniu Chen et.al.** · 2025-01-15


#### [CodecFake-Omni: A Large-Scale Codec-based Deepfake Speech Dataset](https://arxiv.org/abs/2501.08238)
**Jiawei Du et.al.** · 2025-01-14


#### [Exploring the encoding of linguistic representations in the Fully-Connected Layer of generative CNNs for Speech](https://arxiv.org/abs/2501.07726)
**Bruno Ferenc Šegedin et.al.** · 2025-01-13


#### [The 1st SpeechWellness Challenge: Detecting Suicidal Risk Among Adolescents](https://arxiv.org/abs/2501.06474)
**Wen Wu et.al.** · 2025-01-11


#### [Retrieval-Augmented Dialogue Knowledge Aggregation for Expressive Conversational Speech Synthesis](https://arxiv.org/abs/2501.06467)
**Rui Liu et.al.** · 2025-01-11


#### [Unispeaker: A Unified Approach for Multimodality-driven Speaker Generation](https://arxiv.org/abs/2501.06394)
**Zhengyan Sheng et.al.** · 2025-01-11


#### [TTS-Transducer: End-to-End Speech Synthesis with Neural Transducer](https://arxiv.org/abs/2501.06320)
**Vladimir Bataev et.al.** · 2025-01-10


#### [MinMo: A Multimodal Large Language Model for Seamless Voice Interaction](https://arxiv.org/abs/2501.06282)
**Qian Chen et.al.** · 2025-01-10


#### [PROEMO: Prompt-Driven Text-to-Speech Synthesis Based on Emotion and Intensity Control](https://arxiv.org/abs/2501.06276)
**Shaozuo Zhang et.al.** · 2025-01-10


#### [Low-Resource Text-to-Speech Synthesis Using Noise-Augmented Training of ForwardTacotron](https://arxiv.org/abs/2501.05976)
**Kishor Kayyar Lakshminarayana et.al.** · 2025-01-10


#### [MARS6: A Small and Robust Hierarchical-Codec Text-to-Speech Model](https://arxiv.org/abs/2501.05787)
**Matthew Baas et.al.** · 2025-01-10


#### [Probing Speaker-specific Features in Speaker Representations](https://arxiv.org/abs/2501.05310)
**Aemon Yat Fei Chiu et.al.** · 2025-01-09


#### [JELLY: Joint Emotion Recognition and Context Reasoning with LLMs for Conversational Speech Synthesis](https://arxiv.org/abs/2501.04904)
**Jun-Hyeok Cha et.al.** · 2025-01-09


#### [OpenOmni: Large Language Models Pivot Zero-shot Omnimodal Alignment across Language with Real-time Self-Aware Emotional Speech Synthesis](https://arxiv.org/abs/2501.04561)
**Run Luo et.al.** · 2025-01-09


#### [Cued Speech Generation Leveraging a Pre-trained Audiovisual Text-to-Speech Model](https://arxiv.org/abs/2501.04799)
**Sanjana Sankar et.al.** · 2025-01-08


#### [FleSpeech: Flexibly Controllable Speech Generation with Various Prompts](https://arxiv.org/abs/2501.04644)
**Hanzhao Li et.al.** · 2025-01-08


#### [DrawSpeech: Expressive Speech Synthesis Using Prosodic Sketches as Control Conditions](https://arxiv.org/abs/2501.04256)
**Weidong Chen et.al.** · 2025-01-08


#### [Takeaways from Applying LLM Capabilities to Multiple Conversational Avatars in a VR Pilot Study](https://arxiv.org/abs/2501.00168)
**Mykola Maslych et.al.** · 2025-01-06


#### [FaceSpeak: Expressive and High-Quality Speech Synthesis from Human Portraits of Different Styles](https://arxiv.org/abs/2501.03181)
**Tian-Hao Zhang et.al.** · 2025-01-02


#### [RingFormer: A Neural Vocoder with Ring Attention and Convolution-Augmented Transformer](https://arxiv.org/abs/2501.01182)
**Seongho Hong et.al.** · 2025-01-02


#### [Disambiguation of Chinese Polyphones in an End-to-End Framework with Semantic Features Extracted by Pre-trained BERT](https://arxiv.org/abs/2501.01102)
**Dongyang Dai et.al.** · 2025-01-02



### 2024

#### [Stable-TTS: Stable Speaker-Adaptive Text-to-Speech Synthesis via Prosody Prompting](https://arxiv.org/abs/2412.20155)
**Wooseok Han et.al.** · 2024-12-28


#### ["I've Heard of You!": Generate Spoken Named Entity Recognition Data for Unseen Entities](https://arxiv.org/abs/2412.19102)
**Jiawei Yu et.al.** · 2024-12-26


#### [Indonesian-English Code-Switching Speech Synthesizer Utilizing Multilingual STEN-TTS and Bert LID](https://arxiv.org/abs/2412.19043)
**Ahmad Alfani Handoyo et.al.** · 2024-12-26


#### [Advancing NAM-to-Speech Conversion with Novel Methods and the MultiNAM Dataset](https://arxiv.org/abs/2412.18839)
**Neil Shah et.al.** · 2024-12-25


#### [GenPod: Constructive News Framing in AI-Generated Podcasts More Effectively Reduces Negative Emotions Than Non-Constructive Framing](https://arxiv.org/abs/2412.18300)
**Wen Ku et.al.** · 2024-12-24


#### [Interleaved Speech-Text Language Models are Simple Streaming Text to Speech Synthesizers](https://arxiv.org/abs/2412.16102)
**Yifan Yang et.al.** · 2024-12-23


#### [Why Do Speech Language Models Fail to Generate Semantically Coherent Outputs? A Modality Evolving Perspective](https://arxiv.org/abs/2412.17048)
**Hankun Wang et.al.** · 2024-12-22


#### [Incremental Disentanglement for Environment-Aware Zero-Shot Text-to-Speech Synthesis](https://arxiv.org/abs/2412.16977)
**Ye-Xin Lu et.al.** · 2024-12-22


#### [Autoregressive Speech Synthesis with Next-Distribution Prediction](https://arxiv.org/abs/2412.16846)
**Xinfa Zhu et.al.** · 2024-12-22


#### [Scale This, Not That: Investigating Key Dataset Attributes for Efficient Speech Enhancement Scaling](https://arxiv.org/abs/2412.14890)
**Leying Zhang et.al.** · 2024-12-19


#### [ProsodyFM: Unsupervised Phrasing and Intonation Control for Intelligible Speech Synthesis](https://arxiv.org/abs/2412.11795)
**Xiangheng He et.al.** · 2024-12-19


#### [Synthetic Speech Classification: IEEE Signal Processing Cup 2022 challenge](https://arxiv.org/abs/2412.13279)
**Mahieyin Rahmun et.al.** · 2024-12-17


#### [Enhancing Naturalness in LLM-Generated Utterances through Disfluency Insertion](https://arxiv.org/abs/2412.12710)
**Syed Zohaib Hassan et.al.** · 2024-12-17


#### [Phoneme-Level Feature Discrepancies: A Key to Detecting Sophisticated Speech Deepfakes](https://arxiv.org/abs/2412.12619)
**Kuiyuan Zhang et.al.** · 2024-12-17


#### [Hierarchical Control of Emotion Rendering in Speech Synthesis](https://arxiv.org/abs/2412.12498)
**Sho Inoue et.al.** · 2024-12-17


#### [Multi-modal and Multi-scale Spatial Environment Understanding for Immersive Visual Text-to-Speech](https://arxiv.org/abs/2412.11409)
**Rui Liu et.al.** · 2024-12-17


#### [Efficient Generative Modeling with Residual Vector Quantization-Based Tokens](https://arxiv.org/abs/2412.10208)
**Jaehyeon Kim et.al.** · 2024-12-16


#### [AMuSeD: An Attentive Deep Neural Network for Multimodal Sarcasm Detection Incorporating Bi-modal Data Augmentation](https://arxiv.org/abs/2412.10103)
**Xiyuan Gao et.al.** · 2024-12-13


#### [CSSinger: End-to-End Chunkwise Streaming Singing Voice Synthesis System Based on Conditional Variational Autoencoder](https://arxiv.org/abs/2412.08918)
**Jianwei Cui et.al.** · 2024-12-13


#### [EmoSpeech: A Corpus of Emotionally Rich and Contextually Detailed Speech Annotations](https://arxiv.org/abs/2412.06581)
**Weizhen Bian et.al.** · 2024-12-12


#### [Multimodal Latent Language Modeling with Next-Token Diffusion](https://arxiv.org/abs/2412.08635)
**Yutao Sun et.al.** · 2024-12-11


#### [A Unified Model For Voice and Accent Conversion In Speech and Singing using Self-Supervised Learning and Feature Extraction](https://arxiv.org/abs/2412.08312)
**Sowmya Cheripally et.al.** · 2024-12-11


#### [A Preliminary Analysis of Automatic Word and Syllable Prominence Detection in Non-Native Speech With Text-to-Speech Prosody Embeddings](https://arxiv.org/abs/2412.08283)
**Anindita Mondal et.al.** · 2024-12-11


#### [LatentSpeech: Latent Diffusion for Text-To-Speech Generation](https://arxiv.org/abs/2412.08117)
**Haowei Lou et.al.** · 2024-12-11


#### [Aligner-Guided Training Paradigm: Advancing Text-to-Speech Models with Aligner Guided Duration](https://arxiv.org/abs/2412.08112)
**Haowei Lou et.al.** · 2024-12-11


#### [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Survey](https://arxiv.org/abs/2412.06602)
**Tianxin Xie et.al.** · 2024-12-09


#### [DiffStyleTTS: Diffusion-based Hierarchical Prosody Modeling for Text-to-Speech with Diverse and Controllable Styles](https://arxiv.org/abs/2412.03388)
**Jiaxuan Liu et.al.** · 2024-12-04


#### [GLM-4-Voice: Towards Intelligent and Human-Like End-to-End Spoken Chatbot](https://arxiv.org/abs/2412.02612)
**Aohan Zeng et.al.** · 2024-12-03


#### [I2TTS: Image-indicated Immersive Text-to-speech Synthesis with Spatial Perception](https://arxiv.org/abs/2411.13314)
**Jiawei Zhang et.al.** · 2024-12-02


#### [Text Is Not All You Need: Multimodal Prompting Helps LLMs Understand Humor](https://arxiv.org/abs/2412.05315)
**Ashwin Baluja et.al.** · 2024-12-01


#### [Continual Learning in Machine Speech Chain Using Gradient Episodic Memory](https://arxiv.org/abs/2411.18320)
**Geoffrey Tyndall et.al.** · 2024-11-27


#### [SALMONN-omni: A Codec-free LLM for Full-duplex Speech Understanding and Generation](https://arxiv.org/abs/2411.18138)
**Wenyi Yu et.al.** · 2024-11-27


#### [WavChat: A Survey of Spoken Dialogue Models](https://arxiv.org/abs/2411.13577)
**Shengpeng Ji et.al.** · 2024-11-26


#### [Hard-Synth: Synthesizing Diverse Hard Samples for ASR using Zero-Shot TTS and LLM](https://arxiv.org/abs/2411.13159)
**Jiawei Yu et.al.** · 2024-11-20


#### [A Context-Based Numerical Format Prediction for a Text-To-Speech System](https://arxiv.org/abs/2412.00028)
**Yaser Darwesh et.al.** · 2024-11-19


#### [Rethinking MUSHRA: Addressing Modern Challenges in Text-to-Speech Evaluation](https://arxiv.org/abs/2411.12719)
**Praveen Srinivasa Varadhan et.al.** · 2024-11-19


#### [Leveraging Virtual Reality and AI Tutoring for Language Learning: A Case Study of a Virtual Campus Environment with OpenAI GPT Integration with Unity 3D](https://arxiv.org/abs/2411.12619)
**Adithya TG et.al.** · 2024-11-19


#### [ESTVocoder: An Excitation-Spectral-Transformed Neural Vocoder Conditioned on Mel Spectrogram](https://arxiv.org/abs/2411.11258)
**Xiao-Hang Jiang et.al.** · 2024-11-18


#### [Improving Grapheme-to-Phoneme Conversion through In-Context Knowledge Retrieval with Large Language Models](https://arxiv.org/abs/2411.07563)
**Dongrui Han et.al.** · 2024-11-12


#### [Enhancing Accessibility in Special Libraries: A Study on AI-Powered Assistive Technologies for Patrons with Disabilities](https://arxiv.org/abs/2411.06970)
**Snehasish Paul Shivali Chauhan et.al.** · 2024-11-11


#### [Debatts: Zero-Shot Debating Text-to-Speech Synthesis](https://arxiv.org/abs/2411.06540)
**Yiqiao Huang et.al.** · 2024-11-10


#### [Fish-Speech: Leveraging Large Language Models for Advanced Multilingual Text-to-Speech Synthesis](https://arxiv.org/abs/2411.01156)
**Shijia Liao et.al.** · 2024-11-09


#### [CUIfy the XR: An Open-Source Package to Embed LLM-powered Conversational Agents in XR](https://arxiv.org/abs/2411.04671)
**Kadir Burak Buldu et.al.** · 2024-11-07


#### [EmoSphere++: Emotion-Controllable Zero-Shot Text-to-Speech via Emotion-Adaptive Spherical Vector](https://arxiv.org/abs/2411.02625)
**Deok-Hyeon Cho et.al.** · 2024-11-04


#### [Speech is More Than Words: Do Speech-to-Text Translation Systems Leverage Prosody?](https://arxiv.org/abs/2410.24019)
**Ioannis Tsiamas et.al.** · 2024-10-31


#### [Lina-Speech: Gated Linear Attention is a Fast and Parameter-Efficient Learner for text-to-speech synthesis](https://arxiv.org/abs/2410.23320)
**Théodor Lemerle et.al.** · 2024-10-30


#### [Very Attentive Tacotron: Robust and Unbounded Length Generalization in Autoregressive Transformer-Based Text-to-Speech](https://arxiv.org/abs/2410.22179)
**Eric Battenberg et.al.** · 2024-10-29


#### [Fast and High-Quality Auto-Regressive Speech Synthesis via Speculative Decoding](https://arxiv.org/abs/2410.21951)
**Bohan Li et.al.** · 2024-10-29


#### [RDSinger: Reference-based Diffusion Network for Singing Voice Synthesis](https://arxiv.org/abs/2410.21641)
**Kehan Sui et.al.** · 2024-10-29


#### [Asynchronous Tool Usage for Real-Time Agents](https://arxiv.org/abs/2410.21620)
**Antonio A. Ginart et.al.** · 2024-10-28


#### [Enhancing TTS Stability in Hebrew using Discrete Semantic Units](https://arxiv.org/abs/2410.21502)
**Ella Zeldes et.al.** · 2024-10-28


#### [Mitigating Unauthorized Speech Synthesis for Voice Protection](https://arxiv.org/abs/2410.20742)
**Zhisheng Zhang et.al.** · 2024-10-28


#### [Get Large Language Models Ready to Speak: A Late-fusion Approach for Speech Generation](https://arxiv.org/abs/2410.20336)
**Maohao Shen et.al.** · 2024-10-27


#### [Making Social Platforms Accessible: Emotion-Aware Speech Generation with Integrated Text Analysis](https://arxiv.org/abs/2410.19199)
**Suparna De et.al.** · 2024-10-24


#### [STTATTS: Unified Speech-To-Text And Text-To-Speech Model](https://arxiv.org/abs/2410.18607)
**Hawau Olamide Toyin et.al.** · 2024-10-24


#### [ELAICHI: Enhancing Low-resource TTS by Addressing Infrequent and Low-frequency Character Bigrams](https://arxiv.org/abs/2410.17901)
**Srija Anand et.al.** · 2024-10-23


#### [Continuous Speech Tokenizer in Text To Speech](https://arxiv.org/abs/2410.17081)
**Yixing Li et.al.** · 2024-10-22


#### [Enhancing Low-Resource ASR through Versatile TTS: Bridging the Data Gap](https://arxiv.org/abs/2410.16726)
**Guanrou Yang et.al.** · 2024-10-22


#### [Continuous Speech Synthesis using per-token Latent Diffusion](https://arxiv.org/abs/2410.16048)
**Arnon Turetzky et.al.** · 2024-10-21


#### [A Unified Framework for Collecting Text-to-Speech Synthesis Datasets for 22 Indian Languages](https://arxiv.org/abs/2410.14197)
**Sujitha Sathiyamoorthy et.al.** · 2024-10-18


#### [Multi-Source Spatial Knowledge Understanding for Immersive Visual Text-to-Speech](https://arxiv.org/abs/2410.14101)
**Shuwei He et.al.** · 2024-10-18


#### [Enhancing Crowdsourced Audio for Text-to-Speech Models](https://arxiv.org/abs/2410.13357)
**José Giraldo et.al.** · 2024-10-17


#### [DART: Disentanglement of Accent and Speaker Representation in Multispeaker Text-to-Speech](https://arxiv.org/abs/2410.13342)
**Jan Melechovsky et.al.** · 2024-10-17


#### [DurIAN-E 2: Duration Informed Attention Network with Adaptive Variational Autoencoder and Adversarial Learning for Expressive Text-to-Speech Synthesis](https://arxiv.org/abs/2410.13288)
**Yu Gu et.al.** · 2024-10-17


#### [Failing Forward: Improving Generative Error Correction for ASR with Synthetic Data and Retrieval Augmentation](https://arxiv.org/abs/2410.13198)
**Sreyan Ghosh et.al.** · 2024-10-17


#### [ERVQ: Enhanced Residual Vector Quantization with Intra-and-Inter-Codebook Optimization for Neural Audio Codecs](https://arxiv.org/abs/2410.12359)
**Rui-Chen Zheng et.al.** · 2024-10-16


#### [F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching](https://arxiv.org/abs/2410.06885)
**Yushen Chen et.al.** · 2024-10-15


#### [IsoChronoMeter: A simple and effective isochronic translation evaluation metric](https://arxiv.org/abs/2410.11127)
**Nikolai Rozanov et.al.** · 2024-10-14


#### [DMDSpeech: Distilled Diffusion Model Surpassing The Teacher in Zero-shot Speech Synthesis via Direct Metric Optimization](https://arxiv.org/abs/2410.11097)
**Yingahao Aaron Li et.al.** · 2024-10-14


#### [Emphasis Rendering for Conversational Text-to-Speech with Multi-modal Multi-scale Context Modeling](https://arxiv.org/abs/2410.09524)
**Rui Liu et.al.** · 2024-10-12


#### [Unsupervised Data Validation Methods for Efficient Model Training](https://arxiv.org/abs/2410.07880)
**Yurii Paniv et.al.** · 2024-10-10


#### [SONAR: A Synthetic AI-Audio Detection Framework and Benchmark](https://arxiv.org/abs/2410.04324)
**Xiang Li et.al.** · 2024-10-10


#### [Efficient training strategies for natural sounding speech synthesis and speaker adaptation based on FastPitch](https://arxiv.org/abs/2410.06787)
**Teodora Răgman et.al.** · 2024-10-09


#### [Bahasa Harmony: A Comprehensive Dataset for Bahasa Text-to-Speech Synthesis with Discrete Codec Modeling of EnGen-TTS](https://arxiv.org/abs/2410.06608)
**Onkar Kishor Susladkar et.al.** · 2024-10-09


#### [Can DeepFake Speech be Reliably Detected?](https://arxiv.org/abs/2410.06572)
**Hongbin Liu et.al.** · 2024-10-09


#### [SegINR: Segment-wise Implicit Neural Representation for Sequence Alignment in Neural Text-to-Speech](https://arxiv.org/abs/2410.04690)
**Minchan Kim et.al.** · 2024-10-07


#### [HALL-E: Hierarchical Neural Codec Language Model for Minute-Long Zero-Shot Text-to-Speech Synthesis](https://arxiv.org/abs/2410.04380)
**Yuto Nishimura et.al.** · 2024-10-06


#### [Adversarial Attacks and Robust Defenses in Speaker Embedding based Zero-Shot Text-to-Speech System](https://arxiv.org/abs/2410.04017)
**Ze Li et.al.** · 2024-10-05


#### [Generative Semantic Communication for Text-to-Speech Synthesis](https://arxiv.org/abs/2410.03459)
**Jiahao Zheng et.al.** · 2024-10-04


#### [Textless Streaming Speech-to-Speech Translation using Semantic Speech Tokens](https://arxiv.org/abs/2410.03298)
**Jinzheng Zhao et.al.** · 2024-10-04


#### [Narrative Player: Reviving Data Narratives with Visuals](https://arxiv.org/abs/2410.03268)
**Zekai Shao et.al.** · 2024-10-04


#### [MultiVerse: Efficient and Expressive Zero-Shot Multi-Task Text-to-Speech](https://arxiv.org/abs/2410.03192)
**Taejun Bak et.al.** · 2024-10-04


#### [Recent Advances in Speech Language Models: A Survey](https://arxiv.org/abs/2410.03751)
**Wenqian Cui et.al.** · 2024-10-01


#### [Augmentation through Laundering Attacks for Audio Spoof Detection](https://arxiv.org/abs/2410.01108)
**Hashim Ali et.al.** · 2024-10-01


#### [Zero-Shot Text-to-Speech from Continuous Text Streams](https://arxiv.org/abs/2410.00767)
**Trung Dang et.al.** · 2024-10-01


#### [EmoKnob: Enhance Voice Cloning with Fine-Grained Emotion Control](https://arxiv.org/abs/2410.00316)
**Haozhe Chen et.al.** · 2024-10-01


#### [Word-wise intonation model for cross-language TTS systems](https://arxiv.org/abs/2409.20374)
**Tomilov A. A. et.al.** · 2024-09-30


#### [Audio-Based Linguistic Feature Extraction for Enhancing Multi-lingual and Low-Resource Text-to-Speech](https://arxiv.org/abs/2409.18622)
**Youngjae Kim et.al.** · 2024-09-27


#### [Description-based Controllable Text-to-Speech with Cross-Lingual Voice Control](https://arxiv.org/abs/2409.17452)
**Ryuichi Yamamoto et.al.** · 2024-09-26


#### [Exploring synthetic data for cross-speaker style transfer in style representation based TTS](https://arxiv.org/abs/2409.17364)
**Lucas H. Ueda et.al.** · 2024-09-25


#### [Emotional Dimension Control in Language Model-Based Text-to-Speech: Spanning a Broad Spectrum of Human Emotions](https://arxiv.org/abs/2409.16681)
**Kun Zhou et.al.** · 2024-09-25


#### [Enabling Auditory Large Language Models for Automatic Speech Quality Evaluation](https://arxiv.org/abs/2409.16644)
**Siyin Wang et.al.** · 2024-09-25


#### [FastTalker: Jointly Generating Speech and Conversational Gestures from Text](https://arxiv.org/abs/2409.16404)
**Zixin Guo et.al.** · 2024-09-24


#### [Beyond Text-to-Text: An Overview of Multimodal and Generative Artificial Intelligence for Education Using Topic Modeling](https://arxiv.org/abs/2409.16376)
**Ville Heilala et.al.** · 2024-09-24


#### [Facial Expression-Enhanced TTS: Combining Face Representation and Emotion Intensity for Adaptive Speech](https://arxiv.org/abs/2409.16203)
**Yunji Chu et.al.** · 2024-09-24


#### [NanoVoice: Efficient Speaker-Adaptive Text-to-Speech for Multiple Speakers](https://arxiv.org/abs/2409.15760)
**Nohil Park et.al.** · 2024-09-24


#### [VoiceGuider: Enhancing Out-of-Domain Performance in Parameter-Efficient Speaker-Adaptive Text-to-Speech via Autoguidance](https://arxiv.org/abs/2409.15759)
**Jiheum Yeom et.al.** · 2024-09-24


#### [StyleFusion TTS: Multimodal Style-control and Enhanced Feature Fusion for Zero-shot Text-to-speech Synthesis](https://arxiv.org/abs/2409.15741)
**Zhiyong Chen et.al.** · 2024-09-24


#### [A Comprehensive Survey with Critical Analysis for Deepfake Speech Detection](https://arxiv.org/abs/2409.15180)
**Lam Pham et.al.** · 2024-09-23


#### [LlamaPartialSpoof: An LLM-Driven Fake Speech Dataset Simulating Disinformation Generation](https://arxiv.org/abs/2409.14743)
**Hieu-Thi Luong et.al.** · 2024-09-23


#### [Zero-shot Cross-lingual Voice Transfer for TTS](https://arxiv.org/abs/2409.13910)
**Fadi Biadsy et.al.** · 2024-09-20


#### [On the Feasibility of Fully AI-automated Vishing Attacks](https://arxiv.org/abs/2409.13793)
**João Figueiredo et.al.** · 2024-09-20


#### [Enhancing Synthetic Training Data for Speech Commands: From ASR-Based Filtering to Domain Adaptation in SSL Latent Space](https://arxiv.org/abs/2409.12745)
**Sebastião Quintas et.al.** · 2024-09-19


#### [Preference Alignment Improves Language Model-Based TTS](https://arxiv.org/abs/2409.12403)
**Jinchuan Tian et.al.** · 2024-09-19


#### [The Art of Storytelling: Multi-Agent Generative AI for Dynamic Multimodal Narratives](https://arxiv.org/abs/2409.11261)
**Samee Arif et.al.** · 2024-09-19


#### [Low Frame-rate Speech Codec: a Codec Designed for Fast High-quality Speech LLM Training and Inference](https://arxiv.org/abs/2409.12117)
**Edresson Casanova et.al.** · 2024-09-18


#### [Exploring an Inter-Pausal Unit (IPU) based Approach for Indic End-to-End TTS Systems](https://arxiv.org/abs/2409.11915)
**Anusha Prakash et.al.** · 2024-09-18


#### [DPI-TTS: Directional Patch Interaction for Fast-Converging and Style Temporal Modeling in Text-to-Speech](https://arxiv.org/abs/2409.11835)
**Xin Qi et.al.** · 2024-09-18


#### [Speaking from Coarse to Fine: Improving Neural Codec Language Model via Multi-Scale Speech Coding and Generation](https://arxiv.org/abs/2409.11630)
**Haohan Guo et.al.** · 2024-09-18


#### [SpMis: An Investigation of Synthetic Spoken Misinformation Detection](https://arxiv.org/abs/2409.11308)
**Peizhuo Liu et.al.** · 2024-09-17


#### [HLTCOE JHU Submission to the Voice Privacy Challenge 2024](https://arxiv.org/abs/2409.08913)
**Henry Li Xinyuan et.al.** · 2024-09-17


#### [Emo-DPO: Controllable Emotional Speech Synthesis through Direct Preference Optimization](https://arxiv.org/abs/2409.10157)
**Xiaoxue Gao et.al.** · 2024-09-16


#### [StyleTTS-ZS: Efficient High-Quality Zero-Shot Text-to-Speech Synthesis with Distilled Time-Varying Style Diffusion](https://arxiv.org/abs/2409.10058)
**Yinghao Aaron Li et.al.** · 2024-09-16


#### [Acquiring Pronunciation Knowledge from Transcribed Speech Audio via Multi-task Learning](https://arxiv.org/abs/2409.09891)
**Siqi Sun et.al.** · 2024-09-15


#### [E1 TTS: Simple and Fast Non-Autoregressive TTS](https://arxiv.org/abs/2409.09351)
**Zhijun Liu et.al.** · 2024-09-14


#### [Improving Robustness of Diffusion-Based Zero-Shot Speech Synthesis via Stable Formant Generation](https://arxiv.org/abs/2409.09311)
**Changjin Han et.al.** · 2024-09-14


#### [SafeEar: Content Privacy-Preserving Audio Deepfake Detection](https://arxiv.org/abs/2409.09272)
**Xinfeng Li et.al.** · 2024-09-14


#### [Exploring Accessibility Trends and Challenges in Mobile App Development: A Study of Stack Overflow Questions](https://arxiv.org/abs/2409.07945)
**Amila Indika et.al.** · 2024-09-14


#### [AccentBox: Towards High-Fidelity Zero-Shot Accent Generation](https://arxiv.org/abs/2409.09098)
**Jinzuomu Zhong et.al.** · 2024-09-13


#### [Text-To-Speech Synthesis In The Wild](https://arxiv.org/abs/2409.08711)
**Jee-weon Jung et.al.** · 2024-09-13


#### [SSR-Speech: Towards Stable, Safe and Robust Zero-shot Text-based Speech Editing and Synthesis](https://arxiv.org/abs/2409.07556)
**Helin Wang et.al.** · 2024-09-11


#### [D-CAPTCHA++: A Study of Resilience of Deepfake CAPTCHA under Transferable Imperceptible Adversarial Attack](https://arxiv.org/abs/2409.07390)
**Hong-Hanh Nguyen-Le et.al.** · 2024-09-11


#### [Cross-Dialect Text-To-Speech in Pitch-Accent Language Incorporating Multi-Dialect Phoneme-Level BERT](https://arxiv.org/abs/2409.07265)
**Kazuki Yamauchi et.al.** · 2024-09-11


#### [Zero-Shot Text-to-Speech as Golden Speech Generator: A Systematic Framework and its Applicability in Automatic Pronunciation Assessment](https://arxiv.org/abs/2409.07151)
**Tien-Hong Lo et.al.** · 2024-09-11


#### [Enhancing Emotional Text-to-Speech Controllability with Natural Language Guidance through Contrastive Learning and Diffusion Models](https://arxiv.org/abs/2409.06451)
**Xin Jing et.al.** · 2024-09-10


#### [What happens to diffusion model likelihood when your model is conditional?](https://arxiv.org/abs/2409.06364)
**Mattias Cross et.al.** · 2024-09-10


#### [VoiceWukong: Benchmarking Deepfake Voice Detection](https://arxiv.org/abs/2409.06348)
**Ziwei Yan et.al.** · 2024-09-10


#### [Disentangling the Prosody and Semantic Information with Pre-trained Model for In-Context Learning based Zero-Shot Voice Conversion](https://arxiv.org/abs/2409.05004)
**Zhengyang Chen et.al.** · 2024-09-10


#### [LAST: Language Model Aware Speech Tokenization](https://arxiv.org/abs/2409.03701)
**Arnon Turetzky et.al.** · 2024-09-10


#### [AS-Speech: Adaptive Style For Speech Synthesis](https://arxiv.org/abs/2409.05730)
**Zhipeng Li et.al.** · 2024-09-09


#### [IndicVoices-R: Unlocking a Massive Multilingual Multi-speaker Speech Corpus for Scaling Indian TTS](https://arxiv.org/abs/2409.05356)
**Ashwin Sankar et.al.** · 2024-09-09


#### [FireRedTTS: A Foundation Text-To-Speech Framework for Industry-Level Generative Speech Applications](https://arxiv.org/abs/2409.03283)
**Hao-Han Guo et.al.** · 2024-09-05


#### [Training Universal Vocoders with Feature Smoothing-Based Augmentation Methods for High-Quality TTS Systems](https://arxiv.org/abs/2409.02517)
**Jeongmin Liu et.al.** · 2024-09-04


#### [VoxHakka: A Dialectally Diverse Multi-speaker Text-to-Speech System for Taiwanese Hakka](https://arxiv.org/abs/2409.01548)
**Li-Wei Chen et.al.** · 2024-09-03


#### [A multilingual training strategy for low resource Text to Speech](https://arxiv.org/abs/2409.01217)
**Asma Amalas et.al.** · 2024-09-02


#### [A Framework for Synthetic Audio Conversations Generation using Large Language Models](https://arxiv.org/abs/2409.00946)
**Kaung Myat Kyaw et.al.** · 2024-09-02


#### [SoCodec: A Semantic-Ordered Multi-Stream Speech Codec for Efficient Language Model Based Text-to-Speech Synthesis](https://arxiv.org/abs/2409.00933)
**Haohan Guo et.al.** · 2024-09-02


#### [Sample-Efficient Diffusion for Text-To-Speech Synthesis](https://arxiv.org/abs/2409.03717)
**Justin Lovelace et.al.** · 2024-09-01


#### [MaskGCT: Zero-Shot Text-to-Speech with Masked Generative Codec Transformer](https://arxiv.org/abs/2409.00750)
**Yuancheng Wang et.al.** · 2024-09-01


#### [SelectTTS: Synthesizing Anyone's Voice via Discrete Unit-Based Frame Selection](https://arxiv.org/abs/2408.17432)
**Ismail Rasim Ulgen et.al.** · 2024-08-30


#### [AASIST3: KAN-Enhanced AASIST Speech Deepfake Detection using SSL Features and Additional Regularization for the ASVspoof 2024 Challenge](https://arxiv.org/abs/2408.17352)
**Kirill Borodin et.al.** · 2024-08-30


#### [Codec Does Matter: Exploring the Semantic Shortcoming of Codec for Audio Language Model](https://arxiv.org/abs/2408.17175)
**Zhen Ye et.al.** · 2024-08-30


#### [Utilizing Speaker Profiles for Impersonation Audio Detection](https://arxiv.org/abs/2408.17009)
**Hao Gu et.al.** · 2024-08-30


#### [Enabling Beam Search for Language Model-Based Text-to-Speech Synthesis](https://arxiv.org/abs/2408.16373)
**Zehai Tu et.al.** · 2024-08-29


#### [Easy, Interpretable, Effective: openSMILE for voice deepfake detection](https://arxiv.org/abs/2408.15775)
**Octavian Pascu et.al.** · 2024-08-29


#### [Multi-modal Adversarial Training for Zero-Shot Voice Cloning](https://arxiv.org/abs/2408.15916)
**John Janiczek et.al.** · 2024-08-28


#### [VoxInstruct: Expressive Human Instruction-to-Speech Generation with Unified Multilingual Codec Language Modelling](https://arxiv.org/abs/2408.15676)
**Yixuan Zhou et.al.** · 2024-08-28


#### [VoiceTailor: Lightweight Plug-In Adapter for Diffusion-Based Personalized Text-to-Speech](https://arxiv.org/abs/2408.14739)
**Heeseung Kim et.al.** · 2024-08-28


#### [SimpleSpeech 2: Towards Simple and Efficient Text-to-Speech with Flow-based Scalar Latent Transformer Diffusion Models](https://arxiv.org/abs/2408.13893)
**Dongchao Yang et.al.** · 2024-08-28


#### [StyleSpeech: Parameter-efficient Fine Tuning for Pre-trained Controllable Text-to-Speech](https://arxiv.org/abs/2408.14713)
**Haowei Lou et.al.** · 2024-08-27


#### [DualSpeech: Enhancing Speaker-Fidelity and Text-Intelligibility Through Dual Classifier-Free Guidance](https://arxiv.org/abs/2408.14423)
**Jinhyeok Yang et.al.** · 2024-08-27


#### [Anonymization of Voices in Spaces for Civic Dialogue: Measuring Impact on Empathy, Trust, and Feeling Heard](https://arxiv.org/abs/2408.13970)
**Wonjune Kang et.al.** · 2024-08-26


#### [Positional Description for Numerical Normalization](https://arxiv.org/abs/2408.12430)
**Deepanshu Gupta et.al.** · 2024-08-22


#### [VoiceX: A Text-To-Speech Framework for Custom Voices](https://arxiv.org/abs/2408.12170)
**Silvan Mertes et.al.** · 2024-08-22


#### [EELE: Exploring Efficient and Extensible LoRA Integration in Emotional Text-to-Speech](https://arxiv.org/abs/2408.10852)
**Xin Qi et.al.** · 2024-08-20


#### [SSL-TTS: Leveraging Self-Supervised Embeddings and kNN Retrieval for Zero-Shot Multi-speaker TTS](https://arxiv.org/abs/2408.10771)
**Karl El Hajal et.al.** · 2024-08-20


#### [Adversarial training of Keyword Spotting to Minimize TTS Data Overfitting](https://arxiv.org/abs/2408.10463)
**Hyun Jin Park et.al.** · 2024-08-20


#### [PeriodWave: Multi-Period Flow Matching for High-Fidelity Waveform Generation](https://arxiv.org/abs/2408.07547)
**Sang-Hoon Lee et.al.** · 2024-08-14


#### [Style-Talker: Finetuning Audio Language Model and Style-Based Text-to-Speech Model for Fast Spoken Dialogue Generation](https://arxiv.org/abs/2408.11849)
**Yinghao Aaron Li et.al.** · 2024-08-13


#### [SaSLaW: Dialogue Speech Corpus with Audio-visual Egocentric Information Toward Environment-adaptive Dialogue Speech Synthesis](https://arxiv.org/abs/2408.06858)
**Osamu Take et.al.** · 2024-08-13


#### [PRESENT: Zero-Shot Text-to-Prosody Control](https://arxiv.org/abs/2408.06827)
**Perry Lam et.al.** · 2024-08-13


#### [FLEURS-R: A Restored Multilingual Speech Corpus for Generation Tasks](https://arxiv.org/abs/2408.06227)
**Min Ma et.al.** · 2024-08-12


#### [VQ-CTAP: Cross-Modal Fine-Grained Sequence Representation Learning for Speech Processing](https://arxiv.org/abs/2408.05758)
**Chunyu Qiang et.al.** · 2024-08-11


#### [Central Kurdish Text-to-Speech Synthesis with Novel End-to-End Transformer Training](https://arxiv.org/abs/2408.03887)
**Hawraz A. Ahmad et.al.** · 2024-08-06


#### [ALIF: Low-Cost Adversarial Audio Attacks on Black-Box Speech Platforms using Linguistic Features](https://arxiv.org/abs/2408.01808)
**Peng Cheng et.al.** · 2024-08-03


#### [Bailing-TTS: Chinese Dialectal Speech Synthesis Towards Human-like Spontaneous Representation](https://arxiv.org/abs/2408.00284)
**Xinhan Di et.al.** · 2024-08-01


#### [Speech Bandwidth Expansion Via High Fidelity Generative Adversarial Networks](https://arxiv.org/abs/2407.18571)
**Mahmoud Salhab et.al.** · 2024-07-29


#### [Zero-Shot vs. Few-Shot Multi-Speaker TTS Using Pre-trained Czech SpeechT5 Model](https://arxiv.org/abs/2407.17167)
**Jan Lehečka et.al.** · 2024-07-24


#### [Synth4Kws: Synthesized Speech for User Defined Keyword Spotting in Low Resource Environments](https://arxiv.org/abs/2407.16840)
**Pai Zhu et.al.** · 2024-07-23


#### [TTSDS -- Text-to-Speech Distribution Score](https://arxiv.org/abs/2407.12707)
**Christoph Minixhofer et.al.** · 2024-07-22


#### [Braille-to-Speech Generator: Audio Generation Based on Joint Fine-Tuning of CLIP and Fastspeech2](https://arxiv.org/abs/2407.14212)
**Chun Xu et.al.** · 2024-07-19


#### [Spontaneous Style Text-to-Speech Synthesis with Controllable Spontaneous Behaviors Based on Language Models](https://arxiv.org/abs/2407.13509)
**Weiqin Li et.al.** · 2024-07-18


#### [Laugh Now Cry Later: Controlling Time-Varying Emotional States of Flow-Matching-Based Zero-Shot Text-to-Speech](https://arxiv.org/abs/2407.12229)
**Haibin Wu et.al.** · 2024-07-17


#### [Learning High-Frequency Functions Made Easy with Sinusoidal Positional Encoding](https://arxiv.org/abs/2407.09370)
**Chuanhao Sun et.al.** · 2024-07-17


#### [A Language Modeling Approach to Diacritic-Free Hebrew TTS](https://arxiv.org/abs/2407.12206)
**Amit Roth et.al.** · 2024-07-16


#### [CATT: Character-based Arabic Tashkeel Transformer](https://arxiv.org/abs/2407.03236)
**Faris Alasmary et.al.** · 2024-07-14


#### [Autoregressive Speech Synthesis without Vector Quantization](https://arxiv.org/abs/2407.08551)
**Lingwei Meng et.al.** · 2024-07-11


#### [Source Tracing of Audio Deepfake Systems](https://arxiv.org/abs/2407.08016)
**Nicholas Klein et.al.** · 2024-07-10


#### [CosyVoice: A Scalable Multilingual Zero-shot Text-to-speech Synthesizer based on Supervised Semantic Tokens](https://arxiv.org/abs/2407.05407)
**Zhihao Du et.al.** · 2024-07-09


#### [ASRRL-TTS: Agile Speaker Representation Reinforcement Learning for Text-to-Speech Speaker Adaptation](https://arxiv.org/abs/2407.05421)
**Ruibo Fu et.al.** · 2024-07-07


#### [On the Effectiveness of Acoustic BPE in Decoder-Only TTS](https://arxiv.org/abs/2407.03892)
**Bohan Li et.al.** · 2024-07-04


#### [Robust Zero-Shot Text-to-Speech Synthesis with Reverse Inference Optimization](https://arxiv.org/abs/2407.02243)
**Yuchen Hu et.al.** · 2024-07-02


#### [TTSlow: Slow Down Text-to-Speech with Efficiency Robustness Evaluations](https://arxiv.org/abs/2407.01927)
**Xiaoxue Gao et.al.** · 2024-07-02


#### [Open-Source Conversational AI with SpeechBrain 1.0](https://arxiv.org/abs/2407.00463)
**Mirco Ravanelli et.al.** · 2024-07-02


#### [Lightweight Zero-shot Text-to-Speech with Mixture of Adapters](https://arxiv.org/abs/2407.01291)
**Kenichi Fujita et.al.** · 2024-07-01


#### [NAIST Simultaneous Speech Translation System for IWSLT 2024](https://arxiv.org/abs/2407.00826)
**Yuka Ko et.al.** · 2024-06-30


#### [An Attribute Interpolation Method in Speech Synthesis by Model Merging](https://arxiv.org/abs/2407.00766)
**Masato Murata et.al.** · 2024-06-30


#### [FLY-TTS: Fast, Lightweight and High-Quality End-to-End Text-to-Speech Synthesis](https://arxiv.org/abs/2407.00753)
**Yinlin Guo et.al.** · 2024-06-30


#### [LLM-Driven Multimodal Opinion Expression Identification](https://arxiv.org/abs/2406.18088)
**Bonian Jia et.al.** · 2024-06-29


#### [Application of ASV for Voice Identification after VC and Duration Predictor Improvement in TTS Models](https://arxiv.org/abs/2406.19243)
**Borodin Kirill Nikolayevich et.al.** · 2024-06-27


#### [DEX-TTS: Diffusion-based EXpressive Text-to-Speech with Style Modeling on Time Variability](https://arxiv.org/abs/2406.19135)
**Hyun Joon Park et.al.** · 2024-06-27


#### [A Study on Synthesizing Expressive Violin Performances: Approaches and Comparisons](https://arxiv.org/abs/2406.18089)
**Tzu-Yun Hung et.al.** · 2024-06-26


#### [E2 TTS: Embarrassingly Easy Fully Non-Autoregressive Zero-Shot TTS](https://arxiv.org/abs/2406.18009)
**Sefik Emre Eskimez et.al.** · 2024-06-26


#### [Improving Robustness of LLM-based Speech Synthesis by Learning Monotonic Alignment](https://arxiv.org/abs/2406.17957)
**Paarth Neekhara et.al.** · 2024-06-25


#### [High Fidelity Text-to-Speech Via Discrete Tokens Using Token Transducer and Group Masked Language Model](https://arxiv.org/abs/2406.17310)
**Joun Yeop Lee et.al.** · 2024-06-25


#### [Leveraging Parameter-Efficient Transfer Learning for Multi-Lingual Text-to-Speech Adaptation](https://arxiv.org/abs/2406.17257)
**Yingting Li et.al.** · 2024-06-25


#### [Towards Zero-Shot Text-To-Speech for Arabic Dialects](https://arxiv.org/abs/2406.16751)
**Khai Duy Doan et.al.** · 2024-06-25


#### [Exploring the Capability of Mamba in Speech Applications](https://arxiv.org/abs/2406.16808)
**Koichi Miyazaki et.al.** · 2024-06-24


#### [A multi-speaker multi-lingual voice cloning system based on vits2 for limmits 2024 challenge](https://arxiv.org/abs/2406.17801)
**Xiaopeng Wang et.al.** · 2024-06-22


#### [TacoLM: GaTed Attention Equipped Codec Language Model are Efficient Zero-Shot Text to Speech Synthesizers](https://arxiv.org/abs/2406.15752)
**Yakun Song et.al.** · 2024-06-22


#### [InterBiasing: Boost Unseen Word Recognition through Biasing Intermediate Predictions](https://arxiv.org/abs/2406.14890)
**Yu Nakagome et.al.** · 2024-06-21


#### [GLOBE: A High-quality English Corpus with Global Accents for Zero-shot Speaker Adaptive Text-to-Speech](https://arxiv.org/abs/2406.14875)
**Wenbin Wang et.al.** · 2024-06-21


#### [DASB - Discrete Audio and Speech Benchmark](https://arxiv.org/abs/2406.14294)
**Pooneh Mousavi et.al.** · 2024-06-21


#### [Instruction Data Generation and Unsupervised Adaptation for Speech Language Models](https://arxiv.org/abs/2406.12946)
**Vahid Noroozi et.al.** · 2024-06-18


#### [DiTTo-TTS: Efficient and Scalable Zero-Shot Text-to-Speech with Diffusion Transformer](https://arxiv.org/abs/2406.11427)
**Keon Lee et.al.** · 2024-06-17


#### [NAST: Noise Aware Speech Tokenization for Speech Language Models](https://arxiv.org/abs/2406.11037)
**Shoval Messica et.al.** · 2024-06-16


#### [Multi-Scale Accent Modeling with Disentangling for Multi-Speaker Multi-Accent TTS Synthesis](https://arxiv.org/abs/2406.10844)
**Xuehao Zhou et.al.** · 2024-06-16


#### [Phoneme Discretized Saliency Maps for Explainable Detection of AI-Generated Voice](https://arxiv.org/abs/2406.10422)
**Shubham Gupta et.al.** · 2024-06-14


#### [UniAudio 1.5: Large Language Model-driven Audio Codec is A Few-shot Audio Task Learner](https://arxiv.org/abs/2406.10056)
**Dongchao Yang et.al.** · 2024-06-14


#### [MMM: Multi-Layer Multi-Residual Multi-Stream Discrete Speech Representation from Self-supervised Learning Model](https://arxiv.org/abs/2406.09869)
**Jiatong Shi et.al.** · 2024-06-14


#### [DisfluencySpeech -- Single-Speaker Conversational Speech Dataset with Paralanguage](https://arxiv.org/abs/2406.08820)
**Kyra Wang et.al.** · 2024-06-13


#### [Generating Speakers by Prompting Listener Impressions for Pre-trained Multi-Speaker Text-to-Speech Systems](https://arxiv.org/abs/2406.08812)
**Zhengyang Chen et.al.** · 2024-06-13


#### [DubWise: Video-Guided Speech Duration Control in Multimodal LLM-based Text-to-Speech for Dubbing](https://arxiv.org/abs/2406.08802)
**Neha Sahipjohn et.al.** · 2024-06-13


#### [Audio-conditioned phonemic and prosodic annotation for building text-to-speech models from unlabeled speech data](https://arxiv.org/abs/2406.08111)
**Yuma Shirahata et.al.** · 2024-06-12


#### [VECL-TTS: Voice identity and Emotional style controllable Cross-Lingual Text-to-Speech](https://arxiv.org/abs/2406.08076)
**Ashishkumar Gudmalwar et.al.** · 2024-06-12


#### [LibriTTS-P: A Corpus with Speaking Style and Speaker Identity Prompts for Text-to-Speech and Style Captioning](https://arxiv.org/abs/2406.07969)
**Masaya Kawamura et.al.** · 2024-06-12


#### [VALL-E R: Robust and Efficient Zero-Shot Text-to-Speech Synthesis via Monotonic Alignment](https://arxiv.org/abs/2406.07855)
**Bing Han et.al.** · 2024-06-12


#### [EmoSphere-TTS: Emotional Style and Intensity Modeling via Spherical Emotion Vector for Controllable Emotional Text-to-Speech](https://arxiv.org/abs/2406.07803)
**Deok-Hyeon Cho et.al.** · 2024-06-12


#### [The Interspeech 2024 Challenge on Speech Processing Using Discrete Units](https://arxiv.org/abs/2406.07725)
**Xuankai Chang et.al.** · 2024-06-11


#### [Can We Achieve High-quality Direct Speech-to-Speech Translation without Parallel Speech Data?](https://arxiv.org/abs/2406.07289)
**Qingkai Fang et.al.** · 2024-06-11


#### [AudioMarkBench: Benchmarking Robustness of Audio Watermarking](https://arxiv.org/abs/2406.06979)
**Hongbin Liu et.al.** · 2024-06-11


#### [Controlling Emotion in Text-to-Speech with Natural Language Prompts](https://arxiv.org/abs/2406.06406)
**Thomas Bott et.al.** · 2024-06-11


#### [WenetSpeech4TTS: A 12,800-hour Mandarin TTS Corpus for Large Speech Generation Model Benchmark](https://arxiv.org/abs/2406.05763)
**Linhan Ma et.al.** · 2024-06-11


#### [Text-aware and Context-aware Expressive Audiobook Speech Synthesis](https://arxiv.org/abs/2406.05672)
**Dake Guo et.al.** · 2024-06-11


#### [Meta Learning Text-to-Speech Synthesis in over 7000 Languages](https://arxiv.org/abs/2406.06403)
**Florian Lux et.al.** · 2024-06-10


#### [MakeSinger: A Semi-Supervised Training Method for Data-Efficient Singing Voice Synthesis via Classifier-free Diffusion Guidance](https://arxiv.org/abs/2406.05965)
**Semin Kim et.al.** · 2024-06-10


#### [An Investigation of Noise Robustness for Flow-Matching-Based Zero-Shot TTS](https://arxiv.org/abs/2406.05699)
**Xiaofei Wang et.al.** · 2024-06-09


#### [Autoregressive Diffusion Transformer for Text-to-Speech Synthesis](https://arxiv.org/abs/2406.05551)
**Zhijun Liu et.al.** · 2024-06-08


#### [VALL-E 2: Neural Codec Language Models are Human Parity Zero-Shot Text to Speech Synthesizers](https://arxiv.org/abs/2406.05370)
**Sanyuan Chen et.al.** · 2024-06-08


#### [Spectral Codecs: Spectrogram-Based Audio Codecs for High Quality Speech Synthesis](https://arxiv.org/abs/2406.05298)
**Ryan Langman et.al.** · 2024-06-07


#### [XTTS: a Massively Multilingual Zero-Shot Text-to-Speech Model](https://arxiv.org/abs/2406.04904)
**Edresson Casanova et.al.** · 2024-06-07


#### [TraceableSpeech: Towards Proactively Traceable Text-to-Speech with Watermarking](https://arxiv.org/abs/2406.04840)
**Junzuo Zhou et.al.** · 2024-06-07


#### [Boosting Diffusion Model for Spectrogram Up-sampling in Text-to-speech: An Empirical Study](https://arxiv.org/abs/2406.04633)
**Chong Zhang et.al.** · 2024-06-07


#### [Harder or Different? Understanding Generalization of Audio Deepfake Detection](https://arxiv.org/abs/2406.03512)
**Nicolas M. Müller et.al.** · 2024-06-07


#### [Small-E: Small Language Model with Linear Attention for Efficient Speech Synthesis](https://arxiv.org/abs/2406.04467)
**Théodor Lemerle et.al.** · 2024-06-06


#### [Total-Duration-Aware Duration Modeling for Text-to-Speech Systems](https://arxiv.org/abs/2406.04281)
**Sefik Emre Eskimez et.al.** · 2024-06-06


#### [Retrieval Augmented Generation in Prompt-based Text-to-Speech Synthesis with Context-Aware Contrastive Language-Audio Pretraining](https://arxiv.org/abs/2406.03714)
**Jinlong Xue et.al.** · 2024-06-06


#### [Improving Audio Codec-based Zero-Shot Text-to-Speech Synthesis with Multi-Modal Context and Large Language Model](https://arxiv.org/abs/2406.03706)
**Jinlong Xue et.al.** · 2024-06-06


#### [Parallel Synthesis for Autoregressive Speech Generation](https://arxiv.org/abs/2204.11806)
**Po-chun Hsu et.al.** · 2024-06-06


#### [Style Mixture of Experts for Expressive Text-To-Speech Synthesis](https://arxiv.org/abs/2406.03637)
**Ahad Jawaid et.al.** · 2024-06-05


#### [LiveSpeech: Low-Latency Zero-shot Text-to-Speech via Autoregressive Modeling of Audio Discrete Codes](https://arxiv.org/abs/2406.02897)
**Trung Dang et.al.** · 2024-06-05


#### [SimpleSpeech: Towards Simple and Efficient Text-to-Speech with Scalar Latent Transformer Diffusion Models](https://arxiv.org/abs/2406.02328)
**Dongchao Yang et.al.** · 2024-06-05


#### [Seed-TTS: A Family of High-Quality Versatile Speech Generation Models](https://arxiv.org/abs/2406.02430)
**Philip Anastassiou et.al.** · 2024-06-04


#### [BiVocoder: A Bidirectional Neural Vocoder Integrating Feature Extraction and Waveform Generation](https://arxiv.org/abs/2406.02162)
**Hui-Peng Du et.al.** · 2024-06-04


#### [Phonetic Enhanced Language Modeling for Text-to-Speech Synthesis](https://arxiv.org/abs/2406.02009)
**Kun Zhou et.al.** · 2024-06-04


#### [ControlSpeech: Towards Simultaneous Zero-shot Speaker Cloning and Zero-shot Language Style Control With Decoupled Codec](https://arxiv.org/abs/2406.01205)
**Shengpeng Ji et.al.** · 2024-06-03


#### [Accent Conversion in Text-To-Speech Using Multi-Level VAE and Adversarial Training](https://arxiv.org/abs/2406.01018)
**Jan Melechovsky et.al.** · 2024-06-03


#### [Enhancing Zero-shot Text-to-Speech Synthesis with Human Feedback](https://arxiv.org/abs/2406.00654)
**Chen Chen et.al.** · 2024-06-02


#### [Zipper: A Multi-Tower Decoder Architecture for Fusing Modalities](https://arxiv.org/abs/2405.18669)
**Vicky Zayats et.al.** · 2024-05-31


#### [TransVIP: Speech to Speech Translation System with Voice and Isochrony Preservation](https://arxiv.org/abs/2405.17809)
**Chenyang Le et.al.** · 2024-05-28


#### [RSET: Remapping-based Sorting Method for Emotion Transfer Speech Synthesis](https://arxiv.org/abs/2405.17028)
**Haoxiang Shi et.al.** · 2024-05-27


#### [Reinforcement Learning for Fine-tuning Text-to-speech Diffusion Models](https://arxiv.org/abs/2405.14632)
**Jingyi Chen et.al.** · 2024-05-23


#### [A Near-Real-Time Processing Ego Speech Filtering Pipeline Designed for Speech Interruption During Human-Robot Interaction](https://arxiv.org/abs/2405.13477)
**Yue Li et.al.** · 2024-05-22


#### [Multi-speaker Text-to-speech Training with Speaker Anonymized Data](https://arxiv.org/abs/2405.11767)
**Wen-Chin Huang et.al.** · 2024-05-20


#### [VR-GPT: Visual Language Model for Intelligent Virtual Reality Applications](https://arxiv.org/abs/2405.11537)
**Mikhail Konenkov et.al.** · 2024-05-19


#### [Exploring speech style spaces with language models: Emotional TTS without emotion labels](https://arxiv.org/abs/2405.11413)
**Shreeram Suresh Chandra et.al.** · 2024-05-18


#### [Faces that Speak: Jointly Synthesising Talking Face and Speech from Text](https://arxiv.org/abs/2405.10272)
**Youngjoon Jang et.al.** · 2024-05-16


#### [Building a Luganda Text-to-Speech Model From Crowdsourced Data](https://arxiv.org/abs/2405.10211)
**Sulaiman Kagumire et.al.** · 2024-05-16


#### [Evaluating Text-to-Speech Synthesis from a Large Discrete Token-based Speech Language Model](https://arxiv.org/abs/2405.09768)
**Siyang Wang et.al.** · 2024-05-16


#### [Hierarchical Emotion Prediction and Control in Text-to-Speech Synthesis](https://arxiv.org/abs/2405.09171)
**Sho Inoue et.al.** · 2024-05-15


#### [PolyGlotFake: A Novel Multilingual and Multimodal DeepFake Dataset](https://arxiv.org/abs/2405.08838)
**Yang Hou et.al.** · 2024-05-14


#### [Attention-Constrained Inference for Robust Decoder-Only Text-to-Speech](https://arxiv.org/abs/2404.19723)
**Hankun Wang et.al.** · 2024-04-30


#### [MM-TTS: A Unified Framework for Multimodal, Prompt-Induced Emotional Text-to-Speech Synthesis](https://arxiv.org/abs/2404.18398)
**Xiang Li et.al.** · 2024-04-29


#### [USAT: A Universal Speaker-Adaptive Text-to-Speech Approach](https://arxiv.org/abs/2404.18094)
**Wenbin Wang et.al.** · 2024-04-28


#### [TI-ASU: Toward Robust Automatic Speech Understanding through Text-to-speech Imputation Against Missing Speech Modality](https://arxiv.org/abs/2404.17983)
**Tiantian Feng et.al.** · 2024-04-27


#### [An RFP dataset for Real, Fake, and Partially fake audio detection](https://arxiv.org/abs/2404.17721)
**Abdulazeez AlAli et.al.** · 2024-04-26


#### [StoryTTS: A Highly Expressive Text-to-Speech Dataset with Rich Textual Expressiveness Annotations](https://arxiv.org/abs/2404.14946)
**Sen Liu et.al.** · 2024-04-23


#### [Retrieval-Augmented Audio Deepfake Detection](https://arxiv.org/abs/2404.13892)
**Zuheng Kang et.al.** · 2024-04-23


#### [Llama-VITS: Enhancing TTS Synthesis with Semantic Awareness](https://arxiv.org/abs/2404.06714)
**Xincan Feng et.al.** · 2024-04-18


#### [Open vocabulary keyword spotting through transfer learning from speech synthesis](https://arxiv.org/abs/2404.03914)
**Kesavaraj V et.al.** · 2024-04-18


#### [Prior-agnostic Multi-scale Contrastive Text-Audio Pre-training for Parallelized TTS Frontend Modeling](https://arxiv.org/abs/2404.09192)
**Quanxiu Wang et.al.** · 2024-04-14


#### [PromptCodec: High-Fidelity Neural Speech Codec using Disentangled Representation Learning based Adaptive Feature-aware Prompt Encoders](https://arxiv.org/abs/2404.02702)
**Yu Pan et.al.** · 2024-04-13


#### [Voice-Assisted Real-Time Traffic Sign Recognition System Using Convolutional Neural Network](https://arxiv.org/abs/2404.07807)
**Mayura Manawadu et.al.** · 2024-04-11


#### [CoVoMix: Advancing Zero-Shot Speech Generation for Human-like Multi-talker Conversations](https://arxiv.org/abs/2404.06690)
**Leying Zhang et.al.** · 2024-04-10


#### [The X-LANCE Technical Report for Interspeech 2024 Speech Processing Using Discrete Speech Unit Challenge](https://arxiv.org/abs/2404.06079)
**Yiwei Guo et.al.** · 2024-04-10


#### [KazEmoTTS: A Dataset for Kazakh Emotional Text-to-Speech Synthesis](https://arxiv.org/abs/2404.01033)
**Adal Abilbekov et.al.** · 2024-04-09


#### [Cross-Domain Audio Deepfake Detection: Dataset and Analysis](https://arxiv.org/abs/2404.04904)
**Yuang Li et.al.** · 2024-04-07


#### [HyperTTS: Parameter Efficient Adaptation in Text to Speech using Hypernetworks](https://arxiv.org/abs/2404.04645)
**Yingting Li et.al.** · 2024-04-06


#### [RALL-E: Robust Codec Language Modeling with Chain-of-Thought Prompting for Text-to-Speech Synthesis](https://arxiv.org/abs/2404.03204)
**Detai Xin et.al.** · 2024-04-06


#### [CLaM-TTS: Improving Neural Codec Language Model for Zero-Shot Text-to-Speech](https://arxiv.org/abs/2404.02781)
**Jaehyeon Kim et.al.** · 2024-04-03


#### [Humane Speech Synthesis through Zero-Shot Emotion and Disfluency Generation](https://arxiv.org/abs/2404.01339)
**Rohan Chaudhury et.al.** · 2024-03-31


#### [CM-TTS: Enhancing Real Time Text-to-Speech Synthesis Efficiency through Weighted Samplers and Consistency Models](https://arxiv.org/abs/2404.00569)
**Xiang Li et.al.** · 2024-03-31


#### [A Review of Multi-Modal Large Language and Vision Models](https://arxiv.org/abs/2404.01322)
**Kilian Carolan et.al.** · 2024-03-28


#### [NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models](https://arxiv.org/abs/2403.03100)
**Zeqian Ju et.al.** · 2024-03-27


#### [VoiceCraft: Zero-Shot Speech Editing and Text-to-Speech in the Wild](https://arxiv.org/abs/2403.16973)
**Puyuan Peng et.al.** · 2024-03-25


#### [Isometric Neural Machine Translation using Phoneme Count Ratio Reward-based Reinforcement Learning](https://arxiv.org/abs/2403.15469)
**Shivam Ratnakant Mhaskar et.al.** · 2024-03-20


#### [UTDUSS: UTokyo-SaruLab System for Interspeech2024 Speech Processing Using Discrete Speech Unit Challenge](https://arxiv.org/abs/2403.13720)
**Wataru Nakata et.al.** · 2024-03-20


#### [Building speech corpus with diverse voice characteristics for its prompt-based representation](https://arxiv.org/abs/2403.13353)
**Aya Watanabe et.al.** · 2024-03-20


#### [Creating an African American-Sounding TTS: Guidelines, Technical Challenges,and Surprising Evaluations](https://arxiv.org/abs/2403.11209)
**Claudio Pinhanez et.al.** · 2024-03-17


#### [EM-TTS: Efficiently Trained Low-Resource Mongolian Lightweight Text-to-Speech](https://arxiv.org/abs/2403.08164)
**Ziqi Liang et.al.** · 2024-03-17


#### [Fewer-token Neural Speech Codec with Time-invariant Codes](https://arxiv.org/abs/2310.00014)
**Yong Ren et.al.** · 2024-03-11


#### [HAM-TTS: Hierarchical Acoustic Modeling for Token-Based Zero-Shot Text-to-Speech with Model and Data Scaling](https://arxiv.org/abs/2403.05989)
**Chunhui Wang et.al.** · 2024-03-09


#### [Attempt Towards Stress Transfer in Speech-to-Speech Machine Translation](https://arxiv.org/abs/2403.04178)
**Sai Akarsh et.al.** · 2024-03-07


#### [AttentionStitch: How Attention Solves the Speech Editing Problem](https://arxiv.org/abs/2403.04804)
**Antonios Alexos et.al.** · 2024-03-05


#### [Brilla AI: AI Contestant for the National Science and Maths Quiz](https://arxiv.org/abs/2403.01699)
**George Boateng et.al.** · 2024-03-04


#### [Making Flow-Matching-Based Zero-Shot Text-to-Speech Laugh as You Like](https://arxiv.org/abs/2402.07383)
**Naoyuki Kanda et.al.** · 2024-03-04


#### [Towards Accurate Lip-to-Speech Synthesis in-the-Wild](https://arxiv.org/abs/2403.01087)
**Sindhu Hegde et.al.** · 2024-03-02


#### [Extending Multilingual Speech Synthesis to 100+ Languages without Transcribed Data](https://arxiv.org/abs/2402.18932)
**Takaaki Saeki et.al.** · 2024-02-29


#### [MLAAD: The Multi-Language Audio Anti-Spoofing Dataset](https://arxiv.org/abs/2401.09512)
**Nicolas M. Müller et.al.** · 2024-02-28


#### [Cross-lingual Text-To-Speech with Flow-based Voice Conversion for Improved Pronunciation](https://arxiv.org/abs/2210.17264)
**Nikolaos Ellinas et.al.** · 2024-02-27


#### [An Automated End-to-End Open-Source Software for High-Quality Text-to-Speech Dataset Generation](https://arxiv.org/abs/2402.16380)
**Ahmet Gunduz et.al.** · 2024-02-26


#### [Efficient data selection employing Semantic Similarity-based Graph Structures for model training](https://arxiv.org/abs/2402.14888)
**Roxana Petcu et.al.** · 2024-02-22


#### [Daisy-TTS: Simulating Wider Spectrum of Emotions via Prosody Embedding Decomposition](https://arxiv.org/abs/2402.14523)
**Rendi Chevi et.al.** · 2024-02-22


#### [Amphion: An Open-Source Audio, Music and Speech Generation Toolkit](https://arxiv.org/abs/2312.09911)
**Xueyao Zhang et.al.** · 2024-02-22


#### [Data Redaction from Conditional Generative Models](https://arxiv.org/abs/2305.11351)
**Zhifeng Kong et.al.** · 2024-02-20


#### [On the Semantic Latent Space of Diffusion-Based Text-to-Speech Models](https://arxiv.org/abs/2402.12423)
**Miri Varshavsky-Hassid et.al.** · 2024-02-19


#### [Bayesian Parameter-Efficient Fine-Tuning for Overcoming Catastrophic Forgetting](https://arxiv.org/abs/2402.12220)
**Haolin Chen et.al.** · 2024-02-19


#### [Ain't Misbehavin' -- Using LLMs to Generate Expressive Robot Behavior in Conversations with the Tabletop Robot Haru](https://arxiv.org/abs/2402.11571)
**Zining Wang et.al.** · 2024-02-18


#### [Empowering Communication: Speech Technology for Indian and Western Accents through AI-powered Speech Synthesis](https://arxiv.org/abs/2401.11771)
**Vinotha R et.al.** · 2024-02-16


#### [BASE TTS: Lessons from building a billion-parameter Text-to-Speech model on 100K hours of data](https://arxiv.org/abs/2402.08093)
**Mateusz Łajszczak et.al.** · 2024-02-15


#### [MobileSpeech: A Fast and High-Fidelity Framework for Mobile Zero-Shot Text-to-Speech](https://arxiv.org/abs/2402.09378)
**Shengpeng Ji et.al.** · 2024-02-14


#### [A New Approach to Voice Authenticity](https://arxiv.org/abs/2402.06304)
**Nicolas M. Müller et.al.** · 2024-02-09


#### [Unified Speech-Text Pretraining for Spoken Dialog Modeling](https://arxiv.org/abs/2402.05706)
**Heeseung Kim et.al.** · 2024-02-08


#### [Learning Arousal-Valence Representation from Categorical Emotion Labels of Speech](https://arxiv.org/abs/2311.14816)
**Enting Zhou et.al.** · 2024-02-06


#### [Enhancing the Stability of LLM-based Speech Generation Systems through Self-Supervised Representations](https://arxiv.org/abs/2402.03407)
**Álvaro Martín-Cortinas et.al.** · 2024-02-05


#### [LAraBench: Benchmarking Arabic AI with Large Language Models](https://arxiv.org/abs/2305.14982)
**Ahmed Abdelali et.al.** · 2024-02-05


#### [Natural language guidance of high-fidelity text-to-speech with synthetic annotations](https://arxiv.org/abs/2402.01912)
**Dan Lyth et.al.** · 2024-02-02


#### [DQR-TTS: Semi-supervised Text-to-speech Synthesis with Dynamic Quantized Representation](https://arxiv.org/abs/2311.07965)
**Jianzong Wang et.al.** · 2024-02-02


#### [Frame-Wise Breath Detection with Self-Training: An Exploration of Enhancing Breath Naturalness in Text-to-Speech](https://arxiv.org/abs/2402.00288)
**Dong Yang et.al.** · 2024-02-01


#### [PAM: Prompting Audio-Language Models for Audio Quality Assessment](https://arxiv.org/abs/2402.00282)
**Soham Deshmukh et.al.** · 2024-02-01


#### [Singing Voice Data Scaling-up: An Introduction to ACE-Opencpop and KiSing-v2](https://arxiv.org/abs/2401.17619)
**Jiatong Shi et.al.** · 2024-01-31


#### [MM-TTS: Multi-modal Prompt based Style Transfer for Expressive Text-to-Speech Synthesis](https://arxiv.org/abs/2312.10687)
**Wenhao Guan et.al.** · 2024-01-31


#### [ReFlow-TTS: A Rectified Flow Model for High-fidelity Text-to-Speech](https://arxiv.org/abs/2309.17056)
**Wenhao Guan et.al.** · 2024-01-31


#### [VALL-T: Decoder-Only Generative Transducer for Robust and Decoding-Controllable Text-to-Speech](https://arxiv.org/abs/2401.14321)
**Chenpeng Du et.al.** · 2024-01-30


#### [MunTTS: A Text-to-Speech System for Mundari](https://arxiv.org/abs/2401.15579)
**Varun Gumma et.al.** · 2024-01-28


#### [Text to speech synthesis](https://arxiv.org/abs/2401.13891)
**Harini s et.al.** · 2024-01-25


#### [SpeechGPT-Gen: Scaling Chain-of-Information Speech Generation](https://arxiv.org/abs/2401.13527)
**Dong Zhang et.al.** · 2024-01-25


#### [Maximizing Data Efficiency for Cross-Lingual TTS Adaptation by Self-Supervised Representation Mixing and Embedding Initialization](https://arxiv.org/abs/2402.01692)
**Wei-Ping Huang et.al.** · 2024-01-23


#### [SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models](https://arxiv.org/abs/2308.16692)
**Xin Zhang et.al.** · 2024-01-23


#### [Benchmarking Large Multimodal Models against Common Corruptions](https://arxiv.org/abs/2401.11943)
**Jiawei Zhang et.al.** · 2024-01-22


#### [Adversarial speech for voice privacy protection from Personalized Speech generation](https://arxiv.org/abs/2401.11857)
**Shihao Chen et.al.** · 2024-01-22


#### [Latent Filling: Latent Space Data Augmentation for Zero-shot Speech Synthesis](https://arxiv.org/abs/2310.03538)
**Jae-Sung Bae et.al.** · 2024-01-22


#### [Data-driven grapheme-to-phoneme representations for a lexicon-free text-to-speech](https://arxiv.org/abs/2401.10465)
**Abhinav Garg et.al.** · 2024-01-19


#### [UniCATS: A Unified Context-Aware Text-to-Speech Framework with Contextual VQ-Diffusion and Vocoding](https://arxiv.org/abs/2306.07547)
**Chenpeng Du et.al.** · 2024-01-18


#### [VoiceFlow: Efficient Text-to-Speech with Rectified Flow Matching](https://arxiv.org/abs/2309.05027)
**Yiwei Guo et.al.** · 2024-01-16


#### [MCMChaos: Improvising Rap Music with MCMC Methods and Chaos Theory](https://arxiv.org/abs/2401.07967)
**Robert G. Kimelman et.al.** · 2024-01-15


#### [ELLA-V: Stable Neural Codec Language Modeling with Alignment-guided Sequence Reordering](https://arxiv.org/abs/2401.07333)
**Yakun Song et.al.** · 2024-01-14


#### [Multi-Task Learning for Front-End Text Processing in TTS](https://arxiv.org/abs/2401.06321)
**Wonjune Kang et.al.** · 2024-01-12


#### [End to end Hindi to English speech conversion using Bark, mBART and a finetuned XLSR Wav2Vec2](https://arxiv.org/abs/2401.06183)
**Aniket Tathe et.al.** · 2024-01-11


#### [Self-Attention and Hybrid Features for Replay and Deep-Fake Audio Detection](https://arxiv.org/abs/2401.05614)
**Lian Huang et.al.** · 2024-01-11


#### [Noise-robust zero-shot text-to-speech synthesis conditioned on self-supervised speech-representation model with adapters](https://arxiv.org/abs/2401.05111)
**Kenichi Fujita et.al.** · 2024-01-10


#### [Unified speech and gesture synthesis using flow matching](https://arxiv.org/abs/2310.05181)
**Shivam Mehta et.al.** · 2024-01-09


#### [BiSinger: Bilingual Singing Voice Synthesis](https://arxiv.org/abs/2309.14089)
**Huali Zhou et.al.** · 2024-01-09


#### [Evaluating and Personalizing User-Perceived Quality of Text-to-Speech Voices for Delivering Mindfulness Meditation with Different Physical Embodiments](https://arxiv.org/abs/2401.03581)
**Zhonghao Shi et.al.** · 2024-01-07


#### [Transfer the linguistic representations from TTS to accent conversion with non-parallel data](https://arxiv.org/abs/2401.03538)
**Xi Chen et.al.** · 2024-01-07


#### [Incremental FastPitch: Chunk-based High Quality Text to Speech](https://arxiv.org/abs/2401.01755)
**Muyang Du et.al.** · 2024-01-03


#### [Utilizing Neural Transducers for Two-Stage Text-to-Speech via Semantic Token Prediction](https://arxiv.org/abs/2401.01498)
**Minchan Kim et.al.** · 2024-01-03


#### [Normalization of Lithuanian Text Using Regular Expressions](https://arxiv.org/abs/2312.17660)
**Pijus Kasparaitis et.al.** · 2024-01-01



### 2023

#### [Boosting Large Language Model for Speech Synthesis: An Empirical Study](https://arxiv.org/abs/2401.00246)
**Hongkun Hao et.al.** · 2023-12-30


#### [AE-Flow: AutoEncoder Normalizing Flow](https://arxiv.org/abs/2312.16552)
**Jakub Mosiński et.al.** · 2023-12-27


#### [PromptTTS++: Controlling Speaker Identity in Prompt-Based Text-to-Speech Using Natural Language Descriptions](https://arxiv.org/abs/2309.08140)
**Reo Shimizu et.al.** · 2023-12-27


#### [Creating New Voices using Normalizing Flows](https://arxiv.org/abs/2312.14569)
**Piotr Bilinski et.al.** · 2023-12-22


#### [ZMM-TTS: Zero-shot Multilingual and Multispeaker Speech Synthesis Conditioned on Self-supervised Discrete Speech Representations](https://arxiv.org/abs/2312.14398)
**Cheng Gong et.al.** · 2023-12-22


#### [Crowdsourced and Automatic Speech Prominence Estimation](https://arxiv.org/abs/2310.08464)
**Max Morrison et.al.** · 2023-12-22


#### [External Knowledge Augmented Polyphone Disambiguation Using Large Language Model](https://arxiv.org/abs/2312.11920)
**Chen Li et.al.** · 2023-12-19


#### [Assisting Blind People Using Object Detection with Vocal Feedback](https://arxiv.org/abs/2401.01362)
**Heba Najm et.al.** · 2023-12-18


#### [High-Fidelity Speech Synthesis with Minimal Supervision: All Using Diffusion Models](https://arxiv.org/abs/2309.15512)
**Chunyu Qiang et.al.** · 2023-12-18


#### [Learning Speech Representation From Contrastive Token-Acoustic Pretraining](https://arxiv.org/abs/2309.00424)
**Chunyu Qiang et.al.** · 2023-12-18


#### [Minimally-Supervised Speech Synthesis with Conditional Diffusion Model and Language Model: A Comparative Study of Semantic Coding](https://arxiv.org/abs/2307.15484)
**Chunyu Qiang et.al.** · 2023-12-18


#### [A review-based study on different Text-to-Speech technologies](https://arxiv.org/abs/2312.11563)
**Md. Jalal Uddin Chowdhury et.al.** · 2023-12-17


#### [ParrotTTS: Text-to-Speech synthesis by exploiting self-supervised representations](https://arxiv.org/abs/2303.01261)
**Neil Shah et.al.** · 2023-12-17


#### [Neural Text to Articulate Talk: Deep Text to Audiovisual Speech Synthesis achieving both Auditory and Photo-realism](https://arxiv.org/abs/2312.06613)
**Georgios Milis et.al.** · 2023-12-11


#### [An Experimental Study: Assessing the Combined Framework of WavLM and BEST-RQ for Text-to-Speech Synthesis](https://arxiv.org/abs/2312.05415)
**Via Nielson et.al.** · 2023-12-08


#### [Guided Flows for Generative Modeling and Decision Making](https://arxiv.org/abs/2311.13443)
**Qinqing Zheng et.al.** · 2023-12-07


#### [Schrodinger Bridges Beat Diffusion Models on Text-to-Speech Synthesis](https://arxiv.org/abs/2312.03491)
**Zehua Chen et.al.** · 2023-12-06


#### [Rapid Speaker Adaptation in Low Resource Text to Speech Systems using Synthetic Data and Transfer learning](https://arxiv.org/abs/2312.01107)
**Raviraj Joshi et.al.** · 2023-12-02


#### [Code-Mixed Text to Speech Synthesis under Low-Resource Constraints](https://arxiv.org/abs/2312.01103)
**Raviraj Joshi et.al.** · 2023-12-02


#### [Vulnerability of Automatic Identity Recognition to Audio-Visual Deepfakes](https://arxiv.org/abs/2311.17655)
**Pavel Korshunov et.al.** · 2023-11-29


#### [HierSpeech++: Bridging the Gap between Semantic and Acoustic Representation of Speech by Hierarchical Variational Inference for Zero-shot Speech Synthesis](https://arxiv.org/abs/2311.12454)
**Sang-Hoon Lee et.al.** · 2023-11-27


#### [StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models](https://arxiv.org/abs/2306.07691)
**Yinghao Aaron Li et.al.** · 2023-11-20


#### [StyleTTS: A Style-Based Generative Model for Natural and Diverse Text-to-Speech Synthesis](https://arxiv.org/abs/2205.15439)
**Yinghao Aaron Li et.al.** · 2023-11-20


#### [Utilizing Speech Emotion Recognition and Recommender Systems for Negative Emotion Handling in Therapy Chatbots](https://arxiv.org/abs/2311.11116)
**Farideh Majidi et.al.** · 2023-11-18


#### [Data Center Audio/Video Intelligence on Device (DAVID) -- An Edge-AI Platform for Smart-Toys](https://arxiv.org/abs/2311.11030)
**Gabriel Cosache et.al.** · 2023-11-18


#### [A Study on Altering the Latent Space of Pretrained Text to Speech Models for Improved Expressiveness](https://arxiv.org/abs/2311.10804)
**Mathias Vogel et.al.** · 2023-11-17


#### [Improving fairness for spoken language understanding in atypical speech with Text-to-Speech](https://arxiv.org/abs/2311.10149)
**Helin Wang et.al.** · 2023-11-16


#### [ChatAnything: Facetime Chat with LLM-Enhanced Personas](https://arxiv.org/abs/2311.06772)
**Yilin Zhao et.al.** · 2023-11-12


#### [NewsGPT: ChatGPT Integration for Robot-Reporter](https://arxiv.org/abs/2311.06640)
**Abdelhadi Hireche et.al.** · 2023-11-11


#### [Synthetic Speaking Children -- Why We Need Them and How to Make Them](https://arxiv.org/abs/2311.06307)
**Muhammad Ali Farooq et.al.** · 2023-11-08


#### [Transduce and Speak: Neural Transducer for Text-to-Speech with Semantic Token Prediction](https://arxiv.org/abs/2311.02898)
**Minchan Kim et.al.** · 2023-11-08


#### [Improved Child Text-to-Speech Synthesis through Fastpitch-based Transfer Learning](https://arxiv.org/abs/2311.04313)
**Rishabh Jain et.al.** · 2023-11-07


#### [Character-Level Bangla Text-to-IPA Transcription Using Transformer Architecture with Sequence Alignment](https://arxiv.org/abs/2311.03792)
**Jakir Hasan et.al.** · 2023-11-07


#### [Expressive TTS Driven by Natural Language Prompts Using Few Human Annotations](https://arxiv.org/abs/2311.01260)
**Hanglei Zhang et.al.** · 2023-11-02


#### [E3 TTS: Easy End-to-End Diffusion-based Text to Speech](https://arxiv.org/abs/2311.00945)
**Yuan Gao et.al.** · 2023-11-02


#### [An Implementation of Multimodal Fusion System for Intelligent Digital Human Generation](https://arxiv.org/abs/2310.20251)
**Yingjie Zhou et.al.** · 2023-10-31


#### [CoMoSpeech: One-Step Speech and Singing Voice Synthesis via Consistency Model](https://arxiv.org/abs/2305.06908)
**Zhen Ye et.al.** · 2023-10-29


#### [Style Description based Text-to-Speech with Conditional Prosodic Layer Normalization based Diffusion GAN](https://arxiv.org/abs/2310.18169)
**Neeraj Kumar et.al.** · 2023-10-27


#### [ArTST: Arabic Text and Speech Transformer](https://arxiv.org/abs/2310.16621)
**Hawau Olamide Toyin et.al.** · 2023-10-25


#### [Generative Pre-training for Speech with Flow Matching](https://arxiv.org/abs/2310.16338)
**Alexander H. Liu et.al.** · 2023-10-25


#### [SeamlessM4T: Massively Multilingual & Multimodal Machine Translation](https://arxiv.org/abs/2308.11596)
**Seamless Communication et.al.** · 2023-10-25


#### [DPP-TTS: Diversifying prosodic features of speech via determinantal point processes](https://arxiv.org/abs/2310.14663)
**Seongho Joo et.al.** · 2023-10-23


#### [An overview of text-to-speech systems and media applications](https://arxiv.org/abs/2310.14301)
**Mohammad Reza Hasanabadi et.al.** · 2023-10-22


#### [Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale](https://arxiv.org/abs/2306.15687)
**Matthew Le et.al.** · 2023-10-19


#### [Dict-TTS: Learning to Pronounce with Prior Dictionary Knowledge for Text-to-Speech](https://arxiv.org/abs/2206.02147)
**Ziyue Jiang et.al.** · 2023-10-19


#### [Generative Adversarial Training for Text-to-Speech Synthesis Based on Raw Phonetic Input and Explicit Prosody Modelling](https://arxiv.org/abs/2310.09636)
**Tiberiu Boros et.al.** · 2023-10-14


#### [Attentive Multi-Layer Perceptron for Non-autoregressive Generation](https://arxiv.org/abs/2310.09512)
**Shuyang Jiang et.al.** · 2023-10-14


#### [Vec-Tok Speech: speech vectorization and tokenization for neural speech generation](https://arxiv.org/abs/2310.07246)
**Xinfa Zhu et.al.** · 2023-10-12


#### [PromptTTS 2: Describing and Generating Voices with Text Prompt](https://arxiv.org/abs/2309.02285)
**Yichong Leng et.al.** · 2023-10-12


#### [LauraGPT: Listen, Attend, Understand, and Regenerate Audio with GPT](https://arxiv.org/abs/2310.04673)
**Jiaming Wang et.al.** · 2023-10-11


#### [Prosody Analysis of Audiobooks](https://arxiv.org/abs/2310.06930)
**Charuta Pethe et.al.** · 2023-10-10


#### [JVNV: A Corpus of Japanese Emotional Speech with Verbal Content and Nonverbal Expressions](https://arxiv.org/abs/2310.06072)
**Detai Xin et.al.** · 2023-10-09


#### [An Efficient Membership Inference Attack for the Diffusion Model by Proximal Initialization](https://arxiv.org/abs/2305.18355)
**Fei Kong et.al.** · 2023-10-09


#### [Comparative Analysis of Transfer Learning in Deep Learning Text-to-Speech Models on a Few-Shot, Low-Resource, Customized Dataset](https://arxiv.org/abs/2310.04982)
**Ze Liu et.al.** · 2023-10-08


#### [The VoiceMOS Challenge 2023: Zero-shot Subjective Speech Quality Prediction for Multiple Domains](https://arxiv.org/abs/2310.02640)
**Erica Cooper et.al.** · 2023-10-07


#### [HiGNN-TTS: Hierarchical Prosody Modeling with Graph Neural Networks for Expressive Long-form TTS](https://arxiv.org/abs/2309.13907)
**Dake Guo et.al.** · 2023-10-07


#### [FunCodec: A Fundamental, Reproducible and Integrable Open-source Toolkit for Neural Speech Codec](https://arxiv.org/abs/2309.07405)
**Zhihao Du et.al.** · 2023-10-07


#### [ContextSpeech: Expressive and Efficient Text-to-Speech for Paragraph Reading](https://arxiv.org/abs/2307.00782)
**Yujia Xiao et.al.** · 2023-10-07


#### [Towards human-like spoken dialogue generation between AI agents from written dialogue](https://arxiv.org/abs/2310.01088)
**Kentaro Mitsui et.al.** · 2023-10-02


#### [Evaluating Speech Synthesis by Training Recognizers on Synthetic Speech](https://arxiv.org/abs/2310.00706)
**Dareen Alharthi et.al.** · 2023-10-01


#### [Diffusion-Based Mel-Spectrogram Enhancement for Personalized Speech Synthesis with Found Data](https://arxiv.org/abs/2305.10891)
**Yusheng Tian et.al.** · 2023-09-30


#### [Low-Resource Self-Supervised Learning with SSL-Enhanced TTS](https://arxiv.org/abs/2309.17020)
**Po-chun Hsu et.al.** · 2023-09-29


#### [Synthetic Speech Detection Based on Temporal Consistency and Distribution of Speaker Features](https://arxiv.org/abs/2309.16954)
**Yuxiang Zhang et.al.** · 2023-09-29


#### [Mega-TTS 2: Zero-Shot Text-to-Speech with Arbitrary Length Speech Prompts](https://arxiv.org/abs/2307.07218)
**Ziyue Jiang et.al.** · 2023-09-28


#### [Face-StyleSpeech: Improved Face-to-Voice latent mapping for Natural Zero-shot Speech Synthesis from a Face Image](https://arxiv.org/abs/2311.05844)
**Minki Kang et.al.** · 2023-09-25


#### [VoiceLDM: Text-to-Speech with Environmental Context](https://arxiv.org/abs/2309.13664)
**Yeonghyeon Lee et.al.** · 2023-09-24


#### [Coco-Nut: Corpus of Japanese Utterance and Voice Characteristics Description for Prompt-based Control](https://arxiv.org/abs/2309.13509)
**Aya Watanabe et.al.** · 2023-09-24


#### [DurIAN-E: Duration Informed Attention Network For Expressive Text-to-Speech Synthesis](https://arxiv.org/abs/2309.12792)
**Yu Gu et.al.** · 2023-09-22


#### [Improving Language Model-Based Zero-Shot Text-to-Speech Synthesis with Multi-Scale Acoustic Prompts](https://arxiv.org/abs/2309.11977)
**Shun Lei et.al.** · 2023-09-22


#### [Sparks of Large Audio Models: A Survey and Outlook](https://arxiv.org/abs/2308.12792)
**Siddique Latif et.al.** · 2023-09-22


#### [The Impact of Silence on Speech Anti-Spoofing](https://arxiv.org/abs/2309.11827)
**Yuxiang Zhang et.al.** · 2023-09-21


#### [Emotion-Aware Prosodic Phrasing for Expressive Text-to-Speech](https://arxiv.org/abs/2309.11724)
**Rui Liu et.al.** · 2023-09-21


#### [Speak While You Think: Streaming Speech Synthesis During Text Generation](https://arxiv.org/abs/2309.11210)
**Avihu Dekel et.al.** · 2023-09-20


#### [Towards Joint Modeling of Dialogue Response and Speech Synthesis based on Large Language Model](https://arxiv.org/abs/2309.11000)
**Xinyu Zhou et.al.** · 2023-09-20


#### [Exploring Speech Enhancement for Low-resource Speech Synthesis](https://arxiv.org/abs/2309.10795)
**Zhaoheng Ni et.al.** · 2023-09-19


#### [Leveraging Speech PTM, Text LLM, and Emotional TTS for Speech Emotion Recognition](https://arxiv.org/abs/2309.10294)
**Ziyang Ma et.al.** · 2023-09-19


#### [Controllable Speaking Styles Using a Large Language Model](https://arxiv.org/abs/2305.10321)
**Atli Thor Sigurgeirsson et.al.** · 2023-09-19


#### [Applying Automated Machine Translation to Educational Video Courses](https://arxiv.org/abs/2301.03141)
**Linden Wang et.al.** · 2023-09-19


#### [Augmenting text for spoken language understanding with Large Language Models](https://arxiv.org/abs/2309.09390)
**Roshan Sharma et.al.** · 2023-09-17


#### [HiFi-WaveGAN: Generative Adversarial Network with Auxiliary Spectrogram-Phase Loss for High-Fidelity Singing Voice Generation](https://arxiv.org/abs/2210.12740)
**Chunhui Wang et.al.** · 2023-09-17


#### [FastGraphTTS: An Ultrafast Syntax-Aware Speech Synthesis Framework](https://arxiv.org/abs/2309.08837)
**Jianzong Wang et.al.** · 2023-09-16


#### [Cross-lingual Knowledge Distillation via Flow-based Voice Conversion for Robust Polyglot Text-To-Speech](https://arxiv.org/abs/2309.08255)
**Dariusz Piotrowski et.al.** · 2023-09-15


#### [HM-Conformer: A Conformer-based audio deepfake detection system with hierarchical pooling and multi-level classification token aggregation methods](https://arxiv.org/abs/2309.08208)
**Hyun-seo Shin et.al.** · 2023-09-15


#### [Diversity-based core-set selection for text-to-speech with linguistic and acoustic features](https://arxiv.org/abs/2309.08127)
**Kentaro Seki et.al.** · 2023-09-15


#### [Direct Text to Speech Translation System using Acoustic Units](https://arxiv.org/abs/2309.07478)
**Victoria Mingote et.al.** · 2023-09-14


#### [DCTTS: Discrete Diffusion Model with Contrastive Learning for Text-to-speech Generation](https://arxiv.org/abs/2309.06787)
**Zhichao Wu et.al.** · 2023-09-13


#### [MuLanTTS: The Microsoft Speech Synthesis System for Blizzard Challenge 2023](https://arxiv.org/abs/2309.02743)
**Zhihang Xu et.al.** · 2023-09-12


#### [Multi-Modal Automatic Prosody Annotation with Contrastive Pretraining of SSWP](https://arxiv.org/abs/2309.05423)
**Jinzuomu Zhong et.al.** · 2023-09-11


#### [GRASS: Unified Generation Model for Speech-to-Semantic Tasks](https://arxiv.org/abs/2309.02780)
**Aobo Xia et.al.** · 2023-09-11


#### [AudioLDM 2: Learning Holistic Audio Generation with Self-supervised Pretraining](https://arxiv.org/abs/2308.05734)
**Haohe Liu et.al.** · 2023-09-09


#### [Cross-Utterance Conditioned VAE for Speech Generation](https://arxiv.org/abs/2309.04156)
**Yang Li et.al.** · 2023-09-08


#### [Large-Scale Automatic Audiobook Creation](https://arxiv.org/abs/2309.03926)
**Brendan Walsh et.al.** · 2023-09-07


#### [A Comparative Analysis of Pretrained Language Models for Text-to-Speech](https://arxiv.org/abs/2309.01576)
**Marcel Granero-Moya et.al.** · 2023-09-04


#### [Rep2wav: Noise Robust text-to-speech Using self-supervised representations](https://arxiv.org/abs/2308.14553)
**Qiushi Zhu et.al.** · 2023-09-04


#### [DiCLET-TTS: Diffusion Model based Cross-lingual Emotion Transfer for Text-to-Speech -- A Study between English and Mandarin](https://arxiv.org/abs/2309.00883)
**Tao Li et.al.** · 2023-09-02


#### [Expressive paragraph text-to-speech synthesis with multi-step variational autoencoder](https://arxiv.org/abs/2308.13365)
**Xuyuan Li et.al.** · 2023-09-02


#### [The FruitShell French synthesis system at the Blizzard 2023 Challenge](https://arxiv.org/abs/2309.00223)
**Xin Qi et.al.** · 2023-09-01


#### [The DeepZen Speech Synthesis System for Blizzard Challenge 2023](https://arxiv.org/abs/2308.15945)
**Christophe Veaux et.al.** · 2023-09-01


#### [QS-TTS: Towards Semi-Supervised Text-to-Speech Synthesis via Vector-Quantized Self-Supervised Speech Representation Learning](https://arxiv.org/abs/2309.00126)
**Haohan Guo et.al.** · 2023-08-31


#### [Towards Spontaneous Style Modeling with Semi-supervised Pre-training for Conversational Text-to-Speech Synthesis](https://arxiv.org/abs/2308.16593)
**Weiqin Li et.al.** · 2023-08-31


#### [Improving Mandarin Prosodic Structure Prediction with Multi-level Contextual Information](https://arxiv.org/abs/2308.16577)
**Jie Chen et.al.** · 2023-08-31


#### [LightGrad: Lightweight Diffusion Probabilistic Model for Text-to-Speech](https://arxiv.org/abs/2308.16569)
**Jie Chen et.al.** · 2023-08-31


#### [Multi-GradSpeech: Towards Diffusion-based Multi-Speaker Text-to-speech Using Consistent Diffusion Models](https://arxiv.org/abs/2308.10428)
**Heyang Xue et.al.** · 2023-08-31


#### [CALM: Contrastive Cross-modal Speaking Style Modeling for Expressive Text-to-Speech Synthesis](https://arxiv.org/abs/2308.16021)
**Yi Meng et.al.** · 2023-08-30


#### [a unified front-end framework for english text-to-speech synthesis](https://arxiv.org/abs/2305.10666)
**Zelin Ying et.al.** · 2023-08-29


#### [Pruning Self-Attention for Zero-Shot Multi-Speaker Text-to-Speech](https://arxiv.org/abs/2308.14909)
**Hyungchan Yoon et.al.** · 2023-08-28


#### [TextrolSpeech: A Text Style Control Speech Corpus With Codec Language Text-to-Speech Models](https://arxiv.org/abs/2308.14430)
**Shengpeng Ji et.al.** · 2023-08-28


#### [Adversarial Learning of Intermediate Acoustic Feature for End-to-End Lightweight Text-to-Speech](https://arxiv.org/abs/2204.02172)
**Hyungchan Yoon et.al.** · 2023-08-28


#### [Generalizable Zero-Shot Speaker Adaptive Speech Synthesis with Disentangled Representations](https://arxiv.org/abs/2308.13007)
**Wenbin Wang et.al.** · 2023-08-24


#### [AffectEcho: Speaker Independent and Language-Agnostic Emotion and Affect Transfer for Speech Synthesis](https://arxiv.org/abs/2308.08577)
**Hrishikesh Viswanath et.al.** · 2023-08-16


#### [SpeechX: Neural Codec Language Model as a Versatile Speech Transformer](https://arxiv.org/abs/2308.06873)
**Xiaofei Wang et.al.** · 2023-08-14


#### [Miipher: A Robust Speech Restoration Model Integrating Self-Supervised Speech and Text Representations](https://arxiv.org/abs/2303.01664)
**Yuma Koizumi et.al.** · 2023-08-14


#### [Text-to-Video: a Two-stage Framework for Zero-shot Identity-agnostic Talking-head Generation](https://arxiv.org/abs/2308.06457)
**Zhichao Wang et.al.** · 2023-08-12


#### [Data Player: Automatic Generation of Data Videos with Narration-Animation Interplay](https://arxiv.org/abs/2308.04703)
**Leixian Shen et.al.** · 2023-08-09


#### [Towards an AI to Win Ghana's National Science and Maths Quiz](https://arxiv.org/abs/2308.04333)
**George Boateng et.al.** · 2023-08-08


#### [WonderFlow: Narration-Centric Design of Animated Data Videos](https://arxiv.org/abs/2308.04040)
**Yun Wang et.al.** · 2023-08-08


#### [Let's Give a Voice to Conversational Agents in Virtual Reality](https://arxiv.org/abs/2308.02665)
**Michele Yin et.al.** · 2023-08-04


#### [Many-to-Many Spoken Language Translation via Unified Speech and Text Representation Learning with Unit-to-Unit Translation](https://arxiv.org/abs/2308.01831)
**Minsu Kim et.al.** · 2023-08-03


#### [SALTTS: Leveraging Self-Supervised Speech Representations for improved Text-to-Speech Synthesis](https://arxiv.org/abs/2308.01018)
**Ramanan Sivaguru et.al.** · 2023-08-02


#### [Ada-TTA: Towards Adaptive High-Quality Text-to-Talking Avatar Synthesis](https://arxiv.org/abs/2306.03504)
**Zhenhui Ye et.al.** · 2023-08-02


#### [Multilingual context-based pronunciation learning for Text-to-Speech](https://arxiv.org/abs/2307.16709)
**Giulia Comini et.al.** · 2023-07-31


#### [Comparing normalizing flows and diffusion models for prosody and acoustic modelling in text-to-speech](https://arxiv.org/abs/2307.16679)
**Guangyan Zhang et.al.** · 2023-07-31


#### [Improving grapheme-to-phoneme conversion by learning pronunciations from speech recordings](https://arxiv.org/abs/2307.16643)
**Manuel Sam Ribeiro et.al.** · 2023-07-31


#### [DiffProsody: Diffusion-based Latent Prosody Generation for Expressive Speech Synthesis with Prosody Conditional Adversarial Training](https://arxiv.org/abs/2307.16549)
**Hyung-Seok Oh et.al.** · 2023-07-31


#### [VITS2: Improving Quality and Efficiency of Single-Stage Text-to-Speech with Adversarial Learning and Architecture Design](https://arxiv.org/abs/2307.16430)
**Jungil Kong et.al.** · 2023-07-31


#### [Improving TTS for Shanghainese: Addressing Tone Sandhi via Word Segmentation](https://arxiv.org/abs/2307.16199)
**Yuanhao Chen et.al.** · 2023-07-30


#### [METTS: Multilingual Emotional Text-to-Speech by Cross-speaker and Cross-lingual Emotion Transfer](https://arxiv.org/abs/2307.15951)
**Xinfa Zhu et.al.** · 2023-07-29


#### [StyleS2ST: Zero-shot Style Transfer for Direct Speech-to-speech Translation](https://arxiv.org/abs/2305.17732)
**Kun Song et.al.** · 2023-07-25


#### [SC VALL-E: Style-Controllable Zero-Shot Text to Speech Synthesizer](https://arxiv.org/abs/2307.10550)
**Daegyeom Kim et.al.** · 2023-07-20


#### [SLMGAN: Exploiting Speech Language Model Representations for Unsupervised Zero-Shot Voice Conversion in GANs](https://arxiv.org/abs/2307.09435)
**Yinghao Aaron Li et.al.** · 2023-07-18


#### [Controllable Emphasis with zero data for text-to-speech](https://arxiv.org/abs/2307.07062)
**Arnaud Joly et.al.** · 2023-07-13


#### [On the Use of Self-Supervised Speech Representations in Spontaneous Speech Synthesis](https://arxiv.org/abs/2307.05132)
**Siyang Wang et.al.** · 2023-07-11


#### [Interpretable Style Transfer for Text-to-Speech with ControlVAE and Diffusion Bridge](https://arxiv.org/abs/2306.04301)
**Wenhao Guan et.al.** · 2023-07-11


#### [The NPU-MSXF Speech-to-Speech Translation System for IWSLT 2023 Speech-to-Speech Translation Task](https://arxiv.org/abs/2307.04630)
**Kun Song et.al.** · 2023-07-10


#### [Artificial Eye for the Blind](https://arxiv.org/abs/2308.00801)
**Abhinav Benagi et.al.** · 2023-07-07


#### [High-Quality Automatic Voice Over with Accurate Alignment: Supervision through Self-Supervised Discrete Speech Units](https://arxiv.org/abs/2306.17005)
**Junchen Lu et.al.** · 2023-06-29


#### [EmoSpeech: Guiding FastSpeech2 Towards Emotional Text to Speech](https://arxiv.org/abs/2307.00024)
**Daria Diatlova et.al.** · 2023-06-28


#### [UnitSpeech: Speaker-adaptive Speech Synthesis with Untranscribed Data](https://arxiv.org/abs/2306.16083)
**Heeseung Kim et.al.** · 2023-06-28


#### [Improving the quality of neural TTS using long-form content and multi-speaker multi-style modeling](https://arxiv.org/abs/2212.10075)
**Tuomo Raitio et.al.** · 2023-06-28


#### [GenerTTS: Pronunciation Disentanglement for Timbre and Style Generalization in Cross-Lingual Text-to-Speech](https://arxiv.org/abs/2306.15304)
**Yahuan Cong et.al.** · 2023-06-27


#### [DSE-TTS: Dual Speaker Embedding for Cross-Lingual Text-to-Speech](https://arxiv.org/abs/2306.14145)
**Sen Liu et.al.** · 2023-06-25


#### [InstructTTS: Modelling Expressive TTS in Discrete Latent Space with Natural Language Style Prompt](https://arxiv.org/abs/2301.13662)
**Dongchao Yang et.al.** · 2023-06-25


#### [Visual-Aware Text-to-Speech](https://arxiv.org/abs/2306.12020)
**Mohan Zhou et.al.** · 2023-06-21


#### [Expressive Machine Dubbing Through Phrase-level Cross-lingual Prosody Transfer](https://arxiv.org/abs/2306.11662)
**Jakub Swiatkowski et.al.** · 2023-06-21


#### [Low-Resource Text-to-Speech Using Specific Data and Noise Augmentation](https://arxiv.org/abs/2306.10152)
**Kishor Kayyar Lakshminarayana et.al.** · 2023-06-16


#### [CML-TTS A Multilingual Dataset for Speech Synthesis in Low-Resource Languages](https://arxiv.org/abs/2306.10097)
**Frederico S. Oliveira et.al.** · 2023-06-16


#### [Improving Code-Switching and Named Entity Recognition in ASR with Speech Editing based Data Augmentation](https://arxiv.org/abs/2306.08588)
**Zheng Liang et.al.** · 2023-06-14


#### [Towards Building Voice-based Conversational Recommender Systems: Datasets, Potential Solutions, and Prospects](https://arxiv.org/abs/2306.08219)
**Xinghua Qu et.al.** · 2023-06-14


#### [PauseSpeech: Natural Speech Synthesis via Pre-trained Language Model and Pause-based Prosody Modeling](https://arxiv.org/abs/2306.07489)
**Ji-Sang Hwang et.al.** · 2023-06-13


#### [CrossSpeech: Speaker-independent Acoustic Representation for Cross-lingual Speech Synthesis](https://arxiv.org/abs/2302.14370)
**Ji-Hoon Kim et.al.** · 2023-06-12


#### [Generating Multilingual Gender-Ambiguous Text-to-Speech Voices](https://arxiv.org/abs/2211.00375)
**Konstantinos Markopoulos et.al.** · 2023-06-11


#### [Learning Emotional Representations from Imbalanced Speech Data for Speech Emotion Recognition and Emotional Text-to-Speech](https://arxiv.org/abs/2306.05709)
**Shijun Wang et.al.** · 2023-06-09


#### [VIFS: An End-to-End Variational Inference for Foley Sound Synthesis](https://arxiv.org/abs/2306.05004)
**Junhyeok Lee et.al.** · 2023-06-08


#### [Mega-TTS: Zero-Shot Text-to-Speech at Scale with Intrinsic Inductive Bias](https://arxiv.org/abs/2306.03509)
**Ziyue Jiang et.al.** · 2023-06-06


#### [PITS: Variational Pitch Inference without Fundamental Frequency for End-to-End Pitch-controllable TTS](https://arxiv.org/abs/2302.12391)
**Junhyeok Lee et.al.** · 2023-06-06


#### [Rhythm-controllable Attention with High Robustness for Long Sentence Speech Synthesis](https://arxiv.org/abs/2306.02593)
**Dengfeng Ke et.al.** · 2023-06-05


#### [Cross-Lingual Transfer Learning for Phrase Break Prediction with Multilingual Language Model](https://arxiv.org/abs/2306.02579)
**Hoyeon Lee et.al.** · 2023-06-05


#### [Latent Optimal Paths by Gumbel Propagation for Variational Bayesian Dynamic Programming](https://arxiv.org/abs/2306.02568)
**Xinlei Niu et.al.** · 2023-06-05


#### [Towards Robust FastSpeech 2 by Modelling Residual Multimodality](https://arxiv.org/abs/2306.01442)
**Fabian Kögel et.al.** · 2023-06-02


#### [EmoMix: Emotion Mixing via Diffusion Models for Emotional Speech Synthesis](https://arxiv.org/abs/2306.00648)
**Haobin Tang et.al.** · 2023-06-01


#### [The Effects of Input Type and Pronunciation Dictionary Usage in Transfer Learning for Low-Resource Text-to-Speech](https://arxiv.org/abs/2306.00535)
**Phat Do et.al.** · 2023-06-01


#### [PromptStyle: Controllable Style Transfer for Text-to-Speech with Natural Language Descriptions](https://arxiv.org/abs/2305.19522)
**Guanghou Liu et.al.** · 2023-06-01


#### [SQuId: Measuring Speech Naturalness in Many Languages](https://arxiv.org/abs/2210.06324)
**Thibault Sellam et.al.** · 2023-06-01


#### [Text-to-Speech Pipeline for Swiss German -- A comparison](https://arxiv.org/abs/2305.19750)
**Tobias Bollinger et.al.** · 2023-05-31


#### [XPhoneBERT: A Pre-trained Multilingual Model for Phoneme Representations for Text-to-Speech](https://arxiv.org/abs/2305.19709)
**Linh The Nguyen et.al.** · 2023-05-31


#### [NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers](https://arxiv.org/abs/2304.09116)
**Kai Shen et.al.** · 2023-05-31


#### [Towards Selection of Text-to-speech Data to Augment ASR Training](https://arxiv.org/abs/2306.00998)
**Shuo Liu et.al.** · 2023-05-30


#### [Resource-Efficient Fine-Tuning Strategies for Automatic MOS Prediction in Text-to-Speech for Low-Resource Languages](https://arxiv.org/abs/2305.19396)
**Phat Do et.al.** · 2023-05-30


#### [Make-A-Voice: Unified Voice Synthesis With Discrete Representation](https://arxiv.org/abs/2305.19269)
**Rongjie Huang et.al.** · 2023-05-30


#### [STT4SG-350: A Speech Corpus for All Swiss German Dialect Regions](https://arxiv.org/abs/2305.18855)
**Michel Plüss et.al.** · 2023-05-30


#### [LibriTTS-R: A Restored Multi-Speaker Text-to-Speech Corpus](https://arxiv.org/abs/2305.18802)
**Yuma Koizumi et.al.** · 2023-05-30


#### [A Review of Deep Learning Techniques for Speech Processing](https://arxiv.org/abs/2305.00359)
**Ambuj Mehrish et.al.** · 2023-05-30


#### [ADAPTERMIX: Exploring the Efficacy of Mixture of Adapters for Low-Resource TTS Adaptation](https://arxiv.org/abs/2305.18028)
**Ambuj Mehrish et.al.** · 2023-05-29


#### [Automatic Evaluation of Turn-taking Cues in Conversational Speech Synthesis](https://arxiv.org/abs/2305.17971)
**Erik Ekstedt et.al.** · 2023-05-29


#### [OverFlow: Putting flows on top of neural transducers for better TTS](https://arxiv.org/abs/2211.06892)
**Shivam Mehta et.al.** · 2023-05-29


#### [Semi-supervised learning for continuous emotional intensity controllable speech synthesis with disentangled representations](https://arxiv.org/abs/2211.06160)
**Yoori Oh et.al.** · 2023-05-29


#### [Stochastic Pitch Prediction Improves the Diversity and Naturalness of Speech in Glow-TTS](https://arxiv.org/abs/2305.17724)
**Sewade Ogun et.al.** · 2023-05-28


#### [DSPGAN: a GAN-based universal vocoder for high-fidelity TTS by time-frequency domain supervision from DSP](https://arxiv.org/abs/2211.01087)
**Kun Song et.al.** · 2023-05-28


#### [Learning to Speak from Text: Zero-Shot Multilingual Text-to-Speech with Unsupervised Text Pretraining](https://arxiv.org/abs/2301.12596)
**Takaaki Saeki et.al.** · 2023-05-27


#### [DisfluencyFixer: A tool to enhance Language Learning through Speech To Speech Disfluency Correction](https://arxiv.org/abs/2305.16957)
**Vineet Bhat et.al.** · 2023-05-26


#### [Laughter Synthesis using Pseudo Phonetic Tokens with a Large-scale In-the-wild Laughter Corpus](https://arxiv.org/abs/2305.12442)
**Detai Xin et.al.** · 2023-05-26


#### [Betray Oneself: A Novel Audio DeepFake Detection Model via Mono-to-Stereo Conversion](https://arxiv.org/abs/2305.16353)
**Rui Liu et.al.** · 2023-05-25


#### [Multilingual Text-to-Speech Synthesis for Turkic Languages Using Transliteration](https://arxiv.org/abs/2305.15749)
**Rustem Yeshpanov et.al.** · 2023-05-25


#### [EMNS /Imz/ Corpus: An emotive single-speaker dataset for narrative storytelling in games, television and graphic novels](https://arxiv.org/abs/2305.13137)
**Kari Ali Noriy et.al.** · 2023-05-25


#### [Evaluating and reducing the distance between synthetic and real speech distributions](https://arxiv.org/abs/2211.16049)
**Christoph Minixhofer et.al.** · 2023-05-25


#### [Autovocoder: Fast Waveform Generation from a Learned Speech Representation using Differentiable Digital Signal Processing](https://arxiv.org/abs/2211.06989)
**Jacob J Webber et.al.** · 2023-05-25


#### [EfficientSpeech: An On-Device Text to Speech Model](https://arxiv.org/abs/2305.13905)
**Rowel Atienza et.al.** · 2023-05-23


#### [ZET-Speech: Zero-shot adaptive Emotion-controllable Text-to-Speech Synthesis with Diffusion and Style-based Models](https://arxiv.org/abs/2305.13831)
**Minki Kang et.al.** · 2023-05-23


#### [Better speech synthesis through scaling](https://arxiv.org/abs/2305.07243)
**James Betker et.al.** · 2023-05-23


#### [Text Generation with Speech Synthesis for ASR Data Augmentation](https://arxiv.org/abs/2305.16333)
**Zhuangqun Huang et.al.** · 2023-05-22


#### [U-DiT TTS: U-Diffusion Vision Transformer for Text-to-Speech](https://arxiv.org/abs/2305.13195)
**Xin Jing et.al.** · 2023-05-22


#### [ViT-TTS: Visual Text-to-Speech with Scalable Diffusion Transformer](https://arxiv.org/abs/2305.12708)
**Huadai Liu et.al.** · 2023-05-22


#### [VAKTA-SETU: A Speech-to-Speech Machine Translation Service in Select Indic Languages](https://arxiv.org/abs/2305.12518)
**Shivam Mhaskar et.al.** · 2023-05-21


#### [ComedicSpeech: Text To Speech For Stand-up Comedies in Low-Resource Scenarios](https://arxiv.org/abs/2305.12200)
**Yuyue Wang et.al.** · 2023-05-20


#### [MParrotTTS: Multilingual Multi-speaker Text to Speech Synthesis in Low Resource Setting](https://arxiv.org/abs/2305.11926)
**Neil Shah et.al.** · 2023-05-19


#### [UniFLG: Unified Facial Landmark Generator from Text or Speech](https://arxiv.org/abs/2302.14337)
**Kentaro Mitsui et.al.** · 2023-05-19


#### [Parameter-Efficient Learning for Text-to-Speech Accent Adaptation](https://arxiv.org/abs/2305.11320)
**Li-Jen Yang et.al.** · 2023-05-18


#### [FastFit: Towards Real-Time Iterative Neural Vocoder by Replacing U-Net Encoder With Multiple STFTs](https://arxiv.org/abs/2305.10823)
**Won Jang et.al.** · 2023-05-18


#### [CLAPSpeech: Learning Prosody from Text Context with Contrastive Language-Audio Pre-training](https://arxiv.org/abs/2305.10763)
**Zhenhui Ye et.al.** · 2023-05-18


#### [Accented Text-to-Speech Synthesis with Limited Data](https://arxiv.org/abs/2305.04816)
**Xuehao Zhou et.al.** · 2023-05-08


#### [Investigating Content-Aware Neural Text-To-Speech MOS Prediction Using Prosodic and Linguistic Features](https://arxiv.org/abs/2211.00342)
**Alexandra Vioni et.al.** · 2023-05-07


#### [M2-CTTS: End-to-End Multi-scale Multi-modal Conversational Text-to-Speech Synthesis](https://arxiv.org/abs/2305.02269)
**Jinlong Xue et.al.** · 2023-05-03


#### [Source-Filter-Based Generative Adversarial Neural Vocoder for High Fidelity Speech Synthesis](https://arxiv.org/abs/2304.13270)
**Ye-Xin Lu et.al.** · 2023-04-26


#### [Multi-Speaker Multi-Lingual VQTTS System for LIMMITS 2023 Challenge](https://arxiv.org/abs/2304.13121)
**Chenpeng Du et.al.** · 2023-04-25


#### [Zero-shot text-to-speech synthesis conditioned using self-supervised speech representation model](https://arxiv.org/abs/2304.11976)
**Kenichi Fujita et.al.** · 2023-04-24


#### [DiffVoice: Text-to-Speech with Latent Diffusion](https://arxiv.org/abs/2304.11750)
**Zhijun Liu et.al.** · 2023-04-23


#### [SAR: Self-Supervised Anti-Distortion Representation for End-To-End Speech Model](https://arxiv.org/abs/2304.11547)
**Jianzong Wang et.al.** · 2023-04-23


#### [A Virtual Simulation-Pilot Agent for Training of Air Traffic Controllers](https://arxiv.org/abs/2304.07842)
**Juan Zuluaga-Gomez et.al.** · 2023-04-16


#### [Efficiently Trained Low-Resource Mongolian Text-to-Speech System Based On FullConv-TTS](https://arxiv.org/abs/2211.01948)
**Ziqi Liang et.al.** · 2023-04-16


#### [Context-aware Coherent Speaking Style Prediction with Hierarchical Transformers for Audiobook Speech Synthesis](https://arxiv.org/abs/2304.06359)
**Shun Lei et.al.** · 2023-04-13


#### [Enhancing Speech-to-Speech Translation with Multiple TTS Targets](https://arxiv.org/abs/2304.04618)
**Jiatong Shi et.al.** · 2023-04-10


#### [ArmanTTS single-speaker Persian dataset](https://arxiv.org/abs/2304.03585)
**Mohammd Hasan Shamgholi et.al.** · 2023-04-07


#### [Learning to Dub Movies via Hierarchical Prosody Models](https://arxiv.org/abs/2212.04054)
**Gaoxiang Cong et.al.** · 2023-04-04


#### [Ensemble prosody prediction for expressive speech synthesis](https://arxiv.org/abs/2304.00714)
**Tian Huey Teh et.al.** · 2023-04-03


#### [A Survey on Audio Diffusion Models: Text To Speech Synthesis and Enhancement in Generative AI](https://arxiv.org/abs/2303.13336)
**Chenshuang Zhang et.al.** · 2023-04-02


#### [AraSpot: Arabic Spoken Command Spotting](https://arxiv.org/abs/2303.16621)
**Mahmoud Salhab et.al.** · 2023-03-29


#### [Unsupervised Pre-Training For Data-Efficient Text-to-Speech On Low Resource Languages](https://arxiv.org/abs/2303.15669)
**Seongyeon Park et.al.** · 2023-03-28


#### [Text is All You Need: Personalizing ASR Models using Controllable Speech Synthesis](https://arxiv.org/abs/2303.14885)
**Karren Yang et.al.** · 2023-03-27


#### [Wave-U-Net Discriminator: Fast and Lightweight Discriminator for Generative Adversarial Network-Based Speech Synthesis](https://arxiv.org/abs/2303.13909)
**Takuhiro Kaneko et.al.** · 2023-03-24


#### [Can Knowledge of End-to-End Text-to-Speech Models Improve Neural MIDI-to-Audio Synthesis Systems?](https://arxiv.org/abs/2211.13868)
**Xuan Shi et.al.** · 2023-03-21


#### [Code-Switching Text Generation and Injection in Mandarin-English ASR](https://arxiv.org/abs/2303.10949)
**Haibin Yu et.al.** · 2023-03-20


#### [Cross-speaker Emotion Transfer by Manipulating Speech Style Latents](https://arxiv.org/abs/2303.08329)
**Suhee Jo et.al.** · 2023-03-15


#### [Virtuoso: Massive Multilingual Speech-Text Joint Semi-Supervised Learning for Text-To-Speech](https://arxiv.org/abs/2210.15447)
**Takaaki Saeki et.al.** · 2023-03-15


#### [Controlling High-Dimensional Data With Sparse Input](https://arxiv.org/abs/2303.09446)
**Dan Andrei Iliescu et.al.** · 2023-03-14


#### [QI-TTS: Questioning Intonation Control for Emotional Speech Synthesis](https://arxiv.org/abs/2303.07682)
**Haobin Tang et.al.** · 2023-03-14


#### [Grad-StyleSpeech: Any-speaker Adaptive Text-to-Speech Synthesis with Diffusion Models](https://arxiv.org/abs/2211.09383)
**Minki Kang et.al.** · 2023-03-14


#### [DailyTalk: Spoken Dialogue Dataset for Conversational Text-to-Speech](https://arxiv.org/abs/2207.01063)
**Keon Lee et.al.** · 2023-03-13


#### [Fine-grained Emotional Control of Text-To-Speech: Learning To Rank Inter- And Intra-Class Emotion Intensities](https://arxiv.org/abs/2303.01508)
**Shijun Wang et.al.** · 2023-03-11


#### [An End-to-End Neural Network for Image-to-Audio Transformation](https://arxiv.org/abs/2303.06078)
**Liu Chen et.al.** · 2023-03-10


#### [Text-to-ECG: 12-Lead Electrocardiogram Synthesis conditioned on Clinical Text Reports](https://arxiv.org/abs/2303.09395)
**Hyunseung Chung et.al.** · 2023-03-09


#### [Improving Few-Shot Learning for Talking Face System with TTS Data Augmentation](https://arxiv.org/abs/2303.05322)
**Qi Chen et.al.** · 2023-03-09


#### [FoundationTTS: Text-to-Speech for ASR Customization with Generative Language Model](https://arxiv.org/abs/2303.02939)
**Ruiqing Xue et.al.** · 2023-03-08


#### [Do Prosody Transfer Models Transfer Prosody?](https://arxiv.org/abs/2303.04289)
**Atli Thor Sigurgeirsson et.al.** · 2023-03-07


#### [Speak Foreign Languages with Your Own Voice: Cross-Lingual Neural Codec Language Modeling](https://arxiv.org/abs/2303.03926)
**Ziqiang Zhang et.al.** · 2023-03-07


#### [Evaluating Parameter-Efficient Transfer Learning Approaches on SURE Benchmark for Speech Understanding](https://arxiv.org/abs/2303.03267)
**Yingting Li et.al.** · 2023-03-02


#### [LiteG2P: A fast, light and high accuracy model for grapheme-to-phoneme conversion](https://arxiv.org/abs/2303.01086)
**Chunfeng Wang et.al.** · 2023-03-02


#### [Leveraging Large Text Corpora for End-to-End Speech Summarization](https://arxiv.org/abs/2303.00978)
**Kohei Matsuura et.al.** · 2023-03-02


#### [DTW-SiameseNet: Dynamic Time Warped Siamese Network for Mispronunciation Detection and Correction](https://arxiv.org/abs/2303.00171)
**Raviteja Anantha et.al.** · 2023-03-01


#### [UzbekTagger: The rule-based POS tagger for Uzbek language](https://arxiv.org/abs/2301.12711)
**Maksud Sharipov et.al.** · 2023-03-01


#### [ClArTTS: An Open-Source Classical Arabic Text-to-Speech Corpus](https://arxiv.org/abs/2303.00069)
**Ajinkya Kulkarni et.al.** · 2023-02-28


#### [Automatic Heteronym Resolution Pipeline Using RAD-TTS Aligners](https://arxiv.org/abs/2302.14523)
**Jocelyn Huang et.al.** · 2023-02-28


#### [Imaginary Voice: Face-styled Diffusion Model for Text-to-Speech](https://arxiv.org/abs/2302.13700)
**Jiyoung Lee et.al.** · 2023-02-27


#### [Duration-aware pause insertion using pre-trained language model for multi-speaker text-to-speech](https://arxiv.org/abs/2302.13652)
**Dong Yang et.al.** · 2023-02-27


#### [Varianceflow: High-Quality and Controllable Text-to-Speech using Variance Information via Normalizing Flow](https://arxiv.org/abs/2302.13458)
**Yoonhyung Lee et.al.** · 2023-02-27


#### [QuickVC: Any-to-many Voice Conversion Using Inverse Short-time Fourier Transform for Faster Conversion](https://arxiv.org/abs/2302.08296)
**Houjian Guo et.al.** · 2023-02-23


#### [Period VITS: Variational Inference with Explicit Pitch Modeling for End-to-end Emotional Speech Synthesis](https://arxiv.org/abs/2210.15964)
**Yuma Shirahata et.al.** · 2023-02-22


#### [Lightweight and High-Fidelity End-to-End Text-to-Speech with Multi-Band Generation and Inverse Short-Time Fourier Transform](https://arxiv.org/abs/2210.15975)
**Masaya Kawamura et.al.** · 2023-02-21


#### [Towards Building Text-To-Speech Systems for the Next Billion Users](https://arxiv.org/abs/2211.09536)
**Gokul Karthik Kumar et.al.** · 2023-02-17


#### [EmoDiff: Intensity Controllable Emotional Text-to-Speech with Soft-Label Guidance](https://arxiv.org/abs/2211.09496)
**Yiwei Guo et.al.** · 2023-02-16


#### [Fast and small footprint Hybrid HMM-HiFiGAN based system for speech synthesis in Indian languages](https://arxiv.org/abs/2302.06227)
**Sudhanshu Srivastava et.al.** · 2023-02-13


#### [A Vector Quantized Approach for Text to Speech Synthesis on Real-World Spontaneous Speech](https://arxiv.org/abs/2302.04215)
**Li-Wei Chen et.al.** · 2023-02-08


#### [Generating Synthetic Speech from SpokenVocab for Speech Translation](https://arxiv.org/abs/2210.08174)
**Jinming Zhao et.al.** · 2023-02-08


#### [Speak, Read and Prompt: High-Fidelity Text-to-Speech with Minimal Supervision](https://arxiv.org/abs/2302.03540)
**Eugene Kharitonov et.al.** · 2023-02-07


#### [Time out of Mind: Generating Rate of Speech conditioned on emotion and speaker](https://arxiv.org/abs/2301.12331)
**Navjot Kaur et.al.** · 2023-01-31


#### [The PartialSpoof Database and Countermeasures for the Detection of Short Fake Speech Segments Embedded in an Utterance](https://arxiv.org/abs/2204.05177)
**Lin Zhang et.al.** · 2023-01-30


#### [On granularity of prosodic representations in expressive text-to-speech](https://arxiv.org/abs/2301.11446)
**Mikolaj Babianski et.al.** · 2023-01-26


#### [Unsupervised Data Selection for TTS: Using Arabic Broadcast News as a Case Study](https://arxiv.org/abs/2301.09099)
**Massa Baali et.al.** · 2023-01-26


#### [Phoneme-Level BERT for Enhanced Prosody of Text-to-Speech with Grapheme Predictions](https://arxiv.org/abs/2301.08810)
**Yinghao Aaron Li et.al.** · 2023-01-20


#### [Modelling low-resource accents without accent-specific TTS frontend](https://arxiv.org/abs/2301.04606)
**Georgi Tinchev et.al.** · 2023-01-11


#### [UnifySpeech: A Unified Framework for Zero-shot Text-to-Speech and Voice Conversion](https://arxiv.org/abs/2301.03801)
**Haogeng Liu et.al.** · 2023-01-10


#### [Generative Emotional AI for Speech Emotion Recognition: The Case for Synthetic Emotional Speech Augmentation](https://arxiv.org/abs/2301.03751)
**Abdullah Shahid et.al.** · 2023-01-10


#### [Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers](https://arxiv.org/abs/2301.02111)
**Chengyi Wang et.al.** · 2023-01-05


#### [Low-Resource Mongolian Speech Synthesis Based on Automatic Prosody Annotation](https://arxiv.org/abs/2211.09365)
**Xin Yuan et.al.** · 2023-01-04


#### [Dreamento: an open-source dream engineering toolbox for sleep EEG wearables](https://arxiv.org/abs/2207.03977)
**Mahdad Jafarzadeh Esfahani et.al.** · 2023-01-02



### 2022

#### [ResGrad: Residual Denoising Diffusion Probabilistic Models for Text to Speech](https://arxiv.org/abs/2212.14518)
**Zehua Chen et.al.** · 2022-12-30


#### [StyleTTS-VC: One-Shot Voice Conversion by Knowledge Transfer from Style-Based TTS Models](https://arxiv.org/abs/2212.14227)
**Yinghao Aaron Li et.al.** · 2022-12-29


#### [Speech Synthesis with Mixed Emotions](https://arxiv.org/abs/2208.05890)
**Kun Zhou et.al.** · 2022-12-28


#### [HMM-based data augmentation for E2E systems for building conversational speech synthesis systems](https://arxiv.org/abs/2212.11982)
**Ishika Gupta et.al.** · 2022-12-22


#### [ReVISE: Self-Supervised Speech Resynthesis with Visual Input for Universal and Generalized Speech Enhancement](https://arxiv.org/abs/2212.11377)
**Wei-Ning Hsu et.al.** · 2022-12-21


#### [TTS-Guided Training for Accent Conversion Without Parallel Data](https://arxiv.org/abs/2212.10204)
**Yi Zhou et.al.** · 2022-12-20


#### [Speech Aware Dialog System Technology Challenge (DSTC11)](https://arxiv.org/abs/2212.08704)
**Hagen Soltau et.al.** · 2022-12-16


#### [Text-to-speech synthesis based on latent variable conversion using diffusion probabilistic model and variational autoencoder](https://arxiv.org/abs/2212.08329)
**Yusuke Yasuda et.al.** · 2022-12-16


#### [Investigation of Japanese PnG BERT language model in text-to-speech synthesis for pitch accent language](https://arxiv.org/abs/2212.08321)
**Yusuke Yasuda et.al.** · 2022-12-16


#### [RWEN-TTS: Relation-aware Word Encoding Network for Natural Text-to-Speech Synthesis](https://arxiv.org/abs/2212.07939)
**Shinhyeok Oh et.al.** · 2022-12-15


#### [Probing Deep Speaker Embeddings for Speaker-related Tasks](https://arxiv.org/abs/2212.07068)
**Zifeng Zhao et.al.** · 2022-12-14


#### [Anti-Spoofing Using Transfer Learning with Variational Information Bottleneck](https://arxiv.org/abs/2204.01387)
**Youngsik Eom et.al.** · 2022-12-14


#### [A Novel Chinese Dialect TTS Frontend with Non-Autoregressive Neural Machine Translation](https://arxiv.org/abs/2206.04922)
**Junhui Zhang et.al.** · 2022-12-12


#### [BASPRO: a balanced script producer for speech corpus collection based on the genetic algorithm](https://arxiv.org/abs/2301.04120)
**Yu-Wen Chen et.al.** · 2022-12-11


#### [MnTTS2: An Open-Source Multi-Speaker Mongolian Text-to-Speech Synthesis Dataset](https://arxiv.org/abs/2301.00657)
**Kailin Liang et.al.** · 2022-12-11


#### [Study of Indian English Pronunciation Variabilities relative to Received Pronunciation](https://arxiv.org/abs/2204.06502)
**Priyanshi Pal et.al.** · 2022-12-09


#### [SpeechLMScore: Evaluating speech generation using speech language model](https://arxiv.org/abs/2212.04559)
**Soumi Maiti et.al.** · 2022-12-08


#### [Low-Resource End-to-end Sanskrit TTS using Tacotron2, WaveGlow and Transfer Learning](https://arxiv.org/abs/2212.03558)
**Ankur Debnath et.al.** · 2022-12-07


#### [Analysis and Utilization of Entrainment on Acoustic and Emotion Features in User-agent Dialogue](https://arxiv.org/abs/2212.03398)
**Daxin Tan et.al.** · 2022-12-07


#### [UniSyn: An End-to-End Unified Model for Text-to-Speech and Singing Voice Synthesis](https://arxiv.org/abs/2212.01546)
**Yi Lei et.al.** · 2022-12-06


#### [Efficient Incremental Text-to-Speech on GPUs](https://arxiv.org/abs/2211.13939)
**Muyang Du et.al.** · 2022-12-05


#### [ERNIE-SAT: Speech and Text Joint Pretraining for Cross-Lingual Multi-Speaker Text-to-Speech](https://arxiv.org/abs/2211.03545)
**Xiaoran Fan et.al.** · 2022-12-04


#### [SNAC: Speaker-normalized affine coupling layer in flow-based architecture for zero-shot multi-speaker text-to-speech](https://arxiv.org/abs/2211.16866)
**Byoung Jin Choi et.al.** · 2022-11-30


#### [Controllable speech synthesis by learning discrete phoneme-level prosodic representations](https://arxiv.org/abs/2211.16307)
**Nikolaos Ellinas et.al.** · 2022-11-29


#### [Contextual Expressive Text-to-Speech](https://arxiv.org/abs/2211.14548)
**Jianhong Tu et.al.** · 2022-11-26


#### [IMaSC -- ICFOSS Malayalam Speech Corpus](https://arxiv.org/abs/2211.12796)
**Deepa P Gopinath et.al.** · 2022-11-23


#### [PromptTTS: Controllable Text-to-Speech with Text Descriptions](https://arxiv.org/abs/2211.12171)
**Zhifang Guo et.al.** · 2022-11-22


#### [Multi-Speaker Multi-Style Speech Synthesis with Timbre and Style Disentanglement](https://arxiv.org/abs/2211.00967)
**Wei Song et.al.** · 2022-11-22


#### [Adversarial Speaker-Consistency Learning Using Untranscribed Speech Data for Zero-Shot Multi-Speaker Text-to-Speech](https://arxiv.org/abs/2210.05979)
**Byoung Jin Choi et.al.** · 2022-11-22


#### [Back-Translation-Style Data Augmentation for Mandarin Chinese Polyphone Disambiguation](https://arxiv.org/abs/2211.09495)
**Chunyu Qiang et.al.** · 2022-11-17


#### [NANSY++: Unified Voice Synthesis with Neural Analysis and Synthesis](https://arxiv.org/abs/2211.09407)
**Hyeong-Seok Choi et.al.** · 2022-11-17


#### [NatiQ: An End-to-end Text-to-Speech System for Arabic](https://arxiv.org/abs/2206.07373)
**Ahmed Abdelali et.al.** · 2022-11-16


#### [SNIPER Training: Variable Sparsity Rate Training For Text-To-Speech](https://arxiv.org/abs/2211.07283)
**Perry Lam et.al.** · 2022-11-14


#### [Content-Dependent Fine-Grained Speaker Embedding for Zero-Shot Speaker Adaptation in Text-to-Speech Synthesis](https://arxiv.org/abs/2204.00990)
**Yixuan Zhou et.al.** · 2022-11-11


#### [T-Modules: Translation Modules for Zero-Shot Cross-Modal Machine Translation](https://arxiv.org/abs/2205.12216)
**Paul-Ambroise Duquenne et.al.** · 2022-11-10


#### [Accented Text-to-Speech Synthesis with a Conditional Variational Autoencoder](https://arxiv.org/abs/2211.03316)
**Jan Melechovsky et.al.** · 2022-11-07


#### [Parallel Attention Forcing for Machine Translation](https://arxiv.org/abs/2211.03237)
**Qingyun Dou et.al.** · 2022-11-06


#### [An Empirical Study on L2 Accents of Cross-lingual Text-to-Speech Systems via Vowel Space](https://arxiv.org/abs/2211.03078)
**Jihwan Lee et.al.** · 2022-11-06


#### [Nix-TTS: Lightweight and End-to-End Text-to-Speech via Module-wise Distillation](https://arxiv.org/abs/2203.15643)
**Rendi Chevi et.al.** · 2022-11-05


#### [Stutter-TTS: Controlled Synthesis and Improved Recognition of Stuttered Speech](https://arxiv.org/abs/2211.09731)
**Xin Zhang et.al.** · 2022-11-04


#### [NoreSpeech: Knowledge Distillation based Conditional Diffusion Model for Noise-robust Expressive TTS](https://arxiv.org/abs/2211.02448)
**Dongchao Yang et.al.** · 2022-11-04


#### [Improving Speech Prosody of Audiobook Text-to-Speech Synthesis with Acoustic and Textual Contexts](https://arxiv.org/abs/2211.02336)
**Detai Xin et.al.** · 2022-11-04


#### [Robust MelGAN: A robust universal neural vocoder for high-fidelity TTS](https://arxiv.org/abs/2210.17349)
**Kun Song et.al.** · 2022-11-02


#### [AdaVITS: Tiny VITS for Low Computing Resource Speaker Adaptation](https://arxiv.org/abs/2206.00208)
**Kun Song et.al.** · 2022-11-02


#### [Technology Pipeline for Large Scale Cross-Lingual Dubbing of Lecture Videos into Multiple Indian Languages](https://arxiv.org/abs/2211.01338)
**Anusha Prakash et.al.** · 2022-11-01


#### [Adapter-Based Extension of Multi-Speaker Text-to-Speech Model for New Speakers](https://arxiv.org/abs/2211.00585)
**Cheng-Ping Hsieh et.al.** · 2022-11-01


#### [Towards zero-shot Text-based voice editing using acoustic context conditioning, utterance embeddings, and reference encoders](https://arxiv.org/abs/2210.16045)
**Jason Fong et.al.** · 2022-10-28


#### [Residual Adapters for Few-Shot Text-to-Speech Speaker Adaptation](https://arxiv.org/abs/2210.15868)
**Nobuyuki Morioka et.al.** · 2022-10-28


#### [Explicit Intensity Control for Accented Text-to-speech](https://arxiv.org/abs/2210.15364)
**Rui Liu et.al.** · 2022-10-27


#### [FCTalker: Fine and Coarse Grained Context Modeling for Expressive Conversational Speech Synthesis](https://arxiv.org/abs/2210.15360)
**Yifan Hu et.al.** · 2022-10-27


#### [Fine-grained Noise Control for Multispeaker Speech Synthesis](https://arxiv.org/abs/2204.05070)
**Karolos Nikitaras et.al.** · 2022-10-27


#### [Text-to-speech synthesis from dark data with evaluation-in-the-loop data selection](https://arxiv.org/abs/2210.14850)
**Kentaro Seki et.al.** · 2022-10-26


#### [Cover Reproducible Steganography via Deep Generative Models](https://arxiv.org/abs/2210.14632)
**Kejiang Chen et.al.** · 2022-10-26


#### [Improving Speech-to-Speech Translation Through Unlabeled Text](https://arxiv.org/abs/2210.14514)
**Xuan-Phi Nguyen et.al.** · 2022-10-26


#### [The NPU-ASLP System for The ISCSLP 2022 Magichub Code-Swiching ASR Challenge](https://arxiv.org/abs/2210.14448)
**Yuhao Liang et.al.** · 2022-10-26


#### [Semi-Supervised Learning Based on Reference Model for Low-resource TTS](https://arxiv.org/abs/2210.14723)
**Xulong Zhang et.al.** · 2022-10-25


#### [Adapitch: Adaption Multi-Speaker Text-to-Speech Conditioned on Pitch Disentangling with Untranscribed Data](https://arxiv.org/abs/2210.13803)
**Xulong Zhang et.al.** · 2022-10-25


#### [Low-Resource Multilingual and Zero-Shot Multispeaker TTS](https://arxiv.org/abs/2210.12223)
**Florian Lux et.al.** · 2022-10-21


#### [Adaptive re-calibration of channel-wise features for Adversarial Audio Classification](https://arxiv.org/abs/2210.11722)
**Vardhan Dongre et.al.** · 2022-10-21


#### [Exact Prosody Cloning in Zero-Shot Multispeaker Text-to-Speech](https://arxiv.org/abs/2206.12229)
**Florian Lux et.al.** · 2022-10-21


#### [Text Enhancement for Paragraph Processing in End-to-End Code-switching TTS](https://arxiv.org/abs/2210.11429)
**Chunyu Qiang et.al.** · 2022-10-20


#### [Anonymizing Speech with Generative Adversarial Networks to Preserve Speaker Privacy](https://arxiv.org/abs/2210.07002)
**Sarina Meyer et.al.** · 2022-10-20


#### [Towards Relation Extraction From Speech](https://arxiv.org/abs/2210.08759)
**Tongtong Wu et.al.** · 2022-10-17


#### [Pre-Avatar: An Automatic Presentation Generation Framework Leveraging Talking Avatar](https://arxiv.org/abs/2210.06877)
**Aolan Sun et.al.** · 2022-10-13


#### [Can we use Common Voice to train a Multi-Speaker TTS system?](https://arxiv.org/abs/2210.06370)
**Sewade Ogun et.al.** · 2022-10-12


#### [GenerSpeech: Towards Style Transfer for Generalizable Out-Of-Domain Text-to-Speech](https://arxiv.org/abs/2205.07211)
**Rongjie Huang et.al.** · 2022-10-12


#### [UTTS: Unsupervised TTS with Conditional Disentangled Sequential Variational Auto-encoder](https://arxiv.org/abs/2206.02512)
**Jiachen Lian et.al.** · 2022-10-11


#### [An Overview of Affective Speech Synthesis and Conversion in the Deep Learning Era](https://arxiv.org/abs/2210.03538)
**Andreas Triantafyllopoulos et.al.** · 2022-10-06


#### [Transfer Learning Framework for Low-Resource Text-to-Speech using a Large-Scale Unlabeled Speech Corpus](https://arxiv.org/abs/2203.15447)
**Minchan Kim et.al.** · 2022-10-06


#### [Towards MOOCs for Lipreading: Using Synthetic Talking Heads to Train Humans in Lipreading at Scale](https://arxiv.org/abs/2208.09796)
**Aditya Agarwal et.al.** · 2022-10-04


#### [Facial Landmark Predictions with Applications to Metaverse](https://arxiv.org/abs/2209.14698)
**Qiao Han et.al.** · 2022-09-29


#### [Multi-Task Adversarial Training Algorithm for Multi-Speaker Neural Text-to-Speech](https://arxiv.org/abs/2209.12549)
**Yusuke Nakai et.al.** · 2022-09-26


#### [EPIC TTS Models: Empirical Pruning Investigations Characterizing Text-To-Speech Models](https://arxiv.org/abs/2209.10890)
**Perry Lam et.al.** · 2022-09-22


#### [MnTTS: An Open-Source Mongolian Text-to-Speech Synthesis Dataset and Accompanied Baseline](https://arxiv.org/abs/2209.10848)
**Yifan Hu et.al.** · 2022-09-22


#### [Controllable Accented Text-to-Speech Synthesis](https://arxiv.org/abs/2209.10804)
**Rui Liu et.al.** · 2022-09-22


#### [TIMIT-TTS: a Text-to-Speech Dataset for Multimodal Synthetic Media Detection](https://arxiv.org/abs/2209.08000)
**Davide Salvi et.al.** · 2022-09-16


#### [Using Rater and System Metadata to Explain Variance in the VoiceMOS Challenge 2022 Dataset](https://arxiv.org/abs/2209.06358)
**Michael Chinen et.al.** · 2022-09-14


#### [Enhanced Direct Speech-to-Speech Translation Using Self-supervised Pre-training and Data Augmentation](https://arxiv.org/abs/2204.02967)
**Sravya Popuri et.al.** · 2022-09-13


#### [SANIP: Shopping Assistant and Navigation for the visually impaired](https://arxiv.org/abs/2209.03570)
**Shubham Deshmukh et.al.** · 2022-09-08


#### [Non-Standard Vietnamese Word Detection and Normalization for Text-to-Speech](https://arxiv.org/abs/2209.02971)
**Huu-Tien Dang et.al.** · 2022-09-07


#### [Deliberation Model for On-Device Spoken Language Understanding](https://arxiv.org/abs/2204.01893)
**Duc Le et.al.** · 2022-09-07


#### [Improving Contextual Recognition of Rare Words with an Alternate Spelling Prediction Model](https://arxiv.org/abs/2209.01250)
**Jennifer Drexler Fox et.al.** · 2022-09-02


#### [Karaoker: Alignment-free singing voice synthesis with speech training data](https://arxiv.org/abs/2204.04127)
**Panos Kakoulidis et.al.** · 2022-08-31


#### [Training Text-To-Speech Systems From Synthetic Data: A Practical Approach For Accent Transfer Tasks](https://arxiv.org/abs/2208.13183)
**Lev Finkelstein et.al.** · 2022-08-28


#### [SOMOS: The Samsung Open MOS Dataset for the Evaluation of Neural Text-to-Speech Synthesis](https://arxiv.org/abs/2204.03040)
**Georgia Maniati et.al.** · 2022-08-24


#### [Visualising Model Training via Vowel Space for Text-To-Speech Systems](https://arxiv.org/abs/2208.09775)
**Binu Abeysinghe et.al.** · 2022-08-21


#### [Towards Parametric Speech Synthesis Using Gaussian-Markov Model of Spectral Envelope and Wavelet-Based Decomposition of F0](https://arxiv.org/abs/2208.07122)
**Mohammed Salah Al-Radhi et.al.** · 2022-08-15


#### [Hierarchical and Multi-Scale Variational Autoencoder for Diverse and Natural Non-Autoregressive Text-to-Speech](https://arxiv.org/abs/2204.04004)
**Jae-Sung Bae et.al.** · 2022-08-15


#### [A Study of Modeling Rising Intonation in Cantonese Neural Speech Synthesis](https://arxiv.org/abs/2208.02189)
**Qibing Bai et.al.** · 2022-08-03


#### [Few-Shot Cross-Lingual TTS Using Transferable Phoneme Embedding](https://arxiv.org/abs/2206.15427)
**Wei-Ping Huang et.al.** · 2022-08-03


#### [Low-data? No problem: low-resource, language-agnostic conversational text-to-speech via F0-conditioned data augmentation](https://arxiv.org/abs/2207.14607)
**Giulia Comini et.al.** · 2022-07-29


#### [Transplantation of Conversational Speaking Style with Interjections in Sequence-to-Sequence Speech Synthesis](https://arxiv.org/abs/2207.12262)
**Raul Fernandez et.al.** · 2022-07-25


#### [When Is TTS Augmentation Through a Pivot Language Useful?](https://arxiv.org/abs/2207.09889)
**Nathaniel Robinson et.al.** · 2022-07-20


#### [Mixed-Phoneme BERT: Improving BERT with Mixed Phoneme and Sup-Phoneme Representations for Text to Speech](https://arxiv.org/abs/2203.17190)
**Guangyan Zhang et.al.** · 2022-07-19


#### [Regotron: Regularizing the Tacotron2 architecture via monotonic alignment loss](https://arxiv.org/abs/2204.13437)
**Efthymios Georgiou et.al.** · 2022-07-14


#### [ProDiff: Progressive Fast Diffusion Model For High-Quality Text-to-Speech](https://arxiv.org/abs/2207.06389)
**Rongjie Huang et.al.** · 2022-07-13


#### [Controllable and Lossless Non-Autoregressive End-to-End Text-to-Speech](https://arxiv.org/abs/2207.06088)
**Zhengxi Liu et.al.** · 2022-07-13


#### [SATTS: Speaker Attractor Text to Speech, Learning to Speak by Learning to Separate](https://arxiv.org/abs/2207.06011)
**Nabarun Goswami et.al.** · 2022-07-13


#### [Text-driven Emotional Style Control and Cross-speaker Style Transfer in Neural TTS](https://arxiv.org/abs/2207.06000)
**Yookyung Shin et.al.** · 2022-07-13


#### [A Cyclical Approach to Synthetic and Natural Speech Mismatch Refinement of Neural Post-filter for Low-cost Text-to-speech System](https://arxiv.org/abs/2207.05913)
**Yi-Chiao Wu et.al.** · 2022-07-13


#### [LIP: Lightweight Intelligent Preprocessor for meaningful text-to-speech](https://arxiv.org/abs/2207.07118)
**Harshvardhan Anand et.al.** · 2022-07-11


#### [Speaker consistency loss and step-wise optimization for semi-supervised joint training of TTS and ASR using unpaired text data](https://arxiv.org/abs/2207.04659)
**Naoki Makishima et.al.** · 2022-07-11


#### [DelightfulTTS 2: End-to-End Speech Synthesis with Adversarial Vector-Quantized Auto-Encoders](https://arxiv.org/abs/2207.04646)
**Yanqing Liu et.al.** · 2022-07-11


#### [WavThruVec: Latent speech representation as intermediate features for neural speech synthesis](https://arxiv.org/abs/2203.16930)
**Hubert Siuzdak et.al.** · 2022-07-11


#### [VoiceMe: Personalized voice generation in TTS](https://arxiv.org/abs/2203.15379)
**Pol van Rijn et.al.** · 2022-07-11


#### [BibleTTS: a large, high-fidelity, multilingual, and uniquely African speech corpus](https://arxiv.org/abs/2207.03546)
**Josh Meyer et.al.** · 2022-07-07


#### [Glow-WaveGAN 2: High-quality Zero-shot Text-to-speech Synthesis and Any-to-any Voice Conversion](https://arxiv.org/abs/2207.01832)
**Yi Lei et.al.** · 2022-07-05


#### [Cross-Speaker Emotion Transfer for Low-Resource Text-to-Speech Using Non-Parallel Voice Conversion with Pitch-Shift Data Augmentation](https://arxiv.org/abs/2204.10020)
**Ryo Terashima et.al.** · 2022-07-05


#### [BERT, can HE predict contrastive focus? Predicting and controlling prominence in neural TTS using a language model](https://arxiv.org/abs/2207.01718)
**Brooke Stephenson et.al.** · 2022-07-04


#### [Unify and Conquer: How Phonetic Feature Representation Affects Polyglot Text-To-Speech (TTS)](https://arxiv.org/abs/2207.01547)
**Ariadna Sanchez et.al.** · 2022-07-04


#### [Mix and Match: An Empirical Study on Training Corpus Composition for Polyglot Text-To-Speech (TTS)](https://arxiv.org/abs/2207.01507)
**Ziyao Zhang et.al.** · 2022-07-04


#### [Computer-assisted Pronunciation Training -- Speech synthesis is almost all you need](https://arxiv.org/abs/2207.00774)
**Daniel Korzekwa et.al.** · 2022-07-02


#### [A Polyphone BERT for Polyphone Disambiguation in Mandarin Chinese](https://arxiv.org/abs/2207.12089)
**Song Zhang et.al.** · 2022-07-01


#### [Building African Voices](https://arxiv.org/abs/2207.00688)
**Perez Ogayo et.al.** · 2022-07-01


#### [Automatic Evaluation of Speaker Similarity](https://arxiv.org/abs/2207.00344)
**Deja Kamil et.al.** · 2022-07-01


#### [Language Model-Based Emotion Prediction Methods for Emotional Speech Synthesis Systems](https://arxiv.org/abs/2206.15067)
**Hyun-Wook Yoon et.al.** · 2022-07-01


#### [JETS: Jointly Training FastSpeech2 and HiFi-GAN for End to End Text to Speech](https://arxiv.org/abs/2203.16852)
**Dan Lim et.al.** · 2022-07-01


#### [R-MelNet: Reduced Mel-Spectral Modeling for Neural TTS](https://arxiv.org/abs/2206.15276)
**Kyle Kastner et.al.** · 2022-06-30


#### [TTS-by-TTS 2: Data-selective augmentation for neural speech synthesis using ranking support vector machine with variational autoencoder](https://arxiv.org/abs/2206.14984)
**Eunwoo Song et.al.** · 2022-06-30


#### [VQTTS: High-Fidelity Text-to-Speech Synthesis with Self-Supervised VQ Acoustic Feature](https://arxiv.org/abs/2204.00768)
**Chenpeng Du et.al.** · 2022-06-30


#### [Improving Deliberation by Text-Only and Semi-Supervised Training](https://arxiv.org/abs/2206.14716)
**Ke Hu et.al.** · 2022-06-29


#### [Simple and Effective Multi-sentence TTS with Expressive and Coherent Prosody](https://arxiv.org/abs/2206.14643)
**Peter Makarov et.al.** · 2022-06-29


#### [DRSpeech: Degradation-Robust Text-to-Speech Synthesis with Frame-Level and Utterance-Level Acoustic Representation Learning](https://arxiv.org/abs/2203.15683)
**Takaaki Saeki et.al.** · 2022-06-29


#### [Expressive, Variable, and Controllable Duration Modelling in TTS](https://arxiv.org/abs/2206.14165)
**Ammar Abbas et.al.** · 2022-06-28


#### [Comparison of Speech Representations for the MOS Prediction System](https://arxiv.org/abs/2206.13817)
**Aki Kunikoshi et.al.** · 2022-06-28


#### [Synthesizing Personalized Non-speech Vocalization from Discrete Speech Representations](https://arxiv.org/abs/2206.12662)
**Chin-Cheng Hsu et.al.** · 2022-06-25


#### [SANE-TTS: Stable And Natural End-to-End Multilingual Text-to-Speech](https://arxiv.org/abs/2206.12132)
**Hyunjae Cho et.al.** · 2022-06-24


#### [End-to-End Text-to-Speech Based on Latent Representation of Speaking Styles Using Spontaneous Dialogue](https://arxiv.org/abs/2206.12040)
**Kentaro Mitsui et.al.** · 2022-06-24


#### [Towards Optimizing OCR for Accessibility](https://arxiv.org/abs/2206.10254)
**Peya Mowar et.al.** · 2022-06-24


#### [A Simple Baseline for Domain Adaptation in End to End ASR Systems Using Synthetic Data](https://arxiv.org/abs/2206.13240)
**Raviraj Joshi et.al.** · 2022-06-22


#### [Human-in-the-loop Speaker Adaptation for DNN-based Multi-speaker TTS](https://arxiv.org/abs/2206.10256)
**Kenta Udagawa et.al.** · 2022-06-21


#### [Automatic Prosody Annotation with Pre-Trained Text-Speech Model](https://arxiv.org/abs/2206.07956)
**Ziqian Dai et.al.** · 2022-06-16


#### [Accurate Emotion Strength Assessment for Seen and Unseen Speech Based on Data-Driven Deep Learning](https://arxiv.org/abs/2206.07229)
**Rui Liu et.al.** · 2022-06-15


#### [Face-Dubbing++: Lip-Synchronous, Voice Preserving Translation of Videos](https://arxiv.org/abs/2206.04523)
**Alexander Waibel et.al.** · 2022-06-09


#### [FlexLip: A Controllable Text-to-Lip System](https://arxiv.org/abs/2206.03206)
**Dan Oneata et.al.** · 2022-06-07


#### [Preparing an Endangered Language for the Digital Age: The Case of Judeo-Spanish](https://arxiv.org/abs/2205.15599)
**Alp Öktem et.al.** · 2022-05-31


#### [Guided-TTS 2: A Diffusion Model for High-quality Adaptive Text-to-Speech with Untranscribed Data](https://arxiv.org/abs/2205.15370)
**Sungwon Kim et.al.** · 2022-05-30


#### [Exploiting Transliterated Words for Finding Similarity in Inter-Language News Articles using Machine Learning](https://arxiv.org/abs/2206.11860)
**Sameea Naeem et.al.** · 2022-05-29


#### [QSpeech: Low-Qubit Quantum Speech Application Toolkit](https://arxiv.org/abs/2205.13221)
**Zhenhou Hong et.al.** · 2022-05-26


#### [TDASS: Target Domain Adaptation Speech Synthesis Framework for Multi-speaker Low-Resource TTS](https://arxiv.org/abs/2205.11824)
**Xulong Zhang et.al.** · 2022-05-24


#### [PaddleSpeech: An Easy-to-Use All-in-One Speech Toolkit](https://arxiv.org/abs/2205.12007)
**Hui Zhang et.al.** · 2022-05-20


#### [Talking Face Generation with Multilingual TTS](https://arxiv.org/abs/2205.06421)
**Hyoung-Kyu Song et.al.** · 2022-05-13


#### [NaturalSpeech: End-to-End Text to Speech Synthesis with Human-Level Quality](https://arxiv.org/abs/2205.04421)
**Xu Tan et.al.** · 2022-05-10


#### [Cross-Utterance Conditioned VAE for Non-Autoregressive Text-to-Speech](https://arxiv.org/abs/2205.04120)
**Yang Li et.al.** · 2022-05-09


#### [ReCAB-VAE: Gumbel-Softmax Variational Inference Based on Analytic Divergence](https://arxiv.org/abs/2205.04104)
**Sangshin Oh et.al.** · 2022-05-09


#### [SyntaSpeech: Syntax-Aware Generative Adversarial Text-to-Speech](https://arxiv.org/abs/2204.11792)
**Zhenhui Ye et.al.** · 2022-04-25


#### [LibriS2S: A German-English Speech-to-Speech Translation Corpus](https://arxiv.org/abs/2204.10593)
**Pedro Jeuris et.al.** · 2022-04-22


#### [FastDiff: A Fast Conditional Diffusion Model for High-Quality Speech Synthesis](https://arxiv.org/abs/2204.09934)
**Rongjie Huang et.al.** · 2022-04-21


#### [Does Audio Deepfake Detection Generalize?](https://arxiv.org/abs/2203.16263)
**Nicolas M. Müller et.al.** · 2022-04-21


#### [Audio Deep Fake Detection System with Neural Stitching for ADD 2022](https://arxiv.org/abs/2204.08720)
**Rui Yan et.al.** · 2022-04-20


#### [Applying Feature Underspecified Lexicon Phonological Features in Multilingual Text-to-Speech](https://arxiv.org/abs/2204.07228)
**Cong Zhang et.al.** · 2022-04-14


#### [Enhancement of Pitch Controllability using Timbre-Preserving Pitch Augmentation in FastPitch](https://arxiv.org/abs/2204.05753)
**Hanbin Bae et.al.** · 2022-04-12


#### [Arabic Text-To-Speech (TTS) Data Preparation](https://arxiv.org/abs/2204.03255)
**Hala Al Masri et.al.** · 2022-04-07


#### [Unsupervised Quantized Prosody Representation for Controllable Speech Synthesis](https://arxiv.org/abs/2204.03238)
**Yutian Wang et.al.** · 2022-04-07


#### [AdaSpeech 4: Adaptive Text to Speech in Zero-Shot Scenarios](https://arxiv.org/abs/2204.00436)
**Yihan Wu et.al.** · 2022-04-01


#### [An End-to-end Chinese Text Normalization Model based on Rule-guided Flat-Lattice Transformer](https://arxiv.org/abs/2203.16954)
**Wenlin Dai et.al.** · 2022-03-31


#### [A Character-level Span-based Model for Mandarin Prosodic Structure Prediction](https://arxiv.org/abs/2203.16922)
**Xueyuan Chen et.al.** · 2022-03-31


#### [Open Source MagicData-RAMC: A Rich Annotated Mandarin Conversational(RAMC) Speech Dataset](https://arxiv.org/abs/2203.16844)
**Zehui Yang et.al.** · 2022-03-31


#### [NeuFA: Neural Network Based End-to-End Forced Alignment with Bidirectional Attention Mechanism](https://arxiv.org/abs/2203.16838)
**Jingbei Li et.al.** · 2022-03-31


#### [End to End Lip Synchronization with a Temporal AutoEncoder](https://arxiv.org/abs/2203.16224)
**Yoav Shalev et.al.** · 2022-03-30


#### [Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis](https://arxiv.org/abs/2104.12292)
**Erica Cooper et.al.** · 2022-02-25



### 2021

#### [Extending Text-to-Speech Synthesis with Articulatory Movement Prediction using Ultrasound Tongue Imaging](https://arxiv.org/abs/2107.05550)
**Tamás Gábor Csapó et.al.** · 2021-07-13


#### [Location, Location: Enhancing the Evaluation of Text-to-Speech Synthesis Using the Rapid Prosody Transcription Paradigm](https://arxiv.org/abs/2107.02527)
**Elijah Gutierrez et.al.** · 2021-07-07



### 2019

#### [Sequence to Sequence Neural Speech Synthesis with Prosody Modification Capabilities](https://arxiv.org/abs/1909.10302)
**Slava Shechtman et.al.** · 2019-09-26


#### [Neural Harmonic-plus-Noise Waveform Model with Trainable Maximum Voice Frequency for Text-to-Speech Synthesis](https://arxiv.org/abs/1908.10256)
**Xin Wang et.al.** · 2019-08-28


#### [Effective parameter estimation methods for an ExcitNet model in generative text-to-speech systems](https://arxiv.org/abs/1905.08486)
**Ohsung Kwon et.al.** · 2019-05-22



### 2017

#### [Statistical Parametric Speech Synthesis Incorporating Generative Adversarial Networks](https://arxiv.org/abs/1709.08041)
**Yuki Saito et.al.** · 2017-09-26


<!-- PAPERS_TABLE_END -->
