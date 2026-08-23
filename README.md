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

_Showing the last 30 days (59 of 3354 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [Tracking the Trend in How Speech Synthesizers Deceive People](https://arxiv.org/abs/2608.19959) · [📄 Read](papers/2026/2608.19959.md)

**Milan Šalko, Anton Firc, Kamil Malinka, Vojtěch Staněk et al.** · 2026-08-20

<details>
<summary>Abstract</summary>

Advances in speech synthesis have made deepfake audio highly realistic. Earlier studies reported 70-80% human detection accuracy, but relied primarily on older synthesizers. We compare human detection for three selected voice synthesis tools released in 2019, 2022, and 2024 with 82 IT professionals, and benchmark humans against six pretrained detectors on the same material. For fully synthetic speech (full spoofs), the F1 score drops from about 90% for RTVC and YourTTS to 48% for ElevenLabs, although listeners were explicitly warned that deepfakes were present. For partial spoofing, where only one sentence of an utterance is altered, strict accuracy falls to 9%, and listeners classify the synthetic sentence as bona fide 77% of the time. Humans and detectors fail in complementary ways, and neither reliably localizes short manipulations. Additionally, listeners increasingly mislabel bona fide speech as fake, eroding trust in unmanipulated audio. These findings show that human perception alone is unreliable for the selected modern and partial-spoof conditions and motivate procedural verification, provenance, watermarking, and segment-level detection.

</details>

#### [Does Listening Matter? Backchanneling and Nodding in AI Clone](https://arxiv.org/abs/2608.19527) · [📄 Read](papers/2026/2608.19527.md)

**Koji Inoue, Kazushi Kato, Tatsuya Kawahara, Shunichi Kasahara** · 2026-08-20

<details>
<summary>Abstract</summary>

AI clones that imitate a specific person typically reproduce what the person says and how they sound, but not how they listen. We investigate whether adding multimodal listening behaviors gives such a clone more presence and authenticity. We integrated verbal backchannels and head nodding, driven by real-time prediction models, into an AI clone equipped with voice cloning and LLM-based responses. In a within-subjects study (N=35), adding these behaviors significantly improved the perceived attentiveness of the avatar, the sense of talking with the real person, and the feeling of co-presence. These results indicate that AI clone fidelity should extend beyond voice and response content to include interactive listening behavior.

</details>

#### [X2Streaming-TTS: Causal Token-Level Text-to-Speech from Streaming Text with Speech-State Inheritance](https://arxiv.org/abs/2608.18661) · [📄 Read](papers/2026/2608.18661.md)

**Rime Wen, Zehan Liu, Shawn Qin, Lights Shi et al.** · 2026-08-19

<details>
<summary>Abstract</summary>

Streaming text-to-speech is essential for low-latency spoken dialogue systems, yet many systems wait for sentence-level text and are therefore only pseudo-streaming. True token-level synthesis must generate speech from uncertain prefixes while maintaining perceptual continuity over an unbounded stream with bounded context. We present X2Streaming-TTS, a causal TTS framework that consumes asynchronously arriving text tokens and emits speech without accessing future input. To handle uncertain prefixes, we introduce causal commitment, which keeps ambiguous expressions provisional through uncertainty-aware buffering and performs capacity-adaptive, punctuation-aware segmentation. To preserve acoustic continuity, we further introduce causal speech-state inheritance, which carries the complete Code2Wav state and selected historical Talker states across segment boundaries. Together with an attention prior constraint, it blocks access to future positions while retaining bounded acoustic context. Experiments show that X2Streaming-TTS outperforms existing pseudo-streaming models on most subjective and objective metrics. Further analysis shows that causal commitment stabilizes online segmentation and reduces failures caused by insufficient context, while speech-state inheritance improves boundary continuity without degrading naturalness or speaker identity. X2Streaming-TTS thus achieves strict token-level synthesis with quality comparable to the evaluated offline baselines, a median time to first audio token (TTFT) of 15.8 ms for a single request, and a median TTFT of 260.8 ms at 128 concurrent requests. Our implementation is publicly available at https://github.com/X-Square-Robot/X2Streaming-TTS .

</details>

#### [Aslema at NADI 2026: Augmentation through Fewshot for SLU](https://arxiv.org/abs/2608.18689) · [📄 Read](papers/2026/2608.18689.md)

**Tajwaar Shafiq, Hunzalah Hassan Bhatti, Shammur Absar Chowdhury, Firoj Alam** · 2026-08-19

<details>
<summary>Abstract</summary>

We present Aslema, our system for NADI 2026 Shared Task 5, which consists of two subtasks: intent recognition and slot filling. We evaluate four omni LLMs in a zero-shot setting and compare them with fine-tuned models. Our results show that fine-tuning consistently outperforms zero-shot inference. We further explore synthetic data augmentation by using an LLM to generate culturally grounded Tunisian Derja utterances, followed by voice cloning to generate synthetic speech. Incorporating this synthetic data improves performance on both tasks. Our final submitted system, based on Qwen3-Omni-30B and trained with a mixture of original and synthetic data, achieves 86.8% intent accuracy and 34.7 WER on the devtest split. On the official test set it ranks 1st in slot filling (59.5 CoER) and 4th among 8 teams in intent recognition (66.1% accuracy). We release our experimental scripts and will soon share the synthetic dataset to support further research in this area.

</details>

#### [FireRedTTS3: Unified Speech Generation and Editing with Semantically Enriched Speech Representations](https://arxiv.org/abs/2608.17492) · [📄 Read](papers/2026/2608.17492.md)

**Feiyu Shen, Kun Xie, Yichen Wu, Ziqi Dai et al.** · 2026-08-18

<details>
<summary>Abstract</summary>

Recent continuous autoregressive TTS models operate directly on continuous speech representations, preserving rich acoustic details while leveraging the instruction-following capabilities of text LLMs. This paradigm opens new possibilities for voice cloning, instruction-controlled voice design, and speech editing, but remains susceptible to error accumulation during autoregressive generation. Existing solutions often require additional semantic modules, multi-stage tokenizer training pipelines, or complex autoregressive architectures. In this work, we propose FireRedTTS3, a simple yet effective speech generation and editing framework that mitigates error accumulation at the representation level. Specifically, we leverage a frozen Audio Encoder trained on diverse speech understanding tasks as a semantic teacher to regularize the audio feature space. This improves text-speech alignment and stabilizes autoregressive generation while keeping the overall system simple. FireRedTTS3 provides two variants: FireRedTTS3-Base for multilingual and multi-dialect zero-shot voice cloning, and FireRedTTS3-Instruct for unified voice cloning, instruction-controlled voice design, and speech editing. Experiments show that FireRedTTS3-Base achieves the best average speech intelligibility and speaker similarity among compared systems on Seed-TTS-Eval and MiniMax-MLS-Test, while FireRedTTS3-Instruct outperforms competing systems on InstructTTSEval and Ming-Freeform-Audio-Edit. These results demonstrate that semantically enriched continuous speech representations, combined with a simple architecture, enable stable, controllable, and high-fidelity speech generation and editing. Code and models are available at https://github.com/FireRedTeam/FireRedTTS3.

</details>

#### [Speaker-Normalized Semantic Speech Tokens via Iterative S2U-T2U Refinement](https://arxiv.org/abs/2608.16235) · [📄 Read](papers/2026/2608.16235.md)

**Hanlin Zhang, Daxin Tan, Dehua Tao, Chengxi Deng et al.** · 2026-08-17

<details>
<summary>Abstract</summary>

Semantic speech tokens should preserve linguistic content while suppressing speaker- and duration-dependent variation inherited from acoustic inputs. We propose Iterative Semantic Token Purification (ISTP), an alternating speech-to-unit (S2U) and text-to-unit (T2U) training procedure guided by text predictability. Starting from an initial S2U tokenizer, each iteration trains a T2U model on its deduplicated token sequences. The decoded T2U predictions then serve as connectionist temporal classification targets for a newly initialized S2U model, whose outputs supervise the next T2U model. This cycle progressively aligns the two token generators and biases the token space toward information recoverable from text. Experiments on Mandarin and English show substantially improved S2U--T2U agreement. Independently trained de-tokenizers further show that the refined S2U and T2U tokens retain sufficient content for high-intelligibility voice conversion and text-to-speech synthesis. In voice conversion, the generated speaking rate follows the reference more closely. The refined tokens also exhibit substantially improved cross-speaker consistency and reduced probe-recoverable speaker information.

</details>

#### [DuplexGen: Decoupling Content, Timing, and Acoustics for Synthetic Dialogue Speech](https://arxiv.org/abs/2608.16053) · [📄 Read](papers/2026/2608.16053.md)

**Pengcheng Wang, Sheng Li, Jiyi Li, Takahiro Shinozaki** · 2026-08-17

<details>
<summary>Abstract</summary>

Synthetic conversational speech has become an important resource for developing and evaluating conversational speech systems. However, existing dialogue synthesis pipelines typically generate dialogue content first and then insert interruptions, overlap, and backchannels using handcrafted markers or timing rules, making conversational timing prescribed rather than interaction-driven. We present DuplexGen, a dialogue synthesis framework that explicitly decouples content, timing, and acoustics. An LLM first generates the dialogue script, and then two full-duplex conversational models perform the script while listening to each other in real time. This allows conversational timing to emerge naturally while preserving the scripted content. Finally, a high-fidelity text-to-speech model re-renders the interaction without altering its timing. As a demonstration of the proposed framework, we construct a patient--clinician conversational speech corpus with construction-time annotations, including word timestamps, speaker activity, overlap regions, and interaction events. Experimental results show that the proposed framework produces conversational dynamics closer to real dialogue than conventional stitching-based synthesis.

</details>

#### [Iterative Self-Learning for Expressive Text-to-Speech Synthesis](https://arxiv.org/abs/2608.15910) · [📄 Read](papers/2026/2608.15910.md)

**Nicholas Sanders, Gustav Eje Henter, Simon King, Korin Richmond** · 2026-08-16

<details>
<summary>Abstract</summary>

Expressive text-to-speech (TTS) systems that use explicit conditioning labels provide direct and interpretable control over expressive attributes, in contrast to reference-based or prompting-based approaches, but require labeled data. Obtaining these labels at scale is costly and time-consuming, yet no prior semi-supervised framework addresses this specific bottleneck. Existing semi-supervised TTS methods instead target scarcity of paired speech-text data or transcriptions. To address the scarcity of expressive labels, we propose an Iterative Self-Learning (ISL) framework for expressive TTS, built on Invert-Classify, a classifier-free method that recovers discrete expressive labels by inverting a frozen generative model. The framework iteratively pseudo-labels unlabeled speech using the current model, retrains on the combined labeled and pseudo-labeled data, and repeats, progressively refining label quality and synthesis. We validate on two expressive tasks, word-level prominence and utterance-level emotion, across multiple low-resource data splits. We find that iterative refinement can improve pseudo-label accuracy over single-pass baselines. Furthermore, we observe that these improvements in pseudo-labeling of expressivity translate to gains in expressive label adherence and synthesis quality, confirmed by objective metrics and human listening tests. In the most data-scarce conditions, ISL-trained models outperform single-pass pseudo-labeling and further approach fully supervised performance, demonstrating that gradient-based ISL is an effective solution to expressive label scarcity in low-resource TTS.

</details>

#### [Adding Voice Cloning to Text-to-Audio-Video Models with a Single Zero-Initialised Layer](https://arxiv.org/abs/2608.15690) · [📄 Read](papers/2026/2608.15690.md)

**Ivan Mikheev, Viacheslav Vasilev, Anna Dmitrienko, Alexey Letunovskiy et al.** · 2026-08-16

<details>
<summary>Abstract</summary>

Text-to-audio-video (T2AV) generation models produce a video and its soundtrack from a textual description, but offer no control over whose voice speaks in the output. We show that a base T2AV model can be turned into a voice-cloning model by adding a single zero-initialized linear layer on top of its audio backbone, fine-tuning for a comparatively short training schedule, and conditioning on a short reference recording at inference time. The reference is injected through two complementary signals: its diffusion latents are prepended to the audio stream, and a global speaker embedding modulates token of the target audio. On a benchmark of 674 speaker-text pairs spanning 30 speakers we compare against five strong voice-cloning text-to-speech baselines: our enhanced 5B model attains the highest speaker-encoder cosine similarity (SECS) across three independent verification networks (ECAPA-TDNN, WavLM-SV, Resemblyzer), statistically significantly outperforming every baseline. A side product of the architecture is that the audio path can be evaluated without the video path at inference time, yielding a ~30x speed-up over the full audio-video diffusion loop while preserving the voice-cloning behaviour.

</details>

#### [A survey of AI-generated voices and their detection](https://arxiv.org/abs/2608.15411) · [📄 Read](papers/2026/2608.15411.md)

**Chengzhe Sun, Tianle Yang, Siwei Lyu** · 2026-08-15

<details>
<summary>Abstract</summary>

The ability of artificial intelligence (AI) models to generate highly realistic human voices has advanced rapidly. These technologies power accessibility tools, virtual assistants and creative applications, but they also enable harmful uses, including impersonation, fraud and disinformation. Recent incidents of voice cloning scams targeting businesses and political leaders underscore the urgent need for robust safeguards. Unlike image and video deepfakes, the detection of synthetic voices poses unique challenges due to the complexity of phonetics, prosody and auditory perception. This survey offers a comprehensive overview of AI voice generation and detection methods, encompassing both the technical foundations and the latest state-of-the-art advances. This study also identifies key open challenges, benchmark resources and future directions to make this survey useful for future researchers.

</details>

#### [Content Based Video Narration of Gameplay with Vision Language Models](https://arxiv.org/abs/2608.14016) · [📄 Read](papers/2026/2608.14016.md)

**Mathew Varghese** · 2026-08-14

<details>
<summary>Abstract</summary>

Live game commentary is scarce: it exists for professional esports broadcasts and almost nowhere else. We present a content-based video narration system that produces spoken, esports-style commentary for arbitrary gameplay recordings using a general-purpose vision-language model (VLM) and a text-to-speech back end, with no game-specific instrumentation, no engine telemetry, and no task-specific training. Three mechanisms carry the system. Temporal mosaic packing arranges nine uniformly sampled frames into a single 3x3 image, letting an image-native VLM reason about motion while consuming one image payload per segment instead of nine. Context-conditioned prompting replays the K most recent narrations as assistant-role history, suppressing the repetition that dominates per-segment captioning of static scenes. Duration-conditioned generation and elastic alignment constrain narration length in the prompt, then time-scale or symmetrically pad the synthesized audio so each utterance fills its segment slot exactly, giving frame-accurate muxing without a forced aligner. The implementation supports either cloud TTS or a 6-bit quantized 4B-parameter on-device TTS model on Apple silicon, making the speech stage fully local. We report a qualitative case study on real-time strategy footage, a cost model showing the mosaic reduces per-minute image payloads by 9x, and a candid account of observed failure modes - hallucinated game state, resolution loss from mosaicking, and prosody artifacts from time-scaling. We release the system as a reproducible baseline, with an evaluation protocol for the quantitative study a full version will report.

</details>

#### [S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling](https://arxiv.org/abs/2608.14029) · [📄 Read](papers/2026/2608.14029.md)

**Xueqi Wang, Zhigang Wang, Runqing Zhang, Zhenqi Jia et al.** · 2026-08-14

<details>
<summary>Abstract</summary>

Multimodal dialogue retrieval aims to retrieve dialogues from multimodal dialogue banks that are similar to a target dialogue in terms of both textual semantics and acoustic conversational styles. Such dialogue-level retrieval is crucial for many dialogue-related tasks, including Emotion Recognition in Conversation, Spoken Dialogue Systems, and Conversational Speech Synthesis, where external dialogue examples can provide valuable semantic and stylistic references. However, existing retrieval methods are still largely limited to utterance-level or unimodal matching, and often fail to capture the global semantic coherence and stylistic consistency of an entire dialogue. To address this gap, we propose S2Dialog, a unified framework for dialogue-level semantic-style retrieval from multimodal dialogue banks. Specifically, S2Dialog consists of a Dialogue-level Textual Retriever and a Dialogue-level Acoustic Retriever, which encode the textual and acoustic modalities of a dialogue into dialogue-level representations, respectively. To further enhance multimodal retrieval, we introduce Dialogue-level Textual-Acoustic Contrastive Learning, which aligns semantically and stylistically similar dialogues while distinguishing unrelated ones. Extensive experiments on the multimodal dialogue dataset DailyTalk demonstrate that S2Dialog achieves outstanding retrieval performance.

</details>

#### [FastThaiG2P: Lightning-fast Thai Grapheme-to-phoneme Conversion for Voice Agent Pipelines](https://arxiv.org/abs/2608.12814) · [📄 Read](papers/2026/2608.12814.md)

**Charin Polpanumas** · 2026-08-13

<details>
<summary>Abstract</summary>

FastThaiG2P provides sub-millisecond Thai grapheme-to-phoneme conversion for text-to-speech pipelines (International Phonetic Alphabet and Kokoro-TTS conventions) using a PyThaiNLP-tokenized, extensible dictionary and normalization rules for common Central Thai speech. The approach achieves an average latency of 0.15 ms per utterance on a benchmark of 27,242 synthetically generated utterances, of which 30\% is spent on tokenization, 12\% on normalization, and 58\% on out-of-vocabulary fallbacks (0.5\% OOV rate). To demonstrate its effectiveness, we used FastThaiG2P to phonemize Som-TTS, an open dataset containing 20 hours of grapheme-and-audio pairs, then trained an 82M-parameter StyleTTS 2 model based on a Kokoro-TTS recipe. The resulting model vocalizes intelligible Thai speech suitable for prototyping and development at 0.25 real-time factor (4x real-time) with ONNX inference on CPU.

</details>

#### [VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents](https://arxiv.org/abs/2608.13831) · [📄 Read](papers/2026/2608.13831.md)

**Edresson Casanova, Jaehyeon Kim, Mariana Graterol Fuenmayor, Shehzeen Hussain et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Spoken dialogue is a natural form of human--computer interaction, yet most speech language models remain limited to turn-based operation and lack real-time adaptability, such as user barge-in. Recent duplex speech-to-speech and speech-to-text models reduce latency by replacing multi-stage pipelines, but often compromise speech quality because accurate ASR, interruption handling, and high-fidelity synthesis must be optimized jointly. We propose VoiceChat-TTS, a low-latency, continuous, and streamable text-to-speech model for interactive agents. VoiceChat-TTS is driven directly by LLM text-token streams, supports explicit interruption via control tokens, and produces silence when no textual input is available. The model enables always-on, responsive speech generation while preserving modularity and high speech quality, and it supports mid-utterance interruptions without resetting the KV cache.

</details>

#### [MiDashengLM-Gen: Unified Audio Scene Generation via LLM-Driven Autoregressive Flow Matching](https://arxiv.org/abs/2608.11804) · [📄 Read](papers/2026/2608.11804.md)

**Xingwei Sun, Heinrich Dinkel, Gang Li, Jiahao Mei et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Generating coherent audio scenes that simultaneously blend speech, music, and sound effects remains a significant challenge. Current approaches typically rely on a disjointed pipeline where a frozen, decoupled text encoder feeds a separate audio decoder, limiting cross-modal optimization and leading to poor speech intelligibility. To overcome these limitations, we introduce MiDashengLM-Gen, an end-to-end framework that couples a pre-trained Large Language Model (LLM) with per-token conditional flow matching for autoregressive, variable-length mixed-audio scene generation. MiDashengLM-Gen represents a first approach for general text-to-audio generation with one end-to-end trained model. Empirical evaluations demonstrate that MiDashengLM-Gen drastically improves speech intelligibility over existing unified models. On the Seed-TTS benchmark, English Word Error Rate (WER) drops from 12.15% to 2.79%, approaching the performance of dedicated Text-to-Speech (TTS) systems (1.24%). Furthermore, the framework extends effectively to multilingual settings, yielding highly competitive multilingual WERs compared to existing baselines. Lastly, the model maintains competitive mixed-audio generation quality on the MECAT benchmark. Code and checkpoints are available at https://github.com/xiaomi-research/midashenglm-gen and https://huggingface.co/mispeech/midashenglm-gen, and the demo page is available at https://xingws.github.io/midashenglm-gen-demo/.

</details>

#### [Confucius4-TTS: Transcript-Free Cross-Lingual Zero-Shot TTS with a Learnable Speaker Encoder](https://arxiv.org/abs/2608.11650) · [📄 Read](papers/2026/2608.11650.md)

**Huaxuan Wang, Huimin Wang, Ruiyu Zhang, Yingjie Li et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Recent advances in zero-shot text-to-speech (TTS) have substantially improved speech quality and voice cloning fidelity. However, many zero-shot TTS systems still depend on audio prompt transcripts at inference time. This dependency limits cross-lingual voice cloning, since in-the-wild reference audio is often untranscribed. In this technical report, we present Confucius4-TTS, a multilingual zero-shot TTS system that supports 14 languages and performs both intra-lingual and cross-lingual reference cloning without requiring transcripts of audio prompts. Confucius4-TTS follows a two-stage architecture, consisting of text-to-semantic (T2S) and semantic-to-acoustic (S2A) modules. The LLM-based T2S module uses a learnable speaker encoder to extract timbre features from self-supervised speech representations, and the conditional flow-matching S2A module converts the predicted semantic tokens into mel-spectrograms. The same model also supports continuation cloning when a reference transcript is available. Confucius4-TTS is trained on large-scale multilingual speech data. It achieves high intelligibility and speaker similarity on public benchmarks. On the CV3-Eval cross-lingual benchmark, Confucius4-TTS obtains an average WER of 3.73% across six directions. On our internal cross-lingual set, it achieves the best average overall rank in human evaluation among recent open-source and commercial systems. We release code, model checkpoints, and demos at https://github.com/netease-youdao/Confucius4-TTS.

</details>

#### [Luna-TTS Family Technical Report](https://arxiv.org/abs/2608.11593) · [📄 Read](papers/2026/2608.11593.md)

**Feng Yin, Shuai Shi, Junjie Zheng, Kechenying Zhou et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Modern text-to-speech (TTS) is dominated by autoregressive (AR) codec language models, whose left-to-right decoding brings latency that grows with utterance length, error accumulation along the committed prefix, and an artificial generation order imposed on the Residual Vector Quantization (RVQ) token grid. We propose Luna-TTS Family, diffusion-language-model-based TTS systems pretrained on 1 million hours of speech across Chinese, English, Japanese, and Korean. The family is built by progressive adaptation of a pretrained AR text LLM, from causal to bidirectional and finally to block-causal attention, and comprises two variants sharing a single tokenizer, data pipeline, and 0.6B backbone lineage. Luna-TTS is fully non-autoregressive: it generates the entire RVQ token grid in a fixed number of parallel refinement steps, with zero-shot voice cloning and speech editing arising natively as infilling. Luna-TTS Realtime, derived by continual training, is autoregressive over blocks of 32 codec frames (1.28s) while denoising each block in parallel; it supports KV-cached blockwise generation and incremental audio delivery, achieving an end-to-end RTF of 0.0240 and 41.6 ms local first-block latency under the warmed serving protocol. An annealed fine-tuning stage adds explicit control over emotion and non-verbal vocalizations (NVVs), and a reinforcement-learning stage applies GRPO with policy ratios computed over the realized denoising trajectory. On Seed-TTS-Eval, Luna-TTS achieves the best results on all four metrics among compared open-source and commercial systems (0.73 CER / 79.7 SIM on test-zh, 1.49 WER / 76.8 SIM on test-en); on the harder in-the-wild CV3-Eval, it posts the lowest Mandarin and English error rates in our comparison. Against leading commercial systems, it achieves the best results on most objective, model-based, and human-rated metrics for NVV and emotion control.

</details>

#### [CookVoice: Unified Framework for Style Controllable Multi-Modal Human Voice Generation](https://arxiv.org/abs/2608.11590) · [📄 Read](papers/2026/2608.11590.md)

**Haowei Lou, Hye-Young Paik, Dai Jia, Kai Li et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Human voice generation has made rapid progress in speech generation, singing voice generation, voice cloning, and voice editing. However, most existing systems are designed for specific tasks and often rely on task-dependent architectures, control signals, or autoregressive decoding, limiting fine-grained controllability and inference efficiency. In this paper, we propose CookVoice, a unified framework for multimodal, multi-style, and multi-task human voice generation. CookVoice decomposes the human voice into three key factors: content, prosody, and style, enabling both speech and singing voice generation within a unified model. To achieve precise and flexible controllability, we design a flexible alignment strategy that maps text, style, and prosody control signals onto the frame-level of spectrogram. This design allows CookVoice to support a wide range of tasks, including text-to-speech, text-to-singing voice, style-controllable generation, voice mimicry, voice conversion, and voice editing. Experimental results show that CookVoice achieves generation quality comparable to existing Text-to-Speech and text-to-singing voice baselines, while providing stronger style and prosody controllability. Moreover, CookVoice achieves comparable performance to large-scale baselines with only 43.51 million parameters and efficient inference using as few as 4 ODE steps, making it a practical solution for real-world human voice generation applications. Demo page is available at https://haoweilou.github.io/CookVoice/.

</details>

#### [VoiceDesigner: Text-to-Voice Generation and Editing via Unified Diffusion Modeling and Data Augmentation](https://arxiv.org/abs/2608.13613) · [📄 Read](papers/2026/2608.13613.md)

**Jiarui Hai, Karan Thakkar, Ke Chen, Yunyun Wang et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Recent breakthroughs in generative models have made text-to-voice generation (TTV) possible, enabling the synthesis of speech directly from textual voice descriptions. However, existing systems face two key challenges. First, they struggle to generate a diverse range of voices, spanning real-world human speakers and fictional characters. Second, they lack robust and flexible voice editing capabilities, such as voice cloning and the ability to modify attributes like emotion and tone. In this paper, we propose VoiceDesigner, a unified framework for text-to-voice generation and editing that supports diverse and controllable voice design. To tackle the above challenges, we propose solutions from two perspectives. First, we develop a hybrid data pipeline that leverages digital signal processing techniques and speech generation models to construct a diverse voice dataset covering both real-world and fictional voices. Second, we introduce a diffusion transformer with architectural improvements to better handle complex conditioning and enhance multi-task performance, enabling unified voice generation and editing. Through subjective and objective evaluations, VoiceDesigner achieves superior prompt alignment with both voice descriptions and editing instructions, while maintaining competitive perceptual quality and voice usability compared to state-of-the-art TTV models.

</details>

#### [Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions](https://arxiv.org/abs/2608.09930) · [📄 Read](papers/2026/2608.09930.md)

**Oluwanifemi Bamgbose, Simon Rosen, Jash Shah, Lindsay Devon Brin et al.** · 2026-08-10

<details>
<summary>Abstract</summary>

Automated Text-to-Speech (TTS) evaluation methods (Mean Opinion Score (MOS) predictors and Audio Large Language Models (Audio-LLM) judges) are expected to reflect human perception, yet it is unclear how well they capture the distinct aspects of speech that listeners actually perceive. We deconstruct "naturalness" into a linguistically grounded annotation schema spanning 10 distinct perceptual dimensions, and use it to construct the first dimension-level meta-evaluation benchmark for TTS, comprising 860 utterances annotated by trained linguist raters. Results from benchmarking four MOS predictors and four Audio-LLM judges reveal that MOS predictors collapse onto acoustic signal quality, while Audio-LLM judges show selective, prompt-dependent detection that does not generalise across all dimensions. Neither class reliably captures a breadth of linguistically structured speech errors. Our dataset, annotation schema, and evaluation code are publicly released to support more targeted and interpretable TTS evaluation.

</details>

#### [MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection](https://arxiv.org/abs/2608.09593) · [📄 Read](papers/2026/2608.09593.md)

**Yanqiu Li, Yang Xiao, Jisheng Bai, Bin Chen et al.** · 2026-08-10

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis and audio generation have made high-fidelity acoustic forgery low-cost and difficult to attribute, enabling a realistic attack scenario in which speech and background audio are independently manipulated over otherwise authentic video. Yet existing research either focuses on visual manipulation, addresses speech detection in isolation, or conflates speech and non-speech audio as a single undifferentiated audio stream, overlooking the distinct forensic challenges posed by background audio. This conflation is consequential: the two acoustic components arise from fundamentally different generative mechanisms, exhibit distinct artifact profiles, and pose different challenges to detection systems. We introduce MADBench, the first benchmark that treats speech and environmental audio as distinct acoustic components, enabling component-aware evaluation of audio deepfake detection across independently manipulated forgery sources. We benchmark representative state-of-the-art detectors and multimodal large language models under a unified protocol. Our experiments reveal that environmental audio manipulation is more detectable than synthetic speech across general-purpose encoders, while existing pretrained detectors fail on both acoustic components, and manipulated environmental audio asymmetrically degrades speech deepfake detection, findings entirely invisible under the single-label paradigm of prior benchmarks. MADBench establishes a rigorous foundation for future research into robust, component-aware audio deepfake detection.

</details>

#### [CuteTTS: Efficient and High-Quality Speech Synthesis via Autoregressive Modeling of Continuous Latents](https://arxiv.org/abs/2608.08638) · [📄 Read](papers/2026/2608.08638.md)

**Yuqian Zhang, Yao Shi, Kexin Huang, Botian Jiang et al.** · 2026-08-09

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) now supports interactive assistants, personalized media, and accessibility tools. All TTS systems require faithful linguistic rendering, consistent speaker identity, and low-latency response. Yet compact streaming systems must preserve sufficient acoustic detail in a predictable low-rate latent sequence, while iterative diffusion sampling and classifier-free guidance multiply inference cost at every autoregressive step. To strike a balance between high-fidelity synthesis and low-latency inference, we present CuteTTS, a compact continuous-autoregressive TTS system. It combines semantically aligned causal VAE latents with patch-level autoregression, explicit speaker conditioning, and a bidirectional flow-matching head. We further introduce guidance-step distillation, which absorbs classifier-free guidance and multiple solver steps into a single interval-conditioned student. Evaluations on LibriSpeech and Seed-TTS-Eval demonstrate competitive intelligibility and speaker similarity in zero-shot voice cloning, while distillation lowers first-audio latency by 23.3% and real-time factor by 40.8% relative to the base model with comparable objective and subjective quality. These results provide a practical path toward continuous-autoregressive TTS that reconciles high-fidelity generation with the latency demands of real-time interaction.

</details>

#### [CtrlSpeech: Coarse-to-Fine Control for Expressive Speech Synthesis](https://arxiv.org/abs/2608.08362) · [📄 Read](papers/2026/2608.08362.md)

**Zhisheng Zheng, Xiaohang Sun, Zhu Liu, Caren Chen et al.** · 2026-08-08

<details>
<summary>Abstract</summary>

Recent Text-To-Speech (TTS) systems have achieved strong naturalness and zero-shot voice cloning performance, but fine-grained control of expressive speech at the word or phoneme level remains challenging. We propose CtrlSpeech, a controllable, expressive TTS framework with coarse-to-fine control. Built on the DiTAR architecture, CtrlSpeech combines global speaker conditioning with phone-aligned pitch, loudness, and duration signals, enabling localized prosodic control while preserving the target speaker's timbre. This design allows users to adjust expressive attributes at a fine temporal granularity, making speech refinement more flexible and controllable. Experimental results show that CtrlSpeech achieves competitive zero-shot TTS performance and improves controllability over expressive attributes, demonstrating its effectiveness for flexible and practical expressive speech synthesis.

</details>

#### [ReLMCodec: Designing Predictable Speech Tokens from Pre-Quantization Phoneme Structure](https://arxiv.org/abs/2608.08286) · [📄 Read](papers/2026/2608.08286.md)

**Zixiang Wan, Xusheng Yang, Zheng Wang, Peiji Yang** · 2026-08-08

<details>
<summary>Abstract</summary>

Neural speech codecs face a fundamental tension in the language-model era: tokens that support high-fidelity reconstruction are not necessarily easy for autoregressive models to predict. Our controlled analysis of diverse codec and self-supervised speech representations shows that clearer phoneme structure before discrete code assignment is consistently associated with easier autoregressive token prediction. Yet phoneme structure alone is insufficient for high-fidelity reconstruction, which also requires reconstruction-relevant acoustic detail. Guided by this observation, we introduce ReLMCodec, a low-bitrate single-codebook speech codec built upon a preserve--control--refine principle: it preserves the linguistic organization of frozen self-supervised learning (SSL) features at the quantizer input, controls reconstruction-driven drift through Pre-quantization Anchor-Preserving Adaptation (PAPA), and refines the quantized latent space with a training-only WavLM-Large L24 teacher to reduce phoneme-level token fragmentation. Together, these components allow acoustic detail to support waveform reconstruction while keeping the resulting token sequence predictable for autoregressive models. At 650 and 800 bps, ReLMCodec moves the empirical single-stream predictability--reconstruction frontier in our evaluations, with gains that carry over to downstream text-to-speech (TTS) synthesis in both intelligibility and speaker similarity.

</details>

#### [DialectS2S: End-to-End Speech Dialogue Modeling for Low-Resource Chinese Dialects](https://arxiv.org/abs/2608.08067) · [📄 Read](papers/2026/2608.08067.md)

**Yi Shu, Tianyu Peng, Yingzhuo Deng, Wen Yang et al.** · 2026-08-08

<details>
<summary>Abstract</summary>

Current end-to-end speech dialogue models are primarily optimized for mainstream languages and remain limited in low-resource dialect scenarios due to the scarcity of dialect speech data. Moreover, during dialect adaptation, the semantic representation space of speech dialogue models continuously evolves, while conventional speech supervision remains unchanged, leading to semantic inconsistency between hidden representations and speech targets and degrading speech stability and naturalness. To address these issues, we propose DialectS2S, an end-to-end speech dialogue model for Chinese dialects. We first develop a scalable dialect speech dialogue synthesis pipeline for efficient data construction. We further introduce a two-stage post-training strategy with self-aligned speech supervision, which aligns the semantic content of speech supervision with the evolved semantic representations of the model to improve dialect speech generation quality. Experimental results show that DialectS2S consistently outperforms existing baselines across multiple Chinese dialects in speech dialogue, achieving substantial improvements in dialect consistency, response quality, and speech intelligibility. Our work provides an efficient and scalable solution for end-to-end speech dialogue modeling in low-resource dialect scenarios. To facilitate future research and practical applications, we fully open-source the DialectS2S framework, including model checkpoints, training datasets, and fine-tuning code.

</details>

#### [SemBridge: Semantic Token Anchoring for Continuous-Latent Autoregressive Speech Generation](https://arxiv.org/abs/2608.07462) · [📄 Read](papers/2026/2608.07462.md)

**Hanke Xie, Haopeng Lin, Jiale Qian, Dake Guo et al.** · 2026-08-07

<details>
<summary>Abstract</summary>

Continuous-latent autoregressive speech generation has emerged as a promising alternative to discrete-token modeling by avoiding quantization loss and preserving richer acoustic information. However, continuous acoustic targets do not ex- pose linguistic structure as explicit token-level prediction tar- gets. Consequently, the autoregressive language model (LM) must acquire linguistic structure indirectly through acous- tic prediction, which can compromise the content fidelity of generated speech. We propose SemBridge, a training-only semantic-token anchoring framework for continuous-latent autoregressive speech generation. SemBridge uses discrete se- mantic tokens to directly supervise autoregressive LM states and employs a Semantic-Aligned Acoustic VAE to organize the continuous target space under the same semantic refer- ence. The semantic supervision is used only during train- ing, while inference remains entirely continuous. We evalu- ate SemBridge on zero-shot text-to-speech (TTS) and score- conditioned singing voice synthesis (SVS). Across multi- ple benchmarks, SemBridge improves content accuracy, as measured by word and character error rates (WER/CER), while maintaining competitive speaker similarity and percep- tual quality. Experimental results demonstrate that explicit semantic-token supervision for autoregressive state learning is an effective and general direction for continuous speech generation. Speech samples are available.1 The model code and checkpoints will be available at https://github.com/ASLP- lab/SemBridge

</details>

#### [MMAG: A Multi-Control Mixed Audio Generation Benchmark](https://arxiv.org/abs/2608.06900) · [📄 Read](papers/2026/2608.06900.md)

**Zihao Zheng, Xuenan Xu, Jiahao Mei, Yixuan Li et al.** · 2026-08-07

<details>
<summary>Abstract</summary>

Recent audio generation systems have progressed from single-modality synthesis to generating complex acoustic scenes containing speech, music, and sound effects. Therefore, evaluating these models requires assessing multiple interacting capabilities, including semantic fidelity, speaker consistency, and temporal control, yet existing benchmarks focus on isolated domains or coarse-grained descriptions. To address this gap, we introduce the Multi-control Mixed Audio Generation (MMAG) benchmark. MMAG contains approximately 4,000 manually verified audio clips with rich annotations covering speech content, speaker identity, music attributes, sound events, and temporal relationships, together with dedicated subsets for voice cloning and timestamp-conditioned generation. We further propose a systematic evaluation protocol that measures acoustic fidelity, speech quality, semantic alignment, and temporal accuracy. Benchmarking representative agentic orchestrators, unified audio-visual generation models, and native mixed-audio generators reveals substantial performance trade-offs across these capabilities, with no existing model performing consistently well. Our results highlight the remaining challenges of controllable mixed audio generation and establish MMAG as a comprehensive benchmark for future research.

</details>

#### [AffectDF: The Most Comprehensive Benchmark for Speech Deepfake Detection against Emotionally Expressive Attacks](https://arxiv.org/abs/2608.05507) · [📄 Read](papers/2026/2608.05507.md)

**Aurosweta Mahapatra, Xiutian Zhao, Shreeram Suresh Chandra, Zihan Zhang et al.** · 2026-08-06

<details>
<summary>Abstract</summary>

Speech deepfake detection (SDD) systems achieve strong performance on conventional benchmarks; however, existing datasets provide limited coverage of emotionally expressive and recent large audio-language model (LALM)-based attacks. Existing emotional spoofing datasets are also limited in scale and attack diversity, typically covering only voice conversion (VC) or text-to-speech (TTS) attacks. We introduce AffectDF, the most comprehensive benchmark for emotionally expressive speech deepfakes, spanning TTS, VC, emotional VC, and LALM-based spoofing attacks across both acted and spontaneous emotional speech. AffectDF contains approximately 260 hours of speech generated using 21 spoofing attacks across five emotional states. We benchmark state-of-the-art SDD systems under conventional and emotional spoofing conditions, including LALM-based detectors evaluated with both inference-only prompting and supervised fine-tuning. Our experiments reveal severe robustness degradation when models trained on conventional benchmarks are evaluated on AffectDF, with several systems approaching near-random performance. Surprisingly, even large-scale emotional training does not consistently improve cross-domain robustness, indicating that current SDD systems fail to learn generalized spoof representations under emotional and prosodic variability. Robustness further varies substantially across emotional states, attack families, and acted vs spontaneous emotional speech conditions. These findings expose fundamental limitations of current SDD systems and establish AffectDF as a benchmark for developing more robust spoof detection models.

</details>

#### [LILAC: An Idempotent Neural Speech Codec](https://arxiv.org/abs/2608.05727) · [📄 Read](papers/2026/2608.05727.md)

**June Young Yi, Dongwook Lee, Jiheum Yeom, Sungroh Yoon** · 2026-08-06

<details>
<summary>Abstract</summary>

Neural Audio Codecs are widely adopted in speech generation and editing. However, existing neural audio codecs are not idempotent: across the paper's twelve baseline systems, every configuration tested rewrites, on average, at least 15% of its tokens in a single decode-re-encode pass. This poses a problem for utilizing Neural Audio Codecs as token interfaces in pipelines where re-encoding decoded outputs can occur. We present LILAC, a fully convolutional 24 kHz speech codec at 9.375 Hz and 0.75 kbit/s that is codec idempotent by construction; re-encoding the decoded audio of any valid token stream returns the identical stream. LILAC achieves idempotency while maintaining competitive quality, reaching UTMOS 4.14 and 4.24 on LibriSpeech and LibriTTS-R test sets, comparable to SOTA sub-1 kbit/s Neural Audio Codecs.

</details>

#### [Multi Codec Discrete Diffusion Model for Text Guided Speech Inpainting and Editing](https://arxiv.org/abs/2608.06424) · [📄 Read](papers/2026/2608.06424.md)

**Iftach Shoham, Tali Dror, Oren Gal, Haim Permuter et al.** · 2026-08-05

<details>
<summary>Abstract</summary>

Speech recordings often contain missing, corrupted, or incorrect regions that must be reconstructed or modified without re-synthesizing the entire utterance. Speech inpainting restores missing segments, whereas speech editing replaces spoken content according to an edited transcript. Both tasks require the generated speech to express the intended words while remaining consistent with the surrounding speaker identity, prosody, timing, and recording conditions. Discrete diffusion is particularly well suited to these tasks because it can iteratively refine masked tokens while jointly conditioning on both left and right acoustic context. We introduce SIEDD, a discrete diffusion framework for text-guided speech inpainting and editing over hierarchical codec tokens. Its core architecture, HiCoDD, follows the RVQ generation order by representing previously generated codebooks as clean, committed acoustic context and applying diffusion only to the current refinement codebook. This separation enables leakage-free joint training while matching sequential coarse-to-fine inference. The model further combines phoneme-level conditioning, span-localized classifier-free guidance, and duration prediction to support both fixed-duration inpainting and variable-duration text edits. On the RealEdit benchmark, SIEDD achieves the best overall speech-editing performance among the evaluated methods. It also outperforms the evaluated autoregressive baselines across all speech-inpainting settings, on both single and multiple gaps. These results demonstrate that explicitly modeling the codec hierarchy substantially improves context-preserving speech reconstruction and editing. See our full code at https://github.com/iftachShoham/SIEDD.

</details>

#### [Towards Real-world Environment-aware Zero-shot Text-to-speech Synthesis via Disentangled Audio Infilling](https://arxiv.org/abs/2608.03011) · [📄 Read](papers/2026/2608.03011.md)

**Ye-Xin Lu, Xin Wang, Yang Ai, Hui-Peng Du et al.** · 2026-08-04

<details>
<summary>Abstract</summary>

Recent zero-shot text-to-speech (TTS) systems achieve remarkable naturalness and speaker similarity but typically require high-quality speaker prompts and either strip away or entangle the acoustic environment with speaker characteristics, limiting their real-world applicability. We present an extended DAIEN-TTS, an environment-aware zero-shot TTS framework that disentangles and jointly models speech, background noise, and reverberation, enabling independent control over timbre and acoustic environment through separate speaker and environment prompts. Built upon the flow-matching-based F5-TTS, it uses a speech-environment separation module to decompose environmental speech into speech, noise, and reverberation components, which are injected into the Diffusion Transformer for environment-aware generation. Training uses simulated data constructed by mixing clean speech with noise and room impulse responses, together with a cross-speaker conditioning strategy that suppresses speaker information leakage from the environment branch. When real-world data are available, the system can be further fine-tuned to bridge the simulated-to-real domain gap.At inference, a triple classifier-free guidance mechanism enables fine-grained control over speech, noise, and reverberation, and a signal-to-noise-ratio adaptation strategy aligns the synthesized speech with the environment prompt. Experiments on simulated and real-world test sets show that DAIEN-TTS generates environmental personalized speech with high naturalness, strong speaker similarity, and faithful noise and reverberation reproduction, while offering controllability beyond prior environment-aware TTS systems.

</details>

#### [GROW: Group-Relative Advantage-Weighted On-Policy Reinforcement Learning of Autoregressive-Diffusion Text-to-Speech model](https://arxiv.org/abs/2608.03215) · [📄 Read](papers/2026/2608.03215.md)

**Guanrou Yang, Tian Tan, Qian Chen, Ziyang Ma et al.** · 2026-08-04

<details>
<summary>Abstract</summary>

Reinforcement learning for flow-matching text-to-speech is complicated by deterministic ODE sampling: trajectory-level policy-gradient methods typically convert the ODE into an SDE and track per-step likelihood ratios, introducing stochastic perturbations and substantial overhead. We propose GROW, a group-relative advantage-weighted on-policy RL method that acts directly on the standard flow-matching objective. For each prompt, GROW samples a group of on-policy utterances, separately standardizes intelligibility and speaker-similarity rewards within the group, and combines them to reweight flow-matching regression. A Wasserstein-2 velocity penalty anchors the updated model to a frozen pretrained reference. A group-mean reward baseline is introduced to convert reward weighting into advantage weighting. For strong pretrained TTS models with concentrated rewards, positive exponential weighting is dominated by reward-agnostic self-imitation, whereas a zero-mean signed advantage preserves effective within-group credit assignment. Instantiated on DiTAR and evaluated on LibriSpeech and Seed-TTS EN/ZH, GROW reduces average WER from 2.016 to 1.558 and raises speaker similarity from 0.676 to 0.715 while keeping UTMOS. With 10-NFE training rollouts and 32-NFE evaluation, GROW retains comparable performance while training 2.9x faster than 32-NFE DiTAR-GRPO. We will open-source complete GROW codes, faithful DiTAR reproduction, and all model checkpoints.

</details>

#### [Towards More Expressive Spoken LLMs: Fine-Grained Intent Benchmarking and Acoustic-Lexical Decoupled Policy Optimization](https://arxiv.org/abs/2608.03054) · [📄 Read](papers/2026/2608.03054.md)

**Xiang Lin, Tian-Hao Zhang, Chunfeng Wang, Zhou Pan et al.** · 2026-08-04

<details>
<summary>Abstract</summary>

Spoken emotional dialogue requires a model to understand a user's spoken input and generate a response that is both semantically appropriate and emotionally expressive. This is challenging because communicative intent may be stated explicitly in lexical content or conveyed more implicitly through paralinguistic cues, which can complement or diverge from the words themselves. However, two limitations constrain progress in this area: the scarcity of benchmarks that distinguish these intent expressions, and the lack of reinforcement learning objectives that jointly account for response quality and emotional expression. To address the lack of suitable benchmarks, we introduce ParaIntent, a Chinese benchmark comprising 14 intent categories with balanced explicit and implicit samples, together with a multidimensional evaluation protocol covering intent fulfillment, response quality, and emotional expression. For policy optimization, existing approaches either use a shared objective for text and speech or apply reinforcement learning to only one modality, leaving modality-specific learning signals entangled within policy optimization. Motivated by this, we propose Acoustic-Lexical Decoupled Policy Optimization (ALPO), which computes independent textual and acoustic advantages and routes them to the corresponding text and speech tokens within a unified rollout. Under identical reward functions and training budgets, ALPO improves over standard GRPO on most automatic metrics and achieves the best subjective results among the fine-tuned variants, with particularly clear gains in emotional expressiveness on both the synthetic and human-recorded test sets.

</details>

#### [Embodied Empathy: A Multimodal AR and LLM-Powered System for Self-Attachment Psychotherapy with Self-Initiated Humour](https://arxiv.org/abs/2608.02283) · [📄 Read](papers/2026/2608.02283.md)

**Xinyan Ye, Gwyneth Phang, Anandha Gopalan, Abbas Edalat** · 2026-08-03

<details>
<summary>Abstract</summary>

The growing global demand for mental health support increasingly exceeds the supply of qualified practitioners, creating an urgent need for scalable digital interventions that can deliver meaningful emotional connection. In response, we present a novel multimodal application that operationalises the Self-Initiated Humour Protocol (SIHP) within a Self-Attachment Technique (SAT) framework. Our mobile application integrates customisable 3D childhood avatars, augmented reality, and an LLM-driven virtual therapist capable of automated emotion mirroring. An eight-day user study (N=16) indicates the system's feasibility and improvements in self-reported mood. Results show that personalised avatars and text-to-speech output strengthen emotional bonding and perceived empathy. Although emotion mirroring boosts engagement, its effectiveness depends heavily on classification accuracy and animation intensity. Moreover, findings indicate a shift in user expectations--from reactive chatbots to proactive conversational facilitators. We conclude with design implications for leveraging AI and AR to cultivate embodied empathy in digital mental health tools.

</details>

#### [Domain-Specific Evaluation of Text-to-Speech Systems: A Multi-Metric Benchmarking Study](https://arxiv.org/abs/2608.02235) · [📄 Read](papers/2026/2608.02235.md)

**Ali Jafar, Amal Sarmad, Shifa Yousaf, Maryam Bashir** · 2026-08-03

<details>
<summary>Abstract</summary>

Recent advances in neural text-to-speech (TTS) systems have substantially improved speech naturalness and intelligibility across many languages. However, comprehensive evaluation methodologies that jointly assess perceptual quality, speaker similarity, and acoustic fidelity across diverse speech domains remain limited, particularly for low-resource and underrepresented languages. This paper presents a reproducible, multi-metric benchmarking framework for systematic evaluation of modern TTS systems through domain-specific analysis. The proposed framework integrates complementary subjective and objective evaluation protocols and is demonstrated through a comprehensive case study on a representative low-resource language spanning four speech domains: Formal, Conversational, Literary/Storytelling, and Emotional. Four state-of-the-art TTS systems -- Indic-Parler-TTS, MMS-TTS, Microsoft Edge TTS, and Google Gemini TTS -- are evaluated using MUSHRA listening tests, ABX discrimination tests, speaker similarity scoring with Resemblyzer, and acoustic analyses based on mel-cepstral distortion (MCD) and F0 RMSE over 960 audio pairs. Results reveal substantial variation in TTS performance across speech domains, with emotional speech consistently presenting the greatest synthesis challenge (mean MCD 12.03 dB; mean F0 RMSE 889 cents), while conversational speech achieves the highest overall acoustic fidelity. Beyond the empirical findings, this work provides a reproducible evaluation framework, publicly releasing evaluation scripts, result tables, and executable Colab notebooks to support standardized benchmarking and future research on TTS evaluation for low-resource languages.

</details>

#### [SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and Zero-Shot Tasks](https://arxiv.org/abs/2608.02023) · [📄 Read](papers/2026/2608.02023.md)

**Yu Zhang, Ruiqi Li, Changhao Pan, Ke Lei et al.** · 2026-08-03

<details>
<summary>Abstract</summary>

Speech and audio generation is often needed in animation dubbing, audio drama, movies, advertising, games, podcasts, and short-video production. In these scenarios, creators may need to design voices without reference recordings, control speaker styles with natural language, support acoustic scenes with environments and audio effects, and later reuse the designed voices. Therefore, it is important to support multi-speaker speech and audio generation for both instruct and zero-shot tasks. The instruct task requires a caption of the environment, speaker styles, and fine-grained content, while the zero-shot task uses reference audio together with the same fine-grained content. We address these tasks from both the data and model sides. First, we propose SwanData-Caption, which cleans raw speech and audio data, adds targeted synthetic coverage, and annotates diverse and accurate multi-level captions. Then, we propose SwanTale, a multi-speaker expressive speech and audio generation model that supports both zero-shot and instruct tasks. We introduce SwanVAE to support high-quality multi-audio-modality generation. Then, we adopt reward-conditioned quality control and Engram conditioning, along with Unified MoE for multi-task and multi-audio-modality modeling. In addition, we use curriculum learning and GRPO post-training to let the model progressively learn and strengthen its capabilities. Experimental results show that SwanTale leads on multiple key zero-shot and instruct metrics, achieves the best expressiveness scores in both tasks, and supports complex instruct generation involving multi-speaker speech and audio. Demos can be found at https://swanaigc.github.io/\#swantale.

</details>

#### [Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces](https://arxiv.org/abs/2608.00998) · [📄 Read](papers/2026/2608.00998.md)

**Wangzixi Zhou, Bagus Tris Atmaja, Sakriani Sakti** · 2026-08-02

<details>
<summary>Abstract</summary>

The rise of conversational AI has increased interest in emotional Text-to-Speech (TTS). Most systems rely on discrete emotion labels, which fail to capture the nuanced nature of human affect. Recent models employ dimensional representations such as Russell's arousal-valence (A-V) model, offering finer control. However, emotional perception varies across individuals and cultures, which may cause mismatches between modeled and perceived emotions. We propose a personalized and culturally adaptive emotional TTS framework that performs interactive optimization of individualized A-V perception spaces using an Interactive Genetic Algorithm. By adapting emotion representations to each listener, the system produces speech with more perceptually aligned emotional expression than models using averaged A-V values. Evaluations with Japanese, Chinese, and Indonesian participants highlight the importance of personalization and cultural adaptation for moving beyond one-size-fits-all emotional TTS.

</details>

#### [JoyAI-Talker: Full-Duplex Speech Interactive Large Model Built for Empathetic Voice Agents](https://arxiv.org/abs/2608.01119) · [📄 Read](papers/2026/2608.01119.md)

**Yinhao Bai, Jinming Chen, Yafeng Chen, Wei Deng et al.** · 2026-08-02

<details>
<summary>Abstract</summary>

We present JoyAI-Talker, a full-duplex speech dialogue system that delivers robust foundation model capabilities while empowering empathetic interaction and voice agent intelligence. JoyAI-Talker adopts a modular Thinker-Talker architecture and further implements a unified speech-text joint training pipeline to mitigate the common "cognitive degradation" bottleneck, thereby largely preserving the model's core textual reasoning, STEM, and logical capabilities while extending them to speech-based interaction. For expressive speech synthesis, the Talker module employs a text-controllable generation paradigm that enables natural-language instructions to flexibly control vocal attributes and localized paralinguistic events, such as laughter and sighs, supporting more expressive and fine-grained speech responses. To enhance conversational empathy, we introduce the Persona-Adaptive Empathetic Response (PAER) framework. PAER employs a hierarchical cognitive pipeline to extract non-verbal speaker cues, such as gender, age, and emotional state, from raw input audio, incorporate them into the Thinker's CoT reasoning, and generate context-adaptive responses that align semantically appropriate text with fine-grained control over utterance-level expressiveness and localized paralinguistic events, including sighs, speaking rate, and volume. We further integrate Joy-Duplex, a state-driven, plug-and-play full-duplex framework that functions as an efficient gating engine for real-time turn control. Extensive evaluations show that JoyAI-Talker achieves highly competitive performance on foundational T2T and S2T benchmarks. In full-duplex evaluation, the system reaches a high response rate of 0.88 under user interruptions while maintaining an extremely low false-trigger rate under background speech, demonstrating its readiness for fluid and natural speech dialogue.

</details>

#### [dots.tts.edit: Precisely Controlled Speech Editing with a Continuous Autoregressive Model](https://arxiv.org/abs/2608.02673) · [📄 Read](papers/2026/2608.02673.md)

**Hankun Wang, Bohan Li, Shi Lian, Xiaoyu Gu et al.** · 2026-08-02

<details>
<summary>Abstract</summary>

Speech editing for content creation requires precise control over both what an edit should do and where it should apply. Free-form natural language provides a flexible interface for expressing edit requests, but its ambiguity may leave the intended operation, parameters, or target region underspecified. We study a precise and explicit interface for speech editing: a transcript-grounded structural edit instruction with XML-style tags explicitly specifies typed operations and localizes them to transcript spans or boundaries. This semantic timeline avoids explicit timestamp alignment and provides an externally inspectable contract for compositional edits. We instantiate the interface in dots.tts.edit, an editor adapted from the continuous autoregressive dots.tts foundation model. Four representative speech-creation controls cover lexical content, affective expression, pitch and speaking-rate delivery, and temporal phrasing through text, emotion, prosody, and pause editing. Task-specific data pipelines construct operation- and scope-controlled pairs while retaining source-derived context outside each target region. We further introduce doteBench, a bilingual evaluation suite that measures precise instruction following, local preservation, and audio quality across the four controls and their composition. Experiments show leading overall instruction following and local preservation across its five editing categories, while audio quality remains comparable to existing open-source systems. Across three Seed-TTS-Eval shards, the model shows negligible differences from the base model in zero-shot TTS recognition error rate and speaker similarity. The code and model will be released soon.

</details>

#### [REIMU: Efficient Heterogeneous Hierarchical Reasoning for SSL-Based Speech Deepfake Detection](https://arxiv.org/abs/2608.00857) · [📄 Read](papers/2026/2608.00857.md)

**Kwok-Ho Ng, Tingting Song, Bingwen Feng, Peiya Li** · 2026-08-01

<details>
<summary>Abstract</summary>

The increasing realism of speech generated by text-to-speech and voice conversion systems poses growing challenges to media integrity and voice authentication. Self-supervised learning (SSL) has substantially advanced speech deepfake detection, where downstream backbones conventionally process SSL representations through a single forward pass. This work investigates the practical effectiveness of recurrent hierarchical reasoning for this task. We term this controlled study REIMU and systematically compare conventional single-pass backbones, weight-shared recurrence, homogeneous HRM, and heterogeneous HRM across four Base-scale SSL frontends. We further examine heterogeneous high- and low-level modules that combine self-attention with linear attention. Experiments on the ASVspoof 2019 and 2021 evaluation sets show that recurrence and hierarchical decomposition do not inherently improve detection, whereas heterogeneous operator assignment provides a more competitive configuration. Notably, the heterogeneous design remains competitive while using 10.8\% fewer downstream parameters than the matched baseline, demonstrating its potential for parameter-efficient speech deepfake detection.

</details>

#### [Experience-Calibrated Contrastive Decoding for Mitigating Hallucinations in LM-Based Text-to-Speech](https://arxiv.org/abs/2608.00722) · [📄 Read](papers/2026/2608.00722.md)

**Chenlin Liu, Minghui Fang, Zhonghao Bi, Zekai Su et al.** · 2026-08-01

<details>
<summary>Abstract</summary>

Language model-based text-to-speech (LM-based TTS) remains vulnerable to speech hallucinations that deviate from the target text. Existing mitigation mainly relies on architectural changes or additional training, while decoding-time control remains underexplored. We present a conditional information view that distinguishes text-derived alignment information from experience information supplied by acoustic context and learned speech regularities. We hypothesize that an important class of hallucinations begins when alignment support is insufficiently reflected in the selected token at a vulnerable transition. Using predictions from the same speech LM with and without text conditions, we propose Experience-Calibrated Contrastive Decoding (ECCD), a training-free method that strengthens alignment support while preserving useful experience information. ECCD preserves the original expert distribution, applies only positive alignment enhancement, and calibrates its strength using set-level experience compatibility. Across four models, ECCD reduces WER/CER by up to 55.6% in all SeedTTS-Eval settings and 24 of 25 multilingual CV3-Eval settings. A listening test yields a CMOS gain of $+0.644$ while retaining strong speaker similarity. Further analysis shows that alignment influence and decision-level gain vary within linguistic units and are lower at first-error boundaries than at matched correct boundaries. Overall, these extensive experiments and analyses identify conditional information control as a promising decoding-time direction for mitigating speech hallucination.

</details>

#### [AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context Spectral Infilling](https://arxiv.org/abs/2608.00572) · [📄 Read](papers/2026/2608.00572.md)

**Junchuan Zhao, Minh Duc Vu, Bowen Zhang, Ye Wang** · 2026-08-01

<details>
<summary>Abstract</summary>

Bandwidth extension (BWE) aims to recover missing high-frequency content from band-limited speech. Existing methods often formulate BWE as a fixed or predefined bandwidth conversion problem, potentially requiring cutoff-specific models or retraining when the input bandwidth changes. This assumption limits their applicability to practical scenarios where speech may arrive with diverse cutoff frequencies. We propose AnyBand, a unified BWE framework that recasts bandwidth extension as in-context spectral infilling. Motivated by prompt-based zero-shot speech generation, AnyBand conditions high-frequency generation on the observed low-frequency spectrum, using the available band as a frequency-domain prompt that conveys content, speaker, prosodic, and spectral-envelope cues. This formulation enables a single model to perform cutoff-conditioned generation over a continuous range of input bandwidths. AnyBand is trained with missing-band conditional flow matching and an Easy-to-Balanced cutoff curriculum over continuously sampled cutoff frequencies. To better exploit the spectral prompt, we introduce a frequency-aware Diffusion Transformer that models cross-frequency interactions and long-range temporal dependencies, followed by a physically motivated multi-view adversarial refinement stage to enhance spectral realism, envelope coherence, and harmonic consistency. Experiments on multiple datasets and bandwidth settings show that AnyBand consistently improves spectral reconstruction over existing baselines while achieving competitive perceptual quality across both standard and irregular input cutoffs. Audio samples are available.

</details>

#### [Beyond Prompt Adherence: Auditing Attribute-Level Voice Control in Speech Generation](https://arxiv.org/abs/2608.00545) · [📄 Read](papers/2026/2608.00545.md)

**Xianhao Zhou, Jianghao Wu** · 2026-08-01

<details>
<summary>Abstract</summary>

Natural-language descriptions have become a flexible interface for controlling generated speech. Existing evaluations largely assess whether an output matches a prompt, but prompt matching alone does not reveal whether characteristics outside the intended change remain stable. We examine this distinction through a controlled paired audit of three speech-generation systems: CosyVoice3, VoxCPM2, and Fish-Speech-S2. The evaluation contains 5,940 outputs spanning six reference speakers, ten texts, three random seeds, and eleven conditions. Using acoustic, prosodic, content, and speaker measurements, we find that responses in the expected target direction are frequently accompanied by changes outside descriptor-specific signal-level target sets. This pattern remains among outputs whose target response exceeds baseline seed variation, and the accompanying changes differ substantially across systems. We further introduce VoDER-Cal, a training-free candidate selector that retains sufficiently strong target responses while favoring smaller off-target deviations. A three-candidate pool raises the joint success rate from 4.8% under single-sample direct generation to approximately 14% for all candidate-selection policies. Within the matched three-candidate budget, VoDER-Cal reduces held-out off-target deviation from 0.344 under target-only selection to 0.276 and improves listener-rated preservation. Preservation-sensitive evaluation therefore complements prompt-adherence evaluation, while candidate reranking offers a practical inference-time improvement. Code, configuration files, and analysis scripts are available at https://github.com/intelland/VoDER

</details>

#### [Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens](https://arxiv.org/abs/2607.29363) · [📄 Read](papers/2026/2607.29363.md)

**Yi Luo, Rongzhi Gu, Jixun Yao** · 2026-07-31

<details>
<summary>Abstract</summary>

Balancing sequence length, representational capacity, and long-horizon stability is a central problem in autoregressive (AR) speech and audio generation. Representations with higher frame rates or greater capacity can preserve more signal detail, but they also make streaming generation more vulnerable to distribution drift and AR error accumulation. Conversely, shorter and more compressed representations simplify AR modeling, but their limited bandwidth may discard important components and constrain the upper bound of reconstruction fidelity and generation quality. We ask whether a low-frame-rate, high-dimensional, high-bandwidth continuous representation can be co-designed with a streaming generation framework to support robust high-fidelity reconstruction, strong single-token predictability, and superior long-horizon stability. We decompose this goal into two coupled problems: what geometric and statistical properties a high-dimensional representation space should have, and how an AR continuous-token generator should be structured to resist error accumulation. Accordingly, we propose Locodec, a locally encoded codec that shapes its representation space to improve the interpolatability of a lower-dimensional core manifold and the identifiability of the native high-dimensional coordinates, thereby improving the predictability of high-dimensional high-bandwidth tokens. We also propose MP-ELD, a single-token AR flow-matching framework that uses multi-path information routing and residual classifier-free guidance to mitigate error accumulation. Experiments with 8-Hz, 768-dimensional tokens show that our design preserves reconstruction quality, improves single-token predictability, achieves competitive WER, and maintains stable long-form synthesis, without using external SSL/ASR models, pretrained text language models, or post-training stages.

</details>

#### [Teffic-Audio: Tell Fact from Fiction](https://arxiv.org/abs/2607.28351) · [📄 Read](papers/2026/2607.28351.md)

**Wan Lin, Li Wang, Jindong Wang, Kunyu Feng et al.** · 2026-07-30

<details>
<summary>Abstract</summary>

Speech deepfake detection has expanded in scope with increasingly heterogeneous spoofing mechanisms, including speech synthesis, voice conversion, vocoder reconstruction, and neural-codec resynthesis. The resulting spoofing artifacts can be further shaped by variability in source speech, recording environments, and transmission channels. This variability makes robust generalization across heterogeneous conditions a central requirement for practical detection systems. This report presents Teffic-Audio, a general speech deepfake detection system designed for comprehensive evaluation environment. Teffic-Audio adopts a straightforward detector architecture consisting of a Conformer-based speech encoder, multi-head attentive statistics pooling, and a binary classifier. Rather than relying on additional architectural complexity, the system improves generalization through its training recipe, which integrates multi-source data, attack- and source-balanced sampling, and diverse audio augmentation. Trained only with open-source data, Teffic-Audio achieves a pooled EER of 1.454% on the 14 test sets of Speech-DF-Arena, outperforming all currently public systems on the leaderboard. It also obtains the lowest EER on five individual test sets and shows a favorable performance-complexity trade-off compared with larger leading systems. Overall, Teffic-Audio provides a strong and practical reference system for general speech deepfake detection.

</details>

#### [CrowdioSet and PaRIRset: Two Datasets Towards Live Music Source Separation](https://arxiv.org/abs/2607.27828) · [📄 Read](papers/2026/2607.27828.md)

**Enric Gusó, Xavier Serra** · 2026-07-30

<details>
<summary>Abstract</summary>

Most Music Source Separation (MSS) models do not generalize well to live music recordings because they are trained on studio recordings alone, disregarding the venue acoustics, the speaker system's response and audience noise. We propose to bridge this gap by providing and training a model on two novel datasets. First, we present CrowdioSet: a noise dataset comprising 4800 real ambience tracks from Freesound and synthetic sing-alongs for the vocals in MUSDB18 and MOISESDB datasets, generated from zero-shot singing voice conversions. CrowdioSet enables effective audio denoising for live recordings, resulting in superior separation both in objective and subjective evaluations. Second, we introduce PaRIRset, a stereo impulse response dataset captured across 40 professional concert venues using a microphone array. Our results show that adding PaRIRset RIRs increases the performance of a MSS model compared to using real RIRs from Speech Enhancement tasks alone. We make the examples, code, model weights, PaRIRset, and CrowdioSet freely available to the public.

</details>

#### [Cloned Voices, Real Consequences: Evaluating Bias in Political Deepfake Detection for Electoral Integrity in Brazil](https://arxiv.org/abs/2607.28770) · [📄 Read](papers/2026/2607.28770.md)

**Lucas Rafael Stefanel Gris, Daniel Casanova, Frederico Santos De Oliveira, Alef Iury Ferreira et al.** · 2026-07-30

<details>
<summary>Abstract</summary>

Recent advances in generative artificial intelligence have made it easier to fabricate statements and amplify political disinformation during elections. We introduce ParlaSpoof-BR, an audio deepfake dataset derived from recordings of the Brazilian Chamber of Deputies and expanded with synthetic utterances from diverse text-to-speech and voice conversion models. Using ParlaSpoof-BR, we benchmark state-of-the-art audio deepfake detectors, examine their ability to generalize to Brazilian Portuguese political speech, and investigate potential biases in their predictions. Our analysis reveals that current systems struggle to provide consistent decisions across the diversity represented in the dataset, with methodological factors (synthesis model choice, manipulation extent) dominating over demographic disparities. ParlaSpoof-BR provides a domain-specific benchmark for studying audio deepfake detection in a socially consequential and underrepresented setting, supporting the development of more robust detection systems for electoral integrity in Brazil.

</details>

#### [Zero-Shot Face-to-Speech Synthesis via Latent Space Adaptation of a Style-Diffusion TTS Model](https://arxiv.org/abs/2607.26742) · [📄 Read](papers/2026/2607.26742.md)

**Carlos Muñoz-Romero, Jose A. Gonzalez-Lopez** · 2026-07-29

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (TTS) clones a voice from a short audio prompt, but this reliance on reference audio is a barrier when only visual information is available, e.g. for historical figures or video-game characters. In this work, we propose a Face-to-Speech (F2S) framework that predicts a plausible voice from a static facial image. A lightweight Face Adapter, together with soft-tuning of the face encoder's upper blocks, aligns face-recognition features with the style space of a frozen StyleTTS 2 model, kept frozen during training. We evaluate on held-out identities from LRS3, a large-scale audiovisual corpus of English TED-talk videos. The synthesized speech is highly natural (UTMOS 3.7-4.0, matching or exceeding the 3.61 of ground truth), face-to-voice retrieval is consistently above chance, and the generated voice is consistent with the target speaker. Without any retraining, an English-trained adapter also produces fluent Spanish speech, indicating that the face-to-style mapping is largely language-agnostic.

</details>

#### [Extracting Voice Styles from Frozen TTS Models via Gradient-Based Inverse Optimization](https://arxiv.org/abs/2607.25351) · [📄 Read](papers/2026/2607.25351.md)

**Gyeongmin Kim** · 2026-07-28

<details>
<summary>Abstract</summary>

Some text-to-speech systems ship a synthesis model and preset style vectors but not the reference encoder that turns audio into such a vector. The model still accepts a style vector; a user with a voice of their own cannot produce one. We solve for that input directly, inverting the released pipeline by gradient descent: every weight stays frozen and only the style vector is optimized, against time-pooled WavLM statistics of one recording. Because the objective discards the time axis, the synthesized text may differ from the recording, so no transcript and no alignment are needed. On 154 speakers from two corpora, ECAPA-TDNN similarity rises from 0.132 to 0.413 and ResNet from 0.099 to 0.401, improving for every speaker; a verifier at its equal-error point accepts 53% of the recovered voices as the target, against 1% for the presets they start from.

</details>

#### [Qwen-Audio-3.0-TTS: Freely Controllable and Highly Robust Speech Synthesis with Multi-Stage Training Paradigm](https://arxiv.org/abs/2607.23938) · [📄 Read](papers/2026/2607.23938.md)

**Bajian Xiang, Cheng Wen, Han Zhao, Hao Wang et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

In this report, we present Qwen-Audio-3.0-TTS, a production-oriented speech synthesis system that jointly advances content consistency, speaker similarity, prosodic naturalness, audio quality, controllability, multilingual coverage, efficiency, and robustness. It combines a 12.5~Hz low-frame-rate speech tokenizer for reduced inference latency with a five-stage progressive training paradigm for coordinated language model (LM) and flow-matching model (FM) optimization. The model provides production-level control through free-style natural-language instructions and fine-grained inline tags, while supporting 16 languages, 20 Chinese dialect regions, one-pass long-form synthesis up to 3 minutes, and robust generation from noisy, reverberant, or unclear reference speech. Across SEED-TTS-Eval, CV3-Eval, instruction-following, long-form, and acoustic-robustness evaluations, Qwen-Audio-3.0-TTS achieves state-of-the-art performance on many reported dimensions or the strongest aggregate results. It also ranks first on the independent Artificial Analysis Text-to-Speech Leaderboard. These results establish Qwen-Audio-3.0-TTS as a strong foundation for production-level speech synthesis.

</details>

#### [Let Me Look at You: Advanced Facial Expression Modeling for Conversational Speech Synthesis](https://arxiv.org/abs/2607.24430) · [📄 Read](papers/2026/2607.24430.md)

**Yifan Hu, Shuwei He, Rui Liu, Haizhou Li** · 2026-07-27

<details>
<summary>Abstract</summary>

Conversational Speech Synthesis is a fundamental component of human-computer interaction, aiming to generate contextually appropriate, expressive, and empathetic speech. However, facial expressions encode subtle and rich affective cues that are crucial for empathetic speech interaction, whereas existing approaches often overlook this important modality. In addition, the lack of large-scale natural conversational datasets with both speech and visual modalities also limits the development of visual affect understanding in conversational settings.To address these limitations, we propose FacialTalker, a facial-expression-aware CSS framework built upon a large language model backbone. To efficiently encode facial expressions, we propose AUTokenizer, a single-codebook visual tokenizer that discretizes each frame-level facial expression into a compact token, trained with supervision from combinations of facial Action Units. We further introduce a dual direct preference optimization (DualDPO) strategy, which extends the DPO by jointly imposing preference constraints on both visual and speech token sequences, to enhance the model's understanding of facial expressions and speech semantics in multimodal conversational contexts. Moreover, we construct VSDD-1K, a large-scale multimodal dialogue dataset collected through a fully automated pipeline from real-world Internet conversations, comprising over 1,033 hours of synchronized speaker videos and speech, with more than 85\% of frames containing valid faces. Extensive objective and subjective experiments demonstrate that FacialTalker consistently outperforms strong baselines in facial-expression perception and speech synthesis quality, generating speech that is more natural, expressive, and better aligned with the conversational context. The results also validate the effectiveness of our training strategy and dataset construction pipeline.

</details>

#### [Leveraging Gradient Reversal Loss and Multitask Learning for Datasets-Aware Audio Deepfake Detection](https://arxiv.org/abs/2607.23961) · [📄 Read](papers/2026/2607.23961.md)

**Mingrui Liang, Thomas Thebaud, Lukasz Wojciak, Laureano Moro Velazquez et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

Recent advances in speech synthesis and voice conversion, which pose threats to security and privacy, have underscored the need for deepfake detection technology. Although existing detection systems achieve strong performance on individual datasets, they often fail to generalize across diverse datasets. Prior methods for improving generalization, including data augmentation, adversarial training on auxiliary factors such as language or codec types, and Mixture-of-Experts (MoE), are limited by predefined augmentation coverage, difficulties in obtaining auxiliary factors, and substantial model complexity. In this work, we propose a practical dataset-aware framework for deepfake detection. Our method targets heterogeneous datasets for which auxiliary annotations such as language, codec, or spoofing method may not be consistently available. We therefore rely only on dataset identity as a naturally available supervisory signal for multitask (MT) and gradient reversal layer (GRL) training, allowing the model to investigate both dataset-aware multitask supervision and adversarial suppression of dataset-specific information. We conduct experiments following the 2025 Speech DeepFake Arena benchmark protocol, evaluating our model across multiple evaluation datasets and reporting aggregate performance in terms of Equal Error Rate (EER), including Average EER and Pooled EER. Compared with the baseline, MT reduces Average EER by 13.14% relatively, while GRL reduces Pooled EER by 5.32% relatively. These results demonstrate that our method can improve aggregate detection performance across heterogeneous evaluation datasets, offering a practical solution for deploying reliable deepfake detection systems on diverse and unseen real-world data.

</details>

#### [Revisiting Vocos: That Phasiness Business in Time-Frequency Neural Vocoding](https://arxiv.org/abs/2607.24323) · [📄 Read](papers/2026/2607.24323.md)

**Ünal Ege Gaznepoğlu, Frank Zalkow, Mohammad Joshaghani, Emanuël A. P. Habets et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

Recently, time-frequency neural vocoders have been approaching the state-of-the-art quality of time-domain neural vocoders. Vocos is a notable example due to its efficiency, but its audio quality lags behind the time-domain vocoders and the reasons remain debated. Thus, in this study, we revisit Vocos from a phase reconstruction perspective. First, we quantify the gap between time-domain and time-frequency domain vocoders using bandlimited mel spectrograms as inputs. Later, via an ablation study, we verify the Vocos architecture is effective for magnitude modeling, but less so for phase. We then adapt the Vocos backbone to predict phase differences, a precursor for phase reconstruction, and identify 1D convolutional layers are hindering their accurate prediction. Our findings indicate that future research needs to focus on inductive biases that allow the architecture to better model the time-frequency structure of speech signals, without sacrificing the support for arbitrary input representations.

</details>

#### [Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers](https://arxiv.org/abs/2607.23811) · [📄 Read](papers/2026/2607.23811.md)

**Dongseong Hwang, Prasanth Yadla, Kaan Elgin, Shifas Padinjaru Veettil et al.** · 2026-07-26

<details>
<summary>Abstract</summary>

Siri Expressive Voices synthesize rich, configurable speech in real time and entirely on device, powered by AFM 3 Core Advanced, Apple's most powerful on-device foundation model. This work presents the memory-efficient audio synthesis architecture behind that capability: a detokenizer that converts the semantic audio tokens emitted by the foundation model into high-fidelity audio within the tight compute and memory budget of the Apple Matrix Coprocessor (AMX). We convert semantic audio tokens to a residual vector quantization (RVQ) representation with a three-component design, a streaming encoder, a temporal decoder, and a depth decoder, that systematically decouples temporal and depth processing. A single reusable depth decoder with Diffusion Transformer (DiT)-style stage conditioning generates all RVQ levels autoregressively, replacing the dedicated per-level decoders of prior multi-decoder architectures, while causal sliding window attention with fixed-window key-value caching yields constant memory complexity independent of sequence length. Deployed on the AMX, the detokenizer sustains roughly 10 ms per generation step, about 16x faster than real time, with a peak runtime memory of only 21 MB and 329 MB of on-device assets, enabling continuous streaming synthesis of 20-320 seconds of audio. This constant, small footprint replaces the linear and quadratic memory scaling of conventional transformer- and GAN-based approaches. Ablation studies validate the key architectural components, and audio quality assessment confirms that the architecture maintains synthesis fidelity while achieving efficiency gains over existing methods. Operating at a 1-billion-parameter activation size within AFM 3 Core Advanced, it improves Mean Opinion Score by +0.28 overall (4.15 vs. 3.87) and by +0.42 on conversational speech (4.24 vs. 3.82) over the prior on-device text-to-speech system.

</details>

#### [Expose Your Disguise: Recovering Source Speaker Identity From Voice Conversion](https://arxiv.org/abs/2607.23650) · [📄 Read](papers/2026/2607.23650.md)

**Hanlei Zhang, Zhongming Ma, Mingyang Zhang, Tengfei Liu et al.** · 2026-07-26

<details>
<summary>Abstract</summary>

Voice conversion (VC) poses a significant threat to biometric security by allowing attackers to impersonate target speakers. In forensic contexts, recovering the source speaker's identity from converted audio is vital for narrowing the field of suspects. To address this, we propose TRIDENT, a retracing framework designed to restore a source speaker's original identity from a converted audio sample. TRIDENT utilizes a three-pronged architecture consisting of a primary extractor and two auxiliary branches. The first auxiliary branch identifies the underlying voice conversion mechanism. This design acknowledges that even if the exact conversion strategy is unknown, a high-performance model adopted by the attacker is typically a derivative or variant of established mainstream ones. The second auxiliary branch extracts a latent representation of the target speaker, facilitating the isolation of target-specific traits from the composite converted audio sample. Finally, the main extractor leverages insights from both auxiliary branches to decouple confounding factors and distill a highly discriminative representation of the source speaker's identity. Experimental results demonstrate that TRIDENT achieves an accuracy as high as 90.99% against 7 state-of-the-art voice conversion methods. Furthermore, TRIDENT maintains robust performance under challenging conditions, including telephony channels, unseen languages, and adaptive scenarios.

</details>

#### [Singlish, Can or Not? Fine-Tuning and Evaluating Zero-Shot TTS for Singapore English](https://arxiv.org/abs/2607.23027) · [📄 Read](papers/2026/2607.23027.md)

**Ivan Kukanov, Zheng Xin Chai** · 2026-07-25

<details>
<summary>Abstract</summary>

Zero-shot text-to-speech (ZS-TTS) achieves near-human quality for standard English, but it copies regional accents poorly. Prompted with a short Singlish utterance, state-of-the-art systems reproduce a speaker's timbre while flattening the accent toward generic English. We investigate whether targeted fine-tuning off-the-shelf ZS-TTS can close the gap for Singapore English (Singlish). We fine-tune two cutting-edge ZS-TTS models, Chatterbox and CosyVoice 3, on 50 Singlish speakers from the IMDA National Speech Corpus. Three speech distributions are evaluated: real recordings against off-the-shelf and fine-tuned generation driven by the same Singlish audio prompts. The evaluation covers four dimensions: naturalness, intelligibility, speaker similarity, and accent similarity. We separate adaptation (in-domain speakers seen during fine-tuning) from consistency (held-out speakers) to test whether accent transfer generalises beyond the training data. Fine-tuning raises accent similarity on in-domain and out-of-domain speakers for both Chatterbox and CosyVoice 3. It moves the generated distribution measurably toward real Singlish, with the gain persisting on held-out speakers. To our knowledge, this is the first systematic study of Singlish-accented TTS.

</details>

#### [VisionPulse: A Virtual Reality System Enabling Accessible Discovery and Navigation for Blind and Low Vision Users](https://arxiv.org/abs/2607.21944) · [📄 Read](papers/2026/2607.21944.md)

**Samuel Martin, Pooyan Fazli, Hasti Seifi** · 2026-07-24

<details>
<summary>Abstract</summary>

Free exploration is an important aspect of many engaging virtual reality (VR) experiences, yet remains largely inaccessible to blind and low vision (BLV) users due to its reliance on visual feedback. Existing approaches support BLV navigation through prebuilt menus of environment and audio beacons, but offer limited support for free-form discovery. We present VisionPulse, an accessible VR system that enables BLV users to explore virtual environments through natural head and hand movements, combined with auditory, haptic, and text-to-speech feedback. VisionPulse introduces a discovery-driven approach that allows users to progressively uncover regions and objects, alongside navigation support through waypoint guidance and object localization via responsive audio and orientation-based haptics. A study with 12 BLV participants showed a strong preference for VisionPulse's discovery-based exploration and multimodal feedback, without negatively impacting task performance or perceived workload. Our findings underscore the importance of accessible, free-form VR experiences, and contribute insights for inclusive VR design.

</details>

#### [Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning](https://arxiv.org/abs/2607.22304) · [📄 Read](papers/2026/2607.22304.md)

**Roseline Polle, Owen Parsons, George Fairs, Luis Miguel San Martin Fernandez et al.** · 2026-07-24

<details>
<summary>Abstract</summary>

Synthetic data augmentation in speech is common practice for linguistic tasks like ASR, but has seen far less work for paralinguistic ones, especially clinical tasks where labelled data is expensive and some patient groups are underrepresented. Voice cloning is one such augmentation approach, but is typically evaluated on speech intelligibility (WER) or speaker similarity (SS) rather than on downstream performance, and it remains unclear whether these preserve the paralinguistic signal such tasks depend on. We benchmark eight voice cloning models on five paralinguistic tasks across public and clinical datasets, showing most preserve signal with modest degradation. We then clone English clinical speech into Japanese and find that training on cloned data outperforms raw cross-lingual transfer for depression and anxiety detection on real Japanese speech, suggesting voice cloning is a promising direction for augmenting clinical speech data in low-resource languages.

</details>

#### [Cycles of Discourse, Speech Dysfluency, and Active Inference](https://arxiv.org/abs/2607.22180) · [📄 Read](papers/2026/2607.22180.md)

**Thomas Parr, Birtan Demirel, Youssuf Saleh, Sanjay Manohar** · 2026-07-24

<details>
<summary>Abstract</summary>

Speech is a complex motor and social act. We must not only produce and understand sequences of variable-length words formed of ordered syllables but also speak and listen in turn. This theoretical paper introduces a computational model of speech production and auditory segmentation based upon sequences of discrete phonemes. The purpose of this is to develop a vehicle to test (in silico) hypotheses about the mechanisms that govern loss of speech fluency, something that may happen transiently in people who stutter or progressively in various neurodegenerative conditions. The modelling here appeals to Partially Observable Markov Decision Processes that provide a useful generic formulation for specifying the internal model our brains might use to describe dynamic environments in which they can exert partial control and make partial observations. The core features of the specific model used here are: (1) a reciprocal mapping from words to sequences of varying numbers of phonemes (2) a common subset of states for both speech generation and speech perception. A further novel feature is a social component, in which one must infer who is speaking (self or other). We propose a series of hypotheses about the computational mechanisms that might underwrite speech breakdown. For example, we demonstrate that reducing the precision in the next word introduces pauses and start-of-word repetitions of the sort associated with stuttering. We examine the patterns of behaviour and belief-updating predicted by each of these hypotheses, with implications for both speaking and listening. Finally, we discuss plausible neural substrates for the underlying message passing that might be amenable to interrogation with functional imaging.

</details>

</details>
<!-- PAPERS_TABLE_END -->
