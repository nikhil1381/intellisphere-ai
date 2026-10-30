from datetime import datetime, UTC


class Telemetry:

    @staticmethod
    def log_event(
        request_id,
        event_type,
        message
    ):

        timestamp = (
            datetime.now(UTC)
            .isoformat()
        )

        print(
            f"[{timestamp}] "
            f"[{request_id}] "
            f"[{event_type}] "
            f"{message}"
        )