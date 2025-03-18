# from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('weather.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 97eba7c5cb0505fde7e9c2d02e5f09b2
