from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
)

from .models import CervezaModel
from .serializers import CervezaSerializer
# Create your views here.


class CervezaListApiView(ListAPIView):

    serializer_class = CervezaSerializer

    def get_queryset(self):
        return CervezaModel.objects.all()


class CervezaListApiViewByMaker(ListAPIView):

    serializer_class = CervezaSerializer

    def get_queryset(self):
        return self.request.user.cervezas


class CervezaDetailApiView(RetrieveAPIView):

    queryset = CervezaModel.objects.all()
    serializer_class = CervezaSerializer


class CervezaCreateApiView(CreateAPIView):

    serializer_class = CervezaSerializer