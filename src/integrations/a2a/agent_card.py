AGENT_CARD = {
    "name": "IntelliSphereAI",
    "description": "Enterprise HR, IT and Finance assistant.",
    "version": "1.0.0",

    "capabilities": {
        "streaming": False
    },

    "supportedInterfaces": [
        {
            "url": "https://aca-intellisphere-api.proudmeadow-25abeb5a.eastus2.azurecontainerapps.io/a2a/jsonrpc",
            "protocolBinding": "A2A",
            "protocolVersion": "1.0"
        }
    ],

    "defaultInputModes": [
        "text"
    ],

    "defaultOutputModes": [
        "text"
    ],

    "skills": [
        {
            "id": "enterprise-assistant",
            "name": "Enterprise Assistant",
            "description": "Answers HR, IT and Finance questions.",
            "tags": [
                "hr",
                "it",
                "finance",
                "enterprise"
            ]
        }
    ]
}