from src.agents.router_agent import RouterAgent
from src.agents.hr_agent import HRAgent
from src.agents.it_agent import ITAgent
from src.agents.finance_agent import FinanceAgent

from src.services.logger_service import LoggerService
from src.services.memory_service import MemoryService

from monitoring.request_tracker import RequestTracker
from monitoring.telemetry import Telemetry

import time


class IntelliSphereCopilot:

    def __init__(self):

        self.router = RouterAgent()

        self.hr = HRAgent()
        self.it = ITAgent()
        self.finance = FinanceAgent()

        self.memory = MemoryService()

    def ask(self, question):

        request_id = (
            RequestTracker
            .generate_request_id()
        )

        Telemetry.log_event(
            request_id,
            "REQUEST",
            "Conversation started"
        )

        start_time = time.time()

        self.memory.add_message(
            "user",
            question
        )

        LoggerService.log(
            f"Question received: {question}"
        )

        route = self.router.determine_agent(
            question
        )

        Telemetry.log_event(
            request_id,
            "ROUTING",
            f"Selected agent: {route}"
        )

        print(
            f"\n[Router Selected]: {route}"
        )

        if route == "HR":

            answer = self.hr.answer(
                question
            )

        elif route == "IT":

            answer = self.it.answer(
                question
            )

        elif route == "FINANCE":

            answer = self.finance.answer(
                question
            )

        else:

            answer = (
                "Unable to determine agent."
            )

        self.memory.add_message(
            "assistant",
            answer
        )

        LoggerService.log(
            f"Agent selected: {route}"
        )

        LoggerService.log(
            "Response generated"
        )

        latency = (
            time.time()
            - start_time
        )

        Telemetry.log_event(
            request_id,
            "LATENCY",
            f"{latency:.2f} seconds"
        )

        return answer

    def show_memory(self):

        return self.memory.get_messages()

    def clear_memory(self):

        self.memory.clear()