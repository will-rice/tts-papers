# 2024

557 papers in this year.

### [EmoReg: Directional Latent Vector Modeling for Emotional Intensity Regularization in Diffusion-based Voice Conversion](2412.20359.md)
**Ashishkumar Gudmalwar, Ishan D. Biyani, Nirmesh Shah, Pankaj Wasnik et al.** · 2024-12-29

<details>
<summary>Abstract</summary>

The Emotional Voice Conversion (EVC) aims to convert the discrete emotional state from the source emotion to the target for a given speech utterance while preserving linguistic content. In this paper, we propose regularizing emotion intensity in the diffusion-based EVC framework to generate precise speech of the target emotion. Traditional approaches control the intensity of an emotional state in the utterance via emotion class probabilities or intensity labels that often lead to inept style manipulations and degradations in quality. On the contrary, we aim to regulate emotion intensity using self-supervised learning-based feature representations and unsupervised directional latent vector modeling (DVM) in the emotional embedding space within a diffusion-based framework. These emotion embeddings can be modified based on the given target emotion intensity and the corresponding direction vector. Furthermore, the updated embeddings can be fused in the reverse diffusion process to generate the speech with the desired emotion and intensity. In summary, this paper aims to achieve high-quality emotional intensity regularization in the diffusion-based EVC framework, which is the first of its kind work. The effectiveness of the proposed method has been shown across state-of-the-art (SOTA) baselines in terms of subjective and objective evaluations for the English and Hindi languages \footnote{Demo samples are available at the following URL: \url{https://nirmesh-sony.github.io/EmoReg/}}.

</details>

### [Stable-TTS: Stable Speaker-Adaptive Text-to-Speech Synthesis via Prosody Prompting](2412.20155.md)
**Wooseok Han, Minki Kang, Changhun Kim, Eunho Yang** · 2024-12-28

<details>
<summary>Abstract</summary>

Speaker-adaptive Text-to-Speech (TTS) synthesis has attracted considerable attention due to its broad range of applications, such as personalized voice assistant services. While several approaches have been proposed, they often exhibit high sensitivity to either the quantity or the quality of target speech samples. To address these limitations, we introduce Stable-TTS, a novel speaker-adaptive TTS framework that leverages a small subset of a high-quality pre-training dataset, referred to as prior samples. Specifically, Stable-TTS achieves prosody consistency by leveraging the high-quality prosody of prior samples, while effectively capturing the timbre of the target speaker. Additionally, it employs a prior-preservation loss during fine-tuning to maintain the synthesis ability for prior samples to prevent overfitting on target samples. Extensive experiments demonstrate the effectiveness of Stable-TTS even under limited amounts of and noisy target speech samples.

</details>

### [CrossSpeech++: Cross-lingual Speech Synthesis with Decoupled Language and Speaker Generation](2412.20048.md)
**Ji-Hoon Kim, Hong-Sun Yang, Yoon-Cheol Ju, Il-Hwan Kim et al.** · 2024-12-28

<details>
<summary>Abstract</summary>

The goal of this work is to generate natural speech in multiple languages while maintaining the same speaker identity, a task known as cross-lingual speech synthesis. A key challenge of cross-lingual speech synthesis is the language-speaker entanglement problem, which causes the quality of cross-lingual systems to lag behind that of intra-lingual systems. In this paper, we propose CrossSpeech++, which effectively disentangles language and speaker information and significantly improves the quality of cross-lingual speech synthesis. To this end, we break the complex speech generation pipeline into two simple components: language-dependent and speaker-dependent generators. The language-dependent generator produces linguistic variations that are not biased by specific speaker attributes. The speaker-dependent generator models acoustic variations that characterize speaker identity. By handling each type of information in separate modules, our method can effectively disentangle language and speaker representation. We conduct extensive experiments using various metrics, and demonstrate that CrossSpeech++ achieves significant improvements in cross-lingual speech synthesis, outperforming existing methods by a large margin.

</details>

### ["I've Heard of You!": Generate Spoken Named Entity Recognition Data for Unseen Entities](2412.19102.md)
**Jiawei Yu, Xiang Geng, Yuang Li, Mengxin Ren et al.** · 2024-12-26

<details>
<summary>Abstract</summary>

Spoken named entity recognition (NER) aims to identify named entities from speech, playing an important role in speech processing. New named entities appear every day, however, annotating their Spoken NER data is costly. In this paper, we demonstrate that existing Spoken NER systems perform poorly when dealing with previously unseen named entities. To tackle this challenge, we propose a method for generating Spoken NER data based on a named entity dictionary (NED) to reduce costs. Specifically, we first use a large language model (LLM) to generate sentences from the sampled named entities and then use a text-to-speech (TTS) system to generate the speech. Furthermore, we introduce a noise metric to filter out noisy data. To evaluate our approach, we release a novel Spoken NER benchmark along with a corresponding NED containing 8,853 entities. Experiment results show that our method achieves state-of-the-art (SOTA) performance in the in-domain, zero-shot domain adaptation, and fully zero-shot settings. Our data will be available at https://github.com/DeepLearnXMU/HeardU.

</details>

### [Indonesian-English Code-Switching Speech Synthesizer Utilizing Multilingual STEN-TTS and Bert LID](2412.19043.md)
**Ahmad Alfani Handoyo, Chung Tran, Dessi Puji Lestari, Sakriani Sakti** · 2024-12-26

<details>
<summary>Abstract</summary>

Multilingual text-to-speech systems convert text into speech across multiple languages. In many cases, text sentences may contain segments in different languages, a phenomenon known as code-switching. This is particularly common in Indonesia, especially between Indonesian and English. Despite its significance, no research has yet developed a multilingual TTS system capable of handling code-switching between these two languages. This study addresses Indonesian-English code-switching in STEN-TTS. Key modifications include adding a language identification component to the text-to-phoneme conversion using finetuned BERT for per-word language identification, as well as removing language embedding from the base model. Experimental results demonstrate that the code-switching model achieves superior naturalness and improved speech intelligibility compared to the Indonesian and English baseline STEN-TTS models.

</details>

### [VoiceDiT: Dual-Condition Diffusion Transformer for Environment-Aware Speech Synthesis](2412.19259.md)
**Jaemin Jung, Junseok Ahn, Chaeyoung Jung, Tan Dat Nguyen et al.** · 2024-12-26

<details>
<summary>Abstract</summary>

We present VoiceDiT, a multi-modal generative model for producing environment-aware speech and audio from text and visual prompts. While aligning speech with text is crucial for intelligible speech, achieving this alignment in noisy conditions remains a significant and underexplored challenge in the field. To address this, we present a novel audio generation pipeline named VoiceDiT. This pipeline includes three key components: (1) the creation of a large-scale synthetic speech dataset for pre-training and a refined real-world speech dataset for fine-tuning, (2) the Dual-DiT, a model designed to efficiently preserve aligned speech information while accurately reflecting environmental conditions, and (3) a diffusion-based Image-to-Audio Translator that allows the model to bridge the gap between audio and image, facilitating the generation of environmental sound that aligns with the multi-modal prompts. Extensive experimental results demonstrate that VoiceDiT outperforms previous models on real-world datasets, showcasing significant improvements in both audio quality and modality integration.

</details>

### [Advancing NAM-to-Speech Conversion with Novel Methods and the MultiNAM Dataset](2412.18839.md)
**Neil Shah, Shirish Karande, Vineet Gandhi** · 2024-12-25

<details>
<summary>Abstract</summary>

Current Non-Audible Murmur (NAM)-to-speech techniques rely on voice cloning to simulate ground-truth speech from paired whispers. However, the simulated speech often lacks intelligibility and fails to generalize well across different speakers. To address this issue, we focus on learning phoneme-level alignments from paired whispers and text and employ a Text-to-Speech (TTS) system to simulate the ground-truth. To reduce dependence on whispers, we learn phoneme alignments directly from NAMs, though the quality is constrained by the available training data. To further mitigate reliance on NAM/whisper data for ground-truth simulation, we propose incorporating the lip modality to infer speech and introduce a novel diffusion-based method that leverages recent advancements in lip-to-speech technology. Additionally, we release the MultiNAM dataset with over 7.96 hours of paired NAM, whisper, video, and text data from two speakers and benchmark all methods on this dataset. Speech samples and the dataset are available at https://diff-nam.github.io/DiffNAM/

</details>

### [Intra- and Inter-modal Context Interaction Modeling for Conversational Speech Synthesis](2412.18733.md)
**Zhenqi Jia, Rui Liu** · 2024-12-25

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis (CSS) aims to effectively take the multimodal dialogue history (MDH) to generate speech with appropriate conversational prosody for target utterance. The key challenge of CSS is to model the interaction between the MDH and the target utterance. Note that text and speech modalities in MDH have their own unique influences, and they complement each other to produce a comprehensive impact on the target utterance. Previous works did not explicitly model such intra-modal and inter-modal interactions. To address this issue, we propose a new intra-modal and inter-modal context interaction scheme-based CSS system, termed III-CSS. Specifically, in the training phase, we combine the MDH with the text and speech modalities in the target utterance to obtain four modal combinations, including Historical Text-Next Text, Historical Speech-Next Speech, Historical Text-Next Speech, and Historical Speech-Next Text. Then, we design two contrastive learning-based intra-modal and two inter-modal interaction modules to deeply learn the intra-modal and inter-modal context interaction. In the inference phase, we take MDH and adopt trained interaction modules to fully infer the speech prosody of the target utterance's text content. Subjective and objective experiments on the DailyTalk dataset show that III-CSS outperforms the advanced baselines in terms of prosody expressiveness. Code and speech samples are available at https://github.com/AI-S2-Lab/I3CSS.

</details>

### [MRI2Speech: Speech Synthesis from Articulatory Movements Recorded by Real-time MRI](2412.18836.md)
**Neil Shah, Ayan Kashyap, Shirish Karande, Vineet Gandhi** · 2024-12-25

<details>
<summary>Abstract</summary>

Previous real-time MRI (rtMRI)-based speech synthesis models depend heavily on noisy ground-truth speech. Applying loss directly over ground truth mel-spectrograms entangles speech content with MRI noise, resulting in poor intelligibility. We introduce a novel approach that adapts the multi-modal self-supervised AV-HuBERT model for text prediction from rtMRI and incorporates a new flow-based duration predictor for speaker-specific alignment. The predicted text and durations are then used by a speech decoder to synthesize aligned speech in any novel voice. We conduct thorough experiments on two datasets and demonstrate our method's generalization ability to unseen speakers. We assess our framework's performance by masking parts of the rtMRI video to evaluate the impact of different articulators on text prediction. Our method achieves a $15.18\%$ Word Error Rate (WER) on the USC-TIMIT MRI corpus, marking a huge improvement over the current state-of-the-art. Speech samples are available at https://mri2speech.github.io/MRI2Speech/

</details>

### [GenPod: Constructive News Framing in AI-Generated Podcasts More Effectively Reduces Negative Emotions Than Non-Constructive Framing](2412.18300.md)
**Wen Ku, Yihan Liu, Wei Zhang, Pengcheng An** · 2024-12-24

<details>
<summary>Abstract</summary>

AI-generated media products are increasingly prevalent in the news industry, yet their impacts on audience perception remain underexplored. Traditional media often employs negative framing to capture attention and capitalize on news consumption, and without oversight, AI-generated news could reinforce this trend. This study examines how different framing styles-constructive versus non-constructive-affect audience responses in AI-generated podcasts. We developed a pipeline using generative AI and text-to-speech (TTS) technology to create both constructive and non-constructive news podcasts from the same set of news resources. Through empirical research (N=65), we found that constructive podcasts significantly reduced audience's negative emotions compared to non-constructive podcasts. Additionally, in certain news contexts, constructive framing might further enhance audience self-efficacy. Our findings show that simply altering the framing of AI generated content can significantly impact audience responses, and we offer insights on leveraging these effects for positive outcomes while minimizing ethical risks.

</details>

### [Long-Form Speech Generation with Spoken Language Models](2412.18603.md)
**Se Jin Park, Julian Salazar, Aren Jansen, Keisuke Kinoshita et al.** · 2024-12-24

<details>
<summary>Abstract</summary>

We consider the generative modeling of speech over multiple minutes, a requirement for long-form multimedia generation and audio-native voice assistants. However, textless spoken language models struggle to generate plausible speech past tens of seconds, due to high temporal resolution of speech tokens causing loss of coherence, architectural issues with long-sequence training or extrapolation, and memory costs at inference time. From these considerations we derive SpeechSSM, the first speech language model family to learn from and sample long-form spoken audio (e.g., 16 minutes of read or extemporaneous speech) in a single decoding session without text intermediates. SpeechSSMs leverage recent advances in linear-time sequence modeling to greatly surpass current Transformer spoken LMs in coherence and efficiency on multi-minute generations while still matching them at the utterance level. As we found current spoken language evaluations uninformative, especially in this new long-form setting, we also introduce: LibriSpeech-Long, a benchmark for long-form speech evaluation; new embedding-based and LLM-judged metrics; and quality measurements over length and time. Speech samples, the LibriSpeech-Long dataset, and any future code or model releases can be found at https://google.github.io/tacotron/publications/speechssm/.

</details>

### [Interleaved Speech-Text Language Models are Simple Streaming Text to Speech Synthesizers](2412.16102.md)
**Yifan Yang et.al.** · 2024-12-23

### [Why Do Speech Language Models Fail to Generate Semantically Coherent Outputs? A Modality Evolving Perspective](2412.17048.md)
**Hankun Wang et.al.** · 2024-12-22

### [Incremental Disentanglement for Environment-Aware Zero-Shot Text-to-Speech Synthesis](2412.16977.md)
**Ye-Xin Lu et.al.** · 2024-12-22

### [Autoregressive Speech Synthesis with Next-Distribution Prediction](2412.16846.md)
**Xinfa Zhu et.al.** · 2024-12-22

### [Scale This, Not That: Investigating Key Dataset Attributes for Efficient Speech Enhancement Scaling](2412.14890.md)
**Leying Zhang, Wangyou Zhang, Chenda Li, Yanmin Qian** · 2024-12-19

<details>
<summary>Abstract</summary>

Recent speech enhancement models have shown impressive performance gains by scaling up model complexity and training data. However, the impact of dataset variability (e.g. text, language, speaker, and noise) has been underexplored. Analyzing each attribute individually is often challenging, as multiple attributes are usually entangled in commonly used datasets, posing a significant obstacle in understanding the distinct contributions of each attribute to the model's performance. To address this challenge, we propose a generation-training-evaluation framework that leverages zero-shot text-to-speech systems to investigate the impact of controlled attribute variations on speech enhancement performance. It enables us to synthesize training datasets in a scalable manner while carefully altering each attribute. Based on the proposed framework, we analyze the scaling effects of various dataset attributes on the performance of both discriminative and generative SE models. Extensive experiments on multi-domain corpora imply that acoustic attributes (e.g., speaker and noise) are much more important to current speech enhancement models than semantic attributes (e.g., language and text), offering new insights for future research.

</details>

### [Northeastern Uni at Multilingual Counterspeech Generation: Enhancing Counter Speech Generation with LLM Alignment through Direct Preference Optimization](2412.15453.md)
**Sahil Wadhwa, Chengtian Xu, Haoming Chen, Aakash Mahalingam et al.** · 2024-12-19

<details>
<summary>Abstract</summary>

The automatic generation of counter-speech (CS) is a critical strategy for addressing hate speech by providing constructive and informed responses. However, existing methods often fail to generate high-quality, impactful, and scalable CS, particularly across diverse linguistic contexts. In this paper, we propose a novel methodology to enhance CS generation by aligning Large Language Models (LLMs) using Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO). Our approach leverages DPO to align LLM outputs with human preferences, ensuring contextually appropriate and linguistically adaptable responses. Additionally, we incorporate knowledge grounding to enhance the factual accuracy and relevance of generated CS. Experimental results demonstrate that DPO-aligned models significantly outperform SFT baselines on CS benchmarks while scaling effectively to multiple languages. These findings highlight the potential of preference-based alignment techniques to advance CS generation across varied linguistic settings. The model supervision and alignment is done in English and the same model is used for reporting metrics across other languages like Basque, Italian, and Spanish.

</details>

### [Typhoon 2: A Family of Open Text and Multimodal Thai Large Language Models](2412.13702.md)
**Kunat Pipatanakul, Potsawee Manakul, Natapong Nitarach, Warit Sirichotedumrong et al.** · 2024-12-18

<details>
<summary>Abstract</summary>

This paper introduces Typhoon 2, a series of text and multimodal large language models optimized for the Thai language. The series includes models for text, vision, and audio. Typhoon2-Text builds on state-of-the-art open models, such as Llama 3 and Qwen2, and we perform continual pre-training on a mixture of English and Thai data. We employ post-training techniques to enhance Thai language performance while preserving the base models' original capabilities. We release text models across a range of sizes, from 1 to 70 billion parameters, available in both base and instruction-tuned variants. To guardrail text generation, we release Typhoon2-Safety, a classifier enhanced for Thai cultures and language. Typhoon2-Vision improves Thai document understanding while retaining general visual capabilities, such as image captioning. Typhoon2-Audio introduces an end-to-end speech-to-speech model architecture capable of processing audio, speech, and text inputs and generating both text and speech outputs.

</details>

### [Speech Watermarking with Discrete Intermediate Representations](2412.13917.md)
**Shengpeng Ji, Ziyue Jiang, Jialong Zuo, Minghui Fang et al.** · 2024-12-18

<details>
<summary>Abstract</summary>

Speech watermarking techniques can proactively mitigate the potential harmful consequences of instant voice cloning techniques. These techniques involve the insertion of signals into speech that are imperceptible to humans but can be detected by algorithms. Previous approaches typically embed watermark messages into continuous space. However, intuitively, embedding watermark information into robust discrete latent space can significantly improve the robustness of watermarking systems. In this paper, we propose DiscreteWM, a novel speech watermarking framework that injects watermarks into the discrete intermediate representations of speech. Specifically, we map speech into discrete latent space with a vector-quantized autoencoder and inject watermarks by changing the modular arithmetic relation of discrete IDs. To ensure the imperceptibility of watermarks, we also propose a manipulator model to select the candidate tokens for watermark embedding. Experimental results demonstrate that our framework achieves state-of-the-art performance in robustness and imperceptibility, simultaneously. Moreover, our flexible frame-wise approach can serve as an efficient solution for both voice cloning detection and information hiding. Additionally, DiscreteWM can encode 1 to 150 bits of watermark information within a 1-second speech clip, indicating its encoding capacity. Audio samples are available at https://DiscreteWM.github.io/discrete_wm.

</details>

### [Synthetic Speech Classification: IEEE Signal Processing Cup 2022 challenge](2412.13279.md)
**Mahieyin Rahmun, Rafat Hasan Khan, Tanjim Taharat Aurpa, Sadia Khan et al.** · 2024-12-17

<details>
<summary>Abstract</summary>

The aim of this project is to implement and design arobust synthetic speech classifier for the IEEE Signal ProcessingCup 2022 challenge. Here, we learn a synthetic speech attributionmodel using the speech generated from various text-to-speech(TTS) algorithms as well as unknown TTS algorithms. Weexperiment with both the classical machine learning methodssuch as support vector machine, Gaussian mixture model, anddeep learning based methods such as ResNet, VGG16, and twoshallow end-to-end networks. We observe that deep learningbased methods with raw data demonstrate the best performance.

</details>

### [Enhancing Naturalness in LLM-Generated Utterances through Disfluency Insertion](2412.12710.md)
**Syed Zohaib Hassan, Pierre Lison, Pål Halvorsen** · 2024-12-17

<details>
<summary>Abstract</summary>

Disfluencies are a natural feature of spontaneous human speech but are typically absent from the outputs of Large Language Models (LLMs). This absence can diminish the perceived naturalness of synthesized speech, which is an important criteria when building conversational agents that aim to mimick human behaviours. We show how the insertion of disfluencies can alleviate this shortcoming. The proposed approach involves (1) fine-tuning an LLM with Low-Rank Adaptation (LoRA) to incorporate various types of disfluencies into LLM-generated utterances and (2) synthesizing those utterances using a text-to-speech model that supports the generation of speech phenomena such as disfluencies. We evaluated the quality of the generated speech across two metrics: intelligibility and perceived spontaneity. We demonstrate through a user study that the insertion of disfluencies significantly increase the perceived spontaneity of the generated speech. This increase came, however, along with a slight reduction in intelligibility.

</details>

### [Phoneme-Level Feature Discrepancies: A Key to Detecting Sophisticated Speech Deepfakes](2412.12619.md)
**Kuiyuan Zhang, Zhongyun Hua, Rushi Lan, Yushu Zhang et al.** · 2024-12-17

<details>
<summary>Abstract</summary>

Recent advancements in text-to-speech and speech conversion technologies have enabled the creation of highly convincing synthetic speech. While these innovations offer numerous practical benefits, they also cause significant security challenges when maliciously misused. Therefore, there is an urgent need to detect these synthetic speech signals. Phoneme features provide a powerful speech representation for deepfake detection. However, previous phoneme-based detection approaches typically focused on specific phonemes, overlooking temporal inconsistencies across the entire phoneme sequence. In this paper, we develop a new mechanism for detecting speech deepfakes by identifying the inconsistencies of phoneme-level speech features. We design an adaptive phoneme pooling technique that extracts sample-specific phoneme-level features from frame-level speech data. By applying this technique to features extracted by pre-trained audio models on previously unseen deepfake datasets, we demonstrate that deepfake samples often exhibit phoneme-level inconsistencies when compared to genuine speech. To further enhance detection accuracy, we propose a deepfake detector that uses a graph attention network to model the temporal dependencies of phoneme-level features. Additionally, we introduce a random phoneme substitution augmentation technique to increase feature diversity during training. Extensive experiments on four benchmark datasets demonstrate the superior performance of our method over existing state-of-the-art detection methods.

</details>

### [Hierarchical Control of Emotion Rendering in Speech Synthesis](2412.12498.md)
**Sho Inoue, Kun Zhou, Shuai Wang, Haizhou Li** · 2024-12-17

<details>
<summary>Abstract</summary>

Emotional text-to-speech synthesis (TTS) aims to generate realistic emotional speech from input text. However, quantitatively controlling multi-level emotion rendering remains challenging. In this paper, we propose a flow-matching based emotional TTS framework with a novel approach for emotion intensity modeling to facilitate fine-grained control over emotion rendering at the phoneme, word, and utterance levels. We introduce a hierarchical emotion distribution (ED) extractor that captures a quantifiable ED embedding across different speech segment levels. Additionally, we explore various acoustic features and assess their impact on emotion intensity modeling. During TTS training, the hierarchical ED embedding effectively captures the variance in emotion intensity from the reference audio and correlates it with linguistic and speaker information. The TTS model not only generates emotional speech during inference, but also quantitatively controls the emotion rendering over the speech constituents. Both objective and subjective evaluations demonstrate the effectiveness of our framework in terms of speech quality, emotional expressiveness, and hierarchical emotion control.

</details>

### [Deep Speech Synthesis from Multimodal Articulatory Representations](2412.13387.md)
**Peter Wu, Bohan Yu, Kevin Scheck, Alan W Black et al.** · 2024-12-17

<details>
<summary>Abstract</summary>

The amount of articulatory data available for training deep learning models is much less compared to acoustic speech data. In order to improve articulatory-to-acoustic synthesis performance in these low-resource settings, we propose a multimodal pre-training framework. On single-speaker speech synthesis tasks from real-time magnetic resonance imaging and surface electromyography inputs, the intelligibility of synthesized outputs improves noticeably. For example, compared to prior work, utilizing our proposed transfer learning methods improves the MRI-to-speech performance by 36% word error rate. In addition to these intelligibility results, our multimodal pre-trained models consistently outperform unimodal baselines on three objective and subjective synthesis quality metrics.

</details>

### [Libri2Vox Dataset: Target Speaker Extraction with Diverse Speaker Conditions and Synthetic Data](2412.12512.md)
**Yun Liu, Xuechen Liu, Xiaoxiao Miao, Junichi Yamagishi** · 2024-12-17

<details>
<summary>Abstract</summary>

Target speaker extraction (TSE) is essential in speech processing applications, particularly in scenarios with complex acoustic environments. Current TSE systems face challenges in limited data diversity and a lack of robustness in real-world conditions, primarily because they are trained on artificially mixed datasets with limited speaker variability and unrealistic noise profiles. To address these challenges, we propose Libri2Vox, a new dataset that combines clean target speech from the LibriTTS dataset with interference speech from the noisy VoxCeleb2 dataset, providing a large and diverse set of speakers under realistic noisy conditions. We also augment Libri2Vox with synthetic speakers generated using state-of-the-art speech generative models to enhance speaker diversity. Additionally, to further improve the effectiveness of incorporating synthetic data, curriculum learning is implemented to progressively train TSE models with increasing levels of difficulty. Extensive experiments across multiple TSE architectures reveal varying degrees of improvement, with SpeakerBeam demonstrating the most substantial gains: a 1.39 dB improvement in signal-to-distortion ratio (SDR) on the Libri2Talker test set compared to baseline training. Building upon these results, we further enhanced performance through our speaker similarity-based curriculum learning approach with the Conformer architecture, achieving an additional 0.78 dB improvement over conventional random sampling methods in which data samples are randomly selected from the entire dataset. These results demonstrate the complementary benefits of diverse real-world data, synthetic speaker augmentation, and structured training strategies in building robust TSE systems.

</details>

### [ProsodyFM: Unsupervised Phrasing and Intonation Control for Intelligible Speech Synthesis](2412.11795.md)
**Xiangheng He, Junjie Chen, Zixing Zhang, Björn W. Schuller** · 2024-12-16

<details>
<summary>Abstract</summary>

Prosody contains rich information beyond the literal meaning of words, which is crucial for the intelligibility of speech. Current models still fall short in phrasing and intonation; they not only miss or misplace breaks when synthesizing long sentences with complex structures but also produce unnatural intonation. We propose ProsodyFM, a prosody-aware text-to-speech synthesis (TTS) model with a flow-matching (FM) backbone that aims to enhance the phrasing and intonation aspects of prosody. ProsodyFM introduces two key components: a Phrase Break Encoder to capture initial phrase break locations, followed by a Duration Predictor for the flexible adjustment of break durations; and a Terminal Intonation Encoder which learns a bank of intonation shape tokens combined with a novel Pitch Processor for more robust modeling of human-perceived intonation change. ProsodyFM is trained with no explicit prosodic labels and yet can uncover a broad spectrum of break durations and intonation patterns. Experimental results demonstrate that ProsodyFM can effectively improve the phrasing and intonation aspects of prosody, thereby enhancing the overall intelligibility compared to four state-of-the-art (SOTA) models. Out-of-distribution experiments show that this prosody improvement can further bring ProsodyFM superior generalizability for unseen complex sentences and speakers. Our case study intuitively illustrates the powerful and fine-grained controllability of ProsodyFM over phrasing and intonation.

</details>

### [SECodec: Structural Entropy-based Compressive Speech Representation Codec for Speech Language Models](2501.00018.md)
**Linqin Wang, Yaping Liu, Zhengtao Yu, Shengxiang Gao et al.** · 2024-12-16

<details>
<summary>Abstract</summary>

With the rapid advancement of large language models (LLMs), discrete speech representations have become crucial for integrating speech into LLMs. Existing methods for speech representation discretization rely on a predefined codebook size and Euclidean distance-based quantization. However, 1) the size of codebook is a critical parameter that affects both codec performance and downstream task training efficiency. 2) The Euclidean distance-based quantization may lead to audio distortion when the size of the codebook is controlled within a reasonable range. In fact, in the field of information compression, structural information and entropy guidance are crucial, but previous methods have largely overlooked these factors. Therefore, we address the above issues from an information-theoretic perspective, we present SECodec, a novel speech representation codec based on structural entropy (SE) for building speech language models. Specifically, we first model speech as a graph, clustering the speech features nodes within the graph and extracting the corresponding codebook by hierarchically and disentangledly minimizing 2D SE. Then, to address the issue of audio distortion, we propose a new quantization method. This method still adheres to the 2D SE minimization principle, adaptively selecting the most suitable token corresponding to the cluster for each incoming original speech node. Furthermore, we develop a Structural Entropy-based Speech Language Model (SESLM) that leverages SECodec. Experimental results demonstrate that SECodec performs comparably to EnCodec in speech reconstruction, and SESLM surpasses VALL-E in zero-shot text-to-speech tasks. Code, demo speeches, speech feature graph, SE codebook, and models are available at https://github.com/wlq2019/SECodec.

</details>

### [Region-Based Optimization in Continual Learning for Audio Deepfake Detection](2412.11551.md)
**Yujie Chen, Jiangyan Yi, Cunhang Fan, Jianhua Tao et al.** · 2024-12-16

<details>
<summary>Abstract</summary>

Rapid advancements in speech synthesis and voice conversion bring convenience but also new security risks, creating an urgent need for effective audio deepfake detection. Although current models perform well, their effectiveness diminishes when confronted with the diverse and evolving nature of real-world deepfakes. To address this issue, we propose a continual learning method named Region-Based Optimization (RegO) for audio deepfake detection. Specifically, we use the Fisher information matrix to measure important neuron regions for real and fake audio detection, dividing them into four regions. First, we directly fine-tune the less important regions to quickly adapt to new tasks. Next, we apply gradient optimization in parallel for regions important only to real audio detection, and in orthogonal directions for regions important only to fake audio detection. For regions that are important to both, we use sample proportion-based adaptive gradient optimization. This region-adaptive optimization ensures an appropriate trade-off between memory stability and learning plasticity. Additionally, to address the increase of redundant neurons from old tasks, we further introduce the Ebbinghaus forgetting mechanism to release them, thereby promoting the capability of the model to learn more generalized discriminative features. Experimental results show our method achieves a 21.3% improvement in EER over the state-of-the-art continual learning approach RWM for audio deepfake detection. Moreover, the effectiveness of RegO extends beyond the audio deepfake detection domain, showing potential significance in other tasks, such as image recognition. The code is available at https://github.com/cyjie429/RegO

</details>

### [CSSinger: End-to-End Chunkwise Streaming Singing Voice Synthesis System Based on Conditional Variational Autoencoder](2412.08918.md)
**Jianwei Cui et.al.** · 2024-12-13

### [Efficient Generative Modeling with Residual Vector Quantization-Based Tokens](2412.10208.md)
**Jaehyeon Kim, Taehong Moon, Keon Lee, Jaewoong Cho** · 2024-12-13

<details>
<summary>Abstract</summary>

We introduce ResGen, an efficient Residual Vector Quantization (RVQ)-based generative model for high-fidelity generation with fast sampling. RVQ improves data fidelity by increasing the number of quantization steps, referred to as depth, but deeper quantization typically increases inference steps in generative models. To address this, ResGen directly predicts the vector embedding of collective tokens rather than individual ones, ensuring that inference steps remain independent of RVQ depth. Additionally, we formulate token masking and multi-token prediction within a probabilistic framework using discrete diffusion and variational inference. We validate the efficacy and generalizability of the proposed method on two challenging tasks across different modalities: conditional image generation on ImageNet 256x256 and zero-shot text-to-speech synthesis. Experimental results demonstrate that ResGen outperforms autoregressive counterparts in both tasks, delivering superior performance without compromising sampling speed. Furthermore, as we scale the depth of RVQ, our generative models exhibit enhanced generation fidelity or faster sampling speeds compared to similarly sized baseline models.

</details>

### [AMuSeD: An Attentive Deep Neural Network for Multimodal Sarcasm Detection Incorporating Bi-modal Data Augmentation](2412.10103.md)
**Xiyuan Gao, Shubhi Bansal, Kushaan Gowda, Zhu Li et al.** · 2024-12-13

<details>
<summary>Abstract</summary>

Detecting sarcasm effectively requires a nuanced understanding of context, including vocal tones and facial expressions. The progression towards multimodal computational methods in sarcasm detection, however, faces challenges due to the scarcity of data. To address this, we present AMuSeD (Attentive deep neural network for MUltimodal Sarcasm dEtection incorporating bi-modal Data augmentation). This approach utilizes the Multimodal Sarcasm Detection Dataset (MUStARD) and introduces a two-phase bimodal data augmentation strategy. The first phase involves generating varied text samples through Back Translation from several secondary languages. The second phase involves the refinement of a FastSpeech 2-based speech synthesis system, tailored specifically for sarcasm to retain sarcastic intonations. Alongside a cloud-based Text-to-Speech (TTS) service, this Fine-tuned FastSpeech 2 system produces corresponding audio for the text augmentations. We also investigate various attention mechanisms for effectively merging text and audio data, finding self-attention to be the most efficient for bimodal integration. Our experiments reveal that this combined augmentation and attention approach achieves a significant F1-score of 81.0% in text-audio modalities, surpassing even models that use three modalities from the MUStARD dataset.

</details>

### [CosyVoice 2: Scalable Streaming Speech Synthesis with Large Language Models](2412.10117.md)
**Zhihao Du, Yuxuan Wang, Qian Chen, Xian Shi et al.** · 2024-12-13

<details>
<summary>Abstract</summary>

In our previous work, we introduced CosyVoice, a multilingual speech synthesis model based on supervised discrete speech tokens. By employing progressive semantic decoding with two popular generative models, language models (LMs) and Flow Matching, CosyVoice demonstrated high prosody naturalness, content consistency, and speaker similarity in speech in-context learning. Recently, significant progress has been made in multi-modal large language models (LLMs), where the response latency and real-time factor of speech synthesis play a crucial role in the interactive experience. Therefore, in this report, we present an improved streaming speech synthesis model, CosyVoice 2, which incorporates comprehensive and systematic optimizations. Specifically, we introduce finite-scalar quantization to improve the codebook utilization of speech tokens. For the text-speech LM, we streamline the model architecture to allow direct use of a pre-trained LLM as the backbone. In addition, we develop a chunk-aware causal flow matching model to support various synthesis scenarios, enabling both streaming and non-streaming synthesis within a single model. By training on a large-scale multilingual dataset, CosyVoice 2 achieves human-parity naturalness, minimal response latency, and virtually lossless synthesis quality in the streaming mode. We invite readers to listen to the demos at https://funaudiollm.github.io/cosyvoice2.

</details>

### [A Preliminary Analysis of Automatic Word and Syllable Prominence Detection in Non-Native Speech With Text-to-Speech Prosody Embeddings](2412.08283.md)
**Anindita Mondal et.al.** · 2024-12-11

### [LatentSpeech: Latent Diffusion for Text-To-Speech Generation](2412.08117.md)
**Haowei Lou et.al.** · 2024-12-11

### [Aligner-Guided Training Paradigm: Advancing Text-to-Speech Models with Aligner Guided Duration](2412.08112.md)
**Haowei Lou et.al.** · 2024-12-11

### [Multimodal Latent Language Modeling with Next-Token Diffusion](2412.08635.md)
**Yutao Sun, Hangbo Bao, Wenhui Wang, Zhiliang Peng et al.** · 2024-12-11

<details>
<summary>Abstract</summary>

Multimodal generative models require a unified approach to handle both discrete data (e.g., text and code) and continuous data (e.g., image, audio, video). In this work, we propose Latent Language Modeling (LatentLM), which seamlessly integrates continuous and discrete data using causal Transformers. Specifically, we employ a variational autoencoder (VAE) to represent continuous data as latent vectors and introduce next-token diffusion for autoregressive generation of these vectors. Additionally, we develop $σ$-VAE to address the challenges of variance collapse, which is crucial for autoregressive modeling. Extensive experiments demonstrate the effectiveness of LatentLM across various modalities. In image generation, LatentLM surpasses Diffusion Transformers in both performance and scalability. When integrated into multimodal large language models, LatentLM provides a general-purpose interface that unifies multimodal generation and understanding. Experimental results show that LatentLM achieves favorable performance compared to Transfusion and vector quantized models in the setting of scaling up training tokens. In text-to-speech synthesis, LatentLM outperforms the state-of-the-art VALL-E 2 model in speaker similarity and robustness, while requiring 10x fewer decoding steps. The results establish LatentLM as a highly effective and scalable approach to advance large multimodal models.

</details>

### [A Unified Model For Voice and Accent Conversion In Speech and Singing using Self-Supervised Learning and Feature Extraction](2412.08312.md)
**Sowmya Cheripally** · 2024-12-11

<details>
<summary>Abstract</summary>

This paper presents a new voice conversion model capable of transforming both speaking and singing voices. It addresses key challenges in current systems, such as conveying emotions, managing pronunciation and accent changes, and reproducing non-verbal sounds. One of the model's standout features is its ability to perform accent conversion on hybrid voice samples that encompass both speech and singing, allowing it to change the speaker's accent while preserving the original content and prosody. The proposed model uses an encoder-decoder architecture: the encoder is based on HuBERT to process the speech's acoustic and linguistic content, while the HiFi-GAN decoder audio matches the target speaker's voice. The model incorporates fundamental frequency (f0) features and singer embeddings to enhance performance while ensuring the pitch & tone accuracy and vocal identity are preserved during transformation. This approach improves how naturally and flexibly voice style can be transformed, showing strong potential for applications in voice dubbing, content creation, and technologies like Text-to-Speech (TTS) and Interactive Voice Response (IVR) systems.

</details>

### [Zero-Shot Mono-to-Binaural Speech Synthesis](2412.08356.md)
**Alon Levkovitch, Julian Salazar, Soroosh Mariooryad, RJ Skerry-Ryan et al.** · 2024-12-11

<details>
<summary>Abstract</summary>

We present ZeroBAS, a neural method to synthesize binaural audio from monaural audio recordings and positional information without training on any binaural data. To our knowledge, this is the first published zero-shot neural approach to mono-to-binaural audio synthesis. Specifically, we show that a parameter-free geometric time warping and amplitude scaling based on source location suffices to get an initial binaural synthesis that can be refined by iteratively applying a pretrained denoising vocoder. Furthermore, we find this leads to generalization across room conditions, which we measure by introducing a new dataset, TUT Mono-to-Binaural, to evaluate state-of-the-art monaural-to-binaural synthesis methods on unseen conditions. Our zero-shot method is perceptually on-par with the performance of supervised methods on the standard mono-to-binaural dataset, and even surpasses them on our out-of-distribution TUT Mono-to-Binaural dataset. Our results highlight the potential of pretrained generative audio models and zero-shot learning to unlock robust binaural audio synthesis.

</details>

### [Preserving Speaker Information in Direct Speech-to-Speech Translation with Non-Autoregressive Generation and Pretraining](2412.07316.md)
**Rui Zhou, Akinori Ito, Takashi Nose** · 2024-12-10

<details>
<summary>Abstract</summary>

Speech-to-Speech Translation (S2ST) refers to the conversion of speech in one language into semantically equivalent speech in another language, facilitating communication between speakers of different languages. Speech-to-Discrete Unit Translation (S2UT), a mainstream approach for end-to-end S2ST, addresses challenges such as error propagation across modules and slow inference speed often encountered in traditional cascade systems. However, as discrete units primarily capture content information, conventional S2UT methods fail to retain speaker-specific characteristics from the source. Our previous work, SC-S2UT, introduced a speaker adapter and a unit-to-mel structure, enabling the preservation of speaker information and non-autoregressive speech generation. Building on this foundation, this study proposes a self-supervised pretraining method to enrich the information extracted by both the speaker adapter and the unit-to-mel structure. Additionally, we investigate different feature fusion strategies to further improve the integration of speaker and content features. Experiments conducted on the CVSS-T dataset for ES-EN and FR-EN tasks demonstrate that our proposed method achieves a BLEU score improvement of 1.14 compared to SC-S2UT, along with significant enhancements in MOS and speaker similarity. Furthermore, our approach achieves translation quality comparable to traditional S2UT, with only a minimal increase of 0.04s per utterance in inference time, while maintaining high speaker similarity. These results validate the effectiveness of the proposed method.

</details>

### [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Survey](2412.06602.md)
**Tianxin Xie et.al.** · 2024-12-09

### [EmoSpeech: A Corpus of Emotionally Rich and Contextually Detailed Speech Annotations](2412.06581.md)
**Weizhen Bian, Yubo Zhou, Kaitai Zhang, Xiaohan Gu** · 2024-12-09

<details>
<summary>Abstract</summary>

Advances in text-to-speech (TTS) technology have significantly improved the quality of generated speech, closely matching the timbre and intonation of the target speaker. However, due to the inherent complexity of human emotional expression, the development of TTS systems capable of controlling subtle emotional differences remains a formidable challenge. Existing emotional speech databases often suffer from overly simplistic labelling schemes that fail to capture a wide range of emotional states, thus limiting the effectiveness of emotion synthesis in TTS applications. To this end, recent efforts have focussed on building databases that use natural language annotations to describe speech emotions. However, these approaches are costly and require more emotional depth to train robust systems. In this paper, we propose a novel process aimed at building databases by systematically extracting emotion-rich speech segments and annotating them with detailed natural language descriptions through a generative model. This approach enhances the emotional granularity of the database and significantly reduces the reliance on costly manual annotations by automatically augmenting the data with high-level language models. The resulting rich database provides a scalable and economically viable solution for developing a more nuanced and dynamic basis for developing emotionally controlled TTS systems.

</details>

### [BERT-Vocal: End-to-End Voice Synthesis Enhanced with Bidirectional Encoder Representations from Transformers](s2:35e47d50fb05337828d8d3c56cdde70ba1d851d5.md)
**Shivam Devasar, Kunal Vardani, Vinal Patel** · 2024-12-07

<details>
<summary>Abstract</summary>

Recent advancements in text-to-speech synthesis, pri-marily leveraging deep neural network architectures, show promising outcomes. Traditionally, models were trained on single-speaker datasets, requiring extensive retraining for new voices. However, integrating speaker embeddings with the model allows training for multi-speaker scenarios without such inten-sive retraining; however, it suffers from slower convergence. In this paper, an architecture synthesizer module embedded with Bidirectional Encoder Representations from Transformers (BERT) has been developed to enhance the convergence rate. The performance of the proposed system is evaluated with Wavenet vocoders, demonstrating that BERT with attention achieves a Mean Opinion Score (MOS) of 4.2, indicating significant improvements in voice synthesis quality compared to existing models. Furthermore, a Hindi language dataset has been developed with 20 male and 20 female speakers, and our proposed model is also evaluated for this dataset.

</details>

### [Continuous Speech Tokens Makes LLMs Robust Multi-Modality Learners](2412.04917.md)
**Ze Yuan, Yanqing Liu, Shujie Liu, Sheng Zhao** · 2024-12-06

<details>
<summary>Abstract</summary>

Recent advances in GPT-4o like multi-modality models have demonstrated remarkable progress for direct speech-to-speech conversation, with real-time speech interaction experience and strong speech understanding ability. However, current research focuses on discrete speech tokens to align with discrete text tokens for language modelling, which depends on an audio codec with residual connections or independent group tokens, such a codec usually leverages large scale and diverse datasets training to ensure that the discrete speech codes have good representation for varied domain, noise, style data reconstruction as well as a well-designed codec quantizer and encoder-decoder architecture for discrete token language modelling. This paper introduces Flow-Omni, a continuous speech token based GPT-4o like model, capable of real-time speech interaction and low streaming latency. Specifically, first, instead of cross-entropy loss only, we combine flow matching loss with a pretrained autoregressive LLM and a small MLP network to predict the probability distribution of the continuous-valued speech tokens from speech prompt. second, we incorporated the continuous speech tokens to Flow-Omni multi-modality training, thereby achieving robust speech-to-speech performance with discrete text tokens and continuous speech tokens together. Experiments demonstrate that, compared to discrete text and speech multi-modality training and its variants, the continuous speech tokens mitigate robustness issues by avoiding the inherent flaws of discrete speech code's representation loss for LLM.

</details>

### [StableVC: Style Controllable Zero-Shot Voice Conversion with Conditional Flow Matching](2412.04724.md)
**Jixun Yao, Yuguang Yang, Yu Pan, Ziqian Ning et al.** · 2024-12-06

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) aims to transfer the timbre from the source speaker to an arbitrary unseen speaker while preserving the original linguistic content. Despite recent advancements in zero-shot VC using language model-based or diffusion-based approaches, several challenges remain: 1) current approaches primarily focus on adapting timbre from unseen speakers and are unable to transfer style and timbre to different unseen speakers independently; 2) these approaches often suffer from slower inference speeds due to the autoregressive modeling methods or the need for numerous sampling steps; 3) the quality and similarity of the converted samples are still not fully satisfactory. To address these challenges, we propose a style controllable zero-shot VC approach named StableVC, which aims to transfer timbre and style from source speech to different unseen target speakers. Specifically, we decompose speech into linguistic content, timbre, and style, and then employ a conditional flow matching module to reconstruct the high-quality mel-spectrogram based on these decomposed features. To effectively capture timbre and style in a zero-shot manner, we introduce a novel dual attention mechanism with an adaptive gate, rather than using conventional feature concatenation. With this non-autoregressive design, StableVC can efficiently capture the intricate timbre and style from different unseen speakers and generate high-quality speech significantly faster than real-time. Experiments demonstrate that our proposed StableVC outperforms state-of-the-art baseline systems in zero-shot VC and achieves flexible control over timbre and style from different unseen speakers. Moreover, StableVC offers approximately 25x and 1.65x faster sampling compared to autoregressive and diffusion-based baselines.

</details>

### [Fully End-to-End Chinese-Tibetan Bilingual Speech Synthesis](s2:3aacfab6be76329cca0b93f25c2ea5d399bc021c.md)
**Dongliang Chen, Chao Wei, Guanyu Li, Runyu Zhe** · 2024-12-06

<details>
<summary>Abstract</summary>

In this paper, we address the problem of insufficient amount of Tibetan speech data for bilingual speech synthesis. Based on the commonality of Chinese and Tibetan languages, we investigate a hybrid Chinese-Tibetan phoneme conversion table to share model training primitives. And then an end-to-end Chinese-Tibetan bilingual speech synthesis model is trained using the vits model. The model is capable of achieving cross-language speech synthesis for speakers utilizing merely two monolingual corpora; however, the Mean Opinion Scores (MOS) indicate a slight deterioration in the naturalness of the synthesized speech. In addition, this paper investigates the effects of whether Tibetan phonemes are labeled with tones or not, whether the bilingual speech synthesis model uses a hybrid phoneme list or not, and the training set size on the quality of speech synthesis. The experimental results show that for bilingual speech synthesis training, although adding tones to Tibetan can improve the performance of speech synthesis for a specific monolingual, it is difficult to fully utilize its performance because of dataset size; after that, this paper finds that mixed tones outperform other representations, and different language complexities lead to different amounts of data required for training.

</details>

### [DiffStyleTTS: Diffusion-based Hierarchical Prosody Modeling for Text-to-Speech with Diverse and Controllable Styles](2412.03388.md)
**Jiaxuan Liu et.al.** · 2024-12-04

### [Analytic Study of Text-Free Speech Synthesis for Raw Audio using a Self-Supervised Learning Model](2412.03074.md)
**Joonyong Park, Daisuke Saito, Nobuaki Minematsu** · 2024-12-04

<details>
<summary>Abstract</summary>

We examine the text-free speech representations of raw audio obtained from a self-supervised learning (SSL) model by analyzing the synthesized speech using the SSL representations instead of conventional text representations. Since raw audio does not have paired speech representations as transcribed texts do, obtaining speech representations from unpaired speech is crucial for augmenting available datasets for speech synthesis. Specifically, the proposed speech synthesis is conducted using discrete symbol representations from the SSL model in comparison with text representations, and analytical examinations of the synthesized speech have been carried out. The results empirically show that using text representations is advantageous for preserving semantic information, while using discrete symbol representations is superior for preserving acoustic content, including prosodic and intonational information.

</details>

### [Disentangling Speaker Representations from Intuitive Prosodic Features for Speaker-Adaptative and Prosody-Controllable Speech Synthesis](s2:a8e0b0af7798774ae258ea336bf2f36a5deff7f3.md)
**Pengyu Cheng, Zhenhua Ling, Meng Meng, Yujun Wang** · 2024-12-03

<details>
<summary>Abstract</summary>

In this paper, we propose a method of speaker-adaptative and prosody-controllable speech synthesis with a disentanglement between intuitive prosodic features and speaker representations. In this method, the intuitive prosodic features include utterance-level pitch, pitch range, speak rate and energy. A residual speaker information encoder with a set of adversarial classifiers is designed to extract the speaker characteristics that can’t be described by these intuitive prosodic features. Further, the outputs of the residual speaker information encoder are concatenated with intuitive prosodic features to obtain complete speaker representations for acoustic feature prediction. Experimental results have demonstrated that our proposed method can synthesize speech with better naturalness and higher prosody controllability than its counterpart without the disentanglement.

</details>

### [The Codec Language Model-based Zero-Shot Spontaneous Style TTS System for CoVoC Challenge 2024](2412.01100.md)
**Shuoyi Zhou, Yixuan Zhou, Weiqin Li, Jun Chen et al.** · 2024-12-02

<details>
<summary>Abstract</summary>

This paper describes the zero-shot spontaneous style TTS system for the ISCSLP 2024 Conversational Voice Clone Challenge (CoVoC). We propose a LLaMA-based codec language model with a delay pattern to achieve spontaneous style voice cloning. To improve speech intelligibility, we introduce the Classifier-Free Guidance (CFG) strategy in the language model to strengthen conditional guidance on token prediction. To generate high-quality utterances, we adopt effective data preprocessing operations and fine-tune our model with selected high-quality spontaneous speech data. The official evaluations in the CoVoC constrained track show that our system achieves the best speech naturalness MOS of 3.80 and obtains considerable speech quality and speaker similarity results.

</details>

### [Language-Independent Prosody-Enhanced Speech Representations For Multilingual Speech Synthesis](s2:465501bc535660d2012c66d28ca1a1f20ed27fd7.md)
**Chang Liu, Zhen-Hua Ling, Yajun Hu** · 2024-12-02

<details>
<summary>Abstract</summary>

This paper proposes language-independent prosody-enhanced speech representations to improve the naturalness of speech synthesis for the target languages that lack prosodic labels. To build text-to-speech (TTS) systems for low-resource languages, recent studies have employed the representations extracted from self-supervised learning (SSL) speech models, such as wav2vec 2.0, as intermediate representations in TTS models. However, they have generally focused only on the linguistic and phonetic information in SSL representations, disregarding the prosodic information. This paper investigates the prosodic information contained in the multilingual wav2vec 2.0 model through layer-wise probing tests utilizing acoustic prosodic features and prosodic labels. Furthermore, we propose a language-independent prosody enhancement approach to improve the prosodic properties of SSL models. The proposed method introduces a prosodic label prediction loss to fine-tune wav2vec 2.0 model with multilingual prosody-annotated corpora. From the fine-tuned wav 2 vec 2.0 model, the language-independent prosody-enhanced speech representations are extracted and serve as intermediate representations of our acoustic model in the downstream TTS task. The experimental results on six target languages demonstrate that our proposed prosody-enhanced speech representations outperform the original wav2vec 2.0 representations without enhancement.

</details>

### [Text Is Not All You Need: Multimodal Prompting Helps LLMs Understand Humor](2412.05315.md)
**Ashwin Baluja** · 2024-12-01

<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have demonstrated impressive natural language understanding capabilities across various text-based tasks, understanding humor has remained a persistent challenge. Humor is frequently multimodal, relying on phonetic ambiguity, rhythm and timing to convey meaning. In this study, we explore a simple multimodal prompting approach to humor understanding and explanation. We present an LLM with both the text and the spoken form of a joke, generated using an off-the-shelf text-to-speech (TTS) system. Using multimodal cues improves the explanations of humor compared to textual prompts across all tested datasets.

</details>

### [Noro: Noise-Robust One-shot Voice Conversion with Hidden Speaker Representation Learning](2411.19770.md)
**Haorui He, Yuchen Song, Yuancheng Wang, Haoyang Li et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

The effectiveness of one-shot voice conversion (VC) decreases in real-world scenarios where reference speeches, which are often sourced from the internet, contain various disturbances like background noise. To address this issue, we introduce Noro, a noise-robust one-shot VC system. Noro features innovative components tailored for VC using noisy reference speeches, including a dual-branch reference encoding module and a noise-agnostic contrastive speaker loss. Experimental results demonstrate that Noro outperforms our baseline system in both clean and noisy scenarios, highlighting its efficacy for real-world applications. Additionally, we investigate the hidden speaker representation capabilities of our baseline system by repurposing its reference encoder as a speaker encoder. The results show that it is competitive with several advanced self-supervised learning models for speaker representation under the SUPERB settings, highlighting the potential for advancing speaker representation learning through one-shot VC tasks.

</details>

### [Parallel Stacked Aggregated Network for Voice Authentication in IoT-Enabled Smart Devices](2411.19841.md)
**Awais Khan, Ijaz Ul Haq, Khalid Mahmood Malik** · 2024-11-29

<details>
<summary>Abstract</summary>

Voice authentication on IoT-enabled smart devices has gained prominence in recent years due to increasing concerns over user privacy and security. The current authentication systems are vulnerable to different voice-spoofing attacks (e.g., replay, voice cloning, and audio deepfakes) that mimic legitimate voices to deceive authentication systems and enable fraudulent activities (e.g., impersonation, unauthorized access, financial fraud, etc.). Existing solutions are often designed to tackle a single type of attack, leading to compromised performance against unseen attacks. On the other hand, existing unified voice anti-spoofing solutions, not designed specifically for IoT, possess complex architectures and thus cannot be deployed on IoT-enabled smart devices. Additionally, most of these unified solutions exhibit significant performance issues, including higher equal error rates or lower accuracy for specific attacks. To overcome these issues, we present the parallel stacked aggregation network (PSA-Net), a lightweight framework designed as an anti-spoofing defense system for voice-controlled smart IoT devices. The PSA-Net processes raw audios directly and eliminates the need for dataset-dependent handcrafted features or pre-computed spectrograms. Furthermore, PSA-Net employs a split-transform-aggregate approach, which involves the segmentation of utterances, the extraction of intrinsic differentiable embeddings through convolutions, and the aggregation of them to distinguish legitimate from spoofed audios. In contrast to existing deep Resnet-oriented solutions, we incorporate cardinality as an additional dimension in our network, which enhances the PSA-Net ability to generalize across diverse attacks. The results show that the PSA-Net achieves more consistent performance for different attacks that exist in current anti-spoofing solutions.

</details>

### [V2SFlow: Video-to-Speech Generation with Speech Decomposition and Rectified Flow](2411.19486.md)
**Jeongsoo Choi, Ji-Hoon Kim, Jinyu Li, Joon Son Chung et al.** · 2024-11-29

<details>
<summary>Abstract</summary>

In this paper, we introduce V2SFlow, a novel Video-to-Speech (V2S) framework designed to generate natural and intelligible speech directly from silent talking face videos. While recent V2S systems have shown promising results on constrained datasets with limited speakers and vocabularies, their performance often degrades on real-world, unconstrained datasets due to the inherent variability and complexity of speech signals. To address these challenges, we decompose the speech signal into manageable subspaces (content, pitch, and speaker information), each representing distinct speech attributes, and predict them directly from the visual input. To generate coherent and realistic speech from these predicted attributes, we employ a rectified flow matching decoder built on a Transformer architecture, which models efficient probabilistic pathways from random noise to the target speech distribution. Extensive experiments demonstrate that V2SFlow significantly outperforms state-of-the-art methods, even surpassing the naturalness of ground truth utterances. Code and models are available at: https://github.com/kaistmm/V2SFlow

</details>

### [CoDiff-VC: A Codec-Assisted Diffusion Model for Zero-shot Voice Conversion](2411.18918.md)
**Yuke Li, Xinfa Zhu, Hanzhao Li, JiXun Yao et al.** · 2024-11-28

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) aims to convert the original speaker's timbre to any target speaker while keeping the linguistic content. Current mainstream zero-shot voice conversion approaches depend on pre-trained recognition models to disentangle linguistic content and speaker representation. This results in a timbre residue within the decoupled linguistic content and inadequacies in speaker representation modeling. In this study, we propose CoDiff-VC, an end-to-end framework for zero-shot voice conversion that integrates a speech codec and a diffusion model to produce high-fidelity waveforms. Our approach involves employing a single-codebook codec to separate linguistic content from the source speech. To enhance content disentanglement, we introduce Mix-Style layer normalization (MSLN) to perturb the original timbre. Additionally, we incorporate a multi-scale speaker timbre modeling approach to ensure timbre consistency and improve voice detail similarity. To improve speech quality and speaker similarity, we introduce dual classifier-free guidance, providing both content and timbre guidance during the generation process. Objective and subjective experiments affirm that CoDiff-VC significantly improves speaker similarity, generating natural and higher-quality speech.

</details>

### [Mechanisms of Multimodal Synchronization: Insights from Decoder-Based Video-Text-to-Speech Synthesis](2411.17690.md)
**Akshita Gupta, Tatiana Likhomanenko, Karren Dai Yang, Richard He Bai et al.** · 2024-11-26

<details>
<summary>Abstract</summary>

Unified decoder-only transformers have shown promise for multimodal generation, yet the mechanisms by which they synchronize modalities with heterogeneous sampling rates remain underexplored. We investigate these mechanisms through video-text-to-speech (VTTS) synthesis-a controlled task requiring fine-grained temporal alignment between sparse text, video, and continuous speech. Using a unified decoder-only transformer, dubbed Visatronic, trained on VoxCeleb2, we study: (i) how modalities contribute complementary information, (ii) how positional encoding strategies enable synchronization across heterogeneous rates, (iii) how modality ordering shapes the trade-off between in-domain performance and cross-domain transfer, (iv) how phoneme-level synchronization metrics provide diagnostic insight into per-phoneme timing errors. Our findings reveal that both "global sequential indexing'' (unique position IDs across modalities) and "co-temporal ordered indexing'' (identical IDs for temporally corresponding tokens) achieve strong synchronization performance, with co-temporal ordered indexing providing a simple mechanism without explicit timestamp metadata. Both text and video contribute complementary signals: text ensures intelligibility while video provides temporal cues and emotional expressiveness. Modality ordering reveals a consistent trade-off: video-first ordering achieves stronger in-domain performance while text-first ordering generalizes more robustly to unseen domains. Our findings also reveal, that diverse large-scale training enables transferable synchronization strategies. To enable fine-grained analysis, we also introduce TimeSync, a phoneme-level metric that reveals temporal misalignments overlooked by frame-level metrics. These insights establish VTTS as a valuable testbed for understanding temporal synchronization in unified multimodal decoders.

</details>

### [QR-VC: Leveraging Quantization Residuals for Linear Disentanglement in Zero-Shot Voice Conversion](2411.16147.md)
**Youngjun Sim, Jinsung Yoon, Wooyeol Jeong, Young-Joo Suh** · 2024-11-25

<details>
<summary>Abstract</summary>

Zero-shot voice conversion is a technique that alters the speaker identity of an input speech to match a target speaker using only a single reference utterance, without requiring additional training. Recent approaches extensively utilize self-supervised learning features with K-means quantization to extract high-quality content representations while removing speaker identity. However, this quantization process also eliminates fine-grained phonetic and prosodic variations, degrading intelligibility and prosody preservation. While prior works have primarily focused on quantized representations, quantization residuals remain underutilized and deserve further exploration. In this paper, we introduce a novel approach that fully utilizes quantization residuals by leveraging temporal properties of speech components. This facilitates the disentanglement of speaker identity and the recovery of phonetic and prosodic details lost during quantization. By applying only K-means quantization and linear projections, our method achieves simple yet effective disentanglement, without requiring complex architectures or explicit supervision. This allows for high-fidelity voice conversion trained solely with reconstruction losses. Experiments show that the proposed model outperforms existing methods across both subjective and objective metrics. It achieves superior intelligibility and speaker similarity, along with improved prosody preservation, highlighting the impact of our Linear Disentangler module.

</details>

### [Hindi audio-video-Deepfake (HAV-DF): A Hindi language-based Audio-video Deepfake Dataset](2411.15457.md)
**Sukhandeep Kaur, Mubashir Buhari, Naman Khandelwal, Priyansh Tyagi et al.** · 2024-11-23

<details>
<summary>Abstract</summary>

Deepfakes offer great potential for innovation and creativity, but they also pose significant risks to privacy, trust, and security. With a vast Hindi-speaking population, India is particularly vulnerable to deepfake-driven misinformation campaigns. Fake videos or speeches in Hindi can have an enormous impact on rural and semi-urban communities, where digital literacy tends to be lower and people are more inclined to trust video content. The development of effective frameworks and detection tools to combat deepfake misuse requires high-quality, diverse, and extensive datasets. The existing popular datasets like FF-DF (FaceForensics++), and DFDC (DeepFake Detection Challenge) are based on English language.. Hence, this paper aims to create a first novel Hindi deep fake dataset, named ``Hindi audio-video-Deepfake'' (HAV-DF). The dataset has been generated using the faceswap, lipsyn and voice cloning methods. This multi-step process allows us to create a rich, varied dataset that captures the nuances of Hindi speech and facial expressions, providing a robust foundation for training and evaluating deepfake detection models in a Hindi language context. It is unique of its kind as all of the previous datasets contain either deepfake videos or synthesized audio. This type of deepfake dataset can be used for training a detector for both deepfake video and audio datasets. Notably, the newly introduced HAV-DF dataset demonstrates lower detection accuracy's across existing detection methods like Headpose, Xception-c40, etc. Compared to other well-known datasets FF-DF, and DFDC. This trend suggests that the HAV-DF dataset presents deeper challenges to detect, possibly due to its focus on Hindi language content and diverse manipulation techniques. The HAV-DF dataset fills the gap in Hindi-specific deepfake datasets, aiding multilingual deepfake detection development.

</details>

### [VQalAttent: a Transparent Speech Generation Pipeline based on Transformer-learned VQ-VAE Latent Space](2411.14642.md)
**Armani Rodriguez, Silvija Kokalj-Filipovic** · 2024-11-22

<details>
<summary>Abstract</summary>

Generating high-quality speech efficiently remains a key challenge for generative models in speech synthesis. This paper introduces VQalAttent, a lightweight model designed to generate fake speech with tunable performance and interpretability. Leveraging the AudioMNIST dataset, consisting of human utterances of decimal digits (0-9), our method employs a two-step architecture: first, a scalable vector quantized autoencoder (VQ-VAE) that compresses audio spectrograms into discrete latent representations, and second, a decoder-only transformer that learns the probability model of these latents. Trained transformer generates similar latent sequences, convertible to audio spectrograms by the VQ-VAE decoder, from which we generate fake utterances. Interpreting statistical and perceptual quality of the fakes, depending on the dimension and the extrinsic information of the latent space, enables guided improvements in larger, commercial generative models. As a valuable tool for understanding and refining audio synthesis, our results demonstrate VQalAttent's capacity to generate intelligible speech samples with limited computational resources, while the modularity and transparency of the training pipeline helps easily correlate the analytics with modular modifications, hence providing insights for the more complex models.

</details>

### [Lightweight Model Attribution and Detection of Synthetic Speech via Audio Residual Fingerprints](2411.14013.md)
**Matías Pizarro, Mike Laszkiewicz, Dorothea Kolossa, Asja Fischer** · 2024-11-21

<details>
<summary>Abstract</summary>

As speech generation technologies advance, so do risks of impersonation, misinformation, and spoofing. We present a lightweight, training-free approach for detecting synthetic speech and attributing it to its source model. Our method addresses three tasks: (1) single-model attribution in an open-world setting, (2) multi-model attribution in a closed-world setting, and (3) real vs. synthetic speech classification. The core idea is simple: we compute standardized average residuals--the difference between an audio signal and its filtered version--to extract model-agnostic fingerprints that capture synthesis artifacts. Experiments across multiple synthesis systems and languages show AUROC scores above 99%, with strong reliability even when only a subset of model outputs is available. The method maintains high performance under common audio distortions, including echo and moderate background noise, while data augmentation can improve results in more challenging conditions. In addition, out-of-domain detection is performed using Mahalanobis distances to in-domain residual fingerprints, achieving an F1 score of 0.91 on unseen models, reinforcing the method's efficiency, generalizability, and suitability for digital forensics and security applications.

</details>

### [Hard-Synth: Synthesizing Diverse Hard Samples for ASR using Zero-Shot TTS and LLM](2411.13159.md)
**Jiawei Yu et.al.** · 2024-11-20

### [I2TTS: Image-indicated Immersive Text-to-speech Synthesis with Spatial Perception](2411.13314.md)
**Jiawei Zhang, Tian-Hao Zhang, Jun Wang, Jiaran Gao et al.** · 2024-11-20

<details>
<summary>Abstract</summary>

Controlling the style and characteristics of speech synthesis is crucial for adapting the output to specific contexts and user requirements. Previous Text-to-speech (TTS) works have focused primarily on the technical aspects of producing natural-sounding speech, such as intonation, rhythm, and clarity. However, they overlook the fact that there is a growing emphasis on spatial perception of synthesized speech, which may provide immersive experience in gaming and virtual reality. To solve this issue, in this paper, we present a novel multi-modal TTS approach, namely Image-indicated Immersive Text-to-speech Synthesis (I2TTS). Specifically, we introduce a scene prompt encoder that integrates visual scene prompts directly into the synthesis pipeline to control the speech generation process. Additionally, we propose a reverberation classification and refinement technique that adjusts the synthesized mel-spectrogram to enhance the immersive experience, ensuring that the involved reverberation condition matches the scene accurately. Experimental results demonstrate that our model achieves high-quality scene and spatial matching without compromising speech naturalness, marking a significant advancement in the field of context-aware speech synthesis. Project demo page: https://spatialTTS.github.io/ Index Terms-Speech synthesis, scene prompt, spatial perception

</details>

### [Rethinking MUSHRA: Addressing Modern Challenges in Text-to-Speech Evaluation](2411.12719.md)
**Praveen Srinivasa Varadhan, Amogh Gulati, Ashwin Sankar, Srija Anand et al.** · 2024-11-19

<details>
<summary>Abstract</summary>

Despite rapid advancements in TTS models, a consistent and robust human evaluation framework is still lacking. For example, MOS tests fail to differentiate between similar models, and CMOS's pairwise comparisons are time-intensive. The MUSHRA test is a promising alternative for evaluating multiple TTS systems simultaneously, but in this work we show that its reliance on matching human reference speech unduly penalises the scores of modern TTS systems that can exceed human speech quality. More specifically, we conduct a comprehensive assessment of the MUSHRA test, focusing on its sensitivity to factors such as rater variability, listener fatigue, and reference bias. Based on our extensive evaluation involving 492 human listeners across Hindi and Tamil we identify two primary shortcomings: (i) reference-matching bias, where raters are unduly influenced by the human reference, and (ii) judgement ambiguity, arising from a lack of clear fine-grained guidelines. To address these issues, we propose two refined variants of the MUSHRA test. The first variant enables fairer ratings for synthesized samples that surpass human reference quality. The second variant reduces ambiguity, as indicated by the relatively lower variance across raters. By combining these approaches, we achieve both more reliable and more fine-grained assessments. We also release MANGO, a massive dataset of 246,000 human ratings, the first-of-its-kind collection for Indian languages, aiding in analyzing human preferences and developing automatic metrics for evaluating TTS systems.

</details>

### [Leveraging Virtual Reality and AI Tutoring for Language Learning: A Case Study of a Virtual Campus Environment with OpenAI GPT Integration with Unity 3D](2411.12619.md)
**Adithya TG, Abhinavaram N, Gowri Srinivasa** · 2024-11-19

<details>
<summary>Abstract</summary>

This paper presents a new approach to multiple language learning, with Hindi the language to be learnt in our case, by using the integration of virtual reality environments and AI enabled tutoring systems using OpenAIs GPT api calls. We have developed a scenario which has a virtual campus environment using Unity which focuses on a detailed representation of our universitys buildings 11th floor, where most of the cultural and technological activities take place. Within this virtual environment that we have created, we have an AI tutor powered by OpenAI's GPT model which was called using an api which moves around with the user. This provided language learning support in Hindi, as GPT is able to take care of language translation. Our approach mainly involves utilising speech to text, text to text conversion and text to speech capabilities to facilitate real time interaction between users and the AI tutor in the presence of internet. This research demonstrates the use of combining VR technology with AI tutoring for immersive language learning experiences and provides interaction.

</details>

### [A Context-Based Numerical Format Prediction for a Text-To-Speech System](2412.00028.md)
**Yaser Darwesh, Lit Wei Wern, Mumtaz Begum Mustafa** · 2024-11-19

<details>
<summary>Abstract</summary>

Many of the existing TTS systems cannot accurately synthesize text containing a variety of numerical formats, resulting in reduced intelligibility of the synthesized speech. This research aims to develop a numerical format classifier that can classify six types of numeric contexts. Experiments were carried out using the proposed context-based feature extraction technique, which is focused on extracting keywords, punctuation marks, and symbols as the features of the numbers. Support Vector Machine, K-Nearest Neighbors Linear Discriminant Analysis, and Decision Tree were used as classifiers. We have used the 10-fold cross-validation technique to determine the classification accuracy in terms of recall and precision. It can be found that the proposed solution is better than the existing feature extraction technique with improvement to the classification accuracy by 30% to 37%. The use of the number format classification can increase the intelligibility of the TTS systems.

</details>

### [A Neural Denoising Vocoder for Clean Waveform Generation from Noisy Mel-Spectrogram based on Amplitude and Phase Predictions](2411.12268.md)
**Hui-Peng Du, Ye-Xin Lu, Yang Ai, Zhen-Hua Ling** · 2024-11-19

<details>
<summary>Abstract</summary>

This paper proposes a novel neural denoising vocoder that can generate clean speech waveforms from noisy mel-spectrograms. The proposed neural denoising vocoder consists of two components, i.e., a spectrum predictor and a enhancement module. The spectrum predictor first predicts the noisy amplitude and phase spectra from the input noisy mel-spectrogram, and subsequently the enhancement module recovers the clean amplitude and phase spectrum from noisy ones. Finally, clean speech waveforms are reconstructed through inverse short-time Fourier transform (iSTFT). All operations are performed at the frame-level spectral domain, with the APNet vocoder and MP-SENet speech enhancement model used as the backbones for the two components, respectively. Experimental results demonstrate that our proposed neural denoising vocoder achieves state-of-the-art performance compared to existing neural vocoders on the VoiceBank+DEMAND dataset. Additionally, despite the lack of phase information and partial amplitude information in the input mel-spectrogram, the proposed neural denoising vocoder still achieves comparable performance with the serveral advanced speech enhancement methods.

</details>

### [ESTVocoder: An Excitation-Spectral-Transformed Neural Vocoder Conditioned on Mel Spectrogram](2411.11258.md)
**Xiao-Hang Jiang et.al.** · 2024-11-18

### [SAMOS: A Neural MOS Prediction Model Leveraging Semantic Representations and Acoustic Features](2411.11232.md)
**Yu-Fei Shi, Yang Ai, Ye-Xin Lu, Hui-Peng Du et al.** · 2024-11-18

<details>
<summary>Abstract</summary>

Assessing the naturalness of speech using mean opinion score (MOS) prediction models has positive implications for the automatic evaluation of speech synthesis systems. Early MOS prediction models took the raw waveform or amplitude spectrum of speech as input, whereas more advanced methods employed self-supervised-learning (SSL) based models to extract semantic representations from speech for MOS prediction. These methods utilized limited aspects of speech information for MOS prediction, resulting in restricted prediction accuracy. Therefore, in this paper, we propose SAMOS, a MOS prediction model that leverages both Semantic and Acoustic information of speech to be assessed. Specifically, the proposed SAMOS leverages a pretrained wav2vec2 to extract semantic representations and uses the feature extractor of a pretrained BiVocoder to extract acoustic features. These two types of features are then fed into the prediction network, which includes multi-task heads and an aggregation layer, to obtain the final MOS score. Experimental results demonstrate that the proposed SAMOS outperforms current state-of-the-art MOS prediction models on the BVCC dataset and performs comparable performance on the BC2019 dataset, according to the results of system-level evaluation metrics.

</details>

### [SmoothCache: A Universal Inference Acceleration Technique for Diffusion Transformers](2411.10510.md)
**Joseph Liu, Joshua Geddes, Ziyu Guo, Haomiao Jiang et al.** · 2024-11-15

<details>
<summary>Abstract</summary>

Diffusion Transformers (DiT) have emerged as powerful generative models for various tasks, including image, video, and speech synthesis. However, their inference process remains computationally expensive due to the repeated evaluation of resource-intensive attention and feed-forward modules. To address this, we introduce SmoothCache, a model-agnostic inference acceleration technique for DiT architectures. SmoothCache leverages the observed high similarity between layer outputs across adjacent diffusion timesteps. By analyzing layer-wise representation errors from a small calibration set, SmoothCache adaptively caches and reuses key features during inference. Our experiments demonstrate that SmoothCache achieves 8% to 71% speed up while maintaining or even improving generation quality across diverse modalities. We showcase its effectiveness on DiT-XL for image generation, Open-Sora for text-to-video, and Stable Audio Open for text-to-audio, highlighting its potential to enable real-time applications and broaden the accessibility of powerful DiT models.

</details>

### [Zero-shot Voice Conversion with Diffusion Transformers](2411.09943.md)
**Songting Liu** · 2024-11-15

<details>
<summary>Abstract</summary>

Zero-shot voice conversion aims to transform a source speech utterance to match the timbre of a reference speech from an unseen speaker. Traditional approaches struggle with timbre leakage, insufficient timbre representation, and mismatches between training and inference tasks. We propose Seed-VC, a novel framework that addresses these issues by introducing an external timbre shifter during training to perturb the source speech timbre, mitigating leakage and aligning training with inference. Additionally, we employ a diffusion transformer that leverages the entire reference speech context, capturing fine-grained timbre features through in-context learning. Experiments demonstrate that Seed-VC outperforms strong baselines like OpenVoice and CosyVoice, achieving higher speaker similarity and lower word error rates in zero-shot voice conversion tasks. We further extend our approach to zero-shot singing voice conversion by incorporating fundamental frequency (F0) conditioning, resulting in comparative performance to current state-of-the-art methods. Our findings highlight the effectiveness of Seed-VC in overcoming core challenges, paving the way for more accurate and versatile voice conversion systems.

</details>

### [Robust AI-Synthesized Speech Detection Using Feature Decomposition Learning and Synthesizer Feature Augmentation](2411.09167.md)
**Kuiyuan Zhang, Zhongyun Hua, Yushu Zhang, Yifang Guo et al.** · 2024-11-14

<details>
<summary>Abstract</summary>

AI-synthesized speech, also known as deepfake speech, has recently raised significant concerns due to the rapid advancement of speech synthesis and speech conversion techniques. Previous works often rely on distinguishing synthesizer artifacts to identify deepfake speech. However, excessive reliance on these specific synthesizer artifacts may result in unsatisfactory performance when addressing speech signals created by unseen synthesizers. In this paper, we propose a robust deepfake speech detection method that employs feature decomposition to learn synthesizer-independent content features as complementary for detection. Specifically, we propose a dual-stream feature decomposition learning strategy that decomposes the learned speech representation using a synthesizer stream and a content stream. The synthesizer stream specializes in learning synthesizer features through supervised training with synthesizer labels. Meanwhile, the content stream focuses on learning synthesizer-independent content features, enabled by a pseudo-labeling-based supervised learning method. This method randomly transforms speech to generate speed and compression labels for training. Additionally, we employ an adversarial learning technique to reduce the synthesizer-related components in the content stream. The final classification is determined by concatenating the synthesizer and content features. To enhance the model's robustness to different synthesizer characteristics, we further propose a synthesizer feature augmentation strategy that randomly blends the characteristic styles within real and fake audio features and randomly shuffles the synthesizer features with the content features. This strategy effectively enhances the feature diversity and simulates more feature combinations.

</details>

### [Improving Grapheme-to-Phoneme Conversion through In-Context Knowledge Retrieval with Large Language Models](2411.07563.md)
**Dongrui Han, Mingyu Cui, Jiawen Kang, Xixin Wu et al.** · 2024-11-12

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion is a crucial step in Text-to-Speech (TTS) systems, responsible for mapping grapheme to corresponding phonetic representations. However, it faces ambiguities problems where the same grapheme can represent multiple phonemes depending on contexts, posing a challenge for G2P conversion. Inspired by the remarkable success of Large Language Models (LLMs) in handling context-aware scenarios, contextual G2P conversion systems with LLMs' in-context knowledge retrieval (ICKR) capabilities are proposed to promote disambiguation capability. The efficacy of incorporating ICKR into G2P conversion systems is demonstrated thoroughly on the Librig2p dataset. In particular, the best contextual G2P conversion system using ICKR outperforms the baseline with weighted average phoneme error rate (PER) reductions of 2.0% absolute (28.9% relative). Using GPT-4 in the ICKR system can increase of 3.5% absolute (3.8% relative) on the Librig2p dataset.

</details>

### [Wavehax: Aliasing-Free Neural Waveform Synthesis Based on 2D Convolution and Harmonic Prior for Reliable Complex Spectrogram Estimation](2411.06807.md)
**Reo Yoneyama, Atsushi Miyashita, Ryuichi Yamamoto, Tomoki Toda** · 2024-11-11

<details>
<summary>Abstract</summary>

Neural vocoders often struggle with aliasing in latent feature spaces, caused by time-domain nonlinear operations and resampling layers. Aliasing folds high-frequency components into the low-frequency range, making aliased and original frequency components indistinguishable and introducing two practical issues. First, aliasing complicates the waveform generation process, as the subsequent layers must address these aliasing effects, increasing the computational complexity. Second, it limits extrapolation performance, particularly in handling high fundamental frequencies, which degrades the perceptual quality of generated speech waveforms. This paper demonstrates that 1) time-domain nonlinear operations inevitably introduce aliasing but provide a strong inductive bias for harmonic generation, and 2) time-frequency-domain processing can achieve aliasing-free waveform synthesis but lacks the inductive bias for effective harmonic generation. Building on this insight, we propose Wavehax, an aliasing-free neural WAVEform generator that integrates 2D convolution and a HArmonic prior for reliable Complex Spectrogram estimation. Experimental results show that Wavehax achieves speech quality comparable to existing high-fidelity neural vocoders and exhibits exceptional robustness in scenarios requiring high fundamental frequency extrapolation, where aliasing effects become typically severe. Moreover, Wavehax requires less than 5% of the multiply-accumulate operations and model parameters compared to HiFi-GAN V1, while achieving over four times faster CPU inference speed.

</details>

### [Debatts: Zero-Shot Debating Text-to-Speech Synthesis](2411.06540.md)
**Yiqiao Huang et.al.** · 2024-11-10

### [Fish-Speech: Leveraging Large Language Models for Advanced Multilingual Text-to-Speech Synthesis](2411.01156.md)
**Shijia Liao et.al.** · 2024-11-09

### [CUIfy the XR: An Open-Source Package to Embed LLM-powered Conversational Agents in XR](2411.04671.md)
**Kadir Burak Buldu, Süleyman Özdel, Ka Hei Carrie Lau, Mengdi Wang et al.** · 2024-11-07

<details>
<summary>Abstract</summary>

Recent developments in computer graphics, machine learning, and sensor technologies enable numerous opportunities for extended reality (XR) setups for everyday life, from skills training to entertainment. With large corporations offering affordable consumer-grade head-mounted displays (HMDs), XR will likely become pervasive, and HMDs will develop as personal devices like smartphones and tablets. However, having intelligent spaces and naturalistic interactions in XR is as important as technological advances so that users grow their engagement in virtual and augmented spaces. To this end, large language model (LLM)--powered non-player characters (NPCs) with speech-to-text (STT) and text-to-speech (TTS) models bring significant advantages over conventional or pre-scripted NPCs for facilitating more natural conversational user interfaces (CUIs) in XR. This paper provides the community with an open-source, customizable, extendable, and privacy-aware Unity package, CUIfy, that facilitates speech-based NPC-user interaction with widely used LLMs, STT, and TTS models. Our package also supports multiple LLM-powered NPCs per environment and minimizes latency between different computational models through streaming to achieve usable interactions between users and NPCs. We publish our source code in the following repository: https://gitlab.lrz.de/hctl/cuify

</details>

### [MOS-Bench: Benchmarking Generalization Abilities of Subjective Speech Quality Assessment Models](2411.03715.md)
**Wen-Chin Huang, Erica Cooper, Tomoki Toda** · 2024-11-06

<details>
<summary>Abstract</summary>

In this paper, we study the task of subjective speech quality assessment (SSQA), which refers to predicting the perceptual quality of speech. Owing to the development of deep neural network models, SSQA has greatly advanced and has been widely applied in scientific papers to evaluate speech generation systems. Nonetheless, the insufficient out-of-domain (OOD) generalization ability of current SSQA models is underexplored and often overlooked by researchers. To study this problem systematically, we present MOS-Bench, a diverse SSQA dataset collection that currently contains 8 training sets and 17 test sets. Through extensive experiments, we first highlight the OOD generalization challenges of existing models. We then evaluate the efficacy of multiple-dataset training, comparing straightforward data pooling against AlignNet, an existing domain-aware method. We demonstrate that pooling multiple training sets provides a simple yet effective solution, and variation in the data is a key factor for robust generalization beyond training data size.

</details>

### [EmoSphere++: Emotion-Controllable Zero-Shot Text-to-Speech via Emotion-Adaptive Spherical Vector](2411.02625.md)
**Deok-Hyeon Cho et.al.** · 2024-11-04

### [Complete reconstruction of the tongue contour through acoustic to articulatory inversion using real-time MRI data](2411.02037.md)
**Sofiane Azzouz, Pierre-André Vuissoz, Yves Laprie** · 2024-11-04

<details>
<summary>Abstract</summary>

Acoustic articulatory inversion is a major processing challenge, with a wide range of applications from speech synthesis to feedback systems for language learning and rehabilitation. In recent years, deep learning methods have been applied to the inversion of less than a dozen geometrical positions corresponding to sensors glued to easily accessible articulators. It is therefore impossible to know the shape of the whole tongue from root to tip. In this work, we use high-quality real-time MRI data to track the contour of the tongue. The data used to drive the inversion are therefore the unstructured speech signal and the tongue contours. Several architectures relying on a Bi-MSTM including or not an autoencoder to reduce the dimensionality of the latent space, using or not the phonetic segmentation have been explored. The results show that the tongue contour can be recovered with a median accuracy of 2.21 mm (or 1.37 pixel) taking a context of 1 MFCC frame (static, delta and double-delta cepstral features).

</details>

### [Align-SLM: Textless Spoken Language Models with Reinforcement Learning from AI Feedback](2411.01834.md)
**Guan-Ting Lin, Prashanth Gurunath Shivakumar, Aditya Gourav, Yile Gu et al.** · 2024-11-04

<details>
<summary>Abstract</summary>

While textless Spoken Language Models (SLMs) have shown potential in end-to-end speech-to-speech modeling, they still lag behind text-based Large Language Models (LLMs) in terms of semantic coherence and relevance. This work introduces the Align-SLM framework, which leverages preference optimization inspired by Reinforcement Learning with AI Feedback (RLAIF) to enhance the semantic understanding of SLMs. Our approach generates multiple speech continuations from a given prompt and uses semantic metrics to create preference data for Direct Preference Optimization (DPO). We evaluate the framework using ZeroSpeech 2021 benchmarks for lexical and syntactic modeling, the spoken version of the StoryCloze dataset for semantic coherence, and other speech generation metrics, including the GPT4-o score and human evaluation. Experimental results show that our method achieves state-of-the-art performance for SLMs on most benchmarks, highlighting the importance of preference optimization to improve the semantics of SLMs.

</details>

### [Refining the evaluation of speech synthesis: A summary of the Blizzard Challenge 2023](s2:25e29eba42591d338fd1d5a96172a25b9996c6a1.md)
**Olivier Perrotin, Brooke Stephenson, Silvain Gerber, Gérard Bailly et al.** · 2024-11-01

<details>
<summary>Abstract</summary>

The Blizzard Challenge has benchmarked progress in Text-to-Speech (TTS) since 2005. The Challenge has seen important milestones passed, with results suggesting that synthetic speech was indistinguishable from natural speech in terms of intelligibility in 2021 and that by that same year it was perhaps even indistinguishable in naturalness. The high quality of synthetic speech generated by the latest TTS systems has thus revealed limitations with ITU-T P.800.1 Mean Opinion Score (MOS) in detecting the remaining differences between synthetic and natural speech. Yet, it was the only method used in previous Challenges and is still the most popular method in the field for speech synthesis evaluation. In the 2023 Challenge, we addressed observed limitations of past Challenges by incorporating state-of-the-art speech synthesis evaluation techniques to refine the evaluation of speech quality, speaker similarity and intelligibility. For speech quality, a relative comparison of the systems receiving the best MOS was able to discover a greater number of significant differences between systems. Regarding speaker similarity, we demonstrated that there is a strong bias depending on whether the listeners are familiar with the target voice or not. As for intelligibility, the evaluation of language-specific phenomena, such as the pronunciation of homographs, better highlighted system limits compared to global transcription tasks of synthesised utterances. In addition to reporting results for the 18 entries to the 2023 Challenge, we extend the results analysis to type of TTS module to provide some insights on the most recent advances in model design. Overall, this year’s results demonstrate the need for a shift towards new methods for refining TTS evaluation to shed light on increasingly smaller and localised differences between synthesised and natural speech.

</details>

### [DC-Spin: A Speaker-invariant Speech Tokenizer for Spoken Language Models](2410.24177.md)
**Heng-Jui Chang, Hongyu Gong, Changhan Wang, James Glass et al.** · 2024-10-31

<details>
<summary>Abstract</summary>

Spoken language models (SLMs) have gained increasing attention with advancements in text-based, decoder-only language models. SLMs process text and speech, enabling simultaneous speech understanding and generation. This paper presents Double-Codebook Speaker-invariant Clustering (DC-Spin), which aims to improve speech tokenization by bridging audio signals and SLM tokens. DC-Spin extracts speaker-invariant tokens rich in phonetic information and resilient to input variations, enhancing zero-shot SLM tasks and speech resynthesis. We propose a chunk-wise approach to enable streamable DC-Spin without retraining and degradation. Comparisons of tokenization methods (self-supervised and neural audio codecs), model scalability, and downstream task proxies show that tokens easily modeled by an n-gram LM or aligned with phonemes offer strong performance, providing insights for designing speech tokenizers for SLMs.

</details>

### [The ISCSLP 2024 Conversational Voice Clone (CoVoC) Challenge: Tasks, Results and Findings](2411.00064.md)
**Kangxiang Xia, Dake Guo, Jixun Yao, Liumeng Xue et al.** · 2024-10-31

<details>
<summary>Abstract</summary>

The ISCSLP 2024 Conversational Voice Clone (CoVoC) Challenge aims to benchmark and advance zero-shot spontaneous style voice cloning, particularly focusing on generating spontaneous behaviors in conversational speech. The challenge comprises two tracks: an unconstrained track without limitation on data and model usage, and a constrained track only allowing the use of constrained open-source datasets. A 100-hour high-quality conversational speech dataset is also made available with the challenge. This paper details the data, tracks, submitted systems, evaluation results, and findings.

</details>

### [The NPU-HWC System for the ISCSLP 2024 Inspirational and Convincing Audio Generation Challenge](2410.23815.md)
**Dake Guo, Jixun Yao, Xinfa Zhu, Kangxiang Xia et al.** · 2024-10-31

<details>
<summary>Abstract</summary>

This paper presents the NPU-HWC system submitted to the ISCSLP 2024 Inspirational and Convincing Audio Generation Challenge 2024 (ICAGC). Our system consists of two modules: a speech generator for Track 1 and a background audio generator for Track 2. In Track 1, we employ Single-Codec to tokenize the speech into discrete tokens and use a language-model-based approach to achieve zero-shot speaking style cloning. The Single-Codec effectively decouples timbre and speaking style at the token level, reducing the acoustic modeling burden on the autoregressive language model. Additionally, we use DSPGAN to upsample 16 kHz mel-spectrograms to high-fidelity 48 kHz waveforms. In Track 2, we propose a background audio generator based on large language models (LLMs). This system produces scene-appropriate accompaniment descriptions, synthesizes background audio with Tango 2, and integrates it with the speech generated by our Track 1 system. Our submission achieves the second place and the first place in Track 1 and Track 2 respectively.

</details>

### [Lina-Speech: Gated Linear Attention is a Fast and Parameter-Efficient Learner for text-to-speech synthesis](2410.23320.md)
**Théodor Lemerle et.al.** · 2024-10-30

### [Very Attentive Tacotron: Robust and Unbounded Length Generalization in Autoregressive Transformer-Based Text-to-Speech](2410.22179.md)
**Eric Battenberg et.al.** · 2024-10-29

### [RDSinger: Reference-based Diffusion Network for Singing Voice Synthesis](2410.21641.md)
**Kehan Sui et.al.** · 2024-10-29

### [Fast and High-Quality Auto-Regressive Speech Synthesis via Speculative Decoding](2410.21951.md)
**Bohan Li, Hankun Wang, Situo Zhang, Yiwei Guo et al.** · 2024-10-29

<details>
<summary>Abstract</summary>

The auto-regressive architecture, like GPTs, is widely used in modern Text-to-Speech (TTS) systems. However, it incurs substantial inference time, particularly due to the challenges in the next-token prediction posed by lengthy sequences of speech tokens. In this work, we introduce VADUSA, one of the first approaches to accelerate auto-regressive TTS through speculative decoding. Our results show that VADUSA not only significantly improves inference speed but also enhances performance by incorporating draft heads to predict future speech content auto-regressively. Furthermore, the inclusion of a tolerance mechanism during sampling accelerates inference without compromising quality. Our approach demonstrates strong generalization across large datasets and various types of speech tokens.

</details>

### [USpeech: Ultrasound-Enhanced Speech with Minimal Human Effort via Cross-Modal Synthesis](2410.22076.md)
**Luca Jiang-Tao Yu, Running Zhao, Sijie Ji, Edith C. H. Ngai et al.** · 2024-10-29

<details>
<summary>Abstract</summary>

Speech enhancement is crucial for ubiquitous human-computer interaction. Recently, ultrasound-based acoustic sensing has emerged as an attractive choice for speech enhancement because of its superior ubiquity and performance. However, due to inevitable interference from unexpected and unintended sources during audio-ultrasound data acquisition, existing solutions rely heavily on human effort for data collection and processing. This leads to significant data scarcity that limits the full potential of ultrasound-based speech enhancement. To address this, we propose USpeech, a cross-modal ultrasound synthesis framework for speech enhancement with minimal human effort. At its core is a two-stage framework that establishes the correspondence between visual and ultrasonic modalities by leveraging audio as a bridge. This approach overcomes challenges from the lack of paired video-ultrasound datasets and the inherent heterogeneity between video and ultrasound data. Our framework incorporates contrastive video-audio pre-training to project modalities into a shared semantic space and employs an audio-ultrasound encoder-decoder for ultrasound synthesis. We then present a speech enhancement network that enhances speech in the time-frequency domain and recovers the clean speech waveform via a neural vocoder. Comprehensive experiments show USpeech achieves remarkable performance using synthetic ultrasound data comparable to physical data, outperforming state-of-the-art ultrasound-based speech enhancement baselines. USpeech is open-sourced at https://github.com/aiot-lab/USpeech/.

</details>

### [A Closer Look at Neural Codec Resynthesis: Bridging the Gap between Codec and Waveform Generation](2410.22448.md)
**Alexander H. Liu, Qirui Wang, Yuan Gong, James Glass** · 2024-10-29

<details>
<summary>Abstract</summary>

Neural Audio Codecs, initially designed as a compression technique, have gained more attention recently for speech generation. Codec models represent each audio frame as a sequence of tokens, i.e., discrete embeddings. The discrete and low-frequency nature of neural codecs introduced a new way to generate speech with token-based models. As these tokens encode information at various levels of granularity, from coarse to fine, most existing works focus on how to better generate the coarse tokens. In this paper, we focus on an equally important but often overlooked question: How can we better resynthesize the waveform from coarse tokens? We point out that both the choice of learning target and resynthesis approach have a dramatic impact on the generated audio quality. Specifically, we study two different strategies based on token prediction and regression, and introduce a new method based on Schrödinger Bridge. We examine how different design choices affect machine and human perception.

</details>

### [End-to-End Neural Formant Synthesis Using Low-Dimensional Acoustic Parameters](s2:beaf19aaf00d49023c9812536f7f05679f3f3226.md)
**Sumiharu Kobayashi, Tetsuo Kosaka, Takashi Nose** · 2024-10-29

<details>
<summary>Abstract</summary>

Neural vocoders can synthesize high-quality speech waveforms from acoustic features, but they cannot control by acoustic parameters, such as F0 and formant frequencies. Although analysis-synthesis based on signal processing can be controlled using acoustic parameters, its speech quality is inferior to that of neural vocoders. This paper proposes End-to-End Neural Formant Synthesis for generating high-quality speech waveforms with controllable acoustic parameters from low-dimensional representations. We compared three models with different structures, and investigated their synthesis quality and controllability. Experimental results showed that the proposed method performed as well as or better than conventional methods in terms of speech quality and controllability.

</details>

### [Enhancing TTS Stability in Hebrew using Discrete Semantic Units](2410.21502.md)
**Ella Zeldes, Or Tal, Yossi Adi** · 2024-10-28

<details>
<summary>Abstract</summary>

This study introduces a refined approach to Text-to-Speech (TTS) generation that significantly enhances sampling stability across languages, with a particular focus on Hebrew. By leveraging discrete semantic units with higher phonetic correlation obtained from a self-supervised model, our method addresses the inherent instability often encountered in TTS systems, especially those dealing with non-diacriticized scripts like Hebrew. Utilizing HuBERT codes, our model generates discrete representations that are optimized for TTS tasks, thereby reducing the dependency on diacritic-based text processing. This advancement not only simplifies the language modeling process but also improves the robustness and shows controllability of the speech output due to disentenglement properties of the semantic units. The inclusion of a speaker embedding in the vocoder further aids in capturing the unique vocal characteristics of the speaker, contributing to the naturalness of the synthesized speech. Our experimental results demonstrate that this approach not only maintains high performance in Hebrew but also shows adaptability to English, underscoring its effectiveness in enhancing stability in TTS systems universally. Our method, named LOTHM (Language of The Hebrew Man), outperforms existing methods in terms of stability while achieving naturalness and speaker similarity on par with previous methods, making it a compelling choice for future speech synthesis applications. Samples can be found in our page pages.cs.huji.ac.il/adiyoss-lab/LoTHM .

</details>

### [UniStyle: Unified Style Modeling for Speaking Style Captioning and Stylistic Speech Synthesis](s2:88c8adb1723322e3500c4eb67c6711a4fbb3097e.md)
**Xinfa Zhu, Wenjie Tian, Xinsheng Wang, Lei He et al.** · 2024-10-28

<details>
<summary>Abstract</summary>

Understanding the speaking style, such as the emotion of the interlocutor's speech, and responding with speech in an appropriate style is a natural occurrence in human conversations. However, technically, existing research on speech synthesis and speaking style captioning typically proceeds independently. In this work, an innovative framework, referred to as UniStyle, is proposed to incorporate both the capabilities of speaking style captioning and style-controllable speech synthesizing. Specifically, UniStyle consists of a UniConnector and a style prompt-based speech generator. The role of the UniConnector is to bridge the gap between different modalities, namely speech audio and text descriptions. It enables the generation of text descriptions with speech as input and the creation of style representations from text descriptions for speech synthesis with the speech generator. Besides, to overcome the issue of data scarcity, we propose a two-stage and semi-supervised training strategy, which reduces data requirements while boosting performance. Extensive experiments conducted on open-source corpora demonstrate that UniStyle achieves state-of-the-art performance in speaking style captioning and synthesizes expressive speech with various speaker timbres and speaking styles in a zero-shot manner.

</details>

### [Get Large Language Models Ready to Speak: A Late-fusion Approach for Speech Generation](2410.20336.md)
**Maohao Shen et.al.** · 2024-10-27

### [STTATTS: Unified Speech-To-Text And Text-To-Speech Model](2410.18607.md)
**Hawau Olamide Toyin et.al.** · 2024-10-24

### [Making Social Platforms Accessible: Emotion-Aware Speech Generation with Integrated Text Analysis](2410.19199.md)
**Suparna De, Ionut Bostan, Nishanth Sastry** · 2024-10-24

<details>
<summary>Abstract</summary>

Recent studies have outlined the accessibility challenges faced by blind or visually impaired, and less-literate people, in interacting with social networks, in-spite of facilitating technologies such as monotone text-to-speech (TTS) screen readers and audio narration of visual elements such as emojis. Emotional speech generation traditionally relies on human input of the expected emotion together with the text to synthesise, with additional challenges around data simplification (causing information loss) and duration inaccuracy, leading to lack of expressive emotional rendering. In real-life communications, the duration of phonemes can vary since the same sentence might be spoken in a variety of ways depending on the speakers' emotional states or accents (referred to as the one-to-many problem of text to speech generation). As a result, an advanced voice synthesis system is required to account for this unpredictability. We propose an end-to-end context-aware Text-to-Speech (TTS) synthesis system that derives the conveyed emotion from text input and synthesises audio that focuses on emotions and speaker features for natural and expressive speech, integrating advanced natural language processing (NLP) and speech synthesis techniques for real-time applications. Our system also showcases competitive inference time performance when benchmarked against the state-of-the-art TTS models, making it suitable for real-time accessibility applications.

</details>

### [Continuous Speech Tokenizer in Text To Speech](2410.17081.md)
**Yixing Li et.al.** · 2024-10-22

### [Continuous Speech Synthesis using per-token Latent Diffusion](2410.16048.md)
**Arnon Turetzky et.al.** · 2024-10-21

### [LSCodec: Low-Bitrate and Speaker-Decoupled Discrete Speech Codec](2410.15764.md)
**Yiwei Guo, Zhihan Li, Chenpeng Du, Hankun Wang et al.** · 2024-10-21

<details>
<summary>Abstract</summary>

Although discrete speech tokens have exhibited strong potential for language model-based speech generation, their high bitrates and redundant timbre information restrict the development of such models. In this work, we propose LSCodec, a discrete speech codec that has both low bitrate and speaker decoupling ability. LSCodec adopts a multi-stage unsupervised training framework with a speaker perturbation technique. A continuous information bottleneck is first established, followed by vector quantization that produces a discrete speaker-decoupled space. A discrete token vocoder finally refines acoustic details from LSCodec. By reconstruction evaluations, LSCodec demonstrates superior intelligibility and audio quality with only a single codebook and smaller vocabulary size than baselines. Voice conversion and speaker probing experiments prove the excellent speaker disentanglement of LSCodec, and ablation study verifies the effectiveness of the proposed training framework.

</details>

### [CycleDiffusion: Voice Conversion Using Cycle-Consistent Diffusion Models](s2:8b8e50a55c34eaa85c8d87d31d93dfaa19b88862.md)
**D. Yook, Geonhee Han, Hyung-Pil Chang, In-Chul Yoo** · 2024-10-21

<details>
<summary>Abstract</summary>

Voice conversion (VC) refers to the technique of modifying one speaker’s voice to mimic another’s while retaining the original linguistic content. This technology finds its applications in fields such as speech synthesis, accent modification, medicine, security, privacy, and entertainment. Among the various deep generative models used for voice conversion, including variational autoencoders (VAEs) and generative adversarial networks (GANs), diffusion models (DMs) have recently gained attention as promising methods due to their training stability and strong performance in data generation. Nevertheless, traditional DMs focus mainly on learning reconstruction paths like VAEs, rather than conversion paths as GANs do, thereby restricting the quality of the converted speech. To overcome this limitation and enhance voice conversion performance, we propose a cycle-consistent diffusion (CycleDiffusion) model, which comprises two DMs: one for converting the source speaker’s voice to the target speaker’s voice and the other for converting it back to the source speaker’s voice. By employing two DMs and enforcing a cycle consistency loss, the CycleDiffusion model effectively learns both reconstruction and conversion paths, producing high-quality converted speech. The effectiveness of the proposed model in voice conversion is validated through experiments using the VCTK (Voice Cloning Toolkit) dataset.

</details>

### [Anonymising Elderly and Pathological Speech: Voice Conversion Using DDSP and Query-by-Example](2410.15500.md)
**Suhita Ghosh, Melanie Jouaiti, Arnab Das, Yamini Sinha et al.** · 2024-10-20

<details>
<summary>Abstract</summary>

Speech anonymisation aims to protect speaker identity by changing personal identifiers in speech while retaining linguistic content. Current methods fail to retain prosody and unique speech patterns found in elderly and pathological speech domains, which is essential for remote health monitoring. To address this gap, we propose a voice conversion-based method (DDSP-QbE) using differentiable digital signal processing and query-by-example. The proposed method, trained with novel losses, aids in disentangling linguistic, prosodic, and domain representations, enabling the model to adapt to uncommon speech patterns. Objective and subjective evaluations show that DDSP-QbE significantly outperforms the voice conversion state-of-the-art concerning intelligibility, prosody, and domain preservation across diverse datasets, pathologies, and speakers while maintaining quality and speaker anonymity. Experts validate domain preservation by analysing twelve clinically pertinent domain attributes.

</details>

### [Improving Voice Quality in Speech Anonymization With Just Perception-Informed Losses](2410.15499.md)
**Suhita Ghosh, Tim Thiele, Frederic Lorbeer, Frank Dreyer et al.** · 2024-10-20

<details>
<summary>Abstract</summary>

The increasing use of cloud-based speech assistants has heightened the need for effective speech anonymization, which aims to obscure a speaker's identity while retaining critical information for subsequent tasks. One approach to achieving this is through voice conversion. While existing methods often emphasize complex architectures and training techniques, our research underscores the importance of loss functions inspired by the human auditory system. Our proposed loss functions are model-agnostic, incorporating handcrafted and deep learning-based features to effectively capture quality representations. Through objective and subjective evaluations, we demonstrate that a VQVAE-based model, enhanced with our perception-driven losses, surpasses the vanilla model in terms of naturalness, intelligibility, and prosody while maintaining speaker anonymity. These improvements are consistently observed across various datasets, languages, target speakers, and genders.

</details>

### [A Unified Framework for Collecting Text-to-Speech Synthesis Datasets for 22 Indian Languages](2410.14197.md)
**Sujitha Sathiyamoorthy et.al.** · 2024-10-18

### [Enhancing Crowdsourced Audio for Text-to-Speech Models](2410.13357.md)
**José Giraldo et.al.** · 2024-10-17

### [DART: Disentanglement of Accent and Speaker Representation in Multispeaker Text-to-Speech](2410.13342.md)
**Jan Melechovsky et.al.** · 2024-10-17

### [DurIAN-E 2: Duration Informed Attention Network with Adaptive Variational Autoencoder and Adversarial Learning for Expressive Text-to-Speech Synthesis](2410.13288.md)
**Yu Gu et.al.** · 2024-10-17

### [Accelerating Codec-based Speech Synthesis with Multi-Token Prediction and Speculative Decoding](2410.13839.md)
**Tan Dat Nguyen, Ji-Hoon Kim, Jeongsoo Choi, Shukjae Choi et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

The goal of this paper is to accelerate codec-based speech synthesis systems with minimum sacrifice to speech quality. We propose an enhanced inference method that allows for flexible trade-offs between speed and quality during inference without requiring additional training. Our core idea is to predict multiple tokens per inference step of the AR module using multiple prediction heads, resulting in a linear reduction in synthesis time as the number of heads increases. Furthermore, we introduce a novel speculative decoding technique that utilises a Viterbi-based algorithm to select the optimal sequence of generated tokens at each decoding step. In our experiments, we demonstrate that the time required to predict each token is reduced by a factor of 4 to 5 compared to baseline models, with minimal quality trade-off or even improvement in terms of speech intelligibility. Audio samples are available at: multpletokensprediction.github.io/multipletokensprediction.github.io/.

</details>

### [Optimal Transport Maps are Good Voice Converters](2411.02402.md)
**Arip Asadulaev, Rostislav Korst, Vitalii Shutov, Alexander Korotin et al.** · 2024-10-17

<details>
<summary>Abstract</summary>

Recently, neural network-based methods for computing optimal transport maps have been effectively applied to style transfer problems. However, the application of these methods to voice conversion is underexplored. In our paper, we fill this gap by investigating optimal transport as a framework for voice conversion. We present a variety of optimal transport algorithms designed for different data representations, such as mel-spectrograms and latent representation of self-supervised speech models. For the mel-spectogram data representation, we achieve strong results in terms of Frechet Audio Distance (FAD). This performance is consistent with our theoretical analysis, which suggests that our method provides an upper bound on the FAD between the target and generated distributions. Within the latent space of the WavLM encoder, we achived state-of-the-art results and outperformed existing methods even with limited reference speaker data.

</details>

### [ERVQ: Enhanced Residual Vector Quantization with Intra-and-Inter-Codebook Optimization for Neural Audio Codecs](2410.12359.md)
**Rui-Chen Zheng et.al.** · 2024-10-16

### [Beyond Oversmoothing: Evaluating DDPM and MSE for Scalable Speech Synthesis in ASR](2410.12279.md)
**Christoph Minixhofer, Ondrej Klejch, Peter Bell** · 2024-10-16

<details>
<summary>Abstract</summary>

Synthetically generated speech has rapidly approached human levels of naturalness. However, the paradox remains that ASR systems, when trained on TTS output that is judged as natural by humans, continue to perform badly on real speech. In this work, we explore whether this phenomenon is due to the oversmoothing behaviour of models commonly used in TTS, with a particular focus on the behaviour of TTS-for-ASR as the amount of TTS training data is scaled up. We systematically compare Denoising Diffusion Probabilistic Models (DDPM) to Mean Squared Error (MSE) based models for TTS, when used for ASR model training. We test the scalability of the two approaches, varying both the number hours, and the number of different speakers. We find that for a given model size, DDPM can make better use of more data, and a more diverse set of speakers, than MSE models. We achieve the best reported ratio between real and synthetic speech WER to date (1.46), but also find that a large gap remains.

</details>

### [SF-Speech: Straightened Flow for Zero-Shot Voice Clone](2410.12399.md)
**Xuyuan Li, Zengqiang Shang, Hua Hua, Peiyang Shi et al.** · 2024-10-16

<details>
<summary>Abstract</summary>

Recently, neural ordinary differential equations (ODE) models trained with flow matching have achieved impressive performance on the zero-shot voice clone task. Nevertheless, postulating standard Gaussian noise as the initial distribution of ODE gives rise to numerous intersections within the fitted targets of flow matching, which presents challenges to model training and enhances the curvature of the learned generated trajectories. These curved trajectories restrict the capacity of ODE models for generating desirable samples with a few steps. This paper proposes SF-Speech, a novel voice clone model based on ODE and in-context learning. Unlike the previous works, SF-Speech adopts a lightweight multi-stage module to generate a more deterministic initial distribution for ODE. Without introducing any additional loss function, we effectively straighten the curved reverse trajectories of the ODE model by jointly training it with the proposed module. Experiment results on datasets of various scales show that SF-Speech outperforms the state-of-the-art zero-shot TTS methods and requires only a quarter of the solver steps, resulting in a generation speed approximately 3.7 times that of Voicebox and E2 TTS. Audio samples are available at the demo page\footnote{[Online] Available: https://lixuyuan102.github.io/Demo/}.

</details>

### [F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching](2410.06885.md)
**Yushen Chen et.al.** · 2024-10-15

### [DMDSpeech: Distilled Diffusion Model Surpassing The Teacher in Zero-shot Speech Synthesis via Direct Metric Optimization](2410.11097.md)
**Yingahao Aaron Li et.al.** · 2024-10-14

### [IsoChronoMeter: A simple and effective isochronic translation evaluation metric](2410.11127.md)
**Nikolai Rozanov, Vikentiy Pankov, Dmitrii Mukhutdinov, Dima Vypirailenko** · 2024-10-14

<details>
<summary>Abstract</summary>

Machine translation (MT) has come a long way and is readily employed in production systems to serve millions of users daily. With the recent advances in generative AI, a new form of translation is becoming possible - video dubbing. This work motivates the importance of isochronic translation, especially in the context of automatic dubbing, and introduces `IsoChronoMeter' (ICM). ICM is a simple yet effective metric to measure isochrony of translations in a scalable and resource-efficient way without the need for gold data, based on state-of-the-art text-to-speech (TTS) duration predictors. We motivate IsoChronoMeter and demonstrate its effectiveness. Using ICM we demonstrate the shortcomings of state-of-the-art translation systems and show the need for new methods. We release the code at this URL: \url{https://github.com/braskai/isochronometer}.

</details>

### [Emphasis Rendering for Conversational Text-to-Speech with Multi-modal Multi-scale Context Modeling](2410.09524.md)
**Rui Liu, Zhenqi Jia, Jie Yang, Yifan Hu et al.** · 2024-10-12

<details>
<summary>Abstract</summary>

Conversational Text-to-Speech (CTTS) aims to accurately express an utterance with the appropriate style within a conversational setting, which attracts more attention nowadays. While recognizing the significance of the CTTS task, prior studies have not thoroughly investigated speech emphasis expression, which is essential for conveying the underlying intention and attitude in human-machine interaction scenarios, due to the scarcity of conversational emphasis datasets and the difficulty in context understanding. In this paper, we propose a novel Emphasis Rendering scheme for the CTTS model, termed ER-CTTS, that includes two main components: 1) we simultaneously take into account textual and acoustic contexts, with both global and local semantic modeling to understand the conversation context comprehensively; 2) we deeply integrate multi-modal and multi-scale context to learn the influence of context on the emphasis expression of the current utterance. Finally, the inferred emphasis feature is fed into the neural speech synthesizer to generate conversational speech. To address data scarcity, we create emphasis intensity annotations on the existing conversational dataset (DailyTalk). Both objective and subjective evaluations suggest that our model outperforms the baseline models in emphasis rendering within a conversational setting. The code and audio samples are available at https://github.com/CodeStoreTTS/ER-CTTS.

</details>

### [Unsupervised Data Validation Methods for Efficient Model Training](2410.07880.md)
**Yurii Paniv** · 2024-10-10

<details>
<summary>Abstract</summary>

This paper investigates the challenges and potential solutions for improving machine learning systems for low-resource languages. State-of-the-art models in natural language processing (NLP), text-to-speech (TTS), speech-to-text (STT), and vision-language models (VLM) rely heavily on large datasets, which are often unavailable for low-resource languages. This research explores key areas such as defining "quality data," developing methods for generating appropriate data and enhancing accessibility to model training. A comprehensive review of current methodologies, including data augmentation, multilingual transfer learning, synthetic data generation, and data selection techniques, highlights both advancements and limitations. Several open research questions are identified, providing a framework for future studies aimed at optimizing data utilization, reducing the required data quantity, and maintaining high-quality model performance. By addressing these challenges, the paper aims to make advanced machine learning models more accessible for low-resource languages, enhancing their utility and impact across various sectors.

</details>

### [Efficient training strategies for natural sounding speech synthesis and speaker adaptation based on FastPitch](2410.06787.md)
**Teodora Răgman et.al.** · 2024-10-09

### [Bahasa Harmony: A Comprehensive Dataset for Bahasa Text-to-Speech Synthesis with Discrete Codec Modeling of EnGen-TTS](2410.06608.md)
**Onkar Kishor Susladkar et.al.** · 2024-10-09

### [Can DeepFake Speech be Reliably Detected?](2410.06572.md)
**Hongbin Liu, Youzheng Chen, Arun Narayanan, Athula Balachandran et al.** · 2024-10-09

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) systems, particularly those with voice cloning capabilities, have made voice impersonation readily accessible, raising ethical and legal concerns due to potential misuse for malicious activities like misinformation campaigns and fraud. While synthetic speech detectors (SSDs) exist to combat this, they are vulnerable to ``test domain shift", exhibiting decreased performance when audio is altered through transcoding, playback, or background noise. This vulnerability is further exacerbated by deliberate manipulation of synthetic speech aimed at deceiving detectors. This work presents the first systematic study of such active malicious attacks against state-of-the-art open-source SSDs. White-box attacks, black-box attacks, and their transferability are studied from both attack effectiveness and stealthiness, using both hardcoded metrics and human ratings. The results highlight the urgent need for more robust detection methods in the face of evolving adversarial threats.

</details>

### [IntrinsicVoice: Empowering LLMs with Intrinsic Real-time Voice Interaction Abilities](2410.08035.md)
**Xin Zhang, Xiang Lyu, Zhihao Du, Qian Chen et al.** · 2024-10-09

<details>
<summary>Abstract</summary>

Current methods of building LLMs with voice interaction capabilities rely heavily on explicit text autoregressive generation before or during speech response generation to maintain content quality, which unfortunately brings computational overhead and increases latency in multi-turn interactions. To address this, we introduce IntrinsicVoic,e an LLM designed with intrinsic real-time voice interaction capabilities. IntrinsicVoice aims to facilitate the transfer of textual capabilities of pre-trained LLMs to the speech modality by mitigating the modality gap between text and speech. Our novelty architecture, GroupFormer, can reduce speech sequences to lengths comparable to text sequences while generating high-quality audio, significantly reducing the length difference between speech and text, speeding up inference, and alleviating long-text modeling issues. Additionally, we construct a multi-turn speech-to-speech dialogue dataset named \method-500k which includes nearly 500k turns of speech-to-speech dialogues, and a cross-modality training strategy to enhance the semantic alignment between speech and text. Experimental results demonstrate that IntrinsicVoice can generate high-quality speech response with latency lower than 100ms in multi-turn dialogue scenarios. Demos are available at https://instrinsicvoice.github.io/.

</details>

### [Sylber: Syllabic Embedding Representation of Speech from Raw Audio](2410.07168.md)
**Cheol Jun Cho, Nicholas Lee, Akshat Gupta, Dhruv Agarwal et al.** · 2024-10-09

<details>
<summary>Abstract</summary>

Syllables are compositional units of spoken language that efficiently structure human speech perception and production. However, current neural speech representations lack such structure, resulting in dense token sequences that are costly to process. To bridge this gap, we propose a new model, Sylber, that produces speech representations with clean and robust syllabic structure. Specifically, we propose a self-supervised learning (SSL) framework that bootstraps syllabic embeddings by distilling from its own initial unsupervised syllabic segmentation. This results in a highly structured representation of speech features, offering three key benefits: 1) a fast, linear-time syllable segmentation algorithm, 2) efficient syllabic tokenization with an average of 4.27 tokens per second, and 3) novel phonological units suited for efficient spoken language modeling. Our proposed segmentation method is highly robust and generalizes to out-of-domain data and unseen languages without any tuning. By training token-to-speech generative models, fully intelligible speech can be reconstructed from Sylber tokens with a significantly lower bitrate than baseline SSL tokens. This suggests that our model effectively compresses speech into a compact sequence of tokens with minimal information loss. Lastly, we demonstrate that categorical perception-a linguistic phenomenon in speech perception-emerges naturally in Sylber, making the embedding space more categorical and sparse than previous speech features and thus supporting the high efficiency of our tokenization. Together, we present a novel SSL approach for representing speech as syllables, with significant potential for efficient speech tokenization and spoken language modeling.

</details>

### [Diffuse or Confuse: A Diffusion Deepfake Speech Dataset](2410.06796.md)
**Anton Firc, Kamil Malinka, Petr Hanáček** · 2024-10-09

<details>
<summary>Abstract</summary>

Advancements in artificial intelligence and machine learning have significantly improved synthetic speech generation. This paper explores diffusion models, a novel method for creating realistic synthetic speech. We create a diffusion dataset using available tools and pretrained models. Additionally, this study assesses the quality of diffusion-generated deepfakes versus non-diffusion ones and their potential threat to current deepfake detection systems. Findings indicate that the detection of diffusion-based deepfakes is generally comparable to non-diffusion deepfakes, with some variability based on detector architecture. Re-vocoding with diffusion vocoders shows minimal impact, and the overall speech quality is comparable to non-diffusion methods.

</details>

### [End-to-end multi-channel speaker extraction and binaural speech synthesis](2410.05739.md)
**Cheng Chi, Xiaoyu Li, Yuxuan Ke, Qunping Ni et al.** · 2024-10-08

<details>
<summary>Abstract</summary>

Speech clarity and spatial audio immersion are the two most critical factors in enhancing remote conferencing experiences. Existing methods are often limited: either due to the lack of spatial information when using only one microphone, or because their performance is highly dependent on the accuracy of direction-of-arrival estimation when using microphone array. To overcome this issue, we introduce an end-to-end deep learning framework that has the capacity of mapping multi-channel noisy and reverberant signals to clean and spatialized binaural speech directly. This framework unifies source extraction, noise suppression, and binaural rendering into one network. In this framework, a novel magnitude-weighted interaural level difference loss function is proposed that aims to improve the accuracy of spatial rendering. Extensive evaluations show that our method outperforms established baselines in terms of both speech quality and spatial fidelity.

</details>

### [Improving Data Augmentation-based Cross-Speaker Style Transfer for TTS with Singing Voice, Style Filtering, and F0 Matching](2410.05620.md)
**Leonardo B. de M. M. Marques, Lucas H. Ueda, Mário U. Neto, Flávio O. Simões et al.** · 2024-10-08

<details>
<summary>Abstract</summary>

The goal of cross-speaker style transfer in TTS is to transfer a speech style from a source speaker with expressive data to a target speaker with only neutral data. In this context, we propose using a pre-trained singing voice conversion (SVC) model to convert the expressive data into the target speaker's voice. In the conversion process, we apply a fundamental frequency (F0) matching technique to mitigate tonal variances between speakers with significant timbral differences. A style classifier filter is proposed to select the most expressive output audios for the TTS training. Our approach is comparable to state-of-the-art with only a few minutes of neutral data from the target speaker, while other methods require hours. A perceptual assessment showed improvements brought by the SVC and the style filter in naturalness and style intensity for the styles that display more vocal effort. Also, increased speaker similarity is obtained with the proposed F0 matching algorithm.

</details>

### [SegINR: Segment-wise Implicit Neural Representation for Sequence Alignment in Neural Text-to-Speech](2410.04690.md)
**Minchan Kim et.al.** · 2024-10-07

### [HALL-E: Hierarchical Neural Codec Language Model for Minute-Long Zero-Shot Text-to-Speech Synthesis](2410.04380.md)
**Yuto Nishimura et.al.** · 2024-10-06

### [Where are we in audio deepfake detection? A systematic analysis over generative and detection models](2410.04324.md)
**Xiang Li, Pin-Yu Chen, Wenqi Wei** · 2024-10-06

<details>
<summary>Abstract</summary>

Recent advances in Text-to-Speech (TTS) and Voice-Conversion (VC) using generative Artificial Intelligence (AI) technology have made it possible to generate high-quality and realistic human-like audio. This poses growing challenges in distinguishing AI-synthesized speech from the genuine human voice and could raise concerns about misuse for impersonation, fraud, spreading misinformation, and scams. However, existing detection methods for AI-synthesized audio have not kept pace and often fail to generalize across diverse datasets. In this paper, we introduce SONAR, a synthetic AI-Audio Detection Framework and Benchmark, aiming to provide a comprehensive evaluation for distinguishing cutting-edge AI-synthesized auditory content. SONAR includes a novel evaluation dataset sourced from 9 diverse audio synthesis platforms, including leading TTS providers and state-of-the-art TTS models. It is the first framework to uniformly benchmark AI-audio detection across both traditional and foundation model-based detection systems. Through extensive experiments, (1) we reveal the limitations of existing detection methods and demonstrate that foundation models exhibit stronger generalization capabilities, likely due to their model size and the scale and quality of pretraining data. (2) Speech foundation models demonstrate robust cross-lingual generalization capabilities, maintaining strong performance across diverse languages despite being fine-tuned solely on English speech data. This finding also suggests that the primary challenges in audio deepfake detection are more closely tied to the realism and quality of synthetic audio rather than language-specific characteristics. (3) We explore the effectiveness and efficiency of few-shot fine-tuning in improving generalization, highlighting its potential for tailored applications, such as personalized detection systems for specific entities or individuals.

</details>

### [LLM Gesticulator: Leveraging Large Language Models for Scalable and Controllable Co-Speech Gesture Synthesis](2410.10851.md)
**Haozhou Pang, Tianwei Ding, Lanshan He, Ming Tao et al.** · 2024-10-06

<details>
<summary>Abstract</summary>

In this work, we present LLM Gesticulator, an LLM-based audio-driven co-speech gesture generation framework that synthesizes full-body animations that are rhythmically aligned with the input audio while exhibiting natural movements and editability. Compared to previous work, our model demonstrates substantial scalability. As the size of the backbone LLM model increases, our framework shows proportional improvements in evaluation metrics (a.k.a. scaling law). Our method also exhibits strong controllability where the content, style of the generated gestures can be controlled by text prompt. To the best of our knowledge, LLM gesticulator is the first work that use LLM on the co-speech generation task. Evaluation with existing objective metrics and user studies indicate that our framework outperforms prior works.

</details>

### [Adversarial Attacks and Robust Defenses in Speaker Embedding based Zero-Shot Text-to-Speech System](2410.04017.md)
**Ze Li et.al.** · 2024-10-05

### [Generative Semantic Communication for Text-to-Speech Synthesis](2410.03459.md)
**Jiahao Zheng et.al.** · 2024-10-04

### [MultiVerse: Efficient and Expressive Zero-Shot Multi-Task Text-to-Speech](2410.03192.md)
**Taejun Bak et.al.** · 2024-10-04

### [Textless Streaming Speech-to-Speech Translation using Semantic Speech Tokens](2410.03298.md)
**Jinzheng Zhao, Niko Moritz, Egor Lakomkin, Ruiming Xie et al.** · 2024-10-04

<details>
<summary>Abstract</summary>

Cascaded speech-to-speech translation systems often suffer from the error accumulation problem and high latency, which is a result of cascaded modules whose inference delays accumulate. In this paper, we propose a transducer-based speech translation model that outputs discrete speech tokens in a low-latency streaming fashion. This approach eliminates the need for generating text output first, followed by machine translation (MT) and text-to-speech (TTS) systems. The produced speech tokens can be directly used to generate a speech signal with low latency by utilizing an acoustic language model (LM) to obtain acoustic tokens and an audio codec model to retrieve the waveform. Experimental results show that the proposed method outperforms other existing approaches and achieves state-of-the-art results for streaming translation in terms of BLEU, average latency, and BLASER 2.0 scores for multiple language pairs using the CVSS-C dataset as a benchmark.

</details>

### [Narrative Player: Reviving Data Narratives with Visuals](2410.03268.md)
**Zekai Shao, Leixian Shen, Haotian Li, Yi Shan et al.** · 2024-10-04

<details>
<summary>Abstract</summary>

Data-rich documents are commonly found across various fields such as business, finance, and science. However, a general limitation of these documents for reading is their reliance on text to convey data and facts. Visual representation of text aids in providing a satisfactory reading experience in comprehension and engagement. However, existing work emphasizes presenting the insights of local text context, rather than fully conveying data stories within the whole paragraphs and engaging readers. To provide readers with satisfactory data stories, this paper presents Narrative Player, a novel method that automatically revives data narratives with consistent and contextualized visuals. Specifically, it accepts a paragraph and corresponding data table as input and leverages LLMs to characterize the clauses and extract contextualized data facts. Subsequently, the facts are transformed into a coherent visualization sequence with a carefully designed optimization-based approach. Animations are also assigned between adjacent visualizations to enable seamless transitions. Finally, the visualization sequence, transition animations, and audio narration generated by text-to-speech technologies are rendered into a data video. The evaluation results showed that the automatic-generated data videos were well-received by participants and experts for enhancing reading.

</details>

### [Diffusion-based Unsupervised Audio-visual Speech Enhancement](2410.05301.md)
**Jean-Eudes Ayilo, Mostafa Sadeghi, Romain Serizel, Xavier Alameda-Pineda** · 2024-10-04

<details>
<summary>Abstract</summary>

This paper proposes a new unsupervised audio-visual speech enhancement (AVSE) approach that combines a diffusion-based audio-visual speech generative model with a non-negative matrix factorization (NMF) noise model. First, the diffusion model is pre-trained on clean speech conditioned on corresponding video data to simulate the speech generative distribution. This pre-trained model is then paired with the NMF-based noise model to estimate clean speech iteratively. Specifically, a diffusion-based posterior sampling approach is implemented within the reverse diffusion process, where after each iteration, a speech estimate is obtained and used to update the noise parameters. Experimental results confirm that the proposed AVSE approach not only outperforms its audio-only counterpart but also generalizes better than a recent supervised-generative AVSE method. Additionally, the new inference algorithm offers a better balance between inference speed and performance compared to the previous diffusion-based method. Code and demo available at: https://jeaneudesayilo.github.io/fast_UdiffSE

</details>

### [Takin-VC: Expressive Zero-Shot Voice Conversion via Adaptive Hybrid Content Encoding and Enhanced Timbre Modeling](2410.01350.md)
**Yuguang Yang, Yu Pan, Jixun Yao, Xiang Zhang et al.** · 2024-10-02

<details>
<summary>Abstract</summary>

Expressive zero-shot voice conversion (VC) is a critical and challenging task that aims to transform the source timbre into an arbitrary unseen speaker while preserving the original content and expressive qualities. Despite recent progress in zero-shot VC, there remains considerable potential for improvements in speaker similarity and speech naturalness. Moreover, existing zero-shot VC systems struggle to fully reproduce paralinguistic information in highly expressive speech, such as breathing, crying, and emotional nuances, limiting their practical applicability. To address these issues, we propose Takin-VC, a novel expressive zero-shot VC framework via adaptive hybrid content encoding and memory-augmented context-aware timbre modeling. Specifically, we introduce an innovative hybrid content encoder that incorporates an adaptive fusion module, capable of effectively integrating quantized features of the pre-trained WavLM and HybridFormer in an implicit manner, so as to extract precise linguistic features while enriching paralinguistic elements. For timbre modeling, we propose advanced memory-augmented and context-aware modules to generate high-quality target timbre features and fused representations that seamlessly align source content with target timbre. To enhance real-time performance, we advocate a conditional flow matching model to reconstruct the Mel-spectrogram of the source speech. Experimental results show that our Takin-VC consistently surpasses state-of-the-art VC systems, achieving notable improvements in terms of speech naturalness, speech expressiveness, and speaker similarity, while offering enhanced inference speed.

</details>

### [Recent Advances in Speech Language Models: A Survey](2410.03751.md)
**Wenqian Cui et.al.** · 2024-10-01

### [Zero-Shot Text-to-Speech from Continuous Text Streams](2410.00767.md)
**Trung Dang et.al.** · 2024-10-01

### [Augmentation through Laundering Attacks for Audio Spoof Detection](2410.01108.md)
**Hashim Ali, Surya Subramani, Hafiz Malik** · 2024-10-01

<details>
<summary>Abstract</summary>

Recent text-to-speech (TTS) developments have made voice cloning (VC) more realistic, affordable, and easily accessible. This has given rise to many potential abuses of this technology, including Joe Biden's New Hampshire deepfake robocall. Several methodologies have been proposed to detect such clones. However, these methodologies have been trained and evaluated on relatively clean databases. Recently, ASVspoof 5 Challenge introduced a new crowd-sourced database of diverse acoustic conditions including various spoofing attacks and codec conditions. This paper is our submission to the ASVspoof 5 Challenge and aims to investigate the performance of Audio Spoof Detection, trained using data augmentation through laundering attacks, on the ASVSpoof 5 database. The results demonstrate that our system performs worst on A18, A19, A20, A26, and A30 spoofing attacks and in the codec and compression conditions of C08, C09, and C10.

</details>

### [EmoKnob: Enhance Voice Cloning with Fine-Grained Emotion Control](2410.00316.md)
**Haozhe Chen, Run Chen, Julia Hirschberg** · 2024-10-01

<details>
<summary>Abstract</summary>

While recent advances in Text-to-Speech (TTS) technology produce natural and expressive speech, they lack the option for users to select emotion and control intensity. We propose EmoKnob, a framework that allows fine-grained emotion control in speech synthesis with few-shot demonstrative samples of arbitrary emotion. Our framework leverages the expressive speaker representation space made possible by recent advances in foundation voice cloning models. Based on the few-shot capability of our emotion control framework, we propose two methods to apply emotion control on emotions described by open-ended text, enabling an intuitive interface for controlling a diverse array of nuanced emotions. To facilitate a more systematic emotional speech synthesis field, we introduce a set of evaluation metrics designed to rigorously assess the faithfulness and recognizability of emotion control frameworks. Through objective and subjective evaluations, we show that our emotion control framework effectively embeds emotions into speech and surpasses emotion expressiveness of commercial TTS services.

</details>

### [Improving curriculum learning for target speaker extraction with synthetic speakers](2410.00811.md)
**Yun Liu, Xuechen Liu, Junichi Yamagishi** · 2024-10-01

<details>
<summary>Abstract</summary>

Target speaker extraction (TSE) aims to isolate individual speaker voices from complex speech environments. The effectiveness of TSE systems is often compromised when the speaker characteristics are similar to each other. Recent research has introduced curriculum learning (CL), in which TSE models are trained incrementally on speech samples of increasing complexity. In CL training, the model is first trained on samples with low speaker similarity between the target and interference speakers, and then on samples with high speaker similarity. To further improve CL, this paper uses a $k$-nearest neighbor-based voice conversion method to simulate and generate speech of diverse interference speakers, and then uses the generated data as part of the CL. Experiments demonstrate that training data based on synthetic speakers can effectively enhance the model's capabilities and significantly improve the performance of multiple TSE systems.

</details>

### [Decoding Hate: Exploring Language Models' Reactions to Hate Speech](2410.00775.md)
**Paloma Piot, Javier Parapar** · 2024-10-01

<details>
<summary>Abstract</summary>

Hate speech is a harmful form of online expression, often manifesting as derogatory posts. It is a significant risk in digital environments. With the rise of Large Language Models (LLMs), there is concern about their potential to replicate hate speech patterns, given their training on vast amounts of unmoderated internet data. Understanding how LLMs respond to hate speech is crucial for their responsible deployment. However, the behaviour of LLMs towards hate speech has been limited compared. This paper investigates the reactions of seven state-of-the-art LLMs (LLaMA 2, Vicuna, LLaMA 3, Mistral, GPT-3.5, GPT-4, and Gemini Pro) to hate speech. Through qualitative analysis, we aim to reveal the spectrum of responses these models produce, highlighting their capacity to handle hate speech inputs. We also discuss strategies to mitigate hate speech generation by LLMs, particularly through fine-tuning and guideline guardrailing. Finally, we explore the models' responses to hate speech framed in politically correct language.

</details>

### [Word-wise intonation model for cross-language TTS systems](2409.20374.md)
**Tomilov A. A. et.al.** · 2024-09-30

### [Accent conversion using discrete units with parallel data synthesized from controllable accented TTS](2410.03734.md)
**Tuan Nam Nguyen, Ngoc Quan Pham, Alexander Waibel** · 2024-09-30

<details>
<summary>Abstract</summary>

The goal of accent conversion (AC) is to convert speech accents while preserving content and speaker identity. Previous methods either required reference utterances during inference, did not preserve speaker identity well, or used one-to-one systems that could only be trained for each non-native accent. This paper presents a promising AC model that can convert many accents into native to overcome these issues. Our approach utilizes discrete units, derived from clustering self-supervised representations of native speech, as an intermediary target for accent conversion. Leveraging multi-speaker text-to-speech synthesis, it transforms these discrete representations back into native speech while retaining the speaker identity. Additionally, we develop an efficient data augmentation method to train the system without demanding a lot of non-native resources. Our system is proved to improve non-native speaker fluency, sound like a native accent, and preserve original speaker identity well.

</details>

### [FluentEditor2: Text-based Speech Editing by Modeling Multi-Scale Acoustic and Prosody Consistency](2410.03719.md)
**Rui Liu, Jiatian Xi, Ziyue Jiang, Haizhou Li** · 2024-09-28

<details>
<summary>Abstract</summary>

Text-based speech editing (TSE) allows users to edit speech by modifying the corresponding text directly without altering the original recording. Current TSE techniques often focus on minimizing discrepancies between generated speech and reference within edited regions during training to achieve fluent TSE performance. However, the generated speech in the edited region should maintain acoustic and prosodic consistency with the unedited region and the original speech at both the local and global levels. To maintain speech fluency, we propose a new fluency speech editing scheme based on our previous \textit{FluentEditor} model, termed \textit{\textbf{FluentEditor2}}, by modeling the multi-scale acoustic and prosody consistency training criterion in TSE training. Specifically, for local acoustic consistency, we propose \textit{hierarchical local acoustic smoothness constraint} to align the acoustic properties of speech frames, phonemes, and words at the boundary between the generated speech in the edited region and the speech in the unedited region. For global prosody consistency, we propose \textit{contrastive global prosody consistency constraint} to keep the speech in the edited region consistent with the prosody of the original utterance. Extensive experiments on the VCTK and LibriTTS datasets show that \textit{FluentEditor2} surpasses existing neural networks-based TSE methods, including Editspeech, Campnet, A$^3$T, FluentSpeech, and our Fluenteditor, in both subjective and objective. Ablation studies further highlight the contributions of each module to the overall effectiveness of the system. Speech demos are available at: \url{https://github.com/Ai-S2-Lab/FluentEditor2}.

</details>

### [Analyzing and Mitigating Inconsistency in Discrete Audio Tokens for Neural Codec Language Models](2409.19283.md)
**Wenrui Liu, Zhifang Guo, Jin Xu, Yuanjun Lv et al.** · 2024-09-28

<details>
<summary>Abstract</summary>

Building upon advancements in Large Language Models (LLMs), the field of audio processing has seen increased interest in training audio generation tasks with discrete audio token sequences. However, directly discretizing audio by neural audio codecs often results in sequences that fundamentally differ from text sequences. Unlike text, where text token sequences are deterministic, discrete audio tokens can exhibit significant variability based on contextual factors, while still producing perceptually identical audio segments. We refer to this phenomenon as \textbf{Discrete Representation Inconsistency (DRI)}. This inconsistency can lead to a single audio segment being represented by multiple divergent sequences, which creates confusion in neural codec language models and results in omissions and repetitions during speech generation. In this paper, we quantitatively analyze the DRI phenomenon within popular audio tokenizers such as EnCodec. Our approach effectively mitigates the DRI phenomenon of the neural audio codec. Furthermore, extensive experiments on the neural codec language model over LibriTTS and large-scale MLS datases (44,000 hours) demonstrate the effectiveness and generality of our method. The demo of audio samples is available online~\footnote{\url{https://consistencyinneuralcodec.github.io}}.

</details>

### [Audio-Based Linguistic Feature Extraction for Enhancing Multi-lingual and Low-Resource Text-to-Speech](2409.18622.md)
**Youngjae Kim, Yejin Jeon, Gary Geunbae Lee** · 2024-09-27

<details>
<summary>Abstract</summary>

The difficulty of acquiring abundant, high-quality data, especially in multi-lingual contexts, has sparked interest in addressing low-resource scenarios. Moreover, current literature rely on fixed expressions from language IDs, which results in the inadequate learning of language representations, and the failure to generate speech in unseen languages. To address these challenges, we propose a novel method that directly extracts linguistic features from audio input while effectively filtering out miscellaneous acoustic information including speaker-specific attributes like timbre. Subjective and objective evaluations affirm the effectiveness of our approach for multi-lingual text-to-speech, and highlight its superiority in low-resource transfer learning for previously unseen language.

</details>

### [Expressive Prompting: Improving Emotion Intensity and Speaker Consistency in Zero-Shot TTS](2409.18512.md)
**Haoyu Wang, Chunyu Qiang, Tianrui Wang, Cheng Gong et al.** · 2024-09-27

<details>
<summary>Abstract</summary>

Recent advancements in speech synthesis have enabled large language model (LLM)-based systems to perform zero-shot generation with controllable content, timbre, speaker identity, and emotion through input prompts. As a result, these models heavily rely on prompt design to guide the generation process. However, existing prompt selection methods often fail to ensure that prompts contain sufficiently stable speaker identity cues and appropriate emotional intensity indicators, which are crucial for expressive speech synthesis. To address this challenge, we propose a two-stage prompt selection strategy specifically designed for expressive speech synthesis. In the static stage (before synthesis), we first evaluate prompt candidates using pitch-based prosodic features, perceptual audio quality, and text-emotion coherence scores evaluated by an LLM. We further assess the candidates under a specific TTS model by measuring character error rate, speaker similarity, and emotional similarity between the synthesized and prompt speech. In the dynamic stage (during synthesis), we use a textual similarity model to select the prompt that is most aligned with the current input text. Experimental results demonstrate that our strategy effectively selects prompt to synthesize speech with both high-intensity emotional expression and robust speaker identity, leading to more expressive and stable zero-shot TTS performance. Audio samples and codes will be available at https://whyrrrrun.github.io/ExpPro.github.io/.

</details>

### [EMOVA: Empowering Language Models to See, Hear and Speak with Vivid Emotions](2409.18042.md)
**Kai Chen, Yunhao Gou, Runhui Huang, Zhili Liu et al.** · 2024-09-26

<details>
<summary>Abstract</summary>

GPT-4o, an omni-modal model that enables vocal conversations with diverse emotions and tones, marks a milestone for omni-modal foundation models. However, empowering Large Language Models to perceive and generate images, texts, and speeches end-to-end with publicly available data remains challenging for the open-source community. Existing vision-language models rely on external tools for speech processing, while speech-language models still suffer from limited or totally without vision-understanding capabilities. To address this gap, we propose the EMOVA (EMotionally Omni-present Voice Assistant), to enable Large Language Models with end-to-end speech abilities while maintaining the leading vision-language performance. With a semantic-acoustic disentangled speech tokenizer, we surprisingly notice that omni-modal alignment can further enhance vision-language and speech abilities compared with the bi-modal aligned counterparts. Moreover, a lightweight style module is introduced for the flexible speech style controls including emotions and pitches. For the first time, EMOVA achieves state-of-the-art performance on both the vision-language and speech benchmarks, and meanwhile, supporting omni-modal spoken dialogue with vivid emotions.

</details>

### [Description-based Controllable Text-to-Speech with Cross-Lingual Voice Control](2409.17452.md)
**Ryuichi Yamamoto, Yuma Shirahata, Masaya Kawamura, Kentaro Tachibana** · 2024-09-26

<details>
<summary>Abstract</summary>

We propose a novel description-based controllable text-to-speech (TTS) method with cross-lingual control capability. To address the lack of audio-description paired data in the target language, we combine a TTS model trained on the target language with a description control model trained on another language, which maps input text descriptions to the conditional features of the TTS model. These two models share disentangled timbre and style representations based on self-supervised learning (SSL), allowing for disentangled voice control, such as controlling speaking styles while retaining the original timbre. Furthermore, because the SSL-based timbre and style representations are language-agnostic, combining the TTS and description control models while sharing the same embedding space effectively enables cross-lingual control of voice characteristics. Experiments on English and Japanese TTS demonstrate that our method achieves high naturalness and controllability for both languages, even though no Japanese audio-description pairs are used.

</details>

### [Exploring synthetic data for cross-speaker style transfer in style representation based TTS](2409.17364.md)
**Lucas H. Ueda et.al.** · 2024-09-25

### [Emotional Dimension Control in Language Model-Based Text-to-Speech: Spanning a Broad Spectrum of Human Emotions](2409.16681.md)
**Kun Zhou et.al.** · 2024-09-25

### [Enabling Auditory Large Language Models for Automatic Speech Quality Evaluation](2409.16644.md)
**Siyin Wang, Wenyi Yu, Yudong Yang, Changli Tang et al.** · 2024-09-25

<details>
<summary>Abstract</summary>

Speech quality assessment typically requires evaluating audio from multiple aspects, such as mean opinion score (MOS) and speaker similarity (SIM) \etc., which can be challenging to cover using one small model designed for a single task. In this paper, we propose leveraging recently introduced auditory large language models (LLMs) for automatic speech quality assessment. By employing task-specific prompts, auditory LLMs are finetuned to predict MOS, SIM and A/B testing results, which are commonly used for evaluating text-to-speech systems. Additionally, the finetuned auditory LLM is able to generate natural language descriptions assessing aspects like noisiness, distortion, discontinuity, and overall quality, providing more interpretable outputs. Extensive experiments have been performed on the NISQA, BVCC, SOMOS and VoxSim speech quality datasets, using open-source auditory LLMs such as SALMONN, Qwen-Audio, and Qwen2-Audio. For the natural language descriptions task, a commercial model Google Gemini 1.5 Pro is also evaluated. The results demonstrate that auditory LLMs achieve competitive performance compared to state-of-the-art task-specific small models in predicting MOS and SIM, while also delivering promising results in A/B testing and natural language descriptions. Our data processing scripts and finetuned model checkpoints can be found at https://github.com/bytedance/SALMONN.

</details>

### [Enhancing Polyglot Voices by Leveraging Cross-Lingual Fine-Tuning in Any-to-One Voice Conversion](2409.17387.md)
**Giuseppe Ruggiero, Matteo Testa, Jurgen Van de Walle, Luigi Di Caro** · 2024-09-25

<details>
<summary>Abstract</summary>

The creation of artificial polyglot voices remains a challenging task, despite considerable progress in recent years. This paper investigates self-supervised learning for voice conversion to create native-sounding polyglot voices. We introduce a novel cross-lingual any-to-one voice conversion system that is able to preserve the source accent without the need for multilingual data from the target speaker. In addition, we show a novel cross-lingual fine-tuning strategy that further improves the accent and reduces the training data requirements. Objective and subjective evaluations with English, Spanish, French and Mandarin Chinese confirm that our approach improves on state-of-the-art methods, enhancing the speech intelligibility and overall quality of the converted speech, especially in cross-lingual scenarios. Audio samples are available at https://giuseppe-ruggiero.github.io/a2o-vc-demo/

</details>

### [Facial Expression-Enhanced TTS: Combining Face Representation and Emotion Intensity for Adaptive Speech](2409.16203.md)
**Yunji Chu et.al.** · 2024-09-24

### [StyleFusion TTS: Multimodal Style-control and Enhanced Feature Fusion for Zero-shot Text-to-speech Synthesis](2409.15741.md)
**Zhiyong Chen et.al.** · 2024-09-24

### [FastTalker: Jointly Generating Speech and Conversational Gestures from Text](2409.16404.md)
**Zixin Guo, Jian Zhang** · 2024-09-24

<details>
<summary>Abstract</summary>

Generating 3D human gestures and speech from a text script is critical for creating realistic talking avatars. One solution is to leverage separate pipelines for text-to-speech (TTS) and speech-to-gesture (STG), but this approach suffers from poor alignment of speech and gestures and slow inference times. In this paper, we introduce FastTalker, an efficient and effective framework that simultaneously generates high-quality speech audio and 3D human gestures at high inference speeds. Our key insight is reusing the intermediate features from speech synthesis for gesture generation, as these features contain more precise rhythmic information than features re-extracted from generated speech. Specifically, 1) we propose an end-to-end framework that concurrently generates speech waveforms and full-body gestures, using intermediate speech features such as pitch, onset, energy, and duration directly for gesture decoding; 2) we redesign the causal network architecture to eliminate dependencies on future inputs for real applications; 3) we employ Reinforcement Learning-based Neural Architecture Search (NAS) to enhance both performance and inference speed by optimizing our network architecture. Experimental results on the BEAT2 dataset demonstrate that FastTalker achieves state-of-the-art performance in both speech synthesis and gesture generation, processing speech and gestures in 0.17 seconds per second on an NVIDIA 3090.

</details>

### [Beyond Text-to-Text: An Overview of Multimodal and Generative Artificial Intelligence for Education Using Topic Modeling](2409.16376.md)
**Ville Heilala, Roberto Araya, Raija Hämäläinen** · 2024-09-24

<details>
<summary>Abstract</summary>

Generative artificial intelligence (GenAI) can reshape education and learning. While large language models (LLMs) like ChatGPT dominate current educational research, multimodal capabilities, such as text-to-speech and text-to-image, are less explored. This study uses topic modeling to map the research landscape of multimodal and generative AI in education. An extensive literature search using Dimensions yielded 4175 articles. Employing a topic modeling approach, latent topics were extracted, resulting in 38 interpretable topics organized into 14 thematic areas. Findings indicate a predominant focus on text-to-text models in educational contexts, with other modalities underexplored, overlooking the broader potential of multimodal approaches. The results suggest a research gap, stressing the importance of more balanced attention across different AI modalities and educational levels. In summary, this research provides an overview of current trends in generative AI for education, underlining opportunities for future exploration of multimodal technologies to fully realize the transformative potential of artificial intelligence in education.

</details>

### [NanoVoice: Efficient Speaker-Adaptive Text-to-Speech for Multiple Speakers](2409.15760.md)
**Nohil Park, Heeseung Kim, Che Hyun Lee, Jooyoung Choi et al.** · 2024-09-24

<details>
<summary>Abstract</summary>

We present NanoVoice, a personalized text-to-speech model that efficiently constructs voice adapters for multiple speakers simultaneously. NanoVoice introduces a batch-wise speaker adaptation technique capable of fine-tuning multiple references in parallel, significantly reducing training time. Beyond building separate adapters for each speaker, we also propose a parameter sharing technique that reduces the number of parameters used for speaker adaptation. By incorporating a novel trainable scale matrix, NanoVoice mitigates potential performance degradation during parameter sharing. NanoVoice achieves performance comparable to the baselines, while training 4 times faster and using 45 percent fewer parameters for speaker adaptation with 40 reference voices. Extensive ablation studies and analysis further validate the efficiency of our model.

</details>

### [VoiceGuider: Enhancing Out-of-Domain Performance in Parameter-Efficient Speaker-Adaptive Text-to-Speech via Autoguidance](2409.15759.md)
**Jiheum Yeom, Heeseung Kim, Jooyoung Choi, Che Hyun Lee et al.** · 2024-09-24

<details>
<summary>Abstract</summary>

When applying parameter-efficient finetuning via LoRA onto speaker adaptive text-to-speech models, adaptation performance may decline compared to full-finetuned counterparts, especially for out-of-domain speakers. Here, we propose VoiceGuider, a parameter-efficient speaker adaptive text-to-speech system reinforced with autoguidance to enhance the speaker adaptation performance, reducing the gap against full-finetuned models. We carefully explore various ways of strengthening autoguidance, ultimately finding the optimal strategy. VoiceGuider as a result shows robust adaptation performance especially on extreme out-of-domain speech data. We provide audible samples in our demo page.

</details>

### [Textless NLP -- Zero Resource Challenge with Low Resource Compute](2409.19015.md)
**Krithiga Ramadass, Abrit Pal Singh, Srihari J, Sheetal Kalyani** · 2024-09-24

<details>
<summary>Abstract</summary>

This work addresses the persistent challenges of substantial training time and GPU resource requirements even when training lightweight encoder-vocoder models for Textless NLP. We reduce training steps significantly while improving performance by a) leveraging learning rate schedulers for efficient and faster convergence b) optimizing hop length and c) tuning the interpolation scale factors for better audio quality. Additionally, we explore the latent space representation for Indian languages such as Tamil and Bengali for the acoustic unit discovery and voice conversion task. Our approach leverages a quantized encoder architecture, in conjunction with a vocoder which utilizes the proposed mixture of optimized hop length, tuned interpolation scale factors and a cyclic learning rate scheduler. We obtain consistently good results across English, Tamil and Bengali datasets. The proposed method excels in capturing complex linguistic patterns, resulting in clear reconstructed audio during voice conversion with significantly reduced training time.

</details>

### [A Comprehensive Survey with Critical Analysis for Deepfake Speech Detection](2409.15180.md)
**Lam Pham, Phat Lam, Dat Tran, Hieu Tang et al.** · 2024-09-23

<details>
<summary>Abstract</summary>

Thanks to advancements in deep learning, speech generation systems now power a variety of real-world applications, such as text-to-speech for individuals with speech disorders, voice chatbots in call centers, cross-linguistic speech translation, etc. While these systems can autonomously generate human-like speech and replicate specific voices, they also pose risks when misused for malicious purposes. This motivates the research community to develop models for detecting synthesized speech (e.g., fake speech) generated by deep-learning-based models, referred to as the Deepfake Speech Detection task. As the Deepfake Speech Detection task has emerged in recent years, there are not many survey papers proposed for this task. Additionally, existing surveys for the Deepfake Speech Detection task tend to summarize techniques used to construct a Deepfake Speech Detection system rather than providing a thorough analysis. This gap motivated us to conduct a comprehensive survey, providing a critical analysis of the challenges and developments in Deepfake Speech Detection. Our survey is innovatively structured, offering an in-depth analysis of current challenge competitions, public datasets, and the deep-learning techniques that provide enhanced solutions to address existing challenges in the field. From our analysis, we propose hypotheses on leveraging and combining specific deep learning techniques to improve the effectiveness of Deepfake Speech Detection systems. Beyond conducting a survey, we perform extensive experiments to validate these hypotheses and propose a highly competitive model for the task of Deepfake Speech Detection. Given the analysis and the experimental results, we finally indicate potential and promising research directions for the Deepfake Speech Detection task.

</details>

### [LlamaPartialSpoof: An LLM-Driven Fake Speech Dataset Simulating Disinformation Generation](2409.14743.md)
**Hieu-Thi Luong, Haoyang Li, Lin Zhang, Kong Aik Lee et al.** · 2024-09-23

<details>
<summary>Abstract</summary>

Previous fake speech datasets were constructed from a defender's perspective to develop countermeasure (CM) systems without considering diverse motivations of attackers. To better align with real-life scenarios, we created LlamaPartialSpoof, a 130-hour dataset that contains both fully and partially fake speech, using a large language model (LLM) and voice cloning technologies to evaluate the robustness of CMs. By examining valuable information for both attackers and defenders, we identify several key vulnerabilities in current CM systems, which can be exploited to enhance attack success rates, including biases toward certain text-to-speech models or concatenation methods. Our experimental results indicate that the current fake speech detection system struggle to generalize to unseen scenarios, achieving a best performance of 24.49% equal error rate.

</details>

### [HiFi-Glot: High-Fidelity Neural Formant Synthesis with Differentiable Resonant Filters](2409.14823.md)
**Yicheng Gu, Pablo Pérez Zarazaga, Chaoren Wang, Zhizheng Wu et al.** · 2024-09-23

<details>
<summary>Abstract</summary>

Formant synthesis aims to generate speech with controllable formant structures, enabling precise control of vocal resonance and phonetic features. However, while existing formant synthesis approaches enable precise formant manipulation, they often yield an impoverished speech signal by failing to capture the complex co-occurring acoustic cues essential for naturalness. To address this issue, this letter presents HiFi-Glot, an end-to-end neural formant synthesis system that achieves both precise formant control and high-fidelity speech synthesis. Specifically, the proposed model adopts a source--filter architecture inspired by classical formant synthesis, where a neural vocoder generates the glottal excitation signal, and differentiable resonant filters model the formants to produce the speech waveform. Experiment results demonstrate that our proposed HiFi-Glot model can generate speech with higher perceptual quality and naturalness while exhibiting a more precise control over formant frequencies, outperforming industry-standard formant manipulation tools such as Praat. Code, checkpoints, and representative audio samples are available at https://www.yichenggu.com/HiFi-Glot/.

</details>

### [Voice Conversion-based Privacy through Adversarial Information Hiding](2409.14919.md)
**Jacob J Webber, Oliver Watts, Gustav Eje Henter, Jennifer Williams et al.** · 2024-09-23

<details>
<summary>Abstract</summary>

Privacy-preserving voice conversion aims to remove only the attributes of speech audio that convey identity information, keeping other speech characteristics intact. This paper presents a mechanism for privacy-preserving voice conversion that allows controlling the leakage of identity-bearing information using adversarial information hiding. This enables a deliberate trade-off between maintaining source-speech characteristics and modification of speaker identity. As such, the approach improves on voice-conversion techniques like CycleGAN and StarGAN, which were not designed for privacy, meaning that converted speech may leak personal information in unpredictable ways. Our approach is also more flexible than ASR-TTS voice conversion pipelines, which by design discard all prosodic information linked to textual content. Evaluations show that the proposed system successfully modifies perceived speaker identity whilst well maintaining source lexical content.

</details>

### [Zero-shot Cross-lingual Voice Transfer for TTS](2409.13910.md)
**Fadi Biadsy et.al.** · 2024-09-20

### [On the Feasibility of Fully AI-automated Vishing Attacks](2409.13793.md)
**João Figueiredo, Afonso Carvalho, Daniel Castro, Daniel Gonçalves et al.** · 2024-09-20

<details>
<summary>Abstract</summary>

A vishing attack is a form of social engineering where attackers use phone calls to deceive individuals into disclosing sensitive information, such as personal data, financial information, or security credentials. Attackers exploit the perceived urgency and authenticity of voice communication to manipulate victims, often posing as legitimate entities like banks or tech support. Vishing is a particularly serious threat as it bypasses security controls designed to protect information. In this work, we study the potential for vishing attacks to escalate with the advent of AI. In theory, AI-powered software bots may have the ability to automate these attacks by initiating conversations with potential victims via phone calls and deceiving them into disclosing sensitive information. To validate this thesis, we introduce ViKing, an AI-powered vishing system developed using publicly available AI technology. It relies on a Large Language Model (LLM) as its core cognitive processor to steer conversations with victims, complemented by a pipeline of speech-to-text and text-to-speech modules that facilitate audio-text conversion in phone calls. Through a controlled social experiment involving 240 participants, we discovered that ViKing has successfully persuaded many participants to reveal sensitive information, even those who had been explicitly warned about the risk of vishing campaigns. Interactions with ViKing's bots were generally considered realistic. From these findings, we conclude that tools like ViKing may already be accessible to potential malicious actors, while also serving as an invaluable resource for cyber awareness programs.

</details>

### [Audio Codec Augmentation for Robust Collaborative Watermarking of Speech Synthesis](2409.13382.md)
**Lauri Juvela, Xin Wang** · 2024-09-20

<details>
<summary>Abstract</summary>

Automatic detection of synthetic speech is becoming increasingly important as current synthesis methods are both near indistinguishable from human speech and widely accessible to the public. Audio watermarking and other active disclosure methods of are attracting research activity, as they can complement traditional deepfake defenses based on passive detection. In both active and passive detection, robustness is of major interest. Traditional audio watermarks are particularly susceptible to removal attacks by audio codec application. Most generated speech and audio content released into the wild passes through an audio codec purely as a distribution method. We recently proposed collaborative watermarking as method for making generated speech more easily detectable over a noisy but differentiable transmission channel. This paper extends the channel augmentation to work with non-differentiable traditional audio codecs and neural audio codecs and evaluates transferability and effect of codec bitrate over various configurations. The results show that collaborative watermarking can be reliably augmented by black-box audio codecs using a waveform-domain straight-through-estimator for gradient approximation. Furthermore, that results show that channel augmentation with a neural audio codec transfers well to traditional codecs. Listening tests demonstrate collaborative watermarking incurs negligible perceptual degradation with high bitrate codecs or DAC at 8kbps.

</details>

### [Preference Alignment Improves Language Model-Based TTS](2409.12403.md)
**Jinchuan Tian et.al.** · 2024-09-19

### [DiffEditor: Enhancing Speech Editing with Semantic Enrichment and Acoustic Consistency](2409.12992.md)
**Yang Chen, Yuhang Jia, Shiwan Zhao, Ziyue Jiang et al.** · 2024-09-19

<details>
<summary>Abstract</summary>

As text-based speech editing becomes increasingly prevalent, the demand for unrestricted free-text editing continues to grow. However, existing speech editing techniques encounter significant challenges, particularly in maintaining intelligibility and acoustic consistency when dealing with out-of-domain (OOD) text. In this paper, we introduce, DiffEditor, a novel speech editing model designed to enhance performance in OOD text scenarios through semantic enrichment and acoustic consistency. To improve the intelligibility of the edited speech, we enrich the semantic information of phoneme embeddings by integrating word embeddings extracted from a pretrained language model. Furthermore, we emphasize that interframe smoothing properties are critical for modeling acoustic consistency, and thus we propose a first-order loss function to promote smoother transitions at editing boundaries and enhance the overall fluency of the edited speech. Experimental results demonstrate that our model achieves state-of-the-art performance in both in-domain and OOD text scenarios.

</details>

### [NDVQ: Robust Neural Audio Codec with Normal Distribution-Based Vector Quantization](2409.12717.md)
**Zhikang Niu, Sanyuan Chen, Long Zhou, Ziyang Ma et al.** · 2024-09-19

<details>
<summary>Abstract</summary>

Built upon vector quantization (VQ), discrete audio codec models have achieved great success in audio compression and auto-regressive audio generation. However, existing models face substantial challenges in perceptual quality and signal distortion, especially when operating in extremely low bandwidth, rooted in the sensitivity of the VQ codebook to noise. This degradation poses significant challenges for several downstream tasks, such as codec-based speech synthesis. To address this issue, we propose a novel VQ method, Normal Distribution-based Vector Quantization (NDVQ), by introducing an explicit margin between the VQ codes via learning a variance. Specifically, our approach involves mapping the waveform to a latent space and quantizing it by selecting the most likely normal distribution, with each codebook entry representing a unique normal distribution defined by its mean and variance. Using these distribution-based VQ codec codes, a decoder reconstructs the input waveform. NDVQ is trained with additional distribution-related losses, alongside reconstruction and discrimination losses. Experiments demonstrate that NDVQ outperforms existing audio compression baselines, such as EnCodec, in terms of audio quality and zero-shot TTS, particularly in very low bandwidth scenarios.

</details>

### [Low Frame-rate Speech Codec: a Codec Designed for Fast High-quality Speech LLM Training and Inference](2409.12117.md)
**Edresson Casanova et.al.** · 2024-09-18

### [Exploring an Inter-Pausal Unit (IPU) based Approach for Indic End-to-End TTS Systems](2409.11915.md)
**Anusha Prakash et.al.** · 2024-09-18

### [Speaking from Coarse to Fine: Improving Neural Codec Language Model via Multi-Scale Speech Coding and Generation](2409.11630.md)
**Haohan Guo et.al.** · 2024-09-18

### [DPI-TTS: Directional Patch Interaction for Fast-Converging and Style Temporal Modeling in Text-to-Speech](2409.11835.md)
**Xin Qi, Ruibo Fu, Zhengqi Wen, Tao Wang et al.** · 2024-09-18

<details>
<summary>Abstract</summary>

In recent years, speech diffusion models have advanced rapidly. Alongside the widely used U-Net architecture, transformer-based models such as the Diffusion Transformer (DiT) have also gained attention. However, current DiT speech models treat Mel spectrograms as general images, which overlooks the specific acoustic properties of speech. To address these limitations, we propose a method called Directional Patch Interaction for Text-to-Speech (DPI-TTS), which builds on DiT and achieves fast training without compromising accuracy. Notably, DPI-TTS employs a low-to-high frequency, frame-by-frame progressive inference approach that aligns more closely with acoustic properties, enhancing the naturalness of the generated speech. Additionally, we introduce a fine-grained style temporal modeling method that further improves speaker style similarity. Experimental results demonstrate that our method increases the training speed by nearly 2 times and significantly outperforms the baseline models.

</details>

### [Takin: A Cohort of Superior Quality Zero-shot Speech Generation Models](2409.12139.md)
**Sijing Chen, Yuan Feng, Laipeng He, Tianwei He et al.** · 2024-09-18

<details>
<summary>Abstract</summary>

With the advent of the big data and large language model era, zero-shot personalized rapid customization has emerged as a significant trend. In this report, we introduce Takin AudioLLM, a series of techniques and models, mainly including Takin TTS, Takin VC, and Takin Morphing, specifically designed for audiobook production. These models are capable of zero-shot speech production, generating high-quality speech that is nearly indistinguishable from real human speech and facilitating individuals to customize the speech content according to their own needs. Specifically, we first introduce Takin TTS, a neural codec language model that builds upon an enhanced neural speech codec and a multi-task training framework, capable of generating high-fidelity natural speech in a zero-shot way. For Takin VC, we advocate an effective content and timbre joint modeling approach to improve the speaker similarity, while advocating for a conditional flow matching based decoder to further enhance its naturalness and expressiveness. Last, we propose the Takin Morphing system with highly decoupled and advanced timbre and prosody modeling approaches, which enables individuals to customize speech production with their preferred timbre and prosody in a precise and controllable manner. Extensive experiments validate the effectiveness and robustness of our Takin AudioLLM series models. For detailed demos, please refer to https://everest-ai.github.io/takinaudiollm/.

</details>

### [SpMis: An Investigation of Synthetic Spoken Misinformation Detection](2409.11308.md)
**Peizhuo Liu, Li Wang, Renqiang He, Haorui He et al.** · 2024-09-17

<details>
<summary>Abstract</summary>

In recent years, speech generation technology has advanced rapidly, fueled by generative models and large-scale training techniques. While these developments have enabled the production of high-quality synthetic speech, they have also raised concerns about the misuse of this technology, particularly for generating synthetic misinformation. Current research primarily focuses on distinguishing machine-generated speech from human-produced speech, but the more urgent challenge is detecting misinformation within spoken content. This task requires a thorough analysis of factors such as speaker identity, topic, and synthesis. To address this need, we conduct an initial investigation into synthetic spoken misinformation detection by introducing an open-source dataset, SpMis. SpMis includes speech synthesized from over 1,000 speakers across five common topics, utilizing state-of-the-art text-to-speech systems. Although our results show promising detection capabilities, they also reveal substantial challenges for practical implementation, underscoring the importance of ongoing research in this critical area.

</details>

### [Kahaani: A Multimodal Co-Creative Storytelling System](2409.11261.md)
**Samee Arif, Muhammad Saad Haroon, Aamina Jamal Khan, Taimoor Arif et al.** · 2024-09-17

<details>
<summary>Abstract</summary>

This paper introduces Kahaani, a multimodal, co-creative storytelling system that leverages Generative Artificial Intelligence, designed for children to address the challenge of sustaining engagement to foster educational narrative experiences. Here we define co-creative as a collaborative creative process in which both the child and Kahaani contribute to the generation of the story. The system combines Large Language Model (LLM), Text-to-Speech (TTS), Text-to-Music (TTM), and Text-to-Video (TTV) generation to produce a rich, immersive, and accessible storytelling experience. The system grounds the co-creation process in two classical storytelling framework, Freytag's Pyramid and Propp's Narrative Functions. The main goals of Kahaani are: (1) to help children improve their English skills, (2) to teach important life lessons through story morals, and (3) to help them understand how stories are structured, all in a fun and engaging way. We present evaluations for each AI component used, along with a user study involving three parent-child pairs to assess the overall experience and educational value of the system.

</details>

### [Discrete Unit based Masking for Improving Disentanglement in Voice Conversion](2409.11560.md)
**Philip H. Lee, Ismail Rasim Ulgen, Berrak Sisman** · 2024-09-17

<details>
<summary>Abstract</summary>

Voice conversion (VC) aims to modify the speaker's identity while preserving the linguistic content. Commonly, VC methods use an encoder-decoder architecture, where disentangling the speaker's identity from linguistic information is crucial. However, the disentanglement approaches used in these methods are limited as the speaker features depend on the phonetic content of the utterance, compromising disentanglement. This dependency is amplified with attention-based methods. To address this, we introduce a novel masking mechanism in the input before speaker encoding, masking certain discrete speech units that correspond highly with phoneme classes. Our work aims to reduce the phonetic dependency of speaker features by restricting access to some phonetic information. Furthermore, since our approach is at the input level, it is applicable to any encoder-decoder based VC framework. Our approach improves disentanglement and conversion performance across multiple VC methods, showing significant effectiveness, particularly in attention-based method, with 44% relative improvement in objective intelligibility.

</details>

### [Leveraging AI-Generated Emotional Self-Voice to Nudge People towards their Ideal Selves](2409.11531.md)
**Cathy Mengying Fang, Phoebe Chua, Samantha Chan, Joanne Leong et al.** · 2024-09-17

<details>
<summary>Abstract</summary>

Emotions, shaped by past experiences, significantly influence decision-making and goal pursuit. Traditional cognitive-behavioral techniques for personal development rely on mental imagery to envision ideal selves, but may be less effective for individuals who struggle with visualization. This paper introduces Emotional Self-Voice (ESV), a novel system combining emotionally expressive language models and voice cloning technologies to render customized responses in the user's own voice. We investigate the potential of ESV to nudge individuals towards their ideal selves in a study with 60 participants. Across all three conditions (ESV, text-only, and mental imagination), we observed an increase in resilience, confidence, motivation, and goal commitment, and the ESV condition was perceived as uniquely engaging and personalized. We discuss the implications of designing generated self-voice systems as a personalized behavioral intervention for different scenarios.

</details>

### [StyleTTS-ZS: Efficient High-Quality Zero-Shot Text-to-Speech Synthesis with Distilled Time-Varying Style Diffusion](2409.10058.md)
**Yinghao Aaron Li et.al.** · 2024-09-16

### [Emo-DPO: Controllable Emotional Speech Synthesis through Direct Preference Optimization](2409.10157.md)
**Xiaoxue Gao, Chen Zhang, Yiming Chen, Huayun Zhang et al.** · 2024-09-16

<details>
<summary>Abstract</summary>

Current emotional text-to-speech (TTS) models predominantly conduct supervised training to learn the conversion from text and desired emotion to its emotional speech, focusing on a single emotion per text-speech pair. These models only learn the correct emotional outputs without fully comprehending other emotion characteristics, which limits their capabilities of capturing the nuances between different emotions. We propose a controllable Emo-DPO approach, which employs direct preference optimization to differentiate subtle emotional nuances between emotions through optimizing towards preferred emotions over less preferred emotional ones. Instead of relying on traditional neural architectures used in existing emotional TTS models, we propose utilizing the emotion-aware LLM-TTS neural architecture to leverage LLMs' in-context learning and instruction-following capabilities. Comprehensive experiments confirm that our proposed method outperforms the existing baselines.

</details>

### [Exploring Prediction Targets in Masked Pre-Training for Speech Foundation Models](2409.10788.md)
**Li-Wei Chen, Takuya Higuchi, Richard He Bai, A. H. Abdelaziz et al.** · 2024-09-16

<details>
<summary>Abstract</summary>

Speech foundation models, such as HuBERT and its variants, are pre-trained on large amounts of unlabeled speech data and then used for a range of downstream tasks. These models use a masked prediction objective, where the model learns to predict information about masked input segments from the unmasked context. The choice of prediction targets in this framework impacts their performance on downstream tasks. For instance, models pre-trained with targets that capture prosody learn representations suited for speaker-related tasks, while those pre-trained with targets that capture phonetics learn representations suited for content-related tasks. Moreover, prediction targets can differ in the level of detail they capture. Models pre-trained with targets that encode fine-grained acoustic features perform better on tasks like denoising, while those pre-trained with targets focused on higher-level abstractions are more effective for content-related tasks. Despite the importance of prediction targets, the design choices that affect them have not been thoroughly studied. This work explores the design choices and their impact on downstream task performance. Our results indicate that the commonly used design choices for HuBERT can be suboptimal. We propose approaches to create more informative prediction targets and demonstrate their effectiveness through improvements across various downstream tasks.

</details>

### [Acquiring Pronunciation Knowledge from Transcribed Speech Audio via Multi-task Learning](2409.09891.md)
**Siqi Sun, Korin Richmond** · 2024-09-15

<details>
<summary>Abstract</summary>

Recent work has shown the feasibility and benefit of bootstrapping an integrated sequence-to-sequence (Seq2Seq) linguistic frontend from a traditional pipeline-based frontend for text-to-speech (TTS). To overcome the fixed lexical coverage of bootstrapping training data, previous work has proposed to leverage easily accessible transcribed speech audio as an additional training source for acquiring novel pronunciation knowledge for uncovered words, which relies on an auxiliary ASR model as part of a cumbersome implementation flow. In this work, we propose an alternative method to leverage transcribed speech audio as an additional training source, based on multi-task learning (MTL). Experiments show that, compared to a baseline Seq2Seq frontend, the proposed MTL-based method reduces PER from 2.5% to 1.6% for those word types covered exclusively in transcribed speech audio, achieving a similar performance to the previous method but with a much simpler implementation flow.

</details>

### [E1 TTS: Simple and Fast Non-Autoregressive TTS](2409.09351.md)
**Zhijun Liu et.al.** · 2024-09-14

### [Improving Robustness of Diffusion-Based Zero-Shot Speech Synthesis via Stable Formant Generation](2409.09311.md)
**Changjin Han et.al.** · 2024-09-14

### [SafeEar: Content Privacy-Preserving Audio Deepfake Detection](2409.09272.md)
**Xinfeng Li, Kai Li, Yifan Zheng, Chen Yan et al.** · 2024-09-14

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) and Voice Conversion (VC) models have exhibited remarkable performance in generating realistic and natural audio. However, their dark side, audio deepfake poses a significant threat to both society and individuals. Existing countermeasures largely focus on determining the genuineness of speech based on complete original audio recordings, which however often contain private content. This oversight may refrain deepfake detection from many applications, particularly in scenarios involving sensitive information like business secrets. In this paper, we propose SafeEar, a novel framework that aims to detect deepfake audios without relying on accessing the speech content within. Our key idea is to devise a neural audio codec into a novel decoupling model that well separates the semantic and acoustic information from audio samples, and only use the acoustic information (e.g., prosody and timbre) for deepfake detection. In this way, no semantic content will be exposed to the detector. To overcome the challenge of identifying diverse deepfake audio without semantic clues, we enhance our deepfake detector with real-world codec augmentation. Extensive experiments conducted on four benchmark datasets demonstrate SafeEar's effectiveness in detecting various deepfake techniques with an equal error rate (EER) down to 2.02%. Simultaneously, it shields five-language speech content from being deciphered by both machine and human auditory analysis, demonstrated by word error rates (WERs) all above 93.93% and our user study. Furthermore, our benchmark constructed for anti-deepfake and anti-content recovery evaluation helps provide a basis for future research in the realms of audio privacy preservation and deepfake detection.

</details>

### [MacST: Multi-Accent Speech Synthesis via Text Transliteration for Accent Conversion](2409.09352.md)
**Sho Inoue, Shuai Wang, Wanxing Wang, Pengcheng Zhu et al.** · 2024-09-14

<details>
<summary>Abstract</summary>

In accented voice conversion or accent conversion, we seek to convert the accent in speech from one another while preserving speaker identity and semantic content. In this study, we formulate a novel method for creating multi-accented speech samples, thus pairs of accented speech samples by the same speaker, through text transliteration for training accent conversion systems. We begin by generating transliterated text with Large Language Models (LLMs), which is then fed into multilingual TTS models to synthesize accented English speech. As a reference system, we built a sequence-to-sequence model on the synthetic parallel corpus for accent conversion. We validated the proposed method for both native and non-native English speakers. Subjective and objective evaluations further validate our dataset's effectiveness in accent conversion studies.

</details>

### [Text-To-Speech Synthesis In The Wild](2409.08711.md)
**Jee-weon Jung, Wangyou Zhang, Soumi Maiti, Yihan Wu et al.** · 2024-09-13

<details>
<summary>Abstract</summary>

Traditional Text-to-Speech (TTS) systems rely on studio-quality speech recorded in controlled settings.a Recently, an effort known as noisy-TTS training has emerged, aiming to utilize in-the-wild data. However, the lack of dedicated datasets has been a significant limitation. We introduce the TTS In the Wild (TITW) dataset, which is publicly available, created through a fully automated pipeline applied to the VoxCeleb1 dataset. It comprises two training sets: TITW-Hard, derived from the transcription, segmentation, and selection of raw VoxCeleb1 data, and TITW-Easy, which incorporates additional enhancement and data selection based on DNSMOS. State-of-the-art TTS models achieve over 3.0 UTMOS score with TITW-Easy, while TITW-Hard remains difficult showing UTMOS below 2.8.

</details>

### [AccentBox: Towards High-Fidelity Zero-Shot Accent Generation](2409.09098.md)
**Jinzuomu Zhong, Korin Richmond, Zhiba Su, Siqi Sun** · 2024-09-13

<details>
<summary>Abstract</summary>

While recent Zero-Shot Text-to-Speech (ZS-TTS) models have achieved high naturalness and speaker similarity, they fall short in accent fidelity and control. To address this issue, we propose zero-shot accent generation that unifies Foreign Accent Conversion (FAC), accented TTS, and ZS-TTS, with a novel two-stage pipeline. In the first stage, we achieve state-of-the-art (SOTA) on Accent Identification (AID) with 0.56 f1 score on unseen speakers. In the second stage, we condition a ZS-TTS system on the pretrained speaker-agnostic accent embeddings extracted by the AID model. The proposed system achieves higher accent fidelity on inherent/cross accent generation, and enables unseen accent generation.

</details>

### [LLM-Powered Grapheme-to-Phoneme Conversion: Benchmark and Case Study](2409.08554.md)
**Mahta Fetrat Qharabagh, Zahra Dehghanian, Hamid R. Rabiee** · 2024-09-13

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion is critical in speech processing, particularly for applications like speech synthesis. G2P systems must possess linguistic understanding and contextual awareness of languages with polyphone words and context-dependent phonemes. Large language models (LLMs) have recently demonstrated significant potential in various language tasks, suggesting that their phonetic knowledge could be leveraged for G2P. In this paper, we evaluate the performance of LLMs in G2P conversion and introduce prompting and post-processing methods that enhance LLM outputs without additional training or labeled data. We also present a benchmarking dataset designed to assess G2P performance on sentence-level phonetic challenges of the Persian language. Our results show that by applying the proposed methods, LLMs can outperform traditional G2P tools, even in an underrepresented language like Persian, highlighting the potential of developing LLM-aided G2P systems.

</details>

### [LHQ-SVC: Lightweight and High Quality Singing Voice Conversion Modeling](2409.08583.md)
**Yubo Huang, Xin Lai, Muyang Ye, Anran Zhu et al.** · 2024-09-13

<details>
<summary>Abstract</summary>

Singing Voice Conversion (SVC) has emerged as a significant subfield of Voice Conversion (VC), enabling the transformation of one singer's voice into another while preserving musical elements such as melody, rhythm, and timbre. Traditional SVC methods have limitations in terms of audio quality, data requirements, and computational complexity. In this paper, we propose LHQ-SVC, a lightweight, CPU-compatible model based on the SVC framework and diffusion model, designed to reduce model size and computational demand without sacrificing performance. We incorporate features to improve inference quality, and optimize for CPU execution by using performance tuning tools and parallel computing frameworks. Our experiments demonstrate that LHQ-SVC maintains competitive performance, with significant improvements in processing speed and efficiency across different devices. The results suggest that LHQ-SVC can meet

</details>

### [DFADD: The Diffusion and Flow-Matching Based Audio Deepfake Dataset](2409.08731.md)
**Jiawei Du, I-Ming Lin, I-Hsiang Chiu, Xuanjun Chen et al.** · 2024-09-13

<details>
<summary>Abstract</summary>

Mainstream zero-shot TTS production systems like Voicebox and Seed-TTS achieve human parity speech by leveraging Flow-matching and Diffusion models, respectively. Unfortunately, human-level audio synthesis leads to identity misuse and information security issues. Currently, many antispoofing models have been developed against deepfake audio. However, the efficacy of current state-of-the-art anti-spoofing models in countering audio synthesized by diffusion and flowmatching based TTS systems remains unknown. In this paper, we proposed the Diffusion and Flow-matching based Audio Deepfake (DFADD) dataset. The DFADD dataset collected the deepfake audio based on advanced diffusion and flowmatching TTS models. Additionally, we reveal that current anti-spoofing models lack sufficient robustness against highly human-like audio generated by diffusion and flow-matching TTS systems. The proposed DFADD dataset addresses this gap and provides a valuable resource for developing more resilient anti-spoofing models.

</details>

### [Super Monotonic Alignment Search](2409.07704.md)
**Junhyeok Lee, Hyeongju Kim** · 2024-09-12

<details>
<summary>Abstract</summary>

Monotonic alignment search (MAS), introduced by Glow-TTS, is one of the most popular algorithm in text-to-speech to estimate unknown alignments between text and speech. Since this algorithm needs to search for the most probable alignment with dynamic programming by caching all possible paths, the time complexity of the algorithm is $O(T \times S)$, where $T$ is the length of text and $S$ is the length of speech representation. The authors of Glow-TTS run this algorithm on CPU, and while they mentioned it is difficult to parallelize, we found that MAS can be parallelized in text length dimension and CPU execution consumes an inordinate amount of time for inter-device copy. Therefore, we implemented a Triton kernel and PyTorch JIT script to accelerate MAS on GPU without inter-device copy. As a result, Super-MAS Triton kernel is up to 72 times faster in the extreme-length case. The code is available at https://github.com/supertone-inc/super-monotonic-align.

</details>

### [Zero-Shot Sing Voice Conversion: built upon clustering-based phoneme representations](2409.08039.md)
**Wangjin Zhou, Fengrun Zhang, Yiming Liu, Wenhao Guan et al.** · 2024-09-12

<details>
<summary>Abstract</summary>

This study presents an innovative Zero-Shot any-to-any Singing Voice Conversion (SVC) method, leveraging a novel clustering-based phoneme representation to effectively separate content, timbre, and singing style. This approach enables precise voice characteristic manipulation. We discovered that datasets with fewer recordings per artist are more susceptible to timbre leakage. Extensive testing on over 10,000 hours of singing and user feedback revealed our model significantly improves sound quality and timbre accuracy, aligning with our objectives and advancing voice conversion technology. Furthermore, this research advances zero-shot SVC and sets the stage for future work on discrete speech representation, emphasizing the preservation of rhyme.

</details>

### [SSR-Speech: Towards Stable, Safe and Robust Zero-shot Text-based Speech Editing and Synthesis](2409.07556.md)
**Helin Wang et.al.** · 2024-09-11

### [Zero-Shot Text-to-Speech as Golden Speech Generator: A Systematic Framework and its Applicability in Automatic Pronunciation Assessment](2409.07151.md)
**Tien-Hong Lo et.al.** · 2024-09-11

### [D-CAPTCHA++: A Study of Resilience of Deepfake CAPTCHA under Transferable Imperceptible Adversarial Attack](2409.07390.md)
**Hong-Hanh Nguyen-Le, Van-Tuan Tran, Dinh-Thuc Nguyen, Nhien-An Le-Khac** · 2024-09-11

<details>
<summary>Abstract</summary>

The advancements in generative AI have enabled the improvement of audio synthesis models, including text-to-speech and voice conversion. This raises concerns about its potential misuse in social manipulation and political interference, as synthetic speech has become indistinguishable from natural human speech. Several speech-generation programs are utilized for malicious purposes, especially impersonating individuals through phone calls. Therefore, detecting fake audio is crucial to maintain social security and safeguard the integrity of information. Recent research has proposed a D-CAPTCHA system based on the challenge-response protocol to differentiate fake phone calls from real ones. In this work, we study the resilience of this system and introduce a more robust version, D-CAPTCHA++, to defend against fake calls. Specifically, we first expose the vulnerability of the D-CAPTCHA system under transferable imperceptible adversarial attack. Secondly, we mitigate such vulnerability by improving the robustness of the system by using adversarial training in D-CAPTCHA deepfake detectors and task classifiers.

</details>

### [Cross-Dialect Text-To-Speech in Pitch-Accent Language Incorporating Multi-Dialect Phoneme-Level BERT](2409.07265.md)
**Kazuki Yamauchi, Yuki Saito, Hiroshi Saruwatari** · 2024-09-11

<details>
<summary>Abstract</summary>

We explore cross-dialect text-to-speech (CD-TTS), a task to synthesize learned speakers' voices in non-native dialects, especially in pitch-accent languages. CD-TTS is important for developing voice agents that naturally communicate with people across regions. We present a novel TTS model comprising three sub-modules to perform competitively at this task. We first train a backbone TTS model to synthesize dialect speech from a text conditioned on phoneme-level accent latent variables (ALVs) extracted from speech by a reference encoder. Then, we train an ALV predictor to predict ALVs tailored to a target dialect from input text leveraging our novel multi-dialect phoneme-level BERT. We conduct multi-dialect TTS experiments and evaluate the effectiveness of our model by comparing it with a baseline derived from conventional dialect TTS methods. The results show that our model improves the dialectal naturalness of synthetic speech in CD-TTS.

</details>

### [The VoiceMOS Challenge 2024: Beyond Speech Quality Prediction](2409.07001.md)
**Wen-Chin Huang, Szu-Wei Fu, Erica Cooper, Ryandhimas E. Zezario et al.** · 2024-09-11

<details>
<summary>Abstract</summary>

We present the third edition of the VoiceMOS Challenge, a scientific initiative designed to advance research into automatic prediction of human speech ratings. There were three tracks. The first track was on predicting the quality of ``zoomed-in'' high-quality samples from speech synthesis systems. The second track was to predict ratings of samples from singing voice synthesis and voice conversion with a large variety of systems, listeners, and languages. The third track was semi-supervised quality prediction for noisy, clean, and enhanced speech, where a very small amount of labeled training data was provided. Among the eight teams from both academia and industry, we found that many were able to outperform the baseline systems. Successful techniques included retrieval-based methods and the use of non-self-supervised representations like spectrograms and pitch histograms. These results showed that the challenge has advanced the field of subjective speech rating prediction.

</details>

### [Enhancing Emotional Text-to-Speech Controllability with Natural Language Guidance through Contrastive Learning and Diffusion Models](2409.06451.md)
**Xin Jing et.al.** · 2024-09-10

### [Disentangling the Prosody and Semantic Information with Pre-trained Model for In-Context Learning based Zero-Shot Voice Conversion](2409.05004.md)
**Zhengyang Chen et.al.** · 2024-09-10

### [LAST: Language Model Aware Speech Tokenization](2409.03701.md)
**Arnon Turetzky et.al.** · 2024-09-10

### [Prosodic Parameter Manipulation in TTS generated speech for Controlled Speech Generation](2409.12176.md)
**Podakanti Satyajith Chary** · 2024-09-10

<details>
<summary>Abstract</summary>

This paper explores the manipulation of prosodic parameters in Text-to-Speech (TTS) systems to achieve controlled speech generation. By leveraging advanced speech processing techniques, we compare TTS-generated audio with human-recorded speech to analyze differences in pitch, duration, and energy. Key features are extracted using tools like PyWorld and Librosa, which are then adjusted to align with the prosodic characteristics of natural human speech. The modified features undergo synthesis, producing enhanced TTS outputs that more closely mirror the natural prosody of human speech. This approach aims to enhance the naturalness and expressiveness of TTS systems by providing a framework for precise prosodic parameter adjustments. Our methodology involves feature extraction, prosodic manipulation, and synthesis, followed by comprehensive evaluations to ensure consistency with human speech patterns. The findings demonstrate the feasibility and effectiveness of prosodic parameter manipulation for controlled speech generation, highlighting its potential to significantly improve TTS applications.

</details>

### [What happens to diffusion model likelihood when your model is conditional?](2409.06364.md)
**Mattias Cross, Anton Ragni** · 2024-09-10

<details>
<summary>Abstract</summary>

Diffusion Models (DMs) iteratively denoise random samples to produce high-quality data. The iterative sampling process is derived from Stochastic Differential Equations (SDEs), allowing a speed-quality trade-off chosen at inference. Another advantage of sampling with differential equations is exact likelihood computation. These likelihoods have been used to rank unconditional DMs and for out-of-domain classification. Despite the many existing and possible uses of DM likelihoods, the distinct properties captured are unknown, especially in conditional contexts such as Text-To-Image (TTI) or Text-To-Speech synthesis (TTS). Surprisingly, we find that TTS DM likelihoods are agnostic to the text input. TTI likelihood is more expressive but cannot discern confounding prompts. Our results show that applying DMs to conditional tasks reveals inconsistencies and strengthens claims that the properties of DM likelihood are unknown. This impact sheds light on the previously unknown nature of DM likelihoods. Although conditional DMs maximise likelihood, the likelihood in question is not as sensitive to the conditioning input as one expects. This investigation provides a new point-of-view on diffusion likelihoods.

</details>

### [VoiceWukong: Benchmarking Deepfake Voice Detection](2409.06348.md)
**Ziwei Yan, Yanjie Zhao, Haoyu Wang** · 2024-09-10

<details>
<summary>Abstract</summary>

With the rapid advancement of technologies like text-to-speech (TTS) and voice conversion (VC), detecting deepfake voices has become increasingly crucial. However, both academia and industry lack a comprehensive and intuitive benchmark for evaluating detectors. Existing datasets are limited in language diversity and lack many manipulations encountered in real-world production environments. To fill this gap, we propose VoiceWukong, a benchmark designed to evaluate the performance of deepfake voice detectors. To build the dataset, we first collected deepfake voices generated by 19 advanced and widely recognized commercial tools and 15 open-source tools. We then created 38 data variants covering six types of manipulations, constructing the evaluation dataset for deepfake voice detection. VoiceWukong thus includes 265,200 English and 148,200 Chinese deepfake voice samples. Using VoiceWukong, we evaluated 12 state-of-the-art detectors. AASIST2 achieved the best equal error rate (EER) of 13.50%, while all others exceeded 20%. Our findings reveal that these detectors face significant challenges in real-world applications, with dramatically declining performance. In addition, we conducted a user study with more than 300 participants. The results are compared with the performance of the 12 detectors and a multimodel large language model (MLLM), i.e., Qwen2-Audio, where different detectors and humans exhibit varying identification capabilities for deepfake voices at different deception levels, while the LALM demonstrates no detection ability at all. Furthermore, we provide a leaderboard for deepfake voice detection, publicly available at {https://voicewukong.github.io}.

</details>

### [Enhancing Kurdish Text-to-Speech with Native Corpus Training: A High-Quality WaveGlow Vocoder Approach](2409.13734.md)
**Abdulhady Abas Abdullah, Sabat Salih Muhamad, Hadi Veisi** · 2024-09-10

<details>
<summary>Abstract</summary>

The ability to synthesize spoken language from text has greatly facilitated access to digital content with the advances in text-to-speech technology. However, effective TTS development for low-resource languages, such as Central Kurdish (CKB), still faces many challenges due mainly to the lack of linguistic information and dedicated resources. In this paper, we improve the Kurdish TTS system based on Tacotron by training the Kurdish WaveGlow vocoder on a 21-hour central Kurdish speech corpus instead of using a pre-trained English vocoder WaveGlow. Vocoder training on the target language corpus is required to accurately and fluently adapt phonetic and prosodic changes in Kurdish language. The effectiveness of these enhancements is that our model is significantly better than the baseline system with English pretrained models. In particular, our adaptive WaveGlow model achieves an impressive MOS of 4.91, which sets a new benchmark for Kurdish speech synthesis. On one hand, this study empowers the advanced features of the TTS system for Central Kurdish, and on the other hand, it opens the doors for other dialects in Kurdish and other related languages to further develop.

</details>

### [InstructSing: High-Fidelity Singing Voice Generation via Instructing Yourself](2409.06330.md)
**Chang Zeng, Chunhui Wang, Xiaoxiao Miao, Jian Zhao et al.** · 2024-09-10

<details>
<summary>Abstract</summary>

It is challenging to accelerate the training process while ensuring both high-quality generated voices and acceptable inference speed. In this paper, we propose a novel neural vocoder called InstructSing, which can converge much faster compared with other neural vocoders while maintaining good performance by integrating differentiable digital signal processing and adversarial training. It includes one generator and two discriminators. Specifically, the generator incorporates a harmonic-plus-noise (HN) module to produce 8kHz audio as an instructive signal. Subsequently, the HN module is connected with an extended WaveNet by an UNet-based module, which transforms the output of the HN module to a latent variable sequence containing essential periodic and aperiodic information. In addition to the latent sequence, the extended WaveNet also takes the mel-spectrogram as input to generate 48kHz high-fidelity singing voices. In terms of discriminators, we combine a multi-period discriminator, as originally proposed in HiFiGAN, with a multi-resolution multi-band STFT discriminator. Notably, InstructSing achieves comparable voice quality to other neural vocoders but with only one-tenth of the training steps on a 4 NVIDIA V100 GPU machine\footnote{{Demo page: \href{https://wavelandspeech.github.io/instructsing/}{\texttt{https://wavelandspeech.github.io/inst\\ructsing/}}}}. We plan to open-source our code and pretrained model once the paper get accepted.

</details>

### [RobustSVC: HuBERT-based Melody Extractor and Adversarial Learning for Robust Singing Voice Conversion](2409.06237.md)
**Wei Chen, Xintao Zhao, Jun Chen, Binzhu Sha et al.** · 2024-09-10

<details>
<summary>Abstract</summary>

Singing voice conversion (SVC) is hindered by noise sensitivity due to the use of non-robust methods for extracting pitch and energy during the inference. As clean signals are key for the source audio in SVC, music source separation preprocessing offers a viable solution for handling noisy audio, like singing with background music (BGM). However, current separating methods struggle to fully remove noise or excessively suppress signal components, affecting the naturalness and similarity of the processed audio. To tackle this, our study introduces RobustSVC, a novel any-to-one SVC framework that converts noisy vocals into clean vocals sung by the target singer. We replace the non-robust feature with a HuBERT-based melody extractor and use adversarial training mechanisms with three discriminators to reduce information leakage in self-supervised representations. Experimental results show that RobustSVC is noise-robust and achieves higher similarity and naturalness than baseline methods in both noisy and clean vocal conditions.

</details>

### [VC-ENHANCE: Speech Restoration with Integrated Noise Suppression and Voice Conversion](2409.06126.md)
**Kyungguen Byun, Jason Filos, Erik Visser, Sunkuk Moon** · 2024-09-10

<details>
<summary>Abstract</summary>

Noise suppression (NS) algorithms are effective in improving speech quality in many cases. However, aggressive noise suppression can damage the target speech, reducing both speech intelligibility and quality despite removing the noise. This study proposes an explicit speech restoration method using a voice conversion (VC) technique for restoration after noise suppression. We observed that high-quality speech can be restored through a diffusion-based voice conversion stage, conditioned on the target speaker embedding and speech content information extracted from the de-noised speech. This speech restoration can achieve enhancement effects such as bandwidth extension, de-reverberation, and in-painting. Our experimental results demonstrate that this two-stage NS+VC framework outperforms single-stage enhancement models in terms of output speech quality, as measured by objective metrics, while scoring slightly lower in speech intelligibility. To further improve the intelligibility of the combined system, we propose a content encoder adaptation method for robust content extraction in noisy conditions.

</details>

### [IndicVoices-R: Unlocking a Massive Multilingual Multi-speaker Speech Corpus for Scaling Indian TTS](2409.05356.md)
**Ashwin Sankar et.al.** · 2024-09-09

### [AS-Speech: Adaptive Style For Speech Synthesis](2409.05730.md)
**Zhipeng Li, Xiaofen Xing, Jun Wang, Shuaiqi Chen et al.** · 2024-09-09

<details>
<summary>Abstract</summary>

In recent years, there has been significant progress in Text-to-Speech (TTS) synthesis technology, enabling the high-quality synthesis of voices in common scenarios. In unseen situations, adaptive TTS requires a strong generalization capability to speaker style characteristics. However, the existing adaptive methods can only extract and integrate coarse-grained timbre or mixed rhythm attributes separately. In this paper, we propose AS-Speech, an adaptive style methodology that integrates the speaker timbre characteristics and rhythmic attributes into a unified framework for text-to-speech synthesis. Specifically, AS-Speech can accurately simulate style characteristics through fine-grained text-based timbre features and global rhythm information, and achieve high-fidelity speech synthesis through the diffusion model. Experiments show that the proposed model produces voices with higher naturalness and similarity in terms of timbre and rhythm compared to a series of adaptive TTS models.

</details>

### [Estimating the Completeness of Discrete Speech Units](2409.06109.md)
**Sung-Lin Yeh, Hao Tang** · 2024-09-09

<details>
<summary>Abstract</summary>

Representing speech with discrete units has been widely used in speech codec and speech generation. However, there are several unverified claims about self-supervised discrete units, such as disentangling phonetic and speaker information with k-means, or assuming information loss after k-means. In this work, we take an information-theoretic perspective to answer how much information is present (information completeness) and how much information is accessible (information accessibility), before and after residual vector quantization. We show a lower bound for information completeness and estimate completeness on discretized HuBERT representations after residual vector quantization. We find that speaker information is sufficiently present in HuBERT discrete units, and that phonetic information is sufficiently present in the residual, showing that vector quantization does not achieve disentanglement. Our results offer a comprehensive assessment on the choice of discrete units, and suggest that a lot more information in the residual should be mined rather than discarded.

</details>

### [Investigating Neural Audio Codecs for Speech Language Model-Based Speech Generation](2409.04016.md)
**Jiaqi Li, Dongmei Wang, Xiaofei Wang, Yao Qian et al.** · 2024-09-06

<details>
<summary>Abstract</summary>

Neural audio codec tokens serve as the fundamental building blocks for speech language model (SLM)-based speech generation. However, there is no systematic understanding on how the codec system affects the speech generation performance of the SLM. In this work, we examine codec tokens within SLM framework for speech generation to provide insights for effective codec design. We retrain existing high-performing neural codec models on the same data set and loss functions to compare their performance in a uniform setting. We integrate codec tokens into two SLM systems: masked-based parallel speech generation system and an auto-regressive (AR) plus non-auto-regressive (NAR) model-based system. Our findings indicate that better speech reconstruction in codec systems does not guarantee improved speech generation in SLM. A high-quality codec decoder is crucial for natural speech production in SLM, while speech intelligibility depends more on quantization mechanism.

</details>

### [Comparing Speech Anonymization Efficacy by Voice Conversion Using KNN and Disentangled Speaker Feature Representations](s2:61dc74229ccbeb4a0b97ba058b2cc710f470f6e6.md)
**Arnab Das, Carlos Franzreb, Tim Herzig, Philipp Pirlet et al.** · 2024-09-06

<details>
<summary>Abstract</summary>

The growing use of speech-based cloud devices and services has heightened the risk of identity theft and misuse of personal information. Speech anonymization techniques help exercise our right to privacy and shield us from falling prey to such malprac-tices. In this paper, we propose three speech anonymization systems to be submitted to the Voice Privacy Challenge 2024 and describe them in detail. Voice anonymization systems often lack utility for downstream applications, resulting in issues like poor emotion preservation or low intelligibility. This has led to research focused on balancing the privacy-utility trade-off. We propose two methods, that use the KNN-based voice conversion (VC) system as a core anonymization method and show improved intelligibility and emotion preservation. We also propose to employ a vector quantized mutual information-based VC system that learns to distinguish between speaker and content features and alters speaker information during inference time to achieve speaker anonymity. We evaluate these two types of voice conversion systems within the framework of speaker anonymization and analyze the utility-privacy trade-off achieved by each system.

</details>

### [FireRedTTS: A Foundation Text-To-Speech Framework for Industry-Level Generative Speech Applications](2409.03283.md)
**Hao-Han Guo et.al.** · 2024-09-05

### [ZSDEVC: Zero-Shot Diffusion-based Emotional Voice Conversion with Disentangled Mechanism](2409.03636.md)
**Hsing-Hang Chou, Yun-Shao Lin, Ching-Chin Sung, Yu Tsao et al.** · 2024-09-05

<details>
<summary>Abstract</summary>

The human voice conveys not just words but also emotional states and individuality. Emotional voice conversion (EVC) modifies emotional expressions while preserving linguistic content and speaker identity, improving applications like human-machine interaction. While deep learning has advanced EVC models for specific target speakers on well-crafted emotional datasets, existing methods often face issues with emotion accuracy and speech distortion. In addition, the zero-shot scenario, in which emotion conversion is applied to unseen speakers, remains underexplored. This work introduces a novel diffusion framework with disentangled mechanisms and expressive guidance, trained on a large emotional speech dataset and evaluated on unseen speakers across in-domain and out-of-domain datasets. Experimental results show that our method produces expressive speech with high emotional accuracy, naturalness, and quality, showcasing its potential for broader EVC applications.

</details>

### [Speaker and Style Disentanglement of Speech Based on Contrastive Predictive Coding Supported Factorized Variational Autoencoder](2409.03520.md)
**Yuying Xie, Michael Kuhlmann, Frederik Rautenberg, Zheng-Hua Tan et al.** · 2024-09-05

<details>
<summary>Abstract</summary>

Speech signals encompass various information across multiple levels including content, speaker, and style. Disentanglement of these information, although challenging, is important for applications such as voice conversion. The contrastive predictive coding supported factorized variational autoencoder achieves unsupervised disentanglement of a speech signal into speaker and content embeddings by assuming speaker info to be temporally more stable than content-induced variations. However, this assumption may introduce other temporal stable information into the speaker embeddings, like environment or emotion, which we call style. In this work, we propose a method to further disentangle non-content features into distinct speaker and style features, notably by leveraging readily accessible and well-defined speaker labels without the necessity for style labels. Experimental results validate the proposed method's effectiveness on extracting disentangled features, thereby facilitating speaker, style, or combined speaker-style conversion.

</details>

### [Training Universal Vocoders with Feature Smoothing-Based Augmentation Methods for High-Quality TTS Systems](2409.02517.md)
**Jeongmin Liu et.al.** · 2024-09-04

### [Fast, High-Quality and Parameter-Efficient Articulatory Synthesis using Differentiable DSP](2409.02451.md)
**Yisi Liu, Bohan Yu, Drake Lin, Peter Wu et al.** · 2024-09-04

<details>
<summary>Abstract</summary>

Articulatory trajectories like electromagnetic articulography (EMA) provide a low-dimensional representation of the vocal tract filter and have been used as natural, grounded features for speech synthesis. Differentiable digital signal processing (DDSP) is a parameter-efficient framework for audio synthesis. Therefore, integrating low-dimensional EMA features with DDSP can significantly enhance the computational efficiency of speech synthesis. In this paper, we propose a fast, high-quality, and parameter-efficient DDSP articulatory vocoder that can synthesize speech from EMA, F0, and loudness. We incorporate several techniques to solve the harmonics / noise imbalance problem, and add a multi-resolution adversarial loss for better synthesis quality. Our model achieves a transcription word error rate (WER) of 6.67% and a mean opinion score (MOS) of 3.74, with an improvement of 1.63% and 0.16 compared to the state-of-the-art (SOTA) baseline. Our DDSP vocoder is 4.9x faster than the baseline on CPU during inference, and can generate speech of comparable quality with only 0.4M parameters, in contrast to the 9M parameters required by the SOTA.

</details>

### [vec2wav 2.0: Advancing Voice Conversion via Discrete Token Vocoders](2409.01995.md)
**Yiwei Guo, Zhihan Li, Junjie Li, Chenpeng Du et al.** · 2024-09-03

<details>
<summary>Abstract</summary>

We propose a new speech discrete token vocoder, vec2wav 2.0, which advances voice conversion (VC). We use discrete tokens from speech self-supervised models as the content features of source speech, and treat VC as a prompted vocoding task. To amend the loss of speaker timbre in the content tokens, vec2wav 2.0 utilizes the WavLM features to provide strong timbre-dependent information. A novel adaptive Snake activation function is proposed to better incorporate timbre into the waveform reconstruction process. In this way, vec2wav 2.0 learns to alter the speaker timbre appropriately given different reference prompts. Also, no supervised data is required for vec2wav 2.0 to be effectively trained. Experimental results demonstrate that vec2wav 2.0 outperforms all other baselines to a considerable margin in terms of audio quality and speaker similarity in any-to-any VC. Ablation studies verify the effects made by the proposed techniques. Moreover, vec2wav 2.0 achieves competitive cross-lingual VC even only trained on monolingual corpus. Thus, vec2wav 2.0 shows timbre can potentially be manipulated only by speech token vocoders, pushing the frontiers of VC and speech synthesis.

</details>

### [FastVoiceGrad: One-step Diffusion-Based Voice Conversion with Adversarial Conditional Diffusion Distillation](2409.02245.md)
**Takuhiro Kaneko, Hirokazu Kameoka, Kou Tanaka, Yuto Kondo** · 2024-09-03

<details>
<summary>Abstract</summary>

Diffusion-based voice conversion (VC) techniques such as VoiceGrad have attracted interest because of their high VC performance in terms of speech quality and speaker similarity. However, a notable limitation is the slow inference caused by the multi-step reverse diffusion. Therefore, we propose FastVoiceGrad, a novel one-step diffusion-based VC that reduces the number of iterations from dozens to one while inheriting the high VC performance of the multi-step diffusion-based VC. We obtain the model using adversarial conditional diffusion distillation (ACDD), leveraging the ability of generative adversarial networks and diffusion models while reconsidering the initial states in sampling. Evaluations of one-shot any-to-any VC demonstrate that FastVoiceGrad achieves VC performance superior to or comparable to that of previous multi-step diffusion-based VC while enhancing the inference speed. Audio samples are available at https://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/fastvoicegrad/.

</details>

### [Pureformer-VC: Non-parallel One-Shot Voice Conversion with Pure Transformer Blocks and Triplet Discriminative Training](2409.01668.md)
**Wenhan Yao, Zedong Xing, Xiarun Chen, Jia Liu et al.** · 2024-09-03

<details>
<summary>Abstract</summary>

One-shot voice conversion(VC) aims to change the timbre of any source speech to match that of the target speaker with only one speech sample. Existing style transfer-based VC methods relied on speech representation disentanglement and suffered from accurately and independently encoding each speech component and recomposing back to converted speech effectively. To tackle this, we proposed Pureformer-VC, which utilizes Conformer blocks to build a disentangled encoder, and Zipformer blocks to build a style transfer decoder as the generator. In the decoder, we used effective styleformer blocks to integrate speaker characteristics effectively into the generated speech. The models used the generative VAE loss for encoding components and triplet loss for unsupervised discriminative training. We applied the styleformer method to Zipformer's shared weights for style transfer. The experimental results show that the proposed model achieves comparable subjective scores and exhibits improvements in objective metrics compared to existing methods in a one-shot voice conversion scenario.

</details>

### [A multilingual training strategy for low resource Text to Speech](2409.01217.md)
**Asma Amalas et.al.** · 2024-09-02

### [SoCodec: A Semantic-Ordered Multi-Stream Speech Codec for Efficient Language Model Based Text-to-Speech Synthesis](2409.00933.md)
**Haohan Guo et.al.** · 2024-09-02

### [Sample-Efficient Diffusion for Text-To-Speech Synthesis](2409.03717.md)
**Justin Lovelace et.al.** · 2024-09-01

### [MaskGCT: Zero-Shot Text-to-Speech with Masked Generative Codec Transformer](2409.00750.md)
**Yuancheng Wang et.al.** · 2024-09-01

### [Seeing Your Speech Style: A Novel Zero-Shot Identity-Disentanglement Face-based Voice Conversion](2409.00700.md)
**Yan Rong, Li Liu** · 2024-09-01

<details>
<summary>Abstract</summary>

Face-based Voice Conversion (FVC) is a novel task that leverages facial images to generate the target speaker's voice style. Previous work has two shortcomings: (1) suffering from obtaining facial embeddings that are well-aligned with the speaker's voice identity information, and (2) inadequacy in decoupling content and speaker identity information from the audio input. To address these issues, we present a novel FVC method, Identity-Disentanglement Face-based Voice Conversion (ID-FaceVC), which overcomes the above two limitations. More precisely, we propose an Identity-Aware Query-based Contrastive Learning (IAQ-CL) module to extract speaker-specific facial features, and a Mutual Information-based Dual Decoupling (MIDD) module to purify content features from audio, ensuring clear and high-quality voice conversion. Besides, unlike prior works, our method can accept either audio or text inputs, offering controllable speech generation with adjustable emotional tone and speed. Extensive experiments demonstrate that ID-FaceVC achieves state-of-the-art performance across various metrics, with qualitative and user study results confirming its effectiveness in naturalness, similarity, and diversity. Project website with audio samples and code can be found at https://id-facevc.github.io.

</details>

### [Unsupervised Domain Adaptation for Speech Emotion Recognition using K-Nearest Neighbors Voice Conversion](s2:216e1a1b1a85986b531c60ba40c84faf00c63b61.md)
**Pravin Mote, Berrak Sisman, Carlos Busso** · 2024-09-01

<details>
<summary>Abstract</summary>

Abundant speech data for speech emotion recognition (SER) is often unlabeled, rendering it ineffective for model training. Models trained on existing labeled datasets struggle with unlabeled data due to mismatches in data distributions. To avoid the cost of annotating speech data, it is imperative to explore unsupervised adaptation techniques to leverage the potential of unlabeled data. Motivated by this observation, we pro-pose a novel use of voice conversion (VC) for SER, which effectively enhances emotion recognition performance on an unlabeled dataset. Our approach involves leveraging the simplicity and efficacy of the k-nearest neighbor (kNN)-based VC technique to transform speech samples from the unlabeled domain to the labeled domain. In contrast to conventional domain adaptation methods, our approach avoids re-training of a model on transformed unlabeled data. We achieve good results by testing transformed unlabeled samples on a model trained with a different labeled dataset.

</details>

### [Neural Codec Language Models for Disentangled and Textless Voice Conversion](s2:9a27124cb731b0db36cd60fa56ce611502d46f8f.md)
**Alan Baade, Puyuan Peng, David Harwath** · 2024-09-01

<details>
<summary>Abstract</summary>

We introduce a method for textless any-to-any voice conversion based on the recent progress in speech synthesis driven by neural codec language models. To disentangle the speaker and linguistic information, we adapt a speaker normalizing procedure for discrete semantic units, and then generate with an autoregressive language model for greatly improved diversity. We further improve the similarity of the output audio to the target speaker’s voice by leveraging classifier free guidance. We evaluate our techniques against current text to speech synthesis and voice conversion systems and compare the effectiveness of different neural codec language model pipelines. We demonstrate state-of-the-art results in accent disentanglement and speaker similarity for voice conversion with significantly less compute than existing codec language models such as VALL-E.

</details>

### [DiffVC+: Improving Diffusion-based Voice Conversion for Speaker Anonymization](s2:722794b80aaa3f664adfbf42295a2706622e9fa7.md)
**Fan Huang, Kun Zeng, Wei Zhu** · 2024-09-01

<details>
<summary>Abstract</summary>

The increasing risks of speech data leakage prompt growing concerns about voice privacy. This paper proposes DiffVC+, a speaker anonymization model designed to preserve speech privacy. It operates as a diffusion-based voice conversion model that suppresses identity information by converting the speaker’s voice through flexible approaches. DiffVC+ comprises a self-supervised learning (SSL) content encoder that effectively extracts the source speech content, a speaker encoder and an embedding generator that both supply the target speaker embedding, and a diffusion-based decoder generating the converted speech. Furthermore, we propose DiffVC+ light and DiffVC+ decoupled for edge-side and server-side deployments, respectively. Experimental results demonstrate that our models significantly outperform the baseline in terms of the intelligibility and naturalness of the converted speech, while achieving competitive anonymization performance.

</details>

### [Disentangling prosody and timbre embeddings via voice conversion](s2:95dce79bef20ee56ab574c8df089837524698a0b.md)
**Nicolas Gengembre, Olivier Le Blouch, Cédric Gendrot** · 2024-09-01

### [Zero-shot voice conversion based on feature disentanglement](s2:db551bfa300036ca2c35eb37bb991f10ef89c1e0.md)
**Na Guo, Jianguo Wei, Yongwei Li, Wenhuan Lu et al.** · 2024-09-01

### [Kurdish end-to-end speech synthesis using deep neural networks](s2:cf2c4780618bcc6c40e478b0c54c48871212086d.md)
**Sabat S. Muhamad, Hadi Veisi, Aso Mahmudi, A. A. Abdullah et al.** · 2024-09-01

### [Text-to-Speech for Unseen Speakers via Low-Complexity Discrete Unit-Based Frame Selection](2408.17432.md)
**Ismail Rasim Ulgen, Shreeram Suresh Chandra, Junchen Lu, Berrak Sisman** · 2024-08-30

<details>
<summary>Abstract</summary>

Synthesizing the voices of unseen speakers remains a persisting challenge in multi-speaker text-to-speech (TTS). Existing methods model speaker characteristics through speaker conditioning during training, leading to increased model complexity and limiting reproducibility and accessibility. A low-complexity alternative would broaden the reach of speech synthesis research, particularly in settings with limited computational and data resources. To this end, we propose SelectTTS, a simple and effective alternative. SelectTTS selects appropriate frames from the target speaker and decodes them using frame-level self-supervised learning (SSL) features. We demonstrate that this approach can effectively capture speaker characteristics for unseen speakers and achieves performance comparable to state-of-the-art multi-speaker TTS frameworks on both objective and subjective metrics. By directly selecting frames from the target speaker's speech, SelectTTS enables generalization to unseen speakers with significantly lower model complexity. Experimental results show that the proposed approach achieves performance comparable to state-of-the-art systems such as XTTS-v2 and VALL-E, while requiring over 8x fewer parameters and 270x less training data. Moreover, it demonstrates that frame selection with SSL features offers an efficient path to low-complexity, high-quality multi-speaker TTS.

</details>

### [Codec Does Matter: Exploring the Semantic Shortcoming of Codec for Audio Language Model](2408.17175.md)
**Zhen Ye, Peiwen Sun, Jiahe Lei, Hongzhan Lin et al.** · 2024-08-30

<details>
<summary>Abstract</summary>

Recent advancements in audio generation have been significantly propelled by the capabilities of Large Language Models (LLMs). The existing research on audio LLM has primarily focused on enhancing the architecture and scale of audio language models, as well as leveraging larger datasets, and generally, acoustic codecs, such as EnCodec, are used for audio tokenization. However, these codecs were originally designed for audio compression, which may lead to suboptimal performance in the context of audio LLM. Our research aims to address the shortcomings of current audio LLM codecs, particularly their challenges in maintaining semantic integrity in generated audio. For instance, existing methods like VALL-E, which condition acoustic token generation on text transcriptions, often suffer from content inaccuracies and elevated word error rates (WER) due to semantic misinterpretations of acoustic tokens, resulting in word skipping and errors. To overcome these issues, we propose a straightforward yet effective approach called X-Codec. X-Codec incorporates semantic features from a pre-trained semantic encoder before the Residual Vector Quantization (RVQ) stage and introduces a semantic reconstruction loss after RVQ. By enhancing the semantic ability of the codec, X-Codec significantly reduces WER in speech synthesis tasks and extends these benefits to non-speech applications, including music and sound generation. Our experiments in text-to-speech, music continuation, and text-to-sound tasks demonstrate that integrating semantic information substantially improves the overall performance of language models in audio generation. Our code and demo are available (Demo: https://x-codec-audio.github.io Code: https://github.com/zhenye234/xcodec)

</details>

### [Utilizing Speaker Profiles for Impersonation Audio Detection](2408.17009.md)
**Hao Gu, JiangYan Yi, Chenglong Wang, Yong Ren et al.** · 2024-08-30

<details>
<summary>Abstract</summary>

Fake audio detection is an emerging active topic. A growing number of literatures have aimed to detect fake utterance, which are mostly generated by Text-to-speech (TTS) or voice conversion (VC). However, countermeasures against impersonation remain an underexplored area. Impersonation is a fake type that involves an imitator replicating specific traits and speech style of a target speaker. Unlike TTS and VC, which often leave digital traces or signal artifacts, impersonation involves live human beings producing entirely natural speech, rendering the detection of impersonation audio a challenging task. Thus, we propose a novel method that integrates speaker profiles into the process of impersonation audio detection. Speaker profiles are inherent characteristics that are challenging for impersonators to mimic accurately, such as speaker's age, job. We aim to leverage these features to extract discriminative information for detecting impersonation audio. Moreover, there is no large impersonated speech corpora available for quantitative study of impersonation impacts. To address this gap, we further design the first large-scale, diverse-speaker Chinese impersonation dataset, named ImPersonation Audio Detection (IPAD), to advance the community's research on impersonation audio detection. We evaluate several existing fake audio detection methods on our proposed dataset IPAD, demonstrating its necessity and the challenges. Additionally, our findings reveal that incorporating speaker profiles can significantly enhance the model's performance in detecting impersonation audio.

</details>

### [Enabling Beam Search for Language Model-Based Text-to-Speech Synthesis](2408.16373.md)
**Zehai Tu et.al.** · 2024-08-29

### [Mini-Omni: Language Models Can Hear, Talk While Thinking in Streaming](2408.16725.md)
**Zhifei Xie, Changqiao Wu** · 2024-08-29

<details>
<summary>Abstract</summary>

Recent advances in language models have achieved significant progress. GPT-4o, as a new milestone, has enabled real-time conversations with humans, demonstrating near-human natural fluency. Such human-computer interaction necessitates models with the capability to perform reasoning directly with the audio modality and generate output in streaming. However, this remains beyond the reach of current academic models, as they typically depend on extra TTS systems for speech synthesis, resulting in undesirable latency. This paper introduces the Mini-Omni, an audio-based end-to-end conversational model, capable of real-time speech interaction. To achieve this capability, we propose a text-instructed speech generation method, along with batch-parallel strategies during inference to further boost the performance. Our method also helps to retain the original model's language capabilities with minimal degradation, enabling other works to establish real-time interaction capabilities. We call this training method "Any Model Can Talk". We also introduce the VoiceAssistant-400K dataset to fine-tune models optimized for speech output. To our best knowledge, Mini-Omni is the first fully end-to-end, open-source model for real-time speech interaction, offering valuable potential for future research.

</details>

### [RAVE for Speech: Efficient Voice Conversion at High Sampling Rates](2408.16546.md)
**Anders R. Bargum, Simon Lajboschitz, Cumhur Erkut** · 2024-08-29

<details>
<summary>Abstract</summary>

Voice conversion has gained increasing popularity within the field of audio manipulation and speech synthesis. Often, the main objective is to transfer the input identity to that of a target speaker without changing its linguistic content. While current work provides high-fidelity solutions they rarely focus on model simplicity, high-sampling rate environments or stream-ability. By incorporating speech representation learning into a generative timbre transfer model, traditionally created for musical purposes, we investigate the realm of voice conversion generated directly in the time domain at high sampling rates. More specifically, we guide the latent space of a baseline model towards linguistically relevant representations and condition it on external speaker information. Through objective and subjective assessments, we demonstrate that the proposed solution can attain levels of naturalness, quality, and intelligibility comparable to those of a state-of-the-art solution for seen speakers, while significantly decreasing inference time. However, despite the presence of target speaker characteristics in the converted output, the actual similarity to unseen speakers remains a challenge.

</details>

### [Multi-modal Adversarial Training for Zero-Shot Voice Cloning](2408.15916.md)
**John Janiczek et.al.** · 2024-08-28

### [VoxInstruct: Expressive Human Instruction-to-Speech Generation with Unified Multilingual Codec Language Modelling](2408.15676.md)
**Yixuan Zhou et.al.** · 2024-08-28

### [VoiceTailor: Lightweight Plug-In Adapter for Diffusion-Based Personalized Text-to-Speech](2408.14739.md)
**Heeseung Kim et.al.** · 2024-08-28

### [SimpleSpeech 2: Towards Simple and Efficient Text-to-Speech with Flow-based Scalar Latent Transformer Diffusion Models](2408.13893.md)
**Dongchao Yang et.al.** · 2024-08-28

### [Easy, Interpretable, Effective: openSMILE for voice deepfake detection](2408.15775.md)
**Octavian Pascu, Dan Oneata, Horia Cucu, Nicolas M. Müller** · 2024-08-28

<details>
<summary>Abstract</summary>

In this paper, we demonstrate that attacks in the latest ASVspoof5 dataset -- a de facto standard in the field of voice authenticity and deepfake detection -- can be identified with surprising accuracy using a small subset of very simplistic features. These are derived from the openSMILE library, and are scalar-valued, easy to compute, and human interpretable. For example, attack A10`s unvoiced segments have a mean length of 0.09 +- 0.02, while bona fide instances have a mean length of 0.18 +- 0.07. Using this feature alone, a threshold classifier achieves an Equal Error Rate (EER) of 10.3% for attack A10. Similarly, across all attacks, we achieve up to 0.8% EER, with an overall EER of 15.7 +- 6.0%. We explore the generalization capabilities of these features and find that some of them transfer effectively between attacks, primarily when the attacks originate from similar Text-to-Speech (TTS) architectures. This finding may indicate that voice anti-spoofing is, in part, a problem of identifying and remembering signatures or fingerprints of individual TTS systems. This allows to better understand anti-spoofing models and their challenges in real-world application.

</details>

### [Drop the beat! Freestyler for Accompaniment Conditioned Rapping Voice Generation](2408.15474.md)
**Ziqian Ning, Shuai Wang, Yuepeng Jiang, Jixun Yao et al.** · 2024-08-28

<details>
<summary>Abstract</summary>

Rap, a prominent genre of vocal performance, remains underexplored in vocal generation. General vocal synthesis depends on precise note and duration inputs, requiring users to have related musical knowledge, which limits flexibility. In contrast, rap typically features simpler melodies, with a core focus on a strong rhythmic sense that harmonizes with accompanying beats. In this paper, we propose Freestyler, the first system that generates rapping vocals directly from lyrics and accompaniment inputs. Freestyler utilizes language model-based token generation, followed by a conditional flow matching model to produce spectrograms and a neural vocoder to restore audio. It allows a 3-second prompt to enable zero-shot timbre control. Due to the scarcity of publicly available rap datasets, we also present RapBank, a rap song dataset collected from the internet, alongside a meticulously designed processing pipeline. Experimental results show that Freestyler produces high-quality rapping voice generation with enhanced naturalness and strong alignment with accompanying beats, both stylistically and rhythmically.

</details>

### [StyleSpeech: Parameter-efficient Fine Tuning for Pre-trained Controllable Text-to-Speech](2408.14713.md)
**Haowei Lou et.al.** · 2024-08-27

### [MaskCycleGAN-based Whisper to Normal Speech Conversion](2408.14797.md)
**K. Rohith Gupta, K. Ramnath, S. Johanan Joysingh, P. Vijayalakshmi et al.** · 2024-08-27

<details>
<summary>Abstract</summary>

Whisper to normal speech conversion is an active area of research. Various architectures based on generative adversarial networks have been proposed in the recent past. Especially, recent study shows that MaskCycleGAN, which is a mask guided, and cyclic consistency keeping, generative adversarial network, performs really well for voice conversion from spectrogram representations. In the current work we present a MaskCycleGAN approach for the conversion of whispered speech to normal speech. We find that tuning the mask parameters, and pre-processing the signal with a voice activity detector provides superior performance when compared to the existing approach. The wTIMIT dataset is used for evaluation. Objective metrics such as PESQ and G-Loss are used to evaluate the converted speech, along with subjective evaluation using mean opinion score. The results show that the proposed approach offers considerable benefits.

</details>

### [DualSpeech: Enhancing Speaker-Fidelity and Text-Intelligibility Through Dual Classifier-Free Guidance](2408.14423.md)
**Jinhyeok Yang, Junhyeok Lee, Hyeong-Seok Choi, Seunghun Ji et al.** · 2024-08-26

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) models have advanced significantly, aiming to accurately replicate human speech's diversity, including unique speaker identities and linguistic nuances. Despite these advancements, achieving an optimal balance between speaker-fidelity and text-intelligibility remains a challenge, particularly when diverse control demands are considered. Addressing this, we introduce DualSpeech, a TTS model that integrates phoneme-level latent diffusion with dual classifier-free guidance. This approach enables exceptional control over speaker-fidelity and text-intelligibility. Experimental results demonstrate that by utilizing the sophisticated control, DualSpeech surpasses existing state-of-the-art TTS models in performance. Demos are available at https://bit.ly/48Ewoib.

</details>

### [SpeechCraft: A Fine-grained Expressive Speech Dataset with Natural Language Description](2408.13608.md)
**Zeyu Jin, Jia Jia, Qixin Wang, Kehan Li et al.** · 2024-08-24

<details>
<summary>Abstract</summary>

Speech-language multi-modal learning presents a significant challenge due to the fine nuanced information inherent in speech styles. Therefore, a large-scale dataset providing elaborate comprehension of speech style is urgently needed to facilitate insightful interplay between speech audio and natural language. However, constructing such datasets presents a major trade-off between large-scale data collection and high-quality annotation. To tackle this challenge, we propose an automatic speech annotation system for expressiveness interpretation that annotates in-the-wild speech clips with expressive and vivid human language descriptions. Initially, speech audios are processed by a series of expert classifiers and captioning models to capture diverse speech characteristics, followed by a fine-tuned LLaMA for customized annotation generation. Unlike previous tag/templet-based annotation frameworks with limited information and diversity, our system provides in-depth understandings of speech style through tailored natural language descriptions, thereby enabling accurate and voluminous data generation for large model training. With this system, we create SpeechCraft, a fine-grained bilingual expressive speech dataset. It is distinguished by highly descriptive natural language style prompts, containing approximately 2,000 hours of audio data and encompassing over two million speech clips. Extensive experiments demonstrate that the proposed dataset significantly boosts speech-language task performance in stylist speech synthesis and speech style understanding.

</details>

### [SpeechPrompt: Prompting Speech Language Models for Speech Processing Tasks](2408.13040.md)
**Kai-Wei Chang, Haibin Wu, Yu-Kai Wang, Yuan-Kuei Wu et al.** · 2024-08-23

<details>
<summary>Abstract</summary>

Prompting has become a practical method for utilizing pre-trained language models (LMs). This approach offers several advantages. It allows an LM to adapt to new tasks with minimal training and parameter updates, thus achieving efficiency in both storage and computation. Additionally, prompting modifies only the LM's inputs and harnesses the generative capabilities of language models to address various downstream tasks in a unified manner. This significantly reduces the need for human labor in designing task-specific models. These advantages become even more evident as the number of tasks served by the LM scales up. Motivated by the strengths of prompting, we are the first to explore the potential of prompting speech LMs in the domain of speech processing. Recently, there has been a growing interest in converting speech into discrete units for language modeling. Our pioneer research demonstrates that these quantized speech units are highly versatile within our unified prompting framework. Not only can they serve as class labels, but they also contain rich phonetic information that can be re-synthesized back into speech signals for speech generation tasks. Specifically, we reformulate speech processing tasks into speech-to-unit generation tasks. As a result, we can seamlessly integrate tasks such as speech classification, sequence generation, and speech generation within a single, unified prompting framework. The experiment results show that the prompting method can achieve competitive performance compared to the strong fine-tuning method based on self-supervised learning models with a similar number of trainable parameters. The prompting method also shows promising results in the few-shot setting. Moreover, with the advanced speech LMs coming into the stage, the proposed prompting framework attains great potential.

</details>

### [VoiceX: A Text-To-Speech Framework for Custom Voices](2408.12170.md)
**Silvan Mertes, Daksitha Withanage Don, Otto Grothe, Johanna Kuch et al.** · 2024-08-22

<details>
<summary>Abstract</summary>

Modern TTS systems are capable of creating highly realistic and natural-sounding speech. Despite these developments, the process of customizing TTS voices remains a complex task, mostly requiring the expertise of specialists within the field. One reason for this is the utilization of deep learning models, which are characterized by their expansive, non-interpretable parameter spaces, restricting the feasibility of manual customization. In this paper, we present a novel human-in-the-loop paradigm based on an evolutionary algorithm for directly interacting with the parameter space of a neural TTS model. We integrated our approach into a user-friendly graphical user interface that allows users to efficiently create original voices. Those voices can then be used with the backbone TTS model, for which we provide a Python API. Further, we present the results of a user study exploring the capabilities of VoiceX. We show that VoiceX is an appropriate tool for creating individual, custom voices.

</details>

### [LCM-SVC: Latent Diffusion Model Based Singing Voice Conversion with Inference Acceleration via Latent Consistency Distillation](2408.12354.md)
**Shihao Chen, Yu Gu, Jianwei Cui, Jie Zhang et al.** · 2024-08-22

<details>
<summary>Abstract</summary>

Any-to-any singing voice conversion (SVC) aims to transfer a target singer's timbre to other songs using a short voice sample. However many diffusion model based any-to-any SVC methods, which have achieved impressive results, usually suffered from low efficiency caused by a mass of inference steps. In this paper, we propose LCM-SVC, a latent consistency distillation (LCD) based latent diffusion model (LDM) to accelerate inference speed. We achieved one-step or few-step inference while maintaining the high performance by distilling a pre-trained LDM based SVC model, which had the advantages of timbre decoupling and sound quality. Experimental results show that our proposed method can significantly reduce the inference time and largely preserve the sound quality and timbre similarity comparing with other state-of-the-art SVC models. Audio samples are available at https://sounddemos.github.io/lcm-svc.

</details>

### [Improvement Speaker Similarity for Zero-Shot Any-to-Any Voice Conversion of Whispered and Regular Speech](2408.11528.md)
**Anastasia Avdeeva, Aleksei Gusev** · 2024-08-21

<details>
<summary>Abstract</summary>

Zero-shot voice conversion aims to transfer the voice of a source speaker to that of a speaker unseen during training, while preserving the content information. Although various methods have been proposed to reconstruct speaker information in generated speech, there is still room for improvement in achieving high similarity between generated and ground truth recordings. Furthermore, zero-shot voice conversion for speech in specific domains, such as whispered, remains an unexplored area. To address this problem, we propose a SpeakerVC model that can effectively perform zero-shot speech conversion in both voiced and whispered domains, while being lightweight and capable of running in streaming mode without significant quality degradation. In addition, we explore methods to improve the quality of speaker identity transfer and demonstrate their effectiveness for a variety of voice conversion systems.

</details>

### [An Improved Phase Coding Audio Steganography Algorithm](2408.13277.md)
**Guang Yang** · 2024-08-21

<details>
<summary>Abstract</summary>

Advances in AI technology have made voice cloning increasingly accessible, leading to a rise in fraud involving AI-generated audio forgeries. This highlights the need to covertly embed information and verify the authenticity and integrity of audio. Digital Audio Watermarking plays a crucial role in this context. This study presents an improved Phase Coding audio steganography algorithm that segments the audio signal dynamically, embedding data into the mid-frequency phase components. This approach enhances resistance to steganalysis, simplifies computation, and ensures secure audio integrity.

</details>

### [SSL-TTS: Leveraging Self-Supervised Embeddings and kNN Retrieval for Zero-Shot Multi-speaker TTS](2408.10771.md)
**Karl El Hajal et.al.** · 2024-08-20

### [Adversarial training of Keyword Spotting to Minimize TTS Data Overfitting](2408.10463.md)
**Hyun Jin Park et.al.** · 2024-08-20

### [EELE: Exploring Efficient and Extensible LoRA Integration in Emotional Text-to-Speech](2408.10852.md)
**Xin Qi, Ruibo Fu, Zhengqi Wen, Jianhua Tao et al.** · 2024-08-20

<details>
<summary>Abstract</summary>

In the current era of Artificial Intelligence Generated Content (AIGC), a Low-Rank Adaptation (LoRA) method has emerged. It uses a plugin-based approach to learn new knowledge with lower parameter quantities and computational costs, and it can be plugged in and out based on the specific sub-tasks, offering high flexibility. However, the current application schemes primarily incorporate LoRA into the pre-introduced conditional parts of the speech models. This fixes the position of LoRA, limiting the flexibility and scalability of its application. Therefore, we propose the Exploring Efficient and Extensible LoRA Integration in Emotional Text-to-Speech (EELE) method. Starting from a general neutral speech model, we do not pre-introduce emotional information but instead use the LoRA plugin to design a flexible adaptive scheme that endows the model with emotional generation capabilities. Specifically, we initially train the model using only neutral speech data. After training is complete, we insert LoRA into different modules and fine-tune the model with emotional speech data to find the optimal insertion scheme. Through experiments, we compare and test the effects of inserting LoRA at different positions within the model and assess LoRA's ability to learn various emotions, effectively proving the validity of our method. Additionally, we explore the impact of the rank size of LoRA and the difference compared to directly fine-tuning the entire model.

</details>

### [AI-Based IVR](2408.10549.md)
**Gassyrbek Kosherbay, Nurgissa Apbaz** · 2024-08-20

<details>
<summary>Abstract</summary>

The use of traditional IVR (Interactive Voice Response) methods often proves insufficient to meet customer needs. This article examines the application of artificial intelligence (AI) technologies to enhance the efficiency of IVR systems in call centers. A proposed approach is based on the integration of speech-to-text conversion solutions, text query classification using large language models (LLM), and speech synthesis. Special attention is given to adapting these technologies to work with the Kazakh language, including fine-tuning models on specialized datasets. The practical aspects of implementing the developed system in a real call center for query classification are described. The research results demonstrate that the application of AI technologies in call center IVR systems reduces operator workload, improves customer service quality, and increases the efficiency of query processing. The proposed approach can be adapted for use in call centers operating with various languages.

</details>

### [Advancing Voice Cloning for Nepali: Leveraging Transfer Learning in a Low-Resource Language](2408.10128.md)
**Manjil Karki, Pratik Shakya, Sandesh Acharya, Ravi Pandit et al.** · 2024-08-19

<details>
<summary>Abstract</summary>

Voice cloning is a prominent feature in personalized speech interfaces. A neural vocal cloning system can mimic someone's voice using just a few audio samples. Both speaker encoding and speaker adaptation are topics of research in the field of voice cloning. Speaker adaptation relies on fine-tuning a multi-speaker generative model, which involves training a separate model to infer a new speaker embedding used for speaker encoding. Both methods can achieve excellent performance, even with a small number of cloning audios, in terms of the speech's naturalness and similarity to the original speaker. Speaker encoding approaches are more appropriate for low-resource deployment since they require significantly less memory and have a faster cloning time than speaker adaption, which can offer slightly greater naturalness and similarity. The main goal is to create a vocal cloning system that produces audio output with a Nepali accent or that sounds like Nepali. For the further advancement of TTS, the idea of transfer learning was effectively used to address several issues that were encountered in the development of this system, including the poor audio quality and the lack of available data.

</details>

### [Convert and Speak: Zero-shot Accent Conversion with Minimum Supervision](2408.10096.md)
**Zhijun Jia, Huaying Xue, Xiulian Peng, Yan Lu** · 2024-08-19

<details>
<summary>Abstract</summary>

Low resource of parallel data is the key challenge of accent conversion(AC) problem in which both the pronunciation units and prosody pattern need to be converted. We propose a two-stage generative framework "convert-and-speak" in which the conversion is only operated on the semantic token level and the speech is synthesized conditioned on the converted semantic token with a speech generative model in target accent domain. The decoupling design enables the "speaking" module to use massive amount of target accent speech and relieves the parallel data required for the "conversion" module. Conversion with the bridge of semantic token also relieves the requirement for the data with text transcriptions and unlocks the usage of language pre-training technology to further efficiently reduce the need of parallel accent speech data. To reduce the complexity and latency of "speaking", a single-stage AR generative model is designed to achieve good quality as well as lower computation cost. Experiments on Indian-English to general American-English conversion show that the proposed framework achieves state-of-the-art performance in accent similarity, speech quality, and speaker maintenance with only 15 minutes of weakly parallel data which is not constrained to the same speaker. Extensive experimentation with diverse accent types suggests that this framework possesses a high degree of adaptability, making it readily scalable to accommodate other accents with low-resource data. Audio samples are available at https://www.microsoft.com/en-us/research/project/convert-and-speak-zero-shot-accent-conversion-with-minimumsupervision/.

</details>

### [Reimagining speech: a scoping review of deep learning-based methods for non-parallel voice conversion](s2:9346d4bf50ab4baf3938b9c3ce74acc696c9d3b3.md)
**A. R. Bargum, Stefania Serafin, C. Erkut** · 2024-08-16

<details>
<summary>Abstract</summary>

Research on deep learning-powered voice conversion (VC) in speech-to-speech scenarios are gaining increasing popularity. Although many of the works in the field of voice conversion share a common global pipeline, there is considerable diversity in the underlying structures, methods, and neural sub-blocks used across research efforts. Thus, obtaining a comprehensive understanding of the reasons behind the choice of the different methods included when training voice conversion models can be challenging, and the actual hurdles in the proposed solutions are often unclear. To shed light on these aspects, this paper presents a scoping review that explores the use of deep learning in speech analysis, synthesis, and disentangled speech representation learning within modern voice conversion systems. We screened 628 publications from more than 38 venues between 2017 and 2023, followed by an in-depth review of a final database of 130 eligible studies. Based on the review, we summarise the most frequently used approaches to voice conversion based on deep learning and highlight common pitfalls. We condense the knowledge gathered to identify main challenges, supply solutions grounded in the analysis and provide recommendations for future research directions.

</details>

### [PeriodWave: Multi-Period Flow Matching for High-Fidelity Waveform Generation](2408.07547.md)
**Sang-Hoon Lee, Ha-Yeong Choi, Seong-Whan Lee** · 2024-08-14

<details>
<summary>Abstract</summary>

Recently, universal waveform generation tasks have been investigated conditioned on various out-of-distribution scenarios. Although GAN-based methods have shown their strength in fast waveform generation, they are vulnerable to train-inference mismatch scenarios such as two-stage text-to-speech. Meanwhile, diffusion-based models have shown their powerful generative performance in other domains; however, they stay out of the limelight due to slow inference speed in waveform generation tasks. Above all, there is no generator architecture that can explicitly disentangle the natural periodic features of high-resolution waveform signals. In this paper, we propose PeriodWave, a novel universal waveform generation model. First, we introduce a period-aware flow matching estimator that can capture the periodic features of the waveform signal when estimating the vector fields. Additionally, we utilize a multi-period estimator that avoids overlaps to capture different periodic features of waveform signals. Although increasing the number of periods can improve the performance significantly, this requires more computational costs. To reduce this issue, we also propose a single period-conditional universal estimator that can feed-forward parallel by period-wise batch inference. Additionally, we utilize discrete wavelet transform to losslessly disentangle the frequency information of waveform signals for high-frequency modeling, and introduce FreeU to reduce the high-frequency noise for waveform generation. The experimental results demonstrated that our model outperforms the previous models both in Mel-spectrogram reconstruction and text-to-speech tasks. All source code will be available at \url{https://github.com/sh-lee-prml/PeriodWave}.

</details>

### [WavLM model ensemble for audio deepfake detection](2408.07414.md)
**David Combei, Adriana Stan, Dan Oneata, Horia Cucu** · 2024-08-14

<details>
<summary>Abstract</summary>

Audio deepfake detection has become a pivotal task over the last couple of years, as many recent speech synthesis and voice cloning systems generate highly realistic speech samples, thus enabling their use in malicious activities. In this paper we address the issue of audio deepfake detection as it was set in the ASVspoof5 challenge. First, we benchmark ten types of pretrained representations and show that the self-supervised representations stemming from the wav2vec2 and wavLM families perform best. Of the two, wavLM is better when restricting the pretraining data to LibriSpeech, as required by the challenge rules. To further improve performance, we finetune the wavLM model for the deepfake detection task. We extend the ASVspoof5 dataset with samples from other deepfake detection datasets and apply data augmentation. Our final challenge submission consists of a late fusion combination of four models and achieves an equal error rate of 6.56% and 17.08% on the two evaluation sets.

</details>

### [Style-Talker: Finetuning Audio Language Model and Style-Based Text-to-Speech Model for Fast Spoken Dialogue Generation](2408.11849.md)
**Yinghao Aaron Li et.al.** · 2024-08-13

### [SaSLaW: Dialogue Speech Corpus with Audio-visual Egocentric Information Toward Environment-adaptive Dialogue Speech Synthesis](2408.06858.md)
**Osamu Take et.al.** · 2024-08-13

### [PRESENT: Zero-Shot Text-to-Prosody Control](2408.06827.md)
**Perry Lam et.al.** · 2024-08-13

### [VNet: A GAN-based Multi-Tier Discriminator Network for Speech Synthesis Vocoders](2408.06906.md)
**Yubing Cao, Yongming Li, Liejun Wang, Yinfeng Yu** · 2024-08-13

<details>
<summary>Abstract</summary>

Since the introduction of Generative Adversarial Networks (GANs) in speech synthesis, remarkable achievements have been attained. In a thorough exploration of vocoders, it has been discovered that audio waveforms can be generated at speeds exceeding real-time while maintaining high fidelity, achieved through the utilization of GAN-based models. Typically, the inputs to the vocoder consist of band-limited spectral information, which inevitably sacrifices high-frequency details. To address this, we adopt the full-band Mel spectrogram information as input, aiming to provide the vocoder with the most comprehensive information possible. However, previous studies have revealed that the use of full-band spectral information as input can result in the issue of over-smoothing, compromising the naturalness of the synthesized speech. To tackle this challenge, we propose VNet, a GAN-based neural vocoder network that incorporates full-band spectral information and introduces a Multi-Tier Discriminator (MTD) comprising multiple sub-discriminators to generate high-resolution signals. Additionally, we introduce an asymptotically constrained method that modifies the adversarial loss of the generator and discriminator, enhancing the stability of the training process. Through rigorous experiments, we demonstrate that the VNet model is capable of generating high-fidelity speech and significantly improving the performance of the vocoder.

</details>

### [Content and Style Aware Audio-Driven Facial Animation](2408.07005.md)
**Qingju Liu, Hyeongwoo Kim, Gaurav Bharaj** · 2024-08-13

<details>
<summary>Abstract</summary>

Audio-driven 3D facial animation has several virtual humans applications for content creation and editing. While several existing methods provide solutions for speech-driven animation, precise control over content (what) and style (how) of the final performance is still challenging. We propose a novel approach that takes as input an audio, and the corresponding text to extract temporally-aligned content and disentangled style representations, in order to provide controls over 3D facial animation. Our method is trained in two stages, that evolves from audio prominent styles (how it sounds) to visual prominent styles (how it looks). We leverage a high-resource audio dataset in stage I to learn styles that control speech generation in a self-supervised learning framework, and then fine-tune this model with low-resource audio/3D mesh pairs in stage II to control 3D vertex generation. We employ a non-autoregressive seq2seq formulation to model sentence-level dependencies, and better mouth articulations. Our method provides flexibility that the style of a reference audio and the content of a source audio can be combined to enable audio style transfer. Similarly, the content can be modified, e.g. muting or swapping words, that enables style-preserving content editing.

</details>

### [Assessing the perception of emotional prosody in healthy ageing.](s2:6e1c805cafca26738147a478d862ebbbca3f9008.md)
**Cansu Yıldırım, Seren Düzenli-Öztürk, Mümüne Merve Parlak** · 2024-08-13

<details>
<summary>Abstract</summary>

BACKGROUND Emotional prosody is the reflection of emotion types such as happiness, sadness, fear and anger in the speaker's tone of voice. Accurately perceiving, interpreting and expressing emotional prosody is an inseparable part of successful communication and social interaction. There are few studies on emotional prosody, which is crucial for communication, and the results of these studies have inconsistent information regarding age and gender. AIMS The primary aim of this study is to assess the perception of emotional prosody in healthy ageing. The other aim is to examine the effects of variables such as age, gender, language and neurocognitive capacity on the prediction of emotional prosody recognition skills. METHODS AND PROCEDURES Sixty-nine participants between the ages of 18-75 were included in the study. Participants were grouped as the young group aged 18-35 (n = 26), the middle-aged group aged 36-55 (n = 24) and the elderly group aged 56-75 (n = 19). Perceptual emotional prosody test, motor response time test, and neuropsychological test batteries were administered to the participants. Participants were asked to recognise the emotion in the sentences played on the computer. Natural (neutral, containing neither positive nor negative emotion), happy, angry, surprised and panic emotions were evaluated with sentences composed of pseudoword stimuli. RESULTS AND OUTCOMES It was observed that the elderly group performed worse in recognising angry, panic, natural and happy emotions and in total recognition, which gives the correct recognition performance in recognition of all emotions. There was no age-related difference in recognition of the emotion of surprise. The women were more successful in recognising angry, panic, happy and total emotions compared to men. Age and Motor Reaction Time Test scores were found to be significant predictors in the emotional response time regression model. Age, language, attention and gender variables were found to have a significant effect on the regression model created for the success of total recognition of emotions (p < 0.05). CONCLUSIONS AND IMPLICATIONS This was a novel study in which emotional prosody was assessed in the elderly by eliminating lexical-semantic cues related to emotional prosody and associating emotional prosody results with neuropsychiatric tests. All our findings revealed the importance of age for the perception of emotional prosody. In addition, the effects of cognitive functions such as attention, which decline with age, were found to be important. Therefore, it should not be forgotten that many factors contribute to the success of recognising emotional prosody correctly. In this context, clinicians should consider variables such as cognitive health and education when assessing the perception of emotional prosody in elderly individuals. WHAT THIS PAPER ADDS What is already known on the subject Most of the studies compare young and old groups, and these studies evaluate the perception of emotional prosody by using sentences formed by observing the speech sounds, syllables, words and grammar rules in the vocabulary of the language. It has been reported that the perception of emotional prosody is lower, mostly in the elderly group, but there is inconsistent information in terms of age and gender. What this paper adds to existing knowledge Perceptual Prosody Recognition was evaluated with an experimental design in which sentence structures consisting of lexemes were used as stimuli and neurocognitive tests were included, taking into account the phonological and syntactic rules of language. This study was a novel study in diagnosing emotional prosody in terms of comparing different age groups and determining the factors affecting multidimensional emotional prosody, including neuropsychiatric features. What are the clinical implications of this work? All our findings revealed the importance of age for the perception of emotional prosody. In addition, it was determined that the effects of cognitive functions such as attention were important with age.

</details>

### [FLEURS-R: A Restored Multilingual Speech Corpus for Generation Tasks](2408.06227.md)
**Min Ma, Yuma Koizumi, Shigeki Karita, Heiga Zen et al.** · 2024-08-12

<details>
<summary>Abstract</summary>

This paper introduces FLEURS-R, a speech restoration applied version of the Few-shot Learning Evaluation of Universal Representations of Speech (FLEURS) corpus. FLEURS-R maintains an N-way parallel speech corpus in 102 languages as FLEURS, with improved audio quality and fidelity by applying the speech restoration model Miipher. The aim of FLEURS-R is to advance speech technology in more languages and catalyze research including text-to-speech (TTS) and other speech generation tasks in low-resource languages. Comprehensive evaluations with the restored speech and TTS baseline models trained from the new corpus show that the new corpus obtained significantly improved speech quality while maintaining the semantic contents of the speech. The corpus is publicly released via Hugging Face.

</details>

### [The DeepSpeak Dataset](2408.05366.md)
**Sarah Barrington, Maty Bohacek, Hany Farid** · 2024-08-09

<details>
<summary>Abstract</summary>

Deepfakes represent a growing concern across domains such as disinformation, fraud, and non-consensual media. In particular, the rise of video conference and identity-driven attacks in high-stakes scenarios--such as impostor hiring--demands new forensic resources. Despite significant efforts to develop robust detection classifiers to distinguish the real from the fake, commonly used training datasets remain inadequate: relying on low-quality and outdated deepfake generators, consisting of content scraped from online repositories without participant consent, lacking in multimodal coverage, and rarely employing identity-matching protocols to ensure realistic fakes. To overcome these limitations, we present the DeepSpeak dataset, a diverse and multimodal dataset comprising over 100 hours of authentic and deepfake audiovisual content, specifically focused on the challenging and diverse talking heads context. We contribute: i) more than 50 hours of real, self-recorded data collected from 500 diverse and consenting participants, ii) more than 50 hours of state-of-the-art audio and visual deepfakes generated using 14 video synthesis engines and three voice cloning engines, and iii) an embedding-based, identity-matching approach to ensure the creation of convincing, high-quality identity face swaps that realistically simulate adversarial deepfake attacks. We also perform large-scale evaluations of state-of-the-art deepfake detectors and show that, without retraining, these detectors fail to generalize to this DeepSpeak dataset, highlighting the importance of a large and diverse dataset containing deepfakes from the latest generative-AI tools.

</details>

### [MulliVC: Multi-lingual Voice Conversion With Cycle Consistency](2408.04708.md)
**Jiawei Huang, Chen Zhang, Yi Ren, Ziyue Jiang et al.** · 2024-08-08

<details>
<summary>Abstract</summary>

Voice conversion aims to modify the source speaker's voice to resemble the target speaker while preserving the original speech content. Despite notable advancements in voice conversion these days, multi-lingual voice conversion (including both monolingual and cross-lingual scenarios) has yet to be extensively studied. It faces two main challenges: 1) the considerable variability in prosody and articulation habits across languages; and 2) the rarity of paired multi-lingual datasets from the same speaker. In this paper, we propose MulliVC, a novel voice conversion system that only converts timbre and keeps original content and source language prosody without multi-lingual paired data. Specifically, each training step of MulliVC contains three substeps: In step one the model is trained with monolingual speech data; then, steps two and three take inspiration from back translation, construct a cyclical process to disentangle the timbre and other information (content, prosody, and other language-related information) in the absence of multi-lingual data from the same speaker. Both objective and subjective results indicate that MulliVC significantly surpasses other methods in both monolingual and cross-lingual contexts, demonstrating the system's efficacy and the viability of the three-step approach with cycle consistency. Audio samples can be found on our demo page (mullivc.github.io).

</details>

### [Emotional Cues Extraction and Fusion for Multi-modal Emotion Prediction and Recognition in Conversation](2408.04547.md)
**Haoxiang Shi, Ziqi Liang, Jun Yu** · 2024-08-08

<details>
<summary>Abstract</summary>

Emotion Prediction in Conversation (EPC) aims to forecast the emotions of forthcoming utterances by utilizing preceding dialogues. Previous EPC approaches relied on simple context modeling for emotion extraction, overlooking fine-grained emotion cues at the word level. Additionally, prior works failed to account for the intrinsic differences between modalities, resulting in redundant information. To overcome these limitations, we propose an emotional cues extraction and fusion network, which consists of two stages: a modality-specific learning stage that utilizes word-level labels and prosody learning to construct emotion embedding spaces for each modality, and a two-step fusion stage for integrating multi-modal features. Moreover, the emotion features extracted by our model are also applicable to the Emotion Recognition in Conversation (ERC) task. Experimental results validate the efficacy of the proposed method, demonstrating superior performance on both IEMOCAP and MELD datasets.

</details>

### [Central Kurdish Text-to-Speech Synthesis with Novel End-to-End Transformer Training](2408.03887.md)
**Hawraz A. Ahmad et.al.** · 2024-08-06

### [Language Model Can Listen While Speaking](2408.02622.md)
**Ziyang Ma, Yakun Song, Chenpeng Du, Jian Cong et al.** · 2024-08-05

<details>
<summary>Abstract</summary>

Dialogue serves as the most natural manner of human-computer interaction (HCI). Recent advancements in speech language models (SLM) have significantly enhanced speech-based conversational AI. However, these models are limited to turn-based conversation, lacking the ability to interact with humans in real-time spoken scenarios, for example, being interrupted when the generated content is not satisfactory. To address these limitations, we explore full duplex modeling (FDM) in interactive speech language models (iSLM), focusing on enhancing real-time interaction and, more explicitly, exploring the quintessential ability of interruption. We introduce a novel model design, namely listening-while-speaking language model (LSLM), an end-to-end system equipped with both listening and speaking channels. Our LSLM employs a token-based decoder-only TTS for speech generation and a streaming self-supervised learning (SSL) encoder for real-time audio input. LSLM fuses both channels for autoregressive generation and detects turn-taking in real time. Three fusion strategies -- early fusion, middle fusion, and late fusion -- are explored, with middle fusion achieving an optimal balance between speech generation and real-time interaction. Two experimental settings, command-based FDM and voice-based FDM, demonstrate LSLM's robustness to noise and sensitivity to diverse instructions. Our results highlight LSLM's capability to achieve duplex communication with minimal impact on existing systems. This study aims to advance the development of interactive speech dialogue systems, enhancing their applicability in real-world contexts.

</details>

### [Re-ENACT: Reinforcement Learning for Emotional Speech Generation using Actor-Critic Strategy](2408.01892.md)
**Ravi Shankar, Archana Venkataraman** · 2024-08-04

<details>
<summary>Abstract</summary>

In this paper, we propose the first method to modify the prosodic features of a given speech signal using actor-critic reinforcement learning strategy. Our approach uses a Bayesian framework to identify contiguous segments of importance that links segments of the given utterances to perception of emotions in humans. We train a neural network to produce the variational posterior of a collection of Bernoulli random variables; our model applies a Markov prior on it to ensure continuity. A sample from this distribution is used for downstream emotion prediction. Further, we train the neural network to predict a soft assignment over emotion categories as the target variable. In the next step, we modify the prosodic features (pitch, intensity, and rhythm) of the masked segment to increase the score of target emotion. We employ an actor-critic reinforcement learning to train the prosody modifier by discretizing the space of modifications. Further, it provides a simple solution to the problem of gradient computation through WSOLA operation for rhythm manipulation. Our experiments demonstrate that this framework changes the perceived emotion of a given speech utterance to the target. Further, we show that our unified technique is on par with state-of-the-art emotion conversion models from supervised and unsupervised domains that require pairwise training.

</details>

### [End-to-end Tibetan emotional speech synthesis based on Mandarin emotions transfer](s2:f88107984b01c46c93ba238508aa74a20f3260e6.md)
**Weizhao Zhang, Wenxuan Zhang** · 2024-08-04

<details>
<summary>Abstract</summary>

Emotional speech synthesis has attracted much attention in speech synthesis, especially in low-resource languages like Tibetan. However, Tibetan emotional speech synthesis is still in its infancy, facing challenges such as the lack of available public Tibetan emotional datasets and issues related to speaker disentanglement and emotional confusion. To address these problems, we propose an emotional Tibetan speech synthesis method based on improved FastSpeech2 training with a mix of neutral Tibetan, neutral Mandarin, and emotional Mandarin datasets. First, we replaced the normalization layer in the transformer structure of the original FastSpeech2 with an emotion-conditioned layer normalization(ELN), using emotion embeddings as conditional inputs to improve the model’s ability to learn emotions. Then, we used the orthogonal loss to disentangle the speaker vector and emotion vector to alleviate the speaker leakage problem. Additionally, orthogonal loss is also employed to address the problem of emotional confusion by enhancing the correlation between similar emotional features and ensuring independence among different emotional features. Experimental results showed that we successfully synthesized speech in five emotions for both Tibetan and Mandarin by transferring Mandarin emotions without any emotional Tibetan dataset. The mean opinion score (MOS) for all synthesized Tibetan speech was 3.87 or higher, while the MOS for all synthesized Mandarin speech was 3.81 or higher. Additionally, we evaluated the emotional transmission accuracy of the synthesized speech in Tibetan and Mandarin. The results showed that the emotional transmission accuracy of the Tibetan synthesized speech exceeded 80% in neutral, sad, and surprised emotions for the majority of speakers, while the emotional transmission accuracy of the synthesized Mandarin speech exceeded 69% across all five emotions.

</details>

### [Bailing-TTS: Chinese Dialectal Speech Synthesis Towards Human-like Spontaneous Representation](2408.00284.md)
**Xinhan Di et.al.** · 2024-08-01

### [Generative Expressive Conversational Speech Synthesis](2407.21491.md)
**Rui Liu, Yifan Hu, Yi Ren, Xiang Yin et al.** · 2024-07-31

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis (CSS) aims to express a target utterance with the proper speaking style in a user-agent conversation setting. Existing CSS methods employ effective multi-modal context modeling techniques to achieve empathy understanding and expression. However, they often need to design complex network architectures and meticulously optimize the modules within them. In addition, due to the limitations of small-scale datasets containing scripted recording styles, they often fail to simulate real natural conversational styles. To address the above issues, we propose a novel generative expressive CSS system, termed GPT-Talker.We transform the multimodal information of the multi-turn dialogue history into discrete token sequences and seamlessly integrate them to form a comprehensive user-agent dialogue context. Leveraging the power of GPT, we predict the token sequence, that includes both semantic and style knowledge, of response for the agent. After that, the expressive conversational speech is synthesized by the conversation-enriched VITS to deliver feedback to the user.Furthermore, we propose a large-scale Natural CSS Dataset called NCSSD, that includes both naturally recorded conversational speech in improvised styles and dialogues extracted from TV shows. It encompasses both Chinese and English languages, with a total duration of 236 hours.We conducted comprehensive experiments on the reliability of the NCSSD and the effectiveness of our GPT-Talker. Both subjective and objective evaluations demonstrate that our model outperforms other state-of-the-art CSS systems significantly in terms of naturalness and expressiveness. The Code, Dataset, and Pre-trained Model are available at: https://github.com/AI-S2-Lab/GPT-Talker.

</details>

### [Towards Improving NAM-to-Speech Synthesis Intelligibility using Self-Supervised Speech Models](2407.18541.md)
**Neil Shah, Shirish Karande, Vineet Gandhi** · 2024-07-26

<details>
<summary>Abstract</summary>

We propose a novel approach to significantly improve the intelligibility in the Non-Audible Murmur (NAM)-to-speech conversion task, leveraging self-supervision and sequence-to-sequence (Seq2Seq) learning techniques. Unlike conventional methods that explicitly record ground-truth speech, our methodology relies on self-supervision and speech-to-speech synthesis to simulate ground-truth speech. Despite utilizing simulated speech, our method surpasses the current state-of-the-art (SOTA) by 29.08% improvement in the Mel-Cepstral Distortion (MCD) metric. Additionally, we present error rates and demonstrate our model's proficiency to synthesize speech in novel voices of interest. Moreover, we present a methodology for augmenting the existing CSTR NAM TIMIT Plus corpus, setting a benchmark with a Word Error Rate (WER) of 42.57% to gauge the intelligibility of the synthesized speech. Speech samples can be found at https://nam2speech.github.io/NAM2Speech/

</details>

### [Zero-Shot vs. Few-Shot Multi-Speaker TTS Using Pre-trained Czech SpeechT5 Model](2407.17167.md)
**Jan Lehečka et.al.** · 2024-07-24

### [Speech Editing -- a Summary](2407.17172.md)
**Tobias Kässmann, Yining Liu, Danni Liu** · 2024-07-24

<details>
<summary>Abstract</summary>

With the rise of video production and social media, speech editing has become crucial for creators to address issues like mispronunciations, missing words, or stuttering in audio recordings. This paper explores text-based speech editing methods that modify audio via text transcripts without manual waveform editing. These approaches ensure edited audio is indistinguishable from the original by altering the mel-spectrogram. Recent advancements, such as context-aware prosody correction and advanced attention mechanisms, have improved speech editing quality. This paper reviews state-of-the-art methods, compares key metrics, and examines widely used datasets. The aim is to highlight ongoing issues and inspire further research and innovation in speech editing.

</details>

### [Synth4Kws: Synthesized Speech for User Defined Keyword Spotting in Low Resource Environments](2407.16840.md)
**Pai Zhu, Dhruuv Agarwal, Jacob W. Bartel, Kurt Partridge et al.** · 2024-07-23

<details>
<summary>Abstract</summary>

One of the challenges in developing a high quality custom keyword spotting (KWS) model is the lengthy and expensive process of collecting training data covering a wide range of languages, phrases and speaking styles. We introduce Synth4Kws - a framework to leverage Text to Speech (TTS) synthesized data for custom KWS in different resource settings. With no real data, we found increasing TTS phrase diversity and utterance sampling monotonically improves model performance, as evaluated by EER and AUC metrics over 11k utterances of the speech command dataset. In low resource settings, with 50k real utterances as a baseline, we found using optimal amounts of TTS data can improve EER by 30.1% and AUC by 46.7%. Furthermore, we mix TTS data with varying amounts of real data and interpolate the real data needed to achieve various quality targets. Our experiments are based on English and single word utterances but the findings generalize to i18n languages and other keyword types.

</details>

### [Distortion Recovery: A Two-Stage Method for Guitar Effect Removal](2407.16639.md)
**Ying-Shuo Lee, Yueh-Po Peng, Jui-Te Wu, Ming Cheng et al.** · 2024-07-23

<details>
<summary>Abstract</summary>

Removing audio effects from electric guitar recordings makes it easier for post-production and sound editing. An audio distortion recovery model not only improves the clarity of the guitar sounds but also opens up new opportunities for creative adjustments in mixing and mastering. While progress have been made in creating such models, previous efforts have largely focused on synthetic distortions that may be too simplistic to accurately capture the complexities seen in real-world recordings. In this paper, we tackle the task by using a dataset of guitar recordings rendered with commercial-grade audio effect VST plugins. Moreover, we introduce a novel two-stage methodology for audio distortion recovery. The idea is to firstly process the audio signal in the Mel-spectrogram domain in the first stage, and then use a neural vocoder to generate the pristine original guitar sound from the processed Mel-spectrogram in the second stage. We report a set of experiments demonstrating the effectiveness of our approach over existing methods, through both subjective and objective evaluation metrics.

</details>

### [dMel: Speech Tokenization made Simple](2407.15835.md)
**Richard He Bai, Tatiana Likhomanenko, Ruixiang Zhang, Zijin Gu et al.** · 2024-07-22

<details>
<summary>Abstract</summary>

Large language models have revolutionized natural language processing by leveraging self-supervised pretraining on vast textual data. Inspired by this success, researchers have investigated various compression-based speech tokenization methods to discretize continuous speech signals, enabling the application of language modeling techniques to discrete tokens. However, audio compressor introduces additional complexity and computational cost, and often fail on out-of-domain audio signals. In this work, we introduce a novel speech representation (dmel) that discretizes mel-filterbank channels into intensity bins, creating a simpler yet more effective representation compared to existing speech tokenization methods. Our approach demonstrates superior performance in preserving audio content, robustness to out-of-domain data, and offers a training-free, natural, and streamable representation. To address the high-dimensional nature of log-mel spectrograms, we propose an efficient parallel encoding and decoding method for high-dimensional tokens using an LM-style transformer architecture. This innovation enables us to develop RichTTS and RichASR, two models sharing the same architecture while achieving comparable or better results than specialized existing methods. Our results demonstrate the effectiveness of dmel in achieving high performance on both speech synthesis and recognition tasks within a unified framework, paving the way for efficient and effective joint modeling of speech and text.

</details>

### [Towards Realistic Emotional Voice Conversion using Controllable Emotional Intensity](2407.14800.md)
**Tianhua Qi, Shiyan Wang, Cheng Lu, Yan Zhao et al.** · 2024-07-20

<details>
<summary>Abstract</summary>

Realistic emotional voice conversion (EVC) aims to enhance emotional diversity of converted audios, making the synthesized voices more authentic and natural. To this end, we propose Emotional Intensity-aware Network (EINet), dynamically adjusting intonation and rhythm by incorporating controllable emotional intensity. To better capture nuances in emotional intensity, we go beyond mere distance measurements among acoustic features. Instead, an emotion evaluator is utilized to precisely quantify speaker's emotional state. By employing an intensity mapper, intensity pseudo-labels are obtained to bridge the gap between emotional speech intensity modeling and run-time conversion. To ensure high speech quality while retaining controllability, an emotion renderer is used for combining linguistic features smoothly with manipulated emotional features at frame level. Furthermore, we employ a duration predictor to facilitate adaptive prediction of rhythm changes condition on specifying intensity value. Experimental results show EINet's superior performance in naturalness and diversity of emotional expression compared to state-of-the-art EVC methods.

</details>

### [Braille-to-Speech Generator: Audio Generation Based on Joint Fine-Tuning of CLIP and Fastspeech2](2407.14212.md)
**Chun Xu et.al.** · 2024-07-19

### [Rasa: Building Expressive Speech Synthesis Systems for Indian Languages in Low-resource Settings](2407.14056.md)
**Praveen Srinivasa Varadhan, Ashwin Sankar, Giri Raju, Mitesh M. Khapra** · 2024-07-19

<details>
<summary>Abstract</summary>

We release Rasa, the first multilingual expressive TTS dataset for any Indian language, which contains 10 hours of neutral speech and 1-3 hours of expressive speech for each of the 6 Ekman emotions covering 3 languages: Assamese, Bengali, & Tamil. Our ablation studies reveal that just 1 hour of neutral and 30 minutes of expressive data can yield a Fair system as indicated by MUSHRA scores. Increasing neutral data to 10 hours, with minimal expressive data, significantly enhances expressiveness. This offers a practical recipe for resource-constrained languages, prioritizing easily obtainable neutral data alongside smaller amounts of expressive data. We show the importance of syllabically balanced data and pooling emotions to enhance expressiveness. We also highlight challenges in generating specific emotions, e.g., fear and surprise.

</details>

### [MSceneSpeech: A Multi-Scene Speech Dataset For Expressive Speech Synthesis](2407.14006.md)
**Qian Yang, Jialong Zuo, Zhe Su, Ziyue Jiang et al.** · 2024-07-19

<details>
<summary>Abstract</summary>

We introduce an open source high-quality Mandarin TTS dataset MSceneSpeech (Multiple Scene Speech Dataset), which is intended to provide resources for expressive speech synthesis. MSceneSpeech comprises numerous audio recordings and texts performed and recorded according to daily life scenarios. Each scenario includes multiple speakers and a diverse range of prosodic styles, making it suitable for speech synthesis that entails multi-speaker style and prosody modeling. We have established a robust baseline, through the prompting mechanism, that can effectively synthesize speech characterized by both user-specific timbre and scene-specific prosody with arbitrary text input. The open source MSceneSpeech Dataset and audio samples of our baseline are available at https://speechai-demo.github.io/MSceneSpeech/.

</details>

### [Spontaneous Style Text-to-Speech Synthesis with Controllable Spontaneous Behaviors Based on Language Models](2407.13509.md)
**Weiqin Li et.al.** · 2024-07-18

### [Preset-Voice Matching for Privacy Regulated Speech-to-Speech Translation Systems](2407.13153.md)
**Daniel Platnick, Bishoy Abdelnour, Eamon Earl, Rahul Kumar et al.** · 2024-07-18

<details>
<summary>Abstract</summary>

In recent years, there has been increased demand for speech-to-speech translation (S2ST) systems in industry settings. Although successfully commercialized, cloning-based S2ST systems expose their distributors to liabilities when misused by individuals and can infringe on personality rights when exploited by media organizations. This work proposes a regulated S2ST framework called Preset-Voice Matching (PVM). PVM removes cross-lingual voice cloning in S2ST by first matching the input voice to a similar prior consenting speaker voice in the target-language. With this separation, PVM avoids cloning the input speaker, ensuring PVM systems comply with regulations and reduce risk of misuse. Our results demonstrate PVM can significantly improve S2ST system run-time in multi-speaker settings and the naturalness of S2ST synthesized speech. To our knowledge, PVM is the first explicitly regulated S2ST framework leveraging similarly-matched preset-voices for dynamic S2ST tasks.

</details>

### [Laugh Now Cry Later: Controlling Time-Varying Emotional States of Flow-Matching-Based Zero-Shot Text-to-Speech](2407.12229.md)
**Haibin Wu et.al.** · 2024-07-17

### [TTSDS -- Text-to-Speech Distribution Score](2407.12707.md)
**Christoph Minixhofer, Ondřej Klejch, Peter Bell** · 2024-07-17

<details>
<summary>Abstract</summary>

Many recently published Text-to-Speech (TTS) systems produce audio close to real speech. However, TTS evaluation needs to be revisited to make sense of the results obtained with the new architectures, approaches and datasets. We propose evaluating the quality of synthetic speech as a combination of multiple factors such as prosody, speaker identity, and intelligibility. Our approach assesses how well synthetic speech mirrors real speech by obtaining correlates of each factor and measuring their distance from both real speech datasets and noise datasets. We benchmark 35 TTS systems developed between 2008 and 2024 and show that our score computed as an unweighted average of factors strongly correlates with the human evaluations from each time period.

</details>

### [SpikeVoice: High-Quality Text-to-Speech Via Efficient Spiking Neural Network](2408.00788.md)
**Kexin Wang, Jiahong Zhang, Yong Ren, Man Yao et al.** · 2024-07-17

<details>
<summary>Abstract</summary>

Brain-inspired Spiking Neural Network (SNN) has demonstrated its effectiveness and efficiency in vision, natural language, and speech understanding tasks, indicating their capacity to "see", "listen", and "read". In this paper, we design \textbf{SpikeVoice}, which performs high-quality Text-To-Speech (TTS) via SNN, to explore the potential of SNN to "speak". A major obstacle to using SNN for such generative tasks lies in the demand for models to grasp long-term dependencies. The serial nature of spiking neurons, however, leads to the invisibility of information at future spiking time steps, limiting SNN models to capture sequence dependencies solely within the same time step. We term this phenomenon "partial-time dependency". To address this issue, we introduce Spiking Temporal-Sequential Attention STSA in the SpikeVoice. To the best of our knowledge, SpikeVoice is the first TTS work in the SNN field. We perform experiments using four well-established datasets that cover both Chinese and English languages, encompassing scenarios with both single-speaker and multi-speaker configurations. The results demonstrate that SpikeVoice can achieve results comparable to Artificial Neural Networks (ANN) with only 10.5 energy consumption of ANN.

</details>

### [A Language Modeling Approach to Diacritic-Free Hebrew TTS](2407.12206.md)
**Amit Roth et.al.** · 2024-07-16

### [Learning High-Frequency Functions Made Easy with Sinusoidal Positional Encoding](2407.09370.md)
**Chuanhao Sun, Zhihang Yuan, Kai Xu, Luo Mai et al.** · 2024-07-12

<details>
<summary>Abstract</summary>

Fourier features based positional encoding (PE) is commonly used in machine learning tasks that involve learning high-frequency features from low-dimensional inputs, such as 3D view synthesis and time series regression with neural tangent kernels. Despite their effectiveness, existing PEs require manual, empirical adjustment of crucial hyperparameters, specifically the Fourier features, tailored to each unique task. Further, PEs face challenges in efficiently learning high-frequency functions, particularly in tasks with limited data. In this paper, we introduce sinusoidal PE (SPE), designed to efficiently learn adaptive frequency features closely aligned with the true underlying function. Our experiments demonstrate that SPE, without hyperparameter tuning, consistently achieves enhanced fidelity and faster training across various tasks, including 3D view synthesis, Text-to-Speech generation, and 1D regression. SPE is implemented as a direct replacement for existing PEs. Its plug-and-play nature lets numerous tasks easily adopt and benefit from SPE.

</details>

### [Autoregressive Speech Synthesis without Vector Quantization](2407.08551.md)
**Lingwei Meng et.al.** · 2024-07-11

### [Toward accessible comics for blind and low vision readers](2407.08248.md)
**Christophe Rigaud, Jean-Christophe Burie, Samuel Petit** · 2024-07-11

<details>
<summary>Abstract</summary>

This work explores how to fine-tune large language models using prompt engineering techniques with contextual information for generating an accurate text description of the full story, ready to be forwarded to off-the-shelve speech synthesis tools. We propose to use existing computer vision and optical character recognition techniques to build a grounded context from the comic strip image content, such as panels, characters, text, reading order and the association of bubbles and characters. Then we infer character identification and generate comic book script with context-aware panel description including character's appearance, posture, mood, dialogues etc. We believe that such enriched content description can be easily used to produce audiobook and eBook with various voices for characters, captions and playing sound effects.

</details>

### [Source Tracing of Audio Deepfake Systems](2407.08016.md)
**Nicholas Klein, Tianxiang Chen, Hemlata Tak, Ricardo Casal et al.** · 2024-07-10

<details>
<summary>Abstract</summary>

Recent progress in generative AI technology has made audio deepfakes remarkably more realistic. While current research on anti-spoofing systems primarily focuses on assessing whether a given audio sample is fake or genuine, there has been limited attention on discerning the specific techniques to create the audio deepfakes. Algorithms commonly used in audio deepfake generation, like text-to-speech (TTS) and voice conversion (VC), undergo distinct stages including input processing, acoustic modeling, and waveform generation. In this work, we introduce a system designed to classify various spoofing attributes, capturing the distinctive features of individual modules throughout the entire generation pipeline. We evaluate our system on two datasets: the ASVspoof 2019 Logical Access and the Multi-Language Audio Anti-Spoofing Dataset (MLAAD). Results from both experiments demonstrate the robustness of the system to identify the different spoofing attributes of deepfake generation systems.

</details>

### [RT-LA-VocE: Real-Time Low-SNR Audio-Visual Speech Enhancement](2407.07825.md)
**Honglie Chen, Rodrigo Mira, Stavros Petridis, Maja Pantic** · 2024-07-10

<details>
<summary>Abstract</summary>

In this paper, we aim to generate clean speech frame by frame from a live video stream and a noisy audio stream without relying on future inputs. To this end, we propose RT-LA-VocE, which completely re-designs every component of LA-VocE, a state-of-the-art non-causal audio-visual speech enhancement model, to perform causal real-time inference with a 40ms input frame. We do so by devising new visual and audio encoders that rely solely on past frames, replacing the Transformer encoder with the Emformer, and designing a new causal neural vocoder C-HiFi-GAN. On the popular AVSpeech dataset, we show that our algorithm achieves state-of-the-art results in all real-time scenarios. More importantly, each component is carefully tuned to minimize the algorithm latency to the theoretical minimum (40ms) while maintaining a low end-to-end processing latency of 28.15ms per frame, enabling real-time frame-by-frame enhancement with minimal delay.

</details>

### [SaMoye: Zero-shot Singing Voice Conversion Model Based on Feature Disentanglement and Enhancement](2407.07728.md)
**Zihao Wang, Le Ma, Yongsheng Feng, Xin Pan et al.** · 2024-07-10

<details>
<summary>Abstract</summary>

Singing voice conversion (SVC) aims to convert a singer's voice to another singer's from a reference audio while keeping the original semantics. However, existing SVC methods can hardly perform zero-shot due to incomplete feature disentanglement or dependence on the speaker look-up table. We propose the first open-source high-quality zero-shot SVC model SaMoye that can convert singing to human and non-human timbre. SaMoye disentangles the singing voice's features into content, timbre, and pitch features, where we combine multiple ASR models and compress the content features to reduce timbre leaks. Besides, we enhance the timbre features by unfreezing the speaker encoder and mixing the speaker embedding with top-3 similar speakers. We also establish an unparalleled large-scale dataset to guarantee zero-shot performance, which comprises more than 1,815 hours of pure singing voice and 6,367 speakers. We conduct objective and subjective experiments to find that SaMoye outperforms other models in zero-shot SVC tasks even under extreme conditions like converting singing to animals' timbre. The code and weight of SaMoye are available on https://github.com/CarlWangChina/SaMoye-SVC. The weights, code, dataset, and documents of SaMoye are publicly available on \url{https://github.com/CarlWangChina/SaMoye-SVC}.

</details>

### [CosyVoice: A Scalable Multilingual Zero-shot Text-to-speech Synthesizer based on Supervised Semantic Tokens](2407.05407.md)
**Zhihao Du et.al.** · 2024-07-09

### [ASRRL-TTS: Agile Speaker Representation Reinforcement Learning for Text-to-Speech Speaker Adaptation](2407.05421.md)
**Ruibo Fu et.al.** · 2024-07-07

### [Fine-Grained and Interpretable Neural Speech Editing](2407.05471.md)
**Max Morrison, Cameron Churchwell, Nathan Pruyne, Bryan Pardo** · 2024-07-07

<details>
<summary>Abstract</summary>

Fine-grained editing of speech attributes$\unicode{x2014}$such as prosody (i.e., the pitch, loudness, and phoneme durations), pronunciation, speaker identity, and formants$\unicode{x2014}$is useful for fine-tuning and fixing imperfections in human and AI-generated speech recordings for creation of podcasts, film dialogue, and video game dialogue. Existing speech synthesis systems use representations that entangle two or more of these attributes, prohibiting their use in fine-grained, disentangled editing. In this paper, we demonstrate the first disentangled and interpretable representation of speech with comparable subjective and objective vocoding reconstruction accuracy to Mel spectrograms. Our interpretable representation, combined with our proposed data augmentation method, enables training an existing neural vocoder to perform fast, accurate, and high-quality editing of pitch, duration, volume, timbral correlates of volume, pronunciation, speaker identity, and spectral balance.

</details>

### [Emilia: An Extensive, Multilingual, and Diverse Speech Dataset for Large-Scale Speech Generation](2407.05361.md)
**Haorui He, Zengqiang Shang, Chaoren Wang, Xuyuan Li et al.** · 2024-07-07

<details>
<summary>Abstract</summary>

Recent advancements in speech generation models have been significantly driven by the use of large-scale training data. However, producing highly spontaneous, human-like speech remains a challenge due to the scarcity of large, diverse, and spontaneous speech datasets. In response, we introduce Emilia, the first large-scale, multilingual, and diverse speech generation dataset. Emilia starts with over 101k hours of speech across six languages, covering a wide range of speaking styles to enable more natural and spontaneous speech generation. To facilitate the scale-up of Emilia, we also present Emilia-Pipe, the first open-source preprocessing pipeline designed to efficiently transform raw, in-the-wild speech data into high-quality training data with speech annotations. Experimental results demonstrate the effectiveness of both Emilia and Emilia-Pipe. Demos are available at: https://emilia-dataset.github.io/Emilia-Demo-Page/.

</details>

### [FA-GAN: Artifacts-free and Phase-aware High-fidelity GAN-based Vocoder](2407.04575.md)
**Rubing Shen, Yanzhen Ren, Zongkun Sun** · 2024-07-05

<details>
<summary>Abstract</summary>

Generative adversarial network (GAN) based vocoders have achieved significant attention in speech synthesis with high quality and fast inference speed. However, there still exist many noticeable spectral artifacts, resulting in the quality decline of synthesized speech. In this work, we adopt a novel GAN-based vocoder designed for few artifacts and high fidelity, called FA-GAN. To suppress the aliasing artifacts caused by non-ideal upsampling layers in high-frequency components, we introduce the anti-aliased twin deconvolution module in the generator. To alleviate blurring artifacts and enrich the reconstruction of spectral details, we propose a novel fine-grained multi-resolution real and imaginary loss to assist in the modeling of phase information. Experimental results reveal that FA-GAN outperforms the compared approaches in promoting audio quality and alleviating spectral artifacts, and exhibits superior performance when applied to unseen speaker scenarios.

</details>

### [On the Effectiveness of Acoustic BPE in Decoder-Only TTS](2407.03892.md)
**Bohan Li et.al.** · 2024-07-04

### [CATT: Character-based Arabic Tashkeel Transformer](2407.03236.md)
**Faris Alasmary, Orjuwan Zaafarani, Ahmad Ghannam** · 2024-07-03

<details>
<summary>Abstract</summary>

Tashkeel, or Arabic Text Diacritization (ATD), greatly enhances the comprehension of Arabic text by removing ambiguity and minimizing the risk of misinterpretations caused by its absence. It plays a crucial role in improving Arabic text processing, particularly in applications such as text-to-speech and machine translation. This paper introduces a new approach to training ATD models. First, we finetuned two transformers, encoder-only and encoder-decoder, that were initialized from a pretrained character-based BERT. Then, we applied the Noisy-Student approach to boost the performance of the best model. We evaluated our models alongside 11 commercial and open-source models using two manually labeled benchmark datasets: WikiNews and our CATT dataset. Our findings show that our top model surpasses all evaluated models by relative Diacritic Error Rates (DERs) of 30.83\% and 35.21\% on WikiNews and CATT, respectively, achieving state-of-the-art in ATD. In addition, we show that our model outperforms GPT-4-turbo on CATT dataset by a relative DER of 9.36\%. We open-source our CATT models and benchmark dataset for the research community\footnote{https://github.com/abjadai/catt}.

</details>

### [Probing the Feasibility of Multilingual Speaker Anonymization](2407.02937.md)
**Sarina Meyer, Florian Lux, Ngoc Thang Vu** · 2024-07-03

<details>
<summary>Abstract</summary>

In speaker anonymization, speech recordings are modified in a way that the identity of the speaker remains hidden. While this technology could help to protect the privacy of individuals around the globe, current research restricts this by focusing almost exclusively on English data. In this study, we extend a state-of-the-art anonymization system to nine languages by transforming language-dependent components to their multilingual counterparts. Experiments testing the robustness of the anonymized speech against privacy attacks and speech deterioration show an overall success of this system for all languages. The results suggest that speaker embeddings trained on English data can be applied across languages, and that the anonymization performance for a language is mainly affected by the quality of the speech synthesis component used for it.

</details>

### [Robust Zero-Shot Text-to-Speech Synthesis with Reverse Inference Optimization](2407.02243.md)
**Yuchen Hu et.al.** · 2024-07-02

### [TTSlow: Slow Down Text-to-Speech with Efficiency Robustness Evaluations](2407.01927.md)
**Xiaoxue Gao, Yiming Chen, Xianghu Yue, Yu Tsao et al.** · 2024-07-02

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) has been extensively studied for generating high-quality speech with textual inputs, playing a crucial role in various real-time applications. For real-world deployment, ensuring stable and timely generation in TTS models against minor input perturbations is of paramount importance. Therefore, evaluating the robustness of TTS models against such perturbations, commonly known as adversarial attacks, is highly desirable. In this paper, we propose TTSlow, a novel adversarial approach specifically tailored to slow down the speech generation process in TTS systems. To induce long TTS waiting time, we design novel efficiency-oriented adversarial loss to encourage endless generation process. TTSlow encompasses two attack strategies targeting both text inputs and speaker embedding. Specifically, we propose TTSlow-text, which utilizes a combination of homoglyphs-based and swap-based perturbations, along with TTSlow-spk, which employs a gradient optimization attack approach for speaker embedding. TTSlow serves as the first attack approach targeting a wide range of TTS models, including autoregressive and non-autoregressive TTS ones, thereby advancing exploration in audio security. Extensive experiments are conducted to evaluate the inference efficiency of TTS models, and in-depth analysis of generated speech intelligibility is performed using Gemini. The results demonstrate that TTSlow can effectively slow down two TTS models across three publicly available datasets. We are committed to releasing the source code upon acceptance, facilitating further research and benchmarking in this domain.

</details>

### [Lightweight Zero-shot Text-to-Speech with Mixture of Adapters](2407.01291.md)
**Kenichi Fujita et.al.** · 2024-07-01

### [A Comprehensive Survey on Diffusion Models and Their Applications](2408.10207.md)
**Md Manjurul Ahsan, Shivakumar Raman, Yingtao Liu, Zahed Siddique** · 2024-07-01

<details>
<summary>Abstract</summary>

Diffusion Models are probabilistic models that create realistic samples by simulating the diffusion process, gradually adding and removing noise from data. These models have gained popularity in domains such as image processing, speech synthesis, and natural language processing due to their ability to produce high-quality samples. As Diffusion Models are being adopted in various domains, existing literature reviews that often focus on specific areas like computer vision or medical imaging may not serve a broader audience across multiple fields. Therefore, this review presents a comprehensive overview of Diffusion Models, covering their theoretical foundations and algorithmic innovations. We highlight their applications in diverse areas such as media quality, authenticity, synthesis, image transformation, healthcare, and more. By consolidating current knowledge and identifying emerging trends, this review aims to facilitate a deeper understanding and broader adoption of Diffusion Models and provide guidelines for future researchers and practitioners across diverse disciplines.

</details>

### [Planning the development of text-to-speech synthesis models and datasets with dynamic deep learning](s2:9b84b9ae41797c1299bab333e69b63604d7cc1de.md)
**Hawraz A. Ahmad, Tarik Ahmed Rashid** · 2024-07-01

<details>
<summary>Abstract</summary>

Synthesis of Text-to-speech (TTS) is a process that involves translating a natural language text into a speech. Speech synthesisers face a major challenge when recognizing the prosodic elements of written text, such as intonation (the rise and fall of the voice in speaking), and length. In contrast, continuous speech features are influenced by the personality and emotions of the artist. A database is maintained to store the synthesized speech pieces. Its output is determined by how similar the person utters the words and how capable they are of being implied. In the past few years, the field of text-to-speech synthesis has been heavily impacted by the emergence of deep learning, an AI technology that has gained widespread popularity. This review paper presents a taxonomy of models and architectures that are based on deep learning and discusses the various datasets that are utilised in the TTS process. It also covers the evaluation matrices that are commonly used. The paper ends with a look at the future directions of the system and reaches to some Deep learning models that give promising results in this field.

</details>

### [FLY-TTS: Fast, Lightweight and High-Quality End-to-End Text-to-Speech Synthesis](2407.00753.md)
**Yinlin Guo et.al.** · 2024-06-30

### [NAIST Simultaneous Speech Translation System for IWSLT 2024](2407.00826.md)
**Yuka Ko, Ryo Fukuda, Yuta Nishikawa, Yasumasa Kano et al.** · 2024-06-30

<details>
<summary>Abstract</summary>

This paper describes NAIST's submission to the simultaneous track of the IWSLT 2024 Evaluation Campaign: English-to-{German, Japanese, Chinese} speech-to-text translation and English-to-Japanese speech-to-speech translation. We develop a multilingual end-to-end speech-to-text translation model combining two pre-trained language models, HuBERT and mBART. We trained this model with two decoding policies, Local Agreement (LA) and AlignAtt. The submitted models employ the LA policy because it outperformed the AlignAtt policy in previous models. Our speech-to-speech translation method is a cascade of the above speech-to-text model and an incremental text-to-speech (TTS) module that incorporates a phoneme estimation model, a parallel acoustic model, and a parallel WaveGAN vocoder. We improved our incremental TTS by applying the Transformer architecture with the AlignAtt policy for the estimation model. The results show that our upgraded TTS module contributed to improving the system performance.

</details>

### [An Attribute Interpolation Method in Speech Synthesis by Model Merging](2407.00766.md)
**Masato Murata, Koichi Miyazaki, Tomoki Koriyama** · 2024-06-30

<details>
<summary>Abstract</summary>

With the development of speech synthesis, recent research has focused on challenging tasks, such as speaker generation and emotion intensity control. Attribute interpolation is a common approach to these tasks. However, most previous methods for attribute interpolation require specific modules or training methods. We propose an attribute interpolation method in speech synthesis by model merging. Model merging is a method that creates new parameters by only averaging the parameters of base models. The merged model can generate an output with an intermediate feature of the base models. This method is easily applicable without specific modules or training methods, as it uses only existing trained base models. We merged two text-to-speech models to achieve attribute interpolation and evaluated its performance on speaker generation and emotion intensity control tasks. As a result, our proposed method achieved smooth attribute interpolation while keeping the linguistic content in both tasks.

</details>

### [DEX-TTS: Diffusion-based EXpressive Text-to-Speech with Style Modeling on Time Variability](2406.19135.md)
**Hyun Joon Park et.al.** · 2024-06-27

### [E2 TTS: Embarrassingly Easy Fully Non-Autoregressive Zero-Shot TTS](2406.18009.md)
**Sefik Emre Eskimez et.al.** · 2024-06-26

### [A Study on Synthesizing Expressive Violin Performances: Approaches and Comparisons](2406.18089.md)
**Tzu-Yun Hung, Jui-Te Wu, Yu-Chia Kuo, Yo-Wei Hsiao et al.** · 2024-06-26

<details>
<summary>Abstract</summary>

Expressive music synthesis (EMS) for violin performance is a challenging task due to the disagreement among music performers in the interpretation of expressive musical terms (EMTs), scarcity of labeled recordings, and limited generalization ability of the synthesis model. These challenges create trade-offs between model effectiveness, diversity of generated results, and controllability of the synthesis system, making it essential to conduct a comparative study on EMS model design. This paper explores two violin EMS approaches. The end-to-end approach is a modification of a state-of-the-art text-to-speech generator. The parameter-controlled approach is based on a simple parameter sampling process that can render note lengths and other parameters compatible with MIDI-DDSP. We study these two approaches (in total, three model variants) through objective and subjective experiments and discuss several key issues of EMS based on the results.

</details>

### [LLM-Driven Multimodal Opinion Expression Identification](2406.18088.md)
**Bonian Jia, Huiyao Chen, Yueheng Sun, Meishan Zhang et al.** · 2024-06-26

<details>
<summary>Abstract</summary>

Opinion Expression Identification (OEI) is essential in NLP for applications ranging from voice assistants to depression diagnosis. This study extends OEI to encompass multimodal inputs, underlining the significance of auditory cues in delivering emotional subtleties beyond the capabilities of text. We introduce a novel multimodal OEI (MOEI) task, integrating text and speech to mirror real-world scenarios. Utilizing CMU MOSEI and IEMOCAP datasets, we construct the CI-MOEI dataset. Additionally, Text-to-Speech (TTS) technology is applied to the MPQA dataset to obtain the CIM-OEI dataset. We design a template for the OEI task to take full advantage of the generative power of large language models (LLMs). Advancing further, we propose an LLM-driven method STOEI, which combines speech and text modal to identify opinion expressions. Our experiments demonstrate that MOEI significantly improves the performance while our method outperforms existing methods by 9.20\% and obtains SOTA results.

</details>

### [Improving Robustness of LLM-based Speech Synthesis by Learning Monotonic Alignment](2406.17957.md)
**Paarth Neekhara et.al.** · 2024-06-25

### [High Fidelity Text-to-Speech Via Discrete Tokens Using Token Transducer and Group Masked Language Model](2406.17310.md)
**Joun Yeop Lee et.al.** · 2024-06-25

### [Leveraging Parameter-Efficient Transfer Learning for Multi-Lingual Text-to-Speech Adaptation](2406.17257.md)
**Yingting Li et.al.** · 2024-06-25

### [Towards Zero-Shot Text-To-Speech for Arabic Dialects](2406.16751.md)
**Khai Duy Doan et.al.** · 2024-06-25

### [Spatial Voice Conversion: Voice Conversion Preserving Spatial Information and Non-target Signals](2406.17722.md)
**Kentaro Seki, Shinnosuke Takamichi, Norihiro Takamune, Yuki Saito et al.** · 2024-06-25

<details>
<summary>Abstract</summary>

This paper proposes a new task called spatial voice conversion, which aims to convert a target voice while preserving spatial information and non-target signals. Traditional voice conversion methods focus on single-channel waveforms, ignoring the stereo listening experience inherent in human hearing. Our baseline approach addresses this gap by integrating blind source separation (BSS), voice conversion (VC), and spatial mixing to handle multi-channel waveforms. Through experimental evaluations, we organize and identify the key challenges inherent in this task, such as maintaining audio quality and accurately preserving spatial information. Our results highlight the fundamental difficulties in balancing these aspects, providing a benchmark for future research in spatial voice conversion. The proposed method's code is publicly available to encourage further exploration in this domain.

</details>

### [One-Class Learning with Adaptive Centroid Shift for Audio Deepfake Detection](2406.16716.md)
**Hyun Myung Kim, Kangwook Jang, Hoirin Kim** · 2024-06-24

<details>
<summary>Abstract</summary>

As speech synthesis systems continue to make remarkable advances in recent years, the importance of robust deepfake detection systems that perform well in unseen systems has grown. In this paper, we propose a novel adaptive centroid shift (ACS) method that updates the centroid representation by continually shifting as the weighted average of bonafide representations. Our approach uses only bonafide samples to define their centroid, which can yield a specialized centroid for one-class learning. Integrating our ACS with one-class learning gathers bonafide representations into a single cluster, forming well-separated embeddings robust to unseen spoofing attacks. Our proposed method achieves an equal error rate (EER) of 2.19% on the ASVspoof 2021 deepfake dataset, outperforming all existing systems. Furthermore, the t-SNE visualization illustrates that our method effectively maps the bonafide embeddings into a single cluster and successfully disentangles the bonafide and spoof classes.

</details>

### [RefXVC: Cross-Lingual Voice Conversion with Enhanced Reference Leveraging](2406.16326.md)
**Mingyang Zhang, Yi Zhou, Yi Ren, Chen Zhang et al.** · 2024-06-24

<details>
<summary>Abstract</summary>

This paper proposes RefXVC, a method for cross-lingual voice conversion (XVC) that leverages reference information to improve conversion performance. Previous XVC works generally take an average speaker embedding to condition the speaker identity, which does not account for the changing timbre of speech that occurs with different pronunciations. To address this, our method uses both global and local speaker embeddings to capture the timbre changes during speech conversion. Additionally, we observed a connection between timbre and pronunciation in different languages and utilized this by incorporating a timbre encoder and a pronunciation matching network into our model. Furthermore, we found that the variation in tones is not adequately reflected in a sentence, and therefore, we used multiple references to better capture the range of a speaker's voice. The proposed method outperformed existing systems in terms of both speech quality and speaker similarity, highlighting the effectiveness of leveraging reference information in cross-lingual voice conversion. The converted speech samples can be found on the website: \url{http://refxvc.dn3point.com}

</details>

### [DreamVoice: Text-Guided Voice Conversion](2406.16314.md)
**Jiarui Hai, Karan Thakkar, Helin Wang, Zengyi Qin et al.** · 2024-06-24

<details>
<summary>Abstract</summary>

Generative voice technologies are rapidly evolving, offering opportunities for more personalized and inclusive experiences. Traditional one-shot voice conversion (VC) requires a target recording during inference, limiting ease of usage in generating desired voice timbres. Text-guided generation offers an intuitive solution to convert voices to desired "DreamVoices" according to the users' needs. Our paper presents two major contributions to VC technology: (1) DreamVoiceDB, a robust dataset of voice timbre annotations for 900 speakers from VCTK and LibriTTS. (2) Two text-guided VC methods: DreamVC, an end-to-end diffusion-based text-guided VC model; and DreamVG, a versatile text-to-voice generation plugin that can be combined with any one-shot VC models. The experimental results demonstrate that our proposed methods trained on the DreamVoiceDB dataset generate voice timbres accurately aligned with the text prompt and achieve high-quality VC.

</details>

### [TacoLM: GaTed Attention Equipped Codec Language Model are Efficient Zero-Shot Text to Speech Synthesizers](2406.15752.md)
**Yakun Song et.al.** · 2024-06-22

### [A multi-speaker multi-lingual voice cloning system based on vits2 for limmits 2024 challenge](2406.17801.md)
**Xiaopeng Wang, Yi Lu, Xin Qi, Zhiyong Wang et al.** · 2024-06-22

<details>
<summary>Abstract</summary>

This paper presents the development of a speech synthesis system for the LIMMITS'24 Challenge, focusing primarily on Track 2. The objective of the challenge is to establish a multi-speaker, multi-lingual Indic Text-to-Speech system with voice cloning capabilities, covering seven Indian languages with both male and female speakers. The system was trained using challenge data and fine-tuned for few-shot voice cloning on target speakers. Evaluation included both mono-lingual and cross-lingual synthesis across all seven languages, with subjective tests assessing naturalness and speaker similarity. Our system uses the VITS2 architecture, augmented with a multi-lingual ID and a BERT model to enhance contextual language comprehension. In Track 1, where no additional data usage was permitted, our model achieved a Speaker Similarity score of 4.02. In Track 2, which allowed the use of extra data, it attained a Speaker Similarity score of 4.17.

</details>

### [Improving Unsupervised Clean-to-Rendered Guitar Tone Transformation Using GANs and Integrated Unaligned Clean Data](2406.15751.md)
**Yu-Hua Chen, Woosung Choi, Wei-Hsiang Liao, Marco Martínez-Ramírez et al.** · 2024-06-22

<details>
<summary>Abstract</summary>

Recent years have seen increasing interest in applying deep learning methods to the modeling of guitar amplifiers or effect pedals. Existing methods are mainly based on the supervised approach, requiring temporally-aligned data pairs of unprocessed and rendered audio. However, this approach does not scale well, due to the complicated process involved in creating the data pairs. A very recent work done by Wright et al. has explored the potential of leveraging unpaired data for training, using a generative adversarial network (GAN)-based framework. This paper extends their work by using more advanced discriminators in the GAN, and using more unpaired data for training. Specifically, drawing inspiration from recent advancements in neural vocoders, we employ in our GAN-based model for guitar amplifier modeling two sets of discriminators, one based on multi-scale discriminator (MSD) and the other multi-period discriminator (MPD). Moreover, we experiment with adding unprocessed audio signals that do not have the corresponding rendered audio of a target tone to the training data, to see how much the GAN model benefits from the unpaired data. Our experiments show that the proposed two extensions contribute to the modeling of both low-gain and high-gain guitar amplifiers.

</details>

### [GLOBE: A High-quality English Corpus with Global Accents for Zero-shot Speaker Adaptive Text-to-Speech](2406.14875.md)
**Wenbin Wang et.al.** · 2024-06-21

### [Instruction Data Generation and Unsupervised Adaptation for Speech Language Models](2406.12946.md)
**Vahid Noroozi et.al.** · 2024-06-18

### [A Mel Spectrogram Enhancement Paradigm Based on CWT in Speech Synthesis](2406.12164.md)
**Guoqiang Hu, Huaning Tan, Ruilai Li** · 2024-06-18

<details>
<summary>Abstract</summary>

Acoustic features play an important role in improving the quality of the synthesised speech. Currently, the Mel spectrogram is a widely employed acoustic feature in most acoustic models. However, due to the fine-grained loss caused by its Fourier transform process, the clarity of speech synthesised by Mel spectrogram is compromised in mutant signals. In order to obtain a more detailed Mel spectrogram, we propose a Mel spectrogram enhancement paradigm based on the continuous wavelet transform (CWT). This paradigm introduces an additional task: a more detailed wavelet spectrogram, which like the post-processing network takes as input the Mel spectrogram output by the decoder. We choose Tacotron2 and Fastspeech2 for experimental validation in order to test autoregressive (AR) and non-autoregressive (NAR) speech systems, respectively. The experimental results demonstrate that the speech synthesised using the model with the Mel spectrogram enhancement paradigm exhibits higher MOS, with an improvement of 0.14 and 0.09 compared to the baseline model, respectively. These findings provide some validation for the universality of the enhancement paradigm, as they demonstrate the success of the paradigm in different architectures.

</details>

### [Coding Speech through Vocal Tract Kinematics](2406.12998.md)
**Cheol Jun Cho, Peter Wu, Tejas S. Prabhune, Dhruv Agarwal et al.** · 2024-06-18

<details>
<summary>Abstract</summary>

Vocal tract articulation is a natural, grounded control space of speech production. The spatiotemporal coordination of articulators combined with the vocal source shapes intelligible speech sounds to enable effective spoken communication. Based on this physiological grounding of speech, we propose a new framework of neural encoding-decoding of speech -- Speech Articulatory Coding (SPARC). SPARC comprises an articulatory analysis model that infers articulatory features from speech audio, and an articulatory synthesis model that synthesizes speech audio from articulatory features. The articulatory features are kinematic traces of vocal tract articulators and source features, which are intuitively interpretable and controllable, being the actual physical interface of speech production. An additional speaker identity encoder is jointly trained with the articulatory synthesizer to inform the voice texture of individual speakers. By training on large-scale speech data, we achieve a fully intelligible, high-quality articulatory synthesizer that generalizes to unseen speakers. Furthermore, the speaker embedding is effectively disentangled from articulations, which enables accent-perserving zero-shot voice conversion. To the best of our knowledge, this is the first demonstration of universal, high-performance articulatory inference and synthesis, suggesting the proposed framework as a powerful coding system of speech.

</details>

### [Speak in the Scene: Diffusion-based Acoustic Scene Transfer toward Immersive Speech Generation](2406.12688.md)
**Miseul Kim, Soo-Whan Chung, Youna Ji, Hong-Goo Kang et al.** · 2024-06-18

<details>
<summary>Abstract</summary>

This paper introduces a novel task in generative speech processing, Acoustic Scene Transfer (AST), which aims to transfer acoustic scenes of speech signals to diverse environments. AST promises an immersive experience in speech perception by adapting the acoustic scene behind speech signals to desired environments. We propose AST-LDM for the AST task, which generates speech signals accompanied by the target acoustic scene of the reference prompt. Specifically, AST-LDM is a latent diffusion model conditioned by CLAP embeddings that describe target acoustic scenes in either audio or text modalities. The contributions of this paper include introducing the AST task and implementing its baseline model. For AST-LDM, we emphasize its core framework, which is to preserve the input speech and generate audio consistently with both the given speech and the target acoustic environment. Experiments, including objective and subjective tests, validate the feasibility and efficacy of our approach.

</details>

### [DiTTo-TTS: Efficient and Scalable Zero-Shot Text-to-Speech with Diffusion Transformer](2406.11427.md)
**Keon Lee et.al.** · 2024-06-17

### [1000 African Voices: Advancing inclusive multi-speaker multi-accent speech synthesis](2406.11727.md)
**Sewade Ogun, Abraham T. Owodunni, Tobi Olatunji, Eniola Alese et al.** · 2024-06-17

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis have enabled many useful applications like audio directions in Google Maps, screen readers, and automated content generation on platforms like TikTok. However, these systems are mostly dominated by voices sourced from data-rich geographies with personas representative of their source data. Although 3000 of the world's languages are domiciled in Africa, African voices and personas are under-represented in these systems. As speech synthesis becomes increasingly democratized, it is desirable to increase the representation of African English accents. We present Afro-TTS, the first pan-African accented English speech synthesis system able to generate speech in 86 African accents, with 1000 personas representing the rich phonological diversity across the continent for downstream application in Education, Public Health, and Automated Content Creation. Speaker interpolation retains naturalness and accentedness, enabling the creation of new voices.

</details>

### [NAST: Noise Aware Speech Tokenization for Speech Language Models](2406.11037.md)
**Shoval Messica et.al.** · 2024-06-16

### [Multi-Scale Accent Modeling and Disentangling for Multi-Speaker Multi-Accent Text-to-Speech Synthesis](2406.10844.md)
**Xuehao Zhou, Mingyang Zhang, Yi Zhou, Zhizheng Wu et al.** · 2024-06-16

<details>
<summary>Abstract</summary>

Generating speech across different accents while preserving speaker identity is crucial for various real-world applications. However, accurately and independently modeling both speaker and accent characteristics in text-to-speech (TTS) systems is challenging due to the complex variations of accents and the inherent entanglement between speaker and accent identities. In this paper, we propose a novel approach for multi-speaker multi-accent TTS synthesis that aims to synthesize speech for multiple speakers, each with various accents. Our approach employs a multi-scale accent modeling strategy to address accent variations on different levels. Specifically, we introduce both global (utterance level) and local (phoneme level) accent modeling to capture overall accent characteristics within an utterance and fine-grained accent variations across phonemes, respectively. To enable independent control of speakers and accents, we use the speaker embedding to represent speaker identity and achieve speaker-independent accent control through speaker disentanglement within the multi-scale accent modeling. Additionally, we present a local accent prediction model that enables our system to generate accented speech directly from phoneme inputs. We conduct extensive experiments on an English accented speech corpus. Experimental results demonstrate that our proposed system outperforms baseline systems in terms of speech quality and accent rendering for generating multi-speaker multi-accent speech. Ablation studies further validate the effectiveness of different components in our proposed system.

</details>

### [SingMOS: An extensive Open-Source Singing Voice Dataset for MOS Prediction](2406.10911.md)
**Yuxun Tang, Jiatong Shi, Yuning Wu, Qin Jin** · 2024-06-16

<details>
<summary>Abstract</summary>

In speech generation tasks, human subjective ratings, usually referred to as the opinion score, are considered the "gold standard" for speech quality evaluation, with the mean opinion score (MOS) serving as the primary evaluation metric. Due to the high cost of human annotation, several MOS prediction systems have emerged in the speech domain, demonstrating good performance. These MOS prediction models are trained using annotations from previous speech-related challenges. However, compared to the speech domain, the singing domain faces data scarcity and stricter copyright protections, leading to a lack of high-quality MOS-annotated datasets for singing. To address this, we propose SingMOS, a high-quality and diverse MOS dataset for singing, covering a range of Chinese and Japanese datasets. These synthesized vocals are generated using state-of-the-art models in singing synthesis, conversion, or resynthesis tasks and are rated by professional annotators alongside real vocals. Data analysis demonstrates the diversity and reliability of our dataset. Additionally, we conduct further exploration on SingMOS, providing insights for singing MOS prediction and guidance for the continued expansion of SingMOS.

</details>

### [GTR-Voice: Articulatory Phonetics Informed Controllable Expressive Speech Synthesis](2406.10514.md)
**Zehua Kcriss Li, Meiying Melissa Chen, Yi Zhong, Pinxin Liu et al.** · 2024-06-15

<details>
<summary>Abstract</summary>

Expressive speech synthesis aims to generate speech that captures a wide range of para-linguistic features, including emotion and articulation, though current research primarily emphasizes emotional aspects over the nuanced articulatory features mastered by professional voice actors. Inspired by this, we explore expressive speech synthesis through the lens of articulatory phonetics. Specifically, we define a framework with three dimensions: Glottalization, Tenseness, and Resonance (GTR), to guide the synthesis at the voice production level. With this framework, we record a high-quality speech dataset named GTR-Voice, featuring 20 Chinese sentences articulated by a professional voice actor across 125 distinct GTR combinations. We verify the framework and GTR annotations through automatic classification and listening tests, and demonstrate precise controllability along the GTR dimensions on two fine-tuned expressive TTS models. We open-source the dataset and TTS models.

</details>

### [UniAudio 1.5: Large Language Model-driven Audio Codec is A Few-shot Audio Task Learner](2406.10056.md)
**Dongchao Yang et.al.** · 2024-06-14

### [Phoneme Discretized Saliency Maps for Explainable Detection of AI-Generated Voice](2406.10422.md)
**Shubham Gupta, Mirco Ravanelli, Pascal Germain, Cem Subakan** · 2024-06-14

<details>
<summary>Abstract</summary>

In this paper, we propose Phoneme Discretized Saliency Maps (PDSM), a discretization algorithm for saliency maps that takes advantage of phoneme boundaries for explainable detection of AI-generated voice. We experimentally show with two different Text-to-Speech systems (i.e., Tacotron2 and Fastspeech2) that the proposed algorithm produces saliency maps that result in more faithful explanations compared to standard posthoc explanation methods. Moreover, by associating the saliency maps to the phoneme representations, this methodology generates explanations that tend to be more understandable than standard saliency maps on magnitude spectrograms.

</details>

### [Vec-Tok-VC+: Residual-enhanced Robust Zero-shot Voice Conversion with Progressive Constraints in a Dual-mode Training Strategy](2406.09844.md)
**Linhan Ma, Xinfa Zhu, Yuanjun Lv, Zhichao Wang et al.** · 2024-06-14

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) aims to transform source speech into arbitrary unseen target voice while keeping the linguistic content unchanged. Recent VC methods have made significant progress, but semantic losses in the decoupling process as well as training-inference mismatch still hinder conversion performance. In this paper, we propose Vec-Tok-VC+, a novel prompt-based zero-shot VC model improved from Vec-Tok Codec, achieving voice conversion given only a 3s target speaker prompt. We design a residual-enhanced K-Means decoupler to enhance the semantic content extraction with a two-layer clustering process. Besides, we employ teacher-guided refinement to simulate the conversion process to eliminate the training-inference mismatch, forming a dual-mode training strategy. Furthermore, we design a multi-codebook progressive loss function to constrain the layer-wise output of the model from coarse to fine to improve speaker similarity and content accuracy. Objective and subjective evaluations demonstrate that Vec-Tok-VC+ outperforms the strong baselines in naturalness, intelligibility, and speaker similarity.

</details>

### [Generating Speakers by Prompting Listener Impressions for Pre-trained Multi-Speaker Text-to-Speech Systems](2406.08812.md)
**Zhengyang Chen et.al.** · 2024-06-13

### [DubWise: Video-Guided Speech Duration Control in Multimodal LLM-based Text-to-Speech for Dubbing](2406.08802.md)
**Neha Sahipjohn et.al.** · 2024-06-13

### [DisfluencySpeech -- Single-Speaker Conversational Speech Dataset with Paralanguage](2406.08820.md)
**Kyra Wang, Dorien Herremans** · 2024-06-13

<details>
<summary>Abstract</summary>

Laughing, sighing, stuttering, and other forms of paralanguage do not contribute any direct lexical meaning to speech, but they provide crucial propositional context that aids semantic and pragmatic processes such as irony. It is thus important for artificial social agents to both understand and be able to generate speech with semantically-important paralanguage. Most speech datasets do not include transcribed non-lexical speech sounds and disfluencies, while those that do are typically multi-speaker datasets where each speaker provides relatively little audio. This makes it challenging to train conversational Text-to-Speech (TTS) synthesis models that include such paralinguistic components. We thus present DisfluencySpeech, a studio-quality labeled English speech dataset with paralanguage. A single speaker recreates nearly 10 hours of expressive utterances from the Switchboard-1 Telephone Speech Corpus (Switchboard), simulating realistic informal conversations. To aid the development of a TTS model that is able to predictively synthesise paralanguage from text without such components, we provide three different transcripts at different levels of information removal (removal of non-speech events, removal of non-sentence elements, and removal of false starts), as well as benchmark TTS models trained on each of these levels.

</details>

### [SingOMD: Singing Oriented Multi-resolution Discrete Representation Construction from Speech Models](2406.08905.md)
**Yuxun Tang, Yuning Wu, Jiatong Shi, Qin Jin** · 2024-06-13

<details>
<summary>Abstract</summary>

Discrete representation has shown advantages in speech generation tasks, wherein discrete tokens are derived by discretizing hidden features from self-supervised learning (SSL) pre-trained models. However, the direct application of speech SSL models to singing generation encounters domain gaps between speech and singing. Furthermore, singing generation necessitates a more refined representation than typical speech. To address these challenges, we introduce SingOMD, a novel method to extract singing-oriented multi-resolution discrete representations from speech SSL models. Specifically, we first adapt the features from speech SSL through a resynthesis task and incorporate multi-resolution modules based on resampling to better serve singing generation. These adapted multi-resolution features are then discretized via clustering. Extensive experiments demonstrate the robustness, efficiency, and effectiveness of these representations in singing vocoders and singing voice synthesis.

</details>

### [Audio-conditioned phonemic and prosodic annotation for building text-to-speech models from unlabeled speech data](2406.08111.md)
**Yuma Shirahata et.al.** · 2024-06-12

### [LibriTTS-P: A Corpus with Speaking Style and Speaker Identity Prompts for Text-to-Speech and Style Captioning](2406.07969.md)
**Masaya Kawamura et.al.** · 2024-06-12

### [VALL-E R: Robust and Efficient Zero-Shot Text-to-Speech Synthesis via Monotonic Alignment](2406.07855.md)
**Bing Han et.al.** · 2024-06-12

### [VECL-TTS: Voice identity and Emotional style controllable Cross-Lingual Text-to-Speech](2406.08076.md)
**Ashishkumar Gudmalwar, Nirmesh Shah, Sai Akarsh, Pankaj Wasnik et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

Despite the significant advancements in Text-to-Speech (TTS) systems, their full utilization in automatic dubbing remains limited. This task necessitates the extraction of voice identity and emotional style from a reference speech in a source language and subsequently transferring them to a target language using cross-lingual TTS techniques. While previous approaches have mainly concentrated on controlling voice identity within the cross-lingual TTS framework, there has been limited work on incorporating emotion and voice identity together. To this end, we introduce an end-to-end Voice Identity and Emotional Style Controllable Cross-Lingual (VECL) TTS system using multilingual speakers and an emotion embedding network. Moreover, we introduce content and style consistency losses to enhance the quality of synthesized speech further. The proposed system achieved an average relative improvement of 8.83\% compared to the state-of-the-art (SOTA) methods on a database comprising English and three Indian languages (Hindi, Telugu, and Marathi).

</details>

### [TokSing: Singing Voice Synthesis based on Discrete Tokens](2406.08416.md)
**Yuning Wu, Chunlei zhang, Jiatong Shi, Yuxun Tang et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

Recent advancements in speech synthesis witness significant benefits by leveraging discrete tokens extracted from self-supervised learning (SSL) models. Discrete tokens offer higher storage efficiency and greater operability in intermediate representations compared to traditional continuous Mel spectrograms. However, when it comes to singing voice synthesis(SVS), achieving higher levels of melody expression poses a great challenge for utilizing discrete tokens. In this paper, we introduce TokSing, a discrete-based SVS system equipped with a token formulator that offers flexible token blendings. We observe a melody degradation during discretization, prompting us to integrate a melody signal with the discrete token and incorporate a specially-designed melody enhancement strategy in the musical encoder. Extensive experiments demonstrate that our TokSing achieves better performance against the Mel spectrogram baselines while offering advantages in intermediate representation space cost and convergence speed.

</details>

### [FreeV: Free Lunch For Vocoders Through Pseudo Inversed Mel Filter](2406.08196.md)
**Yuanjun Lv, Hai Li, Ying Yan, Junhui Liu et al.** · 2024-06-12

<details>
<summary>Abstract</summary>

Vocoders reconstruct speech waveforms from acoustic features and play a pivotal role in modern TTS systems. Frequent-domain GAN vocoders like Vocos and APNet2 have recently seen rapid advancements, outperforming time-domain models in inference speed while achieving comparable audio quality. However, these frequency-domain vocoders suffer from large parameter sizes, thus introducing extra memory burden. Inspired by PriorGrad and SpecGrad, we employ pseudo-inverse to estimate the amplitude spectrum as the initialization roughly. This simple initialization significantly mitigates the parameter demand for vocoder. Based on APNet2 and our streamlined Amplitude prediction branch, we propose our FreeV, compared with its counterpart APNet2, our FreeV achieves 1.8 times inference speed improvement with nearly half parameters. Meanwhile, our FreeV outperforms APNet2 in resynthesis quality, marking a step forward in pursuing real-time, high-fidelity speech synthesis. Code and checkpoints is available at: https://github.com/BakerBunker/FreeV

</details>

### [SVSNet+: Enhancing Speaker Voice Similarity Assessment Models with Representations from Speech Foundation Models](2406.08445.md)
**Chun Yin, Tai-Shih Chi, Yu Tsao, Hsin-Min Wang** · 2024-06-12

<details>
<summary>Abstract</summary>

Representations from pre-trained speech foundation models (SFMs) have shown impressive performance in many downstream tasks. However, the potential benefits of incorporating pre-trained SFM representations into speaker voice similarity assessment have not been thoroughly investigated. In this paper, we propose SVSNet+, a model that integrates pre-trained SFM representations to improve performance in assessing speaker voice similarity. Experimental results on the Voice Conversion Challenge 2018 and 2020 datasets show that SVSNet+ incorporating WavLM representations shows significant improvements compared to baseline models. In addition, while fine-tuning WavLM with a small dataset of the downstream task does not improve performance, using the same dataset to learn a weighted-sum representation of WavLM can substantially improve performance. Furthermore, when WavLM is replaced by other SFMs, SVSNet+ still outperforms the baseline models and exhibits strong generalization ability.

</details>

### [Asynchronous Voice Anonymization Using Adversarial Perturbation On Speaker Embedding](2406.08200.md)
**Rui Wang, Liping Chen, Kong AiK Lee, Zhen-Hua Ling** · 2024-06-12

<details>
<summary>Abstract</summary>

Voice anonymization has been developed as a technique for preserving privacy by replacing the speaker's voice in a speech signal with that of a pseudo-speaker, thereby obscuring the original voice attributes from machine recognition and human perception. In this paper, we focus on altering the voice attributes against machine recognition while retaining human perception. We referred to this as the asynchronous voice anonymization. To this end, a speech generation framework incorporating a speaker disentanglement mechanism is employed to generate the anonymized speech. The speaker attributes are altered through adversarial perturbation applied on the speaker embedding, while human perception is preserved by controlling the intensity of perturbation. Experiments conducted on the LibriSpeech dataset showed that the speaker attributes were obscured with their human perception preserved for 60.71% of the processed utterances.

</details>

### [WenetSpeech4TTS: A 12,800-hour Mandarin TTS Corpus for Large Speech Generation Model Benchmark](2406.05763.md)
**Linhan Ma et.al.** · 2024-06-11

### [Can We Achieve High-quality Direct Speech-to-Speech Translation without Parallel Speech Data?](2406.07289.md)
**Qingkai Fang, Shaolei Zhang, Zhengrui Ma, Min Zhang et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

Recently proposed two-pass direct speech-to-speech translation (S2ST) models decompose the task into speech-to-text translation (S2TT) and text-to-speech (TTS) within an end-to-end model, yielding promising results. However, the training of these models still relies on parallel speech data, which is extremely challenging to collect. In contrast, S2TT and TTS have accumulated a large amount of data and pretrained models, which have not been fully utilized in the development of S2ST models. Inspired by this, in this paper, we first introduce a composite S2ST model named ComSpeech, which can seamlessly integrate any pretrained S2TT and TTS models into a direct S2ST model. Furthermore, to eliminate the reliance on parallel speech data, we propose a novel training method ComSpeech-ZS that solely utilizes S2TT and TTS data. It aligns representations in the latent space through contrastive learning, enabling the speech synthesis capability learned from the TTS data to generalize to S2ST in a zero-shot manner. Experimental results on the CVSS dataset show that when the parallel speech data is available, ComSpeech surpasses previous two-pass models like UnitY and Translatotron 2 in both translation quality and decoding speed. When there is no parallel speech data, ComSpeech-ZS lags behind \name by only 0.7 ASR-BLEU and outperforms the cascaded models.

</details>

### [AudioMarkBench: Benchmarking Robustness of Audio Watermarking](2406.06979.md)
**Hongbin Liu, Moyang Guo, Zhengyuan Jiang, Lun Wang et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

The increasing realism of synthetic speech, driven by advancements in text-to-speech models, raises ethical concerns regarding impersonation and disinformation. Audio watermarking offers a promising solution via embedding human-imperceptible watermarks into AI-generated audios. However, the robustness of audio watermarking against common/adversarial perturbations remains understudied. We present AudioMarkBench, the first systematic benchmark for evaluating the robustness of audio watermarking against watermark removal and watermark forgery. AudioMarkBench includes a new dataset created from Common-Voice across languages, biological sexes, and ages, 3 state-of-the-art watermarking methods, and 15 types of perturbations. We benchmark the robustness of these methods against the perturbations in no-box, black-box, and white-box settings. Our findings highlight the vulnerabilities of current watermarking techniques and emphasize the need for more robust and fair audio watermarking solutions. Our dataset and code are publicly available at https://github.com/moyangkuo/AudioMarkBench.

</details>

### [A Non-autoregressive Generation Framework for End-to-End Simultaneous Speech-to-Speech Translation](2406.06937.md)
**Zhengrui Ma, Qingkai Fang, Shaolei Zhang, Shoutao Guo et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

Simultaneous translation models play a crucial role in facilitating communication. However, existing research primarily focuses on text-to-text or speech-to-text models, necessitating additional cascade components to achieve speech-to-speech translation. These pipeline methods suffer from error propagation and accumulate delays in each cascade component, resulting in reduced synchronization between the speaker and listener. To overcome these challenges, we propose a novel non-autoregressive generation framework for simultaneous speech translation (NAST-S2X), which integrates speech-to-text and speech-to-speech tasks into a unified end-to-end framework. We develop a non-autoregressive decoder capable of concurrently generating multiple text or acoustic unit tokens upon receiving fixed-length speech chunks. The decoder can generate blank or repeated tokens and employ CTC decoding to dynamically adjust its latency. Experimental results show that NAST-S2X outperforms state-of-the-art models in both speech-to-text and speech-to-speech tasks. It achieves high-quality simultaneous interpretation within a delay of less than 3 seconds and provides a 28 times decoding speedup in offline generation.

</details>

### [CodecFake: Enhancing Anti-Spoofing Models Against Deepfake Audios from Codec-Based Speech Synthesis Systems](2406.07237.md)
**Haibin Wu, Yuan Tseng, Hung-yi Lee** · 2024-06-11

<details>
<summary>Abstract</summary>

Current state-of-the-art (SOTA) codec-based audio synthesis systems can mimic anyone's voice with just a 3-second sample from that specific unseen speaker. Unfortunately, malicious attackers may exploit these technologies, causing misuse and security issues. Anti-spoofing models have been developed to detect fake speech. However, the open question of whether current SOTA anti-spoofing models can effectively counter deepfake audios from codec-based speech synthesis systems remains unanswered. In this paper, we curate an extensive collection of contemporary SOTA codec models, employing them to re-create synthesized speech. This endeavor leads to the creation of CodecFake, the first codec-based deepfake audio dataset. Additionally, we verify that anti-spoofing models trained on commonly used datasets cannot detect synthesized speech from current codec-based speech generation systems. The proposed CodecFake dataset empowers these models to counter this challenge effectively.

</details>

### [Noise-Robust Voice Conversion by Conditional Denoising Training Using Latent Variables of Recording Quality and Environment](2406.07280.md)
**Takuto Igarashi, Yuki Saito, Kentaro Seki, Shinnosuke Takamichi et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

We propose noise-robust voice conversion (VC) which takes into account the recording quality and environment of noisy source speech. Conventional denoising training improves the noise robustness of a VC model by learning noisy-to-clean VC process. However, the naturalness of the converted speech is limited when the noise of the source speech is unseen during the training. To this end, our proposed training conditions a VC model on two latent variables representing the recording quality and environment of the source speech. These latent variables are derived from deep neural networks pre-trained on recording quality assessment and acoustic scene classification and calculated in an utterance-wise or frame-wise manner. As a result, the trained VC model can explicitly learn information about speech degradation during the training. Objective and subjective evaluations show that our training improves the quality of the converted speech compared to the conventional training.

</details>

### [SRC4VC: Smartphone-Recorded Corpus for Voice Conversion Benchmark](2406.07254.md)
**Yuki Saito, Takuto Igarashi, Kentaro Seki, Shinnosuke Takamichi et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

We present SRC4VC, a new corpus containing 11 hours of speech recorded on smartphones by 100 Japanese speakers. Although high-quality multi-speaker corpora can advance voice conversion (VC) technologies, they are not always suitable for testing VC when low-quality speech recording is given as the input. To this end, we first asked 100 crowdworkers to record their voice samples using smartphones. Then, we annotated the recorded samples with speaker-wise recording-quality scores and utterance-wise perceived emotion labels. We also benchmark SRC4VC on any-to-any VC, in which we trained a multi-speaker VC model on high-quality speech and used the SRC4VC speakers' voice samples as the source in VC. The results show that the recording quality mismatch between the training and evaluation data significantly degrades the VC performance, which can be improved by applying speech enhancement to the low-quality source speech samples.

</details>

### [Single-Codec: Single-Codebook Speech Codec towards High-Performance Speech Generation](2406.07422.md)
**Hanzhao Li, Liumeng Xue, Haohan Guo, Xinfa Zhu et al.** · 2024-06-11

<details>
<summary>Abstract</summary>

The multi-codebook speech codec enables the application of large language models (LLM) in TTS but bottlenecks efficiency and robustness due to multi-sequence prediction. To avoid this obstacle, we propose Single-Codec, a single-codebook single-sequence codec, which employs a disentangled VQ-VAE to decouple speech into a time-invariant embedding and a phonetically-rich discrete sequence. Furthermore, the encoder is enhanced with 1) contextual modeling with a BLSTM module to exploit the temporal information, 2) a hybrid sampling module to alleviate distortion from upsampling and downsampling, and 3) a resampling module to encourage discrete units to carry more phonetic information. Compared with multi-codebook codecs, e.g., EnCodec and TiCodec, Single-Codec demonstrates higher reconstruction quality with a lower bandwidth of only 304bps. The effectiveness of Single-Code is further validated by LLM-TTS experiments, showing improved naturalness and intelligibility.

</details>

### [Multimodal Belief Prediction](2406.07466.md)
**John Murzaku, Adil Soubki, Owen Rambow** · 2024-06-11

<details>
<summary>Abstract</summary>

Recognizing a speaker's level of commitment to a belief is a difficult task; humans do not only interpret the meaning of the words in context, but also understand cues from intonation and other aspects of the audio signal. Many papers and corpora in the NLP community have approached the belief prediction task using text-only approaches. We are the first to frame and present results on the multimodal belief prediction task. We use the CB-Prosody corpus (CBP), containing aligned text and audio with speaker belief annotations. We first report baselines and significant features using acoustic-prosodic features and traditional machine learning methods. We then present text and audio baselines for the CBP corpus fine-tuning on BERT and Whisper respectively. Finally, we present our multimodal architecture which fine-tunes on BERT and Whisper and uses multiple fusion methods, improving on both modalities alone.

</details>

### [MakeSinger: A Semi-Supervised Training Method for Data-Efficient Singing Voice Synthesis via Classifier-free Diffusion Guidance](2406.05965.md)
**Semin Kim et.al.** · 2024-06-10

### [Controlling Emotion in Text-to-Speech with Natural Language Prompts](2406.06406.md)
**Thomas Bott, Florian Lux, Ngoc Thang Vu** · 2024-06-10

<details>
<summary>Abstract</summary>

In recent years, prompting has quickly become one of the standard ways of steering the outputs of generative machine learning models, due to its intuitive use of natural language. In this work, we propose a system conditioned on embeddings derived from an emotionally rich text that serves as prompt. Thereby, a joint representation of speaker and prompt embeddings is integrated at several points within a transformer-based architecture. Our approach is trained on merged emotional speech and text datasets and varies prompts in each training iteration to increase the generalization capabilities of the model. Objective and subjective evaluation results demonstrate the ability of the conditioned synthesis system to accurately transfer the emotions present in a prompt to speech. At the same time, precise tractability of speaker identities as well as overall high speech quality and intelligibility are maintained.

</details>

### [Meta Learning Text-to-Speech Synthesis in over 7000 Languages](2406.06403.md)
**Florian Lux, Sarina Meyer, Lyonel Behringer, Frank Zalkow et al.** · 2024-06-10

<details>
<summary>Abstract</summary>

In this work, we take on the challenging task of building a single text-to-speech synthesis system that is capable of generating speech in over 7000 languages, many of which lack sufficient data for traditional TTS development. By leveraging a novel integration of massively multilingual pretraining and meta learning to approximate language representations, our approach enables zero-shot speech synthesis in languages without any available data. We validate our system's performance through objective measures and human evaluation across a diverse linguistic landscape. By releasing our code and models publicly, we aim to empower communities with limited linguistic resources and foster further innovation in the field of speech technology.

</details>

### [JenGAN: Stacked Shifted Filters in GAN-Based Speech Synthesis](2406.06111.md)
**Hyunjae Cho, Junhyeok Lee, Wonbin Jung** · 2024-06-10

<details>
<summary>Abstract</summary>

Non-autoregressive GAN-based neural vocoders are widely used due to their fast inference speed and high perceptual quality. However, they often suffer from audible artifacts such as tonal artifacts in their generated results. Therefore, we propose JenGAN, a new training strategy that involves stacking shifted low-pass filters to ensure the shift-equivariant property. This method helps prevent aliasing and reduce artifacts while preserving the model structure used during inference. In our experimental evaluation, JenGAN consistently enhances the performance of vocoder models, yielding significantly superior scores across the majority of evaluation metrics.

</details>

### [Learning Fine-Grained Controllability on Speech Generation via Efficient Fine-Tuning](2406.06251.md)
**Chung-Ming Chien, Andros Tjandra, Apoorv Vyas, Matt Le et al.** · 2024-06-10

<details>
<summary>Abstract</summary>

As the scale of generative models continues to grow, efficient reuse and adaptation of pre-trained models have become crucial considerations. In this work, we propose Voicebox Adapter, a novel approach that integrates fine-grained conditions into a pre-trained Voicebox speech generation model using a cross-attention module. To ensure a smooth integration of newly added modules with pre-trained ones, we explore various efficient fine-tuning approaches. Our experiment shows that the LoRA with bias-tuning configuration yields the best performance, enhancing controllability without compromising speech quality. Across three fine-grained conditional generation tasks, we demonstrate the effectiveness and resource efficiency of Voicebox Adapter. Follow-up experiments further highlight the robustness of Voicebox Adapter across diverse data setups.

</details>

### [BERTIVITS: The Posterior Encoder Fusion of Pre-Trained Models and Residual Skip Connections for End-to-End Speech Synthesis](s2:ef3151d382340175d8d15d896402800cb9486c67.md)
**Zirui Wang, Minqi Song, Dongbo Zhou** · 2024-06-10

<details>
<summary>Abstract</summary>

Enhancing the naturalness and rhythmicity of generated audio in end-to-end speech synthesis is crucial. The current state-of-the-art (SOTA) model, VITS, utilizes a conditional variational autoencoder architecture. However, it faces challenges, such as limited robustness, due to training solely on text and spectrum data from the training set. Particularly, the posterior encoder struggles with mid- and high-frequency feature extraction, impacting waveform reconstruction. Existing efforts mainly focus on prior encoder enhancements or alignment algorithms, neglecting improvements to spectrum feature extraction. In response, we propose BERTIVITS, a novel model integrating BERT into VITS. Our model features a redesigned posterior encoder with residual connections and utilizes pre-trained models to enhance spectrum feature extraction. Compared to VITS, BERTIVITS shows significant subjective MOS score improvements (0.16 in English, 0.36 in Chinese) and objective Mel-Cepstral coefficient reductions (0.52 in English, 0.49 in Chinese). BERTIVITS is tailored for single-speaker scenarios, improving speech synthesis technology for applications like post-class tutoring or telephone customer service.

</details>

### [An Investigation of Noise Robustness for Flow-Matching-Based Zero-Shot TTS](2406.05699.md)
**Xiaofei Wang et.al.** · 2024-06-09

### [Text-aware and Context-aware Expressive Audiobook Speech Synthesis](2406.05672.md)
**Dake Guo, Xinfa Zhu, Liumeng Xue, Yongmao Zhang et al.** · 2024-06-09

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech have significantly improved the expressiveness of synthetic speech. However, a major challenge remains in generating speech that captures the diverse styles exhibited by professional narrators in audiobooks without relying on manually labeled data or reference speech. To address this problem, we propose a text-aware and context-aware(TACA) style modeling approach for expressive audiobook speech synthesis. We first establish a text-aware style space to cover diverse styles via contrastive learning with the supervision of the speech style. Meanwhile, we adopt a context encoder to incorporate cross-sentence information and the style embedding obtained from text. Finally, we introduce the context encoder to two typical TTS models, VITS-based TTS and language model-based TTS. Experimental results demonstrate that our proposed approach can effectively capture diverse styles and coherent prosody, and consequently improves naturalness and expressiveness in audiobook speech synthesis.

</details>

### [Towards Expressive Zero-Shot Speech Synthesis with Hierarchical Prosody Modeling](2406.05681.md)
**Yuepeng Jiang, Tao Li, Fengyu Yang, Lei Xie et al.** · 2024-06-09

<details>
<summary>Abstract</summary>

Recent research in zero-shot speech synthesis has made significant progress in speaker similarity. However, current efforts focus on timbre generalization rather than prosody modeling, which results in limited naturalness and expressiveness. To address this, we introduce a novel speech synthesis model trained on large-scale datasets, including both timbre and hierarchical prosody modeling. As timbre is a global attribute closely linked to expressiveness, we adopt a global vector to model speaker timbre while guiding prosody modeling. Besides, given that prosody contains both global consistency and local variations, we introduce a diffusion model as the pitch predictor and employ a prosody adaptor to model prosody hierarchically, further enhancing the prosody quality of the synthesized speech. Experimental results show that our model not only maintains comparable timbre quality to the baseline but also exhibits better naturalness and expressiveness.

</details>

### [SPA-SVC: Self-supervised Pitch Augmentation for Singing Voice Conversion](2406.05692.md)
**Bingsong Bai, Fengping Wang, Yingming Gao, Ya Li** · 2024-06-09

<details>
<summary>Abstract</summary>

Diffusion-based singing voice conversion (SVC) models have shown better synthesis quality compared to traditional methods. However, in cross-domain SVC scenarios, where there is a significant disparity in pitch between the source and target voice domains, the models tend to generate audios with hoarseness, posing challenges in achieving high-quality vocal outputs. Therefore, in this paper, we propose a Self-supervised Pitch Augmentation method for Singing Voice Conversion (SPA-SVC), which can enhance the voice quality in SVC tasks without requiring additional data or increasing model parameters. We innovatively introduce a cycle pitch shifting training strategy and Structural Similarity Index (SSIM) loss into our SVC model, effectively enhancing its performance. Experimental results on the public singing datasets M4Singer indicate that our proposed method significantly improves model performance in both general SVC scenarios and particularly in cross-domain SVC scenarios.

</details>

### [Autoregressive Diffusion Transformer for Text-to-Speech Synthesis](2406.05551.md)
**Zhijun Liu et.al.** · 2024-06-08

### [VALL-E 2: Neural Codec Language Models are Human Parity Zero-Shot Text to Speech Synthesizers](2406.05370.md)
**Sanyuan Chen et.al.** · 2024-06-08

### [LDM-SVC: Latent Diffusion Model Based Zero-Shot Any-to-Any Singing Voice Conversion with Singer Guidance](2406.05325.md)
**Shihao Chen, Yu Gu, Jie Zhang, Na Li et al.** · 2024-06-08

<details>
<summary>Abstract</summary>

Any-to-any singing voice conversion (SVC) is an interesting audio editing technique, aiming to convert the singing voice of one singer into that of another, given only a few seconds of singing data. However, during the conversion process, the issue of timbre leakage is inevitable: the converted singing voice still sounds like the original singer's voice. To tackle this, we propose a latent diffusion model for SVC (LDM-SVC) in this work, which attempts to perform SVC in the latent space using an LDM. We pretrain a variational autoencoder structure using the noted open-source So-VITS-SVC project based on the VITS framework, which is then used for the LDM training. Besides, we propose a singer guidance training method based on classifier-free guidance to further suppress the timbre of the original singer. Experimental results show the superiority of the proposed method over previous works in both subjective and objective evaluations of timbre similarity.

</details>

### [Exploring the Benefits of Tokenization of Discrete Acoustic Units](2406.05547.md)
**Avihu Dekel, Raul Fernandez** · 2024-06-08

<details>
<summary>Abstract</summary>

Tokenization algorithms that merge the units of a base vocabulary into larger, variable-rate units have become standard in natural language processing tasks. This idea, however, has been mostly overlooked when the vocabulary consists of phonemes or Discrete Acoustic Units (DAUs), an audio-based representation that is playing an increasingly important role due to the success of discrete language-modeling techniques. In this paper, we showcase the advantages of tokenization of phonetic units and of DAUs on three prediction tasks: grapheme-to-phoneme, grapheme-to-DAUs, and unsupervised speech generation using DAU language modeling. We demonstrate that tokenization yields significant improvements in terms of performance, as well as training and inference speed, across all three tasks. We also offer theoretical insights to provide some explanation for the superior performance observed.

</details>

### [Spectral Codecs: Spectrogram-Based Audio Codecs for High Quality Speech Synthesis](2406.05298.md)
**Ryan Langman et.al.** · 2024-06-07

### [XTTS: a Massively Multilingual Zero-Shot Text-to-Speech Model](2406.04904.md)
**Edresson Casanova et.al.** · 2024-06-07

### [Boosting Diffusion Model for Spectrogram Up-sampling in Text-to-speech: An Empirical Study](2406.04633.md)
**Chong Zhang et.al.** · 2024-06-07

### [TraceableSpeech: Towards Proactively Traceable Text-to-Speech with Watermarking](2406.04840.md)
**Junzuo Zhou, Jiangyan Yi, Tao Wang, Jianhua Tao et al.** · 2024-06-07

<details>
<summary>Abstract</summary>

Various threats posed by the progress in text-to-speech (TTS) have prompted the need to reliably trace synthesized speech. However, contemporary approaches to this task involve adding watermarks to the audio separately after generation, a process that hurts both speech quality and watermark imperceptibility. In addition, these approaches are limited in robustness and flexibility. To address these problems, we propose TraceableSpeech, a novel TTS model that directly generates watermarked speech, improving watermark imperceptibility and speech quality. Furthermore, We design the frame-wise imprinting and extraction of watermarks, achieving higher robustness against resplicing attacks and temporal flexibility in operation. Experimental results show that TraceableSpeech outperforms the strong baseline where VALL-E or HiFicodec individually uses WavMark in watermark imperceptibility, speech quality and resilience against resplicing attacks. It also can apply to speech of various durations. The code is avaliable at https://github.com/zjzser/TraceableSpeech

</details>

### [Small-E: Small Language Model with Linear Attention for Efficient Speech Synthesis](2406.04467.md)
**Théodor Lemerle et.al.** · 2024-06-06

### [Retrieval Augmented Generation in Prompt-based Text-to-Speech Synthesis with Context-Aware Contrastive Language-Audio Pretraining](2406.03714.md)
**Jinlong Xue et.al.** · 2024-06-06

### [Improving Audio Codec-based Zero-Shot Text-to-Speech Synthesis with Multi-Modal Context and Large Language Model](2406.03706.md)
**Jinlong Xue et.al.** · 2024-06-06

### [Parallel Synthesis for Autoregressive Speech Generation](2204.11806.md)
**Po-chun Hsu et.al.** · 2024-06-06

### [Total-Duration-Aware Duration Modeling for Text-to-Speech Systems](2406.04281.md)
**Sefik Emre Eskimez, Xiaofei Wang, Manthan Thakker, Chung-Hsien Tsai et al.** · 2024-06-06

<details>
<summary>Abstract</summary>

Accurate control of the total duration of generated speech by adjusting the speech rate is crucial for various text-to-speech (TTS) applications. However, the impact of adjusting the speech rate on speech quality, such as intelligibility and speaker characteristics, has been underexplored. In this work, we propose a novel total-duration-aware (TDA) duration model for TTS, where phoneme durations are predicted not only from the text input but also from an additional input of the total target duration. We also propose a MaskGIT-based duration model that enhances the diversity and quality of the predicted phoneme durations. Our results demonstrate that the proposed TDA duration models achieve better intelligibility and speaker similarity for various speech rate configurations compared to the baseline models. We also show that the proposed MaskGIT-based model can generate phoneme durations with higher quality and diversity compared to its regression or flow-matching counterparts.

</details>

### [Towards Naturalistic Voice Conversion: NaturalVoices Dataset with an Automatic Processing Pipeline](2406.04494.md)
**Ali N. Salman, Zongyang Du, Shreeram Suresh Chandra, Ismail Rasim Ulgen et al.** · 2024-06-06

<details>
<summary>Abstract</summary>

Voice conversion (VC) research traditionally depends on scripted or acted speech, which lacks the natural spontaneity of real-life conversations. While natural speech data is limited for VC, our study focuses on filling in this gap. We introduce a novel data-sourcing pipeline that makes the release of a natural speech dataset for VC, named NaturalVoices. The pipeline extracts rich information in speech such as emotion and signal-to-noise ratio (SNR) from raw podcast data, utilizing recent deep learning methods and providing flexibility and ease of use. NaturalVoices marks a large-scale, spontaneous, expressive, and emotional speech dataset, comprising over 3,800 hours speech sourced from the original podcasts in the MSP-Podcast dataset. Objective and subjective evaluations demonstrate the effectiveness of using our pipeline for providing natural and expressive data for VC, suggesting the potential of NaturalVoices for broader speech generation tasks.

</details>

### [LiveSpeech: Low-Latency Zero-shot Text-to-Speech via Autoregressive Modeling of Audio Discrete Codes](2406.02897.md)
**Trung Dang et.al.** · 2024-06-05

### [SimpleSpeech: Towards Simple and Efficient Text-to-Speech with Scalar Latent Transformer Diffusion Models](2406.02328.md)
**Dongchao Yang et.al.** · 2024-06-05

### [Style Mixture of Experts for Expressive Text-To-Speech Synthesis](2406.03637.md)
**Ahad Jawaid, Shreeram Suresh Chandra, Junchen Lu, Berrak Sisman** · 2024-06-05

<details>
<summary>Abstract</summary>

Recent advances in style transfer text-to-speech (TTS) have improved the expressiveness of synthesized speech. However, encoding stylistic information (e.g., timbre, emotion, and prosody) from diverse and unseen reference speech remains a challenge. This paper introduces StyleMoE, an approach that addresses the issue of learning averaged style representations in the style encoder by creating style experts that learn from subsets of data. The proposed method replaces the style encoder in a TTS framework with a Mixture of Experts (MoE) layer. The style experts specialize by learning from subsets of reference speech routed to them by the gating network, enabling them to handle different aspects of the style space. As a result, StyleMoE improves the style coverage of the style encoder for style transfer TTS. Our experiments, both objective and subjective, demonstrate improved style transfer for diverse and unseen reference speech. The proposed method enhances the performance of existing state-of-the-art style transfer TTS models and represents the first study of style MoE in TTS.

</details>

### [Addressing Index Collapse of Large-Codebook Speech Tokenizer with Dual-Decoding Product-Quantized Variational Auto-Encoder](2406.02940.md)
**Haohan Guo, Fenglong Xie, Dongchao Yang, Hui Lu et al.** · 2024-06-05

<details>
<summary>Abstract</summary>

VQ-VAE, as a mainstream approach of speech tokenizer, has been troubled by ``index collapse'', where only a small number of codewords are activated in large codebooks. This work proposes product-quantized (PQ) VAE with more codebooks but fewer codewords to address this problem and build large-codebook speech tokenizers. It encodes speech features into multiple VQ subspaces and composes them into codewords in a larger codebook. Besides, to utilize each VQ subspace well, we also enhance PQ-VAE via a dual-decoding training strategy with the encoding and quantized sequences. The experimental results demonstrate that PQ-VAE addresses ``index collapse" effectively, especially for larger codebooks. The model with the proposed training strategy further improves codebook perplexity and reconstruction quality, outperforming other multi-codebook VQ approaches. Finally, PQ-VAE demonstrates its effectiveness in language-model-based TTS, supporting higher-quality speech generation with larger codebooks.

</details>

### [BiVocoder: A Bidirectional Neural Vocoder Integrating Feature Extraction and Waveform Generation](2406.02162.md)
**Hui-Peng Du et.al.** · 2024-06-04

### [Phonetic Enhanced Language Modeling for Text-to-Speech Synthesis](2406.02009.md)
**Kun Zhou et.al.** · 2024-06-04

### [Seed-TTS: A Family of High-Quality Versatile Speech Generation Models](2406.02430.md)
**Philip Anastassiou, Jiawei Chen, Jitong Chen, Yuanzhe Chen et al.** · 2024-06-04

<details>
<summary>Abstract</summary>

We introduce Seed-TTS, a family of large-scale autoregressive text-to-speech (TTS) models capable of generating speech that is virtually indistinguishable from human speech. Seed-TTS serves as a foundation model for speech generation and excels in speech in-context learning, achieving performance in speaker similarity and naturalness that matches ground truth human speech in both objective and subjective evaluations. With fine-tuning, we achieve even higher subjective scores across these metrics. Seed-TTS offers superior controllability over various speech attributes such as emotion and is capable of generating highly expressive and diverse speech for speakers in the wild. Furthermore, we propose a self-distillation method for speech factorization, as well as a reinforcement learning approach to enhance model robustness, speaker similarity, and controllability. We additionally present a non-autoregressive (NAR) variant of the Seed-TTS model, named $\text{Seed-TTS}_\text{DiT}$, which utilizes a fully diffusion-based architecture. Unlike previous NAR-based TTS systems, $\text{Seed-TTS}_\text{DiT}$ does not depend on pre-estimated phoneme durations and performs speech generation through end-to-end processing. We demonstrate that this variant achieves comparable performance to the language model-based variant and showcase its effectiveness in speech editing. We encourage readers to listen to demos at \url{https://bytedancespeech.github.io/seedtts_tech_report}.

</details>

### [Self-Supervised Singing Voice Pre-Training towards Speech-to-Singing Conversion](2406.02429.md)
**Ruiqi Li, Rongjie Huang, Yongqi Wang, Zhiqing Hong et al.** · 2024-06-04

<details>
<summary>Abstract</summary>

Speech-to-singing voice conversion (STS) task always suffers from data scarcity, because it requires paired speech and singing data. Compounding this issue are the challenges of content-pitch alignment and the suboptimal quality of generated outputs, presenting significant hurdles in STS research. This paper presents SVPT, an STS approach boosted by a self-supervised singing voice pre-training model. We leverage spoken language model techniques to tackle the rhythm alignment problem and the in-context learning capability to achieve zero-shot conversion. We adopt discrete-unit random resampling and pitch corruption strategies, enabling training with unpaired singing data and thus mitigating the issue of data scarcity. SVPT also serves as an effective backbone for singing voice synthesis (SVS), offering insights into scaling up SVS models. Experimental results indicate that SVPT delivers notable improvements in both STS and SVS endeavors. Audio samples are available at https://speech2sing.github.io.

</details>

### [Accent Conversion in Text-To-Speech Using Multi-Level VAE and Adversarial Training](2406.01018.md)
**Jan Melechovsky et.al.** · 2024-06-03

### [ControlSpeech: Towards Simultaneous and Independent Zero-shot Speaker Cloning and Zero-shot Language Style Control](2406.01205.md)
**Shengpeng Ji, Qian Chen, Wen Wang, Jialong Zuo et al.** · 2024-06-03

<details>
<summary>Abstract</summary>

In this paper, we present ControlSpeech, a text-to-speech (TTS) system capable of fully cloning the speaker's voice and enabling arbitrary control and adjustment of speaking style. Prior zero-shot TTS models only mimic the speaker's voice without further control and adjustment capabilities while prior controllable TTS models cannot perform speaker-specific voice generation. Therefore, ControlSpeech focuses on a more challenging task: a TTS system with controllable timbre, content, and style at the same time. ControlSpeech takes speech prompts, content prompts, and style prompts as inputs and utilizes bidirectional attention and mask-based parallel decoding to capture codec representations corresponding to timbre, content, and style in a discrete decoupling codec space. Moreover, we analyze the many-to-many issue in textual style control and propose the Style Mixture Semantic Density (SMSD) module, which is based on Gaussian mixture density networks, to resolve this problem. To facilitate empirical validations, we make available a new style controllable dataset called VccmDataset. Our experimental results demonstrate that ControlSpeech exhibits comparable or state-of-the-art (SOTA) performance in terms of controllability, timbre similarity, audio quality, robustness, and generalizability. The relevant code and demo are available at https://github.com/jishengpeng/ControlSpeech .

</details>

### [Generative Pre-trained Speech Language Model with Efficient Hierarchical Transformer](2406.00976.md)
**Yongxin Zhu, Dan Su, Liqiang He, Linli Xu et al.** · 2024-06-03

<details>
<summary>Abstract</summary>

While recent advancements in speech language models have achieved significant progress, they face remarkable challenges in modeling the long acoustic sequences of neural audio codecs. In this paper, we introduce \textbf{G}enerative \textbf{P}re-trained \textbf{S}peech \textbf{T}ransformer (GPST), a hierarchical transformer designed for efficient speech language modeling. GPST quantizes audio waveforms into two distinct types of discrete speech representations and integrates them within a hierarchical transformer architecture, allowing for a unified one-stage generation process and enhancing Hi-Res audio generation capabilities. By training on large corpora of speeches in an end-to-end unsupervised manner, GPST can generate syntactically consistent speech with diverse speaker identities. Given a brief 3-second prompt, GPST can produce natural and coherent personalized speech, demonstrating in-context learning abilities. Moreover, our approach can be easily extended to spoken cross-lingual speech generation by incorporating multi-lingual semantic tokens and universal acoustic tokens. Experimental results indicate that GPST significantly outperforms the existing speech language models in terms of word error rate, speech quality, and speaker similarity. The code is available at \url{https://github.com/youngsheen/GPST}.

</details>

### [Enhancing Zero-shot Text-to-Speech Synthesis with Human Feedback](2406.00654.md)
**Chen Chen et.al.** · 2024-06-02

### [Very Low Complexity Speech Synthesis Using Framewise Autoregressive GAN (FARGAN) with Pitch Prediction](2405.21069.md)
**Jean-Marc Valin, Ahmed Mustafa, Jan Büthe** · 2024-05-31

<details>
<summary>Abstract</summary>

Neural vocoders are now being used in a wide range of speech processing applications. In many of those applications, the vocoder can be the most complex component, so finding lower complexity algorithms can lead to significant practical benefits. In this work, we propose FARGAN, an autoregressive vocoder that takes advantage of long-term pitch prediction to synthesize high-quality speech in small subframes, without the need for teacher-forcing. Experimental results show that the proposed 600~MFLOPS FARGAN vocoder can achieve both higher quality and lower complexity than existing low-complexity vocoders. The quality even matches that of existing higher-complexity vocoders.

</details>

### [Reinforcement Learning for Fine-tuning Text-to-speech Diffusion Models](2405.14632.md)
**Jingyi Chen et.al.** · 2024-05-23

### [Multilingual Prosody Transfer: Comparing Supervised & Transfer Learning](2406.00022.md)
**Arnav Goel, Medha Hira, Anubha Gupta** · 2024-05-23

<details>
<summary>Abstract</summary>

The field of prosody transfer in speech synthesis systems is rapidly advancing. This research is focused on evaluating learning methods for adapting pre-trained monolingual text-to-speech (TTS) models to multilingual conditions, i.e., Supervised Fine-Tuning (SFT) and Transfer Learning (TL). This comparison utilizes three distinct metrics: Mean Opinion Score (MOS), Recognition Accuracy (RA), and Mel Cepstral Distortion (MCD). Results demonstrate that, in comparison to SFT, TL leads to significantly enhanced performance, with an average MOS higher by 1.53 points, a 37.5% increase in RA, and approximately a 7.8-point improvement in MCD. These findings are instrumental in helping build TTS models for low-resource languages.

</details>

### [Real-Time and Accurate: Zero-shot High-Fidelity Singing Voice Conversion with Multi-Condition Flow Synthesis](2405.15093.md)
**Hui Li, Hongyu Wang, Zhijin Chen, Bohan Sun et al.** · 2024-05-23

<details>
<summary>Abstract</summary>

Singing voice conversion is to convert the source singing voice into the target singing voice except for the content. Currently, flow-based models can complete the task of voice conversion, but they struggle to effectively extract latent variables in the more rhythmically rich and emotionally expressive task of singing voice conversion, while also facing issues with low efficiency in speech processing. In this paper, we propose a high-fidelity flow-based model based on multi-decoupling feature constraints called RASVC, which enhances the capture of vocal details by integrating multiple latent attribute encoders. We also use Multi-stream inverse short-time Fourier transform(MS-iSTFT) to enhance the speed of speech processing by skipping some complicated decoder processing steps. We compare the synthesized singing voice with other models from multiple dimensions, and our proposed model is highly consistent with the current state-of-the-art, with the demo which is available at \url{https://lazycat1119.github.io/RASVC-demo/}.

</details>

### [Multi-speaker Text-to-speech Training with Speaker Anonymized Data](2405.11767.md)
**Wen-Chin Huang et.al.** · 2024-05-20

### [VR-GPT: Visual Language Model for Intelligent Virtual Reality Applications](2405.11537.md)
**Mikhail Konenkov, Artem Lykov, Daria Trinitatova, Dzmitry Tsetserukou** · 2024-05-19

<details>
<summary>Abstract</summary>

The advent of immersive Virtual Reality applications has transformed various domains, yet their integration with advanced artificial intelligence technologies like Visual Language Models remains underexplored. This study introduces a pioneering approach utilizing VLMs within VR environments to enhance user interaction and task efficiency. Leveraging the Unity engine and a custom-developed VLM, our system facilitates real-time, intuitive user interactions through natural language processing, without relying on visual text instructions. The incorporation of speech-to-text and text-to-speech technologies allows for seamless communication between the user and the VLM, enabling the system to guide users through complex tasks effectively. Preliminary experimental results indicate that utilizing VLMs not only reduces task completion times but also improves user comfort and task engagement compared to traditional VR interaction methods.

</details>

### [Exploring speech style spaces with language models: Emotional TTS without emotion labels](2405.11413.md)
**Shreeram Suresh Chandra et.al.** · 2024-05-18

### [Wav2wav: Wave-to-Wave Voice Conversion](s2:ff88d7c24c1a2d29b4db9f76c9fbc3f670eecb53.md)
**Changhyeon Jeong, Hyung-Pil Chang, In-Chul Yoo, Dongsuk Yook** · 2024-05-17

<details>
<summary>Abstract</summary>

Voice conversion is the task of changing the speaker characteristics of input speech while preserving its linguistic content. It can be used in various areas, such as entertainment, medicine, and education. The quality of the converted speech is crucial for voice conversion algorithms to be useful in these various applications. Deep learning-based voice conversion algorithms, which have been showing promising results recently, generally consist of three modules: a feature extractor, feature converter, and vocoder. The feature extractor accepts the waveform as the input and extracts speech feature vectors for further processing. These speech feature vectors are later synthesized back into waveforms by the vocoder. The feature converter module performs the actual voice conversion; therefore, many previous studies separately focused on improving this module. These works combined the separately trained vocoder to synthesize the final waveform. Since the feature converter and the vocoder are trained independently, the output of the converter may not be compatible with the input of the vocoder, which causes performance degradation. Furthermore, most voice conversion algorithms utilize mel-spectrogram-based speech feature vectors without modification. These feature vectors have performed well in a variety of speech-processing areas but could be further optimized for voice conversion tasks. To address these problems, we propose a novel wave-to-wave (wav2wav) voice conversion method that integrates the feature extractor, the feature converter, and the vocoder into a single module and trains the system in an end-to-end manner. We evaluated the efficiency of the proposed method using the VCC2018 dataset.

</details>

### [Building a Luganda Text-to-Speech Model From Crowdsourced Data](2405.10211.md)
**Sulaiman Kagumire et.al.** · 2024-05-16

### [Evaluating Text-to-Speech Synthesis from a Large Discrete Token-based Speech Language Model](2405.09768.md)
**Siyang Wang et.al.** · 2024-05-16

### [Faces that Speak: Jointly Synthesising Talking Face and Speech from Text](2405.10272.md)
**Youngjoon Jang, Ji-Hoon Kim, Junseok Ahn, Doyeop Kwak et al.** · 2024-05-16

<details>
<summary>Abstract</summary>

The goal of this work is to simultaneously generate natural talking faces and speech outputs from text. We achieve this by integrating Talking Face Generation (TFG) and Text-to-Speech (TTS) systems into a unified framework. We address the main challenges of each task: (1) generating a range of head poses representative of real-world scenarios, and (2) ensuring voice consistency despite variations in facial motion for the same identity. To tackle these issues, we introduce a motion sampler based on conditional flow matching, which is capable of high-quality motion code generation in an efficient way. Moreover, we introduce a novel conditioning method for the TTS system, which utilises motion-removed features from the TFG model to yield uniform speech outputs. Our extensive experiments demonstrate that our method effectively creates natural-looking talking faces and speech that accurately match the input text. To our knowledge, this is the first effort to build a multimodal synthesis system that can generalise to unseen identities.

</details>

### [Hierarchical Emotion Prediction and Control in Text-to-Speech Synthesis](2405.09171.md)
**Sho Inoue, Kun Zhou, Shuai Wang, Haizhou Li** · 2024-05-15

<details>
<summary>Abstract</summary>

It remains a challenge to effectively control the emotion rendering in text-to-speech (TTS) synthesis. Prior studies have primarily focused on learning a global prosodic representation at the utterance level, which strongly correlates with linguistic prosody. Our goal is to construct a hierarchical emotion distribution (ED) that effectively encapsulates intensity variations of emotions at various levels of granularity, encompassing phonemes, words, and utterances. During TTS training, the hierarchical ED is extracted from the ground-truth audio and guides the predictor to establish a connection between emotional and linguistic prosody. At run-time inference, the TTS model generates emotional speech and, at the same time, provides quantitative control of emotion over the speech constituents. Both objective and subjective evaluations validate the effectiveness of the proposed framework in terms of emotion prediction and control.

</details>

### [PolyGlotFake: A Novel Multilingual and Multimodal DeepFake Dataset](2405.08838.md)
**Yang Hou, Haitao Fu, Chuankai Chen, Zida Li et al.** · 2024-05-14

<details>
<summary>Abstract</summary>

With the rapid advancement of generative AI, multimodal deepfakes, which manipulate both audio and visual modalities, have drawn increasing public concern. Currently, deepfake detection has emerged as a crucial strategy in countering these growing threats. However, as a key factor in training and validating deepfake detectors, most existing deepfake datasets primarily focus on the visual modal, and the few that are multimodal employ outdated techniques, and their audio content is limited to a single language, thereby failing to represent the cutting-edge advancements and globalization trends in current deepfake technologies. To address this gap, we propose a novel, multilingual, and multimodal deepfake dataset: PolyGlotFake. It includes content in seven languages, created using a variety of cutting-edge and popular Text-to-Speech, voice cloning, and lip-sync technologies. We conduct comprehensive experiments using state-of-the-art detection methods on PolyGlotFake dataset. These experiments demonstrate the dataset's significant challenges and its practical value in advancing research into multimodal deepfake detection.

</details>

### [Real-Time Pill Identification for the Visually Impaired Using Deep Learning](2405.05983.md)
**Bo Dang, Wenchao Zhao, Yufeng Li, Danqing Ma et al.** · 2024-05-08

<details>
<summary>Abstract</summary>

The prevalence of mobile technology offers unique opportunities for addressing healthcare challenges, especially for individuals with visual impairments. This paper explores the development and implementation of a deep learning-based mobile application designed to assist blind and visually impaired individuals in real-time pill identification. Utilizing the YOLO framework, the application aims to accurately recognize and differentiate between various pill types through real-time image processing on mobile devices. The system incorporates Text-to- Speech (TTS) to provide immediate auditory feedback, enhancing usability and independence for visually impaired users. Our study evaluates the application's effectiveness in terms of detection accuracy and user experience, highlighting its potential to improve medication management and safety among the visually impaired community. Keywords-Deep Learning; YOLO Framework; Mobile Application; Visual Impairment; Pill Identification; Healthcare

</details>

### [WaveVC: Speech and Fundamental Frequency Consistent Raw Audio Voice Conversion](s2:1d243b2b89463730a17f54170830c4da6d577b91.md)
**Kyungdeuk Ko, Donghyeon Kim, Kyungseok Oh, Hanseok Ko** · 2024-05-08

<details>
<summary>Abstract</summary>

Voice conversion (VC) is a task for changing the speech of a source speaker to the target voice while preserving linguistic information of the source speech. The existing VC methods typically use mel-spectrogram as both input and output, so a separate vocoder is required to transform mel-spectrogram into waveform. Therefore, the VC performance varies depending on the vocoder performance, and noisy speech can be generated due to problems such as train-test mismatch. In this paper, we propose a speech and fundamental frequency consistent raw audio voice conversion method called WaveVC. Unlike other methods, WaveVC does not require a separate vocoder and can perform VC directly on raw audio waveform using 1D convolution. This eliminates the issue of performance degradation caused by the train-test mismatch of the vocoder. In the training phase, WaveVC employs speech loss and F0 loss to preserve the content of the source speech and generate F0 consistent speech using the pre-trained networks. WaveVC is capable of converting voices while maintaining consistency in speech and fundamental frequency. In the test phase, the F0 feature of the source speech is concatenated with a content embedding vector to ensure the converted speech follows the fundamental frequency flow of the source speech. WaveVC achieves higher performances than baseline methods in both many-to-many VC and any-to-any VC. The converted samples are available online.

</details>

### [BUDDy: Single-Channel Blind Unsupervised Dereverberation with Diffusion Models](2405.04272.md)
**Eloi Moliner, Jean-Marie Lemercier, Simon Welker, Timo Gerkmann et al.** · 2024-05-07

<details>
<summary>Abstract</summary>

In this paper, we present an unsupervised single-channel method for joint blind dereverberation and room impulse response estimation, based on posterior sampling with diffusion models. We parameterize the reverberation operator using a filter with exponential decay for each frequency subband, and iteratively estimate the corresponding parameters as the speech utterance gets refined along the reverse diffusion trajectory. A measurement consistency criterion enforces the fidelity of the generated speech with the reverberant measurement, while an unconditional diffusion model implements a strong prior for clean speech generation. Without any knowledge of the room impulse response nor any coupled reverberant-anechoic data, we can successfully perform dereverberation in various acoustic scenarios. Our method significantly outperforms previous blind unsupervised baselines, and we demonstrate its increased robustness to unseen acoustic conditions in comparison to blind supervised methods. Audio samples and code are available online.

</details>

### [MAIN-VC: Lightweight Speech Representation Disentanglement for One-shot Voice Conversion](2405.00930.md)
**Pengcheng Li, Jianzong Wang, Xulong Zhang, Yong Zhang et al.** · 2024-05-02

<details>
<summary>Abstract</summary>

One-shot voice conversion aims to change the timbre of any source speech to match that of the unseen target speaker with only one speech sample. Existing methods face difficulties in satisfactory speech representation disentanglement and suffer from sizable networks as some of them leverage numerous complex modules for disentanglement. In this paper, we propose a model named MAIN-VC to effectively disentangle via a concise neural network. The proposed model utilizes Siamese encoders to learn clean representations, further enhanced by the designed mutual information estimator. The Siamese structure and the newly designed convolution module contribute to the lightweight of our model while ensuring performance in diverse voice conversion tasks. The experimental results show that the proposed model achieves comparable subjective scores and exhibits improvements in objective metrics compared to existing methods in a one-shot voice conversion scenario.

</details>

### [Learning Expressive Disentangled Speech Representations with Soft Speech Units and Adversarial Style Augmentation](2405.00603.md)
**Yimin Deng, Jianzong Wang, Xulong Zhang, Ning Cheng et al.** · 2024-05-01

<details>
<summary>Abstract</summary>

Voice conversion is the task to transform voice characteristics of source speech while preserving content information. Nowadays, self-supervised representation learning models are increasingly utilized in content extraction. However, in these representations, a lot of hidden speaker information leads to timbre leakage while the prosodic information of hidden units lacks use. To address these issues, we propose a novel framework for expressive voice conversion called "SAVC" based on soft speech units from HuBert-soft. Taking soft speech units as input, we design an attribute encoder to extract content and prosody features respectively. Specifically, we first introduce statistic perturbation imposed by adversarial style augmentation to eliminate speaker information. Then the prosody is implicitly modeled on soft speech units with knowledge distillation. Experiment results show that the intelligibility and naturalness of converted speech outperform previous work.

</details>

### [Noise-robust voice conversion using adversarial training with multi-feature decoupling](s2:a5a6a14602a68380f9a4d6abbcdcae3521c853be.md)
**Lele Chen, Xiongwei Zhang, Yihao Li, Meng Sun** · 2024-05-01

### [Attention-Constrained Inference for Robust Decoder-Only Text-to-Speech](2404.19723.md)
**Hankun Wang et.al.** · 2024-04-30

### [Expressivity and Speech Synthesis](2404.19363.md)
**Andreas Triantafyllopoulos, Björn W. Schuller** · 2024-04-30

<details>
<summary>Abstract</summary>

Imbuing machines with the ability to talk has been a longtime pursuit of artificial intelligence (AI) research. From the very beginning, the community has not only aimed to synthesise high-fidelity speech that accurately conveys the semantic meaning of an utterance, but also to colour it with inflections that cover the same range of affective expressions that humans are capable of. After many years of research, it appears that we are on the cusp of achieving this when it comes to single, isolated utterances. This unveils an abundance of potential avenues to explore when it comes to combining these single utterances with the aim of synthesising more complex, longer-term behaviours. In the present chapter, we outline the methodological advances that brought us so far and sketch out the ongoing efforts to reach that coveted next level of artificial expressivity. We also discuss the societal implications coupled with rapidly advancing expressive speech synthesis (ESS) technology and highlight ways to mitigate those risks and ensure the alignment of ESS capabilities with ethical norms.

</details>

### [EAD-VC: Enhancing Speech Auto-Disentanglement for Voice Conversion with IFUB Estimator and Joint Text-Guided Consistent Learning](2404.19212.md)
**Ziqi Liang, Jianzong Wang, Xulong Zhang, Yong Zhang et al.** · 2024-04-30

<details>
<summary>Abstract</summary>

Using unsupervised learning to disentangle speech into content, rhythm, pitch, and timbre for voice conversion has become a hot research topic. Existing works generally take into account disentangling speech components through human-crafted bottleneck features which can not achieve sufficient information disentangling, while pitch and rhythm may still be mixed together. There is a risk of information overlap in the disentangling process which results in less speech naturalness. To overcome such limits, we propose a two-stage model to disentangle speech representations in a self-supervised manner without a human-crafted bottleneck design, which uses the Mutual Information (MI) with the designed upper bound estimator (IFUB) to separate overlapping information between speech components. Moreover, we design a Joint Text-Guided Consistent (TGC) module to guide the extraction of speech content and eliminate timbre leakage issues. Experiments show that our model can achieve a better performance than the baseline, regarding disentanglement effectiveness, speech naturalness, and similarity. Audio samples can be found at https://largeaudiomodel.com/eadvc.

</details>

### [SemantiCodec: An Ultra Low Bitrate Semantic Audio Codec for General Sound](2405.00233.md)
**Haohe Liu, Xuenan Xu, Yi Yuan, Mengyue Wu et al.** · 2024-04-30

<details>
<summary>Abstract</summary>

Large language models (LLMs) have significantly advanced audio processing through audio codecs that convert audio into discrete tokens, enabling the application of language modelling techniques to audio data. However, traditional codecs often operate at high bitrates or within narrow domains such as speech and lack the semantic clues required for efficient language modelling. Addressing these challenges, we introduce SemantiCodec, a novel codec designed to compress audio into fewer than a hundred tokens per second across diverse audio types, including speech, general sound, and music, without compromising quality. SemantiCodec features a dual-encoder architecture: a semantic encoder using a self-supervised pre-trained Audio Masked Autoencoder (AudioMAE), discretized using k-means clustering on extensive audio data, and an acoustic encoder to capture the remaining details. The semantic and acoustic encoder outputs are used to reconstruct audio via a diffusion-model-based decoder. SemantiCodec is presented in three variants with token rates of 25, 50, and 100 per second, supporting a range of ultra-low bit rates between 0.31 kbps and 1.40 kbps. Experimental results demonstrate that SemantiCodec significantly outperforms the state-of-the-art Descript codec on reconstruction quality. Our results also suggest that SemantiCodec contains significantly richer semantic information than all evaluated state-of-the-art audio codecs, even at significantly lower bitrates. Our code and demos are available at https://haoheliu.github.io/SemantiCodec/.

</details>

### [Speaker Anonymization: Disentangling Speaker Features from Pre-Trained Speech Embeddings for Voice Conversion](s2:2859e4dfdde4dd0324c79b9d8b6a44624e26b778.md)
**M. Matassoni, Seraphina Fong, A. Brutti** · 2024-04-30

<details>
<summary>Abstract</summary>

Speech is a crucial source of personal information, and the risk of attackers using such information increases day by day. Speaker privacy protection is crucial, and various approaches have been proposed to hide the speaker’s identity. One approach is voice anonymization, which aims to safeguard speaker identity while maintaining speech content through techniques such as voice conversion or spectral feature alteration. The significance of voice anonymization has grown due to the necessity to protect personal information in applications such as voice assistants, authentication, and customer support. Building upon the S3PRL-VC toolkit and on pre-trained speech and speaker representation models, this paper introduces a feature disentanglement approach to improve the de-identification performance of the state-of-the-art anonymization approaches based on voice conversion. The proposed approach achieves state-of-the-art speaker de-identification and causes minimal impact on the intelligibility of the signal after conversion.

</details>

### [MM-TTS: A Unified Framework for Multimodal, Prompt-Induced Emotional Text-to-Speech Synthesis](2404.18398.md)
**Xiang Li et.al.** · 2024-04-29

### [USAT: A Universal Speaker-Adaptive Text-to-Speech Approach](2404.18094.md)
**Wenbin Wang, Yang Song, Sanjay Jha** · 2024-04-28

<details>
<summary>Abstract</summary>

Conventional text-to-speech (TTS) research has predominantly focused on enhancing the quality of synthesized speech for speakers in the training dataset. The challenge of synthesizing lifelike speech for unseen, out-of-dataset speakers, especially those with limited reference data, remains a significant and unresolved problem. While zero-shot or few-shot speaker-adaptive TTS approaches have been explored, they have many limitations. Zero-shot approaches tend to suffer from insufficient generalization performance to reproduce the voice of speakers with heavy accents. While few-shot methods can reproduce highly varying accents, they bring a significant storage burden and the risk of overfitting and catastrophic forgetting. In addition, prior approaches only provide either zero-shot or few-shot adaptation, constraining their utility across varied real-world scenarios with different demands. Besides, most current evaluations of speaker-adaptive TTS are conducted only on datasets of native speakers, inadvertently neglecting a vast portion of non-native speakers with diverse accents. Our proposed framework unifies both zero-shot and few-shot speaker adaptation strategies, which we term as "instant" and "fine-grained" adaptations based on their merits. To alleviate the insufficient generalization performance observed in zero-shot speaker adaptation, we designed two innovative discriminators and introduced a memory mechanism for the speech decoder. To prevent catastrophic forgetting and reduce storage implications for few-shot speaker adaptation, we designed two adapters and a unique adaptation procedure.

</details>

### [TI-ASU: Toward Robust Automatic Speech Understanding through Text-to-speech Imputation Against Missing Speech Modality](2404.17983.md)
**Tiantian Feng, Xuan Shi, Rahul Gupta, Shrikanth S. Narayanan** · 2024-04-27

<details>
<summary>Abstract</summary>

Automatic Speech Understanding (ASU) aims at human-like speech interpretation, providing nuanced intent, emotion, sentiment, and content understanding from speech and language (text) content conveyed in speech. Typically, training a robust ASU model relies heavily on acquiring large-scale, high-quality speech and associated transcriptions. However, it is often challenging to collect or use speech data for training ASU due to concerns such as privacy. To approach this setting of enabling ASU when speech (audio) modality is missing, we propose TI-ASU, using a pre-trained text-to-speech model to impute the missing speech. We report extensive experiments evaluating TI-ASU on various missing scales, both multi- and single-modality settings, and the use of LLMs. Our findings show that TI-ASU yields substantial benefits to improve ASU in scenarios where even up to 95% of training speech is missing. Moreover, we show that TI-ASU is adaptive to dropout training, improving model robustness in addressing missing speech during inference.

</details>

### [An RFP dataset for Real, Fake, and Partially fake audio detection](2404.17721.md)
**Abdulazeez AlAli, George Theodorakopoulos** · 2024-04-26

<details>
<summary>Abstract</summary>

Recent advances in deep learning have enabled the creation of natural-sounding synthesised speech. However, attackers have also utilised these tech-nologies to conduct attacks such as phishing. Numerous public datasets have been created to facilitate the development of effective detection models. How-ever, available datasets contain only entirely fake audio; therefore, detection models may miss attacks that replace a short section of the real audio with fake audio. In recognition of this problem, the current paper presents the RFP da-taset, which comprises five distinct audio types: partial fake (PF), audio with noise, voice conversion (VC), text-to-speech (TTS), and real. The data are then used to evaluate several detection models, revealing that the available detec-tion models incur a markedly higher equal error rate (EER) when detecting PF audio instead of entirely fake audio. The lowest EER recorded was 25.42%. Therefore, we believe that creators of detection models must seriously consid-er using datasets like RFP that include PF and other types of fake audio.

</details>

### [Online speech synthesis using a chronically implanted brain–computer interface in an individual with ALS](s2:fa58f21ecda2053d2c1c9360e682b1140b6ff4c1.md)
**M. Angrick, S. Luo, Q. Rabbani, D. Candrea et al.** · 2024-04-26

<details>
<summary>Abstract</summary>

Brain–computer interfaces (BCIs) that reconstruct and synthesize speech using brain activity recorded with intracranial electrodes may pave the way toward novel communication interfaces for people who have lost their ability to speak, or who are at high risk of losing this ability, due to neurological disorders. Here, we report online synthesis of intelligible words using a chronically implanted brain-computer interface (BCI) in a man with impaired articulation due to ALS, participating in a clinical trial (ClinicalTrials.gov, NCT03567213) exploring different strategies for BCI communication. The 3-stage approach reported here relies on recurrent neural networks to identify, decode and synthesize speech from electrocorticographic (ECoG) signals acquired across motor, premotor and somatosensory cortices. We demonstrate a reliable BCI that synthesizes commands freely chosen and spoken by the participant from a vocabulary of 6 keywords previously used for decoding commands to control a communication board. Evaluation of the intelligibility of the synthesized speech indicates that 80% of the words can be correctly recognized by human listeners. Our results show that a speech-impaired individual with ALS can use a chronically implanted BCI to reliably produce synthesized words while preserving the participant’s voice profile, and provide further evidence for the stability of ECoG for speech-based BCIs.

</details>

### [The THU-HCSI Multi-Speaker Multi-Lingual Few-Shot Voice Cloning System for LIMMITS'24 Challenge](2404.16619.md)
**Yixuan Zhou, Shuoyi Zhou, Shun Lei, Zhiyong Wu et al.** · 2024-04-25

<details>
<summary>Abstract</summary>

This paper presents the multi-speaker multi-lingual few-shot voice cloning system developed by THU-HCSI team for LIMMITS'24 Challenge. To achieve high speaker similarity and naturalness in both mono-lingual and cross-lingual scenarios, we build the system upon YourTTS and add several enhancements. For further improving speaker similarity and speech quality, we introduce speaker-aware text encoder and flow-based decoder with Transformer blocks. In addition, we denoise the few-shot data, mix up them with pre-training data, and adopt a speaker-balanced sampling strategy to guarantee effective fine-tuning for target speakers. The official evaluations in track 1 show that our system achieves the best speaker similarity MOS of 4.25 and obtains considerable naturalness MOS of 3.97.

</details>

### [HybridVC: Efficient Voice Style Conversion with Text and Audio Prompts](2404.15637.md)
**Xinlei Niu, Jing Zhang, Charles Patrick Martin** · 2024-04-24

<details>
<summary>Abstract</summary>

We introduce HybridVC, a voice conversion (VC) framework built upon a pre-trained conditional variational autoencoder (CVAE) that combines the strengths of a latent model with contrastive learning. HybridVC supports text and audio prompts, enabling more flexible voice style conversion. HybridVC models a latent distribution conditioned on speaker embeddings acquired by a pretrained speaker encoder and optimises style text embeddings to align with the speaker style information through contrastive learning in parallel. Therefore, HybridVC can be efficiently trained under limited computational resources. Our experiments demonstrate HybridVC's superior training efficiency and its capability for advanced multi-modal voice style conversion. This underscores its potential for widespread applications such as user-defined personalised voice in various social media platforms. A comprehensive ablation study further validates the effectiveness of our method.

</details>

### [StoryTTS: A Highly Expressive Text-to-Speech Dataset with Rich Textual Expressiveness Annotations](2404.14946.md)
**Sen Liu et.al.** · 2024-04-23

### [FlashSpeech: Efficient Zero-Shot Speech Synthesis](2404.14700.md)
**Zhen Ye, Zeqian Ju, Haohe Liu, Xu Tan et al.** · 2024-04-23

<details>
<summary>Abstract</summary>

Recent progress in large-scale zero-shot speech synthesis has been significantly advanced by language models and diffusion models. However, the generation process of both methods is slow and computationally intensive. Efficient speech synthesis using a lower computing budget to achieve quality on par with previous work remains a significant challenge. In this paper, we present FlashSpeech, a large-scale zero-shot speech synthesis system with approximately 5\% of the inference time compared with previous work. FlashSpeech is built on the latent consistency model and applies a novel adversarial consistency training approach that can train from scratch without the need for a pre-trained diffusion model as the teacher. Furthermore, a new prosody generator module enhances the diversity of prosody, making the rhythm of the speech sound more natural. The generation processes of FlashSpeech can be achieved efficiently with one or two sampling steps while maintaining high audio quality and high similarity to the audio prompt for zero-shot speech generation. Our experimental results demonstrate the superior performance of FlashSpeech. Notably, FlashSpeech can be about 20 times faster than other zero-shot speech synthesis systems while maintaining comparable performance in terms of voice quality and similarity. Furthermore, FlashSpeech demonstrates its versatility by efficiently performing tasks like voice conversion, speech editing, and diverse speech sampling. Audio samples can be found in https://flashspeech.github.io/.

</details>

### [Every Breath You Don't Take: Deepfake Speech Detection Using Breath](2404.15143.md)
**Seth Layton, Thiago De Andrade, Daniel Olszewski, Kevin Warren et al.** · 2024-04-23

<details>
<summary>Abstract</summary>

Deepfake speech represents a real and growing threat to systems and society. Many detectors have been created to aid in defense against speech deepfakes. While these detectors implement myriad methodologies, many rely on low-level fragments of the speech generation process. We hypothesize that breath, a higher-level part of speech, is a key component of natural speech and thus improper generation in deepfake speech is a performant discriminator. To evaluate this, we create a breath detector and leverage this against a custom dataset of online news article audio to discriminate between real/deepfake speech. Additionally, we make this custom dataset publicly available to facilitate comparison for future work. Applying our simple breath detector as a deepfake speech discriminator on in-the-wild samples allows for accurate classification (perfect 1.0 AUPRC and 0.0 EER on test data) across 33.6 hours of audio. We compare our model with the state-of-the-art SSL-wav2vec model and show that this complex deep learning model completely fails to classify the same in-the-wild samples (0.72 AUPRC and 0.99 EER).

</details>

### [Retrieval-Augmented Audio Deepfake Detection](2404.13892.md)
**Zuheng Kang, Yayun He, Botao Zhao, Xiaoyang Qu et al.** · 2024-04-22

<details>
<summary>Abstract</summary>

With recent advances in speech synthesis including text-to-speech (TTS) and voice conversion (VC) systems enabling the generation of ultra-realistic audio deepfakes, there is growing concern about their potential misuse. However, most deepfake (DF) detection methods rely solely on the fuzzy knowledge learned by a single model, resulting in performance bottlenecks and transparency issues. Inspired by retrieval-augmented generation (RAG), we propose a retrieval-augmented detection (RAD) framework that augments test samples with similar retrieved samples for enhanced detection. We also extend the multi-fusion attentive classifier to integrate it with our proposed RAD framework. Extensive experiments show the superior performance of the proposed RAD framework over baseline methods, achieving state-of-the-art results on the ASVspoof 2021 DF set and competitive results on the 2019 and 2021 LA sets. Further sample analysis indicates that the retriever consistently retrieves samples mostly from the same speaker with acoustic characteristics highly consistent with the query audio, thereby improving detection performance.

</details>

### [Parameter Efficient Fine Tuning: A Comprehensive Analysis Across Applications](2404.13506.md)
**Charith Chandra Sai Balne, Sreyoshi Bhaduri, Tamoghna Roy, Vinija Jain et al.** · 2024-04-21

<details>
<summary>Abstract</summary>

The rise of deep learning has marked significant progress in fields such as computer vision, natural language processing, and medical imaging, primarily through the adaptation of pre-trained models for specific tasks. Traditional fine-tuning methods, involving adjustments to all parameters, face challenges due to high computational and memory demands. This has led to the development of Parameter Efficient Fine-Tuning (PEFT) techniques, which selectively update parameters to balance computational efficiency with performance. This review examines PEFT approaches, offering a detailed comparison of various strategies highlighting applications across different domains, including text generation, medical imaging, protein modeling, and speech synthesis. By assessing the effectiveness of PEFT methods in reducing computational load, speeding up training, and lowering memory usage, this paper contributes to making deep learning more accessible and adaptable, facilitating its wider application and encouraging innovation in model optimization. Ultimately, the paper aims to contribute towards insights into PEFT's evolving landscape, guiding researchers and practitioners in overcoming the limitations of conventional fine-tuning approaches.

</details>

### [Prior-agnostic Multi-scale Contrastive Text-Audio Pre-training for Parallelized TTS Frontend Modeling](2404.09192.md)
**Quanxiu Wang et.al.** · 2024-04-14

### [Wav2vec-VC: Voice Conversion via Hidden Representations of Wav2vec 2.0](s2:126c1dd52edf85f976691e06081e4b636993dae3.md)
**Jaemin Lim, Kiyeon Kim** · 2024-04-14

<details>
<summary>Abstract</summary>

This paper describes an unconventional way to use wav2vec 2.0 representations for voice conversion (VC) purpose. Our experiment shows that aggregate of hidden representations from wav2vec 2.0 layers is more effective in VC than using last-layer representation only. In particular, the aggregate of all hidden representations is dependent on a mainly required characteristic (e.g. vocal or linguistic) by a speech task—but such results are consistent on different datasets for the same task. Based on these results, we propose Wav2vec-VC that uses wav2vec 2.0 hidden-layer representations as input to the disentanglement-based VC. Given a target (/source) utterance, Wav2vec-VC gets an aggregated hidden representation weighted in order to perform the speaker (/content)-related tasks, and feeds it to a speaker (/content) encoder whose output is combined at a decoder to synthesize a voice-converted utterance. Our evaluation shows that Wav2vec-VC outperforms SOTA VC models in terms of both voice similarity and speech intelligibility.

</details>

### [Convnext-TTS And Convnext-VC: Convnext-Based Fast End-To-End Sequence-To-Sequence Text-To-Speech And Voice Conversion](s2:964d9d01bbfc268150e9387e0c841eb0741049b9.md)
**T. Okamoto, Yamato Ohtani, Tomoki Toda, Hisashi Kawai** · 2024-04-14

<details>
<summary>Abstract</summary>

End-to-end (E2E) sequence-to-sequence (S2S) neural text-to-speech (TTS) models and E2E-S2S neural voice conversion (VC) models can achieve high-quality speech synthesis with a single neural network. To further improve the synthesis quality of E2E-S2S TTS and VC models and increase their inference speed, we propose a Transformer-free ConvNeXt-based encoder and decoder. Additionally, to further increase the inference speed, we propose ConvNeXt-TTS and ConvNeXt-VC, which include the WaveNeXt neural vocoder. This is also constructed from ConvNeXt blocks and can achieve much faster synthesis than HiFi-GAN. The results of experiments using the Hi-Fi-CAPTAIN corpus for the E2E-S2S-TTS and E2E-S2S-VC conditions demonstrate that the proposed ConvNeXt-based encoder and decoder can perform inference three times faster than a Transformer-based encoder and decoder while improving the synthesis quality. In particular, ConvNeXt-TTS and ConvNeXt-VC can achieve very fast E2E-S2S-TTS and E2E-S2S-VC with a real-time factor of 0.05 using a single-core CPU.

</details>

### [Unifying One-Shot Voice Conversion and Cloning with Disentangled Speech Representations](s2:ed8789ba7c5962f47faeea3898a8f64d59123790.md)
**Hui Lu, Xixin Wu, Haohan Guo, Songxiang Liu et al.** · 2024-04-14

<details>
<summary>Abstract</summary>

We propose unifying one-shot voice conversion and cloning into a single model that can be end-to-end optimized. To achieve this, we introduce a novel extension to a speech variational auto-encoder (VAE) that disentangles speech into content and speaker representations. Instead of using a fixed Gaussian prior as in the vanilla VAE, we incorporate a learnable text-aware prior as an informative guide for learning the content representation. This results in a content representation with reduced speaker information and more accurate linguistic information. The proposed model can sample the content representation using either the posterior conditioned on speech or the text-aware prior with textual input, enabling one-shot voice conversion and cloning, respectively. Experiments show that the proposed method achieves better or comparable overall performance for one-shot voice conversion and cloning compared to state-of-the-art voice conversion and cloning methods.

</details>

### [Invertible Voice Conversion with Parallel Data](s2:3c9f9e6160d1376addeb47691e1fa908f40e242f.md)
**Zexin Cai, Ming Li** · 2024-04-14

<details>
<summary>Abstract</summary>

This paper introduces an innovative deep learning framework for parallel voice conversion to mitigate inherent risks associated with such systems. Our approach focuses on developing an invertible model capable of countering potential spoofing threats. Specifically, we present a conversion model that allows for the retrieval of source voices, thereby facilitating the identification of the source speaker. This framework is constructed using a series of invertible modules composed of affine coupling layers to ensure the reversibility of the conversion process. We conduct comprehensive training and evaluation of the proposed framework using parallel training data. Our experimental results reveal that this approach achieves comparable performance to non-invertible systems in voice conversion tasks. Notably, the converted outputs can be seamlessly reverted to the original source inputs using the same parameters employed during the forwarding process. This advancement holds considerable promise for elevating the security and reliability of voice conversion.

</details>

### [PromptCodec: High-Fidelity Neural Speech Codec using Disentangled Representation Learning based Adaptive Feature-aware Prompt Encoders](2404.02702.md)
**Yu Pan et.al.** · 2024-04-13

### [Voice Attribute Editing with Text Prompt](2404.08857.md)
**Zhengyan Sheng, Yang Ai, Li-Juan Liu, Jia Pan et al.** · 2024-04-13

<details>
<summary>Abstract</summary>

Despite recent advancements in speech generation with text prompt providing control over speech style, voice attributes in synthesized speech remain elusive and challenging to control. This paper introduces a novel task: voice attribute editing with text prompt, with the goal of making relative modifications to voice attributes according to the actions described in the text prompt. To solve this task, VoxEditor, an end-to-end generative model, is proposed. In VoxEditor, addressing the insufficiency of text prompt, a Residual Memory (ResMem) block is designed, that efficiently maps voice attributes and these descriptors into the shared feature space. Additionally, the ResMem block is enhanced with a voice attribute degree prediction (VADP) block to align voice attributes with corresponding descriptors, addressing the imprecision of text prompt caused by non-quantitative descriptions of voice attributes. We also establish the open-source VCTK-RVA dataset, which leads the way in manual annotations detailing voice characteristic differences among different speakers. Extensive experiments demonstrate the effectiveness and generalizability of our proposed method in terms of both objective and subjective metrics. The dataset and audio samples are available on the website.

</details>

### [Voice-Assisted Real-Time Traffic Sign Recognition System Using Convolutional Neural Network](2404.07807.md)
**Mayura Manawadu, Udaya Wijenayake** · 2024-04-11

<details>
<summary>Abstract</summary>

Traffic signs are important in communicating information to drivers. Thus, comprehension of traffic signs is essential for road safety and ignorance may result in road accidents. Traffic sign detection has been a research spotlight over the past few decades. Real-time and accurate detections are the preliminaries of robust traffic sign detection system which is yet to be achieved. This study presents a voice-assisted real-time traffic sign recognition system which is capable of assisting drivers. This system functions under two subsystems. Initially, the detection and recognition of the traffic signs are carried out using a trained Convolutional Neural Network (CNN). After recognizing the specific traffic sign, it is narrated to the driver as a voice message using a text-to-speech engine. An efficient CNN model for a benchmark dataset is developed for real-time detection and recognition using Deep Learning techniques. The advantage of this system is that even if the driver misses a traffic sign, or does not look at the traffic sign, or is unable to comprehend the sign, the system detects it and narrates it to the driver. A system of this type is also important in the development of autonomous vehicles.

</details>

### [CoVoMix: Advancing Zero-Shot Speech Generation for Human-like Multi-talker Conversations](2404.06690.md)
**Leying Zhang et.al.** · 2024-04-10

### [Llama-VITS: Enhancing TTS Synthesis with Semantic Awareness](2404.06714.md)
**Xincan Feng, Akifumi Yoshimoto** · 2024-04-10

<details>
<summary>Abstract</summary>

Recent advancements in Natural Language Processing (NLP) have seen Large-scale Language Models (LLMs) excel at producing high-quality text for various purposes. Notably, in Text-To-Speech (TTS) systems, the integration of BERT for semantic token generation has underscored the importance of semantic content in producing coherent speech outputs. Despite this, the specific utility of LLMs in enhancing TTS synthesis remains considerably limited. This research introduces an innovative approach, Llama-VITS, which enhances TTS synthesis by enriching the semantic content of text using LLM. Llama-VITS integrates semantic embeddings from Llama2 with the VITS model, a leading end-to-end TTS framework. By leveraging Llama2 for the primary speech synthesis process, our experiments demonstrate that Llama-VITS matches the naturalness of the original VITS (ORI-VITS) and those incorporate BERT (BERT-VITS), on the LJSpeech dataset, a substantial collection of neutral, clear speech. Moreover, our method significantly enhances emotive expressiveness on the EmoV_DB_bea_sem dataset, a curated selection of emotionally consistent speech from the EmoV_DB dataset, highlighting its potential to generate emotive speech.

</details>

### [KazEmoTTS: A Dataset for Kazakh Emotional Text-to-Speech Synthesis](2404.01033.md)
**Adal Abilbekov et.al.** · 2024-04-09

### [SpeechAlign: Aligning Speech Generation to Human Preferences](2404.05600.md)
**Dong Zhang, Zhaowei Li, Shimin Li, Xin Zhang et al.** · 2024-04-08

<details>
<summary>Abstract</summary>

Speech language models have significantly advanced in generating realistic speech, with neural codec language models standing out. However, the integration of human feedback to align speech outputs to human preferences is often neglected. This paper addresses this gap by first analyzing the distribution gap in codec language models, highlighting how it leads to discrepancies between the training and inference phases, which negatively affects performance. Then we explore leveraging learning from human feedback to bridge the distribution gap. We introduce SpeechAlign, an iterative self-improvement strategy that aligns speech language models to human preferences. SpeechAlign involves constructing a preference codec dataset contrasting golden codec tokens against synthetic tokens, followed by preference optimization to improve the codec language model. This cycle of improvement is carried out iteratively to steadily convert weak models to strong ones. Through both subjective and objective evaluations, we show that SpeechAlign can bridge the distribution gap and facilitating continuous self-improvement of the speech language model. Moreover, SpeechAlign exhibits robust generalization capabilities and works for smaller models. Code and models will be available at https://github.com/0nutation/SpeechGPT.

</details>

### [Cross-Domain Audio Deepfake Detection: Dataset and Analysis](2404.04904.md)
**Yuang Li, Min Zhang, Mengxin Ren, Miaomiao Ma et al.** · 2024-04-07

<details>
<summary>Abstract</summary>

Audio deepfake detection (ADD) is essential for preventing the misuse of synthetic voices that may infringe on personal rights and privacy. Recent zero-shot text-to-speech (TTS) models pose higher risks as they can clone voices with a single utterance. However, the existing ADD datasets are outdated, leading to suboptimal generalization of detection models. In this paper, we construct a new cross-domain ADD dataset comprising over 300 hours of speech data that is generated by five advanced zero-shot TTS models. To simulate real-world scenarios, we employ diverse attack methods and audio prompts from different datasets. Experiments show that, through novel attack-augmented training, the Wav2Vec2-large and Whisper-medium models achieve equal error rates of 4.1\% and 6.5\% respectively. Additionally, we demonstrate our models' outstanding few-shot ADD ability by fine-tuning with just one minute of target-domain data. Nonetheless, neural codec compressors greatly affect the detection accuracy, necessitating further research.

</details>

### [HyperTTS: Parameter Efficient Adaptation in Text to Speech using Hypernetworks](2404.04645.md)
**Yingting Li et.al.** · 2024-04-06

### [RALL-E: Robust Codec Language Modeling with Chain-of-Thought Prompting for Text-to-Speech Synthesis](2404.03204.md)
**Detai Xin et.al.** · 2024-04-06

### [Open vocabulary keyword spotting through transfer learning from speech synthesis](2404.03914.md)
**Kesavaraj V, Anil Kumar Vuppala** · 2024-04-05

<details>
<summary>Abstract</summary>

Identifying keywords in an open-vocabulary context is crucial for personalizing interactions with smart devices. Previous approaches to open vocabulary keyword spotting dependon a shared embedding space created by audio and text encoders. However, these approaches suffer from heterogeneous modality representations (i.e., audio-text mismatch). To address this issue, our proposed framework leverages knowledge acquired from a pre-trained text-to-speech (TTS) system. This knowledge transfer allows for the incorporation of awareness of audio projections into the text representations derived from the text encoder. The performance of the proposed approach is compared with various baseline methods across four different datasets. The robustness of our proposed model is evaluated by assessing its performance across different word lengths and in an Out-of-Vocabulary (OOV) scenario. Additionally, the effectiveness of transfer learning from the TTS system is investigated by analyzing its different intermediate representations. The experimental results indicate that, in the challenging LibriPhrase Hard dataset, the proposed approach outperformed the cross-modality correspondence detector (CMCD) method by a significant improvement of 8.22% in area under the curve (AUC) and 12.56% in equal error rate (EER).

</details>

### [M3TCM: Multi-modal Multi-task Context Model for Utterance Classification in Motivational Interviews](2404.03312.md)
**Sayed Muddashir Hossain, Jan Alexandersson, Philipp Müller** · 2024-04-04

<details>
<summary>Abstract</summary>

Accurate utterance classification in motivational interviews is crucial to automatically understand the quality and dynamics of client-therapist interaction, and it can serve as a key input for systems mediating such interactions. Motivational interviews exhibit three important characteristics. First, there are two distinct roles, namely client and therapist. Second, they are often highly emotionally charged, which can be expressed both in text and in prosody. Finally, context is of central importance to classify any given utterance. Previous works did not adequately incorporate all of these characteristics into utterance classification approaches for mental health dialogues. In contrast, we present M3TCM, a Multi-modal, Multi-task Context Model for utterance classification. Our approach for the first time employs multi-task learning to effectively model both joint and individual components of therapist and client behaviour. Furthermore, M3TCM integrates information from the text and speech modality as well as the conversation context. With our novel approach, we outperform the state of the art for utterance classification on the recently introduced AnnoMI dataset with a relative improvement of 20% for the client- and by 15% for therapist utterance classification. In extensive ablation studies, we quantify the improvement resulting from each contribution.

</details>

### [CLaM-TTS: Improving Neural Codec Language Model for Zero-Shot Text-to-Speech](2404.02781.md)
**Jaehyeon Kim et.al.** · 2024-04-03

### [Leveraging the Interplay Between Syntactic and Acoustic Cues for Optimizing Korean TTS Pause Formation](2404.02592.md)
**Yejin Jeon, Yunsu Kim, Gary Geunbae Lee** · 2024-04-03

<details>
<summary>Abstract</summary>

Contemporary neural speech synthesis models have indeed demonstrated remarkable proficiency in synthetic speech generation as they have attained a level of quality comparable to that of human-produced speech. Nevertheless, it is important to note that these achievements have predominantly been verified within the context of high-resource languages such as English. Furthermore, the Tacotron and FastSpeech variants show substantial pausing errors when applied to the Korean language, which affects speech perception and naturalness. In order to address the aforementioned issues, we propose a novel framework that incorporates comprehensive modeling of both syntactic and acoustic cues that are associated with pausing patterns. Remarkably, our framework possesses the capability to consistently generate natural speech even for considerably more extended and intricate out-of-domain (OOD) sentences, despite its training on short audio clips. Architectural design choices are validated through comparisons with baseline models and ablation studies using subjective and objective metrics, thus confirming model performance.

</details>

### [A neural speech decoding framework leveraging deep learning and speech synthesis](s2:b9b250920d2fe542a16aab0d8bf5d329d4ca86ab.md)
**Xupeng Chen, Ran Wang, Amirhossein Khalilian-Gourtani, Leyao Yu et al.** · 2024-04-01

<details>
<summary>Abstract</summary>

Recent research has focused on restoring speech in populations with neurological deficits. Chen, Wang et al. develop a framework for decoding speech from neural signals, which could lead to innovative speech prostheses. Decoding human speech from neural signals is essential for brain–computer interface (BCI) technologies that aim to restore speech in populations with neurological deficits. However, it remains a highly challenging task, compounded by the scarce availability of neural signals with corresponding speech, data complexity and high dimensionality. Here we present a novel deep learning-based neural speech decoding framework that includes an ECoG decoder that translates electrocorticographic (ECoG) signals from the cortex into interpretable speech parameters and a novel differentiable speech synthesizer that maps speech parameters to spectrograms. We have developed a companion speech-to-speech auto-encoder consisting of a speech encoder and the same speech synthesizer to generate reference speech parameters to facilitate the ECoG decoder training. This framework generates natural-sounding speech and is highly reproducible across a cohort of 48 participants. Our experimental results show that our models can decode speech with high correlation, even when limited to only causal operations, which is necessary for adoption by real-time neural prostheses. Finally, we successfully decode speech in participants with either left or right hemisphere coverage, which could lead to speech prostheses in patients with deficits resulting from left hemisphere damage.

</details>

### [Humane Speech Synthesis through Zero-Shot Emotion and Disfluency Generation](2404.01339.md)
**Rohan Chaudhury et.al.** · 2024-03-31

### [CM-TTS: Enhancing Real Time Text-to-Speech Synthesis Efficiency through Weighted Samplers and Consistency Models](2404.00569.md)
**Xiang Li, Fan Bu, Ambuj Mehrish, Yingting Li et al.** · 2024-03-31

<details>
<summary>Abstract</summary>

Neural Text-to-Speech (TTS) systems find broad applications in voice assistants, e-learning, and audiobook creation. The pursuit of modern models, like Diffusion Models (DMs), holds promise for achieving high-fidelity, real-time speech synthesis. Yet, the efficiency of multi-step sampling in Diffusion Models presents challenges. Efforts have been made to integrate GANs with DMs, speeding up inference by approximating denoising distributions, but this introduces issues with model convergence due to adversarial training. To overcome this, we introduce CM-TTS, a novel architecture grounded in consistency models (CMs). Drawing inspiration from continuous-time diffusion models, CM-TTS achieves top-quality speech synthesis in fewer steps without adversarial training or pre-trained model dependencies. We further design weighted samplers to incorporate different sampling positions into model training with dynamic probabilities, ensuring unbiased learning throughout the entire training process. We present a real-time mel-spectrogram generation consistency model, validated through comprehensive evaluations. Experimental results underscore CM-TTS's superiority over existing single-step speech synthesis systems, representing a significant advancement in the field.

</details>

### [A Review of Multi-Modal Large Language and Vision Models](2404.01322.md)
**Kilian Carolan, Laura Fennelly, Alan F. Smeaton** · 2024-03-28

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have recently emerged as a focal point of research and application, driven by their unprecedented ability to understand and generate text with human-like quality. Even more recently, LLMs have been extended into multi-modal large language models (MM-LLMs) which extends their capabilities to deal with image, video and audio information, in addition to text. This opens up applications like text-to-video generation, image captioning, text-to-speech, and more and is achieved either by retro-fitting an LLM with multi-modal capabilities, or building a MM-LLM from scratch. This paper provides an extensive review of the current state of those LLMs with multi-modal capabilities as well as the very recent MM-LLMs. It covers the historical development of LLMs especially the advances enabled by transformer-based architectures like OpenAI's GPT series and Google's BERT, as well as the role of attention mechanisms in enhancing model performance. The paper includes coverage of the major and most important of the LLMs and MM-LLMs and also covers the techniques of model tuning, including fine-tuning and prompt engineering, which tailor pre-trained models to specific tasks or domains. Ethical considerations and challenges, such as data bias and model misuse, are also analysed to underscore the importance of responsible AI development and deployment. Finally, we discuss the implications of open-source versus proprietary models in AI research. Through this review, we provide insights into the transformative potential of MM-LLMs in various applications.

</details>

### [NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models](2403.03100.md)
**Zeqian Ju et.al.** · 2024-03-27

### [Low-Latency Neural Speech Phase Prediction based on Parallel Estimation Architecture and Anti-Wrapping Losses for Speech Generation Tasks](2403.17378.md)
**Yang Ai, Zhen-Hua Ling** · 2024-03-26

<details>
<summary>Abstract</summary>

This paper presents a novel neural speech phase prediction model which predicts wrapped phase spectra directly from amplitude spectra. The proposed model is a cascade of a residual convolutional network and a parallel estimation architecture. The parallel estimation architecture is a core module for direct wrapped phase prediction. This architecture consists of two parallel linear convolutional layers and a phase calculation formula, imitating the process of calculating the phase spectra from the real and imaginary parts of complex spectra and strictly restricting the predicted phase values to the principal value interval. To avoid the error expansion issue caused by phase wrapping, we design anti-wrapping training losses defined between the predicted wrapped phase spectra and natural ones by activating the instantaneous phase error, group delay error and instantaneous angular frequency error using an anti-wrapping function. We mathematically demonstrate that the anti-wrapping function should possess three properties, namely parity, periodicity and monotonicity. We also achieve low-latency streamable phase prediction by combining causal convolutions and knowledge distillation training strategies. For both analysis-synthesis and specific speech generation tasks, experimental results show that our proposed neural speech phase prediction model outperforms the iterative phase estimation algorithms and neural network-based phase prediction methods in terms of phase prediction precision, efficiency and robustness. Compared with HiFi-GAN-based waveform reconstruction method, our proposed model also shows outstanding efficiency advantages while ensuring the quality of synthesized speech. To the best of our knowledge, we are the first to directly predict speech phase spectra from amplitude spectra only via neural networks.

</details>

### [VoiceCraft: Zero-Shot Speech Editing and Text-to-Speech in the Wild](2403.16973.md)
**Puyuan Peng et.al.** · 2024-03-25

### [Training Generative Adversarial Network-Based Vocoder with Limited Data Using Augmentation-Conditional Discriminator](2403.16464.md)
**Takuhiro Kaneko, Hirokazu Kameoka, Kou Tanaka** · 2024-03-25

<details>
<summary>Abstract</summary>

A generative adversarial network (GAN)-based vocoder trained with an adversarial discriminator is commonly used for speech synthesis because of its fast, lightweight, and high-quality characteristics. However, this data-driven model requires a large amount of training data incurring high data-collection costs. This fact motivates us to train a GAN-based vocoder on limited data. A promising solution is to augment the training data to avoid overfitting. However, a standard discriminator is unconditional and insensitive to distributional changes caused by data augmentation. Thus, augmented speech (which can be extraordinary) may be considered real speech. To address this issue, we propose an augmentation-conditional discriminator (AugCondD) that receives the augmentation state as input in addition to speech, thereby assessing the input speech according to the augmentation state, without inhibiting the learning of the original non-augmented distribution. Experimental results indicate that AugCondD improves speech quality under limited data conditions while achieving comparable speech quality under sufficient data conditions. Audio samples are available at https://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/augcondd/.

</details>

### [On Zero-Shot Counterspeech Generation by LLMs](2403.14938.md)
**Punyajoy Saha, Aalok Agrawal, Abhik Jana, Chris Biemann et al.** · 2024-03-22

<details>
<summary>Abstract</summary>

With the emergence of numerous Large Language Models (LLM), the usage of such models in various Natural Language Processing (NLP) applications is increasing extensively. Counterspeech generation is one such key task where efforts are made to develop generative models by fine-tuning LLMs with hatespeech - counterspeech pairs, but none of these attempts explores the intrinsic properties of large language models in zero-shot settings. In this work, we present a comprehensive analysis of the performances of four LLMs namely GPT-2, DialoGPT, ChatGPT and FlanT5 in zero-shot settings for counterspeech generation, which is the first of its kind. For GPT-2 and DialoGPT, we further investigate the deviation in performance with respect to the sizes (small, medium, large) of the models. On the other hand, we propose three different prompting strategies for generating different types of counterspeech and analyse the impact of such strategies on the performance of the models. Our analysis shows that there is an improvement in generation quality for two datasets (17%), however the toxicity increase (25%) with increase in model size. Considering type of model, GPT-2 and FlanT5 models are significantly better in terms of counterspeech quality but also have high toxicity as compared to DialoGPT. ChatGPT are much better at generating counter speech than other models across all metrics. In terms of prompting, we find that our proposed strategies help in improving counter speech generation across all the models.

</details>

### [UTDUSS: UTokyo-SaruLab System for Interspeech2024 Speech Processing Using Discrete Speech Unit Challenge](2403.13720.md)
**Wataru Nakata, Kazuki Yamauchi, Dong Yang, Hiroaki Hyodo et al.** · 2024-03-20

<details>
<summary>Abstract</summary>

We present UTDUSS, the UTokyo-SaruLab system submitted to Interspeech2024 Speech Processing Using Discrete Speech Unit Challenge. The challenge focuses on using discrete speech unit learned from large speech corpora for some tasks. We submitted our UTDUSS system to two text-to-speech tracks: Vocoder and Acoustic+Vocoder. Our system incorporates neural audio codec (NAC) pre-trained on only speech corpora, which makes the learned codec represent rich acoustic features that are necessary for high-fidelity speech reconstruction. For the acoustic+vocoder track, we trained an acoustic model based on Transformer encoder-decoder that predicted the pre-trained NAC tokens from text input. We describe our strategies to build these models, such as data selection, downsampling, and hyper-parameter tuning. Our system ranked in second and first for the Vocoder and Acoustic+Vocoder tracks, respectively.

</details>

### [Building speech corpus with diverse voice characteristics for its prompt-based representation](2403.13353.md)
**Aya Watanabe, Shinnosuke Takamichi, Yuki Saito, Wataru Nakata et al.** · 2024-03-20

<details>
<summary>Abstract</summary>

In text-to-speech synthesis, the ability to control voice characteristics is vital for various applications. By leveraging thriving text prompt-based generation techniques, it should be possible to enhance the nuanced control of voice characteristics. While previous research has explored the prompt-based manipulation of voice characteristics, most studies have used pre-recorded speech, which limits the diversity of voice characteristics available. Thus, we aim to address this gap by creating a novel corpus and developing a model for prompt-based manipulation of voice characteristics in text-to-speech synthesis, facilitating a broader range of voice characteristics. Specifically, we propose a method to build a sizable corpus pairing voice characteristics descriptions with corresponding speech samples. This involves automatically gathering voice-related speech data from the Internet, ensuring its quality, and manually annotating it using crowdsourcing. We implement this method with Japanese language data and analyze the results to validate its effectiveness. Subsequently, we propose a construction method of the model to retrieve speech from voice characteristics descriptions based on a contrastive learning method. We train the model using not only conservative contrastive learning but also feature prediction learning to predict quantitative speech features corresponding to voice characteristics. We evaluate the model performance via experiments with the corpus we constructed above.

</details>

### [An Empirical Study of Speech Language Models for Prompt-Conditioned Speech Synthesis](2403.12402.md)
**Yifan Peng, Ilia Kulikov, Yilin Yang, Sravya Popuri et al.** · 2024-03-19

<details>
<summary>Abstract</summary>

Speech language models (LMs) are promising for high-quality speech synthesis through in-context learning. A typical speech LM takes discrete semantic units as content and a short utterance as prompt, and synthesizes speech which preserves the content's semantics but mimics the prompt's style. However, there is no systematic understanding on how the synthesized audio is controlled by the prompt and content. In this work, we conduct an empirical study of the widely used autoregressive (AR) and non-autoregressive (NAR) speech LMs and provide insights into the prompt design and content semantic units. Our analysis reveals that heterogeneous and nonstationary prompts hurt the audio quality in contrast to the previous finding that longer prompts always lead to better synthesis. Moreover, we find that the speaker style of the synthesized audio is also affected by the content in addition to the prompt. We further show that semantic units carry rich acoustic information such as pitch, tempo, volume and speech emphasis, which might be leaked from the content to the synthesized audio.

</details>

### [Creating an African American-Sounding TTS: Guidelines, Technical Challenges,and Surprising Evaluations](2403.11209.md)
**Claudio Pinhanez, Raul Fernandez, Marcelo Grave, Julio Nogima et al.** · 2024-03-17

<details>
<summary>Abstract</summary>

Representations of AI agents in user interfaces and robotics are predominantly White, not only in terms of facial and skin features, but also in the synthetic voices they use. In this paper we explore some unexpected challenges in the representation of race we found in the process of developing an U.S. English Text-to-Speech (TTS) system aimed to sound like an educated, professional, regional accent-free African American woman. The paper starts by presenting the results of focus groups with African American IT professionals where guidelines and challenges for the creation of a representative and appropriate TTS system were discussed and gathered, followed by a discussion about some of the technical difficulties faced by the TTS system developers. We then describe two studies with U.S. English speakers where the participants were not able to attribute the correct race to the African American TTS voice while overwhelmingly correctly recognizing the race of a White TTS system of similar quality. A focus group with African American IT workers not only confirmed the representativeness of the African American voice we built, but also suggested that the surprising recognition results may have been caused by the inability or the latent prejudice from non-African Americans to associate educated, non-vernacular, professionally-sounding voices to African American people.

</details>

### [EM-TTS: Efficiently Trained Low-Resource Mongolian Lightweight Text-to-Speech](2403.08164.md)
**Ziqi Liang, Haoxiang Shi, Jiawei Wang, Keda Lu** · 2024-03-13

<details>
<summary>Abstract</summary>

Recently, deep learning-based Text-to-Speech (TTS) systems have achieved high-quality speech synthesis results. Recurrent neural networks have become a standard modeling technique for sequential data in TTS systems and are widely used. However, training a TTS model which includes RNN components requires powerful GPU performance and takes a long time. In contrast, CNN-based sequence synthesis techniques can significantly reduce the parameters and training time of a TTS model while guaranteeing a certain performance due to their high parallelism, which alleviate these economic costs of training. In this paper, we propose a lightweight TTS system based on deep convolutional neural networks, which is a two-stage training end-to-end TTS model and does not employ any recurrent units. Our model consists of two stages: Text2Spectrum and SSRN. The former is used to encode phonemes into a coarse mel spectrogram and the latter is used to synthesize the complete spectrum from the coarse mel spectrogram. Meanwhile, we improve the robustness of our model by a series of data augmentations, such as noise suppression, time warping, frequency masking and time masking, for solving the low resource mongolian problem. Experiments show that our model can reduce the training time and parameters while ensuring the quality and naturalness of the synthesized speech compared to using mainstream TTS models. Our method uses NCMMSC2022-MTTSC Challenge dataset for validation, which significantly reduces training time while maintaining a certain accuracy.

</details>

### [Fewer-token Neural Speech Codec with Time-invariant Codes](2310.00014.md)
**Yong Ren et.al.** · 2024-03-11

### [HAM-TTS: Hierarchical Acoustic Modeling for Token-Based Zero-Shot Text-to-Speech with Model and Data Scaling](2403.05989.md)
**Chunhui Wang et.al.** · 2024-03-09

### [Attempt Towards Stress Transfer in Speech-to-Speech Machine Translation](2403.04178.md)
**Sai Akarsh, Vamshi Raghusimha, Anindita Mondal, Anil Vuppala** · 2024-03-07

<details>
<summary>Abstract</summary>

The language diversity in India's education sector poses a significant challenge, hindering inclusivity. Despite the democratization of knowledge through online educational content, the dominance of English, as the internet's lingua franca, limits accessibility, emphasizing the crucial need for translation into Indian languages. Despite existing Speech-to-Speech Machine Translation (SSMT) technologies, the lack of intonation in these systems gives monotonous translations, leading to a loss of audience interest and disengagement from the content. To address this, our paper introduces a dataset with stress annotations in Indian English and also a Text-to-Speech (TTS) architecture capable of incorporating stress into synthesized speech. This dataset is used for training a stress detection model, which is then used in the SSMT system for detecting stress in the source speech and transferring it into the target language speech. The TTS architecture is based on FastPitch and can modify the variances based on stressed words given. We present an Indian English-to-Hindi SSMT system that can transfer stress and aim to enhance the overall quality and engagement of educational content.

</details>

### [AttentionStitch: How Attention Solves the Speech Editing Problem](2403.04804.md)
**Antonios Alexos et.al.** · 2024-03-05

### [Making Flow-Matching-Based Zero-Shot Text-to-Speech Laugh as You Like](2402.07383.md)
**Naoyuki Kanda et.al.** · 2024-03-04

### [Brilla AI: AI Contestant for the National Science and Maths Quiz](2403.01699.md)
**George Boateng, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor et al.** · 2024-03-04

<details>
<summary>Abstract</summary>

The African continent lacks enough qualified teachers which hampers the provision of adequate learning support. An AI could potentially augment the efforts of the limited number of teachers, leading to better learning outcomes. Towards that end, this work describes and evaluates the first key output for the NSMQ AI Grand Challenge, which proposes a robust, real-world benchmark for such an AI: "Build an AI to compete live in Ghana's National Science and Maths Quiz (NSMQ) competition and win - performing better than the best contestants in all rounds and stages of the competition". The NSMQ is an annual live science and mathematics competition for senior secondary school students in Ghana in which 3 teams of 2 students compete by answering questions across biology, chemistry, physics, and math in 5 rounds over 5 progressive stages until a winning team is crowned for that year. In this work, we built Brilla AI, an AI contestant that we deployed to unofficially compete remotely and live in the Riddles round of the 2023 NSMQ Grand Finale, the first of its kind in the 30-year history of the competition. Brilla AI is currently available as a web app that livestreams the Riddles round of the contest, and runs 4 machine learning systems: (1) speech to text (2) question extraction (3) question answering and (4) text to speech that work together in real-time to quickly and accurately provide an answer, and then say it with a Ghanaian accent. In its debut, our AI answered one of the 4 riddles ahead of the 3 human contesting teams, unofficially placing second (tied). Improvements and extensions of this AI could potentially be deployed to offer science tutoring to students and eventually enable millions across Africa to have one-on-one learning interactions, democratizing science education.

</details>

### [Fine-Grained Quantitative Emotion Editing for Speech Generation](2403.02002.md)
**Sho Inoue, Kun Zhou, Shuai Wang, Haizhou Li** · 2024-03-04

<details>
<summary>Abstract</summary>

It remains a significant challenge how to quantitatively control the expressiveness of speech emotion in speech generation. In this work, we present a novel approach for manipulating the rendering of emotions for speech generation. We propose a hierarchical emotion distribution extractor, i.e. Hierarchical ED, that quantifies the intensity of emotions at different levels of granularity. Support vector machines (SVMs) are employed to rank emotion intensity, resulting in a hierarchical emotional embedding. Hierarchical ED is subsequently integrated into the FastSpeech2 framework, guiding the model to learn emotion intensity at phoneme, word, and utterance levels. During synthesis, users can manually edit the emotional intensity of the generated voices. Both objective and subjective evaluations demonstrate the effectiveness of the proposed network in terms of fine-grained quantitative emotion editing.

</details>

### [PAVITS: Exploring Prosody-aware VITS for End-to-End Emotional Voice Conversion](2403.01494.md)
**Tianhua Qi, Wenming Zheng, Cheng Lu, Yuan Zong et al.** · 2024-03-03

<details>
<summary>Abstract</summary>

In this paper, we propose Prosody-aware VITS (PAVITS) for emotional voice conversion (EVC), aiming to achieve two major objectives of EVC: high content naturalness and high emotional naturalness, which are crucial for meeting the demands of human perception. To improve the content naturalness of converted audio, we have developed an end-to-end EVC architecture inspired by the high audio quality of VITS. By seamlessly integrating an acoustic converter and vocoder, we effectively address the common issue of mismatch between emotional prosody training and run-time conversion that is prevalent in existing EVC models. To further enhance the emotional naturalness, we introduce an emotion descriptor to model the subtle prosody variations of different speech emotions. Additionally, we propose a prosody predictor, which predicts prosody features from text based on the provided emotion label. Notably, we introduce a prosody alignment loss to establish a connection between latent prosody features from two distinct modalities, ensuring effective training. Experimental results show that the performance of PAVITS is superior to the state-of-the-art EVC methods. Speech Samples are available at https://jeremychee4.github.io/pavits4EVC/ .

</details>

### [Towards Accurate Lip-to-Speech Synthesis in-the-Wild](2403.01087.md)
**Sindhu Hegde, Rudrabha Mukhopadhyay, C. V. Jawahar, Vinay Namboodiri** · 2024-03-02

<details>
<summary>Abstract</summary>

In this paper, we introduce a novel approach to address the task of synthesizing speech from silent videos of any in-the-wild speaker solely based on lip movements. The traditional approach of directly generating speech from lip videos faces the challenge of not being able to learn a robust language model from speech alone, resulting in unsatisfactory outcomes. To overcome this issue, we propose incorporating noisy text supervision using a state-of-the-art lip-to-text network that instills language information into our model. The noisy text is generated using a pre-trained lip-to-text model, enabling our approach to work without text annotations during inference. We design a visual text-to-speech network that utilizes the visual stream to generate accurate speech, which is in-sync with the silent input video. We perform extensive experiments and ablation studies, demonstrating our approach's superiority over the current state-of-the-art methods on various benchmark datasets. Further, we demonstrate an essential practical application of our method in assistive technology by generating speech for an ALS patient who has lost the voice but can make mouth movements. Our demo video, code, and additional details can be found at \url{http://cvit.iiit.ac.in/research/projects/cvit-projects/ms-l2s-itw}.

</details>

### [VoxGenesis: Unsupervised Discovery of Latent Speaker Manifold for Speech Synthesis](2403.00529.md)
**Weiwei Lin, Chenhang He, Man-Wai Mak, Jiachen Lian et al.** · 2024-03-01

<details>
<summary>Abstract</summary>

Achieving nuanced and accurate emulation of human voice has been a longstanding goal in artificial intelligence. Although significant progress has been made in recent years, the mainstream of speech synthesis models still relies on supervised speaker modeling and explicit reference utterances. However, there are many aspects of human voice, such as emotion, intonation, and speaking style, for which it is hard to obtain accurate labels. In this paper, we propose VoxGenesis, a novel unsupervised speech synthesis framework that can discover a latent speaker manifold and meaningful voice editing directions without supervision. VoxGenesis is conceptually simple. Instead of mapping speech features to waveforms deterministically, VoxGenesis transforms a Gaussian distribution into speech distributions conditioned and aligned by semantic tokens. This forces the model to learn a speaker distribution disentangled from the semantic content. During the inference, sampling from the Gaussian distribution enables the creation of novel speakers with distinct characteristics. More importantly, the exploration of latent space uncovers human-interpretable directions associated with specific speaker characteristics such as gender attributes, pitch, tone, and emotion, allowing for voice editing by manipulating the latent codes along these identified directions. We conduct extensive experiments to evaluate the proposed VoxGenesis using both subjective and objective metrics, finding that it produces significantly more diverse and realistic speakers with distinct characteristics than the previous approaches. We also show that latent space manipulation produces consistent and human-identifiable effects that are not detrimental to the speech quality, which was not possible with previous approaches. Audio samples of VoxGenesis can be found at: \url{https://bit.ly/VoxGenesis}.

</details>

### [Transcription and translation of videos using fine-tuned XLSR Wav2Vec2 on custom dataset and mBART](2403.00212.md)
**Aniket Tathe, Anand Kamble, Suyash Kumbharkar, Atharva Bhandare et al.** · 2024-03-01

<details>
<summary>Abstract</summary>

This research addresses the challenge of training an ASR model for personalized voices with minimal data. Utilizing just 14 minutes of custom audio from a YouTube video, we employ Retrieval-Based Voice Conversion (RVC) to create a custom Common Voice 16.0 corpus. Subsequently, a Cross-lingual Self-supervised Representations (XLSR) Wav2Vec2 model is fine-tuned on this dataset. The developed web-based GUI efficiently transcribes and translates input Hindi videos. By integrating XLSR Wav2Vec2 and mBART, the system aligns the translated text with the video timeline, delivering an accessible solution for multilingual video content transcription and translation for personalized voice.

</details>

### [Audio-visual speech synthesis using vision transformer–enhanced autoencoders with ensemble of loss functions](s2:512b58491d14972cd376394ad0c576126a2b8dd5.md)
**Subhayu Ghosh, S. Sarkar, Sovan Ghosh, Frank Zalkow et al.** · 2024-03-01

### [Extending Multilingual Speech Synthesis to 100+ Languages without Transcribed Data](2402.18932.md)
**Takaaki Saeki, Gary Wang, Nobuyuki Morioka, Isaac Elias et al.** · 2024-02-29

<details>
<summary>Abstract</summary>

Collecting high-quality studio recordings of audio is challenging, which limits the language coverage of text-to-speech (TTS) systems. This paper proposes a framework for scaling a multilingual TTS model to 100+ languages using found data without supervision. The proposed framework combines speech-text encoder pretraining with unsupervised training using untranscribed speech and unspoken text data sources, thereby leveraging massively multilingual joint speech and text representation learning. Without any transcribed speech in a new language, this TTS model can generate intelligible speech in >30 unseen languages (CER difference of <10% to ground truth). With just 15 minutes of transcribed, found data, we can reduce the intelligibility difference to 1% or less from the ground-truth, and achieve naturalness scores that match the ground-truth in several languages.

</details>

### [High-Fidelity Neural Phonetic Posteriorgrams](2402.17735.md)
**Cameron Churchwell, Max Morrison, Bryan Pardo** · 2024-02-27

<details>
<summary>Abstract</summary>

A phonetic posteriorgram (PPG) is a time-varying categorical distribution over acoustic units of speech (e.g., phonemes). PPGs are a popular representation in speech generation due to their ability to disentangle pronunciation features from speaker identity, allowing accurate reconstruction of pronunciation (e.g., voice conversion) and coarse-grained pronunciation editing (e.g., foreign accent conversion). In this paper, we demonstrably improve the quality of PPGs to produce a state-of-the-art interpretable PPG representation. We train an off-the-shelf speech synthesizer using our PPG representation and show that high-quality PPGs yield independent control over pitch and pronunciation. We further demonstrate novel uses of PPGs, such as an acoustic pronunciation distance and fine-grained pronunciation control.

</details>

### [SR-TTS: a rhyme-based end-to-end speech synthesis system](s2:0e476a39ddd47f840939a3cac7281968636ac0a4.md)
**Yihao Yao, Tao Liang, Rui Feng, Keke Shi et al.** · 2024-02-27

<details>
<summary>Abstract</summary>

Deep learning has significantly advanced text-to-speech (TTS) systems. These neural network-based systems have enhanced speech synthesis quality and are increasingly vital in applications like human-computer interaction. However, conventional TTS models still face challenges, as the synthesized speeches often lack naturalness and expressiveness. Additionally, the slow inference speed, reflecting low efficiency, contributes to the reduced voice quality. This paper introduces SynthRhythm-TTS (SR-TTS), an optimized Transformer-based structure designed to enhance synthesized speech. SR-TTS not only improves phonological quality and naturalness but also accelerates the speech generation process, thereby increasing inference efficiency. SR-TTS contains an encoder, a rhythm coordinator, and a decoder. In particular, a pre-duration predictor within the cadence coordinator and a self-attention-based feature predictor work together to enhance the naturalness and articulatory accuracy of speech. In addition, the introduction of causal convolution enhances the consistency of the time series. The cross-linguistic capability of SR-TTS is validated by training it on both English and Chinese corpora. Human evaluation shows that SR-TTS outperforms existing techniques in terms of speech quality and naturalness of expression. This technology is particularly suitable for applications that require high-quality natural speech, such as intelligent assistants, speech synthesized podcasts, and human-computer interaction.

</details>

### [An Automated End-to-End Open-Source Software for High-Quality Text-to-Speech Dataset Generation](2402.16380.md)
**Ahmet Gunduz et.al.** · 2024-02-26

### [Towards Decoding Brain Activity During Passive Listening of Speech](2402.16996.md)
**Milán András Fodor, Tamás Gábor Csapó, Frigyes Viktor Arthur** · 2024-02-26

<details>
<summary>Abstract</summary>

The aim of the study is to investigate the complex mechanisms of speech perception and ultimately decode the electrical changes in the brain accruing while listening to speech. We attempt to decode heard speech from intracranial electroencephalographic (iEEG) data using deep learning methods. The goal is to aid the advancement of brain-computer interface (BCI) technology for speech synthesis, and, hopefully, to provide an additional perspective on the cognitive processes of speech perception. This approach diverges from the conventional focus on speech production and instead chooses to investigate neural representations of perceived speech. This angle opened up a complex perspective, potentially allowing us to study more sophisticated neural patterns. Leveraging the power of deep learning models, the research aimed to establish a connection between these intricate neural activities and the corresponding speech sounds. Despite the approach not having achieved a breakthrough yet, the research sheds light on the potential of decoding neural activity during speech perception. Our current efforts can serve as a foundation, and we are optimistic about the potential of expanding and improving upon this work to move closer towards more advanced BCIs, better understanding of processes underlying perceived speech and its relation to spoken speech.

</details>

### [Daisy-TTS: Simulating Wider Spectrum of Emotions via Prosody Embedding Decomposition](2402.14523.md)
**Rendi Chevi et.al.** · 2024-02-22

### [PeriodGrad: Towards Pitch-Controllable Neural Vocoder Based on a Diffusion Probabilistic Model](2402.14692.md)
**Yukiya Hono, Kei Hashimoto, Yoshihiko Nankaku, Keiichi Tokuda** · 2024-02-22

<details>
<summary>Abstract</summary>

This paper presents a neural vocoder based on a denoising diffusion probabilistic model (DDPM) incorporating explicit periodic signals as auxiliary conditioning signals. Recently, DDPM-based neural vocoders have gained prominence as non-autoregressive models that can generate high-quality waveforms. The neural vocoders based on DDPM have the advantage of training with a simple time-domain loss. In practical applications, such as singing voice synthesis, there is a demand for neural vocoders to generate high-fidelity speech waveforms with flexible pitch control. However, conventional DDPM-based neural vocoders struggle to generate speech waveforms under such conditions. Our proposed model aims to accurately capture the periodic structure of speech waveforms by incorporating explicit periodic signals. Experimental results show that our model improves sound quality and provides better pitch control than conventional DDPM-based neural vocoders.

</details>

### [Compression Robust Synthetic Speech Detection Using Patched Spectrogram Transformer](2402.14205.md)
**Amit Kumar Singh Yadav, Ziyue Xiang, Kratika Bhagtani, Paolo Bestagini et al.** · 2024-02-22

<details>
<summary>Abstract</summary>

Many deep learning synthetic speech generation tools are readily available. The use of synthetic speech has caused financial fraud, impersonation of people, and misinformation to spread. For this reason forensic methods that can detect synthetic speech have been proposed. Existing methods often overfit on one dataset and their performance reduces substantially in practical scenarios such as detecting synthetic speech shared on social platforms. In this paper we propose, Patched Spectrogram Synthetic Speech Detection Transformer (PS3DT), a synthetic speech detector that converts a time domain speech signal to a mel-spectrogram and processes it in patches using a transformer neural network. We evaluate the detection performance of PS3DT on ASVspoof2019 dataset. Our experiments show that PS3DT performs well on ASVspoof2019 dataset compared to other approaches using spectrogram for synthetic speech detection. We also investigate generalization performance of PS3DT on In-the-Wild dataset. PS3DT generalizes well than several existing methods on detecting synthetic speech from an out-of-distribution dataset. We also evaluate robustness of PS3DT to detect telephone quality synthetic speech and synthetic speech shared on social platforms (compressed speech). PS3DT is robust to compression and can detect telephone quality synthetic speech better than several existing methods.

</details>

### [Advancing Large Language Models to Capture Varied Speaking Styles and Respond Properly in Spoken Conversations](2402.12786.md)
**Guan-Ting Lin, Cheng-Han Chiang, Hung-yi Lee** · 2024-02-20

<details>
<summary>Abstract</summary>

In spoken dialogue, even if two current turns are the same sentence, their responses might still differ when they are spoken in different styles. The spoken styles, containing paralinguistic and prosodic information, mark the most significant difference between text and speech modality. When using text-only LLMs to model spoken dialogue, text-only LLMs cannot give different responses based on the speaking style of the current turn. In this paper, we focus on enabling LLMs to listen to the speaking styles and respond properly. Our goal is to teach the LLM that "even if the sentences are identical if they are spoken in different styles, their corresponding responses might be different". Since there is no suitable dataset for achieving this goal, we collect a speech-to-speech dataset, StyleTalk, with the following desired characteristics: when two current speeches have the same content but are spoken in different styles, their responses will be different. To teach LLMs to understand and respond properly to the speaking styles, we propose the Spoken-LLM framework that can model the linguistic content and the speaking styles. We train Spoken-LLM using the StyleTalk dataset and devise a two-stage training pipeline to help the Spoken-LLM better learn the speaking styles. Based on extensive experiments, we show that Spoken-LLM outperforms text-only baselines and prior speech LLMs methods.

</details>

### [SingVisio: Visual Analytics of Diffusion Model for Singing Voice Conversion](2402.12660.md)
**Liumeng Xue, Chaoren Wang, Mingxuan Wang, Xueyao Zhang et al.** · 2024-02-20

<details>
<summary>Abstract</summary>

In this study, we present SingVisio, an interactive visual analysis system that aims to explain the diffusion model used in singing voice conversion. SingVisio provides a visual display of the generation process in diffusion models, showcasing the step-by-step denoising of the noisy spectrum and its transformation into a clean spectrum that captures the desired singer's timbre. The system also facilitates side-by-side comparisons of different conditions, such as source content, melody, and target timbre, highlighting the impact of these conditions on the diffusion generation process and resulting conversions. Through comparative and comprehensive evaluations, SingVisio demonstrates its effectiveness in terms of system design, functionality, explainability, and user-friendliness. It offers users of various backgrounds valuable learning experiences and insights into the diffusion model for singing voice conversion.

</details>

### [StyleDubber: Towards Multi-Scale Style Learning for Movie Dubbing](2402.12636.md)
**Gaoxiang Cong, Yuankai Qi, Liang Li, Amin Beheshti et al.** · 2024-02-20

<details>
<summary>Abstract</summary>

Given a script, the challenge in Movie Dubbing (Visual Voice Cloning, V2C) is to generate speech that aligns well with the video in both time and emotion, based on the tone of a reference audio track. Existing state-of-the-art V2C models break the phonemes in the script according to the divisions between video frames, which solves the temporal alignment problem but leads to incomplete phoneme pronunciation and poor identity stability. To address this problem, we propose StyleDubber, which switches dubbing learning from the frame level to phoneme level. It contains three main components: (1) A multimodal style adaptor operating at the phoneme level to learn pronunciation style from the reference audio, and generate intermediate representations informed by the facial emotion presented in the video; (2) An utterance-level style learning module, which guides both the mel-spectrogram decoding and the refining processes from the intermediate embeddings to improve the overall style expression; And (3) a phoneme-guided lip aligner to maintain lip sync. Extensive experiments on two of the primary benchmarks, V2C and Grid, demonstrate the favorable performance of the proposed method as compared to the current stateof-the-art. The code will be made available at https://github.com/GalaxyCong/StyleDubber.

</details>

### [On the Semantic Latent Space of Diffusion-Based Text-to-Speech Models](2402.12423.md)
**Miri Varshavsky-Hassid et.al.** · 2024-02-19

### [Bayesian Parameter-Efficient Fine-Tuning for Overcoming Catastrophic Forgetting](2402.12220.md)
**Haolin Chen, Philip N. Garner** · 2024-02-19

<details>
<summary>Abstract</summary>

We are motivated primarily by the adaptation of text-to-speech synthesis models; however we argue that more generic parameter-efficient fine-tuning (PEFT) is an appropriate framework to do such adaptation. Nevertheless, catastrophic forgetting remains an issue with PEFT, damaging the pre-trained model's inherent capabilities. We demonstrate that existing Bayesian learning techniques can be applied to PEFT to prevent catastrophic forgetting as long as the parameter shift of the fine-tuned layers can be calculated differentiably. In a principled series of experiments on language modeling and speech synthesis tasks, we utilize established Laplace approximations, including diagonal and Kronecker-factored approaches, to regularize PEFT with the low-rank adaptation (LoRA) and compare their performance in pre-training knowledge preservation. Our results demonstrate that catastrophic forgetting can be overcome by our methods without degrading the fine-tuning performance, and using the Kronecker-factored approximation produces a better preservation of the pre-training knowledge than the diagonal ones.

</details>

### [Speaking in Wavelet Domain: A Simple and Efficient Approach to Speed up Speech Diffusion Model](2402.10642.md)
**Xiangyu Zhang, Daijiao Liu, Hexin Liu, Qiquan Zhang et al.** · 2024-02-16

<details>
<summary>Abstract</summary>

Recently, Denoising Diffusion Probabilistic Models (DDPMs) have attained leading performances across a diverse range of generative tasks. However, in the field of speech synthesis, although DDPMs exhibit impressive performance, their long training duration and substantial inference costs hinder practical deployment. Existing approaches primarily focus on enhancing inference speed, while approaches to accelerate training a key factor in the costs associated with adding or customizing voices often necessitate complex modifications to the model, compromising their universal applicability. To address the aforementioned challenges, we propose an inquiry: is it possible to enhance the training/inference speed and performance of DDPMs by modifying the speech signal itself? In this paper, we double the training and inference speed of Speech DDPMs by simply redirecting the generative target to the wavelet domain. This method not only achieves comparable or superior performance to the original model in speech synthesis tasks but also demonstrates its versatility. By investigating and utilizing different wavelet bases, our approach proves effective not just in speech synthesis, but also in speech enhancement.

</details>

### [BASE TTS: Lessons from building a billion-parameter Text-to-Speech model on 100K hours of data](2402.08093.md)
**Mateusz Łajszczak et.al.** · 2024-02-15

### [MobileSpeech: A Fast and High-Fidelity Framework for Mobile Zero-Shot Text-to-Speech](2402.09378.md)
**Shengpeng Ji et.al.** · 2024-02-14

### [Deep learning-based expressive speech synthesis: a systematic review of approaches, challenges, and resources](s2:3982a48c833e376ff0991faf31e1cd0b00bba0aa.md)
**Huda Barakat, O. Turk, C. Demiroğlu** · 2024-02-12

<details>
<summary>Abstract</summary>

Speech synthesis has made significant strides thanks to the transition from machine learning to deep learning models. Contemporary text-to-speech (TTS) models possess the capability to generate speech of exceptionally high quality, closely mimicking human speech. Nevertheless, given the wide array of applications now employing TTS models, mere high-quality speech generation is no longer sufficient. Present-day TTS models must also excel at producing expressive speech that can convey various speaking styles and emotions, akin to human speech. Consequently, researchers have concentrated their efforts on developing more efficient models for expressive speech synthesis in recent years. This paper presents a systematic review of the literature on expressive speech synthesis models published within the last 5 years, with a particular emphasis on approaches based on deep learning. We offer a comprehensive classification scheme for these models and provide concise descriptions of models falling into each category. Additionally, we summarize the principal challenges encountered in this research domain and outline the strategies employed to tackle these challenges as documented in the literature. In the Section 8, we pinpoint some research gaps in this field that necessitate further exploration. Our objective with this work is to give an all-encompassing overview of this hot research area to offer guidance to interested researchers and future endeavors in this field.

</details>

### [A New Approach to Voice Authenticity](2402.06304.md)
**Nicolas M. Müller, Piotr Kawa, Shen Hu, Matthias Neu et al.** · 2024-02-09

<details>
<summary>Abstract</summary>

Voice faking, driven primarily by recent advances in text-to-speech (TTS) synthesis technology, poses significant societal challenges. Currently, the prevailing assumption is that unaltered human speech can be considered genuine, while fake speech comes from TTS synthesis. We argue that this binary distinction is oversimplified. For instance, altered playback speeds can be used for malicious purposes, like in the 'Drunken Nancy Pelosi' incident. Similarly, editing of audio clips can be done ethically, e.g., for brevity or summarization in news reporting or podcasts, but editing can also create misleading narratives. In this paper, we propose a conceptual shift away from the binary paradigm of audio being either 'fake' or 'real'. Instead, our focus is on pinpointing 'voice edits', which encompass traditional modifications like filters and cuts, as well as TTS synthesis and VC systems. We delineate 6 categories and curate a new challenge dataset rooted in the M-AILABS corpus, for which we present baseline detection systems. And most importantly, we argue that merely categorizing audio as fake or real is a dangerous over-simplification that will fail to move the field of speech technology forward.

</details>

### [GLA-Grad: A Griffin-Lim Extended Waveform Generation Diffusion Model](2402.15516.md)
**Haocheng Liu, Teysir Baoueb, Mathieu Fontaine, Jonathan Le Roux et al.** · 2024-02-09

<details>
<summary>Abstract</summary>

Diffusion models are receiving a growing interest for a variety of signal generation tasks such as speech or music synthesis. WaveGrad, for example, is a successful diffusion model that conditionally uses the mel spectrogram to guide a diffusion process for the generation of high-fidelity audio. However, such models face important challenges concerning the noise diffusion process for training and inference, and they have difficulty generating high-quality speech for speakers that were not seen during training. With the aim of minimizing the conditioning error and increasing the efficiency of the noise diffusion process, we propose in this paper a new scheme called GLA-Grad, which consists in introducing a phase recovery algorithm such as the Griffin-Lim algorithm (GLA) at each step of the regular diffusion process. Furthermore, it can be directly applied to an already-trained waveform generation model, without additional training or fine-tuning. We show that our algorithm outperforms state-of-the-art diffusion models for speech generation, especially when generating speech for a previously unseen target speaker.

</details>

### [Spirit LM: Interleaved Spoken and Written Language Model](2402.05755.md)
**Tu Anh Nguyen, Benjamin Muller, Bokai Yu, Marta R. Costa-jussa et al.** · 2024-02-08

<details>
<summary>Abstract</summary>

We introduce Spirit LM, a foundation multimodal language model that freely mixes text and speech. Our model is based on a 7B pretrained text language model that we extend to the speech modality by continuously training it on text and speech units. Speech and text sequences are concatenated as a single stream of tokens, and trained with a word-level interleaving method using a small automatically-curated speech-text parallel corpus. Spirit LM comes in two versions: a Base version that uses speech phonetic units (HuBERT) and an Expressive version that models expressivity using pitch and style units in addition to the phonetic units. For both versions, the text is encoded with subword BPE tokens. The resulting model displays both the semantic abilities of text models and the expressive abilities of speech models. Additionally, we demonstrate that Spirit LM can learn new tasks in a few-shot fashion across modalities (i.e. ASR, TTS, Speech Classification). We make available model weights and inference code.

</details>

### [Enhancing the Stability of LLM-based Speech Generation Systems through Self-Supervised Representations](2402.03407.md)
**Álvaro Martín-Cortinas et.al.** · 2024-02-05

### [Enhance Reasoning for Large Language Models in the Game Werewolf](2402.02330.md)
**Shuang Wu, Liwen Zhu, Tao Yang, Shiwei Xu et al.** · 2024-02-04

<details>
<summary>Abstract</summary>

This paper presents an innovative framework that integrates Large Language Models (LLMs) with an external Thinker module to enhance the reasoning capabilities of LLM-based agents. Unlike augmenting LLMs with prompt engineering, Thinker directly harnesses knowledge from databases and employs various optimization techniques. The framework forms a reasoning hierarchy where LLMs handle intuitive System-1 tasks such as natural language processing, while the Thinker focuses on cognitive System-2 tasks that require complex logical analysis and domain-specific knowledge. Our framework is presented using a 9-player Werewolf game that demands dual-system reasoning. We introduce a communication protocol between LLMs and the Thinker, and train the Thinker using data from 18800 human sessions and reinforcement learning. Experiments demonstrate the framework's effectiveness in deductive reasoning, speech generation, and online game evaluation. Additionally, we fine-tune a 6B LLM to surpass GPT4 when integrated with the Thinker. This paper also contributes the largest dataset for social deduction games to date.

</details>

### [Natural language guidance of high-fidelity text-to-speech with synthetic annotations](2402.01912.md)
**Dan Lyth et.al.** · 2024-02-02

### [DQR-TTS: Semi-supervised Text-to-speech Synthesis with Dynamic Quantized Representation](2311.07965.md)
**Jianzong Wang et.al.** · 2024-02-02

### [A Case Study on Filtering for End-to-End Speech Translation](2402.01945.md)
**Md Mahfuz Ibn Alam, Antonios Anastasopoulos** · 2024-02-02

<details>
<summary>Abstract</summary>

It is relatively easy to mine a large parallel corpus for any machine learning task, such as speech-to-text or speech-to-speech translation. Although these mined corpora are large in volume, their quality is questionable. This work shows that the simplest filtering technique can trim down these big, noisy datasets to a more manageable, clean dataset. We also show that using this clean dataset can improve the model's performance, as in the case of the multilingual-to-English Speech Translation (ST) model, where, on average, we obtain a 4.65 BLEU score improvement.

</details>

### [Low-Resource Cross-Domain Singing Voice Synthesis via Reduced Self-Supervised Speech Representations](2402.01520.md)
**Panos Kakoulidis, Nikolaos Ellinas, Georgios Vamvoukakis, Myrsini Christidou et al.** · 2024-02-02

<details>
<summary>Abstract</summary>

In this paper, we propose a singing voice synthesis model, Karaoker-SSL, that is trained only on text and speech data as a typical multi-speaker acoustic model. It is a low-resource pipeline that does not utilize any singing data end-to-end, since its vocoder is also trained on speech data. Karaoker-SSL is conditioned by self-supervised speech representations in an unsupervised manner. We preprocess these representations by selecting only a subset of their task-correlated dimensions. The conditioning module is indirectly guided to capture style information during training by multi-tasking. This is achieved with a Conformer-based module, which predicts the pitch from the acoustic model's output. Thus, Karaoker-SSL allows singing voice synthesis without reliance on hand-crafted and domain-specific features. There are also no requirements for text alignments or lyrics timestamps. To refine the voice quality, we employ a U-Net discriminator that is conditioned on the target speaker and follows a Diffusion GAN training scheme.

</details>

### [Frame-Wise Breath Detection with Self-Training: An Exploration of Enhancing Breath Naturalness in Text-to-Speech](2402.00288.md)
**Dong Yang et.al.** · 2024-02-01

### [PAM: Prompting Audio-Language Models for Audio Quality Assessment](2402.00282.md)
**Soham Deshmukh, Dareen Alharthi, Benjamin Elizalde, Hannes Gamper et al.** · 2024-02-01

<details>
<summary>Abstract</summary>

While audio quality is a key performance metric for various audio processing tasks, including generative modeling, its objective measurement remains a challenge. Audio-Language Models (ALMs) are pre-trained on audio-text pairs that may contain information about audio quality, the presence of artifacts, or noise. Given an audio input and a text prompt related to quality, an ALM can be used to calculate a similarity score between the two. Here, we exploit this capability and introduce PAM, a no-reference metric for assessing audio quality for different audio processing tasks. Contrary to other "reference-free" metrics, PAM does not require computing embeddings on a reference dataset nor training a task-specific model on a costly set of human listening scores. We extensively evaluate the reliability of PAM against established metrics and human listening scores on four tasks: text-to-audio (TTA), text-to-music generation (TTM), text-to-speech (TTS), and deep noise suppression (DNS). We perform multiple ablation studies with controlled distortions, in-the-wild setups, and prompt choices. Our evaluation shows that PAM correlates well with existing metrics and human listening scores. These results demonstrate the potential of ALMs for computing a general-purpose audio quality metric.

</details>

### [ReFlow-TTS: A Rectified Flow Model for High-fidelity Text-to-Speech](2309.17056.md)
**Wenhao Guan et.al.** · 2024-01-31

### [VALL-T: Decoder-Only Generative Transducer for Robust and Decoding-Controllable Text-to-Speech](2401.14321.md)
**Chenpeng Du et.al.** · 2024-01-30

### [SpecDiff-GAN: A Spectrally-Shaped Noise Diffusion GAN for Speech and Music Synthesis](2402.01753.md)
**Teysir Baoueb, Haocheng Liu, Mathieu Fontaine, Jonathan Le Roux et al.** · 2024-01-30

<details>
<summary>Abstract</summary>

Generative adversarial network (GAN) models can synthesize highquality audio signals while ensuring fast sample generation. However, they are difficult to train and are prone to several issues including mode collapse and divergence. In this paper, we introduce SpecDiff-GAN, a neural vocoder based on HiFi-GAN, which was initially devised for speech synthesis from mel spectrogram. In our model, the training stability is enhanced by means of a forward diffusion process which consists in injecting noise from a Gaussian distribution to both real and fake samples before inputting them to the discriminator. We further improve the model by exploiting a spectrally-shaped noise distribution with the aim to make the discriminator's task more challenging. We then show the merits of our proposed model for speech and music synthesis on several datasets. Our experiments confirm that our model compares favorably in audio quality and efficiency compared to several baselines.

</details>

### [SongBsAb: A Dual Prevention Approach against Singing Voice Conversion based Illegal Song Covers](2401.17133.md)
**Guangke Chen, Yedi Zhang, Fu Song, Ting Wang et al.** · 2024-01-30

<details>
<summary>Abstract</summary>

Singing voice conversion (SVC) automates song covers by converting a source singing voice from a source singer into a new singing voice with the same lyrics and melody as the source, but sounds like being covered by the target singer of some given target singing voices. However, it raises serious concerns about copyright and civil right infringements. We propose SongBsAb, the first proactive approach to tackle SVC-based illegal song covers. SongBsAb adds perturbations to singing voices before releasing them, so that when they are used, the process of SVC will be interfered, leading to unexpected singing voices. Perturbations are carefully crafted to (1) provide a dual prevention, i.e., preventing the singing voice from being used as the source and target singing voice in SVC, by proposing a gender-transformation loss and a high/low hierarchy multi-target loss, respectively; and (2) be harmless, i.e., no side-effect on the enjoyment of protected songs, by refining a psychoacoustic model-based loss with the backing track as an additional masker, a unique accompanying element for singing voices compared to ordinary speech voices. We also adopt a frame-level interaction reduction-based loss and encoder ensemble to enhance the transferability of SongBsAb to unknown SVC models. We demonstrate the prevention effectiveness, harmlessness, and robustness of SongBsAb on five diverse and promising SVC models, using both English and Chinese datasets, and both objective and human study-based subjective metrics. Our work fosters an emerging research direction for mitigating illegal automated song covers.

</details>

### [Proactive Detection of Voice Cloning with Localized Watermarking](2401.17264.md)
**Robin San Roman, Pierre Fernandez, Alexandre Défossez, Teddy Furon et al.** · 2024-01-30

<details>
<summary>Abstract</summary>

In the rapidly evolving field of speech generative models, there is a pressing need to ensure audio authenticity against the risks of voice cloning. We present AudioSeal, the first audio watermarking technique designed specifically for localized detection of AI-generated speech. AudioSeal employs a generator/detector architecture trained jointly with a localization loss to enable localized watermark detection up to the sample level, and a novel perceptual loss inspired by auditory masking, that enables AudioSeal to achieve better imperceptibility. AudioSeal achieves state-of-the-art performance in terms of robustness to real life audio manipulations and imperceptibility based on automatic and human evaluation metrics. Additionally, AudioSeal is designed with a fast, single-pass detector, that significantly surpasses existing models in speed - achieving detection up to two orders of magnitude faster, making it ideal for large-scale and real-time applications.

</details>

### [SpeechBERTScore: Reference-Aware Automatic Evaluation of Speech Generation Leveraging NLP Evaluation Metrics](2401.16812.md)
**Takaaki Saeki, Soumi Maiti, Shinnosuke Takamichi, Shinji Watanabe et al.** · 2024-01-30

<details>
<summary>Abstract</summary>

While subjective assessments have been the gold standard for evaluating speech generation, there is a growing need for objective metrics that are highly correlated with human subjective judgments due to their cost efficiency. This paper proposes reference-aware automatic evaluation methods for speech generation inspired by evaluation metrics in natural language processing. The proposed SpeechBERTScore computes the BERTScore for self-supervised dense speech features of the generated and reference speech, which can have different sequential lengths. We also propose SpeechBLEU and SpeechTokenDistance, which are computed on speech discrete tokens. The evaluations on synthesized speech show that our method correlates better with human subjective ratings than mel cepstral distortion and a recent mean opinion score prediction model. Also, they are effective in noisy speech evaluation and have cross-lingual applicability.

</details>

### [MunTTS: A Text-to-Speech System for Mundari](2401.15579.md)
**Varun Gumma, Rishav Hada, Aditya Yadavalli, Pamir Gogoi et al.** · 2024-01-28

<details>
<summary>Abstract</summary>

We present MunTTS, an end-to-end text-to-speech (TTS) system specifically for Mundari, a low-resource Indian language of the Austo-Asiatic family. Our work addresses the gap in linguistic technology for underrepresented languages by collecting and processing data to build a speech synthesis system. We begin our study by gathering a substantial dataset of Mundari text and speech and train end-to-end speech models. We also delve into the methods used for training our models, ensuring they are efficient and effective despite the data constraints. We evaluate our system with native speakers and objective metrics, demonstrating its potential as a tool for preserving and promoting the Mundari language in the digital age.

</details>

### [Not My Voice! A Taxonomy of Ethical and Safety Harms of Speech Generators](2402.01708.md)
**Wiebke Hutiri, Oresiti Papakyriakopoulos, Alice Xiang** · 2024-01-25

<details>
<summary>Abstract</summary>

The rapid and wide-scale adoption of AI to generate human speech poses a range of significant ethical and safety risks to society that need to be addressed. For example, a growing number of speech generation incidents are associated with swatting attacks in the United States, where anonymous perpetrators create synthetic voices that call police officers to close down schools and hospitals, or to violently gain access to innocent citizens' homes. Incidents like this demonstrate that multimodal generative AI risks and harms do not exist in isolation, but arise from the interactions of multiple stakeholders and technical AI systems. In this paper we analyse speech generation incidents to study how patterns of specific harms arise. We find that specific harms can be categorised according to the exposure of affected individuals, that is to say whether they are a subject of, interact with, suffer due to, or are excluded from speech generation systems. Similarly, specific harms are also a consequence of the motives of the creators and deployers of the systems. Based on these insights we propose a conceptual framework for modelling pathways to ethical and safety harms of AI, which we use to develop a taxonomy of harms of speech generators. Our relational approach captures the complexity of risks and harms in sociotechnical AI systems, and yields a taxonomy that can support appropriate policy interventions and decision making for the responsible development and release of speech generation models.

</details>

### [Intelli-Z: Toward Intelligible Zero-Shot TTS](2401.13921.md)
**Sunghee Jung, Won Jang, Jaesam Yoon, Bongwan Kim** · 2024-01-25

<details>
<summary>Abstract</summary>

Although numerous recent studies have suggested new frameworks for zero-shot TTS using large-scale, real-world data, studies that focus on the intelligibility of zero-shot TTS are relatively scarce. Zero-shot TTS demands additional efforts to ensure clear pronunciation and speech quality due to its inherent requirement of replacing a core parameter (speaker embedding or acoustic prompt) with a new one at the inference stage. In this study, we propose a zero-shot TTS model focused on intelligibility, which we refer to as Intelli-Z. Intelli-Z learns speaker embeddings by using multi-speaker TTS as its teacher and is trained with a cycle-consistency loss to include mismatched text-speech pairs for training. Additionally, it selectively aggregates speaker embeddings along the temporal dimension to minimize the interference of the text content of reference speech at the inference stage. We substantiate the effectiveness of the proposed methods with an ablation study. The Mean Opinion Score (MOS) increases by 9% for unseen speakers when the first two methods are applied, and it further improves by 16% when selective temporal aggregation is applied.

</details>

### [SpeechGPT-Gen: Scaling Chain-of-Information Speech Generation](2401.13527.md)
**Dong Zhang, Xin Zhang, Jun Zhan, Shimin Li et al.** · 2024-01-24

<details>
<summary>Abstract</summary>

Benefiting from effective speech modeling, current Speech Large Language Models (SLLMs) have demonstrated exceptional capabilities in in-context speech generation and efficient generalization to unseen speakers. However, the prevailing information modeling process is encumbered by certain redundancies, leading to inefficiencies in speech generation. We propose Chain-of-Information Generation (CoIG), a method for decoupling semantic and perceptual information in large-scale speech generation. Building on this, we develop SpeechGPT-Gen, an 8-billion-parameter SLLM efficient in semantic and perceptual information modeling. It comprises an autoregressive model based on LLM for semantic information modeling and a non-autoregressive model employing flow matching for perceptual information modeling. Additionally, we introduce the novel approach of infusing semantic information into the prior distribution to enhance the efficiency of flow matching. Extensive experimental results demonstrate that SpeechGPT-Gen markedly excels in zero-shot text-to-speech, zero-shot voice conversion, and speech-to-speech dialogue, underscoring CoIG's remarkable proficiency in capturing and modeling speech's semantic and perceptual dimensions. Code and models are available at https://github.com/0nutation/SpeechGPT.

</details>

### [Scaling NVIDIA's Multi-speaker Multi-lingual TTS Systems with Zero-Shot TTS to Indic Languages](2401.13851.md)
**Akshit Arora, Rohan Badlani, Sungwon Kim, Rafael Valle et al.** · 2024-01-24

<details>
<summary>Abstract</summary>

In this paper, we describe the TTS models developed by NVIDIA for the MMITS-VC (Multi-speaker, Multi-lingual Indic TTS with Voice Cloning) 2024 Challenge. In Tracks 1 and 2, we utilize RAD-MMM to perform few-shot TTS by training additionally on 5 minutes of target speaker data. In Track 3, we utilize P-Flow to perform zero-shot TTS by training on the challenge dataset as well as external datasets. We use HiFi-GAN vocoders for all submissions. RAD-MMM performs competitively on Tracks 1 and 2, while P-Flow ranks first on Track 3, with mean opinion score (MOS) 4.4 and speaker similarity score (SMOS) of 3.62.

</details>

### [Maximizing Data Efficiency for Cross-Lingual TTS Adaptation by Self-Supervised Representation Mixing and Embedding Initialization](2402.01692.md)
**Wei-Ping Huang et.al.** · 2024-01-23

### [SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models](2308.16692.md)
**Xin Zhang et.al.** · 2024-01-23

### [Latent Filling: Latent Space Data Augmentation for Zero-shot Speech Synthesis](2310.03538.md)
**Jae-Sung Bae et.al.** · 2024-01-22

### [Benchmarking Large Multimodal Models against Common Corruptions](2401.11943.md)
**Jiawei Zhang, Tianyu Pang, Chao Du, Yi Ren et al.** · 2024-01-22

<details>
<summary>Abstract</summary>

This technical report aims to fill a deficiency in the assessment of large multimodal models (LMMs) by specifically examining the self-consistency of their outputs when subjected to common corruptions. We investigate the cross-modal interactions between text, image, and speech, encompassing four essential generation tasks: text-to-image, image-to-text, text-to-speech, and speech-to-text. We create a comprehensive benchmark, named MMCBench, that covers more than 100 popular LMMs (totally over 150 model checkpoints). A thorough evaluation under common corruptions is critical for practical deployment and facilitates a better understanding of the reliability of cutting-edge LMMs. The benchmarking code is available at https://github.com/sail-sg/MMCBench

</details>

### [Data-driven grapheme-to-phoneme representations for a lexicon-free text-to-speech](2401.10465.md)
**Abhinav Garg et.al.** · 2024-01-19

### [Ultra-lightweight Neural Differential DSP Vocoder For High Quality Speech Synthesis](2401.10460.md)
**Prabhav Agrawal, Thilo Koehler, Zhiping Xiu, Prashant Serai et al.** · 2024-01-19

<details>
<summary>Abstract</summary>

Neural vocoders model the raw audio waveform and synthesize high-quality audio, but even the highly efficient ones, like MB-MelGAN and LPCNet, fail to run real-time on a low-end device like a smartglass. A pure digital signal processing (DSP) based vocoder can be implemented via lightweight fast Fourier transforms (FFT), and therefore, is a magnitude faster than any neural vocoder. A DSP vocoder often gets a lower audio quality due to consuming over-smoothed acoustic model predictions of approximate representations for the vocal tract. In this paper, we propose an ultra-lightweight differential DSP (DDSP) vocoder that uses a jointly optimized acoustic model with a DSP vocoder, and learns without an extracted spectral feature for the vocal tract. The model achieves audio quality comparable to neural vocoders with a high average MOS of 4.36 while being efficient as a DSP vocoder. Our C++ implementation, without any hardware-specific optimization, is at 15 MFLOPS, surpasses MB-MelGAN by 340 times in terms of FLOPS, and achieves a vocoder-only RTF of 0.003 and overall RTF of 0.044 while running single-threaded on a 2GHz Intel Xeon CPU.

</details>

### [StreamVoice: Streamable Context-Aware Language Modeling for Real-time Zero-Shot Voice Conversion](2401.11053.md)
**Zhichao Wang, Yuanzhe Chen, Xinsheng Wang, Lei Xie et al.** · 2024-01-19

<details>
<summary>Abstract</summary>

Recent language model (LM) advancements have showcased impressive zero-shot voice conversion (VC) performance. However, existing LM-based VC models usually apply offline conversion from source semantics to acoustic features, demanding the complete source speech and limiting their deployment to real-time applications. In this paper, we introduce StreamVoice, a novel streaming LM-based model for zero-shot VC, facilitating real-time conversion given arbitrary speaker prompts and source speech. Specifically, to enable streaming capability, StreamVoice employs a fully causal context-aware LM with a temporal-independent acoustic predictor, while alternately processing semantic and acoustic features at each time step of autoregression which eliminates the dependence on complete source speech. To address the potential performance degradation from the incomplete context in streaming processing, we enhance the context-awareness of the LM through two strategies: 1) teacher-guided context foresight, using a teacher model to summarize the present and future semantic context during training to guide the model's forecasting for missing context; 2) semantic masking strategy, promoting acoustic prediction from preceding corrupted semantic and acoustic input, enhancing context-learning ability. Notably, StreamVoice is the first LM-based streaming zero-shot VC model without any future look-ahead. Experiments demonstrate StreamVoice's streaming conversion capability while achieving zero-shot performance comparable to non-streaming VC systems.

</details>

### [Gfl-TTS: A text-to-speech model that combines new tonal prediction and alignment](s2:f72871eec2841731ab009e2f25bc666a790dae86.md)
**Yihao Wang, Junhui Niu, Xuegang Deng, Hao Li** · 2024-01-19

<details>
<summary>Abstract</summary>

Despite the considerable attention and successful generation of human-like speech by text-to-speech (TTS) models, there remains ample room for improvement in the naturalness of their speech output and the efficiency of speech-to-text alignment. This paper introduces Gfl-TTS, an acoustic model based on the Grad-TTS backbone network that incorporates prosody prediction and a novel alignment module. During training, this model predicts pitch contours, uniformly increases or decreases F0 information, and introduces an alignment module to enhance the prosody of generated audio. Experimental results conducted on the LJ speech dataset demonstrate that compared to Grad-TTS, this model achieves higher MOS (Mean Opinion Score) ratings. Moreover, Gfl-TTS exhibits faster inference speeds in comparison to Tacotron2 and Grad-TTS.

</details>

### [UniCATS: A Unified Context-Aware Text-to-Speech Framework with Contextual VQ-Diffusion and Vocoding](2306.07547.md)
**Chenpeng Du et.al.** · 2024-01-18

### [MLAAD: The Multi-Language Audio Anti-Spoofing Dataset](2401.09512.md)
**Nicolas M. Müller, Piotr Kawa, Wei Herng Choong, Edresson Casanova et al.** · 2024-01-17

<details>
<summary>Abstract</summary>

This paper presents the Multi-Language Audio Anti-Spoofing Dataset (MLAAD), version 10: a dataset of synthetic audio to train and evaluate audio deepfake detection models. It features 175 Text-to-Speech (TTS) models, comprising a total of 1002.9 hours of synthetic voice in 54 different languages. To evaluate this dataset, we train three state-of-the-art deepfake detection models with MLAAD and observe that it demonstrates superior performance to comparable datasets like InTheWild and FakeOrReal when used as a training resource. Moreover, compared to the renowned ASVspoof 2019 dataset, MLAAD proves to be a complementary resource. In tests across eight datasets, MLAAD and ASVspoof 2019 alternately outperformed each other, each excelling on four datasets. By publishing the dataset and making a trained model accessible via an interactive webserver, we aim to democratize anti-spoofing technology, making it accessible beyond the realm of specialists, and contributing to global efforts against audio spoofing and deepfakes.

</details>

### [VoiceFlow: Efficient Text-to-Speech with Rectified Flow Matching](2309.05027.md)
**Yiwei Guo et.al.** · 2024-01-16

### [DurFlex-EVC: Duration-Flexible Emotional Voice Conversion Leveraging Discrete Representations without Text Alignment](2401.08095.md)
**Hyung-Seok Oh, Sang-Hoon Lee, Deok-Hyeon Cho, Seong-Whan Lee** · 2024-01-16

<details>
<summary>Abstract</summary>

Emotional voice conversion (EVC) involves modifying various acoustic characteristics, such as pitch and spectral envelope, to match a desired emotional state while preserving the speaker's identity. Existing EVC methods often rely on text transcriptions or time-alignment information and struggle to handle varying speech durations effectively. In this paper, we propose DurFlex-EVC, a duration-flexible EVC framework that operates without the need for text or alignment information. We introduce a unit aligner that models contextual information by aligning speech with discrete units representing content, eliminating the need for text or speech-text alignment. Additionally, we design a style autoencoder that effectively disentangles content and emotional style, allowing precise manipulation of the emotional characteristics of the speech. We further enhance emotional expressiveness through a hierarchical stylize encoder that applies the target emotional style at multiple hierarchical levels, refining the stylization process to improve the naturalness and expressiveness of the converted speech. Experimental results from subjective and objective evaluations demonstrate that our approach outperforms baseline models, effectively handling duration variability and enhancing emotional expressiveness in the converted speech.

</details>

### [ED-TTS: Multi-Scale Emotion Modeling using Cross-Domain Emotion Diarization for Emotional Speech Synthesis](2401.08166.md)
**Haobin Tang, Xulong Zhang, Ning Cheng, Jing Xiao et al.** · 2024-01-16

<details>
<summary>Abstract</summary>

Existing emotional speech synthesis methods often utilize an utterance-level style embedding extracted from reference audio, neglecting the inherent multi-scale property of speech prosody. We introduce ED-TTS, a multi-scale emotional speech synthesis model that leverages Speech Emotion Diarization (SED) and Speech Emotion Recognition (SER) to model emotions at different levels. Specifically, our proposed approach integrates the utterance-level emotion embedding extracted by SER with fine-grained frame-level emotion embedding obtained from SED. These embeddings are used to condition the reverse process of the denoising diffusion probabilistic model (DDPM). Additionally, we employ cross-domain SED to accurately predict soft labels, addressing the challenge of a scarcity of fine-grained emotion-annotated datasets for supervising emotional TTS training.

</details>

### [Learning Disentangled Speech Representations with Contrastive Learning and Time-Invariant Retrieval](2401.08096.md)
**Yimin Deng, Huaizhen Tang, Xulong Zhang, Ning Cheng et al.** · 2024-01-16

<details>
<summary>Abstract</summary>

Voice conversion refers to transferring speaker identity with well-preserved content. Better disentanglement of speech representations leads to better voice conversion. Recent studies have found that phonetic information from input audio has the potential ability to well represent content. Besides, the speaker-style modeling with pre-trained models making the process more complex. To tackle these issues, we introduce a new method named "CTVC" which utilizes disentangled speech representations with contrastive learning and time-invariant retrieval. Specifically, a similarity-based compression module is used to facilitate a more intimate connection between the frame-level hidden features and linguistic information at phoneme-level. Additionally, a time-invariant retrieval is proposed for timbre extraction based on multiple segmentations and mutual information. Experimental results demonstrate that "CTVC" outperforms previous studies and improves the sound quality and similarity of converted results.

</details>

### [MCMChaos: Improvising Rap Music with MCMC Methods and Chaos Theory](2401.07967.md)
**Robert G. Kimelman** · 2024-01-15

<details>
<summary>Abstract</summary>

A novel freestyle rap software, MCMChaos 0.0.1, based on rap music transcriptions created in previous research is presented. The software has three different versions, each making use of different mathematical simulation methods: collapsed gibbs sampler and lorenz attractor simulation. As far as we know, these simulation methods have never been used in rap music generation before. The software implements Python Text-to-Speech processing (pyttxs) to convert text wrangled from the MCFlow corpus into English speech. In each version, values simulated from each respective mathematical model alter the rate of speech, volume, and (in the multiple voice case) the voice of the text-to-speech engine on a line-by-line basis. The user of the software is presented with a real-time graphical user interface (GUI) which instantaneously changes the initial values read into the mathematical simulation methods. Future research might attempt to allow for more user control and autonomy.

</details>

### [ELLA-V: Stable Neural Codec Language Modeling with Alignment-guided Sequence Reordering](2401.07333.md)
**Yakun Song et.al.** · 2024-01-14

### [Multi speaker text-to-speech synthesis using generalized end-to-end loss function](s2:4f677ea40117dff2df5a52a8ef1d0b3afca9186a.md)
**Owais Nazir, Aruna Malik, Samayveer Singh, Al-Sakib Khan Pathan** · 2024-01-13

### [Multi-Task Learning for Front-End Text Processing in TTS](2401.06321.md)
**Wonjune Kang, Yun Wang, Shun Zhang, Arthur Hinsvark et al.** · 2024-01-12

<details>
<summary>Abstract</summary>

We propose a multi-task learning (MTL) model for jointly performing three tasks that are commonly solved in a text-to-speech (TTS) front-end: text normalization (TN), part-of-speech (POS) tagging, and homograph disambiguation (HD). Our framework utilizes a tree-like structure with a trunk that learns shared representations, followed by separate task-specific heads. We further incorporate a pre-trained language model to utilize its built-in lexical and contextual knowledge, and study how to best use its embeddings so as to most effectively benefit our multi-task model. Through task-wise ablations, we show that our full model trained on all three tasks achieves the strongest overall performance compared to models trained on individual or sub-combinations of tasks, confirming the advantages of our MTL framework. Finally, we introduce a new HD dataset containing a balanced number of sentences in diverse contexts for a variety of homographs and their pronunciations. We demonstrate that incorporating this dataset into training significantly improves HD performance over only using a commonly used, but imbalanced, pre-existing dataset.

</details>

### [Noise-robust zero-shot text-to-speech synthesis conditioned on self-supervised speech-representation model with adapters](2401.05111.md)
**Kenichi Fujita et.al.** · 2024-01-10

### [Transfer the linguistic representations from TTS to accent conversion with non-parallel data](2401.03538.md)
**Xi Chen et.al.** · 2024-01-07

### [Evaluating and Personalizing User-Perceived Quality of Text-to-Speech Voices for Delivering Mindfulness Meditation with Different Physical Embodiments](2401.03581.md)
**Zhonghao Shi, Han Chen, Anna-Maria Velentza, Siqi Liu et al.** · 2024-01-07

<details>
<summary>Abstract</summary>

Mindfulness-based therapies have been shown to be effective in improving mental health, and technology-based methods have the potential to expand the accessibility of these therapies. To enable real-time personalized content generation for mindfulness practice in these methods, high-quality computer-synthesized text-to-speech (TTS) voices are needed to provide verbal guidance and respond to user performance and preferences. However, the user-perceived quality of state-of-the-art TTS voices has not yet been evaluated for administering mindfulness meditation, which requires emotional expressiveness. In addition, work has not yet been done to study the effect of physical embodiment and personalization on the user-perceived quality of TTS voices for mindfulness. To that end, we designed a two-phase human subject study. In Phase 1, an online Mechanical Turk between-subject study (N=471) evaluated 3 (feminine, masculine, child-like) state-of-the-art TTS voices with 2 (feminine, masculine) human therapists' voices in 3 different physical embodiment settings (no agent, conversational agent, socially assistive robot) with remote participants. Building on findings from Phase 1, in Phase 2, an in-person within-subject study (N=94), we used a novel framework we developed for personalizing TTS voices based on user preferences, and evaluated user-perceived quality compared to best-rated non-personalized voices from Phase 1. We found that the best-rated human voice was perceived better than all TTS voices; the emotional expressiveness and naturalness of TTS voices were poorly rated, while users were satisfied with the clarity of TTS voices. Surprisingly, by allowing users to fine-tune TTS voice features, the user-personalized TTS voices could perform almost as well as human voices, suggesting user personalization could be a simple and very effective tool to improve user-perceived quality of TTS voice.

</details>

### [StreamVC: Real-Time Low-Latency Voice Conversion](2401.03078.md)
**Yang Yang, Yury Kartynnik, Yunpeng Li, Jiuqiang Tang et al.** · 2024-01-05

<details>
<summary>Abstract</summary>

We present StreamVC, a streaming voice conversion solution that preserves the content and prosody of any source speech while matching the voice timbre from any target speech. Unlike previous approaches, StreamVC produces the resulting waveform at low latency from the input signal even on a mobile platform, making it applicable to real-time communication scenarios like calls and video conferencing, and addressing use cases such as voice anonymization in these scenarios. Our design leverages the architecture and training strategy of the SoundStream neural audio codec for lightweight high-quality speech synthesis. We demonstrate the feasibility of learning soft speech units causally, as well as the effectiveness of supplying whitened fundamental frequency information to improve pitch stability without leaking the source timbre information.

</details>

### [Pheme: Efficient and Conversational Speech Generation](2401.02839.md)
**Paweł Budzianowski, Taras Sereda, Tomasz Cichy, Ivan Vulić** · 2024-01-05

<details>
<summary>Abstract</summary>

In recent years, speech generation has seen remarkable progress, now achieving one-shot generation capability that is often virtually indistinguishable from real human voice. Integrating such advancements in speech generation with large language models might revolutionize a wide range of applications. However, certain applications, such as assistive conversational systems, require natural and conversational speech generation tools that also operate efficiently in real time. Current state-of-the-art models like VALL-E and SoundStorm, powered by hierarchical neural audio codecs, require large neural components and extensive training data to work well. In contrast, MQTTS aims to build more compact conversational TTS models while capitalizing on smaller-scale real-life conversational speech data. However, its autoregressive nature yields high inference latency and thus limits its real-time usage. In order to mitigate the current limitations of the state-of-the-art TTS models while capitalizing on their strengths, in this work we introduce the Pheme model series that 1) offers compact yet high-performing models, 2) allows for parallel speech generation of 3) natural conversational speech, and 4) it can be trained efficiently on smaller-scale conversational data, cutting data demands by more than 10x but still matching the quality of the autoregressive TTS models. We also show that through simple teacher-student distillation we can meet significant improvements in voice quality for single-speaker setups on top of pretrained Pheme checkpoints, relying solely on synthetic speech generated by much larger teacher models. Audio samples and pretrained models are available online.

</details>

### [Utilizing Neural Transducers for Two-Stage Text-to-Speech via Semantic Token Prediction](2401.01498.md)
**Minchan Kim et.al.** · 2024-01-03

### [Incremental FastPitch: Chunk-based High Quality Text to Speech](2401.01755.md)
**Muyang Du, Chuan Liu, Junjie Lai** · 2024-01-03

<details>
<summary>Abstract</summary>

Parallel text-to-speech models have been widely applied for real-time speech synthesis, and they offer more controllability and a much faster synthesis process compared with conventional auto-regressive models. Although parallel models have benefits in many aspects, they become naturally unfit for incremental synthesis due to their fully parallel architecture such as transformer. In this work, we propose Incremental FastPitch, a novel FastPitch variant capable of incrementally producing high-quality Mel chunks by improving the architecture with chunk-based FFT blocks, training with receptive-field constrained chunk attention masks, and inference with fixed size past model states. Experimental results show that our proposal can produce speech quality comparable to the parallel FastPitch, with a significant lower latency that allows even lower response time for real-time speech applications.

</details>

### [CoMoSVC: Consistency Model-based Singing Voice Conversion](2401.01792.md)
**Yiwen Lu, Zhen Ye, Wei Xue, Xu Tan et al.** · 2024-01-03

<details>
<summary>Abstract</summary>

The diffusion-based Singing Voice Conversion (SVC) methods have achieved remarkable performances, producing natural audios with high similarity to the target timbre. However, the iterative sampling process results in slow inference speed, and acceleration thus becomes crucial. In this paper, we propose CoMoSVC, a consistency model-based SVC method, which aims to achieve both high-quality generation and high-speed sampling. A diffusion-based teacher model is first specially designed for SVC, and a student model is further distilled under self-consistency properties to achieve one-step sampling. Experiments on a single NVIDIA GTX4090 GPU reveal that although CoMoSVC has a significantly faster inference speed than the state-of-the-art (SOTA) diffusion-based SVC system, it still achieves comparable or superior conversion performance based on both subjective and objective metrics. Audio samples and codes are available at https://comosvc.github.io/.

</details>

### [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Survey](s2:b4543793922b920eae76fb38d2631dc7c0df7aa8.md)
**Tianxin Xie, Yan Rong, Pengfei Zhang, Li Liu** · 2024-01-01

### [HiFi-GANw: Watermarked Speech Synthesis via Fine-Tuning of HiFi-GAN](s2:2617ac79d945418bcd896c984b9aa9ea8454daf1.md)
**Xiangyu Cheng, Yaofei Wang, Chang Liu, Donghui Hu et al.** · 2024-01-01

<details>
<summary>Abstract</summary>

Advancements in speech synthesis technology bring generated speech closer to natural human voices, but they also introduce a series of potential risks, such as the dissemination of false information and voice impersonation. Therefore, it becomes significant to detect any potential misuse of the released speech content. This letter introduces an active strategy that combines audio watermarking with the HiFi-GAN vocoder to embed an invisible watermark in all synthesized speech for detection purposes. We first pre-train a watermark extraction network as the watermark extractor, and then use the watermark extraction loss and speech quality loss of the extractor to adjust the HiFi-GAN generator to ensure that the watermark can be extracted from the synthesized speech. We evaluate the imperceptibility and robustness of the watermark across various speech synthesis models. The experimental results demonstrate that our method effectively withstands various attacks and exhibits excellent imperceptibility. Moreover, our method is universal and compatible with various vocoder-based speech synthesis models.

</details>

### [Autoregressive Speech Synthesis with Next-Distribution Prediction](s2:e4d2d3965230f01d241f2dc9ad68140b6fe8bbdf.md)
**Xinfa Zhu, Wenjie Tian, Lei Xie** · 2024-01-01

### [EfficientTTS 2: Variational End-to-End Text-to-Speech Synthesis and Voice Conversion](s2:94e06b7dd1f19360d812a69d8acc96d2d6c0cc7b.md)
**Chenfeng Miao, Qingying Zhu, Minchuan Chen, Jun Ma et al.** · 2024-01-01

<details>
<summary>Abstract</summary>

Recently, the field of Text-to-Speech (TTS) has been dominated by one-stage text-to-waveform models which have significantly improved speech quality compared to two-stage models. In this work, we propose EfficientTTS 2 (EFTS2), a one-stage high-quality end-to-end TTS framework that is fully differentiable and highly efficient. Our method adopts an adversarial training process, with a differentiable aligner and a hierarchical-VAE-based waveform generator. These design choices free the model from the use of external aligners, invertible structures, and complex training procedures as most previous TTS works have. Moreover, we extend EFTS2 to the voice conversion (VC) task and propose EFTS2-VC, an end-to-end VC model that allows high-quality speech-to-speech conversion. Experimental results suggest that the two proposed models achieve better or at least comparable speech quality compared to baseline models, while also providing faster inference speeds and smaller model sizes.

</details>

### [Active Defense Against Voice Conversion Through Generative Adversarial Network](s2:70fe8113c3526bd6d416bd5aa0a48101c9278fa3.md)
**Shihang Dong, Beijing Chen, Kaijie Ma, Guoying Zhao** · 2024-01-01

<details>
<summary>Abstract</summary>

Active defense is an important approach to counter speech deepfakes that threaten individuals’ privacy, property, and reputation. However, the existing works in this field suffer from issues such as time-consuming and ordinary defense effectiveness. This letter proposes a Generative Adversarial Network (GAN) framework for adversarial attacks as a defense against malicious voice conversion. The proposed method uses a generator to produce adversarial perturbations and adds them to the mel-spectrogram of the target audio to craft adversarial example. In addition, in order to enhance the defense effectiveness, a spectrogram waveform conversion simulation module (SWCSM) is designed to simulate the process of reconstructing waveform from the adversarial mel-spectrogram example and re-extracting mel-spectrogram from the reconstructed waveform. Experiments on four state-of-the-art voice conversion models show that our method achieves the overall best performance among five compared methods in both white-box and black-box scenarios in terms of defense effectiveness and generation time.

</details>

### [Generative Adversarial Network based Neural Vocoder for Myanmar End-to-End Speech Synthesis](s2:1fdc08f215e383b77ce6b0b5cf4610c53fdf816f.md)
**Aye Mya Hlaing, Win Pa Pa** · 2024-01-01

### [End-to-End Speech Synthesis for the Serbian Language Based on Tacotron](s2:97107c399f90b0b1728dc83b3234edec48e84294.md)
**Tijana V. Nosek, S. Suzić, M. Sečujski, Vuk Stanojev et al.** · 2024-01-01

### [End-to-end conversational speech synthesis with controllable emotions in the dimensions of pleasantness and arousal](s2:972c09400b3df4fce8fd35d0c8199b850c2c0bc1.md)
**Hiroki Mori, Hironao Nishino** · 2024-01-01

