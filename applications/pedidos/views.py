from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from .serializers import PedidoCreateSerializer
import requests

# Create your views here.
class CreatePedidoApiView(CreateAPIView):

    serializer_class = PedidoCreateSerializer

    def post(self, request, *args, **kwargs):

        botellas = request.data.get('cantidad_botellas')
        response = requests.post('http://192.168.1.11/crear_pedido/' + str(botellas))
        print(response)
        return self.create(request, *args, **kwargs)