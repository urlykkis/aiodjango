import os

from django.utils import timezone
from aiogram.types import InputFile
from django.http import HttpResponse
from django.shortcuts import render
from .models import CustomUser
from .utils.mailing import send_message, send_photo, restart_bot, startup_bot, shutdown_bot
from django.core.files.storage import FileSystemStorage


def admin_stats(request):
    users = CustomUser.objects.all()
    total_users = len(users)
    total_blocked = len([True for user in users if user.is_banned is True])
    total_admins = len([True for user in users if user.is_staff is True])
    total_noads = len([True for user in users if user.is_ad_blocked is True])
    count_users_today = len([True for user in users if (timezone.now() - user.date_joined).days <= 0])
    count_users_week = len([True for user in users if (timezone.now() - user.date_joined).days <= 7])
    count_users_month = len([True for user in users if (timezone.now() - user.date_joined).days <= 31])
    return render(request,
                  "admin/stats/home.html",
                  {"total_users": total_users,
                   "total_blocked": total_blocked,
                   "total_admins": total_admins,
                   "total_noads": total_noads,
                   "new_users_today": count_users_today,
                   "new_users_week": count_users_week,
                   "new_users_month": count_users_month})


def manage(request):
    return render(request, "admin/manage/home.html")


def mailing(request):
    if request.method == "POST":
        users = CustomUser.objects.all()
        total_sended = 0

        for user in users:
            try:
                send_message(user.telegram_id, request.POST["text"])
                total_sended += 1
            except Exception as e:
                print(e)

        response = {
            "success": True,
            "total_users": len(users),
            "total_sended": total_sended,
        }

        return HttpResponse(str(response))
    else:
        return render(request, "admin/manage/home.html")


def ban(request):
    if request.method == "POST":
        user_id = int(request.POST["userId"])
        user = CustomUser.objects.get(telegram_id=user_id)

        if user:
            user.is_banned = True
            user.save()
            response = {"success": True}
        else:
            response = {"success": False, "error": "User not found"}

        return HttpResponse(str(response))
    else:
        return render(request, "admin/manage/home.html")


def unban(request):
    if request.method == "POST":
        user_id = int(request.POST["userId"])
        user = CustomUser.objects.get(telegram_id=user_id)

        if user:
            user.is_banned = False
            user.save()
            response = {"success": True}
        else:
            response = {"success": False, "error": "User not found"}

        return HttpResponse(str(response))
    else:
        return render(request, "admin/manage/home.html")


def make_admin(request):
    if request.method == "POST":
        user_id = int(request.POST["userId"])
        user = CustomUser.objects.get(telegram_id=user_id)

        if user:
            user.is_staff = True
            user.save()
            response = {"success": True}
        else:
            response = {"success": False, "error": "User not found"}

        return HttpResponse(str(response))
    else:
        return render(request, "admin/manage/home.html")


def message(request):
    if request.method == "POST":

        try:
            if request.FILES:
                file = request.FILES["photo"]
                fs = FileSystemStorage()
                filename = fs.save(file, file)
                file_url = fs.url(filename)
                file = InputFile(f"./{file_url}")
                send_photo(request.POST["userId"], request.POST["text"], file)
                os.remove(file_url)

            else:
                send_message(request.POST["userId"], request.POST["text"])
        except Exception as e:
            print(e)

        return HttpResponse(str({"success": True}))
    else:
        return render(request, "admin/manage/home.html")


def restart(request):
    if request.POST:
        restart_bot()
        return HttpResponse(str({"success": True}))
    else:
        return render(request, "admin/manage/home.html")


def shutdown(request):
    if request.POST:
        shutdown_bot()
        return HttpResponse(str({"success": True}))
    else:
        return render(request, "admin/manage/home.html")


def startup(request):
    if request.POST:
        startup_bot()
        return HttpResponse(str({"success": True}))
    else:
        return render(request, "admin/manage/home.html")


def log(request):
    log = open("./logs/logging.txt", "r", encoding="utf-8")
    data = log.read()
    log.close()
    return render(request, "admin/log/home.html", {"log": data})
