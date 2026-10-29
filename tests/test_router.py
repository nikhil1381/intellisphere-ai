# tests/test_router.py

from src.agents.router_agent import RouterAgent

router = RouterAgent()


def test_hr_question():
    route = router.determine_agent(
        "How many vacation days do employees receive?"
    )

    assert route.lower() == "hr"


def test_it_question():
    route = router.determine_agent(
        "My VPN is not working."
    )

    assert route.lower() == "it"


def test_finance_question():
    route = router.determine_agent(
        "What is the hotel reimbursement limit?"
    )

    assert route.lower() == "finance"