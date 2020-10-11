from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)

from .models import CervezaModel
from .serializers import CervezaSerializer
# Create your views here.


class CervezaListApiView(ListAPIView):

    serializer_class = CervezaSerializer

    def get_queryset(self):
        return CervezaModel.objects.all()


class CervezaDetailApiView(ListAPIView):

    serializer_class = CervezaSerializer

    def get_queryset(self):
        nombre = self.kwargs.get('nombre')
        return CervezaModel.objects.filter(
            nombre__iexact=nombre
        )


class CervezaCreateApiView(CreateAPIView):

    serializer_class = CervezaSerializer