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
