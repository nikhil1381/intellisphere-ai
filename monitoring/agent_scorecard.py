from monitoring.metrics import Metrics


def print_agent_scorecard():

    print(
        "\n=== Agent Scorecard ==="
    )

    for agent, data in (
        Metrics.agents.items()
    ):

        avg_latency = 0
        successes = data.get(
            "successes",
            0
        )

        failures = data.get(
            "failures",
            0
        )

        total = (
            successes
            + failures
        )

        success_rate = 0

        if total:

            success_rate = (
                successes
                / total
            ) * 100
        if data["requests"]:

            avg_latency = (
                data["latency_total"]
                /
                data["requests"]
            )

        print(
            f"\nAgent: {agent}"
        )

        print(
            f"Requests: "
            f"{data['requests']}"
        )

        print(
            f"Average Latency: "
            f"{avg_latency:.2f}s"
        )

        print(
            f"Success Rate: "
            f"{success_rate:.2f}%"
        )