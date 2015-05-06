from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator


def data_table_decorator(Form):
    """
    Decorator that will automatically add suport for creation and deletion of
    user models. It sends the view the queryset for the data.
    """

    def decorator(view_func):

        def wrap(request, *args, **kwargs):
            accion = request.POST.get('accion', None)

            if accion == "new_%s" % Form._meta.model.name:
                # Create new instance of the model
                form = Form(request.POST)
                if form.is_valid():
                    form.save(sistema=request.user.sistema)
                    messages.success(request, _("El objeto fue creado"))
                    return HttpResponseRedirect(request.path)
                else:
                    kwargs['form'] = form

            elif accion == "delete_%s" % Form._meta.model.name:
                # Delete the instance
                Form._meta.model.objects.get(
                    pk=request.POST['articulo_pk']).delete()

                # Redirect to prevent reloading form
                return HttpResponseRedirect(request.path)

            else:
                # Load the data and pass it as kwarg to function.
                p = Paginator(Form._meta.model.objects.all(
                    sistema=request.user.sistema), 1)
                page_index = int(request.GET.get('page', 1))
                kwargs['page'] = p.page(page_index) if page_index in \
                    p.page_range else p.page(1)

                kwargs['form'] = Form()

            return view_func(request, *args, **kwargs)

        return wrap

    return decorator
