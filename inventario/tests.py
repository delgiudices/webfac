from django.test import TestCase
from sistema.models import Sistema
from .models import Articulo
from .exceptions import CantidadError


class ArticuloTestCase(TestCase):

    def setUp(self):
        sistema = Sistema.objects.create(name="Test")
        Articulo.objects.create(
            sistema=sistema,
            nombre="Computadora",
            costo=100, precio=125)

    def test_entrada(self):
        articulo = Articulo.objects.get(nombre="Computadora")
        cantidad_actual = articulo.cantidad
        articulo.entrada(50)
        self.assertEqual(articulo.cantidad, cantidad_actual + 50)

    def test_salida(self):
        articulo = Articulo.objects.get(nombre="Computadora")
        cantidad_actual = articulo.cantidad
        with self.assertRaises(CantidadError):
            articulo.salida(50)

        articulo.entrada(25)
        self.assertEqual(articulo.cantidad, cantidad_actual + 25)
        cantidad_actual = articulo.cantidad

        articulo.salida(10)
        self.assertEqual(articulo.cantidad, cantidad_actual - 10)

    def test_calcular(self):
        articulo = Articulo.objects.get(nombre="Computadora")
        articulo.entrada(25)
        self.assertEqual(articulo._cantidad(), 25)
