import json
from pathlib import Path

dashboard_file = (
    "evaluations/results/"
    "quality_dashboard.json"
)

with open(
    dashboard_file,
    "r"
) as f:

    current = json.load(f)

history_path = Path(
    "evaluations/history/"
    "quality_history.json"
)

if history_path.exists():

    with open(
        history_path,
        "r"
    ) as f:

        history = json.load(f)

else:

    history = []

history.append(current)

with open(
    history_path,
    "w"
) as f:

    json.dump(
        history,
        f,
        indent=4
    )
latest_score = history[-1][
    "overall_score"
]

previous_score = (
    history[-2][
        "overall_score"
    ]
    if len(history) > 1
    else latest_score
)

trend = (
    latest_score
    - previous_score
)

print(
    f"Trend Change: "
    f"{trend}"
)
print(
    f"History entries: "
    f"{len(history)}"
)