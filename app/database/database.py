"""Module to store the configuration and initialization of the database."""
import beanie
from motor import motor_asyncio as ma


async def init_db():
    client = ma.AsyncIOMotorClient("mongodb://localhost:27017")

    await beanie.init_beanie(
        database=client.db_name,
        document_models=["app.models.models.Skills", "app.models.models.Projects"],
    )
