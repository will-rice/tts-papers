# 2022

361 papers in this year.

### [ResGrad: Residual Denoising Diffusion Probabilistic Models for Text to Speech](2212.14518.md)
**Zehua Chen et.al.** · 2022-12-30

### [StyleTTS-VC: One-Shot Voice Conversion by Knowledge Transfer from Style-Based TTS Models](2212.14227.md)
**Yinghao Aaron Li, Cong Han, Nima Mesgarani** · 2022-12-29

<details>
<summary>Abstract</summary>

One-shot voice conversion (VC) aims to convert speech from any source speaker to an arbitrary target speaker with only a few seconds of reference speech from the target speaker. This relies heavily on disentangling the speaker's identity and speech content, a task that still remains challenging. Here, we propose a novel approach to learning disentangled speech representation by transfer learning from style-based text-to-speech (TTS) models. With cycle consistent and adversarial training, the style-based TTS models can perform transcription-guided one-shot VC with high fidelity and similarity. By learning an additional mel-spectrogram encoder through a teacher-student knowledge transfer and novel data augmentation scheme, our approach results in disentangled speech representation without needing the input text. The subjective evaluation shows that our approach can significantly outperform the previous state-of-the-art one-shot voice conversion models in both naturalness and similarity.

</details>

### [Emotional Speech Synthesis using End-to-End neural TTS models](s2:85c776ed9217bc05f5f6c9559ef824f46a0986ed.md)
**S. Nithin, J. Prakash** · 2022-12-29

<details>
<summary>Abstract</summary>

Speech synthesis aims at artificially generating human like speech. The advancements in Artificial Intelligence and Natural Language Processing (NLP), particularly deep learning networks, have significantly improved such attempts. Text to Speech Synthesis (TTS) models based on deep neural networks are now able to generate speech samples with high naturality and intelligibilty. Improving the paralinguistic characteristics of speech, like emotion, is also desirable for effective speech synthesis. But availability of suitable emotional speech dataset for neural TTS may be limited. Transfer Learning offers a viable solution for such scenarios of limited resources. In this paper, we present an overview of emotional speech synthesis using end-to-end neural TTS models and compare the performance of Tacotron 2 and FastSpeech 2 for transfer learning based emotional speech synthesis. To generate speech waveform from generated mel spectrogram, HiFi-GAN vocder is used. The synthesized speech samples are evaluated using ScSer speech emotion recognition model. The Tacotron 2 and FastSpeech 2 models reported classification accuracies of 90% and 79% respectively.

</details>

### [Voice conversion with limited data and limitless data augmentations](2212.13581.md)
**Olga Slizovskaia, Jordi Janer, Pritish Chandna, Oscar Mayor** · 2022-12-27

<details>
<summary>Abstract</summary>

Applying changes to an input speech signal to change the perceived speaker of speech to a target while maintaining the content of the input is a challenging but interesting task known as Voice conversion (VC). Over the last few years, this task has gained significant interest where most systems use data-driven machine learning models. Doing the conversion in a low-latency real-world scenario is even more challenging constrained by the availability of high-quality data. Data augmentations such as pitch shifting and noise addition are often used to increase the amount of data used for training machine learning based models for this task. In this paper we explore the efficacy of common data augmentation techniques for real-time voice conversion and introduce novel techniques for data augmentation based on audio and voice transformation effects as well. We evaluate the conversions for both male and female target speakers using objective and subjective evaluation methodologies.

</details>

### [HMM-based data augmentation for E2E systems for building conversational speech synthesis systems](2212.11982.md)
**Ishika Gupta, Anusha Prakash, Jom Kuriakose, Hema A. Murthy** · 2022-12-22

<details>
<summary>Abstract</summary>

This paper proposes an approach to build a high-quality text-to-speech (TTS) system for technical domains using data augmentation. An end-to-end (E2E) system is trained on hidden Markov model (HMM) based synthesized speech and further fine-tuned with studio-recorded TTS data to improve the timbre of the synthesized voice. The motivation behind the work is that issues of word skips and repetitions are usually absent in HMM systems due to their ability to model the duration distribution of phonemes accurately. Context-dependent pentaphone modeling, along with tree-based clustering and state-tying, takes care of unseen context and out-of-vocabulary words. A language model is also employed to reduce synthesis errors further. Subjective evaluations indicate that speech produced using the proposed system is superior to the baseline E2E synthesis approach in terms of intelligibility when combining complementing attributes from HMM and E2E frameworks. The further analysis highlights the proposed approach's efficacy in low-resource scenarios.

</details>

### [TTS-Guided Training for Accent Conversion Without Parallel Data](2212.10204.md)
**Yi Zhou et.al.** · 2022-12-20

### [Emotion Selectable End-to-End Text-based Speech Editing](2212.10191.md)
**Tao Wang, Jiangyan Yi, Ruibo Fu, Jianhua Tao et al.** · 2022-12-20

<details>
<summary>Abstract</summary>

Text-based speech editing allows users to edit speech by intuitively cutting, copying, and pasting text to speed up the process of editing speech. In the previous work, CampNet (context-aware mask prediction network) is proposed to realize text-based speech editing, significantly improving the quality of edited speech. This paper aims at a new task: adding emotional effect to the editing speech during the text-based speech editing to make the generated speech more expressive. To achieve this task, we propose Emo-CampNet (emotion CampNet), which can provide the option of emotional attributes for the generated speech in text-based speech editing and has the one-shot ability to edit unseen speakers' speech. Firstly, we propose an end-to-end emotion-selectable text-based speech editing model. The key idea of the model is to control the emotion of generated speech by introducing additional emotion attributes based on the context-aware mask prediction network. Secondly, to prevent the emotion of the generated speech from being interfered by the emotional components in the original speech, a neutral content generator is proposed to remove the emotion from the original speech, which is optimized by the generative adversarial framework. Thirdly, two data augmentation methods are proposed to enrich the emotional and pronunciation information in the training set, which can enable the model to edit the unseen speaker's speech. The experimental results that 1) Emo-CampNet can effectively control the emotion of the generated speech in the process of text-based speech editing; And can edit unseen speakers' speech. 2) Detailed ablation experiments further prove the effectiveness of emotional selectivity and data augmentation methods. The demo page is available at https://hairuo55.github.io/Emo-CampNet/

</details>

### [VSVC: Backdoor attack against Keyword Spotting based on Voiceprint Selection and Voice Conversion](2212.10103.md)
**Hanbo Cai, Pengcheng Zhang, Hai Dong, Yan Xiao et al.** · 2022-12-20

<details>
<summary>Abstract</summary>

Keyword spotting (KWS) based on deep neural networks (DNNs) has achieved massive success in voice control scenarios. However, training of such DNN-based KWS systems often requires significant data and hardware resources. Manufacturers often entrust this process to a third-party platform. This makes the training process uncontrollable, where attackers can implant backdoors in the model by manipulating third-party training data. An effective backdoor attack can force the model to make specified judgments under certain conditions, i.e., triggers. In this paper, we design a backdoor attack scheme based on Voiceprint Selection and Voice Conversion, abbreviated as VSVC. Experimental results demonstrated that VSVC is feasible to achieve an average attack success rate close to 97% in four victim models when poisoning less than 1% of the training data.

</details>

### [Speaking Style Conversion in the Waveform Domain Using Discrete Self-Supervised Units](2212.09730.md)
**Gallil Maimon, Yossi Adi** · 2022-12-19

<details>
<summary>Abstract</summary>

We introduce DISSC, a novel, lightweight method that converts the rhythm, pitch contour and timbre of a recording to a target speaker in a textless manner. Unlike DISSC, most voice conversion (VC) methods focus primarily on timbre, and ignore people's unique speaking style (prosody). The proposed approach uses a pretrained, self-supervised model for encoding speech to discrete units, which makes it simple, effective, and fast to train. All conversion modules are only trained on reconstruction like tasks, thus suitable for any-to-many VC with no paired data. We introduce a suite of quantitative and qualitative evaluation metrics for this setup, and empirically demonstrate that DISSC significantly outperforms the evaluated baselines. Code and samples are available at https://pages.cs.huji.ac.il/adiyoss-lab/dissc/.

</details>

### [Text-to-speech synthesis based on latent variable conversion using diffusion probabilistic model and variational autoencoder](2212.08329.md)
**Yusuke Yasuda et.al.** · 2022-12-16

### [Investigation of Japanese PnG BERT language model in text-to-speech synthesis for pitch accent language](2212.08321.md)
**Yusuke Yasuda et.al.** · 2022-12-16

### [Source Tracing: Detecting Voice Spoofing](2212.08601.md)
**Tinglong Zhu, Xingming Wang, Xiaoyi Qin, Ming Li** · 2022-12-16

<details>
<summary>Abstract</summary>

Recent anti-spoofing systems focus on spoofing detection, where the task is only to determine whether the test audio is fake. However, there are few studies putting attention to identifying the methods of generating fake speech. Common spoofing attack algorithms in the logical access (LA) scenario, such as voice conversion and speech synthesis, can be divided into several stages: input processing, conversion, waveform generation, etc. In this work, we propose a system for classifying different spoofing attributes, representing characteristics of different modules in the whole pipeline. Classifying attributes for the spoofing attack other than determining the whole spoofing pipeline can make the system more robust when encountering complex combinations of different modules at different stages. In addition, our system can also be used as an auxiliary system for anti-spoofing against unseen spoofing methods. The experiments are conducted on ASVspoof 2019 LA data set and the proposed method achieved a 20\% relative improvement against conventional binary spoof detection methods.

</details>

### [RWEN-TTS: Relation-aware Word Encoding Network for Natural Text-to-Speech Synthesis](2212.07939.md)
**Shinhyeok Oh, HyeongRae Noh, Yoonseok Hong, Insoo Oh** · 2022-12-15

<details>
<summary>Abstract</summary>

With the advent of deep learning, a huge number of text-to-speech (TTS) models which produce human-like speech have emerged. Recently, by introducing syntactic and semantic information w.r.t the input text, various approaches have been proposed to enrich the naturalness and expressiveness of TTS models. Although these strategies showed impressive results, they still have some limitations in utilizing language information. First, most approaches only use graph networks to utilize syntactic and semantic information without considering linguistic features. Second, most previous works do not explicitly consider adjacent words when encoding syntactic and semantic information, even though it is obvious that adjacent words are usually meaningful when encoding the current word. To address these issues, we propose Relation-aware Word Encoding Network (RWEN), which effectively allows syntactic and semantic information based on two modules (i.e., Semantic-level Relation Encoding and Adjacent Word Relation Encoding). Experimental results show substantial improvements compared to previous works.

</details>

### [Style-Label-Free: Cross-Speaker Style Transfer by Quantized VAE and Speaker-wise Normalization in Speech Synthesis](2212.06397.md)
**Chunyu Qiang, Peng Yang, Hao Che, Xiaorui Wang et al.** · 2022-12-13

<details>
<summary>Abstract</summary>

Cross-speaker style transfer in speech synthesis aims at transferring a style from source speaker to synthesised speech of a target speaker's timbre. Most previous approaches rely on data with style labels, but manually-annotated labels are expensive and not always reliable. In response to this problem, we propose Style-Label-Free, a cross-speaker style transfer method, which can realize the style transfer from source speaker to target speaker without style labels. Firstly, a reference encoder structure based on quantized variational autoencoder (Q-VAE) and style bottleneck is designed to extract discrete style representations. Secondly, a speaker-wise batch normalization layer is proposed to reduce the source speaker leakage. In order to improve the style extraction ability of the reference encoder, a style invariant and contrastive data augmentation method is proposed. Experimental results show that the method outperforms the baseline. We provide a website with audio samples.

</details>

### [A Novel Chinese Dialect TTS Frontend with Non-Autoregressive Neural Machine Translation](2206.04922.md)
**Junhui Zhang et.al.** · 2022-12-12

### [MnTTS2: An Open-Source Multi-Speaker Mongolian Text-to-Speech Synthesis Dataset](2301.00657.md)
**Kailin Liang et.al.** · 2022-12-11

### [A Mandarin Prosodic Boundary Prediction Model Based on Multi-Source Semi-Supervision](s2:83564b4b54193a64904d8a83279982595e1caa9f.md)
**Peiyang Shi, Zengqiang Shang, Pengyuan Zhang** · 2022-12-11

<details>
<summary>Abstract</summary>

High-quality prosodic boundary prediction plays an important role in enhancing speech naturalness and intelligibility in Mandarin text-to-speech tasks. However traditional methods usually require a large amount of token-level labels, which can hardly be applied in low-resource scenarios. In this paper, to solve this problem, we propose a multi-source semi-supervised model using an HMM to assist BERT-based prosody prediction. Our proposed model implements an alternate training mechanism combining BERT-Prosody and HMM, where BERT takes denoised labels from HMM, providing updated character embedding and weak labels for the latter to form a training cycle. Experimental results show that, compared with baseline methods, the F1 score of our model is raised by 1.01%/8.25% respectively at prosodic word/phrase level, approaching the performance of supervised models.

</details>

### [Research on end to end low resource speech synthesis based on meta learning](s2:7abd86453ec8bfa5b8066b1ee549c6c881b887b9.md)
**Guangming Li, Guanyu Li, Yugang Dai, Zhihao Song et al.** · 2022-12-09

<details>
<summary>Abstract</summary>

With the development of deep learning, much progress has been made in end-to-end speech synthesis. The success is obvious especially in quality, pronunciation accuracy, and fluency ,the speech is close to human’s, its accuracy is below human’s tolerance. All these achievements are easy to achieve in the scene of the abundant corpus, however, there are difficulties in corpus collection for 95% languages in today's world and it is difficult to get good results when facing corpus shortage yet. We propose a meta-learning approach to solve the difficulties in low-resource scenarios by learning knowledge from other languages (with a large dataset of high quality). Our model can share information between languages,makes the model trained on a small corpus a good model using the knowledge from other languages. The speech synthesized with our model sounds more natural and achieve a higher level on quality. The resultant speech is close to human’s speech in terms of fluency. We add a parameter generator to the basic end-to-end speech system and our model has smaller parameters than the multilingual model with separate parameters for each language. Experiments show that our model can share information efficiently between languages.

</details>

### [SpeechLMScore: Evaluating speech generation using speech language model](2212.04559.md)
**Soumi Maiti et.al.** · 2022-12-08

### [Learning to Dub Movies via Hierarchical Prosody Models](2212.04054.md)
**Gaoxiang Cong, Liang Li, Yuankai Qi, Zhengjun Zha et al.** · 2022-12-08

<details>
<summary>Abstract</summary>

Given a piece of text, a video clip and a reference audio, the movie dubbing (also known as visual voice clone V2C) task aims to generate speeches that match the speaker's emotion presented in the video using the desired speaker voice as reference. V2C is more challenging than conventional text-to-speech tasks as it additionally requires the generated speech to exactly match the varying emotions and speaking speed presented in the video. Unlike previous works, we propose a novel movie dubbing architecture to tackle these problems via hierarchical prosody modelling, which bridges the visual information to corresponding speech prosody from three aspects: lip, face, and scene. Specifically, we align lip movement to the speech duration, and convey facial expression to speech energy and pitch via attention mechanism based on valence and arousal representations inspired by recent psychology findings. Moreover, we design an emotion booster to capture the atmosphere from global video scenes. All these embeddings together are used to generate mel-spectrogram and then convert to speech waves via existing vocoder. Extensive experimental results on the Chem and V2C benchmark datasets demonstrate the favorable performance of the proposed method. The source code and trained models will be released to the public.

</details>

### [Low-Resource End-to-end Sanskrit TTS using Tacotron2, WaveGlow and Transfer Learning](2212.03558.md)
**Ankur Debnath et.al.** · 2022-12-07

### [Analysis and Utilization of Entrainment on Acoustic and Emotion Features in User-agent Dialogue](2212.03398.md)
**Daxin Tan, Nikos Kargas, David McHardy, Constantinos Papayiannis et al.** · 2022-12-07

<details>
<summary>Abstract</summary>

Entrainment is the phenomenon by which an interlocutor adapts their speaking style to align with their partner in conversations. It has been found in different dimensions as acoustic, prosodic, lexical or syntactic. In this work, we explore and utilize the entrainment phenomenon to improve spoken dialogue systems for voice assistants. We first examine the existence of the entrainment phenomenon in human-to-human dialogues in respect to acoustic feature and then extend the analysis to emotion features. The analysis results show strong evidence of entrainment in terms of both acoustic and emotion features. Based on this findings, we implement two entrainment policies and assess if the integration of entrainment principle into a Text-to-Speech (TTS) system improves the synthesis performance and the user experience. It is found that the integration of the entrainment principle into a TTS system brings performance improvement when considering acoustic features, while no obvious improvement is observed when considering emotion features.

</details>

### [UniSyn: An End-to-End Unified Model for Text-to-Speech and Singing Voice Synthesis](2212.01546.md)
**Yi Lei et.al.** · 2022-12-06

### [Evince the artifacts of Spoof Speech by blending Vocal Tract and Voice Source Features](2212.02013.md)
**Tadipatri Uday Kiran Reddy, Sahukari Chaitanya Varun, Kota Pranav Kumar Sankala Sreekanth, Kodukula Sri Rama Murty** · 2022-12-05

<details>
<summary>Abstract</summary>

With the rapid advancement in synthetic speech generation technologies, great interest in differentiating spoof speech from the natural speech is emerging in the research community. The identification of these synthetic signals is a difficult task not only for the cutting-edge classification models but also for humans themselves. To prevent potential adverse effects, it becomes crucial to detect spoof signals. From a forensics perspective, it is also important to predict the algorithm which generated them to identify the forger. This needs an understanding of the underlying attributes of spoof signals which serve as a signature for the synthesizer. This study emphasizes the segments of speech signals critical in identifying their authenticity by utilizing the Vocal Tract System(\textit{VTS}) and Voice Source(\textit{VS}) features. In this paper, we propose a system that detects spoof signals as well as identifies the corresponding speech-generating algorithm. We achieve 99.58\% in algorithm classification accuracy. From experiments, we found that a VS feature-based system gives more attention to the transition of phonemes, while, a VTS feature-based system gives more attention to stationary segments of speech signals. We perform model fusion techniques on the VS-based and VTS-based systems to exploit the complementary information to develop a robust classifier. Upon analyzing the confusion plots we found that WaveRNN is poorly classified depicting more naturalness. On the other hand, we identified that synthesizer like Waveform Concatenation, and Neural Source Filter is classified with the highest accuracy. Practical implications of this work can aid researchers from both forensics (leverage artifacts) and the speech communities (mitigate artifacts).

</details>

### [ERNIE-SAT: Speech and Text Joint Pretraining for Cross-Lingual Multi-Speaker Text-to-Speech](2211.03545.md)
**Xiaoran Fan et.al.** · 2022-12-04

### [SNAC: Speaker-normalized affine coupling layer in flow-based architecture for zero-shot multi-speaker text-to-speech](2211.16866.md)
**Byoung Jin Choi et.al.** · 2022-11-30

### [Controllable speech synthesis by learning discrete phoneme-level prosodic representations](2211.16307.md)
**Nikolaos Ellinas et.al.** · 2022-11-29

### [Neural Vocoder Feature Estimation for Dry Singing Voice Separation](2211.15948.md)
**Jaekwon Im, Soonbeom Choi, Sangeon Yong, Juhan Nam** · 2022-11-29

<details>
<summary>Abstract</summary>

Singing voice separation (SVS) is a task that separates singing voice audio from its mixture with instrumental audio. Previous SVS studies have mainly employed the spectrogram masking method which requires a large dimensionality in predicting the binary masks. In addition, they focused on extracting a vocal stem that retains the wet sound with the reverberation effect. This result may hinder the reusability of the isolated singing voice. This paper addresses the issues by predicting mel-spectrogram of dry singing voices from the mixed audio as neural vocoder features and synthesizing the singing voice waveforms from the neural vocoder. We experimented with two separation methods. One is predicting binary masks in the mel-spectrogram domain and the other is directly predicting the mel-spectrogram. Furthermore, we add a singing voice detector to identify the singing voice segments over time more explicitly. We measured the model performance in terms of audio, dereverberation, separation, and overall quality. The results show that our proposed model outperforms state-of-the-art singing voice separation models in both objective and subjective evaluation except the audio quality.

</details>

### [Hiding speaker's sex in speech using zero-evidence speaker representation in an analysis/synthesis pipeline](2211.16065.md)
**Paul-Gauthier Noé, Xiaoxiao Miao, Xin Wang, Junichi Yamagishi et al.** · 2022-11-29

<details>
<summary>Abstract</summary>

The use of modern vocoders in an analysis/synthesis pipeline allows us to investigate high-quality voice conversion that can be used for privacy purposes. Here, we propose to transform the speaker embedding and the pitch in order to hide the sex of the speaker. ECAPA-TDNN-based speaker representation fed into a HiFiGAN vocoder is protected using a neural-discriminant analysis approach, which is consistent with the zero-evidence concept of privacy. This approach significantly reduces the information in speech related to the speaker's sex while preserving speech content and some consistency in the resulting protected voices.

</details>

### [Contextual Expressive Text-to-Speech](2211.14548.md)
**Jianhong Tu, Zeyu Cui, Xiaohuan Zhou, Siqi Zheng et al.** · 2022-11-26

<details>
<summary>Abstract</summary>

The goal of expressive Text-to-speech (TTS) is to synthesize natural speech with desired content, prosody, emotion, or timbre, in high expressiveness. Most of previous studies attempt to generate speech from given labels of styles and emotions, which over-simplifies the problem by classifying styles and emotions into a fixed number of pre-defined categories. In this paper, we introduce a new task setting, Contextual TTS (CTTS). The main idea of CTTS is that how a person speaks depends on the particular context she is in, where the context can typically be represented as text. Thus, in the CTTS task, we propose to utilize such context to guide the speech synthesis process instead of relying on explicit labels of styles and emotions. To achieve this task, we construct a synthetic dataset and develop an effective framework. Experiments show that our framework can generate high-quality expressive speech based on the given context both in synthetic datasets and real-world scenarios.

</details>

### [Efficient Incremental Text-to-Speech on GPUs](2211.13939.md)
**Muyang Du, Chuan Liu, Jiaxing Qi, Junjie Lai** · 2022-11-25

<details>
<summary>Abstract</summary>

Incremental text-to-speech, also known as streaming TTS, has been increasingly applied to online speech applications that require ultra-low response latency to provide an optimal user experience. However, most of the existing speech synthesis pipelines deployed on GPU are still non-incremental, which uncovers limitations in high-concurrency scenarios, especially when the pipeline is built with end-to-end neural network models. To address this issue, we present a highly efficient approach to perform real-time incremental TTS on GPUs with Instant Request Pooling and Module-wise Dynamic Batching. Experimental results demonstrate that the proposed method is capable of producing high-quality speech with a first-chunk latency lower than 80ms under 100 QPS on a single NVIDIA A10 GPU and significantly outperforms the non-incremental twin in both concurrency and latency. Our work reveals the effectiveness of high-performance incremental TTS on GPUs.

</details>

### [Puffin: pitch-synchronous neural waveform generation for fullband speech on modest devices](2211.14130.md)
**Oliver Watts, Lovisa Wihlborg, Cassia Valentini-Botinhao** · 2022-11-25

<details>
<summary>Abstract</summary>

We present a neural vocoder designed with low-powered Alternative and Augmentative Communication devices in mind. By combining elements of successful modern vocoders with established ideas from an older generation of technology, our system is able to produce high quality synthetic speech at 48kHz on devices where neural vocoders are otherwise prohibitively complex. The system is trained adversarially using differentiable pitch synchronous overlap add, and reduces complexity by relying on pitch synchronous Inverse Short-Time Fourier Transform (ISTFT) to generate speech samples. Our system achieves comparable quality with a strong (HiFi-GAN) baseline while using only a fraction of the compute. We present results of a perceptual evaluation as well as an analysis of system complexity.

</details>

### [IMaSC -- ICFOSS Malayalam Speech Corpus](2211.12796.md)
**Deepa P Gopinath, Thennal D K, Vrinda V Nair, Swaraj K S et al.** · 2022-11-23

<details>
<summary>Abstract</summary>

Modern text-to-speech (TTS) systems use deep learning to synthesize speech increasingly approaching human quality, but they require a database of high quality audio-text sentence pairs for training. Malayalam, the official language of the Indian state of Kerala and spoken by 35+ million people, is a low resource language in terms of available corpora for TTS systems. In this paper, we present IMaSC, a Malayalam text and speech corpora containing approximately 50 hours of recorded speech. With 8 speakers and a total of 34,473 text-audio pairs, IMaSC is larger than every other publicly available alternative. We evaluated the database by using it to train TTS models for each speaker based on a modern deep learning architecture. Via subjective evaluation, we show that our models perform significantly better in terms of naturalness compared to previous studies and publicly available models, with an average mean opinion score of 4.50, indicating that the synthesized speech is close to human quality.

</details>

### [Adversarial Speaker-Consistency Learning Using Untranscribed Speech Data for Zero-Shot Multi-Speaker Text-to-Speech](2210.05979.md)
**Byoung Jin Choi et.al.** · 2022-11-22

### [PromptTTS: Controllable Text-to-Speech with Text Descriptions](2211.12171.md)
**Zhifang Guo, Yichong Leng, Yihan Wu, Sheng Zhao et al.** · 2022-11-22

<details>
<summary>Abstract</summary>

Using a text description as prompt to guide the generation of text or images (e.g., GPT-3 or DALLE-2) has drawn wide attention recently. Beyond text and image generation, in this work, we explore the possibility of utilizing text descriptions to guide speech synthesis. Thus, we develop a text-to-speech (TTS) system (dubbed as PromptTTS) that takes a prompt with both style and content descriptions as input to synthesize the corresponding speech. Specifically, PromptTTS consists of a style encoder and a content encoder to extract the corresponding representations from the prompt, and a speech decoder to synthesize speech according to the extracted style and content representations. Compared with previous works in controllable TTS that require users to have acoustic knowledge to understand style factors such as prosody and pitch, PromptTTS is more user-friendly since text descriptions are a more natural way to express speech style (e.g., ''A lady whispers to her friend slowly''). Given that there is no TTS dataset with prompts, to benchmark the task of PromptTTS, we construct and release a dataset containing prompts with style and content information and the corresponding speech. Experiments show that PromptTTS can generate speech with precise style control and high speech quality. Audio samples and our dataset are publicly available.

</details>

### [Disentangled Feature Learning for Real-Time Neural Speech Coding](2211.11960.md)
**Xue Jiang, Xiulian Peng, Yuan Zhang, Yan Lu** · 2022-11-22

<details>
<summary>Abstract</summary>

Recently end-to-end neural audio/speech coding has shown its great potential to outperform traditional signal analysis based audio codecs. This is mostly achieved by following the VQ-VAE paradigm where blind features are learned, vector-quantized and coded. In this paper, instead of blind end-to-end learning, we propose to learn disentangled features for real-time neural speech coding. Specifically, more global-like speaker identity and local content features are learned with disentanglement to represent speech. Such a compact feature decomposition not only achieves better coding efficiency by exploiting bit allocation among different features but also provides the flexibility to do audio editing in embedding space, such as voice conversion in real-time communications. Both subjective and objective results demonstrate its coding efficiency and we find that the learned disentangled features show comparable performance on any-to-any voice conversion with modern self-supervised speech representation learning models with far less parameters and low latency, showing the potential of our neural coding framework.

</details>

### [Embedding a Differentiable Mel-cepstral Synthesis Filter to a Neural Speech Synthesis System](2211.11222.md)
**Takenori Yoshimura, Shinji Takaki, Kazuhiro Nakamura, Keiichiro Oura et al.** · 2022-11-21

<details>
<summary>Abstract</summary>

This paper integrates a classic mel-cepstral synthesis filter into a modern neural speech synthesis system towards end-to-end controllable speech synthesis. Since the mel-cepstral synthesis filter is explicitly embedded in neural waveform models in the proposed system, both voice characteristics and the pitch of synthesized speech are highly controlled via a frequency warping parameter and fundamental frequency, respectively. We implement the mel-cepstral synthesis filter as a differentiable and GPU-friendly module to enable the acoustic and waveform models in the proposed system to be simultaneously optimized in an end-to-end manner. Experiments show that the proposed system improves speech quality from a baseline system maintaining controllability. The core PyTorch modules used in the experiments will be publicly available on GitHub.

</details>

### [LA-VocE: Low-SNR Audio-visual Speech Enhancement using Neural Vocoders](2211.10999.md)
**Rodrigo Mira, Buye Xu, Jacob Donley, Anurag Kumar et al.** · 2022-11-20

<details>
<summary>Abstract</summary>

Audio-visual speech enhancement aims to extract clean speech from a noisy environment by leveraging not only the audio itself but also the target speaker's lip movements. This approach has been shown to yield improvements over audio-only speech enhancement, particularly for the removal of interfering speech. Despite recent advances in speech synthesis, most audio-visual approaches continue to use spectral mapping/masking to reproduce the clean audio, often resulting in visual backbones added to existing speech enhancement architectures. In this work, we propose LA-VocE, a new two-stage approach that predicts mel-spectrograms from noisy audio-visual speech via a transformer-based architecture, and then converts them into waveform audio using a neural vocoder (HiFi-GAN). We train and evaluate our framework on thousands of speakers and 11+ different languages, and study our model's ability to adapt to different levels of background noise and speech interference. Our experiments show that LA-VocE outperforms existing methods according to multiple metrics, particularly under very noisy scenarios.

</details>

### [Multi-Speaker Expressive Speech Synthesis via Multiple Factors Decoupling](2211.10568.md)
**Xinfa Zhu, Yi Lei, Kun Song, Yongmao Zhang et al.** · 2022-11-19

<details>
<summary>Abstract</summary>

This paper aims to synthesize the target speaker's speech with desired speaking style and emotion by transferring the style and emotion from reference speech recorded by other speakers. We address this challenging problem with a two-stage framework composed of a text-to-style-and-emotion (Text2SE) module and a style-and-emotion-to-wave (SE2Wave) module, bridging by neural bottleneck (BN) features. To further solve the multi-factor (speaker timbre, speaking style and emotion) decoupling problem, we adopt the multi-label binary vector (MBV) and mutual information (MI) minimization to respectively discretize the extracted embeddings and disentangle these highly entangled factors in both Text2SE and SE2Wave modules. Moreover, we introduce a semi-supervised training strategy to leverage data from multiple speakers, including emotion-labeled data, style-labeled data, and unlabeled data. To better transfer the fine-grained expression from references to the target speaker in non-parallel transfer, we introduce a reference-candidate pool and propose an attention-based reference selection approach. Extensive experiments demonstrate the good design of our model.

</details>

### [NANSY++: Unified Voice Synthesis with Neural Analysis and Synthesis](2211.09407.md)
**Hyeong-Seok Choi et.al.** · 2022-11-17

### [Towards Building Text-To-Speech Systems for the Next Billion Users](2211.09536.md)
**Gokul Karthik Kumar, Praveen S, Pratyush Kumar, Mitesh M. Khapra et al.** · 2022-11-17

<details>
<summary>Abstract</summary>

Deep learning based text-to-speech (TTS) systems have been evolving rapidly with advances in model architectures, training methodologies, and generalization across speakers and languages. However, these advances have not been thoroughly investigated for Indian language speech synthesis. Such investigation is computationally expensive given the number and diversity of Indian languages, relatively lower resource availability, and the diverse set of advances in neural TTS that remain untested. In this paper, we evaluate the choice of acoustic models, vocoders, supplementary loss functions, training schedules, and speaker and language diversity for Dravidian and Indo-Aryan languages. Based on this, we identify monolingual models with FastPitch and HiFi-GAN V1, trained jointly on male and female speakers to perform the best. With this setup, we train and evaluate TTS models for 13 languages and find our models to significantly improve upon existing models in all languages as measured by mean opinion scores. We open-source all models on the Bhashini platform.

</details>

### [EmoDiff: Intensity Controllable Emotional Text-to-Speech with Soft-Label Guidance](2211.09496.md)
**Yiwei Guo, Chenpeng Du, Xie Chen, Kai Yu** · 2022-11-17

<details>
<summary>Abstract</summary>

Although current neural text-to-speech (TTS) models are able to generate high-quality speech, intensity controllable emotional TTS is still a challenging task. Most existing methods need external optimizations for intensity calculation, leading to suboptimal results or degraded quality. In this paper, we propose EmoDiff, a diffusion-based TTS model where emotion intensity can be manipulated by a proposed soft-label guidance technique derived from classifier guidance. Specifically, instead of being guided with a one-hot vector for the specified emotion, EmoDiff is guided with a soft label where the value of the specified emotion and \textit{Neutral} is set to $α$ and $1-α$ respectively. The $α$ here represents the emotion intensity and can be chosen from 0 to 1. Our experiments show that EmoDiff can precisely control the emotion intensity while maintaining high voice quality. Moreover, diverse speech with specified emotion intensity can be generated by sampling in the reverse denoising process.

</details>

### [Back-Translation-Style Data Augmentation for Mandarin Chinese Polyphone Disambiguation](2211.09495.md)
**Chunyu Qiang, Peng Yang, Hao Che, Jinba Xiao et al.** · 2022-11-17

<details>
<summary>Abstract</summary>

Conversion of Chinese Grapheme-to-Phoneme (G2P) plays an important role in Mandarin Chinese Text-To-Speech (TTS) systems, where one of the biggest challenges is the task of polyphone disambiguation. Most of the previous polyphone disambiguation models are trained on manually annotated datasets, and publicly available datasets for polyphone disambiguation are scarce. In this paper we propose a simple back-translation-style data augmentation method for mandarin Chinese polyphone disambiguation, utilizing a large amount of unlabeled text data. Inspired by the back-translation technique proposed in the field of machine translation, we build a Grapheme-to-Phoneme (G2P) model to predict the pronunciation of polyphonic character, and a Phoneme-to-Grapheme (P2G) model to predict pronunciation into text. Meanwhile, a window-based matching strategy and a multi-model scoring strategy are proposed to judge the correctness of the pseudo-label. We design a data balance strategy to improve the accuracy of some typical polyphonic characters in the training set with imbalanced distribution or data scarcity. The experimental result shows the effectiveness of the proposed back-translation-style data augmentation method.

</details>

### [Low-Resource Mongolian Speech Synthesis Based on Automatic Prosody Annotation](2211.09365.md)
**Xin Yuan, Robin Feng, Mingming Ye** · 2022-11-17

<details>
<summary>Abstract</summary>

While deep learning-based text-to-speech (TTS) models such as VITS have shown excellent results, they typically require a sizable set of high-quality <text, audio> pairs to train, which is expensive to collect. So far, most languages in the world still lack the training data needed to develop TTS systems. This paper proposes two improvement methods for the two problems faced by low-resource Mongolian speech synthesis: a) In view of the lack of high-quality <text, audio> pairs of data, it is difficult to model the mapping problem from linguistic features to acoustic features. Improvements are made using pre-trained VITS model and transfer learning methods. b) In view of the problem of less labeled information, this paper proposes to use an automatic prosodic annotation method to label the prosodic information of text and corresponding speech, thereby improving the naturalness and intelligibility of low-resource Mongolian language. Through empirical research, the N-MOS of the method proposed in this paper is 4.195, and the I-MOS is 4.228.

</details>

### [NatiQ: An End-to-end Text-to-Speech System for Arabic](2206.07373.md)
**Ahmed Abdelali et.al.** · 2022-11-16

### [Delivering Speaking Style in Low-resource Voice Conversion with Multi-factor Constraints](2211.08857.md)
**Zhichao Wang, Xinsheng Wang, Lei Xie, Yuanzhe Chen et al.** · 2022-11-16

<details>
<summary>Abstract</summary>

Conveying the linguistic content and maintaining the source speech's speaking style, such as intonation and emotion, is essential in voice conversion (VC). However, in a low-resource situation, where only limited utterances from the target speaker are accessible, existing VC methods are hard to meet this requirement and capture the target speaker's timber. In this work, a novel VC model, referred to as MFC-StyleVC, is proposed for the low-resource VC task. Specifically, speaker timbre constraint generated by clustering method is newly proposed to guide target speaker timbre learning in different stages. Meanwhile, to prevent over-fitting to the target speaker's limited data, perceptual regularization constraints explicitly maintain model performance on specific aspects, including speaking style, linguistic content, and speech quality. Besides, a simulation mode is introduced to simulate the inference process to alleviate the mismatch between training and inference. Extensive experiments performed on highly expressive speech demonstrate the superiority of the proposed method in low-resource VC.

</details>

### [SNIPER Training: Variable Sparsity Rate Training For Text-To-Speech](2211.07283.md)
**Perry Lam et.al.** · 2022-11-14

### [The Potential of Neural Speech Synthesis-based Data Augmentation for Personalized Speech Enhancement](2211.07493.md)
**Anastasia Kuznetsova, Aswin Sivaraman, Minje Kim** · 2022-11-14

<details>
<summary>Abstract</summary>

With the advances in deep learning, speech enhancement systems benefited from large neural network architectures and achieved state-of-the-art quality. However, speaker-agnostic methods are not always desirable, both in terms of quality and their complexity, when they are to be used in a resource-constrained environment. One promising way is personalized speech enhancement (PSE), which is a smaller and easier speech enhancement problem for small models to solve, because it focuses on a particular test-time user. To achieve the personalization goal, while dealing with the typical lack of personal data, we investigate the effect of data augmentation based on neural speech synthesis (NSS). In the proposed method, we show that the quality of the NSS system's synthetic data matters, and if they are good enough the augmented dataset can be used to improve the PSE system that outperforms the speaker-agnostic baseline. The proposed PSE systems show significant complexity reduction while preserving the enhancement quality.

</details>

### [A unified one-shot prosody and speaker conversion system with self-supervised discrete speech units](2211.06535.md)
**Li-Wei Chen, Shinji Watanabe, Alexander Rudnicky** · 2022-11-12

<details>
<summary>Abstract</summary>

We present a unified system to realize one-shot voice conversion (VC) on the pitch, rhythm, and speaker attributes. Existing works generally ignore the correlation between prosody and language content, leading to the degradation of naturalness in converted speech. Additionally, the lack of proper language features prevents these systems from accurately preserving language content after conversion. To address these issues, we devise a cascaded modular system leveraging self-supervised discrete speech units as language representation. These discrete units provide duration information essential for rhythm modeling. Our system first extracts utterance-level prosody and speaker representations from the raw waveform. Given the prosody representation, a prosody predictor estimates pitch, energy, and duration for each discrete unit in the utterance. A synthesizer further reconstructs speech based on the predicted prosody, speaker representation, and discrete units. Experiments show that our system outperforms previous approaches in naturalness, intelligibility, speaker transferability, and prosody transferability. Code and samples are publicly available.

</details>

### [Content-Dependent Fine-Grained Speaker Embedding for Zero-Shot Speaker Adaptation in Text-to-Speech Synthesis](2204.00990.md)
**Yixuan Zhou et.al.** · 2022-11-11

### [MaskedSpeech: Context-aware Speech Synthesis with Masking Strategy](2211.06170.md)
**Ya-Jie Zhang, Wei Song, Yanghao Yue, Zhengchen Zhang et al.** · 2022-11-11

<details>
<summary>Abstract</summary>

Humans often speak in a continuous manner which leads to coherent and consistent prosody properties across neighboring utterances. However, most state-of-the-art speech synthesis systems only consider the information within each sentence and ignore the contextual semantic and acoustic features. This makes it inadequate to generate high-quality paragraph-level speech which requires high expressiveness and naturalness. To synthesize natural and expressive speech for a paragraph, a context-aware speech synthesis system named MaskedSpeech is proposed in this paper, which considers both contextual semantic and acoustic features. Inspired by the masking strategy in the speech editing research, the acoustic features of the current sentence are masked out and concatenated with those of contextual speech, and further used as additional model input. The phoneme encoder takes the concatenated phoneme sequence from neighboring sentences as input and learns fine-grained semantic information from contextual text. Furthermore, cross-utterance coarse-grained semantic features are employed to improve the prosody generation. The model is trained to reconstruct the masked acoustic features with the augmentation of both the contextual semantic and acoustic features. Experimental results demonstrate that the proposed MaskedSpeech outperformed the baseline system significantly in terms of naturalness and expressiveness.

</details>

### [EmoFake: An Initial Dataset for Emotion Fake Audio Detection](2211.05363.md)
**Yan Zhao, Jiangyan Yi, Jianhua Tao, Chenglong Wang et al.** · 2022-11-10

<details>
<summary>Abstract</summary>

Many datasets have been designed to further the development of fake audio detection, such as datasets of the ASVspoof and ADD challenges. However, these datasets do not consider a situation that the emotion of the audio has been changed from one to another, while other information (e.g. speaker identity and content) remains the same. Changing the emotion of an audio can lead to semantic changes. Speech with tampered semantics may pose threats to people's lives. Therefore, this paper reports our progress in developing such an emotion fake audio detection dataset involving changing emotion state of the origin audio named EmoFake. The fake audio in EmoFake is generated by open source emotion voice conversion models. Furthermore, we proposed a method named Graph Attention networks using Deep Emotion embedding (GADE) for the detection of emotion fake audio. Some benchmark experiments are conducted on this dataset. The results show that our designed dataset poses a challenge to the fake audio detection model trained with the LA dataset of ASVspoof 2019. The proposed GADE shows good performance in the face of emotion fake audio.

</details>

### [Expressive-VC: Highly Expressive Voice Conversion with Attention Fusion of Bottleneck and Perturbation Features](2211.04710.md)
**Ziqian Ning, Qicong Xie, Pengcheng Zhu, Zhichao Wang et al.** · 2022-11-09

<details>
<summary>Abstract</summary>

Voice conversion for highly expressive speech is challenging. Current approaches struggle with the balancing between speaker similarity, intelligibility and expressiveness. To address this problem, we propose Expressive-VC, a novel end-to-end voice conversion framework that leverages advantages from both neural bottleneck feature (BNF) approach and information perturbation approach. Specifically, we use a BNF encoder and a Perturbed-Wav encoder to form a content extractor to learn linguistic and para-linguistic features respectively, where BNFs come from a robust pre-trained ASR model and the perturbed wave becomes speaker-irrelevant after signal perturbation. We further fuse the linguistic and para-linguistic features through an attention mechanism, where speaker-dependent prosody features are adopted as the attention query, which result from a prosody encoder with target speaker embedding and normalized pitch and energy of source speech as input. Finally the decoder consumes the integrated features and the speaker-dependent prosody feature to generate the converted speech. Experiments demonstrate that Expressive-VC is superior to several state-of-the-art systems, achieving both high expressiveness captured from the source speech and high speaker similarity with the target speaker; meanwhile intelligibility is well maintained.

</details>

### [PhaseAug: A Differentiable Augmentation for Speech Synthesis to Simulate One-to-Many Mapping](2211.04610.md)
**Junhyeok Lee, Seungu Han, Hyunjae Cho, Wonbin Jung** · 2022-11-08

<details>
<summary>Abstract</summary>

Previous generative adversarial network (GAN)-based neural vocoders are trained to reconstruct the exact ground truth waveform from the paired mel-spectrogram and do not consider the one-to-many relationship of speech synthesis. This conventional training causes overfitting for both the discriminators and the generator, leading to the periodicity artifacts in the generated audio signal. In this work, we present PhaseAug, the first differentiable augmentation for speech synthesis that rotates the phase of each frequency bin to simulate one-to-many mapping. With our proposed method, we outperform baselines without any architecture modification. Code and audio samples will be available at https://github.com/mindslab-ai/phaseaug.

</details>

### [Accented Text-to-Speech Synthesis with a Conditional Variational Autoencoder](2211.03316.md)
**Jan Melechovsky et.al.** · 2022-11-07

### [Towards Integration of Embodiment Features for Prosodic Prominence Prediction from Text](s2:39ff162d527c4a3529b41f4f8e4a79112b843d9f.md)
**P. Madhyastha** · 2022-11-07

<details>
<summary>Abstract</summary>

Prosodic prominence prediction is an important task in the area of speech processing and especially forms an essential part of modern text-to-speech systems. Previous work has broadly focused on acoustic and linguistic features (such as syntactic and semantic features) for predicting prosodic prominence. However, human models of prosody are known to be highly multimodal and grounded on denotations of physical entities and embodied experience. In this paper we present a first study where we integrate multimodal sensorimotor associations by exploiting the Lancaster Sensorimotor Norms towards prosodic prominence prediction. Our results highlight the importance of sensorimotor knowledge especially for models in low-data regimens where we show that it improves the performance by a significant margin.

</details>

### [Adaptive End-to-End Text-to-Speech Synthesis Based on Error Correction Feedback from Humans](s2:2bf14a1cdefc2e549cd655ac99ced53696182d0d.md)
**Kazuki Fujii, Yuki Saito, H. Saruwatari** · 2022-11-07

<details>
<summary>Abstract</summary>

We propose an end-to-end text-to-speech (TTS) method that can intuitively correct accent errors in synthetic speech by using feedback from humans. State-of-the-art end-to-end TTS methods can synthesize high-quality speech, but humans can hardly interpret the black-boxed TTS system represented as a stack of neural networks. This reduced interpretability prevents humans from controlling the TTS system to correct errors in synthetic speech intuitively. In this paper, we focus on a method to involve human listeners in the process of accent error correction for synthetic speech generated by end-to-end TTS. Specifically, we build an end-to-end TTS model equipping a prosody predictor that estimates the change of pitch for each syllable from phoneme embeddings and context-aware word embedding. Then, we perform a human-in-the-loop (HITL) framework to correct errors of the prosody predictor using collective intelligence of human listeners. The results of Japanese TTS experiments show that our HITL framework can successfully correct accent errors and contribute to the quality of synthetic speech comparable to the conventional method requiring an accent dictionary for text analysis.

</details>

### [Parallel Attention Forcing for Machine Translation](2211.03237.md)
**Qingyun Dou, Mark Gales** · 2022-11-06

<details>
<summary>Abstract</summary>

Attention-based autoregressive models have achieved state-of-the-art performance in various sequence-to-sequence tasks, including Text-To-Speech (TTS) and Neural Machine Translation (NMT), but can be difficult to train. The standard training approach, teacher forcing, guides a model with the reference back-history. During inference, the generated back-history must be used. This mismatch limits the evaluation performance. Attention forcing has been introduced to address the mismatch, guiding the model with the generated back-history and reference attention. While successful in tasks with continuous outputs like TTS, attention forcing faces additional challenges in tasks with discrete outputs like NMT. This paper introduces the two extensions of attention forcing to tackle these challenges. (1) Scheduled attention forcing automatically turns attention forcing on and off, which is essential for tasks with discrete outputs. (2) Parallel attention forcing makes training parallel, and is applicable to Transformer-based models. The experiments show that the proposed approaches improve the performance of models based on RNNs and Transformers.

</details>

### [An Empirical Study on L2 Accents of Cross-lingual Text-to-Speech Systems via Vowel Space](2211.03078.md)
**Jihwan Lee, Jae-Sung Bae, Seongkyu Mun, Heejin Choi et al.** · 2022-11-06

<details>
<summary>Abstract</summary>

With the recent developments in cross-lingual Text-to-Speech (TTS) systems, L2 (second-language, or foreign) accent problems arise. Moreover, running a subjective evaluation for such cross-lingual TTS systems is troublesome. The vowel space analysis, which is often utilized to explore various aspects of language including L2 accents, is a great alternative analysis tool. In this study, we apply the vowel space analysis method to explore L2 accents of cross-lingual TTS systems. Through the vowel space analysis, we observe the three followings: a) a parallel architecture (Glow-TTS) is less L2-accented than an auto-regressive one (Tacotron); b) L2 accents are more dominant in non-shared vowels in a language pair; and c) L2 accents of cross-lingual TTS systems share some phenomena with those of human L2 learners. Our findings imply that it is necessary for TTS systems to handle each language pair differently, depending on their linguistic characteristics such as non-shared vowels. They also hint that we can further incorporate linguistics knowledge in developing cross-lingual TTS systems.

</details>

### [Deliberation Networks and How to Train Them](2211.03217.md)
**Qingyun Dou, Mark Gales** · 2022-11-06

<details>
<summary>Abstract</summary>

Deliberation networks are a family of sequence-to-sequence models, which have achieved state-of-the-art performance in a wide range of tasks such as machine translation and speech synthesis. A deliberation network consists of multiple standard sequence-to-sequence models, each one conditioned on the initial input and the output of the previous model. During training, there are several key questions: whether to apply Monte Carlo approximation to the gradients or the loss, whether to train the standard models jointly or separately, whether to run an intermediate model in teacher forcing or free running mode, whether to apply task-specific techniques. Previous work on deliberation networks typically explores one or two training options for a specific task. This work introduces a unifying framework, covering various training options, and addresses the above questions. In general, it is simpler to approximate the gradients. When parallel training is essential, separate training should be adopted. Regardless of the task, the intermediate model should be in free running mode. For tasks where the output is continuous, a guided attention loss can be used to prevent degradation into a standard model.

</details>

### [Preserving background sound in noise-robust voice conversion via multi-task learning](2211.03036.md)
**Jixun Yao, Yi Lei, Qing Wang, Pengcheng Guo et al.** · 2022-11-06

<details>
<summary>Abstract</summary>

Background sound is an informative form of art that is helpful in providing a more immersive experience in real-application voice conversion (VC) scenarios. However, prior research about VC, mainly focusing on clean voices, pay rare attention to VC with background sound. The critical problem for preserving background sound in VC is inevitable speech distortion by the neural separation model and the cascade mismatch between the source separation model and the VC model. In this paper, we propose an end-to-end framework via multi-task learning which sequentially cascades a source separation (SS) module, a bottleneck feature extraction module and a VC module. Specifically, the source separation task explicitly considers critical phase information and confines the distortion caused by the imperfect separation process. The source separation task, the typical VC task and the unified task shares a uniform reconstruction loss constrained by joint training to reduce the mismatch between the SS and VC modules. Experimental results demonstrate that our proposed framework significantly outperforms the baseline systems while achieving comparable quality and speaker similarity to the VC models trained with clean data.

</details>

### [Nix-TTS: Lightweight and End-to-End Text-to-Speech via Module-wise Distillation](2203.15643.md)
**Rendi Chevi et.al.** · 2022-11-05

### [NoreSpeech: Knowledge Distillation based Conditional Diffusion Model for Noise-robust Expressive TTS](2211.02448.md)
**Dongchao Yang et.al.** · 2022-11-04

### [Improving Speech Prosody of Audiobook Text-to-Speech Synthesis with Acoustic and Textual Contexts](2211.02336.md)
**Detai Xin, Sharath Adavanne, Federico Ang, Ashish Kulkarni et al.** · 2022-11-04

<details>
<summary>Abstract</summary>

We present a multi-speaker Japanese audiobook text-to-speech (TTS) system that leverages multimodal context information of preceding acoustic context and bilateral textual context to improve the prosody of synthetic speech. Previous work either uses unilateral or single-modality context, which does not fully represent the context information. The proposed method uses an acoustic context encoder and a textual context encoder to aggregate context information and feeds it to the TTS model, which enables the model to predict context-dependent prosody. We conducted comprehensive objective and subjective evaluations on a multi-speaker Japanese audiobook dataset. Experimental results demonstrate that the proposed method significantly outperforms two previous works. Additionally, we present insights about the different choices of context - modalities, lateral information and length - for audiobook TTS that have never been discussed in the literature before.

</details>

### [Self-Supervised Learning for Speech Enhancement through Synthesis](2211.02542.md)
**Bryce Irvin, Marko Stamenovic, Mikolaj Kegler, Li-Chia Yang** · 2022-11-04

<details>
<summary>Abstract</summary>

Modern speech enhancement (SE) networks typically implement noise suppression through time-frequency masking, latent representation masking, or discriminative signal prediction. In contrast, some recent works explore SE via generative speech synthesis, where the system's output is synthesized by a neural vocoder after an inherently lossy feature-denoising step. In this paper, we propose a denoising vocoder (DeVo) approach, where a vocoder accepts noisy representations and learns to directly synthesize clean speech. We leverage rich representations from self-supervised learning (SSL) speech models to discover relevant features. We conduct a candidate search across 15 potential SSL front-ends and subsequently train our vocoder adversarially with the best SSL configuration. Additionally, we demonstrate a causal version capable of running on streaming audio with 10ms latency and minimal performance degradation. Finally, we conduct both objective evaluations and subjective listening studies to show our system improves objective metrics and outperforms an existing state-of-the-art SE model subjectively.

</details>

### [Neural Feature Predictor and Discriminative Residual Coding for Low-Bitrate Speech Coding](2211.02506.md)
**Haici Yang, Wootaek Lim, Minje Kim** · 2022-11-04

<details>
<summary>Abstract</summary>

Low and ultra-low-bitrate neural speech coding achieves unprecedented coding gain by generating speech signals from compact speech features. This paper introduces additional coding efficiency in neural speech coding by reducing the temporal redundancy existing in the frame-level feature sequence via a recurrent neural predictor. The prediction can achieve a low-entropy residual representation, which we discriminatively code based on their contribution to the signal reconstruction. The harmonization of feature prediction and discriminative coding results in a dynamic bit allocation algorithm that spends more bits on unpredictable but rare events. As a result, we develop a scalable, lightweight, low-latency, and low-bitrate neural speech coding system. We demonstrate the advantage of the proposed methods using the LPCNet as a neural vocoder. While the proposed method guarantees causality in its prediction, the subjective tests and feature space analysis show that our model achieves superior coding efficiency compared to LPCNet and Lyra V2 in the very low bitrates.

</details>

### [Robust MelGAN: A robust universal neural vocoder for high-fidelity TTS](2210.17349.md)
**Kun Song et.al.** · 2022-11-02

### [Multi-Speaker Multi-Style Speech Synthesis with Timbre and Style Disentanglement](2211.00967.md)
**Wei Song, Yanghao Yue, Ya-jie Zhang, Zhengchen Zhang et al.** · 2022-11-02

<details>
<summary>Abstract</summary>

Disentanglement of a speaker's timbre and style is very important for style transfer in multi-speaker multi-style text-to-speech (TTS) scenarios. With the disentanglement of timbres and styles, TTS systems could synthesize expressive speech for a given speaker with any style which has been seen in the training corpus. However, there are still some shortcomings with the current research on timbre and style disentanglement. The current method either requires single-speaker multi-style recordings, which are difficult and expensive to collect, or uses a complex network and complicated training method, which is difficult to reproduce and control the style transfer behavior. To improve the disentanglement effectiveness of timbres and styles, and to remove the reliance on single-speaker multi-style corpus, a simple but effective timbre and style disentanglement method is proposed in this paper. The FastSpeech2 network is employed as the backbone network, with explicit duration, pitch, and energy trajectory to represent the style. Each speaker's data is considered as a separate and isolated style, then a speaker embedding and a style embedding are added to the FastSpeech2 network to learn disentangled representations. Utterance level pitch and energy normalization are utilized to improve the decoupling effect. Experimental results demonstrate that the proposed model could synthesize speech with any style seen during training with high style similarity while maintaining very high speaker similarity.

</details>

### [Predicting phoneme-level prosody latents using AR and flow-based Prior Networks for expressive speech synthesis](2211.01327.md)
**Konstantinos Klapsas, Karolos Nikitaras, Nikolaos Ellinas, June Sig Sung et al.** · 2022-11-02

<details>
<summary>Abstract</summary>

A large part of the expressive speech synthesis literature focuses on learning prosodic representations of the speech signal which are then modeled by a prior distribution during inference. In this paper, we compare different prior architectures at the task of predicting phoneme level prosodic representations extracted with an unsupervised FVAE model. We use both subjective and objective metrics to show that normalizing flow based prior networks can result in more expressive speech at the cost of a slight drop in quality. Furthermore, we show that the synthesized speech has higher variability, for a given text, due to the nature of normalizing flows. We also propose a Dynamical VAE model, that can generate higher quality speech although with decreased expressiveness and variability compared to the flow based models.

</details>

### [SIMD-size aware weight regularization for fast neural vocoding on CPU](2211.00898.md)
**Hiroki Kanagawa, Yusuke Ijima** · 2022-11-02

<details>
<summary>Abstract</summary>

This paper proposes weight regularization for a faster neural vocoder. Pruning time-consuming DNN modules is a promising way to realize a real-time vocoder on a CPU (e.g. WaveRNN, LPCNet). Regularization that encourages sparsity is also effective in avoiding the quality degradation created by pruning. However, the orders of weight matrices must be contiguous in SIMD size for fast vocoding. To ensure this order, we propose explicit SIMD size aware regularization. Our proposed method reshapes a weight matrix into a tensor so that the weights are aligned by group size in advance, and then computes the group Lasso-like regularization loss. Experiments on 70% sparse subband WaveRNN show that pruning in conventional Lasso and column-wise group Lasso degrades the synthetic speech's naturalness. The vocoder with proposed regularization 1) achieves comparable naturalness to that without pruning and 2) performs meaningfully faster than other conventional vocoders using regularization.

</details>

### [A weighted-variance variational autoencoder model for speech enhancement](2211.00990.md)
**Ali Golmakani, Mostafa Sadeghi, Xavier Alameda-Pineda, Romain Serizel** · 2022-11-02

<details>
<summary>Abstract</summary>

We address speech enhancement based on variational autoencoders, which involves learning a speech prior distribution in the time-frequency (TF) domain. A zero-mean complex-valued Gaussian distribution is usually assumed for the generative model, where the speech information is encoded in the variance as a function of a latent variable. In contrast to this commonly used approach, we propose a weighted variance generative model, where the contribution of each spectrogram time-frame in parameter learning is weighted. We impose a Gamma prior distribution on the weights, which would effectively lead to a Student's t-distribution instead of Gaussian for speech generative modeling. We develop efficient training and speech enhancement algorithms based on the proposed generative model. Our experimental results on spectrogram auto-encoding and speech enhancement demonstrate the effectiveness and robustness of the proposed approach compared to the standard unweighted variance model.

</details>

### [Adapter-Based Extension of Multi-Speaker Text-to-Speech Model for New Speakers](2211.00585.md)
**Cheng-Ping Hsieh et.al.** · 2022-11-01

### [Generating Multilingual Gender-Ambiguous Text-to-Speech Voices](2211.00375.md)
**Konstantinos Markopoulos, Georgia Maniati, Georgios Vamvoukakis, Nikolaos Ellinas et al.** · 2022-11-01

<details>
<summary>Abstract</summary>

The gender of any voice user interface is a key element of its perceived identity. Recently, there has been increasing interest in interfaces where the gender is ambiguous rather than clearly identifying as female or male. This work addresses the task of generating novel gender-ambiguous TTS voices in a multi-speaker, multilingual setting. This is accomplished by efficiently sampling from a latent speaker embedding space using a proposed gender-aware method. Extensive objective and subjective evaluations clearly indicate that this method is able to efficiently generate a range of novel, diverse voices that are consistent and perceived as more gender-ambiguous than a baseline voice across all the languages examined. Interestingly, the gender perception is found to be robust across two demographic factors of the listeners: native language and gender. To our knowledge, this is the first systematic and validated approach that can reliably generate a variety of gender-ambiguous voices.

</details>

### [Learning utterance-level representations through token-level acoustic latents prediction for Expressive Speech Synthesis](2211.00523.md)
**Karolos Nikitaras, Konstantinos Klapsas, Nikolaos Ellinas, Georgia Maniati et al.** · 2022-11-01

<details>
<summary>Abstract</summary>

This paper proposes an Expressive Speech Synthesis model that utilizes token-level latent prosodic variables in order to capture and control utterance-level attributes, such as character acting voice and speaking style. Current works aim to explicitly factorize such fine-grained and utterance-level speech attributes into different representations extracted by modules that operate in the corresponding level. We show that the fine-grained latent space also captures coarse-grained information, which is more evident as the dimension of latent space increases in order to capture diverse prosodic representations. Therefore, a trade-off arises between the diversity of the token-level and utterance-level representations and their disentanglement. We alleviate this issue by first capturing rich speech attributes into a token-level latent space and then, separately train a prior network that given the input text, learns utterance-level representations in order to predict the phoneme-level, posterior latents extracted during the previous step. Both qualitative and quantitative evaluations are used to demonstrate the effectiveness of the proposed approach. Audio samples are available in our demo page.

</details>

### [Cross-lingual Text-To-Speech with Flow-based Voice Conversion for Improved Pronunciation](2210.17264.md)
**Nikolaos Ellinas, Georgios Vamvoukakis, Konstantinos Markopoulos, Georgia Maniati et al.** · 2022-10-31

<details>
<summary>Abstract</summary>

This paper presents a method for end-to-end cross-lingual text-to-speech (TTS) which aims to preserve the target language's pronunciation regardless of the original speaker's language. The model used is based on a non-attentive Tacotron architecture, where the decoder has been replaced with a normalizing flow network conditioned on the speaker identity, allowing both TTS and voice conversion (VC) to be performed by the same model due to the inherent linguistic content and speaker identity disentanglement. When used in a cross-lingual setting, acoustic features are initially produced with a native speaker of the target language and then voice conversion is applied by the same model in order to convert these features to the target speaker's voice. We verify through objective and subjective evaluations that our method can have benefits compared to baseline cross-lingual synthesis. By including speakers averaging 7.5 minutes of speech, we also present positive results on low-resource scenarios.

</details>

### [token2vec: A Joint Self-Supervised Pre-training Framework Using Unpaired Speech and Text](2210.16755.md)
**Xianghu Yue, Junyi Ao, Xiaoxue Gao, Haizhou Li** · 2022-10-30

<details>
<summary>Abstract</summary>

Self-supervised pre-training has been successful in both text and speech processing. Speech and text offer different but complementary information. The question is whether we are able to perform a speech-text joint pre-training on unpaired speech and text. In this paper, we take the idea of self-supervised pre-training one step further and propose token2vec, a novel joint pre-training framework for unpaired speech and text based on discrete representations of speech. Firstly, due to the distinct characteristics between speech and text modalities, where speech is continuous while text is discrete, we first discretize speech into a sequence of discrete speech tokens to solve the modality mismatch problem. Secondly, to solve the length mismatch problem, where the speech sequence is usually much longer than text sequence, we convert the words of text into phoneme sequences and randomly repeat each phoneme in the sequences. Finally, we feed the discrete speech and text tokens into a modality-agnostic Transformer encoder and pre-train with token-level masking language modeling (tMLM). Experiments show that token2vec is significantly superior to various speech-only pre-training baselines, with up to 17.7% relative WER reduction. Token2vec model is also validated on a non-ASR task, i.e., spoken intent classification, and shows good transferability.

</details>

### [Residual Adapters for Few-Shot Text-to-Speech Speaker Adaptation](2210.15868.md)
**Nobuyuki Morioka et.al.** · 2022-10-28

### [NNSVS: A Neural Network-Based Singing Voice Synthesis Toolkit](2210.15987.md)
**Ryuichi Yamamoto, Reo Yoneyama, Tomoki Toda** · 2022-10-28

<details>
<summary>Abstract</summary>

This paper describes the design of NNSVS, an open-source software for neural network-based singing voice synthesis research. NNSVS is inspired by Sinsy, an open-source pioneer in singing voice synthesis research, and provides many additional features such as multi-stream models, autoregressive fundamental frequency models, and neural vocoders. Furthermore, NNSVS provides extensive documentation and numerous scripts to build complete singing voice synthesis systems. Experimental results demonstrate that our best system significantly outperforms our reproduction of Sinsy and other baseline systems. The toolkit is available at https://github.com/nnsvs/nnsvs.

</details>

### [FCTalker: Fine and Coarse Grained Context Modeling for Expressive Conversational Speech Synthesis](2210.15360.md)
**Yifan Hu, Rui Liu, Guanglai Gao, Haizhou Li** · 2022-10-27

<details>
<summary>Abstract</summary>

Conversational Text-to-Speech (TTS) aims to synthesis an utterance with the right linguistic and affective prosody in a conversational context. The correlation between the current utterance and the dialogue history at the utterance level was used to improve the expressiveness of synthesized speech. However, the fine-grained information in the dialogue history at the word level also has an important impact on the prosodic expression of an utterance, which has not been well studied in the prior work. Therefore, we propose a novel expressive conversational TTS model, termed as FCTalker, that learn the fine and coarse grained context dependency at the same time during speech generation. Specifically, the FCTalker includes fine and coarse grained encoders to exploit the word and utterance-level context dependency. To model the word-level dependencies between an utterance and its dialogue history, the fine-grained dialogue encoder is built on top of a dialogue BERT model. The experimental results show that the proposed method outperforms all baselines and generates more expressive speech that is contextually appropriate. We release the source code at: https://github.com/walker-hyf/FCTalker.

</details>

### [A Fast and Accurate Pitch Estimation Algorithm Based on the Pseudo Wigner-Ville Distribution](2210.15272.md)
**Yisi Liu, Peter Wu, Alan W Black, Gopala K. Anumanchipalli** · 2022-10-27

<details>
<summary>Abstract</summary>

Estimation of fundamental frequency (F0) in voiced segments of speech signals, also known as pitch tracking, plays a crucial role in pitch synchronous speech analysis, speech synthesis, and speech manipulation. In this paper, we capitalize on the high time and frequency resolution of the pseudo Wigner-Ville distribution (PWVD) and propose a new PWVD-based pitch estimation method. We devise an efficient algorithm to compute PWVD faster and use cepstrum-based pre-filtering to avoid cross-term interference. Evaluating our approach on a database with speech and electroglottograph (EGG) recordings yields a state-of-the-art mean absolute error (MAE) of around 4Hz. Our approach is also effective at voiced/unvoiced classification and handling sudden frequency changes.

</details>

### [Articulation GAN: Unsupervised modeling of articulatory learning](2210.15173.md)
**Gašper Beguš, Alan Zhou, Peter Wu, Gopala K Anumanchipalli** · 2022-10-27

<details>
<summary>Abstract</summary>

Generative deep neural networks are widely used for speech synthesis, but most existing models directly generate waveforms or spectral outputs. Humans, however, produce speech by controlling articulators, which results in the production of speech sounds through physical properties of sound propagation. We introduce the Articulatory Generator to the Generative Adversarial Network paradigm, a new unsupervised generative model of speech production/synthesis. The Articulatory Generator more closely mimics human speech production by learning to generate articulatory representations (electromagnetic articulography or EMA) in a fully unsupervised manner. A separate pre-trained physical model (ema2wav) then transforms the generated EMA representations to speech waveforms, which get sent to the Discriminator for evaluation. Articulatory analysis suggests that the network learns to control articulators in a similar manner to humans during speech production. Acoustic analysis of the outputs suggests that the network learns to generate words that are both present and absent in the training distribution. We additionally discuss implications of articulatory representations for cognitive models of human language and speech technology in general.

</details>

### [Source-Filter HiFi-GAN: Fast and Pitch Controllable High-Fidelity Neural Vocoder](2210.15533.md)
**Reo Yoneyama, Yi-Chiao Wu, Tomoki Toda** · 2022-10-27

<details>
<summary>Abstract</summary>

Our previous work, the unified source-filter GAN (uSFGAN) vocoder, introduced a novel architecture based on the source-filter theory into the parallel waveform generative adversarial network to achieve high voice quality and pitch controllability. However, the high temporal resolution inputs result in high computation costs. Although the HiFi-GAN vocoder achieves fast high-fidelity voice generation thanks to the efficient upsampling-based generator architecture, the pitch controllability is severely limited. To realize a fast and pitch-controllable high-fidelity neural vocoder, we introduce the source-filter theory into HiFi-GAN by hierarchically conditioning the resonance filtering network on a well-estimated source excitation information. According to the experimental results, our proposed method outperforms HiFi-GAN and uSFGAN on a singing voice generation in voice quality and synthesis speed on a single CPU. Furthermore, unlike the uSFGAN vocoder, the proposed method can be easily adopted/integrated in real-time applications and end-to-end systems.

</details>

### [FreeVC: Towards High-Quality Text-Free One-Shot Voice Conversion](2210.15418.md)
**Jingyi li, Weiping tu, Li xiao** · 2022-10-27

<details>
<summary>Abstract</summary>

Voice conversion (VC) can be achieved by first extracting source content information and target speaker information, and then reconstructing waveform with these information. However, current approaches normally either extract dirty content information with speaker information leaked in, or demand a large amount of annotated data for training. Besides, the quality of reconstructed waveform can be degraded by the mismatch between conversion model and vocoder. In this paper, we adopt the end-to-end framework of VITS for high-quality waveform reconstruction, and propose strategies for clean content information extraction without text annotation. We disentangle content information by imposing an information bottleneck to WavLM features, and propose the spectrogram-resize based data augmentation to improve the purity of extracted content information. Experimental results show that the proposed method outperforms the latest VC models trained with annotated data and has greater robustness.

</details>

### [Text-to-speech synthesis from dark data with evaluation-in-the-loop data selection](2210.14850.md)
**Kentaro Seki, Shinnosuke Takamichi, Takaaki Saeki, Hiroshi Saruwatari** · 2022-10-26

<details>
<summary>Abstract</summary>

This paper proposes a method for selecting training data for text-to-speech (TTS) synthesis from dark data. TTS models are typically trained on high-quality speech corpora that cost much time and money for data collection, which makes it very challenging to increase speaker variation. In contrast, there is a large amount of data whose availability is unknown (a.k.a, "dark data"), such as YouTube videos. To utilize data other than TTS corpora, previous studies have selected speech data from the corpora on the basis of acoustic quality. However, considering that TTS models robust to data noise have been proposed, we should select data on the basis of its importance as training data to the given TTS model, not the quality of speech itself. Our method with a loop of training and evaluation selects training data on the basis of the automatically predicted quality of synthetic speech of a given TTS model. Results of evaluations using YouTube data reveal that our method outperforms the conventional acoustic-quality-based method.

</details>

### [Cover Reproducible Steganography via Deep Generative Models](2210.14632.md)
**Kejiang Chen, Hang Zhou, Yaofei Wang, Menghan Li et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

Whereas cryptography easily arouses attacks by means of encrypting a secret message into a suspicious form, steganography is advantageous for its resilience to attacks by concealing the message in an innocent-looking cover signal. Minimal distortion steganography, one of the mainstream steganography frameworks, embeds messages while minimizing the distortion caused by the modification on the cover elements. Due to the unavailability of the original cover signal for the receiver, message embedding is realized by finding the coset leader of the syndrome function of steganographic codes migrated from channel coding, which is complex and has limited performance. Fortunately, deep generative models and the robust semantic of generated data make it possible for the receiver to perfectly reproduce the cover signal from the stego signal. With this advantage, we propose cover-reproducible steganography where the source coding, e.g., arithmetic coding, serves as the steganographic code. Specifically, the decoding process of arithmetic coding is used for message embedding and its encoding process is regarded as message extraction. Taking text-to-speech and text-to-image synthesis tasks as two examples, we illustrate the feasibility of cover-reproducible steganography. Steganalysis experiments and theoretical analysis are conducted to demonstrate that the proposed methods outperform the existing methods in most cases.

</details>

### [The NPU-ASLP System for The ISCSLP 2022 Magichub Code-Swiching ASR Challenge](2210.14448.md)
**Yuhao Liang, Peikun Chen, Fan Yu, Xinfa Zhu et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

This paper describes our NPU-ASLP system submitted to the ISCSLP 2022 Magichub Code-Switching ASR Challenge. In this challenge, we first explore several popular end-to-end ASR architectures and training strategies, including bi-encoder, language-aware encoder (LAE) and mixture of experts (MoE). To improve our system's language modeling ability, we further attempt the internal language model as well as the long context language model. Given the limited training data in the challenge, we further investigate the effects of data augmentation, including speed perturbation, pitch shifting, speech codec, SpecAugment and synthetic data from text-to-speech (TTS). Finally, we explore ROVER-based score fusion to make full use of complementary hypotheses from different models. Our submitted system achieves 16.87% on mix error rate (MER) on the test set and comes to the 2nd place in the challenge ranking.

</details>

### [Bloom Library: Multimodal Datasets in 300+ Languages for a Variety of Downstream Tasks](2210.14712.md)
**Colin Leong, Joshua Nemecek, Jacob Mansdorfer, Anna Filighera et al.** · 2022-10-26

<details>
<summary>Abstract</summary>

We present Bloom Library, a linguistically diverse set of multimodal and multilingual datasets for language modeling, image captioning, visual storytelling, and speech synthesis/recognition. These datasets represent either the most, or among the most, multilingual datasets for each of the included downstream tasks. In total, the initial release of the Bloom Library datasets covers 363 languages across 32 language families. We train downstream task models for various languages represented in the data, showing the viability of the data for future work in low-resource, multimodal NLP and establishing the first known baselines for these downstream tasks in certain languages (e.g., Bisu [bzi], with an estimated population of 700 users). Some of these first-of-their-kind baselines are comparable to state-of-the-art performance for higher-resourced languages. The Bloom Library datasets are released under Creative Commons licenses on the Hugging Face datasets hub to catalyze more linguistically diverse research in the included downstream tasks.

</details>

### [RedPen: Region- and Reason-Annotated Dataset of Unnatural Speech](2210.14406.md)
**Kyumin Park, Keon Lee, Daeyoung Kim, Dongyeop Kang** · 2022-10-26

<details>
<summary>Abstract</summary>

Even with recent advances in speech synthesis models, the evaluation of such models is based purely on human judgement as a single naturalness score, such as the Mean Opinion Score (MOS). The score-based metric does not give any further information about which parts of speech are unnatural or why human judges believe they are unnatural. We present a novel speech dataset, RedPen, with human annotations on unnatural speech regions and their corresponding reasons. RedPen consists of 180 synthesized speeches with unnatural regions annotated by crowd workers; These regions are then reasoned and categorized by error types, such as voice trembling and background noise. We find that our dataset shows a better explanation for unnatural speech regions than the model-driven unnaturalness prediction. Our analysis also shows that each model includes different types of error types. Summing up, our dataset successfully shows the possibility that various error regions and types lie under the single naturalness score. We believe that our dataset will shed light on the evaluation and development of more interpretable speech models in the future. Our dataset will be publicly available upon acceptance.

</details>

### [Semi-Supervised Learning Based on Reference Model for Low-resource TTS](2210.14723.md)
**Xulong Zhang, Jianzong Wang, Ning Cheng, Jing Xiao** · 2022-10-25

<details>
<summary>Abstract</summary>

Most previous neural text-to-speech (TTS) methods are mainly based on supervised learning methods, which means they depend on a large training dataset and hard to achieve comparable performance under low-resource conditions. To address this issue, we propose a semi-supervised learning method for neural TTS in which labeled target data is limited, which can also resolve the problem of exposure bias in the previous auto-regressive models. Specifically, we pre-train the reference model based on Fastspeech2 with much source data, fine-tuned on a limited target dataset. Meanwhile, pseudo labels generated by the original reference model are used to guide the fine-tuned model's training further, achieve a regularization effect, and reduce the overfitting of the fine-tuned model during training on the limited target data. Experimental results show that our proposed semi-supervised learning scheme with limited target data significantly improves the voice quality for test data to achieve naturalness and robustness in speech synthesis.

</details>

### [Adapitch: Adaption Multi-Speaker Text-to-Speech Conditioned on Pitch Disentangling with Untranscribed Data](2210.13803.md)
**Xulong Zhang, Jianzong Wang, Ning Cheng, Jing Xiao** · 2022-10-25

<details>
<summary>Abstract</summary>

In this paper, we proposed Adapitch, a multi-speaker TTS method that makes adaptation of the supervised module with untranscribed data. We design two self supervised modules to train the text encoder and mel decoder separately with untranscribed data to enhance the representation of text and mel. To better handle the prosody information in a synthesized voice, a supervised TTS module is designed conditioned on content disentangling of pitch, text, and speaker. The training phase was separated into two parts, pretrained and fixed the text encoder and mel decoder with unsupervised mode, then the supervised mode on the disentanglement of TTS. Experiment results show that the Adaptich achieved much better quality than baseline methods.

</details>

### [MetaSpeech: Speech Effects Switch Along with Environment for Metaverse](2210.13811.md)
**Xulong Zhang, Jianzong Wang, Ning Cheng, Jing Xiao** · 2022-10-25

<details>
<summary>Abstract</summary>

Metaverse expands the physical world to a new dimension, and the physical environment and Metaverse environment can be directly connected and entered. Voice is an indispensable communication medium in the real world and Metaverse. Fusion of the voice with environment effects is important for user immersion in Metaverse. In this paper, we proposed using the voice conversion based method for the conversion of target environment effect speech. The proposed method was named MetaSpeech, which introduces an environment effect module containing an effect extractor to extract the environment information and an effect encoder to encode the environment effect condition, in which gradient reversal layer was used for adversarial training to keep the speech content and speaker information while disentangling the environmental effects. From the experiment results on the public dataset of LJSpeech with four environment effects, the proposed model could complete the specific environment effect conversion and outperforms the baseline methods from the voice conversion task.

</details>

### [Disentangled Speech Representation Learning for One-Shot Cross-lingual Voice Conversion Using $β$-VAE](2210.13771.md)
**Hui Lu, Disong Wang, Xixin Wu, Zhiyong Wu et al.** · 2022-10-25

<details>
<summary>Abstract</summary>

We propose an unsupervised learning method to disentangle speech into content representation and speaker identity representation. We apply this method to the challenging one-shot cross-lingual voice conversion task to demonstrate the effectiveness of the disentanglement. Inspired by $β$-VAE, we introduce a learning objective that balances between the information captured by the content and speaker representations. In addition, the inductive biases from the architectural design and the training dataset further encourage the desired disentanglement. Both objective and subjective evaluations show the effectiveness of the proposed method in speech disentanglement and in one-shot cross-lingual voice conversion.

</details>

### [Mixed-EVC: Mixed Emotion Synthesis and Control in Voice Conversion](2210.13756.md)
**Kun Zhou, Berrak Sisman, Carlos Busso, Bin Ma et al.** · 2022-10-25

<details>
<summary>Abstract</summary>

Emotional voice conversion (EVC) traditionally targets the transformation of spoken utterances from one emotional state to another, with previous research mainly focusing on discrete emotion categories. This paper departs from the norm by introducing a novel perspective: a nuanced rendering of mixed emotions and enhancing control over emotional expression. To achieve this, we propose a novel EVC framework, Mixed-EVC, which only leverages discrete emotion training labels. We construct an attribute vector that encodes the relationships among these discrete emotions, which is predicted using a ranking-based support vector machine and then integrated into a sequence-to-sequence (seq2seq) EVC framework. Mixed-EVC not only learns to characterize the input emotional style but also quantifies its relevance to other emotions during training. As a result, users have the ability to assign these attributes to achieve their desired rendering of mixed emotions. Objective and subjective evaluations confirm the effectiveness of our approach in terms of mixed emotion synthesis and control while surpassing traditional baselines in the conversion of discrete emotions from one to another.

</details>

### [Efficiently Trained Low-Resource Mongolian Text-to-Speech System Based On FullConv-TTS](2211.01948.md)
**Ziqi Liang** · 2022-10-24

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) have become the standard modeling technique for sequence data, and are used in a number of novel text-to-speech models. However, training a TTS model including RNN components has certain requirements for GPU performance and takes a long time. In contrast, studies have shown that CNN-based sequence synthesis technology can greatly reduce training time in text-to-speech models while ensuring a certain performance due to its high parallelism. We propose a new text-to-speech system based on deep convolutional neural networks that does not employ any RNN components (recurrent units). At the same time, we improve the generality and robustness of our model through a series of data augmentation methods such as Time Warping, Frequency Mask, and Time Mask. The final experimental results show that the TTS model using only the CNN component can reduce the training time compared to the classic TTS models such as Tacotron while ensuring the quality of the synthesized speech.

</details>

### [Low-Resource Multilingual and Zero-Shot Multispeaker TTS](2210.12223.md)
**Florian Lux et.al.** · 2022-10-21

### [Exact Prosody Cloning in Zero-Shot Multispeaker Text-to-Speech](2206.12229.md)
**Florian Lux et.al.** · 2022-10-21

### [Adaptive re-calibration of channel-wise features for Adversarial Audio Classification](2210.11722.md)
**Vardhan Dongre, Abhinav Thimma Reddy, Nikhitha Reddeddy** · 2022-10-21

<details>
<summary>Abstract</summary>

DeepFake Audio, unlike DeepFake images and videos, has been relatively less explored from detection perspective, and the solutions which exist for the synthetic speech classification either use complex networks or dont generalize to different varieties of synthetic speech obtained using different generative and optimization-based methods. Through this work, we propose a channel-wise recalibration of features using attention feature fusion for synthetic speech detection and compare its performance against different detection methods including End2End models and Resnet-based models on synthetic speech generated using Text to Speech and Vocoder systems like WaveNet, WaveRNN, Tactotron, and WaveGlow. We also experiment with Squeeze Excitation (SE) blocks in our Resnet models and found that the combination was able to get better performance. In addition to the analysis, we also demonstrate that the combination of Linear frequency cepstral coefficients (LFCC) and Mel Frequency cepstral coefficients (MFCC) using the attentional feature fusion technique creates better input features representations which can help even simpler models generalize well on synthetic speech classification tasks. Our models (Resnet based using feature fusion) trained on Fake or Real (FoR) dataset and were able to achieve 95% test accuracy with the FoR data, and an average of 90% accuracy with samples we generated using different generative models after adapting this framework.

</details>

### [Text Enhancement for Paragraph Processing in End-to-End Code-switching TTS](2210.11429.md)
**Chunyu Qiang et.al.** · 2022-10-20

### [Robust One-Shot Singing Voice Conversion](2210.11096.md)
**Naoya Takahashi, Mayank Kumar Singh, Yuki Mitsufuji** · 2022-10-20

<details>
<summary>Abstract</summary>

Recent progress in deep generative models has improved the quality of voice conversion in the speech domain. However, high-quality singing voice conversion (SVC) of unseen singers remains challenging due to the wider variety of musical expressions in pitch, loudness, and pronunciation. Moreover, singing voices are often recorded with reverb and accompaniment music, which make SVC even more challenging. In this work, we present a robust one-shot SVC (ROSVC) that performs any-to-any SVC robustly even on such distorted singing voices. To this end, we first propose a one-shot SVC model based on generative adversarial networks that generalizes to unseen singers via partial domain conditioning and learns to accurately recover the target pitch via pitch distribution matching and AdaIN-skip conditioning. We then propose a two-stage training method called Robustify that train the one-shot SVC model in the first stage on clean data to ensure high-quality conversion, and introduces enhancement modules to the encoders of the model in the second stage to enhance the feature extraction from distorted singing voices. To further improve the voice quality and pitch reconstruction accuracy, we finally propose a hierarchical diffusion model for singing voice neural vocoders. Experimental results show that the proposed method outperforms state-of-the-art one-shot SVC baselines for both seen and unseen singers and significantly improves the robustness against distortions.

</details>

### [DisC-VC: Disentangled and F0-Controllable Neural Voice Conversion](2210.11059.md)
**Chihiro Watanabe, Hirokazu Kameoka** · 2022-10-20

<details>
<summary>Abstract</summary>

Voice conversion is a task to convert a non-linguistic feature of a given utterance. Since naturalness of speech strongly depends on its pitch pattern, in some applications, it would be desirable to keep the original rise/fall pitch pattern while changing the speaker identity. Some of the existing methods address this problem by either using a source-filter model or developing a neural network that takes an F0 pattern as input to the model. Although the latter approach can achieve relatively high sound quality compared to the former one, there is no consideration for discrepancy between the target and generated F0 patterns in its training process. In this paper, we propose a new variational-autoencoder-based voice conversion model accompanied by an auxiliary network, which ensures that the conversion result correctly reflects the specified F0/timbre information. We show the effectiveness of the proposed method by objective and subjective evaluations.

</details>

### [A Data-Driven Investigation of Noise-Adaptive Utterance Generation with Linguistic Modification](2210.10252.md)
**Anupama Chingacham, Vera Demberg, Dietrich Klakow** · 2022-10-19

<details>
<summary>Abstract</summary>

In noisy environments, speech can be hard to understand for humans. Spoken dialog systems can help to enhance the intelligibility of their output, either by modifying the speech synthesis (e.g., imitate Lombard speech) or by optimizing the language generation. We here focus on the second type of approach, by which an intended message is realized with words that are more intelligible in a specific noisy environment. By conducting a speech perception experiment, we created a dataset of 900 paraphrases in babble noise, perceived by native English speakers with normal hearing. We find that careful selection of paraphrases can improve intelligibility by 33% at SNR -5 dB. Our analysis of the data shows that the intelligibility differences between paraphrases are mainly driven by noise-robust acoustic cues. Furthermore, we propose an intelligibility-aware paraphrase ranking model, which outperforms baseline models with a relative improvement of 31.37% at SNR -5 dB.

</details>

### [Spoofed training data for speech spoofing countermeasure can be efficiently created using neural vocoders](2210.10570.md)
**Xin Wang, Junichi Yamagishi** · 2022-10-19

<details>
<summary>Abstract</summary>

A good training set for speech spoofing countermeasures requires diverse TTS and VC spoofing attacks, but generating TTS and VC spoofed trials for a target speaker may be technically demanding. Instead of using full-fledged TTS and VC systems, this study uses neural-network-based vocoders to do copy-synthesis on bona fide utterances. The output data can be used as spoofed data. To make better use of pairs of bona fide and spoofed data, this study introduces a contrastive feature loss that can be plugged into the standard training criterion. On the basis of the bona fide trials from the ASVspoof 2019 logical access training set, this study empirically compared a few training sets created in the proposed manner using a few neural non-autoregressive vocoders. Results on multiple test sets suggest good practices such as fine-tuning neural vocoders using bona fide data from the target domain. The results also demonstrated the effectiveness of the contrastive feature loss. Combining the best practices, the trained CM achieved overall competitive performance. Its EERs on the ASVspoof 2021 hidden subsets also outperformed the top-1 challenge submission.

</details>

### [Two-stage training method for Japanese electrolaryngeal speech enhancement based on sequence-to-sequence voice conversion](2210.10314.md)
**Ding Ma, Lester Phillip Violeta, Kazuhiro Kobayashi, Tomoki Toda** · 2022-10-19

<details>
<summary>Abstract</summary>

Sequence-to-sequence (seq2seq) voice conversion (VC) models have greater potential in converting electrolaryngeal (EL) speech to normal speech (EL2SP) compared to conventional VC models. However, EL2SP based on seq2seq VC requires a sufficiently large amount of parallel data for the model training and it suffers from significant performance degradation when the amount of training data is insufficient. To address this issue, we suggest a novel, two-stage strategy to optimize the performance on EL2SP based on seq2seq VC when a small amount of the parallel dataset is available. In contrast to utilizing high-quality data augmentations in previous studies, we first combine a large amount of imperfect synthetic parallel data of EL and normal speech, with the original dataset into VC training. Then, a second stage training is conducted with the original parallel dataset only. The results show that the proposed method progressively improves the performance of EL2SP based on seq2seq VC.

</details>

### [Improving robustness of spontaneous speech synthesis with linguistic speech regularization and pseudo-filled-pause insertion](2210.09815.md)
**Yuta Matsunaga, Takaaki Saeki, Shinnosuke Takamichi, Hiroshi Saruwatari** · 2022-10-18

<details>
<summary>Abstract</summary>

We present a training method with linguistic speech regularization that improves the robustness of spontaneous speech synthesis methods with filled pause (FP) insertion. Spontaneous speech synthesis is aimed at producing speech with human-like disfluencies, such as FPs. Because modeling the complex data distribution of spontaneous speech with a rich FP vocabulary is challenging, the quality of FP-inserted synthetic speech is often limited. To address this issue, we present a method for synthesizing spontaneous speech that improves robustness to diverse FP insertions. Regularization is used to stabilize the synthesis of the linguistic speech (i.e., non-FP) elements. To further improve robustness to diverse FP insertions, it utilizes pseudo-FPs sampled using an FP word prediction model as well as ground-truth FPs. Our experiments demonstrated that the proposed method improves the naturalness of synthetic speech with ground-truth and predicted FPs by 0.24 and 0.26, respectively.

</details>

### [Generating Synthetic Speech from SpokenVocab for Speech Translation](2210.08174.md)
**Jinming Zhao, Gholamreza Haffar, Ehsan Shareghi** · 2022-10-15

<details>
<summary>Abstract</summary>

Training end-to-end speech translation (ST) systems requires sufficiently large-scale data, which is unavailable for most language pairs and domains. One practical solution to the data scarcity issue is to convert machine translation data (MT) to ST data via text-to-speech (TTS) systems. Yet, using TTS systems can be tedious and slow, as the conversion needs to be done for each MT dataset. In this work, we propose a simple, scalable and effective data augmentation technique, i.e., SpokenVocab, to convert MT data to ST data on-the-fly. The idea is to retrieve and stitch audio snippets from a SpokenVocab bank according to words in an MT sequence. Our experiments on multiple language pairs from Must-C show that this method outperforms strong baselines by an average of 1.83 BLEU scores, and it performs equally well as TTS-generated speech. We also showcase how SpokenVocab can be applied in code-switching ST for which often no TTS systems exit. Our code is available at https://github.com/mingzi151/SpokenVocab

</details>

### [Empirical Study Incorporating Linguistic Knowledge on Filled Pauses for Personalized Spontaneous Speech Synthesis](2210.07559.md)
**Yuta Matsunaga, Takaaki Saeki, Shinnosuke Takamichi, Hiroshi Saruwatari** · 2022-10-14

<details>
<summary>Abstract</summary>

We present a comprehensive empirical study for personalized spontaneous speech synthesis on the basis of linguistic knowledge. With the advent of voice cloning for reading-style speech synthesis, a new voice cloning paradigm for human-like and spontaneous speech synthesis is required. We, therefore, focus on personalized spontaneous speech synthesis that can clone both the individual's voice timbre and speech disfluency. Specifically, we deal with filled pauses, a major source of speech disfluency, which is known to play an important role in speech generation and communication in psychology and linguistics. To comparatively evaluate personalized filled pause insertion and non-personalized filled pause prediction methods, we developed a speech synthesis method with a non-personalized external filled pause predictor trained with a multi-speaker corpus. The results clarify the position-word entanglement of filled pauses, i.e., the necessity of precisely predicting positions for naturalness and the necessity of precisely predicting words for individuality on the evaluation of synthesized speech.

</details>

### [Transformer-Based Speech Synthesizer Attribution in an Open Set Scenario](2210.07546.md)
**Emily R. Bartusiak, Edward J. Delp** · 2022-10-14

<details>
<summary>Abstract</summary>

Speech synthesis methods can create realistic-sounding speech, which may be used for fraud, spoofing, and misinformation campaigns. Forensic methods that detect synthesized speech are important for protection against such attacks. Forensic attribution methods provide even more information about the nature of synthesized speech signals because they identify the specific speech synthesis method (i.e., speech synthesizer) used to create a speech signal. Due to the increasing number of realistic-sounding speech synthesizers, we propose a speech attribution method that generalizes to new synthesizers not seen during training. To do so, we investigate speech synthesizer attribution in both a closed set scenario and an open set scenario. In other words, we consider some speech synthesizers to be "known" synthesizers (i.e., part of the closed set) and others to be "unknown" synthesizers (i.e., part of the open set). We represent speech signals as spectrograms and train our proposed method, known as compact attribution transformer (CAT), on the closed set for multi-class classification. Then, we extend our analysis to the open set to attribute synthesized speech signals to both known and unknown synthesizers. We utilize a t-distributed stochastic neighbor embedding (tSNE) on the latent space of the trained CAT to differentiate between each unknown synthesizer. Additionally, we explore poly-1 loss formulations to improve attribution results. Our proposed approach successfully attributes synthesized speech signals to their respective speech synthesizers in both closed and open set scenarios.

</details>

### [Hierarchical Diffusion Models for Singing Voice Neural Vocoder](2210.07508.md)
**Naoya Takahashi, Mayank Kumar, Singh, Yuki Mitsufuji** · 2022-10-14

<details>
<summary>Abstract</summary>

Recent progress in deep generative models has improved the quality of neural vocoders in speech domain. However, generating a high-quality singing voice remains challenging due to a wider variety of musical expressions in pitch, loudness, and pronunciations. In this work, we propose a hierarchical diffusion model for singing voice neural vocoders. The proposed method consists of multiple diffusion models operating in different sampling rates; the model at the lowest sampling rate focuses on generating accurate low-frequency components such as pitch, and other models progressively generate the waveform at higher sampling rates on the basis of the data at the lower sampling rate and acoustic features. Experimental results show that the proposed method produces high-quality singing voices for multiple singers, outperforming state-of-the-art neural vocoders with a similar range of computational costs.

</details>

### [Enriching Style Transfer in multi-scale control based personalized end-to-end speech synthesis](s2:bf4a3238b0e41eea7a6a0e86a25bf87262c61270.md)
**Zhongcai Lyu, Jie Zhu** · 2022-10-14

<details>
<summary>Abstract</summary>

Personalized speech synthesis aims to transfer speech style with a few speech samples from the target speaker. However, pretrain and fine-tuning techniques are required to overcome the problem of poor performance for similarity and prosody in a data-limited condition. In this paper, a zero-shot style transfer framework based on multi-scale control is presented to handle the above problems. Firstly, speaker embedding is extracted from a single reference speech audio by a specially designed reference encoder, with which Speaker-Adaptive Linear Modulation (SALM) could generate the scale and bias vector to influence the encoder output, and consequently greatly enhance the adaptability to unseen speakers. Secondly, we propose a prosody module that includes a prosody extractor and prosody predictor, which can efficiently predict the prosody of the generated speech from the reference audio and text information and achieve phoneme-level prosody control, thus increasing the diversity of the synthesized speech. Using both objective and subjective metrics for evaluation, the experiments demonstrate that our model is capable of synthesizing speech of high naturalness and similarity of speech, with only a few or even a single piece of data from the target speaker.

</details>

### [Anonymizing Speech with Generative Adversarial Networks to Preserve Speaker Privacy](2210.07002.md)
**Sarina Meyer, Pascal Tilli, Pavel Denisov, Florian Lux et al.** · 2022-10-13

<details>
<summary>Abstract</summary>

In order to protect the privacy of speech data, speaker anonymization aims for hiding the identity of a speaker by changing the voice in speech recordings. This typically comes with a privacy-utility trade-off between protection of individuals and usability of the data for downstream applications. One of the challenges in this context is to create non-existent voices that sound as natural as possible. In this work, we propose to tackle this issue by generating speaker embeddings using a generative adversarial network with Wasserstein distance as cost function. By incorporating these artificial embeddings into a speech-to-text-to-speech pipeline, we outperform previous approaches in terms of privacy and utility. According to standard objective metrics and human evaluation, our approach generates intelligible and content-preserving yet privacy-protecting versions of the original recordings.

</details>

### [Pre-Avatar: An Automatic Presentation Generation Framework Leveraging Talking Avatar](2210.06877.md)
**Aolan Sun, Xulong Zhang, Tiandong Ling, Jianzong Wang et al.** · 2022-10-13

<details>
<summary>Abstract</summary>

Since the beginning of the COVID-19 pandemic, remote conferencing and school-teaching have become important tools. The previous applications aim to save the commuting cost with real-time interactions. However, our application is going to lower the production and reproduction costs when preparing the communication materials. This paper proposes a system called Pre-Avatar, generating a presentation video with a talking face of a target speaker with 1 front-face photo and a 3-minute voice recording. Technically, the system consists of three main modules, user experience interface (UEI), talking face module and few-shot text-to-speech (TTS) module. The system firstly clones the target speaker's voice, and then generates the speech, and finally generate an avatar with appropriate lip and head movements. Under any scenario, users only need to replace slides with different notes to generate another new video. The demo has been released here and will be published as free software for use.

</details>

### [On the Utility of Self-supervised Models for Prosody-related Tasks](2210.07185.md)
**Guan-Ting Lin, Chi-Luen Feng, Wei-Ping Huang, Yuan Tseng et al.** · 2022-10-13

<details>
<summary>Abstract</summary>

Self-Supervised Learning (SSL) from speech data has produced models that have achieved remarkable performance in many tasks, and that are known to implicitly represent many aspects of information latently present in speech signals. However, relatively little is known about the suitability of such models for prosody-related tasks or the extent to which they encode prosodic information. We present a new evaluation framework, SUPERB-prosody, consisting of three prosody-related downstream tasks and two pseudo tasks. We find that 13 of the 15 SSL models outperformed the baseline on all the prosody-related tasks. We also show good performance on two pseudo tasks: prosody reconstruction and future prosody prediction. We further analyze the layerwise contributions of the SSL models. Overall we conclude that SSL speech models are highly effective for prosody-related tasks.

</details>

### [Can we use Common Voice to train a Multi-Speaker TTS system?](2210.06370.md)
**Sewade Ogun et.al.** · 2022-10-12

### [SQuId: Measuring Speech Naturalness in Many Languages](2210.06324.md)
**Thibault Sellam, Ankur Bapna, Joshua Camp, Diana Mackinnon et al.** · 2022-10-12

<details>
<summary>Abstract</summary>

Much of text-to-speech research relies on human evaluation, which incurs heavy costs and slows down the development process. The problem is particularly acute in heavily multilingual applications, where recruiting and polling judges can take weeks. We introduce SQuId (Speech Quality Identification), a multilingual naturalness prediction model trained on over a million ratings and tested in 65 locales-the largest effort of this type to date. The main insight is that training one model on many locales consistently outperforms mono-locale baselines. We present our task, the model, and show that it outperforms a competitive baseline based on w2v-BERT and VoiceMOS by 50.0%. We then demonstrate the effectiveness of cross-locale transfer during fine-tuning and highlight its effect on zero-shot locales, i.e., locales for which there is no fine-tuning data. Through a series of analyses, we highlight the role of non-linguistic effects such as sound artifacts in cross-locale transfer. Finally, we present the effect of our design decision, e.g., model size, pre-training diversity, and language rebalancing with several ablation experiments.

</details>

### [UTTS: Unsupervised TTS with Conditional Disentangled Sequential Variational Auto-encoder](2206.02512.md)
**Jiachen Lian et.al.** · 2022-10-11

### [GAN You Hear Me? Reclaiming Unconditional Speech Synthesis from Diffusion Models](2210.05271.md)
**Matthew Baas, Herman Kamper** · 2022-10-11

<details>
<summary>Abstract</summary>

We propose AudioStyleGAN (ASGAN), a new generative adversarial network (GAN) for unconditional speech synthesis. As in the StyleGAN family of image synthesis models, ASGAN maps sampled noise to a disentangled latent vector which is then mapped to a sequence of audio features so that signal aliasing is suppressed at every layer. To successfully train ASGAN, we introduce a number of new techniques, including a modification to adaptive discriminator augmentation to probabilistically skip discriminator updates. ASGAN achieves state-of-the-art results in unconditional speech synthesis on the Google Speech Commands dataset. It is also substantially faster than the top-performing diffusion models. Through a design that encourages disentanglement, ASGAN is able to perform voice conversion and speech editing without being explicitly trained to do so. ASGAN demonstrates that GANs are still highly competitive with diffusion models. Code, models, samples: https://github.com/RF5/simple-asgan/.

</details>

### [An Overview of Affective Speech Synthesis and Conversion in the Deep Learning Era](2210.03538.md)
**Andreas Triantafyllopoulos et.al.** · 2022-10-06

### [Transfer Learning Framework for Low-Resource Text-to-Speech using a Large-Scale Unlabeled Speech Corpus](2203.15447.md)
**Minchan Kim et.al.** · 2022-10-06

### [The Sound of Silence: Efficiency of First Digit Features in Synthetic Audio Detection](2210.02746.md)
**Daniele Mari, Federica Latora, Simone Milani** · 2022-10-06

<details>
<summary>Abstract</summary>

The recent integration of generative neural strategies and audio processing techniques have fostered the widespread of synthetic speech synthesis or transformation algorithms. This capability proves to be harmful in many legal and informative processes (news, biometric authentication, audio evidence in courts, etc.). Thus, the development of efficient detection algorithms is both crucial and challenging due to the heterogeneity of forgery techniques. This work investigates the discriminative role of silenced parts in synthetic speech detection and shows how first digit statistics extracted from MFCC coefficients can efficiently enable a robust detection. The proposed procedure is computationally-lightweight and effective on many different algorithms since it does not rely on large neural detection architecture and obtains an accuracy above 90\% in most of the classes of the ASVSpoof dataset.

</details>

### [Fully Unsupervised Training of Few-shot Keyword Spotting](2210.02732.md)
**Dongjune Lee, Minchan Kim, Sung Hwan Mun, Min Hyun Han et al.** · 2022-10-06

<details>
<summary>Abstract</summary>

For training a few-shot keyword spotting (FS-KWS) model, a large labeled dataset containing massive target keywords has known to be essential to generalize to arbitrary target keywords with only a few enrollment samples. To alleviate the expensive data collection with labeling, in this paper, we propose a novel FS-KWS system trained only on synthetic data. The proposed system is based on metric learning enabling target keywords to be detected using distance metrics. Exploiting the speech synthesis model that generates speech with pseudo phonemes instead of texts, we easily obtain a large collection of multi-view samples with the same semantics. These samples are sufficient for training, considering metric learning does not intrinsically necessitate labeled data. All of the components in our framework do not require any supervision, making our method unsupervised. Experimental results on real datasets show our proposed method is competitive even without any labeled and real datasets.

</details>

### [WaveFit: An Iterative and Non-autoregressive Neural Vocoder based on Fixed-Point Iteration](2210.01029.md)
**Yuma Koizumi, Kohei Yatabe, Heiga Zen, Michiel Bacchiani** · 2022-10-03

<details>
<summary>Abstract</summary>

Denoising diffusion probabilistic models (DDPMs) and generative adversarial networks (GANs) are popular generative models for neural vocoders. The DDPMs and GANs can be characterized by the iterative denoising framework and adversarial training, respectively. This study proposes a fast and high-quality neural vocoder called \textit{WaveFit}, which integrates the essence of GANs into a DDPM-like iterative framework based on fixed-point iteration. WaveFit iteratively denoises an input signal, and trains a deep neural network (DNN) for minimizing an adversarial loss calculated from intermediate outputs at all iterations. Subjective (side-by-side) listening tests showed no statistically significant differences in naturalness between human natural speech and those synthesized by WaveFit with five iterations. Furthermore, the inference speed of WaveFit was more than 240 times faster than WaveRNN. Audio demos are available at \url{google.github.io/df-conformer/wavefit/}.

</details>

### [Facial Landmark Predictions with Applications to Metaverse](2209.14698.md)
**Qiao Han, Jun Zhao, Kwok-Yan Lam** · 2022-09-29

<details>
<summary>Abstract</summary>

This research aims to make metaverse characters more realistic by adding lip animations learnt from videos in the wild. To achieve this, our approach is to extend Tacotron 2 text-to-speech synthesizer to generate lip movements together with mel spectrogram in one pass. The encoder and gate layer weights are pre-trained on LJ Speech 1.1 data set while the decoder is retrained on 93 clips of TED talk videos extracted from LRS 3 data set. Our novel decoder predicts displacement in 20 lip landmark positions across time, using labels automatically extracted by OpenFace 2.0 landmark predictor. Training converged in 7 hours using less than 5 minutes of video. We conducted ablation study for Pre/Post-Net and pre-trained encoder weights to demonstrate the effectiveness of transfer learning between audio and visual speech data.

</details>

### [Multi-Task Adversarial Training Algorithm for Multi-Speaker Neural Text-to-Speech](2209.12549.md)
**Yusuke Nakai et.al.** · 2022-09-26

### [ControlVC: Zero-Shot Voice Conversion with Time-Varying Controls on Pitch and Speed](2209.11866.md)
**Meiying Chen, Zhiyao Duan** · 2022-09-23

<details>
<summary>Abstract</summary>

Recent developments in neural speech synthesis and vocoding have sparked a renewed interest in voice conversion (VC). Beyond timbre transfer, achieving controllability on para-linguistic parameters such as pitch and Speed is critical in deploying VC systems in many application scenarios. Existing studies, however, either only provide utterance-level global control or lack interpretability on the controls. In this paper, we propose ControlVC, the first neural voice conversion system that achieves time-varying controls on pitch and speed. ControlVC uses pre-trained encoders to compute pitch and linguistic embeddings from the source utterance and speaker embeddings from the target utterance. These embeddings are then concatenated and converted to speech using a vocoder. It achieves speed control through TD-PSOLA pre-processing on the source utterance, and achieves pitch control by manipulating the pitch contour before feeding it to the pitch encoder. Systematic subjective and objective evaluations are conducted to assess the speech quality and controllability. Results show that, on non-parallel and zero-shot conversion tasks, ControlVC significantly outperforms two other self-constructed baselines on speech quality, and it can successfully achieve time-varying pitch and speed control.

</details>

### [EPIC TTS Models: Empirical Pruning Investigations Characterizing Text-To-Speech Models](2209.10890.md)
**Perry Lam et.al.** · 2022-09-22

### [MnTTS: An Open-Source Mongolian Text-to-Speech Synthesis Dataset and Accompanied Baseline](2209.10848.md)
**Yifan Hu et.al.** · 2022-09-22

### [Controllable Accented Text-to-Speech Synthesis](2209.10804.md)
**Rui Liu, Berrak Sisman, Guanglai Gao, Haizhou Li** · 2022-09-22

<details>
<summary>Abstract</summary>

Accented text-to-speech (TTS) synthesis seeks to generate speech with an accent (L2) as a variant of the standard version (L1). Accented TTS synthesis is challenging as L2 is different from L1 in both in terms of phonetic rendering and prosody pattern. Furthermore, there is no easy solution to the control of the accent intensity in an utterance. In this work, we propose a neural TTS architecture, that allows us to control the accent and its intensity during inference. This is achieved through three novel mechanisms, 1) an accent variance adaptor to model the complex accent variance with three prosody controlling factors, namely pitch, energy and duration; 2) an accent intensity modeling strategy to quantify the accent intensity; 3) a consistency constraint module to encourage the TTS system to render the expected accent intensity at a fine level. Experiments show that the proposed system attains superior performance to the baseline models in terms of accent rendering and intensity control. To our best knowledge, this is the first study of accented TTS synthesis with explicit intensity control.

</details>

### [A Multi-Stage Multi-Codebook VQ-VAE Approach to High-Performance Neural TTS](2209.10887.md)
**Haohan Guo, Fenglong Xie, Frank K. Soong, Xixin Wu et al.** · 2022-09-22

<details>
<summary>Abstract</summary>

We propose a Multi-Stage, Multi-Codebook (MSMC) approach to high-performance neural TTS synthesis. A vector-quantized, variational autoencoder (VQ-VAE) based feature analyzer is used to encode Mel spectrograms of speech training data by down-sampling progressively in multiple stages into MSMC Representations (MSMCRs) with different time resolutions, and quantizing them with multiple VQ codebooks, respectively. Multi-stage predictors are trained to map the input text sequence to MSMCRs progressively by minimizing a combined loss of the reconstruction Mean Square Error (MSE) and "triplet loss". In synthesis, the neural vocoder converts the predicted MSMCRs into final speech waveforms. The proposed approach is trained and tested with an English TTS database of 16 hours by a female speaker. The proposed TTS achieves an MOS score of 4.41, which outperforms the baseline with an MOS of 3.62. Compact versions of the proposed TTS with much less parameters can still preserve high MOS scores. Ablation studies show that both multiple stages and multiple codebooks are effective for achieving high TTS performance.

</details>

### [An Initial study on Birdsong Re-synthesis Using Neural Vocoders](2209.10479.md)
**Rhythm Bhatia, Tomi H. Kinnunen** · 2022-09-21

<details>
<summary>Abstract</summary>

Modern speech synthesis uses neural vocoders to model raw waveform samples directly. This increased versatility has expanded the scope of vocoders from speech to other domains, such as music. We address another interesting domain of bio-acoustics. We provide initial comparative analysis-resynthesis experiments of birdsong using traditional (WORLD) and two neural (WaveNet autoencoder, parallel WaveGAN) vocoders. Our subjective results indicate no difference in the three vocoders in terms of species discrimination (ABX test). Nonetheless, the WORLD vocoder samples were rated higher in terms of retaining bird-like qualities (MOS test). All vocoders faced issues with pitch and voicing. Our results indicate some of the challenges in processing low-quality wildlife audio data.

</details>

### [Mandarin Singing Voice Synthesis with Denoising Diffusion Probabilistic Wasserstein GAN](2209.10446.md)
**Yin-Ping Cho, Yu Tsao, Hsin-Min Wang, Yi-Wen Liu** · 2022-09-21

<details>
<summary>Abstract</summary>

Singing voice synthesis (SVS) is the computer production of a human-like singing voice from given musical scores. To accomplish end-to-end SVS effectively and efficiently, this work adopts the acoustic model-neural vocoder architecture established for high-quality speech and singing voice synthesis. Specifically, this work aims to pursue a higher level of expressiveness in synthesized voices by combining the diffusion denoising probabilistic model (DDPM) and \emph{Wasserstein} generative adversarial network (WGAN) to construct the backbone of the acoustic model. On top of the proposed acoustic model, a HiFi-GAN neural vocoder is adopted with integrated fine-tuning to ensure optimal synthesis quality for the resulting end-to-end SVS system. This end-to-end system was evaluated with the multi-singer Mpop600 Mandarin singing voice dataset. In the experiments, the proposed system exhibits improvements over previous landmark counterparts in terms of musical expressiveness and high-frequency acoustic details. Moreover, the adversarial acoustic model converged stably without the need to enforce reconstruction objectives, indicating the convergence stability of the proposed DDPM and WGAN combined architecture over alternative GAN-based SVS systems.

</details>

### [Boosting Star-GANs for Voice Conversion with Contrastive Discriminator](2209.10088.md)
**Shijing Si, Jianzong Wang, Xulong Zhang, Xiaoyang Qu et al.** · 2022-09-21

<details>
<summary>Abstract</summary>

Nonparallel multi-domain voice conversion methods such as the StarGAN-VCs have been widely applied in many scenarios. However, the training of these models usually poses a challenge due to their complicated adversarial network architectures. To address this, in this work we leverage the state-of-the-art contrastive learning techniques and incorporate an efficient Siamese network structure into the StarGAN discriminator. Our method is called SimSiam-StarGAN-VC and it boosts the training stability and effectively prevents the discriminator overfitting issue in the training process. We conduct experiments on the Voice Conversion Challenge (VCC 2018) dataset, plus a user study to validate the performance of our framework. Our experimental results show that SimSiam-StarGAN-VC significantly outperforms existing StarGAN-VC methods in terms of both the objective and subjective metrics.

</details>

### [AutoLV: Automatic Lecture Video Generator](2209.08795.md)
**Wenbin Wang, Yang Song, Sanjay Jha** · 2022-09-19

<details>
<summary>Abstract</summary>

We propose an end-to-end lecture video generation system that can generate realistic and complete lecture videos directly from annotated slides, instructor's reference voice and instructor's reference portrait video. Our system is primarily composed of a speech synthesis module with few-shot speaker adaptation and an adversarial learning-based talking-head generation module. It is capable of not only reducing instructors' workload but also changing the language and accent which can help the students follow the lecture more easily and enable a wider dissemination of lecture contents. Our experimental results show that the proposed model outperforms other current approaches in terms of authenticity, naturalness and accuracy. Here is a video demonstration of how our system works, and the outcomes of the evaluation and comparison: https://youtu.be/cY6TYkI0cog.

</details>

### [Leveraging Prosody for Punctuation Prediction of Spontaneous Speech](s2:1bb965584a1e9ab0754c1e3a487ee6c7b636c734.md)
**Yeon-Sook Cho, Sara Ng, Trang Tran, Mari Ostendorf** · 2022-09-18

<details>
<summary>Abstract</summary>

This paper introduces a new neural model for punctuation prediction that incorporates prosodic features to improve automatic punctuation prediction in transcriptions of spontaneous speech. We explore the benefit of intonation and energy features over simply using pauses. In addition, the work poses the question of how to represent interruption points associated with disfluen-cies in spontaneous speech. In experiments on the Switchboard corpus, we find that prosodic information improved punctuation prediction fidelity for both hand transcripts and ASR output. Explicit modeling of interruption points can benefit prediction of standard punctuation, particularly if the convention associates interruptions with commas.

</details>

### [An Efficient and High Fidelity Vietnamese Streaming End-to-End Speech Synthesis](s2:be2ee91e2e9b746d4a3a1aa5707d071dc072fca7.md)
**Tho Tran, The Chuong Chu, V. Hoang, Trung Bui et al.** · 2022-09-18

<details>
<summary>Abstract</summary>

In recent years, parallel end-to-end speech synthesis systems have outperformed the 2-stage TTS approaches in audio quality and latency. A parallel end-to-end speech like VITS can generate the audio with high MOS comparable to ground truth and achieve low latency on GPU. However, the VITS still has high latency when synthesizing long utterances on CPUs. Therefore, in this paper, we propose a streaming method for the parallel speech synthesis model like VITS to synthesize with the long texts effectively on CPU. Our system has achieved human-like speech quality in both the non-streaming and streaming mode on the in-house Vietnamese evaluation set, while the synthesis speed of our system is approximately four times faster than that of the VITS in the non-streaming mode. Furthermore, the customer perceived latency of our system in streaming mode is 25 times faster than the VITS on computer CPU. Our sys-tem in non-streaming mode achieves a MOS of 4.43 compared to ground-truth with MOS 4.56; it also has high-quality speech with a MOS of 4.35 in streaming mode. Finally, we release a Vietnamese single accent dataset used in our experiments.

</details>

### [TIMIT-TTS: a Text-to-Speech Dataset for Multimodal Synthetic Media Detection](2209.08000.md)
**Davide Salvi et.al.** · 2022-09-16

### [Detecting Synthetic Speech Manipulation in Real Audio Recordings](2209.07498.md)
**Md Hafizur Rahman, Martin Graciarena, Diego Castan, Chris Cobo-Kroenke et al.** · 2022-09-15

<details>
<summary>Abstract</summary>

Recent advances in artificial speech and audio technologies have improved the abilities of deep-fake operators to falsify media and spread malicious misinformation. Anyone with limited coding skills can use freely available speech synthesis tools to create convincing simulations of influential speakers' voices with the malicious intent to distort the original message. With the latest technology, malicious operators do not have to generate an entire audio clip; instead, they can insert a partial manipulation or a segment of synthetic speech into a genuine audio recording to change the entire context and meaning of the original message. Detecting these insertions is especially challenging because partially manipulated audio can more easily avoid synthetic speech detectors than entirely fake messages can. This paper describes a potential partial synthetic speech detection system based on the x-ResNet architecture with a probabilistic linear discriminant analysis (PLDA) backend and interleaved aware score processing. Experimental results suggest that the PLDA backend results in a 25% average error reduction among partially synthesized datasets over a non-PLDA baseline.

</details>

### [Using Rater and System Metadata to Explain Variance in the VoiceMOS Challenge 2022 Dataset](2209.06358.md)
**Michael Chinen, Jan Skoglund, Chandan K A Reddy, Alessandro Ragano et al.** · 2022-09-14

<details>
<summary>Abstract</summary>

Non-reference speech quality models are important for a growing number of applications. The VoiceMOS 2022 challenge provided a dataset of synthetic voice conversion and text-to-speech samples with subjective labels. This study looks at the amount of variance that can be explained in subjective ratings of speech quality from metadata and the distribution imbalances of the dataset. Speech quality models were constructed using wav2vec 2.0 with additional metadata features that included rater groups and system identifiers and obtained competitive metrics including a Spearman rank correlation coefficient (SRCC) of 0.934 and MSE of 0.088 at the system-level, and 0.877 and 0.198 at the utterance-level. Using data and metadata that the test restricted or blinded further improved the metrics. A metadata analysis showed that the system-level metrics do not represent the model's system-level prediction as a result of the wide variation in the number of utterances used for each system on the validation and test datasets. We conclude that, in general, conditions should have enough utterances in the test set to bound the sample mean error, and be relatively balanced in utterance count between systems, otherwise the utterance-level metrics may be more reliable and interpretable.

</details>

### [Decoupled Pronunciation and Prosody Modeling in Meta-Learning-Based Multilingual Speech Synthesis](2209.06789.md)
**Yukun Peng, Zhenhua Ling** · 2022-09-14

<details>
<summary>Abstract</summary>

This paper presents a method of decoupled pronunciation and prosody modeling to improve the performance of meta-learning-based multilingual speech synthesis. The baseline meta-learning synthesis method adopts a single text encoder with a parameter generator conditioned on language embeddings and a single decoder to predict mel-spectrograms for all languages. In contrast, our proposed method designs a two-stream model structure that contains two encoders and two decoders for pronunciation and prosody modeling, respectively, considering that the pronunciation knowledge and the prosody knowledge should be shared in different ways among languages. In our experiments, our proposed method effectively improved the intelligibility and naturalness of multilingual speech synthesis comparing with the baseline meta-learning synthesis method.

</details>

### [Enhanced Direct Speech-to-Speech Translation Using Self-supervised Pre-training and Data Augmentation](2204.02967.md)
**Sravya Popuri et.al.** · 2022-09-13

### [Deep Speech Synthesis from Articulatory Representations](2209.06337.md)
**Peter Wu, Shinji Watanabe, Louis Goldstein, Alan W Black et al.** · 2022-09-13

<details>
<summary>Abstract</summary>

In the articulatory synthesis task, speech is synthesized from input features containing information about the physical behavior of the human vocal tract. This task provides a promising direction for speech synthesis research, as the articulatory space is compact, smooth, and interpretable. Current works have highlighted the potential for deep learning models to perform articulatory synthesis. However, it remains unclear whether these models can achieve the efficiency and fidelity of the human speech production system. To help bridge this gap, we propose a time-domain articulatory synthesis methodology and demonstrate its efficacy with both electromagnetic articulography (EMA) and synthetic articulatory feature inputs. Our model is computationally efficient and achieves a transcription word error rate (WER) of 18.5% for the EMA-to-speech task, yielding an improvement of 11.6% compared to prior work. Through interpolation experiments, we also highlight the generalizability and interpretability of our approach.

</details>

### [Automated detection of pronunciation errors in non-native English speech employing deep learning](2209.06265.md)
**Daniel Korzekwa** · 2022-09-13

<details>
<summary>Abstract</summary>

Despite significant advances in recent years, the existing Computer-Assisted Pronunciation Training (CAPT) methods detect pronunciation errors with a relatively low accuracy (precision of 60% at 40%-80% recall). This Ph.D. work proposes novel deep learning methods for detecting pronunciation errors in non-native (L2) English speech, outperforming the state-of-the-art method in AUC metric (Area under the Curve) by 41%, i.e., from 0.528 to 0.749. One of the problems with existing CAPT methods is the low availability of annotated mispronounced speech needed for reliable training of pronunciation error detection models. Therefore, the detection of pronunciation errors is reformulated to the task of generating synthetic mispronounced speech. Intuitively, if we could mimic mispronounced speech and produce any amount of training data, detecting pronunciation errors would be more effective. Furthermore, to eliminate the need to align canonical and recognized phonemes, a novel end-to-end multi-task technique to directly detect pronunciation errors was proposed. The pronunciation error detection models have been used at Amazon to automatically detect pronunciation errors in synthetic speech to accelerate the research into new speech synthesis methods. It was demonstrated that the proposed deep learning methods are applicable in the tasks of detecting and reconstructing dysarthric speech.

</details>

### [SANIP: Shopping Assistant and Navigation for the visually impaired](2209.03570.md)
**Shubham Deshmukh, Favin Fernandes, Amey Chavan, Monali Ahire et al.** · 2022-09-08

<details>
<summary>Abstract</summary>

The proposed shopping assistant model SANIP is going to help blind persons to detect hand held objects and also to get a video feedback of the information retrieved from the detected and recognized objects. The proposed model consists of three python models i.e. Custom Object Detection, Text Detection and Barcode detection. For object detection of the hand held object, we have created our own custom dataset that comprises daily goods such as Parle-G, Tide, and Lays. Other than that we have also collected images of Cart and Exit signs as it is essential for any person to use a cart and also notice the exit sign in case of emergency. For the other 2 models proposed the text and barcode information retrieved is converted from text to speech and relayed to the Blind person. The model was used to detect objects that were trained on and was successful in detecting and recognizing the desired output with a good accuracy and precision.

</details>

### [Non-Standard Vietnamese Word Detection and Normalization for Text-to-Speech](2209.02971.md)
**Huu-Tien Dang, Thi-Hai-Yen Vuong, Xuan-Hieu Phan** · 2022-09-07

<details>
<summary>Abstract</summary>

Converting written texts into their spoken forms is an essential problem in any text-to-speech (TTS) systems. However, building an effective text normalization solution for a real-world TTS system face two main challenges: (1) the semantic ambiguity of non-standard words (NSWs), e.g., numbers, dates, ranges, scores, abbreviations, and (2) transforming NSWs into pronounceable syllables, such as URL, email address, hashtag, and contact name. In this paper, we propose a new two-phase normalization approach to deal with these challenges. First, a model-based tagger is designed to detect NSWs. Then, depending on NSW types, a rule-based normalizer expands those NSWs into their final verbal forms. We conducted three empirical experiments for NSW detection using Conditional Random Fields (CRFs), BiLSTM-CNN-CRF, and BERT-BiGRU-CRF models on a manually annotated dataset including 5819 sentences extracted from Vietnamese news articles. In the second phase, we propose a forward lexicon-based maximum matching algorithm to split down the hashtag, email, URL, and contact name. The experimental results of the tagging phase show that the average F1 scores of the BiLSTM-CNN-CRF and CRF models are above 90.00%, reaching the highest F1 of 95.00% with the BERT-BiGRU-CRF model. Overall, our approach has low sentence error rates, at 8.15% with CRF and 7.11% with BiLSTM-CNN-CRF taggers, and only 6.67% with BERT-BiGRU-CRF tagger.

</details>

### [Investigation into Target Speaking Rate Adaptation for Voice Conversion](2209.01978.md)
**Michael Kuhlmann, Fritz Seebauer, Janek Ebbers, Petra Wagner et al.** · 2022-09-05

<details>
<summary>Abstract</summary>

Disentangling speaker and content attributes of a speech signal into separate latent representations followed by decoding the content with an exchanged speaker representation is a popular approach for voice conversion, which can be trained with non-parallel and unlabeled speech data. However, previous approaches perform disentanglement only implicitly via some sort of information bottleneck or normalization, where it is usually hard to find a good trade-off between voice conversion and content reconstruction. Further, previous works usually do not consider an adaptation of the speaking rate to the target speaker or they put some major restrictions to the data or use case. Therefore, the contribution of this work is two-fold. First, we employ an explicit and fully unsupervised disentanglement approach, which has previously only been used for representation learning, and show that it allows to obtain both superior voice conversion and content reconstruction. Second, we investigate simple and generic approaches to linearly adapt the length of a speech signal, and hence the speaking rate, to a target speaker and show that the proposed adaptation allows to increase the speaking rate similarity with respect to the target speaker.

</details>

### [Improving Contextual Recognition of Rare Words with an Alternate Spelling Prediction Model](2209.01250.md)
**Jennifer Drexler Fox, Natalie Delworth** · 2022-09-02

<details>
<summary>Abstract</summary>

Contextual ASR, which takes a list of bias terms as input along with audio, has drawn recent interest as ASR use becomes more widespread. We are releasing contextual biasing lists to accompany the Earnings21 dataset, creating a public benchmark for this task. We present baseline results on this benchmark using a pretrained end-to-end ASR model from the WeNet toolkit. We show results for shallow fusion contextual biasing applied to two different decoding algorithms. Our baseline results confirm observations that end-to-end models struggle in particular with words that are rarely or never seen during training, and that existing shallow fusion techniques do not adequately address this problem. We propose an alternate spelling prediction model that improves recall of rare words by 34.7% relative and of out-of-vocabulary words by 97.2% relative, compared to contextual biasing without alternate spellings. This model is conceptually similar to ones used in prior work, but is simpler to implement as it does not rely on either a pronunciation dictionary or an existing text-to-speech system.

</details>

### [Lip-to-Speech Synthesis for Arbitrary Speakers in the Wild](2209.00642.md)
**Sindhu B Hegde, K R Prajwal, Rudrabha Mukhopadhyay, Vinay P Namboodiri et al.** · 2022-09-01

<details>
<summary>Abstract</summary>

In this work, we address the problem of generating speech from silent lip videos for any speaker in the wild. In stark contrast to previous works, our method (i) is not restricted to a fixed number of speakers, (ii) does not explicitly impose constraints on the domain or the vocabulary and (iii) deals with videos that are recorded in the wild as opposed to within laboratory settings. The task presents a host of challenges, with the key one being that many features of the desired target speech, like voice, pitch and linguistic content, cannot be entirely inferred from the silent face video. In order to handle these stochastic variations, we propose a new VAE-GAN architecture that learns to associate the lip and speech sequences amidst the variations. With the help of multiple powerful discriminators that guide the training process, our generator learns to synthesize speech sequences in any voice for the lip movements of any person. Extensive experiments on multiple datasets show that we outperform all baselines by a large margin. Further, our network can be fine-tuned on videos of specific identities to achieve a performance comparable to single-speaker models that are trained on $4\times$ more data. We conduct numerous ablation studies to analyze the effect of different modules of our architecture. We also provide a demo video that demonstrates several qualitative results along with the code and trained models on our website: \url{http://cvit.iiit.ac.in/research/projects/cvit-projects/lip-to-speech-synthesis}}

</details>

### [Karaoker: Alignment-free singing voice synthesis with speech training data](2204.04127.md)
**Panos Kakoulidis et.al.** · 2022-08-31

### [Training Text-To-Speech Systems From Synthetic Data: A Practical Approach For Accent Transfer Tasks](2208.13183.md)
**Lev Finkelstein et.al.** · 2022-08-28

### [Mel Spectrogram Inversion with Stable Pitch](2208.12782.md)
**Bruno Di Giorgi, Mark Levy, Richard Sharp** · 2022-08-26

<details>
<summary>Abstract</summary>

Vocoders are models capable of transforming a low-dimensional spectral representation of an audio signal, typically the mel spectrogram, to a waveform. Modern speech generation pipelines use a vocoder as their final component. Recent vocoder models developed for speech achieve a high degree of realism, such that it is natural to wonder how they would perform on music signals. Compared to speech, the heterogeneity and structure of the musical sound texture offers new challenges. In this work we focus on one specific artifact that some vocoder models designed for speech tend to exhibit when applied to music: the perceived instability of pitch when synthesizing sustained notes. We argue that the characteristic sound of this artifact is due to the lack of horizontal phase coherence, which is often the result of using a time-domain target space with a model that is invariant to time-shifts, such as a convolutional neural network. We propose a new vocoder model that is specifically designed for music. Key to improving the pitch stability is the choice of a shift-invariant target space that consists of the magnitude spectrum and the phase gradient. We discuss the reasons that inspired us to re-formulate the vocoder task, outline a working example, and evaluate it on musical signals. Our method results in 60% and 10% improved reconstruction of sustained notes and chords with respect to existing models, using a novel harmonic error metric.

</details>

### [End-to-End Kurdish Speech Synthesis Based on Transfer Learning](s2:fb3fe3bdded908cff0d3dd63f4311fffd7381fb7.md)
**Sabat S. Muhamad, H. Veisi** · 2022-08-26

<details>
<summary>Abstract</summary>

A text-to-speech (TTS) system converts the texts into speech in a specific language. Several TTS systems generate natural-like speech signals in numerous languages, such as English. On the other hand, the Kurdish language has just been examined. Existing preliminary research on Kurdish speech synthesis has utilized old methods and has generated low-quality speech. They also lack important aspects of speech, including intonation, emphasis, and rhythm. Some approaches were presented to address these challenges, including the use of concatenative systems. For example, the unit selection or statistical parametric methods. On the other hand, they need a great deal of time, effort, and domain knowledge. An additional factor for Kurdish speech synthesizers' low performance is the absence of publicly available speech corpora, unlike English, which has many freely-available corpora and audiobooks. The motivation of this paper is to create a Central Kurdish speech corpus and generate a human-like speech from the Kurdish text. This paper explains how to utilize Tacotron 2, an end-to-end neural network architecture and HiFi-GAN vocoder, to produce a high-quality, realistic, and human-like Kurdish voice. This work utilizes "text, audio" pairings, which contain 10 hours of recorded audio samples and texts collected from the Internet and textbooks. It shows how to use English character embedding as the pre-trained knowledge with Kurdish characters as input and how to preprocess these audio examples to get a great outcome. Our evaluations for various types of texts show a mean opinion score of 4.1, comparable with state-of-the-art synthesizers in other languages.

</details>

### [SOMOS: The Samsung Open MOS Dataset for the Evaluation of Neural Text-to-Speech Synthesis](2204.03040.md)
**Georgia Maniati et.al.** · 2022-08-24

### [Visualising Model Training via Vowel Space for Text-To-Speech Systems](2208.09775.md)
**Binu Abeysinghe et.al.** · 2022-08-21

### [Towards MOOCs for Lipreading: Using Synthetic Talking Heads to Train Humans in Lipreading at Scale](2208.09796.md)
**Aditya Agarwal, Bipasha Sen, Rudrabha Mukhopadhyay, Vinay Namboodiri et al.** · 2022-08-21

<details>
<summary>Abstract</summary>

Many people with some form of hearing loss consider lipreading as their primary mode of day-to-day communication. However, finding resources to learn or improve one's lipreading skills can be challenging. This is further exacerbated in the COVID19 pandemic due to restrictions on direct interactions with peers and speech therapists. Today, online MOOCs platforms like Coursera and Udemy have become the most effective form of training for many types of skill development. However, online lipreading resources are scarce as creating such resources is an extensive process needing months of manual effort to record hired actors. Because of the manual pipeline, such platforms are also limited in vocabulary, supported languages, accents, and speakers and have a high usage cost. In this work, we investigate the possibility of replacing real human talking videos with synthetically generated videos. Synthetic data can easily incorporate larger vocabularies, variations in accent, and even local languages and many speakers. We propose an end-to-end automated pipeline to develop such a platform using state-of-the-art talking head video generator networks, text-to-speech models, and computer vision techniques. We then perform an extensive human evaluation using carefully thought out lipreading exercises to validate the quality of our designed platform against the existing lipreading platforms. Our studies concretely point toward the potential of our approach in developing a large-scale lipreading MOOC platform that can impact millions of people with hearing loss.

</details>

### [Audio Deepfake Attribution: An Initial Dataset and Investigation](2208.10489.md)
**Xinrui Yan, Jiangyan Yi, Jianhua Tao, Jie Chen** · 2022-08-21

<details>
<summary>Abstract</summary>

The rapid progress of deep speech synthesis models has posed significant threats to society such as malicious manipulation of content. This has led to an increase in studies aimed at detecting so-called deepfake audio. However, existing works focus on the binary detection of real audio and fake audio. In real-world scenarios such as model copyright protection and digital evidence forensics, binary classification alone is insufficient. It is essential to identify the source of deepfake audio. Therefore, audio deepfake attribution has emerged as a new challenge. To this end, we designed the first deepfake audio dataset for the attribution of audio generation tools, called Audio Deepfake Attribution (ADA), and conducted a comprehensive investigation on system fingerprints. To address the challenges of attribution of continuously emerging unknown audio generation tools in the real world, we propose the Class-Representation Multi-Center Learning (CRML) method for open-set audio deepfake attribution (OSADA). CRML enhances the global directional variation of representations, ensuring the learning of discriminative representations with strong intra-class similarity and inter-class discrepancy among known classes. Finally, the strong class discrimination capability learned from known classes is extended to both known and unknown classes. Experimental results demonstrate that the CRML method effectively addresses open-set risks in real-world scenarios. The dataset is publicly available at: https://zenodo.org/records/13318702, and https://zenodo.org/records/13340666.

</details>

### [A Comparative Study on End-to-End Speech Synthetic Units for Amdo-Tibetan Dialect](s2:7e25eeb9d50371b17af8d6e5526d0b1bafe0b99b.md)
**Qian Li, Zhengjia Dan, Yue Zhao, Xin Huang et al.** · 2022-08-19

<details>
<summary>Abstract</summary>

This paper focuses on the speech synthesis modeling for Amdo-Tibetan dialect. We analyze the linguistic and phonetic characteristics of Amdo-Tibetan and present to use Latin letters as the synthetic unit for building the end-to-end speech synthesis model. The comparative experiments are designed and carried out to evaluate three type of synthetic unit – Latin letters, Tibetan initials and finals, and Tibetan syllables. The experimental results show that the model using the Latin letters transcribed from Tibetan characters by Wiley transliteration has better performance than the ones using the other two synthetic units. Also, this paper compares the different acoustic features and different vocoders for Amdo-Tibetan speech synthesis. The experimental results show that the speech synthesized using mel-spectrogram as acoustic feature and WaveNet as vocoder has the better clarity and naturalness.

</details>

### [Speech Representation Disentanglement with Adversarial Mutual Information Learning for One-shot Voice Conversion](2208.08757.md)
**SiCheng Yang, Methawee Tantrawenith, Haolin Zhuang, Zhiyong Wu et al.** · 2022-08-18

<details>
<summary>Abstract</summary>

One-shot voice conversion (VC) with only a single target speaker's speech for reference has become a hot research topic. Existing works generally disentangle timbre, while information about pitch, rhythm and content is still mixed together. To perform one-shot VC effectively with further disentangling these speech components, we employ random resampling for pitch and content encoder and use the variational contrastive log-ratio upper bound of mutual information and gradient reversal layer based adversarial mutual information learning to ensure the different parts of the latent space containing only the desired disentangled representation during training. Experiments on the VCTK dataset show the model achieves state-of-the-art performance for one-shot VC in terms of naturalness and intellgibility. In addition, we can transfer characteristics of one-shot VC on timbre, pitch and rhythm separately by speech representation disentanglement. Our code, pre-trained models and demo are available at https://im1eon.github.io/IS2022-SRDVC/.

</details>

### [Hierarchical and Multi-Scale Variational Autoencoder for Diverse and Natural Non-Autoregressive Text-to-Speech](2204.04004.md)
**Jae-Sung Bae et.al.** · 2022-08-15

### [Towards Parametric Speech Synthesis Using Gaussian-Markov Model of Spectral Envelope and Wavelet-Based Decomposition of F0](2208.07122.md)
**Mohammed Salah Al-Radhi, Tamás Gábor Csapó, Csaba Zainkó, Géza Németh** · 2022-08-15

<details>
<summary>Abstract</summary>

Neural network-based Text-to-Speech has significantly improved the quality of synthesized speech. Prominent methods (e.g., Tacotron2, FastSpeech, FastPitch) usually generate Mel-spectrogram from text and then synthesize speech using vocoder (e.g., WaveNet, WaveGlow, HiFiGAN). Compared with traditional parametric approaches (e.g., STRAIGHT and WORLD), neural vocoder based end-to-end models suffer from slow inference speed, and the synthesized speech is usually not robust and lack of controllability. In this work, we propose a novel updated vocoder, which is a simple signal model to train and easy to generate waveforms. We use the Gaussian-Markov model toward robust learning of spectral envelope and wavelet-based statistical signal processing to characterize and decompose F0 features. It can retain the fine spectral envelope and achieve high controllability of natural speech. The experimental results demonstrate that our proposed vocoder achieves better naturalness of reconstructed speech than the conventional STRAIGHT vocoder, slightly better than WaveNet, and somewhat worse than the WaveRNN.

</details>

### [Differentiable WORLD Synthesizer-based Neural Vocoder With Application To End-To-End Audio Style Transfer](2208.07282.md)
**Shahan Nercessian** · 2022-08-15

<details>
<summary>Abstract</summary>

In this paper, we propose a differentiable WORLD synthesizer and demonstrate its use in end-to-end audio style transfer tasks such as (singing) voice conversion and the DDSP timbre transfer task. Accordingly, our baseline differentiable synthesizer has no model parameters, yet it yields adequate synthesis quality. We can extend the baseline synthesizer by appending lightweight black-box postnets which apply further processing to the baseline output in order to improve fidelity. An alternative differentiable approach considers extraction of the source excitation spectrum directly, which can improve naturalness albeit for a narrower class of style transfer applications. The acoustic feature parameterization used by our approaches has the added benefit that it naturally disentangles pitch and timbral information so that they can be modeled separately. Moreover, as there exists a robust means of estimating these acoustic features from monophonic audio sources, it allows for parameter loss terms to be added to an end-to-end objective function, which can help convergence and/or further stabilize (adversarial) training.

</details>

### [Speech Synthesis with Mixed Emotions](2208.05890.md)
**Kun Zhou, Berrak Sisman, Rajib Rana, B. W. Schuller et al.** · 2022-08-11

<details>
<summary>Abstract</summary>

Emotional speech synthesis aims to synthesize human voices with various emotional effects. The current studies are mostly focused on imitating an averaged style belonging to a specific emotion type. In this paper, we seek to generate speech with a mixture of emotions at run-time. We propose a novel formulation that measures the relative difference between the speech samples of different emotions. We then incorporate our formulation into a sequence-to-sequence emotional text-to-speech framework. During the training, the framework does not only explicitly characterize emotion styles, but also explores the ordinal nature of emotions by quantifying the differences with other emotions. At run-time, we control the model to produce the desired emotion mixture by manually defining an emotion attribute vector. The objective and subjective evaluations have validated the effectiveness of the proposed framework. To our best knowledge, this research is the first study on modelling, synthesizing, and evaluating mixed emotions in speech.

</details>

### [TGAVC: Improving Autoencoder Voice Conversion with Text-Guided and Adversarial Training](2208.04035.md)
**Huaizhen Tang, Xulong Zhang, Jianzong Wang, Ning Cheng et al.** · 2022-08-08

<details>
<summary>Abstract</summary>

Non-parallel many-to-many voice conversion remains an interesting but challenging speech processing task. Recently, AutoVC, a conditional autoencoder based method, achieved excellent conversion results by disentangling the speaker identity and the speech content using information-constraining bottlenecks. However, due to the pure autoencoder training method, it is difficult to evaluate the separation effect of content and speaker identity. In this paper, a novel voice conversion framework, named $\boldsymbol T$ext $\boldsymbol G$uided $\boldsymbol A$utoVC(TGAVC), is proposed to more effectively separate content and timbre from speech, where an expected content embedding produced based on the text transcriptions is designed to guide the extraction of voice content. In addition, the adversarial training is applied to eliminate the speaker identity information in the estimated content embedding extracted from speech. Under the guidance of the expected content embedding and the adversarial training, the content encoder is trained to extract speaker-independent content embedding from speech. Experiments on AIShell-3 dataset show that the proposed model outperforms AutoVC in terms of naturalness and similarity of converted speech.

</details>

### [A Study of Modeling Rising Intonation in Cantonese Neural Speech Synthesis](2208.02189.md)
**Qibing Bai et.al.** · 2022-08-03

### [Few-Shot Cross-Lingual TTS Using Transferable Phoneme Embedding](2206.15427.md)
**Wei-Ping Huang et.al.** · 2022-08-03

### [Low-data? No problem: low-resource, language-agnostic conversational text-to-speech via F0-conditioned data augmentation](2207.14607.md)
**Giulia Comini, Goeric Huybrechts, Manuel Sam Ribeiro, Adam Gabrys et al.** · 2022-07-29

<details>
<summary>Abstract</summary>

The availability of data in expressive styles across languages is limited, and recording sessions are costly and time consuming. To overcome these issues, we demonstrate how to build low-resource, neural text-to-speech (TTS) voices with only 1 hour of conversational speech, when no other conversational data are available in the same language. Assuming the availability of non-expressive speech data in that language, we propose a 3-step technology: 1) we train an F0-conditioned voice conversion (VC) model as data augmentation technique; 2) we train an F0 predictor to control the conversational flavour of the voice-converted synthetic data; 3) we train a TTS system that consumes the augmented data. We prove that our technology enables F0 controllability, is scalable across speakers and languages and is competitive in terms of naturalness over a state-of-the-art baseline model, another augmented method which does not make use of F0 information.

</details>

### [Transplantation of Conversational Speaking Style with Interjections in Sequence-to-Sequence Speech Synthesis](2207.12262.md)
**Raul Fernandez et.al.** · 2022-07-25

### [Prosody Prediction with Discriminative Representation Method](s2:76fdc6c68c74a93048b4511add0b00fc0c3075eb.md)
**Jipeng Zhang, Hankiz Yilahun, Xiaoqin Feng, Yunlin Chen et al.** · 2022-07-22

<details>
<summary>Abstract</summary>

Rhythm affects the naturalness and intelligibility of Text-To-Speech (TTS). However, rhythm prediction remains a great challenge, usually in two aspects: 1) the united annotation is a relatively difficult task, which depends on expert’s experience. 2) traditional methods based on conditional random field (CRF), which heavily rely on feature engineering, such as word segmentation, part of speech(pos) etc. For above problems, we propose a method to reduce the dependency for united annotation data and conduct the joint experiment which use one unified model on independent data. Meanwhile, we also propose an algorithm of Layer Look Up Table (LLUT): use an embedding layer to learn a discriminative representation for different level of prosody data without any feature engineering. By using this method, the classifier can share the parameters and predict for different prosody level separately, which reduces the number of trainable model parameters. In order to better represent the input text, we use the pre-training model, like BERT, to provide the semantic information. Our experiment shows that the method of LLUT, is better able to acquire the discriminative meaning of different prosody levels. And also, our algorithm is proved to be general for sequence annotation tasks thus we can do extra task, like polyphone-prosody prediction.

</details>

### [End-to-End Multi-speaker Speech Synthesis with Controllable Stress](s2:cd4b039aa0adb8cad5277d24852eaac5ce71f130.md)
**Ting Liang, Askar Hamdulla, Hao Yin, Yunlin Chen** · 2022-07-22

<details>
<summary>Abstract</summary>

In this paper, an end-to-end multi-speaker speech synthesis with controllable stress method is proposed to make the synthetic speech more prominent and expressive, so as to improve the naturalness of synthetic speech. Specifically, we first recorded a small parallel corpus of stress and neutral audio, and labeled the corpora based on three levels of stress: the enhancement of pitch, the stretch of duration, and both. Secondly, based on the multi-speaker acoustic model, the features of the speaker identity and stress are modeled respectively to realize the transfer of stress between different speakers. Finally, we use the LPCNet to convert the spectrum from the target speaker with controllable stress into audio. At the end of the experiment, confusion matrix and Mean Opinion Score (MOS) are used as our evaluation criteria. In addition, we train the basemodel with 100 speakers, so that for any target speaker with only half an hour neutral corpus, can be used to synthesize the stress audio, which greatly improves the efficiency of speech synthesis. Experimental results indicate that the proposed method does not reduce the quality and correctness of synthetic speech, and meanwhile improves the naturalness, expressiveness and similarity of speech synthesis by at least 5% from MOS result.

</details>

### [Mixed-Phoneme BERT: Improving BERT with Mixed Phoneme and Sup-Phoneme Representations for Text to Speech](2203.17190.md)
**Guangyan Zhang et.al.** · 2022-07-19

### [Controllable Data Generation by Deep Learning: A Review](2207.09542.md)
**Shiyu Wang, Yuanqi Du, Xiaojie Guo, Bo Pan et al.** · 2022-07-19

<details>
<summary>Abstract</summary>

Designing and generating new data under targeted properties has been attracting various critical applications such as molecule design, image editing and speech synthesis. Traditional hand-crafted approaches heavily rely on expertise experience and intensive human efforts, yet still suffer from the insufficiency of scientific knowledge and low throughput to support effective and efficient data generation. Recently, the advancement of deep learning has created the opportunity for expressive methods to learn the underlying representation and properties of data. Such capability provides new ways of determining the mutual relationship between the structural patterns and functional properties of the data and leveraging such relationships to generate structural data, given the desired properties. This article is a systematic review that explains this promising research area, commonly known as controllable deep data generation. First, the article raises the potential challenges and provides preliminaries. Then the article formally defines controllable deep data generation, proposes a taxonomy on various techniques and summarizes the evaluation metrics in this specific domain. After that, the article introduces exciting applications of controllable deep data generation, experimentally analyzes and compares existing works. Finally, this article highlights the promising future directions of controllable deep data generation and identifies five potential challenges.

</details>

### [ProDiff: Progressive Fast Diffusion Model For High-Quality Text-to-Speech](2207.06389.md)
**Rongjie Huang et.al.** · 2022-07-13

### [Controllable and Lossless Non-Autoregressive End-to-End Text-to-Speech](2207.06088.md)
**Zhengxi Liu et.al.** · 2022-07-13

### [Text-driven Emotional Style Control and Cross-speaker Style Transfer in Neural TTS](2207.06000.md)
**Yookyung Shin et.al.** · 2022-07-13

### [A Cyclical Approach to Synthetic and Natural Speech Mismatch Refinement of Neural Post-filter for Low-cost Text-to-speech System](2207.05913.md)
**Yi-Chiao Wu et.al.** · 2022-07-13

### [SATTS: Speaker Attractor Text to Speech, Learning to Speak by Learning to Separate](2207.06011.md)
**Nabarun Goswami, Tatsuya Harada** · 2022-07-13

<details>
<summary>Abstract</summary>

The mapping of text to speech (TTS) is non-deterministic, letters may be pronounced differently based on context, or phonemes can vary depending on various physiological and stylistic factors like gender, age, accent, emotions, etc. Neural speaker embeddings, trained to identify or verify speakers are typically used to represent and transfer such characteristics from reference speech to synthesized speech. Speech separation on the other hand is the challenging task of separating individual speakers from an overlapping mixed signal of various speakers. Speaker attractors are high-dimensional embedding vectors that pull the time-frequency bins of each speaker's speech towards themselves while repelling those belonging to other speakers. In this work, we explore the possibility of using these powerful speaker attractors for zero-shot speaker adaptation in multi-speaker TTS synthesis and propose speaker attractor text to speech (SATTS). Through various experiments, we show that SATTS can synthesize natural speech from text from an unseen target speaker's reference signal which might have less than ideal recording conditions, i.e. reverberations or mixed with other speakers.

</details>

### [Subband-based Generative Adversarial Network for Non-parallel Many-to-many Voice Conversion](2207.06057.md)
**Jian Ma, Zhedong Zheng, Hao Fei, Feng Zheng et al.** · 2022-07-13

<details>
<summary>Abstract</summary>

Voice conversion is to generate a new speech with the source content and a target voice style. In this paper, we focus on one general setting, i.e., non-parallel many-to-many voice conversion, which is close to the real-world scenario. As the name implies, non-parallel many-to-many voice conversion does not require the paired source and reference speeches and can be applied to arbitrary voice transfer. In recent years, Generative Adversarial Networks (GANs) and other techniques such as Conditional Variational Autoencoders (CVAEs) have made considerable progress in this field. However, due to the sophistication of voice conversion, the style similarity of the converted speech is still unsatisfactory. Inspired by the inherent structure of mel-spectrogram, we propose a new voice conversion framework, i.e., Subband-based Generative Adversarial Network for Voice Conversion (SGAN-VC). SGAN-VC converts each subband content of the source speech separately by explicitly utilizing the spatial characteristics between different subbands. SGAN-VC contains one style encoder, one content encoder, and one decoder. In particular, the style encoder network is designed to learn style codes for different subbands of the target speaker. The content encoder network can capture the content information on the source speech. Finally, the decoder generates particular subband content. In addition, we propose a pitch-shift module to fine-tune the pitch of the source speaker, making the converted tone more accurate and explainable. Extensive experiments demonstrate that the proposed approach achieves state-of-the-art performance on VCTK Corpus and AISHELL3 datasets both qualitatively and quantitatively, whether on seen or unseen data. Furthermore, the content intelligibility of SGAN-VC on unseen data even exceeds that of StarGANv2-VC with ASR network assistance.

</details>

### [Speaker consistency loss and step-wise optimization for semi-supervised joint training of TTS and ASR using unpaired text data](2207.04659.md)
**Naoki Makishima et.al.** · 2022-07-11

### [DelightfulTTS 2: End-to-End Speech Synthesis with Adversarial Vector-Quantized Auto-Encoders](2207.04646.md)
**Yanqing Liu et.al.** · 2022-07-11

### [WavThruVec: Latent speech representation as intermediate features for neural speech synthesis](2203.16930.md)
**Hubert Siuzdak et.al.** · 2022-07-11

### [LIP: Lightweight Intelligent Preprocessor for meaningful text-to-speech](2207.07118.md)
**Harshvardhan Anand, Nansi Begam, Richa Verma, Sourav Ghosh et al.** · 2022-07-11

<details>
<summary>Abstract</summary>

Existing Text-to-Speech (TTS) systems need to read messages from the email which may have Personal Identifiable Information (PII) to text messages that can have a streak of emojis and punctuation. 92% of the world's online population use emoji with more than 10 billion emojis sent everyday. Lack of preprocessor leads to messages being read as-is including punctuation and infographics like emoticons. This problem worsens if there is a continuous sequence of punctuation/emojis that are quite common in real-world communications like messaging, Social Networking Site (SNS) interactions, etc. In this work, we aim to introduce a lightweight intelligent preprocessor (LIP) that can enhance the readability of a message before being passed downstream to existing TTS systems. We propose multiple sub-modules including: expanding contraction, censoring swear words, and masking of PII, as part of our preprocessor to enhance the readability of text. With a memory footprint of only 3.55 MB and inference time of 4 ms for up to 50-character text, our solution is suitable for real-time deployment. This work being the first of its kind, we try to benchmark with an open independent survey, the result of which shows 76.5% preference towards LIP enabled TTS engine as compared to standard TTS.

</details>

### [A Comparative Study of Self-supervised Speech Representation Based Voice Conversion](2207.04356.md)
**Wen-Chin Huang, Shu-Wen Yang, Tomoki Hayashi, Tomoki Toda** · 2022-07-10

<details>
<summary>Abstract</summary>

We present a large-scale comparative study of self-supervised speech representation (S3R)-based voice conversion (VC). In the context of recognition-synthesis VC, S3Rs are attractive owing to their potential to replace expensive supervised representations such as phonetic posteriorgrams (PPGs), which are commonly adopted by state-of-the-art VC systems. Using S3PRL-VC, an open-source VC software we previously developed, we provide a series of in-depth objective and subjective analyses under three VC settings: intra-/cross-lingual any-to-one (A2O) and any-to-any (A2A) VC, using the voice conversion challenge 2020 (VCC2020) dataset. We investigated S3R-based VC in various aspects, including model type, multilinguality, and supervision. We also studied the effect of a post-discretization process with k-means clustering and showed how it improves in the A2A setting. Finally, the comparison with state-of-the-art VC systems demonstrates the competitiveness of S3R-based VC and also sheds light on the possible improving directions.

</details>

### [FastLTS: Non-Autoregressive End-to-End Unconstrained Lip-to-Speech Synthesis](2207.03800.md)
**Yongqi Wang, Zhou Zhao** · 2022-07-08

<details>
<summary>Abstract</summary>

Unconstrained lip-to-speech synthesis aims to generate corresponding speeches from silent videos of talking faces with no restriction on head poses or vocabulary. Current works mainly use sequence-to-sequence models to solve this problem, either in an autoregressive architecture or a flow-based non-autoregressive architecture. However, these models suffer from several drawbacks: 1) Instead of directly generating audios, they use a two-stage pipeline that first generates mel-spectrograms and then reconstructs audios from the spectrograms. This causes cumbersome deployment and degradation of speech quality due to error propagation; 2) The audio reconstruction algorithm used by these models limits the inference speed and audio quality, while neural vocoders are not available for these models since their output spectrograms are not accurate enough; 3) The autoregressive model suffers from high inference latency, while the flow-based model has high memory occupancy: neither of them is efficient enough in both time and memory usage. To tackle these problems, we propose FastLTS, a non-autoregressive end-to-end model which can directly synthesize high-quality speech audios from unconstrained talking videos with low latency, and has a relatively small model size. Besides, different from the widely used 3D-CNN visual frontend for lip movement encoding, we for the first time propose a transformer-based visual frontend for this task. Experiments show that our model achieves $19.76\times$ speedup for audio waveform generation compared with the current autoregressive model on input sequences of 3 seconds, and obtains superior audio quality.

</details>

### [End-to-End Binaural Speech Synthesis](2207.03697.md)
**Wen Chin Huang, Dejan Markovic, Alexander Richard, Israel Dejene Gebru et al.** · 2022-07-08

<details>
<summary>Abstract</summary>

In this work, we present an end-to-end binaural speech synthesis system that combines a low-bitrate audio codec with a powerful binaural decoder that is capable of accurate speech binauralization while faithfully reconstructing environmental factors like ambient noise or reverb. The network is a modified vector-quantized variational autoencoder, trained with several carefully designed objectives, including an adversarial loss. We evaluate the proposed system on an internal binaural dataset with objective metrics and a perceptual study. Results show that the proposed approach matches the ground truth data more closely than previous methods. In particular, we demonstrate the capability of the adversarial loss in capturing environment effects needed to create an authentic auditory scene.

</details>

### [BibleTTS: a large, high-fidelity, multilingual, and uniquely African speech corpus](2207.03546.md)
**Josh Meyer, David Ifeoluwa Adelani, Edresson Casanova, Alp Öktem et al.** · 2022-07-07

<details>
<summary>Abstract</summary>

BibleTTS is a large, high-quality, open speech dataset for ten languages spoken in Sub-Saharan Africa. The corpus contains up to 86 hours of aligned, studio quality 48kHz single speaker recordings per language, enabling the development of high-quality text-to-speech models. The ten languages represented are: Akuapem Twi, Asante Twi, Chichewa, Ewe, Hausa, Kikuyu, Lingala, Luganda, Luo, and Yoruba. This corpus is a derivative work of Bible recordings made and released by the Open.Bible project from Biblica. We have aligned, cleaned, and filtered the original recordings, and additionally hand-checked a subset of the alignments for each language. We present results for text-to-speech models with Coqui TTS. The data is released under a commercial-friendly CC-BY-SA license.

</details>

### [Glow-WaveGAN 2: High-quality Zero-shot Text-to-speech Synthesis and Any-to-any Voice Conversion](2207.01832.md)
**Yi Lei et.al.** · 2022-07-05

### [WeSinger 2: Fully Parallel Singing Voice Synthesis via Multi-Singer Conditional Adversarial Training](2207.01886.md)
**Zewang Zhang, Yibin Zheng, Xinhui Li, Li Lu** · 2022-07-05

<details>
<summary>Abstract</summary>

This paper aims to introduce a robust singing voice synthesis (SVS) system to produce very natural and realistic singing voices efficiently by leveraging the adversarial training strategy. On one hand, we designed simple but generic random area conditional discriminators to help supervise the acoustic model, which can effectively avoid the over-smoothed spectrogram prediction and improve the expressiveness of SVS. On the other hand, we subtly combined the spectrogram with the frame-level linearly-interpolated F0 sequence as the input for the neural vocoder, which is then optimized with the help of multiple adversarial conditional discriminators in the waveform domain and multi-scale distance functions in the frequency domain. The experimental results and ablation studies concluded that, compared with our previous auto-regressive work, our new system can produce high-quality singing voices efficiently by fine-tuning different singing datasets covering from several minutes to a few hours. A large number of synthesized songs with different timbres are available online https://zzw922cn.github.io/wesinger2 and we highly recommend readers to listen to them.

</details>

### [BERT, can HE predict contrastive focus? Predicting and controlling prominence in neural TTS using a language model](2207.01718.md)
**Brooke Stephenson et.al.** · 2022-07-04

### [Unify and Conquer: How Phonetic Feature Representation Affects Polyglot Text-To-Speech (TTS)](2207.01547.md)
**Ariadna Sanchez et.al.** · 2022-07-04

### [Mix and Match: An Empirical Study on Training Corpus Composition for Polyglot Text-To-Speech (TTS)](2207.01507.md)
**Ziyao Zhang et.al.** · 2022-07-04

### [Cross-speaker Emotion Transfer Based On Prosody Compensation for End-to-End Speech Synthesis](2207.01198.md)
**Tao Li, Xinsheng Wang, Qicong Xie, Zhichao Wang et al.** · 2022-07-04

<details>
<summary>Abstract</summary>

Cross-speaker emotion transfer speech synthesis aims to synthesize emotional speech for a target speaker by transferring the emotion from reference speech recorded by another (source) speaker. In this task, extracting speaker-independent emotion embedding from reference speech plays an important role. However, the emotional information conveyed by such emotion embedding tends to be weakened in the process to squeeze out the source speaker's timbre information. In response to this problem, a prosody compensation module (PCM) is proposed in this paper to compensate for the emotional information loss. Specifically, the PCM tries to obtain speaker-independent emotional information from the intermediate feature of a pre-trained ASR model. To this end, a prosody compensation encoder with global context (GC) blocks is introduced to obtain global emotional information from the ASR model's intermediate feature. Experiments demonstrate that the proposed PCM can effectively compensate the emotion embedding for the emotional information loss, and meanwhile maintain the timbre of the target speaker. Comparisons with state-of-the-art models show that our proposed method presents obvious superiority on the cross-speaker emotion transfer task.

</details>

### [GlowVC: Mel-spectrogram space disentangling model for language-independent text-free voice conversion](2207.01454.md)
**Magdalena Proszewska, Grzegorz Beringer, Daniel Sáez-Trigueros, Thomas Merritt et al.** · 2022-07-04

<details>
<summary>Abstract</summary>

In this paper, we propose GlowVC: a multilingual multi-speaker flow-based model for language-independent text-free voice conversion. We build on Glow-TTS, which provides an architecture that enables use of linguistic features during training without the necessity of using them for VC inference. We consider two versions of our model: GlowVC-conditional and GlowVC-explicit. GlowVC-conditional models the distribution of mel-spectrograms with speaker-conditioned flow and disentangles the mel-spectrogram space into content- and pitch-relevant dimensions, while GlowVC-explicit models the explicit distribution with unconditioned flow and disentangles said space into content-, pitch- and speaker-relevant dimensions. We evaluate our models in terms of intelligibility, speaker similarity and naturalness for intra- and cross-lingual conversion in seen and unseen languages. GlowVC models greatly outperform AutoVC baseline in terms of intelligibility, while achieving just as high speaker similarity in intra-lingual VC, and slightly worse in the cross-lingual setting. Moreover, we demonstrate that GlowVC-explicit surpasses both GlowVC-conditional and AutoVC in terms of naturalness.

</details>

### [Computer-assisted Pronunciation Training -- Speech synthesis is almost all you need](2207.00774.md)
**Daniel Korzekwa et.al.** · 2022-07-02

### [Learning Noise-independent Speech Representation for High-quality Voice Conversion for Noisy Target Speakers](2207.00756.md)
**Liumeng Xue, Shan Yang, Na Hu, Dan Su et al.** · 2022-07-02

<details>
<summary>Abstract</summary>

Building a voice conversion system for noisy target speakers, such as users providing noisy samples or Internet found data, is a challenging task since the use of contaminated speech in model training will apparently degrade the conversion performance. In this paper, we leverage the advances of our recently proposed Glow-WaveGAN and propose a noise-independent speech representation learning approach for high-quality voice conversion for noisy target speakers. Specifically, we learn a latent feature space where we ensure that the target distribution modeled by the conversion model is exactly from the modeled distribution of the waveform generator. With this premise, we further manage to make the latent feature to be noise-invariant. Specifically, we introduce a noise-controllable WaveGAN, which directly learns the noise-independent acoustic representation from waveform by the encoder and conducts noise control in the hidden space through a FiLM module in the decoder. As for the conversion model, importantly, we use a flow-based model to learn the distribution of noise-independent but speaker-related latent features from phoneme posteriorgrams. Experimental results demonstrate that the proposed model achieves high speech quality and speaker similarity in the voice conversion for noisy target speakers.

</details>

### [Language Model-Based Emotion Prediction Methods for Emotional Speech Synthesis Systems](2206.15067.md)
**Hyun-Wook Yoon et.al.** · 2022-07-01

### [JETS: Jointly Training FastSpeech2 and HiFi-GAN for End to End Text to Speech](2203.16852.md)
**Dan Lim et.al.** · 2022-07-01

### [Building African Voices](2207.00688.md)
**Perez Ogayo, Graham Neubig, Alan W Black** · 2022-07-01

<details>
<summary>Abstract</summary>

Modern speech synthesis techniques can produce natural-sounding speech given sufficient high-quality data and compute resources. However, such data is not readily available for many languages. This paper focuses on speech synthesis for low-resourced African languages, from corpus creation to sharing and deploying the Text-to-Speech (TTS) systems. We first create a set of general-purpose instructions on building speech synthesis systems with minimum technological resources and subject-matter expertise. Next, we create new datasets and curate datasets from "found" data (existing recordings) through a participatory approach while considering accessibility, quality, and breadth. We demonstrate that we can develop synthesizers that generate intelligible speech with 25 minutes of created speech, even when recorded in suboptimal environments. Finally, we release the speech data, code, and trained voices for 12 African languages to support researchers and developers.

</details>

### [A Polyphone BERT for Polyphone Disambiguation in Mandarin Chinese](2207.12089.md)
**Song Zhang, Ken Zheng, Xiaoxu Zhu, Baoxiang Li** · 2022-07-01

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion is an indispensable part of the Chinese Mandarin text-to-speech (TTS) system, and the core of G2P conversion is to solve the problem of polyphone disambiguation, which is to pick up the correct pronunciation for several candidates for a Chinese polyphonic character. In this paper, we propose a Chinese polyphone BERT model to predict the pronunciations of Chinese polyphonic characters. Firstly, we create 741 new Chinese monophonic characters from 354 source Chinese polyphonic characters by pronunciation. Then we get a Chinese polyphone BERT by extending a pre-trained Chinese BERT with 741 new Chinese monophonic characters and adding a corresponding embedding layer for new tokens, which is initialized by the embeddings of source Chinese polyphonic characters. In this way, we can turn the polyphone disambiguation task into a pre-training task of the Chinese polyphone BERT. Experimental results demonstrate the effectiveness of the proposed model, and the polyphone BERT model obtain 2% (from 92.1% to 94.1%) improvement of average accuracy compared with the BERT-based classifier model, which is the prior state-of-the-art in polyphone disambiguation.

</details>

### [R-MelNet: Reduced Mel-Spectral Modeling for Neural TTS](2206.15276.md)
**Kyle Kastner et.al.** · 2022-06-30

### [TTS-by-TTS 2: Data-selective augmentation for neural speech synthesis using ranking support vector machine with variational autoencoder](2206.14984.md)
**Eunwoo Song et.al.** · 2022-06-30

### [VQTTS: High-Fidelity Text-to-Speech Synthesis with Self-Supervised VQ Acoustic Feature](2204.00768.md)
**Chenpeng Du et.al.** · 2022-06-30

### [An Evaluation of Three-Stage Voice Conversion Framework for Noisy and Reverberant Conditions](2206.15155.md)
**Yeonjong Choi, Chao Xie, Tomoki Toda** · 2022-06-30

<details>
<summary>Abstract</summary>

This paper presents a new voice conversion (VC) framework capable of dealing with both additive noise and reverberation, and its performance evaluation. There have been studied some VC researches focusing on real-world circumstances where speech data are interfered with background noise and reverberation. To deal with more practical conditions where no clean target dataset is available, one possible approach is zero-shot VC, but its performance tends to degrade compared with VC using sufficient amount of target speech data. To leverage large amount of noisy-reverberant target speech data, we propose a three-stage VC framework based on denoising process using a pretrained denoising model, dereverberation process using a dereverberation model, and VC process using a nonparallel VC model based on a variational autoencoder. The experimental results show that 1) noise and reverberation additively cause significant VC performance degradation, 2) the proposed method alleviates the adverse effects caused by both noise and reverberation, and significantly outperforms the baseline directly trained on the noisy-reverberant speech data, and 3) the potential degradation introduced by the denoising and dereverberation still causes noticeable adverse effects on VC performance.

</details>

### [DRSpeech: Degradation-Robust Text-to-Speech Synthesis with Frame-Level and Utterance-Level Acoustic Representation Learning](2203.15683.md)
**Takaaki Saeki et.al.** · 2022-06-29

### [Improving Deliberation by Text-Only and Semi-Supervised Training](2206.14716.md)
**Ke Hu, Tara N. Sainath, Yanzhang He, Rohit Prabhavalkar et al.** · 2022-06-29

<details>
<summary>Abstract</summary>

Text-only and semi-supervised training based on audio-only data has gained popularity recently due to the wide availability of unlabeled text and speech data. In this work, we propose incorporating text-only and semi-supervised training into an attention-based deliberation model. By incorporating text-only data in training a bidirectional encoder representation from transformer (BERT) for the deliberation text encoder, and large-scale text-to-speech and audio-only utterances using joint acoustic and text decoder (JATD) and semi-supervised training, we achieved 4%-12% WER reduction for various tasks compared to the baseline deliberation. Compared to a state-of-the-art language model (LM) rescoring method, the deliberation model reduces the Google Voice Search WER by 11% relative. We show that the deliberation model also achieves a positive human side-by-side evaluation compared to the state-of-the-art LM rescorer with reasonable endpointer latencies.

</details>

### [Simple and Effective Multi-sentence TTS with Expressive and Coherent Prosody](2206.14643.md)
**Peter Makarov, Ammar Abbas, Mateusz Łajszczak, Arnaud Joly et al.** · 2022-06-29

<details>
<summary>Abstract</summary>

Generating expressive and contextually appropriate prosody remains a challenge for modern text-to-speech (TTS) systems. This is particularly evident for long, multi-sentence inputs. In this paper, we examine simple extensions to a Transformer-based FastSpeech-like system, with the goal of improving prosody for multi-sentence TTS. We find that long context, powerful text features, and training on multi-speaker data all improve prosody. More interestingly, they result in synergies. Long context disambiguates prosody, improves coherence, and plays to the strengths of Transformers. Fine-tuning word-level features from a powerful language model, such as BERT, appears to profit from more training data, readily available in a multi-speaker setting. We look into objective metrics on pausing and pacing and perform thorough subjective evaluations for speech naturalness. Our main system, which incorporates all the extensions, achieves consistently strong results, including statistically significant improvements in speech naturalness over all its competitors.

</details>

### [Expressive, Variable, and Controllable Duration Modelling in TTS](2206.14165.md)
**Ammar Abbas, Thomas Merritt, Alexis Moinet, Sri Karlapati et al.** · 2022-06-28

<details>
<summary>Abstract</summary>

Duration modelling has become an important research problem once more with the rise of non-attention neural text-to-speech systems. The current approaches largely fall back to relying on previous statistical parametric speech synthesis technology for duration prediction, which poorly models the expressiveness and variability in speech. In this paper, we propose two alternate approaches to improve duration modelling. First, we propose a duration model conditioned on phrasing that improves the predicted durations and provides better modelling of pauses. We show that the duration model conditioned on phrasing improves the naturalness of speech over our baseline duration model. Second, we also propose a multi-speaker duration model called Cauliflow, that uses normalising flows to predict durations that better match the complex target duration distribution. Cauliflow performs on par with our other proposed duration model in terms of naturalness, whilst providing variable durations for the same prompt and variable levels of expressiveness. Lastly, we propose to condition Cauliflow on parameters that provide an intuitive control of the pacing and pausing in the synthesised speech in a novel way.

</details>

### [RetrieverTTS: Modeling Decomposed Factors for Text-Based Speech Insertion](2206.13865.md)
**Dacheng Yin, Chuanxin Tang, Yanqing Liu, Xiaoqiang Wang et al.** · 2022-06-28

<details>
<summary>Abstract</summary>

This paper proposes a new "decompose-and-edit" paradigm for the text-based speech insertion task that facilitates arbitrary-length speech insertion and even full sentence generation. In the proposed paradigm, global and local factors in speech are explicitly decomposed and separately manipulated to achieve high speaker similarity and continuous prosody. Specifically, we proposed to represent the global factors by multiple tokens, which are extracted by cross-attention operation and then injected back by link-attention operation. Due to the rich representation of global factors, we manage to achieve high speaker similarity in a zero-shot manner. In addition, we introduce a prosody smoothing task to make the local prosody factor context-aware and therefore achieve satisfactory prosody continuity. We further achieve high voice quality with an adversarial training stage. In the subjective test, our method achieves state-of-the-art performance in both naturalness and similarity. Audio samples can be found at https://ydcustc.github.io/retrieverTTS-demo/.

</details>

### [Comparison of Speech Representations for the MOS Prediction System](2206.13817.md)
**Aki Kunikoshi, Jaebok Kim, Wonsuk Jun, Kåre Sjölander** · 2022-06-28

<details>
<summary>Abstract</summary>

Automatic methods to predict Mean Opinion Score (MOS) of listeners have been researched to assure the quality of Text-to-Speech systems. Many previous studies focus on architectural advances (e.g. MBNet, LDNet, etc.) to capture relations between spectral features and MOS in a more effective way and achieved high accuracy. However, the optimal representation in terms of generalization capability still largely remains unknown. To this end, we compare the performance of Self-Supervised Learning (SSL) features obtained by the wav2vec framework to that of spectral features such as magnitude of spectrogram and melspectrogram. Moreover, we propose to combine the SSL features and features which we believe to retain essential information to the automatic MOS to compensate each other for their drawbacks. We conduct comprehensive experiments on a large-scale listening test corpus collected from past Blizzard and Voice Conversion Challenges. We found that the wav2vec feature set showed the best generalization even though the given ground-truth was not always reliable. Furthermore, we found that the combinations performed the best and analyzed how they bridged the gap between spectral and the wav2vec feature sets.

</details>

### [Avocodo: Generative Adversarial Network for Artifact-free Vocoder](2206.13404.md)
**Taejun Bak, Junmo Lee, Hanbin Bae, Jinhyeok Yang et al.** · 2022-06-27

<details>
<summary>Abstract</summary>

Neural vocoders based on the generative adversarial neural network (GAN) have been widely used due to their fast inference speed and lightweight networks while generating high-quality speech waveforms. Since the perceptually important speech components are primarily concentrated in the low-frequency bands, most GAN-based vocoders perform multi-scale analysis that evaluates downsampled speech waveforms. This multi-scale analysis helps the generator improve speech intelligibility. However, in preliminary experiments, we discovered that the multi-scale analysis which focuses on the low-frequency bands causes unintended artifacts, e.g., aliasing and imaging artifacts, which degrade the synthesized speech waveform quality. Therefore, in this paper, we investigate the relationship between these artifacts and GAN-based vocoders and propose a GAN-based vocoder, called Avocodo, that allows the synthesis of high-fidelity speech with reduced artifacts. We introduce two kinds of discriminators to evaluate speech waveforms in various perspectives: a collaborative multi-band discriminator and a sub-band discriminator. We also utilize a pseudo quadrature mirror filter bank to obtain downsampled multi-band speech waveforms while avoiding aliasing. According to experimental results, Avocodo outperforms baseline GAN-based vocoders, both objectively and subjectively, while reproducing speech with fewer artifacts.

</details>

### [Speak Like a Professional: Increasing Speech Intelligibility by Mimicking Professional Announcer Voice with Voice Conversion](2206.13021.md)
**Tuan Vu Ho, Maori Kobayashi, Masato Akagi** · 2022-06-27

<details>
<summary>Abstract</summary>

In most of practical scenarios, the announcement system must deliver speech messages in a noisy environment, in which the background noise cannot be cancelled out. The local noise reduces speech intelligibility and increases listening effort of the listener, hence hamper the effectiveness of announcement system. There has been reported that voices of professional announcers are clearer and more comprehensive than that of non-expert speakers in noisy environment. This finding suggests that the speech intelligibility might be related to the speaking style of professional announcer, which can be adapted using voice conversion method. Motivated by this idea, this paper proposes a speech intelligibility enhancement in noisy environment by applying voice conversion method on non-professional voice. We discovered that the professional announcers and non-professional speakers are clusterized into different clusters on the speaker embedding plane. This implies that the speech intelligibility can be controlled as an independent feature of speaker individuality. To examine the advantage of converted voice in noisy environment, we experimented using test words masked in pink noise at different SNR levels. The results of objective and subjective evaluations confirm that the speech intelligibility of converted voice is higher than that of original voice in low SNR conditions.

</details>

### [Synthesizing Personalized Non-speech Vocalization from Discrete Speech Representations](2206.12662.md)
**Chin-Cheng Hsu** · 2022-06-25

<details>
<summary>Abstract</summary>

We formulated non-speech vocalization (NSV) modeling as a text-to-speech task and verified its viability. Specifically, we evaluated the phonetic expressivity of HUBERT speech units on NSVs and verified our model's ability to control over speaker timbre even though the training data is speaker few-shot. In addition, we substantiated that the heterogeneity in recording conditions is the major obstacle for NSV modeling. Finally, we discussed five improvements over our method for future research. Audio samples of synthesized NSVs are available on our demo page: https://resemble-ai.github.io/reLaugh.

</details>

### [Self-supervised Context-aware Style Representation for Expressive Speech Synthesis](2206.12559.md)
**Yihan Wu, Xi Wang, Shaofei Zhang, Lei He et al.** · 2022-06-25

<details>
<summary>Abstract</summary>

Expressive speech synthesis, like audiobook synthesis, is still challenging for style representation learning and prediction. Deriving from reference audio or predicting style tags from text requires a huge amount of labeled data, which is costly to acquire and difficult to define and annotate accurately. In this paper, we propose a novel framework for learning style representation from abundant plain text in a self-supervised manner. It leverages an emotion lexicon and uses contrastive learning and deep clustering. We further integrate the style representation as a conditioned embedding in a multi-style Transformer TTS. Comparing with multi-style TTS by predicting style tags trained on the same dataset but with human annotations, our method achieves improved results according to subjective evaluations on both in-domain and out-of-domain test sets in audiobook speech. Moreover, with implicit context-aware style representation, the emotion transition of synthesized audio in a long paragraph appears more natural. The audio samples are available on the demo web.

</details>

### [SANE-TTS: Stable And Natural End-to-End Multilingual Text-to-Speech](2206.12132.md)
**Hyunjae Cho et.al.** · 2022-06-24

### [End-to-End Text-to-Speech Based on Latent Representation of Speaking Styles Using Spontaneous Dialogue](2206.12040.md)
**Kentaro Mitsui et.al.** · 2022-06-24

### [Adversarial Multi-Task Learning for Disentangling Timbre and Pitch in Singing Voice Synthesis](2206.11558.md)
**Tae-Woo Kim, Min-Su Kang, Gyeong-Hoon Lee** · 2022-06-23

<details>
<summary>Abstract</summary>

Recently, deep learning-based generative models have been introduced to generate singing voices. One approach is to predict the parametric vocoder features consisting of explicit speech parameters. This approach has the advantage that the meaning of each feature is explicitly distinguished. Another approach is to predict mel-spectrograms for a neural vocoder. However, parametric vocoders have limitations of voice quality and the mel-spectrogram features are difficult to model because the timbre and pitch information are entangled. In this study, we propose a singing voice synthesis model with multi-task learning to use both approaches -- acoustic features for a parametric vocoder and mel-spectrograms for a neural vocoder. By using the parametric vocoder features as auxiliary features, the proposed model can efficiently disentangle and control the timbre and pitch components of the mel-spectrogram. Moreover, a generative adversarial network framework is applied to improve the quality of singing voices in a multi-singer model. Experimental results demonstrate that our proposed model can generate more natural singing voices than the single-task models, while performing better than the conventional parametric vocoder-based model.

</details>

### [Radio2Speech: High Quality Speech Recovery from Radio Frequency Signals](2206.11066.md)
**Running Zhao, Jiangtao Yu, Tingle Li, Hang Zhao et al.** · 2022-06-22

<details>
<summary>Abstract</summary>

Considering the microphone is easily affected by noise and soundproof materials, the radio frequency (RF) signal is a promising candidate to recover audio as it is immune to noise and can traverse many soundproof objects. In this paper, we introduce Radio2Speech, a system that uses RF signals to recover high quality speech from the loudspeaker. Radio2Speech can recover speech comparable to the quality of the microphone, advancing from recovering only single tone music or incomprehensible speech in existing approaches. We use Radio UNet to accurately recover speech in time-frequency domain from RF signals with limited frequency band. Also, we incorporate the neural vocoder to synthesize the speech waveform from the estimated time-frequency representation without using the contaminated phase. Quantitative and qualitative evaluations show that in quiet, noisy and soundproof scenarios, Radio2Speech achieves state-of-the-art performance and is on par with the microphone that works in quiet scenarios.

</details>

### [Human-in-the-loop Speaker Adaptation for DNN-based Multi-speaker TTS](2206.10256.md)
**Kenta Udagawa et.al.** · 2022-06-21

### [WOLONet: Wave Outlooker for Efficient and High Fidelity Speech Synthesis](2206.09920.md)
**Yi Wang, Yi Si** · 2022-06-20

<details>
<summary>Abstract</summary>

Recently, GAN-based neural vocoders such as Parallel WaveGAN, MelGAN, HiFiGAN, and UnivNet have become popular due to their lightweight and parallel structure, resulting in a real-time synthesized waveform with high fidelity, even on a CPU. HiFiGAN and UnivNet are two SOTA vocoders. Despite their high quality, there is still room for improvement. In this paper, motivated by the structure of Vision Outlooker from computer vision, we adopt a similar idea and propose an effective and lightweight neural vocoder called WOLONet. In this network, we develop a novel lightweight block that uses a location-variable, channel-independent, and depthwise dynamic convolutional kernel with sinusoidally activated dynamic kernel weights. To demonstrate the effectiveness and generalizability of our method, we perform an ablation study to verify our novel design and make a subjective and objective comparison with typical GAN-based vocoders. The results show that our WOLONet achieves the best generation quality while requiring fewer parameters than the two neural SOTA vocoders, HiFiGAN and UnivNet.

</details>

### [Automatic Prosody Annotation with Pre-Trained Text-Speech Model](2206.07956.md)
**Ziqian Dai et.al.** · 2022-06-16

### [Acoustic Modeling for End-to-End Empathetic Dialogue Speech Synthesis Using Linguistic and Prosodic Contexts of Dialogue History](2206.08039.md)
**Yuto Nishimura, Yuki Saito, Shinnosuke Takamichi, Kentaro Tachibana et al.** · 2022-06-16

<details>
<summary>Abstract</summary>

We propose an end-to-end empathetic dialogue speech synthesis (DSS) model that considers both the linguistic and prosodic contexts of dialogue history. Empathy is the active attempt by humans to get inside the interlocutor in dialogue, and empathetic DSS is a technology to implement this act in spoken dialogue systems. Our model is conditioned by the history of linguistic and prosody features for predicting appropriate dialogue context. As such, it can be regarded as an extension of the conventional linguistic-feature-based dialogue history modeling. To train the empathetic DSS model effectively, we investigate 1) a self-supervised learning model pretrained with large speech corpora, 2) a style-guided training using a prosody embedding of the current utterance to be predicted by the dialogue context embedding, 3) a cross-modal attention to combine text and speech modalities, and 4) a sentence-wise embedding to achieve fine-grained prosody modeling rather than utterance-wise modeling. The evaluation results demonstrate that 1) simply considering prosodic contexts of the dialogue history does not improve the quality of speech in empathetic DSS and 2) introducing style-guided training and sentence-wise embedding modeling achieves higher speech quality than that by the conventional method.

</details>

### [EPG2S: Speech Generation and Speech Enhancement based on Electropalatography and Audio Signals using Multimodal Learning](2206.07860.md)
**Li-Chin Chen, Po-Hsun Chen, Richard Tzong-Han Tsai, Yu Tsao** · 2022-06-16

<details>
<summary>Abstract</summary>

Speech generation and enhancement based on articulatory movements facilitate communication when the scope of verbal communication is absent, e.g., in patients who have lost the ability to speak. Although various techniques have been proposed to this end, electropalatography (EPG), which is a monitoring technique that records contact between the tongue and hard palate during speech, has not been adequately explored. Herein, we propose a novel multimodal EPG-to-speech (EPG2S) system that utilizes EPG and speech signals for speech generation and enhancement. Different fusion strategies based on multiple combinations of EPG and noisy speech signals are examined, and the viability of the proposed method is investigated. Experimental results indicate that EPG2S achieves desirable speech generation outcomes based solely on EPG signals. Further, the addition of noisy speech signals is observed to improve quality and intelligibility. Additionally, EPG2S is observed to achieve high-quality speech enhancement based solely on audio signals, with the addition of EPG signals further improving the performance. The late fusion strategy is deemed to be the most effective approach for simultaneous speech generation and enhancement.

</details>

### [Accurate Emotion Strength Assessment for Seen and Unseen Speech Based on Data-Driven Deep Learning](2206.07229.md)
**Rui Liu, Berrak Sisman, Björn Schuller, Guanglai Gao et al.** · 2022-06-15

<details>
<summary>Abstract</summary>

Emotion classification of speech and assessment of the emotion strength are required in applications such as emotional text-to-speech and voice conversion. The emotion attribute ranking function based on Support Vector Machine (SVM) was proposed to predict emotion strength for emotional speech corpus. However, the trained ranking function doesn't generalize to new domains, which limits the scope of applications, especially for out-of-domain or unseen speech. In this paper, we propose a data-driven deep learning model, i.e. StrengthNet, to improve the generalization of emotion strength assessment for seen and unseen speech. This is achieved by the fusion of emotional data from various domains. We follow a multi-task learning network architecture that includes an acoustic encoder, a strength predictor, and an auxiliary emotion predictor. Experiments show that the predicted emotion strength of the proposed StrengthNet is highly correlated with ground truth scores for both seen and unseen speech. We release the source codes at: https://github.com/ttslr/StrengthNet.

</details>

### [VisageSynTalk: Unseen Speaker Video-to-Speech Synthesis via Speech-Visage Feature Selection](2206.07458.md)
**Joanna Hong, Minsu Kim, Yong Man Ro** · 2022-06-15

<details>
<summary>Abstract</summary>

The goal of this work is to reconstruct speech from a silent talking face video. Recent studies have shown impressive performance on synthesizing speech from silent talking face videos. However, they have not explicitly considered on varying identity characteristics of different speakers, which place a challenge in the video-to-speech synthesis, and this becomes more critical in unseen-speaker settings. Our approach is to separate the speech content and the visage-style from a given silent talking face video. By guiding the model to independently focus on modeling the two representations, we can obtain the speech of high intelligibility from the model even when the input video of an unseen subject is given. To this end, we introduce speech-visage selection that separates the speech content and the speaker identity from the visual features of the input video. The disentangled representations are jointly incorporated to synthesize speech through visage-style based synthesizer which generates speech by coating the visage-styles while maintaining the speech content. Thus, the proposed framework brings the advantage of synthesizing the speech containing the right content even with the silent talking face video of an unseen subject. We validate the effectiveness of the proposed framework on the GRID, TCD-TIMIT volunteer, and LRW datasets.

</details>

### [End-to-End Voice Conversion with Information Perturbation](2206.07569.md)
**Qicong Xie, Shan Yang, Yi Lei, Lei Xie et al.** · 2022-06-15

<details>
<summary>Abstract</summary>

The ideal goal of voice conversion is to convert the source speaker's speech to sound naturally like the target speaker while maintaining the linguistic content and the prosody of the source speech. However, current approaches are insufficient to achieve comprehensive source prosody transfer and target speaker timbre preservation in the converted speech, and the quality of the converted speech is also unsatisfied due to the mismatch between the acoustic model and the vocoder. In this paper, we leverage the recent advances in information perturbation and propose a fully end-to-end approach to conduct high-quality voice conversion. We first adopt information perturbation to remove speaker-related information in the source speech to disentangle speaker timbre and linguistic content and thus the linguistic information is subsequently modeled by a content encoder. To better transfer the prosody of the source speech to the target, we particularly introduce a speaker-related pitch encoder which can maintain the general pitch pattern of the source speaker while flexibly modifying the pitch intensity of the generated speech. Finally, one-shot voice conversion is set up through continuous speaker space modeling. Experimental results indicate that the proposed end-to-end approach significantly outperforms the state-of-the-art models in terms of intelligibility, naturalness, and speaker similarity.

</details>

### [RF-Next: Efficient Receptive Field Search for Convolutional Neural Networks](2206.06637.md)
**Shanghua Gao, Zhong-Yu Li, Qi Han, Ming-Ming Cheng et al.** · 2022-06-14

<details>
<summary>Abstract</summary>

Temporal/spatial receptive fields of models play an important role in sequential/spatial tasks. Large receptive fields facilitate long-term relations, while small receptive fields help to capture the local details. Existing methods construct models with hand-designed receptive fields in layers. Can we effectively search for receptive field combinations to replace hand-designed patterns? To answer this question, we propose to find better receptive field combinations through a global-to-local search scheme. Our search scheme exploits both global search to find the coarse combinations and local search to get the refined receptive field combinations further. The global search finds possible coarse combinations other than human-designed patterns. On top of the global search, we propose an expectation-guided iterative local search scheme to refine combinations effectively. Our RF-Next models, plugging receptive field search to various models, boost the performance on many tasks, e.g., temporal action segmentation, object detection, instance segmentation, and speech synthesis. The source code is publicly available on http://mmcheng.net/rfnext.

</details>

### [BigVGAN: A Universal Neural Vocoder with Large-Scale Training](2206.04658.md)
**Sang-gil Lee, Wei Ping, Boris Ginsburg, Bryan Catanzaro et al.** · 2022-06-09

<details>
<summary>Abstract</summary>

Despite recent progress in generative adversarial network (GAN)-based vocoders, where the model generates raw waveform conditioned on acoustic features, it is challenging to synthesize high-fidelity audio for numerous speakers across various recording environments. In this work, we present BigVGAN, a universal vocoder that generalizes well for various out-of-distribution scenarios without fine-tuning. We introduce periodic activation function and anti-aliased representation into the GAN generator, which brings the desired inductive bias for audio synthesis and significantly improves audio quality. In addition, we train our GAN vocoder at the largest scale up to 112M parameters, which is unprecedented in the literature. We identify and address the failure modes in large-scale GAN training for audio, while maintaining high-fidelity output without over-regularization. Our BigVGAN, trained only on clean speech (LibriTTS), achieves the state-of-the-art performance for various zero-shot (out-of-distribution) conditions, including unseen speakers, languages, recording environments, singing voices, music, and instrumental audio. We release our code and model at: https://github.com/NVIDIA/BigVGAN

</details>

### [Speak Like a Dog: Human to Non-human creature Voice Conversion](2206.04780.md)
**Kohei Suzuki, Shoki Sakamoto, Tadahiro Taniguchi, Hirokazu Kameoka** · 2022-06-09

<details>
<summary>Abstract</summary>

This paper proposes a new voice conversion (VC) task from human speech to dog-like speech while preserving linguistic information as an example of human to non-human creature voice conversion (H2NH-VC) tasks. Although most VC studies deal with human to human VC, H2NH-VC aims to convert human speech into non-human creature-like speech. Non-parallel VC allows us to develop H2NH-VC, because we cannot collect a parallel dataset that non-human creatures speak human language. In this study, we propose to use dogs as an example of a non-human creature target domain and define the "speak like a dog" task. To clarify the possibilities and characteristics of the "speak like a dog" task, we conducted a comparative experiment using existing representative non-parallel VC methods in acoustic features (Mel-cepstral coefficients and Mel-spectrograms), network architectures (five different kernel-size settings), and training criteria (variational autoencoder (VAE)- based and generative adversarial network-based). Finally, the converted voices were evaluated using mean opinion scores: dog-likeness, sound quality and intelligibility, and character error rate (CER). The experiment showed that the employment of the Mel-spectrogram improved the dog-likeness of the converted speech, while it is challenging to preserve linguistic information. Challenges and limitations of the current VC methods for H2NH-VC are highlighted.

</details>

### [FlexLip: A Controllable Text-to-Lip System](2206.03206.md)
**Dan Oneata, Beata Lorincz, Adriana Stan, Horia Cucu** · 2022-06-07

<details>
<summary>Abstract</summary>

The task of converting text input into video content is becoming an important topic for synthetic media generation. Several methods have been proposed with some of them reaching close-to-natural performances in constrained tasks. In this paper, we tackle a subissue of the text-to-video generation problem, by converting the text into lip landmarks. However, we do this using a modular, controllable system architecture and evaluate each of its individual components. Our system, entitled FlexLip, is split into two separate modules: text-to-speech and speech-to-lip, both having underlying controllable deep neural network architectures. This modularity enables the easy replacement of each of its components, while also ensuring the fast adaptation to new speaker identities by disentangling or projecting the input features. We show that by using as little as 20 min of data for the audio generation component, and as little as 5 min for the speech-to-lip component, the objective measures of the generated lip landmarks are comparable with those obtained when using a larger set of training samples. We also introduce a series of objective evaluation measures over the complete flow of our system by taking into consideration several aspects of the data and system configuration. These aspects pertain to the quality and amount of training data, the use of pretrained models, and the data contained therein, as well as the identity of the target speaker; with regard to the latter, we show that we can perform zero-shot lip adaptation to an unseen identity by simply updating the shape of the lips in our model.

</details>

### [Dict-TTS: Learning to Pronounce with Prior Dictionary Knowledge for Text-to-Speech](2206.02147.md)
**Ziyue Jiang, Zhe Su, Zhou Zhao, Qian Yang et al.** · 2022-06-05

<details>
<summary>Abstract</summary>

Polyphone disambiguation aims to capture accurate pronunciation knowledge from natural text sequences for reliable Text-to-speech (TTS) systems. However, previous approaches require substantial annotated training data and additional efforts from language experts, making it difficult to extend high-quality neural TTS systems to out-of-domain daily conversations and countless languages worldwide. This paper tackles the polyphone disambiguation problem from a concise and novel perspective: we propose Dict-TTS, a semantic-aware generative text-to-speech model with an online website dictionary (the existing prior information in the natural language). Specifically, we design a semantics-to-pronunciation attention (S2PA) module to match the semantic patterns between the input text sequence and the prior semantics in the dictionary and obtain the corresponding pronunciations; The S2PA module can be easily trained with the end-to-end TTS model without any annotated phoneme labels. Experimental results in three languages show that our model outperforms several strong baseline models in terms of pronunciation accuracy and improves the prosody modeling of TTS systems. Further extensive analyses demonstrate that each design in Dict-TTS is effective. The code is available at \url{https://github.com/Zain-Jiang/Dict-TTS}.

</details>

### [Learning Speaker-specific Lip-to-Speech Generation](2206.02050.md)
**Munender Varshney, Ravindra Yadav, Vinay P. Namboodiri, Rajesh M Hegde** · 2022-06-04

<details>
<summary>Abstract</summary>

Understanding the lip movement and inferring the speech from it is notoriously difficult for the common person. The task of accurate lip-reading gets help from various cues of the speaker and its contextual or environmental setting. Every speaker has a different accent and speaking style, which can be inferred from their visual and speech features. This work aims to understand the correlation/mapping between speech and the sequence of lip movement of individual speakers in an unconstrained and large vocabulary. We model the frame sequence as a prior to the transformer in an auto-encoder setting and learned a joint embedding that exploits temporal properties of both audio and video. We learn temporal synchronization using deep metric learning, which guides the decoder to generate speech in sync with input lip movements. The predictive posterior thus gives us the generated speech in speaker speaking style. We have trained our model on the Grid and Lip2Wav Chemistry lecture dataset to evaluate single speaker natural speech generation tasks from lip movement in an unconstrained natural setting. Extensive evaluation using various qualitative and quantitative metrics with human evaluation also shows that our method outperforms the Lip2Wav Chemistry dataset(large vocabulary in an unconstrained setting) by a good margin across almost all evaluation metrics and marginally outperforms the state-of-the-art on GRID dataset.

</details>

### [AdaVITS: Tiny VITS for Low Computing Resource Speaker Adaptation](2206.00208.md)
**Kun Song, Heyang Xue, Xinsheng Wang, Jian Cong et al.** · 2022-06-01

<details>
<summary>Abstract</summary>

Speaker adaptation in text-to-speech synthesis (TTS) is to finetune a pre-trained TTS model to adapt to new target speakers with limited data. While much effort has been conducted towards this task, seldom work has been performed for low computational resource scenarios due to the challenges raised by the requirement of the lightweight model and less computational complexity. In this paper, a tiny VITS-based TTS model, named AdaVITS, for low computing resource speaker adaptation is proposed. To effectively reduce parameters and computational complexity of VITS, an iSTFT-based wave construction decoder is proposed to replace the upsampling-based decoder which is resource-consuming in the original VITS. Besides, NanoFlow is introduced to share the density estimate across flow blocks to reduce the parameters of the prior encoder. Furthermore, to reduce the computational complexity of the textual encoder, scaled-dot attention is replaced with linear attention. To deal with the instability caused by the simplified model, instead of using the original text encoder, phonetic posteriorgram (PPG) is utilized as linguistic feature via a text-to-PPG module, which is then used as input for the encoder. Experiment shows that AdaVITS can generate stable and natural speech in speaker adaptation with 8.97M model parameters and 0.72GFlops computational complexity.

</details>

### [Preparing an Endangered Language for the Digital Age: The Case of Judeo-Spanish](2205.15599.md)
**Alp Öktem, Rodolfo Zevallos, Yasmin Moslem, Güneş Öztürk et al.** · 2022-05-31

<details>
<summary>Abstract</summary>

We develop machine translation and speech synthesis systems to complement the efforts of revitalizing Judeo-Spanish, the exiled language of Sephardic Jews, which survived for centuries, but now faces the threat of extinction in the digital age. Building on resources created by the Sephardic community of Turkey and elsewhere, we create corpora and tools that would help preserve this language for future generations. For machine translation, we first develop a Spanish to Judeo-Spanish rule-based machine translation system, in order to generate large volumes of synthetic parallel data in the relevant language pairs: Turkish, English and Spanish. Then, we train baseline neural machine translation engines using this synthetic data and authentic parallel data created from translations by the Sephardic community. For text-to-speech synthesis, we present a 3.5 hour single speaker speech corpus for building a neural speech synthesis engine. Resources, model weights and online inference engines are shared publicly.

</details>

### [Efficient decoding self-attention for end-to-end speech synthesis](s2:35fab8043d93071a58190d7566f0de690ecd37f6.md)
**Wei Zhao, Li Xu** · 2022-05-31

<details>
<summary>Abstract</summary>

Self-attention has been innovatively applied to text-to-speech (TTS) because of its parallel structure and superior strength in modeling sequential data. However, when used in end-to-end speech synthesis with an autoregressive decoding scheme, its inference speed becomes relatively low due to the quadratic complexity in sequence length. This problem becomes particularly severe on devices without graphics processing units (GPUs). To alleviate the dilemma, we propose an efficient decoding self-attention (EDSA) module as an alternative. Combined with a dynamic programming decoding procedure, TTS model inference can be effectively accelerated to have a linear computation complexity. We conduct studies on Mandarin and English datasets and find that our proposed model with EDSA can achieve 720% and 50% higher inference speed on the central processing unit (CPU) and GPU respectively, with almost the same performance. Thus, this method may make the deployment of such models easier when there are limited GPU resources. In addition, our model may perform better than the baseline Transformer TTS on out-of-domain utterances.

</details>

### [Guided-TTS 2: A Diffusion Model for High-quality Adaptive Text-to-Speech with Untranscribed Data](2205.15370.md)
**Sungwon Kim et.al.** · 2022-05-30

### [Exploiting Transliterated Words for Finding Similarity in Inter-Language News Articles using Machine Learning](2206.11860.md)
**Sameea Naeem, Arif ur Rahman, Syed Mujtaba Haider, Abdul Basit Mughal** · 2022-05-29

<details>
<summary>Abstract</summary>

Finding similarities between two inter-language news articles is a challenging problem of Natural Language Processing (NLP). It is difficult to find similar news articles in a different language other than the native language of user, there is a need for a Machine Learning based automatic system to find the similarity between two inter-language news articles. In this article, we propose a Machine Learning model with the combination of English Urdu word transliteration which will show whether the English news article is similar to the Urdu news article or not. The existing approaches to find similarities has a major drawback when the archives contain articles of low-resourced languages like Urdu along with English news article. The existing approaches to find similarities has drawback when the archives contain low-resourced languages like Urdu along with English news articles. We used lexicon to link Urdu and English news articles. As Urdu language processing applications like machine translation, text to speech, etc are unable to handle English text at the same time so this research proposed technique to find similarities in English and Urdu news articles based on transliteration.

</details>

### [QSpeech: Low-Qubit Quantum Speech Application Toolkit](2205.13221.md)
**Zhenhou Hong, Jianzong Wang, Xiaoyang Qu, Chendong Zhao et al.** · 2022-05-26

<details>
<summary>Abstract</summary>

Quantum devices with low qubits are common in the Noisy Intermediate-Scale Quantum (NISQ) era. However, Quantum Neural Network (QNN) running on low-qubit quantum devices would be difficult since it is based on Variational Quantum Circuit (VQC), which requires many qubits. Therefore, it is critical to make QNN with VQC run on low-qubit quantum devices. In this study, we propose a novel VQC called the low-qubit VQC. VQC requires numerous qubits based on the input dimension; however, the low-qubit VQC with linear transformation can liberate this condition. Thus, it allows the QNN to run on low-qubit quantum devices for speech applications. Furthermore, as compared to the VQC, our proposed low-qubit VQC can stabilize the training process more. Based on the low-qubit VQC, we implement QSpeech, a library for quick prototyping of hybrid quantum-classical neural networks in the speech field. It has numerous quantum neural layers and QNN models for speech applications. Experiments on Speech Command Recognition and Text-to-Speech show that our proposed low-qubit VQC outperforms VQC and is more stable.

</details>

### [TDASS: Target Domain Adaptation Speech Synthesis Framework for Multi-speaker Low-Resource TTS](2205.11824.md)
**Xulong Zhang et.al.** · 2022-05-24

### [T-Modules: Translation Modules for Zero-Shot Cross-Modal Machine Translation](2205.12216.md)
**Paul-Ambroise Duquenne, Hongyu Gong, Benoît Sagot, Holger Schwenk** · 2022-05-24

<details>
<summary>Abstract</summary>

We present a new approach to perform zero-shot cross-modal transfer between speech and text for translation tasks. Multilingual speech and text are encoded in a joint fixed-size representation space. Then, we compare different approaches to decode these multimodal and multilingual fixed-size representations, enabling zero-shot translation between languages and modalities. All our models are trained without the need of cross-modal labeled translation data. Despite a fixed-size representation, we achieve very competitive results on several text and speech translation tasks. In particular, we significantly improve the state-of-the-art for zero-shot speech translation on Must-C. Incorporating a speech decoder in our framework, we introduce the first results for zero-shot direct speech-to-speech and text-to-speech translation.

</details>

### [PaddleSpeech: An Easy-to-Use All-in-One Speech Toolkit](2205.12007.md)
**Hui Zhang, Tian Yuan, Junkun Chen, Xintong Li et al.** · 2022-05-20

<details>
<summary>Abstract</summary>

PaddleSpeech is an open-source all-in-one speech toolkit. It aims at facilitating the development and research of speech processing technologies by providing an easy-to-use command-line interface and a simple code structure. This paper describes the design philosophy and core architecture of PaddleSpeech to support several essential speech-to-text and text-to-speech tasks. PaddleSpeech achieves competitive or state-of-the-art performance on various speech datasets and implements the most popular methods. It also provides recipes and pretrained models to quickly reproduce the experimental results in this paper. PaddleSpeech is publicly avaiable at https://github.com/PaddlePaddle/PaddleSpeech.

</details>

### [End-to-End Zero-Shot Voice Conversion with Location-Variable Convolutions](2205.09784.md)
**Wonjune Kang, Mark Hasegawa-Johnson, Deb Roy** · 2022-05-19

<details>
<summary>Abstract</summary>

Zero-shot voice conversion is becoming an increasingly popular research topic, as it promises the ability to transform speech to sound like any speaker. However, relatively little work has been done on end-to-end methods for this task, which are appealing because they remove the need for a separate vocoder to generate audio from intermediate features. In this work, we propose LVC-VC, an end-to-end zero-shot voice conversion model that uses location-variable convolutions (LVCs) to jointly model the conversion and speech synthesis processes. LVC-VC utilizes carefully designed input features that have disentangled content and speaker information, and it uses a neural vocoder-like architecture that utilizes LVCs to efficiently combine them and perform voice conversion while directly synthesizing time domain audio. Experiments show that our model achieves especially well balanced performance between voice style transfer and speech intelligibility compared to several baselines.

</details>

### [SDS-200: A Swiss German Speech to Standard German Text Corpus](2205.09501.md)
**Michel Plüss, Manuela Hürlimann, Marc Cuny, Alla Stöckli et al.** · 2022-05-19

<details>
<summary>Abstract</summary>

We present SDS-200, a corpus of Swiss German dialectal speech with Standard German text translations, annotated with dialect, age, and gender information of the speakers. The dataset allows for training speech translation, dialect recognition, and speech synthesis systems, among others. The data was collected using a web recording tool that is open to the public. Each participant was given a text in Standard German and asked to translate it to their Swiss German dialect before recording it. To increase the corpus quality, recordings were validated by other participants. The data consists of 200 hours of speech by around 4000 different speakers and covers a large part of the Swiss-German dialect landscape. We release SDS-200 alongside a baseline speech translation model, which achieves a word error rate (WER) of 30.3 and a BLEU score of 53.1 on the SDS-200 test set. Furthermore, we use SDS-200 to fine-tune a pre-trained XLS-R model, achieving 21.6 WER and 64.0 BLEU.

</details>

### [Macedonian Speech Synthesis for Assistive Technology Applications](2205.09198.md)
**Bojan Sofronievski, Elena Velovska, Martin Velichkovski, Violeta Argirova et al.** · 2022-05-18

<details>
<summary>Abstract</summary>

Speech technology is becoming ever more ubiquitous with the advance of speech enabled devices and services. The use of speech synthesis in Augmentative and Alternative Communication tools, has facilitated inclusion of individuals with speech impediments allowing them to communicate with their surroundings using speech. Although there are numerous speech synthesis systems for the most spoken world languages, there is still a limited offer for smaller languages. We propose and compare three models built using parametric and deep learning techniques for Macedonian trained on a newly recorded corpus. We target low-resource edge deployment for Augmentative and Alternative Communication and assistive technologies, such as communication boards and screen readers. The listening test results show that parametric speech synthesis is as performant compared to the more advanced deep learning models. Since it also requires less resources, and offers full speech rate and pitch control, it is the preferred choice for building a Macedonian TTS system for this application scenario.

</details>

### [SAMU-XLSR: Semantically-Aligned Multimodal Utterance-level Cross-Lingual Speech Representation](2205.08180.md)
**Sameer Khurana, Antoine Laurent, James Glass** · 2022-05-17

<details>
<summary>Abstract</summary>

We propose the SAMU-XLSR: Semantically-Aligned Multimodal Utterance-level Cross-Lingual Speech Representation learning framework. Unlike previous works on speech representation learning, which learns multilingual contextual speech embedding at the resolution of an acoustic frame (10-20ms), this work focuses on learning multimodal (speech-text) multilingual speech embedding at the resolution of a sentence (5-10s) such that the embedding vector space is semantically aligned across different languages. We combine state-of-the-art multilingual acoustic frame-level speech representation learning model XLS-R with the Language Agnostic BERT Sentence Embedding (LaBSE) model to create an utterance-level multimodal multilingual speech encoder SAMU-XLSR. Although we train SAMU-XLSR with only multilingual transcribed speech data, cross-lingual speech-text and speech-speech associations emerge in its learned representation space. To substantiate our claims, we use SAMU-XLSR speech encoder in combination with a pre-trained LaBSE text sentence encoder for cross-lingual speech-to-text translation retrieval, and SAMU-XLSR alone for cross-lingual speech-to-speech translation retrieval. We highlight these applications by performing several cross-lingual text and speech translation retrieval tasks across several datasets.

</details>

### [GenerSpeech: Towards Style Transfer for Generalizable Out-Of-Domain Text-to-Speech](2205.07211.md)
**Rongjie Huang, Yi Ren, Jinglin Liu, Chenye Cui et al.** · 2022-05-15

<details>
<summary>Abstract</summary>

Style transfer for out-of-domain (OOD) speech synthesis aims to generate speech samples with unseen style (e.g., speaker identity, emotion, and prosody) derived from an acoustic reference, while facing the following challenges: 1) The highly dynamic style features in expressive voice are difficult to model and transfer; and 2) the TTS models should be robust enough to handle diverse OOD conditions that differ from the source data. This paper proposes GenerSpeech, a text-to-speech model towards high-fidelity zero-shot style transfer of OOD custom voice. GenerSpeech decomposes the speech variation into the style-agnostic and style-specific parts by introducing two components: 1) a multi-level style adaptor to efficiently model a large range of style conditions, including global speaker and emotion characteristics, and the local (utterance, phoneme, and word-level) fine-grained prosodic representations; and 2) a generalizable content adaptor with Mix-Style Layer Normalization to eliminate style information in the linguistic content representation and thus improve model generalization. Our evaluations on zero-shot style transfer demonstrate that GenerSpeech surpasses the state-of-the-art models in terms of audio quality and style similarity. The extension studies to adaptive style transfer further show that GenerSpeech performs robustly in the few-shot data setting. Audio samples are available at https://GenerSpeech.github.io/

</details>

### [Talking Face Generation with Multilingual TTS](2205.06421.md)
**Hyoung-Kyu Song, Sang Hoon Woo, Junhyeok Lee, Seungmin Yang et al.** · 2022-05-13

<details>
<summary>Abstract</summary>

In this work, we propose a joint system combining a talking face generation system with a text-to-speech system that can generate multilingual talking face videos from only the text input. Our system can synthesize natural multilingual speeches while maintaining the vocal identity of the speaker, as well as lip movements synchronized to the synthesized speech. We demonstrate the generalization capabilities of our system by selecting four languages (Korean, English, Japanese, and Chinese) each from a different language family. We also compare the outputs of our talking face generation model to outputs of a prior work that claims multilingual support. For our demo, we add a translation API to the preprocessing stage and present it in the form of a neural dubber so that users can utilize the multilingual property of our system more easily.

</details>

### [Unified Source-Filter GAN with Harmonic-plus-Noise Source Excitation Generation](2205.06053.md)
**Reo Yoneyama, Yi-Chiao Wu, Tomoki Toda** · 2022-05-12

<details>
<summary>Abstract</summary>

This paper introduces a unified source-filter network with a harmonic-plus-noise source excitation generation mechanism. In our previous work, we proposed unified Source-Filter GAN (uSFGAN) for developing a high-fidelity neural vocoder with flexible voice controllability using a unified source-filter neural network architecture. However, the capability of uSFGAN to model the aperiodic source excitation signal is insufficient, and there is still a gap in sound quality between the natural and generated speech. To improve the source excitation modeling and generated sound quality, a new source excitation generation network separately generating periodic and aperiodic components is proposed. The advanced adversarial training procedure of HiFiGAN is also adopted to replace that of Parallel WaveGAN used in the original uSFGAN. Both objective and subjective evaluation results show that the modified uSFGAN significantly improves the sound quality of the basic uSFGAN while maintaining the voice controllability.

</details>

### [Real-Time Packet Loss Concealment With Mixed Generative and Predictive Model](2205.05785.md)
**Jean-Marc Valin, Ahmed Mustafa, Christopher Montgomery, Timothy B. Terriberry et al.** · 2022-05-11

<details>
<summary>Abstract</summary>

As deep speech enhancement algorithms have recently demonstrated capabilities greatly surpassing their traditional counterparts for suppressing noise, reverberation and echo, attention is turning to the problem of packet loss concealment (PLC). PLC is a challenging task because it not only involves real-time speech synthesis, but also frequent transitions between the received audio and the synthesized concealment. We propose a hybrid neural PLC architecture where the missing speech is synthesized using a generative model conditioned using a predictive model. The resulting algorithm achieves natural concealment that surpasses the quality of existing conventional PLC algorithms and ranked second in the Interspeech 2022 PLC Challenge. We show that our solution not only works for uncompressed audio, but is also applicable to a modern speech codec.

</details>

### [Towards Improved Zero-shot Voice Conversion with Conditional DSVAE](2205.05227.md)
**Jiachen Lian, Chunlei Zhang, Gopala Krishna Anumanchipalli, Dong Yu** · 2022-05-11

<details>
<summary>Abstract</summary>

Disentangling content and speaking style information is essential for zero-shot non-parallel voice conversion (VC). Our previous study investigated a novel framework with disentangled sequential variational autoencoder (DSVAE) as the backbone for information decomposition. We have demonstrated that simultaneous disentangling content embedding and speaker embedding from one utterance is feasible for zero-shot VC. In this study, we continue the direction by raising one concern about the prior distribution of content branch in the DSVAE baseline. We find the random initialized prior distribution will force the content embedding to reduce the phonetic-structure information during the learning process, which is not a desired property. Here, we seek to achieve a better content embedding with more phonetic information preserved. We propose conditional DSVAE, a new model that enables content bias as a condition to the prior modeling and reshapes the content embedding sampled from the posterior distribution. In our experiment on the VCTK dataset, we demonstrate that content embeddings derived from the conditional DSVAE overcome the randomness and achieve a much better phoneme classification accuracy, a stabilized vocalization and a better zero-shot VC performance compared with the competitive DSVAE baseline.

</details>

### [NaturalSpeech: End-to-End Text to Speech Synthesis with Human-Level Quality](2205.04421.md)
**Xu Tan et.al.** · 2022-05-10

### [Cross-Utterance Conditioned VAE for Non-Autoregressive Text-to-Speech](2205.04120.md)
**Yang Li et.al.** · 2022-05-09

### [ReCAB-VAE: Gumbel-Softmax Variational Inference Based on Analytic Divergence](2205.04104.md)
**Sangshin Oh, Seyun Um, Hong-Goo Kang** · 2022-05-09

<details>
<summary>Abstract</summary>

The Gumbel-softmax distribution, or Concrete distribution, is often used to relax the discrete characteristics of a categorical distribution and enable back-propagation through differentiable reparameterization. Although it reliably yields low variance gradients, it still relies on a stochastic sampling process for optimization. In this work, we present a relaxed categorical analytic bound (ReCAB), a novel divergence-like metric which corresponds to the upper bound of the Kullback-Leibler divergence (KLD) of a relaxed categorical distribution. The proposed metric is easy to implement because it has a closed form solution, and empirical results show that it is close to the actual KLD. Along with this new metric, we propose a relaxed categorical analytic bound variational autoencoder (ReCAB-VAE) that successfully models both continuous and relaxed discrete latent representations. We implement an emotional text-to-speech synthesis system based on the proposed framework, and show that the proposed system flexibly and stably controls emotion expressions with better speech quality compared to baselines that use stochastic estimation or categorical distribution approximation.

</details>

### [Muskits: an End-to-End Music Processing Toolkit for Singing Voice Synthesis](2205.04029.md)
**Jiatong Shi, Shuai Guo, Tao Qian, Nan Huo et al.** · 2022-05-09

<details>
<summary>Abstract</summary>

This paper introduces a new open-source platform named Muskits for end-to-end music processing, which mainly focuses on end-to-end singing voice synthesis (E2E-SVS). Muskits supports state-of-the-art SVS models, including RNN SVS, transformer SVS, and XiaoiceSing. The design of Muskits follows the style of widely-used speech processing toolkits, ESPnet and Kaldi, for data prepossessing, training, and recipe pipelines. To the best of our knowledge, this toolkit is the first platform that allows a fair and highly-reproducible comparison between several published works in SVS. In addition, we also demonstrate several advanced usages based on the toolkit functionalities, including multilingual training and transfer learning. This paper describes the major framework of Muskits, its functionalities, and experimental results in single-singer, multi-singer, multilingual, and transfer learning scenarios. The toolkit is publicly available at https://github.com/SJTMusicTeam/Muskits.

</details>

### [EVASS: Emotional Variational End-to-End Speech Synthesis with Semi-Supervised and Adverserial Learning](s2:55a3e96af307c8662967047243115e5dd36d6067.md)
**Mohamed Osman** · 2022-05-08

<details>
<summary>Abstract</summary>

Communicating one's inner state - their emotions and feelings - forms one of the core principles of social communication and behavior in humans. Emotion is an important component of speech, and its inclusion in synthetic speech will allow for breakthroughs in applications like human-machine interfacing, e-book reading, and voice acting. However, modelling emotions in speech in an end-to-end manner has so far remained an under-explored topic of research. To address this, we experiment with novel methods in global emotional modelling in unsupervised, semi-supervised and adverserial contexts using an end-to-end text-to-speech (TTS) architecture. We condition the latent space, duration prediction and audio generation on novel hybrid labels based on ground truth data – 14 emotion labels, 64 sentiment analysis labels, and speaker labels - which may be inferred from input text during inference. Experiments on conditional discriminators were also performed. The final proposed model produces high quality expressive results comparable to the state of the art.

</details>

### [SVTS: Scalable Video-to-Speech Synthesis](2205.02058.md)
**Rodrigo Mira, Alexandros Haliassos, Stavros Petridis, Björn W. Schuller et al.** · 2022-05-04

<details>
<summary>Abstract</summary>

Video-to-speech synthesis (also known as lip-to-speech) refers to the translation of silent lip movements into the corresponding audio. This task has received an increasing amount of attention due to its self-supervised nature (i.e., can be trained without manual labelling) combined with the ever-growing collection of audio-visual data available online. Despite these strong motivations, contemporary video-to-speech works focus mainly on small- to medium-sized corpora with substantial constraints in both vocabulary and setting. In this work, we introduce a scalable video-to-speech framework consisting of two components: a video-to-spectrogram predictor and a pre-trained neural vocoder, which converts the mel-frequency spectrograms into waveform audio. We achieve state-of-the art results for GRID and considerably outperform previous approaches on LRW. More importantly, by focusing on spectrogram prediction using a simple feedforward model, we can efficiently and effectively scale our method to very large and unconstrained datasets: To the best of our knowledge, we are the first to show intelligible results on the challenging LRS3 dataset.

</details>

### [Attentive activation function for improving end-to-end spoofing countermeasure systems](2205.01528.md)
**Woo Hyun Kang, Jahangir Alam, Abderrahim Fathan** · 2022-05-03

<details>
<summary>Abstract</summary>

The main objective of the spoofing countermeasure system is to detect the artifacts within the input speech caused by the speech synthesis or voice conversion process. In order to achieve this, we propose to adopt an attentive activation function, more specifically attention rectified linear unit (AReLU) to the end-to-end spoofing countermeasure system. Since the AReLU employs the attention mechanism to boost the contribution of relevant input features while suppressing the irrelevant ones, introducing AReLU can help the countermeasure system to focus on the features related to the artifacts. The proposed framework was experimented on the logical access (LA) task of ASVSpoof2019 dataset, and outperformed the systems using the standard non-learnable activation functions.

</details>

### [How does a spontaneously speaking conversational agent affect user behavior?](2205.00755.md)
**Takahisa Iizuka, Hiroki Mori** · 2022-05-02

<details>
<summary>Abstract</summary>

This study investigated the effect of synthetic voice of conversational agent trained with spontaneous speech on human interactants. Specifically, we hypothesized that humans will exhibit more social responses when interacting with conversational agent that has a synthetic voice built on spontaneous speech. Typically, speech synthesizers are built on a speech corpus where voice professionals read a set of written sentences. The synthesized speech is clear as if a newscaster were reading a news or a voice actor were playing an anime character. However, this is quite different from spontaneous speech we speak in everyday conversation. Recent advances in speech synthesis enabled us to build a speech synthesizer on a spontaneous speech corpus, and to obtain a near conversational synthesized speech with reasonable quality. By making use of these technology, we examined whether humans produce more social responses to a spontaneously speaking conversational agent. We conducted a large-scale conversation experiment with a conversational agent whose utterances were synthesized with the model trained either with spontaneous speech or read speech. The result showed that the subjects who interacted with the agent whose utterances were synthesized from spontaneous speech tended to show shorter response time and a larger number of backchannels. The result of a questionnaire showed that subjects who interacted with the agent whose utterances were synthesized from spontaneous speech tended to rate their conversation with the agent as closer to a human conversation. These results suggest that speech synthesis built on spontaneous speech is essential to realize a conversational agent as a social actor.

</details>

### [Regotron: Regularizing the Tacotron2 architecture via monotonic alignment loss](2204.13437.md)
**Efthymios Georgiou, Kosmas Kritsis, Georgios Paraskevopoulos, Athanasios Katsamanis et al.** · 2022-04-28

<details>
<summary>Abstract</summary>

Recent deep learning Text-to-Speech (TTS) systems have achieved impressive performance by generating speech close to human parity. However, they suffer from training stability issues as well as incorrect alignment of the intermediate acoustic representation with the input text sequence. In this work, we introduce Regotron, a regularized version of Tacotron2 which aims to alleviate the training issues and at the same time produce monotonic alignments. Our method augments the vanilla Tacotron2 objective function with an additional term, which penalizes non-monotonic alignments in the location-sensitive attention mechanism. By properly adjusting this regularization term we show that the loss curves become smoother, and at the same time Regotron consistently produces monotonic alignments in unseen examples even at an early stage (13\% of the total number of epochs) of its training process, whereas the fully converged Tacotron2 fails to do so. Moreover, our proposed regularization method has no additional computational overhead, while reducing common TTS mistakes and achieving slighlty improved speech naturalness according to subjective mean opinion scores (MOS) collected from 50 evaluators.

</details>

### [SyntaSpeech: Syntax-Aware Generative Adversarial Text-to-Speech](2204.11792.md)
**Zhenhui Ye et.al.** · 2022-04-25

### [Improving Self-Supervised Learning-based MOS Prediction Networks](2204.11030.md)
**Bálint Gyires-Tóth, Csaba Zainkó** · 2022-04-23

<details>
<summary>Abstract</summary>

MOS (Mean Opinion Score) is a subjective method used for the evaluation of a system's quality. Telecommunications (for voice and video), and speech synthesis systems (for generated speech) are a few of the many applications of the method. While MOS tests are widely accepted, they are time-consuming and costly since human input is required. In addition, since the systems and subjects of the tests differ, the results are not really comparable. On the other hand, a large number of previous tests allow us to train machine learning models that are capable of predicting MOS value. By automatically predicting MOS values, both the aforementioned issues can be resolved. The present work introduces data-, training- and post-training specific improvements to a previous self-supervised learning-based MOS prediction model. We used a wav2vec 2.0 model pre-trained on LibriSpeech, extended with LSTM and non-linear dense layers. We introduced transfer learning, target data preprocessing a two- and three-phase training method with different batch formulations, dropout accumulation (for larger batch sizes) and quantization of the predictions. The methods are evaluated using the shared synthetic speech dataset of the first Voice MOS challenge.

</details>

### [LibriS2S: A German-English Speech-to-Speech Translation Corpus](2204.10593.md)
**Pedro Jeuris et.al.** · 2022-04-22

### [Speaking-Rate-Controllable HiFi-GAN Using Feature Interpolation](2204.10561.md)
**Detai Xin, Shinnosuke Takamichi, Takuma Okamoto, Hisashi Kawai et al.** · 2022-04-22

<details>
<summary>Abstract</summary>

This paper presents a speaking-rate-controllable HiFi-GAN neural vocoder. Original HiFi-GAN is a high-fidelity, computationally efficient, and tiny-footprint neural vocoder. We attempt to incorporate a speaking rate control function into HiFi-GAN for improving the accessibility of synthetic speech. The proposed method inserts a differentiable interpolation layer into the HiFi-GAN architecture. A signal resampling method and an image scaling method are implemented in the proposed method to warp the mel-spectrograms or hidden features of the neural vocoder. We also design and open-source a Japanese speech corpus containing three kinds of speaking rates to evaluate the proposed speaking rate control method. Experimental results of comprehensive objective and subjective evaluations demonstrate that 1) the proposed method outperforms a baseline time-scale modification algorithm in speech naturalness, 2) warping mel-spectrograms by image scaling obtained the best performance among all proposed methods, and 3) the proposed speaking rate control method can be incorporated into HiFi-GAN without losing computational efficiency.

</details>

### [FastDiff: A Fast Conditional Diffusion Model for High-Quality Speech Synthesis](2204.09934.md)
**Rongjie Huang et.al.** · 2022-04-21

### [Cross-Speaker Emotion Transfer for Low-Resource Text-to-Speech Using Non-Parallel Voice Conversion with Pitch-Shift Data Augmentation](2204.10020.md)
**Ryo Terashima, Ryuichi Yamamoto, Eunwoo Song, Yuma Shirahata et al.** · 2022-04-21

<details>
<summary>Abstract</summary>

Data augmentation via voice conversion (VC) has been successfully applied to low-resource expressive text-to-speech (TTS) when only neutral data for the target speaker are available. Although the quality of VC is crucial for this approach, it is challenging to learn a stable VC model because the amount of data is limited in low-resource scenarios, and highly expressive speech has large acoustic variety. To address this issue, we propose a novel data augmentation method that combines pitch-shifting and VC techniques. Because pitch-shift data augmentation enables the coverage of a variety of pitch dynamics, it greatly stabilizes training for both VC and TTS models, even when only 1,000 utterances of the target speaker's neutral data are available. Subjective test results showed that a FastSpeech 2-based emotional TTS system with the proposed method improved naturalness and emotional similarity compared with conventional methods.

</details>

### [Audio Deep Fake Detection System with Neural Stitching for ADD 2022](2204.08720.md)
**Rui Yan, Cheng Wen, Shuran Zhou, Tingwei Guo et al.** · 2022-04-19

<details>
<summary>Abstract</summary>

This paper describes our best system and methodology for ADD 2022: The First Audio Deep Synthesis Detection Challenge\cite{Yi2022ADD}. The very same system was used for both two rounds of evaluation in Track 3.2 with a similar training methodology. The first round of Track 3.2 data is generated from Text-to-Speech(TTS) or voice conversion (VC) algorithms, while the second round of data consists of generated fake audio from other participants in Track 3.1, aiming to spoof our systems. Our systems use a standard 34-layer ResNet, with multi-head attention pooling \cite{india2019self} to learn the discriminative embedding for fake audio and spoof detection. We further utilize neural stitching to boost the model's generalization capability in order to perform equally well in different tasks, and more details will be explained in the following sessions. The experiments show that our proposed method outperforms all other systems with a 10.1% equal error rate(EER) in Track 3.2.

</details>

### [Applying Feature Underspecified Lexicon Phonological Features in Multilingual Text-to-Speech](2204.07228.md)
**Cong Zhang, Huinan Zeng, Huang Liu, Jiewen Zheng** · 2022-04-14

<details>
<summary>Abstract</summary>

This study investigates whether the phonological features derived from the Featurally Underspecified Lexicon model can be applied in text-to-speech systems to generate native and non-native speech in English and Mandarin. We present a mapping of ARPABET/pinyin to SAMPA/SAMPA-SC and then to phonological features. This mapping was tested for whether it could lead to the successful generation of native, non-native, and code-switched speech in the two languages. We ran two experiments, one with a small dataset and one with a larger dataset. The results supported that phonological features could be used as a feasible input system for languages in or not in the train data, although further investigation is needed to improve model performance. The results lend support to FUL by presenting successfully synthesised output, and by having the output carrying a source-language accent when synthesising a language not in the training data. The TTS process stimulated human second language acquisition process and thus also confirm FUL's ability to account for acquisition.

</details>

### [Enhancement of Pitch Controllability using Timbre-Preserving Pitch Augmentation in FastPitch](2204.05753.md)
**Hanbin Bae, Young-Sun Joo** · 2022-04-12

<details>
<summary>Abstract</summary>

The recently developed pitch-controllable text-to-speech (TTS) model, i.e. FastPitch, was conditioned for the pitch contours. However, the quality of the synthesized speech degraded considerably for pitch values that deviated significantly from the average pitch; i.e. the ability to control pitch was limited. To address this issue, we propose two algorithms to improve the robustness of FastPitch. First, we propose a novel timbre-preserving pitch-shifting algorithm for natural pitch augmentation. Pitch-shifted speech samples sound more natural when using the proposed algorithm because the speaker's vocal timbre is maintained. Moreover, we propose a training algorithm that defines FastPitch using pitch-augmented speech datasets with different pitch ranges for the same sentence. The experimental results demonstrate that the proposed algorithms improve the pitch controllability of FastPitch.

</details>

### [A Post Auto-regressive GAN Vocoder Focused on Spectrum Fracture](2204.06086.md)
**Zhenxing Lu, Mengnan He, Ruixiong Zhang, Caixia Gong** · 2022-04-12

<details>
<summary>Abstract</summary>

Generative adversarial networks (GANs) have been indicated their superiority in usage of the real-time speech synthesis. Nevertheless, most of them make use of deep convolutional layers as their backbone, which may cause the absence of previous signal information. However, the generation of speech signals invariably require preceding waveform samples in its reconstruction, as the lack of this can lead to artifacts in generated speech. To address this conflict, in this paper, we propose an improved model: a post auto-regressive (AR) GAN vocoder with a self-attention layer, which merging self-attention in an AR loop. It will not participate in inference, but can assist the generator to learn temporal dependencies within frames in training. Furthermore, an ablation study was done to confirm the contribution of each part. Systematic experiments show that our model leads to a consistent improvement on both objective and subjective evaluation performance.

</details>

### [VoiceFixer: A Unified Framework for High-Fidelity Speech Restoration](2204.05841.md)
**Haohe Liu, Xubo Liu, Qiuqiang Kong, Qiao Tian et al.** · 2022-04-12

<details>
<summary>Abstract</summary>

Speech restoration aims to remove distortions in speech signals. Prior methods mainly focus on a single type of distortion, such as speech denoising or dereverberation. However, speech signals can be degraded by several different distortions simultaneously in the real world. It is thus important to extend speech restoration models to deal with multiple distortions. In this paper, we introduce VoiceFixer, a unified framework for high-fidelity speech restoration. VoiceFixer restores speech from multiple distortions (e.g., noise, reverberation, and clipping) and can expand degraded speech (e.g., noisy speech) with a low bandwidth to 44.1 kHz full-bandwidth high-fidelity speech. We design VoiceFixer based on (1) an analysis stage that predicts intermediate-level features from the degraded speech, and (2) a synthesis stage that generates waveform using a neural vocoder. Both objective and subjective evaluations show that VoiceFixer is effective on severely degraded speech, such as real-world historical speech recordings. Samples of VoiceFixer are available at https://haoheliu.github.io/voicefixer.

</details>

### [Fine-grained Noise Control for Multispeaker Speech Synthesis](2204.05070.md)
**Karolos Nikitaras, Georgios Vamvoukakis, Nikolaos Ellinas, Konstantinos Klapsas et al.** · 2022-04-11

<details>
<summary>Abstract</summary>

A text-to-speech (TTS) model typically factorizes speech attributes such as content, speaker and prosody into disentangled representations.Recent works aim to additionally model the acoustic conditions explicitly, in order to disentangle the primary speech factors, i.e. linguistic content, prosody and timbre from any residual factors, such as recording conditions and background noise.This paper proposes unsupervised, interpretable and fine-grained noise and prosody modeling. We incorporate adversarial training, representation bottleneck and utterance-to-frame modeling in order to learn frame-level noise representations. To the same end, we perform fine-grained prosody modeling via a Fully Hierarchical Variational AutoEncoder (FVAE) which additionally results in more expressive speech synthesis.

</details>

### [Enhanced exemplar autoencoder with cycle consistency loss in any-to-one voice conversion](2204.03847.md)
**Weida Liang, Lantian Li, Wenqiang Du, Dong Wang** · 2022-04-08

<details>
<summary>Abstract</summary>

Recent research showed that an autoencoder trained with speech of a single speaker, called exemplar autoencoder (eAE), can be used for any-to-one voice conversion (VC). Compared to large-scale many-to-many models such as AutoVC, the eAE model is easy and fast in training, and may recover more details of the target speaker. To ensure VC quality, the latent code should represent and only represent content information. However, this is not easy to attain for eAE as it is unaware of any speaker variation in model training. To tackle the problem, we propose a simple yet effective approach based on a cycle consistency loss. Specifically, we train eAEs of multiple speakers with a shared encoder, and meanwhile encourage the speech reconstructed from any speaker-specific decoder to get a consistent latent code as the original speech when cycled back and encoded again. Experiments conducted on the AISHELL-3 corpus showed that this new approach improved the baseline eAE consistently. The source code and examples are available at the project page: http://project.cslt.org/.

</details>

### [Unsupervised Quantized Prosody Representation for Controllable Speech Synthesis](2204.03238.md)
**Yutian Wang et.al.** · 2022-04-07

### [Self-supervised learning for robust voice cloning](2204.03421.md)
**Konstantinos Klapsas, Nikolaos Ellinas, Karolos Nikitaras, Georgios Vamvoukakis et al.** · 2022-04-07

<details>
<summary>Abstract</summary>

Voice cloning is a difficult task which requires robust and informative features incorporated in a high quality TTS system in order to effectively copy an unseen speaker's voice. In our work, we utilize features learned in a self-supervised framework via the Bootstrap Your Own Latent (BYOL) method, which is shown to produce high quality speech representations when specific audio augmentations are applied to the vanilla algorithm. We further extend the augmentations in the training procedure to aid the resulting features to capture the speaker identity and to make them robust to noise and acoustic conditions. The learned features are used as pre-trained utterance-level embeddings and as inputs to a Non-Attentive Tacotron based architecture, aiming to achieve multispeaker speech synthesis without utilizing additional speaker features. This method enables us to train our model in an unlabeled multispeaker dataset as well as use unseen speaker embeddings to copy a speaker's voice. Subjective and objective evaluations are used to validate the proposed model, as well as the robustness to the acoustic conditions of the target utterance.

</details>

### [DDOS: A MOS Prediction Framework utilizing Domain Adaptive Pre-training and Distribution of Opinion Scores](2204.03219.md)
**Wei-Cheng Tseng, Wei-Tsung Kao, Hung-yi Lee** · 2022-04-07

<details>
<summary>Abstract</summary>

Mean opinion score (MOS) is a typical subjective evaluation metric for speech synthesis systems. Since collecting MOS is time-consuming, it would be desirable if there are accurate MOS prediction models for automatic evaluation. In this work, we propose DDOS, a novel MOS prediction model. DDOS utilizes domain adaptive pre-training to further pre-train self-supervised learning models on synthetic speech. And a proposed module is added to model the opinion score distribution of each utterance. With the proposed components, DDOS outperforms previous works on BVCC dataset. And the zero shot transfer result on BC2019 dataset is significantly improved. DDOS also wins second place in Interspeech 2022 VoiceMOS challenge in terms of system-level score.

</details>

### [Towards Multi-Scale Speaking Style Modelling with Hierarchical Context Information for Mandarin Speech Synthesis](2204.02743.md)
**Shun Lei, Yixuan Zhou, Liyang Chen, Jiankun Hu et al.** · 2022-04-06

<details>
<summary>Abstract</summary>

Previous works on expressive speech synthesis focus on modelling the mono-scale style embedding from the current sentence or context, but the multi-scale nature of speaking style in human speech is neglected. In this paper, we propose a multi-scale speaking style modelling method to capture and predict multi-scale speaking style for improving the naturalness and expressiveness of synthetic speech. A multi-scale extractor is proposed to extract speaking style embeddings at three different levels from the ground-truth speech, and explicitly guide the training of a multi-scale style predictor based on hierarchical context information. Both objective and subjective evaluations on a Mandarin audiobooks dataset demonstrate that our proposed method can significantly improve the naturalness and expressiveness of the synthesized speech.

</details>

### [A Comparison of Deep Learning MOS Predictors for Speech Synthesis Quality](2204.02249.md)
**Alessandro Ragano, Emmanouil Benetos, Michael Chinen, Helard B. Martinez et al.** · 2022-04-05

<details>
<summary>Abstract</summary>

Speech synthesis quality prediction has made remarkable progress with the development of supervised and self-supervised learning (SSL) MOS predictors but some aspects related to the data are still unclear and require further study. In this paper, we evaluate several MOS predictors based on wav2vec 2.0 and the NISQA speech quality prediction model to explore the role of the training data, the influence of the system type, and the role of cross-domain features in SSL models. Our evaluation is based on the VoiceMOS challenge dataset. Results show that SSL-based models show the highest correlation and lowest mean squared error compared to supervised models. The key point of this study is that benchmarking the statistical performance of MOS predictors alone is not sufficient to rank models since potential issues hidden in the data could bias the evaluated performances.

</details>

### [UTMOS: UTokyo-SaruLab System for VoiceMOS Challenge 2022](2204.02152.md)
**Takaaki Saeki, Detai Xin, Wataru Nakata, Tomoki Koriyama et al.** · 2022-04-05

<details>
<summary>Abstract</summary>

We present the UTokyo-SaruLab mean opinion score (MOS) prediction system submitted to VoiceMOS Challenge 2022. The challenge is to predict the MOS values of speech samples collected from previous Blizzard Challenges and Voice Conversion Challenges for two tracks: a main track for in-domain prediction and an out-of-domain (OOD) track for which there is less labeled data from different listening tests. Our system is based on ensemble learning of strong and weak learners. Strong learners incorporate several improvements to the previous fine-tuning models of self-supervised learning (SSL) models, while weak learners use basic machine-learning methods to predict scores from SSL features. In the Challenge, our system had the highest score on several metrics for both the main and OOD tracks. In addition, we conducted ablation studies to investigate the effectiveness of our proposed methods.

</details>

### [Lip to Speech Synthesis with Visual Context Attentional GAN](2204.01726.md)
**Minsu Kim, Joanna Hong, Yong Man Ro** · 2022-04-04

<details>
<summary>Abstract</summary>

In this paper, we propose a novel lip-to-speech generative adversarial network, Visual Context Attentional GAN (VCA-GAN), which can jointly model local and global lip movements during speech synthesis. Specifically, the proposed VCA-GAN synthesizes the speech from local lip visual features by finding a mapping function of viseme-to-phoneme, while global visual context is embedded into the intermediate layers of the generator to clarify the ambiguity in the mapping induced by homophene. To achieve this, a visual context attention module is proposed where it encodes global representations from the local visual features, and provides the desired global visual context corresponding to the given coarse speech representation to the generator through audio-visual attention. In addition to the explicit modelling of local and global visual representations, synchronization learning is introduced as a form of contrastive learning that guides the generator to synthesize a speech in sync with the given input lip movements. Extensive experiments demonstrate that the proposed VCA-GAN outperforms existing state-of-the-art and is able to effectively synthesize the speech from multi-speaker that has been barely handled in the previous works.

</details>

### [On incorporating social speaker characteristics in synthetic speech](2204.01115.md)
**Sai Sirisha Rallabandi, Sebastian Möller** · 2022-04-03

<details>
<summary>Abstract</summary>

In our previous work, we derived the acoustic features, that contribute to the perception of warmth and competence in synthetic speech. As an extension, in our current work, we investigate the impact of the derived vocal features in the generation of the desired characteristics. The acoustic features, spectral flux, F1 mean and F2 mean and their convex combinations were explored for the generation of higher warmth in female speech. The voiced slope, spectral flux, and their convex combinations were investigated for the generation of higher competence in female speech. We have employed a feature quantization approach in the traditional end-to-end tacotron based speech synthesis model. The listening tests have shown that the convex combination of acoustic features displays higher Mean Opinion Scores of warmth and competence when compared to that of individual features.

</details>

### [AdaSpeech 4: Adaptive Text to Speech in Zero-Shot Scenarios](2204.00436.md)
**Yihan Wu et.al.** · 2022-04-01

### [Residual-guided Personalized Speech Synthesis based on Face Image](2204.01672.md)
**Jianrong Wang, Zixuan Wang, Xiaosheng Hu, Xuewei Li et al.** · 2022-04-01

<details>
<summary>Abstract</summary>

Previous works derive personalized speech features by training the model on a large dataset composed of his/her audio sounds. It was reported that face information has a strong link with the speech sound. Thus in this work, we innovatively extract personalized speech features from human faces to synthesize personalized speech using neural vocoder. A Face-based Residual Personalized Speech Synthesis Model (FR-PSS) containing a speech encoder, a speech synthesizer and a face encoder is designed for PSS. In this model, by designing two speech priors, a residual-guided strategy is introduced to guide the face feature to approach the true speech feature in the training. Moreover, considering the error of feature's absolute values and their directional bias, we formulate a novel tri-item loss function for face encoder. Experimental results show that the speech synthesized by our model is comparable to the personalized speech synthesized by training a large amount of audio data in previous works.

</details>

### [Universal Adaptor: Converting Mel-Spectrograms Between Different Configurations for Speech Synthesis](2204.00170.md)
**Fan-Lin Wang, Po-chun Hsu, Da-rong Liu, Hung-yi Lee** · 2022-04-01

<details>
<summary>Abstract</summary>

Most recent speech synthesis systems are composed of a synthesizer and a vocoder. However, the existing synthesizers and vocoders can only be matched to acoustic features extracted with a specific configuration. Hence, we can't combine arbitrary synthesizers and vocoders together to form a complete system, not to mention apply to a newly developed model. In this paper, we proposed Universal Adaptor, which takes a Mel-spectrogram parametrized by the source configuration and converts it into a Mel-spectrogram parametrized by the target configuration, as long as we feed in the source and the target configurations. Experiments show that the quality of speeches synthesized from our output of Universal Adaptor is comparable to those synthesized from ground truth Mel-spectrogram no matter in single-speaker or multi-speaker scenarios. Moreover, Universal Adaptor can be applied in the recent TTS systems and voice conversion systems without dropping quality.

</details>

### [An End-to-end Chinese Text Normalization Model based on Rule-guided Flat-Lattice Transformer](2203.16954.md)
**Wenlin Dai, Changhe Song, Xiang Li, Zhiyong Wu et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

Text normalization, defined as a procedure transforming non standard words to spoken-form words, is crucial to the intelligibility of synthesized speech in text-to-speech system. Rule-based methods without considering context can not eliminate ambiguation, whereas sequence-to-sequence neural network based methods suffer from the unexpected and uninterpretable errors problem. Recently proposed hybrid system treats rule-based model and neural model as two cascaded sub-modules, where limited interaction capability makes neural network model cannot fully utilize expert knowledge contained in the rules. Inspired by Flat-LAttice Transformer (FLAT), we propose an end-to-end Chinese text normalization model, which accepts Chinese characters as direct input and integrates expert knowledge contained in rules into the neural network, both contribute to the superior performance of proposed model for the text normalization task. We also release a first publicly accessible largescale dataset for Chinese text normalization. Our proposed model has achieved excellent results on this dataset.

</details>

### [A Character-level Span-based Model for Mandarin Prosodic Structure Prediction](2203.16922.md)
**Xueyuan Chen, Changhe Song, Yixuan Zhou, Zhiyong Wu et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

The accuracy of prosodic structure prediction is crucial to the naturalness of synthesized speech in Mandarin text-to-speech system, but now is limited by widely-used sequence-to-sequence framework and error accumulation from previous word segmentation results. In this paper, we propose a span-based Mandarin prosodic structure prediction model to obtain an optimal prosodic structure tree, which can be converted to corresponding prosodic label sequence. Instead of the prerequisite for word segmentation, rich linguistic features are provided by Chinese character-level BERT and sent to encoder with self-attention architecture. On top of this, span representation and label scoring are used to describe all possible prosodic structure trees, of which each tree has its corresponding score. To find the optimal tree with the highest score for a given sentence, a bottom-up CKY-style algorithm is further used. The proposed method can predict prosodic labels of different levels at the same time and accomplish the process directly from Chinese characters in an end-to-end manner. Experiment results on two real-world datasets demonstrate the excellent performance of our span-based method over all sequence-to-sequence baseline approaches.

</details>

### [SpecGrad: Diffusion Probabilistic Model based Neural Vocoder with Adaptive Noise Spectral Shaping](2203.16749.md)
**Yuma Koizumi, Heiga Zen, Kohei Yatabe, Nanxin Chen et al.** · 2022-03-31

<details>
<summary>Abstract</summary>

Neural vocoder using denoising diffusion probabilistic model (DDPM) has been improved by adaptation of the diffusion noise distribution to given acoustic features. In this study, we propose SpecGrad that adapts the diffusion noise so that its time-varying spectral envelope becomes close to the conditioning log-mel spectrogram. This adaptation by time-varying filtering improves the sound quality especially in the high-frequency bands. It is processed in the time-frequency domain to keep the computational cost almost the same as the conventional DDPM-based neural vocoders. Experimental results showed that SpecGrad generates higher-fidelity speech waveform than conventional DDPM-based neural vocoders in both analysis-synthesis and speech enhancement scenarios. Audio demos are available at wavegrad.github.io/specgrad/.

</details>

### [Efficient Non-Autoregressive GAN Voice Conversion using VQWav2vec Features and Dynamic Convolution](2203.17172.md)
**Mingjie Chen, Yanghao Zhou, Heyan Huang, Thomas Hain** · 2022-03-31

<details>
<summary>Abstract</summary>

It was shown recently that a combination of ASR and TTS models yield highly competitive performance on standard voice conversion tasks such as the Voice Conversion Challenge 2020 (VCC2020). To obtain good performance both models require pretraining on large amounts of data, thereby obtaining large models that are potentially inefficient in use. In this work we present a model that is significantly smaller and thereby faster in processing while obtaining equivalent performance. To achieve this the proposed model, Dynamic-GAN-VC (DYGAN-VC), uses a non-autoregressive structure and makes use of vector quantised embeddings obtained from a VQWav2vec model. Furthermore dynamic convolution is introduced to improve speech content modeling while requiring a small number of parameters. Objective and subjective evaluation was performed using the VCC2020 task, yielding MOS scores of up to 3.86, and character error rates as low as 4.3\%. This was achieved with approximately half the number of model parameters, and up to 8 times faster decoding speed.

</details>

### [Does Audio Deepfake Detection Generalize?](2203.16263.md)
**Nicolas M. Müller, Pavel Czempin, Franziska Dieckmann, Adam Froghyar et al.** · 2022-03-30

<details>
<summary>Abstract</summary>

Current text-to-speech algorithms produce realistic fakes of human voices, making deepfake detection a much-needed area of research. While researchers have presented various techniques for detecting audio spoofs, it is often unclear exactly why these architectures are successful: Preprocessing steps, hyperparameter settings, and the degree of fine-tuning are not consistent across related work. Which factors contribute to success, and which are accidental? In this work, we address this problem: We systematize audio spoofing detection by re-implementing and uniformly evaluating architectures from related work. We identify overarching features for successful audio deepfake detection, such as using cqtspec or logspec features instead of melspec features, which improves performance by 37% EER on average, all other factors constant. Additionally, we evaluate generalization capabilities: We collect and publish a new dataset consisting of 37.9 hours of found audio recordings of celebrities and politicians, of which 17.2 hours are deepfakes. We find that related work performs poorly on such real-world data (performance degradation of up to one thousand percent). This may suggest that the community has tailored its solutions too closely to the prevailing ASVSpoof benchmark and that deepfakes are much harder to detect outside the lab than previously thought.

</details>

### [End to End Lip Synchronization with a Temporal AutoEncoder](2203.16224.md)
**Yoav Shalev, Lior Wolf** · 2022-03-30

<details>
<summary>Abstract</summary>

We study the problem of syncing the lip movement in a video with the audio stream. Our solution finds an optimal alignment using a dual-domain recurrent neural network that is trained on synthetic data we generate by dropping and duplicating video frames. Once the alignment is found, we modify the video in order to sync the two sources. Our method is shown to greatly outperform the literature methods on a variety of existing and new benchmarks. As an application, we demonstrate our ability to robustly align text-to-speech generated audio with an existing video stream. Our code and samples are available at https://github.com/itsyoavshalev/End-to-End-Lip-Synchronization-with-a-Temporal-AutoEncoder.

</details>

### [Enhancing Zero-Shot Many to Many Voice Conversion with Self-Attention VAE](2203.16037.md)
**Ziang Long, Yunling Zheng, Meng Yu, Jack Xin** · 2022-03-30

<details>
<summary>Abstract</summary>

Variational auto-encoder (VAE) is an effective neural network architecture to disentangle a speech utterance into speaker identity and linguistic content latent embeddings, then generate an utterance for a target speaker from that of a source speaker. This is possible by concatenating the identity embedding of the target speaker and the content embedding of the source speaker uttering a desired sentence. In this work, we propose to improve VAE models with self-attention and structural regularization (RGSM). Specifically, we found a suitable location of VAE's decoder to add a self-attention layer for incorporating non-local information in generating a converted utterance and hiding the source speaker's identity. We applied relaxed group-wise splitting method (RGSM) to regularize network weights and remarkably enhance generalization performance. In experiments of zero-shot many-to-many voice conversion task on VCTK data set, with the self-attention layer and relaxed group-wise splitting method, our model achieves a gain of speaker classification accuracy on unseen speakers by 28.3\% while slightly improved conversion voice quality in terms of MOSNet scores. Our encouraging findings point to future research on integrating more variety of attention structures in VAE framework while controlling model size and overfitting for advancing zero-shot many-to-many voice conversions.

</details>

### [Applying Syntax$\unicode{x2013}$Prosody Mapping Hypothesis and Prosodic Well-Formedness Constraints to Neural Sequence-to-Sequence Speech Synthesis](2203.15276.md)
**Kei Furukawa, Takeshi Kishiyama, Satoshi Nakamura** · 2022-03-29

<details>
<summary>Abstract</summary>

End-to-end text-to-speech synthesis (TTS), which generates speech sounds directly from strings of texts or phonemes, has improved the quality of speech synthesis over the conventional TTS. However, most previous studies have been evaluated based on subjective naturalness and have not objectively examined whether they can reproduce pitch patterns of phonological phenomena such as downstep, rhythmic boost, and initial lowering that reflect syntactic structures in Japanese. These phenomena can be linguistically explained by phonological constraints and the syntax$\unicode{x2013}$prosody mapping hypothesis (SPMH), which assumes projections from syntactic structures to phonological hierarchy. Although some experiments in psycholinguistics have verified the validity of the SPMH, it is crucial to investigate whether it can be implemented in TTS. To synthesize linguistic phenomena involving syntactic or phonological constraints, we propose a model using phonological symbols based on the SPMH and prosodic well-formedness constraints. Experimental results showed that the proposed method synthesized similar pitch patterns to those reported in linguistics experiments for the phenomena of initial lowering and rhythmic boost. The proposed model efficiently synthesizes phonological phenomena in the test data that were not explicitly included in the training data.

</details>

### [An Overview & Analysis of Sequence-to-Sequence Emotional Voice Conversion](2203.15873.md)
**Zijiang Yang, Xin Jing, Andreas Triantafyllopoulos, Meishu Song et al.** · 2022-03-29

<details>
<summary>Abstract</summary>

Emotional voice conversion (EVC) focuses on converting a speech utterance from a source to a target emotion; it can thus be a key enabling technology for human-computer interaction applications and beyond. However, EVC remains an unsolved research problem with several challenges. In particular, as speech rate and rhythm are two key factors of emotional conversion, models have to generate output sequences of differing length. Sequence-to-sequence modelling is recently emerging as a competitive paradigm for models that can overcome those challenges. In an attempt to stimulate further research in this promising new direction, recent sequence-to-sequence EVC papers were systematically investigated and reviewed from six perspectives: their motivation, training strategies, model architectures, datasets, model inputs, and evaluation methods. This information is organised to provide the research community with an easily digestible overview of the current state-of-the-art. Finally, we discuss existing challenges of sequence-to-sequence EVC.

</details>

### [A Sparsity-promoting Dictionary Model for Variational Autoencoders](2203.15758.md)
**Mostafa Sadeghi, Paul Magron** · 2022-03-29

<details>
<summary>Abstract</summary>

Structuring the latent space in probabilistic deep generative models, e.g., variational autoencoders (VAEs), is important to yield more expressive models and interpretable representations, and to avoid overfitting. One way to achieve this objective is to impose a sparsity constraint on the latent variables, e.g., via a Laplace prior. However, such approaches usually complicate the training phase, and they sacrifice the reconstruction quality to promote sparsity. In this paper, we propose a simple yet effective methodology to structure the latent space via a sparsity-promoting dictionary model, which assumes that each latent code can be written as a sparse linear combination of a dictionary's columns. In particular, we leverage a computationally efficient and tuning-free method, which relies on a zero-mean Gaussian latent prior with learnable variances. We derive a variational inference scheme to train the model. Experiments on speech generative modeling demonstrate the advantage of the proposed approach over competing techniques, since it promotes sparsity while not deteriorating the output speech quality.

</details>

### [STUDIES: Corpus of Japanese Empathetic Dialogue Speech Towards Friendly Voice Agent](2203.14757.md)
**Yuki Saito, Yuto Nishimura, Shinnosuke Takamichi, Kentaro Tachibana et al.** · 2022-03-28

<details>
<summary>Abstract</summary>

We present STUDIES, a new speech corpus for developing a voice agent that can speak in a friendly manner. Humans naturally control their speech prosody to empathize with each other. By incorporating this "empathetic dialogue" behavior into a spoken dialogue system, we can develop a voice agent that can respond to a user more naturally. We designed the STUDIES corpus to include a speaker who speaks with empathy for the interlocutor's emotion explicitly. We describe our methodology to construct an empathetic dialogue speech corpus and report the analysis results of the STUDIES corpus. We conducted a text-to-speech experiment to initially investigate how we can develop more natural voice agent that can tune its speaking style corresponding to the interlocutor's emotion. The results show that the use of interlocutor's emotion label and conversational context embedding can produce speech with the same degree of naturalness as that synthesized by using the agent's emotion label. Our project page of the STUDIES corpus is http://sython.org/Corpus/STUDIES.

</details>

### [vTTS: visual-text to speech](2203.14725.md)
**Yoshifumi Nakano, Takaaki Saeki, Shinnosuke Takamichi, Katsuhito Sudoh et al.** · 2022-03-28

<details>
<summary>Abstract</summary>

This paper proposes visual-text to speech (vTTS), a method for synthesizing speech from visual text (i.e., text as an image). Conventional TTS converts phonemes or characters into discrete symbols and synthesizes a speech waveform from them, thus losing the visual features that the characters essentially have. Therefore, our method synthesizes speech not from discrete symbols but from visual text. The proposed vTTS extracts visual features with a convolutional neural network and then generates acoustic features with a non-autoregressive model inspired by FastSpeech2. Experimental results show that 1) vTTS is capable of generating speech with naturalness comparable to or better than a conventional TTS, 2) it can transfer emphasis and emotion attributes in visual text to speech without additional labels and architectures, and 3) it can synthesize more natural and intelligible speech from unseen and rare characters than conventional TTS.

</details>

### [Analysis of Voice Conversion and Code-Switching Synthesis Using VQ-VAE](2203.14640.md)
**Shuvayanti Das, Jennifer Williams, Catherine Lai** · 2022-03-28

<details>
<summary>Abstract</summary>

This paper presents an analysis of speech synthesis quality achieved by simultaneously performing voice conversion and language code-switching using multilingual VQ-VAE speech synthesis in German, French, English and Italian. In this paper, we utilize VQ code indices representing phone information from VQ-VAE to perform code-switching and a VQ speaker code to perform voice conversion in a single system with a neural vocoder. Our analysis examines several aspects of code-switching including the number of language switches and the number of words involved in each switch. We found that speech synthesis quality degrades after increasing the number of language switches within an utterance and decreasing the number of words. We also found some evidence of accent transfer when performing voice conversion across languages as observed when a speaker's original language differs from the language of a synthetic target utterance. We present results from our listening tests and discuss the inherent difficulties of assessing accent transfer in speech synthesis. Our work highlights some of the limitations and strengths of using a semi-supervised end-to-end system like VQ-VAE for handling multilingual synthesis. Our work provides insight into why multilingual speech synthesis is challenging and we suggest some directions for expanding work in this area.

</details>

### [Neural Vocoder is All You Need for Speech Super-resolution](2203.14941.md)
**Haohe Liu, Woosung Choi, Xubo Liu, Qiuqiang Kong et al.** · 2022-03-28

<details>
<summary>Abstract</summary>

Speech super-resolution (SR) is a task to increase speech sampling rate by generating high-frequency components. Existing speech SR methods are trained in constrained experimental settings, such as a fixed upsampling ratio. These strong constraints can potentially lead to poor generalization ability in mismatched real-world cases. In this paper, we propose a neural vocoder based speech super-resolution method (NVSR) that can handle a variety of input resolution and upsampling ratios. NVSR consists of a mel-bandwidth extension module, a neural vocoder module, and a post-processing module. Our proposed system achieves state-of-the-art results on the VCTK multi-speaker benchmark. On 44.1 kHz target resolution, NVSR outperforms WSRGlow and Nu-wave by 8% and 37% respectively on log spectral distance and achieves a significantly better perceptual quality. We also demonstrate that prior knowledge in the pre-trained vocoder is crucial for speech SR by performing mel-bandwidth extension with a simple replication-padding method. Samples can be found in https://haoheliu.github.io/nvsr.

</details>

### [Bunched LPCNet2: Efficient Neural Vocoders Covering Devices from Cloud to Edge](2203.14416.md)
**Sangjun Park, Kihyun Choo, Joohyung Lee, Anton V. Porov et al.** · 2022-03-27

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) services that run on edge devices have many advantages compared to cloud TTS, e.g., latency and privacy issues. However, neural vocoders with a low complexity and small model footprint inevitably generate annoying sounds. This study proposes a Bunched LPCNet2, an improved LPCNet architecture that provides highly efficient performance in high-quality for cloud servers and in a low-complexity for low-resource edge devices. Single logistic distribution achieves computational efficiency, and insightful tricks reduce the model footprint while maintaining speech quality. A DualRate architecture, which generates a lower sampling rate from a prosody model, is also proposed to reduce maintenance costs. The experiments demonstrate that Bunched LPCNet2 generates satisfactory speech quality with a model footprint of 1.1MB while operating faster than real-time on a RPi 3B. Our audio samples are available at https://srtts.github.io/bunchedLPCNet2.

</details>

### [A Neural Vocoder Based Packet Loss Concealment Algorithm](2203.14010.md)
**Yao Zhou, Changchun Bao** · 2022-03-26

<details>
<summary>Abstract</summary>

The packet loss problem seriously affects the quality of service in Voice over IP (VoIP) sceneries. In this paper, we investigated online receiver-based packet loss concealment which is much more portable and applicable. For ensuring the speech naturalness, rather than directly processing time-domain waveforms or separately reconstructing amplitudes and phases in frequency domain, a flow-based neural vocoder is adopted to generate the substitution waveform of lost packet from Mel-spectrogram which is generated from history contents by a well-designed neural predictor. Furthermore, a waveform similarity-based smoothing post-process is created to mitigate the discontinuity of speech and avoid the artifacts. The experimental results show the outstanding performance of the proposed method.

</details>

### [SpeechSplit 2.0: Unsupervised speech disentanglement for voice conversion Without tuning autoencoder Bottlenecks](2203.14156.md)
**Chak Ho Chan, Kaizhi Qian, Yang Zhang, Mark Hasegawa-Johnson** · 2022-03-26

<details>
<summary>Abstract</summary>

SpeechSplit can perform aspect-specific voice conversion by disentangling speech into content, rhythm, pitch, and timbre using multiple autoencoders in an unsupervised manner. However, SpeechSplit requires careful tuning of the autoencoder bottlenecks, which can be time-consuming and less robust. This paper proposes SpeechSplit 2.0, which constrains the information flow of the speech component to be disentangled on the autoencoder input using efficient signal processing methods instead of bottleneck tuning. Evaluation results show that SpeechSplit 2.0 achieves comparable performance to SpeechSplit in speech disentanglement and superior robustness to the bottleneck size variations. Our code is available at https://github.com/biggytruck/SpeechSplit2.

</details>

### [BDDM: Bilateral Denoising Diffusion Models for Fast and High-Quality Speech Synthesis](2203.13508.md)
**Max W. Y. Lam, Jun Wang, Dan Su, Dong Yu** · 2022-03-25

<details>
<summary>Abstract</summary>

Diffusion probabilistic models (DPMs) and their extensions have emerged as competitive generative models yet confront challenges of efficient sampling. We propose a new bilateral denoising diffusion model (BDDM) that parameterizes both the forward and reverse processes with a schedule network and a score network, which can train with a novel bilateral modeling objective. We show that the new surrogate objective can achieve a lower bound of the log marginal likelihood tighter than a conventional surrogate. We also find that BDDM allows inheriting pre-trained score network parameters from any DPMs and consequently enables speedy and stable learning of the schedule network and optimization of a noise schedule for sampling. Our experiments demonstrate that BDDMs can generate high-fidelity audio samples with as few as three sampling steps. Moreover, compared to other state-of-the-art diffusion-based neural vocoders, BDDMs produce comparable or higher quality samples indistinguishable from human speech, notably with only seven sampling steps (143x faster than WaveGrad and 28.6x faster than DiffWave). We release our code at https://github.com/tencent-ailab/bddm.

</details>

### [HiFi++: a Unified Framework for Bandwidth Extension and Speech Enhancement](2203.13086.md)
**Pavel Andreev, Aibek Alanov, Oleg Ivanov, Dmitry Vetrov** · 2022-03-24

<details>
<summary>Abstract</summary>

Generative adversarial networks have recently demonstrated outstanding performance in neural vocoding outperforming best autoregressive and flow-based models. In this paper, we show that this success can be extended to other tasks of conditional audio generation. In particular, building upon HiFi vocoders, we propose a novel HiFi++ general framework for bandwidth extension and speech enhancement. We show that with the improved generator architecture, HiFi++ performs better or comparably with the state-of-the-art in these tasks while spending significantly less computational resources. The effectiveness of our approach is validated through a series of extensive experiments.

</details>

### [Towards Expressive Speaking Style Modelling with Hierarchical Context Information for Mandarin Speech Synthesis](2203.12201.md)
**Shun Lei, Yixuan Zhou, Liyang Chen, Zhiyong Wu et al.** · 2022-03-23

<details>
<summary>Abstract</summary>

Previous works on expressive speech synthesis mainly focus on current sentence. The context in adjacent sentences is neglected, resulting in inflexible speaking style for the same text, which lacks speech variations. In this paper, we propose a hierarchical framework to model speaking style from context. A hierarchical context encoder is proposed to explore a wider range of contextual information considering structural relationship in context, including inter-phrase and inter-sentence relations. Moreover, to encourage this encoder to learn style representation better, we introduce a novel training strategy with knowledge distillation, which provides the target for encoder training. Both objective and subjective evaluations on a Mandarin lecture dataset demonstrate that the proposed method can significantly improve the naturalness and expressiveness of the synthesized speech.

</details>

### [The VoiceMOS Challenge 2022](2203.11389.md)
**Wen-Chin Huang, Erica Cooper, Yu Tsao, Hsin-Min Wang et al.** · 2022-03-21

<details>
<summary>Abstract</summary>

We present the first edition of the VoiceMOS Challenge, a scientific event that aims to promote the study of automatic prediction of the mean opinion score (MOS) of synthetic speech. This challenge drew 22 participating teams from academia and industry who tried a variety of approaches to tackle the problem of predicting human ratings of synthesized speech. The listening test data for the main track of the challenge consisted of samples from 187 different text-to-speech and voice conversion systems spanning over a decade of research, and the out-of-domain track consisted of data from more recent systems rated in a separate listening test. Results of the challenge show the effectiveness of fine-tuning self-supervised speech models for the MOS prediction task, as well as the difficulty of predicting MOS ratings for unseen speakers and listeners, and for unseen systems in the out-of-domain setting.

</details>

### [AutoTTS: End-to-End Text-to-Speech Synthesis through Differentiable Duration Modeling](2203.11049.md)
**Bac Nguyen, Fabien Cardinaux, Stefan Uhlich** · 2022-03-21

<details>
<summary>Abstract</summary>

Parallel text-to-speech (TTS) models have recently enabled fast and highly-natural speech synthesis. However, they typically require external alignment models, which are not necessarily optimized for the decoder as they are not jointly trained. In this paper, we propose a differentiable duration method for learning monotonic alignments between input and output sequences. Our method is based on a soft-duration mechanism that optimizes a stochastic process in expectation. Using this differentiable duration method, we introduce AutoTTS, a direct text-to-waveform speech synthesis model. AutoTTS enables high-fidelity speech synthesis through a combination of adversarial training and matching the total ground-truth duration. Experimental results show that our model obtains competitive results while enjoying a much simpler training pipeline. Audio samples are available online.

</details>

### [WeSinger: Data-augmented Singing Voice Synthesis with Auxiliary Losses](2203.10750.md)
**Zewang Zhang, Yibin Zheng, Xinhui Li, Li Lu** · 2022-03-21

<details>
<summary>Abstract</summary>

In this paper, we develop a new multi-singer Chinese neural singing voice synthesis (SVS) system named WeSinger. To improve the accuracy and naturalness of synthesized singing voice, we design several specifical modules and techniques: 1) A deep bi-directional LSTM-based duration model with multi-scale rhythm loss and post-processing step; 2) A Transformer-alike acoustic model with progressive pitch-weighted decoder loss; 3) a 24 kHz pitch-aware LPCNet neural vocoder to produce high-quality singing waveforms; 4) A novel data augmentation method with multi-singer pre-training for stronger robustness and naturalness. To our knowledge, WeSinger is the first SVS system to adopt 24 kHz LPCNet and multi-singer pre-training simultaneously. Both quantitative and qualitative evaluation results demonstrate the effectiveness of WeSinger in terms of accuracy and naturalness, and WeSinger achieves state-of-the-art performance on the recent public Chinese singing corpus Opencpop\footnote{https://wenet.org.cn/opencpop/}. Some synthesized singing samples are available online\footnote{https://zzw922cn.github.io/wesinger/}.

</details>

### [Vocal effort modeling in neural TTS for improving the intelligibility of synthetic speech in noise](2203.10637.md)
**Tuomo Raitio, Petko Petkov, Jiangchuan Li, Muhammed Shifas et al.** · 2022-03-20

<details>
<summary>Abstract</summary>

We present a neural text-to-speech (TTS) method that models natural vocal effort variation to improve the intelligibility of synthetic speech in the presence of noise. The method consists of first measuring the spectral tilt of unlabeled conventional speech data, and then conditioning a neural TTS model with normalized spectral tilt among other prosodic factors. Changing the spectral tilt parameter and keeping other prosodic factors unchanged enables effective vocal effort control at synthesis time independent of other prosodic factors. By extrapolation of the spectral tilt values beyond what has been seen in the original data, we can generate speech with high vocal effort levels, thus improving the intelligibility of speech in the presence of masking noise. We evaluate the intelligibility and quality of normal speech and speech with increased vocal effort in the presence of various masking noise conditions, and compare these to well-known speech intelligibility-enhancing algorithms. The evaluations show that the proposed method can improve the intelligibility of synthetic speech with little loss in speech quality.

</details>

### [Improve few-shot voice cloning using multi-modal learning](2203.09708.md)
**Haitong Zhang, Yue Lin** · 2022-03-18

<details>
<summary>Abstract</summary>

Recently, few-shot voice cloning has achieved a significant improvement. However, most models for few-shot voice cloning are single-modal, and multi-modal few-shot voice cloning has been understudied. In this paper, we propose to use multi-modal learning to improve the few-shot voice cloning performance. Inspired by the recent works on unsupervised speech representation, the proposed multi-modal system is built by extending Tacotron2 with an unsupervised speech representation module. We evaluate our proposed system in two few-shot voice cloning scenarios, namely few-shot text-to-speech(TTS) and voice conversion(VC). Experimental results demonstrate that the proposed multi-modal learning can significantly improve the few-shot voice cloning performance over their counterpart single-modal systems.

</details>

### [AdaVocoder: Adaptive Vocoder for Custom Voice](2203.09825.md)
**Xin Yuan, Yongbing Feng, Mingming Ye, Cheng Tuo et al.** · 2022-03-18

<details>
<summary>Abstract</summary>

Custom voice is to construct a personal speech synthesis system by adapting the source speech synthesis model to the target model through the target few recordings. The solution to constructing a custom voice is to combine an adaptive acoustic model with a robust vocoder. However, training a robust vocoder usually requires a multi-speaker dataset, which should include various age groups and various timbres, so that the trained vocoder can be used for unseen speakers. Collecting such a multi-speaker dataset is difficult, and the dataset distribution always has a mismatch with the distribution of the target speaker dataset. This paper proposes an adaptive vocoder for custom voice from another novel perspective to solve the above problems. The adaptive vocoder mainly uses a cross-domain consistency loss to solve the overfitting problem encountered by the GAN-based neural vocoder in the transfer learning of few-shot scenes. We construct two adaptive vocoders, AdaMelGAN and AdaHiFi-GAN. First, We pre-train the source vocoder model on AISHELL3 and CSMSC datasets, respectively. Then, fine-tune it on the internal dataset VXI-children with few adaptation data. The empirical results show that a high-quality custom voice system can be built by combining a adaptive acoustic model with a adaptive vocoder.

</details>

### [DGC-vector: A new speaker embedding for zero-shot voice conversion](2203.09722.md)
**Ruitong Xiao, Haitong Zhang, Yue Lin** · 2022-03-18

<details>
<summary>Abstract</summary>

Recently, more and more zero-shot voice conversion algorithms have been proposed. As a fundamental part of zero-shot voice conversion, speaker embeddings are the key to improving the converted speech's speaker similarity. In this paper, we study the impact of speaker embeddings on zero-shot voice conversion performance. To better represent the characteristics of the target speaker and improve the speaker similarity in zero-shot voice conversion, we propose a novel speaker representation method in this paper. Our method combines the advantages of D-vector, global style token (GST) based speaker representation and auxiliary supervision. Objective and subjective evaluations show that the proposed method achieves a decent performance on zero-shot voice conversion and significantly improves speaker similarity over D-vector and GST-based speaker embedding.

</details>

### [Robotic Speech Synthesis: Perspectives on Interactions, Scenarios, and Ethics](2203.09599.md)
**Yuanchao Li, Catherine Lai** · 2022-03-17

<details>
<summary>Abstract</summary>

In recent years, many works have investigated the feasibility of conversational robots for performing specific tasks, such as healthcare and interview. Along with this development comes a practical issue: how should we synthesize robotic voices to meet the needs of different situations? In this paper, we discuss this issue from three perspectives: 1) the difficulties of synthesizing non-verbal and interaction-oriented speech signals, particularly backchannels; 2) the scenario classification for robotic voice synthesis; 3) the ethical issues regarding the design of robot voice for its emotion and identity. We present the findings of relevant literature and our prior work, trying to bring the attention of human-robot interaction researchers to design better conversational robots in the future.

</details>

### [Text-free non-parallel many-to-many voice conversion using normalising flows](2203.08009.md)
**Thomas Merritt, Abdelhamid Ezzerg, Piotr Biliński, Magdalena Proszewska et al.** · 2022-03-15

<details>
<summary>Abstract</summary>

Non-parallel voice conversion (VC) is typically achieved using lossy representations of the source speech. However, ensuring only speaker identity information is dropped whilst all other information from the source speech is retained is a large challenge. This is particularly challenging in the scenario where at inference-time we have no knowledge of the text being read, i.e., text-free VC. To mitigate this, we investigate information-preserving VC approaches. Normalising flows have gained attention for text-to-speech synthesis, however have been under-explored for VC. Flows utilize invertible functions to learn the likelihood of the data, thus provide a lossless encoding of speech. We investigate normalising flows for VC in both text-conditioned and text-free scenarios. Furthermore, for text-free VC we compare pre-trained and jointly-learnt priors. Flow-based VC evaluations show no degradation between text-free and text-conditioned VC, resulting in improvements over the state-of-the-art. Also, joint-training of the prior is found to negatively impact text-free VC quality.

</details>

### [Practical cognitive speech compression](2203.04415.md)
**Reza Lotfidereshgi, Philippe Gournay** · 2022-03-08

<details>
<summary>Abstract</summary>

This paper presents a new neural speech compression method that is practical in the sense that it operates at low bitrate, introduces a low latency, is compatible in computational complexity with current mobile devices, and provides a subjective quality that is comparable to that of standard mobile-telephony codecs. Other recently proposed neural vocoders also have the ability to operate at low bitrate. However, they do not produce the same level of subjective quality as standard codecs. On the other hand, standard codecs rely on objective and short-term metrics such as the segmental signal-to-noise ratio that correlate only weakly with perception. Furthermore, standard codecs are less efficient than unsupervised neural networks at capturing speech attributes, especially long-term ones. The proposed method combines a cognitive-coding encoder that extracts an interpretable unsupervised hierarchical representation with a multi stage decoder that has a GAN-based architecture. We observe that this method is very robust to the quantization of representation features. An AB test was conducted on a subset of the Harvard sentences that are commonly used to evaluate standard mobile-telephony codecs. The results show that the proposed method outperforms the standard AMR-WB codec in terms of delay, bitrate and subjective quality.

</details>

### [Language-Agnostic Meta-Learning for Low-Resource Text-to-Speech with Articulatory Features](2203.03191.md)
**Florian Lux, Ngoc Thang Vu** · 2022-03-07

<details>
<summary>Abstract</summary>

While neural text-to-speech systems perform remarkably well in high-resource scenarios, they cannot be applied to the majority of the over 6,000 spoken languages in the world due to a lack of appropriate training data. In this work, we use embeddings derived from articulatory vectors rather than embeddings derived from phoneme identities to learn phoneme representations that hold across languages. In conjunction with language agnostic meta learning, this enables us to fine-tune a high-quality text-to-speech model on just 30 minutes of data in a previously unseen language spoken by a previously unseen speaker.

</details>

### [Variational Auto-Encoder based Mandarin Speech Cloning](2203.02967.md)
**Qingyu Xing, Xiaohan Ma** · 2022-03-06

<details>
<summary>Abstract</summary>

Speech cloning technology is becoming more sophisticated thanks to the advances in machine learning. Researchers have successfully implemented natural-sounding English speech synthesis and good English speech cloning by some effective models. However, because of prosodic phrasing and large character set of Mandarin, Chinese utilization of these models is not yet complete. By creating a new dataset and replacing Tacotron synthesizer with VAENAR-TTS, we improved the existing speech cloning technique CV2TTS to almost real-time speech cloning while guaranteeing synthesis quality. In the process, we customized the subjective tests of synthesis quality assessment by attaching various scenarios, so that subjects focus on the differences between voice and our improvements maybe were more advantageous to practical applications. The results of the A/B test, real-time factor (RTF) and 2.74 mean opinion score (MOS) in terms of naturalness and similarity, reflect the real-time high-quality Mandarin speech cloning we achieved.

</details>

### [NeuralDPS: Neural Deterministic Plus Stochastic Model with Multiband Excitation for Noise-Controllable Waveform Generation](2203.02678.md)
**Tao Wang, Ruibo Fu, Jiangyan Yi, Jianhua Tao et al.** · 2022-03-05

<details>
<summary>Abstract</summary>

The traditional vocoders have the advantages of high synthesis efficiency, strong interpretability, and speech editability, while the neural vocoders have the advantage of high synthesis quality. To combine the advantages of two vocoders, inspired by the traditional deterministic plus stochastic model, this paper proposes a novel neural vocoder named NeuralDPS which can retain high speech quality and acquire high synthesis efficiency and noise controllability. Firstly, this framework contains four modules: a deterministic source module, a stochastic source module, a neural V/UV decision module and a neural filter module. The input required by the vocoder is just the spectral parameter, which avoids the error caused by estimating additional parameters, such as F0. Secondly, to solve the problem that different frequency bands may have different proportions of deterministic components and stochastic components, a multiband excitation strategy is used to generate a more accurate excitation signal and reduce the neural filter's burden. Thirdly, a method to control noise components of speech is proposed. In this way, the signal-to-noise ratio (SNR) of speech can be adjusted easily. Objective and subjective experimental results show that our proposed NeuralDPS vocoder can obtain similar performance with the WaveNet and it generates waveforms at least 280 times faster than the WaveNet vocoder. It is also 28% faster than WaveGAN's synthesis efficiency on a single CPU core. We have also verified through experiments that this method can effectively control the noise components in the predicted speech and adjust the SNR of speech. Examples of generated speech can be found at https://hairuo55.github.io/NeuralDPS.

</details>

### [iSTFTNet: Fast and Lightweight Mel-Spectrogram Vocoder Incorporating Inverse Short-Time Fourier Transform](2203.02395.md)
**Takuhiro Kaneko, Kou Tanaka, Hirokazu Kameoka, Shogo Seki** · 2022-03-04

<details>
<summary>Abstract</summary>

In recent text-to-speech synthesis and voice conversion systems, a mel-spectrogram is commonly applied as an intermediate representation, and the necessity for a mel-spectrogram vocoder is increasing. A mel-spectrogram vocoder must solve three inverse problems: recovery of the original-scale magnitude spectrogram, phase reconstruction, and frequency-to-time conversion. A typical convolutional mel-spectrogram vocoder solves these problems jointly and implicitly using a convolutional neural network, including temporal upsampling layers, when directly calculating a raw waveform. Such an approach allows skipping redundant processes during waveform synthesis (e.g., the direct reconstruction of high-dimensional original-scale spectrograms). By contrast, the approach solves all problems in a black box and cannot effectively employ the time-frequency structures existing in a mel-spectrogram. We thus propose iSTFTNet, which replaces some output-side layers of the mel-spectrogram vocoder with the inverse short-time Fourier transform (iSTFT) after sufficiently reducing the frequency dimension using upsampling layers, reducing the computational cost from black-box modeling and avoiding redundant estimations of high-dimensional spectrograms. During our experiments, we applied our ideas to three HiFi-GAN variants and made the models faster and more lightweight with a reasonable speech quality. Audio samples are available at https://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/istftnet/.

</details>

### [Generative Modeling for Low Dimensional Speech Attributes with Neural Spline Flows](2203.01786.md)
**Kevin J. Shih, Rafael Valle, Rohan Badlani, João Felipe Santos et al.** · 2022-03-03

<details>
<summary>Abstract</summary>

Despite recent advances in generative modeling for text-to-speech synthesis, these models do not yet have the same fine-grained adjustability of pitch-conditioned deterministic models such as FastPitch and FastSpeech2. Pitch information is not only low-dimensional, but also discontinuous, making it particularly difficult to model in a generative setting. Our work explores several techniques for handling the aforementioned issues in the context of Normalizing Flow models. We also find this problem to be very well suited for Neural Spline flows, which is a highly expressive alternative to the more common affine-coupling mechanism in Normalizing Flows.

</details>

### [Speaker Adaption with Intuitive Prosodic Features for Statistical Parametric Speech Synthesis](2203.00951.md)
**Pengyu Cheng, Zhenhua Ling** · 2022-03-02

<details>
<summary>Abstract</summary>

In this paper, we propose a method of speaker adaption with intuitive prosodic features for statistical parametric speech synthesis. The intuitive prosodic features employed in this method include pitch, pitch range, speech rate and energy considering that they are directly related with the overall prosodic characteristics of different speakers. The intuitive prosodic features are extracted at utterance-level or speaker-level, and are further integrated into the existing speaker-encoding-based and speaker-embedding-based adaptation frameworks respectively. The acoustic models are sequence-to-sequence ones based on Tacotron2. Intuitive prosodic features are concatenated with text encoder outputs and speaker vectors for decoding acoustic features.Experimental results have demonstrated that our proposed methods can achieve better objective and subjective performance than the baseline methods without intuitive prosodic features. Besides, the proposed speaker adaption method with utterance-level prosodic features has achieved the best similarity of synthetic speech among all compared methods.

</details>

### [A Multi-Scale Time-Frequency Spectrogram Discriminator for GAN-based Non-Autoregressive TTS](2203.01080.md)
**Haohan Guo, Hui Lu, Xixin Wu, Helen Meng** · 2022-03-02

<details>
<summary>Abstract</summary>

The generative adversarial network (GAN) has shown its outstanding capability in improving Non-Autoregressive TTS (NAR-TTS) by adversarially training it with an extra model that discriminates between the real and the generated speech. To maximize the benefits of GAN, it is crucial to find a powerful discriminator that can capture rich distinguishable information. In this paper, we propose a multi-scale time-frequency spectrogram discriminator to help NAR-TTS generate high-fidelity Mel-spectrograms. It treats the spectrogram as a 2D image to exploit the correlation among different components in the time-frequency domain. And a U-Net-based model structure is employed to discriminate at different scales to capture both coarse-grained and fine-grained information. We conduct subjective tests to evaluate the proposed approach. Both multi-scale and time-frequency discriminating bring significant improvement in the naturalness and fidelity. When combining the neural vocoder, it is shown more effective and concise than fine-tuning the vocoder. Finally, we visualize the discriminating maps to compare their difference to verify the effectiveness of multi-scale discriminating.

</details>

### [Revisiting Over-Smoothness in Text to Speech](2202.13066.md)
**Yi Ren, Xu Tan, Tao Qin, Zhou Zhao et al.** · 2022-02-26

<details>
<summary>Abstract</summary>

Non-autoregressive text to speech (NAR-TTS) models have attracted much attention from both academia and industry due to their fast generation speed. One limitation of NAR-TTS models is that they ignore the correlation in time and frequency domains while generating speech mel-spectrograms, and thus cause blurry and over-smoothed results. In this work, we revisit this over-smoothing problem from a novel perspective: the degree of over-smoothness is determined by the gap between the complexity of data distributions and the capability of modeling methods. Both simplifying data distributions and improving modeling methods can alleviate the problem. Accordingly, we first study methods reducing the complexity of data distributions. Then we conduct a comprehensive study on NAR-TTS models that use some advanced modeling methods. Based on these studies, we find that 1) methods that provide additional condition inputs reduce the complexity of data distributions to model, thus alleviating the over-smoothing problem and achieving better voice quality. 2) Among advanced modeling methods, Laplacian mixture loss performs well at modeling multimodal distributions and enjoys its simplicity, while GAN and Glow achieve the best voice quality while suffering from increased training or model complexity. 3) The two categories of methods can be combined to further alleviate the over-smoothness and improve the voice quality. 4) Our experiments on the multi-speaker dataset lead to similar conclusions as above and providing more variance information can reduce the difficulty of modeling the target data distribution and alleviate the requirements for model capacity.

</details>

### [Human Detection of Political Speech Deepfakes across Transcripts, Audio, and Video](2202.12883.md)
**Matthew Groh, Aruna Sankaranarayanan, Nikhil Singh, Dong Young Kim et al.** · 2022-02-25

<details>
<summary>Abstract</summary>

Recent advances in technology for hyper-realistic visual and audio effects provoke the concern that deepfake videos of political speeches will soon be indistinguishable from authentic video recordings. The conventional wisdom in communication theory predicts people will fall for fake news more often when the same version of a story is presented as a video versus text. We conduct 5 pre-registered randomized experiments with 2,215 participants to evaluate how accurately humans distinguish real political speeches from fabrications across base rates of misinformation, audio sources, question framings, and media modalities. We find base rates of misinformation minimally influence discernment and deepfakes with audio produced by the state-of-the-art text-to-speech algorithms are harder to discern than the same deepfakes with voice actor audio. Moreover across all experiments, we find audio and visual information enables more accurate discernment than text alone: human discernment relies more on how something is said, the audio-visual cues, than what is said, the speech content.

</details>

### [Retriever: Learning Content-Style Representation as a Token-Level Bipartite Graph](2202.12307.md)
**Dacheng Yin, Xuanchi Ren, Chong Luo, Yuwang Wang et al.** · 2022-02-24

<details>
<summary>Abstract</summary>

This paper addresses the unsupervised learning of content-style decomposed representation. We first give a definition of style and then model the content-style representation as a token-level bipartite graph. An unsupervised framework, named Retriever, is proposed to learn such representations. First, a cross-attention module is employed to retrieve permutation invariant (P.I.) information, defined as style, from the input data. Second, a vector quantization (VQ) module is used, together with man-induced constraints, to produce interpretable content tokens. Last, an innovative link attention module serves as the decoder to reconstruct data from the decomposed content and style, with the help of the linking keys. Being modal-agnostic, the proposed Retriever is evaluated in both speech and image domains. The state-of-the-art zero-shot voice conversion performance confirms the disentangling ability of our framework. Top performance is also achieved in the part discovery task for images, verifying the interpretability of our representation. In addition, the vivid part-based style transfer quality demonstrates the potential of Retriever to support various fascinating generative tasks. Project page at https://ydcustc.github.io/retriever-demo/.

</details>

### [End-to-end LPCNet: A Neural Vocoder With Fully-Differentiable LPC Estimation](2202.11301.md)
**Krishna Subramani, Jean-Marc Valin, Umut Isik, Paris Smaragdis et al.** · 2022-02-23

<details>
<summary>Abstract</summary>

Neural vocoders have recently demonstrated high quality speech synthesis, but typically require a high computational complexity. LPCNet was proposed as a way to reduce the complexity of neural synthesis by using linear prediction (LP) to assist an autoregressive model. At inference time, LPCNet relies on the LP coefficients being explicitly computed from the input acoustic features. That makes the design of LPCNet-based systems more complicated, while adding the constraint that the input features must represent a clean speech spectrum. We propose an end-to-end version of LPCNet that lifts these limitations by learning to infer the LP coefficients from the input features in the frame rate network. Results show that the proposed end-to-end approach equals or exceeds the quality of the original LPCNet model, but without explicit LP analysis. Our open-source end-to-end model still benefits from LPCNet's low complexity, while allowing for any type of conditioning features.

</details>

### [Improving Cross-lingual Speech Synthesis with Triplet Training Scheme](2202.10729.md)
**Jianhao Ye, Hongbin Zhou, Zhiba Su, Wendi He et al.** · 2022-02-22

<details>
<summary>Abstract</summary>

Recent advances in cross-lingual text-to-speech (TTS) made it possible to synthesize speech in a language foreign to a monolingual speaker. However, there is still a large gap between the pronunciation of generated cross-lingual speech and that of native speakers in terms of naturalness and intelligibility. In this paper, a triplet training scheme is proposed to enhance the cross-lingual pronunciation by allowing previously unseen content and speaker combinations to be seen during training. Proposed method introduces an extra fine-tune stage with triplet loss during training, which efficiently draws the pronunciation of the synthesized foreign speech closer to those from the native anchor speaker, while preserving the non-native speaker's timbre. Experiments are conducted based on a state-of-the-art baseline cross-lingual TTS system and its enhanced variants. All the objective and subjective evaluations show the proposed method brings significant improvement in both intelligibility and naturalness of the synthesized cross-lingual speech.

</details>

### [nnSpeech: Speaker-Guided Conditional Variational Autoencoder for Zero-shot Multi-speaker Text-to-Speech](2202.10712.md)
**Botao Zhao, Xulong Zhang, Jianzong Wang, Ning Cheng et al.** · 2022-02-22

<details>
<summary>Abstract</summary>

Multi-speaker text-to-speech (TTS) using a few adaption data is a challenge in practical applications. To address that, we propose a zero-shot multi-speaker TTS, named nnSpeech, that could synthesis a new speaker voice without fine-tuning and using only one adaption utterance. Compared with using a speaker representation module to extract the characteristics of new speakers, our method bases on a speaker-guided conditional variational autoencoder and can generate a variable Z, which contains both speaker characteristics and content information. The latent variable Z distribution is approximated by another variable conditioned on reference mel-spectrogram and phoneme. Experiments on the English corpus, Mandarin corpus, and cross-dataset proves that our model could generate natural and similar speech with only one adaption speech.

</details>

### [Neural Speech Synthesis on a Shoestring: Improving the Efficiency of LPCNet](2202.11169.md)
**Jean-Marc Valin, Umut Isik, Paris Smaragdis, Arvindh Krishnaswamy** · 2022-02-22

<details>
<summary>Abstract</summary>

Neural speech synthesis models can synthesize high quality speech but typically require a high computational complexity to do so. In previous work, we introduced LPCNet, which uses linear prediction to significantly reduce the complexity of neural synthesis. In this work, we further improve the efficiency of LPCNet -- targeting both algorithmic and computational improvements -- to make it usable on a wide variety of devices. We demonstrate an improvement in synthesis quality while operating 2.5x faster. The resulting open-source LPCNet algorithm can perform real-time neural synthesis on most existing phones and is even usable in some embedded devices.

</details>

### [Wavebender GAN: An architecture for phonetically meaningful speech manipulation](2202.10973.md)
**Gustavo Teodoro Döhler Beck, Ulme Wennberg, Zofia Malisz, Gustav Eje Henter** · 2022-02-22

<details>
<summary>Abstract</summary>

Deep learning has revolutionised synthetic speech quality. However, it has thus far delivered little value to the speech science community. The new methods do not meet the controllability demands that practitioners in this area require e.g.: in listening tests with manipulated speech stimuli. Instead, control of different speech properties in such stimuli is achieved by using legacy signal-processing methods. This limits the range, accuracy, and speech quality of the manipulations. Also, audible artefacts have a negative impact on the methodological validity of results in speech perception studies. This work introduces a system capable of manipulating speech properties through learning rather than design. The architecture learns to control arbitrary speech properties and leverages progress in neural vocoders to obtain realistic output. Experiments with copy synthesis and manipulation of a small set of core speech features (pitch, formants, and voice quality measures) illustrate the promise of the approach for producing speech stimuli that have accurate control and high perceptual quality.

</details>

### [DRVC: A Framework of Any-to-Any Voice Conversion with Self-Supervised Learning](2202.10976.md)
**Qiqi Wang, Xulong Zhang, Jianzong Wang, Ning Cheng et al.** · 2022-02-22

<details>
<summary>Abstract</summary>

Any-to-any voice conversion problem aims to convert voices for source and target speakers, which are out of the training data. Previous works wildly utilize the disentangle-based models. The disentangle-based model assumes the speech consists of content and speaker style information and aims to untangle them to change the style information for conversion. Previous works focus on reducing the dimension of speech to get the content information. But the size is hard to determine to lead to the untangle overlapping problem. We propose the Disentangled Representation Voice Conversion (DRVC) model to address the issue. DRVC model is an end-to-end self-supervised model consisting of the content encoder, timbre encoder, and generator. Instead of the previous work for reducing speech size to get content, we propose a cycle for restricting the disentanglement by the Cycle Reconstruct Loss and Same Loss. The experiments show there is an improvement for converted speech on quality and voice similarity.

</details>

### [CampNet: Context-Aware Mask Prediction for End-to-End Text-Based Speech Editing](2202.09950.md)
**Tao Wang, Jiangyan Yi, Ruibo Fu, Jianhua Tao et al.** · 2022-02-21

<details>
<summary>Abstract</summary>

The text-based speech editor allows the editing of speech through intuitive cutting, copying, and pasting operations to speed up the process of editing speech. However, the major drawback of current systems is that edited speech often sounds unnatural due to cut-copy-paste operation. In addition, it is not obvious how to synthesize records according to a new word not appearing in the transcript. This paper proposes a novel end-to-end text-based speech editing method called context-aware mask prediction network (CampNet). The model can simulate the text-based speech editing process by randomly masking part of speech and then predicting the masked region by sensing the speech context. It can solve unnatural prosody in the edited region and synthesize the speech corresponding to the unseen words in the transcript. Secondly, for the possible operation of text-based speech editing, we design three text-based operations based on CampNet: deletion, insertion, and replacement. These operations can cover various situations of speech editing. Thirdly, to synthesize the speech corresponding to long text in insertion and replacement operations, a word-level autoregressive generation method is proposed. Fourthly, we propose a speaker adaptation method using only one sentence for CampNet and explore the ability of few-shot learning based on CampNet, which provides a new idea for speech forgery tasks. The subjective and objective experiments on VCTK and LibriTTS datasets show that the speech editing results based on CampNet are better than TTS technology, manual editing, and VoCo method. We also conduct detailed ablation experiments to explore the effect of the CampNet structure on its performance. Finally, the experiment shows that speaker adaptation with only one sentence can further improve the naturalness of speech. Examples of generated speech can be found at https://hairuo55.github.io/CampNet.

</details>

### [AVQVC: One-shot Voice Conversion by Vector Quantization with applying contrastive learning](2202.10020.md)
**Huaizhen Tang, Xulong Zhang, Jianzong Wang, Ning Cheng et al.** · 2022-02-21

<details>
<summary>Abstract</summary>

Voice Conversion(VC) refers to changing the timbre of a speech while retaining the discourse content. Recently, many works have focused on disentangle-based learning techniques to separate the timbre and the linguistic content information from a speech signal. Once successful, voice conversion will be feasible and straightforward. This paper proposed a novel one-shot voice conversion framework based on vector quantization voice conversion (VQVC) and AutoVC, called AVQVC. A new training method is applied to VQVC to separate content and timbre information from speech more effectively. The result shows that this approach has better performance than VQVC in separating content and timbre to improve the sound quality of generated speech.

</details>

### [It's Raw! Audio Generation with State-Space Models](2202.09729.md)
**Karan Goel, Albert Gu, Chris Donahue, Christopher Ré** · 2022-02-20

<details>
<summary>Abstract</summary>

Developing architectures suitable for modeling raw audio is a challenging problem due to the high sampling rates of audio waveforms. Standard sequence modeling approaches like RNNs and CNNs have previously been tailored to fit the demands of audio, but the resultant architectures make undesirable computational tradeoffs and struggle to model waveforms effectively. We propose SaShiMi, a new multi-scale architecture for waveform modeling built around the recently introduced S4 model for long sequence modeling. We identify that S4 can be unstable during autoregressive generation, and provide a simple improvement to its parameterization by drawing connections to Hurwitz matrices. SaShiMi yields state-of-the-art performance for unconditional waveform generation in the autoregressive setting. Additionally, SaShiMi improves non-autoregressive generation performance when used as the backbone architecture for a diffusion model. Compared to prior architectures in the autoregressive generation setting, SaShiMi generates piano and speech waveforms which humans find more musical and coherent respectively, e.g. 2x better mean opinion scores than WaveNet on an unconditional speech generation task. On a music generation task, SaShiMi outperforms WaveNet on density estimation and speed at both training and inference even when using 3x fewer parameters. Code can be found at https://github.com/HazyResearch/state-spaces and samples at https://hazyresearch.stanford.edu/sashimi-examples.

</details>

### [VCVTS: Multi-speaker Video-to-Speech synthesis via cross-modal knowledge transfer from voice conversion](2202.09081.md)
**Disong Wang, Shan Yang, Dan Su, Xunying Liu et al.** · 2022-02-18

<details>
<summary>Abstract</summary>

Though significant progress has been made for speaker-dependent Video-to-Speech (VTS) synthesis, little attention is devoted to multi-speaker VTS that can map silent video to speech, while allowing flexible control of speaker identity, all in a single system. This paper proposes a novel multi-speaker VTS system based on cross-modal knowledge transfer from voice conversion (VC), where vector quantization with contrastive predictive coding (VQCPC) is used for the content encoder of VC to derive discrete phoneme-like acoustic units, which are transferred to a Lip-to-Index (Lip2Ind) network to infer the index sequence of acoustic units. The Lip2Ind network can then substitute the content encoder of VC to form a multi-speaker VTS system to convert silent video to acoustic units for reconstructing accurate spoken content. The VTS system also inherits the advantages of VC by using a speaker encoder to produce speaker representations to effectively control the speaker identity of generated speech. Extensive evaluations verify the effectiveness of proposed approach, which can be applied in both constrained vocabulary and open vocabulary conditions, achieving state-of-the-art performance in generating high-quality speech with high naturalness, intelligibility and speaker similarity. Our demo page is released here: https://wendison.github.io/VCVTS-demo/

</details>

### [Attributable-Watermarking of Speech Generative Models](2202.08900.md)
**Yongbaek Cho, Changhoon Kim, Yezhou Yang, Yi Ren** · 2022-02-17

<details>
<summary>Abstract</summary>

Generative models are now capable of synthesizing images, speeches, and videos that are hardly distinguishable from authentic contents. Such capabilities cause concerns such as malicious impersonation and IP theft. This paper investigates a solution for model attribution, i.e., the classification of synthetic contents by their source models via watermarks embedded in the contents. Building on past success of model attribution in the image domain, we discuss algorithmic improvements for generating user-end speech models that empirically achieve high attribution accuracy, while maintaining high generation quality. We show the trade off between attributability and generation quality under a variety of attacks on generated speech signals attempting to remove the watermarks, and the feasibility of learning robust watermarks against these attacks.

</details>

### [Voice Filter: Few-shot text-to-speech speaker adaptation using voice conversion as a post-processing module](2202.08164.md)
**Adam Gabryś, Goeric Huybrechts, Manuel Sam Ribeiro, Chung-Ming Chien et al.** · 2022-02-16

<details>
<summary>Abstract</summary>

State-of-the-art text-to-speech (TTS) systems require several hours of recorded speech data to generate high-quality synthetic speech. When using reduced amounts of training data, standard TTS models suffer from speech quality and intelligibility degradations, making training low-resource TTS systems problematic. In this paper, we propose a novel extremely low-resource TTS method called Voice Filter that uses as little as one minute of speech from a target speaker. It uses voice conversion (VC) as a post-processing module appended to a pre-existing high-quality TTS system and marks a conceptual shift in the existing TTS paradigm, framing the few-shot TTS problem as a VC task. Furthermore, we propose to use a duration-controllable TTS system to create a parallel speech corpus to facilitate the VC task. Results show that the Voice Filter outperforms state-of-the-art few-shot speech synthesis techniques in terms of objective and subjective metrics on one minute of speech on a diverse set of voices, while being competitive against a TTS model built on 30 times more data.

</details>

### [ProsoSpeech: Enhancing Prosody With Quantized Vector Pre-training in Text-to-Speech](2202.07816.md)
**Yi Ren, Ming Lei, Zhiying Huang, Shiliang Zhang et al.** · 2022-02-16

<details>
<summary>Abstract</summary>

Expressive text-to-speech (TTS) has become a hot research topic recently, mainly focusing on modeling prosody in speech. Prosody modeling has several challenges: 1) the extracted pitch used in previous prosody modeling works have inevitable errors, which hurts the prosody modeling; 2) different attributes of prosody (e.g., pitch, duration and energy) are dependent on each other and produce the natural prosody together; and 3) due to high variability of prosody and the limited amount of high-quality data for TTS training, the distribution of prosody cannot be fully shaped. To tackle these issues, we propose ProsoSpeech, which enhances the prosody using quantized latent vectors pre-trained on large-scale unpaired and low-quality text and speech data. Specifically, we first introduce a word-level prosody encoder, which quantizes the low-frequency band of the speech and compresses prosody attributes in the latent prosody vector (LPV). Then we introduce an LPV predictor, which predicts LPV given word sequence. We pre-train the LPV predictor on large-scale text and low-quality speech data and fine-tune it on the high-quality TTS dataset. Finally, our model can generate expressive speech conditioned on the predicted LPV. Experimental results show that ProsoSpeech can generate speech with richer prosody compared with baseline methods.

</details>

### [Unsupervised word-level prosody tagging for controllable speech synthesis](2202.07200.md)
**Yiwei Guo, Chenpeng Du, Kai Yu** · 2022-02-15

<details>
<summary>Abstract</summary>

Although word-level prosody modeling in neural text-to-speech (TTS) has been investigated in recent research for diverse speech synthesis, it is still challenging to control speech synthesis manually without a specific reference. This is largely due to lack of word-level prosody tags. In this work, we propose a novel approach for unsupervised word-level prosody tagging with two stages, where we first group the words into different types with a decision tree according to their phonetic content and then cluster the prosodies using GMM within each type of words separately. This design is based on the assumption that the prosodies of different type of words, such as long or short words, should be tagged with different label sets. Furthermore, a TTS system with the derived word-level prosody tags is trained for controllable speech synthesis. Experiments on LJSpeech show that the TTS model trained with word-level prosody tags not only achieves better naturalness than a typical FastSpeech2 model, but also gains the ability to manipulate word-level prosody.

</details>

### [NewsPod: Automatic and Interactive News Podcasts](2202.07146.md)
**Philippe Laban, Elicia Ye, Srujay Korlakunta, John Canny et al.** · 2022-02-15

<details>
<summary>Abstract</summary>

News podcasts are a popular medium to stay informed and dive deep into news topics. Today, most podcasts are handcrafted by professionals. In this work, we advance the state-of-the-art in automatically generated podcasts, making use of recent advances in natural language processing and text-to-speech technology. We present NewsPod, an automatically generated, interactive news podcast. The podcast is divided into segments, each centered on a news event, with each segment structured as a Question and Answer conversation, whose goal is to engage the listener. A key aspect of the design is the use of distinct voices for each role (questioner, responder), to better simulate a conversation. Another novel aspect of NewsPod allows listeners to interact with the podcast by asking their own questions and receiving automatically generated answers. We validate the soundness of this system design through two usability studies, focused on evaluating the narrative style and interactions with the podcast, respectively. We find that NewsPod is preferred over a baseline by participants, with 80% claiming they would use the system in the future.

</details>

### [Partially Fake Audio Detection by Self-attention-based Fake Span Discovery](2202.06684.md)
**Haibin Wu, Heng-Cheng Kuo, Naijun Zheng, Kuo-Hsuan Hung et al.** · 2022-02-14

<details>
<summary>Abstract</summary>

The past few years have witnessed the significant advances of speech synthesis and voice conversion technologies. However, such technologies can undermine the robustness of broadly implemented biometric identification models and can be harnessed by in-the-wild attackers for illegal uses. The ASVspoof challenge mainly focuses on synthesized audios by advanced speech synthesis and voice conversion models, and replay attacks. Recently, the first Audio Deep Synthesis Detection challenge (ADD 2022) extends the attack scenarios into more aspects. Also ADD 2022 is the first challenge to propose the partially fake audio detection task. Such brand new attacks are dangerous and how to tackle such attacks remains an open question. Thus, we propose a novel framework by introducing the question-answering (fake span discovery) strategy with the self-attention mechanism to detect partially fake audios. The proposed fake span detection module tasks the anti-spoofing model to predict the start and end positions of the fake clip within the partially fake audio, address the model's attention into discovering the fake spans rather than other shortcuts with less generalization, and finally equips the model with the discrimination capacity between real and partially fake audios. Our submission ranked second in the partially fake audio detection track of ADD 2022.

</details>

### [Distribution augmentation for low-resource expressive text-to-speech](2202.06409.md)
**Mateusz Lajszczak, Animesh Prasad, Arent van Korlaar, Bajibabu Bollepalli et al.** · 2022-02-13

<details>
<summary>Abstract</summary>

This paper presents a novel data augmentation technique for text-to-speech (TTS), that allows to generate new (text, audio) training examples without requiring any additional data. Our goal is to increase diversity of text conditionings available during training. This helps to reduce overfitting, especially in low-resource settings. Our method relies on substituting text and audio fragments in a way that preserves syntactical correctness. We take additional measures to ensure that synthesized speech does not contain artifacts caused by combining inconsistent audio samples. The perceptual evaluations show that our method improves speech quality over a number of datasets, speakers, and TTS architectures. We also demonstrate that it greatly improves robustness of attention-based TTS models.

</details>

### [Deep Performer: Score-to-Audio Music Performance Synthesis](2202.06034.md)
**Hao-Wen Dong, Cong Zhou, Taylor Berg-Kirkpatrick, Julian McAuley** · 2022-02-12

<details>
<summary>Abstract</summary>

Music performance synthesis aims to synthesize a musical score into a natural performance. In this paper, we borrow recent advances in text-to-speech synthesis and present the Deep Performer -- a novel system for score-to-audio music performance synthesis. Unlike speech, music often contains polyphony and long notes. Hence, we propose two new techniques for handling polyphonic inputs and providing a fine-grained conditioning in a transformer encoder-decoder model. To train our proposed system, we present a new violin dataset consisting of paired recordings and scores along with estimated alignments between them. We show that our proposed model can synthesize music with clear polyphony and harmonic structures. In a listening test, we achieve competitive quality against the baseline model, a conditional generative audio model, in terms of pitch accuracy, timbre and noise level. Moreover, our proposed model significantly outperforms the baseline on an existing piano dataset in overall quality.

</details>

### [Cross-speaker style transfer for text-to-speech using data augmentation](2202.05083.md)
**Manuel Sam Ribeiro, Julian Roth, Giulia Comini, Goeric Huybrechts et al.** · 2022-02-10

<details>
<summary>Abstract</summary>

We address the problem of cross-speaker style transfer for text-to-speech (TTS) using data augmentation via voice conversion. We assume to have a corpus of neutral non-expressive data from a target speaker and supporting conversational expressive data from different speakers. Our goal is to build a TTS system that is expressive, while retaining the target speaker's identity. The proposed approach relies on voice conversion to first generate high-quality data from the set of supporting expressive speakers. The voice converted data is then pooled with natural data from the target speaker and used to train a single-speaker multi-style TTS system. We provide evidence that this approach is efficient, flexible, and scalable. The method is evaluated using one or more supporting speakers, as well as a variable amount of supporting data. We further provide evidence that this approach allows some controllability of speaking style, when using multiple supporting speakers. We conclude by scaling our proposed technology to a set of 14 speakers across 7 languages. Results indicate that our technology consistently improves synthetic samples in terms of style similarity, while retaining the target speaker's identity.

</details>

### [Conditional Diffusion Probabilistic Model for Speech Enhancement](2202.05256.md)
**Yen-Ju Lu, Zhong-Qiu Wang, Shinji Watanabe, Alexander Richard et al.** · 2022-02-10

<details>
<summary>Abstract</summary>

Speech enhancement is a critical component of many user-oriented audio applications, yet current systems still suffer from distorted and unnatural outputs. While generative models have shown strong potential in speech synthesis, they are still lagging behind in speech enhancement. This work leverages recent advances in diffusion probabilistic models, and proposes a novel speech enhancement algorithm that incorporates characteristics of the observed noisy speech signal into the diffusion and reverse processes. More specifically, we propose a generalized formulation of the diffusion probabilistic model named conditional diffusion probabilistic model that, in its reverse process, can adapt to non-Gaussian real noises in the estimated speech signal. In our experiments, we demonstrate strong performance of the proposed approach compared to representative generative models, and investigate the generalization capability of our models to other datasets with noise characteristics unseen during training.

</details>

### [Building Synthetic Speaker Profiles in Text-to-Speech Systems](2202.03125.md)
**Jie Pu, Yixiong Meng, Oguz Elibol** · 2022-02-07

<details>
<summary>Abstract</summary>

The diversity of speaker profiles in multi-speaker TTS systems is a crucial aspect of its performance, as it measures how many different speaker profiles TTS systems could possibly synthesize. However, this important aspect is often overlooked when building multi-speaker TTS systems and there is no established framework to evaluate this diversity. The reason behind is that most multi-speaker TTS systems are limited to generate speech signals with the same speaker profiles as its training data. They often use discrete speaker embedding vectors which have a one-to-one correspondence with individual speakers. This correspondence limits TTS systems and hinders their capability of generating unseen speaker profiles that did not appear during training. In this paper, we aim to build multi-speaker TTS systems that have a greater variety of speaker profiles and can generate new synthetic speaker profiles that are different from training data. To this end, we propose to use generative models with a triplet loss and a specific shuffle mechanism. In our experiments, the effectiveness and advantages of the proposed method have been demonstrated in terms of both the distinctiveness and intelligibility of synthesized speech signals.

</details>

### [Transformer-based Models of Text Normalization for Speech Applications](2202.00153.md)
**Jae Hun Ro, Felix Stahlberg, Ke Wu, Shankar Kumar** · 2022-02-01

<details>
<summary>Abstract</summary>

Text normalization, or the process of transforming text into a consistent, canonical form, is crucial for speech applications such as text-to-speech synthesis (TTS). In TTS, the system must decide whether to verbalize "1995" as "nineteen ninety five" in "born in 1995" or as "one thousand nine hundred ninety five" in "page 1995". We present an experimental comparison of various Transformer-based sequence-to-sequence (seq2seq) models of text normalization for speech and evaluate them on a variety of datasets of written text aligned to its normalized spoken form. These models include variants of the 2-stage RNN-based tagging/seq2seq architecture introduced by Zhang et al. (2019), where we replace the RNN with a Transformer in one or more stages, as well as vanilla Transformers that output string representations of edit sequences. Of our approaches, using Transformers for sentence context encoding within the 2-stage model proved most effective, with the fine-tuned BERT encoder yielding the best performance.

</details>

### [The HCCL-DKU system for fake audio generation task of the 2022 ICASSP ADD Challenge](2201.12567.md)
**Ziyi Chen, Hua Hua, Yuxiang Zhang, Ming Li et al.** · 2022-01-29

<details>
<summary>Abstract</summary>

The voice conversion task is to modify the speaker identity of continuous speech while preserving the linguistic content. Generally, the naturalness and similarity are two main metrics for evaluating the conversion quality, which has been improved significantly in recent years. This paper presents the HCCL-DKU entry for the fake audio generation task of the 2022 ICASSP ADD challenge. We propose a novel ppg-based voice conversion model that adopts a fully end-to-end structure. Experimental results show that the proposed method outperforms other conversion models, including Tacotron-based and Fastspeech-based models, on conversion quality and spoofing performance against anti-spoofing systems. In addition, we investigate several post-processing methods for better spoofing power. Finally, we achieve second place with a deception success rate of 0.916 in the ADD challenge.

</details>

### [DiffGAN-TTS: High-Fidelity and Efficient Text-to-Speech with Denoising Diffusion GANs](2201.11972.md)
**Songxiang Liu, Dan Su, Dong Yu** · 2022-01-28

<details>
<summary>Abstract</summary>

Denoising diffusion probabilistic models (DDPMs) are expressive generative models that have been used to solve a variety of speech synthesis problems. However, because of their high sampling costs, DDPMs are difficult to use in real-time speech processing applications. In this paper, we introduce DiffGAN-TTS, a novel DDPM-based text-to-speech (TTS) model achieving high-fidelity and efficient speech synthesis. DiffGAN-TTS is based on denoising diffusion generative adversarial networks (GANs), which adopt an adversarially-trained expressive model to approximate the denoising distribution. We show with multi-speaker TTS experiments that DiffGAN-TTS can generate high-fidelity speech samples within only 4 denoising steps. We present an active shallow diffusion mechanism to further speed up inference. A two-stage training scheme is proposed, with a basic TTS acoustic model trained at stage one providing valuable prior information for a DDPM trained at stage two. Our experiments show that DiffGAN-TTS can achieve high synthesis performance with only 1 denoising step.

</details>

### [The MSXF TTS System for ICASSP 2022 ADD Challenge](2201.11400.md)
**Chunyong Yang, Pengfei Liu, Yanli Chen, Hongbin Wang et al.** · 2022-01-27

<details>
<summary>Abstract</summary>

This paper presents our MSXF TTS system for Task 3.1 of the Audio Deep Synthesis Detection (ADD) Challenge 2022. We use an end to end text to speech system, and add a constraint loss to the system when training stage. The end to end TTS system is VITS, and the pre-training self-supervised model is wav2vec 2.0. And we also explore the influence of the speech speed and volume in spoofing. The faster speech means the less the silence part in audio, the easier to fool the detector. We also find the smaller the volume, the better spoofing ability, though we normalize volume for submission. Our team is identified as C2, and we got the fourth place in the challenge.

</details>

### [J-MAC: Japanese multi-speaker audiobook corpus for speech synthesis](2201.10896.md)
**Shinnosuke Takamichi, Wataru Nakata, Naoko Tanji, Hiroshi Saruwatari** · 2022-01-26

<details>
<summary>Abstract</summary>

In this paper, we construct a Japanese audiobook speech corpus called "J-MAC" for speech synthesis research. With the success of reading-style speech synthesis, the research target is shifting to tasks that use complicated contexts. Audiobook speech synthesis is a good example that requires cross-sentence, expressiveness, etc. Unlike reading-style speech, speaker-specific expressiveness in audiobook speech also becomes the context. To enhance this research, we propose a method of constructing a corpus from audiobooks read by professional speakers. From many audiobooks and their texts, our method can automatically extract and refine the data without any language dependency. Specifically, we use vocal-instrumental separation to extract clean data, connectionist temporal classification to roughly align text and audio, and voice activity detection to refine the alignment. J-MAC is open-sourced in our project page. We also conduct audiobook speech synthesis evaluations, and the results give insights into audiobook speech synthesis.

</details>

### [Noise-robust voice conversion with domain adversarial training](2201.10693.md)
**Hongqiang Du, Lei Xie, Haizhou Li** · 2022-01-26

<details>
<summary>Abstract</summary>

Voice conversion has made great progress in the past few years under the studio-quality test scenario in terms of speech quality and speaker similarity. However, in real applications, test speech from source speaker or target speaker can be corrupted by various environment noises, which seriously degrade the speech quality and speaker similarity. In this paper, we propose a novel encoder-decoder based noise-robust voice conversion framework, which consists of a speaker encoder, a content encoder, a decoder, and two domain adversarial neural networks. Specifically, we integrate disentangling speaker and content representation technique with domain adversarial training technique. Domain adversarial training makes speaker representations and content representations extracted by speaker encoder and content encoder from clean speech and noisy speech in the same space, respectively. In this way, the learned speaker and content representations are noise-invariant. Therefore, the two noise-invariant representations can be taken as input by the decoder to predict the clean converted spectrum. The experimental results demonstrate that our proposed method can synthesize clean converted speech under noisy test scenarios, where the source speech and target speech can be corrupted by seen or unseen noise types during the training process. Additionally, both speech quality and speaker similarity are improved.

</details>

### [Invertible Voice Conversion](2201.10687.md)
**Zexin Cai, Ming Li** · 2022-01-26

<details>
<summary>Abstract</summary>

In this paper, we propose an invertible deep learning framework called INVVC for voice conversion. It is designed against the possible threats that inherently come along with voice conversion systems. Specifically, we develop an invertible framework that makes the source identity traceable. The framework is built on a series of invertible $1\times1$ convolutions and flows consisting of affine coupling layers. We apply the proposed framework to one-to-one voice conversion and many-to-one conversion using parallel training data. Experimental results show that this approach yields impressive performance on voice conversion and, moreover, the converted results can be reversed back to the source inputs utilizing the same parameters as in forwarding.

</details>

### [Zero-Shot Long-Form Voice Cloning with Dynamic Convolution Attention](2201.10375.md)
**Artem Gorodetskii, Ivan Ozhiganov** · 2022-01-25

<details>
<summary>Abstract</summary>

With recent advancements in voice cloning, the performance of speech synthesis for a target speaker has been rendered similar to the human level. However, autoregressive voice cloning systems still suffer from text alignment failures, resulting in an inability to synthesize long sentences. In this work, we propose a variant of attention-based text-to-speech system that can reproduce a target voice from a few seconds of reference speech and generalize to very long utterances as well. The proposed system is based on three independently trained components: a speaker encoder, synthesizer and universal vocoder. Generalization to long utterances is realized using an energy-based attention mechanism known as Dynamic Convolution Attention, in combination with a set of modifications proposed for the synthesizer based on Tacotron 2. Moreover, effective zero-shot speaker adaptation is achieved by conditioning both the synthesizer and vocoder on a speaker encoder that has been pretrained on a large corpus of diverse data. We compare several implementations of voice cloning systems in terms of speech naturalness, speaker similarity, alignment consistency and ability to synthesize long utterances, and conclude that the proposed model can produce intelligible synthetic speech for extremely long utterances, while preserving a high extent of naturalness and similarity for short texts.

</details>

### [Improving Adversarial Waveform Generation based Singing Voice Conversion with Harmonic Signals](2201.10130.md)
**Haohan Guo, Zhiping Zhou, Fanbo Meng, Kai Liu** · 2022-01-25

<details>
<summary>Abstract</summary>

Adversarial waveform generation has been a popular approach as the backend of singing voice conversion (SVC) to generate high-quality singing audio. However, the instability of GAN also leads to other problems, such as pitch jitters and U/V errors. It affects the smoothness and continuity of harmonics, hence degrades the conversion quality seriously. This paper proposes to feed harmonic signals to the SVC model in advance to enhance audio generation. We extract the sine excitation from the pitch, and filter it with a linear time-varying (LTV) filter estimated by a neural network. Both these two harmonic signals are adopted as the inputs to generate the singing waveform. In our experiments, two mainstream models, MelGAN and ParallelWaveGAN, are investigated to validate the effectiveness of the proposed approach. We conduct a MOS test on clean and noisy test sets. The result shows that both signals significantly improve SVC in fidelity and timbre similarity. Besides, the case analysis further validates that this method enhances the smoothness and continuity of harmonics in the generated audio, and the filtered excitation better matches the target audio.

</details>

### [Polyphone disambiguation and accent prediction using pre-trained language models in Japanese TTS front-end](2201.09427.md)
**Rem Hida, Masaki Hamada, Chie Kamada, Emiru Tsunoo et al.** · 2022-01-24

<details>
<summary>Abstract</summary>

Although end-to-end text-to-speech (TTS) models can generate natural speech, challenges still remain when it comes to estimating sentence-level phonetic and prosodic information from raw text in Japanese TTS systems. In this paper, we propose a method for polyphone disambiguation (PD) and accent prediction (AP). The proposed method incorporates explicit features extracted from morphological analysis and implicit features extracted from pre-trained language models (PLMs). We use BERT and Flair embeddings as implicit features and examine how to combine them with explicit features. Our objective evaluation results showed that the proposed method improved the accuracy by 5.7 points in PD and 6.0 points in AP. Moreover, the perceptual listening test results confirmed that a TTS system employing our proposed model as a front-end achieved a mean opinion score close to that of synthesized speech with ground-truth pronunciation and accent in terms of naturalness.

</details>

### [Cross-Lingual Text-to-Speech Using Multi-Task Learning and Speaker Classifier Joint Training](2201.08124.md)
**J. Yang, Lei He** · 2022-01-20

<details>
<summary>Abstract</summary>

In cross-lingual speech synthesis, the speech in various languages can be synthesized for a monoglot speaker. Normally, only the data of monoglot speakers are available for model training, thus the speaker similarity is relatively low between the synthesized cross-lingual speech and the native language recordings. Based on the multilingual transformer text-to-speech model, this paper studies a multi-task learning framework to improve the cross-lingual speaker similarity. To further improve the speaker similarity, joint training with a speaker classifier is proposed. Here, a scheme similar to parallel scheduled sampling is proposed to train the transformer model efficiently to avoid breaking the parallel training mechanism when introducing joint training. By using multi-task learning and speaker classifier joint training, in subjective and objective evaluations, the cross-lingual speaker similarity can be consistently improved for both the seen and unseen speakers in the training set.

</details>

### [MHTTS: Fast multi-head text-to-speech for spontaneous speech with imperfect transcription](2201.07438.md)
**Dabiao Ma, Yitong Zhang, Meng Li, Feng Ye** · 2022-01-19

<details>
<summary>Abstract</summary>

Neural network based end-to-end Text-to-Speech (TTS) has greatly improved the quality of synthesized speech. While how to use massive spontaneous speech without transcription efficiently still remains an open problem. In this paper, we propose MHTTS, a fast multi-speaker TTS system that is robust to transcription errors and speaking style speech data. Specifically, we introduce a multi-head model and transfer text information from high-quality corpus with manual transcription to spontaneous speech with imperfectly recognized transcription by jointly training them. MHTTS has three advantages: 1) Our system synthesizes better quality multi-speaker voice with faster inference speed. 2) Our system is capable of transferring correct text information to data with imperfect transcription, simulated using corruption, or provided by an Automatic Speech Recogniser (ASR). 3) Our system can utilize massive real spontaneous speech with imperfect transcription and synthesize expressive voice.

</details>

### [MsEmoTTS: Multi-scale emotion transfer, prediction, and control for emotional speech synthesis](2201.06460.md)
**Yi Lei, Shan Yang, Xinsheng Wang, Lei Xie** · 2022-01-17

<details>
<summary>Abstract</summary>

Expressive synthetic speech is essential for many human-computer interaction and audio broadcast scenarios, and thus synthesizing expressive speech has attracted much attention in recent years. Previous methods performed the expressive speech synthesis either with explicit labels or with a fixed-length style embedding extracted from reference audio, both of which can only learn an average style and thus ignores the multi-scale nature of speech prosody. In this paper, we propose MsEmoTTS, a multi-scale emotional speech synthesis framework, to model the emotion from different levels. Specifically, the proposed method is a typical attention-based sequence-to-sequence model and with proposed three modules, including global-level emotion presenting module (GM), utterance-level emotion presenting module (UM), and local-level emotion presenting module (LM), to model the global emotion category, utterance-level emotion variation, and syllable-level emotion strength, respectively. In addition to modeling the emotion from different levels, the proposed method also allows us to synthesize emotional speech in different ways, i.e., transferring the emotion from reference audio, predicting the emotion from input text, and controlling the emotion strength manually. Extensive experiments conducted on a Chinese emotional speech corpus demonstrate that the proposed method outperforms the compared reference audio-based and text-based emotional speech synthesis methods on the emotion transfer speech synthesis and text-based emotion prediction speech synthesis respectively. Besides, the experiments also show that the proposed method can control the emotion expressions flexibly. Detailed analysis shows the effectiveness of each module and the good design of the proposed method.

</details>

### [KazakhTTS2: Extending the Open-Source Kazakh TTS Corpus With More Data, Speakers, and Topics](2201.05771.md)
**Saida Mussakhojayeva, Yerbolat Khassanov, Huseyin Atakan Varol** · 2022-01-15

<details>
<summary>Abstract</summary>

We present an expanded version of our previously released Kazakh text-to-speech (KazakhTTS) synthesis corpus. In the new KazakhTTS2 corpus, the overall size has increased from 93 hours to 271 hours, the number of speakers has risen from two to five (three females and two males), and the topic coverage has been diversified with the help of new sources, including a book and Wikipedia articles. This corpus is necessary for building high-quality TTS systems for Kazakh, a Central Asian agglutinative language from the Turkic family, which presents several linguistic challenges. We describe the corpus construction process and provide the details of the training and evaluation procedures for the TTS system. Our experimental results indicate that the constructed corpus is sufficient to build robust TTS models for real-world applications, with a subjective mean opinion score ranging from 3.6 to 4.2 for all the five speakers. We believe that our corpus will facilitate speech and language research for Kazakh and other Turkic languages, which are widely considered to be low-resource due to the limited availability of free linguistic data. The constructed corpus, code, and pretrained models are publicly available in our GitHub repository.

</details>

### [Emotion Intensity and its Control for Emotional Voice Conversion](2201.03967.md)
**Kun Zhou, Berrak Sisman, Rajib Rana, Björn W. Schuller et al.** · 2022-01-10

<details>
<summary>Abstract</summary>

Emotional voice conversion (EVC) seeks to convert the emotional state of an utterance while preserving the linguistic content and speaker identity. In EVC, emotions are usually treated as discrete categories overlooking the fact that speech also conveys emotions with various intensity levels that the listener can perceive. In this paper, we aim to explicitly characterize and control the intensity of emotion. We propose to disentangle the speaker style from linguistic content and encode the speaker style into a style embedding in a continuous space that forms the prototype of emotion embedding. We further learn the actual emotion encoder from an emotion-labelled database and study the use of relative attributes to represent fine-grained emotion intensity. To ensure emotional intelligibility, we incorporate emotion classification loss and emotion embedding similarity loss into the training of the EVC network. As desired, the proposed network controls the fine-grained emotion intensity in the output speech. Through both objective and subjective evaluations, we validate the effectiveness of the proposed network for emotional expressiveness and emotion intensity control.

</details>

### [IQDUBBING: Prosody modeling based on discrete self-supervised speech representation for expressive voice conversion](2201.00269.md)
**Wendong Gan, Bolong Wen, Ying Yan, Haitao Chen et al.** · 2022-01-02

<details>
<summary>Abstract</summary>

Prosody modeling is important, but still challenging in expressive voice conversion. As prosody is difficult to model, and other factors, e.g., speaker, environment and content, which are entangled with prosody in speech, should be removed in prosody modeling. In this paper, we present IQDubbing to solve this problem for expressive voice conversion. To model prosody, we leverage the recent advances in discrete self-supervised speech representation (DSSR). Specifically, prosody vector is first extracted from pre-trained VQ-Wav2Vec model, where rich prosody information is embedded while most speaker and environment information are removed effectively by quantization. To further filter out the redundant information except prosody, such as content and partial speaker information, we propose two kinds of prosody filters to sample prosody from the prosody vector. Experiments show that IQDubbing is superior to baseline and comparison systems in terms of speech quality while maintaining prosody consistency and speaker similarity.

</details>

### [Neural Language Models Evaluate Human Performance: The Role of Language and Prosody in Predicting Job Interview Scores](s2:dd8dd481480c6fae1ce27728a7fb2d89c8c63537.md)
**** · 2022-01-01

### [The Importance of Accurate Alignments in End-to-End Speech Synthesis](s2:e2fbb6d05e75e741c6810fa463725c61948c94cd.md)
**Anusha Prakash, H. Murthy** · 2022-01-01

### [Speaker Adaptation Experiments with Limited Data for End-to-End Text-To-Speech Synthesis using Tacotron2](s2:98ef9c1ea982eba7fb9869d1a4b691f502f4bb71.md)
**Ali Raheem Mandeel, M. Al-Radhi, T. Csapó** · 2022-01-01

<details>
<summary>Abstract</summary>

Speech synthesis has the aim of generating humanlike speech from text. Nowadays, with end-to-end systems, highly natural synthesized speech can be achieved if a large enough dataset is available from the target speaker. However, often it would be necessary to adapt to a target speaker for whom only a few training samples are available. Limited data speaker adaptation might be a difficult problem due to the overly few training samples. Issues might appear with a limited speaker dataset, such as the irregular allocation of linguistic tokens (i.e., some speech sounds are left out from the synthesized speech). To build lightweight systems, measuring the number of minimum data samples and training epochs is crucial to acquire a reasonable quality. We conducted detailed experiments with four target speakers for adaptive speaker text-to-speech (TTS) synthesis to show the performance of the end-to-end Tacotron2 model and the WaveGlow neural vocoder with an English dataset at several training data samples and training lengths. According to our investigation of objective and subjective evaluations, the Tacotron2 model exhibits good performance in terms of speech quality and similarity for unseen target speakers at 100 sentences of data (pair of text and audio) with a relatively low training time.

</details>

### [MIST-Tacotron: End-to-End Emotional Speech Synthesis Using Mel-Spectrogram Image Style Transfer](s2:02732830418fadb28fc77b70fe1a7fe6100a05b1.md)
**Sung-Woo Moon, Sunghyun Kim, Yong-Hoon Choi** · 2022-01-01

<details>
<summary>Abstract</summary>

With the development of voice synthesis technology using deep learning, voice synthesis research that expresses the characteristics and emotions of speakers is actively being conducted. Current technology does not satisfactorily express various emotions and characteristics for speakers with very low or high vocal ranges and for speakers with dialects. In this paper, we propose mel-spectrogram image transfer (MIST)-Tacotron, a Tacotron 2-based speech synthesis model that adds a reference encoder with an image style transfer module. The proposed method is a technique that adds image style transfer to the existing Tacotron 2 model and extracts the speaker’s feature from the reference mel-spectrogram using a pre-trained deep learning model. Through the extracted feature, the style such as pitch, tone, and duration of the speaker are trained to express the style and emotion of the speaker more clearly. To extract the speaker’s style independently from the speaker’s timbre and emotion, the ID value for the speaker and the ID value for the emotional state were used as inputs. Performance is evaluated by F0 voiced error (FVE), F0 gross pitch error (F0 GPE), mel-cepstral distortion (MCD), band aperiodicity distortion (BAPD), voiced/unvoiced error (VUVE), false positive rate (FPR), and false negative rate (FNR). The performance of the proposed model was observed to have lower error values than the existing models, GST (Global Style Token) Tacotron and VAE (Variational Autoencoder) Tacotron. As a result of measuring mean opinion score (MOS), the sound quality of the proposed model received the highest score in terms of emotional expression and speaker style reflection.

</details>

### [E2E-V2SResNet: Deep residual convolutional neural networks for end-to-end video driven speech synthesis](s2:8788f9292af5e66470f50f0df6b867c8eb0f2c4b.md)
**Nasir Saleem, Jiechao Gao, Muhammad Irfan, Elena Verdú et al.** · 2022-01-01

