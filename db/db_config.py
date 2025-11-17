# project.db.db_config.py

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import text
import asyncio

from config import *

DATABASE_URL = f"postgresql+asyncpg://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}"

engine = create_async_engine(DATABASE_URL)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False) #autoflush=False

class Base(DeclarativeBase):
    pass


async def test_connection():
    async with engine.connect() as conn:
        result = await conn.execute(text("select version()"))
        print(result.scalar())


# asyncio.run(test_connection())