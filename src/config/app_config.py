import os


class AppConfig:

    ENVIRONMENT = os.getenv(
        "APP_ENVIRONMENT",
        "development"
    )

    DEBUG = ENVIRONMENT == "development"