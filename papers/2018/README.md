# 2018

86 papers in this year.

### [FPETS : Fully Parallel End-to-End Text-to-Speech System](1812.05710.md)
**Dabiao Ma, Zhiba Su, Wenxuan Wang, Yuhao Lu** · 2018-12-12

<details>
<summary>Abstract</summary>

End-to-end Text-to-speech (TTS) system can greatly improve the quality of synthesised speech. But it usually suffers form high time latency due to its auto-regressive structure. And the synthesised speech may also suffer from some error modes, e.g. repeated words, mispronunciations, and skipped words. In this paper, we propose a novel non-autoregressive, fully parallel end-to-end TTS system (FPETS). It utilizes a new alignment model and the recently proposed U-shape convolutional structure, UFANS. Different from RNN, UFANS can capture long term information in a fully parallel manner. Trainable position encoding and two-step training strategy are used for learning better alignments. Experimental results show FPETS utilizes the power of parallel computation and reaches a significant speed up of inference compared with state-of-the-art end-to-end TTS systems. More specifically, FPETS is 600X faster than Tacotron2, 50X faster than DCTTS and 10X faster than Deep Voice3. And FPETS can generates audios with equal or better quality and fewer errors comparing with other system. As far as we know, FPETS is the first end-to-end TTS system which is fully parallel.

</details>

### [Learning latent representations for style control and transfer in end-to-end speech synthesis](1812.04342.md)
**Ya-Jie Zhang, Shifeng Pan, Lei He, Zhen-Hua Ling** · 2018-12-11

<details>
<summary>Abstract</summary>

In this paper, we introduce the Variational Autoencoder (VAE) to an end-to-end speech synthesis model, to learn the latent representation of speaking styles in an unsupervised manner. The style representation learned through VAE shows good properties such as disentangling, scaling, and combination, which makes it easy for style control. Style transfer can be achieved in this framework by first inferring style representation through the recognition network of VAE, then feeding it into TTS network to guide the style in synthesizing speech. To avoid Kullback-Leibler (KL) divergence collapse in training, several techniques are adopted. Finally, the proposed model shows good performance of style control and outperforms Global Style Token (GST) model in ABX preference tests on style transfer.

</details>

### [Evaluation of Japanese end-to-end speech synthesis method inputting kana and prosodic symbols](s2:eec3899cccd7c87262376a20f4800df31fcb7ecc.md)
**Kurihara Kiyoshi, Seiyama Nobumasa, Kumano Tadashi, Imai Atsushi** · 2018-12-03

### [LP-WaveNet: Linear Prediction-based WaveNet Speech Synthesis](1811.11913.md)
**Min-Jae Hwang, Frank Soong, Eunwoo Song, Xi Wang et al.** · 2018-11-29

<details>
<summary>Abstract</summary>

We propose a linear prediction (LP)-based waveform generation method via WaveNet vocoding framework. A WaveNet-based neural vocoder has significantly improved the quality of parametric text-to-speech (TTS) systems. However, it is challenging to effectively train the neural vocoder when the target database contains massive amount of acoustical information such as prosody, style or expressiveness. As a solution, the approaches that only generate the vocal source component by a neural vocoder have been proposed. However, they tend to generate synthetic noise because the vocal source component is independently handled without considering the entire speech production process; where it is inevitable to come up with a mismatch between vocal source and vocal tract filter. To address this problem, we propose an LP-WaveNet vocoder, where the complicated interactions between vocal source and vocal tract components are jointly trained within a mixture density network-based WaveNet model. The experimental results verify that the proposed system outperforms the conventional WaveNet vocoders both objectively and subjectively. In particular, the proposed method achieves 4.47 MOS within the TTS framework.

</details>

### [UFANS: U-shaped Fully-Parallel Acoustic Neural Structure For Statistical Parametric Speech Synthesis With 20X Faster](1811.12208.md)
**Dabiao Ma, Zhiba Su, Yuhao Lu, Wenxuan Wang et al.** · 2018-11-28

<details>
<summary>Abstract</summary>

Neural networks with Auto-regressive structures, such as Recurrent Neural Networks (RNNs), have become the most appealing structures for acoustic modeling of parametric text to speech synthesis (TTS) in ecent studies. Despite the prominent capacity to capture long-term dependency, these models consist of massive sequential computations that cannot be fully parallel. In this paper, we propose a U-shaped Fully-parallel Acoustic Neural Structure (UFANS), which is a deconvolutional alternative of RNNs for Statistical Parametric Speech Synthesis (SPSS). The experiments verify that our proposed model is over 20 times faster than RNN based acoustic model, both training and inference on GPU with comparable speech quality. Furthermore, We also investigate that how long information dependence really matters to synthesized speech quality.

</details>

### [Refined WaveNet Vocoder for Variational Autoencoder Based Voice Conversion](1811.11078.md)
**Wen-Chin Huang, Yi-Chiao Wu, Hsin-Te Hwang, Patrick Lumban Tobing et al.** · 2018-11-27

<details>
<summary>Abstract</summary>

This paper presents a refinement framework of WaveNet vocoders for variational autoencoder (VAE) based voice conversion (VC), which reduces the quality distortion caused by the mismatch between the training data and testing data. Conventional WaveNet vocoders are trained with natural acoustic features but conditioned on the converted features in the conversion stage for VC, and such a mismatch often causes significant quality and similarity degradation. In this work, we take advantage of the particular structure of VAEs to refine WaveNet vocoders with the self-reconstructed features generated by VAE, which are of similar characteristics with the converted features while having the same temporal structure with the target natural features. We analyze these features and show that the self-reconstructed features are similar to the converted features. Objective and subjective experimental results demonstrate the effectiveness of our proposed framework.

</details>

### [TrIMS: Transparent and Isolated Model Sharing for Low Latency Deep LearningInference in Function as a Service Environments](1811.09732.md)
**Abdul Dakkak, Cheng Li, Simon Garcia de Gonzalo, Jinjun Xiong et al.** · 2018-11-24

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have become core computation components within low latency Function as a Service (FaaS) prediction pipelines: including image recognition, object detection, natural language processing, speech synthesis, and personalized recommendation pipelines. Cloud computing, as the de-facto backbone of modern computing infrastructure for both enterprise and consumer applications, has to be able to handle user-defined pipelines of diverse DNN inference workloads while maintaining isolation and latency guarantees, and minimizing resource waste. The current solution for guaranteeing isolation within FaaS is suboptimal -- suffering from "cold start" latency. A major cause of such inefficiency is the need to move large amount of model data within and across servers. We propose TrIMS as a novel solution to address these issues. Our proposed solution consists of a persistent model store across the GPU, CPU, local storage, and cloud storage hierarchy, an efficient resource management layer that provides isolation, and a succinct set of application APIs and container technologies for easy and transparent integration with FaaS, Deep Learning (DL) frameworks, and user code. We demonstrate our solution by interfacing TrIMS with the Apache MXNet framework and demonstrate up to 24x speedup in latency for image classification models and up to 210x speedup for large models. We achieve up to 8x system throughput improvement.

</details>

### [Learning pronunciation from a foreign language in speech synthesis networks](1811.09364.md)
**Younggun Lee, Suwon Shon, Taesu Kim** · 2018-11-23

<details>
<summary>Abstract</summary>

Although there are more than 6,500 languages in the world, the pronunciations of many phonemes sound similar across the languages. When people learn a foreign language, their pronunciation often reflects their native language's characteristics. This motivates us to investigate how the speech synthesis network learns the pronunciation from datasets from different languages. In this study, we are interested in analyzing and taking advantage of multilingual speech synthesis network. First, we train the speech synthesis network bilingually in English and Korean and analyze how the network learns the relations of phoneme pronunciation between the languages. Our experimental result shows that the learned phoneme embedding vectors are located closer if their pronunciations are similar across the languages. Consequently, the trained networks can synthesize the English speakers' Korean speech and vice versa. Using this result, we propose a training framework to utilize information from a different language. To be specific, we pre-train a speech synthesis network using datasets from both high-resource language and low-resource language, then we fine-tune the network using the low-resource language dataset. Finally, we conducted more simulations on 10 different languages to show it is generally extendable to other languages.

</details>

### [Improving Sequence-to-Sequence Acoustic Modeling by Adding Text-Supervision](1811.08111.md)
**Jing-Xuan Zhang, Zhen-Hua Ling, Yuan Jiang, Li-Juan Liu et al.** · 2018-11-20

<details>
<summary>Abstract</summary>

This paper presents methods of making using of text supervision to improve the performance of sequence-to-sequence (seq2seq) voice conversion. Compared with conventional frame-to-frame voice conversion approaches, the seq2seq acoustic modeling method proposed in our previous work achieved higher naturalness and similarity. In this paper, we further improve its performance by utilizing the text transcriptions of parallel training data. First, a multi-task learning structure is designed which adds auxiliary classifiers to the middle layers of the seq2seq model and predicts linguistic labels as a secondary task. Second, a data-augmentation method is proposed which utilizes text alignment to produce extra parallel sequences for model training. Experiments are conducted to evaluate our proposed method with training sets at different sizes. Experimental results show that the multi-task learning with linguistic labels is effective at reducing the errors of seq2seq voice conversion. The data-augmentation method can further improve the performance of seq2seq voice conversion when only 50 or 100 training utterances are available.

</details>

### [Representation Mixing for TTS Synthesis](1811.07240.md)
**Kyle Kastner, João Felipe Santos, Yoshua Bengio, Aaron Courville** · 2018-11-17

<details>
<summary>Abstract</summary>

Recent character and phoneme-based parametric TTS systems using deep learning have shown strong performance in natural speech generation. However, the choice between character or phoneme input can create serious limitations for practical deployment, as direct control of pronunciation is crucial in certain cases. We demonstrate a simple method for combining multiple types of linguistic information in a single encoder, named representation mixing, enabling flexible choice between character, phoneme, or mixed representations during inference. Experiments and user studies on a public audiobook corpus show the efficacy of our approach.

</details>

### [Effect of data reduction on sequence-to-sequence neural TTS](1811.06315.md)
**Javier Latorre, Jakub Lachowicz, Jaime Lorenzo-Trueba, Thomas Merritt et al.** · 2018-11-15

<details>
<summary>Abstract</summary>

Recent speech synthesis systems based on sampling from autoregressive neural networks models can generate speech almost undistinguishable from human recordings. However, these models require large amounts of data. This paper shows that the lack of data from one speaker can be compensated with data from other speakers. The naturalness of Tacotron2-like models trained on a blend of 5k utterances from 7 speakers is better than that of speaker dependent models trained on 15k utterances, but in terms of stability multi-speaker models are always more stable. We also demonstrate that models mixing only 1250 utterances from a target speaker with 5k utterances from another 6 speakers can produce significantly better quality than state-of-the-art DNN-guided unit selection systems trained on more than 10 times the data from the target speaker.

</details>

### [Towards achieving robust universal neural vocoding](1811.06292.md)
**Jaime Lorenzo-Trueba, Thomas Drugman, Javier Latorre, Thomas Merritt et al.** · 2018-11-15

<details>
<summary>Abstract</summary>

This paper explores the potential universality of neural vocoders. We train a WaveRNN-based vocoder on 74 speakers coming from 17 languages. This vocoder is shown to be capable of generating speech of consistently good quality (98% relative mean MUSHRA when compared to natural speech) regardless of whether the input spectrogram comes from a speaker or style seen during training or from an out-of-domain scenario when the recording conditions are studio-quality. When the recordings show significant changes in quality, or when moving towards non-speech vocalizations or singing, the vocoder still significantly outperforms speaker-dependent vocoders, but operates at a lower average relative MUSHRA of 75%. These results are shown to be consistent across languages, regardless of them being seen during training (e.g. English or Japanese) or unseen (e.g. Wolof, Swahili, Ahmaric).

</details>

### [PerformanceNet: Score-to-Audio Music Generation with Multi-Band Convolutional Residual Network](1811.04357.md)
**Bryan Wang, Yi-Hsuan Yang** · 2018-11-11

<details>
<summary>Abstract</summary>

Music creation is typically composed of two parts: composing the musical score, and then performing the score with instruments to make sounds. While recent work has made much progress in automatic music generation in the symbolic domain, few attempts have been made to build an AI model that can render realistic music audio from musical scores. Directly synthesizing audio with sound sample libraries often leads to mechanical and deadpan results, since musical scores do not contain performance-level information, such as subtle changes in timing and dynamics. Moreover, while the task may sound like a text-to-speech synthesis problem, there are fundamental differences since music audio has rich polyphonic sounds. To build such an AI performer, we propose in this paper a deep convolutional model that learns in an end-to-end manner the score-to-audio mapping between a symbolic representation of music called the piano rolls and an audio representation of music called the spectrograms. The model consists of two subnets: the ContourNet, which uses a U-Net structure to learn the correspondence between piano rolls and spectrograms and to give an initial result; and the TextureNet, which further uses a multi-band residual network to refine the result by adding the spectral texture of overtones and timbre. We train the model to generate music clips of the violin, cello, and flute, with a dataset of moderate size. We also present the result of a user study that shows our model achieves higher mean opinion score (MOS) in naturalness and emotional expressivity than a WaveNet-based model and two commercial sound libraries. We open our source code at https://github.com/bwang514/PerformanceNet

</details>

### [AttS2S-VC: Sequence-to-Sequence Voice Conversion with Attention and Context Preservation Mechanisms](1811.04076.md)
**Kou Tanaka, Hirokazu Kameoka, Takuhiro Kaneko, Nobukatsu Hojo** · 2018-11-09

<details>
<summary>Abstract</summary>

This paper describes a method based on a sequence-to-sequence learning (Seq2Seq) with attention and context preservation mechanism for voice conversion (VC) tasks. Seq2Seq has been outstanding at numerous tasks involving sequence modeling such as speech synthesis and recognition, machine translation, and image captioning. In contrast to current VC techniques, our method 1) stabilizes and accelerates the training procedure by considering guided attention and proposed context preservation losses, 2) allows not only spectral envelopes but also fundamental frequency contours and durations of speech to be converted, 3) requires no context information such as phoneme labels, and 4) requires no time-aligned source and target speech data in advance. In our experiment, the proposed VC framework can be trained in only one day, using only one GPU of an NVIDIA Tesla K80, while the quality of the synthesized speech is higher than that of speech converted by Gaussian mixture model-based VC and is comparable to that of speech generated by recurrent neural network-based text-to-speech synthesis, which can be regarded as an upper limit on VC performance.

</details>

### [Distribution-Preserving Steganography Based on Text-to-Speech Generative Models](1811.03732.md)
**Kejiang Chen, Hang Zhou, Hanqing Zhao, Dongdong Chen et al.** · 2018-11-09

<details>
<summary>Abstract</summary>

Steganography is the art and science of hiding secret messages in public communication so that the presence of the secret messages cannot be detected. There are two distribution-preserving steganographic frameworks, one is sampling-based and the other is compression-based. The former requires a perfect sampler which yields data following the same distribution, and the latter needs explicit distribution of generative objects. However, these two conditions are too strict even unrealistic in the traditional data environment, e.g. the distribution of natural images is hard to seize. Fortunately, generative models bring new vitality to distribution-preserving steganography, which can serve as the perfect sampler or provide the explicit distribution of generative media. Take text-to-speech generation task as an example, we propose distribution-preserving steganography based on WaveGlow and WaveNet, which corresponds to the former two categories. Steganalysis experiments and theoretical analysis are conducted to demonstrate that the proposed methods can preserve the distribution.

</details>

### [ExcitNet vocoder: A neural excitation model for parametric speech synthesis systems](1811.04769.md)
**Eunwoo Song, Kyungguen Byun, Hong-Goo Kang** · 2018-11-09

<details>
<summary>Abstract</summary>

This paper proposes a WaveNet-based neural excitation model (ExcitNet) for statistical parametric speech synthesis systems. Conventional WaveNet-based neural vocoding systems significantly improve the perceptual quality of synthesized speech by statistically generating a time sequence of speech waveforms through an auto-regressive framework. However, they often suffer from noisy outputs because of the difficulties in capturing the complicated time-varying nature of speech signals. To improve modeling efficiency, the proposed ExcitNet vocoder employs an adaptive inverse filter to decouple spectral components from the speech signal. The residual component, i.e. excitation signal, is then trained and generated within the WaveNet framework. In this way, the quality of the synthesized speech signal can be further improved since the spectral component is well represented by a deep learning framework and, moreover, the residual component is efficiently generated by the WaveNet framework. Experimental results show that the proposed ExcitNet vocoder, trained both speaker-dependently and speaker-independently, outperforms traditional linear prediction vocoders and similarly configured conventional WaveNet vocoders.

</details>

### [Speaker-adaptive neural vocoders for parametric speech synthesis systems](1811.03311.md)
**Eunwoo Song, Jin-Seob Kim, Kyungguen Byun, Hong-Goo Kang** · 2018-11-08

<details>
<summary>Abstract</summary>

This paper proposes speaker-adaptive neural vocoders for parametric text-to-speech (TTS) systems. Recently proposed WaveNet-based neural vocoding systems successfully generate a time sequence of speech signal with an autoregressive framework. However, it remains a challenge to synthesize high-quality speech when the amount of a target speaker's training data is insufficient. To generate more natural speech signals with the constraint of limited training data, we propose a speaker adaptation task with an effective variation of neural vocoding models. In the proposed method, a speaker-independent training method is applied to capture universal attributes embedded in multiple speakers, and the trained model is then optimized to represent the specific characteristics of the target speaker. Experimental results verify that the proposed TTS systems with speaker-adaptive neural vocoders outperform those with traditional source-filter model-based vocoders and those with WaveNet vocoders, trained either speaker-dependently or speaker-independently. In particular, our TTS system achieves 3.80 and 3.77 MOS for the Korean male and Korean female speakers, respectively, even though we use only ten minutes' speech corpus for training the model.

</details>

### [FloWaveNet : A Generative Flow for Raw Audio](1811.02155.md)
**Sungwon Kim, Sang-gil Lee, Jongyoon Song, Jaehyeon Kim et al.** · 2018-11-06

<details>
<summary>Abstract</summary>

Most modern text-to-speech architectures use a WaveNet vocoder for synthesizing high-fidelity waveform audio, but there have been limitations, such as high inference time, in its practical application due to its ancestral sampling scheme. The recently suggested Parallel WaveNet and ClariNet have achieved real-time audio synthesis capability by incorporating inverse autoregressive flow for parallel sampling. However, these approaches require a two-stage training pipeline with a well-trained teacher network and can only produce natural sound by using probability distillation along with auxiliary loss terms. We propose FloWaveNet, a flow-based generative model for raw audio synthesis. FloWaveNet requires only a single-stage training procedure and a single maximum likelihood loss, without any additional auxiliary terms, and it is inherently parallel due to the characteristics of generative flow. The model can efficiently sample raw audio in real-time, with clarity comparable to previous two-stage parallel models. The code and samples for all models, including our FloWaveNet, are publicly available.

</details>

### [Robust and fine-grained prosody control of end-to-end speech synthesis](1811.02122.md)
**Younggun Lee, Taesu Kim** · 2018-11-06

<details>
<summary>Abstract</summary>

We propose prosody embeddings for emotional and expressive speech synthesis networks. The proposed methods introduce temporal structures in the embedding networks, thus enabling fine-grained control of the speaking style of the synthesized speech. The temporal structures can be designed either on the speech side or the text side, leading to different control resolutions in time. The prosody embedding networks are plugged into end-to-end speech synthesis networks and trained without any other supervision except for the target speech for synthesizing. It is demonstrated that the prosody embedding networks learned to extract prosodic features. By adjusting the learned prosody features, we could change the pitch and amplitude of the synthesized speech both at the frame level and the phoneme level. We also introduce the temporal normalization of prosody embeddings, which shows better robustness against speaker perturbations during prosody transfer tasks.

</details>

### [ConvS2S-VC: Fully convolutional sequence-to-sequence voice conversion](1811.01609.md)
**Hirokazu Kameoka, Kou Tanaka, Damian Kwasny, Takuhiro Kaneko et al.** · 2018-11-05

<details>
<summary>Abstract</summary>

This paper proposes a voice conversion (VC) method using sequence-to-sequence (seq2seq or S2S) learning, which flexibly converts not only the voice characteristics but also the pitch contour and duration of input speech. The proposed method, called ConvS2S-VC, has three key features. First, it uses a model with a fully convolutional architecture. This is particularly advantageous in that it is suitable for parallel computations using GPUs. It is also beneficial since it enables effective normalization techniques such as batch normalization to be used for all the hidden layers in the networks. Second, it achieves many-to-many conversion by simultaneously learning mappings among multiple speakers using only a single model instead of separately learning mappings between each speaker pair using a different model. This enables the model to fully utilize available training data collected from multiple speakers by capturing common latent features that can be shared across different speakers. Owing to this structure, our model works reasonably well even without source speaker information, thus making it able to handle any-to-many conversion tasks. Third, we introduce a mechanism, called the conditional batch normalization that switches batch normalization layers in accordance with the target speaker. This particular mechanism has been found to be extremely effective for our many-to-many conversion model. We conducted speaker identity conversion experiments and found that ConvS2S-VC obtained higher sound quality and speaker similarity than baseline methods. We also found from audio examples that it could perform well in various tasks including emotional expression conversion, electrolaryngeal speech enhancement, and English accent conversion.

</details>

### [Investigating context features hidden in End-to-End TTS](1811.01376.md)
**Kohki Mametani, Tsuneo Kato, Seiichi Yamamoto** · 2018-11-04

<details>
<summary>Abstract</summary>

Recent studies have introduced end-to-end TTS, which integrates the production of context and acoustic features in statistical parametric speech synthesis. As a result, a single neural network replaced laborious feature engineering with automated feature learning. However, little is known about what types of context information end-to-end TTS extracts from text input before synthesizing speech, and the previous knowledge about context features is barely utilized. In this work, we first point out the model similarity between end-to-end TTS and parametric TTS. Based on the similarity, we evaluate the quality of encoder outputs from an end-to-end TTS system against eight criteria that are derived from a standard set of context information used in parametric TTS. We conduct experiments using an evaluation procedure that has been newly developed in the machine learning literature for quantitative analysis of neural representations, while adapting it to the TTS domain. Experimental results show that the encoder outputs reflect both linguistic and phonetic contexts, such as vowel reduction at phoneme level, lexical stress at syllable level, and part-of-speech at word level, possibly due to the joint optimization of context and acoustic features.

</details>

### [A speech-based driver assisting module for Intelligent Transport System](1810.13206.md)
**Himangshu Sarma, Navanath Saharia** · 2018-10-31

<details>
<summary>Abstract</summary>

Aim of this research is to transform images of roadside traffic panels to speech to assist the vehicle driver, which is a new approach in the state-of-the-art of the advanced driver assistance systems. The designed system comprises of three modules, where the first module is used to capture and detect the text area in traffic panels, second module is responsible for converting the image of the detected text area to editable text and the last module is responsible for transforming the text to speech. Additionally, during experiments, we developed a corpus of 250 images of traffic panels for two Indian languages.

</details>

### [WaveGlow: A Flow-based Generative Network for Speech Synthesis](1811.00002.md)
**Ryan Prenger, Rafael Valle, Bryan Catanzaro** · 2018-10-31

<details>
<summary>Abstract</summary>

In this paper we propose WaveGlow: a flow-based network capable of generating high quality speech from mel-spectrograms. WaveGlow combines insights from Glow and WaveNet in order to provide fast, efficient and high-quality audio synthesis, without the need for auto-regression. WaveGlow is implemented using only a single network, trained using only a single cost function: maximizing the likelihood of the training data, which makes the training procedure simple and stable. Our PyTorch implementation produces audio samples at a rate of more than 500 kHz on an NVIDIA V100 GPU. Mean Opinion Scores show that it delivers audio quality as good as the best publicly available WaveNet implementation. All code will be made publicly available online.

</details>

### [Waveform generation for text-to-speech synthesis using pitch-synchronous multi-scale generative adversarial networks](1810.12598.md)
**Lauri Juvela, Bajibabu Bollepalli, Junichi Yamagishi, Paavo Alku** · 2018-10-30

<details>
<summary>Abstract</summary>

The state-of-the-art in text-to-speech synthesis has recently improved considerably due to novel neural waveform generation methods, such as WaveNet. However, these methods suffer from their slow sequential inference process, while their parallel versions are difficult to train and even more expensive computationally. Meanwhile, generative adversarial networks (GANs) have achieved impressive results in image generation and are making their way into audio applications; parallel inference is among their lucrative properties. By adopting recent advances in GAN training techniques, this investigation studies waveform generation for TTS in two domains (speech signal and glottal excitation). Listening test results show that while direct waveform generation with GAN is still far behind WaveNet, a GAN-based glottal excitation model can achieve quality and voice similarity on par with a WaveNet vocoder.

</details>

### [Generative Adversarial Networks for Unpaired Voice Transformation on Impaired Speech](1810.12656.md)
**Li-Wei Chen, Hung-Yi Lee, Yu Tsao** · 2018-10-30

<details>
<summary>Abstract</summary>

This paper focuses on using voice conversion (VC) to improve the speech intelligibility of surgical patients who have had parts of their articulators removed. Due to the difficulty of data collection, VC without parallel data is highly desired. Although techniques for unparallel VC, for example, CycleGAN, have been developed, they usually focus on transforming the speaker identity, and directly transforming the speech of one speaker to that of another speaker and as such do not address the task here. In this paper, we propose a new approach for unparallel VC. The proposed approach transforms impaired speech to normal speech while preserving the linguistic content and speaker characteristics. To our knowledge, this is the first end-to-end GAN-based unsupervised VC model applied to impaired speech. The experimental results show that the proposed approach outperforms CycleGAN.

</details>

### [Speaking style adaptation in Text-To-Speech synthesis using Sequence-to-sequence models with attention](1810.12051.md)
**Bajibabu Bollepalli, Lauri Juvela, Paavo Alku** · 2018-10-29

<details>
<summary>Abstract</summary>

Currently, there are increasing interests in text-to-speech (TTS) synthesis to use sequence-to-sequence models with attention. These models are end-to-end meaning that they learn both co-articulation and duration properties directly from text and speech. Since these models are entirely data-driven, they need large amounts of data to generate synthetic speech with good quality. However, in challenging speaking styles, such as Lombard speech, it is difficult to record sufficiently large speech corpora. Therefore, in this study we propose a transfer learning method to adapt a sequence-to-sequence based TTS system of normal speaking style to Lombard style. Moreover, we experiment with a WaveNet vocoder in synthesis of Lombard speech. We conducted subjective evaluations to assess the performance of the adapted TTS systems. The subjective evaluation results indicated that an adaptation system with the WaveNet vocoder clearly outperformed the conventional deep neural network based TTS system in synthesis of Lombard speech.

</details>

### [Investigation of enhanced Tacotron text-to-speech synthesis systems with self-attention for pitch accent language](1810.11960.md)
**Yusuke Yasuda, Xin Wang, Shinji Takaki, Junichi Yamagishi** · 2018-10-29

<details>
<summary>Abstract</summary>

End-to-end speech synthesis is a promising approach that directly converts raw text to speech. Although it was shown that Tacotron2 outperforms classical pipeline systems with regards to naturalness in English, its applicability to other languages is still unknown. Japanese could be one of the most difficult languages for which to achieve end-to-end speech synthesis, largely due to its character diversity and pitch accents. Therefore, state-of-the-art systems are still based on a traditional pipeline framework that requires a separate text analyzer and duration model. Towards end-to-end Japanese speech synthesis, we extend Tacotron to systems with self-attention to capture long-term dependencies related to pitch accents and compare their audio quality with classical pipeline systems under various conditions to show their pros and cons. In a large-scale listening test, we investigated the impacts of the presence of accentual-type labels, the use of force or predicted alignments, and acoustic features used as local condition parameters of the Wavenet vocoder. Our results reveal that although the proposed systems still do not match the quality of a top-line pipeline system for Japanese, we show important stepping stones towards end-to-end Japanese speech synthesis.

</details>

### [Neural source-filter-based waveform model for statistical parametric speech synthesis](1810.11946.md)
**Xin Wang, Shinji Takaki, Junichi Yamagishi** · 2018-10-29

<details>
<summary>Abstract</summary>

Neural waveform models such as the WaveNet are used in many recent text-to-speech systems, but the original WaveNet is quite slow in waveform generation because of its autoregressive (AR) structure. Although faster non-AR models were recently reported, they may be prohibitively complicated due to the use of a distilling training method and the blend of other disparate training criteria. This study proposes a non-AR neural source-filter waveform model that can be directly trained using spectrum-based training criteria and the stochastic gradient descent method. Given the input acoustic features, the proposed model first uses a source module to generate a sine-based excitation signal and then uses a filter module to transform the excitation signal into the output speech waveform. Our experiments demonstrated that the proposed model generated waveforms at least 100 times faster than the AR WaveNet and the quality of its synthetic speech is close to that of speech generated by the AR WaveNet. Ablation test results showed that both the sine-wave excitation signal and the spectrum-based training criteria were essential to the performance of the proposed model.

</details>

### [LPCNet: Improving Neural Speech Synthesis Through Linear Prediction](1810.11846.md)
**Jean-Marc Valin, Jan Skoglund** · 2018-10-28

<details>
<summary>Abstract</summary>

Neural speech synthesis models have recently demonstrated the ability to synthesize high quality speech for text-to-speech and compression applications. These new models often require powerful GPUs to achieve real-time operation, so being able to reduce their complexity would open the way for many new applications. We propose LPCNet, a WaveRNN variant that combines linear prediction with recurrent neural networks to significantly improve the efficiency of speech synthesis. We demonstrate that LPCNet can achieve significantly higher quality than WaveRNN for the same network size and that high quality LPCNet speech synthesis is achievable with a complexity under 3 GFLOPS. This makes it easier to deploy neural synthesis applications on lower-power devices, such as embedded systems and mobile phones.

</details>

### [Spectrogram-channels u-net: a source separation model viewing each channel as the spectrogram of each source](1810.11520.md)
**Jaehoon Oh, Duyeon Kim, Se-Young Yun** · 2018-10-26

<details>
<summary>Abstract</summary>

Sound source separation has attracted attention from Music Information Retrieval(MIR) researchers, since it is related to many MIR tasks such as automatic lyric transcription, singer identification, and voice conversion. In this paper, we propose an intuitive spectrogram-based model for source separation by adapting U-Net. We call it Spectrogram-Channels U-Net, which means each channel of the output corresponds to the spectrogram of separated source itself. The proposed model can be used for not only singing voice separation but also multi-instrument separation by changing only the number of output channels. In addition, we propose a loss function that balances volumes between different sources. Finally, we yield performance that is state-of-the-art on both separation tasks.

</details>

### [Reducing over-smoothness in speech synthesis using Generative Adversarial Networks](1810.10989.md)
**Leyuan Sheng, Evgeniy N. Pavlovskiy** · 2018-10-25

<details>
<summary>Abstract</summary>

Speech synthesis is widely used in many practical applications. In recent years, speech synthesis technology has developed rapidly. However, one of the reasons why synthetic speech is unnatural is that it often has over-smoothness. In order to improve the naturalness of synthetic speech, we first extract the mel-spectrogram of speech and convert it into a real image, then take the over-smooth mel-spectrogram image as input, and use image-to-image translation Generative Adversarial Networks(GANs) framework to generate a more realistic mel-spectrogram. Finally, the results show that this method greatly reduces the over-smoothness of synthesized speech and is more close to the mel-spectrogram of real speech.

</details>

### [Hierarchical Generative Modeling for Controllable Speech Synthesis](1810.07217.md)
**Wei-Ning Hsu, Yu Zhang, Ron J. Weiss, Heiga Zen et al.** · 2018-10-16

<details>
<summary>Abstract</summary>

This paper proposes a neural sequence-to-sequence text-to-speech (TTS) model which can control latent attributes in the generated speech that are rarely annotated in the training data, such as speaking style, accent, background noise, and recording conditions. The model is formulated as a conditional generative model based on the variational autoencoder (VAE) framework, with two levels of hierarchical latent variables. The first level is a categorical variable, which represents attribute groups (e.g. clean/noisy) and provides interpretability. The second level, conditioned on the first, is a multivariate Gaussian variable, which characterizes specific attribute configurations (e.g. noise level, speaking rate) and enables disentangled fine-grained control over these attributes. This amounts to using a Gaussian mixture model (GMM) for the latent distribution. Extensive evaluation demonstrates its ability to control the aforementioned attributes. In particular, we train a high-quality controllable TTS model on real found data, which is capable of inferring speaker and style attributes from a noisy utterance and use it to synthesize clean speech with controllable speaking style.

</details>

### [Diacritization of Maghrebi Arabic Sub-Dialects](1810.06619.md)
**Ahmed Abdelali, Mohammed Attia, Younes Samih, Kareem Darwish et al.** · 2018-10-15

<details>
<summary>Abstract</summary>

Diacritization process attempt to restore the short vowels in Arabic written text; which typically are omitted. This process is essential for applications such as Text-to-Speech (TTS). While diacritization of Modern Standard Arabic (MSA) still holds the lion share, research on dialectal Arabic (DA) diacritization is very limited. In this paper, we present our contribution and results on the automatic diacritization of two sub-dialects of Maghrebi Arabic, namely Tunisian and Moroccan, using a character-level deep neural network architecture that stacks two bi-LSTM layers over a CRF output layer. The model achieves word error rate of 2.7% and 3.6% for Moroccan and Tunisian respectively and is capable of implicitly identifying the sub-dialect of the input.

</details>

### [End-to-End Korean Emotional Speech Synthesis (only abstract)](s2:03bed4a9d93095b0462fd127b6dad31d38f9be6b.md)
**K. Taeho, Soo-Young Lee** · 2018-10-15

### [A Fully Time-domain Neural Model for Subband-based Speech Synthesizer](1810.05319.md)
**Azam Rabiee, Geonmin Kim, Tae-Ho Kim, Soo-Young Lee** · 2018-10-12

<details>
<summary>Abstract</summary>

This paper introduces a deep neural network model for subband-based speech synthesizer. The model benefits from the short bandwidth of the subband signals to reduce the complexity of the time-domain speech generator. We employed the multi-level wavelet analysis/synthesis to decompose/reconstruct the signal into subbands in time domain. Inspired from the WaveNet, a convolutional neural network (CNN) model predicts subband speech signals fully in time domain. Due to the short bandwidth of the subbands, a simple network architecture is enough to train the simple patterns of the subbands accurately. In the ground truth experiments with teacher-forcing, the subband synthesizer outperforms the fullband model significantly in terms of both subjective and objective measures. In addition, by conditioning the model on the phoneme sequence using a pronunciation dictionary, we have achieved the fully time-domain neural model for subband-based text-to-speech (TTS) synthesizer, which is nearly end-to-end. The generated speech of the subband TTS shows comparable quality as the fullband one with a slighter network architecture for each subband.

</details>

### [Sample Efficient Adaptive Text-to-Speech](1809.10460.md)
**Yutian Chen, Yannis Assael, Brendan Shillingford, David Budden et al.** · 2018-09-27

<details>
<summary>Abstract</summary>

We present a meta-learning approach for adaptive text-to-speech (TTS) with few data. During training, we learn a multi-speaker model using a shared conditional WaveNet core and independent learned embeddings for each speaker. The aim of training is not to produce a neural network with fixed weights, which is then deployed as a TTS system. Instead, the aim is to produce a network that requires few data at deployment time to rapidly adapt to new speakers. We introduce and benchmark three strategies: (i) learning the speaker embedding while keeping the WaveNet core fixed, (ii) fine-tuning the entire architecture with stochastic gradient descent, and (iii) predicting the speaker embedding with a trained neural network encoder. The experiments show that these approaches are successful at adapting the multi-speaker neural network to new speakers, obtaining state-of-the-art results in both sample naturalness and voice similarity with merely a few minutes of audio data from new speakers.

</details>

### [Error Reduction Network for DBLSTM-based Voice Conversion](1809.09841.md)
**Mingyang Zhang, Berrak Sisman, Sai Sirisha Rallabandi, Haizhou Li et al.** · 2018-09-26

<details>
<summary>Abstract</summary>

So far, many of the deep learning approaches for voice conversion produce good quality speech by using a large amount of training data. This paper presents a Deep Bidirectional Long Short-Term Memory (DBLSTM) based voice conversion framework that can work with a limited amount of training data. We propose to implement a DBLSTM based average model that is trained with data from many speakers. Then, we propose to perform adaptation with a limited amount of target data. Last but not least, we propose an error reduction network that can improve the voice conversion quality even further. The proposed framework is motivated by three observations. Firstly, DBLSTM can achieve a remarkable voice conversion by considering the long-term dependencies of the speech utterance. Secondly, DBLSTM based average model can be easily adapted with a small amount of data, to achieve a speech that sounds closer to the target. Thirdly, an error reduction network can be trained with a small amount of training data, and can improve the conversion quality effectively. The experiments show that the proposed voice conversion framework is flexible to work with limited training data and outperforms the traditional frameworks in both objective and subjective evaluations.

</details>

### [WaveCycleGAN: Synthetic-to-natural speech waveform conversion using cycle-consistent adversarial networks](1809.10288.md)
**Kou Tanaka, Takuhiro Kaneko, Nobukatsu Hojo, Hirokazu Kameoka** · 2018-09-25

<details>
<summary>Abstract</summary>

We propose a learning-based filter that allows us to directly modify a synthetic speech waveform into a natural speech waveform. Speech-processing systems using a vocoder framework such as statistical parametric speech synthesis and voice conversion are convenient especially for a limited number of data because it is possible to represent and process interpretable acoustic features over a compact space, such as the fundamental frequency (F0) and mel-cepstrum. However, a well-known problem that leads to the quality degradation of generated speech is an over-smoothing effect that eliminates some detailed structure of generated/converted acoustic features. To address this issue, we propose a synthetic-to-natural speech waveform conversion technique that uses cycle-consistent adversarial networks and which does not require any explicit assumption about speech waveform in adversarial learning. In contrast to current techniques, since our modification is performed at the waveform level, we expect that the proposed method will also make it possible to generate `vocoder-less' sounding speech even if the input speech is synthesized using a vocoder framework. The experimental results demonstrate that our proposed method can 1) alleviate the over-smoothing effect of the acoustic features despite the direct modification method used for the waveform and 2) greatly improve the naturalness of the generated speech sounds.

</details>

### [Neural Speech Synthesis with Transformer Network](1809.08895.md)
**Naihan Li, Shujie Liu, Yanqing Liu, Sheng Zhao et al.** · 2018-09-19

<details>
<summary>Abstract</summary>

Although end-to-end neural text-to-speech (TTS) methods (such as Tacotron2) are proposed and achieve state-of-the-art performance, they still suffer from two problems: 1) low efficiency during training and inference; 2) hard to model long dependency using current recurrent neural networks (RNNs). Inspired by the success of Transformer network in neural machine translation (NMT), in this paper, we introduce and adapt the multi-head attention mechanism to replace the RNN structures and also the original attention mechanism in Tacotron2. With the help of multi-head self-attention, the hidden states in the encoder and decoder are constructed in parallel, which improves the training efficiency. Meanwhile, any two inputs at different times are connected directly by self-attention mechanism, which solves the long range dependency problem effectively. Using phoneme sequences as input, our Transformer TTS network generates mel spectrograms, followed by a WaveNet vocoder to output the final audio results. Experiments are conducted to test the efficiency and performance of our new network. For the efficiency, our Transformer TTS network can speed up the training about 4.25 times faster compared with Tacotron2. For the performance, rigorous human tests show that our proposed model achieves state-of-the-art performance (outperforms Tacotron2 with a gap of 0.048) and is very close to human quality (4.39 vs 4.44 in MOS).

</details>

### [Word Emphasis Prediction for Expressive Text to Speech](s2:183ae29882d548bc51ee591188ffa589f8fec77d.md)
**Y. Mass, Slava Shechtman, Moran Mordechay, R. Hoory et al.** · 2018-09-02

<details>
<summary>Abstract</summary>

Word emphasis prediction is an important part of expressive prosody generation in modern Text-To-Speech (TTS) systems. We present a method for predicting emphasized words for expressive TTS, based on a Deep Neural Network (DNN). We show that the presented method outperforms machine learning methods based on hand-crafted features in terms of objective metrics such as precision and recall. Using a listening test, we further demonstrate that the contribution of the predicted emphasized words to the expressiveness of the synthesized speech is subjectively perceivable

</details>

### [Self-Attention Linguistic-Acoustic Decoder](1808.10678.md)
**Santiago Pascual, Antonio Bonafonte, Joan Serrà** · 2018-08-31

<details>
<summary>Abstract</summary>

The conversion from text to speech relies on the accurate mapping from linguistic to acoustic symbol sequences, for which current practice employs recurrent statistical models like recurrent neural networks. Despite the good performance of such models (in terms of low distortion in the generated speech), their recursive structure tends to make them slow to train and to sample from. In this work, we try to overcome the limitations of recursive structure by using a module based on the transformer decoder network, designed without recurrent connections but emulating them with attention and positioning codes. Our results show that the proposed decoder network is competitive in terms of distortion when compared to a recurrent baseline, whilst being significantly faster in terms of CPU inference time. On average, it increases Mel cepstral distortion between 0.1 and 0.3 dB, but it is over an order of magnitude faster on average. Fast inference is important for the deployment of speech synthesis systems on devices with restricted resources, like mobile phones or embedded systems, where speaking virtual assistants are gaining importance.

</details>

### [Semi-Supervised Training for Improving Data Efficiency in End-to-End Speech Synthesis](1808.10128.md)
**Yu-An Chung, Yuxuan Wang, Wei-Ning Hsu, Yu Zhang et al.** · 2018-08-30

<details>
<summary>Abstract</summary>

Although end-to-end text-to-speech (TTS) models such as Tacotron have shown excellent results, they typically require a sizable set of high-quality <text, audio> pairs for training, which are expensive to collect. In this paper, we propose a semi-supervised training framework to improve the data efficiency of Tacotron. The idea is to allow Tacotron to utilize textual and acoustic knowledge contained in large, publicly-available text and speech corpora. Importantly, these external data are unpaired and potentially noisy. Specifically, first we embed each word in the input text into word vectors and condition the Tacotron encoder on them. We then use an unpaired speech corpus to pre-train the Tacotron decoder in the acoustic domain. Finally, we fine-tune the model using available paired data. We demonstrate that the proposed framework enables Tacotron to generate intelligible speech using less than half an hour of paired training data.

</details>

### [Voice Conversion Based on Cross-Domain Features Using Variational Auto Encoders](1808.09634.md)
**Wen-Chin Huang, Hsin-Te Hwang, Yu-Huai Peng, Yu Tsao et al.** · 2018-08-29

<details>
<summary>Abstract</summary>

An effective approach to non-parallel voice conversion (VC) is to utilize deep neural networks (DNNs), specifically variational auto encoders (VAEs), to model the latent structure of speech in an unsupervised manner. A previous study has confirmed the ef- fectiveness of VAE using the STRAIGHT spectra for VC. How- ever, VAE using other types of spectral features such as mel- cepstral coefficients (MCCs), which are related to human per- ception and have been widely used in VC, have not been prop- erly investigated. Instead of using one specific type of spectral feature, it is expected that VAE may benefit from using multi- ple types of spectral features simultaneously, thereby improving the capability of VAE for VC. To this end, we propose a novel VAE framework (called cross-domain VAE, CDVAE) for VC. Specifically, the proposed framework utilizes both STRAIGHT spectra and MCCs by explicitly regularizing multiple objectives in order to constrain the behavior of the learned encoder and de- coder. Experimental results demonstrate that the proposed CD- VAE framework outperforms the conventional VAE framework in terms of subjective tests.

</details>

### [Voice Conversion with Conditional SampleRNN](1808.08311.md)
**Cong Zhou, Michael Horgan, Vivek Kumar, Cristina Vasco et al.** · 2018-08-24

<details>
<summary>Abstract</summary>

Here we present a novel approach to conditioning the SampleRNN generative model for voice conversion (VC). Conventional methods for VC modify the perceived speaker identity by converting between source and target acoustic features. Our approach focuses on preserving voice content and depends on the generative network to learn voice style. We first train a multi-speaker SampleRNN model conditioned on linguistic features, pitch contour, and speaker identity using a multi-speaker speech corpus. Voice-converted speech is generated using linguistic features and pitch contour extracted from the source speaker, and the target speaker identity. We demonstrate that our system is capable of many-to-many voice conversion without requiring parallel data, enabling broad applications. Subjective evaluation demonstrates that our approach outperforms conventional VC methods.

</details>

### [Multimodal speech synthesis architecture for unsupervised speaker adaptation](1808.06288.md)
**Hieu-Thi Luong, Junichi Yamagishi** · 2018-08-20

<details>
<summary>Abstract</summary>

This paper proposes a new architecture for speaker adaptation of multi-speaker neural-network speech synthesis systems, in which an unseen speaker's voice can be built using a relatively small amount of speech data without transcriptions. This is sometimes called "unsupervised speaker adaptation". More specifically, we concatenate the layers to the audio inputs when performing unsupervised speaker adaptation while we concatenate them to the text inputs when synthesizing speech from text. Two new training schemes for the new architecture are also proposed in this paper. These training schemes are not limited to speech synthesis, other applications are suggested. Experimental results show that the proposed model not only enables adaptation to unseen speakers using untranscribed speech but it also improves the performance of multi-speaker modeling and speaker adaptation using transcribed audio files.

</details>

### [Investigation of Using Disentangled and Interpretable Representations for One-shot Cross-lingual Voice Conversion](1808.05294.md)
**Seyed Hamidreza Mohammadi, Taehwan Kim** · 2018-08-15

<details>
<summary>Abstract</summary>

We study the problem of cross-lingual voice conversion in non-parallel speech corpora and one-shot learning setting. Most prior work require either parallel speech corpora or enough amount of training data from a target speaker. However, we convert an arbitrary sentences of an arbitrary source speaker to target speaker's given only one target speaker training utterance. To achieve this, we formulate the problem as learning disentangled speaker-specific and context-specific representations and follow the idea of [1] which uses Factorized Hierarchical Variational Autoencoder (FHVAE). After training FHVAE on multi-speaker training data, given arbitrary source and target speakers' utterance, we estimate those latent representations and then reconstruct the desired utterance of converted voice to that of target speaker. We investigate the effectiveness of the approach by conducting voice conversion experiments with varying size of training utterances and it was able to achieve reasonable performance with even just one training utterance. We also examine the speech representation and show that World vocoder outperforms Short-time Fourier Transform (STFT) used in [1]. Finally, in the subjective tests, for one language and cross-lingual voice conversion, our approach achieved significantly better or comparable results compared to VAE-STFT and GMM baselines in speech quality and similarity.

</details>

### [Mandarin Prosody Prediction Based on Attention Mechanism and Multi-model Ensemble](s2:8f158c234d74e89e3935dd12d6dcd5a90106c1d4.md)
**Kun Xie, W. Pan** · 2018-08-15

### [ACVAE-VC: Non-parallel many-to-many voice conversion with auxiliary classifier variational autoencoder](1808.05092.md)
**Hirokazu Kameoka, Takuhiro Kaneko, Kou Tanaka, Nobukatsu Hojo** · 2018-08-13

<details>
<summary>Abstract</summary>

This paper proposes a non-parallel many-to-many voice conversion (VC) method using a variant of the conditional variational autoencoder (VAE) called an auxiliary classifier VAE (ACVAE). The proposed method has three key features. First, it adopts fully convolutional architectures to construct the encoder and decoder networks so that the networks can learn conversion rules that capture time dependencies in the acoustic feature sequences of source and target speech. Second, it uses an information-theoretic regularization for the model training to ensure that the information in the attribute class label will not be lost in the conversion process. With regular CVAEs, the encoder and decoder are free to ignore the attribute class label input. This can be problematic since in such a situation, the attribute class label will have little effect on controlling the voice characteristics of input speech at test time. Such situations can be avoided by introducing an auxiliary classifier and training the encoder and decoder so that the attribute classes of the decoder outputs are correctly predicted by the classifier. Third, it avoids producing buzzy-sounding speech at test time by simply transplanting the spectral details of the input speech into its converted version. Subjective evaluation experiments revealed that this simple method worked reasonably well in a non-parallel many-to-many speaker identity conversion task.

</details>

### [Rhythm-Flexible Voice Conversion without Parallel Data Using Cycle-GAN over Phoneme Posteriorgram Sequences](1808.03113.md)
**Cheng-chieh Yeh, Po-chun Hsu, Ju-chieh Chou, Hung-yi Lee et al.** · 2018-08-09

<details>
<summary>Abstract</summary>

Speaking rate refers to the average number of phonemes within some unit time, while the rhythmic patterns refer to duration distributions for realizations of different phonemes within different phonetic structures. Both are key components of prosody in speech, which is different for different speakers. Models like cycle-consistent adversarial network (Cycle-GAN) and variational auto-encoder (VAE) have been successfully applied to voice conversion tasks without parallel data. However, due to the neural network architectures and feature vectors chosen for these approaches, the length of the predicted utterance has to be fixed to that of the input utterance, which limits the flexibility in mimicking the speaking rates and rhythmic patterns for the target speaker. On the other hand, sequence-to-sequence learning model was used to remove the above length constraint, but parallel training data are needed. In this paper, we propose an approach utilizing sequence-to-sequence model trained with unsupervised Cycle-GAN to perform the transformation between the phoneme posteriorgram sequences for different speakers. In this way, the length constraint mentioned above is removed to offer rhythm-flexible voice conversion without requiring parallel data. Preliminary evaluation on two datasets showed very encouraging results.

</details>

### [Predicting Expressive Speaking Style From Text In End-To-End Speech Synthesis](1808.01410.md)
**Daisy Stanton, Yuxuan Wang, RJ Skerry-Ryan** · 2018-08-04

<details>
<summary>Abstract</summary>

Global Style Tokens (GSTs) are a recently-proposed method to learn latent disentangled representations of high-dimensional data. GSTs can be used within Tacotron, a state-of-the-art end-to-end text-to-speech synthesis system, to uncover expressive factors of variation in speaking style. In this work, we introduce the Text-Predicted Global Style Token (TP-GST) architecture, which treats GST combination weights or style embeddings as "virtual" speaking style labels within Tacotron. TP-GST learns to predict stylistic renderings from text alone, requiring neither explicit labels during training nor auxiliary inputs for inference. We show that, when trained on a dataset of expressive speech, our system generates audio with more pitch and energy variation than two state-of-the-art baseline models. We further demonstrate that TP-GSTs can synthesize speech with background noise removed, and corroborate these analyses with positive results on human-rated listener preference audiobook tasks. Finally, we demonstrate that multi-speaker TP-GST models successfully factorize speaker identity and speaking style. We provide a website with audio samples for each of our findings.

</details>

### [Investigating accuracy of pitch-accent annotations in neural network-based speech synthesis and denoising effects](1808.00665.md)
**Hieu-Thi Luong, Xin Wang, Junichi Yamagishi, Nobuyuki Nishizawa** · 2018-08-02

<details>
<summary>Abstract</summary>

We investigated the impact of noisy linguistic features on the performance of a Japanese speech synthesis system based on neural network that uses WaveNet vocoder. We compared an ideal system that uses manually corrected linguistic features including phoneme and prosodic information in training and test sets against a few other systems that use corrupted linguistic features. Both subjective and objective results demonstrate that corrupted linguistic features, especially those in the test set, affected the ideal system's performance significantly in a statistical sense due to a mismatched condition between the training and test sets. Interestingly, while an utterance-level Turing test showed that listeners had a difficult time differentiating synthetic speech from natural speech, it further indicated that adding noise to the linguistic features in the training set can partially reduce the effect of the mismatch, regularize the model, and help the system perform better when linguistic features of the test set are noisy.

</details>

### [Wasserstein GAN and Waveform Loss-based Acoustic Model Training for Multi-speaker Text-to-Speech Synthesis Systems Using a WaveNet Vocoder](1807.11679.md)
**Yi Zhao, Shinji Takaki, Hieu-Thi Luong, Junichi Yamagishi et al.** · 2018-07-31

<details>
<summary>Abstract</summary>

Recent neural networks such as WaveNet and sampleRNN that learn directly from speech waveform samples have achieved very high-quality synthetic speech in terms of both naturalness and speaker similarity even in multi-speaker text-to-speech synthesis systems. Such neural networks are being used as an alternative to vocoders and hence they are often called neural vocoders. The neural vocoder uses acoustic features as local condition parameters, and these parameters need to be accurately predicted by another acoustic model. However, it is not yet clear how to train this acoustic model, which is problematic because the final quality of synthetic speech is significantly affected by the performance of the acoustic model. Significant degradation happens, especially when predicted acoustic features have mismatched characteristics compared to natural ones. In order to reduce the mismatched characteristics between natural and generated acoustic features, we propose frameworks that incorporate either a conditional generative adversarial network (GAN) or its variant, Wasserstein GAN with gradient penalty (WGAN-GP), into multi-speaker speech synthesis that uses the WaveNet vocoder. We also extend the GAN frameworks and use the discretized mixture logistic loss of a well-trained WaveNet in addition to mean squared error and adversarial losses as parts of objective functions. Experimental results show that acoustic models trained using the WGAN-GP framework using back-propagated discretized-mixture-of-logistics (DML) loss achieves the highest subjective evaluation scores in terms of both quality and speaker similarity.

</details>

### [Scaling and bias codes for modeling speaker-adaptive DNN-based speech synthesis systems](1807.11632.md)
**Hieu-Thi Luong, Junichi Yamagishi** · 2018-07-31

<details>
<summary>Abstract</summary>

Most neural-network based speaker-adaptive acoustic models for speech synthesis can be categorized into either layer-based or input-code approaches. Although both approaches have their own pros and cons, most existing works on speaker adaptation focus on improving one or the other. In this paper, after we first systematically overview the common principles of neural-network based speaker-adaptive models, we show that these approaches can be represented in a unified framework and can be generalized further. More specifically, we introduce the use of scaling and bias codes as generalized means for speaker-adaptive transformation. By utilizing these codes, we can create a more efficient factorized speaker-adaptive model and capture advantages of both approaches while reducing their disadvantages. The experiments show that the proposed method can improve the performance of speaker adaptation compared with speaker adaptation based on the conventional input code.

</details>

### [Deep Encoder-Decoder Models for Unsupervised Learning of Controllable Speech Synthesis](1807.11470.md)
**Gustav Eje Henter, Jaime Lorenzo-Trueba, Xin Wang, Junichi Yamagishi** · 2018-07-30

<details>
<summary>Abstract</summary>

Generating versatile and appropriate synthetic speech requires control over the output expression separate from the spoken text. Important non-textual speech variation is seldom annotated, in which case output control must be learned in an unsupervised fashion. In this paper, we perform an in-depth study of methods for unsupervised learning of control in statistical speech synthesis. For example, we show that popular unsupervised training heuristics can be interpreted as variational inference in certain autoencoder models. We additionally connect these models to VQ-VAEs, another, recently-proposed class of deep variational autoencoders, which we show can be derived from a very similar mathematical argument. The implications of these new probabilistic interpretations are discussed. We illustrate the utility of the various approaches with an application to acoustic modelling for emotional speech synthesis, where the unsupervised methods for learning expression control (without access to emotional labels) are found to give results that in many aspects match or surpass the previous best supervised approach.

</details>

### [ClariNet: Parallel Wave Generation in End-to-End Text-to-Speech](1807.07281.md)
**Wei Ping, Kainan Peng, Jitong Chen** · 2018-07-19

<details>
<summary>Abstract</summary>

In this work, we propose a new solution for parallel wave generation by WaveNet. In contrast to parallel WaveNet (van den Oord et al., 2018), we distill a Gaussian inverse autoregressive flow from the autoregressive WaveNet by minimizing a regularized KL divergence between their highly-peaked output distributions. Our method computes the KL divergence in closed-form, which simplifies the training algorithm and provides very efficient distillation. In addition, we introduce the first text-to-wave neural architecture for speech synthesis, which is fully convolutional and enables fast end-to-end training from scratch. It significantly outperforms the previous pipeline that connects a text-to-spectrogram model to a separately trained WaveNet (Ping et al., 2018). We also successfully distill a parallel waveform synthesizer conditioned on the hidden representation in this end-to-end model.

</details>

### [Fast approximate simulation of seismic waves with deep learning](1807.06873.md)
**Benjamin Moseley, Andrew Markham, Tarje Nissen-Meyer** · 2018-07-18

<details>
<summary>Abstract</summary>

We simulate the response of acoustic seismic waves in horizontally layered media using a deep neural network. In contrast to traditional finite-difference modelling techniques our network is able to directly approximate the recorded seismic response at multiple receiver locations in a single inference step, without needing to iteratively model the seismic wavefield through time. This results in an order of magnitude reduction in simulation time from the order of 1 s for FD modelling to the order of 0.1 s using our approach. Such a speed improvement could lead to real-time seismic simulation applications and benefit seismic inversion algorithms based on forward modelling, such as full waveform inversion. Our proof of concept deep neural network is trained using 50,000 synthetic examples of seismic waves propagating through different 2D horizontally layered velocity models. We discuss how our approach could be extended to arbitrary velocity models. Our deep neural network design is inspired by the WaveNet architecture used for speech synthesis. We also investigate using deep neural networks for simulating the full seismic wavefield and for carrying out seismic inversion directly.

</details>

### [Forward Attention in Sequence-to-sequence Acoustic Modelling for Speech Synthesis](1807.06736.md)
**Jing-Xuan Zhang, Zhen-Hua Ling, Li-Rong Dai** · 2018-07-18

<details>
<summary>Abstract</summary>

This paper proposes a forward attention method for the sequenceto- sequence acoustic modeling of speech synthesis. This method is motivated by the nature of the monotonic alignment from phone sequences to acoustic sequences. Only the alignment paths that satisfy the monotonic condition are taken into consideration at each decoder timestep. The modified attention probabilities at each timestep are computed recursively using a forward algorithm. A transition agent for forward attention is further proposed, which helps the attention mechanism to make decisions whether to move forward or stay at each decoder timestep. Experimental results show that the proposed forward attention method achieves faster convergence speed and higher stability than the baseline attention method. Besides, the method of forward attention with transition agent can also help improve the naturalness of synthetic speech and control the speed of synthetic speech effectively.

</details>

### [End-to-End Speech Synthesis for Bangla with Text Normalization](s2:d3077f05032d1ac77f24c9e919a7aa44ae82fc60.md)
**T. Pial, Shahreen Salim Aunti, Shabbir Ahmed, Hasnain Heickal** · 2018-07-01

<details>
<summary>Abstract</summary>

Text to speech synthesis is a well-researched area, yet no system has been developed which can claim to be as convincing as a human voice. An end-to-end system in the context of speech synthesis denotes a system capable of synthesizing speech from text using training data as minimal as transcribed audio data without any language-specific knowledge and phoneme dictionaries. But an end-to-end system should also have the capability to integrate any language-specific rules to improve its performance. In this paper, we propose an end-to-end speech synthesis system for Bangla (also known as Bengali) which uses a minimal front end and a neural network as its statistical parametric model. We also propose a Text Normalization Procedure(TNP) for Bangla and incorporate it to the end-to-end system. We have conducted extensive experiments using different models. From the feedback from the participants of the experiment, we have found out that they felt more positively towards the system if TNP is incorporated. A Wilcoxon signed-rank test was conducted to validate the results of the experiment and the probability of the results being like this because of experimental errors rather than TNP was calculated to be less than 5%.

</details>

### [EMPHASIS: An Emotional Phoneme-based Acoustic Model for Speech Synthesis System](1806.09276.md)
**Hao Li, Yongguo Kang, Zhenyu Wang** · 2018-06-25

<details>
<summary>Abstract</summary>

We present EMPHASIS, an emotional phoneme-based acoustic model for speech synthesis system. EMPHASIS includes a phoneme duration prediction model and an acoustic parameter prediction model. It uses a CBHG-based regression network to model the dependencies between linguistic features and acoustic features. We modify the input and output layer structures of the network to improve the performance. For the linguistic features, we apply a feature grouping strategy to enhance emotional and prosodic features. The acoustic parameters are designed to be suitable for the regression task and waveform reconstruction. EMPHASIS can synthesize speech in real-time and generate expressive interrogative and exclamatory speech with high audio quality. EMPHASIS is designed to be a multi-lingual model and can synthesize Mandarin-English speech for now. In the experiment of emotional speech synthesis, it achieves better subjective results than other real-time speech synthesis systems.

</details>

### [A Variational Prosody Model for Mapping the Context-Sensitive Variation of Functional Prosodic Prototypes](1806.08685.md)
**Branislav Gerazov, Gérard Bailly, Omar Mohammed, Yi Xu et al.** · 2018-06-22

<details>
<summary>Abstract</summary>

The quest for comprehensive generative models of intonation that link linguistic and paralinguistic functions to prosodic forms has been a longstanding challenge of speech communication research. Traditional intonation models have given way to the overwhelming performance of deep learning (DL) techniques for training general purpose end-to-end mappings using millions of tunable parameters. The shift towards black box machine learning models has nonetheless posed the reverse problem -- a compelling need to discover knowledge, to explain, visualise and interpret. Our work bridges between a comprehensive generative model of intonation and state-of-the-art DL techniques. We build upon the modelling paradigm of the Superposition of Functional Contours (SFC) model and propose a Variational Prosody Model (VPM) that uses a network of variational contour generators to capture the context-sensitive variation of the constituent elementary prosodic contours. We show that the VPM can give insight into the intrinsic variability of these prosodic prototypes through learning a meaningful prosodic latent space representation structure. We also show that the VPM is able to capture prosodic phenomena that have multiple dimensions of context based variability. Since it is based on the principle of superposition, the VPM does not necessitate the use of specially crafted corpora for the analysis, opening up the possibilities of using big data for prosody analysis. In a speech synthesis scenario, the model can be used to generate a dynamic and natural prosody contour that is devoid of averaging effects.

</details>

### [Multi-task WaveNet: A Multi-task Generative Model for Statistical Parametric Speech Synthesis without Fundamental Frequency Conditions](1806.08619.md)
**Yu Gu, Yongguo Kang** · 2018-06-22

<details>
<summary>Abstract</summary>

This paper introduces an improved generative model for statistical parametric speech synthesis (SPSS) based on WaveNet under a multi-task learning framework. Different from the original WaveNet model, the proposed Multi-task WaveNet employs the frame-level acoustic feature prediction as the secondary task and the external fundamental frequency prediction model for the original WaveNet can be removed. Therefore the improved WaveNet can generate high-quality speech waveforms only conditioned on linguistic features. Multi-task WaveNet can produce more natural and expressive speech by addressing the pitch prediction error accumulation issue and possesses more succinct inference procedures than the original WaveNet. Experimental results prove that the SPSS method proposed in this paper can achieve better performance than the state-of-the-art approach utilizing the original WaveNet in both objective and subjective preference tests.

</details>

### [Stochastic WaveNet: A Generative Latent Variable Model for Sequential Data](1806.06116.md)
**Guokun Lai, Bohan Li, Guoqing Zheng, Yiming Yang** · 2018-06-15

<details>
<summary>Abstract</summary>

How to model distribution of sequential data, including but not limited to speech and human motions, is an important ongoing research problem. It has been demonstrated that model capacity can be significantly enhanced by introducing stochastic latent variables in the hidden states of recurrent neural networks. Simultaneously, WaveNet, equipped with dilated convolutions, achieves astonishing empirical performance in natural speech generation task. In this paper, we combine the ideas from both stochastic latent variables and dilated convolutions, and propose a new architecture to model sequential data, termed as Stochastic WaveNet, where stochastic latent variables are injected into the WaveNet structure. We argue that Stochastic WaveNet enjoys powerful distribution modeling capacity and the advantage of parallel training from dilated convolutions. In order to efficiently infer the posterior distribution of the latent variables, a novel inference network structure is designed based on the characteristics of WaveNet architecture. State-of-the-art performances on benchmark datasets are obtained by Stochastic WaveNet on natural speech modeling and high quality human handwriting samples can be generated as well.

</details>

### [StarGAN-VC: Non-parallel many-to-many voice conversion with star generative adversarial networks](1806.02169.md)
**Hirokazu Kameoka, Takuhiro Kaneko, Kou Tanaka, Nobukatsu Hojo** · 2018-06-06

<details>
<summary>Abstract</summary>

This paper proposes a method that allows non-parallel many-to-many voice conversion (VC) by using a variant of a generative adversarial network (GAN) called StarGAN. Our method, which we call StarGAN-VC, is noteworthy in that it (1) requires no parallel utterances, transcriptions, or time alignment procedures for speech generator training, (2) simultaneously learns many-to-many mappings across different attribute domains using a single generator network, (3) is able to generate converted speech signals quickly enough to allow real-time implementations and (4) requires only several minutes of training examples to generate reasonably realistic-sounding speech. Subjective evaluation experiments on a non-parallel many-to-many speaker identity conversion task revealed that the proposed method obtained higher sound quality and speaker similarity than a state-of-the-art method based on variational autoencoding GANs.

</details>

### [Voice Imitating Text-to-Speech Neural Networks](1806.00927.md)
**Younggun Lee, Taesu Kim, Soo-Young Lee** · 2018-06-04

<details>
<summary>Abstract</summary>

We propose a neural text-to-speech (TTS) model that can imitate a new speaker's voice using only a small amount of speech sample. We demonstrate voice imitation using only a 6-seconds long speech sample without any other information such as transcripts. Our model also enables voice imitation instantly without additional training of the model. We implemented the voice imitating TTS model by combining a speaker embedder network with a state-of-the-art TTS model, Tacotron. The speaker embedder network takes a new speaker's speech sample and returns a speaker embedding. The speaker embedding with a target sentence are fed to Tacotron, and speech is generated with the new speaker's voice. We show that the speaker embeddings extracted by the speaker embedder network can represent the latent structure in different voices. The generated speech samples from our model have comparable voice quality to the ones from existing multi-speaker TTS models.

</details>

### [A Regression Model of Recurrent Deep Neural Networks for Noise Robust Estimation of the Fundamental Frequency Contour of Speech](1805.02958.md)
**Akihiro Kato, Tomi Kinnunen** · 2018-05-08

<details>
<summary>Abstract</summary>

The fundamental frequency (F0) contour of speech is a key aspect to represent speech prosody that finds use in speech and spoken language analysis such as voice conversion and speech synthesis as well as speaker and language identification. This work proposes new methods to estimate the F0 contour of speech using deep neural networks (DNNs) and recurrent neural networks (RNNs). They are trained using supervised learning with the ground truth of F0 contours. The latest prior research addresses this problem first as a frame-by-frame-classification problem followed by sequence tracking using deep neural network hidden Markov model (DNN-HMM) hybrid architecture. This study, however, tackles the problem as a regression problem instead, in order to obtain F0 contours with higher frequency resolution from clean and noisy speech. Experiments using PTDB-TUG corpus contaminated with additive noise (NOISEX-92) show the proposed method improves gross pitch error (GPE) by more than 25 % at signal-to-noise ratios (SNRs) between -10 dB and +10 dB as compared with one of the most noise-robust F0 trackers, PEFAC. Furthermore, the performance on fine pitch error (FPE) is improved by approximately 20 % against a state-of-the-art DNN-HMM-based approach.

</details>

### [Emphatic Speech Synthesis and Control Based on Characteristic Transferring in End-to-End Speech Synthesis](s2:62c65f0bb9ff087d833b13bdd7e7a03b59fdd872.md)
**Mu Wang, Zhiyong Wu, Xixin Wu, H. Meng et al.** · 2018-05-01

### [Collapsed speech segment detection and suppression for WaveNet vocoder](1804.11055.md)
**Yi-Chiao Wu, Kazuhiro Kobayashi, Tomoki Hayashi, Patrick Lumban Tobing et al.** · 2018-04-30

<details>
<summary>Abstract</summary>

In this paper, we propose a technique to alleviate the quality degradation caused by collapsed speech segments sometimes generated by the WaveNet vocoder. The effectiveness of the WaveNet vocoder for generating natural speech from acoustic features has been proved in recent works. However, it sometimes generates very noisy speech with collapsed speech segments when only a limited amount of training data is available or significant acoustic mismatches exist between the training and testing data. Such a limitation on the corpus and limited ability of the model can easily occur in some speech generation applications, such as voice conversion and speech enhancement. To address this problem, we propose a technique to automatically detect collapsed speech segments. Moreover, to refine the detected segments, we also propose a waveform generation technique for WaveNet using a linear predictive coding constraint. Verification and subjective tests are conducted to investigate the effectiveness of the proposed techniques. The verification results indicate that the detection technique can detect most collapsed segments. The subjective evaluations of voice conversion demonstrate that the generation technique significantly improves the speech quality while maintaining the same speaker similarity.

</details>

### [Speaker-independent raw waveform model for glottal excitation](1804.09593.md)
**Lauri Juvela, Vassilis Tsiaras, Bajibabu Bollepalli, Manu Airaksinen et al.** · 2018-04-25

<details>
<summary>Abstract</summary>

Recent speech technology research has seen a growing interest in using WaveNets as statistical vocoders, i.e., generating speech waveforms from acoustic features. These models have been shown to improve the generated speech quality over classical vocoders in many tasks, such as text-to-speech synthesis and voice conversion. Furthermore, conditioning WaveNets with acoustic features allows sharing the waveform generator model across multiple speakers without additional speaker codes. However, multi-speaker WaveNet models require large amounts of training data and computation to cover the entire acoustic space. This paper proposes leveraging the source-filter model of speech production to more effectively train a speaker-independent waveform generator with limited resources. We present a multi-speaker 'GlotNet' vocoder, which utilizes a WaveNet to generate glottal excitation waveforms, which are then used to excite the corresponding vocal tract filter to produce speech. Listening tests show that the proposed model performs favourably to a direct WaveNet vocoder trained with the same model architecture and data.

</details>

### [The Voice Conversion Challenge 2018: Promoting Development of Parallel and Nonparallel Methods](1804.04262.md)
**Jaime Lorenzo-Trueba, Junichi Yamagishi, Tomoki Toda, Daisuke Saito et al.** · 2018-04-12

<details>
<summary>Abstract</summary>

We present the Voice Conversion Challenge 2018, designed as a follow up to the 2016 edition with the aim of providing a common framework for evaluating and comparing different state-of-the-art voice conversion (VC) systems. The objective of the challenge was to perform speaker conversion (i.e. transform the vocal identity) of a source speaker to a target speaker while maintaining linguistic information. As an update to the previous challenge, we considered both parallel and non-parallel data to form the Hub and Spoke tasks, respectively. A total of 23 teams from around the world submitted their systems, 11 of them additionally participated in the optional Spoke task. A large-scale crowdsourced perceptual evaluation was then carried out to rate the submitted converted speech in terms of naturalness and similarity to the target speaker identity. In this paper, we present a brief summary of the state-of-the-art techniques for VC, followed by a detailed explanation of the challenge tasks and the results that were obtained.

</details>

### [Multi-target Voice Conversion without Parallel Data by Adversarially Learning Disentangled Audio Representations](1804.02812.md)
**Ju-chieh Chou, Cheng-chieh Yeh, Hung-yi Lee, Lin-shan Lee** · 2018-04-09

<details>
<summary>Abstract</summary>

Recently, cycle-consistent adversarial network (Cycle-GAN) has been successfully applied to voice conversion to a different speaker without parallel data, although in those approaches an individual model is needed for each target speaker. In this paper, we propose an adversarial learning framework for voice conversion, with which a single model can be trained to convert the voice to many different speakers, all without parallel data, by separating the speaker characteristics from the linguistic content in speech signals. An autoencoder is first trained to extract speaker-independent latent representations and speaker embedding separately using another auxiliary speaker classifier to regularize the latent representation. The decoder then takes the speaker-independent latent representation and the target speaker embedding as the input to generate the voice of the target speaker with the linguistic content of the source utterance. The quality of decoder output is further improved by patching with the residual signal produced by another pair of generator and discriminator. A target speaker set size of 20 was tested in the preliminary experiments, and very good voice quality was obtained. Conventional voice conversion metrics are reported. We also show that the speaker information has been properly reduced from the latent representations.

</details>

### [A comparison of recent waveform generation and acoustic modeling methods for neural-network-based speech synthesis](1804.02549.md)
**Xin Wang, Jaime Lorenzo-Trueba, Shinji Takaki, Lauri Juvela et al.** · 2018-04-07

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis suggest that limitations such as the lossy nature of the amplitude spectrum with minimum phase approximation and the over-smoothing effect in acoustic modeling can be overcome by using advanced machine learning approaches. In this paper, we build a framework in which we can fairly compare new vocoding and acoustic modeling techniques with conventional approaches by means of a large scale crowdsourced evaluation. Results on acoustic models showed that generative adversarial networks and an autoregressive (AR) model performed better than a normal recurrent network and the AR model performed best. Evaluation on vocoders by using the same AR acoustic model demonstrated that a Wavenet vocoder outperformed classical source-filter-based vocoders. Particularly, generated speech waveforms from the combination of AR acoustic model and Wavenet vocoder achieved a similar score of speech quality to vocoded speech.

</details>

### [Expressive Speech Synthesis via Modeling Expressions with Variational Autoencoder](1804.02135.md)
**Kei Akuzawa, Yusuke Iwasawa, Yutaka Matsuo** · 2018-04-06

<details>
<summary>Abstract</summary>

Recent advances in neural autoregressive models have improve the performance of speech synthesis (SS). However, as they lack the ability to model global characteristics of speech (such as speaker individualities or speaking styles), particularly when these characteristics have not been labeled, making neural autoregressive SS systems more expressive is still an open issue. In this paper, we propose to combine VoiceLoop, an autoregressive SS model, with Variational Autoencoder (VAE). This approach, unlike traditional autoregressive SS systems, uses VAE to model the global characteristics explicitly, enabling the expressiveness of the synthesized speech to be controlled in an unsupervised manner. Experiments using the VCTK and Blizzard2012 datasets show the VAE helps VoiceLoop to generate higher quality speech and to control the expressions in its synthesized speech by incorporating global characteristics into the speech generating process.

</details>

### [Speech waveform synthesis from MFCC sequences with generative adversarial networks](1804.00920.md)
**Lauri Juvela, Bajibabu Bollepalli, Xin Wang, Hirokazu Kameoka et al.** · 2018-04-03

<details>
<summary>Abstract</summary>

This paper proposes a method for generating speech from filterbank mel frequency cepstral coefficients (MFCC), which are widely used in speech applications, such as ASR, but are generally considered unusable for speech synthesis. First, we predict fundamental frequency and voicing information from MFCCs with an autoregressive recurrent neural net. Second, the spectral envelope information contained in MFCCs is converted to all-pole filters, and a pitch-synchronous excitation model matched to these filters is trained. Finally, we introduce a generative adversarial network -based noise model to add a realistic high-frequency stochastic component to the modeled excitation signal. The results show that high quality speech reconstruction can be obtained, given only MFCC information at test time.

</details>

### [Neural Autoregressive Flows](1804.00779.md)
**Chin-Wei Huang, David Krueger, Alexandre Lacoste, Aaron Courville** · 2018-04-03

<details>
<summary>Abstract</summary>

Normalizing flows and autoregressive models have been successfully combined to produce state-of-the-art results in density estimation, via Masked Autoregressive Flows (MAF), and to accelerate state-of-the-art WaveNet-based speech synthesis to 20x faster than real-time, via Inverse Autoregressive Flows (IAF). We unify and generalize these approaches, replacing the (conditionally) affine univariate transformations of MAF/IAF with a more general class of invertible univariate transformations expressed as monotonic neural networks. We demonstrate that the proposed neural autoregressive flows (NAF) are universal approximators for continuous probability distributions, and their greater expressivity allows them to better capture multimodal target distributions. Experimentally, NAF yields state-of-the-art performance on a suite of density estimation tasks and outperforms IAF in variational autoencoders trained on binarized MNIST.

</details>

### [High-quality nonparallel voice conversion based on cycle-consistent adversarial network](1804.00425.md)
**Fuming Fang, Junichi Yamagishi, Isao Echizen, Jaime Lorenzo-Trueba** · 2018-04-02

<details>
<summary>Abstract</summary>

Although voice conversion (VC) algorithms have achieved remarkable success along with the development of machine learning, superior performance is still difficult to achieve when using nonparallel data. In this paper, we propose using a cycle-consistent adversarial network (CycleGAN) for nonparallel data-based VC training. A CycleGAN is a generative adversarial network (GAN) originally developed for unpaired image-to-image translation. A subjective evaluation of inter-gender conversion demonstrated that the proposed method significantly outperformed a method based on the Merlin open source neural network speech synthesis system (a parallel VC system adapted for our setup) and a GAN-based parallel VC system. This is the first research to show that the performance of a nonparallel VC method can exceed that of state-of-the-art parallel VC methods.

</details>

### [Towards End-to-End Prosody Transfer for Expressive Speech Synthesis with Tacotron](1803.09047.md)
**RJ Skerry-Ryan, Eric Battenberg, Ying Xiao, Yuxuan Wang et al.** · 2018-03-24

<details>
<summary>Abstract</summary>

We present an extension to the Tacotron speech synthesis architecture that learns a latent embedding space of prosody, derived from a reference acoustic representation containing the desired prosody. We show that conditioning Tacotron on this learned embedding space results in synthesized audio that matches the prosody of the reference signal with fine time detail even when the reference and synthesis speakers are different. Additionally, we show that a reference prosody embedding can be used to synthesize text that is different from that of the reference utterance. We define several quantitative and subjective metrics for evaluating prosody transfer, and report results with accompanying audio samples from single-speaker and 44-speaker Tacotron models on a prosody transfer task.

</details>

### [Style Tokens: Unsupervised Style Modeling, Control and Transfer in End-to-End Speech Synthesis](1803.09017.md)
**Yuxuan Wang, Daisy Stanton, Yu Zhang, RJ Skerry-Ryan et al.** · 2018-03-23

<details>
<summary>Abstract</summary>

In this work, we propose "global style tokens" (GSTs), a bank of embeddings that are jointly trained within Tacotron, a state-of-the-art end-to-end speech synthesis system. The embeddings are trained with no explicit labels, yet learn to model a large range of acoustic expressiveness. GSTs lead to a rich set of significant results. The soft interpretable "labels" they generate can be used to control synthesis in novel ways, such as varying speed and speaking style - independently of the text content. They can also be used for style transfer, replicating the speaking style of a single audio clip across an entire long-form text corpus. When trained on noisy, unlabeled found data, GSTs learn to factorize noise and speaker identity, providing a path towards highly scalable but robust speech synthesis.

</details>

### [Linear networks based speaker adaptation for speech synthesis](1803.02445.md)
**Zhiying Huang, Heng Lu, Ming Lei, Zhijie Yan** · 2018-03-05

<details>
<summary>Abstract</summary>

Speaker adaptation methods aim to create fair quality synthesis speech voice font for target speakers while only limited resources available. Recently, as deep neural networks based statistical parametric speech synthesis (SPSS) methods become dominant in SPSS TTS back-end modeling, speaker adaptation under the neural network based SPSS framework has also became an important task. In this paper, linear networks (LN) is inserted in multiple neural network layers and fine-tuned together with output layer for best speaker adaptation performance. When adaptation data is extremely small, the low-rank plus diagonal(LRPD) decomposition for LN is employed to make the adapted voice more stable. Speaker adaptation experiments are conducted under a range of adaptation utterances numbers. Moreover, speaker adaptation from 1) female to female, 2) male to female and 3) female to male are investigated. Objective measurement and subjective tests show that LN with LRPD decomposition performs most stable when adaptation data is extremely limited, and our best speaker adaptation (SA) model with only 200 adaptation utterances achieves comparable quality with speaker dependent (SD) model trained with 1000 utterances, in both naturalness and similarity to target speaker.

</details>

### [Can we steal your vocal identity from the Internet?: Initial investigation of cloning Obama's voice using GAN, WaveNet and low-quality found data](1803.00860.md)
**Jaime Lorenzo-Trueba, Fuming Fang, Xin Wang, Isao Echizen et al.** · 2018-03-02

<details>
<summary>Abstract</summary>

Thanks to the growing availability of spoofing databases and rapid advances in using them, systems for detecting voice spoofing attacks are becoming more and more capable, and error rates close to zero are being reached for the ASVspoof2015 database. However, speech synthesis and voice conversion paradigms that are not considered in the ASVspoof2015 database are appearing. Such examples include direct waveform modelling and generative adversarial networks. We also need to investigate the feasibility of training spoofing systems using only low-quality found data. For that purpose, we developed a generative adversarial network-based speech enhancement system that improves the quality of speech data found in publicly available sources. Using the enhanced data, we trained state-of-the-art text-to-speech and voice conversion models and evaluated them in terms of perceptual speech quality and speaker similarity. The results show that the enhancement models significantly improved the SNR of low-quality degraded data found in publicly available sources and that they significantly improved the perceptual cleanliness of the source speech without significantly degrading the naturalness of the voice. However, the results also show limitations when generating speech with the low-quality found data.

</details>

### [An end-to-end synthesis method for Korean text-to-speech systems](s2:1beb067671f249893c2299180f4c6fb3ea0653da.md)
**Yeunju Choi, Youngmoon Jung, Younggwan Kim, Youngjoo Suh et al.** · 2018-03-01

### [Efficient Neural Audio Synthesis](1802.08435.md)
**Nal Kalchbrenner, Erich Elsen, Karen Simonyan, Seb Noury et al.** · 2018-02-23

<details>
<summary>Abstract</summary>

Sequential models achieve state-of-the-art results in audio, visual and textual domains with respect to both estimating the data distribution and generating high-quality samples. Efficient sampling for this class of models has however remained an elusive problem. With a focus on text-to-speech synthesis, we describe a set of general techniques for reducing sampling time while maintaining high output quality. We first describe a single-layer recurrent neural network, the WaveRNN, with a dual softmax layer that matches the quality of the state-of-the-art WaveNet model. The compact form of the network makes it possible to generate 24kHz 16-bit audio 4x faster than real time on a GPU. Second, we apply a weight pruning technique to reduce the number of weights in the WaveRNN. We find that, for a constant number of parameters, large sparse networks perform better than small dense networks and this relationship holds for sparsity levels beyond 96%. The small number of weights in a Sparse WaveRNN makes it possible to sample high-fidelity audio on a mobile CPU in real time. Finally, we propose a new generation scheme based on subscaling that folds a long sequence into a batch of shorter sequences and allows one to generate multiple samples at once. The Subscale WaveRNN produces 16 samples per step without loss of quality and offers an orthogonal method for increasing sampling efficiency.

</details>

### [Fitting New Speakers Based on a Short Untranscribed Sample](1802.06984.md)
**Eliya Nachmani, Adam Polyak, Yaniv Taigman, Lior Wolf** · 2018-02-20

<details>
<summary>Abstract</summary>

Learning-based Text To Speech systems have the potential to generalize from one speaker to the next and thus require a relatively short sample of any new voice. However, this promise is currently largely unrealized. We present a method that is designed to capture a new speaker from a short untranscribed audio sample. This is done by employing an additional network that given an audio sample, places the speaker in the embedding space. This network is trained as part of the speech synthesis system using various consistency losses. Our results demonstrate a greatly improved performance on both the dataset speakers, and, more importantly, when fitting new voices, even from very short samples.

</details>

### [Neural Voice Cloning with a Few Samples](1802.06006.md)
**Sercan O. Arik, Jitong Chen, Kainan Peng, Wei Ping et al.** · 2018-02-14

<details>
<summary>Abstract</summary>

Voice cloning is a highly desired feature for personalized speech interfaces. Neural network based speech synthesis has been shown to generate high quality speech for a large number of speakers. In this paper, we introduce a neural voice cloning system that takes a few audio samples as input. We study two approaches: speaker adaptation and speaker encoding. Speaker adaptation is based on fine-tuning a multi-speaker generative model with a few cloning samples. Speaker encoding is based on training a separate model to directly infer a new speaker embedding from cloning audios and to be used with a multi-speaker generative model. In terms of naturalness of the speech and its similarity to original speaker, both approaches can achieve good performance, even with very few cloning audios. While speaker adaptation can achieve better naturalness and similarity, the cloning time or required memory for the speaker encoding approach is significantly less, making it favorable for low-resource deployment.

</details>

### [Epoch-Synchronous Overlap-Add (ESOLA) for Time- and Pitch-Scale Modification of Speech Signals](1801.06492.md)
**Sunil Rudresh, Aditya Vasisht, Karthika Vijayan, Chandra Sekhar Seelamantula** · 2018-01-19

<details>
<summary>Abstract</summary>

Time- and pitch-scale modifications of speech signals find important applications in speech synthesis, playback systems, voice conversion, learning/hearing aids, etc.. There is a requirement for computationally efficient and real-time implementable algorithms. In this paper, we propose a high quality and computationally efficient time- and pitch-scaling methodology based on the glottal closure instants (GCIs) or epochs in speech signals. The proposed algorithm, termed as epoch-synchronous overlap-add time/pitch-scaling (ESOLA-TS/PS), segments speech signals into overlapping short-time frames and then the adjacent frames are aligned with respect to the epochs and the frames are overlap-added to synthesize time-scale modified speech. Pitch scaling is achieved by resampling the time-scaled speech by a desired sampling factor. We also propose a concept of epoch embedding into speech signals, which facilitates the identification and time-stamping of samples corresponding to epochs and using them for time/pitch-scaling to multiple scaling factors whenever desired, thereby contributing to faster and efficient implementation. The results of perceptual evaluation tests reported in this paper indicate the superiority of ESOLA over state-of-the-art techniques. ESOLA significantly outperforms the conventional pitch synchronous overlap-add (PSOLA) techniques in terms of perceptual quality and intelligibility of the modified speech. Unlike the waveform similarity overlap-add (WSOLA) or synchronous overlap-add (SOLA) techniques, the ESOLA technique has the capability to do exact time-scaling of speech with high quality to any desired modification factor within a range of 0.5 to 2. Compared to synchronous overlap-add with fixed synthesis (SOLAFS), the ESOLA is computationally advantageous and at least three times faster.

</details>

### [An Implementation of Back-Propagation Learning on GF11, a Large SIMD Parallel Computer](1801.01554.md)
**Michael Witbrock, Marco Zagha** · 2018-01-04

<details>
<summary>Abstract</summary>

Current connectionist simulations require huge computational resources. We describe a neural network simulator for the IBM GF11, an experimental SIMD machine with 566 processors and a peak arithmetic performance of 11 Gigaflops. We present our parallel implementation of the backpropagation learning algorithm, techniques for increasing efficiency, performance measurements on the NetTalk text-to-speech benchmark, and a performance model for the simulator. Our simulator currently runs the back-propagation learning algorithm at 900 million connections per second, where each "connection per second" includes both a forward and backward pass. This figure was obtained on the machine when only 356 processors were working; with all 566 processors operational, our simulation will run at over one billion connections per second. We conclude that the GF11 is well-suited to neural network simulation, and we analyze our use of the machine to determine which features are the most important for high performance.

</details>

### [한국어 텍스트 음성 변환 시스템을 위한 엔드투엔드 합성 방식 연구 = (An) end-to-end synthesis method for Korean text-to-speech system](s2:2dc975e0f1dce800da9cb150063c3872fafe86dd.md)
**최연주** · 2018-01-01

