import re

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.utils import timezone


class UsernameValidator(validators.RegexValidator):
    regex = r'^[\w]+\Z'
    message = 'Введите правильное имя пользователя. Оно может содержать только лат. символы и цифры'
    flags = re.ASCII


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UsernameValidator()

    username = models.CharField(
        verbose_name="Имя пользователя",
        max_length=50,
        unique=True,
        validators=[username_validator],
    )
    email = models.EmailField(
        verbose_name='Почта',
        blank=True
    )
    is_staff = models.BooleanField(
        verbose_name='Администратор',
        default=False,
    )
    date_joined = models.DateTimeField(
        verbose_name='Дата регистрации',
        default=timezone.now,
    )
    telegram_id = models.IntegerField(
        verbose_name='Телеграмм',
        default=0,
    )
    is_banned = models.BooleanField(
        verbose_name='Заблокирован',
        default=False,
    )
    is_ad_blocked = models.BooleanField(
        verbose_name='Блокировка Рекламы',
        default=False,
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    font_size = models.IntegerField()

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:50]

    class Meta:
        verbose_name = 'Сниппет'
        verbose_name_plural = 'Сниппеты'
