from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as f

from .utils import load_config

config = load_config(str(Path(__file__).resolve().parent.parent / "config.yaml"))
DUMMY_TOPICS = config["topics"]


class DummyClassifier(nn.Module):
    """
    Dummy text classifier that outputs random probabilities over predefined topics.
    """

    def __init__(self, class_labels: list[str] | None = None) -> None:
        """
        Initialize the dummy classifier.

        Args:
             class_labels (Optional[List[str]]): List of class labels.
                Defaults to a copy of DUMMY_TOPICS.
        """
        super().__init__()
        # prevent changes to the original list
        self.class_labels = class_labels.copy() if class_labels is not None else DUMMY_TOPICS.copy()
        self.num_classes = len(self.class_labels)

    def forward(self, text: str) -> torch.Tensor:
        """
        Forward pass that generates random topic probabilities for input text.

        Args:
            text (str): Input text (never used).

        Returns:
            torch.Tensor: Random topic probabilities of shape (num_classes,).
        """
        # we assume batch_size is always 1
        logits = torch.randn(1, self.num_classes)
        probs = f.softmax(logits, dim=1)
        return probs.squeeze(0)


def probs_to_dict(probs: torch.Tensor, topics: list[str] | None = None) -> dict[str, float]:
    """
    Convert tensor of probabilities to a dictionary mapping topics to probabilities.

    Args:
        probs (torch.Tensor): Probabilities tensor of shape (num_classes,).
        topics (Optional[List[str]]): List of topic names.
            Defaults to a copy of DUMMY_TOPICS.

    Returns:
        Dict[str, float]: Dictionary mapping topics to probabilities of shape {topic: probability}.
    """
    # prevent changes to the original list
    topics = topics.copy() if topics is not None else DUMMY_TOPICS.copy()

    if len(topics) != probs.size(0):
        raise ValueError(f"Number of topics {len(topics)} does not match number of probabilities {probs.size(0)}.")

    return {topic: float(prob) for topic, prob in zip(topics, probs, strict=False)}
