from multiprocessing import Process


class MyBot:
    from aiogram import executor
    from bot_app.app import on_startup
    from bot_app.handlers import dp

    @classmethod
    def run(cls):
        cls.executor.start_polling(cls.dp, on_startup=cls.on_startup, skip_updates=True)


bot_process = Process(target=MyBot.run)
