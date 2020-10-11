from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreatePedidoApiView.as_view()),
]