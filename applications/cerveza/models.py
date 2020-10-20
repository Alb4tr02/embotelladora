from django.db import models

from applications.users.models import User

# Create your models here.
class CervezaModel(models.Model):

    COLOR_CHOICES = (
        ('M', 'Rubia'),
        ('N', 'Negra'),
        ('A', 'Ambar'),
        ('R', 'Roja'),
    )
    FERMENTACION_CHOICES = (
        ('A', 'Ale'),
        ('L', 'Larger'),
        ('H', 'Hibrida'),
    )
    precio = models.IntegerField()
    color = models.CharField(max_length=1, choices=COLOR_CHOICES)
    alcohol = models.FloatField()
    fermentacion = models.CharField(max_length=1, choices=FERMENTACION_CHOICES)
    nombre = models.CharField(max_length=20, unique=True)
    fabricante = models.ForeignKey(User, related_name='cervezas', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.nombre

    def get_full_description(self):
        return f'nombre {self.nombre}, precio {self.precio}, color {self.color}, alcohol {self.alcohol}, fermentacion {self.fermentacion}'