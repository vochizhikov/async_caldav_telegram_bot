# Project.CalendarClient.models.py
from dataclasses import dataclass

from datetime import datetime


@dataclass
class CalendarEvent:
    id: str
    rec_id: str
    start: datetime
    end: datetime
    rrule: str
    name: str
    conference_url: str = None

@dataclass
class UserSettings:
    telegram_id: int
    calendar_username: str
    caldav_password: str
    caldav_url: str
    calendar_url: str
