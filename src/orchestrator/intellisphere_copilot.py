from src.agents.router_agent import RouterAgent
from src.agents.hr_agent import HRAgent
from src.agents.it_agent import ITAgent
from src.agents.finance_agent import FinanceAgent

from src.services.memory_service import MemoryService


class IntelliSphereCopilot:

    def __init__(self):

        self.router = RouterAgent()

        self.hr = HRAgent()
        self.it = ITAgent()
        self.finance = FinanceAgent()
        self.memory = MemoryService()

    def ask(self, question):

        self.memory.add_message(
            "user",
            question
        )

        route = self.router.determine_agent(question)

        print(f"\n[Router Selected]: {route}")

        if route == "HR":
            answer = self.hr.answer(question)

        elif route == "IT":
            answer = self.it.answer(question)

        elif route == "FINANCE":
            answer = self.finance.answer(question)

        else:
            answer = "Unable to determine agent."

        self.memory.add_message(
            "assistant",
            answer
        )

        return answer

    def show_memory(self):

        return self.memory.get_messages()

    def clear_memory(self):

        self.memory.clear()