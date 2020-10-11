from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from .serializers import UserSerializer
from .models import User
# Create your views here.


class UserCreateView(CreateAPIView):

    serializer_class = UserSerializer
