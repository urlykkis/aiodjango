from aiogram.types import Message, CallbackQuery
from bot_app.utils.db_api.functions import get_user_by_id


def check_user_is_banned(func):
    async def wrapped(*args):
        user = await get_user_by_id(args[0].from_user.id)
        if user is None:
            return await func(*args)
        if user.is_banned is True:
            if isinstance(args[0], Message):
                return await args[0].answer("🚫 Вы забанены!")
            elif isinstance(args[0], CallbackQuery):
                return await args[0].message.edit_text("🚫 Вы забанены!")
            else:
                return
        else:
            return await func(*args)

    return wrapped
