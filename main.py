#project.main

import CalendarClient
import asyncio
from config import *
from db.orm import create_tables, insert_user


asyncio.run(insert_user())
