from fastapi import FastAPI
from pydantic import BaseModel, Field, RootModel

from .model import DummyClassifier, probs_to_dict

EXAMPLE_PROBABILITIES = {
    "Soccer": 0.032,
    "Food": 0.172,
    "Stockmarket": 0.048,
    "Yoga": 0.138,
    "Beauty": 0.264,
    "Politics": 0.100,
    "Technology": 0.246,
}

app = FastAPI()


class PredictRequest(BaseModel):
    """
    Request model containing input text to classify.
    """

    text: str = Field(..., examples=["This is an awesome Instagram post"])


class PredictResponse(RootModel[dict[str, float]]):
    """
    Response model containing predicted topic probabilities as a dictionary.
    """

    pass


# initiate model once to avoid initiation on each request
model = DummyClassifier()


@app.post(
    "/predict",
    response_model=PredictResponse,
    responses={200: {"content": {"application/json": {"example": EXAMPLE_PROBABILITIES}}}},
)
async def predict_topic_probabilities(request: PredictRequest):
    """
    Predict topic probabilities for a given text.
    """
    raw_probs = model(request.text)
    probs_dict = probs_to_dict(raw_probs)
    return PredictResponse.model_validate(probs_dict)
