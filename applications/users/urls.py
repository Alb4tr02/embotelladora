from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view()),
    path('login/', views.CustomAuthToken.as_view()),
]
