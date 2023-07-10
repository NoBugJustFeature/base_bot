from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/start"),
        ],
    ],
    resize_keyboard=True
)