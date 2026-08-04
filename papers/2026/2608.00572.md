---
arxiv_id: "2608.00572"
title:
  "AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context
  Spectral Infilling"
authors:
  - Junchuan Zhao
  - Minh Duc Vu
  - Bowen Zhang
  - Ye Wang
submitted: "2026-08-01"
categories:
  - cs.SD
arxiv_url: https://arxiv.org/abs/2608.00572
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-04T07:10:38+00:00"
references_parsed: 0
arxiv_version: ""
---

# AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context Spectral Infilling

Junchuan Zhao¹, Minh Duc Vu², Bowen Zhang³, Ye Wang¹\corresponding

###### Abstract

Bandwidth extension (BWE) aims to recover missing high-frequency content from band-limited speech. Existing methods often formulate BWE as a fixed or predefined bandwidth conversion problem, potentially requiring cutoff-specific models or retraining when the input bandwidth changes. This assumption limits their applicability to practical scenarios where speech may arrive with diverse cutoff frequencies. We propose AnyBand, a unified BWE framework that recasts bandwidth extension as in-context spectral infilling. Motivated by prompt-based zero-shot speech generation, AnyBand conditions high-frequency generation on the observed low-frequency spectrum, using the available band as a frequency-domain prompt that conveys content, speaker, prosodic, and spectral-envelope cues. This formulation enables a single model to perform cutoff-conditioned generation over a continuous range of input bandwidths. AnyBand is trained with missing-band conditional flow matching and an Easy-to-Balanced cutoff curriculum over continuously sampled cutoff frequencies. To better exploit the spectral prompt, we introduce a frequency-aware Diffusion Transformer that models cross-frequency interactions and long-range temporal dependencies, followed by a physically motivated multi-view adversarial refinement stage to enhance spectral realism, envelope coherence, and harmonic consistency. Experiments on multiple datasets and bandwidth settings show that AnyBand consistently improves spectral reconstruction over existing baselines while achieving competitive perceptual quality across both standard and irregular input cutoffs. Audio samples are available¹¹1https://danny-nus.github.io/AnyBand-DemoPage/.

## Introduction

![Refer to caption](https://arxiv.org/html/2608.00572v1/x1.png)

Figure 1: Bandwidth extension as frequency-domain continuation across different cutoff frequencies.

Speech bandwidth is often constrained by acquisition devices, communication channels, compression systems, or legacy recording conditions. Bandwidth extension (BWE) aims to restore missing high-frequency content from band-limited speech, thereby improving clarity, naturalness, and perceptual quality. The task is inherently underdetermined, since multiple acoustically plausible high-frequency continuations may correspond to the same observed low-frequency signal (Yang et al. 2026). Despite substantial advances in neural speech restoration and generative audio modeling, supporting diverse and continuously varying input cutoffs within a single BWE system remains challenging.

Many neural BWE and audio super-resolution methods have improved high-frequency reconstruction under fixed or predefined bandwidth settings using convolutional, WaveNet-based, flow-based, diffusion-based, adversarial, or codec-based generative models  (Kuleshov et al. 2017; Gupta et al. 2019; Li et al. 2021; Su et al. 2021; Lee and Han 2021; Zhang et al. 2021; Lu et al. 2024a; Fang et al. 2025; Zhang et al. 2026). Although these approaches achieve strong performance within their target bandwidth configurations, their behavior is often closely coupled to the source–target bandwidth configurations covered during training. Adapting to a different input cutoff may therefore may require retraining, fine-tuning, or additional model specialization, limiting their flexibility in practical applications.

Recent works have explored unified, flexible, or blind BWE and audio super-resolution systems that support multiple sampling rates, bandwidths, degradation conditions, or unknown low-pass filters  (Andreev et al. 2023; Han and Lee 2022; Liu et al. 2022a, b, 2024; Salhab and Harmanani 2025; Sharma 2026; Moliner et al. 2024; Kim et al. 2024). Although these methods reduce the need for cutoff-specific models, they typically formulate varying bandwidths as separate restoration, upsampling, or conditioning scenarios. We instead cast multi-bandwidth BWE as a unified spectral-infilling problem, where the observed low-frequency spectrum provides acoustic context and a frequency mask specifies the missing region. As shown in Figure 1, different cutoffs correspond to different amounts of observed context under the same frequency-continuation formulation. The model then reconstructs the missing high-frequency content while preserving the harmonic structure, voicing patterns, spectral envelope, and temporal dynamics of the observed band.

We propose AnyBand, a unified framework that formulates BWE over continuously varying cutoff frequencies as in-context spectral infilling. Inspired by acoustic-context conditioning in prompt-based speech generation (Wang et al. 2023; Le et al. 2023; Chen et al. 2025; Eskimez et al. 2024; Zhao et al. 2026a; Liang et al. 2026; Zhao et al. 2026b), AnyBand treats the observed low-frequency spectrum as a frequency-domain prompt and uses an explicit frequency mask to specify the missing band. We refer to this formulation as in-context spectral infilling because the observed spectrum provides acoustic context for generating the unobserved frequency region. A frequency-aware Diffusion Transformer models cross-frequency interactions and long-range temporal dependencies, while Easy-to-Balanced cutoff training and endpoint-focused adversarial refinement improve performance across cutoff conditions and enhance the realism of the generated high-frequency content.

Our contributions are summarized as follows:

- •
  We formulate multi-bandwidth speech extension as an in-context spectral-infilling task, in which the observed low-frequency spectrum provides acoustic context and an explicit frequency mask specifies the missing region across continuously varying cutoff frequencies.
- •
  We propose a frequency-aware conditional flow architecture that explicitly models cross-frequency and long-range temporal dependencies, together with an Easy-to-Balanced curriculum for continuously sampled cutoff frequencies.
- •
  We introduce endpoint-focused multi-view adversarial refinement with complementary objectives for spectral realism, cross-band envelope coherence, and harmonic consistency.

## Related Work

### Speech Bandwidth Extension and Super-Resolution

Early neural BWE and audio super-resolution methods mainly learned direct waveform- or spectrum-level mappings from band-limited to full-band speech. (Kuleshov et al. 2017) introduced a convolutional waveform model, while TFNet (Lim et al. 2018) jointly modeled time- and frequency-domain representations. Later work further improved efficiency for real-time BWE (Li et al. 2021).

Generative methods were subsequently introduced to improve high-frequency reconstruction and perceptual quality, including autoregressive and neural-vocoder-based models (Gupta et al. 2019; Su et al. 2021), normalizing flows (Zhang et al. 2021), and diffusion models  (Lee and Han 2021). Other studies directly predict magnitude, phase, or complex spectra (Hu et al. 2020; Mandel et al. 2023; Lu et al. 2024a), often with adversarial supervision (Andreev et al. 2023; Lu et al. 2024a). Recent work also explores quantized or codec-derived latent spaces  (Fang et al. 2025; Zhang et al. 2026) and Schrödinger bridges  (Kong et al. 2025). However, many of these systems remain specialized for fixed or predefined source–target bandwidth settings.

### Unified and Flexible Bandwidth Extension

Recent studies have developed unified systems for multiple sampling rates, bandwidths, or degradation conditions. NU-Wave 2 (Han and Lee 2022) conditions a diffusion model on input bandwidth, while MS-BWE (Lu et al. 2024b) uses cascaded stages for flexible sampling-rate conversion. NVSR  (Liu et al. 2022a), VoiceFixer (Liu et al. 2022b), and AudioSR  (Liu et al. 2024) address broader super-resolution or restoration settings. Other work improves flexibility or efficiency through adversarial training, diffusion distillation, flow matching, or flexible vocoders  (Salhab and Harmanani 2025; Im and Nam 2025; Choi et al. 2026; Sharma 2026; Yun et al. 2025). Blind BWE further handles unknown degradations; BABE  (Moliner et al. 2024) jointly estimates a low-pass filter and reconstructs full-band audio, but requires inference-time optimization.

A related direction uses partial acoustic context to guide speech generation. Voicebox (Le et al. 2023) infills missing temporal segments, while E2 TTS  (Eskimez et al. 2024) and F5-TTS (Chen et al. 2025) use flow matching conditioned on observed or reference speech. Inspired by this principle, AnyBand treats the observed low-frequency spectrum as acoustic context and uses an explicit frequency mask to formulate varying cutoffs as a common spectral-infilling task.

## Proposed Method

![Refer to caption](https://arxiv.org/html/2608.00572v1/x2.png)

Figure 2: Overview of the proposed AnyBand framework. AnyBand encodes a noisy full-band spectral state together with a clean observed low-band prompt using a frequency encoder, models temporal dependencies with a DiT backbone, and predicts the mel-frequency velocity field using a frequency decoder. The model is trained with an Easy-to-Balanced cutoff curriculum and further refined using multi-view adversarial objectives.

### Problem Formulation: In-Context Spectral Infilling

Rather than treating each input cutoff as a separate source–target conversion setting, AnyBand formulates multi-bandwidth BWE as _in-context spectral infilling_. The observed low-frequency spectrum serves as acoustic context, while the masked high-frequency region specifies the region to be reconstructed. Let $`\mathbf{M}\in\mathbb{R}^{F\times T}`$ denote the target log-mel spectrogram, where $`F`$ and $`T`$ are the numbers of mel bins and temporal frames. Given cutoff frequency $`f_{c}`$ and its mel-bin index $`k_{c}`$, we define the missing-band mask $`\boldsymbol{\mathcal{M}}\in\{0,1\}^{F}`$ as $`\mathcal{M}_{k}=\mathds{1}[k>k_{c}]`$, where zeros and ones denote observed and missing bins, respectively. The masked observation is:

```math
\widetilde{\mathbf{M}}=\left(\mathbf{1}-\boldsymbol{\mathcal{M}}\right)\odot\mathbf{M},
```

with the mask broadcast over time. Thus, $`\widetilde{\mathbf{M}}`$ preserves the spectrum below $`f_{c}`$ and removes the region to be reconstructed.

The retained spectrum provides cues about content, speaker identity, prosody, and spectral structure, while its frequency extent specifies the BWE condition. Conditioned on the clean spectral prompt $`\widetilde{\mathbf{M}}`$ and auxiliary information $`\mathbf{c}`$, AnyBand models $`p_{\theta}(\mathbf{M}\mid\widetilde{\mathbf{M}},\mathbf{c})`$. The frequency mask is used to construct the prompt and identify the reconstruction region rather than being injected as a separate condition. Training over continuously varying cutoffs enables a single model to handle diverse bandwidth settings. At inference, the bandwidth is specified by the extent of the observed spectrum without requiring a separate scalar cutoff embedding.

### AnyBand

As illustrated in Figure 2, AnyBand adopts the temporal DiT backbone of F5-TTS (Chen et al. 2025). Given an intermediate noisy spectral state $`\mathbf{M}_{t}`$, the clean low-band prompt $`\widetilde{\mathbf{M}}`$, a timestep $`t`$, and auxiliary conditioning information $`\mathbf{c}`$, the generator directly predicts the velocity field as:

```math
\hat{\mathbf{v}}_{\theta}=\mathcal{G}_{\theta}\left(\mathbf{M}_{t},\widetilde{\mathbf{M}},t,\mathbf{c}\right).
```

To explicitly capture dependencies along the frequency axis, we augment the backbone with a frequency encoder and decoder placed before and after the temporal DiT, respectively.

#### DiT Backbone.

AnyBand retains the temporal DiT backbone of F5-TTS (Chen et al. 2025), including timestep conditioning and temporal self-attention, while replacing its frame-wise mel projections with the frequency encoder and decoder described below. Given the noisy spectral state $`\mathbf{M}_{t}`$ and clean masked observation $`\widetilde{\mathbf{M}}`$, the frequency encoder produces $`\mathbf{E}_{h}\in\mathbb{R}^{B\times T\times d}`$, which is processed by the DiT to model long-range temporal dependencies.

Following CodecFlow (Zhang et al. 2026), we further use F0 and voiced/unvoiced information as auxiliary conditions for high-frequency reconstruction. We define $`\mathbf{c}=[\mathbf{f}_{0};\mathbf{v}]`$, where $`\mathbf{f}_{0}\in\mathbb{R}^{B\times T}`$ is the normalized F0 trajectory and $`\mathbf{v}\in\{0,1\}^{B\times T}`$ is the voicing indicator. Their projected embeddings are added to $`\mathbf{E}_{h}`$ before temporal modeling. The resulting representations $`\mathbf{E}_{t}\in\mathbb{R}^{B\times T\times d}`$ are then mapped back to the mel-frequency domain by the frequency decoder.

#### Frequency Encoder and Decoder.

Bandwidth extension requires inferring missing high-frequency content from frequency-dependent cues in the observed spectrum, including harmonic structure, spectral envelopes, and cross-band continuity. AnyBand therefore models the frequency axis explicitly before and after the temporal DiT backbone.

For each frame, the frequency encoder treats the $`F`$ mel bins as frequency tokens. Values from the noisy intermediate state $`\mathbf{M}_{t}`$ and clean spectral prompt $`\widetilde{\mathbf{M}}`$ are concatenated, projected to $`d_{f}`$-dimensional embeddings, and combined with learned frequency positional embeddings, yielding $`\mathbf{E}_{M}^{(0)}\in\mathbb{R}^{B\times T\times F\times d_{f}}`$. A shallow stack of pre-normalization Transformer blocks then updates the tokens as:

$`\displaystyle\mathbf{E}_{M}^{(l)\prime}`$$`\displaystyle=\mathbf{E}_{M}^{(l-1)}+\operatorname{F\text{-}MHSA}\left(\operatorname{LN}\left(\mathbf{E}_{M}^{(l-1)}\right)\right),`$$`\displaystyle\mathbf{E}_{M}^{(l)}`$$`\displaystyle=\mathbf{E}_{M}^{(l)\prime}+\operatorname{FFN}\left(\operatorname{LN}\left(\mathbf{E}_{M}^{(l)\prime}\right)\right),`$

where $`\operatorname{F\text{-}MHSA}`$ applies self-attention along the frequency axis independently at each frame. The final frequency tokens are aggregated through attention pooling and projected to the DiT hidden dimension, producing $`\mathbf{E}_{h}\in\mathbb{R}^{B\times T\times d}`$.

After temporal modeling, the frequency decoder maps $`\mathbf{E}_{t}\in\mathbb{R}^{B\times T\times d}`$ back to the mel-frequency domain. Each frame representation is projected to the frequency hidden dimension, broadcast over $`F`$ frequency positions, and combined with learned frequency embeddings. The resulting tokens are processed by a frequency-axis Transformer stack and mapped through a shared linear readout to produce $`\hat{\mathbf{v}}_{\theta}`$. Thus, the encoder aggregates cross-frequency evidence into frame-level representations, while the decoder predicts frequency-specific velocities.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x3.png)

Figure 3: Overview of the proposed discriminators, which jointly assess multi-scale spectral realism, cross-band envelope dependencies, and $`F_{0}`$-aligned harmonic correspondence.

#### Multi-View Spectral Discriminators.

Although the masked flow-matching objective provides stable reconstruction supervision, its pointwise loss may underemphasize perceptually important high-frequency details. Inspired by adversarial training in neural speech generation  (Kong et al. 2020; Lee et al. 2023; Jang et al. 2021; Lee et al. 2024), we introduce three complementary discriminators: $`\mathcal{D}_{\mathrm{spec}}`$, $`\mathcal{D}_{\mathrm{cross}}`$, and $`\mathcal{D}_{\mathrm{harm}}`$, targeting spectral realism, cross-band envelope coherence, and harmonic correspondence, respectively.

The multi-scale spectral discriminator $`\mathcal{D}_{\mathrm{spec}}`$ follows common multi-scale designs  (Kong et al. 2020; Jang et al. 2021). Given a mel spectrogram $`\mathbf{M}`$, we construct three inputs at temporal scales of $`1`$, $`1/2`$, and $`1/4`$ by average pooling along time while preserving frequency resolution. Independent branches then evaluate local time–frequency patterns under different temporal receptive fields.

Motivated by cross-frequency envelope coherence in natural sounds  (Nelken et al. 1999; McDermott and Simoncelli 2011), the cross-band discriminator $`\mathcal{D}_{\mathrm{cross}}`$ evaluates whether reconstructed high-frequency bands follow the temporal dynamics of the observed low-frequency spectrum. We partition the $`F`$ mel bins into $`K`$ contiguous subbands $`\{\mathcal{B}_{j}\}_{j=1}^{K}`$ and compute the envelope of the $`j`$-th subband as:

```math
\mathbf{E}_{s}^{(j)}=\frac{1}{|\mathcal{B}_{j}|}\sum_{k\in\mathcal{B}_{j}}\mathbf{M}_{k,:}.
```

After temporal standardization, the subband envelopes form $`\mathbf{E}_{s}\in\mathbb{R}^{K\times T}`$. We further compute the observed fraction of each subband and the low-band reference envelope as:

$`\displaystyle\rho_{j}`$$`\displaystyle=\frac{1}{|\mathcal{B}_{j}|}\sum_{k\in\mathcal{B}_{j}}\left(1-\mathcal{M}_{k}\right),`$$`\displaystyle\mathbf{E}_{l}`$$`\displaystyle=\sum_{j=1}^{K}\frac{\rho_{j}}{\sum_{i=1}^{K}\rho_{i}+\epsilon}\overline{\mathbf{E}}_{s}^{(j)},`$

where $`\overline{\mathbf{E}}_{s}^{(j)}`$ denotes the standardized envelope. Their element-wise products are locally averaged over time to form a cross-band coherence map, which is combined with the observed-fraction map and fed to $`\mathcal{D}_{\mathrm{cross}}`$.

Inspired by F0-guided source modeling  (Lu et al. 2022; Li et al. 2023; Xu et al. 2025), the harmonic discriminator $`\mathcal{D}_{\mathrm{harm}}`$ evaluates whether reconstructed high-frequency energy is consistent with the harmonic structure implied by F0 and voicing. At frame $`\tau`$, the $`n`$-th harmonic frequency is $`f_{n}(\tau)=nf_{0}(\tau)`$. Bilinear sampling along these trajectories yields an $`F_{0}`$-aligned harmonic feature grid $`\mathbf{H}\in\mathbb{R}^{N_{h}\times T}`$, which is stacked with an observed-harmonic mask and a voiced/unvoiced map before being passed to $`\mathcal{D}_{\mathrm{harm}}`$. All three discriminators are implemented with lightweight 2D CNNs.

### Training and Sampling

#### Easy-to-Balanced Cutoff Training.

Uniform sampling from the beginning may expose the model to severely band-limited inputs before it has learned basic spectral continuation. We therefore introduce an Easy-to-Balanced curriculum that initially favors higher cutoffs and gradually transitions to uniform sampling. Given the normalized cutoff $`\widetilde{f}=(f_{c}-f_{\min})/(f_{\max}-f_{\min})\in[0,1]`$, we sample:

$`\displaystyle p_{s}(\widetilde{f})`$$`\displaystyle=(1-\lambda_{s})\frac{\beta e^{\beta\widetilde{f}}}{e^{\beta}-1}+\lambda_{s},`$$`\displaystyle\lambda_{s}`$$`\displaystyle=\frac{1-\cos\!\left(\pi\min\left(\frac{s}{\rho S},1\right)\right)}{2},`$

where $`\beta`$ controls the initial high-cutoff bias, $`S`$ is the total number of training steps, and $`\rho`$ controls the annealing duration. The sampled cutoff is mapped to the corresponding mel-bin boundary to construct the frequency mask. As training progresses, the distribution smoothly approaches uniform sampling over the full cutoff range.

#### Missing-Band Flow Training.

Following conditional flow matching (Lipman et al. 2023), we sample $`t\in[0,1)`$ and Gaussian noise $`\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I})`$, and construct the intermediate noisy state:

```math
\mathbf{M}_{t}=t\mathbf{M}+(1-t)\boldsymbol{\epsilon}.
```

The clean masked observation $`\widetilde{\mathbf{M}}`$ remains uncorrupted and is provided separately as the spectral prompt. Under this linear probability path, the target velocity is:

```math
\mathbf{v}=\frac{\mathbf{M}-\mathbf{M}_{t}}{1-t}=\mathbf{M}-\boldsymbol{\epsilon}.
```

The generator directly predicts $`\hat{\mathbf{v}}_{\theta}=\mathcal{G}_{\theta}(\mathbf{M}_{t},\widetilde{\mathbf{M}},t,\mathbf{c})`$. Since the observed low-frequency region is already provided through $`\widetilde{\mathbf{M}}`$, the training objective is applied only to the missing frequency region:

```math
\mathcal{L}_{\mathrm{flow}}=\mathbb{E}\left[\frac{\left\|\boldsymbol{\mathcal{M}}\odot\left(\mathbf{v}-\hat{\mathbf{v}}_{\theta}\right)\right\|_{2}^{2}}{T\cdot\sum_{k=1}^{F}\mathcal{M}_{k}}\right],
```

where the expectation is taken over training samples, cutoff frequencies, flow times, and Gaussian noise. The normalization by the number of missing time–frequency elements keeps the loss scale comparable across different cutoff frequencies.

#### Adversarial Refinement.

After flow pretraining, we refine the generator with the proposed multi-view spectral discriminators. Under the velocity-prediction parameterization, the generator directly predicts $`\hat{\mathbf{v}}_{\theta}`$. At an intermediate timestep $`t`$, the corresponding clean-spectrogram estimate is recovered as:

```math
\hat{\mathbf{M}}=\mathbf{M}_{t}+(1-t)\hat{\mathbf{v}}_{\theta}.
```

Rather than applying adversarial supervision to arbitrary intermediate states, we construct fake samples from the model’s own sampling trajectory. We first integrate from Gaussian noise to an endpoint-near timestep $`t_{e}`$ without gradient tracking, and then back-propagate through a short differentiable rollout toward the data endpoint. The generated spectrogram is combined with the observed band as:

```math
\hat{\mathbf{M}}_{\mathrm{fb}}=(1-\boldsymbol{\mathcal{M}})\odot\widetilde{\mathbf{M}}+\boldsymbol{\mathcal{M}}\odot\hat{\mathbf{M}},
```

so that the known region is copied from the input and only the missing band is supplied by the model.

We apply adversarial refinement near the endpoint because earlier flow states are noisy intermediate variables rather than natural spectrograms  (Lipman et al. 2023). This allows the discriminators to focus on spectral realism and high-frequency detail without back-propagating through the full ODE trajectory, following recent adversarial flow-matching audio generation  (Lee et al. 2024).

Let $`\mathcal{Q}=\{\mathrm{spec},\mathrm{cross},\mathrm{harm}\}`$ denote the discriminator set. For each $`\mathcal{D}_{q}`$, we use a hinge GAN loss with generator objective $`\mathcal{L}_{\mathrm{adv}}^{(q)}=-\mathbb{E}[\mathcal{D}_{q}(\hat{\mathbf{M}}_{\mathrm{fb}})]`$, together with feature matching $`\mathcal{L}_{\mathrm{fm}}^{(q)}`$. The generator is optimized with:

```math
\mathcal{L}_{G}=\mathcal{L}_{\mathrm{flow}}+\lambda_{\mathrm{adv}}\sum_{q\in\mathcal{Q}}\mathcal{L}_{\mathrm{adv}}^{(q)}+\lambda_{\mathrm{fm}}\sum_{q\in\mathcal{Q}}\mathcal{L}_{\mathrm{fm}}^{(q)}.
```

#### Sampling.

At inference time, AnyBand initializes the full-band state with Gaussian noise and solves the learned conditional flow over an inference time grid $`0=t_{0}<\cdots<t_{N}=1`$, while the clean observed low-frequency spectrum is provided separately as the spectral prompt. At the $`i`$-th integration step, the generator directly predicts the conditional and unconditional velocity fields, $`\hat{\mathbf{v}}^{\mathrm{cond}}_{i}`$ and $`\hat{\mathbf{v}}^{\emptyset}_{i}`$, respectively. We apply classifier-free guidance in the velocity space as:

```math
\hat{\mathbf{v}}^{\mathrm{cfg}}_{i}=\hat{\mathbf{v}}^{\emptyset}_{i}+w_{\mathrm{cfg}}\left(\hat{\mathbf{v}}^{\mathrm{cond}}_{i}-\hat{\mathbf{v}}^{\emptyset}_{i}\right),
```

where $`w_{\mathrm{cfg}}`$ denotes the guidance scale. The guided velocity field is integrated using the Heun solver. After the final integration step, the observed low-frequency region is restored from the input prompt, while the generated result is retained in the missing high-frequency region.

## Experiment Settings

| Input SR | Method         | VCTK               |                       |                       |                    |                  |                   | EARS               |                       |                       |                    |                  |                   |
| -------- | -------------- | ------------------ | --------------------- | --------------------- | ------------------ | ---------------- | ----------------- | ------------------ | --------------------- | --------------------- | ------------------ | ---------------- | ----------------- |
|          |                | LSD $`\downarrow`$ | LF-LSD $`\downarrow`$ | HF-LSD $`\downarrow`$ | NISQA $`\uparrow`$ | COL $`\uparrow`$ | STOI $`\uparrow`$ | LSD $`\downarrow`$ | LF-LSD $`\downarrow`$ | HF-LSD $`\downarrow`$ | NISQA $`\uparrow`$ | COL $`\uparrow`$ | STOI $`\uparrow`$ |
| 2 kHz    | NU-Wave 2      | 2.685              | 1.364                 | 2.727                 | 1.897              | 2.115            | 0.7746            | 4.039              | 2.145                 | 4.100                 | 2.012              | 2.401            | 0.7285            |
|          | AudioSR        | 2.373              | 0.833                 | 2.417                 | 2.356              | 2.621            | 0.7913            | 1.958              | 1.408                 | 1.971                 | 2.003              | 2.467            | 0.7444            |
|          | FLowHigh       | 1.637              | 0.985                 | 1.655                 | 1.840              | 2.099            | 0.7885            | 2.304              | 1.775                 | 2.319                 | 1.622              | 1.565            | 0.7687            |
|          | Fre-Painter    | 1.323              | 1.008                 | 1.331                 | 2.697              | 2.422            | 0.7820            | 2.568              | 1.730                 | 2.595                 | 2.552              | 2.510            | 0.7748            |
|          | AnyBand (Ours) | 1.248              | 0.539                 | 1.269                 | 3.125              | 3.419            | 0.8214            | 1.546              | 0.534                 | 1.584                 | 3.109              | 2.973            | 0.8067            |
| 4 kHz    | NU-Wave 2      | 2.552              | 1.258                 | 2.636                 | 2.806              | 3.168            | 0.8811            | 3.908              | 1.971                 | 4.036                 | 2.859              | 3.226            | 0.8372            |
|          | AudioSR        | 1.628              | 0.544                 | 1.691                 | 3.865              | 3.700            | 0.8996            | 1.291              | 0.537                 | 1.337                 | 3.739              | 3.886            | 0.8875            |
|          | FLowHigh       | 1.249              | 0.808                 | 1.277                 | 3.784              | 3.704            | 0.9291            | 2.418              | 1.516                 | 2.481                 | 3.297              | 3.400            | 0.9069            |
|          | Fre-Painter    | 1.286              | 0.873                 | 1.312                 | 3.539              | 3.408            | 0.9141            | 2.441              | 1.526                 | 2.503                 | 3.057              | 2.985            | 0.9077            |
|          | AnyBand (Ours) | 1.180              | 0.527                 | 1.219                 | 4.038              | 3.966            | 0.9356            | 1.187              | 0.543                 | 1.231                 | 3.690              | 3.681            | 0.9205            |
| 8 kHz    | NU-Wave 2      | 2.391              | 1.248                 | 2.551                 | 3.100              | 3.397            | 0.9835            | 3.743              | 1.939                 | 4.001                 | 3.142              | 3.393            | 0.9433            |
|          | AudioSR        | 1.528              | 0.542                 | 1.654                 | 3.937              | 3.732            | 0.9777            | 1.173              | 0.558                 | 1.256                 | 3.774              | 3.671            | 0.9713            |
|          | FLowHigh       | 1.228              | 0.814                 | 1.286                 | 4.002              | 4.015            | 0.9877            | 2.337              | 1.492                 | 2.464                 | 3.825              | 3.769            | 0.9845            |
|          | Fre-Painter    | 1.208              | 0.851                 | 1.258                 | 3.831              | 3.764            | 0.9861            | 2.351              | 1.478                 | 2.478                 | 3.715              | 3.670            | 0.9836            |
|          | AnyBand (Ours) | 1.086              | 0.514                 | 1.155                 | 4.014              | 3.983            | 0.9870            | 1.038              | 0.526                 | 1.132                 | 3.834              | 3.737            | 0.9847            |
| 16 kHz   | NU-Wave 2      | 2.065              | 1.287                 | 2.344                 | 3.716              | 3.578            | 0.9972            | 3.526              | 1.999                 | 4.068                 | 3.296              | 3.212            | 0.9553            |
|          | AudioSR        | 1.415              | 0.639                 | 1.644                 | 3.828              | 3.921            | 0.9967            | 1.009              | 0.608                 | 1.150                 | 3.799              | 3.698            | 0.9966            |
|          | FLowHigh       | 1.140              | 0.833                 | 1.246                 | 3.723              | 3.870            | 0.9989            | 2.318              | 1.473                 | 2.626                 | 3.845              | 3.876            | 0.9990            |
|          | Fre-Painter    | 1.137              | 0.909                 | 1.212                 | 3.869              | 3.772            | 0.9996            | 2.299              | 1.490                 | 2.592                 | 3.916              | 3.836            | 0.9995            |
|          | AnyBand (Ours) | 0.974              | 0.567                 | 1.092                 | 3.936              | 3.837            | 0.9992            | 0.986              | 0.583                 | 1.055                 | 3.922              | 3.875            | 0.9964            |

Table 1: Quantitative bandwidth-extension results on the in-domain VCTK and out-of-domain EARS test sets. All systems generate audio at 48 kHz. The best and second-best results within each input setting are highlighted in bold and underlined, respectively.

| Input SR | Method         | LSD $`\downarrow`$ | HF-LSD $`\downarrow`$ | NISQA $`\uparrow`$ | COL $`\uparrow`$ | STOI $`\uparrow`$ |
| -------- | -------------- | ------------------ | --------------------- | ------------------ | ---------------- | ----------------- |
| 3 kHz    | NU-Wave 2      | 2.598              | 2.661                 | 2.244              | 2.357            | 0.8291            |
|          | AudioSR        | 1.643              | 1.690                 | 3.318              | 3.118            | 0.8495            |
|          | FlowHigh       | 1.548              | 1.575                 | 2.394              | 2.302            | 0.8412            |
|          | Fre-Painter    | 1.298              | 1.315                 | 2.995              | 2.687            | 0.8502            |
|          | AnyBand (Ours) | 1.228              | 1.261                 | 3.671              | 3.702            | 0.8523            |
| 6 kHz    | NU-Wave 2      | 2.462              | 2.586                 | 3.172              | 3.497            | 0.9442            |
|          | AudioSR        | 1.585              | 1.680                 | 3.915              | 3.818            | 0.9500            |
|          | FlowHigh       | 1.234              | 1.278                 | 3.948              | 3.891            | 0.9502            |
|          | Fre-Painter    | 1.259              | 1.302                 | 3.654              | 3.546            | 0.9541            |
|          | AnyBand (Ours) | 1.123              | 1.177                 | 4.060              | 4.002            | 0.9575            |
| 12 kHz   | NU-Wave 2      | 2.207              | 2.428                 | 3.219              | 2.803            | 0.9903            |
|          | AudioSR        | 1.458              | 1.635                 | 3.878              | 3.801            | 0.9955            |
|          | FlowHigh       | 1.183              | 1.263                 | 3.996              | 3.944            | 0.9963            |
|          | Fre-Painter    | 1.198              | 1.255                 | 3.849              | 3.785            | 0.9952            |
|          | AnyBand (Ours) | 1.002              | 1.093                 | 3.987              | 3.920            | 0.9968            |
| 15 kHz   | NU-Wave 2      | 2.094              | 2.360                 | 3.558              | 3.396            | 0.9912            |
|          | AudioSR        | 1.415              | 1.644                 | 3.866              | 3.725            | 0.9967            |
|          | FlowHigh       | 1.151              | 1.251                 | 3.710              | 3.656            | 0.9990            |
|          | Fre-Painter    | 1.167              | 1.242                 | 3.954              | 3.868            | 0.9993            |
|          | AnyBand (Ours) | 0.975              | 1.085                 | 3.975              | 3.894            | 0.9987            |

Table 2: Quantitative generalization results on VCTK with irregular input bandwidths. Input sampling rates of 3, 6, 12, and 15 kHz correspond to Nyquist cutoffs of 1.5, 3, 6, and 7.5 kHz, respectively. The best and second-best results are highlighted in bold and underlined, respectively.

### Datasets

We conduct experiments on the 48-kHz VCTK (Yamagishi et al. 2019")) and EARS (Richter et al. 2024) datasets. VCTK speakers p225–p228 are held out for in-domain evaluation, while the remaining speakers are used for training. For out-of-domain evaluation, we use 50 utterances from 10 EARS speakers. Band-limited inputs are constructed by masking mel bins above a given cutoff. Cutoffs are sampled continuously during training and evaluated under both standard and irregular settings. The reported input sampling rate equals twice the cutoff frequency.

### Implementation Details

We use 128-bin mel spectrograms computed at 48 kHz with a 2,048-point FFT and a hop length of 256. AnyBand contains 8 temporal DiT blocks with hidden dimension 384 and 6 attention heads. Its frequency encoder and decoder each use 2 frequency-axis attention blocks with hidden dimension 64 and 4 heads. Following PACE (Zhao et al. 2025), frame-level F0 and voiced/unvoiced features extracted from the input speech are used as auxiliary conditions. All discriminators are lightweight 2D CNNs with Leaky-ReLU activations; branches with the same architecture use independent parameters. Training uses AdamW on eight NVIDIA L40S GPUs with a batch size of 32 per GPU. We train the flow model for 300 epochs with the Easy-to-Balanced cutoff curriculum, using $`\rho=0.7`$ and $`\beta=4`$, followed by 200 epochs of adversarial refinement with uniformly sampled continuous cutoffs. At inference, we use the Heun solver with 50 steps and a classifier-free guidance scale of 1.4. Generated mel spectrograms are converted to 48-kHz waveforms using Vocos²²2https://huggingface.co/kittn/vocos-mel-48khz-alpha1  (Siuzdak 2024).

### Evaluation Metrics

We evaluate spectral reconstruction using log-spectral distance (LSD) (Gray and Markel 1976) and its low- and high-frequency variants  (Han and Lee 2022). LSD is computed over the full spectrum, while LF-LSD and HF-LSD measure distortion in the observed and missing frequency regions, respectively. Lower values indicate better reconstruction. We further report NISQA and its coloration dimension (COL) (Mittag et al. 2021) for overall perceptual quality and frequency-response distortion, and STOI (Taal et al. 2011) for intelligibility preservation. For subjective evaluation, 15 listeners rated the sound quality of outputs from each system and the ground truth on a five-point scale, using five utterances at each input sampling rate of 8, 12, 16, 20, and 24 kHz.

## Results

### Main Results

#### Objective Results.

Table 1 compares AnyBand with representative bandwidth-extension systems (Han and Lee 2022; Liu et al. 2024; Kim et al. 2024; Yun et al. 2025) on the in-domain VCTK and out-of-domain EARS test sets. AnyBand achieves the lowest LSD and HF-LSD across all tested cutoff settings, demonstrating consistently strong full-band and high-frequency reconstruction. Its low LF-LSD further suggests that the observed low-frequency content is well preserved. The spectral gains remain consistent on EARS, indicating good cross-domain generalization, and are most pronounced under severely band-limited conditions. At higher input bandwidths, the differences in perceptual metrics become smaller, but AnyBand remains competitive in NISQA, COL, and STOI while retaining a clear spectral advantage.

Table 2 further evaluates performance at irregular cutoff settings within the continuous training range. AnyBand achieves the best LSD and HF-LSD at every tested cutoff, confirming that a single model can support nonstandard bandwidth configurations without cutoff-specific specialization. The improvements are again larger at lower cutoffs, where a greater portion of the spectrum must be reconstructed, while perceptual quality and intelligibility remain competitive. Overall, these results support mask-specified spectral infilling as an effective formulation for flexible BWE across both standard and irregular cutoff settings.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x4.png)

Figure 4: Subjective scores across different input sampling rates. The dashed horizontal line denotes the ground-truth score, and error bars indicate 95% confidence intervals.

#### Subjective Evaluation.

Figure 4 shows that AnyBand achieves the highest subjective quality at most input sampling rates and remains competitive across all evaluated bandwidths. Its advantage is more evident for severely band-limited inputs, indicating stronger perceptual reconstruction when a larger portion of the spectrum is missing. At higher input sampling rates, the differences among methods become smaller, while all systems remain below the ground-truth quality.

| Input SR | Sampling strategy    | LSD $`\downarrow`$ | HF-LSD $`\downarrow`$ | NISQA $`\uparrow`$ | COL $`\uparrow`$ | STOI $`\uparrow`$ |
| -------- | -------------------- | ------------------ | --------------------- | ------------------ | ---------------- | ----------------- |
| 2 kHz    | Uniform (discrete)   | 1.284              | 1.302                 | 3.165              | 3.232            | 0.8224            |
|          | Uniform (continuous) | 1.358              | 1.386                 | 2.807              | 3.036            | 0.8052            |
|          | Easy-to-balanced     | 1.248              | 1.269                 | 3.125              | 3.419            | 0.8214            |
| 4 kHz    | Uniform (discrete)   | 1.216              | 1.260                 | 3.855              | 3.659            | 0.9287            |
|          | Uniform (continuous) | 1.248              | 1.295                 | 3.698              | 3.567            | 0.9185            |
|          | Easy-to-balanced     | 1.180              | 1.219                 | 4.038              | 3.966            | 0.9356            |
| 8 kHz    | Uniform (discrete)   | 1.101              | 1.143                 | 3.907              | 3.839            | 0.9861            |
|          | Uniform (continuous) | 1.132              | 1.199                 | 3.826              | 3.799            | 0.9842            |
|          | Easy-to-balanced     | 1.086              | 1.155                 | 4.014              | 3.983            | 0.9870            |
| 16 kHz   | Uniform (discrete)   | 0.970              | 1.080                 | 4.011              | 3.926            | 0.9993            |
|          | Uniform (continuous) | 0.993              | 1.094                 | 3.847              | 3.706            | 0.9980            |
|          | Easy-to-balanced     | 0.974              | 1.092                 | 3.936              | 3.837            | 0.9992            |
| Avg.     | Uniform (discrete)   | 1.143              | 1.196                 | 3.735              | 3.664            | 0.9341            |
|          | Uniform (continuous) | 1.183              | 1.244                 | 3.545              | 3.527            | 0.9265            |
|          | Easy-to-balanced     | 1.122              | 1.184                 | 3.778              | 3.801            | 0.9358            |

Table 3: Ablation study of cutoff-sampling strategies on VCTK. Input sampling rates of 2, 4, 8, and 16 kHz correspond to Nyquist cutoffs of 1, 2, 4, and 8 kHz, respectively. The output sampling rate is 48 kHz. The best and second-best results within each input setting are highlighted in bold and underlined, respectively.

| Variants                                   | LSD $`\downarrow`$ | HF-LSD $`\downarrow`$ | NISQA $`\uparrow`$ | COL $`\uparrow`$ | STOI $`\uparrow`$ |
| ------------------------------------------ | ------------------ | --------------------- | ------------------ | ---------------- | ----------------- |
| AnyBand (Ours)                             | 0.974              | 1.092                 | 3.936              | 3.837            | 0.9992            |
| $`-`$ w/o Freq. Modules                    | 1.038              | 1.159                 | 3.772              | 3.656            | 0.9978            |
| $`-`$ w/o F0/UV                            | 1.035              | 1.125                 | 3.758              | 3.698            | 0.9985            |
| $`-`$ w/o $`\mathcal{D}_{\mathrm{spec}}`$  | 1.124              | 1.206                 | 3.673              | 3.628            | 0.9935            |
| $`-`$ w/o $`\mathcal{D}_{\mathrm{cross}}`$ | 0.998              | 1.076                 | 3.847              | 3.752            | 0.9968            |
| $`-`$ w/o $`\mathcal{D}_{\mathrm{harm}}`$  | 1.012              | 1.098                 | 3.760              | 3.735            | 0.9996            |

Table 4: Ablation study of the proposed components on VCTK with a 16-kHz input sampling rate (8-kHz Nyquist cutoff). The best and second-best results are highlighted in bold and underline, respectively.

### Ablation Studies

To better understand the main design choices in AnyBand, we analyze the cutoff-sampling strategy, model components, prediction parameterization, and sampling configuration.

#### Cutoff-sampling strategy.

Table 3 compares three training strategies. Discrete uniform sampling draws equivalent input rates from $`\{2,4,8,16,24,32\}`$ kHz, whereas continuous uniform sampling covers the full cutoff range. Easy-to-Balanced starts from a distribution biased toward higher-cutoff, less underdetermined examples and gradually transitions to continuous uniform sampling. Discrete uniform remains competitive at its predefined training points, while continuous uniform produces weaker average results. Easy-to-Balanced achieves the best overall averages, with its largest gains at low and medium cutoff settings, indicating a better balance across bandwidth conditions.

#### Component analysis.

Table 4 evaluates the main components of AnyBand. In the variant without frequency modules, the frequency encoder and decoder are replaced by the linear input and output projections used in F5-TTS (Chen et al. 2025). The remaining variants remove F0/UV conditioning or one of the three discriminators. Removing the frequency modules or F0/UV conditioning generally degrades both spectral and perceptual metrics. Among the discriminators, removing $`\mathcal{D}_{\mathrm{spec}}`$ causes the largest overall degradation. Although removing $`\mathcal{D}_{\mathrm{cross}}`$ or $`\mathcal{D}_{\mathrm{harm}}`$ yields isolated improvements on individual metrics, each removal worsens the overall metric profile, suggesting that the three discriminators provide complementary supervision.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x5.png)

(a) Solver and steps.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x6.png)

(b) Guidance scale.

Figure 5: Effect of sampling configurations on HF-LSD.

#### Sampling configuration.

Figure 5 examines the sampling solver, number of steps, and classifier-free guidance scale. Increasing the number of steps consistently reduces HF-LSD for both Euler and Heun, with Heun performing better across the tested settings. The improvements diminish as the number of steps increases, revealing a trade-off between reconstruction quality and inference cost. Increasing the guidance scale initially improves high-frequency reconstruction, but the benefit saturates and slightly degrades at larger values. We therefore use the Heun solver with 50 steps and a guidance scale of 1.4.

## Conclusion

We introduced AnyBand, a unified framework for speech bandwidth extension over continuously varying cutoff frequencies. By formulating BWE as in-context spectral infilling, AnyBand uses the observed low-frequency spectrum as an acoustic prompt and a cutoff-derived mask to specify the missing region, enabling a single model to handle diverse bandwidth settings. Its frequency-aware encoder–decoder, F0/UV conditioning, and complementary spectral, cross-band, and harmonic discriminators improve spectral reconstruction and high-frequency realism. We further introduce an Easy-to-Balanced cutoff curriculum and adopt velocity prediction for effective flow-based generation. Experiments on in-domain and out-of-domain datasets show that AnyBand consistently reduces full-band and high-frequency distortion over prior systems while maintaining competitive perceptual quality and intelligibility. These results establish unified spectral infilling as an effective formulation for flexible multi-bandwidth speech extension.

## References

- P. Andreev, A. Alanov, O. Ivanov, and D. Vetrov (2023) Hifi++: a unified framework for bandwidth extension and speech enhancement. In ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5. Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- Y. Chen, Z. Niu, Z. Ma, K. Deng, C. Wang, J. JianZhao, K. Yu, and X. Chen (2025) F5-TTS: a fairytaler that fakes fluent and faithful speech with flow matching. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria, pp. 6255–6271. External Links: [Link](https://aclanthology.org/2025.acl-long.313/), [Document](https://dx.doi.org/10.18653/v1/2025.acl-long.313), ISBN 979-8-89176-251-0 Cited by: Introduction, Unified and Flexible Bandwidth Extension, DiT Backbone., AnyBand, Component analysis..
- W. Choi, S. Lee, H. Lim, and H. Kang (2026) Universr: unified and versatile audio super-resolution via vocoder-free flow matching. In ICASSP 2026-2026 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 15852–15856. Cited by: Unified and Flexible Bandwidth Extension.
- S. E. Eskimez, X. Wang, M. Thakker, C. Li, C. Tsai, Z. Xiao, H. Yang, Z. Zhu, M. Tang, X. Tan, et al. (2024) E2 tts: embarrassingly easy fully non-autoregressive zero-shot tts. In 2024 IEEE spoken language technology workshop (SLT), pp. 682–689. Cited by: Introduction, Unified and Flexible Bandwidth Extension.
- Y. Fang, J. Bai, J. Wang, and X. Zhang (2025) Vector quantized diffusion model based speech bandwidth extension. In ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5. Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- A. Gray and J. Markel (1976) Distance measures for speech processing. IEEE Transactions on Acoustics, Speech, and Signal Processing 24 (5), pp. 380–391. Cited by: Evaluation Metrics.
- A. Gupta, B. Shillingford, Y. Assael, and T. C. Walters (2019) Speech bandwidth extension with wavenet. In 2019 IEEE workshop on applications of signal processing to audio and acoustics (WASPAA), pp. 205–208. Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- S. Han and J. Lee (2022) NU-wave 2: A general neural audio upsampling model for various sampling rates. In 23rd Annual Conference of the International Speech Communication Association, Interspeech 2022, pp. 4401–4405. External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2022-45) Cited by: §B.1. ‣ B.1 Baseline Configurations ‣ Appendix B Experimental Details ‣ AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context Spectral Infilling"), Introduction, Unified and Flexible Bandwidth Extension, Evaluation Metrics, Objective Results..
- S. Hu, B. Zhang, B. Liang, E. Zhao, and S. Lui (2020) Phase-aware music super-resolution using generative adversarial networks. In 21st Annual Conference of the International Speech Communication Association, Interspeech 2020, pp. 4074–4078. External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2020-2605) Cited by: Speech Bandwidth Extension and Super-Resolution.
- J. Im and J. Nam (2025) FlashSR: one-step versatile audio super-resolution via diffusion distillation. In ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5. Cited by: Unified and Flexible Bandwidth Extension.
- W. Jang, D. Lim, J. Yoon, B. Kim, and J. Kim (2021) UnivNet: A neural vocoder with multi-resolution spectrogram discriminators for high-fidelity waveform generation. In 22nd Annual Conference of the International Speech Communication Association, Interspeech 2021, pp. 2207–2211. External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2021-1016) Cited by: Multi-View Spectral Discriminators., Multi-View Spectral Discriminators..
- S. Kim, S. Lee, H. Choi, and S. Lee (2024) Audio super-resolution with robust speech representation learning of masked autoencoder. IEEE/ACM Transactions on Audio, Speech, and Language Processing 32, pp. 1012–1022. Cited by: §B.1. ‣ B.1 Baseline Configurations ‣ Appendix B Experimental Details ‣ AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context Spectral Infilling"), Introduction, Objective Results..
- J. Kong, J. Kim, and J. Bae (2020) Hifi-gan: generative adversarial networks for efficient and high fidelity speech synthesis. Advances in neural information processing systems 33, pp. 17022–17033. Cited by: Multi-View Spectral Discriminators., Multi-View Spectral Discriminators..
- Z. Kong, K. J. Shih, W. Nie, A. Vahdat, S. Lee, J. F. Santos, A. Jukic, R. Valle, and B. Catanzaro (2025) A2sb: audio-to-audio schrodinger bridges. arXiv preprint arXiv:2501.11311. Cited by: Speech Bandwidth Extension and Super-Resolution.
- V. Kuleshov, S. Z. Enam, and S. Ermon (2017) Audio super resolution using neural networks. In 5th International Conference on Learning Representations, Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- M. Le, A. Vyas, B. Shi, B. Karrer, L. Sari, R. Moritz, M. Williamson, V. Manohar, Y. Adi, J. Mahadeokar, et al. (2023) Voicebox: text-guided multilingual universal speech generation at scale. Advances in neural information processing systems 36, pp. 14005–14034. Cited by: Introduction, Unified and Flexible Bandwidth Extension.
- J. Lee and S. Han (2021) NU-wave: A diffusion probabilistic model for neural audio upsampling. In 22nd Annual Conference of the International Speech Communication Association, Interspeech 2021, pp. 1634–1638. External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2021-36) Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- S. Lee, W. Ping, B. Ginsburg, B. Catanzaro, and S. Yoon (2023) BigVGAN: A universal neural vocoder with large-scale training. In The Eleventh International Conference on Learning Representations, Cited by: Multi-View Spectral Discriminators..
- S. Lee, H. Choi, and S. Lee (2024) Accelerating high-fidelity waveform generation via adversarial flow matching optimization. arXiv preprint arXiv:2408.08019. Cited by: Multi-View Spectral Discriminators., Adversarial Refinement..
- T. Li and K. He (2026) Back to basics: let denoising generative models denoise. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 36115–36125. Cited by: §C.3.
- Y. A. Li, C. Han, X. Jiang, and N. Mesgarani (2023) Hiftnet: a fast high-quality neural vocoder with harmonic-plus-noise filter and inverse short time fourier transform. arXiv preprint arXiv:2309.09493. Cited by: Multi-View Spectral Discriminators..
- Y. Li, M. Tagliasacchi, O. Rybakov, V. Ungureanu, and D. Roblek (2021) Real-time speech frequency bandwidth extension. In ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 691–695. Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- Q. Liang, Y. Liu, R. Wei, N. Lu, J. Zhao, and Y. Wang (2026) TED-tts: training-free intra-utterance emotion and duration control for text-to-speech synthesis. In Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 23485–23508. Cited by: Introduction.
- T. Y. Lim, R. A. Yeh, Y. Xu, M. N. Do, and M. Hasegawa-Johnson (2018) Time-frequency networks for audio super-resolution. In 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 646–650. Cited by: Speech Bandwidth Extension and Super-Resolution.
- Y. Lipman, R. T. Chen, H. Ben-Hamu, M. Nickel, and M. Le (2023) Flow matching for generative modeling. In The Eleventh International Conference on Learning Representations, ICLR 2023, Cited by: §C.3, Missing-Band Flow Training., Adversarial Refinement..
- H. Liu, K. Chen, Q. Tian, W. Wang, and M. D. Plumbley (2024) AudioSR: versatile audio super-resolution at scale. In ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1076–1080. Cited by: §B.1. ‣ B.1 Baseline Configurations ‣ Appendix B Experimental Details ‣ AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context Spectral Infilling"), Introduction, Unified and Flexible Bandwidth Extension, Objective Results..
- H. Liu, W. Choi, X. Liu, Q. Kong, Q. Tian, and D. Wang (2022a) Neural vocoder is all you need for speech super-resolution. In 23rd Annual Conference of the International Speech Communication Association, Interspeech 2022, pp. 4227–4231. External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2022-11017) Cited by: Introduction, Unified and Flexible Bandwidth Extension.
- H. Liu, X. Liu, Q. Kong, Q. Tian, Y. Zhao, D. Wang, C. Huang, and Y. Wang (2022b) VoiceFixer: A unified framework for high-fidelity speech restoration. In 23rd Annual Conference of the International Speech Communication Association, Interspeech 2022, pp. 4232–4236. External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2022-11026) Cited by: Introduction, Unified and Flexible Bandwidth Extension.
- Y. Lu, Y. Ai, H. Du, and Z. Ling (2024a) Towards high-quality and efficient speech bandwidth extension with parallel amplitude and phase prediction. IEEE Transactions on Audio, Speech and Language Processing 33, pp. 236–250. Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- Y. Lu, Y. Ai, and Z. Ling (2022) Source-filter-based generative adversarial neural vocoder for high fidelity speech synthesis. In National Conference on Man-Machine Speech Communication, pp. 68–80. Cited by: Multi-View Spectral Discriminators..
- Y. Lu, Y. Ai, Z. Sheng, and Z. Ling (2024b) MultiStage Speech Bandwidth Extension with Flexible Sampling Rate Control. In Interspeech 2024, pp. 2270–2274. External Links: [Document](https://dx.doi.org/10.21437/Interspeech.2024-11), ISSN 2958-1796 Cited by: Unified and Flexible Bandwidth Extension.
- M. Mandel, O. Tal, and Y. Adi (2023) Aero: audio super resolution in the spectral domain. In ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5. Cited by: Speech Bandwidth Extension and Super-Resolution.
- J. H. McDermott and E. P. Simoncelli (2011) Sound texture perception via statistics of the auditory periphery: evidence from sound synthesis. Neuron 71 (5), pp. 926–940. Cited by: Multi-View Spectral Discriminators..
- G. Mittag, B. Naderi, A. Chehadi, and S. Möller (2021) NISQA: A deep cnn-self-attention model for multidimensional speech quality prediction with crowdsourced datasets. In 22nd Annual Conference of the International Speech Communication Association, Interspeech 2021, pp. 2127–2131. External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2021-299) Cited by: Evaluation Metrics.
- E. Moliner, F. Elvander, and V. Välimäki (2024) Blind audio bandwidth extension: a diffusion-based zero-shot approach. IEEE/ACM Transactions on Audio, Speech, and Language Processing 32, pp. 5092–5105. Cited by: Introduction, Unified and Flexible Bandwidth Extension.
- I. Nelken, Y. Rotman, and O. B. Yosef (1999) Responses of auditory-cortex neurons to structural features of natural sounds. Nature 397 (6715), pp. 154–157. Cited by: Multi-View Spectral Discriminators..
- J. Richter, Y. Wu, S. Krenn, S. Welker, B. Lay, S. Watanabe, A. Richard, and T. Gerkmann (2024) EARS: an anechoic fullband speech dataset benchmarked for speech enhancement and dereverberation. In Interspeech, Cited by: Datasets.
- M. Salhab and H. Harmanani (2025) Speech bandwidth expansion via high fidelity generative adversarial networks. In 2025 1st International Conference on Computational Intelligence Approaches and Applications (ICCIAA), pp. 1–7. Cited by: Introduction, Unified and Flexible Bandwidth Extension.
- Y. Sharma (2026) Fast and flexible audio bandwidth extension via vocos. arXiv preprint arXiv:2603.07285. Cited by: Introduction, Unified and Flexible Bandwidth Extension.
- H. Siuzdak (2024) Vocos: closing the gap between time-domain and fourier-based neural vocoders for high-quality audio synthesis. In The Twelfth International Conference on Learning Representations, ICLR 2024, Cited by: Implementation Details.
- J. Su, Y. Wang, A. Finkelstein, and Z. Jin (2021) Bandwidth extension is all you need. In ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 696–700. Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- C. H. Taal, R. C. Hendriks, R. Heusdens, and J. Jensen (2011) An algorithm for intelligibility prediction of time–frequency weighted noisy speech. IEEE Transactions on audio, speech, and language processing 19 (7), pp. 2125–2136. Cited by: Evaluation Metrics.
- C. Wang, S. Chen, Y. Wu, Z. Zhang, L. Zhou, S. Liu, Z. Chen, Y. Liu, H. Wang, J. Li, et al. (2023) Neural codec language models are zero-shot text to speech synthesizers. arXiv preprint arXiv:2301.02111. Cited by: Introduction.
- N. Xu, Z. Huang, and X. Zeng (2025) A universal harmonic discriminator for high-quality gan-based vocoder. In IEEE Automatic Speech Recognition and Understanding Workshop, ASRU 2025, pp. 1–7. External Links: [Document](https://dx.doi.org/10.1109/ASRU65441.2025.11434736) Cited by: Multi-View Spectral Discriminators..
- J. Yamagishi, C. Veaux, and K. MacDonald (2019) CSTR VCTK Corpus: english multi-speaker corpus for CSTR voice cloning toolkit (version 0.92). University of Edinburgh. The Centre for Speech Technology Research (CSTR). External Links: [Document](https://dx.doi.org/10.7488/ds/2645) Cited by: Datasets.
- N. Yang, Y. Li, D. A. Cuji, R. M. Corey, P. Zhao, X. Lin, and A. C. Singer (2026) A survey of advancing audio super-resolution and bandwidth extension from discriminative to generative models. arXiv preprint arXiv:2605.16681. Cited by: Introduction.
- J. Yun, S. Kim, and S. Lee (2025) FLowHigh: towards efficient and high-quality audio super-resolution with single-step flow matching. In ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), pp. 1–5. Cited by: §B.1. ‣ B.1 Baseline Configurations ‣ Appendix B Experimental Details ‣ AnyBand: Unified Multi-Bandwidth Speech Extension via Frequency-Aware In-Context Spectral Infilling"), Unified and Flexible Bandwidth Extension, Objective Results..
- B. Zhang, J. Zhao, I. McLoughlin, Y. Wang, and A. Madhukumar (2026) Codecflow: efficient bandwidth extension via conditional flow matching in neural codec latent space. arXiv preprint arXiv:2603.02022. Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution, DiT Backbone..
- K. Zhang, Y. Ren, C. Xu, and Z. Zhao (2021) WSRGlow: A glow-based waveform generative model for audio super-resolution. In 22nd Annual Conference of the International Speech Communication Association, Interspeech 2021, pp. 1649–1653. External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2021-892) Cited by: Introduction, Speech Bandwidth Extension and Super-Resolution.
- J. Zhao, M. D. Vu, and Y. Wang (2026a) Hierarchical decoding for discrete speech synthesis with multi-resolution spoof detection. arXiv preprint arXiv:2603.05373. Cited by: Introduction.
- J. Zhao, X. Wang, and Y. Wang (2025) Prosody-adaptable audio codecs for zero-shot voice conversion via in-context learning. In 26th Annual Conference of the International Speech Communication Association, Interspeech 2025, External Links: [Document](https://dx.doi.org/10.21437/INTERSPEECH.2025-464) Cited by: Implementation Details.
- J. Zhao, W. Zeng, T. Lyu, and Y. Wang (2026b) Comelsinger: discrete token-based zero-shot singing synthesis with structured melody control and guidance. IEEE Transactions on Audio, Speech and Language Processing. Cited by: Introduction.

## Appendix A Additional Implementation Details

### A.1 Data and Acoustic Features

All speech signals are processed at 48 kHz. During training, we randomly extract waveform segments of 64,000 samples. We follow the acoustic preprocessing configuration of the 48-kHz Vocos model and compute 128-bin mel spectrograms using a 2,048-point FFT and a hop length of 256. The mel filterbank covers 0–24 kHz and uses a magnitude power of 1.0, Slaney normalization, and the Slaney mel scale.

The cutoff frequency is independently sampled for each training segment from the continuous range of 1–16 kHz. The corresponding mel-bin boundary is determined by comparing the center frequency of each mel bin with the sampled cutoff, following the mask definition in the main paper.

Frame-level F0 and voiced/unvoiced features are extracted from the corresponding band-limited input waveform using pYIN, with YIN used as a fallback when pYIN does not return a valid estimate. For voiced frames, F0 is logarithmically normalized as:

```math
\widetilde{f}_{0}=\operatorname{clip}\left(\frac{\log f_{0}-\log 86}{\log 1100-\log 86},0,1\right).
```

The normalized F0 value is set to zero for unvoiced frames, while a separate binary feature indicates the voiced/unvoiced state.

### A.2 Model Configuration

#### Generator.

The AnyBand generator contains approximately 37 million parameters. Its temporal backbone consists of eight DiT blocks with a hidden dimension of 384 and six attention heads. The frequency encoder and decoder each contain two frequency-axis Transformer blocks with a hidden dimension of 64 and four attention heads. The frequency encoder takes the intermediate noisy state $`\mathbf{M}_{t}`$ and the observed spectral prompt $`\widetilde{\mathbf{M}}`$ as input. Their values are concatenated at each time–frequency position and projected into frequency-token embeddings. After frequency-axis self-attention, a learned query performs four-head attention pooling over the frequency tokens to obtain a frame-level representation. The temporal DiT then models long-range dependencies across frames, after which the frequency decoder produces frequency-specific velocity predictions. The frequency mask is used to construct the observed prompt and define the reconstruction region, but is not directly injected into the generator.

#### Discriminators.

The multi-scale spectral discriminator $`\mathcal{D}_{\mathrm{spec}}`$ evaluates mel spectrograms at three temporal resolutions. Each resolution is processed by an independent 2D convolutional branch with channel dimensions of 32, 64, 128, and 256. The cross-band discriminator $`\mathcal{D}_{\mathrm{cross}}`$ partitions the 128 mel bins into 16 contiguous subbands, each containing eight mel bins, and computes local cross-band statistics using a temporal window of 32 frames. The harmonic discriminator $`\mathcal{D}_{\mathrm{harm}}`$ considers the first 12 F0-aligned harmonics, whose amplitudes are bilinearly sampled from the mel spectrogram. The three discriminators use separate, task-specific 2D convolutional networks.

### A.3 Training Configuration

#### Flow Pretraining.

We first train the generator for 300 epochs using the missing-band velocity-prediction objective described in the main paper. The model is optimized with AdamW using an initial learning rate of $`10^{-3}`$ and a cosine-annealing learning-rate schedule with $`T_{\max}=300`$. No learning-rate warmup is used. The Easy-to-Balanced cutoff curriculum uses $`\beta=4`$ and $`\rho=0.7`$.

#### Adversarial Refinement.

The pretrained generator is subsequently refined for 200 epochs using the three proposed discriminators. During this stage, cutoff frequencies are uniformly sampled from the continuous training range. The generator and discriminators are optimized with AdamW using learning rates of $`5\times 10^{-5}`$ and $`2\times 10^{-4}`$, respectively, with $`(\beta_{1},\beta_{2})=(0.8,0.99)`$. Both optimizers use cosine-annealing schedules with $`T_{\max}=200`$ and no learning-rate warmup. The generator and discriminators are updated once per batch in a 1:1 ratio. We set the adversarial-loss weight to $`\lambda_{\mathrm{adv}}=0.1`$ and equally weight the adversarial losses from the three discriminators. The feature-matching weight is set to $`\lambda_{\mathrm{fm}}=2.0`$, with feature-matching losses summed over their intermediate feature maps.

For endpoint-focused adversarial refinement, we first integrate the flow from Gaussian noise to $`t_{e}=0.8`$ without gradient tracking. Starting from the resulting intermediate state, we perform an eight-step differentiable Heun rollout over $`[t_{e},1]`$. The adversarial and feature-matching objectives are applied to the resulting full-band estimate, with the observed frequency region copied from the band-limited input as defined in the main paper.

#### Computational Setup.

AnyBand is trained with bfloat16 mixed precision on eight NVIDIA L40S GPUs, using a batch size of 32 per GPU and a global batch size of 256.

### A.4 Inference Configuration

At inference time, we use the Heun solver with 50 sampling steps and a right-swayed time grid with $`\gamma=2.0`$. Classifier-free guidance is applied in velocity space with a guidance scale of 1.4. The observed spectral prompt is provided separately throughout sampling. The observed frequency region is not overwritten after each intermediate integration step and is copied back only after the final step. We generate one output for each utterance in both objective and subjective evaluations.

## Appendix B Experimental Details

### B.1 Baseline Configurations

#### Common Protocol.

All baseline systems are implemented using their official codebases. We use the same VCTK training split, training utterances, held-out test utterances, and nominal cutoff settings for all methods. To preserve the original formulation of each baseline, band-limited inputs are constructed using the native preprocessing procedure provided by its official implementation. Methods initialized from publicly released checkpoints are subsequently fine-tuned on the shared VCTK training split, whereas the remaining methods are trained from scratch on the same data. All systems generate 48-kHz outputs and are evaluated using the same metric protocols.

#### NU-Wave 2 (Han and Lee 2022).

We use the official implementation of NU-Wave 2³³3https://github.com/maum-ai/nuwave2 and train the model from scratch on the shared VCTK training split. We retain its original bandwidth-conditioning mechanism and native waveform preprocessing procedure, while adapting the training and evaluation cutoff settings to our experimental protocol.

#### AudioSR (Liu et al. 2024).

We use the official AudioSR implementation and its publicly released checkpoint⁴⁴4https://github.com/haoheliu/versatile˙audio˙super˙resolution, followed by fine-tuning on the shared VCTK training split. We retain the official input preprocessing and recommended inference configuration.

#### FLowHigh (Yun et al. 2025).

We use the official FLowHigh implementation⁵⁵5https://github.com/resemble-ai/flowhigh and initialize the model from the released checkpoint⁶⁶6https://drive.google.com/drive/folders/1clsJ3bFTZSCLOb4I0wk0l6FL9Yh33Vof. The model is then fine-tuned on the shared VCTK training split while retaining its original probability path, input preprocessing, and inference procedure.

#### Fre-Painter (Kim et al. 2024).

We use the official implementation of Fre-Painter⁷⁷7https://github.com/ishine/FrePainter and train the model from scratch on the shared VCTK training split. We retain its original preprocessing, training objective, and inference procedure, while adapting the training and evaluation bandwidth settings to our experimental protocol.

### B.2 Ablation Configurations

#### Component Ablations.

For the variant without frequency modules, we replace the proposed frequency encoder and decoder with the frame-wise linear input and output projections used in the original temporal DiT backbone. The variant without F0/VUV removes both auxiliary conditioning features while retaining the remaining generator architecture. To evaluate the contribution of each adversarial objective, we remove one discriminator at a time during adversarial refinement while retaining the other two discriminators. All discriminator ablations are initialized from the same Stage-1 flow checkpoint and independently refined for the same training steps. The remaining training data, cutoff-sampling strategy, optimization settings, and inference configuration are kept identical to those of the full model.

#### Cutoff-Sampling Strategies.

We compare three cutoff-sampling strategies during Stage-1 flow pretraining. _Discrete Uniform_ uniformly samples equivalent input rates from $`\{2,4,8,16,24,32\}`$ kHz, corresponding to cutoff frequencies of $`\{1,2,4,8,12,16\}`$ kHz. _Continuous Uniform_ samples cutoff frequencies uniformly from the full continuous range of 1–16 kHz throughout training. _Easy-to-Balanced_ initially favors higher cutoff frequencies and gradually transitions to the same continuous uniform distribution.

Continuous Uniform and Easy-to-Balanced share the same continuous cutoff support and differ only in how the sampling distribution evolves during Stage-1 training. All three variants use the same model architecture, training data, optimization settings, and training budget. They are then refined using the same Stage-2 adversarial-training configuration, in which cutoff frequencies are uniformly sampled from the continuous training range. Therefore, the compared models differ only in the cutoff-sampling strategy used during Stage-1 flow pretraining.

### B.3 Objective Evaluation Protocol

#### Spectral Metrics.

LSD, LF-LSD, and HF-LSD are computed from the final 48-kHz waveforms. Let $`X_{t,k}`$ and $`\widehat{X}_{t,k}`$ denote the complex STFT coefficients of the reference and generated waveforms at time frame $`t`$ and frequency bin $`k`$, respectively. We first compute their log-power spectra as:

```math
Y_{t,k}=\log_{10}\left(\max\left(|X_{t,k}|^{2},\epsilon\right)\right),
```

where $`\epsilon=10^{-8}`$. The STFT uses a 2,048-sample Hann window with a hop size of 512 samples. For a frequency-bin set $`\mathcal{K}`$, the corresponding spectral distance is defined as:

```math
d(\mathcal{K})=\frac{1}{T}\sum_{t=1}^{T}\sqrt{\frac{1}{|\mathcal{K}|}\sum_{k\in\mathcal{K}}\left(\widehat{Y}_{t,k}-Y_{t,k}\right)^{2}}.
```

Given the input cutoff frequency $`f_{c}`$, LSD is computed over the full frequency range from 0 to 24 kHz. LF-LSD is computed over frequency bins at or below $`f_{c}`$, whereas HF-LSD is computed over frequency bins above $`f_{c}`$ and up to 24 kHz. Reference and generated signals are converted to mono before evaluation. When their lengths differ, the longer signal is trimmed to the length of the shorter one, without additional temporal alignment.

#### Perceptual Quality and Intelligibility Metrics.

We report the overall quality score and coloration dimension predicted by NISQA⁸⁸8https://github.com/gabrielmittag/NISQA as NISQA and COL, respectively. Speech intelligibility is evaluated using the standard STOI metric. All metrics are computed utterance-wise and then averaged over the complete evaluation set.

### B.4 Subjective Evaluation Protocol

We conduct a listening test to evaluate the overall speech quality of the bandwidth-extended speech. The evaluation covers five input sampling rates: 8, 12, 16, 20, and 24 kHz. For each input rate, five utterances are selected, and the outputs of five systems are evaluated. The original 48-kHz recordings are also included as reference samples. A total of 15 listeners participate in the evaluation, with each listener rating 130 audio samples.

The test takes approximately 40 minutes and is divided into three sections, with optional breaks between sections. Participants are instructed to conduct the test in a quiet environment, use headphones or earphones, maintain a comfortable and consistent playback volume, and listen to each complete sample before assigning a score. Each sample is evaluated independently using a five-point overall-speech-quality scale: 5 (_Excellent_), 4 (_Good_), 3 (_Fair_), 2 (_Poor_), and 1 (_Bad_). Participants are asked to focus only on speech quality and disregard the linguistic content, accent, speaking style, and speaker identity. The final score of each system is obtained by averaging the ratings across utterances and listeners. The listening-test instructions and sample-rating interface are shown in Figure 6 and 7, respectively.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x7.png)

Figure 6: Instructions for the subjective listening test.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x8.png)

Figure 7: Interface for rating overall speech quality.

## Appendix C Additional Experimental Analyses

### C.1 Cutoff-Sampling Curriculum Analysis

![Refer to caption](https://arxiv.org/html/2608.00572v1/x9.png)

Figure 8: Illustration of the Easy-to-Balanced cutoff-sampling curriculum. Early training emphasizes larger normalized cutoffs, corresponding to easier inputs with narrower missing bands. The sampling density gradually transitions to a continuous uniform distribution, which is used after $`s\geq\rho S`$.

#### Cutoff-Sampling Curriculum.

Figure 8 illustrates the proposed Easy-to-Balanced cutoff-sampling schedule. At the beginning of training, the sampling density is biased toward larger normalized cutoffs, which correspond to easier bandwidth-extension conditions with a smaller missing frequency region. As training proceeds, the distribution gradually interpolates toward the continuous uniform distribution over the full cutoff range. After the transition stage ends at $`s=\rho S`$, the model is trained using uniform continuous cutoff sampling. This schedule provides a smooth progression from easier to more underdetermined bandwidth conditions, while ultimately preserving balanced coverage of the entire training range.

#### Irregular-Bandwidth Evaluation.

| Input SR | Sampling strategy    | LSD $`\downarrow`$ | HF-LSD $`\downarrow`$ | NISQA $`\uparrow`$ | COL $`\uparrow`$ | STOI $`\uparrow`$ |
| -------- | -------------------- | ------------------ | --------------------- | ------------------ | ---------------- | ----------------- |
| 3 kHz    | Uniform (discrete)   | 1.280              | 1.321                 | 3.511              | 3.602            | 0.8454            |
|          | Uniform (continuous) | 1.265              | 1.305                 | 3.574              | 3.464            | 0.8485            |
|          | Easy-to-Balanced     | 1.228              | 1.261                 | 3.671              | 3.702            | 0.8523            |
| 6 kHz    | Uniform (discrete)   | 1.185              | 1.249                 | 3.709              | 3.654            | 0.9412            |
|          | Uniform (continuous) | 1.156              | 1.218                 | 3.888              | 3.674            | 0.9505            |
|          | Easy-to-Balanced     | 1.123              | 1.177                 | 4.060              | 4.002            | 0.9575            |
| 12 kHz   | Uniform (discrete)   | 1.152              | 1.210                 | 3.894              | 3.825            | 0.9904            |
|          | Uniform (continuous) | 1.021              | 1.102                 | 3.922              | 3.954            | 0.9985            |
|          | Easy-to-Balanced     | 1.002              | 1.093                 | 3.987              | 3.920            | 0.9968            |
| 15 kHz   | Uniform (discrete)   | 1.019              | 1.123                 | 3.861              | 3.956            | 0.9905            |
|          | Uniform (continuous) | 0.993              | 1.092                 | 4.034              | 4.009            | 0.9975            |
|          | Easy-to-Balanced     | 0.975              | 1.085                 | 3.975              | 3.894            | 0.9987            |
| Avg.     | Uniform (discrete)   | 1.159              | 1.226                 | 3.744              | 3.759            | 0.9419            |
|          | Uniform (continuous) | 1.109              | 1.179                 | 3.855              | 3.775            | 0.9488            |
|          | Easy-to-Balanced     | 1.082              | 1.154                 | 3.923              | 3.880            | 0.9513            |

Table 5: Ablation study of cutoff-sampling strategies on VCTK. Input sampling rates of 3, 6, 12, and 15 kHz correspond to Nyquist cutoffs of 1.5, 3, 6, and 7.5 kHz, respectively. The output sampling rate is 48 kHz. The best and second-best results within each input setting are highlighted in bold and underlined, respectively. Avg. denotes the macro-average over the four input sampling rates.

Table 5 extends the cutoff-sampling comparison to irregular input sampling rates. Unlike the regular-bandwidth results, where Continuous Uniform does not consistently outperform Discrete Uniform, Continuous Uniform achieves lower LSD and HF-LSD across all irregular settings. This contrast highlights the importance of exposing the model to continuously varying cutoffs when generalizing beyond the discrete training points. Easy-to-Balanced further obtains the lowest LSD and HF-LSD at every evaluated bandwidth, showing that its advantage cannot be attributed solely to continuous cutoff coverage. The gains are particularly evident at the more challenging 3- and 6-kHz inputs, where it also achieves the best perceptual and intelligibility scores. Although Continuous Uniform is slightly better on several perceptual metrics at higher input bandwidths, Easy-to-Balanced achieves the best average result across all reported metrics.

#### Bandwidth-wise Effects of Easy-to-Balanced Training.

To examine how different bandwidth conditions evolve under Easy-to-Balanced training, we track the full-band LSD throughout Stage-1 training at input sampling rates of 2, 4, 8, 16, and 24 kHz. Figure 9 reports both the absolute LSD and its relative reduction with respect to the first evaluation checkpoint. For an input sampling rate $`s`$, the relative LSD reduction at epoch $`e`$ is defined as

```math
R_{e}^{(s)}=\frac{\operatorname{LSD}_{e_{0}}^{(s)}-\operatorname{LSD}_{e}^{(s)}}{\operatorname{LSD}_{e_{0}}^{(s)}}\times 100\%,
```

where $`e_{0}`$ denotes the first evaluation checkpoint.

As shown in Figure 9(a), lower input sampling rates consistently result in higher absolute LSD, reflecting the greater difficulty of reconstructing a wider missing frequency region. After accounting for these different initial error levels, Figure 9(b) shows that the challenging 2-, 4-, and 8-kHz conditions achieve larger overall relative reductions than the 16- and 24-kHz conditions. The high-bandwidth conditions remain comparatively stable, while the low-bandwidth curves exhibit larger improvements together with some local fluctuations. This behavior is consistent with the intended curriculum: training begins with relatively informative inputs and progressively increases exposure to more severely underdetermined bandwidth conditions before reaching a balanced continuous cutoff distribution.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x10.png)

(a) Absolute LSD.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x11.png)

(b) Relative LSD reduction.

Figure 9: Stage-1 training progress under Easy-to-Balanced cutoff sampling across different input sampling rates. Relative reduction is measured with respect to the first evaluation checkpoint.

### C.2 Component Ablation across Input Bandwidths

| Variant                                    | Input SR: 2 kHz   |                      |                   |                 |                  | Input SR: 4 kHz   |                      |                   |                 |                  | Input SR: 8 kHz   |                      |                   |                 |                  | Input SR: 16 kHz  |                      |                   |                 |                  |
| ------------------------------------------ | ----------------- | -------------------- | ----------------- | --------------- | ---------------- | ----------------- | -------------------- | ----------------- | --------------- | ---------------- | ----------------- | -------------------- | ----------------- | --------------- | ---------------- | ----------------- | -------------------- | ----------------- | --------------- | ---------------- |
|                                            | LSD$`\downarrow`$ | HF-LSD$`\downarrow`$ | NISQA$`\uparrow`$ | COL$`\uparrow`$ | STOI$`\uparrow`$ | LSD$`\downarrow`$ | HF-LSD$`\downarrow`$ | NISQA$`\uparrow`$ | COL$`\uparrow`$ | STOI$`\uparrow`$ | LSD$`\downarrow`$ | HF-LSD$`\downarrow`$ | NISQA$`\uparrow`$ | COL$`\uparrow`$ | STOI$`\uparrow`$ | LSD$`\downarrow`$ | HF-LSD$`\downarrow`$ | NISQA$`\uparrow`$ | COL$`\uparrow`$ | STOI$`\uparrow`$ |
| AnyBand (Ours)                             | 1.248             | 1.269                | 3.125             | 3.419           | 0.8214           | 1.180             | 1.219                | 4.038             | 3.966           | 0.9356           | 1.086             | 1.155                | 4.014             | 3.983           | 0.9870           | 0.974             | 1.092                | 3.936             | 3.837           | 0.9992           |
| $`-`$ w/o Freq. Modules                    | 1.327             | 1.352                | 2.882             | 2.843           | 0.7940           | 1.215             | 1.260                | 3.920             | 3.827           | 0.9140           | 1.090             | 1.141                | 3.918             | 3.856           | 0.9850           | 1.038             | 1.159                | 3.772             | 3.656           | 0.9978           |
| $`-`$ w/o F0/UV                            | 1.332             | 1.369                | 2.905             | 2.980           | 0.8067           | 1.253             | 1.299                | 3.803             | 3.707           | 0.9091           | 1.137             | 1.204                | 3.848             | 3.820           | 0.9830           | 1.035             | 1.125                | 3.758             | 3.698           | 0.9985           |
| $`-`$ w/o $`\mathcal{D}_{\mathrm{spec}}`$  | 1.354             | 1.372                | 2.543             | 2.790           | 0.7852           | 1.229             | 1.278                | 3.825             | 3.843           | 0.8966           | 1.156             | 1.218                | 3.782             | 3.609           | 0.9725           | 1.124             | 1.206                | 3.673             | 3.628           | 0.9935           |
| $`-`$ w/o $`\mathcal{D}_{\mathrm{cross}}`$ | 1.295             | 1.325                | 3.012             | 3.286           | 0.8133           | 1.157             | 1.181                | 4.027             | 3.940           | 0.9204           | 1.122             | 1.165                | 3.955             | 3.896           | 0.9872           | 0.998             | 1.076                | 3.847             | 3.752           | 0.9968           |
| $`-`$ w/o $`\mathcal{D}_{\mathrm{harm}}`$  | 1.280             | 1.311                | 3.000             | 3.322           | 0.8095           | 1.193             | 1.235                | 3.882             | 3.756           | 0.9310           | 1.069             | 1.127                | 3.894             | 3.796           | 0.9865           | 1.012             | 1.098                | 3.760             | 3.735           | 0.9996           |

Table 6: Component ablation across different input sampling rates on VCTK. The corresponding Nyquist cutoffs are half of the input sampling rates. The best and second-best results within each input setting are highlighted in bold and underlined, respectively.

Table 6 extends the component ablation to multiple input sampling rates (2, 4, and 8 kHz). Removing either the frequency-aware modules or the F0/VUV conditioning generally degrades spectral reconstruction, perceptual quality, and intelligibility, with the effects being most pronounced under severely bandwidth-limited inputs. This indicates that explicit frequency-wise modeling and pitch–voicing cues become particularly important when only a small portion of the original spectrum is observed. Their influence becomes less pronounced as the available bandwidth increases, although the complete model provides a more balanced performance across the reported metrics.

Among the adversarial components, removing $`\mathcal{D}_{\mathrm{spec}}`$ results in the most consistent degradation across input bandwidths, confirming the importance of multi-scale spectral realism during adversarial refinement. The contributions of $`\mathcal{D}_{\mathrm{cross}}`$ and $`\mathcal{D}_{\mathrm{harm}}`$ are more dependent on the bandwidth and evaluation metric. Removing either component occasionally improves an individual metric at higher input sampling rates, but generally weakens perceptual quality and performance under more challenging low-bandwidth conditions. Overall, the complete AnyBand model achieves the best average performance across all reported metrics, suggesting that the proposed components provide complementary benefits across different degrees of bandwidth limitation.

### C.3 Prediction Parameterization

| Prediction       | Steps | LSD $`\downarrow`$ | HF-LSD $`\downarrow`$ | NISQA $`\uparrow`$ | COL $`\uparrow`$ | STOI $`\uparrow`$ |
| ---------------- | ----- | ------------------ | --------------------- | ------------------ | ---------------- | ----------------- |
| $`v`$-prediction | 32    | 1.065              | 1.107                 | 4.060              | 3.825            | 0.9912            |
| $`x`$-prediction | 32    | 1.075              | 1.194                 | 3.883              | 3.796            | 0.9905            |
| $`v`$-prediction | 16    | 1.132              | 1.224                 | 3.757              | 3.710            | 0.9844            |
| $`x`$-prediction | 16    | 1.235              | 1.301                 | 3.764              | 3.686            | 0.9726            |

Table 7: Comparison of $`x`$- and $`v`$-prediction under different numbers of sampling steps on VCTK with a 16-kHz input sampling rate (8-kHz Nyquist cutoff). The best result under each sampling-step setting is highlighted in bold.

#### Compared Parameterizations.

We further compare _$`v`$-prediction_, which directly estimates the flow velocity (Lipman et al. 2023), with _$`x`$-prediction_, which predicts the clean spectrogram and converts it to velocity for flow matching and ODE sampling, following JiT (Li and He 2026). The two variants use the same probability path, velocity-space training objective, model architecture, and sampling procedure, differing only in the quantity directly predicted by the generator.

Under $`v`$-prediction, the generator directly estimates the velocity field:

```math
\widehat{\mathbf{v}}_{\theta}=\mathcal{G}_{\theta}\left(\mathbf{M}_{t},\widetilde{\mathbf{M}},t,\mathbf{c}\right).
```

Under $`x`$-prediction, the generator instead predicts the clean full-band spectrogram:

```math
\widehat{\mathbf{M}}_{\theta}=\mathcal{G}_{\theta}\left(\mathbf{M}_{t},\widetilde{\mathbf{M}},t,\mathbf{c}\right),
```

which is converted into the corresponding velocity as:

```math
\widehat{\mathbf{v}}_{\theta}=\frac{\widehat{\mathbf{M}}_{\theta}-\mathbf{M}_{t}}{\delta_{t}},\qquad\delta_{t}=\max(1-t,\delta).
```

The resulting velocity is used for both the masked flow-matching objective and ODE sampling. Although the two parameterizations are algebraically equivalent under perfect prediction, they impose different prediction targets on the generator. $`v`$-prediction directly estimates the vector field required by the ODE solver, whereas $`x`$-prediction first estimates the clean endpoint and then applies a time-dependent conversion to obtain the velocity.

#### Results.

Table 7 compares the two parameterizations under otherwise identical configurations. At 32 sampling steps, $`v`$-prediction outperforms $`x`$-prediction across all reported metrics. At 16 steps, $`v`$-prediction continues to achieve better LSD, HF-LSD, COL, and STOI, whereas $`x`$-prediction obtains only a marginally higher NISQA score. Overall, $`v`$-prediction provides more favorable performance under both standard and reduced sampling budgets, and is therefore adopted in AnyBand.

## Appendix D Qualitative Results

![Refer to caption](https://arxiv.org/html/2608.00572v1/x12.png)

(a) Standard input sampling rates.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x13.png)

(b) Irregular input sampling rates.

Figure 10: Qualitative mel-spectrogram comparisons for a representative utterance under standard and irregular input bandwidths. Horizontal dashed lines indicate the corresponding cutoff frequencies.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x14.png)

(a) Standard input sampling rates.

![Refer to caption](https://arxiv.org/html/2608.00572v1/x15.png)

(b) Irregular input sampling rates.

Figure 11: Additional qualitative mel-spectrogram comparisons under standard and irregular input bandwidths.

Figures 10 and 11 present qualitative mel-spectrogram comparisons for two representative utterances under both standard and irregular input bandwidths. The standard settings include input sampling rates of 2, 4, 8, and 16 kHz, while the irregular settings include 3, 6, 12, and 15 kHz. Each column corresponds to one input sampling rate, and the horizontal dashed line indicates the associated cutoff frequency.

The differences are most apparent under the severely bandwidth-limited 2–6 kHz inputs. NU-Wave 2 tends to produce diffuse high-frequency textures, while AudioSR and FLowHigh occasionally generate sparse, discontinuous, or banded structures above the cutoff. Fre-Painter recovers broader high-frequency energy, but some fine-grained spectral structures remain over-smoothed. In comparison, AnyBand generates more coherent high-frequency patterns that remain temporally aligned with the observed low-frequency content and transition more smoothly across the cutoff boundary. Its reconstructed harmonic and broadband structures are also visually closer to those of the ground-truth spectrograms.

As the available input bandwidth increases, the outputs of all methods become more similar to the ground truth, although AnyBand continues to preserve clearer high-frequency details and spectral continuity. Similar behavior is observed at the irregular input sampling rates, indicating that the learned spectral-continuation behavior is not restricted to the standard bandwidth settings.
