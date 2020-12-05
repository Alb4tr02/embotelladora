from django.shortcuts import render

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer, TokenSerializer
from .models import User
# Create your views here.


class UserCreateView(CreateAPIView):

    permission_classes = ()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'email': response.data.get('email'),
            'username': response.data.get('username')
        })


class CustomAuthToken(ObtainAuthToken):

    permission_classes = ()
    serializer_class = TokenSerializer
    print("llega")
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
