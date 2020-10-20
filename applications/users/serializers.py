from rest_framework import serializers

from django.contrib.auth import authenticate
from rest_framework.response import Response

from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
        'username',
        'email',
        'nombres',
        'apellidos',
        'genero',
        'rol',
        'password',
    )
    def create(self, validated_data):
        fields = UserSerializer.Meta.fields
        extra_fields = {f: validated_data.get(f) for f in fields}
        return User.objects.create_user(**extra_fields)


class TokenSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=128)

    def validate(self, attrs):
        credentials = {'username': attrs.get('username'), 'password': attrs.get('password')}
        user = authenticate(**credentials)
        if user is None:
            raise serializers.ValidationError({"error": "usuario no encontrado"})
        return {'user': user}