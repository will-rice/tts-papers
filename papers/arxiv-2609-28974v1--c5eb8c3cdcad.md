---
identifier: arxiv:2609.28974v1
title: "Same Bit Width, Different Outcomes: Post-Training Quantization of Text-to-Speech Across Architectures"
authors:
  - Se Un Park
  - Yutae Kim
  - Junyoung Park
published: "2026-09-24T03:41:28+00:00"
url: https://arxiv.org/abs/2609.28974v1
source: arxiv
doi: null
arxiv_id: 2609.28974v1
categories:
  - cs.LG
  - cs.SD
  - eess.AS
---

# Same Bit Width, Different Outcomes: Post-Training Quantization of Text-to-Speech Across Architectures

Se Un Park^(∗)    Yutae Kim    Junyoung Park^(∗) ^(†)^(†)thanks:
^(∗)Corresponding authors.

###### Abstract

Post-training quantization (PTQ) reduces the cost of on-device
text-to-speech (TTS), but published evaluations cover one system or
method. We evaluate PTQ across TTS architectures under one protocol with
three core models, weight and activation ablations of eight more, and
two held-out models quantized blind. Four-bit per-channel weights reduce
UTMOS, a predicted mean opinion score, by 2.8 on Supertonic and 0.07 on
Kokoro, and per-tensor scaling can cause severe degradation even at 8
bits. The same bit width yields different outcomes, because the
sensitive component is model-specific and not reliably predicted from
the model class. A staged ablation procedure identifies it, and
per-layer GPTQ can restore it to within 0.1 UTMOS. Real int8 and int4
kernels reproduce the simulated ordering at hardware-dependent cost. On
a Mac mini, a 4-bit weight kernel runs Supertonic at 0.60$`\times`$ the
fp32 latency while int8 is slower, so each configuration requires
validation on the target runtime.

###### Index Terms: 

speech synthesis, post-training quantization, on-device inference, model
compression, edge computing

^(†)^(†)address: UX Factory, Inc.

## 1 Introduction

On-device text-to-speech (TTS) enables private and offline speech
synthesis under memory and compute constraints \[[1](#bib.bib1)\].
Post-training quantization (PTQ) compresses a trained model without
retraining \[[6](#bib.bib2), [14](#bib.bib3)\], but the bit width is
only one of several design choices. Scale sharing, the quantized
components, the activation precision, and the operator coverage of the
runtime each affect the outcome. Prior quantization studies cover a
single system, or several systems under a single
method \[[10](#bib.bib4), [28](#bib.bib5), [11](#bib.bib6)\], and no
study compares heterogeneous pretrained TTS pipelines,
quantized-component scopes, activation granularity, and measured
deployment paths under one protocol.

This paper provides that comparison and shows that the same bit width
yields different outcomes because the sensitive component is
model-specific. The study covers three core models, eight replication
models, and two models that were held out and quantized blind.

- •
  A cross-architecture sensitivity map. Component ablations under one
  protocol reveal model-specific weight sensitivity and interactions
  that amplify the whole-model degradation. Mixed-precision
  configurations reduce the UTMOS degradation, and per-layer GPTQ can
  restore the sensitive component.
- •
  Activation and combination results. Activation sensitivity depends on
  the scale granularity and on the quantized components. Per-channel
  8-bit activations add at most 0.09 UTMOS loss to the selected 4-bit
  configurations of the core models.
- •
  Deployment measurements. Real int8 and int4 execution shows that peak
  memory, latency, and energy depend on the runtime and the hardware
  (Sec. [4.6](#S4.SS6 "4.6 Deployment measurements ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")),
  which motivates the staged procedure tested blind in
  Sec. [4.7](#S4.SS7 "4.7 Staged procedure and blind application ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").

## 2 Related work

TTS compression includes architecture search in
LightSpeech \[[16](#bib.bib7)\], acoustic-model int8 PTQ combined with
architectural compression \[[9](#bib.bib8)\], and
BitTTS \[[10](#bib.bib4)\], which applies extreme ternary quantization
(1.58-bit training) and weight indexing to build compact TTS models for
on-device use and identifies the vocoder as the sensitive component of
its model. PTQ for diffusion models is established for image
generation \[[25](#bib.bib9), [12](#bib.bib10), [5](#bib.bib11)\] and
has been extended to audio generation by PTQ4ADM and timestep-aware
quantization \[[28](#bib.bib5), [11](#bib.bib6)\]. HAWQ ranks layers by
Hessian curvature for mixed precision in vision \[[4](#bib.bib12)\], and
Diet-KIT selects per-layer precision by sensitivity for speech
translation \[[15](#bib.bib13)\].

## 3 Experimental setup

Models and data. The core systems are Supertonic V3
(99M) \[[27](#bib.bib14)\], a flow-matching model with a vocoder,
OmniVoice (0.6B) \[[32](#bib.bib15)\], a masked-diffusion language model
(LM) with a token head and a codec decoder, and the feedforward model
Kokoro (82M) \[[7](#bib.bib16)\]. Their English floating-point (fp)
baselines reach UTMOS 4.473, 4.398, and 4.524 at WER 0.028, 0.032, and
0.030, respectively, on ONNX CPU fp32, torch Metal fp16, and torch x86
fp32, with a default number of function evaluations (NFE) of 8 for
Supertonic and 32 for OmniVoice. The replication models
(Fig. [1](#S4.F1 "Figure 1 ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"))
are the flow-matching F5-TTS \[[3](#bib.bib17)\], the feedforward
StyleTTS 2 \[[13](#bib.bib18)\] and MMS-TTS \[[20](#bib.bib19)\], and
the autoregressive codec-token LMs Zonos \[[26](#bib.bib20)\],
Dia \[[18](#bib.bib21)\], Orpheus \[[2](#bib.bib22)\], Kyutai
TTS \[[30](#bib.bib23)\], and CSM-1B \[[8](#bib.bib24)\]. Two further
models were held out until the procedure of
Sec. [4.7](#S4.SS7 "4.7 Staged procedure and blind application ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")
was fixed and then evaluated blind. Chatterbox \[[23](#bib.bib25)\]
combines a Llama backbone (T3, 503M) that emits speech tokens with a
flow-matching decoder (S3Gen, 112M) and a HiFT vocoder (21M). In
VoxCPM-0.5B \[[31](#bib.bib26)\], a MiniCPM-4 LM (434M) and a residual
acoustic LM (90M) drive a local encoder (60M), a local diffusion
transformer (DiT, 64M) that emits patches of continuous latents, and a
convolutional audio VAE decoder (75M). Each evaluated language uses the
same 200 frozen FLORES-200 devtest sentences \[[19](#bib.bib27)\] with
fixed per-utterance seeds, in English and, where supported, in Korean.
Each condition is paired with the unquantized model at its native
floating-point precision (fp)¹¹ 1 fp32 for Supertonic, Kokoro, F5-TTS,
StyleTTS 2, MMS-TTS, and Chatterbox, fp16 for OmniVoice and Dia, and
bf16 for Orpheus, Kyutai, CSM, VoxCPM, and the Zonos backbone, as
shipped. on the same platform and at the same number of sampling
steps.²² 2 Calibration uses FLORES-200 dev sentences that are disjoint
from the evaluation set. OmniVoice, which is evaluated in both
languages, uses 64 English and 64 Korean sentences, and the English-only
models of
Secs. [4.4](#S4.SS4 "4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")
and [4.7](#S4.SS7 "4.7 Staged procedure and blind application ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")
use 64 English sentences. Code, sentences, per-utterance scores, timing
records, pinned versions, seeds, calibration settings, and the
quantization specification of every run are available at
https://github.com/uxfacdev/tts-ptq-map.

Quantization. The weight-only sweep applies symmetric round-to-nearest
(RTN) quantization at 8, 6, and 4 bits with $`s=\max|w|/(2^{b-1}-1)`$
and 16-bit scale factors shared per tensor, per output channel (the
default), or per group of 128 consecutive weights within a channel
(group:128). Channels denote feature dimensions rather than audio
channels. A weight scale is shared per output feature of a linear layer
or per output filter of a convolution. A per-channel activation scale is
shared per input feature over all time steps, and a per-token activation
scale is shared per time step. Linear and convolution weights are
quantized, whereas biases, embeddings, and normalization parameters
remain in floating point. We quantize the whole model, individual
components, and mixed-precision combinations, and we sweep the NFE over
$`\{4,8,12\}`$ for Supertonic and $`\{4,8,16,32\}`$ for OmniVoice.
Simulated conditions dequantize the weights before execution and measure
quality only. Calibrated PTQ applies per-layer GPTQ \[[6](#bib.bib2)\]
or activation-aware weight scaling \[[14](#bib.bib3), [29](#bib.bib28)\]
to one component at a time, with input statistics collected from 64
English calibration sentences synthesized by the fp model
(Sec. [4.4](#S4.SS4 "4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).
Every other module of that component is quantized by RTN at the same bit
width and granularity. Simulated dynamic 8-bit activations (A8) are
added to W8 per-channel weights and to the W4 group:128 configurations.
For Supertonic the vocoder is excluded from weights and activations, for
Kokoro every module is quantized, and for OmniVoice the W4 configuration
(LM at W4, token head at W8, codec at fp) adds A8 to every module, on
x86 fp32 baselines for Supertonic and Kokoro and on a CUDA fp16 baseline
for OmniVoice. The replication models receive whole-model A8 at
per-channel and per-tensor scales and A8 on their W4 configurations.
Real 4-bit weight execution uses the block-wise 4-bit operator of ONNX
Runtime (MatMulNBits, block size 128) for Supertonic on x86, after the
dense $`1\times 1`$ convolutions of its flow estimator are rewritten as
matrix products so that the kernel covers 99.5% of the weights (7.6% as
shipped), and torchao int4 weight-only quantization (group 128, bf16
operands) for the LMs of OmniVoice, Orpheus, Kyutai, CSM, Chatterbox,
and VoxCPM on an RTX PRO 6000.

Quality and system measurements. UTMOS \[[24](#bib.bib29)\], a predicted
mean opinion score, is the proxy for English naturalness.
NISQA-TTS \[[17](#bib.bib30)\] and DNSMOS P.835 \[[22](#bib.bib31)\] on
251 runs are secondary proxies, compared with UTMOS by the Spearman
correlation of paired deltas over the conditions of one model. The
transcription error of faster-whisper large-v3 \[[21](#bib.bib32)\]
serves as the intelligibility proxy, reported as the per-utterance mean
word error rate (WER) for English and character error rate (CER) for
Korean. Paired 95% bootstrap intervals use 10,000 resamples over the 200
sentences, conditional on the evaluated settings. A quantized
configuration is defined to be quality-preserving on the two English
proxies when its paired $`\Delta`$UTMOS interval lies within
$`[-0.05,0.05]`$ and the upper endpoint of its paired $`\Delta`$WER
interval is at most $`0.01`$ relative to fp, evaluated at unrounded
endpoints.

Real CPU execution uses ONNX Runtime dynamic int8 for Supertonic and
PyTorch dynamic int8 for Kokoro on a Mac mini M4 Pro (4 threads, 20
sentences, 5 repeats). GPU measurements use torchao 0.18 with compiled
execution on A100, L4, and RTX PRO 6000 devices. The LM of OmniVoice
runs at 8-bit weights and activations (W8A8) and the LM of Orpheus at
weight-only int8, with the codecs in floating point, bf16 operands, and
compiled fp16 (OmniVoice) or bf16 (Orpheus) latency baselines. We
measure latency as the real-time factor (RTF), the peak CPU resident set
size (RSS), and the energy per second of audio. On the CPU, the energy
is the whole-chip energy above idle over the complete 20-sentence
process including model loading, whereas the RTF counts synthesis time
only, so $`E\neq P\times\mathrm{RTF}`$. On the GPU, the energy is the
NVML device energy without host power over twelve sentences and three
repeats (twenty and five at the matched operating point), excluding
loading and compilation.

## 4 Results

![Refer to caption](2609.28974v1/fig6.png)

Figure 1: Sensitivity map. Magnitude of the paired UTMOS loss at 4-bit
weights against each model’s own fp baseline for the whole model under
three scale granularities, for the most sensitive component alone at W4
per-channel (component, named in the row label), and for the rest of the
model at W4 per-channel with that component at fp (rest). OmniVoice uses
its CUDA fp16 baseline, and the last two rows are the held-out models of
Sec. [4.7](#S4.SS7 "4.7 Staged procedure and blind application ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").

### 4.1 Scale granularity and bit width

8-bit per-channel weights produce small changes on all three core
models, and the paired 95% intervals include zero. 6-bit weights yield
-0.56 $`\Delta`$UTMOS on Supertonic, -0.003 on Kokoro, and -0.03 on
OmniVoice. 4-bit weights reduce UTMOS by 2.8 on Supertonic and by 0.07
on Kokoro, whereas OmniVoice degrades substantially
(Fig. [1](#S4.F1 "Figure 1 ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).
At 4 bits, group:128 scaling raises the UTMOS of OmniVoice from 1.363
under per-tensor scaling to 3.761 but does not recover Supertonic. A
weight-domain signal-to-quantization-noise ratio estimate, in which the
largest weight of a scale-sharing group sets the quantization step,
gives per-channel scales a 10.6 dB advantage over per-tensor scales on
two released checkpoints, more than one additional bit provides.
Per-tensor scaling also degrades Kokoro (-3.15 $`\Delta`$UTMOS, WER
0.030 to 0.261) and W8 Supertonic (-1.642 at fp-level WER).

### 4.2 Component sensitivity and mixed precision

The vocoder of Supertonic alone yields -2.87 $`\Delta`$UTMOS at W4,
whereas its flow estimator alone yields -0.17. Keeping the vocoder at W8
with the rest at W4 restores UTMOS to 4.252 against 4.473 at fp. The
CUDA ablation of OmniVoice attributes more of the degradation to the
codec decoder (-0.68) than to the token head (-0.17) or the LM (-0.28).
Two components quantized together degrade UTMOS by more than the sum of
their individual losses, with -0.99 for the token head with the codec
and -0.93 for the LM with the token head (the rest column of
Fig. [1](#S4.F1 "Figure 1 ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).
Group:128 scaling improves the decoder-only result to -0.12, whereas the
vocoder of Supertonic remains degraded. The paired 95% intervals lie
within $`\pm`$0.03, $`\pm`$0.09, and $`\pm`$0.01 UTMOS of their
estimates for Supertonic, OmniVoice, and Kokoro, respectively, and
within $`\pm`$0.16 for the replication models.

Across the replication models
(Fig. [1](#S4.F1 "Figure 1 ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")),
group:128 scaling reduces the degradation of Zonos, StyleTTS 2, and
F5-TTS without establishing equivalence to fp, and it has no effect on
Kyutai. For Zonos and Dia the LM carries the loss, since the rest of the
model with the LM at fp loses only -0.05 and -0.27
(Fig. [1](#S4.F1 "Figure 1 ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).
Group:32 scaling does not improve the depth transformer of Kyutai (-2.99
against -2.99 per-channel), whereas 6-bit and 8-bit weights yield -1.38
and -0.02. The W4 decoder of StyleTTS 2 and the rest of its network
yield -0.11 and -0.20 separately but -0.64 together.

### 4.3 Sampling steps and matched baselines

Comparing every step count against a single default-step fp baseline
makes the quantization degradation of OmniVoice appear to decrease with
the number of steps
(Fig. [2](#S4.F2 "Figure 2 ‣ 4.3 Sampling steps and matched baselines ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")),
and pairing each quantized run with fp at the same NFE removes this
confound. Additional steps reduce the WER penalty under W4 (right panel)
without closing the UTMOS gap (left panel), which widens with the number
of steps on Supertonic.

Figure 2: W4 per-channel versus sampling steps (NFE). Left,
$`\Delta`$UTMOS of the W4 run against fp at the same NFE (matched,
solid) and against the single default-step fp run, fp@8 for Supertonic
and fp@32 for OmniVoice (dashed). Right, the matched relative WER
penalty in percent, the mean per-utterance WER of W4 over that of fp at
the same NFE, minus one.

### 4.4 Calibration controls

On the LM of OmniVoice, W4 group:128 GPTQ \[[6](#bib.bib2)\] yields
-0.029 $`\Delta`$UTMOS against -0.093 for RTN, and activation-aware
scaling \[[14](#bib.bib3), [29](#bib.bib28)\] yields -0.100. On the
token head and codec together, the best tested strength
($`\alpha=0.25`$) reduces the per-channel degradation to -0.64 against
-0.99, short of uncalibrated group:128 (-0.39), and no strength recovers
the vocoder of Supertonic.

Table [1](#S4.T1 "Table 1 ‣ 4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")
applies both methods to the vocoder of F5-TTS and the depth transformer
of Kyutai, the most sensitive component of each. Per-layer GPTQ recovers
both. At group:128 the vocoder degrades by -0.07 and the depth
transformer by -0.08 $`\Delta`$UTMOS with WER at fp, against -0.48 and
-2.98 for RTN, and the per-channel results lie between these values.
Scaling is less effective in every cell of
Table [1](#S4.T1 "Table 1 ‣ 4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
Calibration is therefore not a refinement of survivable configurations
but the step that recovers the sensitive component.

| Component                | Scales      | RTN       | Scaling   | GPTQ  |
| ------------------------ | ----------- | --------- | --------- | ----- |
| F5-TTS vocoder           | per-channel | -0.94     | -0.61     | -0.15 |
|                          | group:128   | -0.48     | -0.22     | -0.07 |
| Kyutai depth transformer | per-channel | -2.99^(a) | -1.82^(c) | -0.29 |
|                          | group:128   | -2.98^(b) | -0.20     | -0.08 |
| VoxCPM local DiT         | per-channel | -2.73^(d) | –         | -0.71 |
|                          | group:128   | -1.26     | –         | -0.41 |

Table 1: Calibrated PTQ on the most sensitive component of each model.
Paired $`\Delta`$UTMOS against the model’s own fp baseline under RTN,
activation-aware weight scaling ($`\alpha=0.5`$), and per-layer GPTQ at
per-channel and group:128 scales. WER stays at its fp level (0.035 for
F5-TTS, 0.034 for Kyutai, 0.043 for VoxCPM) in every cell except the
four marked ones, whose WER is ^(a)1.14, ^(b)1.01, ^(c)0.13, and
^(d)0.14.

### 4.5 Activation quantization

At the selected weight configurations, adding per-channel A8 changes the
mean UTMOS estimates by small amounts, with WER within 0.01 of fp. W8
with A8 yields -0.01, -0.07, and -0.06 $`\Delta`$UTMOS on Supertonic,
Kokoro, and OmniVoice, and the W4 configurations move from -0.10 to
-0.10, from -0.04 to -0.13, and from -0.11 to -0.18, respectively.
Per-tensor A8 on the vocoder of Supertonic alone, by contrast, yields
-2.98 at WER 1.30, which per-channel and per-token scales reduce to
-0.20 and -0.08. On OmniVoice, per-tensor A8 on the token head alone
yields -2.31, against -0.14 on the codec decoder alone and -0.95 on the
LM alone, so the most sensitive component moves from the codec decoder
under weight-only PTQ to the token head under per-tensor A8.

On the replication models, per-channel A8 on the whole model changes
UTMOS by at most 0.17 (CSM), and adding it to their W4 configurations
costs at most 0.12 (Orpheus). Per-tensor A8 severely degrades F5-TTS
(-3.10), Kyutai (-2.99), CSM (-2.64), and Zonos (-1.36), and degrades
the remaining four models by 0.08 to 0.29.

### 4.6 Deployment measurements

On the Mac mini M4 Pro, the ONNX Runtime dynamic int8 path of
Supertonic, which uses per-tensor activation scales, raises the WER from
0.028 to 1.11 and the Korean CER from 0.052 to 1.27 at 2.09$`\times`$
the fp32 latency
(Table [2](#S4.T2 "Table 2 ‣ 4.6 Deployment measurements ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).
An x86 control with int8 restricted to the MatMul operators and the
convolutions left in fp32 (MatMul-only) is quality-preserving (UTMOS
4.467, WER 0.029), so the operator coverage of the quantized graph
determines the outcome. Vocoder-excluded dynamic int8 keeps WER and CER
near fp (-0.041 $`\Delta`$UTMOS) at 1.47$`\times`$ the latency and 43%
more energy per audio-second
(Table [2](#S4.T2 "Table 2 ‣ 4.6 Deployment measurements ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).

|                         |       |                |          |       |      |
| ----------------------- | ----- | -------------- | -------- | ----- | ---- |
| Condition               | RTF   | $`\times`$fp   | RSS (MB) | P (W) | E    |
| Supertonic fp32 (NFE 8) | 0.148 | –              | 607      | 19.1  | 3.25 |
| dyn8 full (real int8)   | 0.310 | 2.09$`\times`$ | 329      | 9.7   | 3.21 |
| dyn8, vocoder excl.     | 0.218 | 1.47$`\times`$ | 436      | 19.1  | 4.64 |
| int4 W, vocoder excl.   | 0.089 | 0.60$`\times`$ | 360      | –     | –    |
| Kokoro fp32             | 0.069 | –              | 2712     | 7.5   | 0.99 |
| dyn8 (real int8)        | 0.077 | 1.12$`\times`$ | 2722     | 8.9   | 1.25 |

Table 2: System metrics on the quiet Mac mini M4 Pro over 5 repeats that
agree within 2%. RTF and its multiple of the fp row of the same model,
peak RSS, power P, and the marginal energy E of the whole 20-sentence
process in J per audio-second
(Sec. [3](#S3 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
not measured for the int4 row); dyn8 is dynamic int8.

The effects of compiled GPU int8 differ across models and devices.
Weight-only int8 on the LM of Orpheus runs 1.5$`\times`$ faster than
compiled bf16 at 34% less energy on an L4, whereas the sign of the
energy change of the W8A8 path of OmniVoice depends on the device. At
one fully controlled operating point (NFE 8, compiled, RTX PRO 6000, 200
sentences), compiled fp16, unquantized bf16, and W8A8 score within 0.02
UTMOS of one another, while W8A8 requires 1.11$`\times`$ the latency and
1.27$`\times`$ the energy of compiled fp16, against 0.96$`\times`$ and
0.98$`\times`$ for bf16.

Real 4-bit weight kernels reproduce the simulated ordering. Supertonic
under MatMulNBits degrades by -2.38 $`\Delta`$UTMOS with the vocoder
included and by -0.07 with the vocoder excluded (WER 0.033 against 0.028
at fp, Korean CER unchanged), against -0.10 for the simulated group:128
configuration. On the Mac mini, this vocoder-excluded 4-bit path runs at
0.60$`\times`$ the fp32 latency with 41% lower peak RSS
(Table [2](#S4.T2 "Table 2 ‣ 4.6 Deployment measurements ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")),
whereas the int8 path is slower than fp32. torchao int4 weight-only
quantization of the LM yields -0.14 on OmniVoice (simulated -0.09,
Korean CER +0.013 \[+0.001, +0.029\]), 0.01 on Orpheus, 0.00 on
Chatterbox, and 0.03 on VoxCPM, and it reproduces the severe degradation
of the depth transformer of Kyutai (-2.81) and the degradation of CSM
(-1.02). On the RTX PRO 6000, int4 on OmniVoice at NFE 8 requires
2.1$`\times`$ the latency and 2.2$`\times`$ the energy of compiled fp16,
whereas on the larger LM of Orpheus it runs at 0.50$`\times`$ the
latency and 0.45$`\times`$ the energy of bf16.

### 4.7 Staged procedure and blind application

The results suggest this order of evaluation. Apply separate
intelligibility and naturalness criteria against matched fp baselines,
evaluate weight-scale granularity at fixed precision
(Sec. [4.1](#S4.SS1 "4.1 Scale granularity and bit width ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")),
and where the degradation persists, identify the sensitive component by
ablation and protect it with higher precision or calibrated PTQ
(Secs. [4.2](#S4.SS2 "4.2 Component sensitivity and mixed precision ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")
and [4.4](#S4.SS4 "4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).
Then evaluate activation scaling on its own
(Sec. [4.5](#S4.SS5 "4.5 Activation quantization ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")),
the selected settings in combination, and finally quality and system
cost on the target runtime
(Sec. [4.6](#S4.SS6 "4.6 Deployment measurements ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).
Chatterbox and VoxCPM were quantized after this procedure was fixed,
with the sensitive component predicted from the sensitivity map and
recorded before any run (the vocoder for Chatterbox, the VAE decoder or
the LM for VoxCPM). Both predictions were incorrect. The procedure found
the flow-matching decoder in each case, which neither the model class
nor the parameter share predicted
(Fig. [1](#S4.F1 "Figure 1 ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")).
On Chatterbox, the T3 backbone alone yields -0.01 $`\Delta`$UTMOS at W4,
the flow decoder alone -2.17, and everything except the flow decoder
-0.42, which equals the sum of the individual losses. Group:128 scaling
reduces the flow-decoder loss to -0.55, keeping S3Gen at W8 with T3 at
W4 per-channel yields -0.02 at fp-level WER, and real int4 on T3 yields
0.00. On VoxCPM, the LM, the residual LM, the encoder, and the
projections change UTMOS by at most 0.10 in magnitude, whereas the local
DiT alone degrades by -2.73, the VAE decoder by -1.25, and everything
except the DiT by -1.75, which exceeds the sum of the individual losses.
Group:128 scaling reduces the VAE decoder loss to -0.25 but only halves
the DiT loss (-1.26). Per-layer GPTQ improves the DiT to -0.41 at
group:128 without reaching the quality-preserving band
(Table [1](#S4.T1 "Table 1 ‣ 4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")),
and the all-W4 configuration with both components calibrated yields
-1.01, whereas keeping both at W8 with the remainder at W4 group:128
yields -0.21 at fp-level WER. Real int4 on the LM yields 0.03.

### 4.8 Quality-preserving configurations

Nine configurations meet both conditions of
Sec. [3](#S3 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")
(five rows of
Table [3](#S4.T3 "Table 3 ‣ 4.8 Quality-preserving configurations ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
the W8 results of
Sec. [4.1](#S4.SS1 "4.1 Scale granularity and bit width ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
and the MatMul-only control of
Sec. [4.6](#S4.SS6 "4.6 Deployment measurements ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")),
three of them at 4 bits, namely Kokoro W4 group:128 and the Chatterbox
configuration and real int4 path. The other rows of
Table [3](#S4.T3 "Table 3 ‣ 4.8 Quality-preserving configurations ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures")
fail the UTMOS condition by 0.01 to 0.06 at fp-level WER, except the
Orpheus int4 path, which fails the WER condition by 0.002.

| Configuration                     | CI                     | WER⁺      |
| --------------------------------- | ---------------------- | --------- |
| Kokoro real int8 (PyTorch)        | \[-0.000, 0.003\]      | 0.001     |
| OmniVoice W8A8, compiled, NFE 8   | \[-0.038, 0.048\]      | 0.002     |
| Kokoro W4 group:128               | \[-0.039, -0.035\]     | 0.002     |
| Supertonic int8, no vocoder       | \[-0.056, -0.018\]^(∗) | 0.005     |
| Chatterbox T3 W4, S3Gen W8        | \[-0.032, 0.001\]      | 0.005     |
| Chatterbox real int4 on T3        | \[-0.012, 0.020\]      | 0.003     |
| Orpheus real int4 on the LM       | \[-0.022, 0.034\]      | 0.012^(∗) |
| Kyutai depth transf. W4 g128 GPTQ | \[-0.111, -0.058\]^(∗) | 0.006     |
| F5-TTS vocoder W4 g128 GPTQ       | \[-0.088, -0.046\]^(∗) | 0.004     |
| Supertonic int4 W, no vocoder     | \[-0.094, -0.042\]^(∗) | 0.009     |

Table 3: The quality-preserving criterion applied. The paired 95%
interval of $`\Delta`$UTMOS (CI) must lie within $`[-0.05,0.05]`$, and
the upper endpoint of the paired $`\Delta`$WER interval (WER⁺) must be
at most $`0.01`$, unrounded, against the fp baseline of each
configuration. An asterisk marks a violated condition.

## 5 Limitations

The two blind applications
(Sec. [4.7](#S4.SS7 "4.7 Staged procedure and blind application ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"))
test whether the procedure finds the sensitive component, not the
benefit of its ordering, and both held-out models share the codec-token
or latent-patch design of the sensitivity map. UTMOS is trained on
English. NISQA-TTS shows positive rank correlations with UTMOS across
the conditions of each English model (Spearman 0.79 to 0.97 on ten of
the eleven English baselines and 0.46 on StyleTTS 2), but the Korean
evidence in the text remains CER, and the reported UTMOS improvements
concern predicted naturalness only.³³ 3 An informal listening test (12
raters, 96 clips, clip-level Spearman $`\rho`$ = 0.91 with UTMOS) agrees
with UTMOS on severe degradation (condition MOS at most 2.0) but not
consistently on moderate differences. Listeners rated the VoxCPM
mixed-precision configuration above its DiT W4 group:128 GPTQ variant
despite the lower UTMOS, so the test validates neither moderate UTMOS
differences nor configuration rankings. The bootstrap intervals quantify
sentence sampling and do not correct for the selection of the best
strength or granularity on the test sentences. Across-seed standard
deviations of the paired $`\Delta`$UTMOS (22 conditions, ten models)
stay below 0.06.

## 6 Conclusion

Across three core, eight replication, and two held-out TTS models, the
same bit width yields different outcomes because the sensitive component
is model-specific and was not reliably predicted from the model class
alone. A staged ablation procedure with matched fp baselines identified
that component in two blind tests, and higher precision or per-layer
GPTQ can restore it to within 0.1 UTMOS of fp. The waveform decoder or
codec is the first component to test, and per-tensor scaling can cause
severe degradation even with 8-bit weights or activations.

## References

- \[1\] S. Achanta et al. (2021) On-device neural speech synthesis. In
  Proc. IEEE ASRU, pp. 1155–1161. Cited by:
  [§1](#S1.p1.1 "1 Introduction ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[2\] Canopy Labs (2025) Orpheus TTS: open-weight Llama-based speech
  synthesis (checkpoint orpheus-3b-0.1-ft). Note:
  https://github.com/canopyai/Orpheus-TTSAccessed 2026-09-08 Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[3\] Y. Chen et al. (2025) F5-TTS: a fairytaler that fakes fluent and
  faithful speech with flow matching. In Proc. 63rd Annual Meeting of
  the Association for Computational Linguistics (Volume 1: Long Papers),
  pp. 6255–6271. Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[4\] Z. Dong, Z. Yao, A. Gholami, M. W. Mahoney, and K.
  Keutzer (2019) HAWQ: hessian aware quantization of neural networks
  with mixed-precision. In Proc. IEEE/CVF ICCV, pp. 293–302. Cited by:
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[5\] W. Feng et al. (2025) MPQ-DM: mixed precision quantization for
  extremely low bit diffusion models. In Proc. AAAI Conf. on Artificial
  Intelligence, pp. 16595–16603. Cited by:
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[6\] E. Frantar, S. Ashkboos, T. Hoefler, and D. Alistarh (2023)
  OPTQ: accurate quantization for generative pre-trained transformers.
  In Proc. ICLR, Note: Known as GPTQ in its arXiv version Cited by:
  [§1](#S1.p1.1 "1 Introduction ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
  [§3](#S3.p2.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
  [§4.4](#S4.SS4.p1.1 "4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[7\] Hexgrad (2025) Kokoro-82M: an open-weight TTS model. Note:
  https://huggingface.co/hexgrad/Kokoro-82MAccessed 2026-08-28 Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[8\] B. Iribe, A. Kumar, and the Sesame team (2025) Crossing the
  uncanny valley of conversational voice. Note:
  https://www.sesame.com/research/crossing_the_uncanny_valley_of_voiceAccessed
  2026-09-08 Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[9\] K. Jain, E. Murphy, D. Gupta, J. Dyke, S. Shah, V. Tsiaras, P.
  Petkov, and A. Conkie (2025) Compact neural TTS voices for
  accessibility. In Proc. IEEE ICASSP, Cited by:
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[10\] M. Kawamura, T. Hasumi, Y. Shirahata, and R. Yamamoto (2025)
  BitTTS: highly compact text-to-speech using 1.58-bit quantization and
  weight indexing. In Proc. Interspeech, pp. 5538–5542. Cited by:
  [§1](#S1.p1.1 "1 Introduction ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[11\] T. Khandelwal and M. Fuentes (2025) Post-training quantization
  for audio diffusion transformers. In Proc. IEEE WASPAA, pp. 1–5. Cited
  by:
  [§1](#S1.p1.1 "1 Introduction ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[12\] X. Li et al. (2023) Q-Diffusion: quantizing diffusion models.
  In Proc. IEEE/CVF ICCV, pp. 17489–17499. Cited by:
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[13\] Y. A. Li, C. Han, V. S. Raghavan, G. Mischler, and N.
  Mesgarani (2023) StyleTTS 2: towards human-level text-to-speech
  through style diffusion and adversarial training with large speech
  language models. In Advances in Neural Information Processing Systems
  36 (NeurIPS), Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[14\] J. Lin et al. (2024) AWQ: activation-aware weight quantization
  for on-device LLM compression and acceleration. In Proc. MLSys, Vol.
  6, pp. 87–100. Cited by:
  [§1](#S1.p1.1 "1 Introduction ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
  [§3](#S3.p2.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
  [§4.4](#S4.SS4.p1.1 "4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[15\] D. Liu, S. Koneru, and J. Niehues (2026) Diet-KIT:
  post-training quantization for speech LLMs. In Proc. IWSLT,
  pp. 189–196. External Links:
  [Document](https://dx.doi.org/10.18653/v1/2026.iwslt-1.21) Cited by:
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[16\] R. Luo et al. (2021) LightSpeech: lightweight and fast text to
  speech with neural architecture search. In Proc. IEEE ICASSP,
  pp. 5699–5703. Cited by:
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[17\] G. Mittag and S. Möller (2020) Deep learning based assessment
  of synthetic speech naturalness. In Proc. Interspeech, pp. 1748–1752.
  Cited by:
  [§3](#S3.p3.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[18\] Nari Labs (2025) Dia-1.6B: dialogue text-to-speech (checkpoint
  Dia-1.6B-0626). Note: https://github.com/nari-labs/diaAccessed
  2026-09-08 Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[19\] NLLB Team et al. (2022) No language left behind: scaling
  human-centered machine translation. arXiv preprint arXiv:2207.04672.
  Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[20\] V. Pratap et al. (2024) Scaling speech technology to 1,000+
  languages. Journal of Machine Learning Research 25 (97), pp. 1–52.
  Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[21\] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, and I.
  Sutskever (2023) Robust speech recognition via large-scale weak
  supervision. In Proc. ICML, PMLR, Vol. 202, pp. 28492–28518. Cited by:
  [§3](#S3.p3.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[22\] C. K. A. Reddy, V. Gopal, and R. Cutler (2022) DNSMOS P.835: a
  non-intrusive perceptual objective speech quality metric to evaluate
  noise suppressors. In Proc. IEEE ICASSP, pp. 886–890. Cited by:
  [§3](#S3.p3.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[23\] Resemble AI (2025) Chatterbox-TTS. Note:
  https://github.com/resemble-ai/chatterboxGitHub repository Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[24\] T. Saeki, D. Xin, W. Nakata, T. Koriyama, S. Takamichi, and H.
  Saruwatari (2022) UTMOS: UTokyo-SaruLab system for VoiceMOS challenge 2022. In Proc. Interspeech, pp. 4521–4525. Cited by:
  [§3](#S3.p3.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[25\] Y. Shang, Z. Yuan, B. Xie, B. Wu, and Y. Yan (2023)
  Post-training quantization on diffusion models. In Proc. IEEE/CVF
  CVPR, pp. 1972–1981. Cited by:
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[26\] D. Sucic, M. Osman, G. Clark, C. Warner, and B. Millidge (2025)
  Zonos-v0.1: an expressive, open-source TTS model. Note:
  https://www.zyphra.com/post/beta-release-of-zonos-v0-1Accessed
  2026-09-08 Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[27\] Supertone Inc. (2026) Supertonic 3: lightning-fast, on-device,
  multilingual TTS. Note:
  https://github.com/supertone-inc/supertonicAccessed 2026-08-28 Cited
  by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[28\] J. Vora, A. Krishnan, N. Bouacida, P. R. Shankar, and P.
  Mohapatra (2025) PTQ4ADM: post-training quantization for efficient
  text conditional audio diffusion models. In Proc. IEEE ICASSP,
  pp. 1–5. Cited by:
  [§1](#S1.p1.1 "1 Introduction ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
  [§2](#S2.p1.1 "2 Related work ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[29\] G. Xiao, J. Lin, M. Seznec, H. Wu, J. Demouth, and S.
  Han (2023) SmoothQuant: accurate and efficient post-training
  quantization for large language models. In Proc. ICML, PMLR, Vol. 202,
  pp. 38087–38099. Cited by:
  [§3](#S3.p2.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures"),
  [§4.4](#S4.SS4.p1.1 "4.4 Calibration controls ‣ 4 Results ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[30\] N. Zeghidour et al. (2025) Streaming sequence-to-sequence
  learning with delayed streams modeling. arXiv preprint
  arXiv:2509.08753. Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[31\] Y. Zhou, G. Zeng, X. Liu, X. Li, R. Yu, Z. Wang, et al. (2025)
  VoxCPM: tokenizer-free TTS for context-aware speech generation and
  true-to-life voice cloning. arXiv preprint arXiv:2509.24650. Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
- \[32\] H. Zhu et al. (2026) OmniVoice: towards omnilingual zero-shot
  text-to-speech with diffusion language models. arXiv preprint
  arXiv:2604.00688. Cited by:
  [§3](#S3.p1.1 "3 Experimental setup ‣ Same Bit Width, Different Outcomes:Post-Training Quantization of Text-to-Speech Across Architectures").
