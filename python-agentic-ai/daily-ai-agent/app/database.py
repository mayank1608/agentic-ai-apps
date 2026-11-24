from pymongo import AsyncMongoClient

from app.config import settings


mongo_client: AsyncMongoClient | None = None
database = None


async def connect_to_mongo() -> None:
    global mongo_client, database

    mongo_client = AsyncMongoClient(settings.mongo_uri)

    # Fail during startup if MongoDB cannot be reached.
    await mongo_client.admin.command("ping")

    database = mongo_client[settings.mongo_db]

    # Helpful indexes for later queries.
    await database.tasks.create_index("completed")
    await database.tasks.create_index("created_at")
    await database.conversations.create_index(
        [("session_id", 1), ("created_at", -1)]
    )

    print("Connected to MongoDB")


async def close_mongo_connection() -> None:
    global mongo_client

    if mongo_client is not None:
        await mongo_client.close()

    print("MongoDB connection closed")


def get_database():
    if database is None:
        raise RuntimeError("MongoDB is not initialized")

    return database