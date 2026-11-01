import json

with open(
    "evaluations/results/quality_dashboard.json",
    "r"
) as f:

    quality = json.load(f)

with open(
    "evaluations/results/operations_dashboard.json",
    "r"
) as f:

    operations = json.load(f)

executive_dashboard = {

    "quality_score":
        quality[
            "overall_score"
        ],

    "deployment_approved":
        quality[
            "deployment_approved"
        ],

    "drift_status":
        operations[
            "status"
        ],

    "current_score":
        operations[
            "current_score"
        ],

    "previous_score":
        operations[
            "previous_score"
        ],

    "trend":
        operations[
            "trend"
        ]
}

with open(
    "evaluations/results/executive_dashboard.json",
    "w"
) as f:

    json.dump(
        executive_dashboard,
        f,
        indent=4
    )

print(
    json.dumps(
        executive_dashboard,
        indent=4
    )
)