from azure.monitor.opentelemetry import (
    configure_azure_monitor
)

from src.config.settings import Settings


def initialize_monitoring():
    print(
        "Initializing Azure Monitor..."
    )
    configure_azure_monitor(
        connection_string=
            Settings.APPINSIGHTS_CONNECTION_STRING
    )
    print(
        "Azure Monitor initialized."
    )