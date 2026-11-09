from fastapi import FastAPI  # type: ignore[reportMissingImports]
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

from src.orchestrator.intellisphere_copilot import (
    IntelliSphereCopilot
)
from src.integrations.mcp.server import mcp
from src.integrations.a2a.routes import router as a2a_router
from src.integrations.a2a.sdk_routes import (
    register_a2a_sdk_routes
)

app = FastAPI(
    title="IntelliSphereAI",
    version="1.0.0",
    description="Enterprise HR, IT and Finance Assistant"
)
app.mount(
    "/mcp",
    mcp.streamable_http_app()
)
copilot = IntelliSphereCopilot()

#app.include_router(a2a_router)
register_a2a_sdk_routes(
    app
)

class QuestionRequest(BaseModel):
    question: str


class HealthResponse(BaseModel):
    status: str


class AskResponse(BaseModel):
    answer: str


@app.get(
    "/health",
    response_model=HealthResponse
)
def health():

    return HealthResponse(
        status="healthy"
    )


@app.post(
    "/ask",
    response_model=AskResponse
)
def ask(
    request: QuestionRequest
):

    answer = copilot.ask(
        request.question
    )

    return AskResponse(
        answer=answer
    )
def custom_openapi():

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="IntelliSphereAI",
        version="1.0.0",
        description="Enterprise HR, IT and Finance Assistant",
        routes=app.routes,
    )

    openapi_schema["openapi"] = "3.0.1"

    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi