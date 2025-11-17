#bot.handlers.auth.py

from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State

from CalendarClient.client import AsyncCalendarClient
#from db.orm import save_user

router = Router()


class AuthStates(StatesGroup):
    waiting_for_email = State()
    waiting_for_password = State()
#
#
# @router.message()
# async def ask_email(message: types.Message, state: FSMContext):
#     await state.set_state(AuthStates.waiting_for_email)
#     await message.answer("Введите email CalDAV:")
#
#
# @router.message(StateFilter(AuthStates.waiting_for_email))
# async def get_email(message: types.Message, state: FSMContext):
#     await state.update_data(email=message.text)
#     await state.set_state(AuthStates.waiting_for_password)
#     await message.answer("Введите пароль:")
#
#
# @router.message(StateFilter(AuthStates.waiting_for_password))
# async def get_password(message: types.Message, state: FSMContext):
#     password = message.text
#     data = await state.get_data()
#
#     email = data["email"]
#
#     await message.answer("Подключаюсь к CalDAV...")
#
#     # Подключаемся к CalDAV
#     client = AsyncCalendarClient(email, password)
#
#     calendars = await client.get_calendars()
#
#     text = "Выберите календарь:\n"
#     for cal in calendars:
#         text += f"- {cal.name or 'Без названия'}\n"
#
#     # Сохраняем пользователя
#     await save_user(message.from_user.id, email, password)
#
#     await message.answer(text)
