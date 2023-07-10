#get data from venv
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

ADMIN_GROUP = os.getenv("ADMIN_GROUP")


#for FSM
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()


#init dispatcher 
from aiogram import Bot, Dispatcher

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)


#init database
from psycopg2 import connect

connection=connect(host=DB_HOST,
                   user=DB_USER,
                   password=DB_PASSWORD,
                   database=DB_DATABASE)
                   
connection.autocommit = True