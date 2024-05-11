from django.contrib import admin
from django.urls import path
from .views import user_login, user_register

urlpatterns = [
    path('', user_login, name='login'),
    path('registro', user_register, name='registro'),

]
