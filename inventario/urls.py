from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.inventario, name="inventario"),
    url(r'^articulo/(?P<codigo_articulo>[0-9]+)/$',
        views.articulo, name="articulo")
)
