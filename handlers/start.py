from aiogram.types import Message
from config import dp

from keyboards import kb_menu


@dp.message_handler(text="/start")
async def start(msg: Message):
    await msg.answer("Здравствуйте!\n"
                     "Чем могу помочь?",
                     reply_markup=kb_menu)