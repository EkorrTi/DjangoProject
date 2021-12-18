from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from . import views
from account import views as AccViews

urlpatterns =[
    path('register', AccViews.register, name='register'),
    path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('logout/', AccViews.logout_, name='logout'),
    path('login/', AccViews.login_, name='login'),
    path('account/', AccViews.account_view, name='account'),
    path('post/', views.post_form, name='post'),
    path('<id>/delete', views.post_delete_form, name='post_delete')
]