from django.db import models
from authentication.models import Sistema

# Create your models here.

class Articulo(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    sistema = models.ForeignKey(Sistema)
