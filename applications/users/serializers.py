from rest_framework import serializers

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
