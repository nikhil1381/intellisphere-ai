from a2a.types import a2a_pb2


def build_agent_card():

    card = a2a_pb2.AgentCard()

    card.name = "IntelliSphereAI"
    card.description = (
        "Enterprise HR, IT and Finance assistant."
    )
    card.version = "1.0.0"

    card.default_input_modes.append("text")
    card.default_output_modes.append("text")

    #
    # Interface
    #
    interface = card.supported_interfaces.add()

    interface.url = "https://aca-intellisphere-api.proudmeadow-25abeb5a.eastus2.azurecontainerapps.io/a2a"
    interface.protocol_binding = "JSONRPC"
    interface.protocol_version = "1.0"    

    #
    # Skill
    #
    skill = card.skills.add()

    skill.id = "enterprise-assistant"
    skill.name = "Enterprise Assistant"
    skill.description = (
        "Answers HR, IT and Finance questions."
    )

    skill.tags.extend([
        "hr",
        "it",
        "finance",
        "enterprise",
    ])

    #
    # Capabilities
    #
    card.capabilities.streaming = False
    card.capabilities.push_notifications = False
    card.capabilities.extended_agent_card = False

    return card