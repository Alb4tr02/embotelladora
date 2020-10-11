from django.db import models

from applications.users.models import User
from applications.cerveza.models import CervezaModel
from .managers import PedidoManager
# Create your models here.
class PedidosModel(models.Model):
    
    STATUS_CHOICES = (
        ('P', 'Pendiente'),
        ('C', 'En curso'),
        ('F', 'Finalizado'),
    )
    cliente = models.ForeignKey(User, related_name='pedidos_cliente', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    cerveza = models.ForeignKey(CervezaModel, related_name='pedidos', on_delete=models.CASCADE)
    costo_total = models.IntegerField()
    cantidad_botellas = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True)
    fabricante = models.ForeignKey(User, related_name='pedidos_fabricante', on_delete=models.CASCADE, null=True)

    objects = PedidoManager()