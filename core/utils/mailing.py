from asgiref.sync import async_to_sync

from bot_app.loader import bot
from bot_loader import bot_process
from core.models import CustomUser


@async_to_sync
async def send_message(user_id, text):
    return await bot.send_message(chat_id=user_id, text=text)


@async_to_sync
async def send_photo(user_id, text, photo):
    return await bot.send_photo(chat_id=user_id, caption=text, photo=photo)


def set_user_staff(telegram_id):
    obj = CustomUser.objects.filter(CustomUser.telegram_id == telegram_id).first()
    obj.is_staff = True
    return {
        "user": obj.telegram_id,
        "is_staff": obj.is_staff
    }


def restart_bot():
    bot_process.kill()
    bot_process.start()


def shutdown_bot():
    bot_process.kill()


def startup_bot():
    bot_process.start()
