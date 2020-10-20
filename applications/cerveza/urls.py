from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CervezaCreateApiView.as_view()),
    path('', views.CervezaListApiView.as_view()),
    path('detail/<int:pk>/', views.CervezaDetailApiView.as_view()),
    path('by_maker/', views.CervezaListApiViewByMaker.as_view()),
]