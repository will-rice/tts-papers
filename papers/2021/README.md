# 2021

287 papers in this year.

### [SoK: A Study of the Security on Voice Processing Systems](2112.13144.md)
**Robert Chang, Logan Kuo, Arthur Liu, Nader Sehatbakhsh** · 2021-12-24

<details>
<summary>Abstract</summary>

As the use of Voice Processing Systems (VPS) continues to become more prevalent in our daily lives through the increased reliance on applications such as commercial voice recognition devices as well as major text-to-speech software, the attacks on these systems are increasingly complex, varied, and constantly evolving. With the use cases for VPS rapidly growing into new spaces and purposes, the potential consequences regarding privacy are increasingly more dangerous. In addition, the growing number and increased practicality of over-the-air attacks have made system failures much more probable. In this paper, we will identify and classify an arrangement of unique attacks on voice processing systems. Over the years research has been moving from specialized, untargeted attacks that result in the malfunction of systems and the denial of services to more general, targeted attacks that can force an outcome controlled by an adversary. The current and most frequently used machine learning systems and deep neural networks, which are at the core of modern voice processing systems, were built with a focus on performance and scalability rather than security. Therefore, it is critical for us to reassess the developing voice processing landscape and to identify the state of current attacks and defenses so that we may suggest future developments and theoretical improvements.

</details>

### [Multi-speaker Multi-style Text-to-speech Synthesis With Single-speaker Single-style Training Data Scenarios](2112.12743.md)
**Qicong Xie, Tao Li, Xinsheng Wang, Zhichao Wang et al.** · 2021-12-23

<details>
<summary>Abstract</summary>

In the existing cross-speaker style transfer task, a source speaker with multi-style recordings is necessary to provide the style for a target speaker. However, it is hard for one speaker to express all expected styles. In this paper, a more general task, which is to produce expressive speech by combining any styles and timbres from a multi-speaker corpus in which each speaker has a unique style, is proposed. To realize this task, a novel method is proposed. This method is a Tacotron2-based framework but with a fine-grained text-based prosody predicting module and a speaker identity controller. Experiments demonstrate that the proposed method can successfully express a style of one speaker with the timber of another speaker bypassing the dependency on a single speaker's multi-style corpus. Moreover, the explicit prosody features used in the prosody predicting module can increase the diversity of synthetic speech by adjusting the value of prosody features.

</details>

### [Multi-Singer: Fast Multi-Singer Singing Voice Vocoder With A Large-Scale Corpus](2112.10358.md)
**Rongjie Huang, Feiyang Chen, Yi Ren, Jinglin Liu et al.** · 2021-12-20

<details>
<summary>Abstract</summary>

High-fidelity multi-singer singing voice synthesis is challenging for neural vocoder due to the singing voice data shortage, limited singer generalization, and large computational cost. Existing open corpora could not meet requirements for high-fidelity singing voice synthesis because of the scale and quality weaknesses. Previous vocoders have difficulty in multi-singer modeling, and a distinct degradation emerges when conducting unseen singer singing voice generation. To accelerate singing voice researches in the community, we release a large-scale, multi-singer Chinese singing voice dataset OpenSinger. To tackle the difficulty in unseen singer modeling, we propose Multi-Singer, a fast multi-singer vocoder with generative adversarial networks. Specifically, 1) Multi-Singer uses a multi-band generator to speed up both training and inference procedure. 2) to capture and rebuild singer identity from the acoustic feature (i.e., mel-spectrogram), Multi-Singer adopts a singer conditional discriminator and conditional adversarial training objective. 3) to supervise the reconstruction of singer identity in the spectrum envelopes in frequency domain, we propose an auxiliary singer perceptual loss. The joint training approach effectively works in GANs for multi-singer voices modeling. Experimental results verify the effectiveness of OpenSinger and show that Multi-Singer improves unseen singer singing voices modeling in both speed and quality over previous methods. The further experiment proves that combined with FastSpeech 2 as the acoustic model, Multi-Singer achieves strong robustness in the multi-singer singing voice synthesis pipeline. Samples are available at https://Multi-Singer.github.io/

</details>

### [Training Robust Zero-Shot Voice Conversion Models with Self-supervised Features](2112.04424.md)
**Trung Dang, Dung Tran, Peter Chin, Kazuhito Koishida** · 2021-12-08

<details>
<summary>Abstract</summary>

Unsupervised Zero-Shot Voice Conversion (VC) aims to modify the speaker characteristic of an utterance to match an unseen target speaker without relying on parallel training data. Recently, self-supervised learning of speech representation has been shown to produce useful linguistic units without using transcripts, which can be directly passed to a VC model. In this paper, we showed that high-quality audio samples can be achieved by using a length resampling decoder, which enables the VC model to work in conjunction with different linguistic feature extractors and vocoders without requiring them to operate on the same sequence length. We showed that our method can outperform many baselines on the VCTK dataset. Without modifying the architecture, we further demonstrated that a) using pairs of different audio segments from the same speaker, b) adding a cycle consistency loss, and c) adding a speaker classification loss can help to learn a better speaker embedding. Our model trained on LibriTTS using these techniques achieves the best performance, producing audio samples transferred well to the target speaker's voice, while preserving the linguistic content that is comparable with actual human utterances in terms of Character Error Rate.

</details>

### [Multi-speaker Emotional Text-to-speech Synthesizer](2112.03557.md)
**Sungjae Cho, Soo-Young Lee** · 2021-12-07

<details>
<summary>Abstract</summary>

We present a methodology to train our multi-speaker emotional text-to-speech synthesizer that can express speech for 10 speakers' 7 different emotions. All silences from audio samples are removed prior to learning. This results in fast learning by our model. Curriculum learning is applied to train our model efficiently. Our model is first trained with a large single-speaker neutral dataset, and then trained with neutral speech from all speakers. Finally, our model is trained using datasets of emotional speech from all speakers. In each stage, training samples of each speaker-emotion pair have equal probability to appear in mini-batches. Through this procedure, our model can synthesize speech for all targeted speakers and emotions. Our synthesized audio sets are available on our web page.

</details>

### [VocBench: A Neural Vocoder Benchmark for Speech Synthesis](2112.03099.md)
**Ehab A. AlBadawy, Andrew Gibiansky, Qing He, Jilong Wu et al.** · 2021-12-06

<details>
<summary>Abstract</summary>

Neural vocoders, used for converting the spectral representations of an audio signal to the waveforms, are a commonly used component in speech synthesis pipelines. It focuses on synthesizing waveforms from low-dimensional representation, such as Mel-Spectrograms. In recent years, different approaches have been introduced to develop such vocoders. However, it becomes more challenging to assess these new vocoders and compare their performance to previous ones. To address this problem, we present VocBench, a framework that benchmark the performance of state-of-the art neural vocoders. VocBench uses a systematic study to evaluate different neural vocoders in a shared environment that enables a fair comparison between them. In our experiments, we use the same setup for datasets, training pipeline, and evaluation metrics for all neural vocoders. We perform a subjective and objective evaluation to compare the performance of each vocoder along a different axis. Our results demonstrate that the framework is capable of showing the competitive efficacy and the quality of the synthesized samples for each vocoder. VocBench framework is available at https://github.com/facebookresearch/vocoder-benchmark.

</details>

### [Conditional Deep Hierarchical Variational Autoencoder for Voice Conversion](2112.02796.md)
**Kei Akuzawa, Kotaro Onishi, Keisuke Takiguchi, Kohki Mametani et al.** · 2021-12-06

<details>
<summary>Abstract</summary>

Variational autoencoder-based voice conversion (VAE-VC) has the advantage of requiring only pairs of speeches and speaker labels for training. Unlike the majority of the research in VAE-VC which focuses on utilizing auxiliary losses or discretizing latent variables, this paper investigates how an increasing model expressiveness has benefits and impacts on the VAE-VC. Specifically, we first analyze VAE-VC from a rate-distortion perspective, and point out that model expressiveness is significant for VAE-VC because rate and distortion reflect similarity and naturalness of converted speeches. Based on the analysis, we propose a novel VC method using a deep hierarchical VAE, which has high model expressiveness as well as having fast conversion speed thanks to its non-autoregressive decoder. Also, our analysis reveals another problem that similarity can be degraded when the latent variable of VAEs has redundant information. We address the problem by controlling the information contained in the latent variable using $β$-VAE objective. In the experiment using VCTK corpus, the proposed method achieved mean opinion scores higher than 3.5 on both naturalness and similarity in inter-gender settings, which are higher than the scores of existing autoencoder-based VC methods.

</details>

### [YourTTS: Towards Zero-Shot Multi-Speaker TTS and Zero-Shot Voice Conversion for everyone](2112.02418.md)
**Edresson Casanova, Julian Weber, Christopher Shulby, Arnaldo Candido Junior et al.** · 2021-12-04

<details>
<summary>Abstract</summary>

YourTTS brings the power of a multilingual approach to the task of zero-shot multi-speaker TTS. Our method builds upon the VITS model and adds several novel modifications for zero-shot multi-speaker and multilingual training. We achieved state-of-the-art (SOTA) results in zero-shot multi-speaker TTS and results comparable to SOTA in zero-shot voice conversion on the VCTK dataset. Additionally, our approach achieves promising results in a target language with a single-speaker dataset, opening possibilities for zero-shot multi-speaker TTS and zero-shot voice conversion systems in low-resource languages. Finally, it is possible to fine-tune the YourTTS model with less than 1 minute of speech and achieve state-of-the-art results in voice similarity and with reasonable quality. This is important to allow synthesis for speakers with a very different voice or recording characteristics from those seen during training.

</details>

### [Generating Rich Product Descriptions for Conversational E-commerce Systems](2111.15298.md)
**Shashank Kedia, Aditya Mantha, Sneha Gupta, Stephen Guo et al.** · 2021-11-30

<details>
<summary>Abstract</summary>

Through recent advancements in speech technologies and introduction of smart assistants, such as Amazon Alexa, Apple Siri and Google Home, increasing number of users are interacting with various applications through voice commands. E-commerce companies typically display short product titles on their webpages, either human-curated or algorithmically generated, when brevity is required. However, these titles are dissimilar from natural spoken language. For example, "Lucky Charms Gluten Free Break-fast Cereal, 20.5 oz a box Lucky Charms Gluten Free" is acceptable to display on a webpage, while a similar title cannot be used in a voice based text-to-speech application. In such conversational systems, an easy to comprehend sentence, such as "a 20.5 ounce box of lucky charms gluten free cereal" is preferred. Compared to display devices, where images and detailed product information can be presented to users, short titles for products which convey the most important information, are necessary when interfacing with voice assistants. We propose eBERT, a sequence-to-sequence approach by further pre-training the BERT embeddings on an e-commerce product description corpus, and then fine-tuning the resulting model to generate short, natural, spoken language titles from input web titles. Our extensive experiments on a real-world industry dataset, as well as human evaluation of model output, demonstrate that eBERT summarization outperforms comparable baseline models. Owing to the efficacy of the model, a version of this model has been deployed in real-world setting.

</details>

### [CycleTransGAN-EVC: A CycleGAN-based Emotional Voice Conversion Model with Transformer](2111.15159.md)
**Changzeng Fu, Chaoran Liu, Carlos Toshinori Ishi, Hiroshi Ishiguro** · 2021-11-30

<details>
<summary>Abstract</summary>

In this study, we explore the transformer's ability to capture intra-relations among frames by augmenting the receptive field of models. Concretely, we propose a CycleGAN-based model with the transformer and investigate its ability in the emotional voice conversion task. In the training procedure, we adopt curriculum learning to gradually increase the frame length so that the model can see from the short segment till the entire speech. The proposed method was evaluated on the Japanese emotional speech dataset and compared to several baselines (ACVAE, CycleGAN) with objective and subjective evaluations. The results show that our proposed model is able to convert emotion with higher strength and quality.

</details>

### [ESPnet-SLU: Advancing Spoken Language Understanding through ESPnet](2111.14706.md)
**Siddhant Arora, Siddharth Dalmia, Pavel Denisov, Xuankai Chang et al.** · 2021-11-29

<details>
<summary>Abstract</summary>

As Automatic Speech Processing (ASR) systems are getting better, there is an increasing interest of using the ASR output to do downstream Natural Language Processing (NLP) tasks. However, there are few open source toolkits that can be used to generate reproducible results on different Spoken Language Understanding (SLU) benchmarks. Hence, there is a need to build an open source standard that can be used to have a faster start into SLU research. We present ESPnet-SLU, which is designed for quick development of spoken language understanding in a single framework. ESPnet-SLU is a project inside end-to-end speech processing toolkit, ESPnet, which is a widely used open-source standard for various speech processing tasks like ASR, Text to Speech (TTS) and Speech Translation (ST). We enhance the toolkit to provide implementations for various SLU benchmarks that enable researchers to seamlessly mix-and-match different ASR and NLU models. We also provide pretrained models with intensively tuned hyper-parameters that can match or even outperform the current state-of-the-art performances. The toolkit is publicly available at https://github.com/espnet/espnet.

</details>

### [V2C: Visual Voice Cloning](2111.12890.md)
**Qi Chen, Yuanqing Li, Yuankai Qi, Jiaqiu Zhou et al.** · 2021-11-25

<details>
<summary>Abstract</summary>

Existing Voice Cloning (VC) tasks aim to convert a paragraph text to a speech with desired voice specified by a reference audio. This has significantly boosted the development of artificial speech applications. However, there also exist many scenarios that cannot be well reflected by these VC tasks, such as movie dubbing, which requires the speech to be with emotions consistent with the movie plots. To fill this gap, in this work we propose a new task named Visual Voice Cloning (V2C), which seeks to convert a paragraph of text to a speech with both desired voice specified by a reference audio and desired emotion specified by a reference video. To facilitate research in this field, we construct a dataset, V2C-Animation, and propose a strong baseline based on existing state-of-the-art (SoTA) VC techniques. Our dataset contains 10,217 animated movie clips covering a large variety of genres (e.g., Comedy, Fantasy) and emotions (e.g., happy, sad). We further design a set of evaluation metrics, named MCD-DTW-SL, which help evaluate the similarity between ground-truth speeches and the synthesised ones. Extensive experimental results show that even SoTA VC methods cannot generate satisfying speeches for our V2C task. We hope the proposed new task together with the constructed dataset and evaluation metric will facilitate the research in the field of voice cloning and the broader vision-and-language community.

</details>

### [One-shot Voice Conversion For Style Transfer Based On Speaker Adaptation](2111.12277.md)
**Zhichao Wang, Qicong Xie, Tao Li, Hongqiang Du et al.** · 2021-11-24

<details>
<summary>Abstract</summary>

One-shot style transfer is a challenging task, since training on one utterance makes model extremely easy to over-fit to training data and causes low speaker similarity and lack of expressiveness. In this paper, we build on the recognition-synthesis framework and propose a one-shot voice conversion approach for style transfer based on speaker adaptation. First, a speaker normalization module is adopted to remove speaker-related information in bottleneck features extracted by ASR. Second, we adopt weight regularization in the adaptation process to prevent over-fitting caused by using only one utterance from target speaker as training data. Finally, to comprehensively decouple the speech factors, i.e., content, speaker, style, and transfer source style to the target, a prosody module is used to extract prosody representation. Experiments show that our approach is superior to the state-of-the-art one-shot VC systems in terms of style and speaker similarity; additionally, our approach also maintains good speech quality.

</details>

### [Prosodic Clustering for Phoneme-level Prosody Control in End-to-End Speech Synthesis](2111.10177.md)
**Alexandra Vioni, Myrsini Christidou, Nikolaos Ellinas, Georgios Vamvoukakis et al.** · 2021-11-19

<details>
<summary>Abstract</summary>

This paper presents a method for controlling the prosody at the phoneme level in an autoregressive attention-based text-to-speech system. Instead of learning latent prosodic features with a variational framework as is commonly done, we directly extract phoneme-level F0 and duration features from the speech data in the training set. Each prosodic feature is discretized using unsupervised clustering in order to produce a sequence of prosodic labels for each utterance. This sequence is used in parallel to the phoneme sequence in order to condition the decoder with the utilization of a prosodic encoder and a corresponding attention module. Experimental results show that the proposed method retains the high quality of generated speech, while allowing phoneme-level control of F0 and duration. By replacing the F0 cluster centroids with musical notes, the model can also provide control over the note and octave within the range of the speaker.

</details>

### [Improved Prosodic Clustering for Multispeaker and Speaker-independent Phoneme-level Prosody Control](2111.10168.md)
**Myrsini Christidou, Alexandra Vioni, Nikolaos Ellinas, Georgios Vamvoukakis et al.** · 2021-11-19

<details>
<summary>Abstract</summary>

This paper presents a method for phoneme-level prosody control of F0 and duration on a multispeaker text-to-speech setup, which is based on prosodic clustering. An autoregressive attention-based model is used, incorporating multispeaker architecture modules in parallel to a prosody encoder. Several improvements over the basic single-speaker method are proposed that increase the prosodic control range and coverage. More specifically we employ data augmentation, F0 normalization, balanced clustering for duration, and speaker-independent prosodic clustering. These modifications enable fine-grained phoneme-level prosody control for all speakers contained in the training set, while maintaining the speaker identity. The model is also fine-tuned to unseen speakers with limited amounts of data and it is shown to maintain its prosody control capabilities, verifying that the speaker-independent prosodic clustering is effective. Experimental results verify that the model maintains high output speech quality and that the proposed method allows efficient prosody control within each speaker's range despite the variability that a multispeaker setting introduces.

</details>

### [More than Words: In-the-Wild Visually-Driven Prosody for Text-to-Speech](2111.10139.md)
**Michael Hassid, Michelle Tadmor Ramanovich, Brendan Shillingford, Miaosen Wang et al.** · 2021-11-19

<details>
<summary>Abstract</summary>

In this paper we present VDTTS, a Visually-Driven Text-to-Speech model. Motivated by dubbing, VDTTS takes advantage of video frames as an additional input alongside text, and generates speech that matches the video signal. We demonstrate how this allows VDTTS to, unlike plain TTS models, generate speech that not only has prosodic variations like natural pauses and pitch, but is also synchronized to the input video. Experimentally, we show our model produces well-synchronized outputs, approaching the video-speech synchronization quality of the ground-truth, on several challenging benchmarks including "in-the-wild" content from VoxCeleb2. Supplementary demo videos demonstrating video-speech synchronization, robustness to speaker ID swapping, and prosody, presented at the project page.

</details>

### [Word-Level Style Control for Expressive, Non-attentive Speech Synthesis](2111.10173.md)
**Konstantinos Klapsas, Nikolaos Ellinas, June Sig Sung, Hyoungmin Park et al.** · 2021-11-19

<details>
<summary>Abstract</summary>

This paper presents an expressive speech synthesis architecture for modeling and controlling the speaking style at a word level. It attempts to learn word-level stylistic and prosodic representations of the speech data, with the aid of two encoders. The first one models style by finding a combination of style tokens for each word given the acoustic features, and the second outputs a word-level sequence conditioned only on the phonetic information in order to disentangle it from the style information. The two encoder outputs are aligned and concatenated with the phoneme encoder outputs and then decoded with a Non-Attentive Tacotron model. An extra prior encoder is used to predict the style tokens autoregressively, in order for the model to be able to run without a reference utterance. We find that the resulting model gives both word-level and global control over the style, as well as prosody transfer capabilities.

</details>

### [High Quality Streaming Speech Synthesis with Low, Sentence-Length-Independent Latency](2111.09052.md)
**Nikolaos Ellinas, Georgios Vamvoukakis, Konstantinos Markopoulos, Aimilios Chalamandaris et al.** · 2021-11-17

<details>
<summary>Abstract</summary>

This paper presents an end-to-end text-to-speech system with low latency on a CPU, suitable for real-time applications. The system is composed of an autoregressive attention-based sequence-to-sequence acoustic model and the LPCNet vocoder for waveform generation. An acoustic model architecture that adopts modules from both the Tacotron 1 and 2 models is proposed, while stability is ensured by using a recently proposed purely location-based attention mechanism, suitable for arbitrary sentence length generation. During inference, the decoder is unrolled and acoustic feature generation is performed in a streaming manner, allowing for a nearly constant latency which is independent from the sentence length. Experimental results show that the acoustic model can produce feature sequences with minimal latency about 31 times faster than real-time on a computer CPU and 6.5 times on a mobile CPU, enabling it to meet the conditions required for real-time applications on both devices. The full end-to-end system can generate almost natural quality speech, which is verified by listening tests.

</details>

### [Cross-lingual Low Resource Speaker Adaptation Using Phonological Features](2111.09075.md)
**Georgia Maniati, Nikolaos Ellinas, Konstantinos Markopoulos, Georgios Vamvoukakis et al.** · 2021-11-17

<details>
<summary>Abstract</summary>

The idea of using phonological features instead of phonemes as input to sequence-to-sequence TTS has been recently proposed for zero-shot multilingual speech synthesis. This approach is useful for code-switching, as it facilitates the seamless uttering of foreign text embedded in a stream of native text. In our work, we train a language-agnostic multispeaker model conditioned on a set of phonologically derived features common across different languages, with the goal of achieving cross-lingual speaker adaptation. We first experiment with the effect of language phonological similarity on cross-lingual TTS of several source-target language combinations. Subsequently, we fine-tune the model with very limited data of a new speaker's voice in either a seen or an unseen language, and achieve synthetic speech of equal quality, while preserving the target speaker's identity. With as few as 32 and 8 utterances of target speaker data, we obtain high speaker similarity scores and naturalness comparable to the corresponding literature. In the extreme case of only 2 available adaptation utterances, we find that our model behaves as a few-shot learner, as the performance is similar in both the seen and unseen adaptation language scenarios.

</details>

### [Improving Prosody for Unseen Texts in Speech Synthesis by Utilizing Linguistic Information and Noisy Data](2111.07549.md)
**Zhu Li, Yuqing Zhang, Mengxi Nie, Ming Yan et al.** · 2021-11-15

<details>
<summary>Abstract</summary>

Recent advancements in end-to-end speech synthesis have made it possible to generate highly natural speech. However, training these models typically requires a large amount of high-fidelity speech data, and for unseen texts, the prosody of synthesized speech is relatively unnatural. To address these issues, we propose to combine a fine-tuned BERT-based front-end with a pre-trained FastSpeech2-based acoustic model to improve prosody modeling. The pre-trained BERT is fine-tuned on the polyphone disambiguation task, the joint Chinese word segmentation (CWS) and part-of-speech (POS) tagging task, and the prosody structure prediction (PSP) task in a multi-task learning framework. FastSpeech 2 is pre-trained on large-scale external data that are noisy but easier to obtain. Experimental results show that both the fine-tuned BERT model and the pre-trained FastSpeech 2 can improve prosody, especially for those structurally complex sentences.

</details>

### [Meta-Voice: Fast few-shot style transfer for expressive voice cloning using meta learning](2111.07218.md)
**Songxiang Liu, Dan Su, Dong Yu** · 2021-11-14

<details>
<summary>Abstract</summary>

The task of few-shot style transfer for voice cloning in text-to-speech (TTS) synthesis aims at transferring speaking styles of an arbitrary source speaker to a target speaker's voice using very limited amount of neutral data. This is a very challenging task since the learning algorithm needs to deal with few-shot voice cloning and speaker-prosody disentanglement at the same time. Accelerating the adaptation process for a new target speaker is of importance in real-world applications, but even more challenging. In this paper, we approach to the hard fast few-shot style transfer for voice cloning task using meta learning. We investigate the model-agnostic meta-learning (MAML) algorithm and meta-transfer a pre-trained multi-speaker and multi-prosody base TTS model to be highly sensitive for adaptation with few samples. Domain adversarial training mechanism and orthogonal constraint are adopted to disentangle speaker and prosody representations for effective cross-speaker style transfer. Experimental results show that the proposed approach is able to conduct fast voice cloning using only 5 samples (around 12 second speech data) from a target speaker, with only 100 adaptation steps. Audio samples are available online.

</details>

### [Textless Speech Emotion Conversion using Discrete and Decomposed Representations](2111.07402.md)
**Felix Kreuk, Adam Polyak, Jade Copet, Eugene Kharitonov et al.** · 2021-11-14

<details>
<summary>Abstract</summary>

Speech emotion conversion is the task of modifying the perceived emotion of a speech utterance while preserving the lexical content and speaker identity. In this study, we cast the problem of emotion conversion as a spoken language translation task. We use a decomposition of the speech signal into discrete learned representations, consisting of phonetic-content units, prosodic features, speaker, and emotion. First, we modify the speech content by translating the phonetic-content units to a target emotion, and then predict the prosodic features based on these units. Finally, the speech waveform is generated by feeding the predicted representations into a neural vocoder. Such a paradigm allows us to go beyond spectral and parametric changes of the signal, and model non-verbal vocalizations, such as laughter insertion, yawning removal, etc. We demonstrate objectively and subjectively that the proposed method is vastly superior to current approaches and even beats text-based systems in terms of perceived emotion and audio quality. We rigorously evaluate all components of such a complex system and conclude with an extensive model analysis and ablation study to better emphasize the architectural choices, strengths and weaknesses of the proposed method. Samples are available under the following link: https://speechbot.github.io/emotion.

</details>

### [Direct Noisy Speech Modeling for Noisy-to-Noisy Voice Conversion](2111.07116.md)
**Chao Xie, Yi-Chiao Wu, Patrick Lumban Tobing, Wen-Chin Huang et al.** · 2021-11-13

<details>
<summary>Abstract</summary>

Beyond the conventional voice conversion (VC) where the speaker information is converted without altering the linguistic content, the background sounds are informative and need to be retained in some real-world scenarios, such as VC in movie/video and VC in music where the voice is entangled with background sounds. As a new VC framework, we have developed a noisy-to-noisy (N2N) VC framework to convert the speaker's identity while preserving the background sounds. Although our framework consisting of a denoising module and a VC module well handles the background sounds, the VC module is sensitive to the distortion caused by the denoising module. To address this distortion issue, in this paper we propose the improved VC module to directly model the noisy speech waveform while controlling the background sounds. The experimental results have demonstrated that our improved framework significantly outperforms the previous one and achieves an acceptable score in terms of naturalness, while reaching comparable similarity performance to the upper bound of our framework.

</details>

### [AC-VC: Non-parallel Low Latency Phonetic Posteriorgrams Based Voice Conversion](2111.06601.md)
**Damien Ronssin, Milos Cernak** · 2021-11-12

<details>
<summary>Abstract</summary>

This paper presents AC-VC (Almost Causal Voice Conversion), a phonetic posteriorgrams based voice conversion system that can perform any-to-many voice conversion while having only 57.5 ms future look-ahead. The complete system is composed of three neural networks trained separately with non-parallel data. While most of the current voice conversion systems focus primarily on quality irrespective of algorithmic latency, this work elaborates on designing a method using a minimal amount of future context thus allowing a future real-time implementation. According to a subjective listening test organized in this work, the proposed AC-VC system achieves parity with the non-causal ASR-TTS baseline of the Voice Conversion Challenge 2020 in naturalness with a MOS of 3.5. In contrast, the results indicate that missing future context impacts speaker similarity. Obtained similarity percentage of 65% is lower than the similarity of current best voice conversion systems.

</details>

### [Speaker Generation](2111.05095.md)
**Daisy Stanton, Matt Shannon, Soroosh Mariooryad, RJ Skerry-Ryan et al.** · 2021-11-07

<details>
<summary>Abstract</summary>

This work explores the task of synthesizing speech in nonexistent human-sounding voices. We call this task "speaker generation", and present TacoSpawn, a system that performs competitively at this task. TacoSpawn is a recurrent attention-based text-to-speech model that learns a distribution over a speaker embedding space, which enables sampling of novel and diverse speakers. Our method is easy to implement, and does not require transfer learning from speaker ID systems. We present objective and subjective metrics for evaluating performance on this task, and demonstrate that our proposed objective metrics correlate with human perception of speaker similarity. Audio samples are available on our demo page.

</details>

### [Meta-TTS: Meta-Learning for Few-Shot Speaker Adaptive Text-to-Speech](2111.04040.md)
**Sung-Feng Huang, Chyi-Jiunn Lin, Da-Rong Liu, Yi-Chen Chen et al.** · 2021-11-07

<details>
<summary>Abstract</summary>

Personalizing a speech synthesis system is a highly desired application, where the system can generate speech with the user's voice with rare enrolled recordings. There are two main approaches to build such a system in recent works: speaker adaptation and speaker encoding. On the one hand, speaker adaptation methods fine-tune a trained multi-speaker text-to-speech (TTS) model with few enrolled samples. However, they require at least thousands of fine-tuning steps for high-quality adaptation, making it hard to apply on devices. On the other hand, speaker encoding methods encode enrollment utterances into a speaker embedding. The trained TTS model can synthesize the user's speech conditioned on the corresponding speaker embedding. Nevertheless, the speaker encoder suffers from the generalization gap between the seen and unseen speakers. In this paper, we propose applying a meta-learning algorithm to the speaker adaptation method. More specifically, we use Model Agnostic Meta-Learning (MAML) as the training algorithm of a multi-speaker TTS model, which aims to find a great meta-initialization to adapt the model to any few-shot speaker adaptation tasks quickly. Therefore, we can also adapt the meta-trained TTS model to unseen speakers efficiently. Our experiments compare the proposed method (Meta-TTS) with two baselines: a speaker adaptation method baseline and a speaker encoding method baseline. The evaluation results show that Meta-TTS can synthesize high speaker-similarity speech from few enrollment samples with fewer adaptation steps than the speaker adaptation baseline and outperforms the speaker encoding baseline under the same training scheme. When the speaker encoder of the baseline is pre-trained with extra 8371 speakers of data, Meta-TTS can still outperform the baseline on LibriTTS dataset and achieve comparable results on VCTK dataset.

</details>

### [Emotional Prosody Control for Speech Generation](2111.04730.md)
**Sarath Sivaprasad, Saiteja Kosgi, Vineet Gandhi** · 2021-11-07

<details>
<summary>Abstract</summary>

Machine-generated speech is characterized by its limited or unnatural emotional variation. Current text to speech systems generates speech with either a flat emotion, emotion selected from a predefined set, average variation learned from prosody sequences in training data or transferred from a source style. We propose a text to speech(TTS) system, where a user can choose the emotion of generated speech from a continuous and meaningful emotion space (Arousal-Valence space). The proposed TTS system can generate speech from the text in any speaker's style, with fine control of emotion. We show that the system works on emotion unseen during training and can scale to previously unseen speakers given his/her speech sample. Our work expands the horizon of the state-of-the-art FastSpeech2 backbone to a multi-speaker setting and gives it much-coveted continuous (and interpretable) affective control, without any observable degradation in the quality of the synthesized speech.

</details>

### [Quadrupedal Robotic Guide Dog with Vocal Human-Robot Interaction](2111.03718.md)
**Kavan Mehrizi** · 2021-11-05

<details>
<summary>Abstract</summary>

Guide dogs play a critical role in the lives of many, however training them is a time- and labor-intensive process. We are developing a method to allow an autonomous robot to physically guide humans using direct human-robot communication. The proposed algorithm will be deployed on a Unitree A1 quadrupedal robot and will autonomously navigate the person to their destination while communicating with the person using a speech interface compatible with the robot. This speech interface utilizes cloud based services such as Amazon Polly and Google Cloud to serve as the text-to-speech and speech-to-text engines.

</details>

### [A Comparison of Discrete and Soft Speech Units for Improved Voice Conversion](2111.02392.md)
**Benjamin van Niekerk, Marc-André Carbonneau, Julian Zaïdi, Mathew Baas et al.** · 2021-11-03

<details>
<summary>Abstract</summary>

The goal of voice conversion is to transform source speech into a target voice, keeping the content unchanged. In this paper, we focus on self-supervised representation learning for voice conversion. Specifically, we compare discrete and soft speech units as input features. We find that discrete representations effectively remove speaker information but discard some linguistic content - leading to mispronunciations. As a solution, we propose soft speech units. To learn soft units, we predict a distribution over discrete speech units. By modeling uncertainty, soft units capture more content information, improving the intelligibility and naturalness of converted speech. Samples available at https://ubisoft-laforge.github.io/speech/soft-vc/. Code available at https://github.com/bshall/soft-vc/.

</details>

### [Synthesizing Speech from Intracranial Depth Electrodes using an Encoder-Decoder Framework](2111.01457.md)
**Jonas Kohler, Maarten C. Ottenhoff, Sophocles Goulis, Miguel Angrick et al.** · 2021-11-02

<details>
<summary>Abstract</summary>

Speech Neuroprostheses have the potential to enable communication for people with dysarthria or anarthria. Recent advances have demonstrated high-quality text decoding and speech synthesis from electrocorticographic grids placed on the cortical surface. Here, we investigate a less invasive measurement modality in three participants, namely stereotactic EEG (sEEG) that provides sparse sampling from multiple brain regions, including subcortical regions. To evaluate whether sEEG can also be used to synthesize audio from neural recordings, we employ a recurrent encoder-decoder model based on modern deep learning methods. We find that speech can indeed be reconstructed with correlations up to 0.8 from these minimally invasive recordings, despite limited amounts of training data. In particular, the architecture we employ naturally picks up on the temporal nature of the data and thereby outperforms an existing benchmark based on non-regressive convolutional neural networks.

</details>

### [RefineGAN: Universally Generating Waveform Better than Ground Truth with Highly Accurate Pitch and Intensity Responses](2111.00962.md)
**Shengyuan Xu, Wenxiao Zhao, Jing Guo** · 2021-11-01

<details>
<summary>Abstract</summary>

Most GAN(Generative Adversarial Network)-based approaches towards high-fidelity waveform generation heavily rely on discriminators to improve their performance. However, GAN methods introduce much uncertainty into the generation process and often result in mismatches of pitch and intensity, which is fatal when it comes to sensitive use cases such as singing voice synthesis(SVS). To address this problem, we propose RefineGAN, a high-fidelity neural vocoder focused on the robustness, pitch and intensity accuracy, and high-speed full-band audio generation. We applyed a pitch-guided refine architecture with a multi-scale spectrogram-based loss function to help stabilize the training process and maintain the robustness of the neural vocoder while using the GAN-based training method. Audio generated using this method shows a better performance in subjective tests when compared with the ground-truth audio. This result shows that the fidelity is even improved during the waveform reconstruction by eliminating defects produced by recording procedures. Moreover, it shows that models trained on a specified type of data can perform on totally unseen language and unseen speaker identically well. Generated sample pairs are provided onhttps://timedomain-tech.github.io/refinegan/.

</details>

### [VRAIN-UPV MLLP's system for the Blizzard Challenge 2021](2110.15792.md)
**Alejandro Pérez-González-de-Martos, Albert Sanchis, Alfons Juan** · 2021-10-29

<details>
<summary>Abstract</summary>

This paper presents the VRAIN-UPV MLLP's speech synthesis system for the SH1 task of the Blizzard Challenge 2021. The SH1 task consisted in building a Spanish text-to-speech system trained on (but not limited to) the corpus released by the Blizzard Challenge 2021 organization. It included 5 hours of studio-quality recordings from a native Spanish female speaker. In our case, this dataset was solely used to build a two-stage neural text-to-speech pipeline composed of a non-autoregressive acoustic model with explicit duration modeling and a HiFi-GAN neural vocoder. Our team is identified as J in the evaluation results. Our system obtained very good results in the subjective evaluation tests. Only one system among other 11 participants achieved better naturalness than ours. Concretely, it achieved a naturalness MOS of 3.61 compared to 4.21 for real samples.

</details>

### [Neural Analysis and Synthesis: Reconstructing Speech from Self-Supervised Representations](2110.14513.md)
**Hyeong-Seok Choi, Juheon Lee, Wansoo Kim, Jie Hwan Lee et al.** · 2021-10-27

<details>
<summary>Abstract</summary>

We present a neural analysis and synthesis (NANSY) framework that can manipulate voice, pitch, and speed of an arbitrary speech signal. Most of the previous works have focused on using information bottleneck to disentangle analysis features for controllable synthesis, which usually results in poor reconstruction quality. We address this issue by proposing a novel training strategy based on information perturbation. The idea is to perturb information in the original input signal (e.g., formant, pitch, and frequency response), thereby letting synthesis networks selectively take essential attributes to reconstruct the input signal. Because NANSY does not need any bottleneck structures, it enjoys both high reconstruction quality and controllability. Furthermore, NANSY does not require any labels associated with speech data such as text and speaker information, but rather uses a new set of analysis features, i.e., wav2vec feature and newly proposed pitch feature, Yingram, which allows for fully self-supervised training. Taking advantage of fully self-supervised training, NANSY can be easily extended to a multilingual setting by simply training it with a multilingual dataset. The experiments show that NANSY can achieve significant improvement in performance in several applications such as zero-shot voice conversion, pitch shift, and time-scale modification.

</details>

### [Zero-shot Voice Conversion via Self-supervised Prosody Representation Learning](2110.14422.md)
**Shijun Wang, Dimche Kostadinov, Damian Borth** · 2021-10-27

<details>
<summary>Abstract</summary>

Voice Conversion (VC) for unseen speakers, also known as zero-shot VC, is an attractive research topic as it enables a range of applications like voice customizing, animation production, and others. Recent work in this area made progress with disentanglement methods that separate utterance content and speaker characteristics from speech audio recordings. However, many of these methods are subject to the leakage of prosody (e.g., pitch, volume), causing the speaker voice in the synthesized speech to be different from the desired target speakers. To prevent this issue, we propose a novel self-supervised approach that effectively learns disentangled pitch and volume representations that can represent the prosody styles of different speakers. We then use the learned prosodic representations as conditional information to train and enhance our VC model for zero-shot conversion. In our experiments, we show that our prosody representations are disentangled and rich in prosody information. Moreover, we demonstrate that the addition of our prosody representations improves our VC performance and surpasses state-of-the-art zero-shot VC performances.

</details>

### [SHECS: A Local Smart Hands-free Elderly Care Support System on Smart AR Glasses with AI Technology](2110.13538.md)
**Donghuo Zeng, Jianming Wu, Bo Yang, Tomohiro Obara et al.** · 2021-10-26

<details>
<summary>Abstract</summary>

Some elderly care homes attempt to remedy the shortage of skilled caregivers and provide long-term care for the elderly residents, by enhancing the management of the care support system with the aid of smart devices such as mobile phones and tablets. Since mobile phones and tablets lack the flexibility required for laborious elderly care work, smart AR glasses have already been considered. Although lightweight smart AR devices with a transparent display are more convenient and responsive in an elderly care workplace, fetching data from the server through the Internet results in network congestion not to mention the limited display area. To devise portable smart AR devices that operate smoothly, we first present a no keep alive Internet required smart hands-free elderly care support system that employs smart glasses with facial recognition and text-to-speech synthesis technologies. Our support system utilizes automatic lightweight facial recognition to identify residents, and information about each resident in question can be obtained hands free link with a local database. Moreover, a resident information can be displayed on just a portion of the AR smart glasses on the spot. Due to the limited size of the display area, it cannot show all the necessary information. We exploit synthesized voices in the system to read out the elderly care related information. By using the support system, caregivers can gain an understanding of each resident condition immediately, instead of having to devote considerable time in advance in obtaining the complete information of all elderly residents. Our lightweight facial recognition model achieved high accuracy with fewer model parameters than current state-of-the-art methods. The validation rate of our facial recognition system was 99.3% or higher with the false accept rate of 0.001, and caregivers rated the acceptability at 3.6 (5 levels) or higher.

</details>

### [DelightfulTTS: The Microsoft Speech Synthesis System for Blizzard Challenge 2021](2110.12612.md)
**Yanqing Liu, Zhihang Xu, Gang Wang, Kuan Chen et al.** · 2021-10-25

<details>
<summary>Abstract</summary>

This paper describes the Microsoft end-to-end neural text to speech (TTS) system: DelightfulTTS for Blizzard Challenge 2021. The goal of this challenge is to synthesize natural and high-quality speech from text, and we approach this goal in two perspectives: The first is to directly model and generate waveform in 48 kHz sampling rate, which brings higher perception quality than previous systems with 16 kHz or 24 kHz sampling rate; The second is to model the variation information in speech through a systematic design, which improves the prosody and naturalness. Specifically, for 48 kHz modeling, we predict 16 kHz mel-spectrogram in acoustic model, and propose a vocoder called HiFiNet to directly generate 48 kHz waveform from predicted 16 kHz mel-spectrogram, which can better trade off training efficiency, modelling stability and voice quality. We model variation information systematically from both explicit (speaker ID, language ID, pitch and duration) and implicit (utterance-level and phoneme-level prosody) perspectives: 1) For speaker and language ID, we use lookup embedding in training and inference; 2) For pitch and duration, we extract the values from paired text-speech data in training and use two predictors to predict the values in inference; 3) For utterance-level and phoneme-level prosody, we use two reference encoders to extract the values in training, and use two separate predictors to predict the values in inference. Additionally, we introduce an improved Conformer block to better model the local and global dependency in acoustic model. For task SH1, DelightfulTTS achieves 4.17 mean score in MOS test and 4.35 in SMOS test, which indicates the effectiveness of our proposed system

</details>

### [Discrete Acoustic Space for an Efficient Sampling in Neural Text-To-Speech](2110.12539.md)
**Marek Strong, Jonas Rohnke, Antonio Bonafonte, Mateusz Łajszczak et al.** · 2021-10-24

<details>
<summary>Abstract</summary>

We present a Split Vector Quantized Variational Autoencoder (SVQ-VAE) architecture using a split vector quantizer for NTTS, as an enhancement to the well-known Variational Autoencoder (VAE) and Vector Quantized Variational Autoencoder (VQ-VAE) architectures. Compared to these previous architectures, our proposed model retains the benefits of using an utterance-level bottleneck, while keeping significant representation power and a discretized latent space small enough for efficient prediction from text. We train the model on recordings in the expressive task-oriented dialogues domain and show that SVQ-VAE achieves a statistically significant improvement in naturalness over the VAE and VQ-VAE models. Furthermore, we demonstrate that the SVQ-VAE latent acoustic space is predictable from text, reducing the gap between the standard constant vector synthesis and vocoded recordings by 32%.

</details>

### [CaloFlow II: Even Faster and Still Accurate Generation of Calorimeter Showers with Normalizing Flows](2110.11377.md)
**Claudius Krause, David Shih** · 2021-10-21

<details>
<summary>Abstract</summary>

Recently, we introduced CaloFlow, a high-fidelity generative model for GEANT4 calorimeter shower emulation based on normalizing flows. Here, we present CaloFlow v2, an improvement on our original framework that speeds up shower generation by a further factor of 500 relative to the original. The improvement is based on a technique called Probability Density Distillation, originally developed for speech synthesis in the ML literature, and which we develop further by introducing a set of powerful new loss terms. We demonstrate that CaloFlow v2 preserves the same high fidelity of the original using qualitative (average images, histograms of high level features) and quantitative (classifier metric between GEANT4 and generated samples) measures. The result is a generative model for calorimeter showers that matches the state-of-the-art in speed (a factor of $10^4$ faster than GEANT4) and greatly surpasses the previous state-of-the-art in fidelity.

</details>

### [Disentanglement of Emotional Style and Speaker Identity for Expressive Voice Conversion](2110.10326.md)
**Zongyang Du, Berrak Sisman, Kun Zhou, Haizhou Li** · 2021-10-20

<details>
<summary>Abstract</summary>

Expressive voice conversion performs identity conversion for emotional speakers by jointly converting speaker identity and emotional style. Due to the hierarchical structure of speech emotion, it is challenging to disentangle the emotional style for different speakers. Inspired by the recent success of speaker disentanglement with variational autoencoder (VAE), we propose an any-to-any expressive voice conversion framework, that is called StyleVC. StyleVC is designed to disentangle linguistic content, speaker identity, pitch, and emotional style information. We study the use of style encoder to model emotional style explicitly. At run-time, StyleVC converts both speaker identity and emotional style for arbitrary speakers. Experiments validate the effectiveness of our proposed framework in both objective and subjective evaluations.

</details>

### [Improving Emotional Speech Synthesis by Using SUS-Constrained VAE and Text Encoder Aggregation](2110.09780.md)
**Fengyu Yang, Jian Luan, Yujun Wang** · 2021-10-19

<details>
<summary>Abstract</summary>

Learning emotion embedding from reference audio is a straightforward approach for multi-emotion speech synthesis in encoder-decoder systems. But how to get better emotion embedding and how to inject it into TTS acoustic model more effectively are still under investigation. In this paper, we propose an innovative constraint to help VAE extract emotion embedding with better cluster cohesion. Besides, the obtained emotion embedding is used as query to aggregate latent representations of all encoder layers via attention. Moreover, the queries from encoder layers themselves are also helpful. Experiments prove the proposed methods can enhance the encoding of comprehensive syntactic and semantic information and produce more expressive emotional speech.

</details>

### [Speech Enhancement-assisted Voice Conversion in Noisy Environments](2110.09923.md)
**Yun-Ju Chan, Chiang-Jen Peng, Syu-Siang Wang, Hsin-Min Wang et al.** · 2021-10-19

<details>
<summary>Abstract</summary>

Numerous voice conversion (VC) techniques have been proposed for the conversion of voices among different speakers. Although good quality of the converted speech can be observed when VC is applied in a clean environment, the quality degrades drastically when the system is run in noisy conditions. In order to address this issue, we propose a novel speech enhancement (SE)-assisted VC system that utilizes the SE techniques for signal pre-processing, where the VC and SE components are optimized in an joint training strategy with the aim to provide high-quality converted speech signals. We adopt a popular model, StarGAN, as the VC component and thus call the combined system as EStarGAN. We test the proposed EStarGAN system using a Mandarin speech corpus. The experimental results first verified the effectiveness of joint training strategy used in EStarGAN. Moreover, EStarGAN demonstrated performance robustness in various unseen noisy environments. The subjective listening test results further showed that EStarGAN can improve the sound quality of speech signals converted from noise-corrupted source utterances.

</details>

### [FMFCC-A: A Challenging Mandarin Dataset for Synthetic Speech Detection](2110.09441.md)
**Zhenyu Zhang, Yewei Gu, Xiaowei Yi, Xianfeng Zhao** · 2021-10-18

<details>
<summary>Abstract</summary>

As increasing development of text-to-speech (TTS) and voice conversion (VC) technologies, the detection of synthetic speech has been suffered dramatically. In order to promote the development of synthetic speech detection model against Mandarin TTS and VC technologies, we have constructed a challenging Mandarin dataset and organized the accompanying audio track of the first fake media forensic challenge of China Society of Image and Graphics (FMFCC-A). The FMFCC-A dataset is by far the largest publicly-available Mandarin dataset for synthetic speech detection, which contains 40,000 synthesized Mandarin utterances that generated by 11 Mandarin TTS systems and two Mandarin VC systems, and 10,000 genuine Mandarin utterances collected from 58 speakers. The FMFCC-A dataset is divided into the training, development and evaluation sets, which are used for the research of detection of synthesized Mandarin speech under various previously unknown speech synthesis systems or audio post-processing operations. In addition to describing the construction of the FMFCC-A dataset, we provide a detailed analysis of two baseline methods and the top-performing submissions from the FMFCC-A, which illustrates the usefulness and challenge of FMFCC-A dataset. We hope that the FMFCC-A dataset can fill the gap of lack of Mandarin datasets for synthetic speech detection.

</details>

### [LDNet: Unified Listener Dependent Modeling in MOS Prediction for Synthetic Speech](2110.09103.md)
**Wen-Chin Huang, Erica Cooper, Junichi Yamagishi, Tomoki Toda** · 2021-10-18

<details>
<summary>Abstract</summary>

An effective approach to automatically predict the subjective rating for synthetic speech is to train on a listening test dataset with human-annotated scores. Although each speech sample in the dataset is rated by several listeners, most previous works only used the mean score as the training target. In this work, we present LDNet, a unified framework for mean opinion score (MOS) prediction that predicts the listener-wise perceived quality given the input speech and the listener identity. We reflect recent advances in LD modeling, including design choices of the model architecture, and propose two inference methods that provide more stable results and efficient computation. We conduct systematic experiments on the voice conversion challenge (VCC) 2018 benchmark and a newly collected large-scale MOS dataset, providing an in-depth analysis of the proposed framework. Results show that the mean listener inference method is a better way to utilize the mean scores, whose effectiveness is more obvious when having more ratings per sample.

</details>

### [VISinger: Variational Inference with Adversarial Learning for End-to-End Singing Voice Synthesis](2110.08813.md)
**Yongmao Zhang, Jian Cong, Heyang Xue, Lei Xie et al.** · 2021-10-17

<details>
<summary>Abstract</summary>

In this paper, we propose VISinger, a complete end-to-end high-quality singing voice synthesis (SVS) system that directly generates audio waveform from lyrics and musical score. Our approach is inspired by VITS, which adopts VAE-based posterior encoder augmented with normalizing flow-based prior encoder and adversarial decoder to realize complete end-to-end speech generation. VISinger follows the main architecture of VITS, but makes substantial improvements to the prior encoder based on the characteristics of singing. First, instead of using phoneme-level mean and variance of acoustic features, we introduce a length regulator and a frame prior network to get the frame-level mean and variance on acoustic features, modeling the rich acoustic variation in singing. Second, we further introduce an F0 predictor to guide the frame prior network, leading to stabler singing performance. Finally, to improve the singing rhythm, we modify the duration predictor to specifically predict the phoneme to note duration ratio, helped with singing note normalization. Experiments on a professional Mandarin singing corpus show that VISinger significantly outperforms FastSpeech+Neural-Vocoder two-stage approach and the oracle VITS; ablation study demonstrates the effectiveness of different contributions.

</details>

### [Neural Dubber: Dubbing for Videos According to Scripts](2110.08243.md)
**Chenxu Hu, Qiao Tian, Tingle Li, Yuping Wang et al.** · 2021-10-15

<details>
<summary>Abstract</summary>

Dubbing is a post-production process of re-recording actors' dialogues, which is extensively used in filmmaking and video production. It is usually performed manually by professional voice actors who read lines with proper prosody, and in synchronization with the pre-recorded videos. In this work, we propose Neural Dubber, the first neural network model to solve a novel automatic video dubbing (AVD) task: synthesizing human speech synchronized with the given video from the text. Neural Dubber is a multi-modal text-to-speech (TTS) model that utilizes the lip movement in the video to control the prosody of the generated speech. Furthermore, an image-based speaker embedding (ISE) module is developed for the multi-speaker setting, which enables Neural Dubber to generate speech with a reasonable timbre according to the speaker's face. Experiments on the chemistry lecture single-speaker dataset and LRS2 multi-speaker dataset show that Neural Dubber can generate speech audios on par with state-of-the-art TTS models in terms of speech quality. Most importantly, both qualitative and quantitative evaluations show that Neural Dubber can control the prosody of synthesized speech by the video, and generate high-fidelity speech temporally synchronized with the video. Our project page is at https://tsinghua-mars-lab.github.io/NeuralDubber/ .

</details>

### [ESPnet2-TTS: Extending the Edge of TTS Research](2110.07840.md)
**Tomoki Hayashi, Ryuichi Yamamoto, Takenori Yoshimura, Peter Wu et al.** · 2021-10-15

<details>
<summary>Abstract</summary>

This paper describes ESPnet2-TTS, an end-to-end text-to-speech (E2E-TTS) toolkit. ESPnet2-TTS extends our earlier version, ESPnet-TTS, by adding many new features, including: on-the-fly flexible pre-processing, joint training with neural vocoders, and state-of-the-art TTS models with extensions like full-band E2E text-to-waveform modeling, which simplify the training pipeline and further enhance TTS performance. The unified design of our recipes enables users to quickly reproduce state-of-the-art E2E-TTS results. We also provide many pre-trained models in a unified Python interface for inference, offering a quick means for users to generate baseline samples and build demos. Experimental evaluations with English and Japanese corpora demonstrate that our provided models synthesize utterances comparable to ground-truth ones, achieving state-of-the-art TTS performance. The toolkit is available online at https://github.com/espnet/espnet.

</details>

### [Direct Simultaneous Speech-to-Speech Translation with Variational Monotonic Multihead Attention](2110.08250.md)
**Xutai Ma, Hongyu Gong, Danni Liu, Ann Lee et al.** · 2021-10-15

<details>
<summary>Abstract</summary>

We present a direct simultaneous speech-to-speech translation (Simul-S2ST) model, Furthermore, the generation of translation is independent from intermediate text representations. Our approach leverages recent progress on direct speech-to-speech translation with discrete units, in which a sequence of discrete representations, instead of continuous spectrogram features, learned in an unsupervised manner, are predicted from the model and passed directly to a vocoder for speech synthesis on-the-fly. We also introduce the variational monotonic multihead attention (V-MMA), to handle the challenge of inefficient policy learning in speech simultaneous translation. The simultaneous policy then operates on source speech features and target discrete units. We carry out empirical studies to compare cascaded and direct approach on the Fisher Spanish-English and MuST-C English-Spanish datasets. Direct simultaneous model is shown to outperform the cascaded model by achieving a better tradeoff between translation quality and latency.

</details>

### [SingGAN: Generative Adversarial Network For High-Fidelity Singing Voice Generation](2110.07468.md)
**Rongjie Huang, Chenye Cui, Feiyang Chen, Yi Ren et al.** · 2021-10-14

<details>
<summary>Abstract</summary>

Deep generative models have achieved significant progress in speech synthesis to date, while high-fidelity singing voice synthesis is still an open problem for its long continuous pronunciation, rich high-frequency parts, and strong expressiveness. Existing neural vocoders designed for text-to-speech cannot directly be applied to singing voice synthesis because they result in glitches and poor high-frequency reconstruction. In this work, we propose SingGAN, a generative adversarial network designed for high-fidelity singing voice synthesis. Specifically, 1) to alleviate the glitch problem in the generated samples, we propose source excitation with the adaptive feature learning filters to expand the receptive field patterns and stabilize long continuous signal generation; and 2) SingGAN introduces global and local discriminators at different scales to enrich low-frequency details and promote high-frequency reconstruction; and 3) To improve the training efficiency, SingGAN includes auxiliary spectrogram losses and sub-band feature matching penalty loss. To the best of our knowledge, SingGAN is the first work designed toward high-fidelity singing voice vocoding. Our evaluation of SingGAN demonstrates the state-of-the-art results with higher-quality (MOS 4.05) samples. Also, SingGAN enables a sample speed of 50x faster than real-time on a single NVIDIA 2080Ti GPU. We further show that SingGAN generalizes well to the mel-spectrogram inversion of unseen singers, and the end-to-end singing voice synthesis system SingGAN-SVS enjoys a two-stage pipeline to transform the music scores into expressive singing voices. Audio samples are available at \url{https://SingGAN.github.io/}

</details>

### [FedSpeech: Federated Text-to-Speech with Continual Learning](2110.07216.md)
**Ziyue Jiang, Yi Ren, Ming Lei, Zhou Zhao** · 2021-10-14

<details>
<summary>Abstract</summary>

Federated learning enables collaborative training of machine learning models under strict privacy restrictions and federated text-to-speech aims to synthesize natural speech of multiple users with a few audio training samples stored in their devices locally. However, federated text-to-speech faces several challenges: very few training samples from each speaker are available, training samples are all stored in local device of each user, and global model is vulnerable to various attacks. In this paper, we propose a novel federated learning architecture based on continual learning approaches to overcome the difficulties above. Specifically, 1) we use gradual pruning masks to isolate parameters for preserving speakers' tones; 2) we apply selective masks for effectively reusing knowledge from tasks; 3) a private speaker embedding is introduced to keep users' privacy. Experiments on a reduced VCTK dataset demonstrate the effectiveness of FedSpeech: it nearly matches multi-task training in terms of multi-speaker speech quality; moreover, it sufficiently retains the speakers' tones and even outperforms the multi-task training in the speaker similarity experiment.

</details>

### [Improve Cross-lingual Voice Cloning Using Low-quality Code-switched Data](2110.07210.md)
**Haitong Zhang, Yue Lin** · 2021-10-14

<details>
<summary>Abstract</summary>

Recently, sequence-to-sequence (seq-to-seq) models have been successfully applied in text-to-speech (TTS) to synthesize speech for single-language text. To synthesize speech for multiple languages usually requires multi-lingual speech from the target speaker. However, it is both laborious and expensive to collect high-quality multi-lingual TTS data for the target speakers. In this paper, we proposed to use low-quality code-switched found data from the non-target speakers to achieve cross-lingual voice cloning for the target speakers. Experiments show that our proposed method can generate high-quality code-switched speech in the target voices in terms of both naturalness and speaker consistency. More importantly, we find that our method can achieve a comparable result to the state-of-the-art (SOTA) performance in cross-lingual voice cloning.

</details>

### [Exploring Timbre Disentanglement in Non-Autoregressive Cross-Lingual Text-to-Speech](2110.07192.md)
**Haoyue Zhan, Xinyuan Yu, Haitong Zhang, Yang Zhang et al.** · 2021-10-14

<details>
<summary>Abstract</summary>

In this paper, we study the disentanglement of speaker and language representations in non-autoregressive cross-lingual TTS models from various aspects. We propose a phoneme length regulator that solves the length mismatch problem between IPA input sequence and monolingual alignment results. Using the phoneme length regulator, we present a FastPitch-based cross-lingual model with IPA symbols as input representations. Our experiments show that language-independent input representations (e.g. IPA symbols), an increasing number of training speakers, and explicit modeling of speech variance information all encourage non-autoregressive cross-lingual TTS model to disentangle speaker and language representations. The subjective evaluation shows that our proposed model can achieve decent naturalness and speaker similarity in cross-language voice cloning.

</details>

### [Revisiting IPA-based Cross-lingual Text-to-speech](2110.07187.md)
**Haitong Zhang, Haoyue Zhan, Yang Zhang, Xinyuan Yu et al.** · 2021-10-14

<details>
<summary>Abstract</summary>

International Phonetic Alphabet (IPA) has been widely used in cross-lingual text-to-speech (TTS) to achieve cross-lingual voice cloning (CL VC). However, IPA itself has been understudied in cross-lingual TTS. In this paper, we report some empirical findings of building a cross-lingual TTS model using IPA as inputs. Experiments show that the way to process the IPA and suprasegmental sequence has a negligible impact on the CL VC performance. Furthermore, we find that using a dataset including one speaker per language to build an IPA-based TTS system would fail CL VC since the language-unique IPA and tone/stress symbols could leak the speaker information. In addition, we experiment with different combinations of speakers in the training dataset to further investigate the effect of the number of speakers on the CL VC performance.

</details>

### [Toward Degradation-Robust Voice Conversion](2110.07537.md)
**Chien-yu Huang, Kai-Wei Chang, Hung-yi Lee** · 2021-10-14

<details>
<summary>Abstract</summary>

Any-to-any voice conversion technologies convert the vocal timbre of an utterance to any speaker even unseen during training. Although there have been several state-of-the-art any-to-any voice conversion models, they were all based on clean utterances to convert successfully. However, in real-world scenarios, it is difficult to collect clean utterances of a speaker, and they are usually degraded by noises or reverberations. It thus becomes highly desired to understand how these degradations affect voice conversion and build a degradation-robust model. We report in this paper the first comprehensive study on the degradation robustness of any-to-any voice conversion. We show that the performance of state-of-the-art models nowadays was severely hampered given degraded utterances. To this end, we then propose speech enhancement concatenation and denoising training to improve the robustness. In addition to common degradations, we also consider adversarial noises, which alter the model output significantly yet are human-imperceptible. It was shown that both concatenations with off-the-shelf speech enhancement models and denoising training on voice conversion models could improve the robustness, while each of them had pros and cons.

</details>

### [A Melody-Unsupervision Model for Singing Voice Synthesis](2110.06546.md)
**Soonbeom Choi, Juhan Nam** · 2021-10-13

<details>
<summary>Abstract</summary>

Recent studies in singing voice synthesis have achieved high-quality results leveraging advances in text-to-speech models based on deep neural networks. One of the main issues in training singing voice synthesis models is that they require melody and lyric labels to be temporally aligned with audio data. The temporal alignment is a time-exhausting manual work in preparing for the training data. To address the issue, we propose a melody-unsupervision model that requires only audio-and-lyrics pairs without temporal alignment in training time but generates singing voice audio given a melody and lyrics input in inference time. The proposed model is composed of a phoneme classifier and a singing voice generator jointly trained in an end-to-end manner. The model can be fine-tuned by adjusting the amount of supervision with temporally aligned melody labels. Through experiments in melody-unsupervision and semi-supervision settings, we compare the audio quality of synthesized singing voice. We also show that the proposed model is capable of being trained with speech audio and text labels but can generate singing voice in inference time.

</details>

### [DeepA: A Deep Neural Analyzer For Speech And Singing Vocoding](2110.06434.md)
**Sergey Nikonorov, Berrak Sisman, Mingyang Zhang, Haizhou Li** · 2021-10-13

<details>
<summary>Abstract</summary>

Conventional vocoders are commonly used as analysis tools to provide interpretable features for downstream tasks such as speech synthesis and voice conversion. They are built under certain assumptions about the signals following signal processing principle, therefore, not easily generalizable to different audio, for example, from speech to singing. In this paper, we propose a deep neural analyzer, denoted as DeepA - a neural vocoder that extracts F0 and timbre/aperiodicity encoding from the input speech that emulate those defined in conventional vocoders. Therefore, the resulting parameters are more interpretable than other latent neural representations. At the same time, as the deep neural analyzer is learnable, it is expected to be more accurate for signal reconstruction and manipulation, and generalizable from speech to singing. The proposed neural analyzer is built based on a variational autoencoder (VAE) architecture. We show that DeepA improves F0 estimation over the conventional vocoder (WORLD). To our best knowledge, this is the first study dedicated to the development of a neural framework for extracting learnable vocoder-like parameters.

</details>

### [Exploring the Importance of F0 Trajectories for Speaker Anonymization using X-vectors and Neural Waveform Models](2110.06887.md)
**Ünal Ege Gaznepoglu, Nils Peters** · 2021-10-13

<details>
<summary>Abstract</summary>

Voice conversion for speaker anonymization is an emerging field in speech processing research. Many state-of-the-art approaches are based on the resynthesis of the phoneme posteriorgrams (PPG), the fundamental frequency (F0) of the input signal together with modified X-vectors. Our research focuses on the role of F0 for speaker anonymization, which is an understudied area. Utilizing the VoicePrivacy Challenge 2020 framework and its datasets we developed and evaluated eight low-complexity F0 modifications prior resynthesis. We found that modifying the F0 can improve speaker anonymization by as much as 8% with minor word-error rate degradation.

</details>

### [Fine-grained style control in Transformer-based Text-to-speech Synthesis](2110.06306.md)
**Li-Wei Chen, Alexander Rudnicky** · 2021-10-12

<details>
<summary>Abstract</summary>

In this paper, we present a novel architecture to realize fine-grained style control on the transformer-based text-to-speech synthesis (TransformerTTS). Specifically, we model the speaking style by extracting a time sequence of local style tokens (LST) from the reference speech. The existing content encoder in TransformerTTS is then replaced by our designed cross-attention blocks for fusion and alignment between content and style. As the fusion is performed along with the skip connection, our cross-attention block provides a good inductive bias to gradually infuse the phoneme representation with a given style. Additionally, we prevent the style embedding from encoding linguistic content by randomly truncating LST during training and using wav2vec 2.0 features. Experiments show that with fine-grained style control, our system performs better in terms of naturalness, intelligibility, and style transferability. Our code and samples are publicly available.

</details>

### [Adapting TTS models For New Speakers using Transfer Learning](2110.05798.md)
**Paarth Neekhara, Jason Li, Boris Ginsburg** · 2021-10-12

<details>
<summary>Abstract</summary>

Training neural text-to-speech (TTS) models for a new speaker typically requires several hours of high quality speech data. Prior works on voice cloning attempt to address this challenge by adapting pre-trained multi-speaker TTS models for a new voice, using a few minutes of speech data of the new speaker. However, publicly available large multi-speaker datasets are often noisy, thereby resulting in TTS models that are not suitable for use in products. We address this challenge by proposing transfer-learning guidelines for adapting high quality single-speaker TTS models for a new speaker, using only a few minutes of speech data. We conduct an extensive study using different amounts of data for a new speaker and evaluate the synthesized speech in terms of naturalness and voice/style similarity to the target speaker. We find that fine-tuning a single-speaker TTS model on just 30 minutes of data, can yield comparable performance to a model trained from scratch on more than 27 hours of data for both male and female target speakers.

</details>

### [S3PRL-VC: Open-source Voice Conversion Framework with Self-supervised Speech Representations](2110.06280.md)
**Wen-Chin Huang, Shu-Wen Yang, Tomoki Hayashi, Hung-Yi Lee et al.** · 2021-10-12

<details>
<summary>Abstract</summary>

This paper introduces S3PRL-VC, an open-source voice conversion (VC) framework based on the S3PRL toolkit. In the context of recognition-synthesis VC, self-supervised speech representation (S3R) is valuable in its potential to replace the expensive supervised representation adopted by state-of-the-art VC systems. Moreover, we claim that VC is a good probing task for S3R analysis. In this work, we provide a series of in-depth analyses by benchmarking on the two tasks in VCC2020, namely intra-/cross-lingual any-to-one (A2O) VC, as well as an any-to-any (A2A) setting. We also provide comparisons between not only different S3Rs but also top systems in VCC2020 with supervised representations. Systematic objective and subjective evaluation were conducted, and we show that S3R is comparable with VCC2020 top systems in the A2O setting in terms of similarity, and achieves state-of-the-art in S3R-based A2A VC. We believe the extensive analysis, as well as the toolkit itself, contribute to not only the S3R community but also the VC community. The codebase is now open-sourced.

</details>

### [Discovery of Single Independent Latent Variable](2110.05887.md)
**Uri Shaham, Jonathan Svirsky, Ori Katz, Ronen Talmon** · 2021-10-12

<details>
<summary>Abstract</summary>

Latent variable discovery is a central problem in data analysis with a broad range of applications in applied science. In this work, we consider data given as an invertible mixture of two statistically independent components and assume that one of the components is observed while the other is hidden. Our goal is to recover the hidden component. For this purpose, we propose an autoencoder equipped with a discriminator. Unlike the standard nonlinear ICA problem, which was shown to be non-identifiable, in the special case of ICA we consider here, we show that our approach can recover the component of interest up to entropy-preserving transformation. We demonstrate the performance of the proposed approach in several tasks, including image synthesis, voice cloning, and fetal ECG extraction.

</details>

### [LaughNet: synthesizing laughter utterances from waveform silhouettes and a single laughter example](2110.04946.md)
**Hieu-Thi Luong, Junichi Yamagishi** · 2021-10-11

<details>
<summary>Abstract</summary>

Emotional and controllable speech synthesis is a topic that has received much attention. However, most studies focused on improving the expressiveness and controllability in the context of linguistic content, even though natural verbal human communication is inseparable from spontaneous non-speech expressions such as laughter, crying, or grunting. We propose a model called LaughNet for synthesizing laughter by using waveform silhouettes as inputs. The motivation is not simply synthesizing new laughter utterances, but testing a novel synthesis-control paradigm that uses an abstract representation of the waveform. We conducted basic listening test experiments, and the results showed that LaughNet can synthesize laughter utterances with moderate quality and retain the characteristics of the training example. More importantly, the generated waveforms have shapes similar to the input silhouettes. For future work, we will test the same method on other types of human nonverbal expressions and integrate it into more elaborated synthesis systems.

</details>

### [Denoising Diffusion Gamma Models](2110.05948.md)
**Eliya Nachmani, Robin San Roman, Lior Wolf** · 2021-10-10

<details>
<summary>Abstract</summary>

Generative diffusion processes are an emerging and effective tool for image and speech generation. In the existing methods, the underlying noise distribution of the diffusion process is Gaussian noise. However, fitting distributions with more degrees of freedom could improve the performance of such generative models. In this work, we investigate other types of noise distribution for the diffusion process. Specifically, we introduce the Denoising Diffusion Gamma Model (DDGM) and show that noise from Gamma distribution provides improved results for image and speech generation. Our approach preserves the ability to efficiently sample state in the training diffusion process while using Gamma noise.

</details>

### [Towards Lifelong Learning of Multilingual Text-To-Speech Synthesis](2110.04482.md)
**Mu Yang, Shaojin Ding, Tianlong Chen, Tong Wang et al.** · 2021-10-09

<details>
<summary>Abstract</summary>

This work presents a lifelong learning approach to train a multilingual Text-To-Speech (TTS) system, where each language was seen as an individual task and was learned sequentially and continually. It does not require pooled data from all languages altogether, and thus alleviates the storage and computation burden. One of the challenges of lifelong learning methods is "catastrophic forgetting": in TTS scenario it means that model performance quickly degrades on previous languages when adapted to a new language. We approach this problem via a data-replay-based lifelong learning method. We formulate the replay process as a supervised learning problem, and propose a simple yet effective dual-sampler framework to tackle the heavily language-imbalanced training samples. Through objective and subjective evaluations, we show that this supervised learning formulation outperforms other gradient-based and regularization-based lifelong learning methods, achieving 43% Mel-Cepstral Distortion reduction compared to a fine-tuning baseline.

</details>

### [Using multiple reference audios and style embedding constraints for speech synthesis](2110.04451.md)
**Cheng Gong, Longbiao Wang, Zhenhua Ling, Ju Zhang et al.** · 2021-10-09

<details>
<summary>Abstract</summary>

The end-to-end speech synthesis model can directly take an utterance as reference audio, and generate speech from the text with prosody and speaker characteristics similar to the reference audio. However, an appropriate acoustic embedding must be manually selected during inference. Due to the fact that only the matched text and speech are used in the training process, using unmatched text and speech for inference would cause the model to synthesize speech with low content quality. In this study, we propose to mitigate these two problems by using multiple reference audios and style embedding constraints rather than using only the target audio. Multiple reference audios are automatically selected using the sentence similarity determined by Bidirectional Encoder Representations from Transformers (BERT). In addition, we use ''target'' style embedding from a Pre-trained encoder as a constraint by considering the mutual information between the predicted and ''target'' style embedding. The experimental results show that the proposed model can improve the speech naturalness and content quality with multiple reference audios and can also outperform the baseline model in ABX preference tests of style similarity.

</details>

### [Cross-speaker Emotion Transfer Based on Speaker Condition Layer Normalization and Semi-Supervised Training in Text-To-Speech](2110.04153.md)
**Pengfei Wu, Junjie Pan, Chenchang Xu, Junhui Zhang et al.** · 2021-10-08

<details>
<summary>Abstract</summary>

In expressive speech synthesis, there are high requirements for emotion interpretation. However, it is time-consuming to acquire emotional audio corpus for arbitrary speakers due to their deduction ability. In response to this problem, this paper proposes a cross-speaker emotion transfer method that can realize the transfer of emotions from source speaker to target speaker. A set of emotion tokens is firstly defined to represent various categories of emotions. They are trained to be highly correlated with corresponding emotions for controllable synthesis by cross-entropy loss and semi-supervised training strategy. Meanwhile, to eliminate the down-gradation to the timbre similarity from cross-speaker emotion transfer, speaker condition layer normalization is implemented to model speaker characteristics. Experimental results show that the proposed method outperforms the multi-reference based baseline in terms of timbre similarity, stability and emotion perceive evaluations.

</details>

### [Environment Aware Text-to-Speech Synthesis](2110.03887.md)
**Daxin Tan, Guangyan Zhang, Tan Lee** · 2021-10-08

<details>
<summary>Abstract</summary>

This study aims at designing an environment-aware text-to-speech (TTS) system that can generate speech to suit specific acoustic environments. It is also motivated by the desire to leverage massive data of speech audio from heterogeneous sources in TTS system development. The key idea is to model the acoustic environment in speech audio as a factor of data variability and incorporate it as a condition in the process of neural network based speech synthesis. Two embedding extractors are trained with two purposely constructed datasets for characterization and disentanglement of speaker and environment factors in speech. A neural network model is trained to generate speech from extracted speaker and environment embeddings. Objective and subjective evaluation results demonstrate that the proposed TTS system is able to effectively disentangle speaker and environment factors and synthesize speech audio that carries designated speaker characteristics and environment attribute. Audio samples are available online for demonstration https://daxintan-cuhk.github.io/Environment-Aware-TTS/ .

</details>

### [A study on the efficacy of model pre-training in developing neural text-to-speech system](2110.03857.md)
**Guangyan Zhang, Yichong Leng, Daxin Tan, Ying Qin et al.** · 2021-10-08

<details>
<summary>Abstract</summary>

In the development of neural text-to-speech systems, model pre-training with a large amount of non-target speakers' data is a common approach. However, in terms of ultimately achieved system performance for target speaker(s), the actual benefits of model pre-training are uncertain and unstable, depending very much on the quantity and text content of training data. This study aims to understand better why and how model pre-training can positively contribute to TTS system performance. It is postulated that the pre-training process plays a critical role in learning text-related variation in speech, while further training with the target speaker's data aims to capture the speaker-related variation. Different test sets are created with varying degrees of similarity to target speaker data in terms of text content. Experiments show that leveraging a speaker-independent TTS trained on speech data with diverse text content can improve the target speaker TTS on domain-mismatched text. We also attempt to reduce the amount of pre-training data for a new text domain and improve the data and computational efficiency. It is found that the TTS system could achieve comparable performance when the pre-training data is reduced to 1/8 of its original size.

</details>

### [Applying Phonological Features in Multilingual Text-To-Speech](2110.03609.md)
**Cong Zhang, Huinan Zeng, Huang Liu, Jiewen Zheng** · 2021-10-07

<details>
<summary>Abstract</summary>

This study investigates whether phonological features can be applied in text-to-speech systems to generate native and non-native speech in English and Mandarin. We present a mapping of ARPABET/pinyin to SAMPA/SAMPA-SC and then to phonological features. We tested whether this mapping could lead to the successful generation of native, non-native, and code-switched speech in the two languages. We ran two experiments, one with a small dataset and one with a larger dataset. The results proved that phonological features could be used as a feasible input system, although further investigation is needed to improve model performance. The accented output generated by the TTS models also helps with understanding human second language acquisition processes.

</details>

### [Mixer-TTS: non-autoregressive, fast and compact text-to-speech model conditioned on language model embeddings](2110.03584.md)
**Oktai Tatanov, Stanislav Beliaev, Boris Ginsburg** · 2021-10-07

<details>
<summary>Abstract</summary>

This paper describes Mixer-TTS, a non-autoregressive model for mel-spectrogram generation. The model is based on the MLP-Mixer architecture adapted for speech synthesis. The basic Mixer-TTS contains pitch and duration predictors, with the latter being trained with an unsupervised TTS alignment framework. Alongside the basic model, we propose the extended version which additionally uses token embeddings from a pre-trained language model. Basic Mixer-TTS and its extended version achieve a mean opinion score (MOS) of 4.05 and 4.11, respectively, compared to a MOS of 4.27 of original LJSpeech samples. Both versions have a small number of parameters and enable much faster speech synthesis compared to the models with similar quality.

</details>

### [VisualTTS: TTS with Accurate Lip-Speech Synchronization for Automatic Voice Over](2110.03342.md)
**Junchen Lu, Berrak Sisman, Rui Liu, Mingyang Zhang et al.** · 2021-10-07

<details>
<summary>Abstract</summary>

In this paper, we formulate a novel task to synthesize speech in sync with a silent pre-recorded video, denoted as automatic voice over (AVO). Unlike traditional speech synthesis, AVO seeks to generate not only human-sounding speech, but also perfect lip-speech synchronization. A natural solution to AVO is to condition the speech rendering on the temporal progression of lip sequence in the video. We propose a novel text-to-speech model that is conditioned on visual input, named VisualTTS, for accurate lip-speech synchronization. The proposed VisualTTS adopts two novel mechanisms that are 1) textual-visual attention, and 2) visual fusion strategy during acoustic decoding, which both contribute to forming accurate alignment between the input text content and lip motion in input lip sequence. Experimental results show that VisualTTS achieves accurate lip-speech synchronization and outperforms all baseline systems.

</details>

### [StrengthNet: Deep Learning-based Emotion Strength Assessment for Emotional Speech Synthesis](2110.03156.md)
**Rui Liu, Berrak Sisman, Haizhou Li** · 2021-10-07

<details>
<summary>Abstract</summary>

Recently, emotional speech synthesis has achieved remarkable performance. The emotion strength of synthesized speech can be controlled flexibly using a strength descriptor, which is obtained by an emotion attribute ranking function. However, a trained ranking function on specific data has poor generalization, which limits its applicability for more realistic cases. In this paper, we propose a deep learning based emotion strength assessment network for strength prediction that is referred to as StrengthNet. Our model conforms to a multi-task learning framework with a structure that includes an acoustic encoder, a strength predictor and an auxiliary emotion predictor. A data augmentation strategy was utilized to improve the model generalization. Experiments show that the predicted emotion strength of the proposed StrengthNet are highly correlated with ground truth scores for seen and unseen speech. Our codes are available at: https://github.com/ttslr/StrengthNet.

</details>

### [Towards Universal Neural Vocoding with a Multi-band Excited WaveNet](2110.03329.md)
**Axel Roebel, Frederik Bous** · 2021-10-07

<details>
<summary>Abstract</summary>

This paper introduces the Multi-Band Excited WaveNet a neural vocoder for speaking and singing voices. It aims to advance the state of the art towards an universal neural vocoder, which is a model that can generate voice signals from arbitrary mel spectrograms extracted from voice signals. Following the success of the DDSP model and following the development of the recently proposed excitation vocoders we propose a vocoder structure consisting of multiple specialized DNN that are combined with dedicated signal processing components. All components are implemented as differentiable operators and therefore allow joined optimization of the model parameters. To prove the capacity of the model to reproduce high quality voice signals we evaluate the model on single and multi speaker/singer datasets. We conduct a subjective evaluation demonstrating that the models support a wide range of domain variations (unseen voices, languages, expressivity) achieving perceptive quality that compares with a state of the art universal neural vocoder, however using significantly smaller training datasets and significantly less parameters. We also demonstrate remaining limits of the universality of neural vocoders e.g. the creation of saturated singing voices.

</details>

### [Voice Reenactment with F0 and timing constraints and adversarial learning of conversions](2110.03744.md)
**Frederik Bous, Laurent Benaroya, Nicolas Obin, Axel Roebel** · 2021-10-07

<details>
<summary>Abstract</summary>

This paper introduces voice reenactement as the task of voice conversion (VC) in which the expressivity of the source speaker is preserved during conversion while the identity of a target speaker is transferred. To do so, an original neural- VC architecture is proposed based on sequence-to-sequence voice conversion (S2S-VC) in which the speech prosody of the source speaker is preserved during conversion. First, the S2S-VC architecture is modified so as to synchronize the converted speech with the source speech by mean of phonetic duration encoding; second, the decoder is conditioned on the desired sequence of F0- values and an explicit F0-loss is formulated between the F0 of the source speaker and the one of the converted speech. Besides, an adversarial learning of conversions is integrated within the S2S-VC architecture so as to exploit both advantages of reconstruction of original speech and converted speech with manipulated attributes during training and then reducing the inconsistency between training and conversion. An experimental evaluation on the VCTK speech database shows that the speech prosody can be efficiently preserved during conversion, and that the proposed adversarial learning consistently improves the conversion and the naturalness of the reenacted speech.

</details>

### [Emphasis control for parallel neural TTS](2110.03012.md)
**Shreyas Seshadri, Tuomo Raitio, Dan Castellani, Jiangchuan Li** · 2021-10-06

<details>
<summary>Abstract</summary>

Recent parallel neural text-to-speech (TTS) synthesis methods are able to generate speech with high fidelity while maintaining high performance. However, these systems often lack control over the output prosody, thus restricting the semantic information conveyable for a given text. This paper proposes a hierarchical parallel neural TTS system for prosodic emphasis control by learning a latent space that directly corresponds to a change in emphasis. Three candidate features for the latent space are compared: 1) Variance of pitch and duration within words in a sentence, 2) Wavelet-based feature computed from pitch, energy, and duration, and 3) Learned combination of the two aforementioned approaches. At inference time, word-level prosodic emphasis is achieved by increasing the feature values of the latent space for the given words. Experiments show that all the proposed methods are able to achieve the perception of increased emphasis with little loss in overall quality. Moreover, emphasized utterances were preferred in a pairwise comparison test over the non-emphasized utterances, indicating promise for real-world applications.

</details>

### [Hierarchical prosody modeling and control in non-autoregressive parallel neural TTS](2110.02952.md)
**Tuomo Raitio, Jiangchuan Li, Shreyas Seshadri** · 2021-10-06

<details>
<summary>Abstract</summary>

Neural text-to-speech (TTS) synthesis can generate speech that is indistinguishable from natural speech. However, the synthetic speech often represents the average prosodic style of the database instead of having more versatile prosodic variation. Moreover, many models lack the ability to control the output prosody, which does not allow for different styles for the same text input. In this work, we train a non-autoregressive parallel neural TTS front-end model hierarchically conditioned on both coarse and fine-grained acoustic speech features to learn a latent prosody space with intuitive and meaningful dimensions. Experiments show that a non-autoregressive TTS model hierarchically conditioned on utterance-wise pitch, pitch range, duration, energy, and spectral tilt can effectively control each prosodic dimension, generate a wide variety of speaking styles, and provide word-wise emphasis control, while maintaining equal or better quality to the baseline model.

</details>

### [Style Equalization: Unsupervised Learning of Controllable Generative Sequence Models](2110.02891.md)
**Jen-Hao Rick Chang, Ashish Shrivastava, Hema Swetha Koppula, Xiaoshuai Zhang et al.** · 2021-10-06

<details>
<summary>Abstract</summary>

Controllable generative sequence models with the capability to extract and replicate the style of specific examples enable many applications, including narrating audiobooks in different voices, auto-completing and auto-correcting written handwriting, and generating missing training samples for downstream recognition tasks. However, under an unsupervised-style setting, typical training algorithms for controllable sequence generative models suffer from the training-inference mismatch, where the same sample is used as content and style input during training but unpaired samples are given during inference. In this paper, we tackle the training-inference mismatch encountered during unsupervised learning of controllable generative sequence models. The proposed method is simple yet effective, where we use a style transformation module to transfer target style information into an unrelated style input. This method enables training using unpaired content and style samples and thereby mitigate the training-inference mismatch. We apply style equalization to text-to-speech and text-to-handwriting synthesis on three datasets. We conduct thorough evaluation, including both quantitative and qualitative user studies. Our results show that by mitigating the training-inference mismatch with the proposed style equalization, we achieve style replication scores comparable to real data in our user studies.

</details>

### [Prosody-TTS: An end-to-end speech synthesis system with prosody control](2110.02854.md)
**Giridhar Pamisetty, K. Sri Rama Murty** · 2021-10-06

<details>
<summary>Abstract</summary>

End-to-end text-to-speech synthesis systems achieved immense success in recent times, with improved naturalness and intelligibility. However, the end-to-end models, which primarily depend on the attention-based alignment, do not offer an explicit provision to modify/incorporate the desired prosody while synthesizing the signal. Moreover, the state-of-the-art end-to-end systems use autoregressive models for synthesis, making the prediction sequential. Hence, the inference time and the computational complexity are quite high. This paper proposes Prosody-TTS, an end-to-end speech synthesis model that combines the advantages of statistical parametric models and end-to-end neural network models. It also has a provision to modify or incorporate the desired prosody by controlling the fundamental frequency (f0) and the phone duration. Generating speech samples with appropriate prosody and rhythm helps in improving the naturalness of the synthesized speech. We explicitly model the duration of the phoneme and the f0 to have control over them during the synthesis. The model is trained in an end-to-end fashion to directly generate the speech waveform from the input text, which in turn depends on the auxiliary subtasks of predicting the phoneme duration, f0, and mel spectrogram. Experiments on the Telugu language data of the IndicTTS database show that the proposed Prosody-TTS model achieves state-of-the-art performance with a mean opinion score of 4.08, with a very low inference time.

</details>

### [GANtron: Emotional Speech Synthesis with Generative Adversarial Networks](2110.03390.md)
**Enrique Hortal, Rodrigo Brechard Alarcia** · 2021-10-06

<details>
<summary>Abstract</summary>

Speech synthesis is used in a wide variety of industries. Nonetheless, it always sounds flat or robotic. The state of the art methods that allow for prosody control are very cumbersome to use and do not allow easy tuning. To tackle some of these drawbacks, in this work we target the implementation of a text-to-speech model where the inferred speech can be tuned with the desired emotions. To do so, we use Generative Adversarial Networks (GANs) together with a sequence-to-sequence model using an attention mechanism. We evaluate four different configurations considering different inputs and training strategies, study them and prove how our best model can generate speech files that lie in the same distribution as the initial training dataset. Additionally, a new strategy to boost the training convergence by applying a guided attention loss is proposed.

</details>

### [EdiTTS: Score-based Editing for Controllable Text-to-Speech](2110.02584.md)
**Jaesung Tae, Hyeongju Kim, Taesu Kim** · 2021-10-06

<details>
<summary>Abstract</summary>

We present EdiTTS, an off-the-shelf speech editing methodology based on score-based generative modeling for text-to-speech synthesis. EdiTTS allows for targeted, granular editing of audio, both in terms of content and pitch, without the need for any additional training, task-specific optimization, or architectural modifications to the score-based model backbone. Specifically, we apply coarse yet deliberate perturbations in the Gaussian prior space to induce desired behavior from the diffusion model while applying masks and softening kernels to ensure that iterative edits are applied only to the target region. Through listening tests and speech-to-text back transcription, we show that EdiTTS outperforms existing baselines and produces robust samples that satisfy user-imposed requirements.

</details>

### [MediumVC: Any-to-any voice conversion using synthetic specific-speaker speeches as intermedium features](2110.02500.md)
**Yewei Gu, Zhenyu Zhang, Xiaowei Yi, Xianfeng Zhao** · 2021-10-06

<details>
<summary>Abstract</summary>

To realize any-to-any (A2A) voice conversion (VC), most methods are to perform symmetric self-supervised reconstruction tasks (Xi to Xi), which usually results in inefficient performances due to inadequate feature decoupling, especially for unseen speakers. We propose a two-stage reconstruction task (Xi to Yi to Xi) using synthetic specific-speaker speeches as intermedium features, where A2A VC is divided into two stages: any-to-one (A2O) and one-to-Any (O2A). In the A2O stage, we propose a new A2O method: SingleVC, by employing a noval data augment strategy(pitch-shifted and duration-remained, PSDR) to accomplish Xi to Yi. In the O2A stage, MediumVC is proposed based on pre-trained SingleVC to conduct Yi to Xi. Through such asymmetrical reconstruction tasks (Xi to Yi in SingleVC and Yi to Xi in MediumVC), the models are to capture robust disentangled features purposefully. Experiments indicate MediumVC can enhance the similarity of converted speeches while maintaining a high degree of naturalness.

</details>

### [On the Interplay Between Sparsity, Naturalness, Intelligibility, and Prosody in Speech Synthesis](2110.01147.md)
**Cheng-I Jeff Lai, Erica Cooper, Yang Zhang, Shiyu Chang et al.** · 2021-10-04

<details>
<summary>Abstract</summary>

Are end-to-end text-to-speech (TTS) models over-parametrized? To what extent can these models be pruned, and what happens to their synthesis capabilities? This work serves as a starting point to explore pruning both spectrogram prediction networks and vocoders. We thoroughly investigate the tradeoffs between sparsity and its subsequent effects on synthetic speech. Additionally, we explored several aspects of TTS pruning: amount of finetuning data versus sparsity, TTS-Augmentation to utilize unspoken text, and combining knowledge distillation and pruning. Our findings suggest that not only are end-to-end TTS models highly prunable, but also, perhaps surprisingly, pruned TTS models can produce synthetic speech with equal or higher naturalness and intelligibility, with similar prosody. All of our experiments are conducted on publicly available models, and findings in this work are backed by large-scale subjective tests and objective measures. Code and 200 pruned models are made available to facilitate future research on efficiency in TTS.

</details>

### [Decoupling Speaker-Independent Emotions for Voice Conversion Via Source-Filter Networks](2110.01164.md)
**Zhaojie Luo, Shoufeng Lin, Rui Liu, Jun Baba et al.** · 2021-10-04

<details>
<summary>Abstract</summary>

Emotional voice conversion (VC) aims to convert a neutral voice to an emotional (e.g. happy) one while retaining the linguistic information and speaker identity. We note that the decoupling of emotional features from other speech information (such as speaker, content, etc.) is the key to achieving remarkable performance. Some recent attempts about speech representation decoupling on the neutral speech can not work well on the emotional speech, due to the more complex acoustic properties involved in the latter. To address this problem, here we propose a novel Source-Filter-based Emotional VC model (SFEVC) to achieve proper filtering of speaker-independent emotion features from both the timbre and pitch features. Our SFEVC model consists of multi-channel encoders, emotion separate encoders, and one decoder. Note that all encoder modules adopt a designed information bottlenecks auto-encoder. Additionally, to further improve the conversion quality for various emotions, a novel two-stage training strategy based on the 2D Valence-Arousal (VA) space was proposed. Experimental results show that the proposed SFEVC along with a two-stage training strategy outperforms all baselines and achieves the state-of-the-art performance in speaker-independent emotional VC with nonparallel data.

</details>

### [PortaSpeech: Portable and High-Quality Generative Text-to-Speech](2109.15166.md)
**Yi Ren, Jinglin Liu, Zhou Zhao** · 2021-09-30

<details>
<summary>Abstract</summary>

Non-autoregressive text-to-speech (NAR-TTS) models such as FastSpeech 2 and Glow-TTS can synthesize high-quality speech from the given text in parallel. After analyzing two kinds of generative NAR-TTS models (VAE and normalizing flow), we find that: VAE is good at capturing the long-range semantics features (e.g., prosody) even with small model size but suffers from blurry and unnatural results; and normalizing flow is good at reconstructing the frequency bin-wise details but performs poorly when the number of model parameters is limited. Inspired by these observations, to generate diverse speech with natural details and rich prosody using a lightweight architecture, we propose PortaSpeech, a portable and high-quality generative text-to-speech model. Specifically, 1) to model both the prosody and mel-spectrogram details accurately, we adopt a lightweight VAE with an enhanced prior followed by a flow-based post-net with strong conditional inputs as the main architecture. 2) To further compress the model size and memory footprint, we introduce the grouped parameter sharing mechanism to the affine coupling layers in the post-net. 3) To improve the expressiveness of synthesized speech and reduce the dependency on accurate fine-grained alignment between text and speech, we propose a linguistic encoder with mixture alignment combining hard inter-word alignment and soft intra-word alignment, which explicitly extracts word-level semantic information. Experimental results show that PortaSpeech outperforms other TTS models in both voice quality and prosody modeling in terms of subjective and objective evaluation metrics, and shows only a slight performance degradation when reducing the model parameters to 6.7M (about 4x model size and 3x runtime memory compression ratio compared with FastSpeech 2). Our extensive ablation studies demonstrate that each design in PortaSpeech is effective.

</details>

### [Diffusion-Based Voice Conversion with Fast Maximum Likelihood Sampling Scheme](2109.13821.md)
**Vadim Popov, Ivan Vovk, Vladimir Gogoryan, Tasnima Sadekova et al.** · 2021-09-28

<details>
<summary>Abstract</summary>

Voice conversion is a common speech synthesis task which can be solved in different ways depending on a particular real-world scenario. The most challenging one often referred to as one-shot many-to-many voice conversion consists in copying the target voice from only one reference utterance in the most general case when both source and target speakers do not belong to the training dataset. We present a scalable high-quality solution based on diffusion probabilistic modeling and demonstrate its superior quality compared to state-of-the-art one-shot voice conversion approaches. Moreover, focusing on real-time applications, we investigate general principles which can make diffusion models faster while keeping synthesis quality at a high level. As a result, we develop a novel Stochastic Differential Equations solver suitable for various diffusion model types and generative tasks as shown through empirical studies and justify it by theoretical analysis.

</details>

### [VoiceFixer: Toward General Speech Restoration with Neural Vocoder](2109.13731.md)
**Haohe Liu, Qiuqiang Kong, Qiao Tian, Yan Zhao et al.** · 2021-09-28

<details>
<summary>Abstract</summary>

Speech restoration aims to remove distortions in speech signals. Prior methods mainly focus on single-task speech restoration (SSR), such as speech denoising or speech declipping. However, SSR systems only focus on one task and do not address the general speech restoration problem. In addition, previous SSR systems show limited performance in some speech restoration tasks such as speech super-resolution. To overcome those limitations, we propose a general speech restoration (GSR) task that attempts to remove multiple distortions simultaneously. Furthermore, we propose VoiceFixer, a generative framework to address the GSR task. VoiceFixer consists of an analysis stage and a synthesis stage to mimic the speech analysis and comprehension of the human auditory system. We employ a ResUNet to model the analysis stage and a neural vocoder to model the synthesis stage. We evaluate VoiceFixer with additive noise, room reverberation, low-resolution, and clipping distortions. Our baseline GSR model achieves a 0.499 higher mean opinion score (MOS) than the speech enhancement SSR model. VoiceFixer further surpasses the GSR baseline model on the MOS score by 0.256. Moreover, we observe that VoiceFixer generalizes well to severely degraded real speech recordings, indicating its potential in restoring old movies and historical speeches. The source code is available at https://github.com/haoheliu/voicefixer_main.

</details>

### [MSR-NV: Neural Vocoder Using Multiple Sampling Rates](2109.13714.md)
**Kentaro Mitsui, Kei Sawada** · 2021-09-28

<details>
<summary>Abstract</summary>

The development of neural vocoders (NVs) has resulted in the high-quality and fast generation of waveforms. However, conventional NVs target a single sampling rate and require re-training when applied to different sampling rates. A suitable sampling rate varies from application to application due to the trade-off between speech quality and generation speed. In this study, we propose a method to handle multiple sampling rates in a single NV, called the MSR-NV. By generating waveforms step-by-step starting from a low sampling rate, MSR-NV can efficiently learn the characteristics of each frequency band and synthesize high-quality speech at multiple sampling rates. It can be regarded as an extension of the previously proposed NVs, and in this study, we extend the structure of Parallel WaveGAN (PWG). Experimental evaluation results demonstrate that the proposed method achieves remarkably higher subjective quality than the original PWG trained separately at 16, 24, and 48 kHz, without increasing the inference time. We also show that MSR-NV can leverage speech with lower sampling rates to further improve the quality of the synthetic speech.

</details>

### [FlowVocoder: A small Footprint Neural Vocoder based Normalizing flow for Speech Synthesis](2109.13675.md)
**Manh Luong, Viet Anh Tran** · 2021-09-27

<details>
<summary>Abstract</summary>

Recently, autoregressive neural vocoders have provided remarkable performance in generating high-fidelity speech and have been able to produce synthetic speech in real-time. However, autoregressive neural vocoders such as WaveFlow are capable of modeling waveform signals from mel-spectrogram, its number of parameters is significant to deploy on edge devices. Though NanoFlow, which has a small number of parameters, is a state-of-the-art autoregressive neural vocoder, the performance of NanoFlow is marginally lower than WaveFlow. Therefore, we propose a new type of autoregressive neural vocoder called FlowVocoder, which has a small memory footprint and is capable of generating high-fidelity audio in real-time. Our proposed model improves the density estimation of flow blocks by utilizing a mixture of Cumulative Distribution Functions (CDF) for bipartite transformation. Hence, the proposed model is capable of modeling waveform signals, while its memory footprint is much smaller than WaveFlow. As shown in experiments, FlowVocoder achieves competitive results with baseline methods in terms of both subjective and objective evaluation, also, it is more suitable for real-time text-to-speech applications.

</details>

### [Acoustic Word Embeddings for End-to-End Speech Synthesis](s2:b7f2f04edd37b012e3c52ecf47af1c99e87127e1.md)
**Feiyu Shen, Chenpeng Du, K. Yu** · 2021-09-27

<details>
<summary>Abstract</summary>

The most recent end-to-end speech synthesis systems use phonemes as acoustic input tokens and ignore the information about which word the phonemes come from. However, many words have their specific prosody type, which may significantly affect the naturalness. Prior works have employed pre-trained linguistic word embeddings as TTS system input. However, since linguistic information is not directly relevant to how words are pronounced, TTS quality improvement of these systems is mild. In this paper, we propose a novel and effective way of jointly training acoustic phone and word embeddings for end-to-end TTS systems. Experiments on the LJSpeech dataset show that the acoustic word embeddings dramatically decrease both the training and validation loss in phone-level prosody prediction. Subjective evaluations on naturalness demonstrate that the incorporation of acoustic word embeddings can significantly outperform both pure phone-based system and the TTS system with pre-trained linguistic word embedding.

</details>

### [A Proposal of Automatic Error Correction in Text](2112.01846.md)
**Wulfrano A. Luna-Ramírez, Carlos R. Jaimez-González** · 2021-09-24

<details>
<summary>Abstract</summary>

The great amount of information that can be stored in electronic media is growing up daily. Many of them is got mainly by typing, such as the huge of information obtained from web 2.0 sites; or scaned and processing by an Optical Character Recognition software, like the texts of libraries and goverment offices. Both processes introduce error in texts, so it is difficult to use the data for other purposes than just to read it, i.e. the processing of those texts by other applications like e-learning, learning of languages, electronic tutorials, data minning, information retrieval and even more specialized systems such as tiflologic software, specifically blinded people-oriented applications like automatic reading, where the text would be error free as possible in order to make easier the text to speech task, and so on. In this paper it is showed an application of automatic recognition and correction of ortographic errors in electronic texts. This task is composed of three stages: a) error detection; b) candidate corrections generation; and c) correction -selection of the best candidate. The proposal is based in part of speech text categorization, word similarity, word diccionaries, statistical measures, morphologic analisys and n-grams based language model of Spanish.

</details>

### [Unet-TTS: Improving Unseen Speaker and Style Transfer in One-shot Voice Cloning](2109.11115.md)
**Rui Li, Dong Pu, Minnie Huang, Bill Huang** · 2021-09-23

<details>
<summary>Abstract</summary>

One-shot voice cloning aims to transform speaker voice and speaking style in speech synthesized from a text-to-speech (TTS) system, where only a shot recording from the target reference speech can be used. Out-of-domain transfer is still a challenging task, and one important aspect that impacts the accuracy and similarity of synthetic speech is the conditional representations carrying speaker or style cues extracted from the limited references. In this paper, we present a novel one-shot voice cloning algorithm called Unet-TTS that has good generalization ability for unseen speakers and styles. Based on a skip-connected U-net structure, the new model can efficiently discover speaker-level and utterance-level spectral feature details from the reference audio, enabling accurate inference of complex acoustic characteristics as well as imitation of speaking styles into the synthetic speech. According to both subjective and objective evaluations of similarity, the new model outperforms both speaker embedding and unsupervised style modeling (GST) approaches on an unseen emotional corpus.

</details>

### [Low-Latency Incremental Text-to-Speech Synthesis with Distilled Context Prediction Network](2109.10724.md)
**Takaaki Saeki, Shinnosuke Takamichi, Hiroshi Saruwatari** · 2021-09-22

<details>
<summary>Abstract</summary>

Incremental text-to-speech (TTS) synthesis generates utterances in small linguistic units for the sake of real-time and low-latency applications. We previously proposed an incremental TTS method that leverages a large pre-trained language model to take unobserved future context into account without waiting for the subsequent segment. Although this method achieves comparable speech quality to that of a method that waits for the future context, it entails a huge amount of processing for sampling from the language model at each time step. In this paper, we propose an incremental TTS method that directly predicts the unobserved future context with a lightweight model, instead of sampling words from the large-scale language model. We perform knowledge distillation from a GPT2-based context prediction network into a simple recurrent model by minimizing a teacher-student loss defined between the context embedding vectors of those models. Experimental results show that the proposed method requires about ten times less inference time to achieve comparable synthetic speech quality to that of our previous method, and it can perform incremental synthesis much faster than the average speaking speed of human English speakers, demonstrating the availability of our method to real-time applications.

</details>

### [On-device neural speech synthesis](2109.08710.md)
**Sivanand Achanta, Albert Antony, Ladan Golipour, Jiangchuan Li et al.** · 2021-09-17

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) synthesis, such as Tacotron and WaveRNN, have made it possible to construct a fully neural network based TTS system, by coupling the two components together. Such a system is conceptually simple as it only takes grapheme or phoneme input, uses Mel-spectrogram as an intermediate feature, and directly generates speech samples. The system achieves quality equal or close to natural speech. However, the high computational cost of the system and issues with robustness have limited their usage in real-world speech synthesis applications and products. In this paper, we present key modeling improvements and optimization strategies that enable deploying these models, not only on GPU servers, but also on mobile devices. The proposed system can generate high-quality 24 kHz speech at 5x faster than real time on server and 3x faster than real time on mobile devices.

</details>

### [fairseq S^2: A Scalable and Integrable Speech Synthesis Toolkit](2109.06912.md)
**Changhan Wang, Wei-Ning Hsu, Yossi Adi, Adam Polyak et al.** · 2021-09-14

<details>
<summary>Abstract</summary>

This paper presents fairseq S^2, a fairseq extension for speech synthesis. We implement a number of autoregressive (AR) and non-AR text-to-speech models, and their multi-speaker variants. To enable training speech synthesis models with less curated data, a number of preprocessing tools are built and their importance is shown empirically. To facilitate faster iteration of development and analysis, a suite of automatic metrics is included. Apart from the features added specifically for this extension, fairseq S^2 also benefits from the scalability offered by fairseq and can be easily integrated with other state-of-the-art systems provided in this framework. The code, documentation, and pre-trained models are available at https://github.com/pytorch/fairseq/tree/master/examples/speech_synthesis.

</details>

### [Cross-speaker emotion disentangling and transfer for end-to-end speech synthesis](2109.06733.md)
**Tao Li, Xinsheng Wang, Qicong Xie, Zhichao Wang et al.** · 2021-09-14

<details>
<summary>Abstract</summary>

The cross-speaker emotion transfer task in text-to-speech (TTS) synthesis particularly aims to synthesize speech for a target speaker with the emotion transferred from reference speech recorded by another (source) speaker. During the emotion transfer process, the identity information of the source speaker could also affect the synthesized results, resulting in the issue of speaker leakage. This paper proposes a new method with the aim to synthesize controllable emotional expressive speech and meanwhile maintain the target speaker's identity in the cross-speaker emotion TTS task. The proposed method is a Tacotron2-based framework with emotion embedding as the conditioning variable to provide emotion information. Two emotion disentangling modules are contained in our method to 1) get speaker-irrelevant and emotion-discriminative embedding, and 2) explicitly constrain the emotion and speaker identity of synthetic speech to be that as expected. Moreover, we present an intuitive method to control the emotion strength in the synthetic speech for the target speaker. Specifically, the learned emotion embedding is adjusted with a flexible scalar value, which allows controlling the emotion strength conveyed by the embedding. Extensive experiments have been conducted on a Mandarin disjoint corpus, and the results demonstrate that the proposed method is able to synthesize reasonable emotional speech for the target speaker. Compared to the state-of-the-art reference embedding learned methods, our method gets the best performance on the cross-speaker emotion transfer task, indicating that our method achieves the new state-of-the-art performance on learning the speaker-irrelevant emotion embedding. Furthermore, the strength ranking test and pitch trajectories plots demonstrate that the proposed method can effectively control the emotion strength, leading to prosody-diverse synthetic speech.

</details>

### [Zero-Shot Text-to-Speech for Text-Based Insertion in Audio Narration](2109.05426.md)
**Chuanxin Tang, Chong Luo, Zhiyuan Zhao, Dacheng Yin et al.** · 2021-09-12

<details>
<summary>Abstract</summary>

Given a piece of speech and its transcript text, text-based speech editing aims to generate speech that can be seamlessly inserted into the given speech by editing the transcript. Existing methods adopt a two-stage approach: synthesize the input text using a generic text-to-speech (TTS) engine and then transform the voice to the desired voice using voice conversion (VC). A major problem of this framework is that VC is a challenging problem which usually needs a moderate amount of parallel training data to work satisfactorily. In this paper, we propose a one-stage context-aware framework to generate natural and coherent target speech without any training data of the target speaker. In particular, we manage to perform accurate zero-shot duration prediction for the inserted text. The predicted duration is used to regulate both text embedding and speech embedding. Then, based on the aligned cross-modality input, we directly generate the mel-spectrogram of the edited speech with a transformer-based decoder. Subjective listening tests show that despite the lack of training data for the speaker, our method has achieved satisfactory results. It outperforms a recent zero-shot TTS engine by a large margin.

</details>

### [Referee: Towards reference-free cross-speaker style transfer with low-quality data for expressive speech synthesis](2109.03439.md)
**Songxiang Liu, Shan Yang, Dan Su, Dong Yu** · 2021-09-08

<details>
<summary>Abstract</summary>

Cross-speaker style transfer (CSST) in text-to-speech (TTS) synthesis aims at transferring a speaking style to the synthesised speech in a target speaker's voice. Most previous CSST approaches rely on expensive high-quality data carrying desired speaking style during training and require a reference utterance to obtain speaking style descriptors as conditioning on the generation of a new sentence. This work presents Referee, a robust reference-free CSST approach for expressive TTS, which fully leverages low-quality data to learn speaking styles from text. Referee is built by cascading a text-to-style (T2S) model with a style-to-wave (S2W) model. Phonetic PosteriorGram (PPG), phoneme-level pitch and energy contours are adopted as fine-grained speaking style descriptors, which are predicted from text using the T2S model. A novel pretrain-refinement method is adopted to learn a robust T2S model by only using readily accessible low-quality data. The S2W model is trained with high-quality target data, which is adopted to effectively aggregate style descriptors and generate high-fidelity speech in the target speaker's voice. Experimental results are presented, showing that Referee outperforms a global-style-token (GST)-based baseline approach in CSST.

</details>

### [Time Alignment using Lip Images for Frame-based Electrolaryngeal Voice Conversion](2109.03551.md)
**Yi-Syuan Liou, Wen-Chin Huang, Ming-Chi Yen, Shu-Wei Tsai et al.** · 2021-09-08

<details>
<summary>Abstract</summary>

Voice conversion (VC) is an effective approach to electrolaryngeal (EL) speech enhancement, a task that aims to improve the quality of the artificial voice from an electrolarynx device. In frame-based VC methods, time alignment needs to be performed prior to model training, and the dynamic time warping (DTW) algorithm is widely adopted to compute the best time alignment between each utterance pair. The validity is based on the assumption that the same phonemes of the speakers have similar features and can be mapped by measuring a pre-defined distance between speech frames of the source and the target. However, the special characteristics of the EL speech can break the assumption, resulting in a sub-optimal DTW alignment. In this work, we propose to use lip images for time alignment, as we assume that the lip movements of laryngectomee remain normal compared to healthy people. We investigate two naive lip representations and distance metrics, and experimental results demonstrate that the proposed method can significantly outperform the audio-only alignment in terms of objective and subjective evaluations.

</details>

### [CE-Tacotron2: End-to-End Emotional Speech Synthesis](s2:eb6231480f2375f4ece03c5d709d58dfa9a7a33e.md)
**Zhi Wang, Yinhua Liu, Liang Shan** · 2021-09-08

### [Neural Sequence-to-Sequence Speech Synthesis Using a Hidden Semi-Markov Model Based Structured Attention Mechanism](2108.13985.md)
**Yoshihiko Nankaku, Kenta Sumiya, Takenori Yoshimura, Shinji Takaki et al.** · 2021-08-31

<details>
<summary>Abstract</summary>

This paper proposes a novel Sequence-to-Sequence (Seq2Seq) model integrating the structure of Hidden Semi-Markov Models (HSMMs) into its attention mechanism. In speech synthesis, it has been shown that methods based on Seq2Seq models using deep neural networks can synthesize high quality speech under the appropriate conditions. However, several essential problems still have remained, i.e., requiring large amounts of training data due to an excessive degree for freedom in alignment (mapping function between two sequences), and the difficulty in handling duration due to the lack of explicit duration modeling. The proposed method defines a generative models to realize the simultaneous optimization of alignments and model parameters based on the Variational Auto-Encoder (VAE) framework, and provides monotonic alignments and explicit duration modeling based on the structure of HSMM. The proposed method can be regarded as an integration of Hidden Markov Model (HMM) based speech synthesis and deep learning based speech synthesis using Seq2Seq models, incorporating both the benefits. Subjective evaluation experiments showed that the proposed method obtained higher mean opinion scores than Tacotron 2 on relatively small amount of training data.

</details>

### [Neural HMMs are all you need (for high-quality attention-free TTS)](2108.13320.md)
**Shivam Mehta, Éva Székely, Jonas Beskow, Gustav Eje Henter** · 2021-08-30

<details>
<summary>Abstract</summary>

Neural sequence-to-sequence TTS has achieved significantly better output quality than statistical speech synthesis using HMMs. However, neural TTS is generally not probabilistic and uses non-monotonic attention. Attention failures increase training time and can make synthesis babble incoherently. This paper describes how the old and new paradigms can be combined to obtain the advantages of both worlds, by replacing attention in neural TTS with an autoregressive left-right no-skip hidden Markov model defined by a neural network. Based on this proposal, we modify Tacotron 2 to obtain an HMM-based neural TTS model with monotonic alignment, trained to maximise the full sequence likelihood without approximation. We also describe how to combine ideas from classical and contemporary TTS for best results. The resulting example system is smaller and simpler than Tacotron 2, and learns to speak with fewer iterations and less data, whilst achieving comparable naturalness prior to the post-net. Our approach also allows easy control over speaking rate.

</details>

### [Fine-Grained Prosody Modeling in Neural Speech Synthesis Using ToBI Representation](s2:89a74c51e757aa5c905d264224b10183fd6e7d07.md)
**Yuxiang Zou, Shichao Liu, Xiang Yin, Haopeng Lin et al.** · 2021-08-30

<details>
<summary>Abstract</summary>

Beneﬁting from the great development of deep learning, modern neural text-to-speech (TTS) models can generate speech indistinguishable from natural speech. However, The generated utterances often keep an average prosodic style of the database instead of having rich prosodic variation. For pitch-stressed languages, such as English, accurate intonation and stress are important for conveying semantic information. In this work, we propose a ﬁne-grained prosody modeling method in neural speech synthesis with ToBI (Tones and Break Indices) representation. The proposed system consists of a text fron-tend for ToBI prediction and a Tacotron-based TTS module for prosody modeling. By introducing the ToBI representation, we can control the system to synthesize speech with accurate into-nation and stress at syllable level. Compared with the two base-lines (Tacotron and unsupervised method), experiments show that our model can generate more natural speech with more accurate prosody, as well as effectively control the stress, intonation, and pause of the speech.

</details>

### [Integrated Speech and Gesture Synthesis](2108.11436.md)
**Siyang Wang, Simon Alexanderson, Joakim Gustafson, Jonas Beskow et al.** · 2021-08-25

<details>
<summary>Abstract</summary>

Text-to-speech and co-speech gesture synthesis have until now been treated as separate areas by two different research communities, and applications merely stack the two technologies using a simple system-level pipeline. This can lead to modeling inefficiencies and may introduce inconsistencies that limit the achievable naturalness. We propose to instead synthesize the two modalities in a single model, a new problem we call integrated speech and gesture synthesis (ISG). We also propose a set of models modified from state-of-the-art neural speech-synthesis engines to achieve this goal. We evaluate the models in three carefully-designed user studies, two of which evaluate the synthesized speech and gesture in isolation, plus a combined study that evaluates the models like they will be used in real-world applications -- speech and gesture presented together. The results show that participants rate one of the proposed integrated synthesis models as being as good as the state-of-the-art pipeline system we compare against, in all three tests. The model is able to achieve this with faster synthesis time and greatly reduced parameter count compared to the pipeline system, illustrating some of the potential benefits of treating speech and gesture synthesis together as a single, unified problem. Videos and code are available on our project page at https://swatsw.github.io/isg_icmi21/

</details>

### [One TTS Alignment To Rule Them All](2108.10447.md)
**Rohan Badlani, Adrian Łancucki, Kevin J. Shih, Rafael Valle et al.** · 2021-08-23

<details>
<summary>Abstract</summary>

Speech-to-text alignment is a critical component of neural textto-speech (TTS) models. Autoregressive TTS models typically use an attention mechanism to learn these alignments on-line. However, these alignments tend to be brittle and often fail to generalize to long utterances and out-of-domain text, leading to missing or repeating words. Most non-autoregressive endto-end TTS models rely on durations extracted from external sources. In this paper we leverage the alignment mechanism proposed in RAD-TTS as a generic alignment learning framework, easily applicable to a variety of neural TTS models. The framework combines forward-sum algorithm, the Viterbi algorithm, and a simple and efficient static prior. In our experiments, the alignment learning framework improves all tested TTS architectures, both autoregressive (Flowtron, Tacotron 2) and non-autoregressive (FastPitch, FastSpeech 2, RAD-TTS). Specifically, it improves alignment convergence speed of existing attention-based mechanisms, simplifies the training pipeline, and makes the models more robust to errors on long utterances. Most importantly, the framework improves the perceived speech synthesis quality, as judged by human evaluators.

</details>

### [Improving transfer of expressivity for end-to-end multispeaker text-to-speech synthesis](s2:66946b15a1399794d72542c7d22cad44c1ba6c8f.md)
**Ajinkya Kulkarni, Vincent Colotte, D. Jouvet** · 2021-08-23

<details>
<summary>Abstract</summary>

The main goal of this work is to generate expressive speech in different speaker's voices for which no expressive speech data is available. The presented approach conditions Tacotron 2 speech synthesis with latent representations extracted from text, speaker identity, and reference expressive Mel spectrogram. We propose to use multiclass N-pair loss in the end-to-end multispeaker expressive Text-To-Speech (TTS) for improving the transfer of expressivity to the target speaker's voice. We have jointly trained the end-to-end (E2E) TTS with multiclass N-pair loss to discriminate between various emotions. This augmentation of the loss function during training paves the way to enhance the latent space representation of emotions. We have experimented with two different neural network architectures for expressivity in the encoder, namely global style token (GST) and variational autoencoder (VAE). We transferred the expressivity using the mean of latent representation extracted from the expressivity encoder for each emotion. The obtained results show that adding multiclass N-pair loss based deep metric learning in the training process improves expressivity in the desired speaker's voice.

</details>

### [GC-TTS: Few-shot Speaker Adaptation with Geometric Constraints](2108.06890.md)
**Ji-Hoon Kim, Sang-Hoon Lee, Ji-Hyun Lee, Hong-Gyu Jung et al.** · 2021-08-16

<details>
<summary>Abstract</summary>

Few-shot speaker adaptation is a specific Text-to-Speech (TTS) system that aims to reproduce a novel speaker's voice with a few training data. While numerous attempts have been made to the few-shot speaker adaptation system, there is still a gap in terms of speaker similarity to the target speaker depending on the amount of data. To bridge the gap, we propose GC-TTS which achieves high-quality speaker adaptation with significantly improved speaker similarity. Specifically, we leverage two geometric constraints to learn discriminative speaker representations. Here, a TTS model is pre-trained for base speakers with a sufficient amount of data, and then fine-tuned for novel speakers on a few minutes of data with two geometric constraints. Two geometric constraints enable the model to extract discriminative speaker embeddings from limited data, which leads to the synthesis of intelligible speech. We discuss and verify the effectiveness of GC-TTS by comparing it with popular and essential methods. The experimental results demonstrate that GC-TTS generates high-quality speech from only a few minutes of training data, outperforming standard techniques in terms of speaker similarity to the target speaker.

</details>

### [Enhancing audio quality for expressive Neural Text-to-Speech](2108.06270.md)
**Abdelhamid Ezzerg, Adam Gabrys, Bartosz Putrycz, Daniel Korzekwa et al.** · 2021-08-13

<details>
<summary>Abstract</summary>

Artificial speech synthesis has made a great leap in terms of naturalness as recent Text-to-Speech (TTS) systems are capable of producing speech with similar quality to human recordings. However, not all speaking styles are easy to model: highly expressive voices are still challenging even to recent TTS architectures since there seems to be a trade-off between expressiveness in a generated audio and its signal quality. In this paper, we present a set of techniques that can be leveraged to enhance the signal quality of a highly-expressive voice without the use of additional data. The proposed techniques include: tuning the autoregressive loop's granularity during training; using Generative Adversarial Networks in acoustic modelling; and the use of Variational Auto-Encoders in both the acoustic model and the neural vocoder. We show that, when combined, these techniques greatly closed the gap in perceived naturalness between the baseline system and recordings by 39% in terms of MUSHRA scores for an expressive celebrity voice.

</details>

### [AnyoneNet: Synchronized Speech and Talking Head Generation for Arbitrary Person](2108.04325.md)
**Xinsheng Wang, Qicong Xie, Jihua Zhu, Lei Xie et al.** · 2021-08-09

<details>
<summary>Abstract</summary>

Automatically generating videos in which synthesized speech is synchronized with lip movements in a talking head has great potential in many human-computer interaction scenarios. In this paper, we present an automatic method to generate synchronized speech and talking-head videos on the basis of text and a single face image of an arbitrary person as input. In contrast to previous text-driven talking head generation methods, which can only synthesize the voice of a specific person, the proposed method is capable of synthesizing speech for any person that is inaccessible in the training stage. Specifically, the proposed method decomposes the generation of synchronized speech and talking head videos into two stages, i.e., a text-to-speech (TTS) stage and a speech-driven talking head generation stage. The proposed TTS module is a face-conditioned multi-speaker TTS model that gets the speaker identity information from face images instead of speech, which allows us to synthesize a personalized voice on the basis of the input face image. To generate the talking head videos from the face images, a facial landmark-based method that can predict both lip movements and head rotations is proposed. Extensive experiments demonstrate that the proposed method is able to generate synchronized speech and talking head videos for arbitrary persons and non-persons. Synthesized speech shows consistency with the given face regarding to the synthesized voice's timbre and one's appearance in the image, and the proposed landmark-based talking head method outperforms the state-of-the-art landmark-based method on generating natural talking head videos.

</details>

### [A Streamwise GAN Vocoder for Wideband Speech Coding at Very Low Bit Rate](2108.04051.md)
**Ahmed Mustafa, Jan Büthe, Srikanth Korse, Kishan Gupta et al.** · 2021-08-09

<details>
<summary>Abstract</summary>

Recently, GAN vocoders have seen rapid progress in speech synthesis, starting to outperform autoregressive models in perceptual quality with much higher generation speed. However, autoregressive vocoders are still the common choice for neural generation of speech signals coded at very low bit rates. In this paper, we present a GAN vocoder which is able to generate wideband speech waveforms from parameters coded at 1.6 kbit/s. The proposed model is a modified version of the StyleMelGAN vocoder that can run in frame-by-frame manner, making it suitable for streaming applications. The experimental results show that the proposed model significantly outperforms prior autoregressive vocoders like LPCNet for very low bit rate speech coding, with computational complexity of about 5 GMACs, providing a new state of the art in this domain. Moreover, this streamwise adversarial vocoder delivers quality competitive to advanced speech codecs such as EVS at 5.9 kbit/s on clean speech, which motivates further usage of feed-forward fully-convolutional models for low bit rate speech coding.

</details>

### [Sinsy: A Deep Neural Network-Based Singing Voice Synthesis System](2108.02776.md)
**Yukiya Hono, Kei Hashimoto, Keiichiro Oura, Yoshihiko Nankaku et al.** · 2021-08-05

<details>
<summary>Abstract</summary>

This paper presents Sinsy, a deep neural network (DNN)-based singing voice synthesis (SVS) system. In recent years, DNNs have been utilized in statistical parametric SVS systems, and DNN-based SVS systems have demonstrated better performance than conventional hidden Markov model-based ones. SVS systems are required to synthesize a singing voice with pitch and timing that strictly follow a given musical score. Additionally, singing expressions that are not described on the musical score, such as vibrato and timing fluctuations, should be reproduced. The proposed system is composed of four modules: a time-lag model, a duration model, an acoustic model, and a vocoder, and singing voices can be synthesized taking these characteristics of singing voices into account. To better model a singing voice, the proposed system incorporates improved approaches to modeling pitch and vibrato and better training criteria into the acoustic model. In addition, we incorporated PeriodNet, a non-autoregressive neural vocoder with robustness for the pitch, into our systems to generate a high-fidelity singing voice waveform. Moreover, we propose automatic pitch correction techniques for DNN-based SVS to synthesize singing voices with correct pitch even if the training data has out-of-tune phrases. Experimental results show our system can synthesize a singing voice with better timing, more natural vibrato, and correct pitch, and it can achieve better mean opinion scores in subjective evaluation tests.

</details>

### [Applying the Information Bottleneck Principle to Prosodic Representation Learning](2108.02821.md)
**Guangyan Zhang, Ying Qin, Daxin Tan, Tan Lee** · 2021-08-05

<details>
<summary>Abstract</summary>

This paper describes a novel design of a neural network-based speech generation model for learning prosodic representation.The problem of representation learning is formulated according to the information bottleneck (IB) principle. A modified VQ-VAE quantized layer is incorporated in the speech generation model to control the IB capacity and adjust the balance between reconstruction power and disentangle capability of the learned representation. The proposed model is able to learn word-level prosodic representations from speech data. With an optimized IB capacity, the learned representations not only are adequate to reconstruct the original speech but also can be used to transfer the prosody onto different textual content. Extensive results of the objective and subjective evaluation are presented to demonstrate the effect of IB capacity control, the effectiveness, and potential usage of the learned prosodic representation in controllable neural speech generation.

</details>

### [Information Sieve: Content Leakage Reduction in End-to-End Prosody For Expressive Speech Synthesis](2108.01831.md)
**Xudong Dai, Cheng Gong, Longbiao Wang, Kaili Zhang** · 2021-08-04

<details>
<summary>Abstract</summary>

Expressive neural text-to-speech (TTS) systems incorporate a style encoder to learn a latent embedding as the style information. However, this embedding process may encode redundant textual information. This phenomenon is called content leakage. Researchers have attempted to resolve this problem by adding an ASR or other auxiliary supervision loss functions. In this study, we propose an unsupervised method called the "information sieve" to reduce the effect of content leakage in prosody transfer. The rationale of this approach is that the style encoder can be forced to focus on style information rather than on textual information contained in the reference speech by a well-designed downsample-upsample filter, i.e., the extracted style embeddings can be downsampled at a certain interval and then upsampled by duplication. Furthermore, we used instance normalization in convolution layers to help the system learn a better latent style space. Objective metrics such as the significantly lower word error rate (WER) demonstrate the effectiveness of this model in mitigating content leakage. Listening tests indicate that the model retains its prosody transferability compared with the baseline models such as the original GST-Tacotron and ASR-guided Tacotron.

</details>

### [Daft-Exprt: Cross-Speaker Prosody Transfer on Any Text for Expressive Speech Synthesis](2108.02271.md)
**Julian Zaïdi, Hugo Seuté, Benjamin van Niekerk, Marc-André Carbonneau** · 2021-08-04

<details>
<summary>Abstract</summary>

This paper presents Daft-Exprt, a multi-speaker acoustic model advancing the state-of-the-art for cross-speaker prosody transfer on any text. This is one of the most challenging, and rarely directly addressed, task in speech synthesis, especially for highly expressive data. Daft-Exprt uses FiLM conditioning layers to strategically inject different prosodic information in all parts of the architecture. The model explicitly encodes traditional low-level prosody features such as pitch, loudness and duration, but also higher level prosodic information that helps generating convincing voices in highly expressive styles. Speaker identity and prosodic information are disentangled through an adversarial training strategy that enables accurate prosody transfer across speakers. Experimental results show that Daft-Exprt significantly outperforms strong baselines on inter-text cross-speaker prosody transfer tasks, while yielding naturalness comparable to state-of-the-art expressive models. Moreover, results indicate that the model discards speaker identity information from the prosody representation, and consistently generate speech with the desired voice. We publicly release our code and provide speech samples from our experiments.

</details>

### [Speaker Adaptation with Continuous Vocoder-based DNN-TTS](2108.01154.md)
**Ali Raheem Mandeel, Mohammed Salah Al-Radhi, Tamás Gábor Csapó** · 2021-08-02

<details>
<summary>Abstract</summary>

Traditional vocoder-based statistical parametric speech synthesis can be advantageous in applications that require low computational complexity. Recent neural vocoders, which can produce high naturalness, still cannot fulfill the requirement of being real-time during synthesis. In this paper, we experiment with our earlier continuous vocoder, in which the excitation is modeled with two one-dimensional parameters: continuous F0 and Maximum Voiced Frequency. We show on the data of 9 speakers that an average voice can be trained for DNN-TTS, and speaker adaptation is feasible 400 utterances (about 14 minutes). Objective experiments support that the quality of speaker adaptation with Continuous Vocoder-based DNN-TTS is similar to the quality of the speaker adaptation with a WORLD Vocoder-based baseline.

</details>

### [End to End Bangla Speech Synthesis](2108.00500.md)
**Prithwiraj Bhattacharjee, Rajan Saha Raju, Arif Ahmad, M. Shahidur Rahman** · 2021-08-01

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) system is a system where speech is synthesized from a given text following any particular approach. Concatenative synthesis, Hidden Markov Model (HMM) based synthesis, Deep Learning (DL) based synthesis with multiple building blocks, etc. are the main approaches for implementing a TTS system. Here, we are presenting our deep learning-based end-to-end Bangla speech synthesis system. It has been implemented with minimal human annotation using only 3 major components (Encoder, Decoder, Post-processing net including waveform synthesis). It does not require any frontend preprocessor and Grapheme-to-Phoneme (G2P) converter. Our model has been trained with phonetically balanced 20 hours of single speaker speech data. It has obtained a 3.79 Mean Opinion Score (MOS) on a scale of 5.0 as subjective evaluation and a 0.77 Perceptual Evaluation of Speech Quality(PESQ) score on a scale of [-0.5, 4.5] as objective evaluation. It is outperforming all existing non-commercial state-of-the-art Bangla TTS systems based on naturalness.

</details>

### [A Survey on Audio Synthesis and Audio-Visual Multimodal Processing](2108.00443.md)
**Zhaofeng Shi** · 2021-08-01

<details>
<summary>Abstract</summary>

With the development of deep learning and artificial intelligence, audio synthesis has a pivotal role in the area of machine learning and shows strong applicability in the industry. Meanwhile, significant efforts have been dedicated by researchers to handle multimodal tasks at present such as audio-visual multimodal processing. In this paper, we conduct a survey on audio synthesis and audio-visual multimodal processing, which helps understand current research and future trends. This review focuses on text to speech(TTS), music generation and some tasks that combine visual and acoustic information. The corresponding technical methods are comprehensively classified and introduced, and their future development trends are prospected. This survey can provide some guidance for researchers who are interested in the areas like audio synthesis and audio-visual multimodal processing.

</details>

### [Cross-speaker Style Transfer with Prosody Bottleneck in Neural Speech Synthesis](2107.12562.md)
**Shifeng Pan, Lei He** · 2021-07-27

<details>
<summary>Abstract</summary>

Cross-speaker style transfer is crucial to the applications of multi-style and expressive speech synthesis at scale. It does not require the target speakers to be experts in expressing all styles and to collect corresponding recordings for model training. However, the performances of existing style transfer methods are still far behind real application needs. The root causes are mainly twofold. Firstly, the style embedding extracted from single reference speech can hardly provide fine-grained and appropriate prosody information for arbitrary text to synthesize. Secondly, in these models the content/text, prosody, and speaker timbre are usually highly entangled, it's therefore not realistic to expect a satisfied result when freely combining these components, such as to transfer speaking style between speakers. In this paper, we propose a cross-speaker style transfer text-to-speech (TTS) model with explicit prosody bottleneck. The prosody bottleneck builds up the kernels accounting for speaking style robustly, and disentangles the prosody from content and speaker timbre, therefore guarantees high quality cross-speaker style transfer. Evaluation result shows the proposed method even achieves on-par performance with source speaker's speaker-dependent (SD) model in objective measurement of prosody, and significantly outperforms the cycle consistency and GMVAE-based baselines in objective and subjective evaluations.

</details>

### [Adaptation of Tacotron2-based Text-To-Speech for Articulatory-to-Acoustic Mapping using Ultrasound Tongue Imaging](2107.12051.md)
**Csaba Zainkó, László Tóth, Amin Honarmandi Shandiz, Gábor Gosztolya et al.** · 2021-07-26

<details>
<summary>Abstract</summary>

For articulatory-to-acoustic mapping, typically only limited parallel training data is available, making it impossible to apply fully end-to-end solutions like Tacotron2. In this paper, we experimented with transfer learning and adaptation of a Tacotron2 text-to-speech model to improve the final synthesis quality of ultrasound-based articulatory-to-acoustic mapping with a limited database. We use a multi-speaker pre-trained Tacotron2 TTS model and a pre-trained WaveGlow neural vocoder. The articulatory-to-acoustic conversion contains three steps: 1) from a sequence of ultrasound tongue image recordings, a 3D convolutional neural network predicts the inputs of the pre-trained Tacotron2 model, 2) the Tacotron2 model converts this intermediate representation to an 80-dimensional mel-spectrogram, and 3) the WaveGlow model is applied for final inference. This generated speech contains the timing of the original articulatory data from the ultrasound recording, but the F0 contour and the spectral information is predicted by the Tacotron2 model. The F0 values are independent of the original ultrasound images, but represent the target speaker, as they are inferred from the pre-trained Tacotron2 model. In our experiments, we demonstrated that the synthesized speech quality is more natural with the proposed solutions than with our earlier model.

</details>

### [UR Channel-Robust Synthetic Speech Detection System for ASVspoof 2021](2107.12018.md)
**Xinhui Chen, You Zhang, Ge Zhu, Zhiyao Duan** · 2021-07-26

<details>
<summary>Abstract</summary>

In this paper, we present UR-AIR system submission to the logical access (LA) and the speech deepfake (DF) tracks of the ASVspoof 2021 Challenge. The LA and DF tasks focus on synthetic speech detection (SSD), i.e. detecting text-to-speech and voice conversion as spoofing attacks. Different from previous ASVspoof challenges, the LA task this year presents codec and transmission channel variability, while the new task DF presents general audio compression. Built upon our previous research work on improving the robustness of the SSD systems to channel effects, we propose a channel-robust synthetic speech detection system for the challenge. To mitigate the channel variability issue, we use an acoustic simulator to apply transmission codec, compression codec, and convolutional impulse responses to augmenting the original datasets. For the neural network backbone, we propose to use Emphasized Channel Attention, Propagation and Aggregation Time Delay Neural Networks (ECAPA-TDNN) as our primary model. We also incorporate one-class learning with channel-robust training strategies to further learn a channel-invariant speech representation. Our submission achieved EER 20.33% in the DF task; EER 5.46% and min-tDCF 0.3094 in the LA task.

</details>

### [Beyond Voice Identity Conversion: Manipulating Voice Attributes by Adversarial Learning of Structured Disentangled Representations](2107.12346.md)
**Laurent Benaroya, Nicolas Obin, Axel Roebel** · 2021-07-26

<details>
<summary>Abstract</summary>

Voice conversion (VC) consists of digitally altering the voice of an individual to manipulate part of its content, primarily its identity, while maintaining the rest unchanged. Research in neural VC has accomplished considerable breakthroughs with the capacity to falsify a voice identity using a small amount of data with a highly realistic rendering. This paper goes beyond voice identity and presents a neural architecture that allows the manipulation of voice attributes (e.g., gender and age). Leveraging the latest advances on adversarial learning of structured speech representation, a novel structured neural network is proposed in which multiple auto-encoders are used to encode speech as a set of idealistically independent linguistic and extra-linguistic representations, which are learned adversariarly and can be manipulated during VC. Moreover, the proposed architecture is time-synchronized so that the original voice timing is preserved during conversion which allows lip-sync applications. Applied to voice gender conversion on the real-world VCTK dataset, our proposed architecture can learn successfully gender-independent representation and convert the voice gender with a very high efficiency and naturalness.

</details>

### [StarGANv2-VC: A Diverse, Unsupervised, Non-parallel Framework for Natural-Sounding Voice Conversion](2107.10394.md)
**Yinghao Aaron Li, Ali Zare, Nima Mesgarani** · 2021-07-21

<details>
<summary>Abstract</summary>

We present an unsupervised non-parallel many-to-many voice conversion (VC) method using a generative adversarial network (GAN) called StarGAN v2. Using a combination of adversarial source classifier loss and perceptual loss, our model significantly outperforms previous VC models. Although our model is trained only with 20 English speakers, it generalizes to a variety of voice conversion tasks, such as any-to-many, cross-lingual, and singing conversion. Using a style encoder, our framework can also convert plain reading speech into stylistic speech, such as emotional and falsetto speech. Subjective and objective evaluation experiments on a non-parallel many-to-many voice conversion task revealed that our model produces natural sounding voices, close to the sound quality of state-of-the-art text-to-speech (TTS) based voice conversion methods without the need for text labels. Moreover, our model is completely convolutional and with a faster-than-real-time vocoder such as Parallel WaveGAN can perform real-time voice conversion.

</details>

### [Digital Einstein Experience: Fast Text-to-Speech for Conversational AI](2107.10658.md)
**Joanna Rownicka, Kilian Sprenkamp, Antonio Tripiana, Volodymyr Gromoglasov et al.** · 2021-07-21

<details>
<summary>Abstract</summary>

We describe our approach to create and deliver a custom voice for a conversational AI use-case. More specifically, we provide a voice for a Digital Einstein character, to enable human-computer interaction within the digital conversation experience. To create the voice which fits the context well, we first design a voice character and we produce the recordings which correspond to the desired speech attributes. We then model the voice. Our solution utilizes Fastspeech 2 for log-scaled mel-spectrogram prediction from phonemes and Parallel WaveGAN to generate the waveforms. The system supports a character input and gives a speech waveform at the output. We use a custom dictionary for selected words to ensure their proper pronunciation. Our proposed cloud architecture enables for fast voice delivery, making it possible to talk to the digital version of Albert Einstein in real-time.

</details>

### [SVSNet: An End-to-end Speaker Voice Similarity Assessment Model](2107.09392.md)
**Cheng-Hung Hu, Yu-Huai Peng, Junichi Yamagishi, Yu Tsao et al.** · 2021-07-20

<details>
<summary>Abstract</summary>

Neural evaluation metrics derived for numerous speech generation tasks have recently attracted great attention. In this paper, we propose SVSNet, the first end-to-end neural network model to assess the speaker voice similarity between converted speech and natural speech for voice conversion tasks. Unlike most neural evaluation metrics that use hand-crafted features, SVSNet directly takes the raw waveform as input to more completely utilize speech information for prediction. SVSNet consists of encoder, co-attention, distance calculation, and prediction modules and is trained in an end-to-end manner. The experimental results on the Voice Conversion Challenge 2018 and 2020 (VCC2018 and VCC2020) datasets show that SVSNet outperforms well-known baseline systems in the assessment of speaker similarity at the utterance and system levels.

</details>

### [Translatotron 2: High-quality direct speech-to-speech translation with voice preservation](2107.08661.md)
**Ye Jia, Michelle Tadmor Ramanovich, Tal Remez, Roi Pomerantz** · 2021-07-19

<details>
<summary>Abstract</summary>

We present Translatotron 2, a neural direct speech-to-speech translation model that can be trained end-to-end. Translatotron 2 consists of a speech encoder, a linguistic decoder, an acoustic synthesizer, and a single attention module that connects them together. Experimental results on three datasets consistently show that Translatotron 2 outperforms the original Translatotron by a large margin on both translation quality (up to +15.5 BLEU) and speech generation quality, and approaches the same of cascade systems. In addition, we propose a simple method for preserving speakers' voices from the source speech to the translation speech in a different language. Unlike existing approaches, the proposed method is able to preserve each speaker's voice on speaker turns without requiring for speaker segmentation. Furthermore, compared to existing approaches, it better preserves speaker's privacy and mitigates potential misuse of voice cloning for creating spoofing audio artifacts.

</details>

### [An Improved StarGAN for Emotional Voice Conversion: Enhancing Voice Quality and Data Augmentation](2107.08361.md)
**Xiangheng He, Junjie Chen, Georgios Rizos, Björn W. Schuller** · 2021-07-18

<details>
<summary>Abstract</summary>

Emotional Voice Conversion (EVC) aims to convert the emotional style of a source speech signal to a target style while preserving its content and speaker identity information. Previous emotional conversion studies do not disentangle emotional information from emotion-independent information that should be preserved, thus transforming it all in a monolithic manner and generating audio of low quality, with linguistic distortions. To address this distortion problem, we propose a novel StarGAN framework along with a two-stage training process that separates emotional features from those independent of emotion by using an autoencoder with two encoders as the generator of the Generative Adversarial Network (GAN). The proposed model achieves favourable results in both the objective evaluation and the subjective evaluation in terms of distortion, which reveals that the proposed model can effectively reduce distortion. Furthermore, in data augmentation experiments for end-to-end speech emotion recognition, the proposed StarGAN model achieves an increase of 2% in Micro-F1 and 5% in Macro-F1 compared to the baseline StarGAN model, which indicates that the proposed model is more valuable for data augmentation.

</details>

### [Extending Text-to-Speech Synthesis with Articulatory Movement Prediction using Ultrasound Tongue Imaging](2107.05550.md)
**Tamás Gábor Csapó** · 2021-07-12

<details>
<summary>Abstract</summary>

In this paper, we present our first experiments in text-to-articulation prediction, using ultrasound tongue image targets. We extend a traditional (vocoder-based) DNN-TTS framework with predicting PCA-compressed ultrasound images, of which the continuous tongue motion can be reconstructed in synchrony with synthesized speech. We use the data of eight speakers, train fully connected and recurrent neural networks, and show that FC-DNNs are more suitable for the prediction of sequential data than LSTMs, in case of limited training data. Objective experiments and visualized predictions show that the proposed solution is feasible and the generated ultrasound videos are close to natural tongue movement. Articulatory movement prediction from text input can be useful for audiovisual speech synthesis or computer-assisted pronunciation training.

</details>

### [Many-to-Many Voice Conversion based Feature Disentanglement using Variational Autoencoder](2107.06642.md)
**Manh Luong, Viet Anh Tran** · 2021-07-11

<details>
<summary>Abstract</summary>

Voice conversion is a challenging task which transforms the voice characteristics of a source speaker to a target speaker without changing linguistic content. Recently, there have been many works on many-to-many Voice Conversion (VC) based on Variational Autoencoder (VAEs) achieving good results, however, these methods lack the ability to disentangle speaker identity and linguistic content to achieve good performance on unseen speaker scenarios. In this paper, we propose a new method based on feature disentanglement to tackle many to many voice conversion. The method has the capability to disentangle speaker identity and linguistic content from utterances, it can convert from many source speakers to many target speakers with a single autoencoder network. Moreover, it naturally deals with the unseen target speaker scenarios. We perform both objective and subjective evaluations to show the competitive performance of our proposed method compared with other state-of-the-art models in terms of naturalness and target speaker similarity.

</details>

### [A Deep-Bayesian Framework for Adaptive Speech Duration Modification](2107.04973.md)
**Ravi Shankar, Archana Venkataraman** · 2021-07-11

<details>
<summary>Abstract</summary>

We propose the first method to adaptively modify the duration of a given speech signal. Our approach uses a Bayesian framework to define a latent attention map that links frames of the input and target utterances. We train a masked convolutional encoder-decoder network to produce this attention map via a stochastic version of the mean absolute error loss function; our model also predicts the length of the target speech signal using the encoder embeddings. The predicted length determines the number of steps for the decoder operation. During inference, we generate the attention map as a proxy for the similarity matrix between the given input speech and an unknown target speech signal. Using this similarity matrix, we compute a warping path of alignment between the two signals. Our experiments demonstrate that this adaptive framework produces similar results to dynamic time warping, which relies on a known target signal, on both voice conversion and emotion conversion tasks. We also show that our technique results in a high quality of generated speech that is on par with state-of-the-art vocoders.

</details>

### [Federated Learning with Dynamic Transformer for Text to Speech](2107.08795.md)
**Zhenhou Hong, Jianzong Wang, Xiaoyang Qu, Jie Liu et al.** · 2021-07-09

<details>
<summary>Abstract</summary>

Text to speech (TTS) is a crucial task for user interaction, but TTS model training relies on a sizable set of high-quality original datasets. Due to privacy and security issues, the original datasets are usually unavailable directly. Recently, federated learning proposes a popular distributed machine learning paradigm with an enhanced privacy protection mechanism. It offers a practical and secure framework for data owners to collaborate with others, thus obtaining a better global model trained on the larger dataset. However, due to the high complexity of transformer models, the convergence process becomes slow and unstable in the federated learning setting. Besides, the transformer model trained in federated learning is costly communication and limited computational speed on clients, impeding its popularity. To deal with these challenges, we propose the federated dynamic transformer. On the one hand, the performance is greatly improved comparing with the federated transformer, approaching centralize-trained Transformer-TTS when increasing clients number. On the other hand, it achieves faster and more stable convergence in the training phase and significantly reduces communication time. Experiments on the LJSpeech dataset also strongly prove our method's advantage.

</details>

### [Expressive Voice Conversion: A Joint Framework for Speaker Identity and Emotional Style Transfer](2107.03748.md)
**Zongyang Du, Berrak Sisman, Kun Zhou, Haizhou Li** · 2021-07-08

<details>
<summary>Abstract</summary>

Traditional voice conversion(VC) has been focused on speaker identity conversion for speech with a neutral expression. We note that emotional expression plays an essential role in daily communication, and the emotional style of speech can be speaker-dependent. In this paper, we study the technique to jointly convert the speaker identity and speaker-dependent emotional style, that is called expressive voice conversion. We propose a StarGAN-based framework to learn a many-to-many mapping across different speakers, that takes into account speaker-dependent emotional style without the need for parallel data. To achieve this, we condition the generator on emotional style encoding derived from a pre-trained speech emotion recognition(SER) model. The experiments validate the effectiveness of our proposed framework in both objective and subjective evaluations. To our best knowledge, this is the first study on expressive voice conversion.

</details>

### [SoundStream: An End-to-End Neural Audio Codec](2107.03312.md)
**Neil Zeghidour, Alejandro Luebs, Ahmed Omran, Jan Skoglund et al.** · 2021-07-07

<details>
<summary>Abstract</summary>

We present SoundStream, a novel neural audio codec that can efficiently compress speech, music and general audio at bitrates normally targeted by speech-tailored codecs. SoundStream relies on a model architecture composed by a fully convolutional encoder/decoder network and a residual vector quantizer, which are trained jointly end-to-end. Training leverages recent advances in text-to-speech and speech enhancement, which combine adversarial and reconstruction losses to allow the generation of high-quality audio content from quantized embeddings. By training with structured dropout applied to quantizer layers, a single model can operate across variable bitrates from 3kbps to 18kbps, with a negligible quality loss when compared with models trained at fixed bitrates. In addition, the model is amenable to a low latency implementation, which supports streamable inference and runs in real time on a smartphone CPU. In subjective evaluations using audio at 24kHz sampling rate, SoundStream at 3kbps outperforms Opus at 12kbps and approaches EVS at 9.6kbps. Moreover, we are able to perform joint compression and enhancement either at the encoder or at the decoder side with no additional latency, which we demonstrate through background noise suppression for speech.

</details>

### [VAENAR-TTS: Variational Auto-Encoder based Non-AutoRegressive Text-to-Speech Synthesis](2107.03298.md)
**Hui Lu, Zhiyong Wu, Xixin Wu, Xu Li et al.** · 2021-07-07

<details>
<summary>Abstract</summary>

This paper describes a variational auto-encoder based non-autoregressive text-to-speech (VAENAR-TTS) model. The autoregressive TTS (AR-TTS) models based on the sequence-to-sequence architecture can generate high-quality speech, but their sequential decoding process can be time-consuming. Recently, non-autoregressive TTS (NAR-TTS) models have been shown to be more efficient with the parallel decoding process. However, these NAR-TTS models rely on phoneme-level durations to generate a hard alignment between the text and the spectrogram. Obtaining duration labels, either through forced alignment or knowledge distillation, is cumbersome. Furthermore, hard alignment based on phoneme expansion can degrade the naturalness of the synthesized speech. In contrast, the proposed model of VAENAR-TTS is an end-to-end approach that does not require phoneme-level durations. The VAENAR-TTS model does not contain recurrent structures and is completely non-autoregressive in both the training and inference phases. Based on the VAE architecture, the alignment information is encoded in the latent variable, and attention-based soft alignment between the text and the latent variable is used in the decoder to reconstruct the spectrogram. Experiments show that VAENAR-TTS achieves state-of-the-art synthesis quality, while the synthesis speed is comparable with other NAR-TTS models.

</details>

### [Msdtron: a high-capability multi-speaker speech synthesis system for diverse data using characteristic information](2107.03065.md)
**Qinghua Wu, Quanbo Shen, Jian Luan, YuJun Wang** · 2021-07-07

<details>
<summary>Abstract</summary>

In multi-speaker speech synthesis, data from a number of speakers usually tend to have great diversity due to the fact that the speakers may differ largely in ages, speaking styles, emotions, and so on. It is important but challenging to improve the modeling capabilities for multi-speaker speech synthesis. To address the issue, this paper proposes a high-capability speech synthesis system, called Msdtron, in which 1) a representation of the harmonic structure of speech, called excitation spectrogram, is designed to directly guide the learning of harmonics in mel-spectrogram. 2) conditional gated LSTM (CGLSTM) is proposed to control the flow of text content information through the network by re-weighting the gates of LSTM using speaker information. The experiments show a significant reduction in reconstruction error of mel-spectrogram in the training of the multi-speaker model, and a great improvement is observed in the subjective evaluation of speaker adapted model.

</details>

### [AdaSpeech 3: Adaptive Text to Speech for Spontaneous Style](2107.02530.md)
**Yuzi Yan, Xu Tan, Bohan Li, Guangyan Zhang et al.** · 2021-07-06

<details>
<summary>Abstract</summary>

While recent text to speech (TTS) models perform very well in synthesizing reading-style (e.g., audiobook) speech, it is still challenging to synthesize spontaneous-style speech (e.g., podcast or conversation), mainly because of two reasons: 1) the lack of training data for spontaneous speech; 2) the difficulty in modeling the filled pauses (um and uh) and diverse rhythms in spontaneous speech. In this paper, we develop AdaSpeech 3, an adaptive TTS system that fine-tunes a well-trained reading-style TTS model for spontaneous-style speech. Specifically, 1) to insert filled pauses (FP) in the text sequence appropriately, we introduce an FP predictor to the TTS model; 2) to model the varying rhythms, we introduce a duration predictor based on mixture of experts (MoE), which contains three experts responsible for the generation of fast, medium and slow speech respectively, and fine-tune it as well as the pitch predictor for rhythm adaptation; 3) to adapt to other speaker timbre, we fine-tune some parameters in the decoder with few speech data. To address the challenge of lack of training data, we mine a spontaneous speech dataset to support our research this work and facilitate future research on spontaneous TTS. Experiments show that AdaSpeech 3 synthesizes speech with natural FP and rhythms in spontaneous styles, and achieves much better MOS and SMOS scores than previous adaptive TTS systems.

</details>

### [Location, Location: Enhancing the Evaluation of Text-to-Speech Synthesis Using the Rapid Prosody Transcription Paradigm](2107.02527.md)
**Elijah Gutierrez, Pilar Oplustil-Gallegos, Catherine Lai** · 2021-07-06

<details>
<summary>Abstract</summary>

Text-to-Speech synthesis systems are generally evaluated using Mean Opinion Score (MOS) tests, where listeners score samples of synthetic speech on a Likert scale. A major drawback of MOS tests is that they only offer a general measure of overall quality-i.e., the naturalness of an utterance-and so cannot tell us where exactly synthesis errors occur. This can make evaluation of the appropriateness of prosodic variation within utterances inconclusive. To address this, we propose a novel evaluation method based on the Rapid Prosody Transcription paradigm. This allows listeners to mark the locations of errors in an utterance in real-time, providing a probabilistic representation of the perceptual errors that occur in the synthetic signal. We conduct experiments that confirm that the fine-grained evaluation can be mapped to system rankings of standard MOS tests, but the error marking gives a much more comprehensive assessment of synthesized prosody. In particular, for standard audiobook test set samples, we see that error marks consistently cluster around words at major prosodic boundaries indicated by punctuation. However, for question-answer based stimuli, where we control information structure, we see differences emerge in the ability of neural TTS systems to generate context-appropriate prosodic prominence.

</details>

### [Speech Synthesis from Text and Ultrasound Tongue Image-based Articulatory Input](2107.02003.md)
**Tamás Gábor Csapó, László Tóth, Gábor Gosztolya, Alexandra Markó** · 2021-07-05

<details>
<summary>Abstract</summary>

Articulatory information has been shown to be effective in improving the performance of HMM-based and DNN-based text-to-speech synthesis. Speech synthesis research focuses traditionally on text-to-speech conversion, when the input is text or an estimated linguistic representation, and the target is synthesized speech. However, a research field that has risen in the last decade is articulation-to-speech synthesis (with a target application of a Silent Speech Interface, SSI), when the goal is to synthesize speech from some representation of the movement of the articulatory organs. In this paper, we extend traditional (vocoder-based) DNN-TTS with articulatory input, estimated from ultrasound tongue images. We compare text-only, ultrasound-only, and combined inputs. Using data from eight speakers, we show that that the combined text and articulatory input can have advantages in limited-data scenarios, namely, it may increase the naturalness of synthesized speech compared to single text input. Besides, we analyze the ultrasound tongue recordings of several speakers, and show that misalignments in the ultrasound transducer positioning can have a negative effect on the final synthesis performance.

</details>

### [EditSpeech: A Text Based Speech Editing System Using Partial Inference and Bidirectional Fusion](2107.01554.md)
**Daxin Tan, Liqun Deng, Yu Ting Yeung, Xin Jiang et al.** · 2021-07-04

<details>
<summary>Abstract</summary>

This paper presents the design, implementation and evaluation of a speech editing system, named EditSpeech, which allows a user to perform deletion, insertion and replacement of words in a given speech utterance, without causing audible degradation in speech quality and naturalness. The EditSpeech system is developed upon a neural text-to-speech (NTTS) synthesis framework. Partial inference and bidirectional fusion are proposed to effectively incorporate the contextual information related to the edited region and achieve smooth transition at both left and right boundaries. Distortion introduced to the unmodified parts of the utterance is alleviated. The EditSpeech system is developed and evaluated on English and Chinese in multi-speaker scenarios. Objective and subjective evaluation demonstrate that EditSpeech outperforms a few baseline systems in terms of low spectral distortion and preferred speech quality. Audio samples are available online for demonstration https://daxintan-cuhk.github.io/EditSpeech/ .

</details>

### [Neural-Symbolic Solver for Math Word Problems with Auxiliary Tasks](2107.01431.md)
**Jinghui Qin, Xiaodan Liang, Yining Hong, Jianheng Tang et al.** · 2021-07-03

<details>
<summary>Abstract</summary>

Previous math word problem solvers following the encoder-decoder paradigm fail to explicitly incorporate essential math symbolic constraints, leading to unexplainable and unreasonable predictions. Herein, we propose Neural-Symbolic Solver (NS-Solver) to explicitly and seamlessly incorporate different levels of symbolic constraints by auxiliary tasks. Our NS-Solver consists of a problem reader to encode problems, a programmer to generate symbolic equations, and a symbolic executor to obtain answers. Along with target expression supervision, our solver is also optimized via 4 new auxiliary objectives to enforce different symbolic reasoning: a) self-supervised number prediction task predicting both number quantity and number locations; b) commonsense constant prediction task predicting what prior knowledge (e.g. how many legs a chicken has) is required; c) program consistency checker computing the semantic loss between predicted equation and target equation to ensure reasonable equation mapping; d) duality exploiting task exploiting the quasi duality between symbolic equation generation and problem's part-of-speech generation to enhance the understanding ability of a solver. Besides, to provide a more realistic and challenging benchmark for developing a universal and scalable solver, we also construct a new large-scale MWP benchmark CM17K consisting of 4 kinds of MWPs (arithmetic, one-unknown linear, one-unknown non-linear, equation set) with more than 17K samples. Extensive experiments on Math23K and our CM17k demonstrate the superiority of our NS-Solver compared to state-of-the-art methods.

</details>

### [An Objective Evaluation Framework for Pathological Speech Synthesis](2107.00308.md)
**Bence Mark Halpern, Julian Fritsch, Enno Hermann, Rob van Son et al.** · 2021-07-01

<details>
<summary>Abstract</summary>

The development of pathological speech systems is currently hindered by the lack of a standardised objective evaluation framework. In this work, (1) we utilise existing detection and analysis techniques to propose a general framework for the consistent evaluation of synthetic pathological speech. This framework evaluates the voice quality and the intelligibility aspects of speech and is shown to be complementary using our experiments. (2) Using our proposed evaluation framework, we develop and test a dysarthric voice conversion system (VC) using CycleGAN-VC and a PSOLA-based speech rate modification technique. We show that the developed system is able to synthesise dysarthric speech with different levels of speech intelligibility.

</details>

### [Multi-Scale Spectrogram Modelling for Neural Text-to-Speech](2106.15649.md)
**Ammar Abbas, Bajibabu Bollepalli, Alexis Moinet, Arnaud Joly et al.** · 2021-06-29

<details>
<summary>Abstract</summary>

We propose a novel Multi-Scale Spectrogram (MSS) modelling approach to synthesise speech with an improved coarse and fine-grained prosody. We present a generic multi-scale spectrogram prediction mechanism where the system first predicts coarser scale mel-spectrograms that capture the suprasegmental information in speech, and later uses these coarser scale mel-spectrograms to predict finer scale mel-spectrograms capturing fine-grained prosody. We present details for two specific versions of MSS called Word-level MSS and Sentence-level MSS where the scales in our system are motivated by the linguistic units. The Word-level MSS models word, phoneme, and frame-level spectrograms while Sentence-level MSS models sentence-level spectrogram in addition. Subjective evaluations show that Word-level MSS performs statistically significantly better compared to the baseline on two voices.

</details>

### [A Survey on Neural Speech Synthesis](2106.15561.md)
**Xu Tan, Tao Qin, Frank Soong, Tie-Yan Liu** · 2021-06-29

<details>
<summary>Abstract</summary>

Text to speech (TTS), or speech synthesis, which aims to synthesize intelligible and natural speech given text, is a hot research topic in speech, language, and machine learning communities and has broad applications in the industry. As the development of deep learning and artificial intelligence, neural network-based TTS has significantly improved the quality of synthesized speech in recent years. In this paper, we conduct a comprehensive survey on neural TTS, aiming to provide a good understanding of current research and future trends. We focus on the key components in neural TTS, including text analysis, acoustic models and vocoders, and several advanced topics, including fast TTS, low-resource TTS, robust TTS, expressive TTS, and adaptive TTS, etc. We further summarize resources related to TTS (e.g., datasets, opensource implementations) and discuss future research directions. This survey can serve both academic researchers and industry practitioners working on TTS.

</details>

### [GANSpeech: Adversarial Training for High-Fidelity Multi-Speaker Speech Synthesis](2106.15153.md)
**Jinhyeok Yang, Jae-Sung Bae, Taejun Bak, Youngik Kim et al.** · 2021-06-29

<details>
<summary>Abstract</summary>

Recent advances in neural multi-speaker text-to-speech (TTS) models have enabled the generation of reasonably good speech quality with a single model and made it possible to synthesize the speech of a speaker with limited training data. Fine-tuning to the target speaker data with the multi-speaker model can achieve better quality, however, there still exists a gap compared to the real speech sample and the model depends on the speaker. In this work, we propose GANSpeech, which is a high-fidelity multi-speaker TTS model that adopts the adversarial training method to a non-autoregressive multi-speaker TTS model. In addition, we propose simple but efficient automatic scaling methods for feature matching loss used in adversarial training. In the subjective listening tests, GANSpeech significantly outperformed the baseline multi-speaker FastSpeech and FastSpeech2 models, and showed a better MOS score than the speaker-specific fine-tuned FastSpeech2.

</details>

### [Hierarchical Context-Aware Transformers for Non-Autoregressive Text to Speech](2106.15144.md)
**Jae-Sung Bae, Tae-Jun Bak, Young-Sun Joo, Hoon-Young Cho** · 2021-06-29

<details>
<summary>Abstract</summary>

In this paper, we propose methods for improving the modeling performance of a Transformer-based non-autoregressive text-to-speech (TNA-TTS) model. Although the text encoder and audio decoder handle different types and lengths of data (i.e., text and audio), the TNA-TTS models are not designed considering these variations. Therefore, to improve the modeling performance of the TNA-TTS model we propose a hierarchical Transformer structure-based text encoder and audio decoder that are designed to accommodate the characteristics of each module. For the text encoder, we constrain each self-attention layer so the encoder focuses on a text sequence from the local to the global scope. Conversely, the audio decoder constrains its self-attention layers to focus in the reverse direction, i.e., from global to local scope. Additionally, we further improve the pitch modeling accuracy of the audio decoder by providing sentence and word-level pitch as conditions. Various objective and subjective evaluations verified that the proposed method outperformed the baseline TNA-TTS.

</details>

### [FastPitchFormant: Source-filter based Decomposed Modeling for Speech Synthesis](2106.15123.md)
**Taejun Bak, Jae-Sung Bae, Hanbin Bae, Young-Ik Kim et al.** · 2021-06-29

<details>
<summary>Abstract</summary>

Methods for modeling and controlling prosody with acoustic features have been proposed for neural text-to-speech (TTS) models. Prosodic speech can be generated by conditioning acoustic features. However, synthesized speech with a large pitch-shift scale suffers from audio quality degradation, and speaker characteristics deformation. To address this problem, we propose a feed-forward Transformer based TTS model that is designed based on the source-filter theory. This model, called FastPitchFormant, has a unique structure that handles text and acoustic features in parallel. With modeling each feature separately, the tendency that the model learns the relationship between two features can be mitigated.

</details>

### [AI based Presentation Creator With Customized Audio Content Delivery](2106.14213.md)
**Muvazima Mansoor, Srikanth Chandar, Ramamoorthy Srinath** · 2021-06-27

<details>
<summary>Abstract</summary>

In this paper, we propose an architecture to solve a novel problem statement that has stemmed more so in recent times with an increase in demand for virtual content delivery due to the COVID-19 pandemic. All educational institutions, workplaces, research centers, etc. are trying to bridge the gap of communication during these socially distanced times with the use of online content delivery. The trend now is to create presentations, and then subsequently deliver the same using various virtual meeting platforms. The time being spent in such creation of presentations and delivering is what we try to reduce and eliminate through this paper which aims to use Machine Learning (ML) algorithms and Natural Language Processing (NLP) modules to automate the process of creating a slides-based presentation from a document, and then use state-of-the-art voice cloning models to deliver the content in the desired author's voice. We consider a structured document such as a research paper to be the content that has to be presented. The research paper is first summarized using BERT summarization techniques and condensed into bullet points that go into the slides. Tacotron inspired architecture with Encoder, Synthesizer, and a Generative Adversarial Network (GAN) based vocoder, is used to convey the contents of the slides in the author's voice (or any customized voice). Almost all learning has now been shifted to online mode, and professionals are now working from the comfort of their homes. Due to the current situation, teachers and professionals have shifted to presentations to help them in imparting information. In this paper, we aim to reduce the considerable amount of time that is taken in creating a presentation by automating this process and subsequently delivering this presentation in a customized voice, using a content delivery mechanism that can clone any voice using a short audio clip.

</details>

### [Txt2Vid: Ultra-Low Bitrate Compression of Talking-Head Videos via Text](2106.14014.md)
**Pulkit Tandon, Shubham Chandak, Pat Pataranutaporn, Yimeng Liu et al.** · 2021-06-26

<details>
<summary>Abstract</summary>

Video represents the majority of internet traffic today, driving a continual race between the generation of higher quality content, transmission of larger file sizes, and the development of network infrastructure. In addition, the recent COVID-19 pandemic fueled a surge in the use of video conferencing tools. Since videos take up considerable bandwidth (~100 Kbps to a few Mbps), improved video compression can have a substantial impact on network performance for live and pre-recorded content, providing broader access to multimedia content worldwide. We present a novel video compression pipeline, called Txt2Vid, which dramatically reduces data transmission rates by compressing webcam videos ("talking-head videos") to a text transcript. The text is transmitted and decoded into a realistic reconstruction of the original video using recent advances in deep learning based voice cloning and lip syncing models. Our generative pipeline achieves two to three orders of magnitude reduction in the bitrate as compared to the standard audio-video codecs (encoders-decoders), while maintaining equivalent Quality-of-Experience based on a subjective evaluation by users (n = 242) in an online study. The Txt2Vid framework opens up the potential for creating novel applications such as enabling audio-video communication during poor internet connectivity, or in remote terrains with limited bandwidth. The code for this work is available at https://github.com/tpulkit/txt2vid.git.

</details>

### [Preliminary study on using vector quantization latent spaces for TTS/VC systems with consistent performance](2106.13479.md)
**Hieu-Thi Luong, Junichi Yamagishi** · 2021-06-25

<details>
<summary>Abstract</summary>

Generally speaking, the main objective when training a neural speech synthesis system is to synthesize natural and expressive speech from the output layer of the neural network without much attention given to the hidden layers. However, by learning useful latent representation, the system can be used for many more practical scenarios. In this paper, we investigate the use of quantized vectors to model the latent linguistic embedding and compare it with the continuous counterpart. By enforcing different policies over the latent spaces in the training, we are able to obtain a latent linguistic embedding that takes on different properties while having a similar performance in terms of quality and speaker similarity. Our experiments show that the voice cloning system built with vector quantization has only a small degradation in terms of perceptive evaluations, but has a discrete latent space that is useful for reducing the representation bit-rate, which is desirable for data transferring, or limiting the information leaking, which is important for speaker anonymization and other tasks of that nature.

</details>

### [Basis-MelGAN: Efficient Neural Vocoder Based on Audio Decomposition](2106.13419.md)
**Zhengxi Liu, Yanmin Qian** · 2021-06-25

<details>
<summary>Abstract</summary>

Recent studies have shown that neural vocoders based on generative adversarial network (GAN) can generate audios with high quality. While GAN based neural vocoders have shown to be computationally much more efficient than those based on autoregressive predictions, the real-time generation of the highest quality audio on CPU is still a very challenging task. One major computation of all GAN-based neural vocoders comes from the stacked upsampling layers, which were designed to match the length of the waveform's length of output and temporal resolution. Meanwhile, the computational complexity of upsampling networks is closely correlated with the numbers of samples generated for each window. To reduce the computation of upsampling layers, we propose a new GAN based neural vocoder called Basis-MelGAN where the raw audio samples are decomposed with a learned basis and their associated weights. As the prediction targets of Basis-MelGAN are the weight values associated with each learned basis instead of the raw audio samples, the upsampling layers in Basis-MelGAN can be designed with much simpler networks. Compared with other GAN based neural vocoders, the proposed Basis-MelGAN could produce comparable high-quality audio but significantly reduced computational complexity from HiFi-GAN V1's 17.74 GFLOPs to 7.95 GFLOPs.

</details>

### [Non-Autoregressive TTS with Explicit Duration Modelling for Low-Resource Highly Expressive Speech](2106.12896.md)
**Raahil Shah, Kamil Pokora, Abdelhamid Ezzerg, Viacheslav Klimkov et al.** · 2021-06-24

<details>
<summary>Abstract</summary>

Whilst recent neural text-to-speech (TTS) approaches produce high-quality speech, they typically require a large amount of recordings from the target speaker. In previous work, a 3-step method was proposed to generate high-quality TTS while greatly reducing the amount of data required for training. However, we have observed a ceiling effect in the level of naturalness achievable for highly expressive voices when using this approach. In this paper, we present a method for building highly expressive TTS voices with as little as 15 minutes of speech data from the target speaker. Compared to the current state-of-the-art approach, our proposed improvements close the gap to recordings by 23.3% for naturalness of speech and by 16.3% for speaker similarity. Further, we match the naturalness and speaker similarity of a Tacotron2-based full-data (~10 hours) model using only 15 minutes of target speaker data, whereas with 30 minutes or more, we significantly outperform it. The following improvements are proposed: 1) changing from an autoregressive, attention-based TTS model to a non-autoregressive model replacing attention with an external duration model and 2) an additional Conditional Generative Adversarial Network (cGAN) based fine-tuning step.

</details>

### [Distilling the Knowledge from Conditional Normalizing Flows](2106.12699.md)
**Dmitry Baranchuk, Vladimir Aliev, Artem Babenko** · 2021-06-24

<details>
<summary>Abstract</summary>

Normalizing flows are a powerful class of generative models demonstrating strong performance in several speech and vision problems. In contrast to other generative models, normalizing flows are latent variable models with tractable likelihoods and allow for stable training. However, they have to be carefully designed to represent invertible functions with efficient Jacobian determinant calculation. In practice, these requirements lead to overparameterized and sophisticated architectures that are inferior to alternative feed-forward models in terms of inference time and memory consumption. In this work, we investigate whether one can distill flow-based models into more efficient alternatives. We provide a positive answer to this question by proposing a simple distillation approach and demonstrating its effectiveness on state-of-the-art conditional flow-based models for image super-resolution and speech synthesis.

</details>

### [Non-native English lexicon creation for bilingual speech synthesis](2106.10870.md)
**Arun Baby, Pranav Jawale, Saranya Vinnaitherthan, Sumukh Badam et al.** · 2021-06-21

<details>
<summary>Abstract</summary>

Bilingual English speakers speak English as one of their languages. Their English is of a non-native kind, and their conversations are of a code-mixed fashion. The intelligibility of a bilingual text-to-speech (TTS) system for such non-native English speakers depends on a lexicon that captures the phoneme sequence used by non-native speakers. However, due to the lack of non-native English lexicon, existing bilingual TTS systems employ native English lexicons that are widely available, in addition to their native language lexicon. Due to the inconsistency between the non-native English pronunciation in the audio and native English lexicon in the text, the intelligibility of synthesized speech in such TTS systems is significantly reduced. This paper is motivated by the knowledge that the native language of the speaker highly influences non-native English pronunciation. We propose a generic approach to obtain rules based on letter to phoneme alignment to map native English lexicon to their non-native version. The effectiveness of such mapping is studied by comparing bilingual (Indian English and Hindi) TTS systems trained with and without the proposed rules. The subjective evaluation shows that the bilingual TTS system trained with the proposed non-native English lexicon rules obtains a 6% absolute improvement in preference.

</details>

### [UniTTS: Residual Learning of Unified Embedding Space for Speech Style Control](2106.11171.md)
**Minsu Kang, Sungjae Kim, Injung Kim** · 2021-06-21

<details>
<summary>Abstract</summary>

We propose a novel high-fidelity expressive speech synthesis model, UniTTS, that learns and controls overlapping style attributes avoiding interference. UniTTS represents multiple style attributes in a single unified embedding space by the residuals between the phoneme embeddings before and after applying the attributes. The proposed method is especially effective in controlling multiple attributes that are difficult to separate cleanly, such as speaker ID and emotion, because it minimizes redundancy when adding variance in speaker ID and emotion, and additionally, predicts duration, pitch, and energy based on the speaker ID and emotion. In experiments, the visualization results exhibit that the proposed methods learned multiple attributes harmoniously in a manner that can be easily separated again. As well, UniTTS synthesized high-fidelity speech signals controlling multiple style attributes. The synthesized speech samples are presented at https://anonymous-authors2022.github.io/paper_works/UniTTS/demos/.

</details>

### [Glow-WaveGAN: Learning Speech Representations from GAN-based Variational Auto-Encoder For High Fidelity Flow-based Speech Synthesis](2106.10831.md)
**Jian Cong, Shan Yang, Lei Xie, Dan Su** · 2021-06-21

<details>
<summary>Abstract</summary>

Current two-stage TTS framework typically integrates an acoustic model with a vocoder -- the acoustic model predicts a low resolution intermediate representation such as Mel-spectrum while the vocoder generates waveform from the intermediate representation. Although the intermediate representation is served as a bridge, there still exists critical mismatch between the acoustic model and the vocoder as they are commonly separately learned and work on different distributions of representation, leading to inevitable artifacts in the synthesized speech. In this work, different from using pre-designed intermediate representation in most previous studies, we propose to use VAE combining with GAN to learn a latent representation directly from speech and then utilize a flow-based acoustic model to model the distribution of the latent representation from text. In this way, the mismatch problem is migrated as the two stages work on the same distribution. Results demonstrate that the flow-based acoustic model can exactly model the distribution of our learned speech representation and the proposed TTS framework, namely Glow-WaveGAN, can produce high fidelity speech outperforming the state-of-the-art GAN-based model.

</details>

### [Controllable Context-aware Conversational Speech Synthesis](2106.10828.md)
**Jian Cong, Shan Yang, Na Hu, Guangzhi Li et al.** · 2021-06-21

<details>
<summary>Abstract</summary>

In spoken conversations, spontaneous behaviors like filled pause and prolongations always happen. Conversational partner tends to align features of their speech with their interlocutor which is known as entrainment. To produce human-like conversations, we propose a unified controllable spontaneous conversational speech synthesis framework to model the above two phenomena. Specifically, we use explicit labels to represent two typical spontaneous behaviors filled-pause and prolongation in the acoustic model and develop a neural network based predictor to predict the occurrences of the two behaviors from text. We subsequently develop an algorithm based on the predictor to control the occurrence frequency of the behaviors, making the synthesized speech vary from less disfluent to more disfluent. To model the speech entrainment at acoustic level, we utilize a context acoustic encoder to extract a global style embedding from the previous speech conditioning on the synthesizing of current speech. Furthermore, since the current and previous utterances belong to the different speakers in a conversation, we add a domain adversarial training module to eliminate the speaker-related information in the acoustic encoder while maintaining the style-related information. Experiments show that our proposed approach can synthesize realistic conversations and control the occurrences of the spontaneous behaviors naturally.

</details>

### [Advances in Speech Vocoding for Text-to-Speech with Continuous Parameters](2106.10481.md)
**Mohammed Salah Al-Radhi, Tamás Gábor Csapó, Géza Németh** · 2021-06-19

<details>
<summary>Abstract</summary>

Vocoders received renewed attention as main components in statistical parametric text-to-speech (TTS) synthesis and speech transformation systems. Even though there are vocoding techniques give almost accepted synthesized speech, their high computational complexity and irregular structures are still considered challenging concerns, which yield a variety of voice quality degradation. Therefore, this paper presents new techniques in a continuous vocoder, that is all features are continuous and presents a flexible speech synthesis system. First, a new continuous noise masking based on the phase distortion is proposed to eliminate the perceptual impact of the residual noise and letting an accurate reconstruction of noise characteristics. Second, we addressed the need of neural sequence to sequence modeling approach for the task of TTS based on recurrent networks. Bidirectional long short-term memory (LSTM) and gated recurrent unit (GRU) are studied and applied to model continuous parameters for more natural-sounding like a human. The evaluation results proved that the proposed model achieves the state-of-the-art performance of the speech synthesis compared with the other traditional methods.

</details>

### [Improving robustness of one-shot voice conversion with deep discriminative speaker encoder](2106.10406.md)
**Hongqiang Du, Lei Xie** · 2021-06-19

<details>
<summary>Abstract</summary>

One-shot voice conversion has received significant attention since only one utterance from source speaker and target speaker respectively is required. Moreover, source speaker and target speaker do not need to be seen during training. However, available one-shot voice conversion approaches are not stable for unseen speakers as the speaker embedding extracted from one utterance of an unseen speaker is not reliable. In this paper, we propose a deep discriminative speaker encoder to extract speaker embedding from one utterance more effectively. Specifically, the speaker encoder first integrates residual network and squeeze-and-excitation network to extract discriminative speaker information in frame level by modeling frame-wise and channel-wise interdependence in features. Then attention mechanism is introduced to further emphasize speaker related information via assigning different weights to frame level speaker information. Finally a statistic pooling layer is used to aggregate weighted frame level speaker information to form utterance level speaker embedding. The experimental results demonstrate that our proposed speaker encoder can improve the robustness of one-shot voice conversion for unseen speakers and outperforms baseline systems in terms of speech quality and speaker similarity.

</details>

### [VQMIVC: Vector Quantization and Mutual Information-Based Unsupervised Speech Representation Disentanglement for One-shot Voice Conversion](2106.10132.md)
**Disong Wang, Liqun Deng, Yu Ting Yeung, Xiao Chen et al.** · 2021-06-18

<details>
<summary>Abstract</summary>

One-shot voice conversion (VC), which performs conversion across arbitrary speakers with only a single target-speaker utterance for reference, can be effectively achieved by speech representation disentanglement. Existing work generally ignores the correlation between different speech representations during training, which causes leakage of content information into the speaker representation and thus degrades VC performance. To alleviate this issue, we employ vector quantization (VQ) for content encoding and introduce mutual information (MI) as the correlation metric during training, to achieve proper disentanglement of content, speaker and pitch representations, by reducing their inter-dependencies in an unsupervised manner. Experimental results reflect the superiority of the proposed method in learning effective disentangled speech representations for retaining source linguistic content and intonation variations, while capturing target speaker characteristics. In doing so, the proposed approach achieves higher speech naturalness and speaker similarity than current state-of-the-art one-shot VC systems. Our code, pre-trained models and demo are available at https://github.com/Wendison/VQMIVC.

</details>

### [WaveGrad 2: Iterative Refinement for Text-to-Speech Synthesis](2106.09660.md)
**Nanxin Chen, Yu Zhang, Heiga Zen, Ron J. Weiss et al.** · 2021-06-17

<details>
<summary>Abstract</summary>

This paper introduces WaveGrad 2, a non-autoregressive generative model for text-to-speech synthesis. WaveGrad 2 is trained to estimate the gradient of the log conditional density of the waveform given a phoneme sequence. The model takes an input phoneme sequence, and through an iterative refinement process, generates an audio waveform. This contrasts to the original WaveGrad vocoder which conditions on mel-spectrogram features, generated by a separate model. The iterative refinement process starts from Gaussian noise, and through a series of refinement steps (e.g., 50 steps), progressively recovers the audio sequence. WaveGrad 2 offers a natural way to trade-off between inference speed and sample quality, through adjusting the number of refinement steps. Experiments show that the model can generate high fidelity audio, approaching the performance of a state-of-the-art neural TTS system. We also report various ablation studies over different model configurations. Audio samples are available at https://wavegrad.github.io/v2.

</details>

### [EMOVIE: A Mandarin Emotion Speech Dataset with a Simple Emotional Text-to-Speech Model](2106.09317.md)
**Chenye Cui, Yi Ren, Jinglin Liu, Feiyang Chen et al.** · 2021-06-17

<details>
<summary>Abstract</summary>

Recently, there has been an increasing interest in neural speech synthesis. While the deep neural network achieves the state-of-the-art result in text-to-speech (TTS) tasks, how to generate a more emotional and more expressive speech is becoming a new challenge to researchers due to the scarcity of high-quality emotion speech dataset and the lack of advanced emotional TTS model. In this paper, we first briefly introduce and publicly release a Mandarin emotion speech dataset including 9,724 samples with audio files and its emotion human-labeled annotation. After that, we propose a simple but efficient architecture for emotional speech synthesis called EMSpeech. Unlike those models which need additional reference audio as input, our model could predict emotion labels just from the input text and generate more expressive speech conditioned on the emotion embedding. In the experiment phase, we first validate the effectiveness of our dataset by an emotion classification task. Then we train our model on the proposed dataset and conduct a series of subjective evaluations. Finally, by showing a comparable performance in the emotional speech synthesis task, we successfully demonstrate the ability of the proposed model.

</details>

### [Improving the expressiveness of neural vocoding with non-affine Normalizing Flows](2106.08649.md)
**Adam Gabryś, Yunlong Jiao, Viacheslav Klimkov, Daniel Korzekwa et al.** · 2021-06-16

<details>
<summary>Abstract</summary>

This paper proposes a general enhancement to the Normalizing Flows (NF) used in neural vocoding. As a case study, we improve expressive speech vocoding with a revamped Parallel Wavenet (PW). Specifically, we propose to extend the affine transformation of PW to the more expressive invertible non-affine function. The greater expressiveness of the improved PW leads to better-perceived signal quality and naturalness in the waveform reconstruction and text-to-speech (TTS) tasks. We evaluate the model across different speaking styles on a multi-speaker, multi-lingual dataset. In the waveform reconstruction task, the proposed model closes the naturalness and signal quality gap from the original PW to recordings by $10\%$, and from other state-of-the-art neural vocoding systems by more than $60\%$. We also demonstrate improvements in objective metrics on the evaluation test set with L2 Spectral Distance and Cross-Entropy reduced by $3\%$ and $6\unicode{x2030}$ comparing to the affine PW. Furthermore, we extend the probability density distillation procedure proposed by the original PW paper, so that it works with any non-affine invertible and differentiable function.

</details>

### [A Flow-Based Neural Network for Time Domain Speech Enhancement](2106.09008.md)
**Martin Strauss, Bernd Edler** · 2021-06-16

<details>
<summary>Abstract</summary>

Speech enhancement involves the distinction of a target speech signal from an intrusive background. Although generative approaches using Variational Autoencoders or Generative Adversarial Networks (GANs) have increasingly been used in recent years, normalizing flow (NF) based systems are still scarse, despite their success in related fields. Thus, in this paper we propose a NF framework to directly model the enhancement process by density estimation of clean speech utterances conditioned on their noisy counterpart. The WaveGlow model from speech synthesis is adapted to enable direct enhancement of noisy utterances in time domain. In addition, we demonstrate that nonlinear input companding benefits the model performance by equalizing the distribution of input samples. Experimental evaluation on a publicly available dataset shows comparable results to current state-of-the-art GAN-based approaches, while surpassing the chosen baselines using objective evaluation metrics.

</details>

### [Voicy: Zero-Shot Non-Parallel Voice Conversion in Noisy Reverberant Environments](2106.08873.md)
**Alejandro Mottini, Jaime Lorenzo-Trueba, Sri Vishnu Kumar Karlapati, Thomas Drugman** · 2021-06-16

<details>
<summary>Abstract</summary>

Voice Conversion (VC) is a technique that aims to transform the non-linguistic information of a source utterance to change the perceived identity of the speaker. While there is a rich literature on VC, most proposed methods are trained and evaluated on clean speech recordings. However, many acoustic environments are noisy and reverberant, severely restricting the applicability of popular VC methods to such scenarios. To address this limitation, we propose Voicy, a new VC framework particularly tailored for noisy speech. Our method, which is inspired by the de-noising auto-encoders framework, is comprised of four encoders (speaker, content, phonetic and acoustic-ASR) and one decoder. Importantly, Voicy is capable of performing non-parallel zero-shot VC, an important requirement for any VC system that needs to work on speakers not seen during training. We have validated our approach using a noisy reverberant version of the LibriSpeech dataset. Experimental results show that Voicy outperforms other tested VC techniques in terms of naturalness and target speaker similarity in noisy reverberant environments.

</details>

### [Enriching Source Style Transfer in Recognition-Synthesis based Non-Parallel Voice Conversion](2106.08741.md)
**Zhichao Wang, Xinyong Zhou, Fengyu Yang, Tao Li et al.** · 2021-06-16

<details>
<summary>Abstract</summary>

Current voice conversion (VC) methods can successfully convert timbre of the audio. As modeling source audio's prosody effectively is a challenging task, there are still limitations of transferring source style to the converted speech. This study proposes a source style transfer method based on recognition-synthesis framework. Previously in speech generation task, prosody can be modeled explicitly with prosodic features or implicitly with a latent prosody extractor. In this paper, taking advantages of both, we model the prosody in a hybrid manner, which effectively combines explicit and implicit methods in a proposed prosody module. Specifically, prosodic features are used to explicit model prosody, while VAE and reference encoder are used to implicitly model prosody, which take Mel spectrum and bottleneck feature as input respectively. Furthermore, adversarial training is introduced to remove speaker-related information from the VAE outputs, avoiding leaking source speaker information while transferring style. Finally, we use a modified self-attention based encoder to extract sentential context from bottleneck features, which also implicitly aggregates the prosodic aspects of source speech from the layered representations. Experiments show that our approach is superior to the baseline and a competitive system in terms of style transfer; meanwhile, the speech quality and speaker similarity are well maintained.

</details>

### [Ctrl-P: Temporal Control of Prosodic Variation for Speech Synthesis](2106.08352.md)
**Devang S Ram Mohan, Vivian Hu, Tian Huey Teh, Alexandra Torresquintero et al.** · 2021-06-15

<details>
<summary>Abstract</summary>

Text does not fully specify the spoken form, so text-to-speech models must be able to learn from speech data that vary in ways not explained by the corresponding text. One way to reduce the amount of unexplained variation in training data is to provide acoustic information as an additional learning signal. When generating speech, modifying this acoustic information enables multiple distinct renditions of a text to be produced. Since much of the unexplained variation is in the prosody, we propose a model that generates speech explicitly conditioned on the three primary acoustic correlates of prosody: $F_{0}$, energy and duration. The model is flexible about how the values of these features are specified: they can be externally provided, or predicted from text, or predicted then subsequently modified. Compared to a model that employs a variational auto-encoder to learn unsupervised latent features, our model provides more interpretable, temporally-precise, and disentangled control. When automatically predicting the acoustic features from text, it generates speech that is more natural than that from a Tacotron 2 model with reference encoder. Subsequent human-in-the-loop modification of the predicted acoustic features can significantly further increase naturalness.

</details>

### [ADEPT: A Dataset for Evaluating Prosody Transfer](2106.08321.md)
**Alexandra Torresquintero, Tian Huey Teh, Christopher G. R. Wallis, Marlene Staib et al.** · 2021-06-15

<details>
<summary>Abstract</summary>

Text-to-speech is now able to achieve near-human naturalness and research focus has shifted to increasing expressivity. One popular method is to transfer the prosody from a reference speech sample. There have been considerable advances in using prosody transfer to generate more expressive speech, but the field lacks a clear definition of what successful prosody transfer means and a method for measuring it. We introduce a dataset of prosodically-varied reference natural speech samples for evaluating prosody transfer. The samples include global variations reflecting emotion and interpersonal attitude, and local variations reflecting topical emphasis, propositional attitude, syntactic phrasing and marked tonicity. The corpus only includes prosodic variations that listeners are able to distinguish with reasonable accuracy, and we report these figures as a benchmark against which text-to-speech prosody transfer can be compared. We conclude the paper with a demonstration of our proposed evaluation methodology, using the corpus to evaluate two text-to-speech models that perform prosody transfer.

</details>

### [UnivNet: A Neural Vocoder with Multi-Resolution Spectrogram Discriminators for High-Fidelity Waveform Generation](2106.07889.md)
**Won Jang, Dan Lim, Jaesam Yoon, Bongwan Kim et al.** · 2021-06-15

<details>
<summary>Abstract</summary>

Most neural vocoders employ band-limited mel-spectrograms to generate waveforms. If full-band spectral features are used as the input, the vocoder can be provided with as much acoustic information as possible. However, in some models employing full-band mel-spectrograms, an over-smoothing problem occurs as part of which non-sharp spectrograms are generated. To address this problem, we propose UnivNet, a neural vocoder that synthesizes high-fidelity waveforms in real time. Inspired by works in the field of voice activity detection, we added a multi-resolution spectrogram discriminator that employs multiple linear spectrogram magnitudes computed using various parameter sets. Using full-band mel-spectrograms as input, we expect to generate high-resolution signals by adding a discriminator that employs spectrograms of multiple resolutions as the input. In an evaluation on a dataset containing information on hundreds of speakers, UnivNet obtained the best objective and subjective results among competing models for both seen and unseen speakers. These results, including the best subjective score for text-to-speech, demonstrate the potential for fast adaptation to new speakers without a need for training from scratch.

</details>

### [Pathological voice adaptation with autoencoder-based voice conversion](2106.08427.md)
**Marc Illa, Bence Mark Halpern, Rob van Son, Laureano Moro-Velazquez et al.** · 2021-06-15

<details>
<summary>Abstract</summary>

In this paper, we propose a new approach to pathological speech synthesis. Instead of using healthy speech as a source, we customise an existing pathological speech sample to a new speaker's voice characteristics. This approach alleviates the evaluation problem one normally has when converting typical speech to pathological speech, as in our approach, the voice conversion (VC) model does not need to be optimised for speech degradation but only for the speaker change. This change in the optimisation ensures that any degradation found in naturalness is due to the conversion process and not due to the model exaggerating characteristics of a speech pathology. To show a proof of concept of this method, we convert dysarthric speech using the UASpeech database and an autoencoder-based VC technique. Subjective evaluation results show reasonable naturalness for high intelligibility dysarthric speakers, though lower intelligibility seems to introduce a marginal degradation in naturalness scores for mid and low intelligibility speakers compared to ground truth. Conversion of speaker characteristics for low and high intelligibility speakers is successful, but not for mid. Whether the differences in the results for the different intelligibility levels is due to the intelligibility levels or due to the speakers needs to be further investigated.

</details>

### [A learned conditional prior for the VAE acoustic space of a TTS system](2106.10229.md)
**Penny Karanasou, Sri Karlapati, Alexis Moinet, Arnaud Joly et al.** · 2021-06-14

<details>
<summary>Abstract</summary>

Many factors influence speech yielding different renditions of a given sentence. Generative models, such as variational autoencoders (VAEs), capture this variability and allow multiple renditions of the same sentence via sampling. The degree of prosodic variability depends heavily on the prior that is used when sampling. In this paper, we propose a novel method to compute an informative prior for the VAE latent space of a neural text-to-speech (TTS) system. By doing so, we aim to sample with more prosodic variability, while gaining controllability over the latent space's structure. By using as prior the posterior distribution of a secondary VAE, which we condition on a speaker vector, we can sample from the primary VAE taking explicitly the conditioning into account and resulting in samples from a specific region of the latent space for each condition (i.e. speaker). A formal preference test demonstrates significant preference of the proposed approach over standard Conditional VAE. We also provide visualisations of the latent space where well-separated condition-specific clusters appear, as well as ablation studies to better understand the behaviour of the system.

</details>

### [Non Gaussian Denoising Diffusion Models](2106.07582.md)
**Eliya Nachmani, Robin San Roman, Lior Wolf** · 2021-06-14

<details>
<summary>Abstract</summary>

Generative diffusion processes are an emerging and effective tool for image and speech generation. In the existing methods, the underline noise distribution of the diffusion process is Gaussian noise. However, fitting distributions with more degrees of freedom, could help the performance of such generative models. In this work, we investigate other types of noise distribution for the diffusion process. Specifically, we show that noise from Gamma distribution provides improved results for image and speech generation. Moreover, we show that using a mixture of Gaussian noise variables in the diffusion process improves the performance over a diffusion process that is based on a single distribution. Our approach preserves the ability to efficiently sample state in the training diffusion process while using Gamma noise and a mixture of noise.

</details>

### [Continuous Wavelet Vocoder-based Decomposition of Parametric Speech Waveform Synthesis](2106.06863.md)
**Mohammed Salah Al-Radhi, Tamás Gábor Csapó, Csaba Zainkó, Géza Németh** · 2021-06-12

<details>
<summary>Abstract</summary>

To date, various speech technology systems have adopted the vocoder approach, a method for synthesizing speech waveform that shows a major role in the performance of statistical parametric speech synthesis. WaveNet one of the best models that nearly resembles the human voice, has to generate a waveform in a time consuming sequential manner with an extremely complex structure of its neural networks.

</details>

### [HUI-Audio-Corpus-German: A high quality TTS dataset](2106.06309.md)
**Pascal Puchtler, Johannes Wirth, René Peinl** · 2021-06-11

<details>
<summary>Abstract</summary>

The increasing availability of audio data on the internet lead to a multitude of datasets for development and training of text to speech applications, based on neural networks. Highly differing quality of voice, low sampling rates, lack of text normalization and disadvantageous alignment of audio samples to corresponding transcript sentences still limit the performance of deep neural networks trained on this task. Additionally, data resources in languages like German are still very limited. We introduce the "HUI-Audio-Corpus-German", a large, open-source dataset for TTS engines, created with a processing pipeline, which produces high quality audio to transcription alignments and decreases manual effort needed for creation.

</details>

### [Enhancing Speaking Styles in Conversational Text-to-Speech Synthesis with Graph-based Multi-modal Context Modeling](2106.06233.md)
**Jingbei Li, Yi Meng, Chenyi Li, Zhiyong Wu et al.** · 2021-06-11

<details>
<summary>Abstract</summary>

Comparing with traditional text-to-speech (TTS) systems, conversational TTS systems are required to synthesize speeches with proper speaking style confirming to the conversational context. However, state-of-the-art context modeling methods in conversational TTS only model the textual information in context with a recurrent neural network (RNN). Such methods have limited ability in modeling the inter-speaker influence in conversations, and also neglect the speaking styles and the intra-speaker inertia inside each speaker. Inspired by DialogueGCN and its superiority in modeling such conversational influences than RNN based approaches, we propose a graph-based multi-modal context modeling method and adopt it to conversational TTS to enhance the speaking styles of synthesized speeches. Both the textual and speaking style information in the context are extracted and processed by DialogueGCN to model the inter- and intra-speaker influence in conversations. The outputs of DialogueGCN are then summarized by attention mechanism, and converted to the enhanced speaking style for current utterance. An English conversation corpus is collected and annotated for our research and released to public. Experiment results on this corpus demonstrate the effectiveness of our proposed approach, which outperforms the state-of-the-art context modeling method in conversational TTS in both MOS and ABX preference rate.

</details>

### [Conditional Variational Autoencoder with Adversarial Learning for End-to-End Text-to-Speech](2106.06103.md)
**Jaehyeon Kim, Jungil Kong, Juhee Son** · 2021-06-11

<details>
<summary>Abstract</summary>

Several recent end-to-end text-to-speech (TTS) models enabling single-stage training and parallel sampling have been proposed, but their sample quality does not match that of two-stage TTS systems. In this work, we present a parallel end-to-end TTS method that generates more natural sounding audio than current two-stage models. Our method adopts variational inference augmented with normalizing flows and an adversarial training process, which improves the expressive power of generative modeling. We also propose a stochastic duration predictor to synthesize speech with diverse rhythms from input text. With the uncertainty modeling over latent variables and the stochastic duration predictor, our method expresses the natural one-to-many relationship in which a text input can be spoken in multiple ways with different pitches and rhythms. A subjective human evaluation (mean opinion score, or MOS) on the LJ Speech, a single speaker dataset, shows that our method outperforms the best publicly available TTS systems and achieves a MOS comparable to ground truth.

</details>

### [PriorGrad: Improving Conditional Denoising Diffusion Models with Data-Dependent Adaptive Prior](2106.06406.md)
**Sang-gil Lee, Heeseung Kim, Chaehun Shin, Xu Tan et al.** · 2021-06-11

<details>
<summary>Abstract</summary>

Denoising diffusion probabilistic models have been recently proposed to generate high-quality samples by estimating the gradient of the data density. The framework defines the prior noise as a standard Gaussian distribution, whereas the corresponding data distribution may be more complicated than the standard Gaussian distribution, which potentially introduces inefficiency in denoising the prior noise into the data sample because of the discrepancy between the data and the prior. In this paper, we propose PriorGrad to improve the efficiency of the conditional diffusion model for speech synthesis (for example, a vocoder using a mel-spectrogram as the condition) by applying an adaptive prior derived from the data statistics based on the conditional information. We formulate the training and sampling procedures of PriorGrad and demonstrate the advantages of an adaptive prior through a theoretical analysis. Focusing on the speech synthesis domain, we consider the recently proposed diffusion-based speech generative models based on both the spectral and time domains and show that PriorGrad achieves faster convergence and inference with superior performance, leading to an improved perceptual quality and robustness to a smaller network capacity, and thereby demonstrating the efficiency of a data-dependent adaptive prior.

</details>

### [Sprachsynthese -- State-of-the-Art in englischer und deutscher Sprache](2106.06230.md)
**René Peinl** · 2021-06-11

<details>
<summary>Abstract</summary>

Reading text aloud is an important feature for modern computer applications. It not only facilitates access to information for visually impaired people, but is also a pleasant convenience for non-impaired users. In this article, the state of the art of speech synthesis is presented separately for mel-spectrogram generation and vocoders. It concludes with an overview of available data sets for English and German with a discussion of the transferability of the good speech synthesis results from English to German language.

</details>

### [Improving multi-speaker TTS prosody variance with a residual encoder and normalizing flows](2106.05762.md)
**Iván Vallés-Pérez, Julian Roth, Grzegorz Beringer, Roberto Barra-Chicote et al.** · 2021-06-10

<details>
<summary>Abstract</summary>

Text-to-speech systems recently achieved almost indistinguishable quality from human speech. However, the prosody of those systems is generally flatter than natural speech, producing samples with low expressiveness. Disentanglement of speaker id and prosody is crucial in text-to-speech systems to improve on naturalness and produce more variable syntheses. This paper proposes a new neural text-to-speech model that approaches the disentanglement problem by conditioning a Tacotron2-like architecture on flow-normalized speaker embeddings, and by substituting the reference encoder with a new learned latent distribution responsible for modeling the intra-sentence variability due to the prosody. By removing the reference encoder dependency, the speaker-leakage problem typically happening in this kind of systems disappears, producing more distinctive syntheses at inference time. The new model achieves significantly higher prosody variance than the baseline in a set of quantitative prosody features, as well as higher speaker distinctiveness, without decreasing the speaker intelligibility. Finally, we observe that the normalized speaker embeddings enable much richer speaker interpolations, substantially improving the distinctiveness of the new interpolated speakers.

</details>

### [Speech BERT Embedding For Improving Prosody in Neural TTS](2106.04312.md)
**Liping Chen, Yan Deng, Xi Wang, Frank K. Soong et al.** · 2021-06-08

<details>
<summary>Abstract</summary>

This paper presents a speech BERT model to extract embedded prosody information in speech segments for improving the prosody of synthesized speech in neural text-to-speech (TTS). As a pre-trained model, it can learn prosody attributes from a large amount of speech data, which can utilize more data than the original training data used by the target TTS. The embedding is extracted from the previous segment of a fixed length in the proposed BERT. The extracted embedding is then used together with the mel-spectrogram to predict the following segment in the TTS decoder. Experimental results obtained by the Transformer TTS show that the proposed BERT can extract fine-grained, segment-level prosody, which is complementary to utterance-level prosody to improve the final prosody of the TTS speech. The objective distortions measured on a single speaker TTS are reduced between the generated speech and original recordings. Subjective listening tests also show that the proposed approach is favorably preferred over the TTS without the BERT prosody embedding module, for both in-domain and out-of-domain applications. For Microsoft professional, single/multiple speakers and the LJ Speaker in the public database, subjective preference is similarly confirmed with the new BERT prosody embedding. TTS demo audio samples are in https://judy44chen.github.io/TTSSpeechBERT/.

</details>

### [Learning to Efficiently Sample from Diffusion Probabilistic Models](2106.03802.md)
**Daniel Watson, Jonathan Ho, Mohammad Norouzi, William Chan** · 2021-06-07

<details>
<summary>Abstract</summary>

Denoising Diffusion Probabilistic Models (DDPMs) have emerged as a powerful family of generative models that can yield high-fidelity samples and competitive log-likelihoods across a range of domains, including image and speech synthesis. Key advantages of DDPMs include ease of training, in contrast to generative adversarial networks, and speed of generation, in contrast to autoregressive models. However, DDPMs typically require hundreds-to-thousands of steps to generate a high fidelity sample, making them prohibitively expensive for high dimensional problems. Fortunately, DDPMs allow trading generation speed for sample quality through adjusting the number of refinement steps as a post process. Prior work has been successful in improving generation speed through handcrafting the time schedule by trial and error. We instead view the selection of the inference time schedules as an optimization problem, and introduce an exact dynamic programming algorithm that finds the optimal discrete time schedules for any pre-trained DDPM. Our method exploits the fact that ELBO can be decomposed into separate KL terms, and given any computation budget, discovers the time schedule that maximizes the training ELBO exactly. Our method is efficient, has no hyper-parameters of its own, and can be applied to any pre-trained DDPM with no retraining. We discover inference time schedules requiring as few as 32 refinement steps, while sacrificing less than 0.1 bits per dimension compared to the default 4,000 steps used on ImageNet 64x64 [Ho et al., 2020; Nichol and Dhariwal, 2021].

</details>

### [Meta-StyleSpeech : Multi-Speaker Adaptive Text-to-Speech Generation](2106.03153.md)
**Dongchan Min, Dong Bok Lee, Eunho Yang, Sung Ju Hwang** · 2021-06-06

<details>
<summary>Abstract</summary>

With rapid progress in neural text-to-speech (TTS) models, personalized speech generation is now in high demand for many applications. For practical applicability, a TTS model should generate high-quality speech with only a few audio samples from the given speaker, that are also short in length. However, existing methods either require to fine-tune the model or achieve low adaptation quality without fine-tuning. In this work, we propose StyleSpeech, a new TTS model which not only synthesizes high-quality speech but also effectively adapts to new speakers. Specifically, we propose Style-Adaptive Layer Normalization (SALN) which aligns gain and bias of the text input according to the style extracted from a reference speech audio. With SALN, our model effectively synthesizes speech in the style of the target speaker even from single speech audio. Furthermore, to enhance StyleSpeech's adaptation to speech from new speakers, we extend it to Meta-StyleSpeech by introducing two discriminators trained with style prototypes, and performing episodic training. The experimental results show that our models generate high-quality speech which accurately follows the speaker's voice with single short-duration (1-3 sec) speech audio, significantly outperforming baselines.

</details>

### [Mathematical Vocoder Algorithm : Modified Spectral Inversion for Efficient Neural Speech Synthesis](2106.03167.md)
**Hyun Gon Ryu, Jeong-Hoon Kim, Simon See** · 2021-06-06

<details>
<summary>Abstract</summary>

In this work, we propose a new mathematical vocoder algorithm(modified spectral inversion) that generates a waveform from acoustic features without phase estimation. The main benefit of using our proposed method is that it excludes the training stage of the neural vocoder from the end-to-end speech synthesis model. Our implementation can synthesize high fidelity speech at approximately 20 Mhz on CPU and 59.6MHz on GPU. This is 909 and 2,702 times faster compared to real-time. Since the proposed methodology is not a data-driven method, it is applicable to unseen voices and multiple languages without any additional work. The proposed method is expected to adapt for researching on neural network models capable of synthesizing speech at the studio recording level.

</details>

### [Improving Naturalness and Controllability of Sequence-to-Sequence Speech Synthesis by Learning Local Prosody Representations](s2:5868a853b1c64dad3dff317e90be85b3d012337a.md)
**Cheng Gong, Longbiao Wang, Zhenhua Ling, Shaotong Guo et al.** · 2021-06-06

<details>
<summary>Abstract</summary>

State-of-the-art neural text-to-speech (TTS) networks are trained with a large amount of speech data, which significantly improves the quality of synthetic speech compared with traditional approaches. However, the prosody and controllability of the generated speech is still insufficient, especially in tonal languages. Moreover, the generated prosody is solely defined by the input text, which does not allow for different styles for the same sentence or words. In this study, we extended Tacotron2 with a pitch prediction task to capture discrete pitch-related representations. Specifically, the learned pitch-related suprasegmental information is fed simultaneously with traditional character features into the decoder to generate final Mel spectrogram. Experiments show that the proposed method can improve the quality of the generated speech (mean opinion score of 4.37 vs. 4.22). Moreover, we demonstrated that we can easily achieve word-level pitch control during generation by changing local pitch-related representations before passing them to the decoder network.

</details>

### [Bi-Level Style and Prosody Decoupling Modeling for Personalized End-to-End Speech Synthesis](s2:1ad86ac8f65dcb9c82e56d691358ad765ae010bc.md)
**Ruibo Fu, J. Tao, Zhengqi Wen, Jiangyan Yi et al.** · 2021-06-06

<details>
<summary>Abstract</summary>

End-to-end framework can generate high-quality and high-similarity speech in the personalized speech synthesis task. However, the generalization of out-of-domain texts is still a challenging task. Limited target data leads to unacceptable errors and poor prosody and similarity performance of the synthetic speech. In this paper, we present a bi-level function decoupling framework to realise separate modeling and controlling for solving above problems. Firstly, on the style representation modeling level, compared with the conventional methods that use single embedding to model all the text dependent discrepancies, it is proposed that the speaker embedding and prosody embedding are modeled separately based on the reference audio and phonetic posteriorgram (PPG) by a multi-head attention mechanism. Secondly, on the model structure level, the decoder model structure is factored into average-net and adaptation-net, where the duration prosody controlling and speaker timbre imitation are mainly designed in relatively separate areas. Experimental results on Mandarin dataset show that the proposed methods lead to an improvement on both robustness, naturalness and similarity.

</details>

### [Reinforce-Aligner: Reinforcement Alignment Search for Robust End-to-End Text-to-Speech](2106.02830.md)
**Hyunseung Chung, Sang-Hoon Lee, Seong-Whan Lee** · 2021-06-05

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) synthesis is the process of producing synthesized speech from text or phoneme input. Traditional TTS models contain multiple processing steps and require external aligners, which provide attention alignments of phoneme-to-frame sequences. As the complexity increases and efficiency decreases with every additional step, there is expanding demand in modern synthesis pipelines for end-to-end TTS with efficient internal aligners. In this work, we propose an end-to-end text-to-waveform network with a novel reinforcement learning based duration search method. Our proposed generator is feed-forward and the aligner trains the agent to make optimal duration predictions by receiving active feedback from actions taken to maximize cumulative reward. We demonstrate accurate alignments of phoneme-to-frame sequence generated from trained agents enhance fidelity and naturalness of synthesized audio. Experimental results also show the superiority of our proposed model compared to other state-of-the-art TTS models with internal and external aligners.

</details>

### [Fre-GAN: Adversarial Frequency-consistent Audio Synthesis](2106.02297.md)
**Ji-Hoon Kim, Sang-Hoon Lee, Ji-Hyun Lee, Seong-Whan Lee** · 2021-06-04

<details>
<summary>Abstract</summary>

Although recent works on neural vocoder have improved the quality of synthesized audio, there still exists a gap between generated and ground-truth audio in frequency space. This difference leads to spectral artifacts such as hissing noise or reverberation, and thus degrades the sample quality. In this paper, we propose Fre-GAN which achieves frequency-consistent audio synthesis with highly improved generation quality. Specifically, we first present resolution-connected generator and resolution-wise discriminators, which help learn various scales of spectral distributions over multiple frequency bands. Additionally, to reproduce high-frequency components accurately, we leverage discrete wavelet transform in the discriminators. From our experiments, Fre-GAN achieves high-fidelity waveform generation with a gap of only 0.03 MOS compared to ground-truth audio while outperforming standard models in quality.

</details>

### [NVC-Net: End-to-End Adversarial Voice Conversion](2106.00992.md)
**Bac Nguyen, Fabien Cardinaux** · 2021-06-02

<details>
<summary>Abstract</summary>

Voice conversion has gained increasing popularity in many applications of speech synthesis. The idea is to change the voice identity from one speaker into another while keeping the linguistic content unchanged. Many voice conversion approaches rely on the use of a vocoder to reconstruct the speech from acoustic features, and as a consequence, the speech quality heavily depends on such a vocoder. In this paper, we propose NVC-Net, an end-to-end adversarial network, which performs voice conversion directly on the raw audio waveform of arbitrary length. By disentangling the speaker identity from the speech content, NVC-Net is able to perform non-parallel traditional many-to-many voice conversion as well as zero-shot voice conversion from a short utterance of an unseen target speaker. Importantly, NVC-Net is non-autoregressive and fully convolutional, achieving fast inference. Our model is capable of producing samples at a rate of more than 3600 kHz on an NVIDIA V100 GPU, being orders of magnitude faster than state-of-the-art methods under the same hardware configurations. Objective and subjective evaluations on non-parallel many-to-many voice conversion tasks show that NVC-Net obtains competitive results with significantly fewer parameters.

</details>

### [A Preliminary Study of a Two-Stage Paradigm for Preserving Speaker Identity in Dysarthric Voice Conversion](2106.01415.md)
**Wen-Chin Huang, Kazuhiro Kobayashi, Yu-Huai Peng, Ching-Feng Liu et al.** · 2021-06-02

<details>
<summary>Abstract</summary>

We propose a new paradigm for maintaining speaker identity in dysarthric voice conversion (DVC). The poor quality of dysarthric speech can be greatly improved by statistical VC, but as the normal speech utterances of a dysarthria patient are nearly impossible to collect, previous work failed to recover the individuality of the patient. In light of this, we suggest a novel, two-stage approach for DVC, which is highly flexible in that no normal speech of the patient is required. First, a powerful parallel sequence-to-sequence model converts the input dysarthric speech into a normal speech of a reference speaker as an intermediate product, and a nonparallel, frame-wise VC model realized with a variational autoencoder then converts the speaker identity of the reference speech back to that of the patient while assumed to be capable of preserving the enhanced quality. We investigate several design options. Experimental evaluation results demonstrate the potential of our approach to improving the quality of the dysarthric speech while maintaining the speaker identity.

</details>

### [StarGAN-ZSVC: Towards Zero-Shot Voice Conversion in Low-Resource Contexts](2106.00043.md)
**Matthew Baas, Herman Kamper** · 2021-05-31

<details>
<summary>Abstract</summary>

Voice conversion is the task of converting a spoken utterance from a source speaker so that it appears to be said by a different target speaker while retaining the linguistic content of the utterance. Recent advances have led to major improvements in the quality of voice conversion systems. However, to be useful in a wider range of contexts, voice conversion systems would need to be (i) trainable without access to parallel data, (ii) work in a zero-shot setting where both the source and target speakers are unseen during training, and (iii) run in real time or faster. Recent techniques fulfil one or two of these requirements, but not all three. This paper extends recent voice conversion models based on generative adversarial networks (GANs), to satisfy all three of these conditions. We specifically extend the recent StarGAN-VC model by conditioning it on a speaker embedding (from a potentially unseen speaker). This allows the model to be used in a zero-shot setting, and we therefore call it StarGAN-ZSVC. We compare StarGAN-ZSVC against other voice conversion techniques in a low-resource setting using a small 9-minute training set. Compared to AutoVC -- another recent neural zero-shot approach -- we observe that StarGAN-ZSVC gives small improvements in the zero-shot setting, showing that real-time zero-shot voice conversion is possible even for a model trained on very little data. Further work is required to see whether scaling up StarGAN-ZSVC will also improve zero-shot voice conversion quality in high-resource contexts.

</details>

### [Emotional Voice Conversion: Theory, Databases and ESD](2105.14762.md)
**Kun Zhou, Berrak Sisman, Rui Liu, Haizhou Li** · 2021-05-31

<details>
<summary>Abstract</summary>

In this paper, we first provide a review of the state-of-the-art emotional voice conversion research, and the existing emotional speech databases. We then motivate the development of a novel emotional speech database (ESD) that addresses the increasing research need. With this paper, the ESD database is now made available to the research community. The ESD database consists of 350 parallel utterances spoken by 10 native English and 10 native Chinese speakers and covers 5 emotion categories (neutral, happy, angry, sad and surprise). More than 29 hours of speech data were recorded in a controlled acoustic environment. The database is suitable for multi-speaker and cross-lingual emotional voice conversion studies. As case studies, we implement several state-of-the-art emotional voice conversion systems on the ESD database. This paper provides a reference study on ESD in conjunction with its release.

</details>

### [DiffSVC: A Diffusion Probabilistic Model for Singing Voice Conversion](2105.13871.md)
**Songxiang Liu, Yuewen Cao, Dan Su, Helen Meng** · 2021-05-28

<details>
<summary>Abstract</summary>

Singing voice conversion (SVC) is one promising technique which can enrich the way of human-computer interaction by endowing a computer the ability to produce high-fidelity and expressive singing voice. In this paper, we propose DiffSVC, an SVC system based on denoising diffusion probabilistic model. DiffSVC uses phonetic posteriorgrams (PPGs) as content features. A denoising module is trained in DiffSVC, which takes destroyed mel spectrogram produced by the diffusion/forward process and its corresponding step information as input to predict the added Gaussian noise. We use PPGs, fundamental frequency features and loudness features as auxiliary input to assist the denoising process. Experiments show that DiffSVC can achieve superior conversion performance in terms of naturalness and voice similarity to current state-of-the-art SVC approaches.

</details>

### [Phone-Level Prosody Modelling with GMM-Based MDN for Diverse and Controllable Speech Synthesis](2105.13086.md)
**Chenpeng Du, Kai Yu** · 2021-05-27

<details>
<summary>Abstract</summary>

Generating natural speech with a diverse and smooth prosody pattern is a challenging task. Although random sampling with phone-level prosody distribution has been investigated to generate different prosody patterns, the diversity of the generated speech is still very limited and far from what can be achieved by humans. This is largely due to the use of uni-modal distribution, such as single Gaussian, in the prior works of phone-level prosody modelling. In this work, we propose a novel approach that models phone-level prosodies with a GMM-based mixture density network(MDN) and then extend it for multi-speaker TTS using speaker adaptation transforms of Gaussian means and variances. Furthermore, we show that we can clone the prosodies from a reference speech by sampling prosodies from the Gaussian components that produce the reference prosodies. Our experiments on LJSpeech and LibriTTS dataset show that the proposed method with GMM-based MDN not only achieves significantly better diversity than using a single Gaussian in both single-speaker and multi-speaker TTS, but also provides better naturalness. The prosody cloning experiments demonstrate that the prosody similarity of the proposed method with GMM-based MDN is comparable to recent proposed fine-grained VAE while the target speaker similarity is better.

</details>

### [Deep Learning End to End Speech Synthesis: A Review](s2:295887147460cde4436ec73cd9e88d8be817fa5a.md)
**Owais Nazir, Aruna Malik** · 2021-05-21

<details>
<summary>Abstract</summary>

Speech is a fundamental way of expressing ideas and thoughts. The ability to produce synthetic speech has always been a great interest to mankind. Text-to speech (TTS) or speech synthesis is an approach of producing an artificial speech in contrast to a given input text. Text-to-speech systems have immensely increased and improved in recent years. These advances in speech synthesis are contributed by deep learning techniques. The aim of this paper is to give an understanding regarding dynamics of research in this field and gives a brief introduction of traditional methods used in speech synthesis. Further, the use of various data sets for training deep learning TTS or Speech Synthesis Systems have also been discussed. Moreover, this paper emphasizes on deep learning based end-to-end speech synthesis models which have achieved spectacular achievement in terms of mean opinion score (MOS).

</details>

### [Speaker disentanglement in video-to-speech conversion](2105.09652.md)
**Dan Oneata, Adriana Stan, Horia Cucu** · 2021-05-20

<details>
<summary>Abstract</summary>

The task of video-to-speech aims to translate silent video of lip movement to its corresponding audio signal. Previous approaches to this task are generally limited to the case of a single speaker, but a method that accounts for multiple speakers is desirable as it allows to i) leverage datasets with multiple speakers or few samples per speaker; and ii) control speaker identity at inference time. In this paper, we introduce a new video-to-speech architecture and explore ways of extending it to the multi-speaker scenario: we augment the network with an additional speaker-related input, through which we feed either a discrete identity or a speaker embedding. Interestingly, we observe that the visual encoder of the network is capable of learning the speaker identity from the lip region of the face alone. To better disentangle the two inputs -- linguistic content and speaker identity -- we add adversarial losses that dispel the identity from the video embeddings. To the best of our knowledge, the proposed method is the first to provide important functionalities such as i) control of the target voice and ii) speech synthesis for unseen identities over the state-of-the-art, while still maintaining the intelligibility of the spoken output.

</details>

### [Low-Latency Real-Time Non-Parallel Voice Conversion based on Cyclic Variational Autoencoder and Multiband WaveRNN with Data-Driven Linear Prediction](2105.09858.md)
**Patrick Lumban Tobing, Tomoki Toda** · 2021-05-20

<details>
<summary>Abstract</summary>

This paper presents a low-latency real-time (LLRT) non-parallel voice conversion (VC) framework based on cyclic variational autoencoder (CycleVAE) and multiband WaveRNN with data-driven linear prediction (MWDLP). CycleVAE is a robust non-parallel multispeaker spectral model, which utilizes a speaker-independent latent space and a speaker-dependent code to generate reconstructed/converted spectral features given the spectral features of an input speaker. On the other hand, MWDLP is an efficient and a high-quality neural vocoder that can handle multispeaker data and generate speech waveform for LLRT applications with CPU. To accommodate LLRT constraint with CPU, we propose a novel CycleVAE framework that utilizes mel-spectrogram as spectral features and is built with a sparse network architecture. Further, to improve the modeling performance, we also propose a novel fine-tuning procedure that refines the frame-rate CycleVAE network by utilizing the waveform loss from the MWDLP network. The experimental results demonstrate that the proposed framework achieves high-performance VC, while allowing for LLRT usage with a single-core of $2.1$--$2.7$ GHz CPU on a real-time factor of $0.87$--$0.95$, including input/output, feature extraction, on a frame shift of $10$ ms, a window length of $27.5$ ms, and $2$ lookup frames.

</details>

### [High-Fidelity and Low-Latency Universal Neural Vocoder based on Multiband WaveRNN with Data-Driven Linear Prediction for Discrete Waveform Modeling](2105.09856.md)
**Patrick Lumban Tobing, Tomoki Toda** · 2021-05-20

<details>
<summary>Abstract</summary>

This paper presents a novel high-fidelity and low-latency universal neural vocoder framework based on multiband WaveRNN with data-driven linear prediction for discrete waveform modeling (MWDLP). MWDLP employs a coarse-fine bit WaveRNN architecture for 10-bit mu-law waveform modeling. A sparse gated recurrent unit with a relatively large size of hidden units is utilized, while the multiband modeling is deployed to achieve real-time low-latency usage. A novel technique for data-driven linear prediction (LP) with discrete waveform modeling is proposed, where the LP coefficients are estimated in a data-driven manner. Moreover, a novel loss function using short-time Fourier transform (STFT) for discrete waveform modeling with Gumbel approximation is also proposed. The experimental results demonstrate that the proposed MWDLP framework generates high-fidelity synthetic speech for seen and unseen speakers and/or language on 300 speakers training data including clean and noisy/reverberant conditions, where the number of training utterances is limited to 60 per speaker, while allowing for real-time low-latency processing using a single core of $\sim\!$ 2.1--2.7 GHz CPU with $\sim\!$ 0.57--0.64 real-time factor including input/output and feature extraction.

</details>

### [Disentanglement Learning for Variational Autoencoders Applied to Audio-Visual Speech Enhancement](2105.08970.md)
**Guillaume Carbajal, Julius Richter, Timo Gerkmann** · 2021-05-19

<details>
<summary>Abstract</summary>

Recently, the standard variational autoencoder has been successfully used to learn a probabilistic prior over speech signals, which is then used to perform speech enhancement. Variational autoencoders have then been conditioned on a label describing a high-level speech attribute (e.g. speech activity) that allows for a more explicit control of speech generation. However, the label is not guaranteed to be disentangled from the other latent variables, which results in limited performance improvements compared to the standard variational autoencoder. In this work, we propose to use an adversarial training scheme for variational autoencoders to disentangle the label from the other latent variables. At training, we use a discriminator that competes with the encoder of the variational autoencoder. Simultaneously, we also use an additional encoder that estimates the label for the decoder of the variational autoencoder, which proves to be crucial to learn disentanglement. We show the benefit of the proposed disentanglement learning when a voice activity label, estimated from visual data, is used for speech enhancement.

</details>

### [ItôTTS and ItôWave: Linear Stochastic Differential Equation Is All You Need For Audio Generation](2105.07583.md)
**Shoule Wu, Ziqiang Shi** · 2021-05-17

<details>
<summary>Abstract</summary>

In this paper, we propose to unify the two aspects of voice synthesis, namely text-to-speech (TTS) and vocoder, into one framework based on a pair of forward and reverse-time linear stochastic differential equations (SDE). The solutions of this SDE pair are two stochastic processes, one of which turns the distribution of mel spectrogram (or wave), that we want to generate, into a simple and tractable distribution. The other is the generation procedure that turns this tractable simple signal into the target mel spectrogram (or wave). The model that generates mel spectrogram is called ItôTTS, and the model that generates wave is called ItôWave. ItôTTS and ItôWave use the Wiener process as a driver to gradually subtract the excess signal from the noise signal to generate realistic corresponding meaningful mel spectrogram and audio respectively, under the conditional inputs of original text or mel spectrogram. The results of the experiment show that the mean opinion scores (MOS) of ItôTTS and ItôWave can exceed the current state-of-the-art methods, and reached 3.925$\pm$0.160 and 4.35$\pm$0.115 respectively. The generated audio samples are available at https://wushoule.github.io/ItoAudio/. All authors contribute equally to this work.

</details>

### [Grad-TTS: A Diffusion Probabilistic Model for Text-to-Speech](2105.06337.md)
**Vadim Popov, Ivan Vovk, Vladimir Gogoryan, Tasnima Sadekova et al.** · 2021-05-13

<details>
<summary>Abstract</summary>

Recently, denoising diffusion probabilistic models and generative score matching have shown high potential in modelling complex data distributions while stochastic calculus has provided a unified point of view on these techniques allowing for flexible inference schemes. In this paper we introduce Grad-TTS, a novel text-to-speech model with score-based decoder producing mel-spectrograms by gradually transforming noise predicted by encoder and aligned with text input by means of Monotonic Alignment Search. The framework of stochastic differential equations helps us to generalize conventional diffusion probabilistic models to the case of reconstructing data from noise with different parameters and allows to make this reconstruction flexible by explicitly controlling trade-off between sound quality and inference speed. Subjective human evaluation shows that Grad-TTS is competitive with state-of-the-art text-to-speech approaches in terms of Mean Opinion Score. We will make the code publicly available shortly.

</details>

### [Learning Robust Latent Representations for Controllable Speech Synthesis](2105.04458.md)
**Shakti Kumar, Jithin Pradeep, Hussain Zaidi** · 2021-05-10

<details>
<summary>Abstract</summary>

State-of-the-art Variational Auto-Encoders (VAEs) for learning disentangled latent representations give impressive results in discovering features like pitch, pause duration, and accent in speech data, leading to highly controllable text-to-speech (TTS) synthesis. However, these LSTM-based VAEs fail to learn latent clusters of speaker attributes when trained on either limited or noisy datasets. Further, different latent variables start encoding the same features, limiting the control and expressiveness during speech synthesis. To resolve these issues, we propose RTI-VAE (Reordered Transformer with Information reduction VAE) where we minimize the mutual information between different latent variables and devise a modified Transformer architecture with layer reordering to learn controllable latent representations in speech data. We show that RTI-VAE reduces the cluster overlap of speaker attributes by at least 30\% over LSTM-VAE and by at least 7\% over vanilla Transformer-VAE.

</details>

### [MASS: Multi-task Anthropomorphic Speech Synthesis Framework](2105.04124.md)
**Jinyin Chen, Linhui Ye, Zhaoyan Ming** · 2021-05-10

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) synthesis plays an important role in human-computer interaction. Currently, most TTS technologies focus on the naturalness of speech, namely,making the speeches sound like humans. However, the key tasks of the expression of emotion and the speaker identity are ignored, which limits the application scenarios of TTS synthesis technology. To make the synthesized speech more realistic and expand the application scenarios, we propose a multi-task anthropomorphic speech synthesis framework (MASS), which can synthesize speeches from text with specified emotion and speaker identity. The MASS framework consists of a base TTS module and two novel voice conversion modules: the emotional voice conversion module and the speaker voice conversion module. We propose deep emotion voice conversion model (DEVC) and deep speaker voice conversion model (DSVC) based on convolution residual networks. It solves the problem of feature loss during voice conversion. The model trainings are independent of parallel datasets, and are capable of many-to-many voice conversion. In the emotional voice conversion, speaker voice conversion experiments, as well as the multi-task speech synthesis experiments, experimental results show DEVC and DSVC convert speech effectively. The quantitative and qualitative evaluation results of multi-task speech synthesis experiments show MASS can effectively synthesis speech with specified text, emotion and speaker identity.

</details>

### [DiffSinger: Singing Voice Synthesis via Shallow Diffusion Mechanism](2105.02446.md)
**Jinglin Liu, Chengxi Li, Yi Ren, Feiyang Chen et al.** · 2021-05-06

<details>
<summary>Abstract</summary>

Singing voice synthesis (SVS) systems are built to synthesize high-quality and expressive singing voice, in which the acoustic model generates the acoustic features (e.g., mel-spectrogram) given a music score. Previous singing acoustic models adopt a simple loss (e.g., L1 and L2) or generative adversarial network (GAN) to reconstruct the acoustic features, while they suffer from over-smoothing and unstable training issues respectively, which hinder the naturalness of synthesized singing. In this work, we propose DiffSinger, an acoustic model for SVS based on the diffusion probabilistic model. DiffSinger is a parameterized Markov chain that iteratively converts the noise into mel-spectrogram conditioned on the music score. By implicitly optimizing variational bound, DiffSinger can be stably trained and generate realistic outputs. To further improve the voice quality and speed up inference, we introduce a shallow diffusion mechanism to make better use of the prior knowledge learned by the simple loss. Specifically, DiffSinger starts generation at a shallow step smaller than the total number of diffusion steps, according to the intersection of the diffusion trajectories of the ground-truth mel-spectrogram and the one predicted by a simple mel-spectrogram decoder. Besides, we propose boundary prediction methods to locate the intersection and determine the shallow step adaptively. The evaluations conducted on a Chinese singing dataset demonstrate that DiffSinger outperforms state-of-the-art SVS work. Extensional experiments also prove the generalization of our methods on text-to-speech task (DiffSpeech). Audio samples: https://diffsinger.github.io. Codes: https://github.com/MoonInTheRiver/DiffSinger. The old title of this work: "Diffsinger: Diffusion acoustic model for singing voice synthesis".

</details>

### [How do Voices from Past Speech Synthesis Challenges Compare Today?](2105.02373.md)
**Erica Cooper, Junichi Yamagishi** · 2021-05-05

<details>
<summary>Abstract</summary>

Shared challenges provide a venue for comparing systems trained on common data using a standardized evaluation, and they also provide an invaluable resource for researchers when the data and evaluation results are publicly released. The Blizzard Challenge and Voice Conversion Challenge are two such challenges for text-to-speech synthesis and for speaker conversion, respectively, and their publicly-available system samples and listening test results comprise a historical record of state-of-the-art synthesis methods over the years. In this paper, we revisit these past challenges and conduct a large-scale listening test with samples from many challenges combined. Our aims are to analyze and compare opinions of a large number of systems together, to determine whether and how opinions change over time, and to collect a large-scale dataset of a diverse variety of synthetic samples and their ratings for further research. We found strong correlations challenge by challenge at the system level between the original results and our new listening test. We also observed the importance of the choice of speaker on synthesis quality.

</details>

### [Voice Conversion Based Speaker Normalization for Acoustic Unit Discovery](2105.01786.md)
**Thomas Glarner, Janek Ebbers, Reinhold Häb-Umbach** · 2021-05-04

<details>
<summary>Abstract</summary>

Discovering speaker independent acoustic units purely from spoken input is known to be a hard problem. In this work we propose an unsupervised speaker normalization technique prior to unit discovery. It is based on separating speaker related from content induced variations in a speech signal with an adversarial contrastive predictive coding approach. This technique does neither require transcribed speech nor speaker labels, and, furthermore, can be trained in a multilingual fashion, thus achieving speaker normalization even if only few unlabeled data is available from the target language. The speaker normalization is done by mapping all utterances to a medoid style which is representative for the whole database. We demonstrate the effectiveness of the approach by conducting acoustic unit discovery with a hidden Markov model variational autoencoder noting, however, that the proposed speaker normalization can serve as a front end to any unit discovery system. Experiments on English, Yoruba and Mboshi show improvements compared to using non-normalized input.

</details>

### [Towards a practical lip-to-speech conversion system using deep neural networks and mobile application frontend](2104.14467.md)
**Frigyes Viktor Arthur, Tamás Gábor Csapó** · 2021-04-29

<details>
<summary>Abstract</summary>

Articulatory-to-acoustic (forward) mapping is a technique to predict speech using various articulatory acquisition techniques as input (e.g. ultrasound tongue imaging, MRI, lip video). The advantage of lip video is that it is easily available and affordable: most modern smartphones have a front camera. There are already a few solutions for lip-to-speech synthesis, but they mostly concentrate on offline training and inference. In this paper, we propose a system built from a backend for deep neural network training and inference and a fronted as a form of a mobile application. Our initial evaluation shows that the scenario is feasible: a top-5 classification accuracy of 74% is combined with feedback from the mobile application user, making sure that the speaking impaired might be able to communicate with this solution.

</details>

### [End-to-End Video-To-Speech Synthesis using Generative Adversarial Networks](2104.13332.md)
**Rodrigo Mira, Konstantinos Vougioukas, Pingchuan Ma, Stavros Petridis et al.** · 2021-04-27

<details>
<summary>Abstract</summary>

Video-to-speech is the process of reconstructing the audio speech from a video of a spoken utterance. Previous approaches to this task have relied on a two-step process where an intermediate representation is inferred from the video, and is then decoded into waveform audio using a vocoder or a waveform reconstruction algorithm. In this work, we propose a new end-to-end video-to-speech model based on Generative Adversarial Networks (GANs) which translates spoken video to waveform end-to-end without using any intermediate representation or separate waveform synthesis algorithm. Our model consists of an encoder-decoder architecture that receives raw video as input and generates speech, which is then fed to a waveform critic and a power critic. The use of an adversarial loss based on these two critics enables the direct synthesis of raw audio waveform and ensures its realism. In addition, the use of our three comparative losses helps establish direct correspondence between the generated audio and the input video. We show that this model is able to reconstruct speech with remarkable realism for constrained datasets such as GRID, and that it is the first end-to-end model to produce intelligible speech for LRW (Lip Reading in the Wild), featuring hundreds of speakers recorded entirely `in the wild'. We evaluate the generated samples in two different scenarios -- seen and unseen speakers -- using four objective metrics which measure the quality and intelligibility of artificial speech. We demonstrate that the proposed approach outperforms all previous works in most metrics on GRID and LRW.

</details>

### [Phrase break prediction with bidirectional encoder representations in Japanese text-to-speech synthesis](2104.12395.md)
**Kosuke Futamata, Byeongseon Park, Ryuichi Yamamoto, Kentaro Tachibana** · 2021-04-26

<details>
<summary>Abstract</summary>

We propose a novel phrase break prediction method that combines implicit features extracted from a pre-trained large language model, a.k.a BERT, and explicit features extracted from BiLSTM with linguistic features. In conventional BiLSTM based methods, word representations and/or sentence representations are used as independent components. The proposed method takes account of both representations to extract the latent semantics, which cannot be captured by previous methods. The objective evaluation results show that the proposed method obtains an absolute improvement of 3.2 points for the F1 score compared with BiLSTM-based conventional methods using linguistic features. Moreover, the perceptual listening test results verify that a TTS system that applied our proposed method achieved a mean opinion score of 4.39 in prosody naturalness, which is highly competitive with the score of 4.37 for synthesized speech with ground-truth phrase breaks.

</details>

### [Text-to-Speech Synthesis Techniques for MIDI-to-Audio Synthesis](2104.12292.md)
**Erica Cooper, Xin Wang, Junichi Yamagishi** · 2021-04-25

<details>
<summary>Abstract</summary>

Speech synthesis and music audio generation from symbolic input differ in many aspects but share some similarities. In this study, we investigate how text-to-speech synthesis techniques can be used for piano MIDI-to-audio synthesis tasks. Our investigation includes Tacotron and neural source-filter waveform models as the basic components, with which we build MIDI-to-audio synthesis systems in similar ways to TTS frameworks. We also include reference systems using conventional sound modeling techniques such as sample-based and physical-modeling-based methods. The subjective experimental results demonstrate that the investigated TTS components can be applied to piano MIDI-to-audio synthesis with minor modifications. The results also reveal the performance bottleneck -- while the waveform model can synthesize high quality piano sound given natural acoustic features, the conversion from MIDI to acoustic features is challenging. The full MIDI-to-audio synthesis system is still inferior to the sample-based or physical-modeling-based approaches, but we encourage TTS researchers to test their TTS models for this new task and improve the performance.

</details>

### [An Adaptive Learning based Generative Adversarial Network for One-To-One Voice Conversion](2104.12159.md)
**Sandipan Dhar, Nanda Dulal Jana, Swagatam Das** · 2021-04-25

<details>
<summary>Abstract</summary>

Voice Conversion (VC) emerged as a significant domain of research in the field of speech synthesis in recent years due to its emerging application in voice-assisting technology, automated movie dubbing, and speech-to-singing conversion to name a few. VC basically deals with the conversion of vocal style of one speaker to another speaker while keeping the linguistic contents unchanged. VC task is performed through a three-stage pipeline consisting of speech analysis, speech feature mapping, and speech reconstruction. Nowadays the Generative Adversarial Network (GAN) models are widely in use for speech feature mapping from source to target speaker. In this paper, we propose an adaptive learning-based GAN model called ALGAN-VC for an efficient one-to-one VC of speakers. Our ALGAN-VC framework consists of some approaches to improve the speech quality and voice similarity between source and target speakers. The model incorporates a Dense Residual Network (DRN) like architecture to the generator network for efficient speech feature learning, for source to target speech feature conversion. We also integrate an adaptive learning mechanism to compute the loss function for the proposed model. Moreover, we use a boosted learning rate approach to enhance the learning capability of the proposed model. The model is trained by using both forward and inverse mapping simultaneously for a one-to-one VC. The proposed model is tested on Voice Conversion Challenge (VCC) 2016, 2018, and 2020 datasets as well as on our self-prepared speech dataset, which has been recorded in Indian regional languages and in English. A subjective and objective evaluation of the generated speech samples indicated that the proposed model elegantly performed the voice conversion task by achieving high speaker similarity and adequate speech quality.

</details>

### [Deep Learning Based Assessment of Synthetic Speech Naturalness](2104.11673.md)
**Gabriel Mittag, Sebastian Möller** · 2021-04-23

<details>
<summary>Abstract</summary>

In this paper, we present a new objective prediction model for synthetic speech naturalness. It can be used to evaluate Text-To-Speech or Voice Conversion systems and works language independently. The model is trained end-to-end and based on a CNN-LSTM network that previously showed to give good results for speech quality estimation. We trained and tested the model on 16 different datasets, such as from the Blizzard Challenge and the Voice Conversion Challenge. Further, we show that the reliability of deep learning-based naturalness prediction can be improved by transfer learning from speech quality prediction models that are trained on objective POLQA scores. The proposed model is made publicly available and can, for example, be used to evaluate different TTS system configurations.

</details>

### [Reconstructing Speech from Real-Time Articulatory MRI Using Neural Vocoders](2104.11598.md)
**Yide Yu, Amin Honarmandi Shandiz, László Tóth** · 2021-04-23

<details>
<summary>Abstract</summary>

Several approaches exist for the recording of articulatory movements, such as eletromagnetic and permanent magnetic articulagraphy, ultrasound tongue imaging and surface electromyography. Although magnetic resonance imaging (MRI) is more costly than the above approaches, the recent developments in this area now allow the recording of real-time MRI videos of the articulators with an acceptable resolution. Here, we experiment with the reconstruction of the speech signal from a real-time MRI recording using deep neural networks. Instead of estimating speech directly, our networks are trained to output a spectral vector, from which we reconstruct the speech signal using the WaveGlow neural vocoder. We compare the performance of three deep neural architectures for the estimation task, combining convolutional (CNN) and recurrence-based (LSTM) neural layers. Besides the mean absolute error (MAE) of our networks, we also evaluate our models by comparing the speech signals obtained using several objective speech quality metrics like the mean cepstral distortion (MCD), Short-Time Objective Intelligibility (STOI), Perceptual Evaluation of Speech Quality (PESQ) and Signal-to-Distortion Ratio (SDR). The results indicate that our approach can successfully reconstruct the gross spectral shape, but more improvements are needed to reproduce the fine spectral details.

</details>

### [Building Bilingual and Code-Switched Voice Conversion with Limited Training Data Using Embedding Consistency Loss](2104.10832.md)
**Yaogen Yang, Haozhe Zhang, Xiaoyi Qin, Shanshan Liang et al.** · 2021-04-22

<details>
<summary>Abstract</summary>

Building cross-lingual voice conversion (VC) systems for multiple speakers and multiple languages has been a challenging task for a long time. This paper describes a parallel non-autoregressive network to achieve bilingual and code-switched voice conversion for multiple speakers when there are only mono-lingual corpora for each language. We achieve cross-lingual VC between Mandarin speech with multiple speakers and English speech with multiple speakers by applying bilingual bottleneck features. To boost voice cloning performance, we use an adversarial speaker classifier with a gradient reversal layer to reduce the source speaker's information from the output of encoder. Furthermore, in order to improve speaker similarity between reference speech and converted speech, we adopt an embedding consistency loss between the synthesized speech and its natural reference speech in our network. Experimental results show that our proposed method can achieve high quality converted speech with mean opinion score (MOS) around 4. The conversion system performs well in terms of speaker similarity for both in-set speaker conversion and out-set-of one-shot conversion.

</details>

### [AdaSpeech 2: Adaptive Text to Speech with Untranscribed Data](2104.09715.md)
**Yuzi Yan, Xu Tan, Bohan Li, Tao Qin et al.** · 2021-04-20

<details>
<summary>Abstract</summary>

Text to speech (TTS) is widely used to synthesize personal voice for a target speaker, where a well-trained source TTS model is fine-tuned with few paired adaptation data (speech and its transcripts) on this target speaker. However, in many scenarios, only untranscribed speech data is available for adaptation, which brings challenges to the previous TTS adaptation pipelines (e.g., AdaSpeech). In this paper, we develop AdaSpeech 2, an adaptive TTS system that only leverages untranscribed speech data for adaptation. Specifically, we introduce a mel-spectrogram encoder to a well-trained TTS model to conduct speech reconstruction, and at the same time constrain the output sequence of the mel-spectrogram encoder to be close to that of the original phoneme encoder. In adaptation, we use untranscribed speech data for speech reconstruction and only fine-tune the TTS decoder. AdaSpeech 2 has two advantages: 1) Pluggable: our system can be easily applied to existing trained TTS models without re-training. 2) Effective: our system achieves on-par voice quality with the transcribed TTS adaptation (e.g., AdaSpeech) with the same amount of untranscribed data, and achieves better voice quality than previous untranscribed adaptation methods. Synthesized speech samples can be found at https://speechresearch.github.io/adaspeech2/.

</details>

### [Review of end-to-end speech synthesis technology based on deep learning](2104.09995.md)
**Zhaoxi Mu, Xinyu Yang, Yizhuo Dong** · 2021-04-20

<details>
<summary>Abstract</summary>

As an indispensable part of modern human-computer interaction system, speech synthesis technology helps users get the output of intelligent machine more easily and intuitively, thus has attracted more and more attention. Due to the limitations of high complexity and low efficiency of traditional speech synthesis technology, the current research focus is the deep learning-based end-to-end speech synthesis technology, which has more powerful modeling ability and a simpler pipeline. It mainly consists of three modules: text front-end, acoustic model, and vocoder. This paper reviews the research status of these three parts, and classifies and compares various methods according to their emphasis. Moreover, this paper also summarizes the open-source speech corpus of English, Chinese and other languages that can be used for speech synthesis tasks, and introduces some commonly used subjective and objective speech quality evaluation method. Finally, some attractive future research directions are pointed out.

</details>

### [KazakhTTS: An Open-Source Kazakh Text-to-Speech Synthesis Dataset](2104.08459.md)
**Saida Mussakhojayeva, Aigerim Janaliyeva, Almas Mirzakhmetov, Yerbolat Khassanov et al.** · 2021-04-17

<details>
<summary>Abstract</summary>

This paper introduces a high-quality open-source speech synthesis dataset for Kazakh, a low-resource language spoken by over 13 million people worldwide. The dataset consists of about 93 hours of transcribed audio recordings spoken by two professional speakers (female and male). It is the first publicly available large-scale dataset developed to promote Kazakh text-to-speech (TTS) applications in both academia and industry. In this paper, we share our experience by describing the dataset development procedures and faced challenges, and discuss important future directions. To demonstrate the reliability of our dataset, we built baseline end-to-end TTS models and evaluated them using the subjective mean opinion score (MOS) measure. Evaluation results show that the best TTS models trained on our dataset achieve MOS above 4 for both speakers, which makes them applicable for practical use. The dataset, training recipe, and pretrained TTS models are freely available.

</details>

### [TalkNet 2: Non-Autoregressive Depth-Wise Separable Convolutional Model for Speech Synthesis with Explicit Pitch and Duration Prediction](2104.08189.md)
**Stanislav Beliaev, Boris Ginsburg** · 2021-04-16

<details>
<summary>Abstract</summary>

We propose TalkNet, a non-autoregressive convolutional neural model for speech synthesis with explicit pitch and duration prediction. The model consists of three feed-forward convolutional networks. The first network predicts grapheme durations. An input text is expanded by repeating each symbol according to the predicted duration. The second network predicts pitch value for every mel frame. The third network generates a mel-spectrogram from the expanded text conditioned on predicted pitch. All networks are based on 1D depth-wise separable convolutional architecture. The explicit duration prediction eliminates word skipping and repeating. The quality of the generated speech nearly matches the best auto-regressive models - TalkNet trained on the LJSpeech dataset got MOS 4.08. The model has only 13.2M parameters, almost 2x less than the present state-of-the-art text-to-speech models. The non-autoregressive architecture allows for fast training and inference. The small model size and fast inference make the TalkNet an attractive candidate for embedded speech synthesis.

</details>

### [Proteno: Text Normalization with Limited Data for Fast Deployment in Text to Speech Systems](2104.07777.md)
**Shubhi Tyagi, Antonio Bonafonte, Jaime Lorenzo-Trueba, Javier Latorre** · 2021-04-15

<details>
<summary>Abstract</summary>

Developing Text Normalization (TN) systems for Text-to-Speech (TTS) on new languages is hard. We propose a novel architecture to facilitate it for multiple languages while using data less than 3% of the size of the data used by the state of the art results on English. We treat TN as a sequence classification problem and propose a granular tokenization mechanism that enables the system to learn majority of the classes and their normalizations from the training data itself. This is further combined with minimal precoded linguistic knowledge for other classes. We publish the first results on TN for TTS in Spanish and Tamil and also demonstrate that the performance of the approach is comparable with the previous work done on English. All annotated datasets used for experimentation will be released at https://github.com/amazon-research/proteno.

</details>

### [Towards end-to-end F0 voice conversion based on Dual-GAN with convolutional wavelet kernels](2104.07283.md)
**Clément Le Moine Veillon, Nicolas Obin, Axel Roebel** · 2021-04-15

<details>
<summary>Abstract</summary>

This paper presents a end-to-end framework for the F0 transformation in the context of expressive voice conversion. A single neural network is proposed, in which a first module is used to learn F0 representation over different temporal scales and a second adversarial module is used to learn the transformation from one emotion to another. The first module is composed of a convolution layer with wavelet kernels so that the various temporal scales of F0 variations can be efficiently encoded. The single decomposition/transformation network allows to learn in a end-to-end manner the F0 decomposition that are optimal with respect to the transformation, directly from the raw F0 signal.

</details>

### [Enhancing Word-Level Semantic Representation via Dependency Structure for Expressive Text-to-Speech Synthesis](2104.06835.md)
**Yixuan Zhou, Changhe Song, Jingbei Li, Zhiyong Wu et al.** · 2021-04-14

<details>
<summary>Abstract</summary>

Exploiting rich linguistic information in raw text is crucial for expressive text-to-speech (TTS). As large scale pre-trained text representation develops, bidirectional encoder representations from Transformers (BERT) has been proven to embody semantic information and employed to TTS recently. However, original or simply fine-tuned BERT embeddings still cannot provide sufficient semantic knowledge that expressive TTS models should take into account. In this paper, we propose a word-level semantic representation enhancing method based on dependency structure and pre-trained BERT embedding. The BERT embedding of each word is reprocessed considering its specific dependencies and related words in the sentence, to generate more effective semantic representation for TTS. To better utilize the dependency structure, relational gated graph network (RGGN) is introduced to make semantic information flow and aggregate through the dependency structure. The experimental results show that the proposed method can further improve the naturalness and expressiveness of synthesized speeches on both Mandarin and English datasets.

</details>

### [Non-autoregressive sequence-to-sequence voice conversion](2104.06793.md)
**Tomoki Hayashi, Wen-Chin Huang, Kazuhiro Kobayashi, Tomoki Toda** · 2021-04-14

<details>
<summary>Abstract</summary>

This paper proposes a novel voice conversion (VC) method based on non-autoregressive sequence-to-sequence (NAR-S2S) models. Inspired by the great success of NAR-S2S models such as FastSpeech in text-to-speech (TTS), we extend the FastSpeech2 model for the VC problem. We introduce the convolution-augmented Transformer (Conformer) instead of the Transformer, making it possible to capture both local and global context information from the input sequence. Furthermore, we extend variance predictors to variance converters to explicitly convert the source speaker's prosody components such as pitch and energy into the target speaker. The experimental evaluation with the Japanese speaker dataset, which consists of male and female speakers of 1,000 utterances, demonstrates that the proposed model enables us to perform more stable, faster, and better conversion than autoregressive S2S (AR-S2S) models such as Tacotron2 and Transformer.

</details>

### [FastS2S-VC: Streaming Non-Autoregressive Sequence-to-Sequence Voice Conversion](2104.06900.md)
**Hirokazu Kameoka, Kou Tanaka, Takuhiro Kaneko** · 2021-04-14

<details>
<summary>Abstract</summary>

This paper proposes a non-autoregressive extension of our previously proposed sequence-to-sequence (S2S) model-based voice conversion (VC) methods. S2S model-based VC methods have attracted particular attention in recent years for their flexibility in converting not only the voice identity but also the pitch contour and local duration of input speech, thanks to the ability of the encoder-decoder architecture with the attention mechanism. However, one of the obstacles to making these methods work in real-time is the autoregressive (AR) structure. To overcome this obstacle, we develop a method to obtain a model that is free from an AR structure and behaves similarly to the original S2S models, based on a teacher-student learning framework. In our method, called "FastS2S-VC", the student model consists of encoder, decoder, and attention predictor. The attention predictor learns to predict attention distributions solely from source speech along with a target class index with the guidance of those predicted by the teacher model from both source and target speech. Thanks to this structure, the model is freed from an AR structure and allows for parallelization. Furthermore, we show that FastS2S-VC is suitable for real-time implementation based on a sliding-window approach, and describe how to make it run in real-time. Through speaker-identity and emotional-expression conversion experiments, we confirmed that FastS2S-VC was able to speed up the conversion process by 70 to 100 times compared to the original AR-type S2S-VC methods, without significantly degrading the audio quality and similarity to target speech. We also confirmed that the real-time version of FastS2S-VC can be run with a latency of 32 ms when run on a GPU.

</details>

### [NoiseVC: Towards High Quality Zero-Shot Voice Conversion](2104.06074.md)
**Shijun Wang, Damian Borth** · 2021-04-13

<details>
<summary>Abstract</summary>

Voice conversion (VC) is a task that transforms voice from target audio to source without losing linguistic contents, it is challenging especially when source and target speakers are unseen during training (zero-shot VC). Previous approaches require a pre-trained model or linguistic data to do the zero-shot conversion. Meanwhile, VC models with Vector Quantization (VQ) or Instance Normalization (IN) are able to disentangle contents from audios and achieve successful conversions. However, disentanglement in these models highly relies on heavily constrained bottleneck layers, thus, the sound quality is drastically sacrificed. In this paper, we propose NoiseVC, an approach that can disentangle contents based on VQ and Contrastive Predictive Coding (CPC). Additionally, Noise Augmentation is performed to further enhance disentanglement capability. We conduct several experiments and demonstrate that NoiseVC has a strong disentanglement ability with a small sacrifice of quality.

</details>

### [Unified Source-Filter GAN: Unified Source-filter Network Based On Factorization of Quasi-Periodic Parallel WaveGAN](2104.04668.md)
**Reo Yoneyama, Yi-Chiao Wu, Tomoki Toda** · 2021-04-10

<details>
<summary>Abstract</summary>

We propose a unified approach to data-driven source-filter modeling using a single neural network for developing a neural vocoder capable of generating high-quality synthetic speech waveforms while retaining flexibility of the source-filter model to control their voice characteristics. Our proposed network called unified source-filter generative adversarial networks (uSFGAN) is developed by factorizing quasi-periodic parallel WaveGAN (QPPWG), one of the neural vocoders based on a single neural network, into a source excitation generation network and a vocal tract resonance filtering network by additionally implementing a regularization loss. Moreover, inspired by neural source filter (NSF), only a sinusoidal waveform is additionally used as the simplest clue to generate a periodic source excitation waveform while minimizing the effect of approximations in the source filter model. The experimental results demonstrate that uSFGAN outperforms conventional neural vocoders, such as QPPWG and NSF in both speech quality and pitch controllability.

</details>

### [Grapheme-to-Phoneme Transformer Model for Transfer Learning Dialects](2104.04091.md)
**Eric Engelhart, Mahsa Elyasi, Gaurav Bharaj** · 2021-04-08

<details>
<summary>Abstract</summary>

Grapheme-to-Phoneme (G2P) models convert words to their phonetic pronunciations. Classic G2P methods include rule-based systems and pronunciation dictionaries, while modern G2P systems incorporate learning, such as, LSTM and Transformer-based attention models. Usually, dictionary-based methods require significant manual effort to build, and have limited adaptivity on unseen words. And transformer-based models require significant training data, and do not generalize well, especially for dialects with limited data. We propose a novel use of transformer-based attention model that can adapt to unseen dialects of English language, while using a small dictionary. We show that our method has potential applications for accent transfer for text-to-speech, and for building robust G2P models for dialects with limited pronunciation dictionary size. We experiment with two English dialects: Indian and British. A model trained from scratch using 1000 words from British English dictionary, with 14211 words held out, leads to phoneme error rate (PER) of 26.877%, on a test set generated using the full dictionary. The same model pretrained on CMUDict American English dictionary, and fine-tuned on the same dataset leads to PER of 2.469% on the test set.

</details>

### [Flavored Tacotron: Conditional Learning for Prosodic-linguistic Features](2104.04050.md)
**Mahsa Elyasi, Gaurav Bharaj** · 2021-04-08

<details>
<summary>Abstract</summary>

Neural sequence-to-sequence text-to-speech synthesis (TTS), such as Tacotron-2, transforms text into high-quality speech. However, generating speech with natural prosody still remains a challenge. Yasuda et. al. show that unlike natural speech, Tacotron-2's encoder doesn't fully represent prosodic features (e.g. syllable stress in English) from characters, and result in flat fundamental frequency variations. In this work, we propose a novel carefully designed strategy for conditioning Tacotron-2 on two fundamental prosodic features in English -- stress syllable and pitch accent, that help achieve more natural prosody. To this end, we use of a classifier to learn these features in an end-to-end fashion, and apply feature conditioning at three parts of Tacotron-2's Text-To-Mel Spectrogram: pre-encoder, post-encoder, and intra-decoder. Further, we show that jointly conditioned features at pre-encoder and intra-decoder stages result in prosodically natural synthesized speech (vs. Tacotron-2), and allows the model to produce speech with more accurate pitch accent and stress patterns. Quantitative evaluations show that our formulation achieves higher fundamental frequency contour correlation, and lower Mel Cepstral Distortion measure between synthesized and natural speech. And subjective evaluation shows that the proposed method's Mean Opinion Score of 4.14 fairs higher than baseline Tacotron-2, 3.91, when compared against natural speech (LJSpeech corpus), 4.28.

</details>

### [Half-Truth: A Partially Fake Audio Detection Dataset](2104.03617.md)
**Jiangyan Yi, Ye Bai, Jianhua Tao, Haoxin Ma et al.** · 2021-04-08

<details>
<summary>Abstract</summary>

Diverse promising datasets have been designed to hold back the development of fake audio detection, such as ASVspoof databases. However, previous datasets ignore an attacking situation, in which the hacker hides some small fake clips in real speech audio. This poses a serious threat since that it is difficult to distinguish the small fake clip from the whole speech utterance. Therefore, this paper develops such a dataset for half-truth audio detection (HAD). Partially fake audio in the HAD dataset involves only changing a few words in an utterance.The audio of the words is generated with the very latest state-of-the-art speech synthesis technology. We can not only detect fake uttrances but also localize manipulated regions in a speech using this dataset. Some benchmark results are presented on this dataset. The results show that partially fake audio presents much more challenging than fully fake audio for fake audio detection. The HAD dataset is publicly available: https://zenodo.org/records/10377492.

</details>

### [Towards Multi-Scale Style Control for Expressive Speech Synthesis](2104.03521.md)
**Xiang Li, Changhe Song, Jingbei Li, Zhiyong Wu et al.** · 2021-04-08

<details>
<summary>Abstract</summary>

This paper introduces a multi-scale speech style modeling method for end-to-end expressive speech synthesis. The proposed method employs a multi-scale reference encoder to extract both the global-scale utterance-level and the local-scale quasi-phoneme-level style features of the target speech, which are then fed into the speech synthesis model as an extension to the input phoneme sequence. During training time, the multi-scale style model could be jointly trained with the speech synthesis model in an end-to-end fashion. By applying the proposed method to style transfer task, experimental results indicate that the controllability of the multi-scale speech style model and the expressiveness of the synthesized speech are greatly improved. Moreover, by assigning different reference speeches to extraction of style on each scale, the flexibility of the proposed method is further revealed.

</details>

### [Utilizing Self-supervised Representations for MOS Prediction](2104.03017.md)
**Wei-Cheng Tseng, Chien-yu Huang, Wei-Tsung Kao, Yist Y. Lin et al.** · 2021-04-07

<details>
<summary>Abstract</summary>

Speech quality assessment has been a critical issue in speech processing for decades. Existing automatic evaluations usually require clean references or parallel ground truth data, which is infeasible when the amount of data soars. Subjective tests, on the other hand, do not need any additional clean or parallel data and correlates better to human perception. However, such a test is expensive and time-consuming because crowd work is necessary. It thus becomes highly desired to develop an automatic evaluation approach that correlates well with human perception while not requiring ground truth data. In this paper, we use self-supervised pre-trained models for MOS prediction. We show their representations can distinguish between clean and noisy audios. Then, we fine-tune these pre-trained models followed by simple linear layers in an end-to-end manner. The experiment results showed that our framework outperforms the two previous state-of-the-art models by a significant improvement on Voice Conversion Challenge 2018 and achieves comparable or superior performance on Voice Conversion Challenge 2016. We also conducted an ablation study to further investigate how each module benefits the task. The experiment results are implemented and reproducible with publicly available toolkits.

</details>

### [S2VC: A Framework for Any-to-Any Voice Conversion with Self-Supervised Pretrained Representations](2104.02901.md)
**Jheng-hao Lin, Yist Y. Lin, Chung-Ming Chien, Hung-yi Lee** · 2021-04-07

<details>
<summary>Abstract</summary>

Any-to-any voice conversion (VC) aims to convert the timbre of utterances from and to any speakers seen or unseen during training. Various any-to-any VC approaches have been proposed like AUTOVC, AdaINVC, and FragmentVC. AUTOVC, and AdaINVC utilize source and target encoders to disentangle the content and speaker information of the features. FragmentVC utilizes two encoders to encode source and target information and adopts cross attention to align the source and target features with similar phonetic content. Moreover, pre-trained features are adopted. AUTOVC used dvector to extract speaker information, and self-supervised learning (SSL) features like wav2vec 2.0 is used in FragmentVC to extract the phonetic content information. Different from previous works, we proposed S2VC that utilizes Self-Supervised features as both source and target features for VC model. Supervised phoneme posteriororgram (PPG), which is believed to be speaker-independent and widely used in VC to extract content information, is chosen as a strong baseline for SSL features. The objective evaluation and subjective evaluation both show models taking SSL feature CPC as both source and target features outperforms that taking PPG as source feature, suggesting that SSL features have great potential in improving VC.

</details>

### [The AS-NU System for the M2VoC Challenge](2104.03009.md)
**Cheng-Hung Hu, Yi-Chiao Wu, Wen-Chin Huang, Yu-Huai Peng et al.** · 2021-04-07

<details>
<summary>Abstract</summary>

This paper describes the AS-NU systems for two tracks in MultiSpeaker Multi-Style Voice Cloning Challenge (M2VoC). The first track focuses on using a small number of 100 target utterances for voice cloning, while the second track focuses on using only 5 target utterances for voice cloning. Due to the serious lack of data in the second track, we selected the speaker most similar to the target speaker from the training data of the TTS system, and used the speaker's utterances and the given 5 target utterances to fine-tune our model. The evaluation results show that our systems on the two tracks perform similarly in terms of quality, but there is still a clear gap between the similarity score of the second track and the similarity score of the first track.

</details>

### [NU-Wave: A Diffusion Probabilistic Model for Neural Audio Upsampling](2104.02321.md)
**Junhyeok Lee, Seungu Han** · 2021-04-06

<details>
<summary>Abstract</summary>

In this work, we introduce NU-Wave, the first neural audio upsampling model to produce waveforms of sampling rate 48kHz from coarse 16kHz or 24kHz inputs, while prior works could generate only up to 16kHz. NU-Wave is the first diffusion probabilistic model for audio super-resolution which is engineered based on neural vocoders. NU-Wave generates high-quality audio that achieves high performance in terms of signal-to-noise ratio (SNR), log-spectral distance (LSD), and accuracy of the ABX test. In all cases, NU-Wave outperforms the baseline models despite the substantially smaller model capacity (3.0M parameters) than baselines (5.4-21%). The audio samples of our model are available at https://mindslab-ai.github.io/nuwave, and the code will be made available soon.

</details>

### [StarGAN-based Emotional Voice Conversion for Japanese Phrases](2104.01807.md)
**Asuka Moritani, Ryo Ozaki, Shoki Sakamoto, Hirokazu Kameoka et al.** · 2021-04-05

<details>
<summary>Abstract</summary>

This paper shows that StarGAN-VC, a spectral envelope transformation method for non-parallel many-to-many voice conversion (VC), is capable of emotional VC (EVC). Although StarGAN-VC has been shown to enable speaker identity conversion, its capability for EVC for Japanese phrases has not been clarified. In this paper, we describe the direct application of StarGAN-VC to an EVC task with minimal fundamental frequency and aperiodicity processing. Through subjective evaluation experiments, we evaluated the performance of our StarGAN-EVC system in terms of its ability to achieve EVC for Japanese phrases. The subjective evaluation is conducted in terms of subjective classification and mean opinion score of neutrality and similarity. In addition, the interdependence between the source and target emotional domains was investigated from the perspective of the quality of EVC.

</details>

### [The Multi-speaker Multi-style Voice Cloning Challenge 2021](2104.01818.md)
**Qicong Xie, Xiaohai Tian, Guanghou Liu, Kun Song et al.** · 2021-04-05

<details>
<summary>Abstract</summary>

The Multi-speaker Multi-style Voice Cloning Challenge (M2VoC) aims to provide a common sizable dataset as well as a fair testbed for the benchmarking of the popular voice cloning task. Specifically, we formulate the challenge to adapt an average TTS model to the stylistic target voice with limited data from target speaker, evaluated by speaker identity and style similarity. The challenge consists of two tracks, namely few-shot track and one-shot track, where the participants are required to clone multiple target voices with 100 and 5 samples respectively. There are also two sub-tracks in each track. For sub-track a, to fairly compare different strategies, the participants are allowed to use only the training data provided by the organizer strictly. For sub-track b, the participants are allowed to use any data publicly available. In this paper, we present a detailed explanation on the tasks and data used in the challenge, followed by a summary of submitted systems and evaluation results.

</details>

### [Hi-Fi Multi-Speaker English TTS Dataset](2104.01497.md)
**Evelina Bakhturina, Vitaly Lavrukhin, Boris Ginsburg, Yang Zhang** · 2021-04-03

<details>
<summary>Abstract</summary>

This paper introduces a new multi-speaker English dataset for training text-to-speech models. The dataset is based on LibriVox audiobooks and Project Gutenberg texts, both in the public domain. The new dataset contains about 292 hours of speech from 10 speakers with at least 17 hours per speaker sampled at 44.1 kHz. To select speech samples with high quality, we considered audio recordings with a signal bandwidth of at least 13 kHz and a signal-to-noise ratio (SNR) of at least 32 dB. The dataset is publicly released at http://www.openslr.org/109/ .

</details>

### [Diff-TTS: A Denoising Diffusion Model for Text-to-Speech](2104.01409.md)
**Myeonghun Jeong, Hyeongju Kim, Sung Jun Cheon, Byoung Jin Choi et al.** · 2021-04-03

<details>
<summary>Abstract</summary>

Although neural text-to-speech (TTS) models have attracted a lot of attention and succeeded in generating human-like speech, there is still room for improvements to its naturalness and architectural efficiency. In this work, we propose a novel non-autoregressive TTS model, namely Diff-TTS, which achieves highly natural and efficient speech synthesis. Given the text, Diff-TTS exploits a denoising diffusion framework to transform the noise signal into a mel-spectrogram via diffusion time steps. In order to learn the mel-spectrogram distribution conditioned on the text, we present a likelihood-based optimization method for TTS. Furthermore, to boost up the inference speed, we leverage the accelerated sampling method that allows Diff-TTS to generate raw waveforms much faster without significantly degrading perceptual quality. Through experiments, we verified that Diff-TTS generates 28 times faster than the real-time with a single NVIDIA 2080Ti GPU.

</details>

### [Reinforcement Learning for Emotional Text-to-Speech Synthesis with Improved Emotion Discriminability](2104.01408.md)
**Rui Liu, Berrak Sisman, Haizhou Li** · 2021-04-03

<details>
<summary>Abstract</summary>

Emotional text-to-speech synthesis (ETTS) has seen much progress in recent years. However, the generated voice is often not perceptually identifiable by its intended emotion category. To address this problem, we propose a new interactive training paradigm for ETTS, denoted as i-ETTS, which seeks to directly improve the emotion discriminability by interacting with a speech emotion recognition (SER) model. Moreover, we formulate an iterative training strategy with reinforcement learning to ensure the quality of i-ETTS optimization. Experimental results demonstrate that the proposed i-ETTS outperforms the state-of-the-art baselines by rendering speech with more accurate emotion style. To our best knowledge, this is the first study of reinforcement learning in emotional text-to-speech synthesis.

</details>

### [Attention Forcing for Machine Translation](2104.01264.md)
**Qingyun Dou, Yiting Lu, Potsawee Manakul, Xixin Wu et al.** · 2021-04-02

<details>
<summary>Abstract</summary>

Auto-regressive sequence-to-sequence models with attention mechanisms have achieved state-of-the-art performance in various tasks including Text-To-Speech (TTS) and Neural Machine Translation (NMT). The standard training approach, teacher forcing, guides a model with the reference output history. At inference stage, the generated output history must be used. This mismatch can impact performance. However, it is highly challenging to train the model using the generated output. Several approaches have been proposed to address this problem, normally by selectively using the generated output history. To make training stable, these approaches often require a heuristic schedule or an auxiliary classifier. This paper introduces attention forcing for NMT. This approach guides the model with the generated output history and reference attention, and can reduce the training-inference mismatch without a schedule or a classifier. Attention forcing has been successful in TTS, but its application to NMT is more challenging, due to the discrete and multi-modal nature of the output space. To tackle this problem, this paper adds a selection scheme to vanilla attention forcing, which automatically selects a suitable training approach for each pair of training data. Experiments show that attention forcing can improve the overall translation quality and the diversity of the translations.

</details>

### [SC-GlowTTS: an Efficient Zero-Shot Multi-Speaker Text-To-Speech Model](2104.05557.md)
**Edresson Casanova, Christopher Shulby, Eren Gölge, Nicolas Michael Müller et al.** · 2021-04-02

<details>
<summary>Abstract</summary>

In this paper, we propose SC-GlowTTS: an efficient zero-shot multi-speaker text-to-speech model that improves similarity for speakers unseen during training. We propose a speaker-conditional architecture that explores a flow-based decoder that works in a zero-shot scenario. As text encoders, we explore a dilated residual convolutional-based encoder, gated convolutional-based encoder, and transformer-based encoder. Additionally, we have shown that adjusting a GAN-based vocoder for the spectrograms predicted by the TTS model on the training dataset can significantly improve the similarity and speech quality for new speakers. Our model converges using only 11 speakers, reaching state-of-the-art results for similarity with new speakers, as well as high speech quality.

</details>

### [Assem-VC: Realistic Voice Conversion by Assembling Modern Speech Synthesis Techniques](2104.00931.md)
**Kang-wook Kim, Seung-won Park, Junhyeok Lee, Myun-chul Joe** · 2021-04-02

<details>
<summary>Abstract</summary>

Recent works on voice conversion (VC) focus on preserving the rhythm and the intonation as well as the linguistic content. To preserve these features from the source, we decompose current non-parallel VC systems into two encoders and one decoder. We analyze each module with several experiments and reassemble the best components to propose Assem-VC, a new state-of-the-art any-to-many non-parallel VC system. We also examine that PPG and Cotatron features are speaker-dependent, and attempt to remove speaker identity with adversarial training. Code and audio samples are available at https://github.com/mindslab-ai/assem-vc.

</details>

### [Two Truths and a Lie: Exploring Soft Moderation of COVID-19 Misinformation with Amazon Alexa](2104.04077.md)
**Donald Gover, Filipo Sharevski** · 2021-04-01

<details>
<summary>Abstract</summary>

In this paper, we analyzed the perceived accuracy of COVID-19 vaccine Tweets when they were spoken back by a third-party Amazon Alexa skill. We mimicked the soft moderation that Twitter applies to COVID-19 misinformation content in both forms of warning covers and warning tags to investigate whether the third-party skill could affect how and when users heed these warnings. The results from a 304-participant study suggest that the spoken back warning covers may not work as intended, even when converted from text to speech. We controlled for COVID-19 vaccination hesitancy and political leanings and found that the vaccination hesitant Alexa users ignored any type of warning as long as the Tweets align with their personal beliefs. The politically independent users trusted Alexa less then their politically-laden counterparts and that helped them accurately perceiving truthful COVID-19 information. We discuss soft moderation adaptations for voice assistants to achieve the intended effect of curbing COVID-19 misinformation.

</details>

### [Multi-rate attention architecture for fast streamable Text-to-speech spectrum modeling](2104.00705.md)
**Qing He, Zhiping Xiu, Thilo Koehler, Jilong Wu** · 2021-04-01

<details>
<summary>Abstract</summary>

Typical high quality text-to-speech (TTS) systems today use a two-stage architecture, with a spectrum model stage that generates spectral frames and a vocoder stage that generates the actual audio. High-quality spectrum models usually incorporate the encoder-decoder architecture with self-attention or bi-directional long short-term (BLSTM) units. While these models can produce high quality speech, they often incur O($L$) increase in both latency and real-time factor (RTF) with respect to input length $L$. In other words, longer inputs leads to longer delay and slower synthesis speed, limiting its use in real-time applications. In this paper, we propose a multi-rate attention architecture that breaks the latency and RTF bottlenecks by computing a compact representation during encoding and recurrently generating the attention vector in a streaming manner during decoding. The proposed architecture achieves high audio quality (MOS of 4.31 compared to groundtruth 4.48), low latency, and low RTF at the same time. Meanwhile, both latency and RTF of the proposed system stay constant regardless of input lengths, making it ideal for real-time applications.

</details>

### [Fast DCTTS: Efficient Deep Convolutional Text-to-Speech](2104.00624.md)
**Minsu Kang, Jihyun Lee, Simin Kim, Injung Kim** · 2021-04-01

<details>
<summary>Abstract</summary>

We propose an end-to-end speech synthesizer, Fast DCTTS, that synthesizes speech in real time on a single CPU thread. The proposed model is composed of a carefully-tuned lightweight network designed by applying multiple network reduction and fidelity improvement techniques. In addition, we propose a novel group highway activation that can compromise between computational efficiency and the regularization effect of the gating mechanism. As well, we introduce a new metric called Elastic mel-cepstral distortion (EMCD) to measure the fidelity of the output mel-spectrogram. In experiments, we analyze the effect of the acceleration techniques on speed and speech quality. Compared with the baseline model, the proposed model exhibits improved MOS from 2.62 to 2.74 with only 1.76% computation and 2.75% parameters. The speed on a single CPU thread was improved by 7.45 times, which is fast enough to produce mel-spectrogram in real time without GPU.

</details>

### [Expressive Text-to-Speech using Style Tag](2104.00436.md)
**Minchan Kim, Sung Jun Cheon, Byoung Jin Choi, Jong Jin Kim et al.** · 2021-04-01

<details>
<summary>Abstract</summary>

As recent text-to-speech (TTS) systems have been rapidly improved in speech quality and generation speed, many researchers now focus on a more challenging issue: expressive TTS. To control speaking styles, existing expressive TTS models use categorical style index or reference speech as style input. In this work, we propose StyleTagging-TTS (ST-TTS), a novel expressive TTS model that utilizes a style tag written in natural language. Using a style-tagged TTS dataset and a pre-trained language model, we modeled the relationship between linguistic embedding and speaking style domain, which enables our model to work even with style tags unseen during training. As style tag is written in natural language, it can control speaking style in a more intuitive, interpretable, and scalable way compared with style index or reference speech. In addition, in terms of model architecture, we propose an efficient non-autoregressive (NAR) TTS architecture with single-stage training. The experimental result shows that ST-TTS outperforms the existing expressive TTS model, Tacotron2-GST in speech quality and expressiveness.

</details>

### [Prosody-Enhanced Mandarin Text-to-Speech System](s2:ae699779801e5d895b28be388935ca27a1a904e2.md)
**Fangfang Niu, Wushour Silamu** · 2021-04-01

<details>
<summary>Abstract</summary>

The end-to-end Text-to-Speech (TTS), which can generate speech directly from a given sequence of graphemes or phonemes, has shown superior performance over the conventional TTS. It has been able to generate high-quality speech, but it is still unable to control the local prosody such as word-level emphasis. Although the prominence of synthesized speech can be adjusted by explicit prosody tags, the acquisition of such tags is often time-consuming and laborious. This paper focuses on a deep neural prominence prediction module, using Continuous Wavelet Transform (CWT) to analyze the prosodic signal of input data, get the corresponding continuous prominence values of Chinese characters in the text to guide the training of a prominence prediction network, so that it can realize the mapping from the input text to the corresponding prominence value of each Chinese character in the text. The proposed method does not need to label the training data manually, so a fully automatic prosody control system is realized. Experiments show that the proposed system can generate more natural and expressive speech.

</details>

### [Limited Data Emotional Voice Conversion Leveraging Text-to-Speech: Two-stage Sequence-to-Sequence Training](2103.16809.md)
**Kun Zhou, Berrak Sisman, Haizhou Li** · 2021-03-31

<details>
<summary>Abstract</summary>

Emotional voice conversion (EVC) aims to change the emotional state of an utterance while preserving the linguistic content and speaker identity. In this paper, we propose a novel 2-stage training strategy for sequence-to-sequence emotional voice conversion with a limited amount of emotional speech data. We note that the proposed EVC framework leverages text-to-speech (TTS) as they share a common goal that is to generate high-quality expressive voice. In stage 1, we perform style initialization with a multi-speaker TTS corpus, to disentangle speaking style and linguistic content. In stage 2, we perform emotion training with a limited amount of emotional speech data, to learn how to disentangle emotional style and linguistic information from the speech. The proposed framework can perform both spectrum and prosody conversion and achieves significant improvement over the state-of-the-art baselines in both objective and subjective evaluation.

</details>

### [Parallel Tacotron 2: A Non-Autoregressive Neural TTS Model with Differentiable Duration Modeling](2103.14574.md)
**Isaac Elias, Heiga Zen, Jonathan Shen, Yu Zhang et al.** · 2021-03-26

<details>
<summary>Abstract</summary>

This paper introduces Parallel Tacotron 2, a non-autoregressive neural text-to-speech model with a fully differentiable duration model which does not require supervised duration signals. The duration model is based on a novel attention mechanism and an iterative reconstruction loss based on Soft Dynamic Time Warping, this model can learn token-frame alignments as well as token durations automatically. Experimental results show that Parallel Tacotron 2 outperforms baselines in subjective naturalness in several diverse multi speaker evaluations. Its duration control capability is also demonstrated.

</details>

### [Continual Speaker Adaptation for Text-to-Speech Synthesis](2103.14512.md)
**Hamed Hemati, Damian Borth** · 2021-03-26

<details>
<summary>Abstract</summary>

Training a multi-speaker Text-to-Speech (TTS) model from scratch is computationally expensive and adding new speakers to the dataset requires the model to be re-trained. The naive solution of sequential fine-tuning of a model for new speakers can lead to poor performance of older speakers. This phenomenon is known as catastrophic forgetting. In this paper, we look at TTS modeling from a continual learning perspective, where the goal is to add new speakers without forgetting previous speakers. Therefore, we first propose an experimental setup and show that serial fine-tuning for new speakers can cause the forgetting of the earlier speakers. Then we exploit two well-known techniques for continual learning, namely experience replay and weight regularization. We reveal how one can mitigate the effect of degradation in speech synthesis diversity in sequential training of new speakers using these methods. Finally, we present a simple extension to experience replay to improve the results in extreme setups where we have access to very small buffers.

</details>

### [Improve GAN-based Neural Vocoder using Pointwise Relativistic LeastSquare GAN](2103.14245.md)
**Congyi Wang, Yu Chen, Bin Wang, Yi Shi** · 2021-03-26

<details>
<summary>Abstract</summary>

GAN-based neural vocoders, such as Parallel WaveGAN and MelGAN have attracted great interest due to their lightweight and parallel structures, enabling them to generate high fidelity waveform in a real-time manner. In this paper, inspired by Relativistic GAN, we introduce a novel variant of the LSGAN framework under the context of waveform synthesis, named Pointwise Relativistic LSGAN (PRLSGAN). In this approach, we take the truism score distribution into consideration and combine the original MSE loss with the proposed pointwise relative discrepancy loss to increase the difficulty of the generator to fool the discriminator, leading to improved generation quality. Moreover, PRLSGAN is a general-purposed framework that can be combined with any GAN-based neural vocoder to enhance its generation quality. Experiments have shown a consistent performance boost based on Parallel WaveGAN and MelGAN, demonstrating the effectiveness and strong generalization ability of our proposed PRLSGAN neural vocoders.

</details>

### [SwissDial: Parallel Multidialectal Corpus of Spoken Swiss German](2103.11401.md)
**Pelin Dogan-Schönberger, Julian Mäder, Thomas Hofmann** · 2021-03-21

<details>
<summary>Abstract</summary>

Swiss German is a dialect continuum whose natively acquired dialects significantly differ from the formal variety of the language. These dialects are mostly used for verbal communication and do not have standard orthography. This has led to a lack of annotated datasets, rendering the use of many NLP methods infeasible. In this paper, we introduce the first annotated parallel corpus of spoken Swiss German across 8 major dialects, plus a Standard German reference. Our goal has been to create and to make available a basic dataset for employing data-driven NLP applications in Swiss German. We present our data collection procedure in detail and validate the quality of our corpus by conducting experiments with the recent neural models for speech synthesis.

</details>

### [STYLER: Style Factor Modeling with Rapidity and Robustness via Speech Decomposition for Expressive and Controllable Neural Text to Speech](2103.09474.md)
**Keon Lee, Kyumin Park, Daeyoung Kim** · 2021-03-17

<details>
<summary>Abstract</summary>

Previous works on neural text-to-speech (TTS) have been addressed on limited speed in training and inference time, robustness for difficult synthesis conditions, expressiveness, and controllability. Although several approaches resolve some limitations, there has been no attempt to solve all weaknesses at once. In this paper, we propose STYLER, an expressive and controllable TTS framework with high-speed and robust synthesis. Our novel audio-text aligning method called Mel Calibrator and excluding autoregressive decoding enable rapid training and inference and robust synthesis on unseen data. Also, disentangled style factor modeling under supervision enlarges the controllability in synthesizing process leading to expressive TTS. On top of it, a novel noise modeling pipeline using domain adversarial training and Residual Decoding empowers noise-robust style transfer, decomposing the noise without any additional label. Various experiments demonstrate that STYLER is more effective in speed and robustness than expressive TTS with autoregressive decoding and more expressive and controllable than reading style non-autoregressive TTS. Synthesis samples and experiment results are provided via our demo page, and code is available publicly.

</details>

### [Improving Zero-shot Voice Style Transfer via Disentangled Representation Learning](2103.09420.md)
**Siyang Yuan, Pengyu Cheng, Ruiyi Zhang, Weituo Hao et al.** · 2021-03-17

<details>
<summary>Abstract</summary>

Voice style transfer, also called voice conversion, seeks to modify one speaker's voice to generate speech as if it came from another (target) speaker. Previous works have made progress on voice conversion with parallel training data and pre-known speakers. However, zero-shot voice style transfer, which learns from non-parallel data and generates voices for previously unseen speakers, remains a challenging problem. We propose a novel zero-shot voice transfer method via disentangled representation learning. The proposed method first encodes speaker-related style and voice content of each input voice into separated low-dimensional embedding spaces, and then transfers to a new voice by combining the source content embedding and target style embedding through a decoder. With information-theoretic guidance, the style and content embedding spaces are representative and (ideally) independent of each other. On real-world VCTK datasets, our method outperforms other baselines and obtains state-of-the-art results in terms of transfer accuracy and voice naturalness for voice style transfer experiments under both many-to-many and zero-shot setups.

</details>

### [GAN Vocoder: Multi-Resolution Discriminator Is All You Need](2103.05236.md)
**Jaeseong You, Dalhyun Kim, Gyuhyeon Nam, Geumbyeol Hwang et al.** · 2021-03-09

<details>
<summary>Abstract</summary>

Several of the latest GAN-based vocoders show remarkable achievements, outperforming autoregressive and flow-based competitors in both qualitative and quantitative measures while synthesizing orders of magnitude faster. In this work, we hypothesize that the common factor underlying their success is the multi-resolution discriminating framework, not the minute details in architecture, loss function, or training strategy. We experimentally test the hypothesis by evaluating six different generators paired with one shared multi-resolution discriminating framework. For all evaluative measures with respect to text-to-speech syntheses and for all perceptual metrics, their performances are not distinguishable from one another, which supports our hypothesis.

</details>

### [CUHK-EE Voice Cloning System for ICASSP 2021 M2VoC Challenge](2103.04699.md)
**Daxin Tan, Hingpang Huang, Guangyan Zhang, Tan Lee** · 2021-03-08

<details>
<summary>Abstract</summary>

This paper presents the CUHK-EE voice cloning system for ICASSP 2021 M2VoC challenge. The challenge provides two Mandarin speech corpora: the AIShell-3 corpus of 218 speakers with noise and reverberation and the MST corpus including high-quality speech of one male and one female speakers. 100 and 5 utterances of 3 target speakers in different voice and style are provided in track 1 and 2 respectively, and the participants are required to synthesize speech in target speaker's voice and style. We take part in the track 1 and carry out voice cloning based on 100 utterances of target speakers. An end-to-end voicing cloning system is developed to accomplish the task, which includes: 1. a text and speech front-end module with the help of forced alignment, 2. an acoustic model combining Tacotron2 and DurIAN to predict melspectrogram, 3. a Hifigan vocoder for waveform generation. Our system comprises three stages: multi-speaker training stage, target speaker adaption stage and target speaker synthesis stage. Our team is identified as T17. The subjective evaluation results provided by the challenge organizer demonstrate the effectiveness of our system. Audio samples are available at our demo page: https://daxintan-cuhk.github.io/CUHK-EE-system-M2VoC-challenge/ .

</details>

### [Investigating on Incorporating Pretrained and Learnable Speaker Representations for Multi-Speaker Multi-Style Text-to-Speech](2103.04088.md)
**Chung-Ming Chien, Jheng-Hao Lin, Chien-yu Huang, Po-chun Hsu et al.** · 2021-03-06

<details>
<summary>Abstract</summary>

The few-shot multi-speaker multi-style voice cloning task is to synthesize utterances with voice and speaking style similar to a reference speaker given only a few reference samples. In this work, we investigate different speaker representations and proposed to integrate pretrained and learnable speaker representations. Among different types of embeddings, the embedding pretrained by voice conversion achieves the best performance. The FastSpeech 2 model combined with both pretrained and learnable speaker representations shows great generalization ability on few-shot speakers and achieved 2nd place in the one-shot track of the ICASSP 2021 M2VoC challenge.

</details>

### [Multilingual Byte2Speech Models for Scalable Low-resource Speech Synthesis](2103.03541.md)
**Mutian He, Jingzhou Yang, Lei He, Frank K. Soong** · 2021-03-05

<details>
<summary>Abstract</summary>

To scale neural speech synthesis to various real-world languages, we present a multilingual end-to-end framework that maps byte inputs to spectrograms, thus allowing arbitrary input scripts. Besides strong results on 40+ languages, the framework demonstrates capabilities to adapt to new languages under extreme low-resource and even few-shot scenarios of merely 40s transcribed recording, without the need of per-language resources like lexicon, extra corpus, auxiliary models, or linguistic expertise, thus ensuring scalability. While it retains satisfactory intelligibility and naturalness matching rich-resource models. Exhaustive comparative and ablation studies are performed to reveal the potential of the framework for low-resource languages. Furthermore, we propose a novel method to extract language-specific sub-networks in a multilingual model for a better understanding of its mechanism.

</details>

### [A Neural Text-to-Speech Model Utilizing Broadcast Data Mixed with Background Music](2103.03049.md)
**Hanbin Bae, Jae-Sung Bae, Young-Sun Joo, Young-Ik Kim et al.** · 2021-03-04

<details>
<summary>Abstract</summary>

Recently, it has become easier to obtain speech data from various media such as the internet or YouTube, but directly utilizing them to train a neural text-to-speech (TTS) model is difficult. The proportion of clean speech is insufficient and the remainder includes background music. Even with the global style token (GST). Therefore, we propose the following method to successfully train an end-to-end TTS model with limited broadcast data. First, the background music is removed from the speech by introducing a music filter. Second, the GST-TTS model with an auxiliary quality classifier is trained with the filtered speech and a small amount of clean speech. In particular, the quality classifier makes the embedding vector of the GST layer focus on representing the speech quality (filtered or clean) of the input speech. The experimental results verified that the proposed method synthesized much more high-quality speech than conventional methods.

</details>

### [crank: An Open-Source Software for Nonparallel Voice Conversion Based on Vector-Quantized Variational Autoencoder](2103.02858.md)
**Kazuhiro Kobayashi, Wen-Chin Huang, Yi-Chiao Wu, Patrick Lumban Tobing et al.** · 2021-03-04

<details>
<summary>Abstract</summary>

In this paper, we present an open-source software for developing a nonparallel voice conversion (VC) system named crank. Although we have released an open-source VC software based on the Gaussian mixture model named sprocket in the last VC Challenge, it is not straightforward to apply any speech corpus because it is necessary to prepare parallel utterances of source and target speakers to model a statistical conversion function. To address this issue, in this study, we developed a new open-source VC software that enables users to model the conversion function by using only a nonparallel speech corpus. For implementing the VC software, we used a vector-quantized variational autoencoder (VQVAE). To rapidly examine the effectiveness of recent technologies developed in this research field, crank also supports several representative works for autoencoder-based VC methods such as the use of hierarchical architectures, cyclic architectures, generative adversarial networks, speaker adversarial training, and neural vocoders. Moreover, it is possible to automatically estimate objective measures such as mel-cepstrum distortion and pseudo mean opinion score based on MOSNet. In this paper, we describe representative functions developed in crank and make brief comparisons by objective evaluations.

</details>

### [AdaSpeech: Adaptive Text to Speech for Custom Voice](2103.00993.md)
**Mingjian Chen, Xu Tan, Bohan Li, Yanqing Liu et al.** · 2021-03-01

<details>
<summary>Abstract</summary>

Custom voice, a specific text to speech (TTS) service in commercial speech platforms, aims to adapt a source TTS model to synthesize personal voice for a target speaker using few speech data. Custom voice presents two unique challenges for TTS adaptation: 1) to support diverse customers, the adaptation model needs to handle diverse acoustic conditions that could be very different from source speech data, and 2) to support a large number of customers, the adaptation parameters need to be small enough for each target speaker to reduce memory usage while maintaining high voice quality. In this work, we propose AdaSpeech, an adaptive TTS system for high-quality and efficient customization of new voices. We design several techniques in AdaSpeech to address the two challenges in custom voice: 1) To handle different acoustic conditions, we use two acoustic encoders to extract an utterance-level vector and a sequence of phoneme-level vectors from the target speech during training; in inference, we extract the utterance-level vector from a reference speech and use an acoustic predictor to predict the phoneme-level vectors. 2) To better trade off the adaptation parameters and voice quality, we introduce conditional layer normalization in the mel-spectrogram decoder of AdaSpeech, and fine-tune this part in addition to speaker embedding for adaptation. We pre-train the source TTS model on LibriTTS datasets and fine-tune it on VCTK and LJSpeech datasets (with different acoustic conditions from LibriTTS) with few adaptation data, e.g., 20 sentences, about 1 minute speech. Experiment results show that AdaSpeech achieves much better adaptation quality than baseline methods, with only about 5K specific parameters for each speaker, which demonstrates its effectiveness for custom voice. Audio samples are available at https://speechresearch.github.io/adaspeech/.

</details>

### [End-to-End Korean Speech Synthesis System Using Reformer Network](s2:ce8eca7c1a0efabe1eb0685e31eefc1b338d3cdc.md)
**H. Ihm, Sung Jun Cheon, Byoung Jin Choi, Min Chan Kim et al.** · 2021-02-28

### [MaskCycleGAN-VC: Learning Non-parallel Voice Conversion with Filling in Frames](2102.12841.md)
**Takuhiro Kaneko, Hirokazu Kameoka, Kou Tanaka, Nobukatsu Hojo** · 2021-02-25

<details>
<summary>Abstract</summary>

Non-parallel voice conversion (VC) is a technique for training voice converters without a parallel corpus. Cycle-consistent adversarial network-based VCs (CycleGAN-VC and CycleGAN-VC2) are widely accepted as benchmark methods. However, owing to their insufficient ability to grasp time-frequency structures, their application is limited to mel-cepstrum conversion and not mel-spectrogram conversion despite recent advances in mel-spectrogram vocoders. To overcome this, CycleGAN-VC3, an improved variant of CycleGAN-VC2 that incorporates an additional module called time-frequency adaptive normalization (TFAN), has been proposed. However, an increase in the number of learned parameters is imposed. As an alternative, we propose MaskCycleGAN-VC, which is another extension of CycleGAN-VC2 and is trained using a novel auxiliary task called filling in frames (FIF). With FIF, we apply a temporal mask to the input mel-spectrogram and encourage the converter to fill in missing frames based on surrounding frames. This task allows the converter to learn time-frequency structures in a self-supervised manner and eliminates the need for an additional module such as TFAN. A subjective evaluation of the naturalness and speaker similarity showed that MaskCycleGAN-VC outperformed both CycleGAN-VC2 and CycleGAN-VC3 with a model size similar to that of CycleGAN-VC2. Audio samples are available at http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/maskcyclegan-vc/index.html.

</details>

### [Handling Background Noise in Neural Speech Generation](2102.11906.md)
**Tom Denton, Alejandro Luebs, Felicia S. C. Lim, Andrew Storus et al.** · 2021-02-23

<details>
<summary>Abstract</summary>

Recent advances in neural-network based generative modeling of speech has shown great potential for speech coding. However, the performance of such models drops when the input is not clean speech, e.g., in the presence of background noise, preventing its use in practical applications. In this paper we examine the reason and discuss methods to overcome this issue. Placing a denoising preprocessing stage when extracting features and target clean speech during training is shown to be the best performing strategy.

</details>

### [Investigating Deep Neural Structures and their Interpretability in the Domain of Voice Conversion](2102.11420.md)
**Samuel J. Broughton, Md Asif Jalal, Roger K. Moore** · 2021-02-22

<details>
<summary>Abstract</summary>

Generative Adversarial Networks (GANs) are machine learning networks based around creating synthetic data. Voice Conversion (VC) is a subset of voice translation that involves translating the paralinguistic features of a source speaker to a target speaker while preserving the linguistic information. The aim of non-parallel conditional GANs for VC is to translate an acoustic speech feature sequence from one domain to another without the use of paired data. In the study reported here, we investigated the interpretability of state-of-the-art implementations of non-parallel GANs in the domain of VC. We show that the learned representations in the repeating layers of a particular GAN architecture remain close to their original random initialised parameters, demonstrating that it is the number of repeating layers that is more responsible for the quality of the output. We also analysed the learned representations of a model trained on one particular dataset when used during transfer learning on another dataset. This showed extremely high levels of similarity across the entire network. Together, these results provide new insight into how the learned representations of deep generative networks change during learning and the importance in the number of layers.

</details>

### [Model architectures to extrapolate emotional expressions in DNN-based text-to-speech](2102.10345.md)
**Katsuki Inoue, Sunao Hara, Masanobu Abe, Nobukatsu Hojo et al.** · 2021-02-20

<details>
<summary>Abstract</summary>

This paper proposes architectures that facilitate the extrapolation of emotional expressions in deep neural network (DNN)-based text-to-speech (TTS). In this study, the meaning of "extrapolate emotional expressions" is to borrow emotional expressions from others, and the collection of emotional speech uttered by target speakers is unnecessary. Although a DNN has potential power to construct DNN-based TTS with emotional expressions and some DNN-based TTS systems have demonstrated satisfactory performances in the expression of the diversity of human speech, it is necessary and troublesome to collect emotional speech uttered by target speakers. To solve this issue, we propose architectures to separately train the speaker feature and the emotional feature and to synthesize speech with any combined quality of speakers and emotions. The architectures are parallel model (PM), serial model (SM), auxiliary input model (AIM), and hybrid models (PM&AIM and SM&AIM). These models are trained through emotional speech uttered by few speakers and neutral speech uttered by many speakers. Objective evaluations demonstrate that the performances in the open-emotion test provide insufficient information. They make a comparison with those in the closed-emotion test, but each speaker has their own manner of expressing emotion. However, subjective evaluation results indicate that the proposed models could convey emotional information to some extent. Notably, the PM can correctly convey sad and joyful emotions at a rate of >60%.

</details>

### [WARP-Q: Quality Prediction For Generative Neural Speech Codecs](2102.10449.md)
**Wissam A. Jassim, Jan Skoglund, Michael Chinen, Andrew Hines** · 2021-02-20

<details>
<summary>Abstract</summary>

Good speech quality has been achieved using waveform matching and parametric reconstruction coders. Recently developed very low bit rate generative codecs can reconstruct high quality wideband speech with bit streams less than 3 kb/s. These codecs use a DNN with parametric input to synthesise high quality speech outputs. Existing objective speech quality models (e.g., POLQA, ViSQOL) do not accurately predict the quality of coded speech from these generative models underestimating quality due to signal differences not highlighted in subjective listening tests. We present WARP-Q, a full-reference objective speech quality metric that uses dynamic time warping cost for MFCC speech representations. It is robust to small perceptual signal changes. Evaluation using waveform matching, parametric and generative neural vocoder based codecs as well as channel and environmental noise shows that WARP-Q has better correlation and codec quality ranking for novel codecs compared to traditional metrics in addition to versatility for general quality assessment scenarios.

</details>

### [Alternate Endings: Improving Prosody for Incremental Neural TTS with Predicted Future Text Input](2102.09914.md)
**Brooke Stephenson, Thomas Hueber, Laurent Girin, Laurent Besacier** · 2021-02-19

<details>
<summary>Abstract</summary>

The prosody of a spoken word is determined by its surrounding context. In incremental text-to-speech synthesis, where the synthesizer produces an output before it has access to the complete input, the full context is often unknown which can result in a loss of naturalness in the synthesized speech. In this paper, we investigate whether the use of predicted future text can attenuate this loss. We compare several test conditions of next future word: (a) unknown (zero-word), (b) language model predicted, (c) randomly predicted and (d) ground-truth. We measure the prosodic features (pitch, energy and duration) and find that predicted text provides significant improvements over a zero-word lookahead, but only slight gains over random-word lookahead. We confirm these results with a perceptive test.

</details>

### [AudioVisual Speech Synthesis: A brief literature review](2103.03927.md)
**Efthymios Georgiou, Athanasios Katsamanis** · 2021-02-18

<details>
<summary>Abstract</summary>

This brief literature review studies the problem of audiovisual speech synthesis, which is the problem of generating an animated talking head given a text as input. Due to the high complexity of this problem, we approach it as the composition of two problems. Specifically, that of Text-to-Speech (TTS) synthesis as well as the voice-driven talking head animation. For TTS, we present models that are used to map text to intermediate acoustic representations, e.g. mel-spectrograms, as well as models that generate voice signals conditioned on these intermediate representations, i.e vocoders. For the talking-head animation problem, we categorize approaches based on whether they produce human faces or anthropomorphic figures. An attempt is also made to discuss the importance of the choice of facial models in the second case. Throughout the review, we briefly describe the most important work in audiovisual speech synthesis, trying to highlight the advantages and disadvantages of the various approaches.

</details>

### [Context-Aware Prosody Correction for Text-Based Speech Editing](2102.08328.md)
**Max Morrison, Lucas Rencker, Zeyu Jin, Nicholas J. Bryan et al.** · 2021-02-16

<details>
<summary>Abstract</summary>

Text-based speech editors expedite the process of editing speech recordings by permitting editing via intuitive cut, copy, and paste operations on a speech transcript. A major drawback of current systems, however, is that edited recordings often sound unnatural because of prosody mismatches around edited regions. In our work, we propose a new context-aware method for more natural sounding text-based editing of speech. To do so, we 1) use a series of neural networks to generate salient prosody features that are dependent on the prosody of speech surrounding the edit and amenable to fine-grained user control 2) use the generated features to control a standard pitch-shift and time-stretch method and 3) apply a denoising neural network to remove artifacts induced by the signal manipulation to yield a high-fidelity result. We evaluate our approach using a subjective listening test, provide a detailed comparative analysis, and conclude several interesting insights.

</details>

### [Axial Residual Networks for CycleGAN-based Voice Conversion](2102.08075.md)
**Jaeseong You, Gyuhyeon Nam, Dalhyun Kim, Gyeongsu Chae** · 2021-02-16

<details>
<summary>Abstract</summary>

We propose a novel architecture and improved training objectives for non-parallel voice conversion. Our proposed CycleGAN-based model performs a shape-preserving transformation directly on a high frequency-resolution magnitude spectrogram, converting its style (i.e. speaker identity) while preserving the speech content. Throughout the entire conversion process, the model does not resort to compressed intermediate representations of any sort (e.g. mel spectrogram, low resolution spectrogram, decomposed network feature). We propose an efficient axial residual block architecture to support this expensive procedure and various modifications to the CycleGAN losses to stabilize the training process. We demonstrate via experiments that our proposed model outperforms Scyclone and shows a comparable or better performance to that of CycleGAN-VC2 even without employing a neural vocoder.

</details>

### [VARA-TTS: Non-Autoregressive Text-to-Speech Synthesis based on Very Deep VAE with Residual Attention](2102.06431.md)
**Peng Liu, Yuewen Cao, Songxiang Liu, Na Hu et al.** · 2021-02-12

<details>
<summary>Abstract</summary>

This paper proposes VARA-TTS, a non-autoregressive (non-AR) text-to-speech (TTS) model using a very deep Variational Autoencoder (VDVAE) with Residual Attention mechanism, which refines the textual-to-acoustic alignment layer-wisely. Hierarchical latent variables with different temporal resolutions from the VDVAE are used as queries for residual attention module. By leveraging the coarse global alignment from previous attention layer as an extra input, the following attention layer can produce a refined version of alignment. This amortizes the burden of learning the textual-to-acoustic alignment among multiple attention layers and outperforms the use of only a single attention layer in robustness. An utterance-level speaking speed factor is computed by a jointly-trained speaking speed predictor, which takes the mean-pooled latent variables of the coarsest layer as input, to determine number of acoustic frames at inference. Experimental results show that VARA-TTS achieves slightly inferior speech quality to an AR counterpart Tacotron 2 but an order-of-magnitude speed-up at inference; and outperforms an analogous non-AR model, BVAE-TTS, in terms of speech quality.

</details>

### [Voice Cloning: a Multi-Speaker Text-to-Speech Synthesis Approach based on Transfer Learning](2102.05630.md)
**Giuseppe Ruggiero, Enrico Zovato, Luigi Di Caro, Vincent Pollet** · 2021-02-10

<details>
<summary>Abstract</summary>

Deep learning models are becoming predominant in many fields of machine learning. Text-to-Speech (TTS), the process of synthesizing artificial speech from text, is no exception. To this end, a deep neural network is usually trained using a corpus of several hours of recorded speech from a single speaker. Trying to produce the voice of a speaker other than the one learned is expensive and requires large effort since it is necessary to record a new dataset and retrain the model. This is the main reason why the TTS models are usually single speaker. The proposed approach has the goal to overcome these limitations trying to obtain a system which is able to model a multi-speaker acoustic space. This allows the generation of speech audio similar to the voice of different target speakers, even if they were not observed during the training phase.

</details>

### [CDPAM: Contrastive learning for perceptual audio similarity](2102.05109.md)
**Pranay Manocha, Zeyu Jin, Richard Zhang, Adam Finkelstein** · 2021-02-09

<details>
<summary>Abstract</summary>

Many speech processing methods based on deep learning require an automatic and differentiable audio metric for the loss function. The DPAM approach of Manocha et al. learns a full-reference metric trained directly on human judgments, and thus correlates well with human perception. However, it requires a large number of human annotations and does not generalize well outside the range of perturbations on which it was trained. This paper introduces CDPAM, a metric that builds on and advances DPAM. The primary improvement is to combine contrastive learning and multi-dimensional representations to build robust models from limited data. In addition, we collect human judgments on triplet comparisons to improve generalization to a broader range of audio perturbations. CDPAM correlates well with human responses across nine varied datasets. We also show that adding this metric to existing speech synthesis and enhancement methods yields significant improvement, as measured by objective and subjective tests.

</details>

### [LightSpeech: Lightweight and Fast Text to Speech with Neural Architecture Search](2102.04040.md)
**Renqian Luo, Xu Tan, Rui Wang, Tao Qin et al.** · 2021-02-08

<details>
<summary>Abstract</summary>

Text to speech (TTS) has been broadly used to synthesize natural and intelligible speech in different scenarios. Deploying TTS in various end devices such as mobile phones or embedded devices requires extremely small memory usage and inference latency. While non-autoregressive TTS models such as FastSpeech have achieved significantly faster inference speed than autoregressive models, their model size and inference latency are still large for the deployment in resource constrained devices. In this paper, we propose LightSpeech, which leverages neural architecture search~(NAS) to automatically design more lightweight and efficient models based on FastSpeech. We first profile the components of current FastSpeech model and carefully design a novel search space containing various lightweight and potentially effective architectures. Then NAS is utilized to automatically discover well performing architectures within the search space. Experiments show that the model discovered by our method achieves 15x model compression ratio and 6.5x inference speedup on CPU with on par voice quality. Audio demos are provided at https://speechresearch.github.io/lightspeech.

</details>

### [Prosody prediction for arabic via the open-source boundary-annotated qur’an corpus](s2:6e6fcfae782b4bbb53f396ca2d7902bc18a4c1ca.md)
**M. Sawalha, C. Brierley, E. Atwell** · 2021-02-04

<details>
<summary>Abstract</summary>

A phrase break classifier is needed to predict natural prosodic pauses in text to be read out loud by humans or machines. To develop phrase break classifiers, we need a boundary-annotated and part-of-speech tagged corpus. Boundary annotations in English speech corpora are descriptive, delimiting intonation units perceived by the listener; manual annotation must be done by an expert linguist. For Arabic, there are no existing suitable resources. We take a novel approach to phrase break prediction for Arabic, deriving our prosodic annotation scheme from Tajwid (recitation) mark-up in the Qur’an which we then interpret as additional text-based data for computational analysis. This mark-up is prescriptive, and signifies a widely-used recitation style, and one of seven original styles of transmission. Here we report on version 1.0 of our Boundary-Annotated Qur’an dataset of 77430 words and 8230 sentences, where each word is tagged with prosodic and syntactic information at two coarse-grained levels. We then use this dataset to train, test, and compare two probabilistic taggers (trigram and HMM) for Arabic phrase break prediction, where the task is to predict boundary locations in an unseen test set stripped of boundary annotations by classifying words as breaks or non-breaks. The preponderance of non-breaks in the training data sets a challenging baseline success rate: 85.56%. However, we achieve significant gains in accuracy with a trigram tagger, and significant gains in performance recognition of minority class instances with both taggers via the Balanced Classification Rate metric. This is initial work on a long-term research project to produce annotation schemes, language resources, algorithms, and applications for Classical and Modern Standard Arabic.

</details>

### [Towards Natural and Controllable Cross-Lingual Voice Conversion Based on Neural TTS Model and Phonetic Posteriorgram](2102.01991.md)
**Shengkui Zhao, Hao Wang, Trung Hieu Nguyen, Bin Ma** · 2021-02-03

<details>
<summary>Abstract</summary>

Cross-lingual voice conversion (VC) is an important and challenging problem due to significant mismatches of the phonetic set and the speech prosody of different languages. In this paper, we build upon the neural text-to-speech (TTS) model, i.e., FastSpeech, and LPCNet neural vocoder to design a new cross-lingual VC framework named FastSpeech-VC. We address the mismatches of the phonetic set and the speech prosody by applying Phonetic PosteriorGrams (PPGs), which have been proved to bridge across speaker and language boundaries. Moreover, we add normalized logarithm-scale fundamental frequency (Log-F0) to further compensate for the prosodic mismatches and significantly improve naturalness. Our experiments on English and Mandarin languages demonstrate that with only mono-lingual corpus, the proposed FastSpeech-VC can achieve high quality converted speech with mean opinion score (MOS) close to the professional records while maintaining good speaker similarity. Compared to the baselines using Tacotron2 and Transformer TTS models, the FastSpeech-VC can achieve controllable converted speech rate and much faster inference speed. More importantly, the FastSpeech-VC can easily be adapted to a speaker with limited training utterances.

</details>

### [Universal Neural Vocoding with Parallel WaveNet](2102.01106.md)
**Yunlong Jiao, Adam Gabrys, Georgi Tinchev, Bartosz Putrycz et al.** · 2021-02-01

<details>
<summary>Abstract</summary>

We present a universal neural vocoder based on Parallel WaveNet, with an additional conditioning network called Audio Encoder. Our universal vocoder offers real-time high-quality speech synthesis on a wide range of use cases. We tested it on 43 internal speakers of diverse age and gender, speaking 20 languages in 17 unique styles, of which 7 voices and 5 styles were not exposed during training. We show that the proposed universal vocoder significantly outperforms speaker-dependent vocoders overall. We also show that the proposed vocoder outperforms several existing neural vocoder architectures in terms of naturalness and universality. These findings are consistent when we further test on more than 300 open-source voices.

</details>

### [High Fidelity Speech Regeneration with Application to Speech Enhancement](2102.00429.md)
**Adam Polyak, Lior Wolf, Yossi Adi, Ori Kabeli et al.** · 2021-01-31

<details>
<summary>Abstract</summary>

Speech enhancement has seen great improvement in recent years mainly through contributions in denoising, speaker separation, and dereverberation methods that mostly deal with environmental effects on vocal audio. To enhance speech beyond the limitations of the original signal, we take a regeneration approach, in which we recreate the speech from its essence, including the semi-recognized speech, prosody features, and identity. We propose a wav-to-wav generative model for speech that can generate 24khz speech in a real-time manner and which utilizes a compact speech representation, composed of ASR and identity features, to achieve a higher level of intelligibility. Inspired by voice conversion methods, we train to augment the speech characteristics while preserving the identity of the source using an auxiliary identity network. Perceptual acoustic metrics and subjective tests show that the method obtains valuable improvements over recent baselines.

</details>

### [Triple M: A Practical Text-to-speech Synthesis System With Multi-guidance Attention And Multi-band Multi-time LPCNet](2102.00247.md)
**Shilun Lin, Fenglong Xie, Li Meng, Xinhui Li et al.** · 2021-01-30

<details>
<summary>Abstract</summary>

In this work, a robust and efficient text-to-speech (TTS) synthesis system named Triple M is proposed for large-scale online application. The key components of Triple M are: 1) A sequence-to-sequence model adopts a novel multi-guidance attention to transfer complementary advantages from guiding attention mechanisms to the basic attention mechanism without in-domain performance loss and online service modification. Compared with single attention mechanism, multi-guidance attention not only brings better naturalness to long sentence synthesis, but also reduces the word error rate by 26.8%. 2) A new efficient multi-band multi-time vocoder framework, which reduces the computational complexity from 2.8 to 1.0 GFLOP and speeds up LPCNet by 2.75x on a single CPU.

</details>

### [Expressive Neural Voice Cloning](2102.00151.md)
**Paarth Neekhara, Shehzeen Hussain, Shlomo Dubnov, Farinaz Koushanfar et al.** · 2021-01-30

<details>
<summary>Abstract</summary>

Voice cloning is the task of learning to synthesize the voice of an unseen speaker from a few samples. While current voice cloning methods achieve promising results in Text-to-Speech (TTS) synthesis for a new voice, these approaches lack the ability to control the expressiveness of synthesized audio. In this work, we propose a controllable voice cloning method that allows fine-grained control over various style aspects of the synthesized speech for an unseen speaker. We achieve this by explicitly conditioning the speech synthesis model on a speaker encoding, pitch contour and latent style tokens during training. Through both quantitative and qualitative evaluations, we show that our framework can be used for various expressive voice cloning tasks using only a few transcribed or untranscribed speech samples for a new speaker. These cloning tasks include style transfer from a reference speech, synthesizing speech directly from text, and fine-grained style control by manipulating the style conditioning variables during inference.

</details>

### [Adversarially learning disentangled speech representations for robust multi-factor voice conversion](2102.00184.md)
**Jie Wang, Jingbei Li, Xintao Zhao, Zhiyong Wu et al.** · 2021-01-30

<details>
<summary>Abstract</summary>

Factorizing speech as disentangled speech representations is vital to achieve highly controllable style transfer in voice conversion (VC). Conventional speech representation learning methods in VC only factorize speech as speaker and content, lacking controllability on other prosody-related factors. State-of-the-art speech representation learning methods for more speechfactors are using primary disentangle algorithms such as random resampling and ad-hoc bottleneck layer size adjustment,which however is hard to ensure robust speech representationdisentanglement. To increase the robustness of highly controllable style transfer on multiple factors in VC, we propose a disentangled speech representation learning framework based on adversarial learning. Four speech representations characterizing content, timbre, rhythm and pitch are extracted, and further disentangled by an adversarial Mask-And-Predict (MAP)network inspired by BERT. The adversarial network is used tominimize the correlations between the speech representations,by randomly masking and predicting one of the representationsfrom the others. Experimental results show that the proposedframework significantly improves the robustness of VC on multiple factors by increasing the speech quality MOS from 2.79 to3.30 and decreasing the MCD from 3.89 to 3.58.

</details>

### [A causal convolutional neural network for multi-subject motion modeling and generation](2101.12276.md)
**Shuaiying Hou, Congyi Wang, Wenlin Zhuang, Yu Chen et al.** · 2021-01-28

<details>
<summary>Abstract</summary>

Inspired by the success of WaveNet in multi-subject speech synthesis, we propose a novel neural network based on causal convolutions for multi-subject motion modeling and generation. The network can capture the intrinsic characteristics of the motion of different subjects, such as the influence of skeleton scale variation on motion style. Moreover, after fine-tuning the network using a small motion dataset for a novel skeleton that is not included in the training dataset, it is able to synthesize high-quality motions with a personalized style for the novel skeleton. The experimental results demonstrate that our network can model the intrinsic characteristics of motions well and can be applied to various motion modeling and synthesis tasks.

</details>

### [High-Quality Vocoding Design with Signal Processing for Speech Synthesis and Voice Conversion](2101.10278.md)
**Mohammed Salah Al-Radhi** · 2021-01-25

<details>
<summary>Abstract</summary>

This Ph.D. thesis focuses on developing a system for high-quality speech synthesis and voice conversion. Vocoder-based speech analysis, manipulation, and synthesis plays a crucial role in various kinds of statistical parametric speech research. Although there are vocoding methods which yield close to natural synthesized speech, they are typically computationally expensive, and are thus not suitable for real-time implementation, especially in embedded environments. Therefore, there is a need for simple and computationally feasible digital signal processing algorithms for generating high-quality and natural-sounding synthesized speech. In this dissertation, I propose a solution to extract optimal acoustic features and a new waveform generator to achieve higher sound quality and conversion accuracy by applying advances in deep learning. The approach remains computationally efficient. This challenge resulted in five thesis groups, which are briefly summarized below.

</details>

### [Supervised and Unsupervised Approaches for Controlling Narrow Lexical Focus in Sequence-to-Sequence Speech Synthesis](2101.09940.md)
**Slava Shechtman, Raul Fernandez, David Haws** · 2021-01-25

<details>
<summary>Abstract</summary>

Although Sequence-to-Sequence (S2S) architectures have become state-of-the-art in speech synthesis, capable of generating outputs that approach the perceptual quality of natural samples, they are limited by a lack of flexibility when it comes to controlling the output. In this work we present a framework capable of controlling the prosodic output via a set of concise, interpretable, disentangled parameters. We apply this framework to the realization of emphatic lexical focus, proposing a variety of architectures designed to exploit different levels of supervision based on the availability of labeled resources. We evaluate these approaches via listening tests that demonstrate we are able to successfully realize controllable focus while maintaining the same, or higher, naturalness over an established baseline, and we explore how the different approaches compare when synthesizing in a target voice with or without labeled data.

</details>

### [End-to-End Speech Synthesis for Tibetan Multidialect](s2:a8f35fb70834af6063b242211317707f06a13d70.md)
**Xiaona Xu, Li Yang, Yue Zhao, Hui Wang** · 2021-01-25

<details>
<summary>Abstract</summary>

The research on Tibetan speech synthesis technology has been mainly focusing on single dialect, and thus there is a lack of research on Tibetan multidialect speech synthesis technology. This paper presents an end-to-end Tibetan multidialect speech synthesis model to realize a speech synthesis system which can be used to synthesize different Tibetan dialects. Firstly, Wylie transliteration scheme is used to convert the Tibetan text into the corresponding Latin letters, which effectively reduces the size of training corpus and the workload of front-end text processing. Secondly, a shared feature prediction network with a cyclic sequence-to-sequence structure is built, which maps the Latin transliteration vector of Tibetan character to Mel spectrograms and learns the relevant features of multidialect speech data. Thirdly, two dialect-specific WaveNet vocoders are combined with the feature prediction network, which synthesizes the Mel spectrum of Lhasa-Ü-Tsang and Amdo pastoral dialect into time-domain waveform, respectively. The model avoids using a large number of Tibetan dialect expertise for processing some time-consuming tasks, such as phonetic analysis and phonological annotation. Additionally, it can directly synthesize Lhasa-Ü-Tsang and Amdo pastoral speech on the existing text annotation. The experimental results show that the synthesized speech of Lhasa-Ü-Tsang and Amdo pastoral dialect based on our proposed method has better clarity and naturalness than the Tibetan monolingual model.

</details>

### [Improved parallel WaveGAN vocoder with perceptually weighted spectrogram loss](2101.07412.md)
**Eunwoo Song, Ryuichi Yamamoto, Min-Jae Hwang, Jin-Seob Kim et al.** · 2021-01-19

<details>
<summary>Abstract</summary>

This paper proposes a spectral-domain perceptual weighting technique for Parallel WaveGAN-based text-to-speech (TTS) systems. The recently proposed Parallel WaveGAN vocoder successfully generates waveform sequences using a fast non-autoregressive WaveNet model. By employing multi-resolution short-time Fourier transform (MR-STFT) criteria with a generative adversarial network, the light-weight convolutional networks can be effectively trained without any distillation process. To further improve the vocoding performance, we propose the application of frequency-dependent weighting to the MR-STFT loss function. The proposed method penalizes perceptually-sensitive errors in the frequency domain; thus, the model is optimized toward reducing auditory noise in the synthesized speech. Subjective listening test results demonstrate that our proposed method achieves 4.21 and 4.26 TTS mean opinion scores for female and male Korean speakers, respectively.

</details>

### [Hierarchical disentangled representation learning for singing voice conversion](2101.06842.md)
**Naoya Takahashi, Mayank Kumar Singh, Yuki Mitsufuji** · 2021-01-18

<details>
<summary>Abstract</summary>

Conventional singing voice conversion (SVC) methods often suffer from operating in high-resolution audio owing to a high dimensionality of data. In this paper, we propose a hierarchical representation learning that enables the learning of disentangled representations with multiple resolutions independently. With the learned disentangled representations, the proposed method progressively performs SVC from low to high resolutions. Experimental results show that the proposed method outperforms baselines that operate with a single resolution in terms of mean opinion score (MOS), similarity score, and pitch accuracy.

</details>

### [EmoCat: Language-agnostic Emotional Voice Conversion](2101.05695.md)
**Bastian Schnell, Goeric Huybrechts, Bartek Perz, Thomas Drugman et al.** · 2021-01-14

<details>
<summary>Abstract</summary>

Emotional voice conversion models adapt the emotion in speech without changing the speaker identity or linguistic content. They are less data hungry than text-to-speech models and allow to generate large amounts of emotional data for downstream tasks. In this work we propose EmoCat, a language-agnostic emotional voice conversion model. It achieves high-quality emotion conversion in German with less than 45 minutes of German emotional recordings by exploiting large amounts of emotional data in US English. EmoCat is an encoder-decoder model based on CopyCat, a voice conversion system which transfers prosody. We use adversarial training to remove emotion leakage from the encoder to the decoder. The adversarial training is improved by a novel contribution to gradient reversal to truly reverse gradients. This allows to remove only the leaking information and to converge to better optima with higher conversion performance. Evaluations show that Emocat can convert to different emotions but misses on emotion intensity compared to the recordings, especially for very expressive emotions. EmoCat is able to achieve audio quality on par with the recordings for five out of six tested emotion intensities.

</details>

### [Generating coherent spontaneous speech and gesture from text](2101.05684.md)
**Simon Alexanderson, Éva Székely, Gustav Eje Henter, Taras Kucherenko et al.** · 2021-01-14

<details>
<summary>Abstract</summary>

Embodied human communication encompasses both verbal (speech) and non-verbal information (e.g., gesture and head movements). Recent advances in machine learning have substantially improved the technologies for generating synthetic versions of both of these types of data: On the speech side, text-to-speech systems are now able to generate highly convincing, spontaneous-sounding speech using unscripted speech audio as the source material. On the motion side, probabilistic motion-generation methods can now synthesise vivid and lifelike speech-driven 3D gesticulation. In this paper, we put these two state-of-the-art technologies together in a coherent fashion for the first time. Concretely, we demonstrate a proof-of-concept system trained on a single-speaker audio and motion-capture dataset, that is able to generate both speech and full-body gestures together from text input. In contrast to previous approaches for joint speech-and-gesture generation, we generate full-body gestures from speech synthesis trained on recordings of spontaneous speech from the same person as the motion-capture data. We illustrate our results by visualising gesture spaces and text-speech-gesture alignments, and through a demonstration video at https://simonalexanderson.github.io/IVA2020 .

</details>

### [Controllable cross-speaker emotion transfer for end-to-end speech synthesis](s2:d3d8821c31488c33193d15ee500abe09e22c5baa.md)
**Tao Li, Xinsheng Wang, Qicong Xie, Zhichao Wang et al.** · 2021-01-01

### [A Review of End-to-End Chinese – Mandarin Speech Synthesis Techniques](s2:80837b4c34b2d4cafaf2a041e82774fe27250ebc.md)
**Wenzhuo Gong, Yang Hong, Hancheng Liu, Yutong He** · 2021-01-01

### [Lexical pitch accent and duration modeling for neural end-to-end text-to-speech synthesis](s2:19d7a3f0b0dc1105fa79620a184e2602256c3be3.md)
**Yusuke Yasuda** · 2021-01-01

