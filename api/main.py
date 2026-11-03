from fastapi import FastAPI  # type: ignore[reportMissingImports]
from pydantic import BaseModel

from src.orchestrator.intellisphere_copilot import (
    IntelliSphereCopilot
)

app = FastAPI()

copilot = IntelliSphereCopilot()


class QuestionRequest(BaseModel):
    question: str


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask(
    request: QuestionRequest
):

    answer = copilot.ask(
        request.question
    )

    return {
        "answer": answer
    }