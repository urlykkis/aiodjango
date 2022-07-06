from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('astats/', views.admin_stats),
    path('amanage/', views.manage),
    path('amanage/mailing', views.mailing),
    path('amanage/ban', views.ban),
    path('amanage/message', views.message),
    path('amanage/makeadmin', views.make_admin),
    path('amanage/unban', views.unban),
    path('amanage/shutdown', views.shutdown),
    path('amanage/restart', views.restart),
    path('amanage/startup', views.startup),
    path('alog/', views.log),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
