from datetime import UTC, datetime
import json

from src.plugins.rag_plugin import RAGPlugin

rag = RAGPlugin()

with open(
    "evaluations/hr_groundedness.json",
    "r"
) as f:

    questions = json.load(f)

passed = 0

for item in questions:

    result = rag.answer_with_context(
        item["question"]
    )

    context = result["context"].lower()

    answer = result["answer"].lower()

    expected = (
        item["expected_phrase"]
        .lower()
    )

    grounded = (
        expected in context
        and
        expected in answer
    )

    print(
        f"\nQuestion: {item['question']}"
    )

    print(
        f"Grounded: {grounded}"
    )

    if grounded:
        passed += 1

print(
    f"\nPassed {passed}/{len(questions)}"
)

success_rate = round(
    (passed / len(questions)) * 100,
    2
)

report = {
    "timestamp": datetime.now(
        UTC
    ).isoformat(),

    "total": len(questions),

    "passed": passed,

    "failed": len(questions) - passed,

    "success_rate": success_rate
}

with open(
    "evaluations/results/groundedness_report.json",
    "w"
) as f:

    json.dump(
        report,
        f,
        indent=4
    )