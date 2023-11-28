from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('courses/',courses),
    path('about/',about),
    path('',first_app_home)
]