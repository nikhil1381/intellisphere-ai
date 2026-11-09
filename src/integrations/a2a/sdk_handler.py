from a2a.server.request_handlers.request_handler import (
    RequestHandler,
)

from a2a.utils.errors import UnsupportedOperationError
from a2a.types import a2a_pb2

from src.orchestrator.intellisphere_copilot import (
    IntelliSphereCopilot,
)
from a2a.server.routes.agent_card_routes import (
    create_agent_card_routes,
)

from a2a.server.routes.jsonrpc_routes import (
    create_jsonrpc_routes,
)

from src.integrations.a2a.sdk_handler import (
    IntelliSphereRequestHandler,
)

class IntelliSphereRequestHandler(RequestHandler):

    def __init__(self):
        self.copilot = IntelliSphereCopilot()

    async def on_message_send(
        self,
        params,
        context,
    ):
        raise NotImplementedError()

    async def on_get_task(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_list_tasks(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_cancel_task(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_message_send_stream(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_create_task_push_notification_config(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_get_task_push_notification_config(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_subscribe_to_task(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_list_task_push_notification_configs(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_delete_task_push_notification_config(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_get_extended_agent_card(
        self,
        params,
        context,
    ):
        raise UnsupportedOperationError()

    async def on_message_send(
    self,
    params,
    context,
    ):
        question = ""

        if params.message.parts:
            question = params.message.parts[0].text

        answer = self.copilot.ask(question)

        response_part = a2a_pb2.Part()
        response_part.text = answer

        response_message = a2a_pb2.Message()
        response_message.role = a2a_pb2.ROLE_AGENT
        response_message.parts.append(response_part)

        return response_message