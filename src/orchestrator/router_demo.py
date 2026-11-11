from dotenv import load_dotenv

load_dotenv()

from src.agents.router_agent import RouterAgent

router = RouterAgent()

questions = [
    "How many vacation days do employees receive?",
    "My VPN is not working.",
    "What is the hotel reimbursement limit?"
]

for q in questions:

    print("\nQUESTION:")
    print(q)

    print("ROUTE:")
    print(router.determine_agent(q))