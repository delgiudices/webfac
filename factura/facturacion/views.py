from django.shortcuts import render

# Create your views here.


def facturacion(request):
    context = {}
    return render(request, 'sentir/facturacion/facturacion.html', context)
