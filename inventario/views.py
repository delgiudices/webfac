from django.shortcuts import render
from .forms import ArticuloForm
from .models import Articulo
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.


def support_data_table(Form):

    def decorator(view_func):

        def wrap(request, *args, **kwargs):
            accion = request.POST.get('accion', None)
            if accion == "new_%s" % Form._meta.model.name:
                form = Form(request.POST)
                if form.is_valid():
                    form.save(sistema=request.user.sistema)
                    messages.success(request, _("El objeto fue creado"))
                    return HttpResponseRedirect(request.path)
                else:
                    raise Exception(form.errors)
            elif accion == "delete_%s" % Form._meta.model.name:
                articulo = Form._meta.model.objects.get(
                    pk=request.POST['articulo_pk'])
                articulo.delete()
                return HttpResponseRedirect(request.path)
            else:
                return view_func(request, *args, **kwargs)

            return view_func(request, *args, **kwargs)

        return wrap

    return decorator


@login_required()
@permission_required("inventario.change_articulo", raise_exception=True)
@support_data_table(ArticuloForm)
def inventario(request):

    context = {
        'form': ArticuloForm(),
        'articulos': Articulo.objects.all(sistema=request.user.sistema)
    }

    return render(request, 'sentir/inventario/inventario.html', context)
