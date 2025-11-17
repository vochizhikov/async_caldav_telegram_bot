# Project.CalendarClient.client.py

from aiocaldav import DAVClient

class AsyncCalendarClient:
    def __init__(self, user_settings):
        self.user_settings = user_settings
        self.client = DAVClient(
            url=user_settings.caldav_url,
            username=user_settings.calendar_username,
            password=user_settings.caldav_password
        )
        self.calendar_url = user_settings.calendar_url

    async def get_calendars(self):
        """Вернуть список календарей асинхронно"""
        principal = await self.client.principal()
        calendars = await principal.calendars()
        return calendars

    async def get_calendar(self):
        """Вернуть объект календаря асинхронно"""
        return await self.client.calendar(url=self.calendar_url)