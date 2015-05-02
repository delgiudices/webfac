from django.db import models
from sistema.models import SistemaModel, DataTableModel
from .exceptions import CantidadError
from sistema.models import SistemaModelManager
from collections import OrderedDict


class ArticuloManager(SistemaModelManager):

    def create(self, **kwargs):
        """
        Si se crea un articulo con cantidad mayor que 0
        Se crea un objeto Ajuste con la cantidad dada.
        """
        articulo = super(ArticuloManager, self).create(**kwargs)
        if "cantidad" in kwargs and articulo.cantidad > 0:
            Ajuste.objects.create(
                cantidad=articulo.cantidad,
                articulo=articulo)
        return articulo


class Articulo(SistemaModel, DataTableModel):

    name = "articulo"

    nombre = models.CharField(max_length=50)
    costo = models.DecimalField(max_digits=6, decimal_places=2)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    objects = ArticuloManager()

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
        """
        Calcula la cantidad en base a los ajustes.
        """
        return self.ajuste_set.all()\
            .aggregate(models.Sum('cantidad'))['cantidad__sum']

    def get_fields(self):
        return OrderedDict([
            ('Codigo', self.codigo),
            ('Nombre', self.nombre),
            ('Costo', self.costo),
            ('Precio', self.precio),
            ('Cantidad', self.cantidad),
        ])


class Ajuste(models.Model):

    articulo = models.ForeignKey(Articulo)
    cantidad = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
