import logging
import uvicorn
import os
import asyncio

from django.core.asgi import get_asgi_application
from multiprocessing import Process

logging.basicConfig(level=logging.INFO)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adminbot.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


class MyServer:
    app = get_asgi_application()

    config = uvicorn.Config(app=app, loop=loop, port=8000)
    server = uvicorn.Server(config=config)

    @classmethod
    def run(cls):
        asyncio.run(cls.server.serve())


def run_app():
    from bot_loader import bot_process
    server = Process(target=MyServer.run)

    bot_process.start()
    server.start()


if __name__ == "__main__":
    run_app()

