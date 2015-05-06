from django.shortcuts import render
from .forms import ArticuloForm
from .models import Articulo
from django.contrib.auth.decorators import permission_required, login_required
from sistema.datatable import data_table_decorator
from django.http import HttpResponseRedirect, Http404
# Create your views here.


@login_required()
@permission_required("inventario.change_articulo", raise_exception=True)
@data_table_decorator(ArticuloForm)
def inventario(request, page=None, form=None):

    context = {
        'form': form,
        'page': page,
        'class': Articulo,
    }

    return render(request, 'sentir/inventario/inventario.html', context)


@login_required
@permission_required("inventario.change_articulo", raise_exception=True)
def articulo(request, codigo_articulo):
    accion = request.POST.get('accion')

    # Get the articulo or raise Http404 if articulo is not found
    try:
        articulo = Articulo.objects.get(
            codigo=codigo_articulo, sistema=request.user.sistema)
    except Articulo.DoesNotExist:
        raise Http404

    if accion == 'entrada':
        articulo.entrada(int(request.POST.get('amount', 0)))
        return HttpResponseRedirect(request.path)
    elif accion == 'salida':
        articulo.salida(int(request.POST.get('amount', 0)))
        return HttpResponseRedirect(request.path)

    # When normal requests..
    context = {

    }
    return render(request, 'sentir/inventario/articulo.html', context)
