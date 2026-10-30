import json

with open(
    "evaluations/results/rag_report.json"
) as f:

    rag = json.load(f)

with open(
    "evaluations/results/groundedness_report.json"
) as f:

    grounded = json.load(f)

rag_score = rag["success_rate"]

grounded_score = grounded["success_rate"]

overall_score = round(
    (
        rag_score +
        grounded_score
    ) / 2,

    2
)

deployment_approved = (
    overall_score >= 90
)

dashboard = {
    "rag_score": rag_score,
    "groundedness_score": grounded_score,
    "overall_score": overall_score,
    "deployment_approved":
        deployment_approved
}

with open(
    "evaluations/results/quality_dashboard.json",
    "w"
) as f:

    json.dump(
        dashboard,
        f,
        indent=4
    )

print(
    json.dumps(
        dashboard,
        indent=4
    )
)
