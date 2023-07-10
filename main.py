from aiogram import executor
from handlers import dp

from config import bot


async def on_startup(dp):
    print("Бот запущен")


if __name__=='__main__':
    executor.start_polling(dp, 
                           on_startup=on_startup, 
                           skip_updates=True)