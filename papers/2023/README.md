# 2023

409 papers in this year.

### [Boosting Large Language Model for Speech Synthesis: An Empirical Study](2401.00246.md)
**Hongkun Hao et.al.** · 2023-12-30

### [Attention-based Interactive Disentangling Network for Instance-level Emotional Voice Conversion](2312.17508.md)
**Yun Chen, Lingxiao Yang, Qi Chen, Jian-Huang Lai et al.** · 2023-12-29

<details>
<summary>Abstract</summary>

Emotional Voice Conversion aims to manipulate a speech according to a given emotion while preserving non-emotion components. Existing approaches cannot well express fine-grained emotional attributes. In this paper, we propose an Attention-based Interactive diseNtangling Network (AINN) that leverages instance-wise emotional knowledge for voice conversion. We introduce a two-stage pipeline to effectively train our network: Stage I utilizes inter-speech contrastive learning to model fine-grained emotion and intra-speech disentanglement learning to better separate emotion and content. In Stage II, we propose to regularize the conversion with a multi-view consistency mechanism. This technique helps us transfer fine-grained emotion and maintain speech content. Extensive experiments show that our AINN outperforms state-of-the-arts in both objective and subjective metrics.

</details>

### [Revolutionizing Personalized Voice Synthesis: The Journey towards Emotional and Individual Authenticity with DIVSE (Dynamic Individual Voice Synthesis Engine)](2312.17281.md)
**Fan Shi** · 2023-12-28

<details>
<summary>Abstract</summary>

This comprehensive paper delves into the forefront of personalized voice synthesis within artificial intelligence (AI), spotlighting the Dynamic Individual Voice Synthesis Engine (DIVSE). DIVSE represents a groundbreaking leap in text-to-voice (TTS) technology, uniquely focusing on adapting and personalizing voice outputs to match individual vocal characteristics. The research underlines the gap in current AI-generated voices, which, while technically advanced, fall short in replicating the unique individuality and expressiveness intrinsic to human speech. It outlines the challenges and advancements in personalized voice synthesis, emphasizing the importance of emotional expressiveness, accent and dialect variability, and capturing individual voice traits. The architecture of DIVSE is meticulously detailed, showcasing its three core components: Voice Characteristic Learning Module (VCLM), Emotional Tone and Accent Adaptation Module (ETAAM), and Dynamic Speech Synthesis Engine (DSSE). The innovative approach of DIVSE lies in its adaptive learning capability, which evolves over time to tailor voice outputs to specific user traits. The paper presents a rigorous experimental setup, utilizing accepted datasets and personalization metrics like Mean Opinion Score (MOS) and Emotional Alignment Score, to validate DIVSE's superiority over mainstream models. The results depict a clear advancement in achieving higher personalization and emotional resonance in AI-generated voices.

</details>

### [AE-Flow: AutoEncoder Normalizing Flow](2312.16552.md)
**Jakub Mosiński, Piotr Biliński, Thomas Merritt, Abdelhamid Ezzerg et al.** · 2023-12-27

<details>
<summary>Abstract</summary>

Recently normalizing flows have been gaining traction in text-to-speech (TTS) and voice conversion (VC) due to their state-of-the-art (SOTA) performance. Normalizing flows are unsupervised generative models. In this paper, we introduce supervision to the training process of normalizing flows, without the need for parallel data. We call this training paradigm AutoEncoder Normalizing Flow (AE-Flow). It adds a reconstruction loss forcing the model to use information from the conditioning to reconstruct an audio sample. Our goal is to understand the impact of each component and find the right combination of the negative log-likelihood (NLL) and the reconstruction loss in training normalizing flows with coupling blocks. For that reason we will compare flow-based mapping model trained with: (i) NLL loss, (ii) NLL and reconstruction losses, as well as (iii) reconstruction loss only. Additionally, we compare our model with SOTA VC baseline. The models are evaluated in terms of naturalness, speaker similarity, intelligibility in many-to-many and many-to-any VC settings. The results show that the proposed training paradigm systematically improves speaker similarity and naturalness when compared to regular training methods of normalizing flows. Furthermore, we show that our method improves speaker similarity and intelligibility over the state-of-the-art.

</details>

### [Audiobox: Unified Audio Generation with Natural Language Prompts](2312.15821.md)
**Apoorv Vyas, Bowen Shi, Matthew Le, Andros Tjandra et al.** · 2023-12-25

<details>
<summary>Abstract</summary>

Audio is an essential part of our life, but creating it often requires expertise and is time-consuming. Research communities have made great progress over the past year advancing the performance of large scale audio generative models for a single modality (speech, sound, or music) through adopting more powerful generative models and scaling data. However, these models lack controllability in several aspects: speech generation models cannot synthesize novel styles based on text description and are limited on domain coverage such as outdoor environments; sound generation models only provide coarse-grained control based on descriptions like "a person speaking" and would only generate mumbling human voices. This paper presents Audiobox, a unified model based on flow-matching that is capable of generating various audio modalities. We design description-based and example-based prompting to enhance controllability and unify speech and sound generation paradigms. We allow transcript, vocal, and other audio styles to be controlled independently when generating speech. To improve model generalization with limited labels, we adapt a self-supervised infilling objective to pre-train on large quantities of unlabeled audio. Audiobox sets new benchmarks on speech and sound generation (0.745 similarity on Librispeech for zero-shot TTS; 0.77 FAD on AudioCaps for text-to-sound) and unlocks new methods for generating audio with novel vocal and acoustic styles. We further integrate Bespoke Solvers, which speeds up generation by over 25 times compared to the default ODE solver for flow-matching, without loss of performance on several tasks. Our demo is available at https://audiobox.metademolab.com/

</details>

### [ZMM-TTS: Zero-shot Multilingual and Multispeaker Speech Synthesis Conditioned on Self-supervised Discrete Speech Representations](2312.14398.md)
**Cheng Gong et.al.** · 2023-12-22

### [Creating New Voices using Normalizing Flows](2312.14569.md)
**Piotr Bilinski, Thomas Merritt, Abdelhamid Ezzerg, Kamil Pokora et al.** · 2023-12-22

<details>
<summary>Abstract</summary>

Creating realistic and natural-sounding synthetic speech remains a big challenge for voice identities unseen during training. As there is growing interest in synthesizing voices of new speakers, here we investigate the ability of normalizing flows in text-to-speech (TTS) and voice conversion (VC) modes to extrapolate from speakers observed during training to create unseen speaker identities. Firstly, we create an approach for TTS and VC, and then we comprehensively evaluate our methods and baselines in terms of intelligibility, naturalness, speaker similarity, and ability to create new voices. We use both objective and subjective metrics to benchmark our techniques on 2 evaluation tasks: zero-shot and new voice speech synthesis. The goal of the former task is to measure the precision of the conversion to an unseen voice. The goal of the latter is to measure the ability to create new voices. Extensive evaluations demonstrate that the proposed approach systematically allows to obtain state-of-the-art performance in zero-shot speech synthesis and creates various new voices, unobserved in the training set. We consider this work to be the first attempt to synthesize new voices based on mel-spectrograms and normalizing flows, along with a comprehensive analysis and comparison of the TTS and VC modes.

</details>

### [BrainTalker: Low-Resource Brain-to-Speech Synthesis with Transfer Learning using Wav2Vec 2.0](2312.13600.md)
**Miseul Kim, Zhenyu Piao, Jihyun Lee, Hong-Goo Kang** · 2023-12-21

<details>
<summary>Abstract</summary>

Decoding spoken speech from neural activity in the brain is a fast-emerging research topic, as it could enable communication for people who have difficulties with producing audible speech. For this task, electrocorticography (ECoG) is a common method for recording brain activity with high temporal resolution and high spatial precision. However, due to the risky surgical procedure required for obtaining ECoG recordings, relatively little of this data has been collected, and the amount is insufficient to train a neural network-based Brain-to-Speech (BTS) system. To address this problem, we propose BrainTalker-a novel BTS framework that generates intelligible spoken speech from ECoG signals under extremely low-resource scenarios. We apply a transfer learning approach utilizing a pre-trained self supervised model, Wav2Vec 2.0. Specifically, we train an encoder module to map ECoG signals to latent embeddings that match Wav2Vec 2.0 representations of the corresponding spoken speech. These embeddings are then transformed into mel-spectrograms using stacked convolutional and transformer-based layers, which are fed into a neural vocoder to synthesize speech waveform. Experimental results demonstrate our proposed framework achieves outstanding performance in terms of subjective and objective metrics, including a Pearson correlation coefficient of 0.9 between generated and ground truth mel spectrograms. We share publicly available Demos and Code.

</details>

### [External Knowledge Augmented Polyphone Disambiguation Using Large Language Model](2312.11920.md)
**Chen Li** · 2023-12-19

<details>
<summary>Abstract</summary>

One of the key issues in Mandarin Chinese text-to-speech (TTS) systems is polyphone disambiguation when doing grapheme-to-phoneme (G2P) conversion. In this paper, we introduce a novel method to solve the problem as a generation task. Following the trending research of large language models (LLM) and prompt learning, the proposed method consists of three modules. Retrieval module incorporates external knowledge which is a multi-level semantic dictionary of Chinese polyphonic characters to format the sentence into a prompt. Generation module adopts the decoder-only Transformer architecture to induce the target text. Postprocess module corrects the generated text into a valid result if needed. Experimental results show that our method outperforms the existing methods on a public dataset called CPP. We also empirically study the impacts of different templates of the prompt, different sizes of training data, and whether to incorporate external knowledge.

</details>

### [Evaluating Speech-in-Speech Perception via a Humanoid Robot](2312.12262.md)
**Luke Meyer, Gloria Araiza-Illan, Laura Rachman, Etienne Gaudrain et al.** · 2023-12-19

<details>
<summary>Abstract</summary>

Underlying mechanisms of speech perception masked by background speakers, a common daily listening condition, are often investigated using various and lengthy psychophysical tests. The presence of a social agent, such as an interactive humanoid NAO robot, may help maintain engagement and attention. However, such robots potentially have limited sound quality or processing speed. As a first step towards the use of NAO in psychophysical testing of speech-in-speech perception, we compared normal-hearing young adults' performance when using the standard computer interface to that when using a NAO robot to introduce the test and present all corresponding stimuli. Target sentences were presented with colour and number keywords in the presence of competing masker speech at varying target-to-masker ratios. Sentences were produced by the same speaker, but voice differences between the target and masker were introduced using speech synthesis methods. To assess test performance, speech intelligibility and data collection duration were compared between the computer and NAO setups. Human-robot interaction was assessed using the Negative Attitude Towards Robot Scale (NARS) and quantification of behavioural cues (backchannels). Speech intelligibility results showed functional similarity between the computer and NAO setups. Data collection durations were longer when using NAO. NARS results showed participants had a more positive attitude toward robots prior to their interaction with NAO. The presence of more positive backchannels when using NAO suggest higher engagement with the robot in comparison to the computer. Overall, the study presents the potential of the NAO for presentingspeech materials and collecting psychophysical measurements for speech-in-speech perception.

</details>

### [StyleSpeech: Self-supervised Style Enhancing with VQ-VAE-based Pre-training for Expressive Audiobook Speech Synthesis](2312.12181.md)
**Xueyuan Chen, Xi Wang, Shaofei Zhang, Lei He et al.** · 2023-12-19

<details>
<summary>Abstract</summary>

The expressive quality of synthesized speech for audiobooks is limited by generalized model architecture and unbalanced style distribution in the training data. To address these issues, in this paper, we propose a self-supervised style enhancing method with VQ-VAE-based pre-training for expressive audiobook speech synthesis. Firstly, a text style encoder is pre-trained with a large amount of unlabeled text-only data. Secondly, a spectrogram style extractor based on VQ-VAE is pre-trained in a self-supervised manner, with plenty of audio data that covers complex style variations. Then a novel architecture with two encoder-decoder paths is specially designed to model the pronunciation and high-level style expressiveness respectively, with the guidance of the style extractor. Both objective and subjective evaluations demonstrate that our proposed method can effectively improve the naturalness and expressiveness of the synthesized speech in audiobook synthesis especially for the role and out-of-domain scenarios.

</details>

### [Emotion Rendering for Conversational Speech Synthesis with Heterogeneous Graph-Based Context Modeling](2312.11947.md)
**Rui Liu, Yifan Hu, Yi Ren, Xiang Yin et al.** · 2023-12-19

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis (CSS) aims to accurately express an utterance with the appropriate prosody and emotional inflection within a conversational setting. While recognising the significance of CSS task, the prior studies have not thoroughly investigated the emotional expressiveness problems due to the scarcity of emotional conversational datasets and the difficulty of stateful emotion modeling. In this paper, we propose a novel emotional CSS model, termed ECSS, that includes two main components: 1) to enhance emotion understanding, we introduce a heterogeneous graph-based emotional context modeling mechanism, which takes the multi-source dialogue history as input to model the dialogue context and learn the emotion cues from the context; 2) to achieve emotion rendering, we employ a contrastive learning-based emotion renderer module to infer the accurate emotion style for the target utterance. To address the issue of data scarcity, we meticulously create emotional labels in terms of category and intensity, and annotate additional emotional information on the existing conversational dataset (DailyTalk). Both objective and subjective evaluations suggest that our model outperforms the baseline models in understanding and rendering emotions. These evaluations also underscore the importance of comprehensive emotional annotations. Code and audio samples can be found at: https://github.com/walker-hyf/ECSS.

</details>

### [High-Fidelity Speech Synthesis with Minimal Supervision: All Using Diffusion Models](2309.15512.md)
**Chunyu Qiang et.al.** · 2023-12-18

### [Minimally-Supervised Speech Synthesis with Conditional Diffusion Model and Language Model: A Comparative Study of Semantic Coding](2307.15484.md)
**Chunyu Qiang et.al.** · 2023-12-18

### [Assisting Blind People Using Object Detection with Vocal Feedback](2401.01362.md)
**Heba Najm, Khirallah Elferjani, Alhaam Alariyibi** · 2023-12-18

<details>
<summary>Abstract</summary>

For visually impaired people, it is highly difficult to make independent movement and safely move in both indoors and outdoors environment. Furthermore, these physically and visually challenges prevent them from in day-today live activities. Similarly, they have problem perceiving objects of surrounding environment that may pose a risk to them. The proposed approach suggests detection of objects in real-time video by using a web camera, for the object identification, process. You Look Only Once (YOLO) model is utilized which is CNN-based real-time object detection technique. Additionally, The OpenCV libraries of Python is used to implement the software program as well as deep learning process is performed. Image recognition results are transferred to the visually impaired users in audible form by means of Google text-to-speech library and determine object location relative to its position in the screen. The obtaining result was evaluated by using the mean Average Precision (mAP), and it was found that the proposed approach achieves excellent results when it compared to previous approaches.

</details>

### [ParrotTTS: Text-to-Speech synthesis by exploiting self-supervised representations](2303.01261.md)
**Neil Shah et.al.** · 2023-12-17

### [A review-based study on different Text-to-Speech technologies](2312.11563.md)
**Md. Jalal Uddin Chowdhury, Ashab Hussan** · 2023-12-17

<details>
<summary>Abstract</summary>

This research paper presents a comprehensive review-based study on various Text-to-Speech (TTS) technologies. TTS technology is an important aspect of human-computer interaction, enabling machines to convert written text into audible speech. The paper examines the different TTS technologies available, including concatenative TTS, formant synthesis TTS, and statistical parametric TTS. The study focuses on comparing the advantages and limitations of these technologies in terms of their naturalness of voice, the level of complexity of the system, and their suitability for different applications. In addition, the paper explores the latest advancements in TTS technology, including neural TTS and hybrid TTS. The findings of this research will provide valuable insights for researchers, developers, and users who want to understand the different TTS technologies and their suitability for specific applications.

</details>

### [MM-TTS: Multi-modal Prompt based Style Transfer for Expressive Text-to-Speech Synthesis](2312.10687.md)
**Wenhao Guan, Yishuang Li, Tao Li, Hukai Huang et al.** · 2023-12-17

<details>
<summary>Abstract</summary>

The style transfer task in Text-to-Speech refers to the process of transferring style information into text content to generate corresponding speech with a specific style. However, most existing style transfer approaches are either based on fixed emotional labels or reference speech clips, which cannot achieve flexible style transfer. Recently, some methods have adopted text descriptions to guide style transfer. In this paper, we propose a more flexible multi-modal and style controllable TTS framework named MM-TTS. It can utilize any modality as the prompt in unified multi-modal prompt space, including reference speech, emotional facial images, and text descriptions, to control the style of the generated speech in a system. The challenges of modeling such a multi-modal style controllable TTS mainly lie in two aspects:1)aligning the multi-modal information into a unified style space to enable the input of arbitrary modality as the style prompt in a single system, and 2)efficiently transferring the unified style representation into the given text content, thereby empowering the ability to generate prompt style-related voice. To address these problems, we propose an aligned multi-modal prompt encoder that embeds different modalities into a unified style space, supporting style transfer for different modalities. Additionally, we present a new adaptive style transfer method named Style Adaptive Convolutions to achieve a better style representation. Furthermore, we design a Rectified Flow based Refiner to solve the problem of over-smoothing Mel-spectrogram and generate audio of higher fidelity. Since there is no public dataset for multi-modal TTS, we construct a dataset named MEAD-TTS, which is related to the field of expressive talking head. Our experiments on the MEAD-TTS dataset and out-of-domain datasets demonstrate that MM-TTS can achieve satisfactory results based on multi-modal prompts.

</details>

### [AutoVisual Fusion Suite: A Comprehensive Evaluation of Image Segmentation and Voice Conversion Tools on HuggingFace Platform](2401.05379.md)
**Amirreza Hashemi** · 2023-12-17

<details>
<summary>Abstract</summary>

This study presents a comprehensive evaluation of tools available on the HuggingFace platform for two pivotal applications in artificial intelligence: image segmentation and voice conversion. The primary objective was to identify the top three tools within each category and subsequently install and configure these tools on Linux systems. We leveraged the power of pre-trained segmentation models such as SAM and DETR Model with ResNet-50 backbone for image segmentation, and the so-vits-svc-fork model for voice conversion. This paper delves into the methodologies and challenges encountered during the implementation process, and showcases the successful combination of video segmentation and voice conversion in a unified project named AutoVisual Fusion Suite.

</details>

### [SECap: Speech Emotion Captioning with Large Language Model](2312.10381.md)
**Yaoxun Xu, Hangting Chen, Jianwei Yu, Qiaochu Huang et al.** · 2023-12-16

<details>
<summary>Abstract</summary>

Speech emotions are crucial in human communication and are extensively used in fields like speech synthesis and natural language understanding. Most prior studies, such as speech emotion recognition, have categorized speech emotions into a fixed set of classes. Yet, emotions expressed in human speech are often complex, and categorizing them into predefined groups can be insufficient to adequately represent speech emotions. On the contrary, describing speech emotions directly by means of natural language may be a more effective approach. Regrettably, there are not many studies available that have focused on this direction. Therefore, this paper proposes a speech emotion captioning framework named SECap, aiming at effectively describing speech emotions using natural language. Owing to the impressive capabilities of large language models in language comprehension and text generation, SECap employs LLaMA as the text decoder to allow the production of coherent speech emotion captions. In addition, SECap leverages HuBERT as the audio encoder to extract general speech features and Q-Former as the Bridge-Net to provide LLaMA with emotion-related speech features. To accomplish this, Q-Former utilizes mutual information learning to disentangle emotion-related speech features and speech contents, while implementing contrastive learning to extract more emotion-related speech features. The results of objective and subjective evaluations demonstrate that: 1) the SECap framework outperforms the HTSAT-BART baseline in all objective evaluations; 2) SECap can generate high-quality speech emotion captions that attain performance on par with human annotators in subjective mean opinion score tests.

</details>

### [CONCSS: Contrastive-based Context Comprehension for Dialogue-appropriate Prosody in Conversational Speech Synthesis](2312.10358.md)
**Yayue Deng, Jinlong Xue, Yukang Jia, Qifei Li et al.** · 2023-12-16

<details>
<summary>Abstract</summary>

Conversational speech synthesis (CSS) incorporates historical dialogue as supplementary information with the aim of generating speech that has dialogue-appropriate prosody. While previous methods have already delved into enhancing context comprehension, context representation still lacks effective representation capabilities and context-sensitive discriminability. In this paper, we introduce a contrastive learning-based CSS framework, CONCSS. Within this framework, we define an innovative pretext task specific to CSS that enables the model to perform self-supervised learning on unlabeled conversational datasets to boost the model's context understanding. Additionally, we introduce a sampling strategy for negative sample augmentation to enhance context vectors' discriminability. This is the first attempt to integrate contrastive learning into CSS. We conduct ablation studies on different contrastive learning strategies and comprehensive experiments in comparison with prior CSS systems. Results demonstrate that the synthesized speech from our proposed method exhibits more contextually appropriate and sensitive prosody.

</details>

### [Amphion: An Open-Source Audio, Music and Speech Generation Toolkit](2312.09911.md)
**Xueyao Zhang, Liumeng Xue, Yicheng Gu, Yuancheng Wang et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

Amphion is an open-source toolkit for Audio, Music, and Speech Generation, targeting to ease the way for junior researchers and engineers into these fields. It presents a unified framework that includes diverse generation tasks and models, with the added bonus of being easily extendable for new incorporation. The toolkit is designed with beginner-friendly workflows and pre-trained models, allowing both beginners and seasoned researchers to kick-start their projects with relative ease. The initial release of Amphion v0.1 supports a range of tasks including Text to Speech (TTS), Text to Audio (TTA), and Singing Voice Conversion (SVC), supplemented by essential components like data preprocessing, state-of-the-art vocoders, and evaluation metrics. This paper presents a high-level overview of Amphion. Amphion is open-sourced at https://github.com/open-mmlab/Amphion.

</details>

### [What to Remember: Self-Adaptive Continual Learning for Audio Deepfake Detection](2312.09651.md)
**Xiaohui Zhang, Jiangyan Yi, Chenglong Wang, Chuyuan Zhang et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

The rapid evolution of speech synthesis and voice conversion has raised substantial concerns due to the potential misuse of such technology, prompting a pressing need for effective audio deepfake detection mechanisms. Existing detection models have shown remarkable success in discriminating known deepfake audio, but struggle when encountering new attack types. To address this challenge, one of the emergent effective approaches is continual learning. In this paper, we propose a continual learning approach called Radian Weight Modification (RWM) for audio deepfake detection. The fundamental concept underlying RWM involves categorizing all classes into two groups: those with compact feature distributions across tasks, such as genuine audio, and those with more spread-out distributions, like various types of fake audio. These distinctions are quantified by means of the in-class cosine distance, which subsequently serves as the basis for RWM to introduce a trainable gradient modification direction for distinct data types. Experimental evaluations against mainstream continual learning methods reveal the superiority of RWM in terms of knowledge acquisition and mitigating forgetting in audio deepfake detection. Furthermore, RWM's applicability extends beyond audio deepfake detection, demonstrating its potential significance in diverse machine learning domains such as image recognition.

</details>

### [SELM: Speech Enhancement Using Discrete Tokens and Language Models](2312.09747.md)
**Ziqian Wang, Xinfa Zhu, Zihan Zhang, YuanJun Lv et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

Language models (LMs) have shown superior performances in various speech generation tasks recently, demonstrating their powerful ability for semantic context modeling. Given the intrinsic similarity between speech generation and speech enhancement, harnessing semantic information holds potential advantages for speech enhancement tasks. In light of this, we propose SELM, a novel paradigm for speech enhancement, which integrates discrete tokens and leverages language models. SELM comprises three stages: encoding, modeling, and decoding. We transform continuous waveform signals into discrete tokens using pre-trained self-supervised learning (SSL) models and a k-means tokenizer. Language models then capture comprehensive contextual information within these tokens. Finally, a detokenizer and HiFi-GAN restore them into enhanced speech. Experimental results demonstrate that SELM achieves comparable performance in objective metrics alongside superior results in subjective perception. Our demos are available https://honee-w.github.io/SELM/.

</details>

### [SEF-VC: Speaker Embedding Free Zero-Shot Voice Conversion with Cross Attention](2312.08676.md)
**Junjie Li, Yiwei Guo, Xie Chen, Kai Yu** · 2023-12-14

<details>
<summary>Abstract</summary>

Zero-shot voice conversion (VC) aims to transfer the source speaker timbre to arbitrary unseen target speaker timbre, while keeping the linguistic content unchanged. Although the voice of generated speech can be controlled by providing the speaker embedding of the target speaker, the speaker similarity still lags behind the ground truth recordings. In this paper, we propose SEF-VC, a speaker embedding free voice conversion model, which is designed to learn and incorporate speaker timbre from reference speech via a powerful position-agnostic cross-attention mechanism, and then reconstruct waveform from HuBERT semantic tokens in a non-autoregressive manner. The concise design of SEF-VC enhances its training stability and voice conversion performance. Objective and subjective evaluations demonstrate the superiority of SEF-VC to generate high-quality speech with better similarity to target reference than strong zero-shot VC baselines, even for very short reference speeches.

</details>

### [PerMod: Perceptually Grounded Voice Modification with Latent Diffusion Models](2312.08494.md)
**Robin Netzorg, Ajil Jalal, Luna McNulty, Gopala Krishna Anumanchipalli** · 2023-12-13

<details>
<summary>Abstract</summary>

Perceptual modification of voice is an elusive goal. While non-experts can modify an image or sentence perceptually with available tools, it is not clear how to similarly modify speech along perceptual axes. Voice conversion does make it possible to convert one voice to another, but these modifications are handled by black box models, and the specifics of what perceptual qualities to modify and how to modify them are unclear. Towards allowing greater perceptual control over voice, we introduce PerMod, a conditional latent diffusion model that takes in an input voice and a perceptual qualities vector, and produces a voice with the matching perceptual qualities. Unlike prior work, PerMod generates a new voice corresponding to specific perceptual modifications. Evaluating perceptual quality vectors with RMSE from both human and predicted labels, we demonstrate that PerMod produces voices with the desired perceptual qualities for typical voices, but performs poorly on atypical voices.

</details>

### [Neural Text to Articulate Talk: Deep Text to Audiovisual Speech Synthesis achieving both Auditory and Photo-realism](2312.06613.md)
**Georgios Milis et.al.** · 2023-12-11

### [Neural Speech Embeddings for Speech Synthesis Based on Deep Generative Networks](2312.05814.md)
**Seo-Hyun Lee, Young-Eun Lee, Soowon Kim, Byung-Kwan Ko et al.** · 2023-12-10

<details>
<summary>Abstract</summary>

Brain-to-speech technology represents a fusion of interdisciplinary applications encompassing fields of artificial intelligence, brain-computer interfaces, and speech synthesis. Neural representation learning based intention decoding and speech synthesis directly connects the neural activity to the means of human linguistic communication, which may greatly enhance the naturalness of communication. With the current discoveries on representation learning and the development of the speech synthesis technologies, direct translation of brain signals into speech has shown great promise. Especially, the processed input features and neural speech embeddings which are given to the neural network play a significant role in the overall performance when using deep generative models for speech generation from brain signals. In this paper, we introduce the current brain-to-speech technology with the possibility of speech synthesis from brain signals, which may ultimately facilitate innovation in non-verbal communication. Also, we perform comprehensive analysis on the neural features and neural speech embeddings underlying the neurophysiological activation while performing speech, which may play a significant role in the speech synthesis works.

</details>

### [An Experimental Study: Assessing the Combined Framework of WavLM and BEST-RQ for Text-to-Speech Synthesis](2312.05415.md)
**Via Nielson, Steven Hillis** · 2023-12-08

<details>
<summary>Abstract</summary>

We propose a new model architecture specifically suited for text-to-speech (TTS) models. We combine WavLM, a pre-trained self-supervised learning (SSL) speech model, and the BEST-RQ vector quantization framework. We assess the extent to which the more task-agnostic WavLM, coupled with the superior suitability of the simplistic BEST-RQ framework for a wider array of downstream tasks, yields favorable outcomes. Experiments on the LibriSpeech dataset with SUPERB benchmarking assert that the proposed model significantly underperforms. We speculate the underlying reason for this performance is related to the difference between featurizing raw audio waveforms and spectrograms with a quantizer. We discuss the limitations of this approach to better guide future advancements in TTS.

</details>

### [Neural Concatenative Singing Voice Conversion: Rethinking Concatenation-Based Approach for One-Shot Singing Voice Conversion](2312.04919.md)
**Binzhu Sha, Xu Li, Zhiyong Wu, Ying Shan et al.** · 2023-12-08

<details>
<summary>Abstract</summary>

Any-to-any singing voice conversion (SVC) is confronted with the challenge of ``timbre leakage'' issue caused by inadequate disentanglement between the content and the speaker timbre. To address this issue, this study introduces NeuCoSVC, a novel neural concatenative SVC framework. It consists of a self-supervised learning (SSL) representation extractor, a neural harmonic signal generator, and a waveform synthesizer. The SSL extractor condenses audio into fixed-dimensional SSL features, while the harmonic signal generator leverages linear time-varying filters to produce both raw and filtered harmonic signals for pitch information. The synthesizer reconstructs waveforms using SSL features, harmonic signals, and loudness information. During inference, voice conversion is performed by substituting source SSL features with their nearest counterparts from a matching pool which comprises SSL features extracted from the reference audio, while preserving raw harmonic signals and loudness from the source audio. By directly utilizing SSL features from the reference audio, the proposed framework effectively resolves the ``timbre leakage" issue caused by previous disentanglement-based approaches. Experimental results demonstrate that the proposed NeuCoSVC system outperforms the disentanglement-based speaker embedding approach in one-shot SVC across intra-language, cross-language, and cross-domain evaluations.

</details>

### [Schrodinger Bridges Beat Diffusion Models on Text-to-Speech Synthesis](2312.03491.md)
**Zehua Chen et.al.** · 2023-12-06

### [Detecting Voice Cloning Attacks via Timbre Watermarking](2312.03410.md)
**Chang Liu, Jie Zhang, Tianwei Zhang, Xi Yang et al.** · 2023-12-06

<details>
<summary>Abstract</summary>

Nowadays, it is common to release audio content to the public. However, with the rise of voice cloning technology, attackers have the potential to easily impersonate a specific person by utilizing his publicly released audio without any permission. Therefore, it becomes significant to detect any potential misuse of the released audio content and protect its timbre from being impersonated. To this end, we introduce a novel concept, "Timbre Watermarking", which embeds watermark information into the target individual's speech, eventually defeating the voice cloning attacks. To ensure the watermark is robust to the voice cloning model's learning process, we design an end-to-end voice cloning-resistant detection framework. The core idea of our solution is to embed and extract the watermark in the frequency domain in a temporally invariant manner. To acquire generalization across different voice cloning attacks, we modulate their shared process and integrate it into our framework as a distortion layer. Experiments demonstrate that the proposed timbre watermarking can defend against different voice cloning attacks, exhibit strong resistance against various adaptive attacks (e.g., reconstruction-based removal attacks, watermark overwriting attacks), and achieve practicality in real-world services such as PaddleSpeech, Voice-Cloning-App, and so-vits-svc. In addition, ablation studies are also conducted to verify the effectiveness of our design. Some audio samples are available at https://timbrewatermarking.github.io/samples.

</details>

### [OpenVoice: Versatile Instant Voice Cloning](2312.01479.md)
**Zengyi Qin, Wenliang Zhao, Xumin Yu, Xin Sun** · 2023-12-03

<details>
<summary>Abstract</summary>

We introduce OpenVoice, a versatile voice cloning approach that requires only a short audio clip from the reference speaker to replicate their voice and generate speech in multiple languages. OpenVoice represents a significant advancement in addressing the following open challenges in the field: 1) Flexible Voice Style Control. OpenVoice enables granular control over voice styles, including emotion, accent, rhythm, pauses, and intonation, in addition to replicating the tone color of the reference speaker. The voice styles are not directly copied from and constrained by the style of the reference speaker. Previous approaches lacked the ability to flexibly manipulate voice styles after cloning. 2) Zero-Shot Cross-Lingual Voice Cloning. OpenVoice achieves zero-shot cross-lingual voice cloning for languages not included in the massive-speaker training set. Unlike previous approaches, which typically require extensive massive-speaker multi-lingual (MSML) dataset for all languages, OpenVoice can clone voices into a new language without any massive-speaker training data for that language. OpenVoice is also computationally efficient, costing tens of times less than commercially available APIs that offer even inferior performance. To foster further research in the field, we have made the source code and trained model publicly accessible. We also provide qualitative results in our demo website. OpenVoice has been used by more than 2M users worldwide as the voice engine of MyShell.ai

</details>

### [Rapid Speaker Adaptation in Low Resource Text to Speech Systems using Synthetic Data and Transfer learning](2312.01107.md)
**Raviraj Joshi et.al.** · 2023-12-02

### [Code-Mixed Text to Speech Synthesis under Low-Resource Constraints](2312.01103.md)
**Raviraj Joshi, Nikesh Garera** · 2023-12-02

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) systems are an important component in voice-based e-commerce applications. These applications include end-to-end voice assistant and customer experience (CX) voice bot. Code-mixed TTS is also relevant in these applications since the product names are commonly described in English while the surrounding text is in a regional language. In this work, we describe our approaches for production quality code-mixed Hindi-English TTS systems built for e-commerce applications. We propose a data-oriented approach by utilizing monolingual data sets in individual languages. We leverage a transliteration model to convert the Roman text into a common Devanagari script and then combine both datasets for training. We show that such single script bi-lingual training without any code-mixing works well for pure code-mixed test sets. We further present an exhaustive evaluation of single-speaker adaptation and multi-speaker training with Tacotron2 + Waveglow setup to show that the former approach works better. These approaches are also coupled with transfer learning and decoder-only fine-tuning to improve performance. We compare these approaches with the Google TTS and report a positive CMOS score of 0.02 with the proposed transfer learning approach. We also perform low-resource voice adaptation experiments to show that a new voice can be onboarded with just 3 hrs of data. This highlights the importance of our pre-trained models in resource-constrained settings. This subjective evaluation is performed on a large number of out-of-domain pure code-mixed sentences to demonstrate the high quality of the systems.

</details>

### [HierSpeech++: Bridging the Gap between Semantic and Acoustic Representation of Speech by Hierarchical Variational Inference for Zero-shot Speech Synthesis](2311.12454.md)
**Sang-Hoon Lee et.al.** · 2023-11-27

### [Learning Arousal-Valence Representation from Categorical Emotion Labels of Speech](2311.14816.md)
**Enting Zhou, You Zhang, Zhiyao Duan** · 2023-11-24

<details>
<summary>Abstract</summary>

Dimensional representations of speech emotions such as the arousal-valence (AV) representation provide a continuous and fine-grained description and control than their categorical counterparts. They have wide applications in tasks such as dynamic emotion understanding and expressive text-to-speech synthesis. Existing methods that predict the dimensional emotion representation from speech cast it as a supervised regression task. These methods face data scarcity issues, as dimensional annotations are much harder to acquire than categorical labels. In this work, we propose to learn the AV representation from categorical emotion labels of speech. We start by learning a rich and emotion-relevant high-dimensional speech feature representation using self-supervised pre-training and emotion classification fine-tuning. This representation is then mapped to the 2D AV space according to psychological findings through anchored dimensionality reduction. Experiments show that our method achieves a Concordance Correlation Coefficient (CCC) performance comparable to state-of-the-art supervised regression methods on IEMOCAP without leveraging ground-truth AV annotations during training. This validates our proposed approach on AV prediction. Furthermore, visualization of AV predictions on MEAD and EmoDB datasets shows the interpretability of the learned AV representations.

</details>

### [Custom Data Augmentation for low resource ASR using Bark and Retrieval-Based Voice Conversion](2311.14836.md)
**Anand Kamble, Aniket Tathe, Suyash Kumbharkar, Atharva Bhandare et al.** · 2023-11-24

<details>
<summary>Abstract</summary>

This paper proposes two innovative methodologies to construct customized Common Voice datasets for low-resource languages like Hindi. The first methodology leverages Bark, a transformer-based text-to-audio model developed by Suno, and incorporates Meta's enCodec and a pre-trained HuBert model to enhance Bark's performance. The second methodology employs Retrieval-Based Voice Conversion (RVC) and uses the Ozen toolkit for data preparation. Both methodologies contribute to the advancement of ASR technology and offer valuable insights into addressing the challenges of constructing customized Common Voice datasets for under-resourced languages. Furthermore, they provide a pathway to achieving high-quality, personalized voice generation for a range of applications.

</details>

### [Guided Flows for Generative Modeling and Decision Making](2311.13443.md)
**Qinqing Zheng, Matt Le, Neta Shaul, Yaron Lipman et al.** · 2023-11-22

<details>
<summary>Abstract</summary>

Classifier-free guidance is a key component for enhancing the performance of conditional generative models across diverse tasks. While it has previously demonstrated remarkable improvements for the sample quality, it has only been exclusively employed for diffusion models. In this paper, we integrate classifier-free guidance into Flow Matching (FM) models, an alternative simulation-free approach that trains Continuous Normalizing Flows (CNFs) based on regressing vector fields. We explore the usage of \emph{Guided Flows} for a variety of downstream applications. We show that Guided Flows significantly improves the sample quality in conditional image generation and zero-shot text-to-speech synthesis, boasting state-of-the-art performance. Notably, we are the first to apply flow models for plan generation in the offline reinforcement learning setting, showcasing a 10x speedup in computation compared to diffusion models while maintaining comparable performance.

</details>

### [StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models](2306.07691.md)
**Yinghao Aaron Li et.al.** · 2023-11-20

### [StyleTTS: A Style-Based Generative Model for Natural and Diverse Text-to-Speech Synthesis](2205.15439.md)
**Yinghao Aaron Li et.al.** · 2023-11-20

### [ELF: Encoding Speaker-Specific Latent Speech Feature for Speech Synthesis](2311.11745.md)
**Jungil Kong, Junmo Lee, Jeongmin Kim, Beomjeong Kim et al.** · 2023-11-20

<details>
<summary>Abstract</summary>

In this work, we propose a novel method for modeling numerous speakers, which enables expressing the overall characteristics of speakers in detail like a trained multi-speaker model without additional training on the target speaker's dataset. Although various works with similar purposes have been actively studied, their performance has not yet reached that of trained multi-speaker models due to their fundamental limitations. To overcome previous limitations, we propose effective methods for feature learning and representing target speakers' speech characteristics by discretizing the features and conditioning them to a speech synthesis model. Our method obtained a significantly higher similarity mean opinion score (SMOS) in subjective similarity evaluation than seen speakers of a high-performance multi-speaker model, even with unseen speakers. The proposed method also outperforms a zero-shot method by significant margins. Furthermore, our method shows remarkable performance in generating new artificial speakers. In addition, we demonstrate that the encoded latent features are sufficiently informative to reconstruct an original speaker's speech completely. It implies that our method can be used as a general methodology to encode and reconstruct speakers' characteristics in various tasks.

</details>

### [APNet2: High-quality and High-efficiency Neural Vocoder with Direct Prediction of Amplitude and Phase Spectra](2311.11545.md)
**Hui-Peng Du, Ye-Xin Lu, Yang Ai, Zhen-Hua Ling** · 2023-11-20

<details>
<summary>Abstract</summary>

In our previous work, we proposed a neural vocoder called APNet, which directly predicts speech amplitude and phase spectra with a 5 ms frame shift in parallel from the input acoustic features, and then reconstructs the 16 kHz speech waveform using inverse short-time Fourier transform (ISTFT). APNet demonstrates the capability to generate synthesized speech of comparable quality to the HiFi-GAN vocoder but with a considerably improved inference speed. However, the performance of the APNet vocoder is constrained by the waveform sampling rate and spectral frame shift, limiting its practicality for high-quality speech synthesis. Therefore, this paper proposes an improved iteration of APNet, named APNet2. The proposed APNet2 vocoder adopts ConvNeXt v2 as the backbone network for amplitude and phase predictions, expecting to enhance the modeling capability. Additionally, we introduce a multi-resolution discriminator (MRD) into the GAN-based losses and optimize the form of certain losses. At a common configuration with a waveform sampling rate of 22.05 kHz and spectral frame shift of 256 points (i.e., approximately 11.6ms), our proposed APNet2 vocoder outperformed the original APNet and Vocos vocoders in terms of synthesized speech quality. The synthesized speech quality of APNet2 is also comparable to that of HiFi-GAN and iSTFTNet, while offering a significantly faster inference speed.

</details>

### [Utilizing Speech Emotion Recognition and Recommender Systems for Negative Emotion Handling in Therapy Chatbots](2311.11116.md)
**Farideh Majidi, Marzieh Bahrami** · 2023-11-18

<details>
<summary>Abstract</summary>

Emotional well-being significantly influences mental health and overall quality of life. As therapy chatbots become increasingly prevalent, their ability to comprehend and respond empathetically to users' emotions remains limited. This paper addresses this limitation by proposing an approach to enhance therapy chatbots with auditory perception, enabling them to understand users' feelings and provide human-like empathy. The proposed method incorporates speech emotion recognition (SER) techniques using Convolutional Neural Network (CNN) models and the ShEMO dataset to accurately detect and classify negative emotions, including anger, fear, and sadness. The SER model achieves a validation accuracy of 88%, demonstrating its effectiveness in recognizing emotional states from speech signals. Furthermore, a recommender system is developed, leveraging the SER model's output to generate personalized recommendations for managing negative emotions, for which a new bilingual dataset was generated as well since there is no such dataset available for this task. The recommender model achieves an accuracy of 98% by employing a combination of global vectors for word representation (GloVe) and LSTM models. To provide a more immersive and empathetic user experience, a text-to-speech model called GlowTTS is integrated, enabling the therapy chatbot to audibly communicate the generated recommendations to users in both English and Persian. The proposed approach offers promising potential to enhance therapy chatbots by providing them with the ability to recognize and respond to users' emotions, ultimately improving the delivery of mental health support for both English and Persian-speaking users.

</details>

### [Data Center Audio/Video Intelligence on Device (DAVID) -- An Edge-AI Platform for Smart-Toys](2311.11030.md)
**Gabriel Cosache, Francisco Salgado, Cosmin Rotariu, George Sterpu et al.** · 2023-11-18

<details>
<summary>Abstract</summary>

An overview is given of the DAVID Smart-Toy platform, one of the first Edge AI platform designs to incorporate advanced low-power data processing by neural inference models co-located with the relevant image or audio sensors. There is also on-board capability for in-device text-to-speech generation. Two alternative embodiments are presented: a smart Teddy-bear, and a roving dog-like robot. The platform offers a speech-driven user interface and can observe and interpret user actions and facial expressions via its computer vision sensor node. A particular benefit of this design is that no personally identifiable information passes beyond the neural inference nodes thus providing inbuilt compliance with data protection regulations.

</details>

### [A Study on Altering the Latent Space of Pretrained Text to Speech Models for Improved Expressiveness](2311.10804.md)
**Mathias Vogel et.al.** · 2023-11-17

### [LE-SSL-MOS: Self-Supervised Learning MOS Prediction with Listener Enhancement](2311.10656.md)
**Zili Qi, Xinhui Hu, Wangjin Zhou, Sheng Li et al.** · 2023-11-17

<details>
<summary>Abstract</summary>

Recently, researchers have shown an increasing interest in automatically predicting the subjective evaluation for speech synthesis systems. This prediction is a challenging task, especially on the out-of-domain test set. In this paper, we proposed a novel fusion model for MOS prediction that combines supervised and unsupervised approaches. In the supervised aspect, we developed an SSL-based predictor called LE-SSL-MOS. The LE-SSL-MOS utilizes pre-trained self-supervised learning models and further improves prediction accuracy by utilizing the opinion scores of each utterance in the listener enhancement branch. In the unsupervised aspect, two steps are contained: we fine-tuned the unit language model (ULM) using highly intelligible domain data to improve the correlation of an unsupervised metric - SpeechLMScore. Another is that we utilized ASR confidence as a new metric with the help of ensemble learning. To our knowledge, this is the first architecture that fuses supervised and unsupervised methods for MOS prediction. With these approaches, our experimental results on the VoiceMOS Challenge 2023 show that LE-SSL-MOS performs better than the baseline. Our fusion system achieved an absolute improvement of 13% over LE-SSL-MOS on the noisy and enhanced speech track. Our system ranked 1st and 2nd, respectively, in the French speech synthesis track and the challenge's noisy and enhanced speech track.

</details>

### [Improving fairness for spoken language understanding in atypical speech with Text-to-Speech](2311.10149.md)
**Helin Wang, Venkatesh Ravichandran, Milind Rao, Becky Lammers et al.** · 2023-11-16

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) systems often exhibit suboptimal performance in processing atypical speech, typically caused by neurological conditions and motor impairments. Recent advancements in Text-to-Speech (TTS) synthesis-based augmentation for more fair SLU have struggled to accurately capture the unique vocal characteristics of atypical speakers, largely due to insufficient data. To address this issue, we present a novel data augmentation method for atypical speakers by finetuning a TTS model, called Aty-TTS. Aty-TTS models speaker and atypical characteristics via knowledge transferring from a voice conversion model. Then, we use the augmented data to train SLU models adapted to atypical speech. To train these data augmentation models and evaluate the resulting SLU systems, we have collected a new atypical speech dataset containing intent annotation. Both objective and subjective assessments validate that Aty-TTS is capable of generating high-quality atypical speech. Furthermore, it serves as an effective data augmentation strategy, contributing to more fair SLU systems that can better accommodate individuals with atypical speech patterns.

</details>

### [CLN-VC: Text-Free Voice Conversion Based on Fine-Grained Style Control and Contrastive Learning with Negative Samples Augmentation](2311.08670.md)
**Yimin Deng, Xulong Zhang, Jianzong Wang, Ning Cheng et al.** · 2023-11-15

<details>
<summary>Abstract</summary>

Better disentanglement of speech representation is essential to improve the quality of voice conversion. Recently contrastive learning is applied to voice conversion successfully based on speaker labels. However, the performance of model will reduce in conversion between similar speakers. Hence, we propose an augmented negative sample selection to address the issue. Specifically, we create hard negative samples based on the proposed speaker fusion module to improve learning ability of speaker encoder. Furthermore, considering the fine-grain modeling of speaker style, we employ a reference encoder to extract fine-grained style and conduct the augmented contrastive learning on global style. The experimental results show that the proposed method outperforms previous work in voice conversion tasks.

</details>

### [Exploring the Potential of Large Language Models in Computational Argumentation](2311.09022.md)
**Guizhen Chen, Liying Cheng, Luu Anh Tuan, Lidong Bing** · 2023-11-15

<details>
<summary>Abstract</summary>

Computational argumentation has become an essential tool in various domains, including law, public policy, and artificial intelligence. It is an emerging research field in natural language processing that attracts increasing attention. Research on computational argumentation mainly involves two types of tasks: argument mining and argument generation. As large language models (LLMs) have demonstrated impressive capabilities in understanding context and generating natural language, it is worthwhile to evaluate the performance of LLMs on diverse computational argumentation tasks. This work aims to embark on an assessment of LLMs, such as ChatGPT, Flan models, and LLaMA2 models, in both zero-shot and few-shot settings. We organize existing tasks into six main categories and standardize the format of fourteen openly available datasets. In addition, we present a new benchmark dataset on counter speech generation that aims to holistically evaluate the end-to-end performance of LLMs on argument mining and argument generation. Extensive experiments show that LLMs exhibit commendable performance across most of the datasets, demonstrating their capabilities in the field of argumentation. Our analysis offers valuable suggestions for evaluating computational argumentation and its integration with LLMs in future research endeavors.

</details>

### [AntiFake: Using Adversarial Audio to Prevent Unauthorized Speech Synthesis](s2:547324fa11f2e4c6be4dc85479b1b433dc5e9439.md)
**Zhiyuan Yu, Shixuan Zhai, Ning Zhang** · 2023-11-15

<details>
<summary>Abstract</summary>

The rapid development of deep neural networks and generative AI has catalyzed growth in realistic speech synthesis. While this technology has great potential to improve lives, it also leads to the emergence of ''DeepFake'' where synthesized speech can be misused to deceive humans and machines for nefarious purposes. In response to this evolving threat, there has been a significant amount of interest in mitigating this threat by DeepFake detection. Complementary to the existing work, we propose to take the preventative approach and introduce AntiFake, a defense mechanism that relies on adversarial examples to prevent unauthorized speech synthesis. To ensure the transferability to attackers' unknown synthesis models, an ensemble learning approach is adopted to improve the generalizability of the optimization process. To validate the efficacy of the proposed system, we evaluated AntiFake against five state-of-the-art synthesizers using real-world DeepFake speech samples. The experiments indicated that AntiFake achieved over 95% protection rate even to unknown black-box models. We have also conducted usability tests involving 24 human participants to ensure the solution is accessible to diverse populations.

</details>

### [Reimagining Speech: A Scoping Review of Deep Learning-Powered Voice Conversion](2311.08104.md)
**Anders R. Bargum, Stefania Serafin, Cumhur Erkut** · 2023-11-14

<details>
<summary>Abstract</summary>

Research on deep learning-powered voice conversion (VC) in speech-to-speech scenarios is getting increasingly popular. Although many of the works in the field of voice conversion share a common global pipeline, there is a considerable diversity in the underlying structures, methods, and neural sub-blocks used across research efforts. Thus, obtaining a comprehensive understanding of the reasons behind the choice of the different methods in the voice conversion pipeline can be challenging, and the actual hurdles in the proposed solutions are often unclear. To shed light on these aspects, this paper presents a scoping review that explores the use of deep learning in speech analysis, synthesis, and disentangled speech representation learning within modern voice conversion systems. We screened 621 publications from more than 38 different venues between the years 2017 and 2023, followed by an in-depth review of a final database consisting of 123 eligible studies. Based on the review, we summarise the most frequently used approaches to voice conversion based on deep learning and highlight common pitfalls within the community. Lastly, we condense the knowledge gathered, identify main challenges and provide recommendations for future research directions.

</details>

### [CSLP-AE: A Contrastive Split-Latent Permutation Autoencoder Framework for Zero-Shot Electroencephalography Signal Conversion](2311.07788.md)
**Anders Vestergaard Nørskov, Alexander Neergaard Zahid, Morten Mørup** · 2023-11-13

<details>
<summary>Abstract</summary>

Electroencephalography (EEG) is a prominent non-invasive neuroimaging technique providing insights into brain function. Unfortunately, EEG data exhibit a high degree of noise and variability across subjects hampering generalizable signal extraction. Therefore, a key aim in EEG analysis is to extract the underlying neural activation (content) as well as to account for the individual subject variability (style). We hypothesize that the ability to convert EEG signals between tasks and subjects requires the extraction of latent representations accounting for content and style. Inspired by recent advancements in voice conversion technologies, we propose a novel contrastive split-latent permutation autoencoder (CSLP-AE) framework that directly optimizes for EEG conversion. Importantly, the latent representations are guided using contrastive learning to promote the latent splits to explicitly represent subject (style) and task (content). We contrast CSLP-AE to conventional supervised, unsupervised (AE), and self-supervised (contrastive learning) training and find that the proposed approach provides favorable generalizable characterizations of subject and task. Importantly, the procedure also enables zero-shot conversion between unseen subjects. While the present work only considers conversion of EEG, the proposed CSLP-AE provides a general framework for signal conversion and extraction of content (task activation) and style (subject variability) components of general interest for the modeling and analysis of biological signals.

</details>

### [SponTTS: modeling and transferring spontaneous style for TTS](2311.07179.md)
**Hanzhao Li, Xinfa Zhu, Liumeng Xue, Yang Song et al.** · 2023-11-13

<details>
<summary>Abstract</summary>

Spontaneous speaking style exhibits notable differences from other speaking styles due to various spontaneous phenomena (e.g., filled pauses, prolongation) and substantial prosody variation (e.g., diverse pitch and duration variation, occasional non-verbal speech like a smile), posing challenges to modeling and prediction of spontaneous style. Moreover, the limitation of high-quality spontaneous data constrains spontaneous speech generation for speakers without spontaneous data. To address these problems, we propose SponTTS, a two-stage approach based on neural bottleneck (BN) features to model and transfer spontaneous style for TTS. In the first stage, we adopt a Conditional Variational Autoencoder (CVAE) to capture spontaneous prosody from a BN feature and involve the spontaneous phenomena by the constraint of spontaneous phenomena embedding prediction loss. Besides, we introduce a flow-based predictor to predict a latent spontaneous style representation from the text, which enriches the prosody and context-specific spontaneous phenomena during inference. In the second stage, we adopt a VITS-like module to transfer the spontaneous style learned in the first stage to the target speakers. Experiments demonstrate that SponTTS is effective in modeling spontaneous style and transferring the style to the target speakers, generating spontaneous speech with high naturalness, expressiveness, and speaker similarity. The zero-shot spontaneous style TTS test further verifies the generalization and robustness of SponTTS in generating spontaneous speech for unseen speakers.

</details>

### [ChatAnything: Facetime Chat with LLM-Enhanced Personas](2311.06772.md)
**Yilin Zhao, Xinbin Yuan, Shanghua Gao, Zhijie Lin et al.** · 2023-11-12

<details>
<summary>Abstract</summary>

In this technical report, we target generating anthropomorphized personas for LLM-based characters in an online manner, including visual appearance, personality and tones, with only text descriptions. To achieve this, we first leverage the in-context learning capability of LLMs for personality generation by carefully designing a set of system prompts. We then propose two novel concepts: the mixture of voices (MoV) and the mixture of diffusers (MoD) for diverse voice and appearance generation. For MoV, we utilize the text-to-speech (TTS) algorithms with a variety of pre-defined tones and select the most matching one based on the user-provided text description automatically. For MoD, we combine the recent popular text-to-image generation techniques and talking head algorithms to streamline the process of generating talking objects. We termed the whole framework as ChatAnything. With it, users could be able to animate anything with any personas that are anthropomorphic using just a few text inputs. However, we have observed that the anthropomorphic objects produced by current generative models are often undetectable by pre-trained face landmark detectors, leading to failure of the face motion generation, even if these faces possess human-like appearances because those images are nearly seen during the training (e.g., OOD samples). To address this issue, we incorporate pixel-level guidance to infuse human face landmarks during the image generation phase. To benchmark these metrics, we have built an evaluation dataset. Based on it, we verify that the detection rate of the face landmark is significantly increased from 57.0% to 92.5% thus allowing automatic face animation based on generated speech content. The code and more results can be found at https://chatanything.github.io/.

</details>

### [NewsGPT: ChatGPT Integration for Robot-Reporter](2311.06640.md)
**Abdelhadi Hireche, Abdelkader Nasreddine Belkacem, Sadia Jamil, Chao Chen** · 2023-11-11

<details>
<summary>Abstract</summary>

The integration of large language models (LLMs) with social robots has emerged as a promising avenue for enhancing human-robot interactions at a time when news reports generated by artificial intelligence (AI) are gaining in credibility. This integration is expected to intensify and become a more productive resource for journalism, media, communication, and education. In this paper a novel system is proposed that integrates AI's generative pretrained transformer (GPT) model with the Pepper robot, with the aim of improving the robot's natural language understanding and response generation capabilities for enhanced social interactions. By leveraging GPT's powerful language processing capabilities, this system offers a comprehensive pipeline that incorporates voice input recording, speech-to-text transcription, context analysis, and text-to-speech synthesis action generation. The Pepper robot is enabled to comprehend user queries, generate informative responses with general knowledge, maintain contextually relevant conversations, and act as a more domain-oriented news reporter. It is also linked with a news resource and powered with a Google search capability. To evaluate the performance of the framework, experiments were conducted involving a set of diverse questions. The robot's responses were assessed on the basis of eight criteria, including relevance, context, and fluency. Despite some identified limitations, this system contributes to the field of journalism and human-robot interaction by showcasing the potential of integrating LLMs with social robots. The proposed framework opens up opportunities for improving the conversational capabilities of robots, enabling interactions that are smoother, more engaging, and more context aware.

</details>

### [Adversarial Fine-tuning using Generated Respiratory Sound to Address Class Imbalance](2311.06480.md)
**June-Woo Kim, Chihyeon Yoon, Miika Toikkanen, Sangmin Bae et al.** · 2023-11-11

<details>
<summary>Abstract</summary>

Deep generative models have emerged as a promising approach in the medical image domain to address data scarcity. However, their use for sequential data like respiratory sounds is less explored. In this work, we propose a straightforward approach to augment imbalanced respiratory sound data using an audio diffusion model as a conditional neural vocoder. We also demonstrate a simple yet effective adversarial fine-tuning method to align features between the synthetic and real respiratory sound samples to improve respiratory sound classification performance. Our experimental results on the ICBHI dataset demonstrate that the proposed adversarial fine-tuning is effective, while only using the conventional augmentation method shows performance degradation. Moreover, our method outperforms the baseline by 2.24% on the ICBHI Score and improves the accuracy of the minority classes up to 26.58%. For the supplementary material, we provide the code at https://github.com/kaen2891/adversarial_fine-tuning_using_generated_respiratory_sound.

</details>

### [Transduce and Speak: Neural Transducer for Text-to-Speech with Semantic Token Prediction](2311.02898.md)
**Minchan Kim et.al.** · 2023-11-08

### [Synthetic Speaking Children -- Why We Need Them and How to Make Them](2311.06307.md)
**Muhammad Ali Farooq, Dan Bigioi, Rishabh Jain, Wang Yao et al.** · 2023-11-08

<details>
<summary>Abstract</summary>

Contemporary Human Computer Interaction (HCI) research relies primarily on neural network models for machine vision and speech understanding of a system user. Such models require extensively annotated training datasets for optimal performance and when building interfaces for users from a vulnerable population such as young children, GDPR introduces significant complexities in data collection, management, and processing. Motivated by the training needs of an Edge AI smart toy platform this research explores the latest advances in generative neural technologies and provides a working proof of concept of a controllable data generation pipeline for speech driven facial training data at scale. In this context, we demonstrate how StyleGAN2 can be finetuned to create a gender balanced dataset of children's faces. This dataset includes a variety of controllable factors such as facial expressions, age variations, facial poses, and even speech-driven animations with realistic lip synchronization. By combining generative text to speech models for child voice synthesis and a 3D landmark based talking heads pipeline, we can generate highly realistic, entirely synthetic, talking child video clips. These video clips can provide valuable, and controllable, synthetic training data for neural network models, bridging the gap when real data is scarce or restricted due to privacy regulations.

</details>

### [Loss Masking Is Not Needed in Decoder-only Transformer for Discrete-token-based ASR](2311.04534.md)
**Qian Chen, Wen Wang, Qinglin Zhang, Siqi Zheng et al.** · 2023-11-08

<details>
<summary>Abstract</summary>

Recently, unified speech-text models, such as SpeechGPT, VioLA, and AudioPaLM, have achieved remarkable performance on various speech tasks. These models discretize speech signals into tokens (speech discretization) and use a shared vocabulary for both text and speech tokens. Then they train a single decoder-only Transformer on a mixture of speech tasks. However, these models rely on the Loss Masking strategy for the ASR task, which ignores the dependency among speech tokens. In this paper, we propose to model speech tokens in an autoregressive way, similar to text. We find that applying the conventional cross-entropy loss on input speech tokens does not consistently improve the ASR performance over the Loss Masking approach. To address this issue, we propose a novel approach denoted Smoothed Label Distillation (SLD), which applies a KL divergence loss with smoothed labels on speech tokens. Our experiments show that SLD effectively models speech tokens and outperforms Loss Masking for decoder-only Transformers in ASR tasks with different speech discretization methods. The source code can be found here: https://github.com/alibaba-damo-academy/SpokenNLP/tree/main/sld

</details>

### [Diff-HierVC: Diffusion-based Hierarchical Voice Conversion with Robust Pitch Generation and Masked Prior for Zero-shot Speaker Adaptation](2311.04693.md)
**Ha-Yeong Choi, Sang-Hoon Lee, Seong-Whan Lee** · 2023-11-08

<details>
<summary>Abstract</summary>

Although voice conversion (VC) systems have shown a remarkable ability to transfer voice style, existing methods still have an inaccurate pitch and low speaker adaptation quality. To address these challenges, we introduce Diff-HierVC, a hierarchical VC system based on two diffusion models. We first introduce DiffPitch, which can effectively generate F0 with the target voice style. Subsequently, the generated F0 is fed to DiffVoice to convert the speech with a target voice style. Furthermore, using the source-filter encoder, we disentangle the speech and use the converted Mel-spectrogram as a data-driven prior in DiffVoice to improve the voice style transfer capacity. Finally, by using the masked prior in diffusion models, our model can improve the speaker adaptation quality. Experimental results verify the superiority of our model in pitch generation and voice style transfer performance, and our model also achieves a CER of 0.83% and EER of 3.29% in zero-shot VC scenarios.

</details>

### [Character-Level Bangla Text-to-IPA Transcription Using Transformer Architecture with Sequence Alignment](2311.03792.md)
**Jakir Hasan, Shrestha Datta, Ameya Debnath** · 2023-11-07

<details>
<summary>Abstract</summary>

The International Phonetic Alphabet (IPA) is indispensable in language learning and understanding, aiding users in accurate pronunciation and comprehension. Additionally, it plays a pivotal role in speech therapy, linguistic research, accurate transliteration, and the development of text-to-speech systems, making it an essential tool across diverse fields. Bangla being 7th as one of the widely used languages, gives rise to the need for IPA in its domain. Its IPA mapping is too diverse to be captured manually giving the need for Artificial Intelligence and Machine Learning in this field. In this study, we have utilized a transformer-based sequence-to-sequence model at the letter and symbol level to get the IPA of each Bangla word as the variation of IPA in association of different words is almost null. Our transformer model only consisted of 8.5 million parameters with only a single decoder and encoder layer. Additionally, to handle the punctuation marks and the occurrence of foreign languages in the text, we have utilized manual mapping as the model won't be able to learn to separate them from Bangla words while decreasing our required computational resources. Finally, maintaining the relative position of the sentence component IPAs and generation of the combined IPA has led us to achieve the top position with a word error rate of 0.10582 in the public ranking of DataVerse Challenge - ITVerse 2023 (https://www.kaggle.com/competitions/dataverse_2023/).

</details>

### [E3 TTS: Easy End-to-End Diffusion-based Text to Speech](2311.00945.md)
**Yuan Gao et.al.** · 2023-11-02

### [Expressive TTS Driven by Natural Language Prompts Using Few Human Annotations](2311.01260.md)
**Hanglei Zhang, Yiwei Guo, Sen Liu, Xie Chen et al.** · 2023-11-02

<details>
<summary>Abstract</summary>

Expressive text-to-speech (TTS) aims to synthesize speeches with human-like tones, moods, or even artistic attributes. Recent advancements in expressive TTS empower users with the ability to directly control synthesis style through natural language prompts. However, these methods often require excessive training with a significant amount of style-annotated data, which can be challenging to acquire. Moreover, they may have limited adaptability due to fixed style annotations. In this work, we present FreeStyleTTS (FS-TTS), a controllable expressive TTS model with minimal human annotations. Our approach utilizes a large language model (LLM) to transform expressive TTS into a style retrieval task. The LLM selects the best-matching style references from annotated utterances based on external style prompts, which can be raw input text or natural language style descriptions. The selected reference guides the TTS pipeline to synthesize speeches with the intended style. This innovative approach provides flexible, versatile, and precise style control with minimal human workload. Experiments on a Mandarin storytelling corpus demonstrate FS-TTS's proficiency in leveraging LLM's semantic inference ability to retrieve desired styles from either input text or user-defined descriptions. This results in synthetic speeches that are closely aligned with the specified styles.

</details>

### [On the Opportunities of Green Computing: A Survey](2311.00447.md)
**You Zhou, Xiujing Lin, Xiang Zhang, Maolin Wang et al.** · 2023-11-01

<details>
<summary>Abstract</summary>

Artificial Intelligence (AI) has achieved significant advancements in technology and research with the development over several decades, and is widely used in many areas including computing vision, natural language processing, time-series analysis, speech synthesis, etc. During the age of deep learning, especially with the arise of Large Language Models, a large majority of researchers' attention is paid on pursuing new state-of-the-art (SOTA) results, resulting in ever increasing of model size and computational complexity. The needs for high computing power brings higher carbon emission and undermines research fairness by preventing small or medium-sized research institutions and companies with limited funding in participating in research. To tackle the challenges of computing resources and environmental impact of AI, Green Computing has become a hot research topic. In this survey, we give a systematic overview of the technologies used in Green Computing. We propose the framework of Green Computing and devide it into four key components: (1) Measures of Greenness, (2) Energy-Efficient AI, (3) Energy-Efficient Computing Systems and (4) AI Use Cases for Sustainability. For each components, we discuss the research progress made and the commonly used techniques to optimize the AI efficiency. We conclude that this new research direction has the potential to address the conflicts between resource constraints and AI development. We encourage more researchers to put attention on this direction and make AI more environmental friendly.

</details>

### [Low-latency Real-time Voice Conversion on CPU](2311.00873.md)
**Konstantine Sadov, Matthew Hutter, Asara Near** · 2023-11-01

<details>
<summary>Abstract</summary>

We adapt the architectures of previous audio manipulation and generation neural networks to the task of real-time any-to-one voice conversion. Our resulting model, LLVC ($\textbf{L}$ow-latency $\textbf{L}$ow-resource $\textbf{V}$oice $\textbf{C}$onversion), has a latency of under 20ms at a bitrate of 16kHz and runs nearly 2.8x faster than real-time on a consumer CPU. LLVC uses both a generative adversarial architecture as well as knowledge distillation in order to attain this performance. To our knowledge LLVC achieves both the lowest resource usage as well as the lowest latency of any open-source voice conversion model. We provide open-source samples, code, and pretrained model weights at https://github.com/KoeAI/LLVC.

</details>

### [An Implementation of Multimodal Fusion System for Intelligent Digital Human Generation](2310.20251.md)
**Yingjie Zhou, Yaodong Chen, Kaiyue Bi, Lian Xiong et al.** · 2023-10-31

<details>
<summary>Abstract</summary>

With the rapid development of artificial intelligence (AI), digital humans have attracted more and more attention and are expected to achieve a wide range of applications in several industries. Then, most of the existing digital humans still rely on manual modeling by designers, which is a cumbersome process and has a long development cycle. Therefore, facing the rise of digital humans, there is an urgent need for a digital human generation system combined with AI to improve development efficiency. In this paper, an implementation scheme of an intelligent digital human generation system with multimodal fusion is proposed. Specifically, text, speech and image are taken as inputs, and interactive speech is synthesized using large language model (LLM), voiceprint extraction, and text-to-speech conversion techniques. Then the input image is age-transformed and a suitable image is selected as the driving image. Then, the modification and generation of digital human video content is realized by digital human driving, novel view synthesis, and intelligent dressing techniques. Finally, we enhance the user experience through style transfer, super-resolution, and quality evaluation. Experimental results show that the system can effectively realize digital human generation. The related code is released at https://github.com/zyj-2000/CUMT_2D_PhotoSpeaker.

</details>

### [Seeing Through the Conversation: Audio-Visual Speech Separation based on Diffusion Model](2310.19581.md)
**Suyeon Lee, Chaeyoung Jung, Youngjoon Jang, Jaehun Kim et al.** · 2023-10-30

<details>
<summary>Abstract</summary>

The objective of this work is to extract target speaker's voice from a mixture of voices using visual cues. Existing works on audio-visual speech separation have demonstrated their performance with promising intelligibility, but maintaining naturalness remains a challenge. To address this issue, we propose AVDiffuSS, an audio-visual speech separation model based on a diffusion mechanism known for its capability in generating natural samples. For an effective fusion of the two modalities for diffusion, we also propose a cross-attention-based feature fusion mechanism. This mechanism is specifically tailored for the speech domain to integrate the phonetic information from audio-visual correspondence in speech generation. In this way, the fusion process maintains the high temporal resolution of the features, without excessive computational requirements. We demonstrate that the proposed framework achieves state-of-the-art results on two benchmarks, including VoxCeleb2 and LRS3, producing speech with notably better naturalness.

</details>

### [Style Description based Text-to-Speech with Conditional Prosodic Layer Normalization based Diffusion GAN](2310.18169.md)
**Neeraj Kumar et.al.** · 2023-10-27

### [Controllable Generation of Artificial Speaker Embeddings through Discovery of Principal Directions](2310.17502.md)
**Florian Lux, Pascal Tilli, Sarina Meyer, Ngoc Thang Vu** · 2023-10-26

<details>
<summary>Abstract</summary>

Customizing voice and speaking style in a speech synthesis system with intuitive and fine-grained controls is challenging, given that little data with appropriate labels is available. Furthermore, editing an existing human's voice also comes with ethical concerns. In this paper, we propose a method to generate artificial speaker embeddings that cannot be linked to a real human while offering intuitive and fine-grained control over the voice and speaking style of the embeddings, without requiring any labels for speaker or style. The artificial and controllable embeddings can be fed to a speech synthesis system, conditioned on embeddings of real humans during training, without sacrificing privacy during inference.

</details>

### [Boosting Multi-Speaker Expressive Speech Synthesis with Semi-supervised Contrastive Learning](2310.17101.md)
**Xinfa Zhu, Yuke Li, Yi Lei, Ning Jiang et al.** · 2023-10-26

<details>
<summary>Abstract</summary>

This paper aims to build a multi-speaker expressive TTS system, synthesizing a target speaker's speech with multiple styles and emotions. To this end, we propose a novel contrastive learning-based TTS approach to transfer style and emotion across speakers. Specifically, contrastive learning from different levels, i.e. utterance and category level, is leveraged to extract the disentangled style, emotion, and speaker representations from speech for style and emotion transfer. Furthermore, a semi-supervised training strategy is introduced to improve the data utilization efficiency by involving multi-domain data, including style-labeled data, emotion-labeled data, and abundant unlabeled data. To achieve expressive speech with diverse styles and emotions for a target speaker, the learned disentangled representations are integrated into an improved VITS model. Experiments on multi-domain data demonstrate the effectiveness of the proposed method.

</details>

### [The IMS Toucan System for the Blizzard Challenge 2023](2310.17499.md)
**Florian Lux, Julia Koch, Sarina Meyer, Thomas Bott et al.** · 2023-10-26

<details>
<summary>Abstract</summary>

For our contribution to the Blizzard Challenge 2023, we improved on the system we submitted to the Blizzard Challenge 2021. Our approach entails a rule-based text-to-phoneme processing system that includes rule-based disambiguation of homographs in the French language. It then transforms the phonemes to spectrograms as intermediate representations using a fast and efficient non-autoregressive synthesis architecture based on Conformer and Glow. A GAN based neural vocoder that combines recent state-of-the-art approaches converts the spectrogram to the final wave. We carefully designed the data processing, training, and inference procedures for the challenge data. Our system identifier is G. Open source code and demo are available.

</details>

### [DiffS2UT: A Semantic Preserving Diffusion Model for Textless Direct Speech-to-Speech Translation](2310.17570.md)
**Yongxin Zhu, Zhujin Gao, Xinyuan Zhou, Zhongyi Ye et al.** · 2023-10-26

<details>
<summary>Abstract</summary>

While Diffusion Generative Models have achieved great success on image generation tasks, how to efficiently and effectively incorporate them into speech generation especially translation tasks remains a non-trivial problem. Specifically, due to the low information density of speech data, the transformed discrete speech unit sequence is much longer than the corresponding text transcription, posing significant challenges to existing auto-regressive models. Furthermore, it is not optimal to brutally apply discrete diffusion on the speech unit sequence while disregarding the continuous space structure, which will degrade the generation performance significantly. In this paper, we propose a novel diffusion model by applying the diffusion forward process in the \textit{continuous} speech representation space, while employing the diffusion backward process in the \textit{discrete} speech unit space. In this way, we preserve the semantic structure of the continuous speech representation space in the diffusion process and integrate the continuous and discrete diffusion models. We conduct extensive experiments on the textless direct speech-to-speech translation task, where the proposed method achieves comparable results to the computationally intensive auto-regressive baselines (500 steps on average) with significantly fewer decoding steps (50 steps).

</details>

### [Generative Pre-training for Speech with Flow Matching](2310.16338.md)
**Alexander H. Liu, Matt Le, Apoorv Vyas, Bowen Shi et al.** · 2023-10-25

<details>
<summary>Abstract</summary>

Generative models have gained more and more attention in recent years for their remarkable success in tasks that required estimating and sampling data distribution to generate high-fidelity synthetic data. In speech, text-to-speech synthesis and neural vocoder are good examples where generative models have shined. While generative models have been applied to different applications in speech, there exists no general-purpose generative model that models speech directly. In this work, we take a step toward this direction by showing a single pre-trained generative model can be adapted to different downstream tasks with strong performance. Specifically, we pre-trained a generative model, named SpeechFlow, on 60k hours of untranscribed speech with Flow Matching and masked conditions. Experiment results show the pre-trained generative model can be fine-tuned with task-specific data to match or surpass existing expert models on speech enhancement, separation, and synthesis. Our work suggested a foundational model for generation tasks in speech can be built with generative pre-training.

</details>

### [Modeling Irregular Voice in End-to-End Speech Synthesis via Speaker Adaptation](s2:f3e773c4fc72bfacdeedc0313db39d995f996dfe.md)
**Ali Raheem Mandeel, M. Al-Radhi, T. Csapó** · 2023-10-25

<details>
<summary>Abstract</summary>

End-to-end text-to-speech (TTS) synthesizers may not create a speech similar to the target speaker when the adaptation data is limited or/and chosen randomly. Creaky voice might occur frequently, depending on the speaker and the context. This paper uses speaker adaptation to model creaky voice in speech synthesis. We adapted FastSpeech 2 with four target speakers by selecting the adaptation data based on the occurrence of creaky phonation: 1) sentences with frequent creaky voice, 2) randomly chosen sentences, and 3) sentences with few creaky voice. In an objective evaluation, the proposed model successfully modeled creaky voice using data selection (1), producing speech with more creakiness than the other data selections. A subjective test revealed that these frequent creaky voice synthesized samples (for the average of four speakers) obtained slightly less preference than the synthesized speech from a few creaky voice adaptation sentences. Irregular voice models might contribute to building emotional and personalized speech synthesis.

</details>

### [Enhancing End-to-End Speech Synthesis by Modeling Interrogative Sentences with Speaker Adaptation](s2:161a26583ea8b228a84eff8406d5cde21a44185e.md)
**Ali Raheem Mandeel, M. Al-Radhi, T. Csapó** · 2023-10-25

<details>
<summary>Abstract</summary>

Despite end-to-end text-to-speech (TTS) synthesizers producing human-like speech, they might still need more intuitive user control over prosody. Modeling interrogative sentence prosody is challenging due to the significant variation in question types. Synthesized intonation frequently requires more accuracy, richness, and detail when only a small amount of adaptation data from particular sentence types are available. This paper uses speaker adaptation to enhance the modeling of interrogative sentence prosody in speech synthesis, tested on an English dataset. The adaptation data were selected based on the occurrence of interrogative sentences. The first dataset consisted of sentences with frequent interrogative sentences, whereas the second dataset contained declarative sentences. Two target speakers (male and female) were adapted. Objective and subjective evaluations show that the proposed model achieves remarkable performance in intonation. The MUSHRA subjective listening test has shown better intonation patterns using the interrogative dataset than the declarative one. The potential application of this model is for the vision impaired and chatbots/voice bots.

</details>

### [AutoDiff: combining Auto-encoder and Diffusion model for tabular data synthesizing](2310.15479.md)
**Namjoon Suh, Xiaofeng Lin, Din-Yin Hsieh, Merhdad Honarkhah et al.** · 2023-10-24

<details>
<summary>Abstract</summary>

Diffusion model has become a main paradigm for synthetic data generation in many subfields of modern machine learning, including computer vision, language model, or speech synthesis. In this paper, we leverage the power of diffusion model for generating synthetic tabular data. The heterogeneous features in tabular data have been main obstacles in tabular data synthesis, and we tackle this problem by employing the auto-encoder architecture. When compared with the state-of-the-art tabular synthesizers, the resulting synthetic tables from our model show nice statistical fidelities to the real data, and perform well in downstream tasks for machine learning utilities. We conducted the experiments over $15$ publicly available datasets. Notably, our model adeptly captures the correlations among features, which has been a long-standing challenge in tabular data synthesis. Our code is available at https://github.com/UCLA-Trustworthy-AI-Lab/AutoDiffusion.

</details>

### [DPP-TTS: Diversifying prosodic features of speech via determinantal point processes](2310.14663.md)
**Seongho Joo, Hyukhun Koh, Kyomin Jung** · 2023-10-23

<details>
<summary>Abstract</summary>

With the rapid advancement in deep generative models, recent neural Text-To-Speech(TTS) models have succeeded in synthesizing human-like speech. There have been some efforts to generate speech with various prosody beyond monotonous prosody patterns. However, previous works have several limitations. First, typical TTS models depend on the scaled sampling temperature for boosting the diversity of prosody. Speech samples generated at high sampling temperatures often lack perceptual prosodic diversity, which can adversely affect the naturalness of the speech. Second, the diversity among samples is neglected since the sampling procedure often focuses on a single speech sample rather than multiple ones. In this paper, we propose DPP-TTS: a text-to-speech model based on Determinantal Point Processes (DPPs) with a prosody diversifying module. Our TTS model is capable of generating speech samples that simultaneously consider perceptual diversity in each sample and among multiple samples. We demonstrate that DPP-TTS generates speech samples with more diversified prosody than baselines in the side-by-side comparison test considering the naturalness of speech at the same time.

</details>

### [Acoustic BPE for Speech Generation with Discrete Tokens](2310.14580.md)
**Feiyu Shen, Yiwei Guo, Chenpeng Du, Xie Chen et al.** · 2023-10-23

<details>
<summary>Abstract</summary>

Discrete audio tokens derived from self-supervised learning models have gained widespread usage in speech generation. However, current practice of directly utilizing audio tokens poses challenges for sequence modeling due to the length of the token sequence. Additionally, this approach places the burden on the model to establish correlations between tokens, further complicating the modeling process. To address this issue, we propose acoustic BPE which encodes frequent audio token patterns by utilizing byte-pair encoding. Acoustic BPE effectively reduces the sequence length and leverages the prior morphological information present in token sequence, which alleviates the modeling challenges of token correlation. Through comprehensive investigations on a speech language model trained with acoustic BPE, we confirm the notable advantages it offers, including faster inference and improved syntax capturing capabilities. In addition, we propose a novel rescore method to select the optimal synthetic speech among multiple candidates generated by rich-diversity TTS system. Experiments prove that rescore selection aligns closely with human preference, which highlights acoustic BPE's potential to other speech generation tasks.

</details>

### [An overview of text-to-speech systems and media applications](2310.14301.md)
**Mohammad Reza Hasanabadi** · 2023-10-22

<details>
<summary>Abstract</summary>

Producing synthetic voice, similar to human-like sound, is an emerging novelty of modern interactive media systems. Text-To-Speech (TTS) systems try to generate synthetic and authentic voices via text input. Besides, well known and familiar dubbing, announcing and narrating voices, as valuable possessions of any media organization, can be kept forever by utilizing TTS and Voice Conversion (VC) algorithms . The emergence of deep learning approaches has made such TTS systems more accurate and accessible. To understand TTS systems better, this paper investigates the key components of such systems including text analysis, acoustic modelling and vocoding. The paper then provides details of important state-of-the-art TTS systems based on deep learning. Finally, a comparison is made between recently released systems in term of backbone architecture, type of input and conversion, vocoder used and subjective assessment (MOS). Accordingly, Tacotron 2, Transformer TTS, WaveNet and FastSpeech 1 are among the most successful TTS systems ever released. In the discussion section, some suggestions are made to develop a TTS system with regard to the intended application.

</details>

### [Energy-Based Models For Speech Synthesis](2310.12765.md)
**Wanli Sun, Zehai Tu, Anton Ragni** · 2023-10-19

<details>
<summary>Abstract</summary>

Recently there has been a lot of interest in non-autoregressive (non-AR) models for speech synthesis, such as FastSpeech 2 and diffusion models. Unlike AR models, these models do not have autoregressive dependencies among outputs which makes inference efficient. This paper expands the range of available non-AR models with another member called energy-based models (EBMs). The paper describes how noise contrastive estimation, which relies on the comparison between positive and negative samples, can be used to train EBMs. It proposes a number of strategies for generating effective negative samples, including using high-performing AR models. It also describes how sampling from EBMs can be performed using Langevin Markov Chain Monte-Carlo (MCMC). The use of Langevin MCMC enables to draw connections between EBMs and currently popular diffusion models. Experiments on LJSpeech dataset show that the proposed approach offers improvements over Tacotron 2.

</details>

### [Leveraging Diverse Semantic-based Audio Pretrained Models for Singing Voice Conversion](2310.11160.md)
**Xueyao Zhang, Zihao Fang, Yicheng Gu, Haopeng Chen et al.** · 2023-10-17

<details>
<summary>Abstract</summary>

Singing Voice Conversion (SVC) is a technique that enables any singer to perform any song. To achieve this, it is essential to obtain speaker-agnostic representations from the source audio, which poses a significant challenge. A common solution involves utilizing a semantic-based audio pretrained model as a feature extractor. However, the degree to which the extracted features can meet the SVC requirements remains an open question. This includes their capability to accurately model melody and lyrics, the speaker-independency of their underlying acoustic information, and their robustness for in-the-wild acoustic environments. In this study, we investigate the knowledge within classical semantic-based pretrained models in much detail. We discover that the knowledge of different models is diverse and can be complementary for SVC. Based on the above, we design a Singing Voice Conversion framework based on Diverse Semantic-based Feature Fusion (DSFF-SVC). Experimental results demonstrate that DSFF-SVC can be generalized and improve various existing SVC models, particularly in challenging real-world conversion tasks. Our demo website is available at https://diversesemanticsvc.github.io/.

</details>

### [Generative Adversarial Training for Text-to-Speech Synthesis Based on Raw Phonetic Input and Explicit Prosody Modelling](2310.09636.md)
**Tiberiu Boros et.al.** · 2023-10-14

### [Attentive Multi-Layer Perceptron for Non-autoregressive Generation](2310.09512.md)
**Shuyang Jiang, Jun Zhang, Jiangtao Feng, Lin Zheng et al.** · 2023-10-14

<details>
<summary>Abstract</summary>

Autoregressive~(AR) generation almost dominates sequence generation for its efficacy. Recently, non-autoregressive~(NAR) generation gains increasing popularity for its efficiency and growing efficacy. However, its efficiency is still bottlenecked by quadratic complexity in sequence lengths, which is prohibitive for scaling to long sequence generation and few works have been done to mitigate this problem. In this paper, we propose a novel MLP variant, \textbf{A}ttentive \textbf{M}ulti-\textbf{L}ayer \textbf{P}erceptron~(AMLP), to produce a generation model with linear time and space complexity. Different from classic MLP with static and learnable projection matrices, AMLP leverages adaptive projections computed from inputs in an attentive mode. The sample-aware adaptive projections enable communications among tokens in a sequence, and model the measurement between the query and key space. Furthermore, we marry AMLP with popular NAR models, deriving a highly efficient NAR-AMLP architecture with linear time and space complexity. Empirical results show that such marriage architecture surpasses competitive efficient NAR models, by a significant margin on text-to-speech synthesis and machine translation. We also test AMLP's self- and cross-attention ability separately with extensive ablation experiments, and find them comparable or even superior to the other efficient models. The efficiency analysis further shows that AMLP extremely reduces the memory cost against vanilla non-autoregressive models for long sequences.

</details>

### [Speaking rate attention-based duration prediction for speed control TTS](2310.08846.md)
**Jesuraj Bandekar, Sathvik Udupa, Abhayjeet Singh, Anjali Jayakumar et al.** · 2023-10-13

<details>
<summary>Abstract</summary>

With the advent of high-quality speech synthesis, there is a lot of interest in controlling various prosodic attributes of speech. Speaking rate is an essential attribute towards modelling the expressivity of speech. In this work, we propose a novel approach to control the speaking rate for non-autoregressive TTS. We achieve this by conditioning the speaking rate inside the duration predictor, allowing implicit speaking rate control. We show the benefits of this approach by synthesising audio at various speaking rate factors and measuring the quality of speaking rate-controlled synthesised speech. Further, we study the effect of the speaking rate distribution of the training data towards effective rate control. Finally, we fine-tune a baseline pretrained TTS model to obtain speaking rate control TTS. We provide various analyses to showcase the benefits of using this proposed approach, along with objective as well as subjective metrics. We find that the proposed methods have higher subjective scores and lower speaker rate errors across many speaking rate factors over the baseline.

</details>

### [Low-latency Speech Enhancement via Speech Token Generation](2310.08981.md)
**Huaying Xue, Xiulian Peng, Yan Lu** · 2023-10-13

<details>
<summary>Abstract</summary>

Existing deep learning based speech enhancement mainly employ a data-driven approach, which leverage large amounts of data with a variety of noise types to achieve noise removal from noisy signal. However, the high dependence on the data limits its generalization on the unseen complex noises in real-life environment. In this paper, we focus on the low-latency scenario and regard speech enhancement as a speech generation problem conditioned on the noisy signal, where we generate clean speech instead of identifying and removing noises. Specifically, we propose a conditional generative framework for speech enhancement, which models clean speech by acoustic codes of a neural speech codec and generates the speech codes conditioned on past noisy frames in an auto-regressive way. Moreover, we propose an explicit-alignment approach to align noisy frames with the generated speech tokens to improve the robustness and scalability to different input lengths. Different from other methods that leverage multiple stages to generate speech codes, we leverage a single-stage speech generation approach based on the TF-Codec neural codec to achieve high speech quality with low latency. Extensive results on both synthetic and real-recorded test set show its superiority over data-driven approaches in terms of noise robustness and temporal speech coherence.

</details>

### [Vec-Tok Speech: speech vectorization and tokenization for neural speech generation](2310.07246.md)
**Xinfa Zhu et.al.** · 2023-10-12

### [Crowdsourced and Automatic Speech Prominence Estimation](2310.08464.md)
**Max Morrison, Pranav Pawar, Nathan Pruyne, Jennifer Cole et al.** · 2023-10-12

<details>
<summary>Abstract</summary>

The prominence of a spoken word is the degree to which an average native listener perceives the word as salient or emphasized relative to its context. Speech prominence estimation is the process of assigning a numeric value to the prominence of each word in an utterance. These prominence labels are useful for linguistic analysis, as well as training automated systems to perform emphasis-controlled text-to-speech or emotion recognition. Manually annotating prominence is time-consuming and expensive, which motivates the development of automated methods for speech prominence estimation. However, developing such an automated system using machine-learning methods requires human-annotated training data. Using our system for acquiring such human annotations, we collect and open-source crowdsourced annotations of a portion of the LibriTTS dataset. We use these annotations as ground truth to train a neural speech prominence estimator that generalizes to unseen speakers, datasets, and speaking styles. We investigate design decisions for neural prominence estimation as well as how neural prominence estimation improves as a function of two key factors of annotation cost: dataset size and the number of annotations per utterance.

</details>

### [Voice Conversion for Stuttered Speech, Instruments, Unseen Languages and Textually Described Voices](2310.08104.md)
**Matthew Baas, Herman Kamper** · 2023-10-12

<details>
<summary>Abstract</summary>

Voice conversion aims to convert source speech into a target voice using recordings of the target speaker as a reference. Newer models are producing increasingly realistic output. But what happens when models are fed with non-standard data, such as speech from a user with a speech impairment? We investigate how a recent voice conversion model performs on non-standard downstream voice conversion tasks. We use a simple but robust approach called k-nearest neighbors voice conversion (kNN-VC). We look at four non-standard applications: stuttered voice conversion, cross-lingual voice conversion, musical instrument conversion, and text-to-voice conversion. The latter involves converting to a target voice specified through a text description, e.g. "a young man with a high-pitched voice". Compared to an established baseline, we find that kNN-VC retains high performance in stuttered and cross-lingual voice conversion. Results are more mixed for the musical instrument and text-to-voice conversion tasks. E.g., kNN-VC works well on some instruments like drums but not on others. Nevertheless, this shows that voice conversion models - and kNN-VC in particular - are increasingly applicable in a range of non-standard downstream tasks. But there are still limitations when samples are very far from the training distribution. Code, samples, trained models: https://rf5.github.io/sacair2023-knnvc-demo/.

</details>

### [Prosody Analysis of Audiobooks](2310.06930.md)
**Charuta Pethe, Bach Pham, Felix D Childress, Yunting Yin et al.** · 2023-10-10

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech have made it possible to generate natural-sounding audio from text. However, audiobook narrations involve dramatic vocalizations and intonations by the reader, with greater reliance on emotions, dialogues, and descriptions in the narrative. Using our dataset of 93 aligned book-audiobook pairs, we present improved models for prosody prediction properties (pitch, volume, and rate of speech) from narrative text using language modeling. Our predicted prosody attributes correlate much better with human audiobook readings than results from a state-of-the-art commercial TTS system: our predicted pitch shows a higher correlation with human reading for 22 out of the 24 books, while our predicted volume attribute proves more similar to human reading for 23 out of the 24 books. Finally, we present a human evaluation study to quantify the extent that people prefer prosody-enhanced audiobook readings over commercial text-to-speech systems.

</details>

### [AutoCycle-VC: Towards Bottleneck-Independent Zero-Shot Cross-Lingual Voice Conversion](2310.06546.md)
**Haeyun Choi, Jio Gim, Yuho Lee, Youngin Kim et al.** · 2023-10-10

<details>
<summary>Abstract</summary>

This paper proposes a simple and robust zero-shot voice conversion system with a cycle structure and mel-spectrogram pre-processing. Previous works suffer from information loss and poor synthesis quality due to their reliance on a carefully designed bottleneck structure. Moreover, models relying solely on self-reconstruction loss struggled with reproducing different speakers' voices. To address these issues, we suggested a cycle-consistency loss that considers conversion back and forth between target and source speakers. Additionally, stacked random-shuffled mel-spectrograms and a label smoothing method are utilized during speaker encoder training to extract a time-independent global speaker representation from speech, which is the key to a zero-shot conversion. Our model outperforms existing state-of-the-art results in both subjective and objective evaluations. Furthermore, it facilitates cross-lingual voice conversions and enhances the quality of synthesized speech.

</details>

### [JVNV: A Corpus of Japanese Emotional Speech with Verbal Content and Nonverbal Expressions](2310.06072.md)
**Detai Xin, Junfeng Jiang, Shinnosuke Takamichi, Yuki Saito et al.** · 2023-10-09

<details>
<summary>Abstract</summary>

We present the JVNV, a Japanese emotional speech corpus with verbal content and nonverbal vocalizations whose scripts are generated by a large-scale language model. Existing emotional speech corpora lack not only proper emotional scripts but also nonverbal vocalizations (NVs) that are essential expressions in spoken language to express emotions. We propose an automatic script generation method to produce emotional scripts by providing seed words with sentiment polarity and phrases of nonverbal vocalizations to ChatGPT using prompt engineering. We select 514 scripts with balanced phoneme coverage from the generated candidate scripts with the assistance of emotion confidence scores and language fluency scores. We demonstrate the effectiveness of JVNV by showing that JVNV has better phoneme coverage and emotion recognizability than previous Japanese emotional speech corpora. We then benchmark JVNV on emotional text-to-speech synthesis using discrete codes to represent NVs. We show that there still exists a gap between the performance of synthesizing read-aloud speech and emotional speech, and adding NVs in the speech makes the task even harder, which brings new challenges for this task and makes JVNV a valuable resource for relevant works in the future. To our best knowledge, JVNV is the first speech corpus that generates scripts automatically using large language models.

</details>

### [SHAP-based Prediction of Mother’s History of Depression to Understand the Influence on Child Behavior](s2:6838c43e702a3f995967ba2e3edd5f65ff5f5511.md)
**Maneesh Bilalpur, Saurabh Hinduja, Laura A. Cariola, L. Sheeber et al.** · 2023-10-09

<details>
<summary>Abstract</summary>

Depression strongly impacts parents’ behavior. Does parents’ depression strongly affect the behavior of their children as well? To investigate this question, we compared dyadic interactions between 73 depressed and 75 non-depressed mothers and their adolescent child. Families were of low income and 84% were white. Child behavior was measured from audio-video recordings using manual annotation of verbal and nonverbal behavior by expert coders and by multimodal computational measures of facial expression, face and head dynamics, prosody, speech behavior, and linguistics. For both sets of measures, we used Support Vector Machines. For computational measures, we investigated the relative contribution of single versus multiple modalities using a novel approach to SHapley Additive exPlanations (SHAP). Computational measures outperformed manual ratings by human experts. Among individual computational measures, prosody was the most informative. SHAP reduction resulted in a four-fold decrease in the number of features and highest performance (77% accuracy; positive and negative agreements at 75% and 76%, respectively). These findings suggest that maternal depression strongly impacts the behavior of adolescent children; differences are most revealed in prosody; multimodal features together with SHAP reduction are most powerful.

</details>

### [Comparative Analysis of Transfer Learning in Deep Learning Text-to-Speech Models on a Few-Shot, Low-Resource, Customized Dataset](2310.04982.md)
**Ze Liu et.al.** · 2023-10-08

### [Unified speech and gesture synthesis using flow matching](2310.05181.md)
**Shivam Mehta, Ruibo Tu, Simon Alexanderson, Jonas Beskow et al.** · 2023-10-08

<details>
<summary>Abstract</summary>

As text-to-speech technologies achieve remarkable naturalness in read-aloud tasks, there is growing interest in multimodal synthesis of verbal and non-verbal communicative behaviour, such as spontaneous speech and associated body gestures. This paper presents a novel, unified architecture for jointly synthesising speech acoustics and skeleton-based 3D gesture motion from text, trained using optimal-transport conditional flow matching (OT-CFM). The proposed architecture is simpler than the previous state of the art, has a smaller memory footprint, and can capture the joint distribution of speech and gestures, generating both modalities together in one single process. The new training regime, meanwhile, enables better synthesis quality in much fewer steps (network evaluations) than before. Uni- and multimodal subjective tests demonstrate improved speech naturalness, gesture human-likeness, and cross-modal appropriateness compared to existing benchmarks. Please see https://shivammehta25.github.io/Match-TTSG/ for video examples and code.

</details>

### [Partial Rank Similarity Minimization Method for Quality MOS Prediction of Unseen Speech Synthesis Systems in Zero-Shot and Semi-supervised setting](2310.05078.md)
**Hemant Yadav, Erica Cooper, Junichi Yamagishi, Sunayana Sitaram et al.** · 2023-10-08

<details>
<summary>Abstract</summary>

This paper introduces a novel objective function for quality mean opinion score (MOS) prediction of unseen speech synthesis systems. The proposed function measures the similarity of relative positions of predicted MOS values, in a mini-batch, rather than the actual MOS values. That is the partial rank similarity is measured (PRS) rather than the individual MOS values as with the L1 loss. Our experiments on out-of-domain speech synthesis systems demonstrate that the PRS outperforms L1 loss in zero-shot and semi-supervised settings, exhibiting stronger correlation with ground truth. These findings highlight the importance of considering rank order, as done by PRS, when training MOS prediction models. We also argue that mean squared error and linear correlation coefficient metrics may be unreliable for evaluating MOS prediction models. In conclusion, PRS-trained models provide a robust framework for evaluating speech quality and offer insights for developing high-quality speech synthesis systems. Code and models are available at github.com/nii-yamagishilab/partial_rank_similarity/

</details>

### [A Comparative Study of Voice Conversion Models with Large-Scale Speech and Singing Data: The T13 Systems for the Singing Voice Conversion Challenge 2023](2310.05203.md)
**Ryuichi Yamamoto, Reo Yoneyama, Lester Phillip Violeta, Wen-Chin Huang et al.** · 2023-10-08

<details>
<summary>Abstract</summary>

This paper presents our systems (denoted as T13) for the singing voice conversion challenge (SVCC) 2023. For both in-domain and cross-domain English singing voice conversion (SVC) tasks (Task 1 and Task 2), we adopt a recognition-synthesis approach with self-supervised learning-based representation. To achieve data-efficient SVC with a limited amount of target singer/speaker's data (150 to 160 utterances for SVCC 2023), we first train a diffusion-based any-to-any voice conversion model using publicly available large-scale 750 hours of speech and singing data. Then, we finetune the model for each target singer/speaker of Task 1 and Task 2. Large-scale listening tests conducted by SVCC 2023 show that our T13 system achieves competitive naturalness and speaker similarity for the harder cross-domain SVC (Task 2), which implies the generalization ability of our proposed method. Our objective evaluation results show that using large datasets is particularly beneficial for cross-domain SVC.

</details>

### [VITS-based Singing Voice Conversion System with DSPGAN post-processing for SVCC2023](2310.05118.md)
**Yiquan Zhou, Meng Chen, Yi Lei, Jihua Zhu et al.** · 2023-10-08

<details>
<summary>Abstract</summary>

This paper presents the T02 team's system for the Singing Voice Conversion Challenge 2023 (SVCC2023). Our system entails a VITS-based SVC model, incorporating three modules: a feature extractor, a voice converter, and a post-processor. Specifically, the feature extractor provides F0 contours and extracts speaker-independent linguistic content from the input singing voice by leveraging a HuBERT model. The voice converter is employed to recompose the speaker timbre, F0, and linguistic content to generate the waveform of the target speaker. Besides, to further improve the audio quality, a fine-tuned DSPGAN vocoder is introduced to re-synthesise the waveform. Given the limited target speaker data, we utilize a two-stage training strategy to adapt the base model to the target speaker. During model adaptation, several tricks, such as data augmentation and joint training with auxiliary singer data, are involved. Official challenge results show that our system achieves superior performance, especially in the cross-domain task, ranking 1st and 2nd in naturalness and similarity, respectively. Further ablation justifies the effectiveness of our system design.

</details>

### [HiGNN-TTS: Hierarchical Prosody Modeling with Graph Neural Networks for Expressive Long-form TTS](2309.13907.md)
**Dake Guo et.al.** · 2023-10-07

### [FunCodec: A Fundamental, Reproducible and Integrable Open-source Toolkit for Neural Speech Codec](2309.07405.md)
**Zhihao Du et.al.** · 2023-10-07

### [Zero-Shot Emotion Transfer For Cross-Lingual Speech Synthesis](2310.03963.md)
**Yuke Li, Xinfa Zhu, Yi Lei, Hai Li et al.** · 2023-10-06

<details>
<summary>Abstract</summary>

Zero-shot emotion transfer in cross-lingual speech synthesis aims to transfer emotion from an arbitrary speech reference in the source language to the synthetic speech in the target language. Building such a system faces challenges of unnatural foreign accents and difficulty in modeling the shared emotional expressions of different languages. Building on the DelightfulTTS neural architecture, this paper addresses these challenges by introducing specifically-designed modules to model the language-specific prosody features and language-shared emotional expressions separately. Specifically, the language-specific speech prosody is learned by a non-autoregressive predictive coding (NPC) module to improve the naturalness of the synthetic cross-lingual speech. The shared emotional expression between different languages is extracted from a pre-trained self-supervised model HuBERT with strong generalization capabilities. We further use hierarchical emotion modeling to capture more comprehensive emotions across different languages. Experimental results demonstrate the proposed framework's effectiveness in synthesizing bi-lingual emotional speech for the monolingual target speaker without emotional training data.

</details>

### [U-Style: Cascading U-nets with Multi-level Speaker and Style Modeling for Zero-Shot Voice Cloning](2310.04004.md)
**Tao Li, Zhichao Wang, Xinfa Zhu, Jian Cong et al.** · 2023-10-06

<details>
<summary>Abstract</summary>

Zero-shot speaker cloning aims to synthesize speech for any target speaker unseen during TTS system building, given only a single speech reference of the speaker at hand. Although more practical in real applications, the current zero-shot methods still produce speech with undesirable naturalness and speaker similarity. Moreover, endowing the target speaker with arbitrary speaking styles in the zero-shot setup has not been considered. This is because the unique challenge of zero-shot speaker and style cloning is to learn the disentangled speaker and style representations from only short references representing an arbitrary speaker and an arbitrary style. To address this challenge, we propose U-Style, which employs Grad-TTS as the backbone, particularly cascading a speaker-specific encoder and a style-specific encoder between the text encoder and the diffusion decoder. Thus, leveraging signal perturbation, U-Style is explicitly decomposed into speaker- and style-specific modeling parts, achieving better speaker and style disentanglement. To improve unseen speaker and style modeling ability, these two encoders conduct multi-level speaker and style modeling by skip-connected U-nets, incorporating the representation extraction and information reconstruction process. Besides, to improve the naturalness of synthetic speech, we adopt mean-based instance normalization and style adaptive layer normalization in these encoders to perform representation extraction and condition adaptation, respectively. Experiments show that U-Style significantly surpasses the state-of-the-art methods in unseen speaker cloning regarding naturalness and speaker similarity. Notably, U-Style can transfer the style from an unseen source speaker to another unseen target speaker, achieving flexible combinations of desired speaker timbre and style in zero-shot voice cloning.

</details>

### [The VoiceMOS Challenge 2023: Zero-shot Subjective Speech Quality Prediction for Multiple Domains](2310.02640.md)
**Erica Cooper, Wen-Chin Huang, Yu Tsao, Hsin-Min Wang et al.** · 2023-10-04

<details>
<summary>Abstract</summary>

We present the second edition of the VoiceMOS Challenge, a scientific event that aims to promote the study of automatic prediction of the mean opinion score (MOS) of synthesized and processed speech. This year, we emphasize real-world and challenging zero-shot out-of-domain MOS prediction with three tracks for three different voice evaluation scenarios. Ten teams from industry and academia in seven different countries participated. Surprisingly, we found that the two sub-tracks of French text-to-speech synthesis had large differences in their predictability, and that singing voice-converted samples were not as difficult to predict as we had expected. Use of diverse datasets and listener information during training appeared to be successful approaches.

</details>

### [VITS-Based Singing Voice Conversion Leveraging Whisper and multi-scale F0 Modeling](2310.02802.md)
**Ziqian Ning, Yuepeng Jiang, Zhichao Wang, Bin Zhang et al.** · 2023-10-04

<details>
<summary>Abstract</summary>

This paper introduces the T23 team's system submitted to the Singing Voice Conversion Challenge 2023. Following the recognition-synthesis framework, our singing conversion model is based on VITS, incorporating four key modules: a prior encoder, a posterior encoder, a decoder, and a parallel bank of transposed convolutions (PBTC) module. We particularly leverage Whisper, a powerful pre-trained ASR model, to extract bottleneck features (BNF) as the input of the prior encoder. Before BNF extraction, we perform pitch perturbation to the source signal to remove speaker timbre, which effectively avoids the leakage of the source speaker timbre to the target. Moreover, the PBTC module extracts multi-scale F0 as the auxiliary input to the prior encoder, thereby capturing better pitch variations of singing. We design a three-stage training strategy to better adapt the base model to the target speaker with limited target speaker data. Official challenge results show that our system has superior performance in naturalness, ranking 1st and 2nd respectively in Task 1 and 2. Further ablation justifies the effectiveness of our system design.

</details>

### [Improving severity preservation of healthy-to-pathological voice conversion with global style tokens](2310.02570.md)
**Bence Mark Halpern, Wen-Chin Huang, Lester Phillip Violeta, R. J. J. H. van Son et al.** · 2023-10-04

<details>
<summary>Abstract</summary>

In healthy-to-pathological voice conversion (H2P-VC), healthy speech is converted into pathological while preserving the identity. The paper improves on previous two-stage approach to H2P-VC where (1) speech is created first with the appropriate severity, (2) then the speaker identity of the voice is converted while preserving the severity of the voice. Specifically, we propose improvements to (2) by using phonetic posteriorgrams (PPG) and global style tokens (GST). Furthermore, we present a new dataset that contains parallel recordings of pathological and healthy speakers with the same identity which allows more precise evaluation. Listening tests by expert listeners show that the framework preserves severity of the source sample, while modelling target speaker's voice. We also show that (a) pathology impacts x-vectors but not all speaker information is lost, (b) choosing source speakers based on severity labels alone is insufficient.

</details>

### [Soft Convex Quantization: Revisiting Vector Quantization with Convex Optimization](2310.03004.md)
**Tanmay Gautam, Reid Pryzant, Ziyi Yang, Chenguang Zhu et al.** · 2023-10-04

<details>
<summary>Abstract</summary>

Vector Quantization (VQ) is a well-known technique in deep learning for extracting informative discrete latent representations. VQ-embedded models have shown impressive results in a range of applications including image and speech generation. VQ operates as a parametric K-means algorithm that quantizes inputs using a single codebook vector in the forward pass. While powerful, this technique faces practical challenges including codebook collapse, non-differentiability and lossy compression. To mitigate the aforementioned issues, we propose Soft Convex Quantization (SCQ) as a direct substitute for VQ. SCQ works like a differentiable convex optimization (DCO) layer: in the forward pass, we solve for the optimal convex combination of codebook vectors that quantize the inputs. In the backward pass, we leverage differentiability through the optimality conditions of the forward solution. We then introduce a scalable relaxation of the SCQ optimization and demonstrate its efficacy on the CIFAR-10, GTSRB and LSUN datasets. We train powerful SCQ autoencoder models that significantly outperform matched VQ-based architectures, observing an order of magnitude better image reconstruction and codebook usage with comparable quantization runtime.

</details>

### [Towards human-like spoken dialogue generation between AI agents from written dialogue](2310.01088.md)
**Kentaro Mitsui, Yukiya Hono, Kei Sawada** · 2023-10-02

<details>
<summary>Abstract</summary>

The advent of large language models (LLMs) has made it possible to generate natural written dialogues between two agents. However, generating human-like spoken dialogues from these written dialogues remains challenging. Spoken dialogues have several unique characteristics: they frequently include backchannels and laughter, and the smoothness of turn-taking significantly influences the fluidity of conversation. This study proposes CHATS - CHatty Agents Text-to-Speech - a discrete token-based system designed to generate spoken dialogues based on written dialogues. Our system can generate speech for both the speaker side and the listener side simultaneously, using only the transcription from the speaker side, which eliminates the need for transcriptions of backchannels or laughter. Moreover, CHATS facilitates natural turn-taking; it determines the appropriate duration of silence after each utterance in the absence of overlap, and it initiates the generation of overlapping speech based on the phoneme sequence of the next utterance in case of overlap. Experimental evaluations indicate that CHATS outperforms the text-to-speech baseline, producing spoken dialogues that are more interactive and fluid while retaining clarity and intelligibility.

</details>

### [DiffAR: Denoising Diffusion Autoregressive Model for Raw Speech Waveform Generation](2310.01381.md)
**Roi Benita, Michael Elad, Joseph Keshet** · 2023-10-02

<details>
<summary>Abstract</summary>

Diffusion models have recently been shown to be relevant for high-quality speech generation. Most work has been focused on generating spectrograms, and as such, they further require a subsequent model to convert the spectrogram to a waveform (i.e., a vocoder). This work proposes a diffusion probabilistic end-to-end model for generating a raw speech waveform. The proposed model is autoregressive, generating overlapping frames sequentially, where each frame is conditioned on a portion of the previously generated one. Hence, our model can effectively synthesize an unlimited speech duration while preserving high-fidelity synthesis and temporal coherence. We implemented the proposed model for unconditional and conditional speech generation, where the latter can be driven by an input sequence of phonemes, amplitudes, and pitch values. Working on the waveform directly has some empirical advantages. Specifically, it allows the creation of local acoustic behaviors, like vocal fry, which makes the overall waveform sounds more natural. Furthermore, the proposed diffusion model is stochastic and not deterministic; therefore, each inference generates a slightly different waveform variation, enabling abundance of valid realizations. Experiments show that the proposed model generates speech with superior quality compared with other state-of-the-art neural speech generation systems.

</details>

### [Evaluating Speech Synthesis by Training Recognizers on Synthetic Speech](2310.00706.md)
**Dareen Alharthi et.al.** · 2023-10-01

### [The limits of the Mean Opinion Score for speech synthesis evaluation](s2:009d0132d9457493f978b79ab187774ecba81689.md)
**Sébastien Le Maguer, Simon King, Naomi Harte** · 2023-10-01

<details>
<summary>Abstract</summary>

The release of WaveNet and Tacotron has forever transformed the speech synthesis landscape. Thanks to these game-changing innovations, the quality of synthetic speech has reached unprecedented levels. However, to measure this leap in quality, an overwhelming majority of studies still rely on the Absolute Category Rating (ACR) protocol and compare systems using its output; the Mean Opinion Score (MOS). This protocol is not without controversy, and as the current state-of-the-art synthesis systems now produce outputs remarkably close to human speech, it is now vital to determine how reliable this score is. To do so, we conducted a series of four experiments replicating and following the 2013 edition of the Blizzard Challenge. With these experiments, we asked four questions about the MOS: How stable is the MOS of a system across time? How do the scores of lower quality systems influence the MOS of higher quality systems? How does the introduction of modern technologies influence the scores of past systems? How does the MOS of modern technologies evolve in isolation? The results of our experiments are manyfold. Firstly, we verify the superiority of modern technologies in comparison to historical synthesis. Then, we show that despite its origin as an absolute category rating, MOS is a relative score. While minimal variations are observed during the replication of the 2013-EH2 task, these variations can still lead to di ff erent conclusions for the intermediate systems. Our experiments also illustrate the sensitivity of MOS to the presence / absence of lower and higher anchors. Overall, our experiments suggest that we may have reached the end of a cul-de-sac by only evaluating the overall quality with MOS. We must embark on a new road and develop di ff erent evaluation protocols better suited to the analysis of modern speech synthesis technologies.

</details>

### [Diffusion-Based Mel-Spectrogram Enhancement for Personalized Speech Synthesis with Found Data](2305.10891.md)
**Yusheng Tian et.al.** · 2023-09-30

### [Low-Resource Self-Supervised Learning with SSL-Enhanced TTS](2309.17020.md)
**Po-chun Hsu et.al.** · 2023-09-29

### [Synthetic Speech Detection Based on Temporal Consistency and Distribution of Speaker Features](2309.16954.md)
**Yuxiang Zhang, Zhuo Li, Jingze Lu, Wenchao Wang et al.** · 2023-09-29

<details>
<summary>Abstract</summary>

Current synthetic speech detection (SSD) methods perform well on certain datasets but still face issues of robustness and interpretability. A possible reason is that these methods do not analyze the deficiencies of synthetic speech. In this paper, the flaws of the speaker features inherent in the text-to-speech (TTS) process are analyzed. Differences in the temporal consistency of intra-utterance speaker features arise due to the lack of fine-grained control over speaker features in TTS. Since the speaker representations in TTS are based on speaker embeddings extracted by encoders, the distribution of inter-utterance speaker features differs between synthetic and bonafide speech. Based on these analyzes, an SSD method based on temporal consistency and distribution of speaker features is proposed. On one hand, modeling the temporal consistency of intra-utterance speaker features can aid speech anti-spoofing. On the other hand, distribution differences in inter-utterance speaker features can be utilized for SSD. The proposed method offers low computational complexity and performs well in both cross-dataset and silence trimming scenarios.

</details>

### [Mega-TTS 2: Zero-Shot Text-to-Speech with Arbitrary Length Speech Prompts](2307.07218.md)
**Ziyue Jiang et.al.** · 2023-09-28

### [NOMAD: Unsupervised Learning of Perceptual Embeddings for Speech Enhancement and Non-matching Reference Audio Quality Assessment](2309.16284.md)
**Alessandro Ragano, Jan Skoglund, Andrew Hines** · 2023-09-28

<details>
<summary>Abstract</summary>

This paper presents NOMAD (Non-Matching Audio Distance), a differentiable perceptual similarity metric that measures the distance of a degraded signal against non-matching references. The proposed method is based on learning deep feature embeddings via a triplet loss guided by the Neurogram Similarity Index Measure (NSIM) to capture degradation intensity. During inference, the similarity score between any two audio samples is computed through Euclidean distance of their embeddings. NOMAD is fully unsupervised and can be used in general perceptual audio tasks for audio analysis e.g. quality assessment and generative tasks such as speech enhancement and speech synthesis. The proposed method is evaluated with 3 tasks. Ranking degradation intensity, predicting speech quality, and as a loss function for speech enhancement. Results indicate NOMAD outperforms other non-matching reference approaches in both ranking degradation intensity and quality assessment, exhibiting competitive performance with full-reference audio metrics. NOMAD demonstrates a promising technique that mimics human capabilities in assessing audio quality with non-matching references to learn perceptual embeddings without the need for human-generated labels.

</details>

### [DualVC 2: Dynamic Masked Convolution for Unified Streaming and Non-Streaming Voice Conversion](2309.15496.md)
**Ziqian Ning, Yuepeng Jiang, Pengcheng Zhu, Shuai Wang et al.** · 2023-09-27

<details>
<summary>Abstract</summary>

Voice conversion is becoming increasingly popular, and a growing number of application scenarios require models with streaming inference capabilities. The recently proposed DualVC attempts to achieve this objective through streaming model architecture design and intra-model knowledge distillation along with hybrid predictive coding to compensate for the lack of future information. However, DualVC encounters several problems that limit its performance. First, the autoregressive decoder has error accumulation in its nature and limits the inference speed as well. Second, the causal convolution enables streaming capability but cannot sufficiently use future information within chunks. Third, the model is unable to effectively address the noise in the unvoiced segments, lowering the sound quality. In this paper, we propose DualVC 2 to address these issues. Specifically, the model backbone is migrated to a Conformer-based architecture, empowering parallel inference. Causal convolution is replaced by non-causal convolution with dynamic chunk mask to make better use of within-chunk future information. Also, quiet attention is introduced to enhance the model's noise robustness. Experiments show that DualVC 2 outperforms DualVC and other baseline systems in both subjective and objective metrics, with only 186.4 ms latency. Our audio samples are made publicly available.

</details>

### [Face-StyleSpeech: Improved Face-to-Voice latent mapping for Natural Zero-shot Speech Synthesis from a Face Image](2311.05844.md)
**Minki Kang et.al.** · 2023-09-25

### [BiSinger: Bilingual Singing Voice Synthesis](2309.14089.md)
**Huali Zhou, Yueqian Lin, Yao Shi, Peng Sun et al.** · 2023-09-25

<details>
<summary>Abstract</summary>

Although Singing Voice Synthesis (SVS) has made great strides with Text-to-Speech (TTS) techniques, multilingual singing voice modeling remains relatively unexplored. This paper presents BiSinger, a bilingual pop SVS system for English and Chinese Mandarin. Current systems require separate models per language and cannot accurately represent both Chinese and English, hindering code-switch SVS. To address this gap, we design a shared representation between Chinese and English singing voices, achieved by using the CMU dictionary with mapping rules. We fuse monolingual singing datasets with open-source singing voice conversion techniques to generate bilingual singing voices while also exploring the potential use of bilingual speech data. Experiments affirm that our language-independent representation and incorporation of related datasets enable a single model with enhanced performance in English and code-switch SVS while maintaining Chinese song performance. Audio samples are available at https://bisinger-svs.github.io.

</details>

### [VoiceLens: Controllable Speaker Generation and Editing with Flow](2309.14094.md)
**Yao Shi, Ming Li** · 2023-09-25

<details>
<summary>Abstract</summary>

Currently, many multi-speaker speech synthesis and voice conversion systems address speaker variations with an embedding vector. Modeling it directly allows new voices outside of training data to be synthesized. GMM based approaches such as Tacospawn are favored in literature for this generation task, but there are still some limitations when difficult conditionings are involved. In this paper, we propose VoiceLens, a semi-supervised flow-based approach, to model speaker embedding distributions for multi-conditional speaker generation. VoiceLens maps speaker embeddings into a combination of independent attributes and residual information. It allows new voices associated with certain attributes to be \textit{generated} for existing TTS models, and attributes of known voices to be meaningfully \textit{edited}. We show in this paper, VoiceLens displays an unconditional generation capacity that is similar to Tacospawn while obtaining higher controllability and flexibility when used in a conditional manner. In addition, we show synthesizing less noisy speech from known noisy speakers without re-training the TTS model is possible via solely editing their embeddings with a SNR conditioned VoiceLens model. Demos are available at sos1sos2sixteen.github.io/voicelens.

</details>

### [Towards General-Purpose Text-Instruction-Guided Voice Conversion](2309.14324.md)
**Chun-Yi Kuan, Chen An Li, Tsu-Yuan Hsu, Tse-Yang Lin et al.** · 2023-09-25

<details>
<summary>Abstract</summary>

This paper introduces a novel voice conversion (VC) model, guided by text instructions such as "articulate slowly with a deep tone" or "speak in a cheerful boyish voice". Unlike traditional methods that rely on reference utterances to determine the attributes of the converted speech, our model adds versatility and specificity to voice conversion. The proposed VC model is a neural codec language model which processes a sequence of discrete codes, resulting in the code sequence of converted speech. It utilizes text instructions as style prompts to modify the prosody and emotional information of the given speech. In contrast to previous approaches, which often rely on employing separate encoders like prosody and content encoders to handle different aspects of the source speech, our model handles various information of speech in an end-to-end manner. Experiments have demonstrated the impressive capabilities of our model in comprehending instructions and delivering reasonable results.

</details>

### [VoiceLDM: Text-to-Speech with Environmental Context](2309.13664.md)
**Yeonghyeon Lee, Inmo Yeon, Juhan Nam, Joon Son Chung** · 2023-09-24

<details>
<summary>Abstract</summary>

This paper presents VoiceLDM, a model designed to produce audio that accurately follows two distinct natural language text prompts: the description prompt and the content prompt. The former provides information about the overall environmental context of the audio, while the latter conveys the linguistic content. To achieve this, we adopt a text-to-audio (TTA) model based on latent diffusion models and extend its functionality to incorporate an additional content prompt as a conditional input. By utilizing pretrained contrastive language-audio pretraining (CLAP) and Whisper, VoiceLDM is trained on large amounts of real-world audio without manual annotations or transcriptions. Additionally, we employ dual classifier-free guidance to further enhance the controllability of VoiceLDM. Experimental results demonstrate that VoiceLDM is capable of generating plausible audio that aligns well with both input conditions, even surpassing the speech intelligibility of the ground truth audio on the AudioCaps test set. Furthermore, we explore the text-to-speech (TTS) and zero-shot text-to-audio capabilities of VoiceLDM and show that it achieves competitive results. Demos and code are available at https://voiceldm.github.io.

</details>

### [Coco-Nut: Corpus of Japanese Utterance and Voice Characteristics Description for Prompt-based Control](2309.13509.md)
**Aya Watanabe, Shinnosuke Takamichi, Yuki Saito, Wataru Nakata et al.** · 2023-09-24

<details>
<summary>Abstract</summary>

In text-to-speech, controlling voice characteristics is important in achieving various-purpose speech synthesis. Considering the success of text-conditioned generation, such as text-to-image, free-form text instruction should be useful for intuitive and complicated control of voice characteristics. A sufficiently large corpus of high-quality and diverse voice samples with corresponding free-form descriptions can advance such control research. However, neither an open corpus nor a scalable method is currently available. To this end, we develop Coco-Nut, a new corpus including diverse Japanese utterances, along with text transcriptions and free-form voice characteristics descriptions. Our methodology to construct this corpus consists of 1) automatic collection of voice-related audio data from the Internet, 2) quality assurance, and 3) manual annotation using crowdsourcing. Additionally, we benchmark our corpus on the prompt embedding model trained by contrastive speech-text learning.

</details>

### [DurIAN-E: Duration Informed Attention Network For Expressive Text-to-Speech Synthesis](2309.12792.md)
**Yu Gu et.al.** · 2023-09-22

### [Improving Language Model-Based Zero-Shot Text-to-Speech Synthesis with Multi-Scale Acoustic Prompts](2309.11977.md)
**Shun Lei et.al.** · 2023-09-22

### [The Impact of Silence on Speech Anti-Spoofing](2309.11827.md)
**Yuxiang Zhang, Zhuo Li, Jingze Lu, Hua Hua et al.** · 2023-09-21

<details>
<summary>Abstract</summary>

The current speech anti-spoofing countermeasures (CMs) show excellent performance on specific datasets. However, removing the silence of test speech through Voice Activity Detection (VAD) can severely degrade performance. In this paper, the impact of silence on speech anti-spoofing is analyzed. First, the reasons for the impact are explored, including the proportion of silence duration and the content of silence. The proportion of silence duration in spoof speech generated by text-to-speech (TTS) algorithms is lower than that in bonafide speech. And the content of silence generated by different waveform generators varies compared to bonafide speech. Then the impact of silence on model prediction is explored. Even after retraining, the spoof speech generated by neural network based end-to-end TTS algorithms suffers a significant rise in error rates when the silence is removed. To demonstrate the reasons for the impact of silence on CMs, the attention distribution of a CM is visualized through class activation mapping (CAM). Furthermore, the implementation and analysis of the experiments masking silence or non-silence demonstrates the significance of the proportion of silence duration for detecting TTS and the importance of silence content for detecting voice conversion (VC). Based on the experimental results, improving the robustness of CMs against unknown spoofing attacks by masking silence is also proposed. Finally, the attacks on anti-spoofing CMs through concatenating silence, and the mitigation of VAD and silence attack through low-pass filtering are introduced.

</details>

### [FluentEditor: Text-based Speech Editing by Considering Acoustic and Prosody Consistency](2309.11725.md)
**Rui Liu, Jiatian Xi, Ziyue Jiang, Haizhou Li** · 2023-09-21

<details>
<summary>Abstract</summary>

Text-based speech editing (TSE) techniques are designed to enable users to edit the output audio by modifying the input text transcript instead of the audio itself. Despite much progress in neural network-based TSE techniques, the current techniques have focused on reducing the difference between the generated speech segment and the reference target in the editing region, ignoring its local and global fluency in the context and original utterance. To maintain the speech fluency, we propose a fluency speech editing model, termed \textit{FluentEditor}, by considering fluency-aware training criterion in the TSE training. Specifically, the \textit{acoustic consistency constraint} aims to smooth the transition between the edited region and its neighboring acoustic segments consistent with the ground truth, while the \textit{prosody consistency constraint} seeks to ensure that the prosody attributes within the edited regions remain consistent with the overall style of the original utterance. The subjective and objective experimental results on VCTK demonstrate that our \textit{FluentEditor} outperforms all advanced baselines in terms of naturalness and fluency. The audio samples and code are available at \url{https://github.com/Ai-S2-Lab/FluentEditor}.

</details>

### [Emotion-Aware Prosodic Phrasing for Expressive Text-to-Speech](2309.11724.md)
**Rui Liu, Bin Liu, Haizhou Li** · 2023-09-21

<details>
<summary>Abstract</summary>

Prosodic phrasing is crucial to the naturalness and intelligibility of end-to-end Text-to-Speech (TTS). There exist both linguistic and emotional prosody in natural speech. As the study of prosodic phrasing has been linguistically motivated, prosodic phrasing for expressive emotion rendering has not been well studied. In this paper, we propose an emotion-aware prosodic phrasing model, termed \textit{EmoPP}, to mine the emotional cues of utterance accurately and predict appropriate phrase breaks. We first conduct objective observations on the ESD dataset to validate the strong correlation between emotion and prosodic phrasing. Then the objective and subjective evaluations show that the EmoPP outperforms all baselines and achieves remarkable performance in terms of emotion expressiveness. The audio samples and the code are available at \url{https://github.com/AI-S2-Lab/EmoPP}.

</details>

### [A Discourse-level Multi-scale Prosodic Model for Fine-grained Emotion Analysis](2309.11849.md)
**Xianhao Wei, Jia Jia, Xiang Li, Zhiyong Wu et al.** · 2023-09-21

<details>
<summary>Abstract</summary>

This paper explores predicting suitable prosodic features for fine-grained emotion analysis from the discourse-level text. To obtain fine-grained emotional prosodic features as predictive values for our model, we extract a phoneme-level Local Prosody Embedding sequence (LPEs) and a Global Style Embedding as prosodic speech features from the speech with the help of a style transfer model. We propose a Discourse-level Multi-scale text Prosodic Model (D-MPM) that exploits multi-scale text to predict these two prosodic features. The proposed model can be used to analyze better emotional prosodic features and thus guide the speech synthesis model to synthesize more expressive speech. To quantitatively evaluate the proposed model, we contribute a new and large-scale Discourse-level Chinese Audiobook (DCA) dataset with more than 13,000 utterances annotated sequences to evaluate the proposed model. Experimental results on the DCA dataset show that the multi-scale text information effectively helps to predict prosodic features, and the discourse-level text improves both the overall coherence and the user experience. More interestingly, although we aim at the synthesis effect of the style transfer model, the synthesized speech by the proposed text prosodic analysis model is even better than the style transfer from the original speech in some user evaluation indicators.

</details>

### [Towards Joint Modeling of Dialogue Response and Speech Synthesis based on Large Language Model](2309.11000.md)
**Xinyu Zhou et.al.** · 2023-09-20

### [Speak While You Think: Streaming Speech Synthesis During Text Generation](2309.11210.md)
**Avihu Dekel, Slava Shechtman, Raul Fernandez, David Haws et al.** · 2023-09-20

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) demonstrate impressive capabilities, yet interaction with these models is mostly facilitated through text. Using Text-To-Speech to synthesize LLM outputs typically results in notable latency, which is impractical for fluent voice conversations. We propose LLM2Speech, an architecture to synthesize speech while text is being generated by an LLM which yields significant latency reduction. LLM2Speech mimics the predictions of a non-streaming teacher model while limiting the exposure to future context in order to enable streaming. It exploits the hidden embeddings of the LLM, a by-product of the text generation that contains informative semantic context. Experimental results show that LLM2Speech maintains the teacher's quality while reducing the latency to enable natural conversations.

</details>

### [TRAVID: An End-to-End Video Translation Framework](2309.11338.md)
**Prottay Kumar Adhikary, Bandaru Sugandhi, Subhojit Ghimire, Santanu Pal et al.** · 2023-09-20

<details>
<summary>Abstract</summary>

In today's globalized world, effective communication with people from diverse linguistic backgrounds has become increasingly crucial. While traditional methods of language translation, such as written text or voice-only translations, can accomplish the task, they often fail to capture the complete context and nuanced information conveyed through nonverbal cues like facial expressions and lip movements. In this paper, we present an end-to-end video translation system that not only translates spoken language but also synchronizes the translated speech with the lip movements of the speaker. Our system focuses on translating educational lectures in various Indian languages, and it is designed to be effective even in low-resource system settings. By incorporating lip movements that align with the target language and matching them with the speaker's voice using voice cloning techniques, our application offers an enhanced experience for students and users. This additional feature creates a more immersive and realistic learning environment, ultimately making the learning process more effective and engaging.

</details>

### [Leveraging Speech PTM, Text LLM, and Emotional TTS for Speech Emotion Recognition](2309.10294.md)
**Ziyang Ma et.al.** · 2023-09-19

### [Speech Synthesis By Unrolling Diffusion Process using Neural Network Layers](2309.09652.md)
**Peter Ochieng** · 2023-09-18

<details>
<summary>Abstract</summary>

This work introduces UDPNet, a novel architecture designed to accelerate the reverse diffusion process in speech synthesis. Unlike traditional diffusion models that rely on timestep embeddings and shared network parameters, UDPNet unrolls the reverse diffusion process directly into the network architecture, with successive layers corresponding to equally spaced steps in the diffusion schedule. Each layer progressively refines the noisy input, culminating in a high-fidelity estimation of the original data, \(x_0\). Additionally, we redefine the learning target by predicting latent variables instead of the conventional \(x_0\) or noise \(ε_0\). This shift addresses the common issue of large prediction errors in early denoising stages, effectively reducing speech distortion. Extensive evaluations on single- and multi-speaker datasets demonstrate that UDPNet consistently outperforms state-of-the-art methods in both quality and efficiency, while generalizing effectively to unseen speech. These results position UDPNet as a robust solution for real-time speech synthesis applications. Sample audio is available at https://onexpeters.github.io/UDPNet.

</details>

### [HiFTNet: A Fast High-Quality Neural Vocoder with Harmonic-plus-Noise Filter and Inverse Short Time Fourier Transform](2309.09493.md)
**Yinghao Aaron Li, Cong Han, Xilin Jiang, Nima Mesgarani** · 2023-09-18

<details>
<summary>Abstract</summary>

Recent advancements in speech synthesis have leveraged GAN-based networks like HiFi-GAN and BigVGAN to produce high-fidelity waveforms from mel-spectrograms. However, these networks are computationally expensive and parameter-heavy. iSTFTNet addresses these limitations by integrating inverse short-time Fourier transform (iSTFT) into the network, achieving both speed and parameter efficiency. In this paper, we introduce an extension to iSTFTNet, termed HiFTNet, which incorporates a harmonic-plus-noise source filter in the time-frequency domain that uses a sinusoidal source from the fundamental frequency (F0) inferred via a pre-trained F0 estimation network for fast inference speed. Subjective evaluations on LJSpeech show that our model significantly outperforms both iSTFTNet and HiFi-GAN, achieving ground-truth-level performance. HiFTNet also outperforms BigVGAN-base on LibriTTS for unseen speakers and achieves comparable performance to BigVGAN while being four times faster with only $1/6$ of the parameters. Our work sets a new benchmark for efficient, high-quality neural vocoding, paving the way for real-time applications that demand high quality speech synthesis.

</details>

### [Face-Driven Zero-Shot Voice Conversion with Memory-based Face-Voice Alignment](2309.09470.md)
**Zheng-Yan Sheng, Yang Ai, Yan-Nian Chen, Zhen-Hua Ling** · 2023-09-18

<details>
<summary>Abstract</summary>

This paper presents a novel task, zero-shot voice conversion based on face images (zero-shot FaceVC), which aims at converting the voice characteristics of an utterance from any source speaker to a newly coming target speaker, solely relying on a single face image of the target speaker. To address this task, we propose a face-voice memory-based zero-shot FaceVC method. This method leverages a memory-based face-voice alignment module, in which slots act as the bridge to align these two modalities, allowing for the capture of voice characteristics from face images. A mixed supervision strategy is also introduced to mitigate the long-standing issue of the inconsistency between training and inference phases for voice conversion tasks. To obtain speaker-independent content-related representations, we transfer the knowledge from a pretrained zero-shot voice conversion model to our zero-shot FaceVC model. Considering the differences between FaceVC and traditional voice conversion tasks, systematic subjective and objective metrics are designed to thoroughly evaluate the homogeneity, diversity and consistency of voice characteristics controlled by face images. Through extensive experiments, we demonstrate the superiority of our proposed method on the zero-shot FaceVC task. Samples are presented on our demo website.

</details>

### [HiFi-WaveGAN: Generative Adversarial Network with Auxiliary Spectrogram-Phase Loss for High-Fidelity Singing Voice Generation](2210.12740.md)
**Chunhui Wang et.al.** · 2023-09-17

### [Augmenting text for spoken language understanding with Large Language Models](2309.09390.md)
**Roshan Sharma, Suyoun Kim, Daniel Lazar, Trang Le et al.** · 2023-09-17

<details>
<summary>Abstract</summary>

Spoken semantic parsing (SSP) involves generating machine-comprehensible parses from input speech. Training robust models for existing application domains represented in training data or extending to new domains requires corresponding triplets of speech-transcript-semantic parse data, which is expensive to obtain. In this paper, we address this challenge by examining methods that can use transcript-semantic parse data (unpaired text) without corresponding speech. First, when unpaired text is drawn from existing textual corpora, Joint Audio Text (JAT) and Text-to-Speech (TTS) are compared as ways to generate speech representations for unpaired text. Experiments on the STOP dataset show that unpaired text from existing and new domains improves performance by 2% and 30% in absolute Exact Match (EM) respectively. Second, we consider the setting when unpaired text is not available in existing textual corpora. We propose to prompt Large Language Models (LLMs) to generate unpaired text for existing and new domains. Experiments show that examples and words that co-occur with intents can be used to generate unpaired text with Llama 2.0. Using the generated text with JAT and TTS for spoken semantic parsing improves EM on STOP by 1.4% and 2.6% absolute for existing and new domains respectively.

</details>

### [PromptVC: Flexible Stylistic Voice Conversion in Latent Space Driven by Natural Language Prompts](2309.09262.md)
**Jixun Yao, Yuguang Yang, Yi Lei, Ziqian Ning et al.** · 2023-09-17

<details>
<summary>Abstract</summary>

Style voice conversion aims to transform the style of source speech to a desired style according to real-world application demands. However, the current style voice conversion approach relies on pre-defined labels or reference speech to control the conversion process, which leads to limitations in style diversity or falls short in terms of the intuitive and interpretability of style representation. In this study, we propose PromptVC, a novel style voice conversion approach that employs a latent diffusion model to generate a style vector driven by natural language prompts. Specifically, the style vector is extracted by a style encoder during training, and then the latent diffusion model is trained independently to sample the style vector from noise, with this process being conditioned on natural language prompts. To improve style expressiveness, we leverage HuBERT to extract discrete tokens and replace them with the K-Means center embedding to serve as the linguistic content, which minimizes residual style information. Additionally, we deduplicate the same discrete token and employ a differentiable duration predictor to re-predict the duration of each token, which can adapt the duration of the same linguistic content to different styles. The subjective and objective evaluation results demonstrate the effectiveness of our proposed system.

</details>

### [FastGraphTTS: An Ultrafast Syntax-Aware Speech Synthesis Framework](2309.08837.md)
**Jianzong Wang, Xulong Zhang, Aolan Sun, Ning Cheng et al.** · 2023-09-16

<details>
<summary>Abstract</summary>

This paper integrates graph-to-sequence into an end-to-end text-to-speech framework for syntax-aware modelling with syntactic information of input text. Specifically, the input text is parsed by a dependency parsing module to form a syntactic graph. The syntactic graph is then encoded by a graph encoder to extract the syntactic hidden information, which is concatenated with phoneme embedding and input to the alignment and flow-based decoding modules to generate the raw audio waveform. The model is experimented on two languages, English and Mandarin, using single-speaker, few samples of target speakers, and multi-speaker datasets, respectively. Experimental results show better prosodic consistency performance between input text and generated audio, and also get higher scores in the subjective prosodic evaluation, and show the ability of voice conversion. Besides, the efficiency of the model is largely boosted through the design of the AI chip operator with 5x acceleration.

</details>

### [Cross-lingual Knowledge Distillation via Flow-based Voice Conversion for Robust Polyglot Text-To-Speech](2309.08255.md)
**Dariusz Piotrowski, Renard Korzeniowski, Alessio Falai, Sebastian Cygert et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

In this work, we introduce a framework for cross-lingual speech synthesis, which involves an upstream Voice Conversion (VC) model and a downstream Text-To-Speech (TTS) model. The proposed framework consists of 4 stages. In the first two stages, we use a VC model to convert utterances in the target locale to the voice of the target speaker. In the third stage, the converted data is combined with the linguistic features and durations from recordings in the target language, which are then used to train a single-speaker acoustic model. Finally, the last stage entails the training of a locale-independent vocoder. Our evaluations show that the proposed paradigm outperforms state-of-the-art approaches which are based on training a large multilingual TTS model. In addition, our experiments demonstrate the robustness of our approach with different model architectures, languages, speakers and amounts of data. Moreover, our solution is especially beneficial in low-resource settings.

</details>

### [HM-Conformer: A Conformer-based audio deepfake detection system with hierarchical pooling and multi-level classification token aggregation methods](2309.08208.md)
**Hyun-seo Shin, Jungwoo Heo, Ju-ho Kim, Chan-yeong Lim et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

Audio deepfake detection (ADD) is the task of detecting spoofing attacks generated by text-to-speech or voice conversion systems. Spoofing evidence, which helps to distinguish between spoofed and bona-fide utterances, might exist either locally or globally in the input features. To capture these, the Conformer, which consists of Transformers and CNN, possesses a suitable structure. However, since the Conformer was designed for sequence-to-sequence tasks, its direct application to ADD tasks may be sub-optimal. To tackle this limitation, we propose HM-Conformer by adopting two components: (1) Hierarchical pooling method progressively reducing the sequence length to eliminate duplicated information (2) Multi-level classification token aggregation method utilizing classification tokens to gather information from different blocks. Owing to these components, HM-Conformer can efficiently detect spoofing evidence by processing various sequence lengths and aggregating them. In experimental results on the ASVspoof 2021 Deepfake dataset, HM-Conformer achieved a 15.71% EER, showing competitive performance compared to recent systems.

</details>

### [PromptTTS++: Controlling Speaker Identity in Prompt-Based Text-to-Speech Using Natural Language Descriptions](2309.08140.md)
**Reo Shimizu, Ryuichi Yamamoto, Masaya Kawamura, Yuma Shirahata et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

We propose PromptTTS++, a prompt-based text-to-speech (TTS) synthesis system that allows control over speaker identity using natural language descriptions. To control speaker identity within the prompt-based TTS framework, we introduce the concept of speaker prompt, which describes voice characteristics (e.g., gender-neutral, young, old, and muffled) designed to be approximately independent of speaking style. Since there is no large-scale dataset containing speaker prompts, we first construct a dataset based on the LibriTTS-R corpus with manually annotated speaker prompts. We then employ a diffusion-based acoustic model with mixture density networks to model diverse speaker factors in the training data. Unlike previous studies that rely on style prompts describing only a limited aspect of speaker individuality, such as pitch, speaking speed, and energy, our method utilizes an additional speaker prompt to effectively learn the mapping from natural language descriptions to the acoustic features of diverse speakers. Our subjective evaluation results show that the proposed method can better control speaker characteristics than the methods without the speaker prompt. Audio samples are available at https://reppy4620.github.io/demo.promptttspp/.

</details>

### [Diversity-based core-set selection for text-to-speech with linguistic and acoustic features](2309.08127.md)
**Kentaro Seki, Shinnosuke Takamichi, Takaaki Saeki, Hiroshi Saruwatari** · 2023-09-15

<details>
<summary>Abstract</summary>

This paper proposes a method for extracting a lightweight subset from a text-to-speech (TTS) corpus ensuring synthetic speech quality. In recent years, methods have been proposed for constructing large-scale TTS corpora by collecting diverse data from massive sources such as audiobooks and YouTube. Although these methods have gained significant attention for enhancing the expressive capabilities of TTS systems, they often prioritize collecting vast amounts of data without considering practical constraints like storage capacity and computation time in training, which limits the available data quantity. Consequently, the need arises to efficiently collect data within these volume constraints. To address this, we propose a method for selecting the core subset~(known as \textit{core-set}) from a TTS corpus on the basis of a \textit{diversity metric}, which measures the degree to which a subset encompasses a wide range. Experimental results demonstrate that our proposed method performs significantly better than the baseline phoneme-balanced data selection across language and corpus size.

</details>

### [Residual Speaker Representation for One-Shot Voice Conversion](2309.08166.md)
**Le Xu, Jiangyan Yi, Tao Wang, Yong Ren et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

Recently, there have been significant advancements in voice conversion, resulting in high-quality performance. However, there are still two critical challenges in this field. Firstly, current voice conversion methods have limited robustness when encountering unseen speakers. Secondly, they also have limited ability to control timbre representation. To address these challenges, this paper presents a novel approach that leverages tokens of multi-layer residual approximations to enhance robustness when dealing with unseen speakers, called the residual speaker module. Introducing multi-layer approximations facilitates the separation of information from the timbre, enabling effective control over timbre in voice conversion. The proposed method outperforms baselines in subjective and objective evaluations, demonstrating superior performance and increased robustness. Our demo page is publicly available.

</details>

### [Direct Text to Speech Translation System using Acoustic Units](2309.07478.md)
**Victoria Mingote, Pablo Gimeno, Luis Vicente, Sameer Khurana et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

This paper proposes a direct text to speech translation system using discrete acoustic units. This framework employs text in different source languages as input to generate speech in the target language without the need for text transcriptions in this language. Motivated by the success of acoustic units in previous works for direct speech to speech translation systems, we use the same pipeline to extract the acoustic units using a speech encoder combined with a clustering algorithm. Once units are obtained, an encoder-decoder architecture is trained to predict them. Then a vocoder generates speech from units. Our approach for direct text to speech translation was tested on the new CVSS corpus with two different text mBART models employed as initialisation. The systems presented report competitive performance for most of the language pairs evaluated. Besides, results show a remarkable improvement when initialising our proposed architecture with a model pre-trained with more languages.

</details>

### [SnakeGAN: A Universal Vocoder Leveraging DDSP Prior Knowledge and Periodic Inductive Bias](2309.07803.md)
**Sipan Li, Songxiang Liu, Luwen Zhang, Xiang Li et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Generative adversarial network (GAN)-based neural vocoders have been widely used in audio synthesis tasks due to their high generation quality, efficient inference, and small computation footprint. However, it is still challenging to train a universal vocoder which can generalize well to out-of-domain (OOD) scenarios, such as unseen speaking styles, non-speech vocalization, singing, and musical pieces. In this work, we propose SnakeGAN, a GAN-based universal vocoder, which can synthesize high-fidelity audio in various OOD scenarios. SnakeGAN takes a coarse-grained signal generated by a differentiable digital signal processing (DDSP) model as prior knowledge, aiming at recovering high-fidelity waveform from a Mel-spectrogram. We introduce periodic nonlinearities through the Snake activation function and anti-aliased representation into the generator, which further brings the desired inductive bias for audio synthesis and significantly improves the extrapolation capacity for universal vocoding in unseen scenarios. To validate the effectiveness of our proposed method, we train SnakeGAN with only speech data and evaluate its performance for various OOD distributions with both subjective and objective metrics. Experimental results show that SnakeGAN significantly outperforms the compared approaches and can generate high-fidelity audio samples including unseen speakers with unseen styles, singing voices, instrumental pieces, and nonverbal vocalization.

</details>

### [AAS-VC: On the Generalization Ability of Automatic Alignment Search based Non-autoregressive Sequence-to-sequence Voice Conversion](2309.07598.md)
**Wen-Chin Huang, Kazuhiro Kobayashi, Tomoki Toda** · 2023-09-14

<details>
<summary>Abstract</summary>

Non-autoregressive (non-AR) sequence-to-seqeunce (seq2seq) models for voice conversion (VC) is attractive in its ability to effectively model the temporal structure while enjoying boosted intelligibility and fast inference thanks to non-AR modeling. However, the dependency of current non-AR seq2seq VC models on ground truth durations extracted from an external AR model greatly limits its generalization ability to smaller training datasets. In this paper, we first demonstrate the above-mentioned problem by varying the training data size. Then, we present AAS-VC, a non-AR seq2seq VC model based on automatic alignment search (AAS), which removes the dependency on external durations and serves as a proper inductive bias to provide the required generalization ability for small datasets. Experimental results show that AAS-VC can generalize better to a training dataset of only 5 minutes. We also conducted ablation studies to justify several model design choices. The audio samples and implementation are available online.

</details>

### [StarGAN-VC++: Towards Emotion Preserving Voice Conversion Using Deep Embeddings](2309.07592.md)
**Arnab Das, Suhita Ghosh, Tim Polzehl, Sebastian Stober** · 2023-09-14

<details>
<summary>Abstract</summary>

Voice conversion (VC) transforms an utterance to sound like another person without changing the linguistic content. A recently proposed generative adversarial network-based VC method, StarGANv2-VC is very successful in generating natural-sounding conversions. However, the method fails to preserve the emotion of the source speaker in the converted samples. Emotion preservation is necessary for natural human-computer interaction. In this paper, we show that StarGANv2-VC fails to disentangle the speaker and emotion representations, pertinent to preserve emotion. Specifically, there is an emotion leakage from the reference audio used to capture the speaker embeddings while training. To counter the problem, we propose novel emotion-aware losses and an unsupervised method which exploits emotion supervision through latent emotion representations. The objective and subjective evaluations prove the efficacy of the proposed strategy over diverse datasets, emotions, gender, etc.

</details>

### [Emo-StarGAN: A Semi-Supervised Any-to-Many Non-Parallel Emotion-Preserving Voice Conversion](2309.07586.md)
**Suhita Ghosh, Arnab Das, Yamini Sinha, Ingo Siegert et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Speech anonymisation prevents misuse of spoken data by removing any personal identifier while preserving at least linguistic content. However, emotion preservation is crucial for natural human-computer interaction. The well-known voice conversion technique StarGANv2-VC achieves anonymisation but fails to preserve emotion. This work presents an any-to-many semi-supervised StarGANv2-VC variant trained on partially emotion-labelled non-parallel data. We propose emotion-aware losses computed on the emotion embeddings and acoustic features correlated to emotion. Additionally, we use an emotion classifier to provide direct emotion supervision. Objective and subjective evaluations show that the proposed approach significantly improves emotion preservation over the vanilla StarGANv2-VC. This considerable improvement is seen over diverse datasets, emotions, target speakers, and inter-group conversions without compromising intelligibility and anonymisation.

</details>

### [DCTTS: Discrete Diffusion Model with Contrastive Learning for Text-to-speech Generation](2309.06787.md)
**Zhichao Wu et.al.** · 2023-09-13

### [Distinguishing Neural Speech Synthesis Models Through Fingerprints in Speech Waveforms](2309.06780.md)
**Chu Yuan Zhang, Jiangyan Yi, Jianhua Tao, Chenglong Wang et al.** · 2023-09-13

<details>
<summary>Abstract</summary>

Recent strides in neural speech synthesis technologies, while enjoying widespread applications, have nonetheless introduced a series of challenges, spurring interest in the defence against the threat of misuse and abuse. Notably, source attribution of synthesized speech has value in forensics and intellectual property protection, but prior work in this area has certain limitations in scope. To address the gaps, we present our findings concerning the identification of the sources of synthesized speech in this paper. We investigate the existence of speech synthesis model fingerprints in the generated speech waveforms, with a focus on the acoustic model and the vocoder, and study the influence of each component on the fingerprint in the overall speech waveforms. Our research, conducted using the multi-speaker LibriTTS dataset, demonstrates two key insights: (1) vocoders and acoustic models impart distinct, model-specific fingerprints on the waveforms they generate, and (2) vocoder fingerprints are the more dominant of the two, and may mask the fingerprints from the acoustic model. These findings strongly suggest the existence of model-specific fingerprints for both the acoustic model and the vocoder, highlighting their potential utility in source identification applications.

</details>

### [Can large-scale vocoded spoofed data improve speech spoofing countermeasure with a self-supervised front end?](2309.06014.md)
**Xin Wang, Junichi Yamagishi** · 2023-09-12

<details>
<summary>Abstract</summary>

A speech spoofing countermeasure (CM) that discriminates between unseen spoofed and bona fide data requires diverse training data. While many datasets use spoofed data generated by speech synthesis systems, it was recently found that data vocoded by neural vocoders were also effective as the spoofed training data. Since many neural vocoders are fast in building and generation, this study used multiple neural vocoders and created more than 9,000 hours of vocoded data on the basis of the VoxCeleb2 corpus. This study investigates how this large-scale vocoded data can improve spoofing countermeasures that use data-hungry self-supervised learning (SSL) models. Experiments demonstrated that the overall CM performance on multiple test sets improved when using features extracted by an SSL model continually trained on the vocoded data. Further improvement was observed when using a new SSL distilled from the two SSLs before and after the continual training. The CM with the distilled SSL outperformed the previous best model on challenging unseen test sets, including the ASVspoof 2019 logical access, WaveFake, and In-the-Wild.

</details>

### [CleanUNet 2: A Hybrid Speech Denoising Model on Waveform and Spectrogram](2309.05975.md)
**Zhifeng Kong, Wei Ping, Ambrish Dantrey, Bryan Catanzaro** · 2023-09-12

<details>
<summary>Abstract</summary>

In this work, we present CleanUNet 2, a speech denoising model that combines the advantages of waveform denoiser and spectrogram denoiser and achieves the best of both worlds. CleanUNet 2 uses a two-stage framework inspired by popular speech synthesis methods that consist of a waveform model and a spectrogram model. Specifically, CleanUNet 2 builds upon CleanUNet, the state-of-the-art waveform denoiser, and further boosts its performance by taking predicted spectrograms from a spectrogram denoiser as the input. We demonstrate that CleanUNet 2 outperforms previous methods in terms of various objective and subjective evaluations.

</details>

### [Multi-Modal Automatic Prosody Annotation with Contrastive Pretraining of SSWP](2309.05423.md)
**Jinzuomu Zhong et.al.** · 2023-09-11

### [AudioLDM 2: Learning Holistic Audio Generation with Self-supervised Pretraining](2308.05734.md)
**Haohe Liu et.al.** · 2023-09-09

### [Cross-Utterance Conditioned VAE for Speech Generation](2309.04156.md)
**Yang Li, Cheng Yu, Guangzhi Sun, Weiqin Zu et al.** · 2023-09-08

<details>
<summary>Abstract</summary>

Speech synthesis systems powered by neural networks hold promise for multimedia production, but frequently face issues with producing expressive speech and seamless editing. In response, we present the Cross-Utterance Conditioned Variational Autoencoder speech synthesis (CUC-VAE S2) framework to enhance prosody and ensure natural speech generation. This framework leverages the powerful representational capabilities of pre-trained language models and the re-expression abilities of variational autoencoders (VAEs). The core component of the CUC-VAE S2 framework is the cross-utterance CVAE, which extracts acoustic, speaker, and textual features from surrounding sentences to generate context-sensitive prosodic features, more accurately emulating human prosody generation. We further propose two practical algorithms tailored for distinct speech synthesis applications: CUC-VAE TTS for text-to-speech and CUC-VAE SE for speech editing. The CUC-VAE TTS is a direct application of the framework, designed to generate audio with contextual prosody derived from surrounding texts. On the other hand, the CUC-VAE SE algorithm leverages real mel spectrogram sampling conditioned on contextual information, producing audio that closely mirrors real sound and thereby facilitating flexible speech editing based on text such as deletion, insertion, and replacement. Experimental results on the LibriTTS datasets demonstrate that our proposed models significantly enhance speech synthesis and editing, producing more natural and expressive speech.

</details>

### [Parallel and Limited Data Voice Conversion Using Stochastic Variational Deep Kernel Learning](2309.04420.md)
**Mohamadreza Jafaryani, Hamid Sheikhzadeh, Vahid Pourahmadi** · 2023-09-08

<details>
<summary>Abstract</summary>

Typically, voice conversion is regarded as an engineering problem with limited training data. The reliance on massive amounts of data hinders the practical applicability of deep learning approaches, which have been extensively researched in recent years. On the other hand, statistical methods are effective with limited data but have difficulties in modelling complex mapping functions. This paper proposes a voice conversion method that works with limited data and is based on stochastic variational deep kernel learning (SVDKL). At the same time, SVDKL enables the use of deep neural networks' expressive capability as well as the high flexibility of the Gaussian process as a Bayesian and non-parametric method. When the conventional kernel is combined with the deep neural network, it is possible to estimate non-smooth and more complex functions. Furthermore, the model's sparse variational Gaussian process solves the scalability problem and, unlike the exact Gaussian process, allows for the learning of a global mapping function for the entire acoustic space. One of the most important aspects of the proposed scheme is that the model parameters are trained using marginal likelihood optimization, which considers both data fitting and model complexity. Considering the complexity of the model reduces the amount of training data by increasing the resistance to overfitting. To evaluate the proposed scheme, we examined the model's performance with approximately 80 seconds of training data. The results indicated that our method obtained a higher mean opinion score, smaller spectral distortion, and better preference tests than the compared methods.

</details>

### [Large-Scale Automatic Audiobook Creation](2309.03926.md)
**Brendan Walsh, Mark Hamilton, Greg Newby, Xi Wang et al.** · 2023-09-07

<details>
<summary>Abstract</summary>

An audiobook can dramatically improve a work of literature's accessibility and improve reader engagement. However, audiobooks can take hundreds of hours of human effort to create, edit, and publish. In this work, we present a system that can automatically generate high-quality audiobooks from online e-books. In particular, we leverage recent advances in neural text-to-speech to create and release thousands of human-quality, open-license audiobooks from the Project Gutenberg e-book collection. Our method can identify the proper subset of e-book content to read for a wide collection of diversely structured books and can operate on hundreds of books in parallel. Our system allows users to customize an audiobook's speaking speed and style, emotional intonation, and can even match a desired voice using a small amount of sample audio. This work contributed over five thousand open-license audiobooks and an interactive demo that allows users to quickly create their own customized audiobooks. To listen to the audiobook collection visit \url{https://aka.ms/audiobook}.

</details>

### [GRASS: Unified Generation Model for Speech-to-Semantic Tasks](2309.02780.md)
**Aobo Xia, Shuyu Lei, Yushu Yang, Xiang Guo et al.** · 2023-09-06

<details>
<summary>Abstract</summary>

This paper explores the instruction fine-tuning technique for speech-to-semantic tasks by introducing a unified end-to-end (E2E) framework that generates target text conditioned on a task-related prompt for audio data. We pre-train the model using large and diverse data, where instruction-speech pairs are constructed via a text-to-speech (TTS) system. Extensive experiments demonstrate that our proposed model achieves state-of-the-art (SOTA) results on many benchmarks covering speech named entity recognition, speech sentiment analysis, speech question answering, and more, after fine-tuning. Furthermore, the proposed model achieves competitive performance in zero-shot and few-shot scenarios. To facilitate future work on instruction fine-tuning for speech-to-semantic tasks, we release our instruction dataset and code.

</details>

### [MuLanTTS: The Microsoft Speech Synthesis System for Blizzard Challenge 2023](2309.02743.md)
**Zhihang Xu, Shaofei Zhang, Xi Wang, Jiajun Zhang et al.** · 2023-09-06

<details>
<summary>Abstract</summary>

In this paper, we present MuLanTTS, the Microsoft end-to-end neural text-to-speech (TTS) system designed for the Blizzard Challenge 2023. About 50 hours of audiobook corpus for French TTS as hub task and another 2 hours of speaker adaptation as spoke task are released to build synthesized voices for different test purposes including sentences, paragraphs, homographs, lists, etc. Building upon DelightfulTTS, we adopt contextual and emotion encoders to adapt the audiobook data to enrich beyond sentences for long-form prosody and dialogue expressiveness. Regarding the recording quality, we also apply denoise algorithms and long audio processing for both corpora. For the hub task, only the 50-hour single speaker data is used for building the TTS system, while for the spoke task, a multi-speaker source model is used for target speaker fine tuning. MuLanTTS achieves mean scores of quality assessment 4.3 and 4.5 in the respective tasks, statistically comparable with natural speech while keeping good similarity according to similarity assessment. The excellent and similarity in this year's new and dense statistical evaluation show the effectiveness of our proposed system in both tasks.

</details>

### [BigVSAN: Enhancing GAN-based Neural Vocoders with Slicing Adversarial Network](2309.02836.md)
**Takashi Shibuya, Yuhta Takida, Yuki Mitsufuji** · 2023-09-06

<details>
<summary>Abstract</summary>

Generative adversarial network (GAN)-based vocoders have been intensively studied because they can synthesize high-fidelity audio waveforms faster than real-time. However, it has been reported that most GANs fail to obtain the optimal projection for discriminating between real and fake data in the feature space. In the literature, it has been demonstrated that slicing adversarial network (SAN), an improved GAN training framework that can find the optimal projection, is effective in the image generation task. In this paper, we investigate the effectiveness of SAN in the vocoding task. For this purpose, we propose a scheme to modify least-squares GAN, which most GAN-based vocoders adopt, so that their loss functions satisfy the requirements of SAN. Through our experiments, we demonstrate that SAN can improve the performance of GAN-based vocoders, including BigVGAN, with small modifications. Our code is available at https://github.com/sony/bigvsan.

</details>

### [Highly Controllable Diffusion-based Any-to-Any Voice Conversion Model with Frame-level Prosody Feature](2309.03364.md)
**Kyungguen Byun, Sunkuk Moon, Erik Visser** · 2023-09-06

<details>
<summary>Abstract</summary>

We propose a highly controllable voice manipulation system that can perform any-to-any voice conversion (VC) and prosody modulation simultaneously. State-of-the-art VC systems can transfer sentence-level characteristics such as speaker, emotion, and speaking style. However, manipulating the frame-level prosody, such as pitch, energy and speaking rate, still remains challenging. Our proposed model utilizes a frame-level prosody feature to effectively transfer such properties. Specifically, pitch and energy trajectories are integrated in a prosody conditioning module and then fed alongside speaker and contents embeddings to a diffusion-based decoder generating a converted speech mel-spectrogram. To adjust the speaking rate, our system includes a self-supervised model based post-processing step which allows improved controllability. The proposed model showed comparable speech quality and improved intelligibility compared to a SOTA approach. It can cover a varying range of fundamental frequency (F0), energy and speed modulation while maintaining converted speech quality.

</details>

### [Stylebook: Content-Dependent Speaking Style Modeling for Any-to-Any Voice Conversion using Only Speech Data](2309.02730.md)
**Hyungseob Lim, Kyungguen Byun, Sunkuk Moon, Erik Visser** · 2023-09-06

<details>
<summary>Abstract</summary>

While many recent any-to-any voice conversion models succeed in transferring some target speech's style information to the converted speech, they still lack the ability to faithfully reproduce the speaking style of the target speaker. In this work, we propose a novel method to extract rich style information from target utterances and to efficiently transfer it to source speech content without requiring text transcriptions or speaker labeling. Our proposed approach introduces an attention mechanism utilizing a self-supervised learning (SSL) model to collect the speaking styles of a target speaker each corresponding to the different phonetic content. The styles are represented with a set of embeddings called stylebook. In the next step, the stylebook is attended with the source speech's phonetic content to determine the final target style for each source content. Finally, content information extracted from the source speech and content-dependent target style embeddings are fed into a diffusion-based decoder to generate the converted speech mel-spectrogram. Experiment results show that our proposed method combined with a diffusion-based generative model can achieve better speaker similarity in any-to-any voice conversion tasks when compared to baseline models, while the increase in computational complexity with longer utterances is suppressed.

</details>

### [PromptTTS 2: Describing and Generating Voices with Text Prompt](2309.02285.md)
**Yichong Leng, Zhifang Guo, Kai Shen, Xu Tan et al.** · 2023-09-05

<details>
<summary>Abstract</summary>

Speech conveys more information than text, as the same word can be uttered in various voices to convey diverse information. Compared to traditional text-to-speech (TTS) methods relying on speech prompts (reference speech) for voice variability, using text prompts (descriptions) is more user-friendly since speech prompts can be hard to find or may not exist at all. TTS approaches based on the text prompt face two main challenges: 1) the one-to-many problem, where not all details about voice variability can be described in the text prompt, and 2) the limited availability of text prompt datasets, where vendors and large cost of data labeling are required to write text prompts for speech. In this work, we introduce PromptTTS 2 to address these challenges with a variation network to provide variability information of voice not captured by text prompts, and a prompt generation pipeline to utilize the large language models (LLM) to compose high quality text prompts. Specifically, the variation network predicts the representation extracted from the reference speech (which contains full information about voice variability) based on the text prompt representation. For the prompt generation pipeline, it generates text prompts for speech with a speech language understanding model to recognize voice attributes (e.g., gender, speed) from speech and a large language model to formulate text prompts based on the recognition results. Experiments on a large-scale (44K hours) speech dataset demonstrate that compared to the previous works, PromptTTS 2 generates voices more consistent with text prompts and supports the sampling of diverse voice variability, thereby offering users more choices on voice generation. Additionally, the prompt generation pipeline produces high-quality text prompts, eliminating the large labeling cost. The demo page of PromptTTS 2 is available online.

</details>

### [FSD: An Initial Chinese Dataset for Fake Song Detection](2309.02232.md)
**Yuankun Xie, Jingjing Zhou, Xiaolin Lu, Zhenghao Jiang et al.** · 2023-09-05

<details>
<summary>Abstract</summary>

Singing voice synthesis and singing voice conversion have significantly advanced, revolutionizing musical experiences. However, the rise of "Deepfake Songs" generated by these technologies raises concerns about authenticity. Unlike Audio DeepFake Detection (ADD), the field of song deepfake detection lacks specialized datasets or methods for song authenticity verification. In this paper, we initially construct a Chinese Fake Song Detection (FSD) dataset to investigate the field of song deepfake detection. The fake songs in the FSD dataset are generated by five state-of-the-art singing voice synthesis and singing voice conversion methods. Our initial experiments on FSD revealed the ineffectiveness of existing speech-trained ADD models for the task of song deepFake detection. Thus, we employ the FSD dataset for the training of ADD models. We subsequently evaluate these models under two scenarios: one with the original songs and another with separated vocal tracks. Experiment results show that song-trained ADD models exhibit a 38.58% reduction in average equal error rate compared to speech-trained ADD models on the FSD test set.

</details>

### [Evaluating Methods for Ground-Truth-Free Foreign Accent Conversion](2309.02133.md)
**Wen-Chin Huang, Tomoki Toda** · 2023-09-05

<details>
<summary>Abstract</summary>

Foreign accent conversion (FAC) is a special application of voice conversion (VC) which aims to convert the accented speech of a non-native speaker to a native-sounding speech with the same speaker identity. FAC is difficult since the native speech from the desired non-native speaker to be used as the training target is impossible to collect. In this work, we evaluate three recently proposed methods for ground-truth-free FAC, where all of them aim to harness the power of sequence-to-sequence (seq2seq) and non-parallel VC models to properly convert the accent and control the speaker identity. Our experimental evaluation results show that no single method was significantly better than the others in all evaluation axes, which is in contrast to conclusions drawn in previous studies. We also explain the effectiveness of these methods with the training input and output of the seq2seq model and examine the design choice of the non-parallel VC model, and show that intelligibility measures such as word error rates do not correlate well with subjective accentedness. Finally, our implementation is open-sourced to promote reproducible research and help future researchers improve upon the compared systems.

</details>

### [Weigh Your Own Words: Improving Hate Speech Counter Narrative Generation via Attention Regularization](2309.02311.md)
**Helena Bonaldi, Giuseppe Attanasio, Debora Nozza, Marco Guerini** · 2023-09-05

<details>
<summary>Abstract</summary>

Recent computational approaches for combating online hate speech involve the automatic generation of counter narratives by adapting Pretrained Transformer-based Language Models (PLMs) with human-curated data. This process, however, can produce in-domain overfitting, resulting in models generating acceptable narratives only for hatred similar to training data, with little portability to other targets or to real-world toxic language. This paper introduces novel attention regularization methodologies to improve the generalization capabilities of PLMs for counter narratives generation. Overfitting to training-specific terms is then discouraged, resulting in more diverse and richer narratives. We experiment with two attention-based regularization techniques on a benchmark English dataset. Regularized models produce better counter narratives than state-of-the-art approaches in most cases, both in terms of automatic metrics and human evaluation, especially when hateful targets are not present in the training data. This work paves the way for better and more flexible counter-speech generation models, a task for which datasets are highly challenging to produce.

</details>

### [A Comparative Analysis of Pretrained Language Models for Text-to-Speech](2309.01576.md)
**Marcel Granero-Moya et.al.** · 2023-09-04

### [Rep2wav: Noise Robust text-to-speech Using self-supervised representations](2308.14553.md)
**Qiushi Zhu et.al.** · 2023-09-04

### [Deep Learning based Multilingual Speech Synthesis using Multi Feature Fusion Methods](s2:505cebd16e54128566c6f6aae5930fa14a73d476.md)
**P. Nuthakki, Madhavi Katamaneni, C. J. N., Kumari Gubbala et al.** · 2023-09-04

<details>
<summary>Abstract</summary>

The poor intelligibility and out-of-the-ordinary nature of the traditional concatenation speech synthesis technologies are two major problems. CNN's context deep learning approaches aren't robust enough for sensitive speech synthesis. Our suggested approach may satisfy such needs and modify the complexities of voice synthesis. The suggested model's minimal aperiodic distortion makes it an excellent candidate for a communication recognition model. Our suggested method is as close to human speech as possible, despite the fact that speech synthesis has a number of audible flaws. Additionally, there is excellent hard work to be done in incorporating sentiment analysis into text categorization using natural language processing. The intensity of feeling varies greatly from nation to country. To improve their voice synthesis outputs, models need to include more and more concealed layers & nodes into the updated mixture density network. For our suggested algorithm to perform at its best, we need a more robust network foundation and optimization methods. We hope that after reading this article and trying out the example data provided, both experienced researchers and those just starting out would have a better grasp of the steps involved in creating a deep learning approach. Overcoming fitting issues with less data in training, the model is making progress. More space is needed to hold the input parameters in the DL-based method.

</details>

### [MSM-VC: High-fidelity Source Style Transfer for Non-Parallel Voice Conversion by Multi-scale Style Modeling](2309.01142.md)
**Zhichao Wang, Xinsheng Wang, Qicong Xie, Tao Li et al.** · 2023-09-03

<details>
<summary>Abstract</summary>

In addition to conveying the linguistic content from source speech to converted speech, maintaining the speaking style of source speech also plays an important role in the voice conversion (VC) task, which is essential in many scenarios with highly expressive source speech, such as dubbing and data augmentation. Previous work generally took explicit prosodic features or fixed-length style embedding extracted from source speech to model the speaking style of source speech, which is insufficient to achieve comprehensive style modeling and target speaker timbre preservation. Inspired by the style's multi-scale nature of human speech, a multi-scale style modeling method for the VC task, referred to as MSM-VC, is proposed in this paper. MSM-VC models the speaking style of source speech from different levels. To effectively convey the speaking style and meanwhile prevent timbre leakage from source speech to converted speech, each level's style is modeled by specific representation. Specifically, prosodic features, pre-trained ASR model's bottleneck features, and features extracted by a model trained with a self-supervised strategy are adopted to model the frame, local, and global-level styles, respectively. Besides, to balance the performance of source style modeling and target speaker timbre preservation, an explicit constraint module consisting of a pre-trained speech emotion recognition model and a speaker classifier is introduced to MSM-VC. This explicit constraint module also makes it possible to simulate the style transfer inference process during the training to improve the disentanglement ability and alleviate the mismatch between training and inference. Experiments performed on the highly expressive speech corpus demonstrate that MSM-VC is superior to the state-of-the-art VC methods for modeling source speech style while maintaining good speech quality and speaker similarity.

</details>

### [DiCLET-TTS: Diffusion Model based Cross-lingual Emotion Transfer for Text-to-Speech -- A Study between English and Mandarin](2309.00883.md)
**Tao Li et.al.** · 2023-09-02

### [Expressive paragraph text-to-speech synthesis with multi-step variational autoencoder](2308.13365.md)
**Xuyuan Li et.al.** · 2023-09-02

### [The FruitShell French synthesis system at the Blizzard 2023 Challenge](2309.00223.md)
**Xin Qi, Xiaopeng Wang, Zhiyong Wang, Wang Liu et al.** · 2023-09-01

<details>
<summary>Abstract</summary>

This paper presents a French text-to-speech synthesis system for the Blizzard Challenge 2023. The challenge consists of two tasks: generating high-quality speech from female speakers and generating speech that closely resembles specific individuals. Regarding the competition data, we conducted a screening process to remove missing or erroneous text data. We organized all symbols except for phonemes and eliminated symbols that had no pronunciation or zero duration. Additionally, we added word boundary and start/end symbols to the text, which we have found to improve speech quality based on our previous experience. For the Spoke task, we performed data augmentation according to the competition rules. We used an open-source G2P model to transcribe the French texts into phonemes. As the G2P model uses the International Phonetic Alphabet (IPA), we applied the same transcription process to the provided competition data for standardization. However, due to compiler limitations in recognizing special symbols from the IPA chart, we followed the rules to convert all phonemes into the phonetic scheme used in the competition data. Finally, we resampled all competition audio to a uniform sampling rate of 16 kHz. We employed a VITS-based acoustic model with the hifigan vocoder. For the Spoke task, we trained a multi-speaker model and incorporated speaker information into the duration predictor, vocoder, and flow layers of the model. The evaluation results of our system showed a quality MOS score of 3.6 for the Hub task and 3.4 for the Spoke task, placing our system at an average level among all participating teams.

</details>

### [QS-TTS: Towards Semi-Supervised Text-to-Speech Synthesis via Vector-Quantized Self-Supervised Speech Representation Learning](2309.00126.md)
**Haohan Guo et.al.** · 2023-08-31

### [Towards Spontaneous Style Modeling with Semi-supervised Pre-training for Conversational Text-to-Speech Synthesis](2308.16593.md)
**Weiqin Li et.al.** · 2023-08-31

### [LightGrad: Lightweight Diffusion Probabilistic Model for Text-to-Speech](2308.16569.md)
**Jie Chen et.al.** · 2023-08-31

### [Multi-GradSpeech: Towards Diffusion-based Multi-Speaker Text-to-speech Using Consistent Diffusion Models](2308.10428.md)
**Heyang Xue et.al.** · 2023-08-31

### [Improving Mandarin Prosodic Structure Prediction with Multi-level Contextual Information](2308.16577.md)
**Jie Chen, Changhe Song, Deyi Tuo, Xixin Wu et al.** · 2023-08-31

<details>
<summary>Abstract</summary>

For text-to-speech (TTS) synthesis, prosodic structure prediction (PSP) plays an important role in producing natural and intelligible speech. Although inter-utterance linguistic information can influence the speech interpretation of the target utterance, previous works on PSP mainly focus on utilizing intrautterance linguistic information of the current utterance only. This work proposes to use inter-utterance linguistic information to improve the performance of PSP. Multi-level contextual information, which includes both inter-utterance and intrautterance linguistic information, is extracted by a hierarchical encoder from character level, utterance level and discourse level of the input text. Then a multi-task learning (MTL) decoder predicts prosodic boundaries from multi-level contextual information. Objective evaluation results on two datasets show that our method achieves better F1 scores in predicting prosodic word (PW), prosodic phrase (PPH) and intonational phrase (IPH). It demonstrates the effectiveness of using multi-level contextual information for PSP. Subjective preference tests also indicate the naturalness of synthesized speeches are improved.

</details>

### [CALM: Contrastive Cross-modal Speaking Style Modeling for Expressive Text-to-Speech Synthesis](2308.16021.md)
**Yi Meng, Xiang Li, Zhiyong Wu, Tingtian Li et al.** · 2023-08-30

<details>
<summary>Abstract</summary>

To further improve the speaking styles of synthesized speeches, current text-to-speech (TTS) synthesis systems commonly employ reference speeches to stylize their outputs instead of just the input texts. These reference speeches are obtained by manual selection which is resource-consuming, or selected by semantic features. However, semantic features contain not only style-related information, but also style irrelevant information. The information irrelevant to speaking style in the text could interfere the reference audio selection and result in improper speaking styles. To improve the reference selection, we propose Contrastive Acoustic-Linguistic Module (CALM) to extract the Style-related Text Feature (STF) from the text. CALM optimizes the correlation between the speaking style embedding and the extracted STF with contrastive learning. Thus, a certain number of the most appropriate reference speeches for the input text are selected by retrieving the speeches with the top STF similarities. Then the style embeddings are weighted summarized according to their STF similarities and used to stylize the synthesized speech of TTS. Experiment results demonstrate the effectiveness of our proposed approach, with both objective evaluations and subjective evaluations on the speaking styles of the synthesized speeches outperform a baseline approach with semantic-feature-based reference selection.

</details>

### [The DeepZen Speech Synthesis System for Blizzard Challenge 2023](2308.15945.md)
**Christophe Veaux, Ranniery Maia, Spyridoula Papandreou** · 2023-08-30

<details>
<summary>Abstract</summary>

This paper describes the DeepZen text to speech (TTS) system for Blizzard Challenge 2023. The goal of this challenge is to synthesise natural and high-quality speech in French, from a large monospeaker dataset (hub task) and from a smaller dataset by speaker adaptation (spoke task). We participated to both tasks with the same model architecture. Our approach has been to use an auto-regressive model, which retains an advantage for generating natural sounding speech but to improve prosodic control in several ways. Similarly to non-attentive Tacotron, the model uses a duration predictor and gaussian upsampling at inference, but with a simpler unsupervised training. We also model the speaking style at both sentence and word levels by extracting global and local style tokens from the reference speech. At inference, the global and local style tokens are predicted from a BERT model run on text. This BERT model is also used to predict specific pronunciation features like schwa elision and optional liaisons. Finally, a modified version of HifiGAN trained on a large public dataset and fine-tuned on the target voices is used to generate speech waveform. Our team is identified as O in the the Blizzard evaluation and MUSHRA test results show that our system performs second ex aequo in both hub task (median score of 0.75) and spoke task (median score of 0.68), over 18 and 14 participants, respectively.

</details>

### [A Review of Differentiable Digital Signal Processing for Music & Speech Synthesis](2308.15422.md)
**Ben Hayes, Jordie Shier, György Fazekas, Andrew McPherson et al.** · 2023-08-29

<details>
<summary>Abstract</summary>

The term "differentiable digital signal processing" describes a family of techniques in which loss function gradients are backpropagated through digital signal processors, facilitating their integration into neural networks. This article surveys the literature on differentiable audio signal processing, focusing on its use in music & speech synthesis. We catalogue applications to tasks including music performance rendering, sound matching, and voice transformation, discussing the motivations for and implications of the use of this methodology. This is accompanied by an overview of digital signal processing operations that have been implemented differentiably. Finally, we highlight open challenges, including optimisation pathologies, robustness to real-world conditions, and design trade-offs, and discuss directions for future research.

</details>

### [Pruning Self-Attention for Zero-Shot Multi-Speaker Text-to-Speech](2308.14909.md)
**Hyungchan Yoon et.al.** · 2023-08-28

### [TextrolSpeech: A Text Style Control Speech Corpus With Codec Language Text-to-Speech Models](2308.14430.md)
**Shengpeng Ji et.al.** · 2023-08-28

### [Adversarial Learning of Intermediate Acoustic Feature for End-to-End Lightweight Text-to-Speech](2204.02172.md)
**Hyungchan Yoon et.al.** · 2023-08-28

### [Voice Conversion with Denoising Diffusion Probabilistic GAN Models](2308.14319.md)
**Xulong Zhang, Jianzong Wang, Ning Cheng, Jing Xiao** · 2023-08-28

<details>
<summary>Abstract</summary>

Voice conversion is a method that allows for the transformation of speaking style while maintaining the integrity of linguistic information. There are many researchers using deep generative models for voice conversion tasks. Generative Adversarial Networks (GANs) can quickly generate high-quality samples, but the generated samples lack diversity. The samples generated by the Denoising Diffusion Probabilistic Models (DDPMs) are better than GANs in terms of mode coverage and sample diversity. But the DDPMs have high computational costs and the inference speed is slower than GANs. In order to make GANs and DDPMs more practical we proposes DiffGAN-VC, a variant of GANs and DDPMS, to achieve non-parallel many-to-many voice conversion (VC). We use large steps to achieve denoising, and also introduce a multimodal conditional GANs to model the denoising diffusion generative adversarial network. According to both objective and subjective evaluation experiments, DiffGAN-VC has been shown to achieve high voice quality on non-parallel data sets. Compared with the CycleGAN-VC method, DiffGAN-VC achieves speaker similarity, naturalness and higher sound quality.

</details>

### [Generalizable Zero-Shot Speaker Adaptive Speech Synthesis with Disentangled Representations](2308.13007.md)
**Wenbin Wang et.al.** · 2023-08-24

### [Real-time Detection of AI-Generated Speech for DeepFake Voice Conversion](2308.12734.md)
**Jordan J. Bird, Ahmad Lotfi** · 2023-08-24

<details>
<summary>Abstract</summary>

There are growing implications surrounding generative AI in the speech domain that enable voice cloning and real-time voice conversion from one individual to another. This technology poses a significant ethical threat and could lead to breaches of privacy and misrepresentation, thus there is an urgent need for real-time detection of AI-generated speech for DeepFake Voice Conversion. To address the above emerging issues, the DEEP-VOICE dataset is generated in this study, comprised of real human speech from eight well-known figures and their speech converted to one another using Retrieval-based Voice Conversion. Presenting as a binary classification problem of whether the speech is real or AI-generated, statistical analysis of temporal audio features through t-testing reveals that there are significantly different distributions. Hyperparameter optimisation is implemented for machine learning models to identify the source of speech. Following the training of 208 individual machine learning models over 10-fold cross validation, it is found that the Extreme Gradient Boosting model can achieve an average classification accuracy of 99.3% and can classify speech in real-time, at around 0.004 milliseconds given one second of speech. All data generated for this study is released publicly for future research on AI speech detection.

</details>

### [Evaluation of the Speech Resynthesis Capabilities of the VoicePrivacy Challenge Baseline B1](2308.11337.md)
**Ünal Ege Gaznepoglu, Nils Peters** · 2023-08-22

<details>
<summary>Abstract</summary>

Speaker anonymization systems continue to improve their ability to obfuscate the original speaker characteristics in a speech signal, but often create processing artifacts and unnatural sounding voices as a tradeoff. Many of those systems stem from the VoicePrivacy Challenge (VPC) Baseline B1, using a neural vocoder to synthesize speech from an F0, x-vectors and bottleneck features-based speech representation. Inspired by this, we investigate the reproduction capabilities of the aforementioned baseline, to assess how successful the shared methodology is in synthesizing human-like speech. We use four objective metrics to measure speech quality, waveform similarity, and F0 similarity. Our findings indicate that both the speech representation and the vocoder introduces artifacts, causing an unnatural perception. A MUSHRA-like listening test on 18 subjects corroborate our findings, motivating further research on the analysis and synthesis components of the VPC Baseline B1.

</details>

### [PMVC: Data Augmentation-Based Prosody Modeling for Expressive Voice Conversion](2308.11084.md)
**Yimin Deng, Huaizhen Tang, Xulong Zhang, Jianzong Wang et al.** · 2023-08-21

<details>
<summary>Abstract</summary>

Voice conversion as the style transfer task applied to speech, refers to converting one person's speech into a new speech that sounds like another person's. Up to now, there has been a lot of research devoted to better implementation of VC tasks. However, a good voice conversion model should not only match the timbre information of the target speaker, but also expressive information such as prosody, pace, pause, etc. In this context, prosody modeling is crucial for achieving expressive voice conversion that sounds natural and convincing. Unfortunately, prosody modeling is important but challenging, especially without text transcriptions. In this paper, we firstly propose a novel voice conversion framework named 'PMVC', which effectively separates and models the content, timbre, and prosodic information from the speech without text transcriptions. Specially, we introduce a new speech augmentation algorithm for robust prosody extraction. And building upon this, mask and predict mechanism is applied in the disentanglement of prosody and content information. The experimental results on the AIShell-3 corpus supports our improvement of naturalness and similarity of converted speech.

</details>

### [Speech Synthesis from Articulatory Movements Recorded by Real-time MRI](s2:977f2f760d0eb99d73182fd8334c1986989c5b07.md)
**Yuto Otani, S. Sawada, Hidefumi Ohmura, Kouichi Katsurada** · 2023-08-20

<details>
<summary>Abstract</summary>

Previous speech synthesis models from articulatory movements recorded using real-time MRI (rtMRI) only predicted vocal tract shape parameters and required additional pitch information to generate a speech waveform. This study proposes a two-stage deep learning model composed of CNN-BiLSTM that predicts a mel-spectrogram from a rtMRI video and a HiFi-GAN vocoder that synthesizes a speech waveform. We evaluated our model on two databases: the ATR 503 sentences rtMRI database and the USC-TIMIT database. The experimental results on the ATR 503 sentences rtMRI database show that the PESQ score and the RMSE of F 0 are 1.64 and 26.7 Hz. This demonstrates that all acoustic parameters, including fundamental frequency, can be estimated from the rtMRI videos. In the experiment on the USC-TIMIT database, we obtained a good PESQ score and RMSE for F 0 . However, the synthesized speech is unclear, indicating that the quality of the datasets affects the intelligibility of the synthesized speech.

</details>

### [Speaking State Decoder with Transition Detection for Next Speaker Prediction](s2:12425c65dcf4bb80e122f73780a3935ce51d5692.md)
**Shao-Hao Lu, Yun-Shao Lin, Chi-Chun Lee** · 2023-08-20

<details>
<summary>Abstract</summary>

Next speaker prediction and turn change prediction are two important tasks in group interaction and human-agent interaction. In order to carry out a fluent conversation, we need to identify who is currently speaking, who is the next speaker and when the next speaker starts to speak. These questions are computationally designed as the task of next speaker prediction . Behav-iors such as gaze direction, speaking prosody or gestures have been modeled to perform this task. In this work, we propose a decoder-based speaking state decoder (SSD) for next speaker prediction, which jointly considers current behavior features, past history of talking and speaking state transition detection model. Our decoder approach achieves next speaker prediction with UAR of 78.11%, which is 3.41% improvement over the champion model in MultiMediate challenge 2021.

</details>

### [Effects of Convolutional Autoencoder Bottleneck Width on StarGAN-based Singing Technique Conversion](2308.10021.md)
**Tung-Cheng Su, Yung-Chuan Chang, Yi-Wen Liu** · 2023-08-19

<details>
<summary>Abstract</summary>

Singing technique conversion (STC) refers to the task of converting from one voice technique to another while leaving the original singer identity, melody, and linguistic components intact. Previous STC studies, as well as singing voice conversion research in general, have utilized convolutional autoencoders (CAEs) for conversion, but how the bottleneck width of the CAE affects the synthesis quality has not been thoroughly evaluated. To this end, we constructed a GAN-based multi-domain STC system which took advantage of the WORLD vocoder representation and the CAE architecture. We varied the bottleneck width of the CAE, and evaluated the conversion results subjectively. The model was trained on a Mandarin dataset which features four singers and four singing techniques: the chest voice, the falsetto, the raspy voice, and the whistle voice. The results show that a wider bottleneck corresponds to better articulation clarity but does not necessarily lead to higher likeness to the target technique. Among the four techniques, we also found that the whistle voice is the easiest target for conversion, while the other three techniques as a source produce more convincing conversion results than the whistle.

</details>

### [AffectEcho: Speaker Independent and Language-Agnostic Emotion and Affect Transfer for Speech Synthesis](2308.08577.md)
**Hrishikesh Viswanath, Aneesh Bhattacharya, Pascal Jutras-Dubé, Prerit Gupta et al.** · 2023-08-16

<details>
<summary>Abstract</summary>

Affect is an emotional characteristic encompassing valence, arousal, and intensity, and is a crucial attribute for enabling authentic conversations. While existing text-to-speech (TTS) and speech-to-speech systems rely on strength embedding vectors and global style tokens to capture emotions, these models represent emotions as a component of style or represent them in discrete categories. We propose AffectEcho, an emotion translation model, that uses a Vector Quantized codebook to model emotions within a quantized space featuring five levels of affect intensity to capture complex nuances and subtle differences in the same emotion. The quantized emotional embeddings are implicitly derived from spoken speech samples, eliminating the need for one-hot vectors or explicit strength embeddings. Experimental results demonstrate the effectiveness of our approach in controlling the emotions of generated speech while preserving identity, style, and emotional cadence unique to each speaker. We showcase the language-independent emotion modeling capability of the quantized emotional embeddings learned from a bilingual (English and Chinese) speech corpus with an emotion transfer task from a reference speech to a target speech. We achieve state-of-art results on both qualitative and quantitative metrics.

</details>

### [DiffV2S: Diffusion-based Video-to-Speech Synthesis with Vision-guided Speaker Embedding](2308.07787.md)
**Jeongsoo Choi, Joanna Hong, Yong Man Ro** · 2023-08-15

<details>
<summary>Abstract</summary>

Recent research has demonstrated impressive results in video-to-speech synthesis which involves reconstructing speech solely from visual input. However, previous works have struggled to accurately synthesize speech due to a lack of sufficient guidance for the model to infer the correct content with the appropriate sound. To resolve the issue, they have adopted an extra speaker embedding as a speaking style guidance from a reference auditory information. Nevertheless, it is not always possible to obtain the audio information from the corresponding video input, especially during the inference time. In this paper, we present a novel vision-guided speaker embedding extractor using a self-supervised pre-trained model and prompt tuning technique. In doing so, the rich speaker embedding information can be produced solely from input visual information, and the extra audio information is not necessary during the inference time. Using the extracted vision-guided speaker embedding representations, we further develop a diffusion-based video-to-speech synthesis model, so called DiffV2S, conditioned on those speaker embeddings and the visual representation extracted from the input video. The proposed DiffV2S not only maintains phoneme details contained in the input video frames, but also creates a highly intelligible mel-spectrogram in which the speaker identities of the multiple speakers are all preserved. Our experimental results show that DiffV2S achieves the state-of-the-art performance compared to the previous video-to-speech synthesis technique.

</details>

### [SpeechX: Neural Codec Language Model as a Versatile Speech Transformer](2308.06873.md)
**Xiaofei Wang et.al.** · 2023-08-14

### [Miipher: A Robust Speech Restoration Model Integrating Self-Supervised Speech and Text Representations](2303.01664.md)
**Yuma Koizumi et.al.** · 2023-08-14

### [iSTFTNet2: Faster and More Lightweight iSTFT-Based Neural Vocoder Using 1D-2D CNN](2308.07117.md)
**Takuhiro Kaneko, Hirokazu Kameoka, Kou Tanaka, Shogo Seki** · 2023-08-14

<details>
<summary>Abstract</summary>

The inverse short-time Fourier transform network (iSTFTNet) has garnered attention owing to its fast, lightweight, and high-fidelity speech synthesis. It obtains these characteristics using a fast and lightweight 1D CNN as the backbone and replacing some neural processes with iSTFT. Owing to the difficulty of a 1D CNN to model high-dimensional spectrograms, the frequency dimension is reduced via temporal upsampling. However, this strategy compromises the potential to enhance the speed. Therefore, we propose iSTFTNet2, an improved variant of iSTFTNet with a 1D-2D CNN that employs 1D and 2D CNNs to model temporal and spectrogram structures, respectively. We designed a 2D CNN that performs frequency upsampling after conversion in a few-frequency space. This design facilitates the modeling of high-dimensional spectrograms without compromising the speed. The results demonstrated that iSTFTNet2 made iSTFTNet faster and more lightweight with comparable speech quality. Audio samples are available at https://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/istftnet2/.

</details>

### [Text-to-Video: a Two-stage Framework for Zero-shot Identity-agnostic Talking-head Generation](2308.06457.md)
**Zhichao Wang, Mengyu Dai, Keld Lundgaard** · 2023-08-12

<details>
<summary>Abstract</summary>

The advent of ChatGPT has introduced innovative methods for information gathering and analysis. However, the information provided by ChatGPT is limited to text, and the visualization of this information remains constrained. Previous research has explored zero-shot text-to-video (TTV) approaches to transform text into videos. However, these methods lacked control over the identity of the generated audio, i.e., not identity-agnostic, hindering their effectiveness. To address this limitation, we propose a novel two-stage framework for person-agnostic video cloning, specifically focusing on TTV generation. In the first stage, we leverage pretrained zero-shot models to achieve text-to-speech (TTS) conversion. In the second stage, an audio-driven talking head generation method is employed to produce compelling videos privided the audio generated in the first stage. This paper presents a comparative analysis of different TTS and audio-driven talking head generation methods, identifying the most promising approach for future research and development. Some audio and videos samples can be found in the following link: https://github.com/ZhichaoWang970201/Text-to-Video/tree/main.

</details>

### [Phoneme Hallucinator: One-shot Voice Conversion via Set Expansion](2308.06382.md)
**Siyuan Shan, Yang Li, Amartya Banerjee, Junier B. Oliva** · 2023-08-11

<details>
<summary>Abstract</summary>

Voice conversion (VC) aims at altering a person's voice to make it sound similar to the voice of another person while preserving linguistic content. Existing methods suffer from a dilemma between content intelligibility and speaker similarity; i.e., methods with higher intelligibility usually have a lower speaker similarity, while methods with higher speaker similarity usually require plenty of target speaker voice data to achieve high intelligibility. In this work, we propose a novel method \textit{Phoneme Hallucinator} that achieves the best of both worlds. Phoneme Hallucinator is a one-shot VC model; it adopts a novel model to hallucinate diversified and high-fidelity target speaker phonemes based just on a short target speaker voice (e.g. 3 seconds). The hallucinated phonemes are then exploited to perform neighbor-based voice conversion. Our model is a text-free, any-to-any VC model that requires no text annotations and supports conversion to any unseen speaker. Objective and subjective evaluations show that \textit{Phoneme Hallucinator} outperforms existing VC methods for both intelligibility and speaker similarity.

</details>

### [EXPRESSO: A Benchmark and Analysis of Discrete Expressive Speech Resynthesis](2308.05725.md)
**Tu Anh Nguyen, Wei-Ning Hsu, Antony D'Avirro, Bowen Shi et al.** · 2023-08-10

<details>
<summary>Abstract</summary>

Recent work has shown that it is possible to resynthesize high-quality speech based, not on text, but on low bitrate discrete units that have been learned in a self-supervised fashion and can therefore capture expressive aspects of speech that are hard to transcribe (prosody, voice styles, non-verbal vocalization). The adoption of these methods is still limited by the fact that most speech synthesis datasets are read, severely limiting spontaneity and expressivity. Here, we introduce Expresso, a high-quality expressive speech dataset for textless speech synthesis that includes both read speech and improvised dialogues rendered in 26 spontaneous expressive styles. We illustrate the challenges and potentials of this dataset with an expressive resynthesis benchmark where the task is to encode the input in low-bitrate units and resynthesize it in a target voice while preserving content and style. We evaluate resynthesis quality with automatic metrics for different self-supervised discrete encoders, and explore tradeoffs between quality, bitrate and invariance to speaker and style. All the dataset, evaluation metrics and baseline models are open source

</details>

### [Data Player: Automatic Generation of Data Videos with Narration-Animation Interplay](2308.04703.md)
**Leixian Shen, Yizhi Zhang, Haidong Zhang, Yun Wang** · 2023-08-09

<details>
<summary>Abstract</summary>

Data visualizations and narratives are often integrated to convey data stories effectively. Among various data storytelling formats, data videos have been garnering increasing attention. These videos provide an intuitive interpretation of data charts while vividly articulating the underlying data insights. However, the production of data videos demands a diverse set of professional skills and considerable manual labor, including understanding narratives, linking visual elements with narration segments, designing and crafting animations, recording audio narrations, and synchronizing audio with visual animations. To simplify this process, our paper introduces a novel method, referred to as Data Player, capable of automatically generating dynamic data videos with narration-animation interplay. This approach lowers the technical barriers associated with creating data videos rich in narration. To enable narration-animation interplay, Data Player constructs references between visualizations and text input. Specifically, it first extracts data into tables from the visualizations. Subsequently, it utilizes large language models to form semantic connections between text and visuals. Finally, Data Player encodes animation design knowledge as computational low-level constraints, allowing for the recommendation of suitable animation presets that align with the audio narration produced by text-to-speech technologies. We assessed Data Player's efficacy through an example gallery, a user study, and expert interviews. The evaluation results demonstrated that Data Player can generate high-quality data videos that are comparable to human-composed ones.

</details>

### [On Error Propagation of Diffusion Models](2308.05021.md)
**Yangming Li, Mihaela van der Schaar** · 2023-08-09

<details>
<summary>Abstract</summary>

Although diffusion models (DMs) have shown promising performances in a number of tasks (e.g., speech synthesis and image generation), they might suffer from error propagation because of their sequential structure. However, this is not certain because some sequential models, such as Conditional Random Field (CRF), are free from this problem. To address this issue, we develop a theoretical framework to mathematically formulate error propagation in the architecture of DMs, The framework contains three elements, including modular error, cumulative error, and propagation equation. The modular and cumulative errors are related by the equation, which interprets that DMs are indeed affected by error propagation. Our theoretical study also suggests that the cumulative error is closely related to the generation quality of DMs. Based on this finding, we apply the cumulative error as a regularization term to reduce error propagation. Because the term is computationally intractable, we derive its upper bound and design a bootstrap algorithm to efficiently estimate the bound for optimization. We have conducted extensive experiments on multiple image datasets, showing that our proposed regularization reduces error propagation, significantly improves vanilla DMs, and outperforms previous baselines.

</details>

### [Towards an AI to Win Ghana's National Science and Maths Quiz](2308.04333.md)
**George Boateng, Jonathan Abrefah Mensah, Kevin Takyi Yeboah, William Edor et al.** · 2023-08-08

<details>
<summary>Abstract</summary>

Can an AI win Ghana's National Science and Maths Quiz (NSMQ)? That is the question we seek to answer in the NSMQ AI project, an open-source project that is building AI to compete live in the NSMQ and win. The NSMQ is an annual live science and mathematics competition for senior secondary school students in Ghana in which 3 teams of 2 students compete by answering questions across biology, chemistry, physics, and math in 5 rounds over 5 progressive stages until a winning team is crowned for that year. The NSMQ is an exciting live quiz competition with interesting technical challenges across speech-to-text, text-to-speech, question-answering, and human-computer interaction. In this ongoing work that began in January 2023, we give an overview of the project, describe each of the teams, progress made thus far, and the next steps toward our planned launch and debut of the AI in October for NSMQ 2023. An AI that conquers this grand challenge can have real-world impact on education such as enabling millions of students across Africa to have one-on-one learning support from this AI.

</details>

### [Let's Give a Voice to Conversational Agents in Virtual Reality](2308.02665.md)
**Michele Yin, Gabriel Roccabruna, Abhinav Azad, Giuseppe Riccardi** · 2023-08-04

<details>
<summary>Abstract</summary>

The dialogue experience with conversational agents can be greatly enhanced with multimodal and immersive interactions in virtual reality. In this work, we present an open-source architecture with the goal of simplifying the development of conversational agents operating in virtual environments. The architecture offers the possibility of plugging in conversational agents of different domains and adding custom or cloud-based Speech-To-Text and Text-To-Speech models to make the interaction voice-based. Using this architecture, we present two conversational prototypes operating in the digital health domain developed in Unity for both non-immersive displays and VR headsets.

</details>

### [Textless Unit-to-Unit training for Many-to-Many Multilingual Speech-to-Speech Translation](2308.01831.md)
**Minsu Kim, Jeongsoo Choi, Dahun Kim, Yong Man Ro** · 2023-08-03

<details>
<summary>Abstract</summary>

This paper proposes a textless training method for many-to-many multilingual speech-to-speech translation that can also benefit the transfer of pre-trained knowledge to text-based systems, text-to-speech synthesis and text-to-speech translation. To this end, we represent multilingual speech with speech units that are the discretized representations of speech features derived from a self-supervised speech model. By treating the speech units as pseudo-text, we can focus on the linguistic content of the speech, which can be easily associated with both speech and text modalities at the phonetic level information. By setting both the inputs and outputs of our learning problem as speech units, we propose to train an encoder-decoder model in a many-to-many spoken language translation setting, namely Unit-to-Unit Translation (UTUT). Specifically, the encoder is conditioned on the source language token to correctly understand the input spoken language, while the decoder is conditioned on the target language token to generate the translated speech in the target language. Therefore, during the training, the model can build the knowledge of how languages are comprehended and how to relate them to different languages. Since speech units can be easily associated from both audio and text by quantization and phonemization respectively, the trained model can easily transferred to text-related tasks, even if it is trained in a textless manner. We demonstrate that the proposed UTUT model can be effectively utilized not only for Speech-to-Speech Translation (S2ST) but also for multilingual Text-to-Speech Synthesis (T2S) and Text-to-Speech Translation (T2ST), requiring only minimal fine-tuning steps on text inputs. By conducting comprehensive experiments encompassing various languages, we validate the efficacy of the proposed method across diverse multilingual tasks.

</details>

### [Adversarial Training of Denoising Diffusion Model Using Dual Discriminators for High-Fidelity Multi-Speaker TTS](2308.01573.md)
**Myeongjin Ko, Yong-Hoon Choi** · 2023-08-03

<details>
<summary>Abstract</summary>

The diffusion model is capable of generating high-quality data through a probabilistic approach. However, it suffers from the drawback of slow generation speed due to the requirement of a large number of time steps. To address this limitation, recent models such as denoising diffusion implicit models (DDIM) focus on generating samples without directly modeling the probability distribution, while models like denoising diffusion generative adversarial networks (GAN) combine diffusion processes with GANs. In the field of speech synthesis, a recent diffusion speech synthesis model called DiffGAN-TTS, utilizing the structure of GANs, has been introduced and demonstrates superior performance in both speech quality and generation speed. In this paper, to further enhance the performance of DiffGAN-TTS, we propose a speech synthesis model with two discriminators: a diffusion discriminator for learning the distribution of the reverse process and a spectrogram discriminator for learning the distribution of the generated data. Objective metrics such as structural similarity index measure (SSIM), mel-cepstral distortion (MCD), F0 root mean squared error (F0 RMSE), short-time objective intelligibility (STOI), perceptual evaluation of speech quality (PESQ), as well as subjective metrics like mean opinion score (MOS), are used to evaluate the performance of the proposed model. The evaluation results show that the proposed model outperforms recent state-of-the-art models such as FastSpeech2 and DiffGAN-TTS in various metrics. Our implementation and audio samples are located on GitHub.

</details>

### [SALTTS: Leveraging Self-Supervised Speech Representations for improved Text-to-Speech Synthesis](2308.01018.md)
**Ramanan Sivaguru et.al.** · 2023-08-02

### [An end-to-end Tacotron model versus pre trained Tacotron model for Arabic text-to-speech synthesis](s2:83b48904744c080a8b0cf4efca9caae4d308d150.md)
**A. Mutawa** · 2023-08-01

### [Comparing normalizing flows and diffusion models for prosody and acoustic modelling in text-to-speech](2307.16679.md)
**Guangyan Zhang et.al.** · 2023-07-31

### [DiffProsody: Diffusion-based Latent Prosody Generation for Expressive Speech Synthesis with Prosody Conditional Adversarial Training](2307.16549.md)
**Hyung-Seok Oh et.al.** · 2023-07-31

### [VITS2: Improving Quality and Efficiency of Single-Stage Text-to-Speech with Adversarial Learning and Architecture Design](2307.16430.md)
**Jungil Kong, Jihoon Park, Beomjeong Kim, Jeongmin Kim et al.** · 2023-07-31

<details>
<summary>Abstract</summary>

Single-stage text-to-speech models have been actively studied recently, and their results have outperformed two-stage pipeline systems. Although the previous single-stage model has made great progress, there is room for improvement in terms of its intermittent unnaturalness, computational efficiency, and strong dependence on phoneme conversion. In this work, we introduce VITS2, a single-stage text-to-speech model that efficiently synthesizes a more natural speech by improving several aspects of the previous work. We propose improved structures and training mechanisms and present that the proposed methods are effective in improving naturalness, similarity of speech characteristics in a multi-speaker model, and efficiency of training and inference. Furthermore, we demonstrate that the strong dependence on phoneme conversion in previous works can be significantly reduced with our method, which allows a fully end-to-end single-stage approach.

</details>

### [Audio-visual video-to-speech synthesis with synthesized input audio](2307.16584.md)
**Triantafyllos Kefalas, Yannis Panagakis, Maja Pantic** · 2023-07-31

<details>
<summary>Abstract</summary>

Video-to-speech synthesis involves reconstructing the speech signal of a speaker from a silent video. The implicit assumption of this task is that the sound signal is either missing or contains a high amount of noise/corruption such that it is not useful for processing. Previous works in the literature either use video inputs only or employ both video and audio inputs during training, and discard the input audio pathway during inference. In this work we investigate the effect of using video and audio inputs for video-to-speech synthesis during both training and inference. In particular, we use pre-trained video-to-speech models to synthesize the missing speech signals and then train an audio-visual-to-speech synthesis model, using both the silent video and the synthesized speech as inputs, to predict the final reconstructed speech. Our experiments demonstrate that this approach is successful with both raw waveforms and mel spectrograms as target outputs.

</details>

### [METTS: Multilingual Emotional Text-to-Speech by Cross-speaker and Cross-lingual Emotion Transfer](2307.15951.md)
**Xinfa Zhu, Yi Lei, Tao Li, Yongmao Zhang et al.** · 2023-07-29

<details>
<summary>Abstract</summary>

Previous multilingual text-to-speech (TTS) approaches have considered leveraging monolingual speaker data to enable cross-lingual speech synthesis. However, such data-efficient approaches have ignored synthesizing emotional aspects of speech due to the challenges of cross-speaker cross-lingual emotion transfer - the heavy entanglement of speaker timbre, emotion, and language factors in the speech signal will make a system produce cross-lingual synthetic speech with an undesired foreign accent and weak emotion expressiveness. This paper proposes the Multilingual Emotional TTS (METTS) model to mitigate these problems, realizing both cross-speaker and cross-lingual emotion transfer. Specifically, METTS takes DelightfulTTS as the backbone model and proposes the following designs. First, to alleviate the foreign accent problem, METTS introduces multi-scale emotion modeling to disentangle speech prosody into coarse-grained and fine-grained scales, producing language-agnostic and language-specific emotion representations, respectively. Second, as a pre-processing step, formant shift-based information perturbation is applied to the reference signal for better disentanglement of speaker timbre in the speech. Third, a vector quantization-based emotion matcher is designed for reference selection, leading to decent naturalness and emotion diversity in cross-lingual synthetic speech. Experiments demonstrate the good design of METTS.

</details>

### [MSStyleTTS: Multi-Scale Style Modeling with Hierarchical Context Information for Expressive Speech Synthesis](2307.16012.md)
**Shun Lei, Yixuan Zhou, Liyang Chen, Zhiyong Wu et al.** · 2023-07-29

<details>
<summary>Abstract</summary>

Expressive speech synthesis is crucial for many human-computer interaction scenarios, such as audiobooks, podcasts, and voice assistants. Previous works focus on predicting the style embeddings at one single scale from the information within the current sentence. Whereas, context information in neighboring sentences and multi-scale nature of style in human speech are neglected, making it challenging to convert multi-sentence text into natural and expressive speech. In this paper, we propose MSStyleTTS, a style modeling method for expressive speech synthesis, to capture and predict styles at different levels from a wider range of context rather than a sentence. Two sub-modules, including multi-scale style extractor and multi-scale style predictor, are trained together with a FastSpeech 2 based acoustic model. The predictor is designed to explore the hierarchical context information by considering structural relationships in context and predict style embeddings at global-level, sentence-level and subword-level. The extractor extracts multi-scale style embedding from the ground-truth speech and explicitly guides the style prediction. Evaluations on both in-domain and out-of-domain audiobook datasets demonstrate that the proposed method significantly outperforms the three baselines. In addition, we conduct the analysis of the context information and multi-scale style representations that have never been discussed before.

</details>

### [StyleS2ST: Zero-shot Style Transfer for Direct Speech-to-speech Translation](2305.17732.md)
**Kun Song et.al.** · 2023-07-25

### [CQNV: A combination of coarsely quantized bitstream and neural vocoder for low rate speech coding](2307.13295.md)
**Youqiang Zheng, Li Xiao, Weiping Tu, Yuhong Yang et al.** · 2023-07-25

<details>
<summary>Abstract</summary>

Recently, speech codecs based on neural networks have proven to perform better than traditional methods. However, redundancy in traditional parameter quantization is visible within the codec architecture of combining the traditional codec with the neural vocoder. In this paper, we propose a novel framework named CQNV, which combines the coarsely quantized parameters of a traditional parametric codec to reduce the bitrate with a neural vocoder to improve the quality of the decoded speech. Furthermore, we introduce a parameters processing module into the neural vocoder to enhance the application of the bitstream of traditional speech coding parameters to the neural vocoder, further improving the reconstructed speech's quality. In the experiments, both subjective and objective evaluations demonstrate the effectiveness of the proposed CQNV framework. Specifically, our proposed method can achieve higher quality reconstructed speech at 1.1 kbps than Lyra and Encodec at 3 kbps.

</details>

### [SCRAPS: Speech Contrastive Representations of Acoustic and Phonetic Spaces](2307.12445.md)
**Ivan Vallés-Pérez, Grzegorz Beringer, Piotr Bilinski, Gary Cook et al.** · 2023-07-23

<details>
<summary>Abstract</summary>

Numerous examples in the literature proved that deep learning models have the ability to work well with multimodal data. Recently, CLIP has enabled deep learning systems to learn shared latent spaces between images and text descriptions, with outstanding zero- or few-shot results in downstream tasks. In this paper we explore the same idea proposed by CLIP but applied to the speech domain, where the phonetic and acoustic spaces usually coexist. We train a CLIP-based model with the aim to learn shared representations of phonetic and acoustic spaces. The results show that the proposed model is sensible to phonetic changes, with a 91% of score drops when replacing 20% of the phonemes at random, while providing substantial robustness against different kinds of noise, with a 10% performance drop when mixing the audio with 75% of Gaussian noise. We also provide empirical evidence showing that the resulting embeddings are useful for a variety of downstream applications, such as intelligibility evaluation and the ability to leverage rich pre-trained phonetic embeddings in speech generation task. Finally, we discuss potential applications with interesting implications for the speech generation and recognition fields.

</details>

### [SC VALL-E: Style-Controllable Zero-Shot Text to Speech Synthesizer](2307.10550.md)
**Daegyeom Kim et.al.** · 2023-07-20

### [An analysis on the effects of speaker embedding choice in non auto-regressive TTS](2307.09898.md)
**Adriana Stan, Johannah O'Mahony** · 2023-07-19

<details>
<summary>Abstract</summary>

In this paper we introduce a first attempt on understanding how a non-autoregressive factorised multi-speaker speech synthesis architecture exploits the information present in different speaker embedding sets. We analyse if jointly learning the representations, and initialising them from pretrained models determine any quality improvements for target speaker identities. In a separate analysis, we investigate how the different sets of embeddings impact the network's core speech abstraction (i.e. zero conditioned) in terms of speaker identity and representation learning. We show that, regardless of the used set of embeddings and learning strategy, the network can handle various speaker identities equally well, with barely noticeable variations in speech output quality, and that speaker leakage within the core structure of the synthesis system is inevitable in the standard training procedures adopted thus far.

</details>

### [SLMGAN: Exploiting Speech Language Model Representations for Unsupervised Zero-Shot Voice Conversion in GANs](2307.09435.md)
**Yinghao Aaron Li et.al.** · 2023-07-18

### [Single and Multi-Speaker Cloned Voice Detection: From Perceptual to Learned Features](2307.07683.md)
**Sarah Barrington, Romit Barua, Gautham Koorma, Hany Farid** · 2023-07-15

<details>
<summary>Abstract</summary>

Synthetic-voice cloning technologies have seen significant advances in recent years, giving rise to a range of potential harms. From small- and large-scale financial fraud to disinformation campaigns, the need for reliable methods to differentiate real and synthesized voices is imperative. We describe three techniques for differentiating a real from a cloned voice designed to impersonate a specific person. These three approaches differ in their feature extraction stage with low-dimensional perceptual features offering high interpretability but lower accuracy, to generic spectral features, and end-to-end learned features offering less interpretability but higher accuracy. We show the efficacy of these approaches when trained on a single speaker's voice and when trained on multiple voices. The learned features consistently yield an equal error rate between 0% and 4%, and are reasonably robust to adversarial laundering.

</details>

### [Rhythm Modeling for Voice Conversion](2307.06040.md)
**Benjamin van Niekerk, Marc-André Carbonneau, Herman Kamper** · 2023-07-12

<details>
<summary>Abstract</summary>

Voice conversion aims to transform source speech into a different target voice. However, typical voice conversion systems do not account for rhythm, which is an important factor in the perception of speaker identity. To bridge this gap, we introduce Urhythmic-an unsupervised method for rhythm conversion that does not require parallel data or text transcriptions. Using self-supervised representations, we first divide source audio into segments approximating sonorants, obstruents, and silences. Then we model rhythm by estimating speaking rate or the duration distribution of each segment type. Finally, we match the target speaking rate or rhythm by time-stretching the speech segments. Experiments show that Urhythmic outperforms existing unsupervised methods in terms of quality and prosody. Code and checkpoints: https://github.com/bshall/urhythmic. Audio demo page: https://ubisoft-laforge.github.io/speech/urhythmic.

</details>

### [On the Use of Self-Supervised Speech Representations in Spontaneous Speech Synthesis](2307.05132.md)
**Siyang Wang et.al.** · 2023-07-11

### [Interpretable Style Transfer for Text-to-Speech with ControlVAE and Diffusion Bridge](2306.04301.md)
**Wenhao Guan et.al.** · 2023-07-11

### [The Ethical Implications of Generative Audio Models: A Systematic Literature Review](2307.05527.md)
**Julia Barnett** · 2023-07-07

<details>
<summary>Abstract</summary>

Generative audio models typically focus their applications in music and speech generation, with recent models having human-like quality in their audio output. This paper conducts a systematic literature review of 884 papers in the area of generative audio models in order to both quantify the degree to which researchers in the field are considering potential negative impacts and identify the types of ethical implications researchers in this area need to consider. Though 65% of generative audio research papers note positive potential impacts of their work, less than 10% discuss any negative impacts. This jarringly small percentage of papers considering negative impact is particularly worrying because the issues brought to light by the few papers doing so are raising serious ethical implications and concerns relevant to the broader field such as the potential for fraud, deep-fakes, and copyright infringement. By quantifying this lack of ethical consideration in generative audio research and identifying key areas of potential harm, this paper lays the groundwork for future work in the field at a critical point in time in order to guide more conscientious research as this field progresses.

</details>

### [Deep Speech Synthesis from MRI-Based Articulatory Representations](2307.02471.md)
**Peter Wu, Tingle Li, Yijing Lu, Yubin Zhang et al.** · 2023-07-05

<details>
<summary>Abstract</summary>

In this paper, we study articulatory synthesis, a speech synthesis method using human vocal tract information that offers a way to develop efficient, generalizable and interpretable synthesizers. While recent advances have enabled intelligible articulatory synthesis using electromagnetic articulography (EMA), these methods lack critical articulatory information like excitation and nasality, limiting generalization capabilities. To bridge this gap, we propose an alternative MRI-based feature set that covers a much more extensive articulatory space than EMA. We also introduce normalization and denoising procedures to enhance the generalizability of deep learning methods trained on MRI data. Moreover, we propose an MRI-to-speech model that improves both computational efficiency and speech fidelity. Finally, through a series of ablations, we show that the proposed MRI representation is more comprehensive than EMA and identify the most suitable MRI feature subset for articulatory synthesis.

</details>

### [ContextSpeech: Expressive and Efficient Text-to-Speech for Paragraph Reading](2307.00782.md)
**Yujia Xiao, Shaofei Zhang, Xi Wang, Xu Tan et al.** · 2023-07-03

<details>
<summary>Abstract</summary>

While state-of-the-art Text-to-Speech systems can generate natural speech of very high quality at sentence level, they still meet great challenges in speech generation for paragraph / long-form reading. Such deficiencies are due to i) ignorance of cross-sentence contextual information, and ii) high computation and memory cost for long-form synthesis. To address these issues, this work develops a lightweight yet effective TTS system, ContextSpeech. Specifically, we first design a memory-cached recurrence mechanism to incorporate global text and speech context into sentence encoding. Then we construct hierarchically-structured textual semantics to broaden the scope for global context enhancement. Additionally, we integrate linearized self-attention to improve model efficiency. Experiments show that ContextSpeech significantly improves the voice quality and prosody expressiveness in paragraph reading with competitive model efficiency. Audio samples are available at: https://contextspeech.github.io/demo/

</details>

### [RobustL2S: Speaker-Specific Lip-to-Speech Synthesis exploiting Self-Supervised Representations](2307.01233.md)
**Neha Sahipjohn, Neil Shah, Vishal Tambrahalli, Vineet Gandhi** · 2023-07-03

<details>
<summary>Abstract</summary>

Significant progress has been made in speaker dependent Lip-to-Speech synthesis, which aims to generate speech from silent videos of talking faces. Current state-of-the-art approaches primarily employ non-autoregressive sequence-to-sequence architectures to directly predict mel-spectrograms or audio waveforms from lip representations. We hypothesize that the direct mel-prediction hampers training/model efficiency due to the entanglement of speech content with ambient information and speaker characteristics. To this end, we propose RobustL2S, a modularized framework for Lip-to-Speech synthesis. First, a non-autoregressive sequence-to-sequence model maps self-supervised visual features to a representation of disentangled speech content. A vocoder then converts the speech features into raw waveforms. Extensive evaluations confirm the effectiveness of our setup, achieving state-of-the-art performance on the unconstrained Lip2Wav dataset and the constrained GRID and TCD-TIMIT datasets. Speech samples from RobustL2S can be found at https://neha-sherin.github.io/RobustL2S/

</details>

### [An End-to-End Multi-Module Audio Deepfake Generation System for ADD Challenge 2023](2307.00729.md)
**Sheng Zhao, Qilong Yuan, Yibo Duan, Zhuoyue Chen** · 2023-07-03

<details>
<summary>Abstract</summary>

The task of synthetic speech generation is to generate language content from a given text, then simulating fake human voice.The key factors that determine the effect of synthetic speech generation mainly include speed of generation, accuracy of word segmentation, naturalness of synthesized speech, etc. This paper builds an end-to-end multi-module synthetic speech generation model, including speaker encoder, synthesizer based on Tacotron2, and vocoder based on WaveRNN. In addition, we perform a lot of comparative experiments on different datasets and various model structures. Finally, we won the first place in the ADD 2023 challenge Track 1.1 with the weighted deception success rate (WDSR) of 44.97%.

</details>

### [High-Quality Automatic Voice Over with Accurate Alignment: Supervision through Self-Supervised Discrete Speech Units](2306.17005.md)
**Junchen Lu, Berrak Sisman, Mingyang Zhang, Haizhou Li** · 2023-06-29

<details>
<summary>Abstract</summary>

The goal of Automatic Voice Over (AVO) is to generate speech in sync with a silent video given its text script. Recent AVO frameworks built upon text-to-speech synthesis (TTS) have shown impressive results. However, the current AVO learning objective of acoustic feature reconstruction brings in indirect supervision for inter-modal alignment learning, thus limiting the synchronization performance and synthetic speech quality. To this end, we propose a novel AVO method leveraging the learning objective of self-supervised discrete speech unit prediction, which not only provides more direct supervision for the alignment learning, but also alleviates the mismatch between the text-video context and acoustic features. Experimental results show that our proposed method achieves remarkable lip-speech synchronization and high speech quality by outperforming baselines in both objective and subjective evaluations. Code and speech samples are publicly available.

</details>

### [Deep Learning-based F0 Synthesis for Speaker Anonymization](2306.16860.md)
**Ünal Ege Gaznepoglu, Nils Peters** · 2023-06-29

<details>
<summary>Abstract</summary>

Voice conversion for speaker anonymization is an emerging concept for privacy protection. In a deep learning setting, this is achieved by extracting multiple features from speech, altering the speaker identity, and waveform synthesis. However, many existing systems do not modify fundamental frequency (F0) trajectories, which convey prosody information and can reveal speaker identity. Moreover, mismatch between F0 and other features can degrade speech quality and intelligibility. In this paper, we formally introduce a method that synthesizes F0 trajectories from other speech features and evaluate its reconstructional capabilities. Then we test our approach within a speaker anonymization framework, comparing it to a baseline and a state-of-the-art F0 modification that utilizes speaker information. The results show that our method improves both speaker anonymity, measured by the equal error rate, and utility, measured by the word error rate.

</details>

### [Learning Multilingual Expressive Speech Representation for Prosody Prediction without Parallel Data](2306.17199.md)
**Jarod Duret, Titouan Parcollet, Yannick Estève** · 2023-06-29

<details>
<summary>Abstract</summary>

We propose a method for speech-to-speech emotionpreserving translation that operates at the level of discrete speech units. Our approach relies on the use of multilingual emotion embedding that can capture affective information in a language-independent manner. We show that this embedding can be used to predict the pitch and duration of speech units in a target language, allowing us to resynthesize the source speech signal with the same emotional content. We evaluate our approach to English and French speech signals and show that it outperforms a baseline method that does not use emotional information, including when the emotion embedding is extracted from a different language. Even if this preliminary study does not address directly the machine translation issue, our results demonstrate the effectiveness of our approach for cross-lingual emotion preservation in the context of speech resynthesis.

</details>

### [Improving the quality of neural TTS using long-form content and multi-speaker multi-style modeling](2212.10075.md)
**Tuomo Raitio et.al.** · 2023-06-28

### [EmoSpeech: Guiding FastSpeech2 Towards Emotional Text to Speech](2307.00024.md)
**Daria Diatlova, Vitaly Shutov** · 2023-06-28

<details>
<summary>Abstract</summary>

State-of-the-art speech synthesis models try to get as close as possible to the human voice. Hence, modelling emotions is an essential part of Text-To-Speech (TTS) research. In our work, we selected FastSpeech2 as the starting point and proposed a series of modifications for synthesizing emotional speech. According to automatic and human evaluation, our model, EmoSpeech, surpasses existing models regarding both MOS score and emotion recognition accuracy in generated speech. We provided a detailed ablation study for every extension to FastSpeech2 architecture that forms EmoSpeech. The uneven distribution of emotions in the text is crucial for better, synthesized speech and intonation perception. Our model includes a conditioning mechanism that effectively handles this issue by allowing emotions to contribute to each phone with varying intensity levels. The human assessment indicates that proposed modifications generate audio with higher MOS and emotional expressiveness.

</details>

### [UnitSpeech: Speaker-adaptive Speech Synthesis with Untranscribed Data](2306.16083.md)
**Heeseung Kim, Sungwon Kim, Jiheum Yeom, Sungroh Yoon** · 2023-06-28

<details>
<summary>Abstract</summary>

We propose UnitSpeech, a speaker-adaptive speech synthesis method that fine-tunes a diffusion-based text-to-speech (TTS) model using minimal untranscribed data. To achieve this, we use the self-supervised unit representation as a pseudo transcript and integrate the unit encoder into the pre-trained TTS model. We train the unit encoder to provide speech content to the diffusion-based decoder and then fine-tune the decoder for speaker adaptation to the reference speaker using a single $<$unit, speech$>$ pair. UnitSpeech performs speech synthesis tasks such as TTS and voice conversion (VC) in a personalized manner without requiring model re-training for each task. UnitSpeech achieves comparable and superior results on personalized TTS and any-to-any VC tasks compared to previous baselines. Our model also shows widespread adaptive performance on real-world data and other tasks that use a unit sequence as input.

</details>

### [Two-Stage Voice Anonymization for Enhanced Privacy](2306.16069.md)
**Francesco Nespoli, Daniel Barreda, Joerg Bitzer, Patrick A. Naylor** · 2023-06-28

<details>
<summary>Abstract</summary>

In recent years, the need for privacy preservation when manipulating or storing personal data, including speech , has become a major issue. In this paper, we present a system addressing the speaker-level anonymization problem. We propose and evaluate a two-stage anonymization pipeline exploiting a state-of-the-art anonymization model described in the Voice Privacy Challenge 2022 in combination with a zero-shot voice conversion architecture able to capture speaker characteristics from a few seconds of speech. We show this architecture can lead to strong privacy preservation while preserving pitch information. Finally, we propose a new compressed metric to evaluate anonymization systems in privacy scenarios with different constraints on privacy and utility.

</details>

### [Fake the Real: Backdoor Attack on Deep Speech Classification via Voice Conversion](2306.15875.md)
**Zhe Ye, Terui Mao, Li Dong, Diqun Yan** · 2023-06-28

<details>
<summary>Abstract</summary>

Deep speech classification has achieved tremendous success and greatly promoted the emergence of many real-world applications. However, backdoor attacks present a new security threat to it, particularly with untrustworthy third-party platforms, as pre-defined triggers set by the attacker can activate the backdoor. Most of the triggers in existing speech backdoor attacks are sample-agnostic, and even if the triggers are designed to be unnoticeable, they can still be audible. This work explores a backdoor attack that utilizes sample-specific triggers based on voice conversion. Specifically, we adopt a pre-trained voice conversion model to generate the trigger, ensuring that the poisoned samples does not introduce any additional audible noise. Extensive experiments on two speech classification tasks demonstrate the effectiveness of our attack. Furthermore, we analyzed the specific scenarios that activated the proposed backdoor and verified its resistance against fine-tuning.

</details>

### [GenerTTS: Pronunciation Disentanglement for Timbre and Style Generalization in Cross-Lingual Text-to-Speech](2306.15304.md)
**Yahuan Cong, Haoyu Zhang, Haopeng Lin, Shichao Liu et al.** · 2023-06-27

<details>
<summary>Abstract</summary>

Cross-lingual timbre and style generalizable text-to-speech (TTS) aims to synthesize speech with a specific reference timbre or style that is never trained in the target language. It encounters the following challenges: 1) timbre and pronunciation are correlated since multilingual speech of a specific speaker is usually hard to obtain; 2) style and pronunciation are mixed because the speech style contains language-agnostic and language-specific parts. To address these challenges, we propose GenerTTS, which mainly includes the following works: 1) we elaborately design a HuBERT-based information bottleneck to disentangle timbre and pronunciation/style; 2) we minimize the mutual information between style and language to discard the language-specific information in the style embedding. The experiments indicate that GenerTTS outperforms baseline systems in terms of style similarity and pronunciation accuracy, and enables cross-lingual timbre and style generalization.

</details>

### [The Singing Voice Conversion Challenge 2023](2306.14422.md)
**Wen-Chin Huang, Lester Phillip Violeta, Songxiang Liu, Jiatong Shi et al.** · 2023-06-26

<details>
<summary>Abstract</summary>

We present the latest iteration of the voice conversion challenge (VCC) series, a bi-annual scientific event aiming to compare and understand different voice conversion (VC) systems based on a common dataset. This year we shifted our focus to singing voice conversion (SVC), thus named the challenge the Singing Voice Conversion Challenge (SVCC). A new database was constructed for two tasks, namely in-domain and cross-domain SVC. The challenge was run for two months, and in total we received 26 submissions, including 2 baselines. Through a large-scale crowd-sourced listening test, we observed that for both tasks, although human-level naturalness was achieved by the top system, no team was able to obtain a similarity score as high as the target speakers. Also, as expected, cross-domain SVC is harder than in-domain SVC, especially in the similarity aspect. We also investigated whether existing objective measurements were able to predict perceptual performance, and found that only few of them could reach a significant correlation.

</details>

### [DSE-TTS: Dual Speaker Embedding for Cross-Lingual Text-to-Speech](2306.14145.md)
**Sen Liu et.al.** · 2023-06-25

### [Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale](2306.15687.md)
**Matthew Le, Apoorv Vyas, Bowen Shi, Brian Karrer et al.** · 2023-06-23

<details>
<summary>Abstract</summary>

Large-scale generative models such as GPT and DALL-E have revolutionized the research community. These models not only generate high fidelity outputs, but are also generalists which can solve tasks not explicitly taught. In contrast, speech generative models are still primitive in terms of scale and task generalization. In this paper, we present Voicebox, the most versatile text-guided generative model for speech at scale. Voicebox is a non-autoregressive flow-matching model trained to infill speech, given audio context and text, trained on over 50K hours of speech that are not filtered or enhanced. Similar to GPT, Voicebox can perform many different tasks through in-context learning, but is more flexible as it can also condition on future context. Voicebox can be used for mono or cross-lingual zero-shot text-to-speech synthesis, noise removal, content editing, style conversion, and diverse sample generation. In particular, Voicebox outperforms the state-of-the-art zero-shot TTS model VALL-E on both intelligibility (5.9% vs 1.9% word error rates) and audio similarity (0.580 vs 0.681) while being up to 20 times faster. Audio samples can be found in \url{https://voicebox.metademolab.com}.

</details>

### [Visual-Aware Text-to-Speech](2306.12020.md)
**Mohan Zhou, Yalong Bai, Wei Zhang, Ting Yao et al.** · 2023-06-21

<details>
<summary>Abstract</summary>

Dynamically synthesizing talking speech that actively responds to a listening head is critical during the face-to-face interaction. For example, the speaker could take advantage of the listener's facial expression to adjust the tones, stressed syllables, or pauses. In this work, we present a new visual-aware text-to-speech (VA-TTS) task to synthesize speech conditioned on both textual inputs and sequential visual feedback (e.g., nod, smile) of the listener in face-to-face communication. Different from traditional text-to-speech, VA-TTS highlights the impact of visual modality. On this newly-minted task, we devise a baseline model to fuse phoneme linguistic information and listener visual signals for speech synthesis. Extensive experiments on multimodal conversation dataset ViCo-X verify our proposal for generating more natural audio with scenario-appropriate rhythm and prosody.

</details>

### [Cross-lingual Prosody Transfer for Expressive Machine Dubbing](2306.11658.md)
**Jakub Swiatkowski, Duo Wang, Mikolaj Babianski, Patrick Lumban Tobing et al.** · 2023-06-20

<details>
<summary>Abstract</summary>

Prosody transfer is well-studied in the context of expressive speech synthesis. Cross-lingual prosody transfer, however, is challenging and has been under-explored to date. In this paper, we present a novel solution to learn prosody representations that are transferable across languages and speakers for machine dubbing of expressive multimedia contents. Multimedia contents often contain field recordings. To enable prosody transfer from noisy audios, we introduce a novel noise modelling module that disentangles noise conditioning from prosody conditioning, and thereby gains independent control of noise levels in the synthesised speech. We augment noisy training data with clean data to improve the ability of the model to map the denoised reference audio to clean speech. Our proposed system can generate speech with context-matching prosody and closes the gap between a strong baseline and human expressive dialogs by 11.2%.

</details>

### [Phase Repair for Time-Domain Convolutional Neural Networks in Music Super-Resolution](2306.11282.md)
**Yenan Zhang, Guilly Kolkman, Hiroshi Watanabe** · 2023-06-20

<details>
<summary>Abstract</summary>

Audio Super-Resolution (SR) is an important topic as low-resolution recordings are ubiquitous in daily life. In this paper, we focus on the music SR task, which is challenging due to the wide frequency response and dynamic range of music. Many models are designed in time domain to jointly process magnitude and phase of audio signals. However, prior works show that approaches using Time-Domain Convolutional Neural Network (TD-CNN) tend to produce annoying artifacts in their waveform outputs, and the cause of the artifacts is yet to be identified. To the best of our knowledge, this work is the first to demonstrate the artifacts in TD-CNNs are caused by the phase distortion via a subjective experiment. We further propose Time-Domain Phase Repair (TD-PR), which uses a neural vocoder pre-trained on the wide-band data to repair the phase components in the waveform outputs of TD-CNNs. Although the vocoder and TD-CNNs are independently trained, the proposed TD-PR obtained better mean opinion score, significantly improving the perceptual quality of TD-CNN baselines. Since the proposed TD-PR only repairs the phase components of the waveforms, the improved perceptual quality in turn indicates that phase distortion has been the cause of the annoying artifacts of TD-CNNs. Moreover, a single pretrained vocoder can be directly applied to arbitrary TD-CNNs without additional adaptation. Therefore, we apply TD-PR to three TD-CNNs that have different architecture and parameter amount. Consistent improvements are observed when TD-PR is applied to all three TD-CNN baselines. Audio samples are available on the demo page.

</details>

### [LM-VC: Zero-shot Voice Conversion via Speech Generation based on Language Models](2306.10521.md)
**Zhichao Wang, Yuanzhe Chen, Lei Xie, Qiao Tian et al.** · 2023-06-18

<details>
<summary>Abstract</summary>

Language model (LM) based audio generation frameworks, e.g., AudioLM, have recently achieved new state-of-the-art performance in zero-shot audio generation. In this paper, we explore the feasibility of LMs for zero-shot voice conversion. An intuitive approach is to follow AudioLM - Tokenizing speech into semantic and acoustic tokens respectively by HuBERT and SoundStream, and converting source semantic tokens to target acoustic tokens conditioned on acoustic tokens of the target speaker. However, such an approach encounters several issues: 1) the linguistic content contained in semantic tokens may get dispersed during multi-layer modeling while the lengthy speech input in the voice conversion task makes contextual learning even harder; 2) the semantic tokens still contain speaker-related information, which may be leaked to the target speech, lowering the target speaker similarity; 3) the generation diversity in the sampling of the LM can lead to unexpected outcomes during inference, leading to unnatural pronunciation and speech quality degradation. To mitigate these problems, we propose LM-VC, a two-stage language modeling approach that generates coarse acoustic tokens for recovering the source linguistic content and target speaker's timbre, and then reconstructs the fine for acoustic details as converted speech. Specifically, to enhance content preservation and facilitates better disentanglement, a masked prefix LM with a mask prediction strategy is used for coarse acoustic modeling. This model is encouraged to recover the masked content from the surrounding context and generate target speech based on the target speaker's utterance and corrupted semantic tokens. Besides, to further alleviate the sampling error in the generation, an external LM, which employs window attention to capture the local acoustic relations, is introduced to participate in the coarse acoustic modeling.

</details>

### [CML-TTS A Multilingual Dataset for Speech Synthesis in Low-Resource Languages](2306.10097.md)
**Frederico S. Oliveira et.al.** · 2023-06-16

### [Low-Resource Text-to-Speech Using Specific Data and Noise Augmentation](2306.10152.md)
**Kishor Kayyar Lakshminarayana, Christian Dittmar, Nicola Pia, Emanuël Habets** · 2023-06-16

<details>
<summary>Abstract</summary>

Many neural text-to-speech architectures can synthesize nearly natural speech from text inputs. These architectures must be trained with tens of hours of annotated and high-quality speech data. Compiling such large databases for every new voice requires a lot of time and effort. In this paper, we describe a method to extend the popular Tacotron-2 architecture and its training with data augmentation to enable single-speaker synthesis using a limited amount of specific training data. In contrast to elaborate augmentation methods proposed in the literature, we use simple stationary noises for data augmentation. Our extension is easy to implement and adds almost no computational overhead during training and inference. Using only two hours of training data, our approach was rated by human listeners to be on par with the baseline Tacotron-2 trained with 23.5 hours of LJSpeech data. In addition, we tested our model with a semantically unpredictable sentences test, which showed that both models exhibit similar intelligibility levels.

</details>

### [Investigating the Utility of Surprisal from Large Language Models for Speech Synthesis Prosody](2306.09814.md)
**Sofoklis Kakouros, Juraj Šimko, Martti Vainio, Antti Suni** · 2023-06-16

<details>
<summary>Abstract</summary>

This paper investigates the use of word surprisal, a measure of the predictability of a word in a given context, as a feature to aid speech synthesis prosody. We explore how word surprisal extracted from large language models (LLMs) correlates with word prominence, a signal-based measure of the salience of a word in a given discourse. We also examine how context length and LLM size affect the results, and how a speech synthesizer conditioned with surprisal values compares with a baseline system. To evaluate these factors, we conducted experiments using a large corpus of English text and LLMs of varying sizes. Our results show that word surprisal and word prominence are moderately correlated, suggesting that they capture related but distinct aspects of language use. We find that length of context and size of the LLM impact the correlations, but not in the direction anticipated, with longer contexts and larger LLMs generally underpredicting prominent words in a nearly linear manner. We demonstrate that, in line with these findings, a speech synthesizer conditioned with surprisal values provides a minimal improvement over the baseline with the results suggesting a limited effect of using surprisal values for eliciting appropriate prominence patterns.

</details>

### [Diff-TTSG: Denoising probabilistic integrated speech and gesture synthesis](2306.09417.md)
**Shivam Mehta, Siyang Wang, Simon Alexanderson, Jonas Beskow et al.** · 2023-06-15

<details>
<summary>Abstract</summary>

With read-aloud speech synthesis achieving high naturalness scores, there is a growing research interest in synthesising spontaneous speech. However, human spontaneous face-to-face conversation has both spoken and non-verbal aspects (here, co-speech gestures). Only recently has research begun to explore the benefits of jointly synthesising these two modalities in a single system. The previous state of the art used non-probabilistic methods, which fail to capture the variability of human speech and motion, and risk producing oversmoothing artefacts and sub-optimal synthesis quality. We present the first diffusion-based probabilistic model, called Diff-TTSG, that jointly learns to synthesise speech and gestures together. Our method can be trained on small datasets from scratch. Furthermore, we describe a set of careful uni- and multi-modal subjective tests for evaluating integrated speech and gesture synthesis systems, and use them to validate our proposed approach. Please see https://shivammehta25.github.io/Diff-TTSG/ for video examples, data, and code.

</details>

### [Towards Building Voice-based Conversational Recommender Systems: Datasets, Potential Solutions, and Prospects](2306.08219.md)
**Xinghua Qu, Hongyang Liu, Zhu Sun, Xiang Yin et al.** · 2023-06-14

<details>
<summary>Abstract</summary>

Conversational recommender systems (CRSs) have become crucial emerging research topics in the field of RSs, thanks to their natural advantages of explicitly acquiring user preferences via interactive conversations and revealing the reasons behind recommendations. However, the majority of current CRSs are text-based, which is less user-friendly and may pose challenges for certain users, such as those with visual impairments or limited writing and reading abilities. Therefore, for the first time, this paper investigates the potential of voice-based CRS (VCRSs) to revolutionize the way users interact with RSs in a natural, intuitive, convenient, and accessible fashion. To support such studies, we create two VCRSs benchmark datasets in the e-commerce and movie domains, after realizing the lack of such datasets through an exhaustive literature review. Specifically, we first empirically verify the benefits and necessity of creating such datasets. Thereafter, we convert the user-item interactions to text-based conversations through the ChatGPT-driven prompts for generating diverse and natural templates, and then synthesize the corresponding audios via the text-to-speech model. Meanwhile, a number of strategies are delicately designed to ensure the naturalness and high quality of voice conversations. On this basis, we further explore the potential solutions and point out possible directions to build end-to-end VCRSs by seamlessly extracting and integrating voice-based inputs, thus delivering performance-enhanced, self-explainable, and user-friendly VCRSs. Our study aims to establish the foundation and motivate further pioneering research in the emerging field of VCRSs. This aligns with the principles of explainable AI and AI for social good, viz., utilizing technology's potential to create a fair, sustainable, and just world.

</details>

### [PauseSpeech: Natural Speech Synthesis via Pre-trained Language Model and Pause-based Prosody Modeling](2306.07489.md)
**Ji-Sang Hwang et.al.** · 2023-06-13

### [CrossSpeech: Speaker-independent Acoustic Representation for Cross-lingual Speech Synthesis](2302.14370.md)
**Ji-Hoon Kim et.al.** · 2023-06-12

### [HiddenSinger: High-Quality Singing Voice Synthesis via Neural Audio Codec and Latent Diffusion Models](2306.06814.md)
**Ji-Sang Hwang, Sang-Hoon Lee, Seong-Whan Lee** · 2023-06-12

<details>
<summary>Abstract</summary>

Recently, denoising diffusion models have demonstrated remarkable performance among generative models in various domains. However, in the speech domain, the application of diffusion models for synthesizing time-varying audio faces limitations in terms of complexity and controllability, as speech synthesis requires very high-dimensional samples with long-term acoustic features. To alleviate the challenges posed by model complexity in singing voice synthesis, we propose HiddenSinger, a high-quality singing voice synthesis system using a neural audio codec and latent diffusion models. To ensure high-fidelity audio, we introduce an audio autoencoder that can encode audio into an audio codec as a compressed representation and reconstruct the high-fidelity audio from the low-dimensional compressed latent vector. Subsequently, we use the latent diffusion models to sample a latent representation from a musical score. In addition, our proposed model is extended to an unsupervised singing voice learning framework, HiddenSinger-U, to train the model using an unlabeled singing voice dataset. Experimental results demonstrate that our model outperforms previous models in terms of audio quality. Furthermore, the HiddenSinger-U can synthesize high-quality singing voices of speakers trained solely on unlabeled data.

</details>

### [Mandarin Electrolaryngeal Speech Voice Conversion using Cross-domain Features](2306.06653.md)
**Hsin-Hao Chen, Yung-Lun Chien, Ming-Chi Yen, Shu-Wei Tsai et al.** · 2023-06-11

<details>
<summary>Abstract</summary>

Patients who have had their entire larynx removed, including the vocal folds, owing to throat cancer may experience difficulties in speaking. In such cases, electrolarynx devices are often prescribed to produce speech, which is commonly referred to as electrolaryngeal speech (EL speech). However, the quality and intelligibility of EL speech are poor. To address this problem, EL voice conversion (ELVC) is a method used to improve the intelligibility and quality of EL speech. In this paper, we propose a novel ELVC system that incorporates cross-domain features, specifically spectral features and self-supervised learning (SSL) embeddings. The experimental results show that applying cross-domain features can notably improve the conversion performance for the ELVC task compared with utilizing only traditional spectral features.

</details>

### [Audio-Visual Mandarin Electrolaryngeal Speech Voice Conversion](2306.06652.md)
**Yung-Lun Chien, Hsin-Hao Chen, Ming-Chi Yen, Shu-Wei Tsai et al.** · 2023-06-11

<details>
<summary>Abstract</summary>

Electrolarynx is a commonly used assistive device to help patients with removed vocal cords regain their ability to speak. Although the electrolarynx can generate excitation signals like the vocal cords, the naturalness and intelligibility of electrolaryngeal (EL) speech are very different from those of natural (NL) speech. Many deep-learning-based models have been applied to electrolaryngeal speech voice conversion (ELVC) for converting EL speech to NL speech. In this study, we propose a multimodal voice conversion (VC) model that integrates acoustic and visual information into a unified network. We compared different pre-trained models as visual feature extractors and evaluated the effectiveness of these features in the ELVC task. The experimental results demonstrate that the proposed multimodal VC model outperforms single-modal models in both objective and subjective metrics, suggesting that the integration of visual information can significantly improve the quality of ELVC.

</details>

### [Vocoder-Free Non-Parallel Conversion of Whispered Speech With Masked Cycle-Consistent Generative Adversarial Networks](2306.06514.md)
**Dominik Wagner, Ilja Baumann, Tobias Bocklet** · 2023-06-10

<details>
<summary>Abstract</summary>

Cycle-consistent generative adversarial networks have been widely used in non-parallel voice conversion (VC). Their ability to learn mappings between source and target features without relying on parallel training data eliminates the need for temporal alignments. However, most methods decouple the conversion of acoustic features from synthesizing the audio signal by using separate models for conversion and waveform synthesis. This work unifies conversion and synthesis into a single model, thereby eliminating the need for a separate vocoder. By leveraging cycle-consistent training and a self-supervised auxiliary training task, our model is able to efficiently generate converted high-quality raw audio waveforms. Subjective listening tests showed that our unified approach achieved improvements of up to 6.7% relative to the baseline in whispered VC. Mean opinion score predictions also yielded stable results in conventional VC (between 0.5% and 2.4% relative improvement).

</details>

### [Learning Emotional Representations from Imbalanced Speech Data for Speech Emotion Recognition and Emotional Text-to-Speech](2306.05709.md)
**Shijun Wang et.al.** · 2023-06-09

### [Boosting Fast and High-Quality Speech Synthesis with Linear Diffusion](2306.05708.md)
**Haogeng Liu, Tao Wang, Jie Cao, Ran He et al.** · 2023-06-09

<details>
<summary>Abstract</summary>

Denoising Diffusion Probabilistic Models have shown extraordinary ability on various generative tasks. However, their slow inference speed renders them impractical in speech synthesis. This paper proposes a linear diffusion model (LinDiff) based on an ordinary differential equation to simultaneously reach fast inference and high sample quality. Firstly, we employ linear interpolation between the target and noise to design a diffusion sequence for training, while previously the diffusion path that links the noise and target is a curved segment. When decreasing the number of sampling steps (i.e., the number of line segments used to fit the path), the ease of fitting straight lines compared to curves allows us to generate higher quality samples from a random noise with fewer iterations. Secondly, to reduce computational complexity and achieve effective global modeling of noisy speech, LinDiff employs a patch-based processing approach that partitions the input signal into small patches. The patch-wise token leverages Transformer architecture for effective modeling of global information. Adversarial training is used to further improve the sample quality with decreased sampling steps. We test proposed method with speech synthesis conditioned on acoustic feature (Mel-spectrograms). Experimental results verify that our model can synthesize high-quality speech even with only one diffusion step. Both subjective and objective evaluations demonstrate that our model can synthesize speech of a quality comparable to that of autoregressive models with faster synthesis speed (3 diffusion steps).

</details>

### [VIFS: An End-to-End Variational Inference for Foley Sound Synthesis](2306.05004.md)
**Junhyeok Lee, Hyeonuk Nam, Yong-Hwa Park** · 2023-06-08

<details>
<summary>Abstract</summary>

The goal of DCASE 2023 Challenge Task 7 is to generate various sound clips for Foley sound synthesis (FSS) by "category-to-sound" approach. "Category" is expressed by a single index while corresponding "sound" covers diverse and different sound examples. To generate diverse sounds for a given category, we adopt VITS, a text-to-speech (TTS) model with variational inference. In addition, we apply various techniques from speech synthesis including PhaseAug and Avocodo. Different from TTS models which generate short pronunciation from phonemes and speaker identity, the category-to-sound problem requires generating diverse sounds just from a category index. To compensate for the difference while maintaining consistency within each audio clip, we heavily modified the prior encoder to enhance consistency with posterior latent variables. This introduced additional Gaussian on the prior encoder which promotes variance within the category. With these modifications, we propose VIFS, variational inference for end-to-end Foley sound synthesis, which generates diverse high-quality sounds.

</details>

### [Mega-TTS: Zero-Shot Text-to-Speech at Scale with Intrinsic Inductive Bias](2306.03509.md)
**Ziyue Jiang et.al.** · 2023-06-06

### [PITS: Variational Pitch Inference without Fundamental Frequency for End-to-End Pitch-controllable TTS](2302.12391.md)
**Junhyeok Lee et.al.** · 2023-06-06

### [Ada-TTA: Towards Adaptive High-Quality Text-to-Talking Avatar Synthesis](2306.03504.md)
**Zhenhui Ye, Ziyue Jiang, Yi Ren, Jinglin Liu et al.** · 2023-06-06

<details>
<summary>Abstract</summary>

We are interested in a novel task, namely low-resource text-to-talking avatar. Given only a few-minute-long talking person video with the audio track as the training data and arbitrary texts as the driving input, we aim to synthesize high-quality talking portrait videos corresponding to the input text. This task has broad application prospects in the digital human industry but has not been technically achieved yet due to two challenges: (1) It is challenging to mimic the timbre from out-of-domain audio for a traditional multi-speaker Text-to-Speech system. (2) It is hard to render high-fidelity and lip-synchronized talking avatars with limited training data. In this paper, we introduce Adaptive Text-to-Talking Avatar (Ada-TTA), which (1) designs a generic zero-shot multi-speaker TTS model that well disentangles the text content, timbre, and prosody; and (2) embraces recent advances in neural rendering to achieve realistic audio-driven talking face video generation. With these designs, our method overcomes the aforementioned two challenges and achieves to generate identity-preserving speech and realistic talking person video. Experiments demonstrate that our method could synthesize realistic, identity-preserving, and audio-visual synchronized talking avatar videos.

</details>

### [Take the Hint: Improving Arabic Diacritization with Partially-Diacritized Text](2306.03557.md)
**Parnia Bahar, Mattia Di Gangi, Nick Rossenbach, Mohammad Zeineldeen** · 2023-06-06

<details>
<summary>Abstract</summary>

Automatic Arabic diacritization is useful in many applications, ranging from reading support for language learners to accurate pronunciation predictor for downstream tasks like speech synthesis. While most of the previous works focused on models that operate on raw non-diacritized text, production systems can gain accuracy by first letting humans partly annotate ambiguous words. In this paper, we propose 2SDiac, a multi-source model that can effectively support optional diacritics in input to inform all predictions. We also introduce Guided Learning, a training scheme to leverage given diacritics in input with different levels of random masking. We show that the provided hints during test affect more output positions than those annotated. Moreover, experiments on two common benchmarks show that our approach i) greatly outperforms the baseline also when evaluated on non-diacritized text; and ii) achieves state-of-the-art results while reducing the parameter count by over 60%.

</details>

### [Rhythm-controllable Attention with High Robustness for Long Sentence Speech Synthesis](2306.02593.md)
**Dengfeng Ke et.al.** · 2023-06-05

### [Cross-Lingual Transfer Learning for Phrase Break Prediction with Multilingual Language Model](2306.02579.md)
**Hoyeon Lee, Hyun-Wook Yoon, Jong-Hwan Kim, Jae-Min Kim** · 2023-06-05

<details>
<summary>Abstract</summary>

Phrase break prediction is a crucial task for improving the prosody naturalness of a text-to-speech (TTS) system. However, most proposed phrase break prediction models are monolingual, trained exclusively on a large amount of labeled data. In this paper, we address this issue for low-resource languages with limited labeled data using cross-lingual transfer. We investigate the effectiveness of zero-shot and few-shot cross-lingual transfer for phrase break prediction using a pre-trained multilingual language model. We use manually collected datasets in four Indo-European languages: one high-resource language and three with limited resources. Our findings demonstrate that cross-lingual transfer learning can be a particularly effective approach, especially in the few-shot setting, for improving performance in low-resource languages. This suggests that cross-lingual transfer can be inexpensive and effective for developing TTS front-end in resource-poor languages.

</details>

### [Latent Optimal Paths by Gumbel Propagation for Variational Bayesian Dynamic Programming](2306.02568.md)
**Xinlei Niu, Christian Walder, Jing Zhang, Charles Patrick Martin** · 2023-06-05

<details>
<summary>Abstract</summary>

We propose the stochastic optimal path which solves the classical optimal path problem by a probability-softening solution. This unified approach transforms a wide range of DP problems into directed acyclic graphs in which all paths follow a Gibbs distribution. We show the equivalence of the Gibbs distribution to a message-passing algorithm by the properties of the Gumbel distribution and give all the ingredients required for variational Bayesian inference of a latent path, namely Bayesian dynamic programming (BDP). We demonstrate the usage of BDP in the latent space of variational autoencoders (VAEs) and propose the BDP-VAE which captures structured sparse optimal paths as latent variables. This enables end-to-end training for generative tasks in which models rely on unobserved structural information. At last, we validate the behavior of our approach and showcase its applicability in two real-world applications: text-to-speech and singing voice synthesis. Our implementation code is available at \url{https://github.com/XinleiNIU/LatentOptimalPathsBayesianDP}.

</details>

### [PolyVoice: Language Models for Speech to Speech Translation](2306.02982.md)
**Qianqian Dong, Zhiying Huang, Qiao Tian, Chen Xu et al.** · 2023-06-05

<details>
<summary>Abstract</summary>

We propose PolyVoice, a language model-based framework for speech-to-speech translation (S2ST) system. Our framework consists of two language models: a translation language model and a speech synthesis language model. We use discretized speech units, which are generated in a fully unsupervised way, and thus our framework can be used for unwritten languages. For the speech synthesis part, we adopt the existing VALL-E X approach and build a unit-based audio language model. This grants our framework the ability to preserve the voice characteristics and the speaking style of the original speech. We examine our system on Chinese $\rightarrow$ English and English $\rightarrow$ Spanish pairs. Experimental results show that our system can generate speech with high translation quality and audio quality. Speech samples are available at https://speechtranslation.github.io/polyvoice.

</details>

### [Multi-Speaker Speech Synthesis from Electromyographic Signals by Soft Speech Unit Prediction](s2:913aa6186a1e9adf4e7492aec9e9465da5662a02.md)
**Kevin Scheck, T. Schultz** · 2023-06-04

<details>
<summary>Abstract</summary>

Electromyographic (EMG) signals of articulatory muscles reflect the speech production process even if the user is speaking silently i.e. moving the articulators without producing audible sound. We propose Speech-Unit-based EMG-to-Speech (SU-E2S), a system which relies on EMG to synthesize speech which contains the articulated content but is vocalized in another voice, determined by an acoustic reference utterance. It is based on a Voice Conversion (VC) system which decomposes acoustic speech into continuous soft speech units and a speaker embedding and then reconstructs acoustic features. SU-E2S performs speech synthesis by predicting soft speech units from EMG and using them as input to the VC system. Experiments show that the SU-E2S output is on par in terms of intelligibility of predicting acoustic features directly from EMG, but adds the functionality of synthesizing speech in other voices.

</details>

### [CN-CVS: A Mandarin Audio-Visual Dataset for Large Vocabulary Continuous Visual to Speech Synthesis](s2:8d95944048d1c2bedb7a9ec00115fb3d3855d0b8.md)
**Cheng Chen, Dong Wang, T. Zheng** · 2023-06-04

<details>
<summary>Abstract</summary>

Research on Video to Speech Synthesis (VTS) surges recently and the focus is gradually shifting from small-vocabulary short-phrase VTS to large-vocabulary continuous VTS (LVC-VTS). A large-scale dataset with sufficient speakers and utterances is a prerequisite for such research, and the database is certainly language dependent.In this paper, we introduce CN-CVS, a large-scale Mandarin continuous visual-speech dataset, to support LVC-VTS research. The dataset contains about 200k utterances from more than 2500 individuals, amounting to more than 300 hours of visual-speech data. We built a state-of-the-art VTS model with the new dataset and conducted preliminary studies. Our results show that models that achieve good performance on small vocabulary tasks may perform very poor on CN-CVS, indicating that continuous VTS is indeed a challenging task, and the main challenge comes from the unconstrained vocabulary. The dataset and baseline code can be downloaded for free from http://cncvs.cslt.org.

</details>

### [Why We Should Report the Details in Subjective Evaluation of TTS More Rigorously](2306.02044.md)
**Cheng-Han Chiang, Wei-Ping Huang, Hung-yi Lee** · 2023-06-03

<details>
<summary>Abstract</summary>

This paper emphasizes the importance of reporting experiment details in subjective evaluations and demonstrates how such details can significantly impact evaluation results in the field of speech synthesis. Through an analysis of 80 papers presented at INTERSPEECH 2022, we find a lack of thorough reporting on critical details such as evaluator recruitment and filtering, instructions and payments, and the geographic and linguistic backgrounds of evaluators. To illustrate the effect of these details on evaluation outcomes, we conducted mean opinion score (MOS) tests on three well-known TTS systems under different evaluation settings and we obtain at least three distinct rankings of TTS models. We urge the community to report experiment details in subjective evaluations to improve the reliability and interpretability of experimental results.

</details>

### [SpeechGen: Unlocking the Generative Power of Speech Language Models with Prompts](2306.02207.md)
**Haibin Wu, Kai-Wei Chang, Yuan-Kuei Wu, Hung-yi Lee** · 2023-06-03

<details>
<summary>Abstract</summary>

Large language models (LLMs) have gained considerable attention for Artificial Intelligence Generated Content (AIGC), particularly with the emergence of ChatGPT. However, the direct adaptation of continuous speech to LLMs that process discrete tokens remains an unsolved challenge, hindering the application of LLMs for speech generation. The advanced speech LMs are in the corner, as that speech signals encapsulate a wealth of information, including speaker and emotion, beyond textual data alone. Prompt tuning has demonstrated notable gains in parameter efficiency and competitive performance on some speech classification tasks. However, the extent to which prompts can effectively elicit generation tasks from speech LMs remains an open question. In this paper, we present pioneering research that explores the application of prompt tuning to stimulate speech LMs for various generation tasks, within a unified framework called SpeechGen, with around 10M trainable parameters. The proposed unified framework holds great promise for efficiency and effectiveness, particularly with the imminent arrival of advanced speech LMs, which will significantly enhance the capabilities of the framework. The code and demos of SpeechGen will be available on the project website: \url{https://ga642381.github.io/SpeechPrompt/speechgen}

</details>

### [BabySLM: language-acquisition-friendly benchmark of self-supervised spoken language models](2306.01506.md)
**Marvin Lavechin, Yaya Sy, Hadrien Titeux, María Andrea Cruz Blandón et al.** · 2023-06-02

<details>
<summary>Abstract</summary>

Self-supervised techniques for learning speech representations have been shown to develop linguistic competence from exposure to speech without the need for human labels. In order to fully realize the potential of these approaches and further our understanding of how infants learn language, simulations must closely emulate real-life situations by training on developmentally plausible corpora and benchmarking against appropriate test sets. To this end, we propose a language-acquisition-friendly benchmark to probe spoken language models at the lexical and syntactic levels, both of which are compatible with the vocabulary typical of children's language experiences. This paper introduces the benchmark and summarizes a range of experiments showing its usefulness. In addition, we highlight two exciting challenges that need to be addressed for further progress: bridging the gap between text and speech and between clean speech and in-the-wild speech.

</details>

### [Towards Robust FastSpeech 2 by Modelling Residual Multimodality](2306.01442.md)
**Fabian Kögel, Bac Nguyen, Fabien Cardinaux** · 2023-06-02

<details>
<summary>Abstract</summary>

State-of-the-art non-autoregressive text-to-speech (TTS) models based on FastSpeech 2 can efficiently synthesise high-fidelity and natural speech. For expressive speech datasets however, we observe characteristic audio distortions. We demonstrate that such artefacts are introduced to the vocoder reconstruction by over-smooth mel-spectrogram predictions, which are induced by the choice of mean-squared-error (MSE) loss for training the mel-spectrogram decoder. With MSE loss FastSpeech 2 is limited to learn conditional averages of the training distribution, which might not lie close to a natural sample if the distribution still appears multimodal after all conditioning signals. To alleviate this problem, we introduce TVC-GMM, a mixture model of Trivariate-Chain Gaussian distributions, to model the residual multimodality. TVC-GMM reduces spectrogram smoothness and improves perceptual audio quality in particular for expressive datasets as shown by both objective and subjective evaluation.

</details>

### [Speaker-independent neural formant synthesis](2306.01957.md)
**Pablo Pérez Zarazaga, Zofia Malisz, Gustav Eje Henter, Lauri Juvela** · 2023-06-02

<details>
<summary>Abstract</summary>

We describe speaker-independent speech synthesis driven by a small set of phonetically meaningful speech parameters such as formant frequencies. The intention is to leverage deep-learning advances to provide a highly realistic signal generator that includes control affordances required for stimulus creation in the speech sciences. Our approach turns input speech parameters into predicted mel-spectrograms, which are rendered into waveforms by a pre-trained neural vocoder. Experiments with WaveNet and HiFi-GAN confirm that the method achieves our goals of accurate control over speech parameters combined with high perceptual audio quality. We also find that the small set of phonetically relevant speech parameters we use is sufficient to allow for speaker-independent synthesis (a.k.a. universal vocoding).

</details>

### [In-the-wild Speech Emotion Conversion Using Disentangled Self-Supervised Representations and Neural Vocoder-based Resynthesis](2306.01916.md)
**Navin Raj Prabhu, Nale Lehmann-Willenbrock, Timo Gerkmann** · 2023-06-02

<details>
<summary>Abstract</summary>

Speech emotion conversion aims to convert the expressed emotion of a spoken utterance to a target emotion while preserving the lexical information and the speaker's identity. In this work, we specifically focus on in-the-wild emotion conversion where parallel data does not exist, and the problem of disentangling lexical, speaker, and emotion information arises. In this paper, we introduce a methodology that uses self-supervised networks to disentangle the lexical, speaker, and emotional content of the utterance, and subsequently uses a HiFiGAN vocoder to resynthesise the disentangled representations to a speech signal of the targeted emotion. For better representation and to achieve emotion intensity control, we specifically focus on the aro\-usal dimension of continuous representations, as opposed to performing emotion conversion on categorical representations. We test our methodology on the large in-the-wild MSP-Podcast dataset. Results reveal that the proposed approach is aptly conditioned on the emotional content of input speech and is capable of synthesising natural-sounding speech for a target emotion. Results further reveal that the methodology better synthesises speech for mid-scale arousal (2 to 6) than for extreme arousal (1 and 7).

</details>

### [EmoMix: Emotion Mixing via Diffusion Models for Emotional Speech Synthesis](2306.00648.md)
**Haobin Tang et.al.** · 2023-06-01

### [The Effects of Input Type and Pronunciation Dictionary Usage in Transfer Learning for Low-Resource Text-to-Speech](2306.00535.md)
**Phat Do, Matt Coler, Jelske Dijkstra, Esther Klabbers** · 2023-06-01

<details>
<summary>Abstract</summary>

We compare phone labels and articulatory features as input for cross-lingual transfer learning in text-to-speech (TTS) for low-resource languages (LRLs). Experiments with FastSpeech 2 and the LRL West Frisian show that using articulatory features outperformed using phone labels in both intelligibility and naturalness. For LRLs without pronunciation dictionaries, we propose two novel approaches: a) using a massively multilingual model to convert grapheme-to-phone (G2P) in both training and synthesizing, and b) using a universal phone recognizer to create a makeshift dictionary. Results show that the G2P approach performs largely on par with using a ground-truth dictionary and the phone recognition approach, while performing generally worse, remains a viable option for LRLs less suitable for the G2P approach. Within each approach, using articulatory features as input outperforms using phone labels.

</details>

### [Vocos: Closing the gap between time-domain and Fourier-based neural vocoders for high-quality audio synthesis](2306.00814.md)
**Hubert Siuzdak** · 2023-06-01

<details>
<summary>Abstract</summary>

Recent advancements in neural vocoding are predominantly driven by Generative Adversarial Networks (GANs) operating in the time-domain. While effective, this approach neglects the inductive bias offered by time-frequency representations, resulting in reduntant and computionally-intensive upsampling operations. Fourier-based time-frequency representation is an appealing alternative, aligning more accurately with human auditory perception, and benefitting from well-established fast algorithms for its computation. Nevertheless, direct reconstruction of complex-valued spectrograms has been historically problematic, primarily due to phase recovery issues. This study seeks to close this gap by presenting Vocos, a new model that directly generates Fourier spectral coefficients. Vocos not only matches the state-of-the-art in audio quality, as demonstrated in our evaluations, but it also substantially improves computational efficiency, achieving an order of magnitude increase in speed compared to prevailing time-domain neural vocoding approaches. The source code and model weights have been open-sourced at https://github.com/gemelo-ai/vocos.

</details>

### [ALO-VC: Any-to-any Low-latency One-shot Voice Conversion](2306.01100.md)
**Bohan Wang, Damien Ronssin, Milos Cernak** · 2023-06-01

<details>
<summary>Abstract</summary>

This paper presents ALO-VC, a non-parallel low-latency one-shot phonetic posteriorgrams (PPGs) based voice conversion method. ALO-VC enables any-to-any voice conversion using only one utterance from the target speaker, with only 47.5 ms future look-ahead. The proposed hybrid signal processing and machine learning pipeline combines a pre-trained speaker encoder, a pitch predictor to predict the converted speech's prosody, and positional encoding to convey the phoneme's location information. We introduce two system versions: ALO-VC-R, which uses a pre-trained d-vector speaker encoder, and ALO-VC-E, which improves performance using the ECAPA-TDNN speaker encoder. The experimental results demonstrate both ALO-VC-R and ALO-VC-E can achieve comparable performance to non-causal baseline systems on the VCTK dataset and two out-of-domain datasets. Furthermore, both proposed systems can be deployed on a single CPU core with 55 ms latency and 0.78 real-time factor. Our demo is available online.

</details>

### [XPhoneBERT: A Pre-trained Multilingual Model for Phoneme Representations for Text-to-Speech](2305.19709.md)
**Linh The Nguyen et.al.** · 2023-05-31

### [Text-to-Speech Pipeline for Swiss German -- A comparison](2305.19750.md)
**Tobias Bollinger, Jan Deriu, Manfred Vogel** · 2023-05-31

<details>
<summary>Abstract</summary>

In this work, we studied the synthesis of Swiss German speech using different Text-to-Speech (TTS) models. We evaluated the TTS models on three corpora, and we found, that VITS models performed best, hence, using them for further testing. We also introduce a new method to evaluate TTS models by letting the discriminator of a trained vocoder GAN model predict whether a given waveform is human or synthesized. In summary, our best model delivers speech synthesis for different Swiss German dialects with previously unachieved quality.

</details>

### [PromptStyle: Controllable Style Transfer for Text-to-Speech with Natural Language Descriptions](2305.19522.md)
**Guanghou Liu, Yongmao Zhang, Yi Lei, Yunlin Chen et al.** · 2023-05-31

<details>
<summary>Abstract</summary>

Style transfer TTS has shown impressive performance in recent years. However, style control is often restricted to systems built on expressive speech recordings with discrete style categories. In practical situations, users may be interested in transferring style by typing text descriptions of desired styles, without the reference speech in the target style. The text-guided content generation techniques have drawn wide attention recently. In this work, we explore the possibility of controllable style transfer with natural language descriptions. To this end, we propose PromptStyle, a text prompt-guided cross-speaker style transfer system. Specifically, PromptStyle consists of an improved VITS and a cross-modal style encoder. The cross-modal style encoder constructs a shared space of stylistic and semantic representation through a two-stage training process. Experiments show that PromptStyle can achieve proper style transfer with text prompts while maintaining relatively high stability and speaker similarity. Audio samples are available in our demo page.

</details>

### [Intelligible Lip-to-Speech Synthesis with Speech Units](2305.19603.md)
**Jeongsoo Choi, Minsu Kim, Yong Man Ro** · 2023-05-31

<details>
<summary>Abstract</summary>

In this paper, we propose a novel Lip-to-Speech synthesis (L2S) framework, for synthesizing intelligible speech from a silent lip movement video. Specifically, to complement the insufficient supervisory signal of the previous L2S model, we propose to use quantized self-supervised speech representations, named speech units, as an additional prediction target for the L2S model. Therefore, the proposed L2S model is trained to generate multiple targets, mel-spectrogram and speech units. As the speech units are discrete while mel-spectrogram is continuous, the proposed multi-target L2S model can be trained with strong content supervision, without using text-labeled data. Moreover, to accurately convert the synthesized mel-spectrogram into a waveform, we introduce a multi-input vocoder that can generate a clear waveform even from blurry and noisy mel-spectrogram by referring to the speech units. Extensive experimental results confirm the effectiveness of the proposed method in L2S.

</details>

### [Towards Selection of Text-to-speech Data to Augment ASR Training](2306.00998.md)
**Shuo Liu et.al.** · 2023-05-30

### [Resource-Efficient Fine-Tuning Strategies for Automatic MOS Prediction in Text-to-Speech for Low-Resource Languages](2305.19396.md)
**Phat Do et.al.** · 2023-05-30

### [Make-A-Voice: Unified Voice Synthesis With Discrete Representation](2305.19269.md)
**Rongjie Huang et.al.** · 2023-05-30

### [LibriTTS-R: A Restored Multi-Speaker Text-to-Speech Corpus](2305.18802.md)
**Yuma Koizumi et.al.** · 2023-05-30

### [Voice Conversion With Just Nearest Neighbors](2305.18975.md)
**Matthew Baas, Benjamin van Niekerk, Herman Kamper** · 2023-05-30

<details>
<summary>Abstract</summary>

Any-to-any voice conversion aims to transform source speech into a target voice with just a few examples of the target speaker as a reference. Recent methods produce convincing conversions, but at the cost of increased complexity -- making results difficult to reproduce and build on. Instead, we keep it simple. We propose k-nearest neighbors voice conversion (kNN-VC): a straightforward yet effective method for any-to-any conversion. First, we extract self-supervised representations of the source and reference speech. To convert to the target speaker, we replace each frame of the source representation with its nearest neighbor in the reference. Finally, a pretrained vocoder synthesizes audio from the converted representation. Objective and subjective evaluations show that kNN-VC improves speaker similarity with similar intelligibility scores to existing methods. Code, samples, trained models: https://bshall.github.io/knn-vc

</details>

### [ADAPTERMIX: Exploring the Efficacy of Mixture of Adapters for Low-Resource TTS Adaptation](2305.18028.md)
**Ambuj Mehrish et.al.** · 2023-05-29

### [OverFlow: Putting flows on top of neural transducers for better TTS](2211.06892.md)
**Shivam Mehta et.al.** · 2023-05-29

### [Semi-supervised learning for continuous emotional intensity controllable speech synthesis with disentangled representations](2211.06160.md)
**Yoori Oh et.al.** · 2023-05-29

### [DSPGAN: a GAN-based universal vocoder for high-fidelity TTS by time-frequency domain supervision from DSP](2211.01087.md)
**Kun Song et.al.** · 2023-05-28

### [Stochastic Pitch Prediction Improves the Diversity and Naturalness of Speech in Glow-TTS](2305.17724.md)
**Sewade Ogun, Vincent Colotte, Emmanuel Vincent** · 2023-05-28

<details>
<summary>Abstract</summary>

Flow-based generative models are widely used in text-to-speech (TTS) systems to learn the distribution of audio features (e.g., Mel-spectrograms) given the input tokens and to sample from this distribution to generate diverse utterances. However, in the zero-shot multi-speaker TTS scenario, the generated utterances lack diversity and naturalness. In this paper, we propose to improve the diversity of utterances by explicitly learning the distribution of fundamental frequency sequences (pitch contours) of each speaker during training using a stochastic flow-based pitch predictor, then conditioning the model on generated pitch contours during inference. The experimental results demonstrate that the proposed method yields a significant improvement in the naturalness and diversity of speech generated by a Glow-TTS model that uses explicit stochastic pitch prediction, over a Glow-TTS baseline and an improved Glow-TTS model that uses a stochastic duration predictor.

</details>

### [Learning to Speak from Text: Zero-Shot Multilingual Text-to-Speech with Unsupervised Text Pretraining](2301.12596.md)
**Takaaki Saeki et.al.** · 2023-05-27

### [Creating Personalized Synthetic Voices from Post-Glossectomy Speech with Guided Diffusion Models](2305.17436.md)
**Yusheng Tian, Guangyan Zhang, Tan Lee** · 2023-05-27

<details>
<summary>Abstract</summary>

This paper is about developing personalized speech synthesis systems with recordings of mildly impaired speech. In particular, we consider consonant and vowel alterations resulted from partial glossectomy, the surgical removal of part of the tongue. The aim is to restore articulation in the synthesized speech and maximally preserve the target speaker's individuality. We propose to tackle the problem with guided diffusion models. Specifically, a diffusion-based speech synthesis model is trained on original recordings, to capture and preserve the target speaker's original articulation style. When using the model for inference, a separately trained phone classifier will guide the synthesis process towards proper articulation. Objective and subjective evaluation results show that the proposed method substantially improves articulation in the synthesized speech over original recordings, and preserves more of the target speaker's individuality than a voice conversion baseline.

</details>

### [An Efficient Membership Inference Attack for the Diffusion Model by Proximal Initialization](2305.18355.md)
**Fei Kong, Jinhao Duan, RuiPeng Ma, Hengtao Shen et al.** · 2023-05-26

<details>
<summary>Abstract</summary>

Recently, diffusion models have achieved remarkable success in generating tasks, including image and audio generation. However, like other generative models, diffusion models are prone to privacy issues. In this paper, we propose an efficient query-based membership inference attack (MIA), namely Proximal Initialization Attack (PIA), which utilizes groundtruth trajectory obtained by $ε$ initialized in $t=0$ and predicted point to infer memberships. Experimental results indicate that the proposed method can achieve competitive performance with only two queries on both discrete-time and continuous-time diffusion models. Moreover, previous works on the privacy of diffusion models have focused on vision tasks without considering audio tasks. Therefore, we also explore the robustness of diffusion models to MIA in the text-to-speech (TTS) task, which is an audio generation task. To the best of our knowledge, this work is the first to study the robustness of diffusion models to MIA in the TTS task. Experimental results indicate that models with mel-spectrogram (image-like) output are vulnerable to MIA, while models with audio output are relatively robust to MIA. {Code is available at \url{https://github.com/kong13661/PIA}}.

</details>

### [Diverse and Expressive Speech Prosody Prediction with Denoising Diffusion Probabilistic Model](2305.16749.md)
**Xiang Li, Songxiang Liu, Max W. Y. Lam, Zhiyong Wu et al.** · 2023-05-26

<details>
<summary>Abstract</summary>

Expressive human speech generally abounds with rich and flexible speech prosody variations. The speech prosody predictors in existing expressive speech synthesis methods mostly produce deterministic predictions, which are learned by directly minimizing the norm of prosody prediction error. Its unimodal nature leads to a mismatch with ground truth distribution and harms the model's ability in making diverse predictions. Thus, we propose a novel prosody predictor based on the denoising diffusion probabilistic model to take advantage of its high-quality generative modeling and training stability. Experiment results confirm that the proposed prosody predictor outperforms the deterministic baseline on both the expressiveness and diversity of prediction results with even fewer network parameters.

</details>

### [Automatic Tuning of Loss Trade-offs without Hyper-parameter Search in End-to-End Zero-Shot Speech Synthesis](2305.16699.md)
**Seongyeon Park, Bohyung Kim, Tae-hyun Oh** · 2023-05-26

<details>
<summary>Abstract</summary>

Recently, zero-shot TTS and VC methods have gained attention due to their practicality of being able to generate voices even unseen during training. Among these methods, zero-shot modifications of the VITS model have shown superior performance, while having useful properties inherited from VITS. However, the performance of VITS and VITS-based zero-shot models vary dramatically depending on how the losses are balanced. This can be problematic, as it requires a burdensome procedure of tuning loss balance hyper-parameters to find the optimal balance. In this work, we propose a novel framework that finds this optimum without search, by inducing the decoder of VITS-based models to its full reconstruction ability. With our framework, we show superior performance compared to baselines in zero-shot TTS and VC, achieving state-of-the-art performance. Furthermore, we show the robustness of our framework in various settings. We provide an explanation for the results in the discussion.

</details>

### [Autovocoder: Fast Waveform Generation from a Learned Speech Representation using Differentiable Digital Signal Processing](2211.06989.md)
**Jacob J Webber et.al.** · 2023-05-25

### [Multilingual Text-to-Speech Synthesis for Turkic Languages Using Transliteration](2305.15749.md)
**Rustem Yeshpanov, Saida Mussakhojayeva, Yerbolat Khassanov** · 2023-05-25

<details>
<summary>Abstract</summary>

This work aims to build a multilingual text-to-speech (TTS) synthesis system for ten lower-resourced Turkic languages: Azerbaijani, Bashkir, Kazakh, Kyrgyz, Sakha, Tatar, Turkish, Turkmen, Uyghur, and Uzbek. We specifically target the zero-shot learning scenario, where a TTS model trained using the data of one language is applied to synthesise speech for other, unseen languages. An end-to-end TTS system based on the Tacotron 2 architecture was trained using only the available data of the Kazakh language. To generate speech for the other Turkic languages, we first mapped the letters of the Turkic alphabets onto the symbols of the International Phonetic Alphabet (IPA), which were then converted to the Kazakh alphabet letters. To demonstrate the feasibility of the proposed approach, we evaluated the multilingual Turkic TTS model subjectively and obtained promising results. To enable replication of the experiments, we make our code and dataset publicly available in our GitHub repository.

</details>

### [Betray Oneself: A Novel Audio DeepFake Detection Model via Mono-to-Stereo Conversion](2305.16353.md)
**Rui Liu, Jinhua Zhang, Guanglai Gao, Haizhou Li** · 2023-05-25

<details>
<summary>Abstract</summary>

Audio Deepfake Detection (ADD) aims to detect the fake audio generated by text-to-speech (TTS), voice conversion (VC) and replay, etc., which is an emerging topic. Traditionally we take the mono signal as input and focus on robust feature extraction and effective classifier design. However, the dual-channel stereo information in the audio signal also includes important cues for deepfake, which has not been studied in the prior work. In this paper, we propose a novel ADD model, termed as M2S-ADD, that attempts to discover audio authenticity cues during the mono-to-stereo conversion process. We first projects the mono to a stereo signal using a pretrained stereo synthesizer, then employs a dual-branch neural architecture to process the left and right channel signals, respectively. In this way, we effectively reveal the artifacts in the fake audio, thus improve the ADD performance. The experiments on the ASVspoof2019 database show that M2S-ADD outperforms all baselines that input mono. We release the source code at \url{https://github.com/AI-S2-Lab/M2S-ADD}.

</details>

### [DDDM-VC: Decoupled Denoising Diffusion Models with Disentangled Representation and Prior Mixup for Verified Robust Voice Conversion](2305.15816.md)
**Ha-Yeong Choi, Sang-Hoon Lee, Seong-Whan Lee** · 2023-05-25

<details>
<summary>Abstract</summary>

Diffusion-based generative models have exhibited powerful generative performance in recent years. However, as many attributes exist in the data distribution and owing to several limitations of sharing the model parameters across all levels of the generation process, it remains challenging to control specific styles for each attribute. To address the above problem, this paper presents decoupled denoising diffusion models (DDDMs) with disentangled representations, which can control the style for each attribute in generative models. We apply DDDMs to voice conversion (VC) tasks to address the challenges of disentangling and controlling each speech attribute (e.g., linguistic information, intonation, and timbre). First, we use a self-supervised representation to disentangle the speech representation. Subsequently, the DDDMs are applied to resynthesize the speech from the disentangled representations for denoising with respect to each attribute. Moreover, we also propose the prior mixup for robust voice style transfer, which uses the converted representation of the mixed style as a prior distribution for the diffusion models. The experimental results reveal that our method outperforms publicly available VC models. Furthermore, we show that our method provides robust generative performance regardless of the model size. Audio samples are available https://hayeong0.github.io/DDDM-VC-demo/.

</details>

### [LAraBench: Benchmarking Arabic AI with Large Language Models](2305.14982.md)
**Ahmed Abdelali, Hamdy Mubarak, Shammur Absar Chowdhury, Maram Hasanain et al.** · 2023-05-24

<details>
<summary>Abstract</summary>

Recent advancements in Large Language Models (LLMs) have significantly influenced the landscape of language and speech research. Despite this progress, these models lack specific benchmarking against state-of-the-art (SOTA) models tailored to particular languages and tasks. LAraBench addresses this gap for Arabic Natural Language Processing (NLP) and Speech Processing tasks, including sequence tagging and content classification across different domains. We utilized models such as GPT-3.5-turbo, GPT-4, BLOOMZ, Jais-13b-chat, Whisper, and USM, employing zero and few-shot learning techniques to tackle 33 distinct tasks across 61 publicly available datasets. This involved 98 experimental setups, encompassing ~296K data points, ~46 hours of speech, and 30 sentences for Text-to-Speech (TTS). This effort resulted in 330+ sets of experiments. Our analysis focused on measuring the performance gap between SOTA models and LLMs. The overarching trend observed was that SOTA models generally outperformed LLMs in zero-shot learning, with a few exceptions. Notably, larger computational models with few-shot learning techniques managed to reduce these performance gaps. Our findings provide valuable insights into the applicability of LLMs for Arabic NLP and speech processing tasks.

</details>

### [EfficientSpeech: An On-Device Text to Speech Model](2305.13905.md)
**Rowel Atienza et.al.** · 2023-05-23

### [ZET-Speech: Zero-shot adaptive Emotion-controllable Text-to-Speech Synthesis with Diffusion and Style-based Models](2305.13831.md)
**Minki Kang et.al.** · 2023-05-23

### [i-Code Studio: A Configurable and Composable Framework for Integrative AI](2305.13738.md)
**Yuwei Fang, Mahmoud Khademi, Chenguang Zhu, Ziyi Yang et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

Artificial General Intelligence (AGI) requires comprehensive understanding and generation capabilities for a variety of tasks spanning different modalities and functionalities. Integrative AI is one important direction to approach AGI, through combining multiple models to tackle complex multimodal tasks. However, there is a lack of a flexible and composable platform to facilitate efficient and effective model composition and coordination. In this paper, we propose the i-Code Studio, a configurable and composable framework for Integrative AI. The i-Code Studio orchestrates multiple pre-trained models in a finetuning-free fashion to conduct complex multimodal tasks. Instead of simple model composition, the i-Code Studio provides an integrative, flexible, and composable setting for developers to quickly and easily compose cutting-edge services and technologies tailored to their specific requirements. The i-Code Studio achieves impressive results on a variety of zero-shot multimodal tasks, such as video-to-text retrieval, speech-to-speech translation, and visual question answering. We also demonstrate how to quickly build a multimodal agent based on the i-Code Studio that can communicate and personalize for users.

</details>

### [FluentSpeech: Stutter-Oriented Automatic Speech Editing with Context-Aware Diffusion Models](2305.13612.md)
**Ziyue Jiang, Qian Yang, Jialong Zuo, Zhenhui Ye et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

Stutter removal is an essential scenario in the field of speech editing. However, when the speech recording contains stutters, the existing text-based speech editing approaches still suffer from: 1) the over-smoothing problem in the edited speech; 2) lack of robustness due to the noise introduced by stutter; 3) to remove the stutters, users are required to determine the edited region manually. To tackle the challenges in stutter removal, we propose FluentSpeech, a stutter-oriented automatic speech editing model. Specifically, 1) we propose a context-aware diffusion model that iteratively refines the modified mel-spectrogram with the guidance of context features; 2) we introduce a stutter predictor module to inject the stutter information into the hidden sequence; 3) we also propose a stutter-oriented automatic speech editing (SASE) dataset that contains spontaneous speech recordings with time-aligned stutter labels to train the automatic stutter localization model. Experimental results on VCTK and LibriTTS datasets demonstrate that our model achieves state-of-the-art performance on speech editing. Further experiments on our SASE dataset show that FluentSpeech can effectively improve the fluency of stuttering speech in terms of objective and subjective metrics. Code and audio samples can be found at https://github.com/Zain-Jiang/Speech-Editing-Toolkit.

</details>

### [ChatGPT-EDSS: Empathetic Dialogue Speech Synthesis Trained from ChatGPT-derived Context Word Embeddings](2305.13724.md)
**Yuki Saito, Shinnosuke Takamichi, Eiji Iimori, Kentaro Tachibana et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

We propose ChatGPT-EDSS, an empathetic dialogue speech synthesis (EDSS) method using ChatGPT for extracting dialogue context. ChatGPT is a chatbot that can deeply understand the content and purpose of an input prompt and appropriately respond to the user's request. We focus on ChatGPT's reading comprehension and introduce it to EDSS, a task of synthesizing speech that can empathize with the interlocutor's emotion. Our method first gives chat history to ChatGPT and asks it to generate three words representing the intention, emotion, and speaking style for each line in the chat. Then, it trains an EDSS model using the embeddings of ChatGPT-derived context words as the conditioning features. The experimental results demonstrate that our method performs comparably to ones using emotion labels or neural network-derived context embeddings learned from chat histories. The collected ChatGPT-derived context information is available at https://sarulab-speech.github.io/demo_ChatGPT_EDSS/.

</details>

### [CALLS: Japanese Empathetic Dialogue Speech Corpus of Complaint Handling and Attentive Listening in Customer Center](2305.13713.md)
**Yuki Saito, Eiji Iimori, Shinnosuke Takamichi, Kentaro Tachibana et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

We present CALLS, a Japanese speech corpus that considers phone calls in a customer center as a new domain of empathetic spoken dialogue. The existing STUDIES corpus covers only empathetic dialogue between a teacher and student in a school. To extend the application range of empathetic dialogue speech synthesis (EDSS), we designed our corpus to include the same female speaker as the STUDIES teacher, acting as an operator in simulated phone calls. We describe a corpus construction methodology and analyze the recorded speech. We also conduct EDSS experiments using the CALLS and STUDIES corpora to investigate the effect of domain differences. The results show that mixing the two corpora during training causes biased improvements in the quality of synthetic speech due to the different degrees of expressiveness. Our project page of the corpus is http://sython.org/Corpus/STUDIES-2.

</details>

### [U-DiT TTS: U-Diffusion Vision Transformer for Text-to-Speech](2305.13195.md)
**Xin Jing et.al.** · 2023-05-22

### [ViT-TTS: Visual Text-to-Speech with Scalable Diffusion Transformer](2305.12708.md)
**Huadai Liu et.al.** · 2023-05-22

### [EMNS /Imz/ Corpus: An emotive single-speaker dataset for narrative storytelling in games, television and graphic novels](2305.13137.md)
**Kari Ali Noriy, Xiaosong Yang, Jian Jun Zhang** · 2023-05-22

<details>
<summary>Abstract</summary>

The increasing adoption of text-to-speech technologies has led to a growing demand for natural and emotive voices that adapt to a conversation's context and emotional tone. The Emotive Narrative Storytelling (EMNS) corpus is a unique speech dataset created to enhance conversations' expressiveness and emotive quality in interactive narrative-driven systems. The corpus consists of a 2.3-hour recording featuring a female speaker delivering labelled utterances. It encompasses eight acted emotional states, evenly distributed with a variance of 0.68%, along with expressiveness levels and natural language descriptions with word emphasis labels. The evaluation of audio samples from different datasets revealed that the EMNS corpus achieved the highest average scores in accurately conveying emotions and demonstrating expressiveness. It outperformed other datasets in conveying shared emotions and achieved comparable levels of genuineness. A classification task confirmed the accurate representation of intended emotions in the corpus, with participants recognising the recordings as genuine and expressive. Additionally, the availability of the dataset collection tool under the Apache 2.0 License simplifies remote speech data collection for researchers.

</details>

### [Laughter Synthesis using Pseudo Phonetic Tokens with a Large-scale In-the-wild Laughter Corpus](2305.12442.md)
**Detai Xin, Shinnosuke Takamichi, Ai Morimatsu, Hiroshi Saruwatari** · 2023-05-21

<details>
<summary>Abstract</summary>

We present a large-scale in-the-wild Japanese laughter corpus and a laughter synthesis method. Previous work on laughter synthesis lacks not only data but also proper ways to represent laughter. To solve these problems, we first propose an in-the-wild corpus comprising $3.5$ hours of laughter, which is to our best knowledge the largest laughter corpus designed for laughter synthesis. We then propose pseudo phonetic tokens (PPTs) to represent laughter by a sequence of discrete tokens, which are obtained by training a clustering model on features extracted from laughter by a pretrained self-supervised model. Laughter can then be synthesized by feeding PPTs into a text-to-speech system. We further show PPTs can be used to train a language model for unconditional laughter generation. Results of comprehensive subjective and objective evaluations demonstrate that the proposed method significantly outperforms a baseline method, and can generate natural laughter unconditionally.

</details>

### [DualVC: Dual-mode Voice Conversion using Intra-model Knowledge Distillation and Hybrid Predictive Coding](2305.12425.md)
**Ziqian Ning, Yuepeng Jiang, Pengcheng Zhu, Jixun Yao et al.** · 2023-05-21

<details>
<summary>Abstract</summary>

Voice conversion is an increasingly popular technology, and the growing number of real-time applications requires models with streaming conversion capabilities. Unlike typical (non-streaming) voice conversion, which can leverage the entire utterance as full context, streaming voice conversion faces significant challenges due to the missing future information, resulting in degraded intelligibility, speaker similarity, and sound quality. To address this challenge, we propose DualVC, a dual-mode neural voice conversion approach that supports both streaming and non-streaming modes using jointly trained separate network parameters. Furthermore, we propose intra-model knowledge distillation and hybrid predictive coding (HPC) to enhance the performance of streaming conversion. Additionally, we incorporate data augmentation to train a noise-robust autoregressive decoder, improving the model's performance on long-form speech conversion. Experimental results demonstrate that the proposed model outperforms the baseline models in the context of streaming voice conversion, while maintaining comparable performance to the non-streaming topline system that leverages the complete context, albeit with a latency of only 252.8 ms.

</details>

### [ComedicSpeech: Text To Speech For Stand-up Comedies in Low-Resource Scenarios](2305.12200.md)
**Yuyue Wang, Huan Xiao, Yihan Wu, Ruihua Song** · 2023-05-20

<details>
<summary>Abstract</summary>

Text to Speech (TTS) models can generate natural and high-quality speech, but it is not expressive enough when synthesizing speech with dramatic expressiveness, such as stand-up comedies. Considering comedians have diverse personal speech styles, including personal prosody, rhythm, and fillers, it requires real-world datasets and strong speech style modeling capabilities, which brings challenges. In this paper, we construct a new dataset and develop ComedicSpeech, a TTS system tailored for the stand-up comedy synthesis in low-resource scenarios. First, we extract prosody representation by the prosody encoder and condition it to the TTS model in a flexible way. Second, we enhance the personal rhythm modeling by a conditional duration predictor. Third, we model the personal fillers by introducing comedian-related special tokens. Experiments show that ComedicSpeech achieves better expressiveness than baselines with only ten-minute training data for each comedian. The audio samples are available at https://xh621.github.io/stand-up-comedy-demo/

</details>

### [MParrotTTS: Multilingual Multi-speaker Text to Speech Synthesis in Low Resource Setting](2305.11926.md)
**Neil Shah, Vishal Tambrahalli, Saiteja Kosgi, Niranjan Pedanekar et al.** · 2023-05-19

<details>
<summary>Abstract</summary>

We present MParrotTTS, a unified multilingual, multi-speaker text-to-speech (TTS) synthesis model that can produce high-quality speech. Benefiting from a modularized training paradigm exploiting self-supervised speech representations, MParrotTTS adapts to a new language with minimal supervised data and generalizes to languages not seen while training the self-supervised backbone. Moreover, without training on any bilingual or parallel examples, MParrotTTS can transfer voices across languages while preserving the speaker-specific characteristics, e.g., synthesizing fluent Hindi speech using a French speaker's voice and accent. We present extensive results on six languages in terms of speech naturalness and speaker similarity in parallel and cross-lingual synthesis. The proposed model outperforms the state-of-the-art multilingual TTS models and baselines, using only a small fraction of supervised training data. Speech samples from our model can be found at https://paper2438.github.io/tts/

</details>

### [Parameter-Efficient Learning for Text-to-Speech Accent Adaptation](2305.11320.md)
**Li-Jen Yang et.al.** · 2023-05-18

### [FastFit: Towards Real-Time Iterative Neural Vocoder by Replacing U-Net Encoder With Multiple STFTs](2305.10823.md)
**Won Jang et.al.** · 2023-05-18

### [CLAPSpeech: Learning Prosody from Text Context with Contrastive Language-Audio Pre-training](2305.10763.md)
**Zhenhui Ye et.al.** · 2023-05-18

### [Data Redaction from Conditional Generative Models](2305.11351.md)
**Zhifeng Kong, Kamalika Chaudhuri** · 2023-05-18

<details>
<summary>Abstract</summary>

Deep generative models are known to produce undesirable samples such as harmful content. Traditional mitigation methods include re-training from scratch, filtering, or editing; however, these are either computationally expensive or can be circumvented by third parties. In this paper, we take a different approach and study how to post-edit an already-trained conditional generative model so that it redacts certain conditionals that will, with high probability, lead to undesirable content. This is done by distilling the conditioning network in the models, giving a solution that is effective, efficient, controllable, and universal for a class of deep generative models. We conduct experiments on redacting prompts in text-to-image models and redacting voices in text-to-speech models. Our method is computationally light, leads to better redaction quality and robustness than baseline methods while still retaining high generation quality.

</details>

### [A unified front-end framework for English text-to-speech synthesis](2305.10666.md)
**Zelin Ying, Chen Li, Yu Dong, Qiuqiang Kong et al.** · 2023-05-18

<details>
<summary>Abstract</summary>

The front-end is a critical component of English text-to-speech (TTS) systems, responsible for extracting linguistic features that are essential for a text-to-speech model to synthesize speech, such as prosodies and phonemes. The English TTS front-end typically consists of a text normalization (TN) module, a prosody word prosody phrase (PWPP) module, and a grapheme-to-phoneme (G2P) module. However, current research on the English TTS front-end focuses solely on individual modules, neglecting the interdependence between them and resulting in sub-optimal performance for each module. Therefore, this paper proposes a unified front-end framework that captures the dependencies among the English TTS front-end modules. Extensive experiments have demonstrated that the proposed method achieves state-of-the-art (SOTA) performance in all modules.

</details>

### [Improving Generalization Ability of Countermeasures for New Mismatch Scenario by Combining Multiple Advanced Regularization Terms](2305.10940.md)
**Chang Zeng, Xin Wang, Xiaoxiao Miao, Erica Cooper et al.** · 2023-05-18

<details>
<summary>Abstract</summary>

The ability of countermeasure models to generalize from seen speech synthesis methods to unseen ones has been investigated in the ASVspoof challenge. However, a new mismatch scenario in which fake audio may be generated from real audio with unseen genres has not been studied thoroughly. To this end, we first use five different vocoders to create a new dataset called CN-Spoof based on the CN-Celeb1\&2 datasets. Then, we design two auxiliary objectives for regularization via meta-optimization and a genre alignment module, respectively, and combine them with the main anti-spoofing objective using learnable weights for multiple loss terms. The results on our cross-genre evaluation dataset for anti-spoofing show that the proposed method significantly improved the generalization ability of the countermeasures compared with the baseline system in the genre mismatch scenario.

</details>

### [Data Augmentation for Diverse Voice Conversion in Noisy Environments](2305.10684.md)
**Avani Tanna, Michael Saxon, Amr El Abbadi, William Yang Wang** · 2023-05-18

<details>
<summary>Abstract</summary>

Voice conversion (VC) models have demonstrated impressive few-shot conversion quality on the clean, native speech populations they're trained on. However, when source or target speech accents, background noise conditions, or microphone characteristics differ from training, quality voice conversion is not guaranteed. These problems are often left unexamined in VC research, giving rise to frustration in users trying to use pretrained VC models on their own data. We are interested in accent-preserving voice conversion for name pronunciation from self-recorded examples, a domain in which all three of the aforementioned conditions are present, and posit that demonstrating higher performance in this domain correlates with creating VC models that are more usable by otherwise frustrated users. We demonstrate that existing SOTA encoder-decoder VC models can be made robust to these variations and endowed with natural denoising capabilities using more diverse data and simple data augmentation techniques in pretraining.

</details>

### [Brain-inspired learning in artificial neural networks: a review](2305.11252.md)
**Samuel Schmidgall, Jascha Achterberg, Thomas Miconi, Louis Kirsch et al.** · 2023-05-18

<details>
<summary>Abstract</summary>

Artificial neural networks (ANNs) have emerged as an essential tool in machine learning, achieving remarkable success across diverse domains, including image and speech generation, game playing, and robotics. However, there exist fundamental differences between ANNs' operating mechanisms and those of the biological brain, particularly concerning learning processes. This paper presents a comprehensive review of current brain-inspired learning representations in artificial neural networks. We investigate the integration of more biologically plausible mechanisms, such as synaptic plasticity, to enhance these networks' capabilities. Moreover, we delve into the potential advantages and challenges accompanying this approach. Ultimately, we pinpoint promising avenues for future research in this rapidly advancing field, which could bring us closer to understanding the essence of intelligence.

</details>

### [Controllable Speaking Styles Using a Large Language Model](2305.10321.md)
**Atli Thor Sigurgeirsson, Simon King** · 2023-05-17

<details>
<summary>Abstract</summary>

Reference-based Text-to-Speech (TTS) models can generate multiple, prosodically-different renditions of the same target text. Such models jointly learn a latent acoustic space during training, which can be sampled from during inference. Controlling these models during inference typically requires finding an appropriate reference utterance, which is non-trivial. Large generative language models (LLMs) have shown excellent performance in various language-related tasks. Given only a natural language query text (the prompt), such models can be used to solve specific, context-dependent tasks. Recent work in TTS has attempted similar prompt-based control of novel speaking style generation. Those methods do not require a reference utterance and can, under ideal conditions, be controlled with only a prompt. But existing methods typically require a prompt-labelled speech corpus for jointly training a prompt-conditioned encoder. In contrast, we instead employ an LLM to directly suggest prosodic modifications for a controllable TTS model, using contextual information provided in the prompt. The prompt can be designed for a multitude of tasks. Here, we give two demonstrations: control of speaking style; prosody appropriate for a given dialogue context. The proposed method is rated most appropriate in 50% of cases vs. 31% for a baseline model.

</details>

### [APNet: An All-Frame-Level Neural Vocoder Incorporating Direct Prediction of Amplitude and Phase Spectra](2305.07952.md)
**Yang Ai, Zhen-Hua Ling** · 2023-05-13

<details>
<summary>Abstract</summary>

This paper presents a novel neural vocoder named APNet which reconstructs speech waveforms from acoustic features by predicting amplitude and phase spectra directly. The APNet vocoder is composed of an amplitude spectrum predictor (ASP) and a phase spectrum predictor (PSP). The ASP is a residual convolution network which predicts frame-level log amplitude spectra from acoustic features. The PSP also adopts a residual convolution network using acoustic features as input, then passes the output of this network through two parallel linear convolution layers respectively, and finally integrates into a phase calculation formula to estimate frame-level phase spectra. Finally, the outputs of ASP and PSP are combined to reconstruct speech waveforms by inverse short-time Fourier transform (ISTFT). All operations of the ASP and PSP are performed at the frame level. We train the ASP and PSP jointly and define multilevel loss functions based on amplitude mean square error, phase anti-wrapping error, short-time spectral inconsistency error and time domain reconstruction error. Experimental results show that our proposed APNet vocoder achieves an approximately 8x faster inference speed than HiFi-GAN v1 on a CPU due to the all-frame-level operations, while its synthesized speech quality is comparable to HiFi-GAN v1. The synthesized speech quality of the APNet vocoder is also better than that of several equally efficient models. Ablation experiments also confirm that the proposed parallel phase estimation architecture is essential to phase modeling and the proposed loss functions are helpful for improving the synthesized speech quality.

</details>

### [Better speech synthesis through scaling](2305.07243.md)
**James Betker** · 2023-05-12

<details>
<summary>Abstract</summary>

In recent years, the field of image generation has been revolutionized by the application of autoregressive transformers and DDPMs. These approaches model the process of image generation as a step-wise probabilistic processes and leverage large amounts of compute and data to learn the image distribution. This methodology of improving performance need not be confined to images. This paper describes a way to apply advances in the image generative domain to speech synthesis. The result is TorToise -- an expressive, multi-voice text-to-speech system. All model code and trained weights have been open-sourced at https://github.com/neonbjb/tortoise-tts.

</details>

### [CoMoSpeech: One-Step Speech and Singing Voice Synthesis via Consistency Model](2305.06908.md)
**Zhen Ye, Wei Xue, Xu Tan, Jie Chen et al.** · 2023-05-11

<details>
<summary>Abstract</summary>

Denoising diffusion probabilistic models (DDPMs) have shown promising performance for speech synthesis. However, a large number of iterative steps are required to achieve high sample quality, which restricts the inference speed. Maintaining sample quality while increasing sampling speed has become a challenging task. In this paper, we propose a "Co"nsistency "Mo"del-based "Speech" synthesis method, CoMoSpeech, which achieve speech synthesis through a single diffusion sampling step while achieving high audio quality. The consistency constraint is applied to distill a consistency model from a well-designed diffusion-based teacher model, which ultimately yields superior performances in the distilled CoMoSpeech. Our experiments show that by generating audio recordings by a single sampling step, the CoMoSpeech achieves an inference speed more than 150 times faster than real-time on a single NVIDIA A100 GPU, which is comparable to FastSpeech2, making diffusion-sampling based speech synthesis truly practical. Meanwhile, objective and subjective evaluations on text-to-speech and singing voice synthesis show that the proposed teacher models yield the best audio quality, and the one-step sampling based CoMoSpeech achieves the best inference speed with better or comparable audio quality to other conventional multi-step diffusion model baselines. Audio samples are available at https://comospeech.github.io/.

</details>

### [Zero-shot personalized lip-to-speech synthesis with face image based voice control](2305.14359.md)
**Zheng-Yan Sheng, Yang Ai, Zhen-Hua Ling** · 2023-05-09

<details>
<summary>Abstract</summary>

Lip-to-Speech (Lip2Speech) synthesis, which predicts corresponding speech from talking face images, has witnessed significant progress with various models and training strategies in a series of independent studies. However, existing studies can not achieve voice control under zero-shot condition, because extra speaker embeddings need to be extracted from natural reference speech and are unavailable when only the silent video of an unseen speaker is given. In this paper, we propose a zero-shot personalized Lip2Speech synthesis method, in which face images control speaker identities. A variational autoencoder is adopted to disentangle the speaker identity and linguistic content representations, which enables speaker embeddings to control the voice characteristics of synthetic speech for unseen speakers. Furthermore, we propose associated cross-modal representation learning to promote the ability of face-based speaker embeddings (FSE) on voice control. Extensive experiments verify the effectiveness of the proposed method whose synthetic utterances are more natural and matching with the personality of input video than the compared methods. To our best knowledge, this paper makes the first attempt on zero-shot personalized Lip2Speech synthesis with a face image rather than reference audio to control voice characteristics.

</details>

### [Who is Speaking Actually? Robust and Versatile Speaker Traceability for Voice Conversion](2305.05152.md)
**Yanzhen Ren, Hongcheng Zhu, Liming Zhai, Zongkun Sun et al.** · 2023-05-09

<details>
<summary>Abstract</summary>

Voice conversion (VC), as a voice style transfer technology, is becoming increasingly prevalent while raising serious concerns about its illegal use. Proactively tracing the origins of VC-generated speeches, i.e., speaker traceability, can prevent the misuse of VC, but unfortunately has not been extensively studied. In this paper, we are the first to investigate the speaker traceability for VC and propose a traceable VC framework named VoxTracer. Our VoxTracer is similar to but beyond the paradigm of audio watermarking. We first use unique speaker embedding to represent speaker identity. Then we design a VAE-Glow structure, in which the hiding process imperceptibly integrates the source speaker identity into the VC, and the tracing process accurately recovers the source speaker identity and even the source speech in spite of severe speech quality degradation. To address the speech mismatch between the hiding and tracing processes affected by different distortions, we also adopt an asynchronous training strategy to optimize the VAE-Glow models. The VoxTracer is versatile enough to be applied to arbitrary VC methods and popular audio coding standards. Extensive experiments demonstrate that the VoxTracer achieves not only high imperceptibility in hiding, but also nearly 100% tracing accuracy against various types of audio lossy compressions (AAC, MP3, Opus and SILK) with a broad range of bitrates (16 kbps - 128 kbps) even in a very short time duration (0.74s). Our speech demo is available at https://anonymous.4open.science/w/DEMOofVoxTracer.

</details>

### [Accented Text-to-Speech Synthesis with Limited Data](2305.04816.md)
**Xuehao Zhou, Mingyang Zhang, Yi Zhou, Zhizheng Wu et al.** · 2023-05-08

<details>
<summary>Abstract</summary>

This paper presents an accented text-to-speech (TTS) synthesis framework with limited training data. We study two aspects concerning accent rendering: phonetic (phoneme difference) and prosodic (pitch pattern and phoneme duration) variations. The proposed accented TTS framework consists of two models: an accented front-end for grapheme-to-phoneme (G2P) conversion and an accented acoustic model with integrated pitch and duration predictors for phoneme-to-Mel-spectrogram prediction. The accented front-end directly models the phonetic variation, while the accented acoustic model explicitly controls the prosodic variation. Specifically, both models are first pre-trained on a large amount of data, then only the accent-related layers are fine-tuned on a limited amount of data for the target accent. In the experiments, speech data of three English accents, i.e., General American English, Irish English, and British English Received Pronunciation, are used for pre-training. The pre-trained models are then fine-tuned with Scottish and General Australian English accents, respectively. Both objective and subjective evaluation results show that the accented TTS front-end fine-tuned with a small accented phonetic lexicon (5k words) effectively handles the phonetic variation of accents, while the accented TTS acoustic model fine-tuned with a limited amount of accented speech data (approximately 3 minutes) effectively improves the prosodic rendering including pitch and duration. The overall accent modeling contributes to improved speech quality and accent similarity.

</details>

### [AlignSTS: Speech-to-Singing Conversion via Cross-Modal Alignment](2305.04476.md)
**Ruiqi Li, Rongjie Huang, Lichao Zhang, Jinglin Liu et al.** · 2023-05-08

<details>
<summary>Abstract</summary>

The speech-to-singing (STS) voice conversion task aims to generate singing samples corresponding to speech recordings while facing a major challenge: the alignment between the target (singing) pitch contour and the source (speech) content is difficult to learn in a text-free situation. This paper proposes AlignSTS, an STS model based on explicit cross-modal alignment, which views speech variance such as pitch and content as different modalities. Inspired by the mechanism of how humans will sing the lyrics to the melody, AlignSTS: 1) adopts a novel rhythm adaptor to predict the target rhythm representation to bridge the modality gap between content and pitch, where the rhythm representation is computed in a simple yet effective way and is quantized into a discrete space; and 2) uses the predicted rhythm representation to re-align the content based on cross-attention and conducts a cross-modal fusion for re-synthesize. Extensive experiments show that AlignSTS achieves superior performance in terms of both objective and subjective metrics. Audio samples are available at https://alignsts.github.io.

</details>

### [Investigating Content-Aware Neural Text-To-Speech MOS Prediction Using Prosodic and Linguistic Features](2211.00342.md)
**Alexandra Vioni et.al.** · 2023-05-07

### [M2-CTTS: End-to-End Multi-scale Multi-modal Conversational Text-to-Speech Synthesis](2305.02269.md)
**Jinlong Xue et.al.** · 2023-05-03

### [Source-Filter-Based Generative Adversarial Neural Vocoder for High Fidelity Speech Synthesis](2304.13270.md)
**Ye-Xin Lu et.al.** · 2023-04-26

### [Multi-Speaker Multi-Lingual VQTTS System for LIMMITS 2023 Challenge](2304.13121.md)
**Chenpeng Du, Yiwei Guo, Feiyu Shen, Kai Yu** · 2023-04-25

<details>
<summary>Abstract</summary>

In this paper, we describe the systems developed by the SJTU X-LANCE team for LIMMITS 2023 Challenge, and we mainly focus on the winning system on naturalness for track 1. The aim of this challenge is to build a multi-speaker multi-lingual text-to-speech (TTS) system for Marathi, Hindi and Telugu. Each of the languages has a male and a female speaker in the given dataset. In track 1, only 5 hours data from each speaker can be selected to train the TTS model. Our system is based on the recently proposed VQTTS that utilizes VQ acoustic feature rather than mel-spectrogram. We introduce additional speaker embeddings and language embeddings to VQTTS for controlling the speaker and language information. In the cross-lingual evaluations where we need to synthesize speech in a cross-lingual speaker's voice, we provide a native speaker's embedding to the acoustic model and the target speaker's embedding to the vocoder. In the subjective MOS listening test on naturalness, our system achieves 4.77 which ranks first.

</details>

### [AI-Synthesized Voice Detection Using Neural Vocoder Artifacts](2304.13085.md)
**Chengzhe Sun, Shan Jia, Shuwei Hou, Siwei Lyu** · 2023-04-25

<details>
<summary>Abstract</summary>

Advancements in AI-synthesized human voices have created a growing threat of impersonation and disinformation, making it crucial to develop methods to detect synthetic human voices. This study proposes a new approach to identifying synthetic human voices by detecting artifacts of vocoders in audio signals. Most DeepFake audio synthesis models use a neural vocoder, a neural network that generates waveforms from temporal-frequency representations like mel-spectrograms. By identifying neural vocoder processing in audio, we can determine if a sample is synthesized. To detect synthetic human voices, we introduce a multi-task learning framework for a binary-class RawNet2 model that shares the feature extractor with a vocoder identification module. By treating vocoder identification as a pretext task, we constrain the feature extractor to focus on vocoder artifacts and provide discriminative features for the final binary classifier. Our experiments show that the improved RawNet2 model based on vocoder identification achieves high classification performance on the binary task overall.

</details>

### [Zero-shot text-to-speech synthesis conditioned using self-supervised speech representation model](2304.11976.md)
**Kenichi Fujita et.al.** · 2023-04-24

### [DiffVoice: Text-to-Speech with Latent Diffusion](2304.11750.md)
**Zhijun Liu et.al.** · 2023-04-23

### [SAR: Self-Supervised Anti-Distortion Representation for End-To-End Speech Model](2304.11547.md)
**Jianzong Wang, Xulong Zhang, Haobin Tang, Aolan Sun et al.** · 2023-04-23

<details>
<summary>Abstract</summary>

In recent Text-to-Speech (TTS) systems, a neural vocoder often generates speech samples by solely conditioning on acoustic features predicted from an acoustic model. However, there are always distortions existing in the predicted acoustic features, compared to those of the groundtruth, especially in the common case of poor acoustic modeling due to low-quality training data. To overcome such limits, we propose a Self-supervised learning framework to learn an Anti-distortion acoustic Representation (SAR) to replace human-crafted acoustic features by introducing distortion prior to an auto-encoder pre-training process. The learned acoustic representation from the proposed framework is proved anti-distortion compared to the most commonly used mel-spectrogram through both objective and subjective evaluation.

</details>

### [Designing a realistic peer-like embodied conversational agent for supporting children's storytelling](2304.09399.md)
**Zhixin Li, Ying Xu** · 2023-04-19

<details>
<summary>Abstract</summary>

Advances in artificial intelligence have facilitated the use of large language models (LLMs) and AI-generated synthetic media in education, which may inspire HCI researchers to develop technologies, in particular, embodied conversational agents (ECAs) to simulate the kind of scaffolding children might receive from a human partner. In this paper, we will propose a design prototype of a peer-like ECA named STARie that integrates multiple AI models - GPT-3, Speech Synthesis (Real-time Voice Cloning), VOCA (Voice Operated Character Animation), and FLAME (Faces Learned with an Articulated Model and Expressions) that aims to support narrative production in collaborative storytelling, specifically for children aged 4-8. However, designing a child-centered ECA raises concerns about age appropriateness, children privacy, gender choices of ECAs, and the uncanny valley effect. Thus, this paper will also discuss considerations and ethical concerns that must be taken into account when designing such an ECA. This proposal offers insights into the potential use of AI-generated synthetic media in child-centered AI design and how peer-like AI embodiment may support children\textquotesingle s storytelling.

</details>

### [NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers](2304.09116.md)
**Kai Shen, Zeqian Ju, Xu Tan, Yanqing Liu et al.** · 2023-04-18

<details>
<summary>Abstract</summary>

Scaling text-to-speech (TTS) to large-scale, multi-speaker, and in-the-wild datasets is important to capture the diversity in human speech such as speaker identities, prosodies, and styles (e.g., singing). Current large TTS systems usually quantize speech into discrete tokens and use language models to generate these tokens one by one, which suffer from unstable prosody, word skipping/repeating issue, and poor voice quality. In this paper, we develop NaturalSpeech 2, a TTS system that leverages a neural audio codec with residual vector quantizers to get the quantized latent vectors and uses a diffusion model to generate these latent vectors conditioned on text input. To enhance the zero-shot capability that is important to achieve diverse speech synthesis, we design a speech prompting mechanism to facilitate in-context learning in the diffusion model and the duration/pitch predictor. We scale NaturalSpeech 2 to large-scale datasets with 44K hours of speech and singing data and evaluate its voice quality on unseen speakers. NaturalSpeech 2 outperforms previous TTS systems by a large margin in terms of prosody/timbre similarity, robustness, and voice quality in a zero-shot setting, and performs novel zero-shot singing synthesis with only a speech prompt. Audio samples are available at https://speechresearch.github.io/naturalspeech2.

</details>

### [A Novel End-to-End Turkish Text-to-Speech (TTS) System via Deep Learning](s2:0efd5e1d893289e36db5eafb08bd26fb6c19cc19.md)
**Saadin Oyucu** · 2023-04-18

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) systems have made strides but creating natural-sounding human voices remains challenging. Existing methods rely on noncomprehensive models with only one-layer nonlinear transformations, which are less effective for processing complex data such as speech, images, and video. To overcome this, deep learning (DL)-based solutions have been proposed for TTS but require a large amount of training data. Unfortunately, there is no available corpus for Turkish TTS, unlike English, which has ample resources. To address this, our study focused on developing a Turkish speech synthesis system using a DL approach. We obtained a large corpus from a male speaker and proposed a Tacotron 2 + HiFi-GAN structure for the TTS system. Real users rated the quality of synthesized speech as 4.49 using Mean Opinion Score (MOS). Additionally, MOS-Listening Quality Objective evaluated the speech quality objectively, obtaining a score of 4.32. The speech waveform inference time was determined by a real-time factor, with 1 s of speech data synthesized in 0.92 s. To the best of our knowledge, these findings represent the first documented deep learning and HiFi-GAN-based TTS system for Turkish TTS.

</details>

### [Context-aware Coherent Speaking Style Prediction with Hierarchical Transformers for Audiobook Speech Synthesis](2304.06359.md)
**Shun Lei et.al.** · 2023-04-13

### [Enhancing Speech-to-Speech Translation with Multiple TTS Targets](2304.04618.md)
**Jiatong Shi, Yun Tang, Ann Lee, Hirofumi Inaguma et al.** · 2023-04-10

<details>
<summary>Abstract</summary>

It has been known that direct speech-to-speech translation (S2ST) models usually suffer from the data scarcity issue because of the limited existing parallel materials for both source and target speech. Therefore to train a direct S2ST system, previous works usually utilize text-to-speech (TTS) systems to generate samples in the target language by augmenting the data from speech-to-text translation (S2TT). However, there is a limited investigation into how the synthesized target speech would affect the S2ST models. In this work, we analyze the effect of changing synthesized target speech for direct S2ST models. We find that simply combining the target speech from different TTS systems can potentially improve the S2ST performances. Following that, we also propose a multi-task framework that jointly optimizes the S2ST system with multiple targets from different TTS systems. Extensive experiments demonstrate that our proposed framework achieves consistent improvements (2.8 BLEU) over the baselines on the Fisher Spanish-English dataset.

</details>

### [An investigation of phrase break prediction in an End-to-End TTS system](2304.04157.md)
**Anandaswarup Vadapalli** · 2023-04-09

<details>
<summary>Abstract</summary>

Purpose: This work explores the use of external phrase break prediction models to enhance listener comprehension in End-to-End Text-to-Speech (TTS) systems. Methods: The effectiveness of these models is evaluated based on listener preferences in subjective tests. Two approaches are explored: (1) a bidirectional LSTM model with task-specific embeddings trained from scratch, and (2) a pre-trained BERT model fine-tuned on phrase break prediction. Both models are trained on a multi-speaker English corpus to predict phrase break locations in text. The End-to-End TTS system used comprises a Tacotron2 model with Dynamic Convolutional Attention for mel spectrogram prediction and a WaveRNN vocoder for waveform generation. Results: The listening tests show a clear preference for text synthesized with predicted phrase breaks over text synthesized without them. Conclusion: These results confirm the value of incorporating external phrasing models within End-to-End TTS to enhance listener comprehension.

</details>

### [ArmanTTS single-speaker Persian dataset](2304.03585.md)
**Mohammd Hasan Shamgholi, Vahid Saeedi, Javad Peymanfard, Leila Alhabib et al.** · 2023-04-07

<details>
<summary>Abstract</summary>

TTS, or text-to-speech, is a complicated process that can be accomplished through appropriate modeling using deep learning methods. In order to implement deep learning models, a suitable dataset is required. Since there is a scarce amount of work done in this field for the Persian language, this paper will introduce the single speaker dataset: ArmanTTS. We compared the characteristics of this dataset with those of various prevalent datasets to prove that ArmanTTS meets the necessary standards for teaching a Persian text-to-speech conversion model. We also combined the Tacotron 2 and HiFi GAN to design a model that can receive phonemes as input, with the output being the corresponding speech. 4.0 value of MOS was obtained from real speech, 3.87 value was obtained by the vocoder prediction and 2.98 value was reached with the synthetic speech generated by the TTS model.

</details>

### [Ensemble prosody prediction for expressive speech synthesis](2304.00714.md)
**Tian Huey Teh, Vivian Hu, Devang S Ram Mohan, Zack Hodari et al.** · 2023-04-03

<details>
<summary>Abstract</summary>

Generating expressive speech with rich and varied prosody continues to be a challenge for Text-to-Speech. Most efforts have focused on sophisticated neural architectures intended to better model the data distribution. Yet, in evaluations it is generally found that no single model is preferred for all input texts. This suggests an approach that has rarely been used before for Text-to-Speech: an ensemble of models. We apply ensemble learning to prosody prediction. We construct simple ensembles of prosody predictors by varying either model architecture or model parameter values. To automatically select amongst the models in the ensemble when performing Text-to-Speech, we propose a novel, and computationally trivial, variance-based criterion. We demonstrate that even a small ensemble of prosody predictors yields useful diversity, which, combined with the proposed selection criterion, outperforms any individual model from the ensemble.

</details>

### [A Survey on Audio Diffusion Models: Text To Speech Synthesis and Enhancement in Generative AI](2303.13336.md)
**Chenshuang Zhang et.al.** · 2023-04-02

### [AraSpot: Arabic Spoken Command Spotting](2303.16621.md)
**Mahmoud Salhab, Haidar Harmanani** · 2023-03-29

<details>
<summary>Abstract</summary>

Spoken keyword spotting (KWS) is the task of identifying a keyword in an audio stream and is widely used in smart devices at the edge in order to activate voice assistants and perform hands-free tasks. The task is daunting as there is a need, on the one hand, to achieve high accuracy while at the same time ensuring that such systems continue to run efficiently on low power and possibly limited computational capabilities devices. This work presents AraSpot for Arabic keyword spotting trained on 40 Arabic keywords, using different online data augmentation, and introducing ConformerGRU model architecture. Finally, we further improve the performance of the model by training a text-to-speech model for synthetic data generation. AraSpot achieved a State-of-the-Art SOTA 99.59% result outperforming previous approaches.

</details>

### [Unsupervised Pre-Training For Data-Efficient Text-to-Speech On Low Resource Languages](2303.15669.md)
**Seongyeon Park et.al.** · 2023-03-28

### [Wave-U-Net Discriminator: Fast and Lightweight Discriminator for Generative Adversarial Network-Based Speech Synthesis](2303.13909.md)
**Takuhiro Kaneko et.al.** · 2023-03-24

### [Can Knowledge of End-to-End Text-to-Speech Models Improve Neural MIDI-to-Audio Synthesis Systems?](2211.13868.md)
**Xuan Shi et.al.** · 2023-03-21

### [Personalized Lightweight Text-to-Speech: Voice Cloning with Adaptive Structured Pruning](2303.11816.md)
**Sung-Feng Huang, Chia-ping Chen, Zhi-Sheng Chen, Yu-Pao Tsai et al.** · 2023-03-21

<details>
<summary>Abstract</summary>

Personalized TTS is an exciting and highly desired application that allows users to train their TTS voice using only a few recordings. However, TTS training typically requires many hours of recording and a large model, making it unsuitable for deployment on mobile devices. To overcome this limitation, related works typically require fine-tuning a pre-trained TTS model to preserve its ability to generate high-quality audio samples while adapting to the target speaker's voice. This process is commonly referred to as ``voice cloning.'' Although related works have achieved significant success in changing the TTS model's voice, they are still required to fine-tune from a large pre-trained model, resulting in a significant size for the voice-cloned model. In this paper, we propose applying trainable structured pruning to voice cloning. By training the structured pruning masks with voice-cloning data, we can produce a unique pruned model for each target speaker. Our experiments demonstrate that using learnable structured pruning, we can compress the model size to 7 times smaller while achieving comparable voice-cloning performance.

</details>

### [Self-Supervised Representations for Singing Voice Conversion](2303.12197.md)
**Tejas Jayashankar, Jilong Wu, Leda Sari, David Kant et al.** · 2023-03-21

<details>
<summary>Abstract</summary>

A singing voice conversion model converts a song in the voice of an arbitrary source singer to the voice of a target singer. Recently, methods that leverage self-supervised audio representations such as HuBERT and Wav2Vec 2.0 have helped further the state-of-the-art. Though these methods produce more natural and melodic singing outputs, they often rely on confusion and disentanglement losses to render the self-supervised representations speaker and pitch-invariant. In this paper, we circumvent disentanglement training and propose a new model that leverages ASR fine-tuned self-supervised representations as inputs to a HiFi-GAN neural vocoder for singing voice conversion. We experiment with different f0 encoding schemes and show that an f0 harmonic generation module that uses a parallel bank of transposed convolutions (PBTC) alongside ASR fine-tuned Wav2Vec 2.0 features results in the best singing voice conversion quality. Additionally, the model is capable of making a spoken voice sing. We also show that a simple f0 shifting scheme during inference helps retain singer identity and bolsters the performance of our singing voice conversion model. Our results are backed up by extensive MOS studies that compare different ablations and baselines.

</details>

### [TriAAN-VC: Triple Adaptive Attention Normalization for Any-to-Any Voice Conversion](2303.09057.md)
**Hyun Joon Park, Seok Woo Yang, Jin Sob Kim, Wooseok Shin et al.** · 2023-03-16

<details>
<summary>Abstract</summary>

Voice Conversion (VC) must be achieved while maintaining the content of the source speech and representing the characteristics of the target speaker. The existing methods do not simultaneously satisfy the above two aspects of VC, and their conversion outputs suffer from a trade-off problem between maintaining source contents and target characteristics. In this study, we propose Triple Adaptive Attention Normalization VC (TriAAN-VC), comprising an encoder-decoder and an attention-based adaptive normalization block, that can be applied to non-parallel any-to-any VC. The proposed adaptive normalization block extracts target speaker representations and achieves conversion while minimizing the loss of the source content with siamese loss. We evaluated TriAAN-VC on the VCTK dataset in terms of the maintenance of the source content and target speaker similarity. Experimental results for one-shot VC suggest that TriAAN-VC achieves state-of-the-art performance while mitigating the trade-off problem encountered in the existing VC methods.

</details>

### [Cross-speaker Emotion Transfer by Manipulating Speech Style Latents](2303.08329.md)
**Suhee Jo, Younggun Lee, Yookyung Shin, Yeongtae Hwang et al.** · 2023-03-15

<details>
<summary>Abstract</summary>

In recent years, emotional text-to-speech has shown considerable progress. However, it requires a large amount of labeled data, which is not easily accessible. Even if it is possible to acquire an emotional speech dataset, there is still a limitation in controlling emotion intensity. In this work, we propose a novel method for cross-speaker emotion transfer and manipulation using vector arithmetic in latent style space. By leveraging only a few labeled samples, we generate emotional speech from reading-style speech without losing the speaker identity. Furthermore, emotion strength is readily controllable using a scalar value, providing an intuitive way for users to manipulate speech. Experimental results show the proposed method affords superior performance in terms of expressiveness, naturalness, and controllability, preserving speaker identity.

</details>

### [Grad-StyleSpeech: Any-speaker Adaptive Text-to-Speech Synthesis with Diffusion Models](2211.09383.md)
**Minki Kang et.al.** · 2023-03-14

### [Controllable Prosody Generation With Partial Inputs](2303.09446.md)
**Dan Andrei Iliescu, Devang Savita Ram Mohan, Tian Huey Teh, Zack Hodari** · 2023-03-14

<details>
<summary>Abstract</summary>

We address the problem of human-in-the-loop control for generating prosody in the context of text-to-speech synthesis. Controlling prosody is challenging because existing generative models lack an efficient interface through which users can modify the output quickly and precisely. To solve this, we introduce a novel framework whereby the user provides partial inputs and the generative model generates the missing features. We propose a model that is specifically designed to encode partial prosodic features and output complete audio. We show empirically that our model displays two essential qualities of a human-in-the-loop control mechanism: efficiency and robustness. With even a very small number of input values (~4), our model enables users to improve the quality of the output significantly in terms of listener preference (4:1).

</details>

### [QI-TTS: Questioning Intonation Control for Emotional Speech Synthesis](2303.07682.md)
**Haobin Tang, Xulong Zhang, Jianzong Wang, Ning Cheng et al.** · 2023-03-14

<details>
<summary>Abstract</summary>

Recent expressive text to speech (TTS) models focus on synthesizing emotional speech, but some fine-grained styles such as intonation are neglected. In this paper, we propose QI-TTS which aims to better transfer and control intonation to further deliver the speaker's questioning intention while transferring emotion from reference speech. We propose a multi-style extractor to extract style embedding from two different levels. While the sentence level represents emotion, the final syllable level represents intonation. For fine-grained intonation control, we use relative attributes to represent intonation intensity at the syllable level.Experiments have validated the effectiveness of QI-TTS for improving intonation expressiveness in emotional speech synthesis.

</details>

### [Improving Prosody for Cross-Speaker Style Transfer by Semi-Supervised Style Extractor and Hierarchical Modeling in Speech Synthesis](2303.07711.md)
**Chunyu Qiang, Peng Yang, Hao Che, Ying Zhang et al.** · 2023-03-14

<details>
<summary>Abstract</summary>

Cross-speaker style transfer in speech synthesis aims at transferring a style from source speaker to synthesized speech of a target speaker's timbre. In most previous methods, the synthesized fine-grained prosody features often represent the source speaker's average style, similar to the one-to-many problem(i.e., multiple prosody variations correspond to the same text). In response to this problem, a strength-controlled semi-supervised style extractor is proposed to disentangle the style from content and timbre, improving the representation and interpretability of the global style embedding, which can alleviate the one-to-many mapping and data imbalance problems in prosody prediction. A hierarchical prosody predictor is proposed to improve prosody modeling. We find that better style transfer can be achieved by using the source speaker's prosody features that are easily predicted. Additionally, a speaker-transfer-wise cycle consistency loss is proposed to assist the model in learning unseen style-timbre combinations during the training phase. Experimental results show that the method outperforms the baseline. We provide a website with audio samples.

</details>

### [VANI: Very-lightweight Accent-controllable TTS for Native and Non-native speakers with Identity Preservation](2303.07578.md)
**Rohan Badlani, Akshit Arora, Subhankar Ghosh, Rafael Valle et al.** · 2023-03-14

<details>
<summary>Abstract</summary>

We introduce VANI, a very lightweight multi-lingual accent controllable speech synthesis system. Our model builds upon disentanglement strategies proposed in RADMMM and supports explicit control of accent, language, speaker and fine-grained $F_0$ and energy features for speech synthesis. We utilize the Indic languages dataset, released for LIMMITS 2023 as part of ICASSP Signal Processing Grand Challenge, to synthesize speech in 3 different languages. Our model supports transferring the language of a speaker while retaining their voice and the native accent of the target language. We utilize the large-parameter RADMMM model for Track $1$ and lightweight VANI model for Track $2$ and $3$ of the competition.

</details>

### [DailyTalk: Spoken Dialogue Dataset for Conversational Text-to-Speech](2207.01063.md)
**Keon Lee et.al.** · 2023-03-13

### [An End-to-End Neural Network for Image-to-Audio Transformation](2303.06078.md)
**Liu Chen, Michael Deisher, Munir Georges** · 2023-03-10

<details>
<summary>Abstract</summary>

This paper describes an end-to-end (E2E) neural architecture for the audio rendering of small portions of display content on low resource personal computing devices. It is intended to address the problem of accessibility for vision-impaired or vision-distracted users at the hardware level. Neural image-to-text (ITT) and text-to-speech (TTS) approaches are reviewed and a new technique is introduced to efficiently integrate them in a way that is both efficient and back-propagate-able, leading to a non-autoregressive E2E image-to-speech (ITS) neural network that is efficient and trainable. Experimental results are presented showing that, compared with the non-E2E approach, the proposed E2E system is 29% faster and uses 19% fewer parameters with a 2% reduction in phone accuracy. A future direction to address accuracy is presented.

</details>

### [Improving Few-Shot Learning for Talking Face System with TTS Data Augmentation](2303.05322.md)
**Qi Chen et.al.** · 2023-03-09

### [Text-to-ECG: 12-Lead Electrocardiogram Synthesis conditioned on Clinical Text Reports](2303.09395.md)
**Hyunseung Chung, Jiho Kim, Joon-myoung Kwon, Ki-Hyun Jeon et al.** · 2023-03-09

<details>
<summary>Abstract</summary>

Electrocardiogram (ECG) synthesis is the area of research focused on generating realistic synthetic ECG signals for medical use without concerns over annotation costs or clinical data privacy restrictions. Traditional ECG generation models consider a single ECG lead and utilize GAN-based generative models. These models can only generate single lead samples and require separate training for each diagnosis class. The diagnosis classes of ECGs are insufficient to capture the intricate differences between ECGs depending on various features (e.g. patient demographic details, co-existing diagnosis classes, etc.). To alleviate these challenges, we present a text-to-ECG task, in which textual inputs are used to produce ECG outputs. Then we propose Auto-TTE, an autoregressive generative model conditioned on clinical text reports to synthesize 12-lead ECGs, for the first time to our knowledge. We compare the performance of our model with other representative models in text-to-speech and text-to-image. Experimental results show the superiority of our model in various quantitative evaluations and qualitative analysis. Finally, we conduct a user study with three board-certified cardiologists to confirm the fidelity and semantic alignment of generated samples. our code will be available at https://github.com/TClife/text_to_ecg

</details>

### [FoundationTTS: Text-to-Speech for ASR Customization with Generative Language Model](2303.02939.md)
**Ruiqing Xue et.al.** · 2023-03-08

### [Speak Foreign Languages with Your Own Voice: Cross-Lingual Neural Codec Language Modeling](2303.03926.md)
**Ziqiang Zhang et.al.** · 2023-03-07

### [Do Prosody Transfer Models Transfer Prosody?](2303.04289.md)
**Atli Thor Sigurgeirsson, Simon King** · 2023-03-07

<details>
<summary>Abstract</summary>

Some recent models for Text-to-Speech synthesis aim to transfer the prosody of a reference utterance to the generated target synthetic speech. This is done by using a learned embedding of the reference utterance, which is used to condition speech generation. During training, the reference utterance is identical to the target utterance. Yet, during synthesis, these models are often used to transfer prosody from a reference that differs from the text or speaker being synthesized. To address this inconsistency, we propose to use a different, but prosodically-related, utterance during training too. We believe this should encourage the model to learn to transfer only those characteristics that the reference and target have in common. If prosody transfer methods do indeed transfer prosody they should be able to be trained in the way we propose. However, results show that a model trained under these conditions performs significantly worse than one trained using the target utterance as a reference. To explain this, we hypothesize that prosody transfer models do not learn a transferable representation of prosody, but rather an utterance-level representation which is highly dependent on both the reference speaker and reference text.

</details>

### [WESPER: Zero-shot and Realtime Whisper to Normal Voice Conversion for Whisper-based Speech Interactions](2303.01639.md)
**Jun Rekimoto** · 2023-03-03

<details>
<summary>Abstract</summary>

Recognizing whispered speech and converting it to normal speech creates many possibilities for speech interaction. Because the sound pressure of whispered speech is significantly lower than that of normal speech, it can be used as a semi-silent speech interaction in public places without being audible to others. Converting whispers to normal speech also improves the speech quality for people with speech or hearing impairments. However, conventional speech conversion techniques do not provide sufficient conversion quality or require speaker-dependent datasets consisting of pairs of whispered and normal speech utterances. To address these problems, we propose WESPER, a zero-shot, real-time whisper-to-normal speech conversion mechanism based on self-supervised learning. WESPER consists of a speech-to-unit (STU) encoder, which generates hidden speech units common to both whispered and normal speech, and a unit-to-speech (UTS) decoder, which reconstructs speech from the encoded speech units. Unlike the existing methods, this conversion is user-independent and does not require a paired dataset for whispered and normal speech. The UTS decoder can reconstruct speech in any target speaker's voice from speech units, and it requires only an unlabeled target speaker's speech data. We confirmed that the quality of the speech converted from a whisper was improved while preserving its natural prosody. Additionally, we confirmed the effectiveness of the proposed approach to perform speech reconstruction for people with speech or hearing disabilities. (project page: http://lab.rekimoto.org/projects/wesper )

</details>

### [Fine-grained Emotional Control of Text-To-Speech: Learning To Rank Inter- And Intra-Class Emotion Intensities](2303.01508.md)
**Shijun Wang, Jón Guðnason, Damian Borth** · 2023-03-02

<details>
<summary>Abstract</summary>

State-of-the-art Text-To-Speech (TTS) models are capable of producing high-quality speech. The generated speech, however, is usually neutral in emotional expression, whereas very often one would want fine-grained emotional control of words or phonemes. Although still challenging, the first TTS models have been recently proposed that are able to control voice by manually assigning emotion intensity. Unfortunately, due to the neglect of intra-class distance, the intensity differences are often unrecognizable. In this paper, we propose a fine-grained controllable emotional TTS, that considers both inter- and intra-class distances and be able to synthesize speech with recognizable intensity difference. Our subjective and objective experiments demonstrate that our model exceeds two state-of-the-art controllable TTS models for controllability, emotion expressiveness and naturalness.

</details>

### [Evaluating Parameter-Efficient Transfer Learning Approaches on SURE Benchmark for Speech Understanding](2303.03267.md)
**Yingting Li, Ambuj Mehrish, Shuai Zhao, Rishabh Bhardwaj et al.** · 2023-03-02

<details>
<summary>Abstract</summary>

Fine-tuning is widely used as the default algorithm for transfer learning from pre-trained models. Parameter inefficiency can however arise when, during transfer learning, all the parameters of a large pre-trained model need to be updated for individual downstream tasks. As the number of parameters grows, fine-tuning is prone to overfitting and catastrophic forgetting. In addition, full fine-tuning can become prohibitively expensive when the model is used for many tasks. To mitigate this issue, parameter-efficient transfer learning algorithms, such as adapters and prefix tuning, have been proposed as a way to introduce a few trainable parameters that can be plugged into large pre-trained language models such as BERT, and HuBERT. In this paper, we introduce the Speech UndeRstanding Evaluation (SURE) benchmark for parameter-efficient learning for various speech-processing tasks. Additionally, we introduce a new adapter, ConvAdapter, based on 1D convolution. We show that ConvAdapter outperforms the standard adapters while showing comparable performance against prefix tuning and LoRA with only 0.94% of trainable parameters on some of the task in SURE. We further explore the effectiveness of parameter efficient transfer learning for speech synthesis task such as Text-to-Speech (TTS).

</details>

### [DTW-SiameseNet: Dynamic Time Warped Siamese Network for Mispronunciation Detection and Correction](2303.00171.md)
**Raviteja Anantha, Kriti Bhasin, Daniela de la Parra Aguilar, Prabal Vashisht et al.** · 2023-03-01

<details>
<summary>Abstract</summary>

Personal Digital Assistants (PDAs) - such as Siri, Alexa and Google Assistant, to name a few - play an increasingly important role to access information and complete tasks spanning multiple domains, and by diverse groups of users. A text-to-speech (TTS) module allows PDAs to interact in a natural, human-like manner, and play a vital role when the interaction involves people with visual impairments or other disabilities. To cater to the needs of a diverse set of users, inclusive TTS is important to recognize and pronounce correctly text in different languages and dialects. Despite great progress in speech synthesis, the pronunciation accuracy of named entities in a multi-lingual setting still has a large room for improvement. Existing approaches to correct named entity (NE) mispronunciations, like retraining Grapheme-to-Phoneme (G2P) models, or maintaining a TTS pronunciation dictionary, require expensive annotation of the ground truth pronunciation, which is also time consuming. In this work, we present a highly-precise, PDA-compatible pronunciation learning framework for the task of TTS mispronunciation detection and correction. In addition, we also propose a novel mispronunciation detection model called DTW-SiameseNet, which employs metric learning with a Siamese architecture for Dynamic Time Warping (DTW) with triplet loss. We demonstrate that a locale-agnostic, privacy-preserving solution to the problem of TTS mispronunciation detection is feasible. We evaluate our approach on a real-world dataset, and a corpus of NE pronunciations of an anonymized audio dataset of person names recorded by participants from 10 different locales. Human evaluation shows our proposed approach improves pronunciation accuracy on average by ~6% compared to strong phoneme-based and audio-based baselines.

</details>

### [On the Audio-visual Synchronization for Lip-to-Speech Synthesis](2303.00502.md)
**Zhe Niu, Brian Mak** · 2023-03-01

<details>
<summary>Abstract</summary>

Most lip-to-speech (LTS) synthesis models are trained and evaluated under the assumption that the audio-video pairs in the dataset are perfectly synchronized. In this work, we show that the commonly used audio-visual datasets, such as GRID, TCD-TIMIT, and Lip2Wav, can have data asynchrony issues. Training lip-to-speech with such datasets may further cause the model asynchrony issue -- that is, the generated speech and the input video are out of sync. To address these asynchrony issues, we propose a synchronized lip-to-speech (SLTS) model with an automatic synchronization mechanism (ASM) to correct data asynchrony and penalize model asynchrony. We further demonstrate the limitation of the commonly adopted evaluation metrics for LTS with asynchronous test data and introduce an audio alignment frontend before the metrics sensitive to time alignment for better evaluation. We compare our method with state-of-the-art approaches on conventional and time-aligned metrics to show the benefits of synchronization training.

</details>

### [ClArTTS: An Open-Source Classical Arabic Text-to-Speech Corpus](2303.00069.md)
**Ajinkya Kulkarni et.al.** · 2023-02-28

### [Automatic Heteronym Resolution Pipeline Using RAD-TTS Aligners](2302.14523.md)
**Jocelyn Huang, Evelina Bakhturina, Oktai Tatanov** · 2023-02-28

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) transduction is part of the standard text-to-speech (TTS) pipeline. However, G2P conversion is difficult for languages that contain heteronyms -- words that have one spelling but can be pronounced in multiple ways. G2P datasets with annotated heteronyms are limited in size and expensive to create, as human labeling remains the primary method for heteronym disambiguation. We propose a RAD-TTS Aligner-based pipeline to automatically disambiguate heteronyms in datasets that contain both audio with text transcripts. The best pronunciation can be chosen by generating all possible candidates for each heteronym and scoring them with an Aligner model. The resulting labels can be used to create training datasets for use in both multi-stage and end-to-end G2P systems.

</details>

### [UniFLG: Unified Facial Landmark Generator from Text or Speech](2302.14337.md)
**Kentaro Mitsui, Yukiya Hono, Kei Sawada** · 2023-02-28

<details>
<summary>Abstract</summary>

Talking face generation has been extensively investigated owing to its wide applicability. The two primary frameworks used for talking face generation comprise a text-driven framework, which generates synchronized speech and talking faces from text, and a speech-driven framework, which generates talking faces from speech. To integrate these frameworks, this paper proposes a unified facial landmark generator (UniFLG). The proposed system exploits end-to-end text-to-speech not only for synthesizing speech but also for extracting a series of latent representations that are common to text and speech, and feeds it to a landmark decoder to generate facial landmarks. We demonstrate that our system achieves higher naturalness in both speech synthesis and facial landmark generation compared to the state-of-the-art text-driven method. We further demonstrate that our system can generate facial landmarks from speech of speakers without facial video data or even speech data.

</details>

### [Overview of Voice Conversion Methods Based on Deep Learning](s2:c4a0b2ee7334fa8d9d594d8fb7093a6e6568c8e3.md)
**Tomasz Walczyna, Z. Piotrowski** · 2023-02-28

<details>
<summary>Abstract</summary>

Voice conversion is a process where the essence of a speaker’s identity is seamlessly transferred to another speaker, all while preserving the content of their speech. This usage is accomplished using algorithms that blend speech processing techniques, such as speech analysis, speaker classification, and vocoding. The cutting-edge voice conversion technology is characterized by deep neural networks that effectively separate a speaker’s voice from their linguistic content. This article offers a comprehensive overview of the development status of this area of science based on the current state-of-the-art voice conversion methods.

</details>

### [Imaginary Voice: Face-styled Diffusion Model for Text-to-Speech](2302.13700.md)
**Jiyoung Lee et.al.** · 2023-02-27

### [Duration-aware pause insertion using pre-trained language model for multi-speaker text-to-speech](2302.13652.md)
**Dong Yang et.al.** · 2023-02-27

### [Varianceflow: High-Quality and Controllable Text-to-Speech using Variance Information via Normalizing Flow](2302.13458.md)
**Yoonhyung Lee, Jinhyeok Yang, Kyomin Jung** · 2023-02-27

<details>
<summary>Abstract</summary>

There are two types of methods for non-autoregressive text-to-speech models to learn the one-to-many relationship between text and speech effectively. The first one is to use an advanced generative framework such as normalizing flow (NF). The second one is to use variance information such as pitch or energy together when generating speech. For the second type, it is also possible to control the variance factors by adjusting the variance values provided to a model. In this paper, we propose a novel model called VarianceFlow combining the advantages of the two types. By modeling the variance with NF, VarianceFlow predicts the variance information more precisely with improved speech quality. Also, the objective function of NF makes the model use the variance information and the text in a disentangled manner resulting in more precise variance control. In experiments, VarianceFlow shows superior performance over other state-of-the-art TTS models both in terms of speech quality and controllability.

</details>

### [Cross-modal Face- and Voice-style Transfer](2302.13838.md)
**Naoya Takahashi, Mayank K. Singh, Yuki Mitsufuji** · 2023-02-27

<details>
<summary>Abstract</summary>

Image-to-image translation and voice conversion enable the generation of a new facial image and voice while maintaining some of the semantics such as a pose in an image and linguistic content in audio, respectively. They can aid in the content-creation process in many applications. However, as they are limited to the conversion within each modality, matching the impression of the generated face and voice remains an open question. We propose a cross-modal style transfer framework called XFaVoT that jointly learns four tasks: image translation and voice conversion tasks with audio or image guidance, which enables the generation of ``face that matches given voice" and ``voice that matches given face", and intra-modality translation tasks with a single framework. Experimental results on multiple datasets show that XFaVoT achieves cross-modal style translation of image and voice, outperforming baselines in terms of quality, diversity, and face-voice correspondence.

</details>

### [A Comparative Analysis Of Latent Regressor Losses For Singing Voice Conversion](2302.13678.md)
**Brendan O'Connor, Simon Dixon** · 2023-02-27

<details>
<summary>Abstract</summary>

Previous research has shown that established techniques for spoken voice conversion (VC) do not perform as well when applied to singing voice conversion (SVC). We propose an alternative loss component in a loss function that is otherwise well-established among VC tasks, which has been shown to improve our model's SVC performance. We first trained a singer identity embedding (SIE) network on mel-spectrograms of singer recordings to produce singer-specific variance encodings using contrastive learning. We subsequently trained a well-known autoencoder framework (AutoVC) conditioned on these SIEs, and measured differences in SVC performance when using different latent regressor loss components. We found that using this loss w.r.t. SIEs leads to better performance than w.r.t. bottleneck embeddings, where converted audio is more natural and specific towards target singers. The inclusion of this loss component has the advantage of explicitly forcing the network to reconstruct with timbral similarity, and also negates the effect of poor disentanglement in AutoVC's bottleneck embeddings. We demonstrate peculiar diversity between computational and human evaluations on singer-converted audio clips, which highlights the necessity of both. We also propose a pitch-matching mechanism between source and target singers to ensure these evaluations are not influenced by differences in pitch register.

</details>

### [Period VITS: Variational Inference with Explicit Pitch Modeling for End-to-end Emotional Speech Synthesis](2210.15964.md)
**Yuma Shirahata et.al.** · 2023-02-22

### [Lightweight and High-Fidelity End-to-End Text-to-Speech with Multi-Band Generation and Inverse Short-Time Fourier Transform](2210.15975.md)
**Masaya Kawamura et.al.** · 2023-02-21

### [Nonparallel Emotional Voice Conversion For Unseen Speaker-Emotion Pairs Using Dual Domain Adversarial Network & Virtual Domain Pairing](2302.10536.md)
**Nirmesh Shah, Mayank Kumar Singh, Naoya Takahashi, Naoyuki Onoe** · 2023-02-21

<details>
<summary>Abstract</summary>

Primary goal of an emotional voice conversion (EVC) system is to convert the emotion of a given speech signal from one style to another style without modifying the linguistic content of the signal. Most of the state-of-the-art approaches convert emotions for seen speaker-emotion combinations only. In this paper, we tackle the problem of converting the emotion of speakers whose only neutral data are present during the time of training and testing (i.e., unseen speaker-emotion combinations). To this end, we extend a recently proposed StartGANv2-VC architecture by utilizing dual encoders for learning the speaker and emotion style embeddings separately along with dual domain source classifiers. For achieving the conversion to unseen speaker-emotion combinations, we propose a Virtual Domain Pairing (VDP) training strategy, which virtually incorporates the speaker-emotion pairs that are not present in the real data without compromising the min-max game of a discriminator and generator in adversarial training. We evaluate the proposed method using a Hindi emotional database.

</details>

### [Exposing AI-Synthesized Human Voices Using Neural Vocoder Artifacts](2302.09198.md)
**Chengzhe Sun, Shan Jia, Shuwei Hou, Ehab AlBadawy et al.** · 2023-02-18

<details>
<summary>Abstract</summary>

The advancements of AI-synthesized human voices have introduced a growing threat of impersonation and disinformation. It is therefore of practical importance to developdetection methods for synthetic human voices. This work proposes a new approach to detect synthetic human voices based on identifying artifacts of neural vocoders in audio signals. A neural vocoder is a specially designed neural network that synthesizes waveforms from temporal-frequency representations, e.g., mel-spectrograms. The neural vocoder is a core component in most DeepFake audio synthesis models. Hence the identification of neural vocoder processing implies that an audio sample may have been synthesized. To take advantage of the vocoder artifacts for synthetic human voice detection, we introduce a multi-task learning framework for a binary-class RawNet2 model that shares the front-end feature extractor with a vocoder identification module. We treat the vocoder identification as a pretext task to constrain the front-end feature extractor to focus on vocoder artifacts and provide discriminative features for the final binary classifier. Our experiments show that the improved RawNet2 model based on vocoder identification achieves an overall high classification performance on the binary task.

</details>

### [Lip-to-Speech Synthesis in the Wild with Multi-task Learning](2302.08841.md)
**Minsu Kim, Joanna Hong, Yong Man Ro** · 2023-02-17

<details>
<summary>Abstract</summary>

Recent studies have shown impressive performance in Lip-to-speech synthesis that aims to reconstruct speech from visual information alone. However, they have been suffering from synthesizing accurate speech in the wild, due to insufficient supervision for guiding the model to infer the correct content. Distinct from the previous methods, in this paper, we develop a powerful Lip2Speech method that can reconstruct speech with correct contents from the input lip movements, even in a wild environment. To this end, we design multi-task learning that guides the model using multimodal supervision, i.e., text and audio, to complement the insufficient word representations of acoustic feature reconstruction loss. Thus, the proposed framework brings the advantage of synthesizing speech containing the right content of multiple speakers with unconstrained sentences. We verify the effectiveness of the proposed method using LRS2, LRS3, and LRW datasets.

</details>

### [Fast and small footprint Hybrid HMM-HiFiGAN based system for speech synthesis in Indian languages](2302.06227.md)
**Sudhanshu Srivastava et.al.** · 2023-02-13

### [ERNIE-Music: Text-to-Waveform Music Generation with Diffusion Models](2302.04456.md)
**Pengfei Zhu, Chao Pang, Yekun Chai, Lei Li et al.** · 2023-02-09

<details>
<summary>Abstract</summary>

In recent years, the burgeoning interest in diffusion models has led to significant advances in image and speech generation. Nevertheless, the direct synthesis of music waveforms from unrestricted textual prompts remains a relatively underexplored domain. In response to this lacuna, this paper introduces a pioneering contribution in the form of a text-to-waveform music generation model, underpinned by the utilization of diffusion models. Our methodology hinges on the innovative incorporation of free-form textual prompts as conditional factors to guide the waveform generation process within the diffusion model framework. Addressing the challenge of limited text-music parallel data, we undertake the creation of a dataset by harnessing web resources, a task facilitated by weak supervision techniques. Furthermore, a rigorous empirical inquiry is undertaken to contrast the efficacy of two distinct prompt formats for text conditioning, namely, music tags and unconstrained textual descriptions. The outcomes of this comparative analysis affirm the superior performance of our proposed model in terms of enhancing text-music relevance. Finally, our work culminates in a demonstrative exhibition of the excellent capabilities of our model in text-to-music generation. We further demonstrate that our generated music in the waveform domain outperforms previous works by a large margin in terms of diversity, quality, and text-music relevance.

</details>

### [An Emotion Speech Synthesis Method Based on VITS](s2:d5c1191f15c27f6d77a97b0ac8fbecf36072e489.md)
**Wei Zhao, Zheng Yang** · 2023-02-09

<details>
<summary>Abstract</summary>

People and things can be connected through the Internet of Things (IoT), and speech synthesis is one of the key technologies. At this stage, end-to-end speech synthesis systems are capable of synthesizing relatively realistic human voices, but the current commonly used parallel text-to-speech suffers from loss of useful information during the two-stage delivery process, and the control features of the synthesized speech are monotonous, with insufficient expression of features, including emotion, leading to emotional speech synthesis becoming a challenging task. In this paper, we propose a new system named Emo-VITS, which is based on the highly expressive speech synthesis module VITS, to realize the emotion control of text-to-speech synthesis. We designed the emotion network to extract the global and local features of the reference audio, and then fused the global and local features through the emotion feature fusion module based on the attention mechanism, so as to achieve more accurate and comprehensive emotion speech synthesis. The experimental results show that the Emo-VITS system’s error rate went up a little bit compared with the network without emotionality and does not affect the semantic understanding. However, this system is superior to other networks in naturalness, sound quality, and emotional similarity.

</details>

### [A Vector Quantized Approach for Text to Speech Synthesis on Real-World Spontaneous Speech](2302.04215.md)
**Li-Wei Chen, Shinji Watanabe, Alexander Rudnicky** · 2023-02-08

<details>
<summary>Abstract</summary>

Recent Text-to-Speech (TTS) systems trained on reading or acted corpora have achieved near human-level naturalness. The diversity of human speech, however, often goes beyond the coverage of these corpora. We believe the ability to handle such diversity is crucial for AI systems to achieve human-level communication. Our work explores the use of more abundant real-world data for building speech synthesizers. We train TTS systems using real-world speech from YouTube and podcasts. We observe the mismatch between training and inference alignments in mel-spectrogram based autoregressive models, leading to unintelligible synthesis, and demonstrate that learned discrete codes within multiple code groups effectively resolves this issue. We introduce our MQTTS system whose architecture is designed for multiple code generation and monotonic alignment, along with the use of a clean silence prompt to improve synthesis quality. We conduct ablation analyses to identify the efficacy of our methods. We show that MQTTS outperforms existing TTS systems in several objective and subjective measures.

</details>

### [Speak, Read and Prompt: High-Fidelity Text-to-Speech with Minimal Supervision](2302.03540.md)
**Eugene Kharitonov et.al.** · 2023-02-07

### [Beyond Statistical Similarity: Rethinking Metrics for Deep Generative Models in Engineering Design](2302.02913.md)
**Lyle Regenwetter, Akash Srivastava, Dan Gutfreund, Faez Ahmed** · 2023-02-06

<details>
<summary>Abstract</summary>

Deep generative models such as Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs), Diffusion Models, and Transformers, have shown great promise in a variety of applications, including image and speech synthesis, natural language processing, and drug discovery. However, when applied to engineering design problems, evaluating the performance of these models can be challenging, as traditional statistical metrics based on likelihood may not fully capture the requirements of engineering applications. This paper doubles as a review and practical guide to evaluation metrics for deep generative models (DGMs) in engineering design. We first summarize the well-accepted `classic' evaluation metrics for deep generative models grounded in machine learning theory. Using case studies, we then highlight why these metrics seldom translate well to design problems but see frequent use due to the lack of established alternatives. Next, we curate a set of design-specific metrics which have been proposed across different research communities and can be used for evaluating deep generative models. These metrics focus on unique requirements in design and engineering, such as constraint satisfaction, functional performance, novelty, and conditioning. Throughout our discussion, we apply the metrics to models trained on simple-to-visualize 2-dimensional example problems. Finally, we evaluate four deep generative models on a bicycle frame design problem and structural topology generation problem. In particular, we showcase the use of proposed metrics to quantify performance target achievement, design novelty, and geometric constraints. We publicly release the code for the datasets, models, and metrics used throughout the paper at https://decode.mit.edu/projects/metrics/.

</details>

### [InstructTTS: Modelling Expressive TTS in Discrete Latent Space with Natural Language Style Prompt](2301.13662.md)
**Dongchao Yang, Songxiang Liu, Rongjie Huang, Chao Weng et al.** · 2023-01-31

<details>
<summary>Abstract</summary>

Expressive text-to-speech (TTS) aims to synthesize different speaking style speech according to human's demands. Nowadays, there are two common ways to control speaking styles: (1) Pre-defining a group of speaking style and using categorical index to denote different speaking style. However, there are limitations in the diversity of expressiveness, as these models can only generate the pre-defined styles. (2) Using reference speech as style input, which results in a problem that the extracted style information is not intuitive or interpretable. In this study, we attempt to use natural language as style prompt to control the styles in the synthetic speech, e.g., "Sigh tone in full of sad mood with some helpless feeling". Considering that there is no existing TTS corpus which is proper to benchmark this novel task, we first construct a speech corpus, whose speech samples are annotated with not only content transcriptions but also style descriptions in natural language. Then we propose an expressive TTS model, named as InstructTTS, which is novel in the sense of following aspects: (1) We fully take the advantage of self-supervised learning and cross-modal metric learning, and propose a novel three-stage training procedure to obtain a robust sentence embedding model, which can effectively capture semantic information from the style prompts and control the speaking style in the generated speech. (2) We propose to model acoustic features in discrete latent space and train a novel discrete diffusion probabilistic model to generate vector-quantized (VQ) acoustic tokens rather than the commonly-used mel spectrogram. (3) We jointly apply mutual information (MI) estimation and minimization during acoustic model training to minimize style-speaker and style-content MI, avoiding possible content and speaker information leakage from the style prompt.

</details>

### [UzbekTagger: The rule-based POS tagger for Uzbek language](2301.12711.md)
**Maksud Sharipov, Elmurod Kuriyozov, Ollabergan Yuldashev, Ogabek Sobirov** · 2023-01-30

<details>
<summary>Abstract</summary>

This research paper presents a part-of-speech (POS) annotated dataset and tagger tool for the low-resource Uzbek language. The dataset includes 12 tags, which were used to develop a rule-based POS-tagger tool. The corpus text used in the annotation process was made sure to be balanced over 20 different fields in order to ensure its representativeness. Uzbek being an agglutinative language so the most of the words in an Uzbek sentence are formed by adding suffixes. This nature of it makes the POS-tagging task difficult to find the stems of words and the right part-of-speech they belong to. The methodology proposed in this research is the stemming of the words with an affix/suffix stripping approach including database of the stem forms of the words in the Uzbek language. The tagger tool was tested on the annotated dataset and showed high accuracy in identifying and tagging parts of speech in Uzbek text. This newly presented dataset and tagger tool can be used for a variety of natural language processing tasks such as language modeling, machine translation, and text-to-speech synthesis. The presented dataset is the first of its kind to be made publicly available for Uzbek, and the POS-tagger tool created can also be used as a pivot to use as a base for other closely-related Turkic languages.

</details>

### [Time out of Mind: Generating Rate of Speech conditioned on emotion and speaker](2301.12331.md)
**Navjot Kaur, Paige Tuttosi** · 2023-01-29

<details>
<summary>Abstract</summary>

Voice synthesis has seen significant improvements in the past decade resulting in highly intelligible voices. Further investigations have resulted in models that can produce variable speech, including conditional emotional expression. The problem lies, however, in a focus on phrase-level modifications and prosodic vocal features. Using the CREMA-D dataset we have trained a GAN conditioned on emotion to generate worth lengths for a given input text. These word lengths are relative to neutral speech and can be provided, through speech synthesis markup language (SSML) to a text-to-speech (TTS) system to generate more expressive speech. Additionally, a generative model is also trained using implicit maximum likelihood estimation (IMLE) and a comparative analysis with GANs is included. We were able to achieve better performances on objective measures for neutral speech, and better time alignment for happy speech when compared to an out-of-box model. However, further investigation of subjective evaluation is required.

</details>

### [On granularity of prosodic representations in expressive text-to-speech](2301.11446.md)
**Mikolaj Babianski et.al.** · 2023-01-26

### [Multilingual Multiaccented Multispeaker TTS with RADTTS](2301.10335.md)
**Rohan Badlani, Rafael Valle, Kevin J. Shih, João Felipe Santos et al.** · 2023-01-24

<details>
<summary>Abstract</summary>

We work to create a multilingual speech synthesis system which can generate speech with the proper accent while retaining the characteristics of an individual voice. This is challenging to do because it is expensive to obtain bilingual training data in multiple languages, and the lack of such data results in strong correlations that entangle speaker, language, and accent, resulting in poor transfer capabilities. To overcome this, we present a multilingual, multiaccented, multispeaker speech synthesis model based on RADTTS with explicit control over accent, language, speaker and fine-grained $F_0$ and energy features. Our proposed model does not rely on bilingual training data. We demonstrate an ability to control synthesized accent for any speaker in an open-source dataset comprising of 7 accents. Human subjective evaluation demonstrates that our model can better retain a speaker's voice and accent quality than controlled baselines while synthesizing fluent speech in all target languages and accents in our dataset.

</details>

### [Phoneme-Level BERT for Enhanced Prosody of Text-to-Speech with Grapheme Predictions](2301.08810.md)
**Yinghao Aaron Li, Cong Han, Xilin Jiang, Nima Mesgarani** · 2023-01-20

<details>
<summary>Abstract</summary>

Large-scale pre-trained language models have been shown to be helpful in improving the naturalness of text-to-speech (TTS) models by enabling them to produce more naturalistic prosodic patterns. However, these models are usually word-level or sup-phoneme-level and jointly trained with phonemes, making them inefficient for the downstream TTS task where only phonemes are needed. In this work, we propose a phoneme-level BERT (PL-BERT) with a pretext task of predicting the corresponding graphemes along with the regular masked phoneme predictions. Subjective evaluations show that our phoneme-level BERT encoder has significantly improved the mean opinion scores (MOS) of rated naturalness of synthesized speech compared with the state-of-the-art (SOTA) StyleTTS baseline on out-of-distribution (OOD) texts.

</details>

### [Warning: Humans Cannot Reliably Detect Speech Deepfakes](2301.07829.md)
**Kimberly T. Mai, Sergi D. Bray, Toby Davies, Lewis D. Griffin** · 2023-01-19

<details>
<summary>Abstract</summary>

Speech deepfakes are artificial voices generated by machine learning models. Previous literature has highlighted deepfakes as one of the biggest security threats arising from progress in artificial intelligence due to their potential for misuse. However, studies investigating human detection capabilities are limited. We presented genuine and deepfake audio to n = 529 individuals and asked them to identify the deepfakes. We ran our experiments in English and Mandarin to understand if language affects detection performance and decision-making rationale. We found that detection capability is unreliable. Listeners only correctly spotted the deepfakes 73% of the time, and there was no difference in detectability between the two languages. Increasing listener awareness by providing examples of speech deepfakes only improves results slightly. As speech synthesis algorithms improve and become more realistic, we can expect the detection task to become harder. The difficulty of detecting speech deepfakes confirms their potential for misuse and signals that defenses against this threat are needed.

</details>

### [Msanii: High Fidelity Music Synthesis on a Shoestring Budget](2301.06468.md)
**Kinyugo Maina** · 2023-01-16

<details>
<summary>Abstract</summary>

In this paper, we present Msanii, a novel diffusion-based model for synthesizing long-context, high-fidelity music efficiently. Our model combines the expressiveness of mel spectrograms, the generative capabilities of diffusion models, and the vocoding capabilities of neural vocoders. We demonstrate the effectiveness of Msanii by synthesizing tens of seconds (190 seconds) of stereo music at high sample rates (44.1 kHz) without the use of concatenative synthesis, cascading architectures, or compression techniques. To the best of our knowledge, this is the first work to successfully employ a diffusion-based model for synthesizing such long music samples at high sample rates. Our demo can be found https://kinyugo.github.io/msanii-demo and our code https://github.com/Kinyugo/msanii .

</details>

### [Modelling low-resource accents without accent-specific TTS frontend](2301.04606.md)
**Georgi Tinchev, Marta Czarnowska, Kamil Deja, Kayoko Yanagisawa et al.** · 2023-01-11

<details>
<summary>Abstract</summary>

This work focuses on modelling a speaker's accent that does not have a dedicated text-to-speech (TTS) frontend, including a grapheme-to-phoneme (G2P) module. Prior work on modelling accents assumes a phonetic transcription is available for the target accent, which might not be the case for low-resource, regional accents. In our work, we propose an approach whereby we first augment the target accent data to sound like the donor voice via voice conversion, then train a multi-speaker multi-accent TTS model on the combination of recordings and synthetic data, to generate the donor's voice speaking in the target accent. Throughout the procedure, we use a TTS frontend developed for the same language but a different accent. We show qualitative and quantitative analysis where the proposed strategy achieves state-of-the-art results compared to other generative models. Our work demonstrates that low resource accents can be modelled with relatively little data and without developing an accent-specific TTS frontend. Audio samples of our model converting to multiple accents are available on our web page.

</details>

### [UnifySpeech: A Unified Framework for Zero-shot Text-to-Speech and Voice Conversion](2301.03801.md)
**Haogeng Liu et.al.** · 2023-01-10

### [Generative Emotional AI for Speech Emotion Recognition: The Case for Synthetic Emotional Speech Augmentation](2301.03751.md)
**Abdullah Shahid, Siddique Latif, Junaid Qadir** · 2023-01-10

<details>
<summary>Abstract</summary>

Despite advances in deep learning, current state-of-the-art speech emotion recognition (SER) systems still have poor performance due to a lack of speech emotion datasets. This paper proposes augmenting SER systems with synthetic emotional speech generated by an end-to-end text-to-speech (TTS) system based on an extended Tacotron architecture. The proposed TTS system includes encoders for speaker and emotion embeddings, a sequence-to-sequence text generator for creating Mel-spectrograms, and a WaveRNN to generate audio from the Mel-spectrograms. Extensive experiments show that the quality of the generated emotional speech can significantly improve SER performance on multiple datasets, as demonstrated by a higher mean opinion score (MOS) compared to the baseline. The generated samples were also effective at augmenting SER performance.

</details>

### [Applying Automated Machine Translation to Educational Video Courses](2301.03141.md)
**Linden Wang** · 2023-01-09

<details>
<summary>Abstract</summary>

We studied the capability of automated machine translation in the online video education space by automatically translating Khan Academy videos with state-of-the-art translation models and applying text-to-speech synthesis and audio/video synchronization to build engaging videos in target languages. We also analyzed and established two reliable translation confidence estimators based on round-trip translations in order to efficiently manage translation quality and reduce human translation effort. Finally, we developed a deployable system to deliver translated videos to end users and collect user corrections for iterative improvement.

</details>

### [Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers](2301.02111.md)
**Chengyi Wang et.al.** · 2023-01-05

### [ITTS model: speech generation for image captioning using feature extraction for end-to-end synthesis](s2:677b538f235a18029accacbdade41f137d8133cb.md)
**Tushar Ghorpade, S. Shinde** · 2023-01-01

