import pytest

from papers_pipeline.config import TopicConfig
from papers_pipeline.models import Paper
from papers_pipeline.topics import TopicDecision, build_topic_gate
from topic_plugin import accept_topic


@pytest.mark.parametrize(
    ("title", "abstract", "decision"),
    [
        (
            "Zero-Shot Text-to-Speech",
            "A diffusion model for speech synthesis.",
            TopicDecision(True, "accepted"),
        ),
        (
            "Fast TTS",
            "A transformer that reads text aloud.",
            TopicDecision(True, "accepted"),
        ),
        (
            "Robust Speech Recognition",
            "A neural text-to-speech front end for automatic speech recognition.",
            TopicDecision(False, "matched excluded term: speech recognition"),
        ),
        (
            "Text-to-Speech in Classrooms",
            "A survey of teachers who use screen readers.",
            TopicDecision(False, "missing ML signal"),
        ),
        (
            "Neural Image Captioning",
            "A transformer model; code at https://example.test.",
            TopicDecision(False, "missing TTS signal"),
        ),
    ],
)
def test_accept_topic_applies_legacy_rule(
    paper: Paper, title: str, abstract: str, decision: TopicDecision
) -> None:
    candidate = paper.model_copy(update={"title": title, "abstract": abstract})

    assert accept_topic(candidate) == decision


def test_papers_yml_plugin_reference_builds_repository_gate(paper: Paper) -> None:
    gate = build_topic_gate(TopicConfig(plugin="topic_plugin:accept_topic"))
    candidate = paper.model_copy(
        update={"title": "Neural Vocoder", "abstract": "A GAN vocoder."}
    )

    assert gate(candidate) == TopicDecision(True, "accepted")
