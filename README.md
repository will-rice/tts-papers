# tts-papers

A curated, automatically-updated collection of papers on **text-to-speech synthesis**, neural vocoders, voice conversion, voice cloning, prosody, and related topics — starting from the Tacotron/WaveNet era (2017) and growing every day.

Beyond a reading list, this repo is built to be **browsed by LLMs**. Every paper is mirrored as a markdown file with structured YAML frontmatter and inline citation links that resolve to sibling files in the corpus when the cited work is here, or to arXiv / DOI otherwise. Point an agent at [`papers/README.md`](papers/README.md) and it can crawl the literature graph the same way you would.

## How it works

- Papers are sourced from [arXiv](https://arxiv.org/) and [Hugging Face Papers](https://huggingface.co/papers) via their public APIs.
- Query this corpus over MCP: `https://wrice-papers-mcp.hf.space/tts/mcp` ([server code](https://huggingface.co/spaces/wrice/papers-mcp)).
- A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs **daily at 06:00 UTC** to pull papers submitted in the previous 8 days.
- Results are filtered with a negative-keyword blacklist plus an ML signal check and a positive TTS/speech-generation relevance gate.
- The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Markdown corpus

Each paper is also available as LLM-friendly markdown under `papers/<year>/<arxiv_id>.md`. The conversion pipeline:

- Converts arXiv's HTML rendering (`arxiv.org/html/<id>`, falling back to [ar5iv](https://ar5iv.labs.arxiv.org) for pre-2024 papers) — the article is extracted from the page, figures become absolute-URL images, and equations become GitHub-native ` ```math ` blocks.
- Papers without a usable HTML rendering fall back to LaTeX source (`arxiv.org/e-print/<id>`) via [pandoc](https://pandoc.org), then PDF via [marker](https://github.com/datalab-to/marker).
- Auto-flagged or manually-listed (`papers/.fixme.txt`) low-quality outputs go through a Claude Sonnet remediation pass.
- Citations are rewritten as clickable links — local sibling MD when the cited paper is in this corpus, external arXiv/DOI URLs otherwise.

Browse the corpus at [papers/README.md](papers/README.md). Each paper file has YAML frontmatter with metadata + diagnostics (`source`, `converter`, `llm_remediated`, `citations_resolved`).

## Running locally

You'll need pandoc and Node (for Prettier, which normalizes the generated markdown):

```bash
# macOS
brew install pandoc node

# Ubuntu
sudo apt-get install pandoc nodejs npm
```

Then run `npm ci` to install the pinned Prettier used by the pipeline, CI, and pre-commit.

```bash
# Incremental fetch (last 8 days)
uv run python scripts/fetch_papers.py

# Full historical fetch (everything since 2017-01-01)
uv run python scripts/fetch_papers.py --full
uv run python scripts/convert_papers.py --regenerate-all

# Custom window
uv run python scripts/fetch_papers.py --days 30
```

The fetch script uses only the Python standard library (plus a Prettier pass on the README); the conversion pipeline adds `marker-pdf`, `anthropic`, `pyyaml`, and the `pandoc` system binary (managed via `uv` and your package manager). Both scripts format the markdown they generate with the repo-pinned [Prettier](https://prettier.io/) (`npm ci`), and a [Format workflow](.github/workflows/format.yml) enforces it on every PR.

## Triggering a manual update

Open the **Actions** tab → **Fetch TTS Papers** → **Run workflow**.
Select _full = true_ to back-fill from 2017 and rebuild all paper markdown, or leave it as _false_ for an incremental update.

## Search terms

The following keyword queries are used against arXiv title and abstract fields and Hugging Face Papers search:

`text to speech` · `text-to-speech` · `speech synthesis` · `neural text to speech` · `neural vocoder` · `voice conversion` · `voice cloning` · `speech generation` · `acoustic model speech` · `prosody prediction` · `expressive speech synthesis` · `zero-shot TTS` · `end-to-end speech synthesis` · `diffusion speech synthesis`

## Papers

<!-- PAPERS_TABLE_START -->

_Showing the last 30 days (61 of 3418 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [LACE: Layer-Wise Compression for Dynamic Frame Rate Codecs](https://arxiv.org/abs/2609.17509) · [📄 Read](papers/2026/2609.17509.md)

**Thanapat Trachu, Samuele Cornell, William Chen, Shinji Watanabe** · 2026-09-15

<details>
<summary>Abstract</summary>

Neural audio codecs are a key component in speech language modeling. However, their high frame rates lead to long sequence lengths, increasing computational costs. Dynamic frame rate codecs mitigate this by reducing the effective frame rate using a compression step to merge multiple frames together. However, most prior methods either operate on single-codebook codecs or apply a single compression step before multi-layer quantization. This forces all quantization layers to share the same segmentation boundaries, despite the residual embeddings at different quantization layers exhibiting different rates of change over time. We propose LACE (Layer-Adaptive Codec Encoding), a dynamic frame rate codec that applies an independent compression step at each quantization layer, enabling layer-specific segmentation boundaries. To use LACE tokens in downstream text-to-speech (TTS), we further introduce union alignment and boundary anchor mechanisms to make durations consistent across layers while preserving compression benefits. Experiments on LibriTTS show that LACE offers a better rate-quality tradeoff than prior dynamic frame rate methods on the reconstruction task and improves TTS inference efficiency while maintaining competitive synthesis quality. Our code is released as part of the ESPnet3 codec recipe.

</details>

#### [Self-Distilled Pronunciation and Accent Control for Neural Text-to-Speech](https://arxiv.org/abs/2609.17234) · [📄 Read](papers/2026/2609.17234.md)

**Shuhei Kato** · 2026-09-15

<details>
<summary>Abstract</summary>

Text-to-speech that reads raw text has no lexicon: a rare word is read as guessed. Remedies train a reading-and-accent channel on recorded speech or edit words one at a time from exemplars. We do neither. The frozen backbone reads a sentence containing a common word it already says correctly, and its own output then serves as the teacher for the same sentence, with that word replaced by a tagged, accented reading; this training pair is the whole idea. On Sarashina2.2-TTS, screened raters at Fleiss' kappa = 0.85 hear the prescribed accent on 0.89 of unseen words against 0.57 for kana, which cannot express one; kana wins no pair; naturalness is not measurably hurt. Moved untuned to autoregressive, diffusion, and encoder-decoder backbones, it transfers reading, 0.25 to 0.47 above no edit on 319 words, and on CosyVoice 2 accent on two words in three, but not on Irodori; the paper locates why.

</details>

#### [Taming Long-form Text-to-Speech](https://arxiv.org/abs/2609.16989) · [📄 Read](papers/2026/2609.16989.md)

**Rongxiang Wang, Berkin Durmus, Aysegul Orhon, Eduardo Pacheco et al.** · 2026-09-15

<details>
<summary>Abstract</summary>

Long-form text-to-speech (TTS) enables multi-turn conversations with consistent prosody and higher quality voice cloning from longer reference audio. Recent open-weights autoregressive TTS models such as Qwen3-TTS and VoxCPM2 attain state-of-the-art word error rate (WER) and speaker similarity (SIM) on short-form prompts but significantly deteriorate when used with long-form prompts. We propose Localized Attention-Constrained Inference (LACI), an inference-only method to detect TTS errors in near real-time, roll back to the error onset and regenerate with temporary guardrails, adding negligible computational overhead. Using LACI, we improve worst-of-N WER across 10 RNG seeds for Qwen3-TTS-0.6B from 35.2% to 3.4% on prompts longer than 1500 words, even surpassing its short-form reliability of 5.4\% on prompts with fewer than 500 words. To demonstrate the efficacy of LACI on voice cloning reliability, we propose a sliding-window version of the SIM metric that we call wSIM. wSIM exposes several novel failure patterns that are not captured by SIM. LACI improves worst-of-N wSIM from 0.01 to 0.47 on 120 seconds of reference audio while reducing the rate of catastrophic generations with WER above 30% from 26% to below 1%

</details>

#### [The Evolving Bottleneck in Speech Generation: Interface Co-design and Staged Alignment from CosyVoice to Qwen-Audio-3.0-TTS](https://arxiv.org/abs/2609.16514) · [📄 Read](papers/2026/2609.16514.md)

**Qian Chen, Xiangang Li, Xiang Lv, Han Zhao et al.** · 2026-09-15

<details>
<summary>Abstract</summary>

Speech synthesis systems are commonly narrated as a sequence of larger models, better tokenizers, and broader data. This technical retrospective offers a different account of the CosyVoice lineage, from CosyVoice through CosyVoice 2 and CosyVoice 3 to Qwen-Audio-3.0-TTS: progress came from repeatedly relocating the system's dominant bottleneck. Across the lineage, a stable decomposition separates an autoregressive language model that plans speech from a flow-matching model that renders acoustics. What changes is the contract between them. CosyVoice establishes supervised semantic tokens as a content-aligned interface; CosyVoice 2 makes that interface causally available for streaming and removes the utterance-level speaker embedding from the language model; CosyVoice 3 improves the learnability and coverage of the interface through multitask supervision, scaling, and differentiable reward optimization; and Qwen-Audio-3.0-TTS reduces token rate, conditions its renderer on continuous language-model hidden states instead of token embeddings, and progressively aligns the coupled system. We formalize this history through four interface dimensions---representation, ownership, availability, and gradient reach---and separate within-paper evidence from cross-paper comparison. The resulting synthesis connects discrete autoregressive, continuous non-autoregressive, hybrid, and continuous autoregressive speech-generation paradigms, and yields practical principles for diagnosing and training modular speech generators.

</details>

#### [Language Orthogonalization for Zero-Shot Cross-Lingual Audio Deepfake Detection](https://arxiv.org/abs/2609.16458) · [📄 Read](papers/2026/2609.16458.md)

**Minu Kim, Ji Sub Um, Hoirin Kim** · 2026-09-15

<details>
<summary>Abstract</summary>

Audio deepfake detectors need to transfer to languages absent from training, as multilingual speech synthesis outpaces labeled anti-spoofing resources. While detectors increasingly rely on self-supervised speech models (S3Ms), these backbones encode language-dependent structure that confounds spoof cues. We address this confound through language orthogonalization, a target-free ridge map that removes S3M variation projected onto continuous language-identification (LID) embeddings. Across six languages, six S3M backbones, and all Leave-N-Out settings, it consistently reduces EER across unseen languages. Cross-lingual EER correlates with LID-space distance, where orthogonalization yields larger gains for more distant transfers.

</details>

#### [Reducing the Output-Mode Gap in Speech Language Models via Joint-Output On-Policy Distillation](https://arxiv.org/abs/2609.15313) · [📄 Read](papers/2026/2609.15313.md)

**Daxin Tan, Dehua Tao, Chengxi Deng, Hanlin Zhang et al.** · 2026-09-14

<details>
<summary>Abstract</summary>

Autoregressive generation of interleaved text and acoustic tokens is a common approach to spoken-response generation in speech large language models. Although this design enables streaming generation with explicit textual guidance, generated acoustic tokens become part of the context for subsequent text predictions. Given identical speech inputs, we observe markedly lower answer accuracy for the internal text generated in speech-to-text-and-speech (S2TS) mode than for speech-to-text (S2T) responses. We term this discrepancy the \emph{output-mode gap} (OMG). To reduce OMG, we propose \emph{Joint-Output On-Policy Distillation} (JO-OPD), which distills the model's stronger S2T policy into joint generation using student-generated S2TS trajectories. At each text position, the S2T teacher provides soft targets from a text-only projection of the student's preceding outputs, while the student predicts from the corresponding full interleaved history. A preservation objective further regularizes native non-text predictions. Experiments on Step-Audio-2-mini and Baichuan-Audio-Instruct reveal OMG across two interleaved generation architectures. On Step-Audio-2-mini, JO-OPD reduces OMG from 42.87 to 16.26 percentage points on Spoken-MQA and from 29.72 to 13.04 points on speech-rendered GSM8K, with little change in S2T accuracy and substantially larger reductions than matched SFT baselines. ASR-based evaluation further shows a 7.49-point improvement in spoken-answer accuracy on Spoken-MQA.

</details>

#### [Cross-Lingual F5-TTS 2: A Simplified Framework for Language-Agnostic Voice Cloning](https://arxiv.org/abs/2609.15184) · [📄 Read](papers/2026/2609.15184.md)

**Qingyu Liu, Rixi Xu, Yushen Chen, Zhikang Niu et al.** · 2026-09-14

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) can clone a speaker's voice from a short audio prompt, yet most TTS systems still require the audio prompt transcript during inference. This dependency prevents cross-lingual voice cloning when the audio prompt transcript is unavailable, particularly for unseen languages. Cross-Lingual F5-TTS removes this dependency and enables transcript-free cross-lingual voice cloning, but it prepares its training data with forced alignment. Forced alignment is sensitive to boundary errors, and its cost grows as more languages are covered. Its speaking rate predictor is also unreliable at estimating duration when the audio prompt begins or ends with silence. In this paper, we present Cross-Lingual F5-TTS 2, a simplified framework for transcript-free cross-lingual voice cloning without forced alignment. Instead of using forced alignment to segment real utterances, we build same-speaker prompt and target pairs using a pretrained F5-TTS model and fine-tune the same model on these constructed pairs. This simplifies data preparation and preserves the acoustic modeling capability of the pretrained model, enabling adaptation with only a short fine-tuning stage. We further make the syllable-level speaking rate predictor robust to leading and trailing silence through silence-aware augmentation. Experiments show that Cross-Lingual F5-TTS 2 reaches higher speaker similarity than F5-TTS and Cross-Lingual F5-TTS while maintaining intelligibility. All related resources are publicly available.

</details>

#### [Tone on a Budget: A Reference-Free Metric for Lexical Tone in Massively Multilingual Text-to-Speech](https://arxiv.org/abs/2609.14817) · [📄 Read](papers/2026/2609.14817.md)

**Moses Daudu, Adeola Enitan Bamidele, Honor-Jesus Bezaleel** · 2026-09-13

<details>
<summary>Abstract</summary>

In Yorùbá, pitch alone separates \d{o}k\d{o} (husband, Mid), \d{o}k\d{ò} (vehicle, Low), and \d{o}k\d{ó} (hoe, High) -- the diacritics ARE the tone marks. Yet character error rate (CER), the standard automated metric for text-to-speech (TTS), is in practice computed from ASR output that drops those marks: a synthesizer can ace CER and still say vehicle for husband. We introduce DunDun -- named for the dùndún, the Yorùbá talking drum that speaks through pitch alone -- an automated, reference-free lexical-tone metric that needs no tone-labelled corpus. The gold High/Mid/Low sequence is read from the input text's diacritics (in TTS that text exists by construction, so no reference recording is needed); the prediction comes from the audio's pitch track. We validate three ways. Flattening pitch with PSOLA resynthesis collapses DunDun while CER does not move. Inverting High and Low in the answer key of 300 native recordings drives the two-class readout to 0.14, symmetrically below its 0.35 chance level -- a consistency check on the scoring path, not independent evidence. And three native listeners, over 67 blind A/B trials, pick the tone-correct clip 89.6% of the time (95% CI 80.0-94.8; p < 1e-4); whether DunDun tracks those judgements trial by trial is not resolved at this sample size. Applied to a massively multilingual zero-shot TTS model, DunDun shows what CER cannot: Yorùbá tone sits near the native anchor before any Yorùbá fine-tuning (0.567 +/- 0.02 over five decode seeds vs. 0.596; chance 0.33), despite the 21.4% CER the model's own paper reports; and a few hours of clean audio halve CER (5.6% to 2.7% by 5h, 1.7% by 15h) while tone saturates within the hour. On non-tonal Swahili, CER already captures the gains: the metric a language needs is language-dependent. We release the metric and the complete validation protocol.

</details>

#### [Quantifying the Generation Modality Gap in Speech-Text Language Models](https://arxiv.org/abs/2609.14743) · [📄 Read](papers/2026/2609.14743.md)

**Ju-Chieh Chou, Jiawei Zhou, Karen Livescu** · 2026-09-13

<details>
<summary>Abstract</summary>

Pure speech language models often lag behind text and speech-text language models in generating coherent content, but this gap is difficult to quantify because speech and text systems are typically evaluated with different metrics and trained on different data. We study the speech-text modality gap in a family of spoken language models, based on flow matching for continuous acoustic feature generation. We construct a unified generation-based evaluation suite that compares speech-only, text-only, and speech-text language models trained on matched data distributions and evaluated in matched generation settings. We evaluate generated continuations along multiple dimensions: semantic coherence, measured by transcribing generated speech and scoring it with a reference language model; local phonetic structure, measured by phone n-gram distributional statistics; speaker consistency and acoustic quality; and emotion-based distributional metrics. Across datasets, we find that joint speech-text modeling substantially improves semantic coherence. However, the improvement is not uniform across metrics: phone-level metrics change only modestly, speaker similarity and predicted quality are lower for speech-text continuations, while emotion-based distributional metrics improve. Compared with larger-scale speech-only models, our speech-text model closes much of the scaling gap in transcript-based semantic coherence, suggesting that text provides an efficient semantic training signal for spoken language modeling.

</details>

#### [Dynamic Learning Solutions: A System for Personalized Educational Video Generation](https://arxiv.org/abs/2609.14408) · [📄 Read](papers/2026/2609.14408.md)

**Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy, Deepak Parmar et al.** · 2026-09-13

<details>
<summary>Abstract</summary>

We present an automated pipeline that converts NCERT textbooks into interactive video explanations that respond directly to user queries. A user uploads a PDF and asks a question; the system then generates a video-based explanation as output, handling both text and visual elements from the PDF for multi-modal retrieval and response generation. The pipeline combines a Retrieval-Augmented Generation (RAG) model with generative multimedia components. The RAG stage is optimized for the structure of NCERT textbooks and performs best on content from those books. Given a user query, the RAG model retrieves relevant content from the PDF and generates a multi-scene script containing narrative explanations and structured visual prompts aligned with the textbook's explanatory style. These prompts are passed to a Stable Diffusion module, implemented layer by layer for interpretability and control, which generates contextually relevant images. The images are then processed by DynamiCrafter to produce animated sequences. Finally, a Google Text-to-Speech module generates synchronized narration, aligning speech with the visual scenes through time-based control. The result is a coherent video explanation integrating animation, narration, and textbook-aligned visuals, transforming static educational material into an engaging learning experience. By combining multi-modal document retrieval, generative visual models, animation frameworks, and speech synthesis, this pipeline demonstrates a scalable approach to delivering interactive, personalized digital education content.

</details>

#### [Modeling, Scaling, and Decoding: Optimizing Controllable Speech Generation with Nonverbal Vocalizations](https://arxiv.org/abs/2609.14231) · [📄 Read](papers/2026/2609.14231.md)

**Ziyu Zhang, Yun Chen, Taihui Wang, Hanzhao Li et al.** · 2026-09-13

<details>
<summary>Abstract</summary>

Controllable synthesis of nonverbal vocalizations (NVVs) is es- sential for natural and expressive speech, but remains challeng- ing due to their acoustic diversity and imbalanced distribution in existing corpora. To address these challenges, we develop an NVV-aware DiTAR system that models continuous speech latents, encodes the 16 target NVV categories as dedicated to- kens, and adapts stop prediction to distinguish mid-utterance vocalizations from utterance boundaries. Training begins with large-scale bilingual pre-training on diverse NVV speech, fol- lowed by continued supervised fine-tuning on a corpus en- hanced through targeted synthetic augmentation and frequency- aware rebalancing. At inference time, we select the acoustic prompt, tune the LM-guidance and noise-injection scales, and apply Best-of-N sampling with multi-metric selection to re- duce generation failures. The final system achieves an official weighted bilingual score of 62.786, ranking first in Mandarin, second in English, and first overall among participating systems in Track 2 of the ISCSLP 2026 NVVSpeech Challenge. Ab- lation studies show that targeted augmentation benefits under- represented NVV categories the most, while robust candidate selection requires balancing NVV correctness, lexical fidelity, and perceptual quality.

</details>

#### [Bangla Sentence Function Classification: Corpus Development, Model Benchmarking, and Interpretability](https://arxiv.org/abs/2609.13869) · [📄 Read](papers/2026/2609.13869.md)

**Swapnil Kundu Argha, Abdullah Al Shafi, Rowzatul Zannat, Shoumik Barman Polok et al.** · 2026-09-12

<details>
<summary>Abstract</summary>

Automatic sentence function identification is important for many downstream natural language processing (NLP) applications such as dialogue systems, text-to-speech synthesis, and machine translation. However, benchmark resources for Bangla sentence function classification remain limited. To mitigate this gap, this paper introduces a corpus of 10,000 Bangla sentences, manually annotated into four functional categories, namely declarative, interrogative, imperative, and exclamatory. The corpus is nearly balanced across the four classes, with high annotation reliability reflected by a Fleiss\' Kappa of 0.82. Furthermore, we evaluate multiple feature representations, including Bag-of-Words (BoW), TF-IDF, and Word2Vec, with several classical machine learning classifiers. In addition, two heterogeneous ensemble models, namely Single-Level Ensemble (SLE) and Double-Level Ensemble (DLE), are utilized to improve classification performance. Experimental results show that TF-IDF consistently outperforms Word2Vec, likely due to its ability to emphasize discriminative lexical cues associated with sentence functions, particularly given the relatively small corpus used to train Word2Vec. The DLE model with TF-IDF features achieves the best performance with accuracy and macro-F1 of 0.95, demonstrating the effectiveness of sparse lexical representations and heterogeneous ensemble learning for this task. Further cross-validation confirms the robustness of the approach, while LIME-based interpretability provides insights into model predictions. The developed corpus and model benchmarking establish strong baselines for Bangla sentence function classification.

</details>

#### [The VoiceMOS Challenge 2026: Evaluating Speech Enhancement, Emotional TTS and Accented TTS Systems](https://arxiv.org/abs/2609.13792) · [📄 Read](papers/2026/2609.13792.md)

**Wen-Chin Huang, Wei Wang, Marvin Sach, Xiaoxue Gao et al.** · 2026-09-12

<details>
<summary>Abstract</summary>

We present the results of the VoiceMOS Challenge 2026, the fifth edition of a scientific challenge on automatic prediction of subjective speech assessments. After expanding the scope to music and general audio in 2025, we refocused the evaluation target on speech and organized three tracks: prediction of absolute and comparative category ratings for enhanced speech, prediction of naturalness and emotion-related tasks for emotional text-to-speech systems, and prediction of speaker and accent similarity for codec-based speech synthesis systems. The challenge attracted a total of 18 teams worldwide, with most teams successfully surpassing the provided baselines. We summarize the challenge results, representative top-performing systems, participant feedback, and directions for future editions.

</details>

#### [DiTAR+: Dual Optimization for Robust Autoregressive Diffusion Speech Synthesis](https://arxiv.org/abs/2609.13909) · [📄 Read](papers/2026/2609.13909.md)

**Ziyu Zhang, Tianlun Zuo, Hanzhao Li, Haoyu Zhang et al.** · 2026-09-12

<details>
<summary>Abstract</summary>

Continuous-latent Autoregressive Diffusion Transformer (AR-DiT) models have demonstrated immense potential in zero-shot speech generation. However, they still suffer from limited decoding stability when synthesizing long utterances or complex linguistic structures. This instability primarily stems from a restricted historical receptive field and an acoustic inertia dependency within the diffusion decoder, which causes the model to ignore semantic conditions. To address these challenges, we propose DiTAR+, a dual-optimization framework. First, we introduce Dilated Context Sampling to expand the macro-level historical receptive field without violating physical temporal continuity, thereby preventing cumulative error propagation. Second, we propose Hierarchical Acoustic Masking to prevent shallow layers from attending to acoustic pre-context, explicitly decoupling semantic alignment from acoustic detail reconstruction. Extensive experiments show that our framework effectively mitigates pronunciation errors and semantic hallucinations, enhances generation robustness on challenging sentences, and maintains exceptionally high speaker similarity throughout the entirety of long-form utterances. On the linguistically challenging ZH-Hard set, DiTAR+ reduces the word error rate from 12.478% to 9.893%, and on extended utterances of 25 to 35 seconds it improves speaker similarity from 0.741 to 0.759 while simultaneously lowering the word error rate from 2.778% to 2.173%, outperforming both discrete-token and pure flow-matching baselines.

</details>

#### [CRAF: Cross-View Residual-Aware Fusion for Deepfake Speech Detection](https://arxiv.org/abs/2609.13842) · [📄 Read](papers/2026/2609.13842.md)

**Minh-Xuan Phan, Khalid Zaman, Candy Olivia Mawalim, Masashi Unoki** · 2026-09-12

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis and voice conversion have made deepfake speech increasingly realistic, making generalization to unseen spoofing attacks a critical challenge. Pretrained speech and audio models offer a promising direction for improving robustness to such unseen attacks. Self-supervised learning (SSL) models capture fine-grained, low-level acoustic characteristics, whereas Auditory Large Language Models (ALLMs) provide higher-level contextual representations. These complementary views can provide useful cues for improving generalization to unseen attacks. However, direct fusion does not explicitly disentangle information shared across the two views from view-specific complementary information, limiting effective cross-view integration. To address this, we propose CRAF, a cross-view residual-aware fusion framework that uses ALLM-guided cross-view attention to enrich SSL representations and adopts ALLM as a high-level reference to separate ALLM-explainable information from complementary SSL residual information. The residual is selectively refined through adaptive gating and integrated through SSL-primary fusion. Experiments on ASVspoof 5 show that CRAF with Kimi-Audio achieves an EER of 5.96% and a minDCF of 0.1192, demonstrating robustness to unseen spoofing attacks.

</details>

#### [Realtime-Venus: A full-duplex interaction system with asynchronous delegation](https://arxiv.org/abs/2609.13814) · [📄 Read](papers/2026/2609.13814.md)

**Ruixiang Zhao, Hualei Wang, Renhe Sun, Enzhi Zhou et al.** · 2026-09-12

<details>
<summary>Abstract</summary>

Natural interaction in digital and physical environments requires continuous perception and timely responses. Spoken dialogue relies on acoustic and linguistic cues, while video interaction also requires grounding the conversation in evolving visual context. We present Realtime-Venus, a proactive full-duplex interaction system with two separately trained 9B models: Realtime-Venus-Omni for audio-visual interaction and Realtime-Venus-Audio for spoken interaction. Each model serves as a complete conversational frontend, integrating continuous perception, conversational control, and native speech generation through a shared causal timeline for user inputs, model outputs, and delegation events. A dual-loop runtime coordinates live interaction with background reasoning and tool execution. Foreground interaction continues while Realtime-Venus-Harness executes tasks asynchronously and returns results for integration into the ongoing dialogue. Both models follow a common post-training recipe combining offline understanding, proactive full-duplex trajectories, and delegation workflows. Among the evaluated online models, Realtime-Venus-Omni achieves the highest scores on six of eight video benchmarks, including StreamingBench (70.2%), OVO-Bench (64.7%), and Daily-Omni (81.3%). Across eight audio understanding and spoken question answering benchmarks, Realtime-Venus-Audio leads the compared models on MMAU (78.0%), MMAU-Pro (63.2%), Llama Questions (83.8%), and Speech CMMLU (67.8%), while matching the best VoiceBench AlpacaEval score of 4.81. On Full-Duplex-Bench v1.5, Realtime-Venus-Audio responds to 75% of user interruptions and achieves continuation rates of 97%, 88%, and 86% under backchannels, other-directed speech, and background speech, respectively, exceeding Gemini 3.1 Live and GPT-4o on all three continuation metrics.

</details>

#### [StepAudio 3 Gen Technical Report](https://arxiv.org/abs/2609.12945) · [📄 Read](papers/2026/2609.12945.md)

**Bin Lin, Bo Zhao, Boyang Wang, Boyang Zhang et al.** · 2026-09-11

<details>
<summary>Abstract</summary>

We introduce StepAudio 3 Gen, a general-purpose audio generation model that supports zero-shot text-to-speech (TTS), voice design, vocal generation, sound effects, music, vibe speech, and mixtures of multiple audio types within a unified framework. At its core, StepAudio 3 Gen is a discrete autoregressive generator that models audio directly over residual vector quantization (RVQ) tokens, departing from the diffusion Transformer-based continuous generation paradigm prevalent in recent general audio models. Its StepAudio Tokenizer represents general audio at 12.5 Hz in a shared $16 \times 2048$ residual code space, jointly quantizing semantic and waveform-level acoustic features so that each code layer preserves both types of information. For generation, the backbone predicts the first codebook along the time axis using autoregressive modeling, while a lightweight causal Transformer completes the remaining fifteen codebooks along the codebook axis. Our study further identifies three key design principles: (1) interference-aware progressive pretraining for acquiring audio capabilities while preserving the textual abilities of the large language model, (2) RVQ Adaptor for effectively incorporating multi-codebook acoustic representations, and (3) discrete autoregressive modeling over a shared representation across general audio domains. With progressive pretraining, multi-task instruction training, and supervised fine-tuning, StepAudio 3 Gen achieves state-of-the-art performance on both TTS and voice design, while retaining strong generation capabilities across speech, vocals, sound effects, and music. Audio samples are available at https://stepaudiollm.github.io/step-audio-3-gen/.

</details>

#### [PhaseGAN: High-Fidelity Vocoder via Decoupled Amplitude and GAN-Driven Phase Reconstruction](https://arxiv.org/abs/2609.12918) · [📄 Read](papers/2026/2609.12918.md)

**Wenzheng Zhang, Xueliang Zhang, Shulin He, Fei Zhao et al.** · 2026-09-11

<details>
<summary>Abstract</summary>

A vocoder is a pivotal component of modern text-to-speech (TTS) systems. Despite the significant progress of neural network-based vocoders, accurate phase reconstruction remains the main challenge limiting both audio quality and modeling efficiency. We introduce PhaseGAN, a lightweight vocoder that addresses this limitation through a "mel $\rightarrow$ Amplitude $\rightarrow$ Phase" reconstruction pipeline. By reconstructing amplitude and phase spectra via distinct methodologies, the proposed PhaseGAN outperforms state-of-the-art baselines while utilizing fewer model parameters and reduced computational requirements. The compact version generates high-fidelity audio with approximately 500K parameters and 1 GMAC computational load, making it highly suitable for real-time applications on edge devices. In addition, our approach exhibits exceptional musical audio synthesis capabilities despite no training on musical data, illustrating unprecedented cross-domain generalization. See https://github.com/phasegan/phasegan-audio-demo for demos of our work.

</details>

#### [AlignDPO: Preference-Gated Alignment for Reducing Hallucination in Decoder-Only TTS](https://arxiv.org/abs/2609.12855) · [📄 Read](papers/2026/2609.12855.md)

**Xiao Zhou, Oisín Turbitt, Kit Bower-Morris, Jonathan Carlton et al.** · 2026-09-11

<details>
<summary>Abstract</summary>

Decoder-only text-to-speech (TTS) models scale efficiently but remain prone to content hallucinations that arise from weak text-speech alignment during autoregressive generation. We find that robustness is governed by a non-monotone relation to the sharpness of the alignment-bearing attention heads: a moderate degree is best, whereas over-sharpening is no better than the unaligned backbone and even less robust. Guided by this, we present AlignDPO, a post-training method that reaches this moderate regime by folding a lightweight connectionist-temporal-classification (CTC) alignment term into Direct Preference Optimization (DPO), applied only to the chosen samples, with no architectural or inference-time change. On the Seed-TTS-Eval English set, this significantly reduces the content-hallucination and word error rates relative to a strong DPO baseline and lowers the severe content-hallucination rate to ~0.6% (from 4.4%); a listening study further finds it preferred for naturalness over both the backbone and that baseline. Alignment is thus best learned and kept moderate rather than maximized or imposed at decoding. Audio samples are available at https://align-dpo-demo.vercel.app.

</details>

#### [X-Pred MeanFlow for Streaming Token-to-Mel Speech Decoding](https://arxiv.org/abs/2609.12728) · [📄 Read](papers/2026/2609.12728.md)

**Hanke Xie, Xiaming Ren, Qirui Zhan, Jingbin Hu et al.** · 2026-09-11

<details>
<summary>Abstract</summary>

Recent advancements in discrete token-based speech generation have highlighted the importance of efficient token-to-waveform synthesis in streaming and dialogue scenarios. Flow-matching acoustic decoders achieve high-quality token-to-mel generation, but their iterative sampling requires multiple neural function evaluations, limiting low-latency speech synthesis. MeanFlow reduces the sampling budget by modeling the average velocity over a temporal interval, yet maintaining high acoustic quality under extremely few-step token-to-mel generation remains challenging. To address this challenge, we propose X-Pred MeanFlow, a few-step streaming token-to-mel decoder that reparameterizes MeanFlow with mel-space prediction. The decoder predicts a generalized mel field and analytically derives the corresponding average velocity for sampling, thereby preserving the MeanFlow formulation while providing a direct acoustic prediction target. We further introduce layer-selective block-wise attention to enable continuous chunk-wise generation with bounded context. Experiments show that X-Pred MeanFlow improves few-step token-to-mel synthesis over Direct-$u$ MeanFlow and supports stable streaming generation. Speech samples are available.https://renxiaming.github.io/xpred-meanflow-stream-demo

</details>

#### [CVSS-X: A Multilingual Speech-to-Speech Translation Corpus for 28 Languages](https://arxiv.org/abs/2609.13413) · [📄 Read](papers/2026/2609.13413.md)

**Lucas Rafael Stefanel Gris, Alef Iury Siqueira Ferreira, Frederico Santos de Oliveira, Augusto Seben da Rosa et al.** · 2026-09-11

<details>
<summary>Abstract</summary>

We introduce CVSS-X, a large-scale synthetic speech-to-speech translation corpus that extends CVSS by reversing the translation direction. While CVSS translates from 21 languages into English, CVSS-X enables translation from English into 28 target languages spanning 12 language families. The corpus comprises approximately 240,000 parallel speech pairs per language, totaling over 16,000 hours, eight times larger than CVSS. We provide two variants: CVSS-X-C with two canonical voices per language, and CVSS-X-T with cross-lingual voice cloning, both fully generated. Evaluation shows comparable translation quality to CVSS with consistent performance across typologically diverse languages. Combined with CVSS, this enables research on bidirectional and multilingual speech-to-speech translation. The code is available at https://github.com/ErmisAI/XVSS-X and the dataset under CC-BY-NC 4.0 license at https://huggingface.co/datasets/lgris/XVSS-X.

</details>

#### [Not All Attacks Are Learned Equally in Speech Deepfake Detection](https://arxiv.org/abs/2609.11763) · [📄 Read](papers/2026/2609.11763.md)

**Avantika Singh, Aurosweta Mahapatra, Ismail Rasim Ulgen, Nicholas Andrews et al.** · 2026-09-10

<details>
<summary>Abstract</summary>

Speech deepfake detection (SDD) models are trained on multi-attack datasets containing diverse spoofing systems, such as text-to-speech (TTS) and voice conversion (VC). In standard classifier training on multi-attack datasets, all attacks are treated as one spoofed class, and performance is reported using overall Equal Error Rate (EER). This aggregate view obscures how individual attacks shape learning and generalization. To better understand this attack-level behavior, we first balance TTS and VC exposure using sample and attack omission. We then measure attack-wise EER at inference and analyze attack-wise training loss and predictive entropy to characterize optimization. Results show that attacks contribute unequally: some attacks have high EER sensitivity and concentrated entropy with low loss, indicating strong influence on the decision boundary. We define these as high-impact attacks. To reduce uneven generalization across attacks, we propose a replay-regularized, attack-aware curriculum that steps exposure based on measured attack influence. Experiments on ASVspoof 2019, 2021, ASVspoof 5, and Fake-or-Real show improved overall robustness and reduced attack-level imbalance compared with standard multi-attack training.

</details>

#### [Continuous-Time Acoustic Modelling with Neural Controlled Differential Equations](https://arxiv.org/abs/2609.11725) · [📄 Read](papers/2026/2609.11725.md)

**Mattias Cross, Minghui Zhao, Anton Ragni** · 2026-09-10

<details>
<summary>Abstract</summary>

Text-to-speech (TTS) models commonly address text--speech alignment by expanding phone-level encoder states to frame-level decoder inputs using predicted durations. While this length-regulation step resolves alignment structurally, this use of duration typically changes only where and how often latent states appear, not the values of the states themselves. This paper proposes a continuous-time mechanism for duration-aware acoustic modelling in TTS using neural controlled differential equations (CDEs). We formulate the phone representation as a temporally parameterised control path and use a neural acoustic vector field to produce a continuous-time hidden state whose values evolve with phonetic content and duration-derived timing. The resulting trajectory can be sampled at discrete points and integrated into a standard acoustic decoder pipeline. Objective results contrast CDEs and typical recurrent models. Subjective results suggest that CDE-based models evaluating one phone per step can improve rank-order agreement between synthesised and reference emotion intensity while maintaining comparable emotion-expression quality to a strong baseline. Additional experiments with half-phone step-sizes suggest that temporal resolution changes the trade-off between style tracking and absolute calibration. These results position CDEs as a promising design space for continuous-time and duration-aware style-sensitive TTS.

</details>

#### [Complex-Text Robustness Evaluation and Failure Diagnosis for Low-Resource Multilingual Text-to-Speech](https://arxiv.org/abs/2609.11545) · [📄 Read](papers/2026/2609.11545.md)

**Tianlun Zuo, Ziyu Zhang, Tingzhi Mao, Zhonghua Fu et al.** · 2026-09-10

<details>
<summary>Abstract</summary>

Low-resource multilingual text-to-speech (TTS) systems have expanded language coverage, but their robustness under complex text inputs remains insufficiently diagnosed. Existing evaluations mainly focus on naturalness, speaker similarity, and content consistency using regular test sentences, while providing limited insight into how multilingual TTS systems fail when handling challenging inputs such as numbers, dates, named entities, long sentences, code-switched expressions, and punctuation-related structures. This paper proposes a complex-text robustness diagnosis framework for low-resource multilingual TTS. We evaluate robustness from three dimensions: content consistency, language consistency, and generation stability. A multilingual robustness testing scheme is designed for Thai, Vietnamese, Swahili, and Indonesian, covering ordinary sentences and multiple types of complex text inputs. We further introduce automatic diagnostic metrics, including character error rate, language identification accuracy, and duration abnormal rate. To support input-level risk analysis before speech generation, we propose a lightweight Text Risk Score (TRS), which estimates synthesis risk from interpretable text features without manual annotation or model training. Experiments on three representative multilingual TTS systems, including OmniVoice, VoxCPM2, and MMS-TTS, show that complex text inputs expose systematic failure patterns that are not fully reflected by ordinary short-sentence evaluation. Different systems exhibit distinct vulnerabilities in number normalization, named entity handling, long-text generation, and code-switched input processing. Furthermore, TRS shows a positive correlation with content errors and duration abnormalities, demonstrating its usefulness as a low-cost pre-synthesis indicator for complex-text risk diagnosis in low-resource multilingual TTS.

</details>

#### [Post-Training Zero-Shot TTS for Fine-Grained Emotion and Duration Control via Natural Language](https://arxiv.org/abs/2609.11523) · [📄 Read](papers/2026/2609.11523.md)

**Lianru Gao, Yujie Guo, Yong Qin** · 2026-09-10

<details>
<summary>Abstract</summary>

Audiobook narration, conversational agents, and audiovisual dubbing require speech that conveys changing emotions and adapts its pacing within a single utterance. But most existing TTS systems typically rely on utterance-level style conditioning, making such fine-grained control difficult to achieve. In light of this, and inspired by the success of post-training in large language models, we propose a unified post-training framework that equips pretrained text-to-speech models with natural-language control over segment-level emotion and duration. Supervised fine-tuning establishes instruction-conditioned speech generation, while reinforcement learning with group relative policy optimization refines control accuracy using emotion and duration rewards alongside content and speaker preservation objectives. By reusing the pretrained architecture, our approach avoids additional inference-time control modules. Experiments demonstrate significantly improved fine-grained controllability while maintaining speech intelligibility and speaker identity, highlighting post-training as a practical approach to extending existing speech synthesis models.

</details>

#### [Flexible and Interpretable Accent Distance Measurements](https://arxiv.org/abs/2609.11458) · [📄 Read](papers/2026/2609.11458.md)

**Charles McGhee, Mark J. F. Gales, Kate M. Knill** · 2026-09-10

<details>
<summary>Abstract</summary>

Determining the differences between two speakers' accents is a fundamental task in linguistics and speech technology research. The methodology used to measure these differences depends on the specific research area. A phonetics researcher may demonstrate accent variation by comparing vowel formants in paired recordings of individual words. These results will be interpretable, but the recordings will be time-consuming to collect and may not be representative of connected speech. Accented Text-to-Speech (TTS) research has pushed towards using accent embeddings derived from accent classification tasks. These embeddings can be produced from any speech recording, but are not readily interpretable. In this paper, we demonstrate that articulatory representations created through articulatory inversion can be used as an interpretable basis for accent comparison and that optimal transport provides a framework for accent comparison across arbitrary recording types.

</details>

#### [ZipCodec: Ultra-Low-Frame-Rate Streaming Speech Coding](https://arxiv.org/abs/2609.11642) · [📄 Read](papers/2026/2609.11642.md)

**Luca Della Libera, Cem Subakan, Mirco Ravanelli** · 2026-09-10

<details>
<summary>Abstract</summary>

Neural audio codecs are a fundamental component of modern speech generation systems. While recent codecs achieve increasingly low bitrates, reducing frame rate remains challenging, as each token must preserve more information while maintaining reconstruction quality. We present ZipCodec, a streaming neural speech codec operating at 6.25 Hz and 0.80 kbps with a theoretical latency of 160 ms. Our approach combines large-scale WavLM distillation with a redesigned transformer-based architecture, a scalar spherical quantizer, and a latency-aware streaming decoder. Experiments show that ZipCodec substantially outperforms existing streaming codecs at comparable bitrates in both reconstruction and downstream tasks, while operating at a significantly lower frame rate. Despite its 842M parameters, ZipCodec achieves real-time single-stream inference on a consumer-grade CPU. Demo samples, code and checkpoints are available at https://lucadellalib.github.io/zipcodec-web/.

</details>

#### [Seeing the Voice, Preserving the Self: A Participatory Design Approach to Deaf-Centric Text-to-Speech](https://arxiv.org/abs/2609.10199) · [📄 Read](papers/2026/2609.10199.md)

**Shela Atemnkeng, Patrick Boudreault, Paige DeVries, Lloyd May et al.** · 2026-09-09

<details>
<summary>Abstract</summary>

We describe a participatory design approach toward developing Deaf-centric text-to-speech (TTS) technologies. While TTS is growing rapidly in the mainstream, it has received little attention to date in the deaf and hard of hearing (DHH) technology space. Critical problems have remained unaddressed for DHH users, including the ability to manipulate tone, emotions and delivery via non-auditory means. Verifying that the generated speech matches intent and is appropriate for a given situation without having to listen to it is another challenge. Respecting cultural and identity factors in the generated speech is also important. This work explores the design space with DHH participants through two focus groups, three co-design sessions, and four one-on-one early-stage design evaluation sessions. Participants included people both familiar and unfamiliar with TTS, as well as DHH content creators. We describe key findings, design ideas, results, and implications for future Deaf-centric TTS development. We also identify unmet technology requirements that pose barriers to adoption of Deaf-centric TTS technology.

</details>

#### [X2-NativeCursor: Native-Token Text Progress Tracking for Incremental-Text Streaming Codec TTS](https://arxiv.org/abs/2609.09677) · [📄 Read](papers/2026/2609.09677.md)

**Zehan Liu, Carl Chen, Rime Wen, Kaiqi Fu et al.** · 2026-09-09

<details>
<summary>Abstract</summary>

Incremental-text streaming text-to-speech (TTS) needs online text progress tracking for synchronized highlighting, interruption handling, and dialogue-history updates. Input text arrives before it is spoken, so text arrival alone cannot indicate speech progress. Existing waveform-based alignment requires complete audio or adds acoustic processing during streaming. We propose X2-NativeCursor, a lightweight observer that tracks progress from native speech tokens before waveform decoding without changing the TTS generator. Its normalization plan links spoken labels to their original-text spans. Text and native-token encoders feed a local matcher that estimates the current label position. A separate output rule converts revisable position estimates into a cursor that never moves backward. Mean absolute error against an automatic reference is 0.151 Chinese characters with 80-ms lookahead, versus 1.253 characters with 320-ms lookahead for an online waveform baseline. Alignment real-time factor also decreases from 0.3598 to 0.0180 relative to this baseline. Lower tracking error is retained under a second automatic alignment reference. We evaluate X2-NativeCursor on Qwen3-TTS and validate its adaptation to CosyVoice2 by training a separate observer for each backbone. Code is publicly available at https://github.com/X-Square-Robot/X2Streaming-TTS.

</details>

#### [SCNet: Enhancing GAN-based Speech Generation with Subband Condition Network and Magnitude-aware Phase Loss](https://arxiv.org/abs/2609.10025) · [📄 Read](papers/2026/2609.10025.md)

**Nan Xu, Mingxue Yang** · 2026-09-09

<details>
<summary>Abstract</summary>

Recent speech generation has been predominantly driven by GAN-based networks aimed at high-quality waveform synthesis from mel-spectrograms. However, these methods often operate as black-box models, leading to the loss of inherent spectral information. In this work, we propose SCNet, a GAN-based vocoder augmented with a Subband Condition Network to address this issue. Specifically, SCNet leverages a subband signal predicted by a lightweight condition network as prior knowledge. This subband signal is then transformed via STFT to obtain Fourier coefficients, which are integrated into the backbone for the enhanced reconstruction. Additionally, to mitigate the phase wrapping, we introduce a magnitude-aware phase loss that computes instantaneous phase errors weighted by the corresponding magnitude, emphasizing regions with higher energy. Experimental results demonstrate that SCNet achieves superior performance in both objective and subjective evaluations for high-quality speech generation.

</details>

#### [SpeechAnnotator: A Context-Aware Multi-Agent Framework and Benchmark for Multidimensional Speech Annotation](https://arxiv.org/abs/2609.09947) · [📄 Read](papers/2026/2609.09947.md)

**Qirui Zhan, Shuiyuan Wang, Jingbin Hu, Haoyu Zhang et al.** · 2026-09-09

<details>
<summary>Abstract</summary>

Recent controllable speech generation requires training data with fine-grained annotations of speaker traits, prosody, emotion, paralinguistic cues, acoustic scenes, and context. Existing workflows often rely on manual correction, paid hosted multimodal services, or fixed processing chains, which limits large-scale data processing through annotation cost, external-service dependence, or weak cross-stage recovery. We introduce SpeechAnnotator, a locally deployable, context-aware multi-agent framework built entirely from open-source models and tools. Supporting frontend modules first obtain speaker-aware segments and final segment transcripts, while prior evidence extractors attach heterogeneous segment-level cues. Three specialist agents then collaborate through shared state: the Planning Agent converts local audio evidence, speaker history, neighboring segments, and recording-level context into field-specific contracts; the Labeling Agent performs contract-guided multimodal prediction for directly observable attributes; and the Review Agent runs a bounded review loop that checks evidence support and cross-segment consistency, triggering relabeling only for unsupported or inconsistent fields. To address the fragmentation of existing evaluation resources across isolated tasks and narrow-domain test sets, we introduce SpeechAnnotator-Bench (SA-Bench), containing 8.87 hours of human-annotated audio across nine source formats, together with SpeechAnnotator-Eval (SA-Eval), which separates Timeline-Eval for speaker-aware timeline recovery, Closed-Eval for finite-set attributes, and Open-Eval for open-ended attributes. Experiments and ablations show that SpeechAnnotator provides a locally deployable alternative to commercial audio-capable systems, while the bounded review loop improves multidimensional annotation through evidence- and context-aware field-level recovery.

</details>

#### [SphereVAE: Hyperspherical Latent Autoencoders for Robust Autoregressive Speech Representation Modeling](https://arxiv.org/abs/2609.09903) · [📄 Read](papers/2026/2609.09903.md)

**Haoyu Zhang, Jingbin Hu, Hanke Xie, Qirui Zhan et al.** · 2026-09-09

<details>
<summary>Abstract</summary>

With the rapid development of speech generation technology, discrete codec representations have been widely used because they provide a stable prediction paradigm. In expressive speech generation, however, the quantization bottleneck of discrete codecs results in information gaps in fine-grained prosody, timbre, pronunciation, and frame-to-frame continuity. Continuous representations (e.g., VAE latents), by eliminating this constraint, have emerged as a more effective alternative for autoregressive modeling. Yet when continuous representations are used as autoregressive prediction targets, prediction errors can accumulate along the generation chain, causing latent drift and degrading long-form stability. To mitigate this problem, we propose SphereVAE, which constrains the VAE latent space to the unit hypersphere. SphereVAE defines a Power Spherical posterior on the hypersphere and regularizes the latent distribution toward a uniform prior, so that information is encoded mainly by directional variation, providing a bounded geometric target for autoregressive prediction and reducing the risk of norm drift. SphereVAE underperforms the standard VAE on reconstruction metrics due to reduced latent freedom. However, when integrated into VoxCPM for zero-shot TTS and long-text generation, it yields lower content error rates with comparable speaker similarity, and shows more stable long-range speaker consistency. These results indicate that an appropriate latent geometric constraint can effectively mitigate autoregressive error accumulation and drift in speech generation.

</details>

#### [TASTE2: Text-Aligned Speech Modeling and Deployment toward Full-Duplex Voice Interaction](https://arxiv.org/abs/2609.08956) · [📄 Read](papers/2026/2609.08956.md)

**Yi-Chang Chen, Chun Wei Chen, Dien-Ruei Wu, Jie Lin et al.** · 2026-09-08

<details>
<summary>Abstract</summary>

Full-duplex voice interaction requires more than utterance-level conversion. It must process streaming speech, manage turn-taking and interruptions, while preserving pretrained linguistic competence and acoustic paralinguistic cues. We ask whether TASTE (Text-Aligned Speech Tokenization and Embedding) provides a viable path toward this goal. We present TASTE2, which transforms utterance-level TASTE into an incremental dialogue stack. A shared text-token vocabulary removes word-level averaging, while modality-aligned dialogue training predicts one continuous audio latent per text token without interleaving heterogeneous token streams. An incremental Speech Detokenizer enables streaming synthesis through CosyVoice2. After speech and dialogue training, TASTE2 (Merge) reaches 56.3% on LLaMA-Questions against a 57.3% Qwen2.5-7B Instruct text-only reference (98.2% accuracy retention), and TASTE2 (Direct) reaches 53.0% (92.4% retention). We build TASTE2 VoiceBot, which processes user speech incrementally, streams synthesized audio, and stops generation on barge-in. On Full-Duplex-Bench v1.0, TASTE2 and TASTE2 VoiceBot handle interruptions well while maintaining high conversational coherence. Natural conversation remains challenging, and deployed mean time to first audio is 2.701 s on two NVIDIA RTX A6000 after TensorRT acceleration. Finally, to our knowledge, we provide the first systematic characterization of explicit paralinguistic control in a TASTE based model. Fast speaking rate serves as a cross-strategy proof of concept after dialogue SFT, while emotion control is strategy dependent and the remaining attributes stay weak. Together, these results establish TASTE based modeling as a practical route toward full-duplex systems while identifying natural conversation robustness, speech generation latency, and feature general paralinguistic control as open challenges. Explore TASTE2 online.

</details>

#### [Disentangled Global-Local Feature Learning with E-Branchformer for Audio Deepfake Detection](https://arxiv.org/abs/2609.08948) · [📄 Read](papers/2026/2609.08948.md)

**Phuong Tuan Dat, Ho Bao Thu, Nguyen Tran Trung, Pham Viet Hoang et al.** · 2026-09-08

<details>
<summary>Abstract</summary>

The rapid advancement of voice synthesis technologies such as text-to-speech and voice conversion poses significant threats to speech-based authentication systems, necessitating robust deepfake detection methods. In this work, we propose a novel E-Branchformer-based architecture that effectively leverages self-supervised speech representations for audio deepfake detection. Our model employs parallel branches to simultaneously capture global contextual dependencies through multi-head self-attention and local temporal patterns through convolutional processing. To enhance discriminative capability, we integrate depthwise convolution and Squeeze-and-Excitation modules that enrich the classification token with refined patch token information after feature merging. Extensive experiments on ASVspoof 2021 LA, DF, and In-the-Wild datasets demonstrate state-of-the-art performance with equal error rates of 0.88%, 1.85%, and 6.30% respectively, substantially outperforming existing methods. Comprehensive ablation studies validate that the dual-branch architecture provides complementary discriminative information, Squeeze-and-Excitation Aggregation significantly improves SSL feature integration, and the combination of DWConv and SE modules is critical for effective class token enhancement. The superior performance on real-world scenarios demonstrates strong generalization capability to diverse acoustic conditions and unseen spoofing attacks.

</details>

#### [TontaubeV1: Streaming Text-to-Speech with Hierarchical Codec Modeling and Bounded Context](https://arxiv.org/abs/2609.08703) · [📄 Read](papers/2026/2609.08703.md)

**Fritz Cremer, Jonathan Cremer** · 2026-09-08

<details>
<summary>Abstract</summary>

Text-to-speech systems often face a trade-off between natural prosody and efficient inference: higher perceptual quality typically comes at increased computational cost and latency. We present TontaubeV1, a model that preserves natural prosody while enabling streaming from a single consumer GPU. Speech is encoded by the hierarchical DualCodec representation at 12.5 Hz, which separates a semantic stream from successive acoustic refinements. Our design assumes that prosodic structure is largely established when the semantic stream is generated, and allocates capacity accordingly: a Qwen3-1.7B-derived transformer predicts that stream and thereby the utterance duration, while three progressively smaller Qwen3-0.6B-derived transformers each add one acoustic refinement. Text is tokenized per character rather than by subword. Paired text and audio markers at shared positions support long-form generation with bounded context, and overlapping DualCodec reconstructions are mapped into the VibeVoice acoustic latent space and decoded causally, enabling streaming despite DualCodec's noncausal decoder. The model accepts up to one minute of reference audio for voice conditioning and is designed primarily for English and German, with additional multilingual support. The four predictors total 2.9B parameters; on a single RTX 5090 the streaming path reaches approximately 200 ms to first audio. In separate non-streaming measurements, the end-to-end real-time factor (RTF) is 0.08 for one input and the aggregate RTF is 0.02 across eight concurrent inputs. On our LLM-as-a-judge audiobook-reading benchmark, TontaubeV1 matches ElevenLabs Flash v2.5 and outperforms Fish Audio S2 Pro, the April 2026 Gradium API, and Cartesia Sonic 3 on prosody. The model weights are released on Hugging Face under the Tontaube Community Model License 1.0.

</details>

#### [AuK Technical Report: An Open-Source Foundational Model for Speech Generation and Editing](https://arxiv.org/abs/2609.08936) · [📄 Read](papers/2026/2609.08936.md)

**Ziyang Ma, Zhikang Niu, Wenming Tu, Tianrui Wang et al.** · 2026-09-08

<details>
<summary>Abstract</summary>

We introduce AuK, an open-source foundational model that unifies speech generation and editing through a common interface of natural-language instructions and audio context. To support this broad capability set, we construct approximately 3.03 billion instruction--audio instances and 1.95 million hours of effective supervision across five task families: speech generation, content editing, enhancement and separation, paralinguistic editing, and acoustic editing. AuK combines a multimodal large language model for semantic conditioning, an VAE jointly trained on speech, general audio, and music for acoustic conditioning, and a hybrid rectified-flow Transformer that performs dual-stream MMDiT blocks followed by unified single-stream DiT blocks for generation. Training begins with generation-only warm-up and proceeds to joint generation--editing pre-training. We then apply complementary post-training strategies: human-feedback preference optimization for open-ended editing and reward-based reinforcement learning for speech generation. To reduce inference cost, we further distill the model with consistency initialization and task-routed Decoupled DMD. The resulting AuK-Flash performs 4-step inference without classifier-free guidance and achieves a 4.5 wall-clock speedup over the full model under matched conditions. Experiments demonstrate leading performance on zero-shot and instruction-controlled speech generation and general instruction-guided editing, while remaining competitive on signal-level restoration tasks. We release both the source code and model weights to support reproducibility and further research.

</details>

#### [Audio Deepfake Detection Using Temporal Coherence Analysis](https://arxiv.org/abs/2609.09489) · [📄 Read](papers/2026/2609.09489.md)

**Justin D. Norman, Sarah Barrington** · 2026-09-08

<details>
<summary>Abstract</summary>

The proliferation of AI-generated audio (so-called "deepfake" audio) poses significant threats to information integrity, from voice cloning fraud to synthetic music copyright disputes. We present a temporal coherence analysis framework built upon Contrastive Language-Audio Pretraining (CLAP) embeddings that spans speech, instrumental music, and music with vocals. By computing pairwise cosine similarities between audio segment embeddings and extracting statistical features from the resulting distributions, we train lightweight ensemble classifiers that reliably distinguish authentic from synthetic audio. Our work provides an interpretable, computationally efficient alternative to common deep learning methods while still achieving competitive performance across speech and music domains. Further, we reveal two notable empirical findings about audio deepfakes: (1) a feature-label inversion phenomenon in which 21 of 29 statistical features reverse their discriminative direction between training and in-the-wild deployment, and (2) a speech--music direction reversal in which entropy discriminates in opposite directions for speech and music deepfakes.

</details>

#### [What Did I Just Say? Self-Listening for Full-Duplex Speech Models](https://arxiv.org/abs/2609.05592) · [📄 Read](papers/2026/2609.05592.md)

**Xuanning Zhou, Junyi Ao, Xiaotong Liu, Tom Ko et al.** · 2026-09-04

<details>
<summary>Abstract</summary>

Full-duplex spoken language models can listen and speak simultaneously, enabling them to handle interruptions and backchannels in human conversation. However, text generation, speech synthesis, and audio playback proceed asynchronously. As a result, what a model believes it has said may not match what has actually been played to the user. We refer to the problem of recovering from an interruption while remaining aware of the model's realized speech as anchor interruption. To address this problem, we propose Self-Listening, a full-duplex modeling approach that interleaves user speech, model text, and the model's played speech. By feeding the realized speech output back to the model as an input stream, self-listening grounds interruption recovery in what the user has actually heard. We further introduce AnchorSpeech, a collection with homogeneous training and test splits for tracking which items of structured ordered responses have actually been spoken. AnchorSpeech-test evaluates whether a model can respond consistently with the last completed item before an interruption. Experiments show that, compared with full-duplex baselines, models equipped with self-listening mechanism achieve better anchoring performance.

</details>

#### [PACodec: A Low-bitrate Neural Speech Codec with Parallel Additive Vector Quantization](https://arxiv.org/abs/2609.03363) · [📄 Read](papers/2026/2609.03363.md)

**Fei Liu, Yang Ai, Xiao-Hang Jiang, Zhen-Hua Ling** · 2026-09-03

<details>
<summary>Abstract</summary>

This paper proposes PACodec, a novel low-bitrate neural speech codec based on parallel additive vector quantization (PAVQ). Unlike the mainstream residual vector quantization (RVQ) used in most neural speech codecs, where vector quantizers (VQs) are sequentially dependent, the PAVQ strategy adopted in PACodec aggregates parallel quantization results to optimize bitrate usage. Specifically, the PAVQ adopts a "global-local-global" (GLG) design: the global encoded features are quantized in parallel by multiple independent VQs, each attending to a local component of the representation, and their outputs are aggregated through addition to yield the final global quantization result for decoding. Experimental results show that PACodec, as each VQ focuses only on local information, supports smaller codebooks and reduces bitrate by 30% compared with baselines at the same decoding quality, with only minor model complexity. Further analysis shows that, owing to the GLG framework of PAVQ, the proposed PACodec is disentanglement-friendly, and each independent VQ captures different aspects of speech, e.g., content, timbre, and acoustic details, suggesting potential for application to downstream tasks such as voice conversion.

</details>

#### [Building and Evaluating Fixed-Voice Thai TTS from Synthetic Speech](https://arxiv.org/abs/2609.03502) · [📄 Read](papers/2026/2609.03502.md)

**Kunat Pipatanakul, Potsawee Manakul, Warit Sirichotedumrong, Sittipong Sripaisarnmongkol et al.** · 2026-09-03

<details>
<summary>Abstract</summary>

In low-resource settings, deploying TTS typically requires choosing between a large voice-cloning model with costly inference or a compact fixed-voice system that requires a speaker-specific corpus. We study a third route: using a large voice-cloning model as a programmable data source to turn a short voice reference (e.g., 15 seconds) into a compact fixed-voice student trained entirely on synthetic speech. This setting makes pipeline design consequential: teacher errors become training targets, while filtering failed generations can reduce coverage of difficult texts. Thai further introduces challenges from ambiguous word boundaries, lexical tone, names and loanwords, numeric verbalization, and Thai-English code-switching. We study how text preparation, synthetic generation, quality filtering, rejection sampling, and frontend choices affect the resulting student, and where teacher limitations remain. We evaluate CER, Challenge-Set Keyword Accuracy, Prosody Pause Accuracy, speaker similarity, and speaking rate. The resulting 82M-parameter model, Wayu-Paxa-TTS-Edge, enables on-device Thai TTS without reference audio. It achieves 68.2% Challenge-Set Keyword Accuracy (85.5% of Gemini 3.1) and 91.4% pause precision, outperforming its OmniVoice teacher (89.9%) and reaching 94.8% of Gemini 3.1. It also achieves the lowest pause-placement error and intra-word pause rates among the three systems, and 3.7% and 1.1% CER on Thai and English, respectively. We open-source the model and evaluation framework for Thai TTS development.

</details>

#### [Deep Neural Compression for RIR-Characterized Acoustic Environments with Structure-Aware Constraints](https://arxiv.org/abs/2609.04085) · [📄 Read](papers/2026/2609.04085.md)

**Chen-Yuan Ning, Yang Ai, Hui-Peng Du, Xiao-Hang Jiang et al.** · 2026-09-03

<details>
<summary>Abstract</summary>

Room impulse responses (RIRs) characterize the acoustic environment of a room by capturing how sound propagates and decays within an enclosed space. In applications such as immersive audio rendering, accurate acoustic reconstruction often relies on spatially densely sampled RIRs. This consequently gives rise to a large volume of RIR data, imposing a substantial burden on storage. Although recent neural audio codecs provide an effective framework for low-bitrate compression, their training objectives are mainly tailored to speech and general audio, and are therefore not well aligned with the acoustic characteristics of RIRs. Therefore, we propose an EnCodec-based neural RIR compression method, which incorporates RIR structure-aware constraints at two levels. Specifically, at the RIR level, structure-aware constraints are imposed on the global decay behavior and local energy distribution of RIRs through energy decay curve (EDC) regularization and a short-time window energy constraint, while at the reverberant-speech level, reverberant-speech supervision is further introduced to constrain the consistency of the reverberant speech generated by the reconstructed RIRs. Experimental results show that, at a low bitrate of 375 bps, the proposed method achieves lower RIR reconstruction error and better reverberant-speech perceptual consistency than audio-oriented codecs.

</details>

#### [Brain2Speech-Net: Intelligible, Real-Time Brain-to-Speech Synthesis Without Text Decoding](https://arxiv.org/abs/2609.04455) · [📄 Read](papers/2026/2609.04455.md)

**Shreeram Suresh Chandra, Zexin Cai, Yu Tsao, Simon King et al.** · 2026-09-03

<details>
<summary>Abstract</summary>

The loss of speech limits communication for individuals with paralysis. Restoring speech by synthesizing it directly from neural activity is challenging: intracortical data are scarce and lack aligned targets, so most systems rely on cascaded neural-to-text-to-speech pipelines that add latency and propagate errors. We present Brain2Speech-Net, among the first single-stage frameworks to remain intelligible under limited data while removing intermediate text decoding. A differentiable phoneme bottleneck preserves linguistic structure without explicit text decoding. A lightweight deep-HMM aligner then maps this bottleneck to contextual phoneme representations in a TTS latent space. It learns monotonic alignment between neural recordings and phoneme segments without frame-level supervision, inheriting strong acoustic priors for data-efficient training. On an intracortical dataset, Brain2Speech-Net achieves strong intelligibility in objective and listening tests while running faster than real time. Unlike cascaded systems that incur high latency and direct speech-unit models that lack intelligibility, it delivers both intelligible and real-time speech.

</details>

#### [Alignment-Free Text-Audiobox for Voice Dubbing and Full-Duplex Dialogue Synthesis](https://arxiv.org/abs/2609.03992) · [📄 Read](papers/2026/2609.03992.md)

**Sanyuan Chen, Min-Jae Hwang, Sho Inoue, Anna Sun et al.** · 2026-09-03

<details>
<summary>Abstract</summary>

We present Alignment-Free Text-Audiobox (Text-AB), a unified framework for high-quality voice dubbing and full-duplex dialogue synthesis. Building on a Diffusion Transformer trained with a flow-matching objective, Text-AB departs from the Audiobox system along three dimensions. First, it operates in a latent diffusion framework using DAC-VAE features that encode 48 kHz waveforms into a 25 Hz latent sequence, giving over 10x higher compression than previous EnCodec representations while improving resynthesis quality. Second, Text-AB is alignment-free: it consumes raw text via an off-the-shelf text encoder and learns text-speech alignment through cross-attention, removing the need for forced alignment and explicit duration prediction. Third, we scale model and data substantially, pretraining a 3B-parameter model on 480k hours of monolingual speech, followed by supervised fine-tuning on three downstream tasks: cross-lingual voice dubbing, full-duplex dialogue synthesis, and emotional full-duplex dialogue synthesis. At inference, Text-AB supports one-shot generation for up to ~1 min of speech and arbitrarily long-form generation via a multi-diffusion scheme, plus a multi-stage reranking strategy that enhances quality based on automated metrics. On a real-world dubbing benchmark, Text-AB delivers a step-change improvement over the latest internal dubbing system, with large gains in prosody similarity, voice similarity, naturalness, and shareability. For full-duplex dialogue synthesis, it approaches human recordings on short-form conversations and substantially outperforms the latest internal model on long-form human-likeness and expressivity, while natively modeling turn-taking, back-channeling, and emotional dynamics. For emotional dialogue synthesis, emotion conditioning significantly improves emotion alignment and emotional interaction quality over the unconditioned baseline.

</details>

#### [Ready to Speak: Aligning LLMs for TTS-Friendly Text Generation](https://arxiv.org/abs/2609.01246) · [📄 Read](papers/2026/2609.01246.md)

**Thibaut Thonet, Jos Rozen, Laurent Besacier** · 2026-09-01

<details>
<summary>Abstract</summary>

Current Large Language Models (LLMs) are primarily optimized for written text, often producing outputs that are grammatically correct and helpful yet poorly suited for spoken delivery via Text-to-Speech (TTS). In this work, we study how to make LLMs natively generate TTS-friendly text, which we frame as a preference alignment problem: instead of relying on downstream rewriting modules, we directly align LLMs to generate text optimized for spoken delivery. We introduce two preference datasets spanning different target domains, CORA and Recipe, which contain paired TTS-friendly and TTS-unfriendly responses. We further propose an evaluation suite combining a pattern-based heuristic metric, a TTS$\to$ASR evaluation pipeline, and a MUSHRA listening study with human judges. Our experiments compare the recently proposed Feature-aware Sampling and Tuning (FaST) framework -- leveraging interpretable features instead of a black-box reward model -- against an array of alignment baselines on the TTS-friendly generation task. Notably, we found that FaST achieves the best overall tradeoff between TTS-friendliness and helpfulness across various settings. We also identified a strong correlation between our different metrics, highlighting the ability to reliably assess TTS-friendliness via an efficient heuristic.

</details>

#### [Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech](https://arxiv.org/abs/2609.01016) · [📄 Read](papers/2026/2609.01016.md)

**Che Hyun Lee, Sangkwon Park, Donghun Kang, Dongwook Lee et al.** · 2026-09-01

<details>
<summary>Abstract</summary>

Current speech synthesis struggles with code-switching, which mixes a foreign language phrase into a primary language utterance, causing the phrase to be spoken with the primary language's accent rather than its native one. We propose Phrase-Localized Language-Contrastive Guidance (LCG), a training-free inference framework that restores a native accent to code-switched phrases in cross-lingual text-to-speech. LCG replaces the single language guidance applied across the whole utterance with a separate guidance for each region, so each part is guided by its own language. To choose where to apply this localized guidance, we propose a self-attention probing technique that finds the phrase boundaries without external alignments. Together, these components generate speech in which each region carries the accent of its own language, requiring no fine-tuning or auxiliary models. Across diverse language pairs, LCG robustly increases the nativeness of the code-switched phrase while suppressing accent leakage, and preserving overall speaker identity and naturalness.

</details>

#### [Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models](https://arxiv.org/abs/2609.01723) · [📄 Read](papers/2026/2609.01723.md)

**Kunlin Cai, Kaiyuan Zhang, Zihang Xiang, Jinghuai Zhang et al.** · 2026-09-01

<details>
<summary>Abstract</summary>

Text-to-Speech (TTS) foundation models are increasingly fine-tuned on private datasets to synthesize highly personalized voices, introducing severe privacy risks by exposing both biometric identities and sensitive speech content. Existing black-box membership inference attacks (MIAs) follow a two-stage pipeline of query generation and representation engineering, both of which face unique challenges when adapted to TTS. For query generation, dual conditioning on synthesis text and reference speech creates a large and underexplored query design space with no established criterion for identifying an effective query. For representation engineering, the multi-level speech characteristics and temporal variability of speech make low-level representations and direct comparisons inadequate for capturing membership signals. To address these challenges, we present the first black-box MIA framework explicitly tailored to TTS models at both the speaker and record levels. For query generation, we characterize the feasible query space and establish two criteria, scorable extent and memorization elicitation, for evaluating five representative queries, identifying recitation as the strongest. For representation engineering, we obtain multi-level speech representations from embedding models and temporally align the generated and target audio for fine-grained comparison. Evaluations across three state-of-the-art TTS models (CosyVoice2, F5-TTS, and XTTS-v2) fine-tuned on two benchmark datasets (VCTK and British Dialect) reveal severe privacy leakage: speaker-level AUC remains above 0.80 and approaches 1.0 in the strongest settings, while record-level AUC ranges from 0.80 to 0.90 and remains effective even in challenging scenarios where both members and non-members are of the same speakers. We further identify speech characteristics associated with disproportionate vulnerability to memorization.

</details>

#### [BiMTokenizer: Preserving Semantic-Acoustic Balance in Low-Bitrate Speech Tokenization via Bidirectional State-Space Modeling](https://arxiv.org/abs/2609.00562) · [📄 Read](papers/2026/2609.00562.md)

**Xin Zhang, Lin Li, Chuanbo Liu, Jianquan Liu et al.** · 2026-09-01

<details>
<summary>Abstract</summary>

Speech codecs serve as bridges between continuous speech signals and large language models, yet face an inherent conflict between acoustic fidelity and semantic preservation. To mitigate this conflict, recent works increasingly adopt dual-tower architectures to decouple semantic and acoustic modeling with separate encoders. However, these dual-tower designs incur substantial architectural overhead. To avoid such complexity, we revisit the single-tower paradigm and propose BiMTokenizer, a low-bitrate speech codec (around 1.1 kbps) combining a bidirectional state-space backbone with Residual Spherical Leech Quantization (RSLQ). The bidirectional backbone strengthens temporal modeling, while RSLQ offers a fixed, well-separated lattice bottleneck for robust semantic and acoustic tokenization without learned-codebook collapse. Experiments show that BiMTokenizer achieves superior acoustic reconstruction and the lowest WER among low-bitrate codec baselines across both clean and noisy environments, while using less than half the parameters of recent dual-tower baselines. Furthermore, its robust semantic representations yield strong performance on downstream speech understanding tasks, confirming that a well-designed single-tower codec can preserve the semantic-acoustic balance at low bitrates. The code and model weights are available at https://github.com/ZhangXinWhut/BiMTokenizer.

</details>

#### [Heard but Not Heeded: Paralinguistic Information Encoding and Loss in Audio-Language Models](https://arxiv.org/abs/2609.00727) · [📄 Read](papers/2026/2609.00727.md)

**Bhuvan Koduru, Dareen Safar B Alharthi, Rita Singh, Bhiksha Raj** · 2026-09-01

<details>
<summary>Abstract</summary>

Audio language models are designed to understand speech, yet it remains unclear whether they capture how something is said beyond what is said. We present a mechanistic analysis of paralinguistic information in four open source models, Whisper-large-v2, Qwen2-Audio-7B Instruct, Qwen2.5-Omni-7B, and Chroma-4B, using the Expresso dataset with controlled speaking styles. We combine centered kernel alignment, linear probing with leave one speaker out evaluation, open ended tone prediction, and a content prosody leakage metric to trace how style information moves from the audio encoder to the final output. All models strongly encode speaking style in the late encoder, that is, the top third of the audio encoder's layers, but this information is consistently degraded before reaching the output. The projector reshapes representation geometry without removing information, while decoders differ in how much style they preserve depending on architecture and training objective. At the output level, models fall into two behaviors. Some are content driven, where predictions depend mainly on text. Others are acoustic driven, where predictions vary with speaking style. The leakage metric quantifies this difference, and qualitative results confirm it. Overall, we identify a gap between what models encode and what they use, highlighting a key limitation in current audio language models.

</details>

#### [When Does Predictor-Based RL Align with Human Perception? A Study of Subjective Rewards in Codec-Based Speech Language Models](https://arxiv.org/abs/2608.31035) · [📄 Read](papers/2026/2608.31035.md)

**Joonyong Park, Jerry Li** · 2026-08-31

<details>
<summary>Abstract</summary>

Codec-based text-to-speech (TTS) models make language-model post-training applicable to speech generation, but it remains unclear when learned perceptual predictors can serve as reinforcement learning rewards without losing alignment with human listeners. We study this question with Group Relative Policy Optimization (GRPO) using learned rewards for anime-like speaking style, naturalness, likability, and arousal. To prevent perceptual rewards from being optimized through transcript drift, we introduce a character error rate (CER) zone constraint and compare policy optimization with Best-of-$N$ reranking under the same reward gate. Across single-reward runs, each reward primarily improves its own target metric, showing that subjective predictors are not interchangeable quality surrogates. Multi-rater A/B tests further show uneven human transfer, while a reward-gap analysis separates average transfer from within-axis calibration: signed reward gaps significantly predict listener choices in the pooled analysis, whereas residual CER gaps do not, but per-axis calibration remains heterogeneous. Best-of-8 is a strong human-level baseline and is not clearly worse than GRPO perceptually, suggesting that GRPO should be viewed as amortizing reward-selected behavior into the policy rather than uniformly outperforming reranking. These results support analyzing subjective speech rewards as predictor-axis-base tuples and provide practical diagnostics for selecting rewards before multi-reward speech post-training.

</details>

#### [Sequential Trajectories and Simultaneous Blending: Multi-Emotion Modeling for Instruction-Following TTS](https://arxiv.org/abs/2608.30325) · [📄 Read](papers/2026/2608.30325.md)

**Yan Zhou, Yun Hong, Yang Feng** · 2026-08-31

<details>
<summary>Abstract</summary>

Natural-language instructions enable flexible control of synthesized speech, yet emotional TTS systems primarily model a single utterance-level affect, leaving multi-emotion control underexplored. We study two complementary multi-emotion TTS tasks: emotion trajectory, which spans several ordered affective stages, and emotion blending, in which multiple emotions coexist throughout an utterance. These tasks expose a supervision mismatch: supervised fine-tuning (SFT) does not explicitly evaluate emotion features, while single-emotion rewards provide neither structure-aware feedback for trajectory completion nor pair-aware feedback for blending. We introduce HybridEmo, a post-training framework that initializes both tasks with SFT and then aligns the speech-token policy through Group Relative Policy Optimization using a sample-aware hybrid reward. For trajectory samples, segment-aligned consistency combines average and weakest-stage evidence to preserve the correctness and completeness of prescribed stages. For blending samples, a GMM-based reward combines frame-level support from the union of target-emotion anchors in an offline emotion space with an utterance-level weaker-target margin. Both branches share an ASR reward and are routed within a unified policy. On MultiEmo-Test, HybridEmo significantly improves trajectory correctness and blending intensity, without a noticeable degradation in speaker similarity. Human evaluation prefers HybridEmo to CosyVoice 3 and EmoVoice-0.5B, with nearly balanced preferences against Qwen3-TTS.

</details>

#### [When Patients Cut In: Extending Clinical Conversational AI Safety to Interruptions](https://arxiv.org/abs/2608.29241) · [📄 Read](papers/2026/2608.29241.md)

**Zachary Ellis, Spencer Hazel, Adam Brandt, Yajie Vera He et al.** · 2026-08-29

<details>
<summary>Abstract</summary>

Clinical voice agents are now deployed in routine care, where real patients do not wait their turn: they interrupt. These systems typically use a cascaded architecture (speech-to-text -> LLM -> text-to-speech), so when a patient cuts the agent off mid-utterance, clinically required content can be lost even when the model handles cooperative transcripts well. Yet clinical conversational-AI benchmarks almost universally assume patients wait for the agent to finish, missing interruption-induced loss of required content. We present a transcript-based evaluation of interruption recovery, adapting conversation-analytic overlap categories into three operational types (recognitional, competitive, transitional sub-unit) and testing four deployment-oriented, non-reasoning LLM configurations across four cells spanning history-taking (information gathering) and FAQ (information provision), scored on whether the agent preserves the clinically required content. In the gathering cells, target-question failure varied across models; in the provision cells, where arms are directly comparable, failure rose for every model. Rankings differ across cells, and competitive FAQ interruption produced 30/30 provision-coverage failures for all four models (Wilson 95% CI: 88.6-100.0%; baseline 0/30 for three, 4/30 for Llama). A brief apology marker ("sorry to interrupt") shifts recovery by tens of percentage points, inconsistently across models, and for one it reduces recovery. Interruption robustness therefore cannot be a single score: evaluation must be content-grounded, reported per cell, and matched to the deployment's interruption profile.

</details>

#### [EmoSay: Artificial Intelligence-Driven Text-to-Emotional-Speech System for Affective Communication in Extended Reality](https://arxiv.org/abs/2608.26566) · [📄 Read](papers/2026/2608.26566.md)

**Sikiru Ademola Adewale, Sunday D. Ubur, Nikitha Donekal Chandrashekar, Onyeka Emebo et al.** · 2026-08-27

<details>
<summary>Abstract</summary>

While contemporary neural text-to-speech (TTS) systems have achieved high levels of intelligibility, they frequently lack the emotional nuance required for authentic affective communication. This limitation is particularly critical in Extended Reality (XR), where the absence of emotionally expressive audio can diminish user presence and spatial immersion. We present EmoSay, an Artificial Intelligence-driven Text-to-Emotional-Speech (TTES) system designed to bridge the semantic-affective gap in immersive environments. EmoSay modulates a neural synthesis pipeline using discrete emotional prompts, delivering the output through a Unity-based interface featuring high-fidelity spatialized audio. The system was evaluated through a comprehensive user study focusing on perception, engagement, and the subjective sense of empathy. Our results demonstrate that EmoSay significantly enhances the immersive experience, achieving a System Usability Scale (SUS) score of 74.76, indicating strong usability and seamless integration within the XR workflow. Subjective assessments reveal a high degree of perceived naturalness and a strong positive correlation between emotional expressiveness and user engagement. Regression analysis identifies vocal naturalness as the strongest of the tested predictors of user satisfaction, suggesting that EmoSay's affective prosody helps meet the heightened expectations for realism in immersive settings. This work contributes a scalable, affect-aware framework for inclusive XR design and demonstrates the role synthetic emotion can play in fostering human-computer rapport through voice-first interaction.

</details>

#### [Your Voice Cloning System is Secretly a Voice Anonymizer](https://arxiv.org/abs/2608.27360) · [📄 Read](papers/2026/2608.27360.md)

**Romolo Muletta, Felix Matthias Saaro, Mark Cieliebak, Jan Deriu** · 2026-08-27

<details>
<summary>Abstract</summary>

Speaker anonymization suppresses speaker-identifying attributes from speech while preserving linguistic content and quality. We propose repurposing XTTSv2, a multilingual voice cloning model trained on 27k hours of speech, for speaker anonymization without retraining. Our key insight is that XTTSv2's voice cloning capabilities preserve prosodic structure independently of speaker identity, enabling voice conversion by conditioning on a pseudo-speaker. We introduce an iterative refinement strategy that balances privacy and utility by maximizing a harmonic mean of speaker dissimilarity and intelligibility. Evaluated on seven European languages across CommonVoice and Multilingual LibriSpeech, our system achieves near-optimal privacy (EER $\approx$ 0.49), competitive intelligibility, and substantially better speech quality than dedicated anonymization baselines, while requiring no language-specific training. We release the code here: https://github.com/rm00cr/coqui-tts.

</details>

#### [HUG-VIS: A Multimodal Benchmark for Human-centered Understanding and Generation in Visual Intelligence](https://arxiv.org/abs/2608.26517) · [📄 Read](papers/2026/2608.26517.md)

**Fei Ma, Zebang Cheng, Minghui Li, Hongbo Xu et al.** · 2026-08-27

<details>
<summary>Abstract</summary>

Visual intelligence seeks to perceive, interpret, and synthesize the visual world and is central to modern computer vision. Human-centered visual intelligence is especially demanding because it studies people as expressive, socially situated subjects whose meaning is rarely conveyed by appearance alone. It couples vision with audio and language across four representative tasks: human emotion recognition, human video generation, human voice cloning, and human video matting. Yet existing resources remain task-specific, providing modalities and annotations for individual problems rather than a shared foundation coordinating understanding and generation. This limits multimodal signal use and broader research. We address this gap with HUG-VIS, a unified benchmark for Human-centered Understanding and Generation in Visual Intelligence. It contains 8,400 seated half-body videos of 30 professional actors, each performing the same 280 emotion-action-prompt assignments under a controlled Mandarin studio protocol, with synchronized video, audio, text, and alpha mattes. We evaluate diverse open- and closed-source models across the four tasks under a unified zero-shot protocol using automatic metrics, criterion-specific mean opinion scores, and multiple cross-task analyses. Results show that (i) linguistic content dominates current emotion recognition, while purely visual affect recognition is weakest; (ii) in video generation and voice cloning, automatic metrics and human judgment agree overall but differ in their top rankings, requiring joint reporting; (iii) boundary fidelity under motion is the main remaining obstacle for human matting; and (iv) task difficulty varies across emotions, models, and metrics, with notable cross-task correlations. The dataset and results are available at https://github.com/GML-MMGroup/HUG-VIS.

</details>

#### [CSAVocoder: A Causal Spatial Audio Vocoder Towards Real-Time Spatial Audio Generation](https://arxiv.org/abs/2608.25404) · [📄 Read](papers/2026/2608.25404.md)

**Zhiyuan Zhu, Han Wang, Wenxiang Guo, Yu Zhang et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Spatial audio vocoders are able to convert mel-spectrograms produced by generative models into spatial audio waveforms. Most neural vocoders are designed for monaural audio, and direct extensions to spatial audio can degrade spatial quality by ignoring inter-channel cues. We present CSAVocoder, a causal GAN-based spatial audio vocoder that jointly optimizes waveform fidelity and spatial rendering. Our framework introduces a Spatial Adaptor that fuses multi-channel mel-spectrograms with dynamic source-listener pose information, together with a spatial consistency discriminator that supervises inter-channel cues. To meet real-time requirements, we design a strictly causal, stateful generator that supports efficient streaming inference with constant memory overhead. Experiments on large-scale spatial audio datasets show that CSAVocoder improves spatial fidelity at competitive audio quality and real-time performance.

</details>

#### [InteractGesture: Progressive Chunk Guidance for Continuous Streaming Co-Speech Gesture Control](https://arxiv.org/abs/2608.25734) · [📄 Read](papers/2026/2608.25734.md)

**Ekkasit Pinyoanuntapong, Ajinkya Deogade, Paul Streli, Wenjing Zhang et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Co-speech gesture generation has made significant progress toward realistic full-body motion from speaker audio, yet existing models lack fine-grained spatial controllability of individual joints. To address this, we introduce \emph{InteractGesture}, a model-agnostic, inference-time method for spatially controllable gesture generation. \emph{InteractGesture} guides target latent estimates of a diffusion sampler through a differentiable RVQ-VAE decoder, backpropagating spatial control gradients to adjust motion latents during sampling. A primary challenge in streaming co-speech generation is chunk-wise dependency: standard sequential inference freezes prior chunks, preventing spatial constraints in future chunks from adjusting preceding trajectories and causing boundary inconsistencies. To overcome this limitation, we propose \emph{Progressive Chunk Guidance}, a chunk-window strategy that maintains an active set of editable chunk latents with staggered delays, enabling spatial constraints to propagate gradients backward across chunk boundaries during streaming generation. Experiments on the BEAT2 dataset show that \emph{InteractGesture} improves multi-joint spatial control while preserving overall gesture quality. Furthermore, our approach supports diverse applications, including sparse joint positioning, dense joint trajectory control, and directional pointing. Our project page is available at https://exitudio.github.io/interactgesture-page .

</details>

#### [OmniJudge or OmniBias? Diagnosing Multimodal Judges through Balanced, Decoupled Lenses](https://arxiv.org/abs/2608.24160) · [📄 Read](papers/2026/2608.24160.md)

**Guangzheng Hu, Ziyue Jiang, Weixu Qiao, Lixin Zhang et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

Multimodal understanding models that can jointly judge text-to-image (T2I), text-to-video (T2V) and text-to-speech (TTS) generation are increasingly used as "OmniJudges" for evaluation and automatic annotation. How reliably they understand what they score remains unclear, since existing benchmarks and training data tend to overemphasize positive examples and to conflate distinct failure modes, so a judge may score well without recognizing failures while its capability gaps stay hidden. Motivated by this, we introduce D3-Omni, a balanced and decoupled benchmark for diagnosing fine-grained multimodal understanding, covering 53 orthogonal binary dimensions (17/22/14) and 10,671 samples (3,526/1,998/5,147) across the three tasks. Rather than re-generating outputs, which may leak information across dimensions, we fix verified fully positive seeds and derive negatives through controlled prompt rewriting and atomic, dimension-isolating perturbations. The resulting D3 design is Dual-balanced, which helps alleviate negative-sample scarcity and per-dimension label imbalance; Decoupled, so that each error is attributable to a single capability; and Dynamic, steering construction toward under-represented regions of the label distribution as generative models improve.The suite reaches near 1:1 per-dimension parity and a uniform distribution over all total-score levels. Under this balanced view, even strong OmniJudges tend to struggle on modality-related dimensions, to confirm satisfied requirements far more reliably than they detect violated ones, and to treat nominally distinct attributes as largely a single decision, suggesting that aggregate accuracy may hide systematic blind spots that a balanced and decoupled lens can help expose and, in turn, address.

</details>

#### [FireRedAudio: A General-Purpose Audio Language Model with Decoupled Continuous Representations for Understanding and Generation](https://arxiv.org/abs/2608.24168) · [📄 Read](papers/2026/2608.24168.md)

**Junjie Li, Xuelong Geng, Kun Xie, Feiyu Shen et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

A unified audio model must recognize and understand linguistic, paralinguistic, and environmental information while supporting speech synthesis and editing. A key challenge is representation: understanding favors compact features suited to long-context modeling, whereas speech generation requires reconstructible features that preserve fine-grained acoustic detail. We introduce FireRedAudio, a general-purpose audio language model with a shared 9B-parameter LLM. To the best of our knowledge, it is the first publicly disclosed unified audio-language model to provide separate continuous input representations for understanding and generation within a single trainable autoregressive LLM. Audio to be recognized or analyzed is processed by a dedicated Audio Encoder, while speech inputs for generation use a RedAE-based pathway. The LLM directly generates text or conditions a flow-matching DiT to produce continuous acoustic latents. Through progressive multitask training, FireRedAudio supports ASR and audio understanding, with the latter extending to recordings of up to one hour, as well as zero-shot TTS, Instruct TTS, and semantic and acoustic speech editing. Its structured organization of long-form audio achieves second-level timestamp accuracy. Across comprehensive evaluations, FireRedAudio achieves competitive or leading performance in audio understanding and multilingual ASR, strong content accuracy and speaker preservation in zero-shot TTS, leading instruction following in Instruct TTS, and substantial improvements over Ming-UniAudio-Edit in both semantic and acoustic speech editing. These results demonstrate the viability of decoupled continuous input representations for unifying audio understanding and continuous-latent speech generation in a model of moderate scale. Our code is available at https://github.com/FireRedTeam/FireRedAudio.

</details>

#### [Speech-to-SOAP: End-to-End Summarization of Medical Dialogues: KIT@BeTraC 2026](https://arxiv.org/abs/2608.24327) · [📄 Read](papers/2026/2608.24327.md)

**Enes Yavuz Ugan, Fabian Retkowski, Yuka Ko, Thai-Binh Nguyen et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

With the advent of Large Language Models and its instruction following capabilities a promising application is the task of summarization. Within this domain of task the extractive sub-task of clinical protocolling has emerged as a topic of particular interest as it can significantly reduce the downtime and protocolling burden of health-care workers thus enabling them to focus on their core work helping humans. A further step towards automation is the direct generation of clinical notes from speech without intermediate transcripts, reducing processing time while preserving information such as coughing or other paralinguistic cues that may be lost in transcript-based systems. To this end, we present KIT's submission to this years BeTraC challenge in the lightweight track. Our main contribution is a scalable data augmentation pipeline that unifies heterogeneous medical dialogue datasets through synthetic speech generation and automatically generated SOAP supervision, enabling robust adaptation of a speech foundation model for end-to-end speech-to-SOAP generation.

</details>

#### [Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight](https://arxiv.org/abs/2608.24314) · [📄 Read](papers/2026/2608.24314.md)

**Anupam Purwar, Shashank Singh, Kritika Srivastava** · 2026-08-25

<details>
<summary>Abstract</summary>

Evaluating conversational voice agents at scale re- quires reliable assessment methods that capture both observ- able interaction quality and the contextual judgment typically provided by human evaluators. We investigate LLM-as-a-Judge evaluation by comparing human judgments with GPT-4.1 and GPT-5 on telecom and retail voice-agent conversations, across conversational quality and safety dimensions. The same interac- tions are scored under three evaluation configurations, p0, p1, and p2, to test whether automated judgments are sensitive to the evaluation setup and whether observed patterns generalize across configurations and judge models. Beyond aggregate agreement, we examine metric-level correlations, evaluator consistency, and systematic human-LLM disagreement to identify which conver- sational attributes can be judged reliably by automation and which remain sensitive to interpretation and context. Effective voice-agent evaluation is also shaped by pipeline-level factors such as speech generation, streaming, and error propagation across ASR, reasoning, and tool-calling stages, motivating our focus on comparing how human and LLM judges score the same interactions end to end. Our results show that LLM- based evaluation can serve as an effective component of large- scale voice-agent assessment, but that its reliability is metric- and configuration-dependent rather than uniform. This pro- vides an empirical framework for identifying which metrics suit automated evaluation and supports hybrid pipelines in which LLM judges handle scalable assessment while human evaluators remain engaged for metrics that demand contextual interpretation and higher-confidence judgment.

</details>

#### [EmoTra-TTS: Smooth Intra-Utterance Emotion Transitions for Speech Synthesis](https://arxiv.org/abs/2608.23791) · [📄 Read](papers/2026/2608.23791.md)

**Tianchi Liu, Zeyang Song, Tianrui Wang, Zhipeng Li et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

Psychological research on emotion dynamics has established that human affect is a continuous, evolving process: emotions rise, decay, and transition within seconds. Current emotional text-to-speech (TTS) systems, however, condition on a single discrete label or static embedding per utterance, fundamentally misaligning with the temporal nature of affect. While recent LLM-based TTS systems may implicitly vary prosody through text understanding, such variation is neither explicitly controllable nor precise enough for targeted intra-utterance transitions. We address three challenges: (1) a multi-pass flow blending pipeline synthesizes frame-aligned transition audio, circumventing the scarcity of natural intra-utterance transitions; (2) dual-stage Valence-Arousal-Dominance (VAD) conditioning guides prosodic planning in the LLM and acoustic realization in the flow decoder via frame-level VAD embeddings; (3) direction-magnitude decoupled injection structurally separates emotion direction from injection magnitude, preventing content degradation. EmoTra-TTS adds only +0.43% parameters with no latency overhead, achieves 30%-87% relative improvement on emotion transition quality, corroborated by 64.4%-79.5% overall win rates in pairwise preference tests against four SOTA baselines and two commercial systems.

</details>

</details>
<!-- PAPERS_TABLE_END -->
