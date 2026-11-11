from mcp.server.fastmcp import FastMCP

from src.orchestrator.intellisphere_copilot import (
    IntelliSphereCopilot
)

print("Starting MCP Server...")

mcp = FastMCP("IntelliSphereAI")

print("MCP Server created")

copilot = IntelliSphereCopilot()


@mcp.tool()
def ask_intellisphere(question: str) -> str:
    """
    Ask IntelliSphereAI a question.

    Routes questions automatically
    to HR, IT or Finance agents.
    """

    return copilot.ask(question)


if __name__ == "__main__":
    print("Starting MCP HTTP Server...")

    mcp.run(
        transport="streamable-http"
    )