from django.conf.urls import patterns, url
from facturacion import views

urlpatterns = patterns('',
    url(r'^$', views.facturacion),
)
