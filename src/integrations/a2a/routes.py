from fastapi import APIRouter

from src.orchestrator.intellisphere_copilot import (
    IntelliSphereCopilot
)

from .agent_card import AGENT_CARD
from .models import (
    A2ATaskRequest,
    A2ATaskResponse,
    A2AMessage
)

router = APIRouter()

copilot = IntelliSphereCopilot()


@router.get("/.well-known/agent.json")
def get_agent_card():
    return AGENT_CARD


@router.post("/a2a/tasks")
def create_task(
    request: A2ATaskRequest
):

    question = request.message.parts[0]

    answer = copilot.ask(
        question
    )

    return A2ATaskResponse(
        message=A2AMessage(
            role="agent",
            parts=[answer]
        )
    )