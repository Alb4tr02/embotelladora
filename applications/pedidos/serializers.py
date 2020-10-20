from rest_framework import serializers

from .models import PedidosModel


class PedidoCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PedidosModel
        fields = (
            'cerveza',
            'cantidad_botellas',
        )

    def create(self, validated_data):
        fields = PedidoCreateSerializer.Meta.fields
        data = {f: validated_data.get(f) for f in fields}
        data['cliente'] = self.context.get('request').user
        data['fabricante'] = validated_data.get('cerveza').fabricante
        return PedidosModel.objects.create_pedido(**data)
