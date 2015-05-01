from django.db import models
from sistema.models import SistemaModel
from .exceptions import CantidadError


class Articulo(SistemaModel):

    nombre = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)

    def entrada(self, amount):
        Ajuste.objects.create(articulo=self, cantidad=amount)
        self.cantidad += amount
        self.save()

    def salida(self, amount):

        if self.cantidad - amount < 0:
            raise CantidadError

        Ajuste.objects.create(articulo=self, cantidad=-amount)
        self.cantidad -= amount
        self.save()

    def _cantidad(self):
        return self.ajuste_set.all()\
            .aggregate(models.Sum('cantidad'))['cantidad__sum']


class Ajuste(models.Model):

    articulo = models.ForeignKey(Articulo)
    cantidad = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
