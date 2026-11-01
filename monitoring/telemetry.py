from datetime import datetime, UTC
from opentelemetry import trace
tracer = trace.get_tracer(
    "intellisphere"
)
class Telemetry:

    @staticmethod
    def log_event(
        request_id,
        event_type,
        message,
    ):  

        timestamp = (
            datetime.now(UTC)
            .isoformat()
        )

        with tracer.start_as_current_span(
            event_type
        ) as span:

            span.set_attribute(
                "request_id",
                request_id
            )

            span.set_attribute(
                "event_type",
                event_type
            )

            span.set_attribute(
                "message",
                message
            )

        print(
            f"[{timestamp}] "
            f"[{request_id}] "
            f"[{event_type}] "
            f"{message}"
        )