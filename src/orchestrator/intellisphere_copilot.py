from src.agents.router_agent import RouterAgent
from src.agents.hr_agent import HRAgent
from src.agents.it_agent import ITAgent
from src.agents.finance_agent import FinanceAgent


class IntelliSphereCopilot:

    def __init__(self):

        self.router = RouterAgent()

        self.hr = HRAgent()
        self.it = ITAgent()
        self.finance = FinanceAgent()

    def ask(self, question):

        route = self.router.determine_agent(question)

        print(f"\n[Router Selected]: {route}")

        if route == "HR":
            return self.hr.answer(question)

        if route == "IT":
            return self.it.answer(question)

        if route == "FINANCE":
            return self.finance.answer(question)

        return "Unable to determine agent."