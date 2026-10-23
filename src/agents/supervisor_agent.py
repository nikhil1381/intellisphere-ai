from src.agents.hr_agent import HRAgent
from src.agents.it_agent import ITAgent
from src.agents.finance_agent import FinanceAgent


class SupervisorAgent:

    def __init__(self):

        self.hr = HRAgent()
        self.it = ITAgent()
        self.finance = FinanceAgent()

    def route(self, question):

        q = question.lower()

        if any(word in q for word in
               ["vacation", "leave", "remote work", "parental"]):
            return self.hr.answer(question)

        if any(word in q for word in
               ["vpn", "password", "laptop", "software"]):
            return self.it.answer(question)

        if any(word in q for word in
               ["expense", "travel", "hotel", "meal"]):
            return self.finance.answer(question)

        return "No suitable agent found."