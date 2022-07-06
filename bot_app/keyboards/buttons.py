from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


async def keyboard(data, message=None, second_message=None):

    global keyboard
    if data == "start":
        button1 = InlineKeyboardButton("📝 Профиль", callback_data="profile")
        button2 = InlineKeyboardButton("🌐 Сайт", url="http://127.0.0.1/")
        keyboard = InlineKeyboardMarkup().add(button1).add(button2)

    elif data == "back":
        button1 = InlineKeyboardButton("🔙 Назад", callback_data="back")
        keyboard = InlineKeyboardMarkup().add(button1)
    return keyboard
