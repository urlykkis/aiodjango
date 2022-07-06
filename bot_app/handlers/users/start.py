from aiogram.types import Message, ChatType, ParseMode
from bot_app.loader import dp
from bot_app.utils.db_api.functions import get_user_by_id, add_user
from bot_app.keyboards.buttons import keyboard
from bot_app.utils.ban_decorator import check_user_is_banned
from bot_app.utils.log_decorator import bot_logging


@dp.message_handler(commands=['start'], chat_type=ChatType.PRIVATE)
@bot_logging
@check_user_is_banned
async def command_start(message: Message):
    if await get_user_by_id(message.from_user.id) is None:
        await add_user(message.from_user.username, message.from_user.id)

    await message.answer("*💎 Меню*",
                         reply_markup=await keyboard("start"),
                         parse_mode=ParseMode.MARKDOWN)
