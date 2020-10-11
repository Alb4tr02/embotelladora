from django.db import models

class PedidoManager(models.Manager):

    def create_pedido(self, **data):

        pedido = self.model(
            **data
        )
        pedido.status = "P"
        pedido.costo_total = pedido.cantidad_botellas * pedido.cerveza.precio
        pedido.save(using=self.db)
        return pedido