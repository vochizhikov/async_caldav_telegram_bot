#project.db.orm
from .db_config import async_session, Base, engine
from .models import UsersDB

async def insert_user():
    async with async_session() as session:
        user = UsersDB(telegram_id=1231123123, calendar_username='test2')
        session.add(user)

        await session.commit()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)