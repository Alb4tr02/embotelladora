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
                  )

    def create(self, validated_data):
        fields = CervezaSerializer.Meta.fields
        fabricante = self.context.get('request').user
        print(fabricante)
        extra_fields = {f: validated_data.get(f) for f in fields}
        extra_fields['fabricante'] = fabricante
        return CervezaModel.objects.create(**extra_fields)
