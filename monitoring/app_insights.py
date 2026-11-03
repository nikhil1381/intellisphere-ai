from azure.monitor.opentelemetry import (
    configure_azure_monitor
)

from src.config.settings import Settings


def initialize_monitoring():

    print(
        "Initializing Azure Monitor..."
    )

    connection_string = (
        Settings.APPINSIGHTS_CONNECTION_STRING
    )

    if (
        not connection_string
    ):

        print(
            "Azure Monitor not configured."
        )

        return

    configure_azure_monitor(
        connection_string=
            connection_string
    )

    print(
        "Azure Monitor initialized."
    )