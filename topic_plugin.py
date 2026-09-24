"""TTS relevance rule ported from the legacy fetch_papers.py.

A paper is accepted when its title and abstract contain no excluded phrase,
at least one ML signal, and at least one TTS/speech-generation signal (a
positive phrase or the word-bounded "TTS" acronym).
"""

import re

from papers_pipeline.models import Paper
from papers_pipeline.topics import TopicDecision

EXCLUDED_PHRASES = (
    "speech recognition",
    "automatic speech recognition",
    "speaker recognition",
    "speaker verification",
    "speaker identification",
    # Neuroscience / brain-computer interfaces
    "speech neuroprosthesis",
    "cochlear implant",
    "resting-state fmri",
    "neural speech tracking",
    # Medical / clinical
    "dysarthria diagnosis",
    "stuttering detection",
    "alzheimer",
    "parkinson",
    # Hardware / physics where "synthesis" is not speech synthesis
    "frequency synthesizer",
    "circuit synthesis",
)

TTS_PHRASES = (
    "text-to-speech",
    "text to speech",
    "speech synthesis",
    "speech synthesizer",
    "voice synthesis",
    "vocoder",
    "voice conversion",
    "voice cloning",
    "speech generation",
    "singing voice synthesis",
    "singing voice conversion",
    "speech editing",
    "speech language model",
    "spoken language model",
    "codec language model",
    "speech codec",
    "audio codec",
    "prosody",
    "expressive speech",
    "speech-to-speech",
    "voice generation",
    "audio generation",
    "speech generative",
    "speech restoration",
    "speech tokenizer",
    "speech token",
    "spoken dialogue generation",
)

# Bare "TTS" needs word boundaries: a substring match would hit every "https://".
TTS_ACRONYM = re.compile(r"\btts\b")

ML_PHRASES = (
    "machine learning",
    "deep learning",
    "neural",
    "transformer",
    "diffusion",
    "gan",
    "generative",
    "self-supervised",
    "multimodal",
    "learning-based",
    "autoregressive",
    "flow matching",
    "flow-matching",
    "end-to-end",
    "sequence-to-sequence",
    "vocoder",
    "codec",
    "language model",
    "llm",
    "zero-shot",
    "few-shot",
    "in-context",
    "fine-tun",
    "pretrain",
    "pre-train",
    "tokenizer",
    "encoder",
    "decoder",
    "embedding",
    "attention",
    "reinforcement learning",
    "foundation model",
    "speech model",
    "voice model",
    "synthesis model",
    "tts system",
    "prediction model",
    "adaptation",
    "data-driven",
    "training",
    "learned",
    "representation",
    "state-of-the-art",
    "high-fidelity",
    "dataset",
    "corpus",
    "benchmark",
)


def accept_topic(paper: Paper) -> TopicDecision:
    """Apply the legacy TTS relevance rule to a paper's title and abstract.

    Args:
        paper: Normalized paper to classify.

    Returns:
        Acceptance decision with the rule that decided it.
    """
    text = f"{paper.title} {paper.abstract}".lower()
    excluded = next((phrase for phrase in EXCLUDED_PHRASES if phrase in text), None)
    if excluded is not None:
        return TopicDecision(False, f"matched excluded term: {excluded}")
    if not any(phrase in text for phrase in ML_PHRASES):
        return TopicDecision(False, "missing ML signal")
    if not (any(phrase in text for phrase in TTS_PHRASES) or TTS_ACRONYM.search(text)):
        return TopicDecision(False, "missing TTS signal")
    return TopicDecision(True, "accepted")
