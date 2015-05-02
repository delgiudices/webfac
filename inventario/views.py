from django.shortcuts import render
from .forms import ArticuloForm
from .models import Articulo
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.


def inventario(request):
    accion = request.POST.get('accion', None)
    if accion == "new_articulo":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save(sistema=request.user.sistema)
            messages.success(request, _("El articulo fue creado"))
            return HttpResponseRedirect(reverse(inventario))
        else:
            raise Exception(form.errors)
    elif accion == "delete_articulo":
        articulo = Articulo.objects.get(pk=request.POST['articulo_pk'])
        articulo.delete()

    return render(request, 'sentir/inventario/inventario.html')
