from django.contrib import admin
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.html import format_html
from core.views import admin_stats

from .models import CustomUser, Snippet

admin.site.site_header = "Admin Dashboard"
admin.site.unregister(Group)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'telegram_id', 'is_staff', 'is_banned', 'is_ad_blocked')
    list_filter = ('is_staff', 'date_joined', 'is_banned', 'is_ad_blocked')

    fieldsets = (
        ('Информация',
         {
             'fields': ('username', 'email', 'date_joined', 'telegram_id')
         }),
        ('Выбор',
         {
             'fields': ('is_staff', 'is_banned', 'is_ad_blocked')
         }),
    )

    search_fields = ('username', )

    #change_list_template = 'admin/core/core_change_list.html'


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'font_size_html_display')
    list_filter = ('created', )
    #change_list_template = 'admin/snippets/snippets_change_list.html'

    readonly_fields = ('body_preview', )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>/', self.change_font_size)
        ]
        return custom_urls + urls

    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'font size sets succesfully')
        return HttpResponseRedirect("../")

    def font_size_html_display(self, obj):
        display_size = obj.font_size if obj.font_size <= 30 else 30
        return format_html(
            f'<span style="font-size: {display_size}px;">{obj.font_size}</span>'
        )
