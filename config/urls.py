from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings # Правильный импорт settings подтянет все настройки


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('prostoapp.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


