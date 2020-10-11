from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.UserCreateView.as_view()),
    path('login/', views.CustomAuthToken.as_view()),
]
