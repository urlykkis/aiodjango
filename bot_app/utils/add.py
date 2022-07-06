
async def main():
    import os
    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sbhbot.settings')
    django.setup()

    from bot_app.utils.manageaccounts import AClient
    from bot_app.utils.db_api.functions import add_new_account, CustomUser, get_user_by_id

    user_db = await get_user_by_id(1046227957)

    with open("accs.txt", "r", encoding="utf-8") as file:
        accounts = file.read().splitlines()

    for account in accounts:
        try:
            args = account.split(":")
            client = AClient(args[0], args[1])
            response = client.login()
            print(account, response)
            if response == "Successfully logged in":
                await add_new_account(args[0], args[1], user_db, client.client.steam_id)
        except Exception as e:
            print(e)

import asyncio
asyncio.get_event_loop().run_until_complete(main())
