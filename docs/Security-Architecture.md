# IntelliSphere AI Security Architecture

## Development Environment

Secrets stored in:

- .env file

Used for:

- Azure OpenAI API Key
- Azure AI Search Key

## Production Design

Secrets stored in:

- Azure Key Vault

Authentication:

- Managed Identity

Authorization:

- Azure RBAC

Benefits:

- No secrets in source code
- No secrets in GitHub
- Centralized secret rotation
- Auditable access