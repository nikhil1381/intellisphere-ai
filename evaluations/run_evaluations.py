import json

from src.agents.router_agent import RouterAgent

router = RouterAgent()

with open(
    "evaluations/hr_questions.json",
    "r"
) as f:

    questions = json.load(f)

passed = 0

for item in questions:
    print(item)
    route = router.determine_agent(
        item["question"]
    )

    if route.lower() == item["expected_agent"]:
        passed += 1

print(
    f"Passed {passed}/{len(questions)}"
)