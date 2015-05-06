from django.test import TestCase
from sistema.models import Sistema, SistemaModel

# Create your tests here.


class SistemaModelTestCase(TestCase):

    """
    def setUp(self):
        self.sistema = Sistema.objects.create(name="Kalia")
        self.sistema_2 = Sistema.objects.create(name="NeosCloud")
        SistemaModel.for_sistema.create(sistema=self.sistema)
        SistemaModel.for_sistema.create(sistema=self.sistema)

    def test_get_next_codigo(self):
        sistema = Sistema.objects.get(name="Kalia")
        self.assertEqual(
            SistemaModel.for_sistema.get_next_codigo(self.sistema),
            SistemaModel.for_sistema.all(sistema)[1].codigo + 1)

    def test_create(self):
        sistema = Sistema.objects.get(name="Kalia")
        models = SistemaModel.for_sistema.all(sistema)
        self.assertEqual(
            models[0].codigo + 1,
            models[1].codigo)
    """
