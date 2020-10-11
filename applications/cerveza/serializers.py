from rest_framework import serializers

from .models import CervezaModel

class CervezaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CervezaModel
        fields = ('__all__')