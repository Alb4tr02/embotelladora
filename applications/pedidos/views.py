from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from .serializers import PedidoCreateSerializer

# Create your views here.
class CreatePedidoApiView(CreateAPIView):

    serializer_class = PedidoCreateSerializer