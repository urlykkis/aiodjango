from asgiref.sync import sync_to_async
from django.utils import timezone
from core.models import CustomUser


@sync_to_async
def get_user_by_id(telegram_id):
    try:
        user_db = CustomUser.objects.get(telegram_id=telegram_id)
        return user_db
    except CustomUser.DoesNotExist:
        return None


@sync_to_async
def add_user(username, telegram_id):
    user = CustomUser(
        username=username,
        email="none",
        is_staff=False,
        date_joined=timezone.now(),
        telegram_id=telegram_id,
        is_banned=False,
        is_ad_blocked=False
    )
    user.save()
    return user
