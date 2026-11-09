from a2a.server.routes.agent_card_routes import (
    create_agent_card_routes,
)

from a2a.server.routes.jsonrpc_routes import (
    create_jsonrpc_routes,
)

from a2a.server.routes.fastapi_routes import (
    add_a2a_routes_to_fastapi,
)

from src.integrations.a2a.sdk_agent_card import (
    build_agent_card,
)

from src.integrations.a2a.sdk_handler import (
    IntelliSphereRequestHandler,
)


def register_a2a_sdk_routes(app):

    handler = IntelliSphereRequestHandler()

    agent_card = build_agent_card()

    agent_card_routes = create_agent_card_routes(
        agent_card
    )

    jsonrpc_routes = create_jsonrpc_routes(
        request_handler=handler,
        rpc_url="/a2a"
    )

    add_a2a_routes_to_fastapi(
        app,
        agent_card_routes=agent_card_routes,
        jsonrpc_routes=jsonrpc_routes,
    )