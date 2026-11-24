from datetime import datetime, timezone

from bson import ObjectId
from pymongo import ReturnDocument

from app.database import get_database


def serialize_task(task: dict | None) -> dict | None:
    if task is None:
        return None

    result = dict(task)
    result["id"] = str(result.pop("_id"))

    if isinstance(result.get("created_at"), datetime):
        result["created_at"] = result["created_at"].isoformat()

    if isinstance(result.get("updated_at"), datetime):
        result["updated_at"] = result["updated_at"].isoformat()

    return result


async def create_task(
    title: str,
    due_date: str | None = None,
    priority: str = "medium",
) -> dict:
    database = get_database()

    priority = priority.lower()

    if priority not in {"low", "medium", "high"}:
        raise ValueError("Priority must be low, medium, or high")

    document = {
        "title": title.strip(),
        "due_date": due_date,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc),
    }

    result = await database.tasks.insert_one(document)
    saved_task = await database.tasks.find_one(
        {"_id": result.inserted_id}
    )

    return serialize_task(saved_task)


async def list_tasks(
    status: str = "open",
    limit: int = 20,
) -> list[dict]:
    database = get_database()

    limit = max(1, min(limit, 50))

    query: dict = {}

    if status == "open":
        query["completed"] = False
    elif status == "completed":
        query["completed"] = True
    elif status != "all":
        raise ValueError("Status must be open, completed, or all")

    cursor = (
        database.tasks
        .find(query)
        .sort("created_at", -1)
        .limit(limit)
    )

    tasks = await cursor.to_list(length=limit)

    return [serialize_task(task) for task in tasks]


async def complete_task(task_id: str) -> dict:
    database = get_database()

    if not ObjectId.is_valid(task_id):
        raise ValueError("The task ID is not valid")

    updated_task = await database.tasks.find_one_and_update(
        {"_id": ObjectId(task_id)},
        {
            "$set": {
                "completed": True,
                "updated_at": datetime.now(timezone.utc),
            }
        },
        return_document=ReturnDocument.AFTER,
    )

    if updated_task is None:
        raise ValueError("Task was not found")

    return serialize_task(updated_task)