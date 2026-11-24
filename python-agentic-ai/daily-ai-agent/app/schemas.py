from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=4000,
        examples=["Add review authentication API to my tasks"],
    )

    session_id: str = Field(
        min_length=1,
        max_length=100,
        examples=["mayank-session-001"],
    )


class ChatResponse(BaseModel):
    response: str