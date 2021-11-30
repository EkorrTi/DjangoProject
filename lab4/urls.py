from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('article.urls')),
    path('admin/', admin.site.urls)
]