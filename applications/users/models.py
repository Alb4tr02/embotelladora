from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    ROL_CHOICES = (
        ('F', 'Fabricante'),
        ('C', 'Cliente'),
    )
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices=GENDER_CHOICES)
    rol = models.CharField(max_length=1, choices=ROL_CHOICES)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.nombres + ' - ' + self.apellidos
