import asyncio
import CalendarClient

from config import *


async def main():
    user_settings = CalendarClient.UserSettings(
        telegram_id=TELEGRAM_ID,
        calendar_username=MAIL,
        caldav_password=PASSWORD,
        caldav_url=CALDAV_URL,
        calendar_url=CALENDAR_URL
    )

    client = CalendarClient.AsyncCalendarClient(user_settings)

    calendars = await client.get_calendars()
    for cal in calendars:
        print("URL:", cal.url)
        print("Name:", getattr(cal, "name", "<нет имени>"))
        print("-" * 40)


asyncio.run(main())
