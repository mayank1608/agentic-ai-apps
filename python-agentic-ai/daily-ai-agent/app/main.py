from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings
from app.database import (
    close_mongo_connection,
    connect_to_mongo,
)
from app.schemas import ChatRequest, ChatResponse
from app.services.agent_service import run_agent


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()

    yield

    await close_mongo_connection()


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/health")
async def health() -> dict:
    return {
        "status": "healthy",
        "application": settings.app_name,
    }


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    response = await run_agent(
        message=request.message,
        session_id=request.session_id,
    )

    return ChatResponse(response=response)