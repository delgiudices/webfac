from django.test import TestCase, RequestFactory
from sistema.models import Sistema
from .models import Articulo
from .exceptions import CantidadError
from django.contrib.auth import get_user_model
from inventario.views import inventario
from django.contrib.messages.storage.fallback import FallbackStorage


class InventarioPageTestCase(TestCase):

    def setUp(self):
        self.sistema = Sistema.objects.create(name="Test")
        self.user = get_user_model().objects.create_superuser(
            username="test", email="someemail@domain.com",
            password="test", sistema=self.sistema)
        self.factory = RequestFactory()

    def test_inventario_page_exists(self):
        request = self.factory.get('/inventario')
        request.user = self.user
        response = inventario(request)
        self.assertEqual(response.status_code, 200)

    def test_create_articulo(self):
        request = self.factory.post('/inventario', {
            'accion': 'new_articulo', 'nombre': 'Computadora',
            'costo': '150.0', 'precio': '123', })
        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)
        request.user = self.user
        inventario(request)
        self.assertTrue(len(Articulo.objects.filter(
            sistema=self.sistema, nombre='Computadora')) > 0)

    def test_delete_articulo(self):
        a = Articulo.objects.create(
            nombre="Computadora", costo=0, precio=0, sistema=self.sistema)

        request = self.factory.post('/inventario', {
            'accion': 'delete_articulo', 'articulo_pk': '%s' % a.pk})
        request.user = self.user

        setattr(request, 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request, '_messages', messages)

        response = inventario(request)

        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Articulo.DoesNotExist):
            Articulo.objects.get(pk=a.pk)


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

        self.assertTrue(len(articulo.ajuste_set.all()) > 0)

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

        self.assertTrue(len(articulo.ajuste_set.all()) > 0)

    def test_calcular(self):
        articulo = Articulo.objects.get(nombre="Computadora")
        articulo.entrada(25)
        self.assertEqual(articulo._cantidad(), 25)


class AjusteTestCase(TestCase):

    def setUp(self):
        sistema = Sistema.objects.create(name="Test")
        articulo = Articulo(
            sistema=sistema,
            nombre="Computadora",
            costo=100, precio=125, cantidad=10)
        articulo.save()

    def test_create(self):
        articulo = Articulo.objects.get(nombre="Computadora")
        self.assertTrue(len(articulo.ajuste_set.all()) > 0)
