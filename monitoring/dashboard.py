from monitoring.metrics import Metrics


def print_dashboard():

    avg_latency = 0

    if Metrics.total_requests:

        avg_latency = (
            Metrics.total_latency
            /
            Metrics.total_requests
        )

    print(
        "\n=== IntelliSphereAI Dashboard ==="
    )

    print(
        f"Requests: "
        f"{Metrics.total_requests}"
    )

    print(
        f"Average Latency: "
        f"{avg_latency:.2f}s"
    )

    print(
        f"Agent Usage: "
        f"{Metrics.routed_agents}"
    )