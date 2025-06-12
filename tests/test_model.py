import pytest
import torch

from app.model import DUMMY_TOPICS, DummyClassifier, probs_to_dict


def test_dummy_classifier_init():
    model = DummyClassifier()
    assert model.num_classes == len(DUMMY_TOPICS)
    assert model.class_labels == DUMMY_TOPICS


def test_dummy_classifier_forward():
    model = DummyClassifier()
    probs = model("some test")
    assert isinstance(probs, torch.Tensor)
    assert probs.shape == (len(DUMMY_TOPICS),)
    # considers floating point error
    assert torch.all(probs >= 0) and torch.isclose(probs.sum(), torch.tensor(1.0), atol=1e-5)


def test_probs_to_dict_default_topics():
    model = DummyClassifier()
    probs = model("test")
    prob_dict = probs_to_dict(probs)
    assert isinstance(prob_dict, dict)
    assert set(prob_dict.keys()) == set(DUMMY_TOPICS)
    assert all(isinstance(v, float) for v in prob_dict.values())


def test_probs_to_dict_custom_topics():
    probs = torch.tensor([0.1, 0.9])
    topics = ["A", "B"]
    result = probs_to_dict(probs, topics)
    assert set(result.keys()) == {"A", "B"}
    # considers floating point error
    assert pytest.approx(result["A"], abs=1e-5) == 0.1
    assert pytest.approx(result["B"], abs=1e-5) == 0.9


def test_probs_to_dict_raises():
    probs = torch.tensor([0.1, 0.2])
    topics = ["A"]  # length mismatch
    with pytest.raises(ValueError):
        probs_to_dict(probs, topics)
