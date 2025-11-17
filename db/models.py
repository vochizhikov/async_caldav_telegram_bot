# project.db.models.py
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime, Text, MetaData, Integer, String

from .db_config import Base



class CalendarsORM(Base):
    __tablename__ = "calendars"

    id_owner: Mapped[int]
    id: Mapped[str] = mapped_column(String, primary_key=True)
    name: Mapped[String] = mapped_column(DateTime, nullable=False)
    active: Mapped[int] = mapped_column(DateTime, nullable=False, default=0)


class UsersDB(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column()
    calendar_username: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    caldav_password: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    caldav_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    calendar_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    active: Mapped[int] = mapped_column(nullable=False, default=0)


#
#
# metadata_obj = MetaData()
#

#
#
# class CalendarEventORM(Base):
#     __tablename__ = "calendar_events"
#
#     # PRIMARY KEY
#     id_uuid: Mapped[str] = mapped_column(String, primary_key=True)  # UID
#
#     # Доп. поля
#     rec_id: Mapped[Optional[str]] = mapped_column(String, nullable=True)
#     start: Mapped[datetime] = mapped_column(DateTime, nullable=False)
#     end: Mapped[datetime] = mapped_column(DateTime, nullable=False)
#     rrule: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
#     name: Mapped[str] = mapped_column(String, nullable=False)
#     conference_url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
