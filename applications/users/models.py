from django.db import models

from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
