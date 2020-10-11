from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CervezaCreateApiView.as_view()),
    path('', views.CervezaListApiView.as_view()),
    path('detail/<nombre>/', views.CervezaDetailApiView.as_view()),
]