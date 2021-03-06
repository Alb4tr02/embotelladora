from rest_framework import serializers

from .models import CervezaModel

class CervezaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CervezaModel
        fields = (
            'precio',
            'color',
            'alcohol',
            'fermentacion',
            'nombre',
            'id')

    def create(self, validated_data):
        fields = CervezaSerializer.Meta.fields
        fabricante = self.context.get('request').user
        extra_fields = {f: validated_data.get(f) for f in fields}
        extra_fields['fabricante'] = fabricante
        return CervezaModel.objects.create(**extra_fields)
