from django.shortcuts import render
from .forms import ArticuloForm
from .models import Articulo
from django.contrib.auth.decorators import permission_required, login_required
from sistema.datatable import data_table_decorator
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
