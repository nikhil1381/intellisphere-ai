from pydantic import BaseModel


class A2AMessage(BaseModel):
    role: str
    parts: list


class A2ATaskRequest(BaseModel):
    message: A2AMessage


class A2ATaskResponse(BaseModel):
    message: A2AMessage

class JsonRpcRequest(BaseModel):
    jsonrpc: str
    id: str | int | None = None
    method: str
    params: dict