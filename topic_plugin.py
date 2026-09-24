from papers_pipeline.models import Paper
from papers_pipeline.topics import TopicDecision


def accept_topic(paper: Paper) -> TopicDecision:
    return TopicDecision(accepted=True, reason="repository plugin accepted paper")
