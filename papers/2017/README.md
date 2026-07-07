# 2017

27 papers in this year.

### [Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions](1712.05884.md)
**Jonathan Shen, Ruoming Pang, Ron J. Weiss, Mike Schuster et al.** · 2017-12-16

<details>
<summary>Abstract</summary>

This paper describes Tacotron 2, a neural network architecture for speech synthesis directly from text. The system is composed of a recurrent sequence-to-sequence feature prediction network that maps character embeddings to mel-scale spectrograms, followed by a modified WaveNet model acting as a vocoder to synthesize timedomain waveforms from those spectrograms. Our model achieves a mean opinion score (MOS) of $4.53$ comparable to a MOS of $4.58$ for professionally recorded speech. To validate our design choices, we present ablation studies of key components of our system and evaluate the impact of using mel spectrograms as the input to WaveNet instead of linguistic, duration, and $F_0$ features. We further demonstrate that using a compact acoustic intermediate representation enables significant simplification of the WaveNet architecture.

</details>

### [Creating New Language and Voice Components for the Updated MaryTTS Text-to-Speech Synthesis Platform](1712.04787.md)
**Ingmar Steiner, Sébastien Le Maguer** · 2017-12-13

<details>
<summary>Abstract</summary>

We present a new workflow to create components for the MaryTTS text-to-speech synthesis platform, which is popular with researchers and developers, extending it to support new languages and custom synthetic voices. This workflow replaces the previous toolkit with an efficient, flexible process that leverages modern build automation and cloud-hosted infrastructure. Moreover, it is compatible with the updated MaryTTS architecture, enabling new features and state-of-the-art paradigms such as synthesis based on deep neural networks (DNNs). Like MaryTTS itself, the new tools are free, open source software (FOSS), and promote the use of open data.

</details>

### [ObamaNet: Photo-realistic lip-sync from text](1801.01442.md)
**Rithesh Kumar, Jose Sotelo, Kundan Kumar, Alexandre de Brebisson et al.** · 2017-12-06

<details>
<summary>Abstract</summary>

We present ObamaNet, the first architecture that generates both audio and synchronized photo-realistic lip-sync videos from any new text. Contrary to other published lip-sync approaches, ours is only composed of fully trainable neural modules and does not rely on any traditional computer graphics methods. More precisely, we use three main modules: a text-to-speech network based on Char2Wav, a time-delayed LSTM to generate mouth-keypoints synced to the audio, and a network based on Pix2Pix to generate the video frames conditioned on the keypoints.

</details>

### [Word level prosody prediction using large audiobook dataset](s2:9092a07fff3143ea987d706267f3f50b2922e94a.md)
**Yanfeng Lu, Chenyu Yang, M. Dong** · 2017-12-01

### [Parallel-Data-Free Voice Conversion Using Cycle-Consistent Adversarial Networks](1711.11293.md)
**Takuhiro Kaneko, Hirokazu Kameoka** · 2017-11-30

<details>
<summary>Abstract</summary>

We propose a parallel-data-free voice-conversion (VC) method that can learn a mapping from source to target speech without relying on parallel data. The proposed method is general purpose, high quality, and parallel-data free and works without any extra data, modules, or alignment procedure. It also avoids over-smoothing, which occurs in many conventional statistical model-based VC methods. Our method, called CycleGAN-VC, uses a cycle-consistent adversarial network (CycleGAN) with gated convolutional neural networks (CNNs) and an identity-mapping loss. A CycleGAN learns forward and inverse mappings simultaneously using adversarial and cycle-consistency losses. This makes it possible to find an optimal pseudo pair from unpaired data. Furthermore, the adversarial loss contributes to reducing over-smoothing of the converted feature sequence. We configure a CycleGAN with gated CNNs and train it with an identity-mapping loss. This allows the mapping function to capture sequential and hierarchical structures while preserving linguistic information. We evaluated our method on a parallel-data-free VC task. An objective evaluation showed that the converted feature sequence was near natural in terms of global variance and modulation spectra. A subjective evaluation showed that the quality of the converted speech was comparable to that obtained with a Gaussian mixture model-based method under advantageous conditions with parallel and twice the amount of data.

</details>

### [Parallel WaveNet: Fast High-Fidelity Speech Synthesis](1711.10433.md)
**Aaron van den Oord, Yazhe Li, Igor Babuschkin, Karen Simonyan et al.** · 2017-11-28

<details>
<summary>Abstract</summary>

The recently-developed WaveNet architecture is the current state of the art in realistic speech synthesis, consistently rated as more natural sounding for many different languages than any previous system. However, because WaveNet relies on sequential generation of one audio sample at a time, it is poorly suited to today's massively parallel computers, and therefore hard to deploy in a real-time production setting. This paper introduces Probability Density Distillation, a new method for training a parallel feed-forward network from a trained WaveNet with no significant difference in quality. The resulting system is capable of generating high-fidelity speech samples at more than 20 times faster than real-time, and is deployed online by Google Assistant, including serving multiple English and Japanese voices.

</details>

### [Uncovering Latent Style Factors for Expressive Speech Synthesis](1711.00520.md)
**Yuxuan Wang, RJ Skerry-Ryan, Ying Xiao, Daisy Stanton et al.** · 2017-11-01

<details>
<summary>Abstract</summary>

Prosodic modeling is a core problem in speech synthesis. The key challenge is producing desirable prosody from textual input containing only phonetic information. In this preliminary study, we introduce the concept of "style tokens" in Tacotron, a recently proposed end-to-end neural speech synthesis model. Using style tokens, we aim to extract independent prosodic styles from training data. We show that without annotation data or an explicit supervision signal, our approach can automatically learn a variety of prosodic variations in a purely data-driven way. Importantly, each style token corresponds to a fixed style factor regardless of the given text sequence. As a result, we can control the prosodic style of synthetic speech in a somewhat predictable and globally consistent way.

</details>

### [JSUT corpus: free large-scale Japanese speech corpus for end-to-end speech synthesis](1711.00354.md)
**Ryosuke Sonobe, Shinnosuke Takamichi, Hiroshi Saruwatari** · 2017-10-28

<details>
<summary>Abstract</summary>

Thanks to improvements in machine learning techniques including deep learning, a free large-scale speech corpus that can be shared between academic institutions and commercial companies has an important role. However, such a corpus for Japanese speech synthesis does not exist. In this paper, we designed a novel Japanese speech corpus, named the "JSUT corpus," that is aimed at achieving end-to-end speech synthesis. The corpus consists of 10 hours of reading-style speech data and its transcription and covers all of the main pronunciations of daily-use Japanese characters. In this paper, we describe how we designed and analyzed the corpus. The corpus is freely available online.

</details>

### [Efficiently Trainable Text-to-Speech System Based on Deep Convolutional Networks with Guided Attention](1710.08969.md)
**Hideyuki Tachibana, Katsuya Uenoyama, Shunsuke Aihara** · 2017-10-24

<details>
<summary>Abstract</summary>

This paper describes a novel text-to-speech (TTS) technique based on deep convolutional neural networks (CNN), without use of any recurrent units. Recurrent neural networks (RNN) have become a standard technique to model sequential data recently, and this technique has been used in some cutting-edge neural TTS techniques. However, training RNN components often requires a very powerful computer, or a very long time, typically several days or weeks. Recent other studies, on the other hand, have shown that CNN-based sequence synthesis can be much faster than RNN-based techniques, because of high parallelizability. The objective of this paper is to show that an alternative neural TTS based only on CNN alleviate these economic costs of training. In our experiment, the proposed Deep Convolutional TTS was sufficiently trained overnight (15 hours), using an ordinary gaming PC equipped with two GPUs, while the quality of the synthesized speech was almost acceptable.

</details>

### [Deep Voice 3: Scaling Text-to-Speech with Convolutional Sequence Learning](1710.07654.md)
**Wei Ping, Kainan Peng, Andrew Gibiansky, Sercan O. Arik et al.** · 2017-10-20

<details>
<summary>Abstract</summary>

We present Deep Voice 3, a fully-convolutional attention-based neural text-to-speech (TTS) system. Deep Voice 3 matches state-of-the-art neural speech synthesis systems in naturalness while training ten times faster. We scale Deep Voice 3 to data set sizes unprecedented for TTS, training on more than eight hundred hours of audio from over two thousand speakers. In addition, we identify common error modes of attention-based speech synthesis networks, demonstrate how to mitigate them, and compare several different waveform synthesis methods. We also describe how to scale inference to ten million queries per day on one single-GPU server.

</details>

### [Statistical Parametric Speech Synthesis Incorporating Generative Adversarial Networks](1709.08041.md)
**Yuki Saito et.al.** · 2017-09-26

### [Audio Super Resolution using Neural Networks](1708.00853.md)
**Volodymyr Kuleshov, S. Zayd Enam, Stefano Ermon** · 2017-08-02

<details>
<summary>Abstract</summary>

We introduce a new audio processing technique that increases the sampling rate of signals such as speech or music using deep convolutional neural networks. Our model is trained on pairs of low and high-quality audio examples; at test-time, it predicts missing samples within a low-resolution signal in an interpolation process similar to image super-resolution. Our method is simple and does not involve specialized audio processing techniques; in our experiments, it outperforms baselines on standard speech and music benchmarks at upscaling ratios of 2x, 4x, and 6x. The method has practical applications in telephony, compression, and text-to-speech generation; it demonstrates the effectiveness of feed-forward convolutional architectures on an audio generation task.

</details>

### [SPEECH-COCO: 600k Visually Grounded Spoken Captions Aligned to MSCOCO Data Set](1707.08435.md)
**William Havard, Laurent Besacier, Olivier Rosec** · 2017-07-26

<details>
<summary>Abstract</summary>

This paper presents an augmentation of MSCOCO dataset where speech is added to image and text. Speech captions are generated using text-to-speech (TTS) synthesis resulting in 616,767 spoken captions (more than 600h) paired with images. Disfluencies and speed perturbation are added to the signal in order to sound more natural. Each speech signal (WAV) is paired with a JSON file containing exact timecode for each word/syllable/phoneme in the spoken caption. Such a corpus could be used for Language and Vision (LaVi) tasks including speech input or output instead of text. Investigating multimodal learning schemes for unsupervised speech pattern discovery is also possible with this corpus, as demonstrated by a preliminary study conducted on a subset of the corpus (10h, 10k spoken captions). The dataset is available on Zenodo: https://zenodo.org/record/4282267

</details>

### [VoiceLoop: Voice Fitting and Synthesis via a Phonological Loop](1707.06588.md)
**Yaniv Taigman, Lior Wolf, Adam Polyak, Eliya Nachmani** · 2017-07-20

<details>
<summary>Abstract</summary>

We present a new neural text to speech (TTS) method that is able to transform text to speech in voices that are sampled in the wild. Unlike other systems, our solution is able to deal with unconstrained voice samples and without requiring aligned phonemes or linguistic features. The network architecture is simpler than those in the existing literature and is based on a novel shifting buffer working memory. The same buffer is used for estimating the attention, computing the output audio, and for updating the buffer itself. The input sentence is encoded using a context-free lookup table that contains one entry per character or phoneme. The speakers are similarly represented by a short vector that can also be fitted to new identities, even with only a few samples. Variability in the generated speech is achieved by priming the buffer prior to generating the audio. Experimental results on several datasets demonstrate convincing capabilities, making TTS accessible to a wider range of applications. In order to promote reproducibility, we release our source code and models.

</details>

### [Statistical Parametric Speech Synthesis Using Generative Adversarial Networks Under A Multi-task Learning Framework](1707.01670.md)
**Shan Yang, Lei Xie, Xiao Chen, Xiaoyan Lou et al.** · 2017-07-06

<details>
<summary>Abstract</summary>

In this paper, we aim at improving the performance of synthesized speech in statistical parametric speech synthesis (SPSS) based on a generative adversarial network (GAN). In particular, we propose a novel architecture combining the traditional acoustic loss function and the GAN's discriminative loss under a multi-task learning (MTL) framework. The mean squared error (MSE) is usually used to estimate the parameters of deep neural networks, which only considers the numerical difference between the raw audio and the synthesized one. To mitigate this problem, we introduce the GAN as a second task to determine if the input is a natural speech with specific conditions. In this MTL framework, the MSE optimization improves the stability of GAN, and at the same time GAN produces samples with a distribution closer to natural speech. Listening tests show that the multi-task architecture can generate more natural speech that satisfies human perception than the conventional methods.

</details>

### [Hidden-Markov-Model Based Speech Enhancement](1707.01090.md)
**Daniel Dzibela, Armin Sehr** · 2017-07-04

<details>
<summary>Abstract</summary>

The goal of this contribution is to use a parametric speech synthesis system for reducing background noise and other interferences from recorded speech signals. In a first step, Hidden Markov Models of the synthesis system are trained. Two adequate training corpora consisting of text and corresponding speech files have been set up and cleared of various faults, including inaudible utterances or incorrect assignments between audio and text data. Those are tested and compared against each other regarding e.g. flaws in the synthesized speech, it's naturalness and intelligibility. Thus different voices have been synthesized, whose quality depends less on the number of training samples used, but much more on the cleanliness and signal-to-noise ratio of those. Generalized voice models have been used for synthesis and the results greatly differ between the two speech corpora. Tests regarding the adaptation to different speakers show that a resemblance to the original speaker is audible throughout all recordings, yet the synthesized voices sound robotic and unnatural in smaller parts. The spoken text, however, is usually intelligible, which shows that the models are working well. In a novel approach, speech is synthesized using side information of the original audio signal, particularly the pitch frequency. Results show an increase of speech quality and intelligibility in comparison to speech synthesized solely from text, up to the point of being nearly indistinguishable from the original.

</details>

### [Deep Voice 2: Multi-Speaker Neural Text-to-Speech](1705.08947.md)
**Sercan Arik, Gregory Diamos, Andrew Gibiansky, John Miller et al.** · 2017-05-24

<details>
<summary>Abstract</summary>

We introduce a technique for augmenting neural text-to-speech (TTS) with lowdimensional trainable speaker embeddings to generate different voices from a single model. As a starting point, we show improvements over the two state-ofthe-art approaches for single-speaker neural TTS: Deep Voice 1 and Tacotron. We introduce Deep Voice 2, which is based on a similar pipeline with Deep Voice 1, but constructed with higher performance building blocks and demonstrates a significant audio quality improvement over Deep Voice 1. We improve Tacotron by introducing a post-processing neural vocoder, and demonstrate a significant audio quality improvement. We then demonstrate our technique for multi-speaker speech synthesis for both Deep Voice 2 and Tacotron on two multi-speaker TTS datasets. We show that a single neural TTS system can learn hundreds of unique voices from less than half an hour of data per speaker, while achieving high audio quality synthesis and preserving the speaker identities almost perfectly.

</details>

### [Learning Latent Representations for Speech Generation and Transformation](1704.04222.md)
**Wei-Ning Hsu, Yu Zhang, James Glass** · 2017-04-13

<details>
<summary>Abstract</summary>

An ability to model a generative process and learn a latent representation for speech in an unsupervised fashion will be crucial to process vast quantities of unlabelled speech data. Recently, deep probabilistic generative models such as Variational Autoencoders (VAEs) have achieved tremendous success in modeling natural images. In this paper, we apply a convolutional VAE to model the generative process of natural speech. We derive latent space arithmetic operations to disentangle learned latent representations. We demonstrate the capability of our model to modify the phonetic content or the speaker identity for speech segments using the derived operations, without the need for parallel supervisory data.

</details>

### [Sampling-based speech parameter generation using moment-matching networks](1704.03626.md)
**Shinnosuke Takamichi, Tomoki Koriyama, Hiroshi Saruwatari** · 2017-04-12

<details>
<summary>Abstract</summary>

This paper presents sampling-based speech parameter generation using moment-matching networks for Deep Neural Network (DNN)-based speech synthesis. Although people never produce exactly the same speech even if we try to express the same linguistic and para-linguistic information, typical statistical speech synthesis produces completely the same speech, i.e., there is no inter-utterance variation in synthetic speech. To give synthetic speech natural inter-utterance variation, this paper builds DNN acoustic models that make it possible to randomly sample speech parameters. The DNNs are trained so that they make the moments of generated speech parameters close to those of natural speech parameters. Since the variation of speech parameters is compressed into a low-dimensional simple prior noise vector, our algorithm has lower computation cost than direct sampling of speech parameters. As the first step towards generating synthetic speech that has natural inter-utterance variation, this paper investigates whether or not the proposed sampling-based generation deteriorates synthetic speech quality. In evaluation, we compare speech quality of conventional maximum likelihood-based generation and proposed sampling-based generation. The result demonstrates the proposed generation causes no degradation in speech quality.

</details>

### [Voice Conversion from Unaligned Corpora using Variational Autoencoding Wasserstein Generative Adversarial Networks](1704.00849.md)
**Chin-Cheng Hsu, Hsin-Te Hwang, Yi-Chiao Wu, Yu Tsao et al.** · 2017-04-04

<details>
<summary>Abstract</summary>

Building a voice conversion (VC) system from non-parallel speech corpora is challenging but highly valuable in real application scenarios. In most situations, the source and the target speakers do not repeat the same texts or they may even speak different languages. In this case, one possible, although indirect, solution is to build a generative model for speech. Generative models focus on explaining the observations with latent variables instead of learning a pairwise transformation function, thereby bypassing the requirement of speech frame alignment. In this paper, we propose a non-parallel VC framework with a variational autoencoding Wasserstein generative adversarial network (VAW-GAN) that explicitly considers a VC objective when building the speech model. Experimental results corroborate the capability of our framework for building a VC system from unaligned data, and demonstrate improved conversion quality.

</details>

### [PROSODY PREDICTION FOR TAMIL TEXT-TO-SPEECH SYNTHESIZER USING SENTIMENT ANALYSIS](s2:9ca31730a8779aaf08c9c3be95250aff3f7765e4.md)
**Vaibhavi Rajendran, B. Kumar** · 2017-04-01

<details>
<summary>Abstract</summary>

A speech synthesizer which sounds similar to a human voice is preferred over a robotic voice, and hence to increase the naturalness of a speech synthesizer an efficacious prosody model is imperative. Hence, this paper is focused on developing a prosody prediction model using sentiment analysis for a Tamil speech synthesizer. Two variations of prosody prediction models using SentiWordNet are experimented: one without a stemmer and the other with a stemmer. The prosody prediction model with a stemmer performs much more efficiently than the one without a stemmer as it tackles the highly agglutinative and inflectional words in Tamil language in a better way and is exemplified clearly, in this paper. The performance of the prosody prediction model with a stemmer has a higher classification accuracy of 77% on the test set in comparison to the 57% accuracy by the prosody model without a stemmer.

</details>

### [Tacotron: Towards End-to-End Speech Synthesis](1703.10135.md)
**Yuxuan Wang, RJ Skerry-Ryan, Daisy Stanton, Yonghui Wu et al.** · 2017-03-29

<details>
<summary>Abstract</summary>

A text-to-speech synthesis system typically consists of multiple stages, such as a text analysis frontend, an acoustic model and an audio synthesis module. Building these components often requires extensive domain expertise and may contain brittle design choices. In this paper, we present Tacotron, an end-to-end generative text-to-speech model that synthesizes speech directly from characters. Given <text, audio> pairs, the model can be trained completely from scratch with random initialization. We present several key techniques to make the sequence-to-sequence framework perform well for this challenging task. Tacotron achieves a 3.82 subjective 5-scale mean opinion score on US English, outperforming a production parametric system in terms of naturalness. In addition, since Tacotron generates speech at the frame level, it's substantially faster than sample-level autoregressive methods.

</details>

### [Tacotron: A Fully End-to-End Text-To-Speech Synthesis Model](s2:4185286ec9d65086803c3ddf1cae1b27a9d6b5bb.md)
**Yuxuan Wang, R. Skerry-Ryan, Daisy Stanton, Yonghui Wu et al.** · 2017-03-29

### [Deep Voice: Real-time Neural Text-to-Speech](1702.07825.md)
**Sercan O. Arik, Mike Chrzanowski, Adam Coates, Gregory Diamos et al.** · 2017-02-25

<details>
<summary>Abstract</summary>

We present Deep Voice, a production-quality text-to-speech system constructed entirely from deep neural networks. Deep Voice lays the groundwork for truly end-to-end neural speech synthesis. The system comprises five major building blocks: a segmentation model for locating phoneme boundaries, a grapheme-to-phoneme conversion model, a phoneme duration prediction model, a fundamental frequency prediction model, and an audio synthesis model. For the segmentation model, we propose a novel way of performing phoneme boundary detection with deep neural networks using connectionist temporal classification (CTC) loss. For the audio synthesis model, we implement a variant of WaveNet that requires fewer parameters and trains faster than the original. By using a neural network for each component, our system is simpler and more flexible than traditional text-to-speech systems, where each component requires laborious feature engineering and extensive domain expertise. Finally, we show that inference with our system can be performed faster than real time and describe optimized WaveNet inference kernels on both CPU and GPU that achieve up to 400x speedups over existing implementations.

</details>

### [Char2Wav: End-to-End Speech Synthesis](s2:9203d6c076bffe87336f2ea91f5851436c02dbe6.md)
**Jose M. R. Sotelo, Soroush Mehri, Kundan Kumar, J. F. Santos et al.** · 2017-02-17

### [Prosody and Prediction in Neural Speech Processing](s2:8a94e63458f01dfdcf591551c23c7ae25da051e6.md)
**Pelle Söderström** · 2017-01-01

### [End-to-End Neural Speech Synthesis](s2:25825b97b3ef21eb50e209961cf72c09755c6b11.md)
**Alex Barron** · 2017-01-01

