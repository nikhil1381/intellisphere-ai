import json
from datetime import UTC, datetime

from src.plugins.rag_plugin import RAGPlugin

rag = RAGPlugin()

with open(
    "evaluations/hr_rag_questions.json",
    "r"
) as f:

    questions = json.load(f)

results = []
passed = 0
QUALITY_THRESHOLD = 90.0

for item in questions:

    answer = rag.answer(
        item["question"]
    )

    answer_text = answer.lower()

    success = all(
        keyword.lower() in answer_text
        for keyword in item["expected_keywords"]
    )
    
    if success:
        passed += 1

    results.append(
        {
            "question": item["question"],
            "answer": answer,
            "passed": success
        }
    )

report = {
    "timestamp": str(datetime.now(UTC)),
    "total": len(questions),
    "passed": passed,
    "failed": len(questions) - passed,
    "success_rate": round(
        (passed / len(questions)) * 100,
        2
    ),
    "results": results
}

with open(
    "evaluations/results/rag_report.json",
    "w"
) as f:

    json.dump(
        report,
        f,
        indent=4
    )

print(
    f"Passed {passed}/{len(questions)}"
)

success_rate = round(
    (passed / len(questions)) * 100,
    2
)
if success_rate < QUALITY_THRESHOLD:
    raise Exception(
        f"Quality Gate Failed: "
        f"{success_rate}% "
        f"is below "
        f"{QUALITY_THRESHOLD}%"
    )
def answer_with_context(self, question):

    context = self.search_plugin.search_documents(
        question
    )

    response = self.client.chat.completions.create(
        ...
    )

    return {
        "context": context,
        "answer": response.choices[0].message.content
    }