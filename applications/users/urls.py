from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('tony/', views.UserCreateView.as_view()),
]
