from django.db import models
from sistema.models import SistemaModel


class Articulo(SistemaModel):

    nombre = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
