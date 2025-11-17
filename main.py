#project.main

# import CalendarClient
# import asyncio
# from config import *
# from db.orm import create_tables, insert_user
#
#
# asyncio.run(insert_user())

import asyncio
from bot.bot import bot
from bot.dispatcher import dp

from bot.handlers import start, auth, calendars


async def main():
    dp.include_router(start.router)
    dp.include_router(auth.router)
    dp.include_router(calendars.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
