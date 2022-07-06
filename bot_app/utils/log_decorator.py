from aiogram.types import Message, CallbackQuery


def bot_logging(func):
    def wrapped(*args, **kwargs):
        with open("./logs/logging.txt", "a+", encoding="utf-8") as file:
            if isinstance(args[0], Message):
                action: Message = args[0]
                file.write(f"UID: {action.from_user.id} - Message: {action.text}\n")
            elif isinstance(args[0], CallbackQuery):
                action: CallbackQuery = args[0]
                file.write(f"UID: {action.from_user.id} - Call: {action.data}\n")

            return func(*args)
    return wrapped
