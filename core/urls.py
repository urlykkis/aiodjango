# -*- coding: utf-8 -*-
from django.urls import path

from core.views import admin_stats, manage

urlpatterns = [
    path("stats/", admin_stats),
    path("manage/", manage),
]
