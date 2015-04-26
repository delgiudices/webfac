from django.shortcuts import render
from authentication.models import Sistema
from facturacion.models import Articulo

# Create your views here.
def facturacion(request):
    context = {}
    sistema = Sistema.objects.get(nombre="Dettagli")
    context["articulos"] = Articulo.objects.filter(sistema=sistema)
    return render(request, 'sentir/facturacion/facturacion.html', context)
