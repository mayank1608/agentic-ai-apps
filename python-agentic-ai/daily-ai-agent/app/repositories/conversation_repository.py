from datetime import datetime, timezone

from app.database import get_database

import asyncio

from app.services.sql_tools import get_recent_work_items_sync


async def save_message(
    session_id: str,
    role: str,
    content: str,
) -> None:
    database = get_database()

    await database.conversations.insert_one(
        {
            "session_id": session_id,
            "role": role,
            "content": content,
            "created_at": datetime.now(timezone.utc),
        }
    )


async def get_recent_messages(
    session_id: str,
    limit: int = 12,
) -> list[dict]:
    database = get_database()

    cursor = (
        database.conversations
        .find(
            {"session_id": session_id},
            {"_id": 0, "role": 1, "content": 1},
        )
        .sort("created_at", -1)
        .limit(limit)
    )

    documents = await cursor.to_list(length=limit)

    # The query returns newest first, but Claude needs oldest first.
    documents.reverse()

    return [
        {
            "role": document["role"],
            "content": document["content"],
        }
        for document in documents
    ]

""" 
MongoDB should remain responsible for:
    Agent tasks.
    Conversation history.
    User preferences.
    Tool execution logs. 

SQL Server should initially provide read-only business information such as:
    Work items.
    Application incidents.
    Release status.
    Project data.
    Reporting data.
    Do not let Claude generate unrestricted SQL. Give it narrowly defined tools backed by fixed, parameterized queries.  
"""
async def get_recent_work_items(
    assigned_to: str,
) -> list[dict]:
    return await asyncio.to_thread(
        get_recent_work_items_sync,
        assigned_to,
    )