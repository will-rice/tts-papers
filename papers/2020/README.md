# 2020

262 papers in this year.

### [Unified Mandarin TTS Front-end Based on Distilled BERT Model](2012.15404.md)
**Yang Zhang, Liqun Deng, Yasheng Wang** · 2020-12-31

<details>
<summary>Abstract</summary>

The front-end module in a typical Mandarin text-to-speech system (TTS) is composed of a long pipeline of text processing components, which requires extensive efforts to build and is prone to large accumulative model size and cascade errors. In this paper, a pre-trained language model (PLM) based model is proposed to simultaneously tackle the two most important tasks in TTS front-end, i.e., prosodic structure prediction (PSP) and grapheme-to-phoneme (G2P) conversion. We use a pre-trained Chinese BERT[1] as the text encoder and employ multi-task learning technique to adapt it to the two TTS front-end tasks. Then, the BERT encoder is distilled into a smaller model by employing a knowledge distillation technique called TinyBERT[2], making the whole model size 25% of that of benchmark pipeline models while maintaining competitive performance on both tasks. With the proposed the methods, we are able to run the whole TTS front-end module in a light and unified manner, which is more friendly to deployment on mobile devices.

</details>

### [EfficientNet-Absolute Zero for Continuous Speech Keyword Spotting](2012.15695.md)
**Amir Mohammad Rostami, Ali Karimi, Mohammad Ali Akhaee** · 2020-12-31

<details>
<summary>Abstract</summary>

Keyword spotting is a process of finding some specific words or phrases in recorded speeches by computers. Deep neural network algorithms, as a powerful engine, can handle this problem if they are trained over an appropriate dataset. To this end, the football keyword dataset (FKD), as a new keyword spotting dataset in Persian, is collected with crowdsourcing. This dataset contains nearly 31000 samples in 18 classes. The continuous speech synthesis method proposed to made FKD usable in the practical application which works with continuous speeches. Besides, we proposed a lightweight architecture called EfficientNet-A0 (absolute zero) by applying the compound scaling method on EfficientNet-B0 for keyword spotting task. Finally, the proposed architecture is evaluated with various models. It is realized that EfficientNet-A0 and Resnet models outperform other models on this dataset.

</details>

### [Text-Free Image-to-Speech Synthesis Using Learned Segmental Units](2012.15454.md)
**Wei-Ning Hsu, David Harwath, Christopher Song, James Glass** · 2020-12-31

<details>
<summary>Abstract</summary>

In this paper we present the first model for directly synthesizing fluent, natural-sounding spoken audio captions for images that does not require natural language text as an intermediate representation or source of supervision. Instead, we connect the image captioning module and the speech synthesis module with a set of discrete, sub-word speech units that are discovered with a self-supervised visual grounding task. We conduct experiments on the Flickr8k spoken caption dataset in addition to a novel corpus of spoken audio captions collected for the popular MSCOCO dataset, demonstrating that our generated captions also capture diverse visual semantics of the images they describe. We investigate several different intermediate speech representations, and empirically find that the representation must satisfy several important properties to serve as drop-in replacements for text.

</details>

### [Multi-view Temporal Alignment for Non-parallel Articulatory-to-Acoustic Speech Synthesis](2012.15184.md)
**Jose A. Gonzalez-Lopez, Miriam Gonzalez-Atienza, Alejandro Gomez-Alanis, Jose L. Perez-Cordoba et al.** · 2020-12-30

<details>
<summary>Abstract</summary>

Articulatory-to-acoustic (A2A) synthesis refers to the generation of audible speech from captured movement of the speech articulators. This technique has numerous applications, such as restoring oral communication to people who cannot longer speak due to illness or injury. Most successful techniques so far adopt a supervised learning framework, in which time-synchronous articulatory-and-speech recordings are used to train a supervised machine learning algorithm that can be used later to map articulator movements to speech. This, however, prevents the application of A2A techniques in cases where parallel data is unavailable, e.g., a person has already lost her/his voice and only articulatory data can be captured. In this work, we propose a solution to this problem based on the theory of multi-view learning. The proposed algorithm attempts to find an optimal temporal alignment between pairs of non-aligned articulatory-and-acoustic sequences with the same phonetic content by projecting them into a common latent space where both views are maximally correlated and then applying dynamic time warping. Several variants of this idea are discussed and explored. We show that the quality of speech generated in the non-aligned scenario is comparable to that obtained in the parallel scenario.

</details>

### [Detection of Lexical Stress Errors in Non-Native (L2) English with Data Augmentation and Attention](2012.14788.md)
**Daniel Korzekwa, Roberto Barra-Chicote, Szymon Zaporowski, Grzegorz Beringer et al.** · 2020-12-29

<details>
<summary>Abstract</summary>

This paper describes two novel complementary techniques that improve the detection of lexical stress errors in non-native (L2) English speech: attention-based feature extraction and data augmentation based on Neural Text-To-Speech (TTS). In a classical approach, audio features are usually extracted from fixed regions of speech such as the syllable nucleus. We propose an attention-based deep learning model that automatically derives optimal syllable-level representation from frame-level and phoneme-level audio features. Training this model is challenging because of the limited amount of incorrect stress patterns. To solve this problem, we propose to augment the training set with incorrectly stressed words generated with Neural TTS. Combining both techniques achieves 94.8% precision and 49.2% recall for the detection of incorrectly stressed words in L2 English speech of Slavic and Baltic speakers.

</details>

### [Building Multi lingual TTS using Cross Lingual Voice Conversion](2012.14039.md)
**Qinghua Sun, Kenji Nagamatsu** · 2020-12-28

<details>
<summary>Abstract</summary>

In this paper we propose a new cross-lingual Voice Conversion (VC) approach which can generate all speech parameters (MCEP, LF0, BAP) from one DNN model using PPGs (Phonetic PosteriorGrams) extracted from inputted speech using several ASR acoustic models. Using the proposed VC method, we tried three different approaches to build a multilingual TTS system without recording a multilingual speech corpus. A listening test was carried out to evaluate both speech quality (naturalness) and voice similarity between converted speech and target speech. The results show that Approach 1 achieved the highest level of naturalness (3.28 MOS on a 5-point scale) and similarity (2.77 MOS).

</details>

### [Incremental Text-to-Speech Synthesis Using Pseudo Lookahead with Large Pretrained Language Model](2012.12612.md)
**Takaaki Saeki, Shinnosuke Takamichi, Hiroshi Saruwatari** · 2020-12-23

<details>
<summary>Abstract</summary>

This letter presents an incremental text-to-speech (TTS) method that performs synthesis in small linguistic units while maintaining the naturalness of output speech. Incremental TTS is generally subject to a trade-off between latency and synthetic speech quality. It is challenging to produce high-quality speech with a low-latency setup that does not make much use of an unobserved future sentence (hereafter, "lookahead"). To resolve this issue, we propose an incremental TTS method that uses a pseudo lookahead generated with a language model to take the future contextual information into account without increasing latency. Our method can be regarded as imitating a human's incremental reading and uses pretrained GPT2, which accounts for the large-scale linguistic knowledge, for the lookahead generation. Evaluation results show that our method 1) achieves higher speech quality than the method taking only observed information into account and 2) achieves a speech quality equivalent to waiting for the future context observation.

</details>

### [Myanmar Text-to-Speech Synthesis Using End-to-End Model](s2:9fa5411e664ca7fba114b4daccf7f64d8a67bc4a.md)
**Qinglai Qin, Jian Yang, Peiying Li** · 2020-12-18

<details>
<summary>Abstract</summary>

In this paper, we propose a Myanmar speech synthesis system based on an End-to-End neural network model, which integrates the Myanmar phone model into the Tacotron2 End-to-End model. Based on the Seq2seq model architecture, we use phone-level embedding to form a feature prediction network from phone sequences to Mel spectrum, and combine with a semi-supervised speech generation network to generate high-quality Myanmar synthesized speech. In addition, we introduced the BERT pre-training decoder module to assist the phone feature extraction, which reduces the system's dependence on the phone feature extraction network and improve the text feature richness. Compared with other Myanmar speech synthesis systems, this method effectively improves the naturalness and accuracy of synthesized speech under low resource conditions.

</details>

### [Parallel WaveNet conditioned on VAE latent vectors](2012.09703.md)
**Jonas Rohnke, Tom Merritt, Jaime Lorenzo-Trueba, Adam Gabrys et al.** · 2020-12-17

<details>
<summary>Abstract</summary>

Recently the state-of-the-art text-to-speech synthesis systems have shifted to a two-model approach: a sequence-to-sequence model to predict a representation of speech (typically mel-spectrograms), followed by a 'neural vocoder' model which produces the time-domain speech waveform from this intermediate speech representation. This approach is capable of synthesizing speech that is confusable with natural speech recordings. However, the inference speed of neural vocoder approaches represents a major obstacle for deploying this technology for commercial applications. Parallel WaveNet is one approach which has been developed to address this issue, trading off some synthesis quality for significantly faster inference speed. In this paper we investigate the use of a sentence-level conditioning vector to improve the signal quality of a Parallel WaveNet neural vocoder. We condition the neural vocoder with the latent vector from a pre-trained VAE component of a Tacotron 2-style sequence-to-sequence model. With this, we are able to significantly improve the quality of vocoded speech.

</details>

### [DenoiSpeech: Denoising Text to Speech with Frame-Level Noise Modeling](2012.09547.md)
**Chen Zhang, Yi Ren, Xu Tan, Jinglin Liu et al.** · 2020-12-17

<details>
<summary>Abstract</summary>

While neural-based text to speech (TTS) models can synthesize natural and intelligible voice, they usually require high-quality speech data, which is costly to collect. In many scenarios, only noisy speech of a target speaker is available, which presents challenges for TTS model training for this speaker. Previous works usually address the challenge using two methods: 1) training the TTS model using the speech denoised with an enhancement model; 2) taking a single noise embedding as input when training with noisy speech. However, they usually cannot handle speech with real-world complicated noise such as those with high variations along time. In this paper, we develop DenoiSpeech, a TTS system that can synthesize clean speech for a speaker with noisy speech data. In DenoiSpeech, we handle real-world noisy speech by modeling the fine-grained frame-level noise with a noise condition module, which is jointly trained with the TTS model. Experimental results on real-world data show that DenoiSpeech outperforms the previous two methods by 0.31 and 0.66 MOS respectively.

</details>

### [Multi-SpectroGAN: High-Diversity and High-Fidelity Spectrogram Generation with Adversarial Style Combination for Speech Synthesis](2012.07267.md)
**Sang-Hoon Lee, Hyun-Wook Yoon, Hyeong-Rae Noh, Ji-Hoon Kim et al.** · 2020-12-14

<details>
<summary>Abstract</summary>

While generative adversarial networks (GANs) based neural text-to-speech (TTS) systems have shown significant improvement in neural speech synthesis, there is no TTS system to learn to synthesize speech from text sequences with only adversarial feedback. Because adversarial feedback alone is not sufficient to train the generator, current models still require the reconstruction loss compared with the ground-truth and the generated mel-spectrogram directly. In this paper, we present Multi-SpectroGAN (MSG), which can train the multi-speaker model with only the adversarial feedback by conditioning a self-supervised hidden representation of the generator to a conditional discriminator. This leads to better guidance for generator training. Moreover, we also propose adversarial style combination (ASC) for better generalization in the unseen speaking style and transcript, which can learn latent representations of the combined style embedding from multiple mel-spectrograms. Trained with ASC and feature matching, the MSG synthesizes a high-diversity mel-spectrogram by controlling and mixing the individual speaking styles (e.g., duration, pitch, and energy). The result shows that the MSG synthesizes a high-fidelity mel-spectrogram, which has almost the same naturalness MOS score as the ground-truth mel-spectrogram.

</details>

### [Few Shot Adaptive Normalization Driven Multi-Speaker Speech Synthesis](2012.07252.md)
**Neeraj Kumar, Srishti Goel, Ankur Narang, Brejesh Lall** · 2020-12-14

<details>
<summary>Abstract</summary>

The style of the speech varies from person to person and every person exhibits his or her own style of speaking that is determined by the language, geography, culture and other factors. Style is best captured by prosody of a signal. High quality multi-speaker speech synthesis while considering prosody and in a few shot manner is an area of active research with many real-world applications. While multiple efforts have been made in this direction, it remains an interesting and challenging problem. In this paper, we present a novel few shot multi-speaker speech synthesis approach (FSM-SS) that leverages adaptive normalization architecture with a non-autoregressive multi-head attention model. Given an input text and a reference speech sample of an unseen person, FSM-SS can generate speech in that person's style in a few shot manner. Additionally, we demonstrate how the affine parameters of normalization help in capturing the prosodic features such as energy and fundamental frequency in a disentangled fashion and can be used to generate morphed speech output. We demonstrate the efficacy of our proposed architecture on multi-speaker VCTK and LibriTTS datasets, using multiple quantitative metrics that measure generated speech distortion and MoS, along with speaker embedding analysis of the generated speech vs the actual speech samples.

</details>

### [Syntactic representation learning for neural network based TTS with syntactic parse tree traversal](2012.06971.md)
**Changhe Song, Jingbei Li, Yixuan Zhou, Zhiyong Wu et al.** · 2020-12-13

<details>
<summary>Abstract</summary>

Syntactic structure of a sentence text is correlated with the prosodic structure of the speech that is crucial for improving the prosody and naturalness of a text-to-speech (TTS) system. Nowadays TTS systems usually try to incorporate syntactic structure information with manually designed features based on expert knowledge. In this paper, we propose a syntactic representation learning method based on syntactic parse tree traversal to automatically utilize the syntactic structure information. Two constituent label sequences are linearized through left-first and right-first traversals from constituent parse tree. Syntactic representations are then extracted at word level from each constituent label sequence by a corresponding uni-directional gated recurrent unit (GRU) network. Meanwhile, nuclear-norm maximization loss is introduced to enhance the discriminability and diversity of the embeddings of constituent labels. Upsampled syntactic representations and phoneme embeddings are concatenated to serve as the encoder input of Tacotron2. Experimental results demonstrate the effectiveness of our proposed approach, with mean opinion score (MOS) increasing from 3.70 to 3.82 and ABX preference exceeding by 17% compared with the baseline. In addition, for sentences with multiple syntactic parse trees, prosodic differences can be clearly perceived from the synthesized speeches.

</details>

### [Using previous acoustic context to improve Text-to-Speech synthesis](2012.03763.md)
**Pilar Oplustil-Gallegos, Simon King** · 2020-12-07

<details>
<summary>Abstract</summary>

Many speech synthesis datasets, especially those derived from audiobooks, naturally comprise sequences of utterances. Nevertheless, such data are commonly treated as individual, unordered utterances both when training a model and at inference time. This discards important prosodic phenomena above the utterance level. In this paper, we leverage the sequential nature of the data using an acoustic context encoder that produces an embedding of the previous utterance audio. This is input to the decoder in a Tacotron 2 model. The embedding is also used for a secondary task, providing additional supervision. We compare two secondary tasks: predicting the ordering of utterance pairs, and predicting the embedding of the current utterance audio. Results show that the relation between consecutive utterances is informative: our proposed model significantly improves naturalness over a Tacotron 2 baseline.

</details>

### [EfficientTTS: An Efficient and High-Quality Text-to-Speech Architecture](2012.03500.md)
**Chenfeng Miao, Shuang Liang, Zhencheng Liu, Minchuan Chen et al.** · 2020-12-07

<details>
<summary>Abstract</summary>

In this work, we address the Text-to-Speech (TTS) task by proposing a non-autoregressive architecture called EfficientTTS. Unlike the dominant non-autoregressive TTS models, which are trained with the need of external aligners, EfficientTTS optimizes all its parameters with a stable, end-to-end training procedure, while allowing for synthesizing high quality speech in a fast and efficient manner. EfficientTTS is motivated by a new monotonic alignment modeling approach (also introduced in this work), which specifies monotonic constraints to the sequence alignment with almost no increase of computation. By combining EfficientTTS with different feed-forward network structures, we develop a family of TTS models, including both text-to-melspectrogram and text-to-waveform networks. We experimentally show that the proposed models significantly outperform counterpart models such as Tacotron 2 and Glow-TTS in terms of speech quality, training efficiency and synthesis speed, while still producing the speeches of strong robustness and great diversity. In addition, we demonstrate that proposed approach can be easily extended to autoregressive models such as Tacotron 2.

</details>

### [Personalized End-to-End Mandarin Speech Synthesis using Small-sized Corpus](s2:29ab1d6d8077858781548c225853b87dd577de6c.md)
**Chenhan Yuan, Yi-Chin Huang** · 2020-12-07

### [Cross-Modal Generalization: Learning in Low Resource Modalities via Meta-Alignment](2012.02813.md)
**Paul Pu Liang, Peter Wu, Liu Ziyin, Louis-Philippe Morency et al.** · 2020-12-04

<details>
<summary>Abstract</summary>

The natural world is abundant with concepts expressed via visual, acoustic, tactile, and linguistic modalities. Much of the existing progress in multimodal learning, however, focuses primarily on problems where the same set of modalities are present at train and test time, which makes learning in low-resource modalities particularly difficult. In this work, we propose algorithms for cross-modal generalization: a learning paradigm to train a model that can (1) quickly perform new tasks in a target modality (i.e. meta-learning) and (2) doing so while being trained on a different source modality. We study a key research question: how can we ensure generalization across modalities despite using separate encoders for different source and target modalities? Our solution is based on meta-alignment, a novel method to align representation spaces using strongly and weakly paired cross-modal data while ensuring quick generalization to new tasks across different modalities. We study this problem on 3 classification tasks: text to image, image to audio, and text to speech. Our results demonstrate strong performance even when the new target modality has only a few (1-10) labeled samples and in the presence of noisy labels, a scenario particularly prevalent in low-resource modalities.

</details>

### [Text-to-speech for the hearing impaired](2012.02174.md)
**Josef Schlittenlacher, Thomas Baer** · 2020-12-03

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) systems offer the opportunity to compensate for a hearing loss at the source rather than correcting for it at the receiving end. This removes limitations such as time constraints for algorithms that amplify a sound in a hearing aid and can lead to higher speech quality. We propose an algorithm that restores loudness to normal perception at a high resolution in time, frequency and level, and embed it in a TTS system that uses Tacotron2 and WaveGlow to produce individually amplified speech. Subjective evaluations of speech quality showed that the proposed algorithm led to high-quality audio with sound quality similar to original or linearly amplified speech but considerably higher speech intelligibility in noise. Transfer learning led to a quick adaptation of the produced spectra from original speech to individually amplified speech, resulted in high speech quality and intelligibility, and thus gives us a way to train an individual TTS system efficiently.

</details>

### [GraphPB: Graphical Representations of Prosody Boundary in Speech Synthesis](2012.02626.md)
**Aolan Sun, Jianzong Wang, Ning Cheng, Huayi Peng et al.** · 2020-12-03

<details>
<summary>Abstract</summary>

This paper introduces a graphical representation approach of prosody boundary (GraphPB) in the task of Chinese speech synthesis, intending to parse the semantic and syntactic relationship of input sequences in a graphical domain for improving the prosody performance. The nodes of the graph embedding are formed by prosodic words, and the edges are formed by the other prosodic boundaries, namely prosodic phrase boundary (PPH) and intonation phrase boundary (IPH). Different Graph Neural Networks (GNN) like Gated Graph Neural Network (GGNN) and Graph Long Short-term Memory (G-LSTM) are utilised as graph encoders to exploit the graphical prosody boundary information. Graph-to-sequence model is proposed and formed by a graph encoder and an attentional decoder. Two techniques are proposed to embed sequential information into the graph-to-sequence text-to-speech model. The experimental results show that this proposed approach can encode the phonetic and prosody rhythm of an utterance. The mean opinion score (MOS) of these GNN models shows comparative results with the state-of-the-art sequence-to-sequence models with better performance in the aspect of prosody. This provides an alternative approach for prosody modelling in end-to-end speech synthesis.

</details>

### [MelGlow: Efficient Waveform Generative Network Based on Location-Variable Convolution](2012.01684.md)
**Zhen Zeng, Jianzong Wang, Ning Cheng, Jing Xiao** · 2020-12-03

<details>
<summary>Abstract</summary>

Recent neural vocoders usually use a WaveNet-like network to capture the long-term dependencies of the waveform, but a large number of parameters are required to obtain good modeling capabilities. In this paper, an efficient network, named location-variable convolution, is proposed to model the dependencies of waveforms. Different from the use of unified convolution kernels in WaveNet to capture the dependencies of arbitrary waveforms, location-variable convolutions utilizes a kernel predictor to generate multiple sets of convolution kernels based on the mel-spectrum, where each set of convolution kernels is used to perform convolution operations on the associated waveform intervals. Combining WaveGlow and location-variable convolutions, an efficient vocoder, named MelGlow, is designed. Experiments on the LJSpeech dataset show that MelGlow achieves better performance than WaveGlow at small model sizes, which verifies the effectiveness and potential optimization space of location-variable convolutions.

</details>

### [Phonetic Posteriorgrams based Many-to-Many Singing Voice Conversion via Adversarial Training](2012.01837.md)
**Haohan Guo, Heng Lu, Na Hu, Chunlei Zhang et al.** · 2020-12-03

<details>
<summary>Abstract</summary>

This paper describes an end-to-end adversarial singing voice conversion (EA-SVC) approach. It can directly generate arbitrary singing waveform by given phonetic posteriorgram (PPG) representing content, F0 representing pitch, and speaker embedding representing timbre, respectively. Proposed system is composed of three modules: generator $G$, the audio generation discriminator $D_{A}$, and the feature disentanglement discriminator $D_F$. The generator $G$ encodes the features in parallel and inversely transforms them into the target waveform. In order to make timbre conversion more stable and controllable, speaker embedding is further decomposed to the weighted sum of a group of trainable vectors representing different timbre clusters. Further, to realize more robust and accurate singing conversion, disentanglement discriminator $D_F$ is proposed to remove pitch and timbre related information that remains in the encoded PPG. Finally, a two-stage training is conducted to keep a stable and effective adversarial training process. Subjective evaluation results demonstrate the effectiveness of our proposed methods. Proposed system outperforms conventional cascade approach and the WaveNet based end-to-end approach in terms of both singing quality and singer similarity. Further objective analysis reveals that the model trained with the proposed two-stage training strategy can produce a smoother and sharper formant which leads to higher audio quality.

</details>

### [Vietnamese Speech Synthesis with End-to-End Model and Text Normalization](s2:540b990bec5a5b95a7f4816d65d36dcc08b724a7.md)
**D. Nhan, N. Tri, Cao Xuan Nam** · 2020-11-26

<details>
<summary>Abstract</summary>

Speech synthesis systems are now getting smarter and more natural thanks to the power of deep neural networks. However, each language has a different phonological and contextual characteristics, we have conducted experiments, statistics, and applied Vietnamese phonetics to improve speech synthesis systems based on Tacotron2 neural networks. Our methods achieve the accuracy of 97% in text normalization task, and the synthesized speeches with a MOS score of 3.97, asymptotic to 4.43 of the voices that are directly recorded. We also provide a library for standardizing Vietnamese text called Vinorm and a package that converts text into a phonetic format called Viphoneme, which is used as an input for end-to-end neural networks, make the synthesis process faster, more intelligent and natural than using character inputs.

</details>

### [FBWave: Efficient and Scalable Neural Vocoders for Streaming Text-To-Speech on the Edge](2011.12985.md)
**Bichen Wu, Qing He, Peizhao Zhang, Thilo Koehler et al.** · 2020-11-25

<details>
<summary>Abstract</summary>

Nowadays more and more applications can benefit from edge-based text-to-speech (TTS). However, most existing TTS models are too computationally expensive and are not flexible enough to be deployed on the diverse variety of edge devices with their equally diverse computational capacities. To address this, we propose FBWave, a family of efficient and scalable neural vocoders that can achieve optimal performance-efficiency trade-offs for different edge devices. FBWave is a hybrid flow-based generative model that combines the advantages of autoregressive and non-autoregressive models. It produces high quality audio and supports streaming during inference while remaining highly computationally efficient. Our experiments show that FBWave can achieve similar audio quality to WaveRNN while reducing MACs by 40x. More efficient variants of FBWave can achieve up to 109x fewer MACs while still delivering acceptable audio quality. Audio demos are available at https://bichenwu09.github.io/vocoder_demos.

</details>

### [TFGAN: Time and Frequency Domain Based Generative Adversarial Network for High-fidelity Speech Synthesis](2011.12206.md)
**Qiao Tian, Yi Chen, Zewang Zhang, Heng Lu et al.** · 2020-11-24

<details>
<summary>Abstract</summary>

Recently, GAN based speech synthesis methods, such as MelGAN, have become very popular. Compared to conventional autoregressive based methods, parallel structures based generators make waveform generation process fast and stable. However, the quality of generated speech by autoregressive based neural vocoders, such as WaveRNN, is still higher than GAN. To address this issue, we propose a novel vocoder model: TFGAN, which is adversarially learned both in time and frequency domain. On one hand, we propose to discriminate ground-truth waveform from synthetic one in frequency domain for offering more consistency guarantees instead of only in time domain. On the other hand, in contrast to the conventionally frequency-domain STFT loss approach or feature map loss by discriminator to learn waveform, we propose a set of time-domain loss that encourage the generator to capture the waveform directly. TFGAN has nearly same synthesis speed as MelGAN, but the fidelity is significantly improved by our novel learning method. In our experiments, TFGAN shows the ability to achieve comparable mean opinion score (MOS) than autoregressive vocoder under speech synthesis context.

</details>

### [Empirical Evaluation of Deep Learning Model Compression Techniques on the WaveNet Vocoder](2011.10469.md)
**Sam Davis, Giuseppe Coccia, Sam Gooch, Julian Mack** · 2020-11-20

<details>
<summary>Abstract</summary>

WaveNet is a state-of-the-art text-to-speech vocoder that remains challenging to deploy due to its autoregressive loop. In this work we focus on ways to accelerate the original WaveNet architecture directly, as opposed to modifying the architecture, such that the model can be deployed as part of a scalable text-to-speech system. We survey a wide variety of model compression techniques that are amenable to deployment on a range of hardware platforms. In particular, we compare different model sparsity methods and levels, and seven widely used precisions as targets for quantization; and are able to achieve models with a compression ratio of up to 13.84 without loss in audio fidelity compared to a dense, single-precision floating-point baseline. All techniques are implemented using existing open source deep learning frameworks and libraries to encourage their wider adoption.

</details>

### [Universal MelGAN: A Robust Neural Vocoder for High-Fidelity Waveform Generation in Multiple Domains](2011.09631.md)
**Won Jang, Dan Lim, Jaesam Yoon** · 2020-11-19

<details>
<summary>Abstract</summary>

We propose Universal MelGAN, a vocoder that synthesizes high-fidelity speech in multiple domains. To preserve sound quality when the MelGAN-based structure is trained with a dataset of hundreds of speakers, we added multi-resolution spectrogram discriminators to sharpen the spectral resolution of the generated waveforms. This enables the model to generate realistic waveforms of multi-speakers, by alleviating the over-smoothing problem in the high frequency band of the large footprint model. Our structure generates signals close to ground-truth data without reducing the inference speed, by discriminating the waveform and spectrogram during training. The model achieved the best mean opinion score (MOS) in most scenarios using ground-truth mel-spectrogram as an input. Especially, it showed superior performance in unseen domains with regard of speaker, emotion, and language. Moreover, in a multi-speaker text-to-speech scenario using mel-spectrogram generated by a transformer model, it synthesized high-fidelity speech of 4.22 MOS. These results, achieved without external domain information, highlight the potential of the proposed model as a universal vocoder.

</details>

### [Controllable Emotion Transfer For End-to-End Speech Synthesis](2011.08679.md)
**Tao Li, Shan Yang, Liumeng Xue, Lei Xie** · 2020-11-17

<details>
<summary>Abstract</summary>

Emotion embedding space learned from references is a straightforward approach for emotion transfer in encoder-decoder structured emotional text to speech (TTS) systems. However, the transferred emotion in the synthetic speech is not accurate and expressive enough with emotion category confusions. Moreover, it is hard to select an appropriate reference to deliver desired emotion strength. To solve these problems, we propose a novel approach based on Tacotron. First, we plug two emotion classifiers -- one after the reference encoder, one after the decoder output -- to enhance the emotion-discriminative ability of the emotion embedding and the predicted mel-spectrum. Second, we adopt style loss to measure the difference between the generated and reference mel-spectrum. The emotion strength in the synthetic speech can be controlled by adjusting the value of the emotion embedding as the emotion embedding can be viewed as the feature map of the mel-spectrum. Experiments on emotion transfer and strength control have shown that the synthetic speech of the proposed method is more accurate and expressive with less emotion category confusions and the control of emotion strength is more salient to listeners.

</details>

### [s-Transformer: Segment-Transformer for Robust Neural Speech Synthesis](2011.08480.md)
**Xi Wang, Huaiping Ming, Lei He, Frank K. Soong** · 2020-11-17

<details>
<summary>Abstract</summary>

Neural end-to-end text-to-speech (TTS) , which adopts either a recurrent model, e.g. Tacotron, or an attention one, e.g. Transformer, to characterize a speech utterance, has achieved significant improvement of speech synthesis. However, it is still very challenging to deal with different sentence lengths, particularly, for long sentences where sequence model has limitation of the effective context length. We propose a novel segment-Transformer (s-Transformer), which models speech at segment level where recurrence is reused via cached memories for both the encoder and decoder. Long-range contexts can be captured by the extended memory, meanwhile, the encoder-decoder attention on segment which is much easier to handle. In addition, we employ a modified relative positional self attention to generalize sequence length beyond a period possibly unseen in the training data. By comparing the proposed s-Transformer with the standard Transformer, on short sentences, both achieve the same MOS scores of 4.29, which is very close to 4.32 by the recordings; similar scores of 4.22 vs 4.2 on long sentences, and significantly better for extra-long sentences with a gain of 0.2 in MOS. Since the cached memory is updated with time, the s-Transformer generates rather natural and coherent speech for a long period of time.

</details>

### [Fine-grained Emotion Strength Transfer, Control and Prediction for Emotional Speech Synthesis](2011.08477.md)
**Yi Lei, Shan Yang, Lei Xie** · 2020-11-17

<details>
<summary>Abstract</summary>

This paper proposes a unified model to conduct emotion transfer, control and prediction for sequence-to-sequence based fine-grained emotional speech synthesis. Conventional emotional speech synthesis often needs manual labels or reference audio to determine the emotional expressions of synthesized speech. Such coarse labels cannot control the details of speech emotion, often resulting in an averaged emotion expression delivery, and it is also hard to choose suitable reference audio during inference. To conduct fine-grained emotion expression generation, we introduce phoneme-level emotion strength representations through a learned ranking function to describe the local emotion details, and the sentence-level emotion category is adopted to render the global emotions of synthesized speech. With the global render and local descriptors of emotions, we can obtain fine-grained emotion expressions from reference audio via its emotion descriptors (for transfer) or directly from phoneme-level manual labels (for control). As for the emotional speech synthesis with arbitrary text inputs, the proposed model can also predict phoneme-level emotion expressions from texts, which does not require any reference audio or manual label.

</details>

### [Learn2Sing: Target Speaker Singing Voice Synthesis by learning from a Singing Teacher](2011.08467.md)
**Heyang Xue, Shan Yang, Yi Lei, Lei Xie et al.** · 2020-11-17

<details>
<summary>Abstract</summary>

Singing voice synthesis has been paid rising attention with the rapid development of speech synthesis area. In general, a studio-level singing corpus is usually necessary to produce a natural singing voice from lyrics and music-related transcription. However, such a corpus is difficult to collect since it's hard for many of us to sing like a professional singer. In this paper, we propose an approach -- Learn2Sing that only needs a singing teacher to generate the target speakers' singing voice without their singing voice data. In our approach, a teacher's singing corpus and speech from multiple target speakers are trained in a frame-level auto-regressive acoustic model where singing and speaking share the common speaker embedding and style tag embedding. Meanwhile, since there is no music-related transcription for the target speaker, we use log-scale fundamental frequency (LF0) as an auxiliary feature as the inputs of the acoustic model for building a unified input representation. In order to enable the target speaker to sing without singing reference audio in the inference stage, a duration model and an LF0 prediction model are also trained. Particularly, we employ domain adversarial training (DAT) in the acoustic model, which aims to enhance the singing performance of target speakers by disentangling style from acoustic features of singing and speaking data. Our experiments indicate that the proposed approach is capable of synthesizing singing voice for target speaker given only their speech samples.

</details>

### [Accent and Speaker Disentanglement in Many-to-many Voice Conversion](2011.08609.md)
**Zhichao Wang, Wenshuo Ge, Xiong Wang, Shan Yang et al.** · 2020-11-17

<details>
<summary>Abstract</summary>

This paper proposes an interesting voice and accent joint conversion approach, which can convert an arbitrary source speaker's voice to a target speaker with non-native accent. This problem is challenging as each target speaker only has training data in native accent and we need to disentangle accent and speaker information in the conversion model training and re-combine them in the conversion stage. In our recognition-synthesis conversion framework, we manage to solve this problem by two proposed tricks. First, we use accent-dependent speech recognizers to obtain bottleneck features for different accented speakers. This aims to wipe out other factors beyond the linguistic information in the BN features for conversion model training. Second, we propose to use adversarial training to better disentangle the speaker and accent information in our encoder-decoder based conversion model. Specifically, we plug an auxiliary speaker classifier to the encoder, trained with an adversarial loss to wipe out speaker information from the encoder output. Experiments show that our approach is superior to the baseline. The proposed tricks are quite effective in improving accentedness and audio quality and speaker similarity are well maintained.

</details>

### [Optimizing voice conversion network with cycle consistency loss of speaker identity](2011.08548.md)
**Hongqiang Du, Xiaohai Tian, Lei Xie, Haizhou Li** · 2020-11-17

<details>
<summary>Abstract</summary>

We propose a novel training scheme to optimize voice conversion network with a speaker identity loss function. The training scheme not only minimizes frame-level spectral loss, but also speaker identity loss. We introduce a cycle consistency loss that constrains the converted speech to maintain the same speaker identity as reference speech at utterance level. While the proposed training scheme is applicable to any voice conversion networks, we formulate the study under the average model voice conversion framework in this paper. Experiments conducted on CMU-ARCTIC and CSTR-VCTK corpus confirm that the proposed method outperforms baseline methods in terms of speaker similarity.

</details>

### [Hierarchical Prosody Modeling for Non-Autoregressive Speech Synthesis](2011.06465.md)
**Chung-Ming Chien, Hung-yi Lee** · 2020-11-12

<details>
<summary>Abstract</summary>

Prosody modeling is an essential component in modern text-to-speech (TTS) frameworks. By explicitly providing prosody features to the TTS model, the style of synthesized utterances can thus be controlled. However, predicting natural and reasonable prosody at inference time is challenging. In this work, we analyzed the behavior of non-autoregressive TTS models under different prosody-modeling settings and proposed a hierarchical architecture, in which the prediction of phoneme-level prosody features are conditioned on the word-level prosody features. The proposed method outperforms other competitors in terms of audio quality and prosody naturalness in our objective and subjective evaluation.

</details>

### [Using IPA-Based Tacotron for Data Efficient Cross-Lingual Speaker Adaptation and Pronunciation Enhancement](2011.06392.md)
**Hamed Hemati, Damian Borth** · 2020-11-12

<details>
<summary>Abstract</summary>

Recent neural Text-to-Speech (TTS) models have been shown to perform very well when enough data is available. However, fine-tuning them for new speakers or languages is not straightforward in a low-resource setup. In this paper, we show that by applying minor modifications to a Tacotron model, one can transfer an existing TTS model for new speakers from the same or a different language using only 20 minutes of data. For this purpose, we first introduce a base multi-lingual Tacotron with language-agnostic input, then demonstrate how transfer learning is done for different scenarios of speaker adaptation without exploiting any pre-trained speaker encoder or code-switching technique. We evaluate the transferred model in both subjective and objective ways.

</details>

### [Low-resource expressive text-to-speech using data augmentation](2011.05707.md)
**Goeric Huybrechts, Thomas Merritt, Giulia Comini, Bartek Perz et al.** · 2020-11-11

<details>
<summary>Abstract</summary>

While recent neural text-to-speech (TTS) systems perform remarkably well, they typically require a substantial amount of recordings from the target speaker reading in the desired speaking style. In this work, we present a novel 3-step methodology to circumvent the costly operation of recording large amounts of target data in order to build expressive style voices with as little as 15 minutes of such recordings. First, we augment data via voice conversion by leveraging recordings in the desired speaking style from other speakers. Next, we use that synthetic data on top of the available recordings to train a TTS model. Finally, we fine-tune that model to further increase quality. Our evaluations show that the proposed changes bring significant improvements over non-augmented models across many perceived aspects of synthesised speech. We demonstrate the proposed approach on 2 styles (newscaster and conversational), on various speakers, and on both single and multi-speaker models, illustrating the robustness of our approach.

</details>

### [Using GANs to Synthesise Minimum Training Data for Deepfake Generation](2011.05421.md)
**Simranjeet Singh, Rajneesh Sharma, Alan F. Smeaton** · 2020-11-10

<details>
<summary>Abstract</summary>

There are many applications of Generative Adversarial Networks (GANs) in fields like computer vision, natural language processing, speech synthesis, and more. Undoubtedly the most notable results have been in the area of image synthesis and in particular in the generation of deepfake videos. While deepfakes have received much negative media coverage, they can be a useful technology in applications like entertainment, customer relations, or even assistive care. One problem with generating deepfakes is the requirement for a lot of image training data of the subject which is not an issue if the subject is a celebrity for whom many images already exist. If there are only a small number of training images then the quality of the deepfake will be poor. Some media reports have indicated that a good deepfake can be produced with as few as 500 images but in practice, quality deepfakes require many thousands of images, one of the reasons why deepfakes of celebrities and politicians have become so popular. In this study, we exploit the property of a GAN to produce images of an individual with variable facial expressions which we then use to generate a deepfake. We observe that with such variability in facial expressions of synthetic GAN-generated training images and a reduced quantity of them, we can produce a near-realistic deepfake videos.

</details>

### [Pretraining Strategies, Waveform Model Choice, and Acoustic Configurations for Multi-Speaker End-to-End Speech Synthesis](2011.04839.md)
**Erica Cooper, Xin Wang, Yi Zhao, Yusuke Yasuda et al.** · 2020-11-10

<details>
<summary>Abstract</summary>

We explore pretraining strategies including choice of base corpus with the aim of choosing the best strategy for zero-shot multi-speaker end-to-end synthesis. We also examine choice of neural vocoder for waveform synthesis, as well as acoustic configurations used for mel spectrograms and final audio output. We find that fine-tuning a multi-speaker model from found audiobook data that has passed a simple quality threshold can improve naturalness and similarity to unseen target speakers of synthetic speech. Additionally, we find that listeners can discern between a 16kHz and 24kHz sampling rate, and that WaveRNN produces output waveforms of a comparable quality to WaveNet, with a faster inference time.

</details>

### [Enhancing Low-Quality Voice Recordings Using Disentangled Channel Factor and Neural Waveform Model](2011.05038.md)
**Haoyu Li, Yang Ai, Junichi Yamagishi** · 2020-11-10

<details>
<summary>Abstract</summary>

High-quality speech corpora are essential foundations for most speech applications. However, such speech data are expensive and limited since they are collected in professional recording environments. In this work, we propose an encoder-decoder neural network to automatically enhance low-quality recordings to professional high-quality recordings. To address channel variability, we first filter out the channel characteristics from the original input audio using the encoder network with adversarial training. Next, we disentangle the channel factor from a reference audio. Conditioned on this factor, an auto-regressive decoder is then used to predict the target-environment Mel spectrogram. Finally, we apply a neural vocoder to synthesize the speech waveform. Experimental results show that the proposed system can generate a professional high-quality speech waveform when setting high-quality audio as the reference. It also improves speech enhancement performance compared with several state-of-the-art baseline systems.

</details>

### [Fine-grained Style Modeling, Transfer and Prediction in Text-to-Speech Synthesis via Phone-Level Content-Style Disentanglement](2011.03943.md)
**Daxin Tan, Tan Lee** · 2020-11-08

<details>
<summary>Abstract</summary>

This paper presents a novel design of neural network system for fine-grained style modeling, transfer and prediction in expressive text-to-speech (TTS) synthesis. Fine-grained modeling is realized by extracting style embeddings from the mel-spectrograms of phone-level speech segments. Collaborative learning and adversarial learning strategies are applied in order to achieve effective disentanglement of content and style factors in speech and alleviate the "content leakage" problem in style modeling. The proposed system can be used for varying-content speech style transfer in the single-speaker scenario. The results of objective and subjective evaluation show that our system performs better than other fine-grained speech style transfer models, especially in the aspect of content preservation. By incorporating a style predictor, the proposed system can also be used for text-to-speech synthesis. Audio samples are provided for system demonstration https://daxintan-cuhk.github.io/pl-csd-speech .

</details>

### [Denoising-and-Dereverberation Hierarchical Neural Vocoder for Robust Waveform Generation](2011.03955.md)
**Yang Ai, Haoyu Li, Xin Wang, Junichi Yamagishi et al.** · 2020-11-08

<details>
<summary>Abstract</summary>

This paper presents a denoising and dereverberation hierarchical neural vocoder (DNR-HiNet) to convert noisy and reverberant acoustic features into a clean speech waveform. We implement it mainly by modifying the amplitude spectrum predictor (ASP) in the original HiNet vocoder. This modified denoising and dereverberation ASP (DNR-ASP) can predict clean log amplitude spectra (LAS) from input degraded acoustic features. To achieve this, the DNR-ASP first predicts the noisy and reverberant LAS, noise LAS related to the noise information, and room impulse response related to the reverberation information then performs initial denoising and dereverberation. The initial processed LAS are then enhanced by another neural network as the final clean LAS. To further improve the quality of the generated clean LAS, we also introduce a bandwidth extension model and frequency resolution extension model in the DNR-ASP. The experimental results indicate that the DNR-HiNet vocoder was able to generate a denoised and dereverberated waveform given noisy and reverberant acoustic features and outperformed the original HiNet vocoder and a few other neural vocoders. We also applied the DNR-HiNet vocoder to speech enhancement tasks, and its performance was competitive with several advanced speech enhancement methods.

</details>

### [Naturalization of Text by the Insertion of Pauses and Filler Words](2011.03713.md)
**Richa Sharma, Parth Vipul Shah, Ashwini M. Joshi** · 2020-11-07

<details>
<summary>Abstract</summary>

In this article, we introduce a set of methods to naturalize text based on natural human speech. Voice-based interactions provide a natural way of interfacing with electronic systems and are seeing a widespread adaptation of late. These computerized voices can be naturalized to some degree by inserting pauses and filler words at appropriate positions. The first proposed text transformation method uses the frequency of bigrams in the training data to make appropriate insertions in the input sentence. It uses a probability distribution to choose the insertions from a set of all possible insertions. This method is fast and can be included before a Text-To-Speech module. The second method uses a Recurrent Neural Network to predict the next word to be inserted. It confirms the insertions given by the bigram method. Additionally, the degree of naturalization can be controlled in both these methods. On the conduction of a blind survey, we conclude that the output of these text transformation methods is comparable to natural speech.

</details>

### [Wave-Tacotron: Spectrogram-free end-to-end text-to-speech synthesis](2011.03568.md)
**Ron J. Weiss, RJ Skerry-Ryan, Eric Battenberg, Soroosh Mariooryad et al.** · 2020-11-06

<details>
<summary>Abstract</summary>

We describe a sequence-to-sequence neural network which directly generates speech waveforms from text inputs. The architecture extends the Tacotron model by incorporating a normalizing flow into the autoregressive decoder loop. Output waveforms are modeled as a sequence of non-overlapping fixed-length blocks, each one containing hundreds of samples. The interdependencies of waveform samples within each block are modeled using the normalizing flow, enabling parallel training and synthesis. Longer-term dependencies are handled autoregressively by conditioning each flow on preceding blocks.This model can be optimized directly with maximum likelihood, with-out using intermediate, hand-designed features nor additional loss terms. Contemporary state-of-the-art text-to-speech (TTS) systems use a cascade of separately learned models: one (such as Tacotron) which generates intermediate features (such as spectrograms) from text, followed by a vocoder (such as WaveRNN) which generates waveform samples from the intermediate features. The proposed system, in contrast, does not use a fixed intermediate representation, and learns all parameters end-to-end. Experiments show that the proposed model generates speech with quality approaching a state-of-the-art neural TTS system, with significantly improved generation speed.

</details>

### [Improving Prosody Modelling with Cross-Utterance BERT Embeddings for End-to-end Speech Synthesis](2011.05161.md)
**Guanghui Xu, Wei Song, Zhengchen Zhang, Chao Zhang et al.** · 2020-11-06

<details>
<summary>Abstract</summary>

Despite prosody is related to the linguistic information up to the discourse structure, most text-to-speech (TTS) systems only take into account that within each sentence, which makes it challenging when converting a paragraph of texts into natural and expressive speech. In this paper, we propose to use the text embeddings of the neighboring sentences to improve the prosody generation for each utterance of a paragraph in an end-to-end fashion without using any explicit prosody features. More specifically, cross-utterance (CU) context vectors, which are produced by an additional CU encoder based on the sentence embeddings extracted by a pre-trained BERT model, are used to augment the input of the Tacotron2 decoder. Two types of BERT embeddings are investigated, which leads to the use of different CU encoder structures. Experimental results on a Mandarin audiobook dataset and the LJ-Speech English audiobook dataset demonstrate the use of CU information can improve the naturalness and expressiveness of the synthesized speech. Subjective listening testing shows most of the participants prefer the voice generated using the CU encoder over that generated using standard Tacotron2. It is also found that the prosody can be controlled indirectly by changing the neighbouring sentences.

</details>

### [The Importance Weighted Autoencoder in End-to-End Speech Synthesis](s2:428de665a7baeec08baf30114680bed17b8c4636.md)
**Yutian Wang, Yujiang Peng, Jingling Wang, Hongya Wang et al.** · 2020-11-06

<details>
<summary>Abstract</summary>

The modeling of style when synthesizing speech from text aim to enrich the emotional expression of synthesized speech. In this paper, the importance weighted autoencoder(IWAE) is introduced into Tacotron, an end-to-end speech synthesis system, to learn the latent representation of speaking styles independent of text content in an unsupervised way. Compared with the Variational Autoencoder(VAE), a generative model that can be used to model prior data distribution, IWAE has a strictly tighter variational lower bound derive from different weighted importance. In the proposed network, we input the style representation, learned by IWAE, into Tacotron to generate speech with more rhythmic. Finally, the proposed model shows better performance of speech quality in both objective and subjective ways compared to Global Style Token (GST) and VAE-Tacotron.

</details>

### [Semi-supervised URL Segmentation with Recurrent Neural Networks Pre-trained on Knowledge Graph Entities](2011.03138.md)
**Hao Zhang, Jae Ro, Richard Sproat** · 2020-11-05

<details>
<summary>Abstract</summary>

Breaking domain names such as openresearch into component words open and research is important for applications like Text-to-Speech synthesis and web search. We link this problem to the classic problem of Chinese word segmentation and show the effectiveness of a tagging model based on Recurrent Neural Networks (RNNs) using characters as input. To compensate for the lack of training data, we propose a pre-training method on concatenated entity names in a large knowledge database. Pre-training improves the model by 33% and brings the sequence accuracy to 85%.

</details>

### [Molecumentary: Scalable Narrated Documentaries Using Molecular Visualization](2011.02418.md)
**David Kouřil, Ondřej Strnad, Peter Mindek, Sarkis Halladjian et al.** · 2020-11-04

<details>
<summary>Abstract</summary>

We present a method for producing documentary-style content using real-time scientific visualization. We produce molecumentaries, i.e., molecular documentaries featuring structural models from molecular biology. We employ scalable methods instead of the rigid traditional production pipeline. Our method is motivated by the rapid evolution of interactive scientific visualization, which shows great potential in science dissemination. Without some form of explanation or guidance, however, novices and lay-persons often find it difficult to gain insights from the visualization itself. We integrate such knowledge using the verbal channel and provide it along an engaging visual presentation. To realize the synthesis of a molecumentary, we provide technical solutions along two major production steps: 1) preparing a story structure and 2) turning the story into a concrete narrative. In the first step, information about the model from heterogeneous sources is compiled into a story graph. Local knowledge is combined with remote sources to complete the story graph and enrich the final result. In the second step, a narrative, i.e., story elements presented in sequence, is synthesized using the story graph. We present a method for traversing the story graph and generating a virtual tour, using automated camera and visualization transitions. Texts written by domain experts are turned into verbal representations using text-to-speech functionality and provided as a commentary. Using the described framework we synthesize automatic fly-throughs with descriptions that mimic a manually authored documentary. Furthermore, we demonstrate a second scenario: guiding the documentary narrative by a textual input.

</details>

### [Prosodic Representation Learning and Contextual Sampling for Neural Text-to-Speech](2011.02252.md)
**Sri Karlapati, Ammar Abbas, Zack Hodari, Alexis Moinet et al.** · 2020-11-04

<details>
<summary>Abstract</summary>

In this paper, we introduce Kathaka, a model trained with a novel two-stage training process for neural speech synthesis with contextually appropriate prosody. In Stage I, we learn a prosodic distribution at the sentence level from mel-spectrograms available during training. In Stage II, we propose a novel method to sample from this learnt prosodic distribution using the contextual information available in text. To do this, we use BERT on text, and graph-attention networks on parse trees extracted from text. We show a statistically significant relative improvement of $13.2\%$ in naturalness over a strong baseline when compared to recordings. We also conduct an ablation study on variations of our sampling technique, and show a statistically significant improvement over the baseline in each case.

</details>

### [Learning in your voice: Non-parallel voice conversion based on speaker consistency loss](2011.02168.md)
**Yoohwan Kwon, Soo-Whan Chung, Hee-Soo Heo, Hong-Goo Kang** · 2020-11-04

<details>
<summary>Abstract</summary>

In this paper, we propose a novel voice conversion strategy to resolve the mismatch between the training and conversion scenarios when parallel speech corpus is unavailable for training. Based on auto-encoder and disentanglement frameworks, we design the proposed model to extract identity and content representations while reconstructing the input speech signal itself. Since we use other speaker's identity information in the training process, the training philosophy is naturally matched with the objective of voice conversion process. In addition, we effectively design the disentanglement framework to reliably preserve linguistic information and to enhance the quality of converted speech signals. The superiority of the proposed method is shown in subjective listening tests as well as objective measures.

</details>

### [StyleMelGAN: An Efficient High-Fidelity Adversarial Vocoder with Temporal Adaptive Normalization](2011.01557.md)
**Ahmed Mustafa, Nicola Pia, Guillaume Fuchs** · 2020-11-03

<details>
<summary>Abstract</summary>

In recent years, neural vocoders have surpassed classical speech generation approaches in naturalness and perceptual quality of the synthesized speech. Computationally heavy models like WaveNet and WaveGlow achieve best results, while lightweight GAN models, e.g. MelGAN and Parallel WaveGAN, remain inferior in terms of perceptual quality. We therefore propose StyleMelGAN, a lightweight neural vocoder allowing synthesis of high-fidelity speech with low computational complexity. StyleMelGAN employs temporal adaptive normalization to style a low-dimensional noise vector with the acoustic features of the target speech. For efficient training, multiple random-window discriminators adversarially evaluate the speech signal analyzed by a filter bank, with regularization provided by a multi-scale spectral reconstruction loss. The highly parallelizable speech generation is several times faster than real-time on CPUs and GPUs. MUSHRA and P.800 listening tests show that StyleMelGAN outperforms prior neural vocoders in copy-synthesis and Text-to-Speech scenarios.

</details>

### [Training Wake Word Detection with Synthesized Speech Data on Confusion Words](2011.01460.md)
**Yan Jia, Zexin Cai, Murong Ma, Zeqing Zhao et al.** · 2020-11-03

<details>
<summary>Abstract</summary>

Confusing-words are commonly encountered in real-life keyword spotting applications, which causes severe degradation of performance due to complex spoken terms and various kinds of words that sound similar to the predefined keywords. To enhance the wake word detection system's robustness on such scenarios, we investigate two data augmentation setups for training end-to-end KWS systems. One is involving the synthesized data from a multi-speaker speech synthesis system, and the other augmentation is performed by adding random noise to the acoustic feature. Experimental results show that augmentations help improve the system's robustness. Moreover, by augmenting the training set with the synthetic data generated by the multi-speaker text-to-speech system, we achieve a significant improvement regarding confusing words scenario.

</details>

### [VAW-GAN for Disentanglement and Recomposition of Emotional Elements in Speech](2011.02314.md)
**Kun Zhou, Berrak Sisman, Haizhou Li** · 2020-11-03

<details>
<summary>Abstract</summary>

Emotional voice conversion (EVC) aims to convert the emotion of speech from one state to another while preserving the linguistic content and speaker identity. In this paper, we study the disentanglement and recomposition of emotional elements in speech through variational autoencoding Wasserstein generative adversarial network (VAW-GAN). We propose a speaker-dependent EVC framework based on VAW-GAN, that includes two VAW-GAN pipelines, one for spectrum conversion, and another for prosody conversion. We train a spectral encoder that disentangles emotion and prosody (F0) information from spectral features; we also train a prosodic encoder that disentangles emotion modulation of prosody (affective prosody) from linguistic prosody. At run-time, the decoder of spectral VAW-GAN is conditioned on the output of prosodic VAW-GAN. The vocoder takes the converted spectral and prosodic features to generate the target emotional speech. Experiments validate the effectiveness of our proposed method in both objective and subjective evaluations.

</details>

### [Learning to Maximize Speech Quality Directly Using MOS Prediction for Neural Text-to-Speech](2011.01174.md)
**Yeunju Choi, Youngmoon Jung, Youngjoo Suh, Hoirin Kim** · 2020-11-02

<details>
<summary>Abstract</summary>

Although recent neural text-to-speech (TTS) systems have achieved high-quality speech synthesis, there are cases where a TTS system generates low-quality speech, mainly caused by limited training data or information loss during knowledge distillation. Therefore, we propose a novel method to improve speech quality by training a TTS model under the supervision of perceptual loss, which measures the distance between the maximum possible speech quality score and the predicted one. We first pre-train a mean opinion score (MOS) prediction model and then train a TTS model to maximize the MOS of synthesized speech using the pre-trained MOS prediction model. The proposed method can be applied independently regardless of the TTS model architecture or the cause of speech quality degradation and efficiently without increasing the inference time or model complexity. The evaluation results for the MOS and phone error rate demonstrate that our proposed approach improves previous models in terms of both naturalness and intelligibility.

</details>

### [CAMP: a Two-Stage Approach to Modelling Prosody in Context](2011.01175.md)
**Zack Hodari, Alexis Moinet, Sri Karlapati, Jaime Lorenzo-Trueba et al.** · 2020-11-02

<details>
<summary>Abstract</summary>

Prosody is an integral part of communication, but remains an open problem in state-of-the-art speech synthesis. There are two major issues faced when modelling prosody: (1) prosody varies at a slower rate compared with other content in the acoustic signal (e.g. segmental information and background noise); (2) determining appropriate prosody without sufficient context is an ill-posed problem. In this paper, we propose solutions to both these issues. To mitigate the challenge of modelling a slow-varying signal, we learn to disentangle prosodic information using a word level representation. To alleviate the ill-posed nature of prosody modelling, we use syntactic and semantic information derived from text to learn a context-dependent prior over our prosodic space. Our Context-Aware Model of Prosody (CAMP) outperforms the state-of-the-art technique, closing the gap with natural speech by 26%. We also find that replacing attention with a jointly-trained duration model improves prosody significantly.

</details>

### [FeatherTTS: Robust and Efficient attention based Neural TTS](2011.00935.md)
**Qiao Tian, Zewang Zhang, Chao Liu, Heng Lu et al.** · 2020-11-02

<details>
<summary>Abstract</summary>

Attention based neural TTS is elegant speech synthesis pipeline and has shown a powerful ability to generate natural speech. However, it is still not robust enough to meet the stability requirements for industrial products. Besides, it suffers from slow inference speed owning to the autoregressive generation process. In this work, we propose FeatherTTS, a robust and efficient attention-based neural TTS system. Firstly, we propose a novel Gaussian attention which utilizes interpretability of Gaussian attention and the strict monotonic property in TTS. By this method, we replace the commonly used stop token prediction architecture with attentive stop prediction. Secondly, we apply block sparsity on the autoregressive decoder to speed up speech synthesis. The experimental results show that our proposed FeatherTTS not only nearly eliminates the problem of word skipping, repeating in particularly hard texts and keep the naturalness of generated speech, but also speeds up acoustic feature generation by 3.5 times over Tacotron. Overall, the proposed FeatherTTS can be $35$x faster than real-time on a single CPU.

</details>

### [CVC: Contrastive Learning for Non-parallel Voice Conversion](2011.00782.md)
**Tingle Li, Yichen Liu, Chenxu Hu, Hang Zhao** · 2020-11-02

<details>
<summary>Abstract</summary>

Cycle consistent generative adversarial network (CycleGAN) and variational autoencoder (VAE) based models have gained popularity in non-parallel voice conversion recently. However, they often suffer from difficult training process and unsatisfactory results. In this paper, we propose CVC, a contrastive learning-based adversarial approach for voice conversion. Compared to previous CycleGAN-based methods, CVC only requires an efficient one-way GAN training by taking the advantage of contrastive learning. When it comes to non-parallel one-to-one voice conversion, CVC is on par or better than CycleGAN and VAE while effectively reducing training time. CVC further demonstrates superior performance in many-to-one voice conversion, enabling the conversion from unseen speakers.

</details>

### [AGAIN-VC: A One-shot Voice Conversion using Activation Guidance and Adaptive Instance Normalization](2011.00316.md)
**Yen-Hao Chen, Da-Yi Wu, Tsung-Han Wu, Hung-yi Lee** · 2020-10-31

<details>
<summary>Abstract</summary>

Recently, voice conversion (VC) has been widely studied. Many VC systems use disentangle-based learning techniques to separate the speaker and the linguistic content information from a speech signal. Subsequently, they convert the voice by changing the speaker information to that of the target speaker. To prevent the speaker information from leaking into the content embeddings, previous works either reduce the dimension or quantize the content embedding as a strong information bottleneck. These mechanisms somehow hurt the synthesis quality. In this work, we propose AGAIN-VC, an innovative VC system using Activation Guidance and Adaptive Instance Normalization. AGAIN-VC is an auto-encoder-based model, comprising of a single encoder and a decoder. With a proper activation as an information bottleneck on content embeddings, the trade-off between the synthesis quality and the speaker similarity of the converted speech is improved drastically. This one-shot VC system obtains the best performance regardless of the subjective or objective evaluations.

</details>

### [DeviceTTS: A Small-Footprint, Fast, Stable Network for On-Device Text-to-Speech](2010.15311.md)
**Zhiying Huang, Hao Li, Ming Lei** · 2020-10-29

<details>
<summary>Abstract</summary>

With the number of smart devices increasing, the demand for on-device text-to-speech (TTS) increases rapidly. In recent years, many prominent End-to-End TTS methods have been proposed, and have greatly improved the quality of synthesized speech. However, to ensure the qualified speech, most TTS systems depend on large and complex neural network models, and it's hard to deploy these TTS systems on-device. In this paper, a small-footprint, fast, stable network for on-device TTS is proposed, named as DeviceTTS. DeviceTTS makes use of a duration predictor as a bridge between encoder and decoder so as to avoid the problem of words skipping and repeating in Tacotron. As we all know, model size is a key factor for on-device TTS. For DeviceTTS, Deep Feedforward Sequential Memory Network (DFSMN) is used as the basic component. Moreover, to speed up inference, mix-resolution decoder is proposed for balance the inference speed and speech quality. Experiences are done with WORLD and LPCNet vocoder. Finally, with only 1.4 million model parameters and 0.099 GFLOPS, DeviceTTS achieves comparable performance with Tacotron and FastSpeech. As far as we know, the DeviceTTS can meet the needs of most of the devices in practical application.

</details>

### [The IQIYI System for Voice Conversion Challenge 2020](2010.15317.md)
**Wendong Gan, Haitao Chen, Yin Yan, Jianwei Li et al.** · 2020-10-29

<details>
<summary>Abstract</summary>

This paper presents the IQIYI voice conversion system (T24) for Voice Conversion 2020. In the competition, each target speaker has 70 sentences. We have built an end-to-end voice conversion system based on PPG. First, the ASR acoustic model calculates the BN feature, which represents the content-related information in the speech. Then the Mel feature is calculated through an improved prosody tacotron model. Finally, the Mel spectrum is converted to wav through an improved LPCNet. The evaluation results show that this system can achieve better voice conversion effects. In the case of using 16k rather than 24k sampling rate audio, the conversion result is relatively good in naturalness and similarity. Among them, our best results are in the similarity evaluation of the Task 2, the 2nd in the ASV-based objective evaluation and the 5th in the subjective evaluation.

</details>

### [Speech Synthesis and Control Using Differentiable DSP](2010.15084.md)
**Giorgio Fabbro, Vladimir Golkov, Thomas Kemp, Daniel Cremers** · 2020-10-28

<details>
<summary>Abstract</summary>

Modern text-to-speech systems are able to produce natural and high-quality speech, but speech contains factors of variation (e.g. pitch, rhythm, loudness, timbre)\ that text alone cannot contain. In this work we move towards a speech synthesis system that can produce diverse speech renditions of a text by allowing (but not requiring) explicit control over the various factors of variation. We propose a new neural vocoder that offers control of such factors of variation. This is achieved by employing differentiable digital signal processing (DDSP) (previously used only for music rather than speech), which exposes these factors of variation. The results show that the proposed approach can produce natural speech with realistic timbre, and individual factors of variation can be freely controlled.

</details>

### [PPG-based singing voice conversion with adversarial representation learning](2010.14804.md)
**Zhonghao Li, Benlai Tang, Xiang Yin, Yuan Wan et al.** · 2020-10-28

<details>
<summary>Abstract</summary>

Singing voice conversion (SVC) aims to convert the voice of one singer to that of other singers while keeping the singing content and melody. On top of recent voice conversion works, we propose a novel model to steadily convert songs while keeping their naturalness and intonation. We build an end-to-end architecture, taking phonetic posteriorgrams (PPGs) as inputs and generating mel spectrograms. Specifically, we implement two separate encoders: one encodes PPGs as content, and the other compresses mel spectrograms to supply acoustic and musical information. To improve the performance on timbre and melody, an adversarial singer confusion module and a mel-regressive representation learning module are designed for the model. Objective and subjective experiments are conducted on our private Chinese singing corpus. Comparing with the baselines, our methods can significantly improve the conversion performance in terms of naturalness, melody, and voice similarity. Moreover, our PPG-based method is proved to be robust for noisy sources.

</details>

### [Seen and Unseen emotional style transfer for voice conversion with a new emotional speech dataset](2010.14794.md)
**Kun Zhou, Berrak Sisman, Rui Liu, Haizhou Li** · 2020-10-28

<details>
<summary>Abstract</summary>

Emotional voice conversion aims to transform emotional prosody in speech while preserving the linguistic content and speaker identity. Prior studies show that it is possible to disentangle emotional prosody using an encoder-decoder network conditioned on discrete representation, such as one-hot emotion labels. Such networks learn to remember a fixed set of emotional styles. In this paper, we propose a novel framework based on variational auto-encoding Wasserstein generative adversarial network (VAW-GAN), which makes use of a pre-trained speech emotion recognition (SER) model to transfer emotional style during training and at run-time inference. In this way, the network is able to transfer both seen and unseen emotional style to a new utterance. We show that the proposed framework achieves remarkable performance by consistently outperforming the baseline framework. This paper also marks the release of an emotional speech dataset (ESD) for voice conversion, which has multiple speakers and languages.

</details>

### [Parallel waveform synthesis based on generative adversarial networks with voicing-aware conditional discriminators](2010.14151.md)
**Ryuichi Yamamoto, Eunwoo Song, Min-Jae Hwang, Jae-Min Kim** · 2020-10-27

<details>
<summary>Abstract</summary>

This paper proposes voicing-aware conditional discriminators for Parallel WaveGAN-based waveform synthesis systems. In this framework, we adopt a projection-based conditioning method that can significantly improve the discriminator's performance. Furthermore, the conventional discriminator is separated into two waveform discriminators for modeling voiced and unvoiced speech. As each discriminator learns the distinctive characteristics of the harmonic and noise components, respectively, the adversarial training process becomes more efficient, allowing the generator to produce more realistic speech waveforms. Subjective test results demonstrate the superiority of the proposed method over the conventional Parallel WaveGAN and WaveNet systems. In particular, our speaker-independently trained model within a FastSpeech 2 based text-to-speech framework achieves the mean opinion scores of 4.20, 4.18, 4.21, and 4.31 for four Japanese speakers, respectively.

</details>

### [TTS-by-TTS: TTS-driven Data Augmentation for Fast and High-Quality Speech Synthesis](2010.13421.md)
**Min-Jae Hwang, Ryuichi Yamamoto, Eunwoo Song, Jae-Min Kim** · 2020-10-26

<details>
<summary>Abstract</summary>

In this paper, we propose a text-to-speech (TTS)-driven data augmentation method for improving the quality of a non-autoregressive (AR) TTS system. Recently proposed non-AR models, such as FastSpeech 2, have successfully achieved fast speech synthesis system. However, their quality is not satisfactory, especially when the amount of training data is insufficient. To address this problem, we propose an effective data augmentation method using a well-designed AR TTS system. In this method, large-scale synthetic corpora including text-waveform pairs with phoneme duration are generated by the AR TTS system and then used to train the target non-AR model. Perceptual listening test results showed that the proposed method significantly improved the quality of the non-AR TTS system. In particular, we augmented five hours of a training database to 179 hours of a synthetic one. Using these databases, our TTS system consisting of a FastSpeech 2 acoustic model with a Parallel WaveGAN vocoder achieved a mean opinion score of 3.74, which is 40% higher than that achieved by the conventional method.

</details>

### [Emotion controllable speech synthesis using emotion-unlabeled dataset with the assistance of cross-domain speech emotion recognition](2010.13350.md)
**Xiong Cai, Dongyang Dai, Zhiyong Wu, Xiang Li et al.** · 2020-10-26

<details>
<summary>Abstract</summary>

Neural text-to-speech (TTS) approaches generally require a huge number of high quality speech data, which makes it difficult to obtain such a dataset with extra emotion labels. In this paper, we propose a novel approach for emotional TTS synthesis on a TTS dataset without emotion labels. Specifically, our proposed method consists of a cross-domain speech emotion recognition (SER) model and an emotional TTS model. Firstly, we train the cross-domain SER model on both SER and TTS datasets. Then, we use emotion labels on the TTS dataset predicted by the trained SER model to build an auxiliary SER task and jointly train it with the TTS model. Experimental results show that our proposed method can generate speech with the specified emotional expressiveness and nearly no hindering on the speech quality.

</details>

### [Dynamic Soft Windowing and Language Dependent Style Token for Code-Switching End-to-End Speech Synthesis](s2:a80deca1ff9d0a7940afdcdb69789a1c34441223.md)
**Ruibo Fu, J. Tao, Zhengqi Wen, Jiangyan Yi et al.** · 2020-10-25

<details>
<summary>Abstract</summary>

Most of current end-to-end speech synthesis assumes the input text is in a single language situation. However, code-switching in speech occurs frequently in routine life, in which speakers switch between languages in the same utterance. And building a large mixed-language speech database is difﬁcult and uneconomical. In this paper, both windowing technique and style token modeling are designed for the code-switching end-to-end speech synthesis. To improve the consistency of speaking style in bilingual situation, compared with the conventional windowing techniques that used ﬁxed constraints, the dynamic attention reweighting soft windowing mechanism is proposed to ensure the smooth transition of code-switching. To compensate the shortage of mixed-language training data, the language dependent style token is designed for the cross-language multi-speaker acoustic modeling, where both the Mandarin and English monolingual data are the extended training data set. The attention gating is proposed to adjust style token dynamically based on the language and the attended context infromation. Experimental results show that proposed methods lead to an improvement on intelligibility, naturalness and similarity.

</details>

### [Testing the Limits of Representation Mixing for Pronunciation Correction in End-to-End Speech Synthesis](s2:8a76e11c81b8e1c6dd246bf4b71840558a125687.md)
**Jason Fong, Jason Taylor, Simon King** · 2020-10-25

<details>
<summary>Abstract</summary>

Accurate pronunciation is an essential requirement for text-to-speech (TTS) systems. Systems trained on raw text exhibit pronunciation errors in output speech due to ambiguous letter-to-sound relations. Without an intermediate phonemic representation, it is difﬁcult to intervene and correct these errors. Re-taining explicit control over pronunciation runs counter to the current drive toward end-to-end (E2E) TTS using sequence-to-sequence models. On the one hand, E2E TTS aims to eliminate manual intervention, especially expert skill such as phonemic transcription of words in a lexicon. On the other, a system making difﬁcult-to-correct pronunciation errors is of little practical use. Some intervention is necessary. We explore the minimal amount of linguistic features required to correct pronunciation errors in an otherwise E2E TTS system that accepts graphemic input. We use representation-mixing: within each sequence the system accepts either graphemic and/or phonemic input. We quantify how little training data needs to be phonemically labelled - that is, how small a lexicon must be written - to ensure control over pronunciation. We ﬁnd modest correction is possible with 500 phonemised word types from the LJ speech dataset but correction works best when the majority of word types are phonemised with syllable boundaries.

</details>

### [Dynamic Speaker Representations Adjustment and Decoder Factorization for Speaker Adaptation in End-to-End Speech Synthesis](s2:f8c325dbe6b8377c77093d5914ba9438e09abc23.md)
**Ruibo Fu, J. Tao, Zhengqi Wen, Jiangyan Yi et al.** · 2020-10-25

<details>
<summary>Abstract</summary>

End-to-end speech synthesis can reach high quality and naturalness with low-resource adaptation data. However, the generalization of out-domain texts and the improving modeling accuracy of speaker representations are still challenging tasks. The limited adaptation data leads to unacceptable errors and low similarity of the synthetic speech. In this paper, both speaker representations modeling and acoustic model structure are improved for the speaker adaptation task. On the one hand, compared with the conventional methods that focused on using ﬁxed global speaker representations, the attention gating is proposed to adjust speaker representations dynamically based on the attended context and prosody information, which can describe more pronunciation characteristics in phoneme level. On the other hand, to improve the robustness and avoid over-ﬁtting, the decoder model is factored into average-net and adaptation-net, which are designed for learning speaker independent acoustic features and target speaker timbre imitation respectively. And the context discriminator is pre-trained by large ASR data to supervise the average-net generating proper speaker independent acoustic features for different phoneme. Experimental results on Mandarin dataset show that proposed methods lead to an improvement on intelligibility, naturalness and similarity.

</details>

### [End-to-End Text-to-Speech Synthesis with Unaligned Multiple Language Units Based on Attention](s2:ded7f8b91ab3d339c70138dd555c2a810e277649.md)
**Masashi Aso, Shinnosuke Takamichi, H. Saruwatari** · 2020-10-25

<details>
<summary>Abstract</summary>

This paper presents the use of unaligned multiple language units for end-to-end text-to-speech (TTS). End-to-end TTS is a promising technology in that it does not require intermediate representation such as prosodic contexts. However, it causes mispronunciation and unnatural prosody. To alleviate this problem, previous methods have used multiple language units, e.g., phonemes and characters, but required the units to be hard-aligned. In this paper, we propose a multi-input attention structure that simultaneously accepts multiple language units without alignments among them. We consider using not only traditional phonemes and characters but also subwords tokenized in a language-independent manner. We also propose a progressive training strategy to deal with the unaligned multiple language units. The experimental results demonstrated that our model and training strategy improve speech quality.

</details>

### [GraphSpeech: Syntax-Aware Graph Attention Network For Neural Speech Synthesis](2010.12423.md)
**Rui Liu, Berrak Sisman, Haizhou Li** · 2020-10-23

<details>
<summary>Abstract</summary>

Attention-based end-to-end text-to-speech synthesis (TTS) is superior to conventional statistical methods in many ways. Transformer-based TTS is one of such successful implementations. While Transformer TTS models the speech frame sequence well with a self-attention mechanism, it does not associate input text with output utterances from a syntactic point of view at sentence level. We propose a novel neural TTS model, denoted as GraphSpeech, that is formulated under graph neural network framework. GraphSpeech encodes explicitly the syntactic relation of input lexical tokens in a sentence, and incorporates such information to derive syntactically motivated character embeddings for TTS attention mechanism. Experiments show that GraphSpeech consistently outperforms the Transformer TTS baseline in terms of spectrum and prosody rendering of utterances.

</details>

### [Any-to-One Sequence-to-Sequence Voice Conversion using Self-Supervised Discrete Speech Representations](2010.12231.md)
**Wen-Chin Huang, Yi-Chiao Wu, Tomoki Hayashi, Tomoki Toda** · 2020-10-23

<details>
<summary>Abstract</summary>

We present a novel approach to any-to-one (A2O) voice conversion (VC) in a sequence-to-sequence (seq2seq) framework. A2O VC aims to convert any speaker, including those unseen during training, to a fixed target speaker. We utilize vq-wav2vec (VQW2V), a discretized self-supervised speech representation that was learned from massive unlabeled data, which is assumed to be speaker-independent and well corresponds to underlying linguistic contents. Given a training dataset of the target speaker, we extract VQW2V and acoustic features to estimate a seq2seq mapping function from the former to the latter. With the help of a pretraining method and a newly designed postprocessing technique, our model can be generalized to only 5 min of data, even outperforming the same model trained with parallel data.

</details>

### [The NTU-AISG Text-to-speech System for Blizzard Challenge 2020](2010.11489.md)
**Haobo Zhang, Tingzhi Mao, Haihua Xu, Hao Huang** · 2020-10-22

<details>
<summary>Abstract</summary>

We report our NTU-AISG Text-to-speech (TTS) entry systems for the Blizzard Challenge 2020 in this paper. There are two TTS tasks in this year's challenge, one is a Mandarin TTS task, the other is a Shanghai dialect TTS task. We have participated both. One of the main challenges is to build TTS systems with low-resource constraints, particularly for the case of Shanghai dialect, of which about three hours data are available to participants. To overcome the constraint, we adopt an average-speaker modeling method. That is, we first employ external Mandarin data to train both End-to-end acoustic model and WaveNet vocoder, then we use Shanghai dialect to tune the acoustic model and WaveNet vocoder respectively. Apart from this, we have no Shanghai dialect lexicon despite syllable transcripts are provided for the training data. Since we are not sure if similar syllable transcripts are provided for the evaluation data during the training stage, we use Mandarin lexicon for Shanghai dialect instead. With the letter, as decomposed from the corresponding Mandarin syllable, as input, though the naturalness and original speaker similarity of the synthesized speech are good, subjective evaluation results indicate the intelligibility of the synthesized speech is deeply undermined for the Shanghai dialect TTS system.

</details>

### [Parallel Tacotron: Non-Autoregressive and Controllable TTS](2010.11439.md)
**Isaac Elias, Heiga Zen, Jonathan Shen, Yu Zhang et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

Although neural end-to-end text-to-speech models can synthesize highly natural speech, there is still room for improvements to its efficiency and naturalness. This paper proposes a non-autoregressive neural text-to-speech model augmented with a variational autoencoder-based residual encoder. This model, called \emph{Parallel Tacotron}, is highly parallelizable during both training and inference, allowing efficient synthesis on modern parallel hardware. The use of the variational autoencoder relaxes the one-to-many mapping nature of the text-to-speech problem and improves naturalness. To further improve the naturalness, we use lightweight convolutions, which can efficiently capture local contexts, and introduce an iterative spectrogram loss inspired by iterative refinement. Experimental results show that Parallel Tacotron matches a strong autoregressive baseline in subjective evaluations with significantly decreased inference time.

</details>

### [NU-GAN: High resolution neural upsampling with GAN](2010.11362.md)
**Rithesh Kumar, Kundan Kumar, Vicki Anand, Yoshua Bengio et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

In this paper, we propose NU-GAN, a new method for resampling audio from lower to higher sampling rates (upsampling). Audio upsampling is an important problem since productionizing generative speech technology requires operating at high sampling rates. Such applications use audio at a resolution of 44.1 kHz or 48 kHz, whereas current speech synthesis methods are equipped to handle a maximum of 24 kHz resolution. NU-GAN takes a leap towards solving audio upsampling as a separate component in the text-to-speech (TTS) pipeline by leveraging techniques for audio generation using GANs. ABX preference tests indicate that our NU-GAN resampler is capable of resampling 22 kHz to 44.1 kHz audio that is distinguishable from original audio only 7.4% higher than random chance for single speaker dataset, and 10.8% higher than chance for multi-speaker dataset.

</details>

### [CycleGAN-VC3: Examining and Improving CycleGAN-VCs for Mel-spectrogram Conversion](2010.11672.md)
**Takuhiro Kaneko, Hirokazu Kameoka, Kou Tanaka, Nobukatsu Hojo** · 2020-10-22

<details>
<summary>Abstract</summary>

Non-parallel voice conversion (VC) is a technique for learning mappings between source and target speeches without using a parallel corpus. Recently, cycle-consistent adversarial network (CycleGAN)-VC and CycleGAN-VC2 have shown promising results regarding this problem and have been widely used as benchmark methods. However, owing to the ambiguity of the effectiveness of CycleGAN-VC/VC2 for mel-spectrogram conversion, they are typically used for mel-cepstrum conversion even when comparative methods employ mel-spectrogram as a conversion target. To address this, we examined the applicability of CycleGAN-VC/VC2 to mel-spectrogram conversion. Through initial experiments, we discovered that their direct applications compromised the time-frequency structure that should be preserved during conversion. To remedy this, we propose CycleGAN-VC3, an improvement of CycleGAN-VC2 that incorporates time-frequency adaptive normalization (TFAN). Using TFAN, we can adjust the scale and bias of the converted features while reflecting the time-frequency structure of the source mel-spectrogram. We evaluated CycleGAN-VC3 on inter-gender and intra-gender non-parallel VC. A subjective evaluation of naturalness and similarity showed that for every VC pair, CycleGAN-VC3 outperforms or is competitive with the two types of CycleGAN-VC2, one of which was applied to mel-cepstrum and the other to mel-spectrogram. Audio samples are available at http://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/cyclegan-vc3/index.html.

</details>

### [Towards Low-Resource StarGAN Voice Conversion using Weight Adaptive Instance Normalization](2010.11646.md)
**Mingjie Chen, Yanpei Shi, Thomas Hain** · 2020-10-22

<details>
<summary>Abstract</summary>

Many-to-many voice conversion with non-parallel training data has seen significant progress in recent years. StarGAN-based models have been interests of voice conversion. However, most of the StarGAN-based methods only focused on voice conversion experiments for the situations where the number of speakers was small, and the amount of training data was large. In this work, we aim at improving the data efficiency of the model and achieving a many-to-many non-parallel StarGAN-based voice conversion for a relatively large number of speakers with limited training samples. In order to improve data efficiency, the proposed model uses a speaker encoder for extracting speaker embeddings and conducts adaptive instance normalization (AdaIN) on convolutional weights. Experiments are conducted with 109 speakers under two low-resource situations, where the number of training samples is 20 and 5 per speaker. An objective evaluation shows the proposed model is better than the baseline methods. Furthermore, a subjective evaluation shows that, for both naturalness and similarity, the proposed model outperforms the baseline method.

</details>

### [A Graph-Based Framework for Structured Prediction Tasks in Sanskrit](s2:8e37861fa514cf9cc74481f6fbb078b1ef78baf6.md)
**Amrith Krishna, Ashim Gupta, Pawan Goyal, Bishal Santra et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

Abstract We propose a framework using energy-based models for multiple structured prediction tasks in Sanskrit. Ours is an arc-factored model, similar to the graph-based parsing approaches, and we consider the tasks of word segmentation, morphological parsing, dependency parsing, syntactic linearization, and prosodification, a “prosody-level” task we introduce in this work. Ours is a search-based structured prediction framework, which expects a graph as input, where relevant linguistic information is encoded in the nodes, and the edges are then used to indicate the association between these nodes. Typically, the state-of-the-art models for morphosyntactic tasks in morphologically rich languages still rely on hand-crafted features for their performance. But here, we automate the learning of the feature function. The feature function so learned, along with the search space we construct, encode relevant linguistic information for the tasks we consider. This enables us to substantially reduce the training data requirements to as low as 10%, as compared to the data requirements for the neural state-of-the-art models. Our experiments in Czech and Sanskrit show the language-agnostic nature of the framework, where we train highly competitive models for both the languages. Moreover, our framework enables us to incorporate language-specific constraints to prune the search space and to filter the candidates during inference. We obtain significant improvements in morphosyntactic tasks for Sanskrit by incorporating language-specific constraints into the model. In all the tasks we discuss for Sanskrit, we either achieve state-of-the-art results or ours is the only data-driven solution for those tasks.

</details>

### [An Investigation of the Relation Between Grapheme Embeddings and Pronunciation for Tacotron-based Systems](2010.10694.md)
**Antoine Perquin, Erica Cooper, Junichi Yamagishi** · 2020-10-21

<details>
<summary>Abstract</summary>

End-to-end models, particularly Tacotron-based ones, are currently a popular solution for text-to-speech synthesis. They allow the production of high-quality synthesized speech with little to no text preprocessing. Indeed, they can be trained using either graphemes or phonemes as input directly. However, in the case of grapheme inputs, little is known concerning the relation between the underlying representations learned by the model and word pronunciations. This work investigates this relation in the case of a Tacotron model trained on French graphemes. Our analysis shows that grapheme embeddings are related to phoneme information despite no such information being present during training. Thanks to this property, we show that grapheme embeddings learned by Tacotron models can be useful for tasks such as grapheme-to-phoneme conversion and control of the pronunciation in synthetic speech.

</details>

### [Learning Disentangled Phone and Speaker Representations in a Semi-Supervised VQ-VAE Paradigm](2010.10727.md)
**Jennifer Williams, Yi Zhao, Erica Cooper, Junichi Yamagishi** · 2020-10-21

<details>
<summary>Abstract</summary>

We present a new approach to disentangle speaker voice and phone content by introducing new components to the VQ-VAE architecture for speech synthesis. The original VQ-VAE does not generalize well to unseen speakers or content. To alleviate this problem, we have incorporated a speaker encoder and speaker VQ codebook that learns global speaker characteristics entirely separate from the existing sub-phone codebooks. We also compare two training methods: self-supervised with global conditions and semi-supervised with speaker labels. Adding a speaker VQ component improves objective measures of speech synthesis quality (estimated MOS, speaker similarity, ASR-based intelligibility) and provides learned representations that are meaningful. Our speaker VQ codebook indices can be used in a simple speaker diarization task and perform slightly better than an x-vector baseline. Additionally, phones can be recognized from sub-phone VQ codebook indices in our semi-supervised VQ-VAE better than self-supervised with global conditions.

</details>

### [End-to-End Text-to-Speech using Latent Duration based on VQ-VAE](2010.09602.md)
**Yusuke Yasuda, Xin Wang, Junichi Yamagishi** · 2020-10-19

<details>
<summary>Abstract</summary>

Explicit duration modeling is a key to achieving robust and efficient alignment in text-to-speech synthesis (TTS). We propose a new TTS framework using explicit duration modeling that incorporates duration as a discrete latent variable to TTS and enables joint optimization of whole modules from scratch. We formulate our method based on conditional VQ-VAE to handle discrete duration in a variational autoencoder and provide a theoretical explanation to justify our method. In our framework, a connectionist temporal classification (CTC) -based force aligner acts as the approximate posterior, and text-to-duration works as the prior in the variational autoencoder. We evaluated our proposed method with a listening test and compared it with other TTS methods based on soft-attention or explicit duration modeling. The results showed that our systems rated between soft-attention-based methods (Transformer-TTS, Tacotron2) and explicit duration modeling-based methods (Fastspeech).

</details>

### [Towards Natural Bilingual and Code-Switched Speech Synthesis Based on Mix of Monolingual Recordings and Cross-Lingual Voice Conversion](2010.08136.md)
**Shengkui Zhao, Trung Hieu Nguyen, Hao Wang, Bin Ma** · 2020-10-16

<details>
<summary>Abstract</summary>

Recent state-of-the-art neural text-to-speech (TTS) synthesis models have dramatically improved intelligibility and naturalness of generated speech from text. However, building a good bilingual or code-switched TTS for a particular voice is still a challenge. The main reason is that it is not easy to obtain a bilingual corpus from a speaker who achieves native-level fluency in both languages. In this paper, we explore the use of Mandarin speech recordings from a Mandarin speaker, and English speech recordings from another English speaker to build high-quality bilingual and code-switched TTS for both speakers. A Tacotron2-based cross-lingual voice conversion system is employed to generate the Mandarin speaker's English speech and the English speaker's Mandarin speech, which show good naturalness and speaker similarity. The obtained bilingual data are then augmented with code-switched utterances synthesized using a Transformer model. With these data, three neural TTS models -- Tacotron2, Transformer and FastSpeech are applied for building bilingual and code-switched TTS. Subjective evaluation results show that all the three systems can produce (near-)native-level speech in both languages for each of the speaker.

</details>

### [Chinese Speech Synthesis System Based on End to End](s2:734f04fe481a547cb56dce8d6b3c6aa2e24aa3cc.md)
**Hao Zhang, Xiaojun Huang** · 2020-10-16

<details>
<summary>Abstract</summary>

This paper describes an end-to-end Chinese speech synthesis scheme, a neural network architecture for speech synthesis directly from text, which is based on the improvement of tacotron2. In order to improve the original seq2seq model, multi attention mechanism is used to replace the original position-based attention mechanism to improve the sound quality of synthetic speech. The prosodic style coding module is added to better show the prosodic and stylistic characteristics of the synthesized speech. Then an LpcNet vocoder is used to replace the original WaveNet to generate time-domain waveform, which improves the synthesis efficiency and reduces the synthesis time. The experiments show that the speech synthesis system is effective and timely. The synthesized speech is natural and has good prosodic style.

</details>

### [The NeteaseGames System for Voice Conversion Challenge 2020 with Vector-quantization Variational Autoencoder and WaveNet](2010.07630.md)
**Haitong Zhang** · 2020-10-15

<details>
<summary>Abstract</summary>

This paper presents the description of our submitted system for Voice Conversion Challenge (VCC) 2020 with vector-quantization variational autoencoder (VQ-VAE) with WaveNet as the decoder, i.e., VQ-VAE-WaveNet. VQ-VAE-WaveNet is a nonparallel VAE-based voice conversion that reconstructs the acoustic features along with separating the linguistic information with speaker identity. The model is further improved with the WaveNet cycle as the decoder to generate the high-quality speech waveform, since WaveNet, as an autoregressive neural vocoder, has achieved the SoTA result of waveform generation. In practice, our system can be developed with VCC 2020 dataset for both Task 1 (intra-lingual) and Task 2 (cross-lingual). However, we only submit our system for the intra-lingual voice conversion task. The results of VCC 2020 demonstrate that our system VQ-VAE-WaveNet achieves: 3.04 mean opinion score (MOS) in naturalness and a 3.28 average score in similarity ( the speaker similarity percentage (Sim) of 75.99%) for Task 1. The subjective evaluations also reveal that our system gives top performance when no supervised learning is involved. What's more, our system performs well in some objective evaluations. Specifically, our system achieves an average score of 3.95 in naturalness in automatic naturalness prediction and ranked the 6th and 8th, respectively in ASV-based speaker similarity and spoofing countermeasures.

</details>

### [The Zero Resource Speech Challenge 2020: Discovering discrete subword and word units](2010.05967.md)
**Ewan Dunbar, Julien Karadayi, Mathieu Bernard, Xuan-Nga Cao et al.** · 2020-10-12

<details>
<summary>Abstract</summary>

We present the Zero Resource Speech Challenge 2020, which aims at learning speech representations from raw audio signals without any labels. It combines the data sets and metrics from two previous benchmarks (2017 and 2019) and features two tasks which tap into two levels of speech representation. The first task is to discover low bit-rate subword representations that optimize the quality of speech synthesis; the second one is to discover word-like units from unsegmented raw speech. We present the results of the twenty submitted models and discuss the implications of the main findings for unsupervised speech learning.

</details>

### [HiFi-GAN: Generative Adversarial Networks for Efficient and High Fidelity Speech Synthesis](2010.05646.md)
**Jungil Kong, Jaehyeon Kim, Jaekyoung Bae** · 2020-10-12

<details>
<summary>Abstract</summary>

Several recent work on speech synthesis have employed generative adversarial networks (GANs) to produce raw waveforms. Although such methods improve the sampling efficiency and memory usage, their sample quality has not yet reached that of autoregressive and flow-based generative models. In this work, we propose HiFi-GAN, which achieves both efficient and high-fidelity speech synthesis. As speech audio consists of sinusoidal signals with various periods, we demonstrate that modeling periodic patterns of an audio is crucial for enhancing sample quality. A subjective human evaluation (mean opinion score, MOS) of a single speaker dataset indicates that our proposed method demonstrates similarity to human quality while generating 22.05 kHz high-fidelity audio 167.9 times faster than real-time on a single V100 GPU. We further show the generality of HiFi-GAN to the mel-spectrogram inversion of unseen speakers and end-to-end speech synthesis. Finally, a small footprint version of HiFi-GAN generates samples 13.4 times faster than real-time on CPU with comparable quality to an autoregressive counterpart.

</details>

### [The NU Voice Conversion System for the Voice Conversion Challenge 2020: On the Effectiveness of Sequence-to-sequence Models and Autoregressive Neural Vocoders](2010.04446.md)
**Wen-Chin Huang, Patrick Lumban Tobing, Yi-Chiao Wu, Kazuhiro Kobayashi et al.** · 2020-10-09

<details>
<summary>Abstract</summary>

In this paper, we present the voice conversion (VC) systems developed at Nagoya University (NU) for the Voice Conversion Challenge 2020 (VCC2020). We aim to determine the effectiveness of two recent significant technologies in VC: sequence-to-sequence (seq2seq) models and autoregressive (AR) neural vocoders. Two respective systems were developed for the two tasks in the challenge: for task 1, we adopted the Voice Transformer Network, a Transformer-based seq2seq VC model, and extended it with synthetic parallel data to tackle nonparallel data; for task 2, we used the frame-based cyclic variational autoencoder (CycleVAE) to model the spectral features of a speech waveform and the AR WaveNet vocoder with additional fine-tuning. By comparing with the baseline systems, we confirmed that the seq2seq modeling can improve the conversion similarity and that the use of AR vocoders can improve the naturalness of the converted speech.

</details>

### [Baseline System of Voice Conversion Challenge 2020 with Cyclic Variational Autoencoder and Parallel WaveGAN](2010.04429.md)
**Patrick Lumban Tobing, Yi-Chiao Wu, Tomoki Toda** · 2020-10-09

<details>
<summary>Abstract</summary>

In this paper, we present a description of the baseline system of Voice Conversion Challenge (VCC) 2020 with a cyclic variational autoencoder (CycleVAE) and Parallel WaveGAN (PWG), i.e., CycleVAEPWG. CycleVAE is a nonparallel VAE-based voice conversion that utilizes converted acoustic features to consider cyclically reconstructed spectra during optimization. On the other hand, PWG is a non-autoregressive neural vocoder that is based on a generative adversarial network for a high-quality and fast waveform generator. In practice, the CycleVAEPWG system can be straightforwardly developed with the VCC 2020 dataset using a unified model for both Task 1 (intralingual) and Task 2 (cross-lingual), where our open-source implementation is available at https://github.com/bigpon/vcc20_baseline_cyclevae. The results of VCC 2020 have demonstrated that the CycleVAEPWG baseline achieves the following: 1) a mean opinion score (MOS) of 2.87 in naturalness and a speaker similarity percentage (Sim) of 75.37% for Task 1, and 2) a MOS of 2.56 and a Sim of 56.46% for Task 2, showing an approximately or nearly average score for naturalness and an above average score for speaker similarity.

</details>

### [Leveraging Unpaired Text Data for Training End-to-End Speech-to-Intent Systems](2010.04284.md)
**Yinghui Huang, Hong-Kwang Kuo, Samuel Thomas, Zvi Kons et al.** · 2020-10-08

<details>
<summary>Abstract</summary>

Training an end-to-end (E2E) neural network speech-to-intent (S2I) system that directly extracts intents from speech requires large amounts of intent-labeled speech data, which is time consuming and expensive to collect. Initializing the S2I model with an ASR model trained on copious speech data can alleviate data sparsity. In this paper, we attempt to leverage NLU text resources. We implemented a CTC-based S2I system that matches the performance of a state-of-the-art, traditional cascaded SLU system. We performed controlled experiments with varying amounts of speech and text training data. When only a tenth of the original data is available, intent classification accuracy degrades by 7.6% absolute. Assuming we have additional text-to-intent data (without speech) available, we investigated two techniques to improve the S2I system: (1) transfer learning, in which acoustic embeddings for intent classification are tied to fine-tuned BERT text embeddings; and (2) data augmentation, in which the text-to-intent data is converted into speech-to-intent data using a multi-speaker text-to-speech system. The proposed approaches recover 80% of performance lost due to using limited intent-labeled speech.

</details>

### [Latent linguistic embedding for cross-lingual text-to-speech and voice conversion](2010.03717.md)
**Hieu-Thi Luong, Junichi Yamagishi** · 2020-10-08

<details>
<summary>Abstract</summary>

As the recently proposed voice cloning system, NAUTILUS, is capable of cloning unseen voices using untranscribed speech, we investigate the feasibility of using it to develop a unified cross-lingual TTS/VC system. Cross-lingual speech generation is the scenario in which speech utterances are generated with the voices of target speakers in a language not spoken by them originally. This type of system is not simply cloning the voice of the target speaker, but essentially creating a new voice that can be considered better than the original under a specific framing. By using a well-trained English latent linguistic embedding to create a cross-lingual TTS and VC system for several German, Finnish, and Mandarin speakers included in the Voice Conversion Challenge 2020, we show that our method not only creates cross-lingual VC with high speaker similarity but also can be seamlessly used for cross-lingual TTS without having to perform any extra steps. However, the subjective evaluations of perceived naturalness seemed to vary between target speakers, which is one aspect for future improvement.

</details>

### [FastVC: Fast Voice Conversion with non-parallel data](2010.04185.md)
**Oriol Barbany Mayor, Milos Cernak** · 2020-10-08

<details>
<summary>Abstract</summary>

This paper introduces FastVC, an end-to-end model for fast Voice Conversion (VC). The proposed model can convert speech of arbitrary length from multiple source speakers to multiple target speakers. FastVC is based on a conditional AutoEncoder (AE) trained on non-parallel data and requires no annotations at all. This model's latent representation is shown to be speaker-independent and similar to phonemes, which is a desirable feature for VC systems. While the current VC systems primarily focus on achieving the highest overall speech quality, this paper tries to balance the development concerning resources needed to run the systems. Despite the simple structure of the proposed model, it outperforms the VC Challenge 2020 baselines on the cross-lingual task in terms of naturalness.

</details>

### [Neural Speech Synthesis for Estonian](2010.02636.md)
**Liisa Rätsep, Liisi Piits, Hille Pajupuu, Indrek Hein et al.** · 2020-10-06

<details>
<summary>Abstract</summary>

This technical report describes the results of a collaboration between the NLP research group at the University of Tartu and the Institute of Estonian Language on improving neural speech synthesis for Estonian. The report (written in Estonian) describes the project results, the summary of which is: (1) Speech synthesis data from 6 speakers for a total of 92.4 hours is collected and openly released (CC-BY-4.0). Data available at https://konekorpus.tartunlp.ai and https://www.eki.ee/litsents/. (2) software and models for neural speech synthesis is released open-source (MIT license). Available at https://koodivaramu.eesti.ee/tartunlp/text-to-speech . (3) We ran evaluations of the new models and compared them to other existing solutions (HMM-based HTS models from EKI, http://www.eki.ee/heli/, and Google's speech synthesis for Estonian, accessed via https://translate.google.com). Evaluation includes voice acceptability MOS scores for sentence-level and longer excerpts, detailed error analysis and evaluation of the pre-processing module.

</details>

### [Digital Voicing of Silent Speech](2010.02960.md)
**David Gaddy, Dan Klein** · 2020-10-06

<details>
<summary>Abstract</summary>

In this paper, we consider the task of digitally voicing silent speech, where silently mouthed words are converted to audible speech based on electromyography (EMG) sensor measurements that capture muscle impulses. While prior work has focused on training speech synthesis models from EMG collected during vocalized speech, we are the first to train from EMG collected during silently articulated speech. We introduce a method of training on silent EMG by transferring audio targets from vocalized to silent signals. Our method greatly improves intelligibility of audio generated from silent EMG compared to a baseline that only trains with vocalized data, decreasing transcription word error rate from 64% to 4% in one data condition and 88% to 68% in another. To spur further development on this task, we share our new dataset of silent and vocalized facial EMG measurements.

</details>

### [VoiceGrad: Non-Parallel Any-to-Many Voice Conversion with Annealed Langevin Dynamics](2010.02977.md)
**Hirokazu Kameoka, Takuhiro Kaneko, Kou Tanaka, Nobukatsu Hojo et al.** · 2020-10-06

<details>
<summary>Abstract</summary>

In this paper, we propose a non-parallel any-to-many voice conversion (VC) method termed VoiceGrad. Inspired by WaveGrad, a recently introduced novel waveform generation method, VoiceGrad is based upon the concepts of score matching and Langevin dynamics. It uses weighted denoising score matching to train a score approximator, a fully convolutional network with a U-Net structure designed to predict the gradient of the log density of the speech feature sequences of multiple speakers, and performs VC by using annealed Langevin dynamics to iteratively update an input feature sequence towards the nearest stationary point of the target distribution based on the trained score approximator network. Thanks to the nature of this concept, VoiceGrad enables any-to-many VC, a VC scenario in which the speaker of input speech can be arbitrary, and allows for non-parallel training, which requires no parallel utterances or transcriptions.

</details>

### [The Academia Sinica Systems of Voice Conversion for VCC2020](2010.02669.md)
**Yu-Huai Peng, Cheng-Hung Hu, Alexander Kang, Hung-Shin Lee et al.** · 2020-10-06

<details>
<summary>Abstract</summary>

This paper describes the Academia Sinica systems for the two tasks of Voice Conversion Challenge 2020, namely voice conversion within the same language (Task 1) and cross-lingual voice conversion (Task 2). For both tasks, we followed the cascaded ASR+TTS structure, using phonetic tokens as the TTS input instead of the text or characters. For Task 1, we used the international phonetic alphabet (IPA) as the input of the TTS model. For Task 2, we used unsupervised phonetic symbols extracted by the vector-quantized variational autoencoder (VQVAE). In the evaluation, the listening test showed that our systems performed well in the VCC2020 challenge.

</details>

### [JSSS: free Japanese speech corpus for summarization and simplification](2010.01793.md)
**Shinnosuke Takamichi, Mamoru Komachi, Naoko Tanji, Hiroshi Saruwatari** · 2020-10-05

<details>
<summary>Abstract</summary>

In this paper, we construct a new Japanese speech corpus for speech-based summarization and simplification, "JSSS" (pronounced "j-triple-s"). Given the success of reading-style speech synthesis from short-form sentences, we aim to design more difficult tasks for delivering information to humans. Our corpus contains voices recorded for two tasks that have a role in providing information under constraints: duration-constrained text-to-speech summarization and speaking-style simplification. It also contains utterances of long-form sentences as an optional task. This paper describes how we designed the corpus, which is available on our project page.

</details>

### [On End-to-End Chinese Speech Synthesis Based on World-Tacotron](s2:0b03c8c06005d5c69c1eb89808de0d6942b7129f.md)
**Diaohan Luo, Shutao Sun** · 2020-10-01

<details>
<summary>Abstract</summary>

In recent years, there have been many attempts at Chinese speech synthesis with Tacotron, an end-to-end speech synthesis model. However, Tacotron adopts Griffin-Lim algorithm which requires acoustic features with high dimensionality and synthesizes speech with low quality. Google launched Tacotron 2 which adopted WaveNet instead of Griffin-Lim and greatly enhanced the quality of speech synthesis, however, WaveNet should be trained with mass data and has slow synthesis speed. With regard to the above-mentioned issues, we propose World-Tacotron, which combines World vocoder with the Tacotron model optimized by Tacotron 2. Our scheme reduces the dimensionality of original Tacotron by 98% (from 2129 to 38) while improving the synthesis quality. In addition, the articulation at the end of the speech synthesized by World-Tacotron is incomplete. Therefore, the paper optimizes the articulation by deleting the trim in preprocessing, which however will result in a longer convergence period.

</details>

### [Transfer Learning from Speech Synthesis to Voice Conversion with Non-Parallel Training Data](2009.14399.md)
**Mingyang Zhang, Yi Zhou, Li Zhao, Haizhou Li** · 2020-09-30

<details>
<summary>Abstract</summary>

This paper presents a novel framework to build a voice conversion (VC) system by learning from a text-to-speech (TTS) synthesis system, that is called TTS-VC transfer learning. We first develop a multi-speaker speech synthesis system with sequence-to-sequence encoder-decoder architecture, where the encoder extracts robust linguistic representations of text, and the decoder, conditioned on target speaker embedding, takes the context vectors and the attention recurrent network cell output to generate target acoustic features. We take advantage of the fact that TTS system maps input text to speaker independent context vectors, and reuse such a mapping to supervise the training of latent representations of an encoder-decoder voice conversion system. In the voice conversion system, the encoder takes speech instead of text as input, while the decoder is functionally similar to TTS decoder. As we condition the decoder on speaker embedding, the system can be trained on non-parallel data for any-to-any voice conversion. During voice conversion training, we present both text and speech to speech synthesis and voice conversion networks respectively. At run-time, the voice conversion network uses its own encoder-decoder architecture. Experiments show that the proposed approach outperforms two competitive voice conversion baselines consistently, namely phonetic posteriorgram and variational autoencoder methods, in terms of speech quality, naturalness, and speaker similarity.

</details>

### [Transfer Learning from Monolingual ASR to Transcription-free Cross-lingual Voice Conversion](2009.14668.md)
**Che-Jui Chang** · 2020-09-30

<details>
<summary>Abstract</summary>

Cross-lingual voice conversion (VC) is a task that aims to synthesize target voices with the same content while source and target speakers speak in different languages. Its challenge lies in the fact that the source and target data are naturally non-parallel, and it is even difficult to bridge the gaps between languages with no transcriptions provided. In this paper, we focus on knowledge transfer from monolin-gual ASR to cross-lingual VC, in order to address the con-tent mismatch problem. To achieve this, we first train a monolingual acoustic model for the source language, use it to extract phonetic features for all the speech in the VC dataset, and then train a Seq2Seq conversion model to pre-dict the mel-spectrograms. We successfully address cross-lingual VC without any transcription or language-specific knowledge for foreign speech. We experiment this on Voice Conversion Challenge 2020 datasets and show that our speaker-dependent conversion model outperforms the zero-shot baseline, achieving MOS of 3.83 and 3.54 in speech quality and speaker similarity for cross-lingual conversion. When compared to Cascade ASR-TTS method, our proposed one significantly reduces the MOS drop be-tween intra- and cross-lingual conversion.

</details>

### [Automatic Arabic Dialect Identification Systems for Written Texts: A Survey](2009.12622.md)
**Maha J. Althobaiti** · 2020-09-26

<details>
<summary>Abstract</summary>

Arabic dialect identification is a specific task of natural language processing, aiming to automatically predict the Arabic dialect of a given text. Arabic dialect identification is the first step in various natural language processing applications such as machine translation, multilingual text-to-speech synthesis, and cross-language text generation. Therefore, in the last decade, interest has increased in addressing the problem of Arabic dialect identification. In this paper, we present a comprehensive survey of Arabic dialect identification research in written texts. We first define the problem and its challenges. Then, the survey extensively discusses in a critical manner many aspects related to Arabic dialect identification task. So, we review the traditional machine learning methods, deep learning architectures, and complex learning approaches to Arabic dialect identification. We also detail the features and techniques for feature representations used to train the proposed systems. Moreover, we illustrate the taxonomy of Arabic dialects studied in the literature, the various levels of text processing at which Arabic dialect identification are conducted (e.g., token, sentence, and document level), as well as the available annotated resources, including evaluation benchmark corpora. Open challenges and issues are discussed at the end of the survey.

</details>

### [Neural Face Models for Example-Based Visual Speech Synthesis](2009.10361.md)
**Wolfgang Paier, Anna Hilsmann, Peter Eisert** · 2020-09-22

<details>
<summary>Abstract</summary>

Creating realistic animations of human faces with computer graphic models is still a challenging task. It is often solved either with tedious manual work or motion capture based techniques that require specialised and costly hardware. Example based animation approaches circumvent these problems by re-using captured data of real people. This data is split into short motion samples that can be looped or concatenated in order to create novel motion sequences. The obvious advantages of this approach are the simplicity of use and the high realism, since the data exhibits only real deformations. Rather than tuning weights of a complex face rig, the animation task is performed on a higher level by arranging typical motion samples in a way such that the desired facial performance is achieved. Two difficulties with example based approaches, however, are high memory requirements as well as the creation of artefact-free and realistic transitions between motion samples. We solve these problems by combining the realism and simplicity of example-based animations with the advantages of neural face models. Our neural face model is capable of synthesising high quality 3D face geometry and texture according to a compact latent parameter vector. This latent representation reduces memory requirements by a factor of 100 and helps creating seamless transitions between concatenated motion samples. In this paper, we present a marker-less approach for facial motion capture based on multi-view video. Based on the captured data, we learn a neural representation of facial expressions, which is used to seamlessly concatenate facial performances during the animation procedure. We demonstrate the effectiveness of our approach by synthesising mouthings for Swiss-German sign language based on viseme query sequences.

</details>

### [Accent Estimation of Japanese Words from Their Surfaces and Romanizations for Building Large Vocabulary Accent Dictionaries](2009.09679.md)
**Hideyuki Tachibana, Yotaro Katayama** · 2020-09-21

<details>
<summary>Abstract</summary>

In Japanese text-to-speech (TTS), it is necessary to add accent information to the input sentence. However, there are a limited number of publicly available accent dictionaries, and those dictionaries e.g. UniDic, do not contain many compound words, proper nouns, etc., which are required in a practical TTS system. In order to build a large scale accent dictionary that contains those words, the authors developed an accent estimation technique that predicts the accent of a word from its limited information, namely the surface (e.g. kanji) and the yomi (simplified phonetic information). It is experimentally shown that the technique can estimate accents with high accuracies, especially for some categories of words. The authors applied this technique to an existing large vocabulary Japanese dictionary NEologd, and obtained a large vocabulary Japanese accent dictionary. Many cases have been observed in which the use of this dictionary yields more appropriate phonetic information than UniDic.

</details>

### [DiffWave: A Versatile Diffusion Model for Audio Synthesis](2009.09761.md)
**Zhifeng Kong, Wei Ping, Jiaji Huang, Kexin Zhao et al.** · 2020-09-21

<details>
<summary>Abstract</summary>

In this work, we propose DiffWave, a versatile diffusion probabilistic model for conditional and unconditional waveform generation. The model is non-autoregressive, and converts the white noise signal into structured waveform through a Markov chain with a constant number of steps at synthesis. It is efficiently trained by optimizing a variant of variational bound on the data likelihood. DiffWave produces high-fidelity audios in different waveform generation tasks, including neural vocoding conditioned on mel spectrogram, class-conditional generation, and unconditional generation. We demonstrate that DiffWave matches a strong WaveNet vocoder in terms of speech quality (MOS: 4.44 versus 4.43), while synthesizing orders of magnitude faster. In particular, it significantly outperforms autoregressive and GAN-based waveform models in the challenging unconditional generation task in terms of audio quality and sample diversity from various automatic and human evaluations.

</details>

### [Analysis of artifacts in EEG signals for building BCIs](2009.09116.md)
**Srihari Maruthachalam** · 2020-09-18

<details>
<summary>Abstract</summary>

Brain-Computer Interface (BCI) is an essential mechanism that interprets the human brain signal. It provides an assistive technology that enables persons with motor disabilities to communicate with the world and also empowers them to lead independent lives. The common BCI devices use Electroencephalography (EEG) electrical activity recorded from the scalp. EEG signals are noisy owing to the presence of many artifacts, namely, eye blink, head movement, and jaw movement. Such artifacts corrupt the EEG signal and make EEG analysis challenging. This issue is addressed by locating the artifacts and excluding the EEG segment from the analysis, which could lead to a loss of useful information. However, we propose a practical BCI that uses the artifacts which has a low signal to noise ratio. The objective of our work is to classify different types of artifacts, namely eye blink, head nod, head turn, and jaw movements in the EEG signal. The occurrence of the artifacts is first located in the EEG signal. The located artifacts are then classified using linear time and dynamic time warping techniques. The located artifacts can be used by a person with a motor disability to control a smartphone. A speech synthesis application that uses eyeblinks in a single channel EEG system and jaw clinches in four channels EEG system are developed. Word prediction models are used for word completion, thus reducing the number of artifacts required.

</details>

### [Hierarchical Multi-Grained Generative Model for Expressive Speech Synthesis](2009.08474.md)
**Yukiya Hono, Kazuna Tsuboi, Kei Sawada, Kei Hashimoto et al.** · 2020-09-17

<details>
<summary>Abstract</summary>

This paper proposes a hierarchical generative model with a multi-grained latent variable to synthesize expressive speech. In recent years, fine-grained latent variables are introduced into the text-to-speech synthesis that enable the fine control of the prosody and speaking styles of synthesized speech. However, the naturalness of speech degrades when these latent variables are obtained by sampling from the standard Gaussian prior. To solve this problem, we propose a novel framework for modeling the fine-grained latent variables, considering the dependence on an input text, a hierarchical linguistic structure, and a temporal structure of latent variables. This framework consists of a multi-grained variational autoencoder, a conditional prior, and a multi-level auto-regressive latent converter to obtain the different time-resolution latent variables and sample the finer-level latent variables from the coarser-level ones by taking into account the input text. Experimental results indicate an appropriate method of sampling fine-grained latent variables without the reference signal at the synthesis stage. Our proposed framework also provides the controllability of speaking style in an entire utterance.

</details>

### [Controllable neural text-to-speech synthesis using intuitive prosodic features](2009.06775.md)
**Tuomo Raitio, Ramya Rasipuram, Dan Castellani** · 2020-09-14

<details>
<summary>Abstract</summary>

Modern neural text-to-speech (TTS) synthesis can generate speech that is indistinguishable from natural speech. However, the prosody of generated utterances often represents the average prosodic style of the database instead of having wide prosodic variation. Moreover, the generated prosody is solely defined by the input text, which does not allow for different styles for the same sentence. In this work, we train a sequence-to-sequence neural network conditioned on acoustic speech features to learn a latent prosody space with intuitive and meaningful dimensions. Experiments show that a model conditioned on sentence-wise pitch, pitch range, phone duration, energy, and spectral tilt can effectively control each prosodic dimension and generate a wide variety of speaking styles, while maintaining similar mean opinion score (4.23) to our Tacotron baseline (4.26).

</details>

### [DualLip: A System for Joint Lip Reading and Generation](2009.05784.md)
**Weicong Chen, Xu Tan, Yingce Xia, Tao Qin et al.** · 2020-09-12

<details>
<summary>Abstract</summary>

Lip reading aims to recognize text from talking lip, while lip generation aims to synthesize talking lip according to text, which is a key component in talking face generation and is a dual task of lip reading. In this paper, we develop DualLip, a system that jointly improves lip reading and generation by leveraging the task duality and using unlabeled text and lip video data. The key ideas of the DualLip include: 1) Generate lip video from unlabeled text with a lip generation model, and use the pseudo pairs to improve lip reading; 2) Generate text from unlabeled lip video with a lip reading model, and use the pseudo pairs to improve lip generation. We further extend DualLip to talking face generation with two additionally introduced components: lip to face generation and text to speech generation. Experiments on GRID and TCD-TIMIT demonstrate the effectiveness of DualLip on improving lip reading, lip generation, and talking face generation by utilizing unlabeled data. Specifically, the lip generation model in our DualLip system trained with only10% paired data surpasses the performance of that trained with the whole paired data. And on the GRID benchmark of lip reading, we achieve 1.16% character error rate and 2.71% word error rate, outperforming the state-of-the-art models using the same amount of paired data.

</details>

### [Visual-speech Synthesis of Exaggerated Corrective Feedback](2009.05748.md)
**Yaohua Bu, Weijun Li, Tianyi Ma, Shengqi Chen et al.** · 2020-09-12

<details>
<summary>Abstract</summary>

To provide more discriminative feedback for the second language (L2) learners to better identify their mispronunciation, we propose a method for exaggerated visual-speech feedback in computer-assisted pronunciation training (CAPT). The speech exaggeration is realized by an emphatic speech generation neural network based on Tacotron, while the visual exaggeration is accomplished by ADC Viseme Blending, namely increasing Amplitude of movement, extending the phone's Duration and enhancing the color Contrast. User studies show that exaggerated feedback outperforms non-exaggerated version on helping learners with pronunciation identification and pronunciation improvement.

</details>

### [Exploration of End-to-end Synthesisers forZero Resource Speech Challenge 2020](2009.04983.md)
**Karthik Pandia D S, Anusha Prakash, Mano Ranjith Kumar, Hema A Murthy** · 2020-09-10

<details>
<summary>Abstract</summary>

A Spoken dialogue system for an unseen language is referred to as Zero resource speech. It is especially beneficial for developing applications for languages that have low digital resources. Zero resource speech synthesis is the task of building text-to-speech (TTS) models in the absence of transcriptions. In this work, speech is modelled as a sequence of transient and steady-state acoustic units, and a unique set of acoustic units is discovered by iterative training. Using the acoustic unit sequence, TTS models are trained. The main goal of this work is to improve the synthesis quality of zero resource TTS system. Four different systems are proposed. All the systems consist of three stages: unit discovery, followed by unit sequence to spectrogram mapping, and finally spectrogram to speech inversion. Modifications are proposed to the spectrogram mapping stage. These modifications include training the mapping on voice data, using x-vectors to improve the mapping, two-stage learning, and gender-specific modelling. Evaluation of the proposed systems in the Zerospeech 2020 challenge shows that quite good quality synthesis can be achieved.

</details>

### [What the Future Brings: Investigating the Impact of Lookahead for Incremental Neural TTS](2009.02035.md)
**Brooke Stephenson, Laurent Besacier, Laurent Girin, Thomas Hueber** · 2020-09-04

<details>
<summary>Abstract</summary>

In incremental text to speech synthesis (iTTS), the synthesizer produces an audio output before it has access to the entire input sentence. In this paper, we study the behavior of a neural sequence-to-sequence TTS system when used in an incremental mode, i.e. when generating speech output for token n, the system has access to n + k tokens from the text sequence. We first analyze the impact of this incremental policy on the evolution of the encoder representations of token n for different values of k (the lookahead parameter). The results show that, on average, tokens travel 88% of the way to their full context representation with a one-word lookahead and 94% after 2 words. We then investigate which text features are the most influential on the evolution towards the final representation using a random forest analysis. The results show that the most salient factors are related to token length. We finally evaluate the effects of lookahead k at the decoder level, using a MUSHRA listening test. This test shows results that contrast with the above high figures: speech synthesis quality obtained with 2 word-lookahead is significantly lower than the one obtained with the full sentence.

</details>

### [Voice Conversion Challenge 2020: Intra-lingual semi-parallel and cross-lingual voice conversion](2008.12527.md)
**Yi Zhao, Wen-Chin Huang, Xiaohai Tian, Junichi Yamagishi et al.** · 2020-08-28

<details>
<summary>Abstract</summary>

The voice conversion challenge is a bi-annual scientific event held to compare and understand different voice conversion (VC) systems built on a common dataset. In 2020, we organized the third edition of the challenge and constructed and distributed a new database for two tasks, intra-lingual semi-parallel and cross-lingual VC. After a two-month challenge period, we received 33 submissions, including 3 baselines built on the database. From the results of crowd-sourced listening tests, we observed that VC methods have progressed rapidly thanks to advanced deep learning methods. In particular, speaker similarity scores of several systems turned out to be as high as target speakers in the intra-lingual semi-parallel VC task. However, we confirmed that none of them have achieved human-level naturalness yet for the same task. The cross-lingual conversion task is, as expected, a more difficult task, and the overall naturalness and similarity scores were lower than those for the intra-lingual conversion task. However, we observed encouraging results, and the MOS scores of the best systems were higher than 4.0. We also show a few additional analysis results to aid in understanding cross-lingual VC better.

</details>

### [Nonparallel Voice Conversion with Augmented Classifier Star Generative Adversarial Networks](2008.12604.md)
**Hirokazu Kameoka, Takuhiro Kaneko, Kou Tanaka, Nobukatsu Hojo** · 2020-08-27

<details>
<summary>Abstract</summary>

We previously proposed a method that allows for nonparallel voice conversion (VC) by using a variant of generative adversarial networks (GANs) called StarGAN. The main features of our method, called StarGAN-VC, are as follows: First, it requires no parallel utterances, transcriptions, or time alignment procedures for speech generator training. Second, it can simultaneously learn mappings across multiple domains using a single generator network and thus fully exploit available training data collected from multiple domains to capture latent features that are common to all the domains. Third, it can generate converted speech signals quickly enough to allow real-time implementations and requires only several minutes of training examples to generate reasonably realistic-sounding speech. In this paper, we describe three formulations of StarGAN, including a newly introduced novel StarGAN variant called "Augmented classifier StarGAN (A-StarGAN)", and compare them in a nonparallel VC task. We also compare them with several baseline methods.

</details>

### [Efficient neural speech synthesis for low-resource languages through multilingual modeling](2008.09659.md)
**Marcel de Korte, Jaebok Kim, Esther Klabbers** · 2020-08-20

<details>
<summary>Abstract</summary>

Recent advances in neural TTS have led to models that can produce high-quality synthetic speech. However, these models typically require large amounts of training data, which can make it costly to produce a new voice with the desired quality. Although multi-speaker modeling can reduce the data requirements necessary for a new voice, this approach is usually not viable for many low-resource languages for which abundant multi-speaker data is not available. In this paper, we therefore investigated to what extent multilingual multi-speaker modeling can be an alternative to monolingual multi-speaker modeling, and explored how data from foreign languages may best be combined with low-resource language data. We found that multilingual modeling can increase the naturalness of low-resource language speech, showed that multilingual models can produce speech with a naturalness comparable to monolingual multi-speaker models, and saw that the target language naturalness was affected by the strategy used to add foreign language data.

</details>

### [Laughter Synthesis: Combining Seq2seq modeling with Transfer Learning](2008.09483.md)
**Noé Tits, Kevin El Haddad, Thierry Dutoit** · 2020-08-20

<details>
<summary>Abstract</summary>

Despite the growing interest for expressive speech synthesis, synthesis of nonverbal expressions is an under-explored area. In this paper we propose an audio laughter synthesis system based on a sequence-to-sequence TTS synthesis system. We leverage transfer learning by training a deep learning model to learn to generate both speech and laughs from annotations. We evaluate our model with a listening test, comparing its performance to an HMM-based laughter synthesis one and assess that it reaches higher perceived naturalness. Our solution is a first step towards a TTS system that would be able to synthesize speech with a control on amusement level with laughter integration.

</details>

### [CinC-GAN for Effective F0 prediction for Whisper-to-Normal Speech Conversion](2008.07788.md)
**Maitreya Patel, Mirali Purohit, Jui Shah, Hemant A. Patil** · 2020-08-18

<details>
<summary>Abstract</summary>

Recently, Generative Adversarial Networks (GAN)-based methods have shown remarkable performance for the Voice Conversion and WHiSPer-to-normal SPeeCH (WHSP2SPCH) conversion. One of the key challenges in WHSP2SPCH conversion is the prediction of fundamental frequency (F0). Recently, authors have proposed state-of-the-art method Cycle-Consistent Generative Adversarial Networks (CycleGAN) for WHSP2SPCH conversion. The CycleGAN-based method uses two different models, one for Mel Cepstral Coefficients (MCC) mapping, and another for F0 prediction, where F0 is highly dependent on the pre-trained model of MCC mapping. This leads to additional non-linear noise in predicted F0. To suppress this noise, we propose Cycle-in-Cycle GAN (i.e., CinC-GAN). It is specially designed to increase the effectiveness in F0 prediction without losing the accuracy of MCC mapping. We evaluated the proposed method on a non-parallel setting and analyzed on speaker-specific, and gender-specific tasks. The objective and subjective tests show that CinC-GAN significantly outperforms the CycleGAN. In addition, we analyze the CycleGAN and CinC-GAN for unseen speakers and the results show the clear superiority of CinC-GAN.

</details>

### [Audio Dequantization for High Fidelity Audio Generation in Flow-based Neural Vocoder](2008.06867.md)
**Hyun-Wook Yoon, Sang-Hoon Lee, Hyeong-Rae Noh, Seong-Whan Lee** · 2020-08-16

<details>
<summary>Abstract</summary>

In recent works, a flow-based neural vocoder has shown significant improvement in real-time speech generation task. The sequence of invertible flow operations allows the model to convert samples from simple distribution to audio samples. However, training a continuous density model on discrete audio data can degrade model performance due to the topological difference between latent and actual distribution. To resolve this problem, we propose audio dequantization methods in flow-based neural vocoder for high fidelity audio generation. Data dequantization is a well-known method in image generation but has not yet been studied in the audio domain. For this reason, we implement various audio dequantization methods in flow-based neural vocoder and investigate the effect on the generated audio. We conduct various objective performance assessments and subjective evaluation to show that audio dequantization can improve audio generation quality. From our experiments, using audio dequantization produces waveform audio with better harmonic structure and fewer digital artifacts.

</details>

### [Unsupervised Acoustic Unit Representation Learning for Voice Conversion using WaveNet Auto-encoders](2008.06892.md)
**Mingjie Chen, Thomas Hain** · 2020-08-16

<details>
<summary>Abstract</summary>

Unsupervised representation learning of speech has been of keen interest in recent years, which is for example evident in the wide interest of the ZeroSpeech challenges. This work presents a new method for learning frame level representations based on WaveNet auto-encoders. Of particular interest in the ZeroSpeech Challenge 2019 were models with discrete latent variable such as the Vector Quantized Variational Auto-Encoder (VQVAE). However these models generate speech with relatively poor quality. In this work we aim to address this with two approaches: first WaveNet is used as the decoder and to generate waveform data directly from the latent representation; second, the low complexity of latent representations is improved with two alternative disentanglement learning methods, namely instance normalization and sliced vector quantization. The method was developed and tested in the context of the recent ZeroSpeech challenge 2020. The system output submitted to the challenge obtained the top position for naturalness (Mean Opinion Score 4.06), top position for intelligibility (Character Error Rate 0.15), and third position for the quality of the representation (ABX test score 12.5). These and further analysis in this paper illustrates that quality of the converted speech and the acoustic units representation can be well balanced.

</details>

### [Online Speaker Adaptation for WaveNet-based Neural Vocoders](2008.06182.md)
**Qiuchen Huang, Yang Ai, Zhenhua Ling** · 2020-08-14

<details>
<summary>Abstract</summary>

In this paper, we propose an online speaker adaptation method for WaveNet-based neural vocoders in order to improve their performance on speaker-independent waveform generation. In this method, a speaker encoder is first constructed using a large speaker-verification dataset which can extract a speaker embedding vector from an utterance pronounced by an arbitrary speaker. At the training stage, a speaker-aware WaveNet vocoder is then built using a multi-speaker dataset which adopts both acoustic feature sequences and speaker embedding vectors as conditions.At the generation stage, we first feed the acoustic feature sequence from a test speaker into the speaker encoder to obtain the speaker embedding vector of the utterance. Then, both the speaker embedding vector and acoustic features pass the speaker-aware WaveNet vocoder to reconstruct speech waveforms. Experimental results demonstrate that our method can achieve a better objective and subjective performance on reconstructing waveforms of unseen speakers than the conventional speaker-independent WaveNet vocoder.

</details>

### [Enhancing Speech Intelligibility in Text-To-Speech Synthesis using Speaking Style Conversion](2008.05809.md)
**Dipjyoti Paul, Muhammed PV Shifas, Yannis Pantazis, Yannis Stylianou** · 2020-08-13

<details>
<summary>Abstract</summary>

The increased adoption of digital assistants makes text-to-speech (TTS) synthesis systems an indispensable feature of modern mobile devices. It is hence desirable to build a system capable of generating highly intelligible speech in the presence of noise. Past studies have investigated style conversion in TTS synthesis, yet degraded synthesized quality often leads to worse intelligibility. To overcome such limitations, we proposed a novel transfer learning approach using Tacotron and WaveRNN based TTS synthesis. The proposed speech system exploits two modification strategies: (a) Lombard speaking style data and (b) Spectral Shaping and Dynamic Range Compression (SSDRC) which has been shown to provide high intelligibility gains by redistributing the signal energy on the time-frequency domain. We refer to this extension as Lombard-SSDRC TTS system. Intelligibility enhancement as quantified by the Intelligibility in Bits (SIIB-Gauss) measure shows that the proposed Lombard-SSDRC TTS system shows significant relative improvement between 110% and 130% in speech-shaped noise (SSN), and 47% to 140% in competing-speaker noise (CSN) against the state-of-the-art TTS approach. Additional subjective evaluation shows that Lombard-SSDRC TTS successfully increases the speech intelligibility with relative improvement of 455% for SSN and 104% for CSN in median keyword correction rate compared to the baseline TTS method.

</details>

### [Prosody Learning Mechanism for Speech Synthesis System Without Text Length Limit](2008.05656.md)
**Zhen Zeng, Jianzong Wang, Ning Cheng, Jing Xiao** · 2020-08-13

<details>
<summary>Abstract</summary>

Recent neural speech synthesis systems have gradually focused on the control of prosody to improve the quality of synthesized speech, but they rarely consider the variability of prosody and the correlation between prosody and semantics together. In this paper, a prosody learning mechanism is proposed to model the prosody of speech based on TTS system, where the prosody information of speech is extracted from the melspectrum by a prosody learner and combined with the phoneme sequence to reconstruct the mel-spectrum. Meanwhile, the sematic features of text from the pre-trained language model is introduced to improve the prosody prediction results. In addition, a novel self-attention structure, named as local attention, is proposed to lift this restriction of input text length, where the relative position information of the sequence is modeled by the relative position matrices so that the position encodings is no longer needed. Experiments on English and Mandarin show that speech with more satisfactory prosody has obtained in our model. Especially in Mandarin synthesis, our proposed model outperforms baseline model with a MOS gap of 0.08, and the overall naturalness of the synthesized speech has been significantly improved.

</details>

### [An Overview of Deep Learning Architectures in Few-Shot Learning Domain](2008.06365.md)
**Shruti Jadon, Aryan Jadon** · 2020-08-12

<details>
<summary>Abstract</summary>

Since 2012, Deep learning has revolutionized Artificial Intelligence and has achieved state-of-the-art outcomes in different domains, ranging from Image Classification to Speech Generation. Though it has many potentials, our current architectures come with the pre-requisite of large amounts of data. Few-Shot Learning (also known as one-shot learning) is a sub-field of machine learning that aims to create such models that can learn the desired objective with less data, similar to how humans learn. In this paper, we have reviewed some of the well-known deep learning-based approaches towards few-shot learning. We have discussed the recent achievements, challenges, and possibilities of improvement of few-shot learning based deep learning architectures. Our aim for this paper is threefold: (i) Give a brief introduction to deep learning architectures for few-shot learning with pointers to core references. (ii) Indicate how deep learning has been applied to the low-data regime, from data preparation to model training. and, (iii) Provide a starting point for people interested in experimenting and perhaps contributing to the field of few-shot learning by pointing out some useful resources and open-source code. Our code is available at Github: https://github.com/shruti-jadon/Hands-on-One-Shot-Learning.

</details>

### [Bunched LPCNet : Vocoder for Low-cost Neural Text-To-Speech Systems](2008.04574.md)
**Ravichander Vipperla, Sangjun Park, Kihyun Choo, Samin Ishtiaq et al.** · 2020-08-11

<details>
<summary>Abstract</summary>

LPCNet is an efficient vocoder that combines linear prediction and deep neural network modules to keep the computational complexity low. In this work, we present two techniques to further reduce it's complexity, aiming for a low-cost LPCNet vocoder-based neural Text-to-Speech (TTS) System. These techniques are: 1) Sample-bunching, which allows LPCNet to generate more than one audio sample per inference; and 2) Bit-bunching, which reduces the computations in the final layer of LPCNet. With the proposed bunching techniques, LPCNet, in conjunction with a Deep Convolutional TTS (DCTTS) acoustic model, shows a 2.19x improvement over the baseline run-time when running on a mobile device, with a less than 0.1 decrease in TTS mean opinion score (MOS).

</details>

### [Unsupervised Learning For Sequence-to-sequence Text-to-speech For Low-resource Languages](2008.04549.md)
**Haitong Zhang, Yue Lin** · 2020-08-11

<details>
<summary>Abstract</summary>

Recently, sequence-to-sequence models with attention have been successfully applied in Text-to-speech (TTS). These models can generate near-human speech with a large accurately-transcribed speech corpus. However, preparing such a large data-set is both expensive and laborious. To alleviate the problem of heavy data demand, we propose a novel unsupervised pre-training mechanism in this paper. Specifically, we first use Vector-quantization Variational-Autoencoder (VQ-VAE) to ex-tract the unsupervised linguistic units from large-scale, publicly found, and untranscribed speech. We then pre-train the sequence-to-sequence TTS model by using the<unsupervised linguistic units, audio>pairs. Finally, we fine-tune the model with a small amount of<text, audio>paired data from the target speaker. As a result, both objective and subjective evaluations show that our proposed method can synthesize more intelligible and natural speech with the same amount of paired training data. Besides, we extend our proposed method to the hypothesized low-resource languages and verify the effectiveness of the method using objective evaluation.

</details>

### [Modeling Prosodic Phrasing with Multi-Task Learning in Tacotron-based TTS](2008.05284.md)
**Rui Liu, Berrak Sisman, Feilong Bao, Guanglai Gao et al.** · 2020-08-11

<details>
<summary>Abstract</summary>

Tacotron-based end-to-end speech synthesis has shown remarkable voice quality. However, the rendering of prosody in the synthesized speech remains to be improved, especially for long sentences, where prosodic phrasing errors can occur frequently. In this paper, we extend the Tacotron-based speech synthesis framework to explicitly model the prosodic phrase breaks. We propose a multi-task learning scheme for Tacotron training, that optimizes the system to predict both Mel spectrum and phrase breaks. To our best knowledge, this is the first implementation of multi-task learning for Tacotron based TTS with a prosodic phrasing model. Experiments show that our proposed training scheme consistently improves the voice quality for both Chinese and Mongolian systems.

</details>

### [Spectrum and Prosody Conversion for Cross-lingual Voice Conversion with CycleGAN](2008.04562.md)
**Zongyang Du, Kun Zhou, Berrak Sisman, Haizhou Li** · 2020-08-11

<details>
<summary>Abstract</summary>

Cross-lingual voice conversion aims to change source speaker's voice to sound like that of target speaker, when source and target speakers speak different languages. It relies on non-parallel training data from two different languages, hence, is more challenging than mono-lingual voice conversion. Previous studies on cross-lingual voice conversion mainly focus on spectral conversion with a linear transformation for F0 transfer. However, as an important prosodic factor, F0 is inherently hierarchical, thus it is insufficient to just use a linear method for conversion. We propose the use of continuous wavelet transform (CWT) decomposition for F0 modeling. CWT provides a way to decompose a signal into different temporal scales that explain prosody in different time resolutions. We also propose to train two CycleGAN pipelines for spectrum and prosody mapping respectively. In this way, we eliminate the need for parallel data of any two languages and any alignment techniques. Experimental results show that our proposed Spectrum-Prosody-CycleGAN framework outperforms the Spectrum-CycleGAN baseline in subjective evaluation. To our best knowledge, this is the first study of prosody in cross-lingual voice conversion.

</details>

### [VAW-GAN for Singing Voice Conversion with Non-parallel Training Data](2008.03992.md)
**Junchen Lu, Kun Zhou, Berrak Sisman, Haizhou Li** · 2020-08-10

<details>
<summary>Abstract</summary>

Singing voice conversion aims to convert singer's voice from source to target without changing singing content. Parallel training data is typically required for the training of singing voice conversion system, that is however not practical in real-life applications. Recent encoder-decoder structures, such as variational autoencoding Wasserstein generative adversarial network (VAW-GAN), provide an effective way to learn a mapping through non-parallel training data. In this paper, we propose a singing voice conversion framework that is based on VAW-GAN. We train an encoder to disentangle singer identity and singing prosody (F0 contour) from phonetic content. By conditioning on singer identity and F0, the decoder generates output spectral features with unseen target singer identity, and improves the F0 rendering. Experimental results show that the proposed framework achieves better performance than the baseline frameworks.

</details>

### [Data Efficient Voice Cloning from Noisy Samples with Domain Adversarial Training](2008.04265.md)
**Jian Cong, Shan Yang, Lei Xie, Guoqiao Yu et al.** · 2020-08-10

<details>
<summary>Abstract</summary>

Data efficient voice cloning aims at synthesizing target speaker's voice with only a few enrollment samples at hand. To this end, speaker adaptation and speaker encoding are two typical methods based on base model trained from multiple speakers. The former uses a small set of target speaker data to transfer the multi-speaker model to target speaker's voice through direct model update, while in the latter, only a few seconds of target speaker's audio directly goes through an extra speaker encoding model along with the multi-speaker model to synthesize target speaker's voice without model update. Nevertheless, the two methods need clean target speaker data. However, the samples provided by user may inevitably contain acoustic noise in real applications. It's still challenging to generating target voice with noisy data. In this paper, we study the data efficient voice cloning problem from noisy samples under the sequence-to-sequence based TTS paradigm. Specifically, we introduce domain adversarial training (DAT) to speaker adaptation and speaker encoding, which aims to disentangle noise from speech-noise mixture. Experiments show that for both speaker adaptation and encoding, the proposed approaches can consistently synthesize clean speech from noisy speaker samples, apparently outperforming the method adopting state-of-the-art speech enhancement module.

</details>

### [Speaker Conditional WaveRNN: Towards Universal Neural Vocoder for Unseen Speaker and Recording Conditions](2008.05289.md)
**Dipjyoti Paul, Yannis Pantazis, Yannis Stylianou** · 2020-08-09

<details>
<summary>Abstract</summary>

Recent advancements in deep learning led to human-level performance in single-speaker speech synthesis. However, there are still limitations in terms of speech quality when generalizing those systems into multiple-speaker models especially for unseen speakers and unseen recording qualities. For instance, conventional neural vocoders are adjusted to the training speaker and have poor generalization capabilities to unseen speakers. In this work, we propose a variant of WaveRNN, referred to as speaker conditional WaveRNN (SC-WaveRNN). We target towards the development of an efficient universal vocoder even for unseen speakers and recording conditions. In contrast to standard WaveRNN, SC-WaveRNN exploits additional information given in the form of speaker embeddings. Using publicly-available data for training, SC-WaveRNN achieves significantly better performance over baseline WaveRNN on both subjective and objective metrics. In MOS, SC-WaveRNN achieves an improvement of about 23% for seen speaker and seen recording condition and up to 95% for unseen speaker and unseen condition. Finally, we extend our work by implementing a multi-speaker text-to-speech (TTS) synthesis similar to zero-shot speaker adaptation. In terms of performance, our system has been preferred over the baseline TTS system by 60% over 15.5% and by 60.9% over 32.6%, for seen and unseen speakers, respectively.

</details>

### [SpeedySpeech: Efficient Neural Speech Synthesis](2008.03802.md)
**Jan Vainer, Ondřej Dušek** · 2020-08-09

<details>
<summary>Abstract</summary>

While recent neural sequence-to-sequence models have greatly improved the quality of speech synthesis, there has not been a system capable of fast training, fast inference and high-quality audio synthesis at the same time. We propose a student-teacher network capable of high-quality faster-than-real-time spectrogram synthesis, with low requirements on computational resources and fast training time. We show that self-attention layers are not necessary for generation of high quality audio. We utilize simple convolutional blocks with residual connections in both student and teacher networks and use only a single attention layer in the teacher model. Coupled with a MelGAN vocoder, our model's voice quality was rated significantly higher than Tacotron 2. Our model can be efficiently trained on a single GPU and can run in real time even on a CPU. We provide both our source code and audio samples in our GitHub repository.

</details>

### [Deep MOS Predictor for Synthetic Speech Using Cluster-Based Modeling](2008.03710.md)
**Yeunju Choi, Youngmoon Jung, Hoirin Kim** · 2020-08-09

<details>
<summary>Abstract</summary>

While deep learning has made impressive progress in speech synthesis and voice conversion, the assessment of the synthesized speech is still carried out by human participants. Several recent papers have proposed deep-learning-based assessment models and shown the potential to automate the speech quality assessment. To improve the previously proposed assessment model, MOSNet, we propose three models using cluster-based modeling methods: using a global quality token (GQT) layer, using an Encoding Layer, and using both of them. We perform experiments using the evaluation results of the Voice Conversion Challenge 2018 to predict the mean opinion score of synthesized speech and similarity score between synthesized speech and reference speech. The results show that the GQT layer helps to predict human assessment better by automatically learning the useful quality tokens for the task and that the Encoding Layer helps to utilize frame-level scores more precisely.

</details>

### [An Overview of Voice Conversion and its Challenges: From Statistical Modeling to Deep Learning](2008.03648.md)
**Berrak Sisman, Junichi Yamagishi, Simon King, Haizhou Li** · 2020-08-09

<details>
<summary>Abstract</summary>

Speaker identity is one of the important characteristics of human speech. In voice conversion, we change the speaker identity from one to another, while keeping the linguistic content unchanged. Voice conversion involves multiple speech processing techniques, such as speech analysis, spectral conversion, prosody conversion, speaker characterization, and vocoding. With the recent advances in theory and practice, we are now able to produce human-like voice quality with high speaker similarity. In this paper, we provide a comprehensive overview of the state-of-the-art of voice conversion techniques and their performance evaluation methods from the statistical approaches to deep learning, and discuss their promise and limitations. We will also report the recent Voice Conversion Challenges (VCC), the performance of the current state of technology, and provide a summary of the available resources for voice conversion research.

</details>

### [Incremental Text to Speech for Neural Sequence-to-Sequence Models using Reinforcement Learning](2008.03096.md)
**Devang S Ram Mohan, Raphael Lenain, Lorenzo Foglianti, Tian Huey Teh et al.** · 2020-08-07

<details>
<summary>Abstract</summary>

Modern approaches to text to speech require the entire input character sequence to be processed before any audio is synthesised. This latency limits the suitability of such models for time-sensitive tasks like simultaneous interpretation. Interleaving the action of reading a character with that of synthesising audio reduces this latency. However, the order of this sequence of interleaved actions varies across sentences, which raises the question of how the actions should be chosen. We propose a reinforcement learning based framework to train an agent to make this decision. We compare our performance against that of deterministic, rule-based systems. Our results demonstrate that our agent successfully balances the trade-off between the latency of audio generation and the quality of synthesised audio. More broadly, we show that neural sequence-to-sequence models can be adapted to run in an incremental manner.

</details>

### [Multi-speaker Text-to-speech Synthesis Using Deep Gaussian Processes](2008.02950.md)
**Kentaro Mitsui, Tomoki Koriyama, Hiroshi Saruwatari** · 2020-08-07

<details>
<summary>Abstract</summary>

Multi-speaker speech synthesis is a technique for modeling multiple speakers' voices with a single model. Although many approaches using deep neural networks (DNNs) have been proposed, DNNs are prone to overfitting when the amount of training data is limited. We propose a framework for multi-speaker speech synthesis using deep Gaussian processes (DGPs); a DGP is a deep architecture of Bayesian kernel regressions and thus robust to overfitting. In this framework, speaker information is fed to duration/acoustic models using speaker codes. We also examine the use of deep Gaussian process latent variable models (DGPLVMs). In this approach, the representation of each speaker is learned simultaneously with other model parameters, and therefore the similarity or dissimilarity of speakers is considered efficiently. We experimentally evaluated two situations to investigate the effectiveness of the proposed methods. In one situation, the amount of data from each speaker is balanced (speaker-balanced), and in the other, the data from certain speakers are limited (speaker-imbalanced). Subjective and objective evaluation results showed that both the DGP and DGPLVM synthesize multi-speaker speech more effective than a DNN in the speaker-balanced situation. We also found that the DGPLVM outperforms the DGP significantly in the speaker-imbalanced situation.

</details>

### [Controllable Neural Prosody Synthesis](2008.03388.md)
**Max Morrison, Zeyu Jin, Justin Salamon, Nicholas J. Bryan et al.** · 2020-08-07

<details>
<summary>Abstract</summary>

Speech synthesis has recently seen significant improvements in fidelity, driven by the advent of neural vocoders and neural prosody generators. However, these systems lack intuitive user controls over prosody, making them unable to rectify prosody errors (e.g., misplaced emphases and contextually inappropriate emotions) or generate prosodies with diverse speaker excitement levels and emotions. We address these limitations with a user-controllable, context-aware neural prosody generator. Given a real or synthesized speech recording, our model allows a user to input prosody constraints for certain time frames and generates the remaining time frames from input text and contextual prosody. We also propose a pitch-shifting neural vocoder to modify input speech to match the synthesized prosody. Through objective and subjective evaluations we show that we can successfully incorporate user control into our prosody generation model without sacrificing the overall naturalness of the synthesized speech.

</details>

### [DurIAN-SC: Duration Informed Attention Network based Singing Voice Conversion System](2008.03009.md)
**Liqiang Zhang, Chengzhu Yu, Heng Lu, Chao Weng et al.** · 2020-08-07

<details>
<summary>Abstract</summary>

Singing voice conversion is converting the timbre in the source singing to the target speaker's voice while keeping singing content the same. However, singing data for target speaker is much more difficult to collect compared with normal speech data.In this paper, we introduce a singing voice conversion algorithm that is capable of generating high quality target speaker's singing using only his/her normal speech data. First, we manage to integrate the training and conversion process of speech and singing into one framework by unifying the features used in standard speech synthesis system and singing synthesis system. In this way, normal speech data can also contribute to singing voice conversion training, making the singing voice conversion system more robust especially when the singing database is small.Moreover, in order to achieve one-shot singing voice conversion, a speaker embedding module is developed using both speech and singing data, which provides target speaker identify information during conversion. Experiments indicate proposed sing conversion system can convert source singing to target speaker's high-quality singing with only 20 seconds of target speaker's enrollment speech data.

</details>

### [Phonological Features for 0-shot Multilingual Speech Synthesis](2008.04107.md)
**Marlene Staib, Tian Huey Teh, Alexandra Torresquintero, Devang S Ram Mohan et al.** · 2020-08-06

<details>
<summary>Abstract</summary>

Code-switching---the intra-utterance use of multiple languages---is prevalent across the world. Within text-to-speech (TTS), multilingual models have been found to enable code-switching. By modifying the linguistic input to sequence-to-sequence TTS, we show that code-switching is possible for languages unseen during training, even within monolingual models. We use a small set of phonological features derived from the International Phonetic Alphabet (IPA), such as vowel height and frontness, consonant place and manner. This allows the model topology to stay unchanged for different languages, and enables new, previously unseen feature combinations to be interpreted by the model. We show that this allows us to generate intelligible, code-switched speech in a new language at test time, including the approximation of sounds never seen in training.

</details>

### [Ultrasound-based Articulatory-to-Acoustic Mapping with WaveGlow Speech Synthesis](2008.03152.md)
**Tamás Gábor Csapó, Csaba Zainkó, László Tóth, Gábor Gosztolya et al.** · 2020-08-06

<details>
<summary>Abstract</summary>

For articulatory-to-acoustic mapping using deep neural networks, typically spectral and excitation parameters of vocoders have been used as the training targets. However, vocoding often results in buzzy and muffled final speech quality. Therefore, in this paper on ultrasound-based articulatory-to-acoustic conversion, we use a flow-based neural vocoder (WaveGlow) pre-trained on a large amount of English and Hungarian speech data. The inputs of the convolutional neural network are ultrasound tongue images. The training target is the 80-dimensional mel-spectrogram, which results in a finer detailed spectral representation than the previously used 25-dimensional Mel-Generalized Cepstrum. From the output of the ultrasound-to-mel-spectrogram prediction, WaveGlow inference results in synthesized speech. We compare the proposed WaveGlow-based system with a continuous vocoder which does not use strict voiced/unvoiced decision when predicting F0. The results demonstrate that during the articulatory-to-acoustic mapping experiments, the WaveGlow neural vocoder produces significantly more natural synthesized speech than the baseline system. Besides, the advantage of WaveGlow is that F0 is included in the mel-spectrogram representation, and it is not necessary to predict the excitation separately.

</details>

### [HooliGAN: Robust, High Quality Neural Vocoding](2008.02493.md)
**Ollie McCarthy, Zohaib Ahmed** · 2020-08-06

<details>
<summary>Abstract</summary>

Recent developments in generative models have shown that deep learning combined with traditional digital signal processing (DSP) techniques could successfully generate convincing violin samples [1], that source-excitation combined with WaveNet yields high-quality vocoders [2, 3] and that generative adversarial network (GAN) training can improve naturalness [4, 5]. By combining the ideas in these models we introduce HooliGAN, a robust vocoder that has state of the art results, finetunes very well to smaller datasets (<30 minutes of speechdata) and generates audio at 2.2MHz on GPU and 35kHz on CPU. We also show a simple modification to Tacotron-basedmodels that allows seamless integration with HooliGAN. Results from our listening tests show the proposed model's ability to consistently output high-quality audio with a variety of datasets, big and small. We provide samples at the following demo page: https://resemble-ai.github.io/hooligan_demo/

</details>

### [Learning Boost by Exploiting the Auxiliary Task in Multi-task Domain](2008.02043.md)
**Jonghwa Yim, Sang Hwan Kim** · 2020-08-05

<details>
<summary>Abstract</summary>

Learning two tasks in a single shared function has some benefits. Firstly by acquiring information from the second task, the shared function leverages useful information that could have been neglected or underestimated in the first task. Secondly, it helps to generalize the function that can be learned using generally applicable information for both tasks. To fully enjoy these benefits, Multi-task Learning (MTL) has long been researched in various domains such as computer vision, language understanding, and speech synthesis. While MTL benefits from the positive transfer of information from multiple tasks, in a real environment, tasks inevitably have a conflict between them during the learning phase, called negative transfer. The negative transfer hampers function from achieving the optimality and degrades the performance. To solve the problem of the task conflict, previous works only suggested partial solutions that are not fundamental, but ad-hoc. A common approach is using a weighted sum of losses. The weights are adjusted to induce positive transfer. Paradoxically, this kind of solution acknowledges the problem of negative transfer and cannot remove it unless the weight of the task is set to zero. Therefore, these previous methods had limited success. In this paper, we introduce a novel approach that can drive positive transfer and suppress negative transfer by leveraging class-wise weights in the learning process. The weights act as an arbitrator of the fundamental unit of information to determine its positive or negative status to the main task.

</details>

### [Recognition-Synthesis Based Non-Parallel Voice Conversion with Adversarial Learning](2008.02371.md)
**Jing-Xuan Zhang, Zhen-Hua Ling, Li-Rong Dai** · 2020-08-05

<details>
<summary>Abstract</summary>

This paper presents an adversarial learning method for recognition-synthesis based non-parallel voice conversion. A recognizer is used to transform acoustic features into linguistic representations while a synthesizer recovers output features from the recognizer outputs together with the speaker identity. By separating the speaker characteristics from the linguistic representations, voice conversion can be achieved by replacing the speaker identity with the target one. In our proposed method, a speaker adversarial loss is adopted in order to obtain speaker-independent linguistic representations using the recognizer. Furthermore, discriminators are introduced and a generative adversarial network (GAN) loss is used to prevent the predicted features from being over-smoothed. For training model parameters, a strategy of pre-training on a multi-speaker dataset and then fine-tuning on the source-target speaker pair is designed. Our method achieved higher similarity than the baseline model that obtained the best performance in Voice Conversion Challenge 2018.

</details>

### [Expressive TTS Training with Frame and Style Reconstruction Loss](2008.01490.md)
**Rui Liu, Berrak Sisman, Guanglai Gao, Haizhou Li** · 2020-08-04

<details>
<summary>Abstract</summary>

We propose a novel training strategy for Tacotron-based text-to-speech (TTS) system to improve the expressiveness of speech. One of the key challenges in prosody modeling is the lack of reference that makes explicit modeling difficult. The proposed technique doesn't require prosody annotations from training data. It doesn't attempt to model prosody explicitly either, but rather encodes the association between input text and its prosody styles using a Tacotron-based TTS framework. Our proposed idea marks a departure from the style token paradigm where prosody is explicitly modeled by a bank of prosody embeddings. The proposed training strategy adopts a combination of two objective functions: 1) frame level reconstruction loss, that is calculated between the synthesized and target spectral features; 2) utterance level style reconstruction loss, that is calculated between the deep style features of synthesized and target speech. The proposed style reconstruction loss is formulated as a perceptual loss to ensure that utterance level speech style is taken into consideration during training. Experiments show that the proposed training strategy achieves remarkable performance and outperforms a state-of-the-art baseline in both naturalness and expressiveness. To our best knowledge, this is the first study to incorporate utterance level perceptual quality as a loss function into Tacotron training for improved expressiveness.

</details>

### [One Model, Many Languages: Meta-learning for Multilingual Text-to-Speech](2008.00768.md)
**Tomáš Nekvinda, Ondřej Dušek** · 2020-08-03

<details>
<summary>Abstract</summary>

We introduce an approach to multilingual speech synthesis which uses the meta-learning concept of contextual parameter generation and produces natural-sounding multilingual speech using more languages and less training data than previous approaches. Our model is based on Tacotron 2 with a fully convolutional input text encoder whose weights are predicted by a separate parameter generator network. To boost voice cloning, the model uses an adversarial speaker classifier with a gradient reversal layer that removes speaker-specific information from the encoder. We arranged two experiments to compare our model with baselines using various levels of cross-lingual parameter sharing, in order to evaluate: (1) stability and performance when training on low amounts of data, (2) pronunciation accuracy and voice quality of code-switching synthesis. For training, we used the CSS10 dataset and our new small dataset based on Common Voice recordings in five languages. Our model is shown to effectively share information across languages and according to a subjective evaluation test, it produces more natural and accurate code-switching speech than the baselines.

</details>

### [Exploiting Deep Sentential Context for Expressive End-to-End Speech Synthesis](2008.00613.md)
**Fengyu Yang, Shan Yang, Qinghua Wu, Yujun Wang et al.** · 2020-08-03

<details>
<summary>Abstract</summary>

Attention-based seq2seq text-to-speech systems, especially those use self-attention networks (SAN), have achieved state-of-art performance. But an expressive corpus with rich prosody is still challenging to model as 1) prosodic aspects, which span across different sentential granularities and mainly determine acoustic expressiveness, are difficult to quantize and label and 2) the current seq2seq framework extracts prosodic information solely from a text encoder, which is easily collapsed to an averaged expression for expressive contents. In this paper, we propose a context extractor, which is built upon SAN-based text encoder, to sufficiently exploit the sentential context over an expressive corpus for seq2seq-based TTS. Our context extractor first collects prosodic-related sentential context information from different SAN layers and then aggregates them to learn a comprehensive sentence representation to enhance the expressiveness of the final generated speech. Specifically, we investigate two methods of context aggregation: 1) direct aggregation which directly concatenates the outputs of different SAN layers, and 2) weighted aggregation which uses multi-head attention to automatically learn contributions for different SAN layers. Experiments on two expressive corpora show that our approach can produce more natural speech with much richer prosodic variations, and weighted aggregation is more superior in modeling expressivity.

</details>

### [A Spectral Energy Distance for Parallel Speech Synthesis](2008.01160.md)
**Alexey A. Gritsenko, Tim Salimans, Rianne van den Berg, Jasper Snoek et al.** · 2020-08-03

<details>
<summary>Abstract</summary>

Speech synthesis is an important practical generative modeling problem that has seen great progress over the last few years, with likelihood-based autoregressive neural models now outperforming traditional concatenative systems. A downside of such autoregressive models is that they require executing tens of thousands of sequential operations per second of generated audio, making them ill-suited for deployment on specialized deep learning hardware. Here, we propose a new learning method that allows us to train highly parallel models of speech, without requiring access to an analytical likelihood function. Our approach is based on a generalized energy distance between the distributions of the generated and real audio. This spectral energy distance is a proper scoring rule with respect to the distribution over magnitude-spectrograms of the generated waveform audio and offers statistical consistency guarantees. The distance can be calculated from minibatches without bias, and does not involve adversarial learning, yielding a stable and consistent method for training implicit generative models. Empirically, we achieve state-of-the-art generation quality among implicit generative models, as judged by the recently-proposed cFDSD metric. When combining our method with adversarial techniques, we also improve upon the recently-proposed GAN-TTS model in terms of Mean Opinion Score as judged by trained human evaluators.

</details>

### [Audiovisual Speech Synthesis using Tacotron2](2008.00620.md)
**Ahmed Hussen Abdelaziz, Anushree Prasanna Kumar, Chloe Seivwright, Gabriele Fanelli et al.** · 2020-08-03

<details>
<summary>Abstract</summary>

Audiovisual speech synthesis is the problem of synthesizing a talking face while maximizing the coherency of the acoustic and visual speech. In this paper, we propose and compare two audiovisual speech synthesis systems for 3D face models. The first system is the AVTacotron2, which is an end-to-end text-to-audiovisual speech synthesizer based on the Tacotron2 architecture. AVTacotron2 converts a sequence of phonemes representing the sentence to synthesize into a sequence of acoustic features and the corresponding controllers of a face model. The output acoustic features are used to condition a WaveRNN to reconstruct the speech waveform, and the output facial controllers are used to generate the corresponding video of the talking face. The second audiovisual speech synthesis system is modular, where acoustic speech is synthesized from text using the traditional Tacotron2. The reconstructed acoustic speech signal is then used to drive the facial controls of the face model using an independently trained audio-to-facial-animation neural network. We further condition both the end-to-end and modular approaches on emotion embeddings that encode the required prosody to generate emotional audiovisual speech. We analyze the performance of the two systems and compare them to the ground truth videos using subjective evaluation tests. The end-to-end and modular systems are able to synthesize close to human-like audiovisual speech with mean opinion scores (MOS) of 4.1 and 3.9, respectively, compared to a MOS of 4.1 for the ground truth generated from professionally recorded videos. While the end-to-end system gives a better overall quality, the modular approach is more flexible and the quality of acoustic speech and visual speech synthesis is almost independent of each other.

</details>

### [Neural text-to-speech with a modeling-by-generation excitation vocoder](2008.00132.md)
**Eunwoo Song, Min-Jae Hwang, Ryuichi Yamamoto, Jin-Seob Kim et al.** · 2020-08-01

<details>
<summary>Abstract</summary>

This paper proposes a modeling-by-generation (MbG) excitation vocoder for a neural text-to-speech (TTS) system. Recently proposed neural excitation vocoders can realize qualified waveform generation by combining a vocal tract filter with a WaveNet-based glottal excitation generator. However, when these vocoders are used in a TTS system, the quality of synthesized speech is often degraded owing to a mismatch between training and synthesis steps. Specifically, the vocoder is separately trained from an acoustic model front-end. Therefore, estimation errors of the acoustic model are inevitably boosted throughout the synthesis process of the vocoder back-end. To address this problem, we propose to incorporate an MbG structure into the vocoder's training process. In the proposed method, the excitation signal is extracted by the acoustic model's generated spectral parameters, and the neural vocoder is then optimized not only to learn the target excitation's distribution but also to compensate for the estimation errors occurring from the acoustic model. Furthermore, as the generated spectral parameters are shared in the training and synthesis steps, their mismatch conditions can be reduced effectively. The experimental results verify that the proposed system provides high-quality synthetic speech by achieving a mean opinion score of 4.57 within the TTS framework.

</details>

### [Speaking Speed Control of End-to-End Speech Synthesis using Sentence-Level Conditioning](2007.15281.md)
**Jae-Sung Bae, Hanbin Bae, Young-Sun Joo, Junmo Lee et al.** · 2020-07-30

<details>
<summary>Abstract</summary>

This paper proposes a controllable end-to-end text-to-speech (TTS) system to control the speaking speed (speed-controllable TTS; SCTTS) of synthesized speech with sentence-level speaking-rate value as an additional input. The speaking-rate value, the ratio of the number of input phonemes to the length of input speech, is adopted in the proposed system to control the speaking speed. Furthermore, the proposed SCTTS system can control the speaking speed while retaining other speech attributes, such as the pitch, by adopting the global style token-based style encoder. The proposed SCTTS does not require any additional well-trained model or an external speech database to extract phoneme-level duration information and can be trained in an end-to-end manner. In addition, our listening tests on fast-, normal-, and slow-speed speech showed that the SCTTS can generate more natural speech than other phoneme duration control approaches which increase or decrease duration at the same rate for the entire sentence, especially in the case of slow-speed speech.

</details>

### [VocGAN: A High-Fidelity Real-time Vocoder with a Hierarchically-nested Adversarial Network](2007.15256.md)
**Jinhyeok Yang, Junmo Lee, Youngik Kim, Hoonyoung Cho et al.** · 2020-07-30

<details>
<summary>Abstract</summary>

We present a novel high-fidelity real-time neural vocoder called VocGAN. A recently developed GAN-based vocoder, MelGAN, produces speech waveforms in real-time. However, it often produces a waveform that is insufficient in quality or inconsistent with acoustic characteristics of the input mel spectrogram. VocGAN is nearly as fast as MelGAN, but it significantly improves the quality and consistency of the output waveform. VocGAN applies a multi-scale waveform generator and a hierarchically-nested discriminator to learn multiple levels of acoustic properties in a balanced way. It also applies the joint conditional and unconditional objective, which has shown successful results in high-resolution image synthesis. In experiments, VocGAN synthesizes speech waveforms 416.7x faster on a GTX 1080Ti GPU and 3.24x faster on a CPU than real-time. Compared with MelGAN, it also exhibits significantly improved quality in multiple evaluation metrics including mean opinion score (MOS) with minimal additional overhead. Additionally, compared with Parallel WaveGAN, another recently developed high-fidelity vocoder, VocGAN is 6.98x faster on a CPU and exhibits higher MOS.

</details>

### [Quasi-Periodic Parallel WaveGAN: A Non-autoregressive Raw Waveform Generative Model with Pitch-dependent Dilated Convolution Neural Network](2007.12955.md)
**Yi-Chiao Wu, Tomoki Hayashi, Takuma Okamoto, Hisashi Kawai et al.** · 2020-07-25

<details>
<summary>Abstract</summary>

In this paper, we propose a quasi-periodic parallel WaveGAN (QPPWG) waveform generative model, which applies a quasi-periodic (QP) structure to a parallel WaveGAN (PWG) model using pitch-dependent dilated convolution networks (PDCNNs). PWG is a small-footprint GAN-based raw waveform generative model, whose generation time is much faster than real time because of its compact model and non-autoregressive (non-AR) and non-causal mechanisms. Although PWG achieves high-fidelity speech generation, the generic and simple network architecture lacks pitch controllability for an unseen auxiliary fundamental frequency ($F_{0}$) feature such as a scaled $F_{0}$. To improve the pitch controllability and speech modeling capability, we apply a QP structure with PDCNNs to PWG, which introduces pitch information to the network by dynamically changing the network architecture corresponding to the auxiliary $F_{0}$ feature. Both objective and subjective experimental results show that QPPWG outperforms PWG when the auxiliary $F_{0}$ feature is scaled. Moreover, analyses of the intermediate outputs of QPPWG also show better tractability and interpretability of QPPWG, which respectively models spectral and excitation-like signals using the cascaded fixed and adaptive blocks of the QP structure.

</details>

### [A Transfer Learning End-to-End ArabicText-To-Speech (TTS) Deep Architecture](2007.11541.md)
**Fady Fahmy, Mahmoud Khalil, Hazem Abbas** · 2020-07-22

<details>
<summary>Abstract</summary>

Speech synthesis is the artificial production of human speech. A typical text-to-speech system converts a language text into a waveform. There exist many English TTS systems that produce mature, natural, and human-like speech synthesizers. In contrast, other languages, including Arabic, have not been considered until recently. Existing Arabic speech synthesis solutions are slow, of low quality, and the naturalness of synthesized speech is inferior to the English synthesizers. They also lack essential speech key factors such as intonation, stress, and rhythm. Different works were proposed to solve those issues, including the use of concatenative methods such as unit selection or parametric methods. However, they required a lot of laborious work and domain expertise. Another reason for such poor performance of Arabic speech synthesizers is the lack of speech corpora, unlike English that has many publicly available corpora and audiobooks. This work describes how to generate high quality, natural, and human-like Arabic speech using an end-to-end neural deep network architecture. This work uses just $\langle$ text, audio $\rangle$ pairs with a relatively small amount of recorded audio samples with a total of 2.41 hours. It illustrates how to use English character embedding despite using diacritic Arabic characters as input and how to preprocess these audio samples to achieve the best results.

</details>

### [Translate Reverberated Speech to Anechoic Ones: Speech Dereverberation with BERT](2007.08052.md)
**Yang Jiao** · 2020-07-16

<details>
<summary>Abstract</summary>

Single channel speech dereverberation is considered in this work. Inspired by the recent success of Bidirectional Encoder Representations from Transformers (BERT) model in the domain of Natural Language Processing (NLP), we investigate its applicability as backbone sequence model to enhance reverberated speech signal. We present a variation of the basic BERT model: a pre-sequence network, which extracts local spectral-temporal information and/or provides order information, before the backbone sequence model. In addition, we use pre-trained neural vocoder for implicit phase reconstruction. To evaluate our method, we used the data from the 3rd CHiME challenge, and compare our results with other methods. Experiments show that the proposed method outperforms traditional method WPE, and achieve comparable performance with state-of-the-art BLSTM-based sequence models.

</details>

### [Neural MOS Prediction for Synthesized Speech Using Multi-Task Learning With Spoofing Detection and Spoofing Type Classification](2007.08267.md)
**Yeunju Choi, Youngmoon Jung, Hoirin Kim** · 2020-07-16

<details>
<summary>Abstract</summary>

Several studies have proposed deep-learning-based models to predict the mean opinion score (MOS) of synthesized speech, showing the possibility of replacing human raters. However, inter- and intra-rater variability in MOSs makes it hard to ensure the high performance of the models. In this paper, we propose a multi-task learning (MTL) method to improve the performance of a MOS prediction model using the following two auxiliary tasks: spoofing detection (SD) and spoofing type classification (STC). Besides, we use the focal loss to maximize the synergy between SD and STC for MOS prediction. Experiments using the MOS evaluation results of the Voice Conversion Challenge 2018 show that proposed MTL with two auxiliary tasks improves MOS prediction. Our proposed model achieves up to 11.6% relative improvement in performance over the baseline model.

</details>

### [Xiaomingbot: A Multilingual Robot News Reporter](2007.08005.md)
**Runxin Xu, Jun Cao, Mingxuan Wang, Jiaze Chen et al.** · 2020-07-12

<details>
<summary>Abstract</summary>

This paper proposes the building of Xiaomingbot, an intelligent, multilingual and multimodal software robot equipped with four integral capabilities: news generation, news translation, news reading and avatar animation. Its system summarizes Chinese news that it automatically generates from data tables. Next, it translates the summary or the full article into multiple languages, and reads the multilingual rendition through synthesized speech. Notably, Xiaomingbot utilizes a voice cloning technology to synthesize the speech trained from a real person's voice data in one input language. The proposed system enjoys several merits: it has an animated avatar, and is able to generate and read multilingual news. Since it was put into practice, Xiaomingbot has written over 600,000 articles, and gained over 150,000 followers on social media platforms.

</details>

### [Fast Griffin Lim based Waveform Generation Strategy for Text-to-Speech Synthesis](2007.05764.md)
**Ankit Sharma, Puneet Kumar, Vikas Maddukuri, Nagasai Madamshettib et al.** · 2020-07-11

<details>
<summary>Abstract</summary>

The performance of text-to-speech (TTS) systems heavily depends on spectrogram to waveform generation, also known as the speech reconstruction phase. The time required for the same is known as synthesis delay. In this paper, an approach to reduce speech synthesis delay has been proposed. It aims to enhance the TTS systems for real-time applications such as digital assistants, mobile phones, embedded devices, etc. The proposed approach applies Fast Griffin Lim Algorithm (FGLA) instead Griffin Lim algorithm (GLA) as vocoder in the speech synthesis phase. GLA and FGLA are both iterative, but the convergence rate of FGLA is faster than GLA. The proposed approach is tested on LJSpeech, Blizzard and Tatoeba datasets and the results for FGLA are compared against GLA and neural Generative Adversarial Network (GAN) based vocoder. The performance is evaluated based on synthesis delay and speech quality. A 36.58% reduction in speech synthesis delay has been observed. The quality of the output speech has improved, which is advocated by higher Mean opinion scores (MOS) and faster convergence with FGLA as opposed to GLA.

</details>

### [Quasi-Periodic WaveNet: An Autoregressive Raw Waveform Generative Model with Pitch-dependent Dilated Convolution Neural Network](2007.05663.md)
**Yi-Chiao Wu, Tomoki Hayashi, Patrick Lumban Tobing, Kazuhiro Kobayashi et al.** · 2020-07-11

<details>
<summary>Abstract</summary>

In this paper, a pitch-adaptive waveform generative model named Quasi-Periodic WaveNet (QPNet) is proposed to improve the limited pitch controllability of vanilla WaveNet (WN) using pitch-dependent dilated convolution neural networks (PDCNNs). Specifically, as a probabilistic autoregressive generation model with stacked dilated convolution layers, WN achieves high-fidelity audio waveform generation. However, the pure-data-driven nature and the lack of prior knowledge of audio signals degrade the pitch controllability of WN. For instance, it is difficult for WN to precisely generate the periodic components of audio signals when the given auxiliary fundamental frequency ($F_{0}$) features are outside the $F_{0}$ range observed in the training data. To address this problem, QPNet with two novel designs is proposed. First, the PDCNN component is applied to dynamically change the network architecture of WN according to the given auxiliary $F_{0}$ features. Second, a cascaded network structure is utilized to simultaneously model the long- and short-term dependencies of quasi-periodic signals such as speech. The performances of single-tone sinusoid and speech generations are evaluated. The experimental results show the effectiveness of the PDCNNs for unseen auxiliary $F_{0}$ features and the effectiveness of the cascaded structure for speech generation.

</details>

### [Prosodic Prominence and Boundaries in Sequence-to-Sequence Speech Synthesis](2006.15967.md)
**Antti Suni, Sofoklis Kakouros, Martti Vainio, Juraj Šimko** · 2020-06-29

<details>
<summary>Abstract</summary>

Recent advances in deep learning methods have elevated synthetic speech quality to human level, and the field is now moving towards addressing prosodic variation in synthetic speech.Despite successes in this effort, the state-of-the-art systems fall short of faithfully reproducing local prosodic events that give rise to, e.g., word-level emphasis and phrasal structure. This type of prosodic variation often reflects long-distance semantic relationships that are not accessible for end-to-end systems with a single sentence as their synthesis domain. One of the possible solutions might be conditioning the synthesized speech by explicit prosodic labels, potentially generated using longer portions of text. In this work we evaluate whether augmenting the textual input with such prosodic labels capturing word-level prominence and phrasal boundary strength can result in more accurate realization of sentence prosody. We use an automatic wavelet-based technique to extract such labels from speech material, and use them as an input to a tacotron-like synthesis system alongside textual information. The results of objective evaluation of synthesized speech show that using the prosodic labels significantly improves the output in terms of faithfulness of f0 and energy contours, in comparison with state-of-the-art implementations.

</details>

### [Normalizing Text using Language Modelling based on Phonetics and String Similarity](2006.14116.md)
**Fenil Doshi, Jimit Gandhi, Deep Gosalia, Sudhir Bagul** · 2020-06-25

<details>
<summary>Abstract</summary>

Social media networks and chatting platforms often use an informal version of natural text. Adversarial spelling attacks also tend to alter the input text by modifying the characters in the text. Normalizing these texts is an essential step for various applications like language translation and text to speech synthesis where the models are trained over clean regular English language. We propose a new robust model to perform text normalization. Our system uses the BERT language model to predict the masked words that correspond to the unnormalized words. We propose two unique masking strategies that try to replace the unnormalized words in the text with their root form using a unique score based on phonetic and string similarity metrics.We use human-centric evaluations where volunteers were asked to rank the normalized text. Our strategies yield an accuracy of 86.7% and 83.2% which indicates the effectiveness of our system in dealing with text normalization.

</details>

### [Recurrent Quantum Neural Networks](2006.14619.md)
**Johannes Bausch** · 2020-06-25

<details>
<summary>Abstract</summary>

Recurrent neural networks are the foundation of many sequence-to-sequence models in machine learning, such as machine translation and speech synthesis. In contrast, applied quantum computing is in its infancy. Nevertheless there already exist quantum machine learning models such as variational quantum eigensolvers which have been used successfully e.g. in the context of energy minimization tasks. In this work we construct a quantum recurrent neural network (QRNN) with demonstrable performance on non-trivial tasks such as sequence learning and integer digit classification. The QRNN cell is built from parametrized quantum neurons, which, in conjunction with amplitude amplification, create a nonlinear activation of polynomials of its inputs and cell state, and allow the extraction of a probability distribution over predicted classes at each step. To study the model's performance, we provide an implementation in pytorch, which allows the relatively efficient optimization of parametrized quantum circuits with thousands of parameters. We establish a QRNN training setup by benchmarking optimization hyperparameters, and analyse suitable network topologies for simple memorisation and sequence prediction tasks from Elman's seminal paper (1990) on temporal structure learning. We then proceed to evaluate the QRNN on MNIST classification, both by feeding the QRNN each image pixel-by-pixel; and by utilising modern data augmentation as preprocessing step. Finally, we analyse to what extent the unitary nature of the network counteracts the vanishing gradient problem that plagues many existing quantum classifiers and classical RNNs.

</details>

### [Articulatory-WaveNet: Autoregressive Model For Acoustic-to-Articulatory Inversion](2006.12594.md)
**Narjes Bozorg, Michael T. Johnson** · 2020-06-22

<details>
<summary>Abstract</summary>

This paper presents Articulatory-WaveNet, a new approach for acoustic-to-articulator inversion. The proposed system uses the WaveNet speech synthesis architecture, with dilated causal convolutional layers using previous values of the predicted articulatory trajectories conditioned on acoustic features. The system was trained and evaluated on the ElectroMagnetic Articulography corpus of Mandarin Accented English (EMA-MAE),consisting of 39 speakers including both native English speakers and native Mandarin speakers speaking English. Results show significant improvement in both correlation and RMSE between the generated and true articulatory trajectories for the new method, with an average correlation of 0.83, representing a 36% relative improvement over the 0.61 correlation obtained with a baseline Hidden Markov Model (HMM)-Gaussian Mixture Model (GMM) inversion framework. To the best of our knowledge, this paper presents the first application of a point-by-point waveform synthesis approach to the problem of acoustic-to-articulatory inversion and the results show improved performance compared to previous methods for speaker dependent acoustic to articulatory inversion.

</details>

### [Adversarial representation learning for private speech generation](2006.09114.md)
**David Ericsson, Adam Östberg, Edvin Listo Zec, John Martinsson et al.** · 2020-06-16

<details>
<summary>Abstract</summary>

As more and more data is collected in various settings across organizations, companies, and countries, there has been an increase in the demand of user privacy. Developing privacy preserving methods for data analytics is thus an important area of research. In this work we present a model based on generative adversarial networks (GANs) that learns to obfuscate specific sensitive attributes in speech data. We train a model that learns to hide sensitive information in the data, while preserving the meaning in the utterance. The model is trained in two steps: first to filter sensitive information in the spectrogram domain, and then to generate new and private information independent of the filtered one. The model is based on a U-Net CNN that takes mel-spectrograms as input. A MelGAN is used to invert the spectrograms back to raw audio waveforms. We show that it is possible to hide sensitive information such as gender by generating new data, trained adversarially to maintain utility and realism.

</details>

### [SE-MelGAN -- Speaker Agnostic Rapid Speech Enhancement](2006.07637.md)
**Luka Chkhetiani, Levan Bejanidze** · 2020-06-13

<details>
<summary>Abstract</summary>

Recent advancement in Generative Adversarial Networks in speech synthesis domain[3],[2] have shown, that it's possible to train GANs [8] in a reliable manner for high quality coherent waveform generation from mel-spectograms. We propose that it is possible to transfer the MelGAN's [3] robustness in learning speech features to speech enhancement and noise reduction domain without any model modification tasks. Our proposed method generalizes over multi-speaker speech dataset and is able to robustly handle unseen background noises during the inference. Also, we show that by increasing the batch size for this particular approach not only yields better speech results, but generalizes over multi-speaker dataset easily and leads to faster convergence. Additionally, it outperforms previous state of the art GAN approach for speech enhancement SEGAN [5] in two domains: 1. quality ; 2. speed. Proposed method runs at more than 100x faster than realtime on GPU and more than 2x faster than real time on CPU without any hardware optimization tasks, right at the speed of MelGAN [3].

</details>

### [Generic Indic Text-to-speech Synthesisers with Rapid Adaptation in an End-to-end Framework](2006.06971.md)
**Anusha Prakash, Hema A Murthy** · 2020-06-12

<details>
<summary>Abstract</summary>

Building text-to-speech (TTS) synthesisers for Indian languages is a difficult task owing to a large number of active languages. Indian languages can be classified into a finite set of families, prominent among them, Indo-Aryan and Dravidian. The proposed work exploits this property to build a generic TTS system using multiple languages from the same family in an end-to-end framework. Generic systems are quite robust as they are capable of capturing a variety of phonotactics across languages. These systems are then adapted to a new language in the same family using small amounts of adaptation data. Experiments indicate that good quality TTS systems can be built using only 7 minutes of adaptation data. An average degradation mean opinion score of 3.98 is obtained for the adapted TTSes. Extensive analysis of systematic interactions between languages in the generic TTSes is carried out. x-vectors are included as speaker embedding to synthesise text in a particular speaker's voice. An interesting observation is that the prosody of the target speaker's voice is preserved. These results are quite promising as they indicate the capability of generic TTSes to handle speaker and language switching seamlessly, along with the ease of adaptation to a new language.

</details>

### [Neural voice cloning with a few low-quality samples](2006.06940.md)
**Sunghee Jung, Hoirin Kim** · 2020-06-12

<details>
<summary>Abstract</summary>

In this paper, we explore the possibility of speech synthesis from low quality found data using only limited number of samples of target speaker. We try to extract only the speaker embedding from found data of target speaker unlike previous works which tries to train the entire text-to-speech system on found data. Also, the two speaker mimicking approaches which are adaptation and speaker-encoder-based are applied on newly released LibriTTS dataset and previously released VCTK corpus to examine the impact of speaker variety on clarity and target-speaker-similarity .

</details>

### [Non-parallel voice conversion based on source-to-target direct mapping](2006.06937.md)
**Sunghee Jung, Youngjoo Suh, Yeunju Choi, Hoirin Kim** · 2020-06-12

<details>
<summary>Abstract</summary>

Recent works of utilizing phonetic posteriograms (PPGs) for non-parallel voice conversion have significantly increased the usability of voice conversion since the source and target DBs are no longer required for matching contents. In this approach, the PPGs are used as the linguistic bridge between source and target speaker features. However, this PPG-based non-parallel voice conversion has some limitation that it needs two cascading networks at conversion time, making it less suitable for real-time applications and vulnerable to source speaker intelligibility at conversion stage. To address this limitation, we propose a new non-parallel voice conversion technique that employs a single neural network for direct source-to-target voice parameter mapping. With this single network structure, the proposed approach can reduce both conversion time and number of network parameters, which can be especially important factors in embedded or real-time environments. Additionally, it improves the quality of voice conversion by skipping the phone recognizer at conversion stage. It can effectively prevent possible loss of phonetic information the PPG-based indirect method suffers. Experiments show that our approach reduces number of network parameters and conversion time by 41.9% and 44.5%, respectively, with improved voice similarity over the original PPG-based method.

</details>

### [FastPitch: Parallel Text-to-speech with Pitch Prediction](2006.06873.md)
**Adrian Łańcucki** · 2020-06-11

<details>
<summary>Abstract</summary>

We present FastPitch, a fully-parallel text-to-speech model based on FastSpeech, conditioned on fundamental frequency contours. The model predicts pitch contours during inference. By altering these predictions, the generated speech can be more expressive, better match the semantic of the utterance, and in the end more engaging to the listener. Uniformly increasing or decreasing pitch with FastPitch generates speech that resembles the voluntary modulation of voice. Conditioning on frequency contours improves the overall quality of synthesized speech, making it comparable to state-of-the-art. It does not introduce an overhead, and FastPitch retains the favorable, fully-parallel Transformer architecture, with over 900x real-time factor for mel-spectrogram synthesis of a typical utterance.

</details>

### [MultiSpeech: Multi-Speaker Text to Speech with Transformer](2006.04664.md)
**Mingjian Chen, Xu Tan, Yi Ren, Jin Xu et al.** · 2020-06-08

<details>
<summary>Abstract</summary>

Transformer-based text to speech (TTS) model (e.g., Transformer TTS~\cite{li2019neural}, FastSpeech~\cite{ren2019fastspeech}) has shown the advantages of training and inference efficiency over RNN-based model (e.g., Tacotron~\cite{shen2018natural}) due to its parallel computation in training and/or inference. However, the parallel computation increases the difficulty while learning the alignment between text and speech in Transformer, which is further magnified in the multi-speaker scenario with noisy data and diverse speakers, and hinders the applicability of Transformer for multi-speaker TTS. In this paper, we develop a robust and high-quality multi-speaker Transformer TTS system called MultiSpeech, with several specially designed components/techniques to improve text-to-speech alignment: 1) a diagonal constraint on the weight matrix of encoder-decoder attention in both training and inference; 2) layer normalization on phoneme embedding in encoder to better preserve position information; 3) a bottleneck in decoder pre-net to prevent copy between consecutive speech frames. Experiments on VCTK and LibriTTS multi-speaker datasets demonstrate the effectiveness of MultiSpeech: 1) it synthesizes more robust and better quality multi-speaker voice than naive Transformer based TTS; 2) with a MutiSpeech model as the teacher, we obtain a strong multi-speaker FastSpeech model with almost zero quality degradation while enjoying extremely fast inference speed.

</details>

### [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](2006.04558.md)
**Yi Ren, Chenxu Hu, Xu Tan, Tao Qin et al.** · 2020-06-08

<details>
<summary>Abstract</summary>

Non-autoregressive text to speech (TTS) models such as FastSpeech can synthesize speech significantly faster than previous autoregressive models with comparable quality. The training of FastSpeech model relies on an autoregressive teacher model for duration prediction (to provide more information as input) and knowledge distillation (to simplify the data distribution in output), which can ease the one-to-many mapping problem (i.e., multiple speech variations correspond to the same text) in TTS. However, FastSpeech has several disadvantages: 1) the teacher-student distillation pipeline is complicated and time-consuming, 2) the duration extracted from the teacher model is not accurate enough, and the target mel-spectrograms distilled from teacher model suffer from information loss due to data simplification, both of which limit the voice quality. In this paper, we propose FastSpeech 2, which addresses the issues in FastSpeech and better solves the one-to-many mapping problem in TTS by 1) directly training the model with ground-truth target instead of the simplified output from teacher, and 2) introducing more variation information of speech (e.g., pitch, energy and more accurate duration) as conditional inputs. Specifically, we extract duration, pitch and energy from speech waveform and directly take them as conditional inputs in training and use predicted values in inference. We further design FastSpeech 2s, which is the first attempt to directly generate speech waveform from text in parallel, enjoying the benefit of fully end-to-end inference. Experimental results show that 1) FastSpeech 2 achieves a 3x training speed-up over FastSpeech, and FastSpeech 2s enjoys even faster inference speed; 2) FastSpeech 2 and 2s outperform FastSpeech in voice quality, and FastSpeech 2 can even surpass autoregressive models. Audio samples are available at https://speechresearch.github.io/fastspeech2/.

</details>

### [WaveNODE: A Continuous Normalizing Flow for Speech Synthesis](2006.04598.md)
**Hyeongju Kim, Hyeonseung Lee, Woo Hyun Kang, Sung Jun Cheon et al.** · 2020-06-08

<details>
<summary>Abstract</summary>

In recent years, various flow-based generative models have been proposed to generate high-fidelity waveforms in real-time. However, these models require either a well-trained teacher network or a number of flow steps making them memory-inefficient. In this paper, we propose a novel generative model called WaveNODE which exploits a continuous normalizing flow for speech synthesis. Unlike the conventional models, WaveNODE places no constraint on the function used for flow operation, thus allowing the usage of more flexible and complex functions. Moreover, WaveNODE can be optimized to maximize the likelihood without requiring any teacher network or auxiliary loss terms. We experimentally show that WaveNODE achieves comparable performance with fewer parameters compared to the conventional flow-based vocoders.

</details>

### [Zero resource speech synthesis using transcripts derived from perceptual acoustic units](2006.04372.md)
**Karthik Pandia D S, Hema A Murthy** · 2020-06-08

<details>
<summary>Abstract</summary>

Zerospeech synthesis is the task of building vocabulary independent speech synthesis systems, where transcriptions are not available for training data. It is, therefore, necessary to convert training data into a sequence of fundamental acoustic units that can be used for synthesis during the test. This paper attempts to discover, and model perceptual acoustic units consisting of steady-state, and transient regions in speech. The transients roughly correspond to CV, VC units, while the steady-state corresponds to sonorants and fricatives. The speech signal is first preprocessed by segmenting the same into CVC-like units using a short-term energy-like contour. These CVC segments are clustered using a connected components-based graph clustering technique. The clustered CVC segments are initialized such that the onset (CV) and decays (VC) correspond to transients, and the rhyme corresponds to steady-states. Following this initialization, the units are allowed to re-organise on the continuous speech into a final set of AUs in an HMM-GMM framework. AU sequences thus obtained are used to train synthesis models. The performance of the proposed approach is evaluated on the Zerospeech 2019 challenge database. Subjective and objective scores show that reasonably good quality synthesis with low bit rate encoding can be achieved using the proposed AUs.

</details>

### [VQVC+: One-Shot Voice Conversion by Vector Quantization and U-Net architecture](2006.04154.md)
**Da-Yi Wu, Yen-Hao Chen, Hung-Yi Lee** · 2020-06-07

<details>
<summary>Abstract</summary>

Voice conversion (VC) is a task that transforms the source speaker's timbre, accent, and tones in audio into another one's while preserving the linguistic content. It is still a challenging work, especially in a one-shot setting. Auto-encoder-based VC methods disentangle the speaker and the content in input speech without given the speaker's identity, so these methods can further generalize to unseen speakers. The disentangle capability is achieved by vector quantization (VQ), adversarial training, or instance normalization (IN). However, the imperfect disentanglement may harm the quality of output speech. In this work, to further improve audio quality, we use the U-Net architecture within an auto-encoder-based VC system. We find that to leverage the U-Net architecture, a strong information bottleneck is necessary. The VQ-based method, which quantizes the latent vectors, can serve the purpose. The objective and the subjective evaluations show that the proposed method performs well in both audio naturalness and speaker similarity.

</details>

### [End-to-End Adversarial Text-to-Speech](2006.03575.md)
**Jeff Donahue, Sander Dieleman, Mikołaj Bińkowski, Erich Elsen et al.** · 2020-06-05

<details>
<summary>Abstract</summary>

Modern text-to-speech synthesis pipelines typically involve multiple processing stages, each of which is designed or learnt independently from the rest. In this work, we take on the challenging task of learning to synthesise speech from normalised text or phonemes in an end-to-end manner, resulting in models which operate directly on character or phoneme input sequences and produce raw speech audio outputs. Our proposed generator is feed-forward and thus efficient for both training and inference, using a differentiable alignment scheme based on token length prediction. It learns to produce high fidelity audio through a combination of adversarial feedback and prediction losses constraining the generated audio to roughly match the ground truth in terms of its total duration and mel-spectrogram. To allow the model to capture temporal variation in the generated audio, we employ soft dynamic time warping in the spectrogram-based prediction loss. The resulting model achieves a mean opinion score exceeding 4 on a 5 point scale, which is comparable to the state-of-the-art models relying on multi-stage training and additional supervision.

</details>

### [Mandarin Prosody Boundary Prediction based on Sequence-to-sequence Model](s2:0583653837c479828ec355f88e9ecb679bcdc9eb.md)
**Yajing Yan, Jiaolong Jiang, Hongwu Yang** · 2020-06-01

<details>
<summary>Abstract</summary>

The prediction of prosodic structure of sentences is the key for improving the naturalness of Mandarin speech synthesis. In this paper, we proposed a sequence-to-sequence (seq2seq) model-based method to improve the predictive accuracy of the prosodic boundaries from Chinese sentence. A large-scale text corpus including 100,000 Chinese sentences is collected that is manually labelled the part-of-speech and the boundaries of the prosodic words and prosodic phrases under the guidance of a linguistic expert. By analyzing the text corpus, the shallow features such as part-of-speech, word length and word embedding are selected as the input features of the seq2seq model. At the same time, a new deep feature named syntactic hierarchical number (SHN) is proposed to predict the boundary of prosodic phrases, which describes the relationship between syntactic structure and prosodic structure. Finally, we get the seq2seq model by training the labelled text corpus to predict the boundaries of prosodic words and prosodic phrases. The experimental results show that the seq2seq model achieves F1-score of 97.15% in prosodic word and 82.98% in prosodic phrase boundary prediction. Compared to the other models, our proposed method are more effective on the prediction of prosodic structure, which can be applied to the front-end of speech synthesis.

</details>

### [A comparison of Vietnamese Statistical Parametric Speech Synthesis Systems](2005.12962.md)
**Huy Kinh Phan, Viet Lam Phung, Tuan Anh Dinh, Bao Quoc Nguyen** · 2020-05-26

<details>
<summary>Abstract</summary>

In recent years, statistical parametric speech synthesis (SPSS) systems have been widely utilized in many interactive speech-based systems (e.g.~Amazon's Alexa, Bose's headphones). To select a suitable SPSS system, both speech quality and performance efficiency (e.g.~decoding time) must be taken into account. In the paper, we compared four popular Vietnamese SPSS techniques using: 1) hidden Markov models (HMM), 2) deep neural networks (DNN), 3) generative adversarial networks (GAN), and 4) end-to-end (E2E) architectures, which consists of Tacontron~2 and WaveGlow vocoder in terms of speech quality and performance efficiency. We showed that the E2E systems accomplished the best quality, but required the power of GPU to achieve real-time performance. We also showed that the HMM-based system had inferior speech quality, but it was the most efficient system. Surprisingly, the E2E systems were more efficient than the DNN and GAN in inference on GPU. Surprisingly, the GAN-based system did not outperform the DNN in term of quality.

</details>

### [Noise Robust TTS for Low Resource Speakers using Pre-trained Model and Speech Enhancement](2005.12531.md)
**Dongyang Dai, Li Chen, Yuping Wang, Mu Wang et al.** · 2020-05-26

<details>
<summary>Abstract</summary>

With the popularity of deep neural network, speech synthesis task has achieved significant improvements based on the end-to-end encoder-decoder framework in the recent days. More and more applications relying on speech synthesis technology have been widely used in our daily life. Robust speech synthesis model depends on high quality and customized data which needs lots of collecting efforts. It is worth investigating how to take advantage of low-quality and low resource voice data which can be easily obtained from the Internet for usage of synthesizing personalized voice. In this paper, the proposed end-to-end speech synthesis model uses both speaker embedding and noise representation as conditional inputs to model speaker and noise information respectively. Firstly, the speech synthesis model is pre-trained with both multi-speaker clean data and noisy augmented data; then the pre-trained model is adapted on noisy low-resource new speaker data; finally, by setting the clean speech condition, the model can synthesize the new speaker's clean voice. Experimental results show that the speech generated by the proposed approach has better subjective evaluation results than the method directly fine-tuning pre-trained multi-speaker speech synthesis model with denoised new speaker data.

</details>

### [Transformer VQ-VAE for Unsupervised Unit Discovery and Speech Synthesis: ZeroSpeech 2020 Challenge](2005.11676.md)
**Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2020-05-24

<details>
<summary>Abstract</summary>

In this paper, we report our submitted system for the ZeroSpeech 2020 challenge on Track 2019. The main theme in this challenge is to build a speech synthesizer without any textual information or phonetic labels. In order to tackle those challenges, we build a system that must address two major components such as 1) given speech audio, extract subword units in an unsupervised way and 2) re-synthesize the audio from novel speakers. The system also needs to balance the codebook performance between the ABX error rate and the bitrate compression rate. Our main contribution here is we proposed Transformer-based VQ-VAE for unsupervised unit discovery and Transformer-based inverter for the speech synthesis given the extracted codebook. Additionally, we also explored several regularization methods to improve performance even further.

</details>

### [How Does That Sound? Multi-Language SpokenName2Vec Algorithm Using Speech Generation and Deep Learning](2005.11838.md)
**Aviad Elyashar, Rami Puzis, Michael Fire** · 2020-05-24

<details>
<summary>Abstract</summary>

Searching for information about a specific person is an online activity frequently performed by many users. In most cases, users are aided by queries containing a name and sending back to the web search engines for finding their will. Typically, Web search engines provide just a few accurate results associated with a name-containing query. Currently, most solutions for suggesting synonyms in online search are based on pattern matching and phonetic encoding, however very often, the performance of such solutions is less than optimal. In this paper, we propose SpokenName2Vec, a novel and generic approach which addresses the similar name suggestion problem by utilizing automated speech generation, and deep learning to produce spoken name embeddings. This sophisticated and innovative embeddings captures the way people pronounce names in any language and accent. Utilizing the name pronunciation can be helpful for both differentiating and detecting names that sound alike, but are written differently. The proposed approach was demonstrated on a large-scale dataset consisting of 250,000 forenames and evaluated using a machine learning classifier and 7,399 names with their verified synonyms. The performance of the proposed approach was found to be superior to 10 other algorithms evaluated in this study, including well used phonetic and string similarity algorithms, and two recently proposed algorithms. The results obtained suggest that the proposed approach could serve as a useful and valuable tool for solving the similar name suggestion problem.

</details>

### [Glow-TTS: A Generative Flow for Text-to-Speech via Monotonic Alignment Search](2005.11129.md)
**Jaehyeon Kim, Sungwon Kim, Jungil Kong, Sungroh Yoon** · 2020-05-22

<details>
<summary>Abstract</summary>

Recently, text-to-speech (TTS) models such as FastSpeech and ParaNet have been proposed to generate mel-spectrograms from text in parallel. Despite the advantage, the parallel TTS models cannot be trained without guidance from autoregressive TTS models as their external aligners. In this work, we propose Glow-TTS, a flow-based generative model for parallel TTS that does not require any external aligner. By combining the properties of flows and dynamic programming, the proposed model searches for the most probable monotonic alignment between text and the latent representation of speech on its own. We demonstrate that enforcing hard monotonic alignments enables robust TTS, which generalizes to long utterances, and employing generative flows enables fast, diverse, and controllable speech synthesis. Glow-TTS obtains an order-of-magnitude speed-up over the autoregressive model, Tacotron 2, at synthesis with comparable speech quality. We further show that our model can be easily extended to a multi-speaker setting.

</details>

### [NAUTILUS: a Versatile Voice Cloning System](2005.11004.md)
**Hieu-Thi Luong, Junichi Yamagishi** · 2020-05-22

<details>
<summary>Abstract</summary>

We introduce a novel speech synthesis system, called NAUTILUS, that can generate speech with a target voice either from a text input or a reference utterance of an arbitrary source speaker. By using a multi-speaker speech corpus to train all requisite encoders and decoders in the initial training stage, our system can clone unseen voices using untranscribed speech of target speakers on the basis of the backpropagation algorithm. Moreover, depending on the data circumstance of the target speaker, the cloning strategy can be adjusted to take advantage of additional data and modify the behaviors of text-to-speech (TTS) and/or voice conversion (VC) systems to accommodate the situation. We test the performance of the proposed framework by using deep convolution layers to model the encoders, decoders and WaveNet vocoder. Evaluations show that it achieves comparable quality with state-of-the-art TTS and VC systems when cloning with just five minutes of untranscribed speech. Moreover, it is demonstrated that the proposed framework has the ability to switch between TTS and VC with high speaker consistency, which will be useful for many applications.

</details>

### [Cross-lingual Multispeaker Text-to-Speech under Limited-Data Scenario](2005.10441.md)
**Zexin Cai, Yaogen Yang, Ming Li** · 2020-05-21

<details>
<summary>Abstract</summary>

Modeling voices for multiple speakers and multiple languages in one text-to-speech system has been a challenge for a long time. This paper presents an extension on Tacotron2 to achieve bilingual multispeaker speech synthesis when there are limited data for each language. We achieve cross-lingual synthesis, including code-switching cases, between English and Mandarin for monolingual speakers. The two languages share the same phonemic representations for input, while the language attribute and the speaker identity are independently controlled by language tokens and speaker embeddings, respectively. In addition, we investigate the model's performance on the cross-lingual synthesis, with and without a bilingual dataset during training. With the bilingual dataset, not only can the model generate high-fidelity speech for all speakers concerning the language they speak, but also can generate accented, yet fluent and intelligible speech for monolingual speakers regarding non-native language. For example, the Mandarin speaker can speak English fluently. Furthermore, the model trained with bilingual dataset is robust for code-switching text-to-speech, as shown in our results and provided samples.{https://caizexin.github.io/mlms-syn-samples/index.html}.

</details>

### [Conversational End-to-End TTS for Voice Agent](2005.10438.md)
**Haohan Guo, Shaofei Zhang, Frank K. Soong, Lei He et al.** · 2020-05-21

<details>
<summary>Abstract</summary>

End-to-end neural TTS has achieved superior performance on reading style speech synthesis. However, it's still a challenge to build a high-quality conversational TTS due to the limitations of the corpus and modeling capability. This study aims at building a conversational TTS for a voice agent under sequence to sequence modeling framework. We firstly construct a spontaneous conversational speech corpus well designed for the voice agent with a new recording scheme ensuring both recording quality and conversational speaking style. Secondly, we propose a conversation context-aware end-to-end TTS approach which has an auxiliary encoder and a conversational context encoder to reinforce the information about the current utterance and its context in a conversation as well. Experimental results show that the proposed methods produce more natural prosody in accordance with the conversational context, with significant preference gains at both utterance-level and conversation-level. Moreover, we find that the model has the ability to express some spontaneous behaviors, like fillers and repeated words, which makes the conversational speaking style more realistic.

</details>

### [Investigation of learning abilities on linguistic features in sequence-to-sequence text-to-speech synthesis](2005.10390.md)
**Yusuke Yasuda, Xin Wang, Junichi Yamagishi** · 2020-05-20

<details>
<summary>Abstract</summary>

Neural sequence-to-sequence text-to-speech synthesis (TTS) can produce high-quality speech directly from text or simple linguistic features such as phonemes. Unlike traditional pipeline TTS, the neural sequence-to-sequence TTS does not require manually annotated and complicated linguistic features such as part-of-speech tags and syntactic structures for system training. However, it must be carefully designed and well optimized so that it can implicitly extract useful linguistic features from the input features. In this paper we investigate under what conditions the neural sequence-to-sequence TTS can work well in Japanese and English along with comparisons with deep neural network (DNN) based pipeline TTS systems. Unlike past comparative studies, the pipeline systems also use autoregressive probabilistic modeling and a neural vocoder. We investigated systems from three aspects: a) model architecture, b) model parameter size, and c) language. For the model architecture aspect, we adopt modified Tacotron systems that we previously proposed and their variants using an encoder from Tacotron or Tacotron2. For the model parameter size aspect, we investigate two model parameter sizes. For the language aspect, we conduct listening tests in both Japanese and English to see if our findings can be generalized across languages. Our experiments suggest that a) a neural sequence-to-sequence TTS system should have a sufficient number of model parameters to produce high quality speech, b) it should also use a powerful encoder when it takes characters as inputs, and c) the encoder still has a room for improvement and needs to have an improved architecture to learn supra-segmental features more appropriately.

</details>

### [Improving Accent Conversion with Reference Encoder and End-To-End Text-To-Speech](2005.09271.md)
**Wenjie Li, Benlai Tang, Xiang Yin, Yushi Zhao et al.** · 2020-05-19

<details>
<summary>Abstract</summary>

Accent conversion (AC) transforms a non-native speaker's accent into a native accent while maintaining the speaker's voice timbre. In this paper, we propose approaches to improving accent conversion applicability, as well as quality. First of all, we assume no reference speech is available at the conversion stage, and hence we employ an end-to-end text-to-speech system that is trained on native speech to generate native reference speech. To improve the quality and accent of the converted speech, we introduce reference encoders which make us capable of utilizing multi-source information. This is motivated by acoustic features extracted from native reference and linguistic information, which are complementary to conventional phonetic posteriorgrams (PPGs), so they can be concatenated as features to improve a baseline system based only on PPGs. Moreover, we optimize model architecture using GMM-based attention instead of windowed attention to elevate synthesized performance. Experimental results indicate when the proposed techniques are applied the integrated system significantly raises the scores of acoustic quality (30$\%$ relative increase in mean opinion score) and native accent (68$\%$ relative preference) while retaining the voice identity of the non-native speaker.

</details>

### [Bayesian Subspace HMM for the Zerospeech 2020 Challenge](2005.09282.md)
**Bolaji Yusuf, Lucas Ondel** · 2020-05-19

<details>
<summary>Abstract</summary>

In this paper we describe our submission to the Zerospeech 2020 challenge, where the participants are required to discover latent representations from unannotated speech, and to use those representations to perform speech synthesis, with synthesis quality used as a proxy metric for the unit quality. In our system, we use the Bayesian Subspace Hidden Markov Model (SHMM) for unit discovery. The SHMM models each unit as an HMM whose parameters are constrained to lie in a low dimensional subspace of the total parameter space which is trained to model phonetic variability. Our system compares favorably with the baseline on the human-evaluated character error rate while maintaining significantly lower unit bitrate.

</details>

### [Vector-quantized neural networks for acoustic unit discovery in the ZeroSpeech 2020 challenge](2005.09409.md)
**Benjamin van Niekerk, Leanne Nortje, Herman Kamper** · 2020-05-19

<details>
<summary>Abstract</summary>

In this paper, we explore vector quantization for acoustic unit discovery. Leveraging unlabelled data, we aim to learn discrete representations of speech that separate phonetic content from speaker-specific details. We propose two neural models to tackle this challenge - both use vector quantization to map continuous features to a finite set of codes. The first model is a type of vector-quantized variational autoencoder (VQ-VAE). The VQ-VAE encodes speech into a sequence of discrete units before reconstructing the audio waveform. Our second model combines vector quantization with contrastive predictive coding (VQ-CPC). The idea is to learn a representation of speech by predicting future acoustic units. We evaluate the models on English and Indonesian data for the ZeroSpeech 2020 challenge. In ABX phone discrimination tests, both models outperform all submissions to the 2019 and 2020 challenges, with a relative improvement of more than 30%. The models also perform competitively on a downstream voice conversion task. Of the two, VQ-CPC performs slightly better in general and is simpler and faster to train. Finally, probing experiments show that vector quantization is an effective bottleneck, forcing the models to discard speaker information.

</details>

### [Transferring Source Style in Non-Parallel Voice Conversion](2005.09178.md)
**Songxiang Liu, Yuewen Cao, Shiyin Kang, Na Hu et al.** · 2020-05-19

<details>
<summary>Abstract</summary>

Voice conversion (VC) techniques aim to modify speaker identity of an utterance while preserving the underlying linguistic information. Most VC approaches ignore modeling of the speaking style (e.g. emotion and emphasis), which may contain the factors intentionally added by the speaker and should be retained during conversion. This study proposes a sequence-to-sequence based non-parallel VC approach, which has the capability of transferring the speaking style from the source speech to the converted speech by explicitly modeling. Objective evaluation and subjective listening tests show superiority of the proposed VC approach in terms of speech naturalness and speaker similarity of the converted speech. Experiments are also conducted to show the source-style transferability of the proposed approach.

</details>

### [A Cyclical Post-filtering Approach to Mismatch Refinement of Neural Vocoder for Text-to-speech Systems](2005.08659.md)
**Yi-Chiao Wu, Patrick Lumban Tobing, Kazuki Yasuhara, Noriyuki Matsunaga et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

Recently, the effectiveness of text-to-speech (TTS) systems combined with neural vocoders to generate high-fidelity speech has been shown. However, collecting the required training data and building these advanced systems from scratch are time and resource consuming. An economical approach is to develop a neural vocoder to enhance the speech generated by existing or low-cost TTS systems. Nonetheless, this approach usually suffers from two issues: 1) temporal mismatches between TTS and natural waveforms and 2) acoustic mismatches between training and testing data. To address these issues, we adopt a cyclic voice conversion (VC) model to generate temporally matched pseudo-VC data for training and acoustically matched enhanced data for testing the neural vocoders. Because of the generality, this framework can be applied to arbitrary TTS systems and neural vocoders. In this paper, we apply the proposed method with a state-of-the-art WaveNet vocoder for two different basic TTS systems, and both objective and subjective experimental results confirm the effectiveness of the proposed framework.

</details>

### [Attentron: Few-Shot Text-to-Speech Utilizing Attention-Based Variable-Length Embedding](2005.08484.md)
**Seungwoo Choi, Seungju Han, Dongyoung Kim, Sungjoo Ha** · 2020-05-18

<details>
<summary>Abstract</summary>

On account of growing demands for personalization, the need for a so-called few-shot TTS system that clones speakers with only a few data is emerging. To address this issue, we propose Attentron, a few-shot TTS model that clones voices of speakers unseen during training. It introduces two special encoders, each serving different purposes. A fine-grained encoder extracts variable-length style information via an attention mechanism, and a coarse-grained encoder greatly stabilizes the speech synthesis, circumventing unintelligible gibberish even for synthesizing speech of unseen speakers. In addition, the model can scale out to an arbitrary number of reference audios to improve the quality of the synthesized speech. According to our experiments, including a human evaluation, the proposed model significantly outperforms state-of-the-art models when generating speech for unseen speakers in terms of speaker similarity and quality.

</details>

### [MoBoAligner: a Neural Alignment Model for Non-autoregressive TTS with Monotonic Boundary Search](2005.08528.md)
**Naihan Li, Shujie Liu, Yanqing Liu, Sheng Zhao et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

To speed up the inference of neural speech synthesis, non-autoregressive models receive increasing attention recently. In non-autoregressive models, additional durations of text tokens are required to make a hard alignment between the encoder and the decoder. The duration-based alignment plays a crucial role since it controls the correspondence between text tokens and spectrum frames and determines the rhythm and speed of synthesized audio. To get better duration-based alignment and improve the quality of non-autoregressive speech synthesis, in this paper, we propose a novel neural alignment model named MoboAligner. Given the pairs of the text and mel spectrum, MoboAligner tries to identify the boundaries of text tokens in the given mel spectrum frames based on the token-frame similarity in the neural semantic space with an end-to-end framework. With these boundaries, durations can be extracted and used in the training of non-autoregressive TTS models. Compared with the duration extracted by TransformerTTS, MoboAligner brings improvement for the non-autoregressive TTS model on MOS (3.74 comparing to FastSpeech's 3.44). Besides, MoboAligner is task-specified and lightweight, which reduces the parameter number by 45% and the training time consuming by 30%.

</details>

### [Quasi-Periodic Parallel WaveGAN Vocoder: A Non-autoregressive Pitch-dependent Dilated Convolution Model for Parametric Speech Generation](2005.08654.md)
**Yi-Chiao Wu, Tomoki Hayashi, Takuma Okamoto, Hisashi Kawai et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

In this paper, we propose a parallel WaveGAN (PWG)-like neural vocoder with a quasi-periodic (QP) architecture to improve the pitch controllability of PWG. PWG is a compact non-autoregressive (non-AR) speech generation model, whose generative speed is much faster than real time. While utilizing PWG as a vocoder to generate speech on the basis of acoustic features such as spectral and prosodic features, PWG generates high-fidelity speech. However, when the input acoustic features include unseen pitches, the pitch accuracy of PWG-generated speech degrades because of the fixed and generic network of PWG without prior knowledge of speech periodicity. The proposed QPPWG adopts a pitch-dependent dilated convolution network (PDCNN) module, which introduces the pitch information into PWG via the dynamically changed network architecture, to improve the pitch controllability and speech modeling capability of vanilla PWG. Both objective and subjective evaluation results show the higher pitch accuracy and comparable speech quality of QPPWG-generated speech when the QPPWG model size is only 70 % of that of vanilla PWG.

</details>

### [Defending Your Voice: Adversarial Attack on Voice Conversion](2005.08781.md)
**Chien-yu Huang, Yist Y. Lin, Hung-yi Lee, Lin-shan Lee** · 2020-05-18

<details>
<summary>Abstract</summary>

Substantial improvements have been achieved in recent years in voice conversion, which converts the speaker characteristics of an utterance into those of another speaker without changing the linguistic content of the utterance. Nonetheless, the improved conversion technologies also led to concerns about privacy and authentication. It thus becomes highly desired to be able to prevent one's voice from being improperly utilized with such voice conversion technologies. This is why we report in this paper the first known attempt to perform adversarial attack on voice conversion. We introduce human imperceptible noise into the utterances of a speaker whose voice is to be defended. Given these adversarial examples, voice conversion models cannot convert other utterances so as to sound like being produced by the defended speaker. Preliminary experiments were conducted on two currently state-of-the-art zero-shot voice conversion models. Objective and subjective evaluation results in both white-box and black-box scenarios are reported. It was shown that the speaker characteristics of the converted utterances were made obviously different from those of the defended speaker, while the adversarial examples of the defended speaker are not distinguishable from the authentic utterances.

</details>

### [Robust Training of Vector Quantized Bottleneck Models](2005.08520.md)
**Adrian Łańcucki, Jan Chorowski, Guillaume Sanchez, Ricard Marxer et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

In this paper we demonstrate methods for reliable and efficient training of discrete representation using Vector-Quantized Variational Auto-Encoder models (VQ-VAEs). Discrete latent variable models have been shown to learn nontrivial representations of speech, applicable to unsupervised voice conversion and reaching state-of-the-art performance on unit discovery tasks. For unsupervised representation learning, they became viable alternatives to continuous latent variable models such as the Variational Auto-Encoder (VAE). However, training deep discrete variable models is challenging, due to the inherent non-differentiability of the discretization operation. In this paper we focus on VQ-VAE, a state-of-the-art discrete bottleneck model shown to perform on par with its continuous counterparts. It quantizes encoder outputs with on-line $k$-means clustering. We show that the codebook learning can suffer from poor initialization and non-stationarity of clustered encoder outputs. We demonstrate that these can be successfully overcome by increasing the learning rate for the codebook and periodic date-dependent codeword re-initialization. As a result, we achieve more robust training across different tasks, and significantly increase the usage of latent codewords even for large codebooks. This has practical benefit, for instance, in unsupervised representation learning, where large codebooks may lead to disentanglement of latent representations.

</details>

### [Many-to-Many Voice Transformer Network](2005.08445.md)
**Hirokazu Kameoka, Wen-Chin Huang, Kou Tanaka, Takuhiro Kaneko et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

This paper proposes a voice conversion (VC) method based on a sequence-to-sequence (S2S) learning framework, which enables simultaneous conversion of the voice characteristics, pitch contour, and duration of input speech. We previously proposed an S2S-based VC method using a transformer network architecture called the voice transformer network (VTN). The original VTN was designed to learn only a mapping of speech feature sequences from one speaker to another. The main idea we propose is an extension of the original VTN that can simultaneously learn mappings among multiple speakers. This extension called the many-to-many VTN makes it able to fully use available training data collected from multiple speakers by capturing common latent features that can be shared across different speakers. It also allows us to introduce a training loss called the identity mapping loss to ensure that the input feature sequence will remain unchanged when the source and target speaker indices are the same. Using this particular loss for model training has been found to be extremely effective in improving the performance of the model at test time. We conducted speaker identity conversion experiments and found that our model obtained higher sound quality and speaker similarity than baseline methods. We also found that our model, with a slight modification to its architecture, could handle any-to-many conversion tasks reasonably well.

</details>

### [Learning Individual Speaking Styles for Accurate Lip to Speech Synthesis](2005.08209.md)
**K R Prajwal, Rudrabha Mukhopadhyay, Vinay Namboodiri, C V Jawahar** · 2020-05-17

<details>
<summary>Abstract</summary>

Humans involuntarily tend to infer parts of the conversation from lip movements when the speech is absent or corrupted by external noise. In this work, we explore the task of lip to speech synthesis, i.e., learning to generate natural speech given only the lip movements of a speaker. Acknowledging the importance of contextual and speaker-specific cues for accurate lip-reading, we take a different path from existing works. We focus on learning accurate lip sequences to speech mappings for individual speakers in unconstrained, large vocabulary settings. To this end, we collect and release a large-scale benchmark dataset, the first of its kind, specifically to train and evaluate the single-speaker lip to speech task in natural settings. We propose a novel approach with key design choices to achieve accurate, natural lip to speech synthesis in such unconstrained scenarios for the first time. Extensive evaluation using quantitative, qualitative metrics and human evaluation shows that our method is four times more intelligible than previous works in this space. Please check out our demo video for a quick overview of the paper, method, and qualitative results. https://www.youtube.com/watch?v=HziA-jmlk_4&feature=youtu.be

</details>

### [Semi-supervised Learning for Multi-speaker Text-to-speech Synthesis Using Discrete Speech Representation](2005.08024.md)
**Tao Tu, Yuan-Jui Chen, Alexander H. Liu, Hung-yi Lee** · 2020-05-16

<details>
<summary>Abstract</summary>

Recently, end-to-end multi-speaker text-to-speech (TTS) systems gain success in the situation where a lot of high-quality speech plus their corresponding transcriptions are available. However, laborious paired data collection processes prevent many institutes from building multi-speaker TTS systems of great performance. In this work, we propose a semi-supervised learning approach for multi-speaker TTS. A multi-speaker TTS model can learn from the untranscribed audio via the proposed encoder-decoder framework with discrete speech representation. The experiment results demonstrate that with only an hour of paired speech data, no matter the paired data is from multiple speakers or a single speaker, the proposed model can generate intelligible speech in different voices. We found the model can benefit from the proposed semi-supervised learning approach even when part of the unpaired speech data is noisy. In addition, our analysis reveals that different speaker characteristics of the paired data have an impact on the effectiveness of semi-supervised TTS.

</details>

### [JDI-T: Jointly trained Duration Informed Transformer for Text-To-Speech without Explicit Alignment](2005.07799.md)
**Dan Lim, Won Jang, Gyeonghwan O, Heayoung Park et al.** · 2020-05-15

<details>
<summary>Abstract</summary>

We propose Jointly trained Duration Informed Transformer (JDI-T), a feed-forward Transformer with a duration predictor jointly trained without explicit alignments in order to generate an acoustic feature sequence from an input text. In this work, inspired by the recent success of the duration informed networks such as FastSpeech and DurIAN, we further simplify its sequential, two-stage training pipeline to a single-stage training. Specifically, we extract the phoneme duration from the autoregressive Transformer on the fly during the joint training instead of pretraining the autoregressive model and using it as a phoneme duration extractor. To our best knowledge, it is the first implementation to jointly train the feed-forward Transformer without relying on a pre-trained phoneme duration extractor in a single training pipeline. We evaluate the effectiveness of the proposed model on the publicly available Korean Single speaker Speech (KSS) dataset compared to the baseline text-to-speech (TTS) models trained by ESPnet-TTS.

</details>

### [WG-WaveNet: Real-Time High-Fidelity Speech Synthesis without GPU](2005.07412.md)
**Po-chun Hsu, Hung-yi Lee** · 2020-05-15

<details>
<summary>Abstract</summary>

In this paper, we propose WG-WaveNet, a fast, lightweight, and high-quality waveform generation model. WG-WaveNet is composed of a compact flow-based model and a post-filter. The two components are jointly trained by maximizing the likelihood of the training data and optimizing loss functions on the frequency domains. As we design a flow-based model that is heavily compressed, the proposed model requires much less computational resources compared to other waveform generation models during both training and inference time; even though the model is highly compressed, the post-filter maintains the quality of generated waveform. Our PyTorch implementation can be trained using less than 8 GB GPU memory and generates audio samples at a rate of more than 960 kHz on an NVIDIA 1080Ti GPU. Furthermore, even if synthesizing on a CPU, we show that the proposed method is capable of generating 44.1 kHz speech waveform 1.2 times faster than real-time. Experiments also show that the quality of generated audio is comparable to those of other methods. Audio samples are publicly available online.

</details>

### [Reverberation Modeling for Source-Filter-based Neural Vocoder](2005.07379.md)
**Yang Ai, Xin Wang, Junichi Yamagishi, Zhen-Hua Ling** · 2020-05-15

<details>
<summary>Abstract</summary>

This paper presents a reverberation module for source-filter-based neural vocoders that improves the performance of reverberant effect modeling. This module uses the output waveform of neural vocoders as an input and produces a reverberant waveform by convolving the input with a room impulse response (RIR). We propose two approaches to parameterizing and estimating the RIR. The first approach assumes a global time-invariant (GTI) RIR and directly learns the values of the RIR on a training dataset. The second approach assumes an utterance-level time-variant (UTV) RIR, which is invariant within one utterance but varies across utterances, and uses another neural network to predict the RIR values. We add the proposed reverberation module to the phase spectrum predictor (PSP) of a HiNet vocoder and jointly train the model. Experimental results demonstrate that the proposed module was helpful for modeling the reverberation effect and improving the perceived quality of generated reverberant speech. The UTV-RIR was shown to be more robust than the GTI-RIR to unknown reverberation conditions and achieved a perceptually better reverberation effect.

</details>

### [Converting Anyone's Emotion: Towards Speaker-Independent Emotional Voice Conversion](2005.07025.md)
**Kun Zhou, Berrak Sisman, Mingyang Zhang, Haizhou Li** · 2020-05-13

<details>
<summary>Abstract</summary>

Emotional voice conversion aims to convert the emotion of speech from one state to another while preserving the linguistic content and speaker identity. The prior studies on emotional voice conversion are mostly carried out under the assumption that emotion is speaker-dependent. We consider that there is a common code between speakers for emotional expression in a spoken language, therefore, a speaker-independent mapping between emotional states is possible. In this paper, we propose a speaker-independent emotional voice conversion framework, that can convert anyone's emotion without the need for parallel data. We propose a VAW-GAN based encoder-decoder structure to learn the spectrum and prosody mapping. We perform prosody conversion by using continuous wavelet transform (CWT) to model the temporal dependencies. We also investigate the use of F0 as an additional input to the decoder to improve emotion conversion performance. Experiments show that the proposed speaker-independent framework achieves competitive results for both seen and unseen speakers.

</details>

### [Flowtron: an Autoregressive Flow-based Generative Network for Text-to-Speech Synthesis](2005.05957.md)
**Rafael Valle, Kevin Shih, Ryan Prenger, Bryan Catanzaro** · 2020-05-12

<details>
<summary>Abstract</summary>

In this paper we propose Flowtron: an autoregressive flow-based generative network for text-to-speech synthesis with control over speech variation and style transfer. Flowtron borrows insights from IAF and revamps Tacotron in order to provide high-quality and expressive mel-spectrogram synthesis. Flowtron is optimized by maximizing the likelihood of the training data, which makes training simple and stable. Flowtron learns an invertible mapping of data to a latent space that can be manipulated to control many aspects of speech synthesis (pitch, tone, speech rate, cadence, accent). Our mean opinion scores (MOS) show that Flowtron matches state-of-the-art TTS models in terms of speech quality. In addition, we provide results on control of speech variation, interpolation between samples and style transfer between speakers seen and unseen during training. Code and pre-trained models will be made publicly available at https://github.com/NVIDIA/flowtron

</details>

### [AdaDurIAN: Few-shot Adaptation for Neural Text-to-Speech with DurIAN](2005.05642.md)
**Zewang Zhang, Qiao Tian, Heng Lu, Ling-Hui Chen et al.** · 2020-05-12

<details>
<summary>Abstract</summary>

This paper investigates how to leverage a DurIAN-based average model to enable a new speaker to have both accurate pronunciation and fluent cross-lingual speaking with very limited monolingual data. A weakness of the recently proposed end-to-end text-to-speech (TTS) systems is that robust alignment is hard to achieve, which hinders it to scale well with very limited data. To cope with this issue, we introduce AdaDurIAN by training an improved DurIAN-based average model and leverage it to few-shot learning with the shared speaker-independent content encoder across different speakers. Several few-shot learning tasks in our experiments show AdaDurIAN can outperform the baseline end-to-end system by a large margin. Subjective evaluations also show that AdaDurIAN yields higher mean opinion score (MOS) of naturalness and more preferences of speaker similarity. In addition, we also apply AdaDurIAN to emotion transfer tasks and demonstrate its promising performance.

</details>

### [FeatherWave: An efficient high-fidelity neural vocoder with multi-band linear prediction](2005.05551.md)
**Qiao Tian, Zewang Zhang, Heng Lu, Ling-Hui Chen et al.** · 2020-05-12

<details>
<summary>Abstract</summary>

In this paper, we propose the FeatherWave, yet another variant of WaveRNN vocoder combining the multi-band signal processing and the linear predictive coding. The LPCNet, a recently proposed neural vocoder which utilized the linear predictive characteristic of speech signal in the WaveRNN architecture, can generate high quality speech with a speed faster than real-time on a single CPU core. However, LPCNet is still not efficient enough for online speech generation tasks. To address this issue, we adopt the multi-band linear predictive coding for WaveRNN vocoder. The multi-band method enables the model to generate several speech samples in parallel at one step. Therefore, it can significantly improve the efficiency of speech synthesis. The proposed model with 4 sub-bands needs less than 1.6 GFLOPS for speech generation. In our experiments, it can generate 24 kHz high-fidelity audio 9x faster than real-time on a single CPU, which is much faster than the LPCNet vocoder. Furthermore, our subjective listening test shows that the FeatherWave can generate speech with better quality than LPCNet.

</details>

### [Luganda Text-to-Speech Machine](2005.05447.md)
**Irene Nandutu, Ernest Mwebaze** · 2020-05-11

<details>
<summary>Abstract</summary>

In Uganda, Luganda is the most spoken native language. It is used for communication in informal as well as formal business transactions. The development of technology startups globally related to TTS has mainly been with languages like English, French, etc. These are added in TTS engines by Google, Microsoft among others, allowing developers in these regions to innovate TTS products. Luganda is not supported because the language is not built and trained on these engines. In this study, we analyzed the Luganda language structure and constructions and then proposed and developed a Luganda TTS. The system was built and trained using locally sourced Luganda language text and audio. The engine is now able to capture text and reads it aloud. We tested the accuracy using MRT and MOS. MRT and MOS tests results are quite good with MRT having better results. The results general score was 71%. This study will enhance previous solutions to NLP gaps in Uganda, as well as provide raw data such that other research in this area can take place.

</details>

### [Multi-band MelGAN: Faster Waveform Generation for High-Quality Text-to-Speech](2005.05106.md)
**Geng Yang, Shan Yang, Kai Liu, Peng Fang et al.** · 2020-05-11

<details>
<summary>Abstract</summary>

In this paper, we propose multi-band MelGAN, a much faster waveform generation model targeting to high-quality text-to-speech. Specifically, we improve the original MelGAN by the following aspects. First, we increase the receptive field of the generator, which is proven to be beneficial to speech generation. Second, we substitute the feature matching loss with the multi-resolution STFT loss to better measure the difference between fake and real speech. Together with pre-training, this improvement leads to both better quality and better training stability. More importantly, we extend MelGAN with multi-band processing: the generator takes mel-spectrograms as input and produces sub-band signals which are subsequently summed back to full-band signals as discriminator input. The proposed multi-band MelGAN has achieved high MOS of 4.34 and 4.22 in waveform generation and TTS, respectively. With only 1.91M parameters, our model effectively reduces the total computational complexity of the original MelGAN from 5.85 to 0.95 GFLOPS. Our Pytorch implementation, which will be open-resourced shortly, can achieve a real-time factor of 0.03 on CPU without hardware specific optimization.

</details>

### [TTS-Portuguese Corpus: a corpus for speech synthesis in Brazilian Portuguese](2005.05144.md)
**Edresson Casanova, Arnaldo Candido Junior, Christopher Shulby, Frederico Santos de Oliveira et al.** · 2020-05-11

<details>
<summary>Abstract</summary>

Speech provides a natural way for human-computer interaction. In particular, speech synthesis systems are popular in different applications, such as personal assistants, GPS applications, screen readers and accessibility tools. However, not all languages are on the same level when in terms of resources and systems for speech synthesis. This work consists of creating publicly available resources for Brazilian Portuguese in the form of a novel dataset along with deep learning models for end-to-end speech synthesis. Such dataset has 10.5 hours from a single speaker, from which a Tacotron 2 model with the RTISI-LA vocoder presented the best performance, achieving a 4.03 MOS value. The obtained results are comparable to related works covering English language and the state-of-the-art in Portuguese.

</details>

### [End-To-End Speech Synthesis Applied to Brazilian Portuguese](s2:8bb5be75a0561a6249eadaa0ce9f24d4a1d092c1.md)
**Edresson Casanova, Arnaldo Candido, F. S. Oliveira, C. Shulby et al.** · 2020-05-11

### [Corpus Generation for Voice Command in Smart Home and the Effect of Speech Synthesis on End-to-End SLU](s2:0b4a4a33c74a0ea64b8837ba2f9b6449f1504877.md)
**Thierry Desot, François Portet, Michel Vacher** · 2020-05-11

### [Scyclone: High-Quality and Parallel-Data-Free Voice Conversion Using Spectrogram and Cycle-Consistent Adversarial Networks](2005.03334.md)
**Masaya Tanaka, Takashi Nose, Aoi Kanagaki, Ryohei Shimizu et al.** · 2020-05-07

<details>
<summary>Abstract</summary>

This paper proposes Scyclone, a high-quality voice conversion (VC) technique without parallel data training. Scyclone improves speech naturalness and speaker similarity of the converted speech by introducing CycleGAN-based spectrogram conversion with a simplified WaveRNN-based vocoder. In Scyclone, a linear spectrogram is used as the conversion features instead of vocoder parameters, which avoids quality degradation due to extraction errors in fundamental frequency and voiced/unvoiced parameters. The spectrogram of source and target speakers are modeled by modified CycleGAN networks, and the waveform is reconstructed using the simplified WaveRNN with a single Gaussian probability density function. The subjective experiments with completely unpaired training data show that Scyclone is significantly better than CycleGAN-VC2, one of the existing state-of-the-art parallel-data-free VC techniques.

</details>

### [Cotatron: Transcription-Guided Speech Encoder for Any-to-Many Voice Conversion without Parallel Data](2005.03295.md)
**Seung-won Park, Doo-young Kim, Myun-chul Joe** · 2020-05-07

<details>
<summary>Abstract</summary>

We propose Cotatron, a transcription-guided speech encoder for speaker-independent linguistic representation. Cotatron is based on the multispeaker TTS architecture and can be trained with conventional TTS datasets. We train a voice conversion system to reconstruct speech with Cotatron features, which is similar to the previous methods based on Phonetic Posteriorgram (PPG). By training and evaluating our system with 108 speakers from the VCTK dataset, we outperform the previous method in terms of both naturalness and speaker similarity. Our system can also convert speech from speakers that are unseen during training, and utilize ASR to automate the transcription with minimal reduction of the performance. Audio samples are available at https://mindslab-ai.github.io/cotatron, and the code with a pre-trained model will be made available soon.

</details>

### [Building A User-Centric and Content-Driven Socialbot](2005.02623.md)
**Hao Fang** · 2020-05-06

<details>
<summary>Abstract</summary>

To build Sounding Board, we develop a system architecture that is capable of accommodating dialog strategies that we designed for socialbot conversations. The architecture consists of a multi-dimensional language understanding module for analyzing user utterances, a hierarchical dialog management framework for dialog context tracking and complex dialog control, and a language generation process that realizes the response plan and makes adjustments for speech synthesis. Additionally, we construct a new knowledge base to power the socialbot by collecting social chat content from a variety of sources. An important contribution of the system is the synergy between the knowledge base and the dialog management, i.e., the use of a graph structure to organize the knowledge base that makes dialog control very efficient in bringing related content to the discussion. Using the data collected from Sounding Board during the competition, we carry out in-depth analyses of socialbot conversations and user ratings which provide valuable insights in evaluation methods for socialbots. We additionally investigate a new approach for system evaluation and diagnosis that allows scoring individual dialog segments in the conversation. Finally, observing that socialbots suffer from the issue of shallow conversations about topics associated with unstructured data, we study the problem of enabling extended socialbot conversations grounded on a document. To bring together machine reading and dialog control techniques, a graph-based document representation is proposed, together with methods for automatically constructing the graph. Using the graph-based representation, dialog control can be carried out by retrieving nodes or moving along edges in the graph. To illustrate the usage, a mixed-initiative dialog strategy is designed for socialbot conversations on news articles.

</details>

### [Can Speaker Augmentation Improve Multi-Speaker End-to-End TTS?](2005.01245.md)
**Erica Cooper, Cheng-I Lai, Yusuke Yasuda, Junichi Yamagishi** · 2020-05-04

<details>
<summary>Abstract</summary>

Previous work on speaker adaptation for end-to-end speech synthesis still falls short in speaker similarity. We investigate an orthogonal approach to the current speaker adaptation paradigms, speaker augmentation, by creating artificial speakers and by taking advantage of low-quality data. The base Tacotron2 model is modified to account for the channel and dialect factors inherent in these corpora. In addition, we describe a warm-start training strategy that we adopted for Tacotron2 training. A large-scale listening test is conducted, and a distance metric is adopted to evaluate synthesis of dialects. This is followed by an analysis on synthesis quality, speaker and dialect similarity, and a remark on the effectiveness of our speaker augmentation approach. Audio samples are available online.

</details>

### [Improving End-to-End Speech Synthesis with Local Recurrent Neural Network Enhanced Transformer](s2:39206ad9fe0859a0043bd8caea2e3f8202b67533.md)
**Yibin Zheng, Xinhui Li, Fenglong Xie, Li Lu** · 2020-05-01

<details>
<summary>Abstract</summary>

Although Transformer based neural end-to-end TTS model has demonstrated extreme effectiveness in capturing long-term dependencies and achieved state-of-the-art performance, it still suffers from two problems. 1) limited ability to model sequential and local structures in sequences; 2) heavily rely on position embeddings that have limited effect but require an amount of design efforts. In this paper, we introduce local recurrent neural network (Local-RNN) into Transformer to make full use of the advantages of both RNN and Transformer while mitigating their drawbacks. The sequential and local structures could be effectively modeled by Local-RNN, while the long-term dependencies could be captured by Transformer without any use of position embeddings. Subjective evaluation results show our proposed model outperforms baseline (Transformer) with a gap of 0.12 in MOS and achieves close to human quality (4.34 vs. 4.45 in MOS) on general test. Case level intelligibility test also show an absolute improvement of 6.5% in case level intelligibility rate over the baseline on a challenging test.

</details>

### [Focusing on Attention: Prosody Transfer and Adaptative Optimization Strategy for Multi-Speaker End-to-End Speech Synthesis](s2:b43f9efa0af16ddfff43d50a20faf1ff38234e95.md)
**Ruibo Fu, J. Tao, Zhengqi Wen, Jiangyan Yi et al.** · 2020-05-01

<details>
<summary>Abstract</summary>

End-to-end speech synthesis can generate high-quality synthetic speech and achieve high similarity scores with low-resource adaptation data. However, the generalization of out-domain texts is still a challenging task. The limited adaptation data leads to unacceptable errors and the poor prosody performance of the synthetic speech. In this paper, we present two novel methods to handle the above problems by focusing on the attention. Firstly, compared with the conventional methods that extract prosody embeddings for conditioning input, a duration controller with feedback mechanism is proposed, which can control the states transition in the sequence-to-sequence model more directly and precisely. Secondly, to alleviate the unmatching text-audio pairs’ impact on model, an adaptative optimization strategy which would consider the matching degree of the training sample is also proposed. Experimental results on Mandarin dataset show that proposed methods lead to an improvement on both robustness and overall naturalness.

</details>

### [Semi-Supervised Learning Based on Hierarchical Generative Models for End-to-End Speech Synthesis](s2:6a82214f258258ec3ba02926b0b7b80baa77c2cf.md)
**Takato Fujimoto, Shinji Takaki, Kei Hashimoto, Keiichiro Oura et al.** · 2020-05-01

<details>
<summary>Abstract</summary>

This paper proposes a general framework of semi-supervised learning based on hierarchical generative models and adapts it to a Japanese end-to-end text-to-speech (TTS) system. In English TTS, several end-to-end systems have recently achieved sound quality close to that of natural human speech. However, in non-alphabetic languages such as Japanese, it is difficult to realize true text-input end-to-end TTS due to character diversity and pitch accents. To address this problem, we propose end-to-end TTS based on semi-supervised learning that makes the most of existing data consisting of any combination of text, phoneme, and waveform as training data. To demonstrate the effectiveness of the proposed system, listening tests were conducted for pronunciation and naturalness. Our results show that the proposed system improves both pronunciation and naturalness.

</details>

### [CopyCat: Many-to-Many Fine-Grained Prosody Transfer for Neural Text-to-Speech](2004.14617.md)
**Sri Karlapati, Alexis Moinet, Arnaud Joly, Viacheslav Klimkov et al.** · 2020-04-30

<details>
<summary>Abstract</summary>

Prosody Transfer (PT) is a technique that aims to use the prosody from a source audio as a reference while synthesising speech. Fine-grained PT aims at capturing prosodic aspects like rhythm, emphasis, melody, duration, and loudness, from a source audio at a very granular level and transferring them when synthesising speech in a different target speaker's voice. Current approaches for fine-grained PT suffer from source speaker leakage, where the synthesised speech has the voice identity of the source speaker as opposed to the target speaker. In order to mitigate this issue, they compromise on the quality of PT. In this paper, we propose CopyCat, a novel, many-to-many PT system that is robust to source speaker leakage, without using parallel data. We achieve this through a novel reference encoder architecture capable of capturing temporal prosodic representations which are robust to source speaker leakage. We compare CopyCat against a state-of-the-art fine-grained PT model through various subjective evaluations, where we show a relative improvement of $47\%$ in the quality of prosody transfer and $14\%$ in preserving the target speaker identity, while still maintaining the same naturalness.

</details>

### [Conditional Spoken Digit Generation with StyleGAN](2004.13764.md)
**Kasperi Palkama, Lauri Juvela, Alexander Ilin** · 2020-04-28

<details>
<summary>Abstract</summary>

This paper adapts a StyleGAN model for speech generation with minimal or no conditioning on text. StyleGAN is a multi-scale convolutional GAN capable of hierarchically capturing data structure and latent variation on multiple spatial (or temporal) levels. The model has previously achieved impressive results on facial image generation, and it is appealing to audio applications due to similar multi-level structures present in the data. In this paper, we train a StyleGAN to generate mel-frequency spectrograms on the Speech Commands dataset, which contains spoken digits uttered by multiple speakers in varying acoustic conditions. In a conditional setting our model is conditioned on the digit identity, while learning the remaining data variation remains an unsupervised task. We compare our model to the current unsupervised state-of-the-art speech synthesis GAN architecture, the WaveGAN, and show that the proposed model outperforms according to numerical measures and subjective evaluation by listening tests.

</details>

### [ByteSing: A Chinese Singing Voice Synthesis System Using Duration Allocated Encoder-Decoder Acoustic Models and WaveRNN Vocoders](2004.11012.md)
**Yu Gu, Xiang Yin, Yonghui Rao, Yuan Wan et al.** · 2020-04-23

<details>
<summary>Abstract</summary>

This paper presents ByteSing, a Chinese singing voice synthesis (SVS) system based on duration allocated Tacotron-like acoustic models and WaveRNN neural vocoders. Different from the conventional SVS models, the proposed ByteSing employs Tacotron-like encoder-decoder structures as the acoustic models, in which the CBHG models and recurrent neural networks (RNNs) are explored as encoders and decoders respectively. Meanwhile an auxiliary phoneme duration prediction model is utilized to expand the input sequence, which can enhance the model controllable capacity, model stability and tempo prediction accuracy. WaveRNN neural vocoders are also adopted as neural vocoders to further improve the voice quality of synthesized songs. Both objective and subjective experimental results prove that the SVS method proposed in this paper can produce quite natural, expressive and high-fidelity songs by improving the pitch and spectrogram prediction accuracy and the models using attention mechanism can achieve best performance.

</details>

### [Unsupervised Speech Decomposition via Triple Information Bottleneck](2004.11284.md)
**Kaizhi Qian, Yang Zhang, Shiyu Chang, David Cox et al.** · 2020-04-23

<details>
<summary>Abstract</summary>

Speech information can be roughly decomposed into four components: language content, timbre, pitch, and rhythm. Obtaining disentangled representations of these components is useful in many speech analysis and generation applications. Recently, state-of-the-art voice conversion systems have led to speech representations that can disentangle speaker-dependent and independent information. However, these systems can only disentangle timbre, while information about pitch, rhythm and content is still mixed together. Further disentangling the remaining speech components is an under-determined problem in the absence of explicit annotations for each component, which are difficult and expensive to obtain. In this paper, we propose SpeechSplit, which can blindly decompose speech into its four components by introducing three carefully designed information bottlenecks. SpeechSplit is among the first algorithms that can separately perform style transfer on timbre, pitch and rhythm without text labels. Our code is publicly available at https://github.com/auspicious3000/SpeechSplit.

</details>

### [Utterance-level Sequential Modeling For Deep Gaussian Process Based Speech Synthesis Using Simple Recurrent Unit](2004.10823.md)
**Tomoki Koriyama, Hiroshi Saruwatari** · 2020-04-22

<details>
<summary>Abstract</summary>

This paper presents a deep Gaussian process (DGP) model with a recurrent architecture for speech sequence modeling. DGP is a Bayesian deep model that can be trained effectively with the consideration of model complexity and is a kernel regression model that can have high expressibility. In the previous studies, it was shown that the DGP-based speech synthesis outperformed neural network-based one, in which both models used a feed-forward architecture. To improve the naturalness of synthetic speech, in this paper, we show that DGP can be applied to utterance-level modeling using recurrent architecture models. We adopt a simple recurrent unit (SRU) for the proposed model to achieve a recurrent architecture, in which we can execute fast speech parameter generation by using the high parallelization nature of SRU. The objective and subjective evaluation results show that the proposed SRU-DGP-based speech synthesis outperforms not only feed-forward DGP but also automatically tuned SRU- and long short-term memory (LSTM)-based neural networks.

</details>

### [Data Processing for Optimizing Naturalness of Vietnamese Text-to-speech System](2004.09607.md)
**Viet Lam Phung, Phan Huy Kinh, Anh Tuan Dinh, Quoc Bao Nguyen** · 2020-04-20

<details>
<summary>Abstract</summary>

Abstract End-to-end text-to-speech (TTS) systems has proved its great success in the presence of a large amount of high-quality training data recorded in anechoic room with high-quality microphone. Another approach is to use available source of found data like radio broadcast news. We aim to optimize the naturalness of TTS system on the found data using a novel data processing method. The data processing method includes 1) utterance selection and 2) prosodic punctuation insertion to prepare training data which can optimize the naturalness of TTS systems. We showed that using the processing data method, an end-to-end TTS achieved a mean opinion score (MOS) of 4.1 compared to 4.3 of natural speech. We showed that the punctuation insertion contributed the most to the result. To facilitate the research and development of TTS systems, we distributed the processed data of one speaker at https://forms.gle/6Hk5YkqgDxAaC2BU6.

</details>

### [Knowledge-and-Data-Driven Amplitude Spectrum Prediction for Hierarchical Neural Vocoders](2004.07832.md)
**Yang Ai, Zhen-Hua Ling** · 2020-04-16

<details>
<summary>Abstract</summary>

In our previous work, we have proposed a neural vocoder called HiNet which recovers speech waveforms by predicting amplitude and phase spectra hierarchically from input acoustic features. In HiNet, the amplitude spectrum predictor (ASP) predicts log amplitude spectra (LAS) from input acoustic features. This paper proposes a novel knowledge-and-data-driven ASP (KDD-ASP) to improve the conventional one. First, acoustic features (i.e., F0 and mel-cepstra) pass through a knowledge-driven LAS recovery module to obtain approximate LAS (ALAS). This module is designed based on the combination of STFT and source-filter theory, in which the source part and the filter part are designed based on input F0 and mel-cepstra, respectively. Then, the recovered ALAS are processed by a data-driven LAS refinement module which consists of multiple trainable convolutional layers to get the final LAS. Experimental results show that the HiNet vocoder using KDD-ASP can achieve higher quality of synthetic speech than that using conventional ASP and the WaveRNN vocoder on a text-to-speech (TTS) task.

</details>

### [F0-consistent many-to-many non-parallel voice conversion via conditional autoencoder](2004.07370.md)
**Kaizhi Qian, Zeyu Jin, Mark Hasegawa-Johnson, Gautham J. Mysore** · 2020-04-15

<details>
<summary>Abstract</summary>

Non-parallel many-to-many voice conversion remains an interesting but challenging speech processing task. Many style-transfer-inspired methods such as generative adversarial networks (GANs) and variational autoencoders (VAEs) have been proposed. Recently, AutoVC, a conditional autoencoders (CAEs) based method achieved state-of-the-art results by disentangling the speaker identity and speech content using information-constraining bottlenecks, and it achieves zero-shot conversion by swapping in a different speaker's identity embedding to synthesize a new voice. However, we found that while speaker identity is disentangled from speech content, a significant amount of prosodic information, such as source F0, leaks through the bottleneck, causing target F0 to fluctuate unnaturally. Furthermore, AutoVC has no control of the converted F0 and thus unsuitable for many applications. In the paper, we modified and improved autoencoder-based voice conversion to disentangle content, F0, and speaker identity at the same time. Therefore, we can control the F0 contour, generate speech with F0 consistent with the target speaker, and significantly improve quality and similarity. We support our improvement through quantitative and qualitative analysis.

</details>

### [Generating Multilingual Voices Using Speaker Space Translation Based on Bilingual Speaker Data](2004.04972.md)
**Soumi Maiti, Erik Marchi, Alistair Conkie** · 2020-04-10

<details>
<summary>Abstract</summary>

We present progress towards bilingual Text-to-Speech which is able to transform a monolingual voice to speak a second language while preserving speaker voice quality. We demonstrate that a bilingual speaker embedding space contains a separate distribution for each language and that a simple transform in speaker space generated by the speaker embedding can be used to control the degree of accent of a synthetic voice in a language. The same transform can be applied even to monolingual speakers. In our experiments speaker data from an English-Spanish (Mexican) bilingual speaker was used, and the goal was to enable English speakers to speak Spanish and Spanish speakers to speak English. We found that the simple transform was sufficient to convert a voice from one language to the other with a high degree of naturalness. In one case the transformed voice outperformed a native language voice in listening tests. Experiments further indicated that the transform preserved many of the characteristics of the original voice. The degree of accent present can be controlled and naturalness is relatively consistent across a range of accent values.

</details>

### [Scalable Multilingual Frontend for TTS](2004.04934.md)
**Alistair Conkie, Andrew Finch** · 2020-04-10

<details>
<summary>Abstract</summary>

This paper describes progress towards making a Neural Text-to-Speech (TTS) Frontend that works for many languages and can be easily extended to new languages. We take a Machine Translation (MT) inspired approach to constructing the frontend, and model both text normalization and pronunciation on a sentence level by building and using sequence-to-sequence (S2S) models. We experimented with training normalization and pronunciation as separate S2S models and with training a single S2S model combining both functions. For our language-independent approach to pronunciation we do not use a lexicon. Instead all pronunciations, including context-based pronunciations, are captured in the S2S model. We also present a language-independent chunking and splicing technique that allows us to process arbitrary-length sentences. Models for 18 languages were trained and evaluated. Many of the accuracy measurements are above 99%. We also evaluated the models in the context of end-to-end synthesis against our current production system.

</details>

### [Advancing Speech Synthesis using EEG](2004.04731.md)
**Gautam Krishna, Co Tran, Mason Carnahan, Ahmed Tewfik** · 2020-04-09

<details>
<summary>Abstract</summary>

In this paper we introduce attention-regression model to demonstrate predicting acoustic features from electroencephalography (EEG) features recorded in parallel with spoken sentences. First we demonstrate predicting acoustic features directly from EEG features using our attention model and then we demonstrate predicting acoustic features from EEG features using a two-step approach where in the first step we use our attention model to predict articulatory features from EEG features and then in second step another attention-regression model is trained to transform the predicted articulatory features to acoustic features. Our proposed attention-regression model demonstrates superior performance compared to the regression model introduced by authors in [1] when tested using their data set for majority of the subjects during test time. The results presented in this paper further advances the work described by authors in [1].

</details>

### [Noise Tokens: Learning Neural Noise Templates for Environment-Aware Speech Enhancement](2004.04001.md)
**Haoyu Li, Junichi Yamagishi** · 2020-04-08

<details>
<summary>Abstract</summary>

In recent years, speech enhancement (SE) has achieved impressive progress with the success of deep neural networks (DNNs). However, the DNN approach usually fails to generalize well to unseen environmental noise that is not included in the training. To address this problem, we propose "noise tokens" (NTs), which are a set of neural noise templates that are jointly trained with the SE system. NTs dynamically capture the environment variability and thus enable the DNN model to handle various environments to produce STFT magnitude with higher quality. Experimental results show that using NTs is an effective strategy that consistently improves the generalization ability of SE systems across different DNN architectures. Furthermore, we investigate applying a state-of-the-art neural vocoder to generate waveform instead of traditional inverse STFT (ISTFT). Subjective listening tests show the residual noise can be significantly suppressed through mel-spectrogram correction and vocoder-based waveform synthesis.

</details>

### [Multi-Target Emotional Voice Conversion With Neural Vocoders](2004.03782.md)
**Songxiang Liu, Yuewen Cao, Helen Meng** · 2020-04-08

<details>
<summary>Abstract</summary>

Emotional voice conversion (EVC) is one way to generate expressive synthetic speech. Previous approaches mainly focused on modeling one-to-one mapping, i.e., conversion from one emotional state to another emotional state, with Mel-cepstral vocoders. In this paper, we investigate building a multi-target EVC (MTEVC) architecture, which combines a deep bidirectional long-short term memory (DBLSTM)-based conversion model and a neural vocoder. Phonetic posteriorgrams (PPGs) containing rich linguistic information are incorporated into the conversion model as auxiliary input features, which boost the conversion performance. To leverage the advantages of the newly emerged neural vocoders, we investigate the conditional WaveNet and flow-based WaveNet (FloWaveNet) as speech generators. The vocoders take in additional speaker information and emotion information as auxiliary features and are trained with a multi-speaker and multi-emotion speech corpus. Objective metrics and subjective evaluation of the experimental results verify the efficacy of the proposed MTEVC architecture for EVC.

</details>

### [Emotional Voice Conversion With Cycle-consistent Adversarial Network](2004.03781.md)
**Songxiang Liu, Yuewen Cao, Helen Meng** · 2020-04-08

<details>
<summary>Abstract</summary>

Emotional Voice Conversion, or emotional VC, is a technique of converting speech from one emotion state into another one, keeping the basic linguistic information and speaker identity. Previous approaches for emotional VC need parallel data and use dynamic time warping (DTW) method to temporally align the source-target speech parameters. These approaches often define a minimum generation loss as the objective function, such as L1 or L2 loss, to learn model parameters. Recently, cycle-consistent generative adversarial networks (CycleGAN) have been used successfully for non-parallel VC. This paper investigates the efficacy of using CycleGAN for emotional VC tasks. Rather than attempting to learn a mapping between parallel training data using a frame-to-frame minimum generation loss, the CycleGAN uses two discriminators and one classifier to guide the learning process, where the discriminators aim to differentiate between the natural and converted speech and the classifier aims to classify the underlying emotion from the natural and converted speech. The training process of the CycleGAN models randomly pairs source-target speech parameters, without any temporal alignment operation. The objective and subjective evaluation results confirm the effectiveness of using CycleGAN models for emotional VC. The non-parallel training for a CycleGAN indicates its potential for non-parallel emotional VC.

</details>

### [g2pM: A Neural Grapheme-to-Phoneme Conversion Package for Mandarin Chinese Based on a New Open Benchmark Dataset](2004.03136.md)
**Kyubyong Park, Seanie Lee** · 2020-04-07

<details>
<summary>Abstract</summary>

Conversion of Chinese graphemes to phonemes (G2P) is an essential component in Mandarin Chinese Text-To-Speech (TTS) systems. One of the biggest challenges in Chinese G2P conversion is how to disambiguate the pronunciation of polyphones - characters having multiple pronunciations. Although many academic efforts have been made to address it, there has been no open dataset that can serve as a standard benchmark for fair comparison to date. In addition, most of the reported systems are hard to employ for researchers or practitioners who want to convert Chinese text into pinyin at their convenience. Motivated by these, in this work, we introduce a new benchmark dataset that consists of 99,000+ sentences for Chinese polyphone disambiguation. We train a simple neural network model on it, and find that it outperforms other preexisting G2P systems. Finally, we package our project and share it on PyPi.

</details>

### [Vocoder-Based Speech Synthesis from Silent Videos](2004.02541.md)
**Daniel Michelsanti, Olga Slizovskaia, Gloria Haro, Emilia Gómez et al.** · 2020-04-06

<details>
<summary>Abstract</summary>

Both acoustic and visual information influence human perception of speech. For this reason, the lack of audio in a video sequence determines an extremely low speech intelligibility for untrained lip readers. In this paper, we present a way to synthesise speech from the silent video of a talker using deep learning. The system learns a mapping function from raw video frames to acoustic features and reconstructs the speech with a vocoder synthesis algorithm. To improve speech reconstruction performance, our model is also trained to predict text information in a multi-task learning fashion and it is able to simultaneously reconstruct and recognise speech in real time. The results in terms of estimated speech quality and intelligibility show the effectiveness of our method, which exhibits an improvement over existing video-to-speech approaches.

</details>

### [Non-parallel Voice Conversion System with WaveNet Vocoder and Collapsed Speech Suppression](2003.11750.md)
**Yi-Chiao Wu, Patrick Lumban Tobing, Kazuhiro Kobayashi, Tomoki Hayashi et al.** · 2020-03-26

<details>
<summary>Abstract</summary>

In this paper, we integrate a simple non-parallel voice conversion (VC) system with a WaveNet (WN) vocoder and a proposed collapsed speech suppression technique. The effectiveness of WN as a vocoder for generating high-fidelity speech waveforms on the basis of acoustic features has been confirmed in recent works. However, when combining the WN vocoder with a VC system, the distorted acoustic features, acoustic and temporal mismatches, and exposure bias usually lead to significant speech quality degradation, making WN generate some very noisy speech segments called collapsed speech. To tackle the problem, we take conventional-vocoder-generated speech as the reference speech to derive a linear predictive coding distribution constraint (LPCDC) to avoid the collapsed speech problem. Furthermore, to mitigate the negative effects introduced by the LPCDC, we propose a collapsed speech segment detector (CSSD) to ensure that the LPCDC is only applied to the problematic segments to limit the loss of quality to short periods. Objective and subjective evaluations are conducted, and the experimental results confirm the effectiveness of the proposed method, which further improves the speech quality of our previous non-parallel VC system submitted to Voice Conversion Challenge 2018.

</details>

### [Perception of prosodic variation for speech synthesis using an unsupervised discrete representation of F0](2003.06686.md)
**Zack Hodari, Catherine Lai, Simon King** · 2020-03-14

<details>
<summary>Abstract</summary>

In English, prosody adds a broad range of information to segment sequences, from information structure (e.g. contrast) to stylistic variation (e.g. expression of emotion). However, when learning to control prosody in text-to-speech voices, it is not clear what exactly the control is modifying. Existing research on discrete representation learning for prosody has demonstrated high naturalness, but no analysis has been performed on what these representations capture, or if they can generate meaningfully-distinct variants of an utterance. We present a phrase-level variational autoencoder with a multi-modal prior, using the mode centres as "intonation codes". Our evaluation establishes which intonation codes are perceptually distinct, finding that the intonation codes from our multi-modal latent model were significantly more distinct than a baseline using k-means clustering. We carry out a follow-up qualitative study to determine what information the codes are carrying. Most commonly, listeners commented on the intonation codes having a statement or question style. However, many other affect-related styles were also reported, including: emotional, uncertain, surprised, sarcastic, passive aggressive, and upset.

</details>

### [Voice conversion using coefficient mapping and neural network](2003.05184.md)
**Olaide Ayodeji Agbolade, Samson A. Oyetunji** · 2020-03-11

<details>
<summary>Abstract</summary>

The research presents a voice conversion model using coefficient mapping and neural network. Most previous works on parametric speech synthesis did not account for losses in spectral details causing over smoothing and invariably, an appreciable deviation of the converted speech from the targeted speaker. An improved model that uses both linear predictive coding (LPC) and line spectral frequency (LSF) coefficients to parametrize the source speech signal was developed in this work to reveal the effect of over-smoothing. Non-linear mapping ability of neural network was employed in mapping the source speech vectors into the acoustic vector space of the target. Training LPC coefficients with neural network yielded a poor result due to the instability of the LPC filter poles. The LPC coefficients were converted to line spectral frequency coefficients before been trained with a 3-layer neural network. The algorithm was tested with noisy data with the result evaluated using Mel-Cepstral Distance measurement. Cepstral distance evaluation shows a 35.7 percent reduction in the spectral distance between the target and the converted speech.

</details>

### [Vowels and Prosody Contribution in Neural Network Based Voice Conversion Algorithm with Noisy Training Data](2003.04640.md)
**Olaide Agbolade** · 2020-03-10

<details>
<summary>Abstract</summary>

This research presents a neural network based voice conversion (VC) model. While it is a known fact that voiced sounds and prosody are the most important component of the voice conversion framework, what is not known is their objective contributions particularly in a noisy and uncontrolled environment. This model uses a 2-layer feedforward neural network to map the Linear prediction analysis coefficients of a source speaker to the acoustic vector space of the target speaker with a view to objectively determine the contributions of the voiced, unvoiced and supra-segmental components of sounds to the voice conversion model. Results showed that vowels 'a', 'i', 'o' have the most significant contribution in the conversion success. The voiceless sounds were also found to be most affected by the noisy training data. An average noise level of 40 dB above the noise floor were found to degrade the voice conversion success by 55.14 percent relative to the voiced sounds. The result also shows that for cross-gender voice conversion, prosody conversion is more significant in scenarios where a female is the target speaker.

</details>

### [Unsupervised Style and Content Separation by Minimizing Mutual Information for Speech Synthesis](2003.06227.md)
**Ting-Yao Hu, Ashish Shrivastava, Oncel Tuzel, Chandra Dhir** · 2020-03-09

<details>
<summary>Abstract</summary>

We present a method to generate speech from input text and a style vector that is extracted from a reference speech signal in an unsupervised manner, i.e., no style annotation, such as speaker information, is required. Existing unsupervised methods, during training, generate speech by computing style from the corresponding ground truth sample and use a decoder to combine the style vector with the input text. Training the model in such a way leaks content information into the style vector. The decoder can use the leaked content and ignore some of the input text to minimize the reconstruction loss. At inference time, when the reference speech does not match the content input, the output may not contain all of the content of the input text. We refer to this problem as "content leakage", which we address by explicitly estimating and minimizing the mutual information between the style and the content through an adversarial training formulation. We call our method MIST - Mutual Information based Style Content Separation. The main goal of the method is to preserve the input content in the synthesized speech signal, which we measure by the word error rate (WER) and show substantial improvements over state-of-the-art unsupervised speech synthesis methods.

</details>

### [Statistical Context-Dependent Units Boundary Correction for Corpus-based Unit-Selection Text-to-Speech](2003.02837.md)
**Claudio Zito, Fabio Tesser, Mauro Nicolao, Piero Cosi** · 2020-03-05

<details>
<summary>Abstract</summary>

In this study, we present an innovative technique for speaker adaptation in order to improve the accuracy of segmentation with application to unit-selection Text-To-Speech (TTS) systems. Unlike conventional techniques for speaker adaptation, which attempt to improve the accuracy of the segmentation using acoustic models that are more robust in the face of the speaker's characteristics, we aim to use only context dependent characteristics extrapolated with linguistic analysis techniques. In simple terms, we use the intuitive idea that context dependent information is tightly correlated with the related acoustic waveform. We propose a statistical model, which predicts correcting values to reduce the systematic error produced by a state-of-the-art Hidden Markov Model (HMM) based speech segmentation. Our approach consists of two phases: (1) identifying context-dependent phonetic unit classes (for instance, the class which identifies vowels as being the nucleus of monosyllabic words); and (2) building a regression model that associates the mean error value made by the ASR during the segmentation of a single speaker corpus to each class. The success of the approach is evaluated by comparing the corrected boundaries of units and the state-of-the-art HHM segmentation against a reference alignment, which is supposed to be the optimal solution. In conclusion, our work supplies a first analysis of a model sensitive to speaker-dependent characteristics, robust to defective and noisy information, and a very simple implementation which could be utilized as an alternative to either more expensive speaker-adaptation systems or of numerous manual correction sessions.

</details>

### [A Neuro-AI Interface for Evaluating Generative Adversarial Networks](2003.03193.md)
**Zhengwei Wang, Qi She, Alan F. Smeaton, Tomas E. Ward et al.** · 2020-03-05

<details>
<summary>Abstract</summary>

Generative adversarial networks (GANs) are increasingly attracting attention in the computer vision, natural language processing, speech synthesis and similar domains. However, evaluating the performance of GANs is still an open and challenging problem. Existing evaluation metrics primarily measure the dissimilarity between real and generated images using automated statistical methods. They often require large sample sizes for evaluation and do not directly reflect human perception of image quality. In this work, we introduce an evaluation metric called Neuroscore, for evaluating the performance of GANs, that more directly reflects psychoperceptual image quality through the utilization of brain signals. Our results show that Neuroscore has superior performance to the current evaluation metrics in that: (1) It is more consistent with human judgment; (2) The evaluation process needs much smaller numbers of samples; and (3) It is able to rank the quality of images on a per GAN basis. A convolutional neural network (CNN) based neuro-AI interface is proposed to predict Neuroscore from GAN-generated images directly without the need for neural responses. Importantly, we show that including neural responses during the training phase of the network can significantly improve the prediction capability of the proposed model. Codes and data can be referred at this link: https://github.com/villawang/Neuro-AI-Interface.

</details>

### [AlignTTS: Efficient Feed-Forward Text-to-Speech System without Explicit Alignment](2003.01950.md)
**Zhen Zeng, Jianzong Wang, Ning Cheng, Tian Xia et al.** · 2020-03-04

<details>
<summary>Abstract</summary>

Targeting at both high efficiency and performance, we propose AlignTTS to predict the mel-spectrum in parallel. AlignTTS is based on a Feed-Forward Transformer which generates mel-spectrum from a sequence of characters, and the duration of each character is determined by a duration predictor.Instead of adopting the attention mechanism in Transformer TTS to align text to mel-spectrum, the alignment loss is presented to consider all possible alignments in training by use of dynamic programming. Experiments on the LJSpeech dataset show that our model achieves not only state-of-the-art performance which outperforms Transformer TTS by 0.03 in mean option score (MOS), but also a high efficiency which is more than 50 times faster than real-time.

</details>

### [GraphTTS: graph-to-sequence modelling in neural text-to-speech](2003.01924.md)
**Aolan Sun, Jianzong Wang, Ning Cheng, Huayi Peng et al.** · 2020-03-04

<details>
<summary>Abstract</summary>

This paper leverages the graph-to-sequence method in neural text-to-speech (GraphTTS), which maps the graph embedding of the input sequence to spectrograms. The graphical inputs consist of node and edge representations constructed from input texts. The encoding of these graphical inputs incorporates syntax information by a GNN encoder module. Besides, applying the encoder of GraphTTS as a graph auxiliary encoder (GAE) can analyse prosody information from the semantic structure of texts. This can remove the manual selection of reference audios process and makes prosody modelling an end-to-end procedure. Experimental analysis shows that GraphTTS outperforms the state-of-the-art sequence-to-sequence models by 0.24 in Mean Opinion Score (MOS). GAE can adjust the pause, ventilation and tones of synthesised audios automatically. This experimental conclusion may give some inspiration to researchers working on improving speech synthesis prosody.

</details>

### [Generating EEG features from Acoustic features](2003.00007.md)
**Gautam Krishna, Co Tran, Mason Carnahan, Yan Han et al.** · 2020-02-29

<details>
<summary>Abstract</summary>

In this paper we demonstrate predicting electroencephalograpgy (EEG) features from acoustic features using recurrent neural network (RNN) based regression model and generative adversarial network (GAN). We predict various types of EEG features from acoustic features. We compare our results with the previously studied problem on speech synthesis using EEG and our results demonstrate that EEG features can be generated from acoustic features with lower root mean square error (RMSE), normalized RMSE values compared to generating acoustic features from EEG features (ie: speech synthesis using EEG) when tested using the same data sets.

</details>

### [Comparison of Speech Representations for Automatic Quality Estimation in Multi-Speaker Text-to-Speech Synthesis](2002.12645.md)
**Jennifer Williams, Joanna Rownicka, Pilar Oplustil, Simon King** · 2020-02-28

<details>
<summary>Abstract</summary>

We aim to characterize how different speakers contribute to the perceived output quality of multi-speaker Text-to-Speech (TTS) synthesis. We automatically rate the quality of TTS using a neural network (NN) trained on human mean opinion score (MOS) ratings. First, we train and evaluate our NN model on 13 different TTS and voice conversion (VC) systems from the ASVSpoof 2019 Logical Access (LA) Dataset. Since it is not known how best to represent speech for this task, we compare 8 different representations alongside MOSNet frame-based features. Our representations include image-based spectrogram features and x-vector embeddings that explicitly model different types of noise such as T60 reverberation time. Our NN predicts MOS with a high correlation to human judgments. We report prediction correlation and error. A key finding is the quality achieved for certain speakers seems consistent, regardless of the TTS or VC system. It is widely accepted that some speakers give higher quality than others for building a TTS system: our method provides an automatic way to identify such speakers. Finally, to see if our quality prediction models generalize, we predict quality scores for synthetic speech using a separate multi-speaker TTS system that was trained on LibriTTS data, and conduct our own MOS listening test to compare human ratings with our NN predictions.

</details>

### [Controllable Sequence-To-Sequence Neural TTS with LPCNET Backend for Real-time Speech Synthesis on CPU](2002.10708.md)
**Slava Shechtman, Carmel Rabinovitz, Alex Sorin, Zvi Kons et al.** · 2020-02-25

<details>
<summary>Abstract</summary>

State-of-the-art sequence-to-sequence acoustic networks, that convert a phonetic sequence to a sequence of spectral features with no explicit prosody prediction, generate speech with close to natural quality, when cascaded with neural vocoders, such as Wavenet. However, the combined system is typically too heavy for real-time speech synthesis on a CPU. In this work we present a sequence-to-sequence acoustic network combined with lightweight LPCNet neural vocoder, designed for real-time speech synthesis on a CPU. In addition, the system allows sentence-level pace and expressivity control at inference time. We demonstrate that the proposed system can synthesize high quality 22 kHz speech in real-time on a general-purpose CPU. In terms of MOS score degradation relative to PCM, the system attained as low as 6.1-6.5% for quality and 6.3- 7.0% for expressiveness, reaching equivalent or better quality when compared to a similar system with a Wavenet vocoder backend.

</details>

### [Semi-Supervised Neural Architecture Search](2002.10389.md)
**Renqian Luo, Xu Tan, Rui Wang, Tao Qin et al.** · 2020-02-24

<details>
<summary>Abstract</summary>

Neural architecture search (NAS) relies on a good controller to generate better architectures or predict the accuracy of given architectures. However, training the controller requires both abundant and high-quality pairs of architectures and their accuracy, while it is costly to evaluate an architecture and obtain its accuracy. In this paper, we propose SemiNAS, a semi-supervised NAS approach that leverages numerous unlabeled architectures (without evaluation and thus nearly no cost). Specifically, SemiNAS 1) trains an initial accuracy predictor with a small set of architecture-accuracy data pairs; 2) uses the trained accuracy predictor to predict the accuracy of large amount of architectures (without evaluation); and 3) adds the generated data pairs to the original data to further improve the predictor. The trained accuracy predictor can be applied to various NAS algorithms by predicting the accuracy of candidate architectures for them. SemiNAS has two advantages: 1) It reduces the computational cost under the same accuracy guarantee. On NASBench-101 benchmark dataset, it achieves comparable accuracy with gradient-based method while using only 1/7 architecture-accuracy pairs. 2) It achieves higher accuracy under the same computational cost. It achieves 94.02% test accuracy on NASBench-101, outperforming all the baselines when using the same number of architectures. On ImageNet, it achieves 23.5% top-1 error rate (under 600M FLOPS constraint) using 4 GPU-days for search. We further apply it to LJSpeech text to speech task and it achieves 97% intelligibility rate in the low-resource setting and 15% test error rate in the robustness setting, with 9%, 7% improvements over the baseline respectively.

</details>

### [An Educational Study on Prosodic Symbols and Their Acoustic Realization Using Japanese End-to-end Speech Synthesis](s2:885ab5a52e6aed3d4d19e1bb0bdeb2d525f7b142.md)
**Yoshizawa Fuki, Kumano Tadashi, Minematsu Nobuaki, Kurihara Kiyoshi** · 2020-02-24

### [Speech Synthesis using EEG](2002.12756.md)
**Gautam Krishna, Co Tran, Yan Han, Mason Carnahan** · 2020-02-22

<details>
<summary>Abstract</summary>

In this paper we demonstrate speech synthesis using different electroencephalography (EEG) feature sets recently introduced in [1]. We make use of a recurrent neural network (RNN) regression model to predict acoustic features directly from EEG features. We demonstrate our results using EEG features recorded in parallel with spoken speech as well as using EEG recorded in parallel with listening utterances. We provide EEG based speech synthesis results for four subjects in this paper and our results demonstrate the feasibility of synthesizing speech directly from EEG features.

</details>

### [On the Discrepancy between Density Estimation and Sequence Generation](2002.07233.md)
**Jason Lee, Dustin Tran, Orhan Firat, Kyunghyun Cho** · 2020-02-17

<details>
<summary>Abstract</summary>

Many sequence-to-sequence generation tasks, including machine translation and text-to-speech, can be posed as estimating the density of the output y given the input x: p(y|x). Given this interpretation, it is natural to evaluate sequence-to-sequence models using conditional log-likelihood on a test set. However, the goal of sequence-to-sequence generation (or structured prediction) is to find the best output y^ given an input x, and each task has its own downstream metric R that scores a model output by comparing against a set of references y*: R(y^, y* | x). While we hope that a model that excels in density estimation also performs well on the downstream metric, the exact correlation has not been studied for sequence generation tasks. In this paper, by comparing several density estimators on five machine translation tasks, we find that the correlation between rankings of models based on log-likelihood and BLEU varies significantly depending on the range of the model families being compared. First, log-likelihood is highly correlated with BLEU when we consider models within the same family (e.g. autoregressive models, or latent variable models with the same parameterization of the prior). However, we observe no correlation between rankings of models across different families: (1) among non-autoregressive latent variable models, a flexible prior distribution is better at density estimation but gives worse generation quality than a simple prior, and (2) autoregressive models offer the best translation performance overall, while latent variable models with a normalizing flow prior give the highest held-out log-likelihood across all datasets. Therefore, we recommend using a simple prior for the latent variable non-autoregressive model when fast generation speed is desired.

</details>

### [Interactive Text-to-Speech System via Joint Style Analysis](2002.06758.md)
**Yang Gao, Weiyi Zheng, Zhaojun Yang, Thilo Kohler et al.** · 2020-02-17

<details>
<summary>Abstract</summary>

While modern TTS technologies have made significant advancements in audio quality, there is still a lack of behavior naturalness compared to conversing with people. We propose a style-embedded TTS system that generates styled responses based on the speech query style. To achieve this, the system includes a style extraction model that extracts a style embedding from the speech query, which is then used by the TTS to produce a matching response. We faced two main challenges: 1) only a small portion of the TTS training dataset has style labels, which is needed to train a multi-style TTS that respects different style embeddings during inference. 2) The TTS system and the style extraction model have disjoint training datasets. We need consistent style labels across these two datasets so that the TTS can learn to respect the labels produced by the style extraction model during inference. To solve these, we adopted a semi-supervised approach that uses the style extraction model to create style labels for the TTS dataset and applied transfer learning to learn the style embedding jointly. Our experiment results show user preference for the styled TTS responses and demonstrate the style-embedded TTS system's capability of mimicking the speech query style.

</details>

### [Lifter Training and Sub-band Modeling for Computationally Efficient and High-Quality Voice Conversion Using Spectral Differentials](2002.06778.md)
**Takaaki Saeki, Yuki Saito, Shinnosuke Takamichi, Hiroshi Saruwatari** · 2020-02-17

<details>
<summary>Abstract</summary>

In this paper, we propose computationally efficient and high-quality methods for statistical voice conversion (VC) with direct waveform modification based on spectral differentials. The conventional method with a minimum-phase filter achieves high-quality conversion but requires heavy computation in filtering. This is because the minimum phase using a fixed lifter of the Hilbert transform often results in a long-tap filter. One of our methods is a data-driven method for lifter training. Since this method takes filter truncation into account in training, it can shorten the tap length of the filter while preserving conversion accuracy. Our other method is sub-band processing for extending the conventional method from narrow-band (16 kHz) to full-band (48 kHz) VC, which can convert a full-band waveform with higher converted-speech quality. Experimental results indicate that 1) the proposed lifter-training method for narrow-band VC can shorten the tap length to 1/16 without degrading the converted-speech quality and 2) the proposed sub-band-processing method for full-band VC can improve the converted-speech quality than the conventional method.

</details>

### [Many-to-Many Voice Conversion using Conditional Cycle-Consistent Adversarial Networks](2002.06328.md)
**Shindong Lee, BongGu Ko, Keonnyeong Lee, In-Chul Yoo et al.** · 2020-02-15

<details>
<summary>Abstract</summary>

Voice conversion (VC) refers to transforming the speaker characteristics of an utterance without altering its linguistic contents. Many works on voice conversion require to have parallel training data that is highly expensive to acquire. Recently, the cycle-consistent adversarial network (CycleGAN), which does not require parallel training data, has been applied to voice conversion, showing the state-of-the-art performance. The CycleGAN based voice conversion, however, can be used only for a pair of speakers, i.e., one-to-one voice conversion between two speakers. In this paper, we extend the CycleGAN by conditioning the network on speakers. As a result, the proposed method can perform many-to-many voice conversion among multiple speakers using a single generative adversarial network (GAN). Compared to building multiple CycleGANs for each pair of speakers, the proposed method reduces the computational and spatial cost significantly without compromising the sound quality of the converted voice. Experimental results using the VCC2018 corpus confirm the efficiency of the proposed method.

</details>

### [On the localness modeling for the self-attention based end-to-end speech synthesis](s2:ac0e0e6cfb5bac417c7769867b1366bd64d1b8bd.md)
**Shan Yang, Heng Lu, Shiyin Kang, Liumeng Xue et al.** · 2020-02-11

<details>
<summary>Abstract</summary>

Attention based end-to-end speech synthesis achieves better performance in both prosody and quality compared to the conventional "front-end"-"back-end" structure. But training such end-to-end framework is usually time-consuming because of the use of recurrent neural networks. To enable parallel calculation and long-range dependency modeling, a solely self-attention based framework named Transformer is proposed recently in the end-to-end family. However, it lacks position information in sequential modeling, so that the extra position representation is crucial to achieve good performance. Besides, the weighted sum form of self-attention is conducted over the whole input sequence when computing latent representation, which may disperse the attention to the whole input sequence other than focusing on the more important neighboring input states, resulting in generation errors. In this paper, we introduce two localness modeling methods to enhance the self-attention based representation for speech synthesis, which maintain the abilities of parallel computation and global-range dependency modeling in self-attention while improving the generation stability. We systematically analyze the solely self-attention based end-to-end speech synthesis framework, and unveil the importance of local context. Then we add the proposed relative-position-aware method to enhance local edges and experiment with different architectures to examine the effectiveness of localness modeling. In order to achieve query-specific window and discard the hyper-parameter of the relative-position-aware approach, we further conduct Gaussian-based bias to enhance localness. Experimental results indicate that the two proposed localness enhanced methods can both improve the performance of the self-attention model, especially when applied to the encoder part. And the query-specific window of Gaussian bias approach is more robust compared with the fixed relative edges.

</details>

### [Fully-hierarchical fine-grained prosody modeling for interpretable speech synthesis](2002.03785.md)
**Guangzhi Sun, Yu Zhang, Ron J. Weiss, Yuan Cao et al.** · 2020-02-06

<details>
<summary>Abstract</summary>

This paper proposes a hierarchical, fine-grained and interpretable latent variable model for prosody based on the Tacotron 2 text-to-speech model. It achieves multi-resolution modeling of prosody by conditioning finer level representations on coarser level ones. Additionally, it imposes hierarchical conditioning across all latent dimensions using a conditional variational auto-encoder (VAE) with an auto-regressive structure. Evaluation of reconstruction performance illustrates that the new structure does not degrade the model while allowing better interpretability. Interpretations of prosody attributes are provided together with the comparison between word-level and phone-level prosody representations. Moreover, both qualitative and quantitative evaluations are used to demonstrate the improvement in the disentanglement of the latent dimensions.

</details>

### [BOFFIN TTS: Few-Shot Speaker Adaptation by Bayesian Optimization](2002.01953.md)
**Henry B. Moss, Vatsal Aggarwal, Nishant Prateek, Javier González et al.** · 2020-02-04

<details>
<summary>Abstract</summary>

We present BOFFIN TTS (Bayesian Optimization For FIne-tuning Neural Text To Speech), a novel approach for few-shot speaker adaptation. Here, the task is to fine-tune a pre-trained TTS model to mimic a new speaker using a small corpus of target utterances. We demonstrate that there does not exist a one-size-fits-all adaptation strategy, with convincing synthesis requiring a corpus-specific configuration of the hyper-parameters that control fine-tuning. By using Bayesian optimization to efficiently optimize these hyper-parameter values for a target speaker, we are able to perform adaptation with an average 30% improvement in speaker similarity over standard techniques. Results indicate, across multiple corpora, that BOFFIN TTS can learn to synthesize new speakers using less than ten minutes of audio, achieving the same naturalness as produced for the speakers used to train the base model.

</details>

### [WaveTTS: Tacotron-based TTS with Joint Time-Frequency Domain Loss](2002.00417.md)
**Rui Liu, Berrak Sisman, Feilong Bao, Guanglai Gao et al.** · 2020-02-02

<details>
<summary>Abstract</summary>

Tacotron-based text-to-speech (TTS) systems directly synthesize speech from text input. Such frameworks typically consist of a feature prediction network that maps character sequences to frequency-domain acoustic features, followed by a waveform reconstruction algorithm or a neural vocoder that generates the time-domain waveform from acoustic features. As the loss function is usually calculated only for frequency-domain acoustic features, that doesn't directly control the quality of the generated time-domain waveform. To address this problem, we propose a new training scheme for Tacotron-based TTS, referred to as WaveTTS, that has 2 loss functions: 1) time-domain loss, denoted as the waveform loss, that measures the distortion between the natural and generated waveform; and 2) frequency-domain loss, that measures the Mel-scale acoustic feature loss between the natural and generated acoustic features. WaveTTS ensures both the quality of the acoustic features and the resulting speech waveform. To our best knowledge, this is the first implementation of Tacotron with joint time-frequency domain loss. Experimental results show that the proposed framework outperforms the baselines and achieves high-quality synthesized speech.

</details>

### [Transforming Spectrum and Prosody for Emotional Voice Conversion with Non-Parallel Training Data](2002.00198.md)
**Kun Zhou, Berrak Sisman, Haizhou Li** · 2020-02-01

<details>
<summary>Abstract</summary>

Emotional voice conversion aims to convert the spectrum and prosody to change the emotional patterns of speech, while preserving the speaker identity and linguistic content. Many studies require parallel speech data between different emotional patterns, which is not practical in real life. Moreover, they often model the conversion of fundamental frequency (F0) with a simple linear transform. As F0 is a key aspect of intonation that is hierarchical in nature, we believe that it is more adequate to model F0 in different temporal scales by using wavelet transform. We propose a CycleGAN network to find an optimal pseudo pair from non-parallel training data by learning forward and inverse mappings simultaneously using adversarial and cycle-consistency losses. We also study the use of continuous wavelet transform (CWT) to decompose F0 into ten temporal scales, that describes speech prosody at different time resolution, for effective F0 conversion. Experimental results show that our proposed framework outperforms the baselines both in objective and subjective evaluations.

</details>

### [Improving LPCNet-based Text-to-Speech with Linear Prediction-structured Mixture Density Network](2001.11686.md)
**Min-Jae Hwang, Eunwoo Song, Ryuichi Yamamoto, Frank Soong et al.** · 2020-01-31

<details>
<summary>Abstract</summary>

In this paper, we propose an improved LPCNet vocoder using a linear prediction (LP)-structured mixture density network (MDN). The recently proposed LPCNet vocoder has successfully achieved high-quality and lightweight speech synthesis systems by combining a vocal tract LP filter with a WaveRNN-based vocal source (i.e., excitation) generator. However, the quality of synthesized speech is often unstable because the vocal source component is insufficiently represented by the mu-law quantization method, and the model is trained without considering the entire speech production mechanism. To address this problem, we first introduce LP-MDN, which enables the autoregressive neural vocoder to structurally represent the interactions between the vocal tract and vocal source components. Then, we propose to incorporate the LP-MDN to the LPCNet vocoder by replacing the conventional discretized output with continuous density distribution. The experimental results verify that the proposed system provides high quality synthetic speech by achieving a mean opinion score of 4.41 within a text-to-speech framework.

</details>

### [Unsupervised Representation Disentanglement using Cross Domain Features and Adversarial Learning in Variational Autoencoder based Voice Conversion](2001.07849.md)
**Wen-Chin Huang, Hao Luo, Hsin-Te Hwang, Chen-Chou Lo et al.** · 2020-01-22

<details>
<summary>Abstract</summary>

An effective approach for voice conversion (VC) is to disentangle linguistic content from other components in the speech signal. The effectiveness of variational autoencoder (VAE) based VC (VAE-VC), for instance, strongly relies on this principle. In our prior work, we proposed a cross-domain VAE-VC (CDVAE-VC) framework, which utilized acoustic features of different properties, to improve the performance of VAE-VC. We believed that the success came from more disentangled latent representations. In this paper, we extend the CDVAE-VC framework by incorporating the concept of adversarial learning, in order to further increase the degree of disentanglement, thereby improving the quality and similarity of converted speech. More specifically, we first investigate the effectiveness of incorporating the generative adversarial networks (GANs) with CDVAE-VC. Then, we consider the concept of domain adversarial training and add an explicit constraint to the latent representation, realized by a speaker classifier, to explicitly eliminate the speaker information that resides in the latent code. Experimental results confirm that the degree of disentanglement of the learned latent representation can be enhanced by both GANs and the speaker classifier. Meanwhile, subjective evaluation results in terms of quality and similarity scores demonstrate the effectiveness of our proposed methods.

</details>

### [From Speech-to-Speech Translation to Automatic Dubbing](2001.06785.md)
**Marcello Federico, Robert Enyedi, Roberto Barra-Chicote, Ritwik Giri et al.** · 2020-01-19

<details>
<summary>Abstract</summary>

We present enhancements to a speech-to-speech translation pipeline in order to perform automatic dubbing. Our architecture features neural machine translation generating output of preferred length, prosodic alignment of the translation with the original speech segments, neural text-to-speech with fine tuning of the duration of each utterance, and, finally, audio rendering to enriches text-to-speech output with background noise and reverberation extracted from the original audio. We report on a subjective evaluation of automatic dubbing of excerpts of TED Talks from English into Italian, which measures the perceived naturalness of automatic dubbing and the relative importance of each proposed enhancement.

</details>

### [SqueezeWave: Extremely Lightweight Vocoders for On-device Speech Synthesis](2001.05685.md)
**Bohan Zhai, Tianren Gao, Flora Xue, Daniel Rothchild et al.** · 2020-01-16

<details>
<summary>Abstract</summary>

Automatic speech synthesis is a challenging task that is becoming increasingly important as edge devices begin to interact with users through speech. Typical text-to-speech pipelines include a vocoder, which translates intermediate audio representations into an audio waveform. Most existing vocoders are difficult to parallelize since each generated sample is conditioned on previous samples. WaveGlow is a flow-based feed-forward alternative to these auto-regressive models (Prenger et al., 2019). However, while WaveGlow can be easily parallelized, the model is too expensive for real-time speech synthesis on the edge. This paper presents SqueezeWave, a family of lightweight vocoders based on WaveGlow that can generate audio of similar quality to WaveGlow with 61x - 214x fewer MACs. Code, trained models, and generated audio are publicly available at https://github.com/tianrengao/SqueezeWave.

</details>

### [Establishing Human-Robot Trust through Music-Driven Robotic Emotion Prosody and Gesture](2001.05863.md)
**Richard Savery, Ryan Rose, Gil Weinberg** · 2020-01-11

<details>
<summary>Abstract</summary>

As human-robot collaboration opportunities continue to expand, trust becomes ever more important for full engagement and utilization of robots. Affective trust, built on emotional relationship and interpersonal bonds is particularly critical as it is more resilient to mistakes and increases the willingness to collaborate. In this paper we present a novel model built on music-driven emotional prosody and gestures that encourages the perception of a robotic identity, designed to avoid uncanny valley. Symbolic musical phrases were generated and tagged with emotional information by human musicians. These phrases controlled a synthesis engine playing back pre-rendered audio samples generated through interpolation of phonemes and electronic instruments. Gestures were also driven by the symbolic phrases, encoding the emotion from the musical phrase to low degree-of-freedom movements. Through a user study we showed that our system was able to accurately portray a range of emotions to the user. We also showed with a significant result that our non-linguistic audio generation achieved an 8% higher mean of average trust than using a state-of-the-art text-to-speech system.

</details>

### [Mel-spectrogram augmentation for sequence to sequence voice conversion](2001.01401.md)
**Yeongtae Hwang, Hyemin Cho, Hongsun Yang, Dong-Ok Won et al.** · 2020-01-06

<details>
<summary>Abstract</summary>

For training the sequence-to-sequence voice conversion model, we need to handle an issue of insufficient data about the number of speech pairs which consist of the same utterance. This study experimentally investigated the effects of Mel-spectrogram augmentation on training the sequence-to-sequence voice conversion (VC) model from scratch. For Mel-spectrogram augmentation, we adopted the policies proposed in SpecAugment. In addition, we proposed new policies (i.e., frequency warping, loudness and time length control) for more data variations. Moreover, to find the appropriate hyperparameters of augmentation policies without training the VC model, we proposed hyperparameter search strategy and the new metric for reducing experimental cost, namely deformation per deteriorating ratio. We compared the effect of these Mel-spectrogram augmentation methods based on various sizes of training set and augmentation policies. In the experimental results, the time axis warping based policies (i.e., time length control and time warping.) showed better performance than other policies. These results indicate that the use of the Mel-spectrogram augmentation is more beneficial for training the VC model.

</details>

### [Excitation-based Voice Quality Analysis and Modification](2001.00582.md)
**Thomas Drugman, Thierry Dutoit, Baris Bozkurt** · 2020-01-02

<details>
<summary>Abstract</summary>

This paper investigates the differences occuring in the excitation for different voice qualities. Its goal is two-fold. First a large corpus containing three voice qualities (modal, soft and loud) uttered by the same speaker is analyzed and significant differences in characteristics extracted from the excitation are observed. Secondly rules of modification derived from the analysis are used to build a voice quality transformation system applied as a post-process to HMM-based speech synthesis. The system is shown to effectively achieve the transformations while maintaining the delivered quality.

</details>

### [Memory Attention: Robust Alignment Using Gating Mechanism for End-to-End Speech Synthesis](s2:19d30339bdba44e45031f5bd39e2f4e298fe0a36.md)
**Joun Yeop Lee, Sung Jun Cheon, Byoung Jin Choi, N. Kim** · 2020-01-01

<details>
<summary>Abstract</summary>

Recent end-to-end (e2e) speech synthesis systems usually employ attention techniques to align an input text sequence against a mel-spectrogram sequence. Attention-based e2e approach has shown state-of-the-art performance in speech synthesis. However, generating stable and robust attention alignment to avoid some serious failures such as repeating, missing, and mumbling phones is still an ongoing challenge. In order to mitigate these alignment failures, we propose a novel attention method called memory attention for e2e speech synthesis, which is inspired by the gating mechanism of the long-short term memory (LSTM). Leveraging the sequence modeling power of the gating techniques, memory attention can produce a stable alignment by controlling the amount of content-based and location-based information. For performance evaluation, we compared our proposed memory attention algorithm with various conventional attention techniques in single speaker and emotional speech synthesis scenarios. From the experimental results, we conclude that memory attention can robustly generate various stylish speech.

</details>

### [Educational review on prosodic symbols and its acoustic realization using Japanese end-to-end speech synthesis](s2:f48054a4d3fa06919b43a231f428d6f144acecc9.md)
**Yoshizawa Fuki, Kumano Tadashi, Minematsu Nobuaki, Kurihara Kiyoshi** · 2020-01-01

### [A study on Japanese end-to-end speech synthesis using romanized input text with accent symbols.](s2:adf7e4bc41a1b76b91cdde9938aca0720817b594.md)
**Hirai Toshio, Hoa Vu, Setiawan Ivan** · 2020-01-01

### [End-to-End Text-To-Speech synthesis for under resourced South African languages](s2:fa35d4f178ab60bf0a42e815bf5ab39f729c9a4f.md)
**Thapelo Nthite, M. Tsoeu** · 2020-01-01

<details>
<summary>Abstract</summary>

Text-To-Speech (TTS) systems have been widely adopted around the world for various applications, such as reading to the blind and producing speech for dialog systems. There is however, a lack of TTS systems for South African languages due to limited resources. End-to-end TTS methods using Deep Learning have recently been proposed. These methods eliminate the need for time aligned TTS corpora, making them attractive for under resourced languages. In this paper we present the first reported use of an end-to-end approach for implementing TTS systems for isiXhosa and Sesotho. We train the model using the Lwazi II Sotho corpus as well as the Lwazi III Xhosa corpus. The performance of the system is compared to the Qfrency TTS system using a mean opinion score and a word error rate. The results show that the end-to-end system implemented is able to outperform the Qfrency TTS system by an MOS of 0.68 and 0.83 for intelligibility and naturalness respectively. This is one of the first reported implementations of an end-to-end TTS for any South African language.

</details>

