from aiogram.types import CallbackQuery, ChatType, ParseMode
from bot_app.loader import dp
from bot_app.utils.db_api.functions import get_user_by_id
from bot_app.keyboards.buttons import keyboard
from bot_app.utils.ban_decorator import check_user_is_banned
from bot_app.utils.log_decorator import bot_logging


@dp.callback_query_handler(text="profile", chat_type=ChatType.PRIVATE)
@bot_logging
@check_user_is_banned
async def callback_profile(call: CallbackQuery):
    user_info = await get_user_by_id(call.from_user.id)
    text = f"*📝 Профиль: *\n\n" \
           f"*Имя пользователя на сайте*: `{user_info.username}`\n" \
           f"*ID пользователя на сайте*: `{user_info.id}`\n" \
           f"*Email на сайте*: `{user_info.email}`\n" \
           f"*Дата регистрации на сайте:* `{user_info.date_joined}`\n" \
           f"*Блокировка рекламы:* `{'Нет' if user_info.is_ad_blocked is False else 'Да'}`\n\n" \
           f"*Администратор на сайте*: `{'Нет' if user_info.is_staff is False else 'Да'}`"
    await call.message.edit_text(text,
                                 reply_markup=await keyboard("back"),
                                 parse_mode=ParseMode.MARKDOWN)


@dp.callback_query_handler(text="back", chat_type=ChatType.PRIVATE)
@bot_logging
@check_user_is_banned
async def callback_back(call: CallbackQuery):
    await call.message.edit_text("*💎 Меню*",
                                 reply_markup=await keyboard("start"),
                                 parse_mode=ParseMode.MARKDOWN)
