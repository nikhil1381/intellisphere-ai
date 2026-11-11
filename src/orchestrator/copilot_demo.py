from dotenv import load_dotenv

load_dotenv()

from src.orchestrator.intellisphere_copilot import IntelliSphereCopilot

copilot = IntelliSphereCopilot()

questions = [

    "How many vacation days do employees receive?",

    "My VPN is not working",

    "What is the hotel reimbursement limit?"
]

for question in questions:

    print("\n" + "=" * 60)

    print(f"\nQUESTION:\n{question}")

    answer = copilot.ask(question)

    print("\nANSWER:\n")
    print(answer)
    
    from monitoring.dashboard import print_dashboard
    print_dashboard()

    from monitoring.agent_scorecard import (
    print_agent_scorecard
    )
    from monitoring.kb_health import (
    KnowledgeBaseHealth
    )
    KnowledgeBaseHealth.print_kb_health()