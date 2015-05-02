from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'factura.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/$', auth_views.login),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^facturacion/', include('facturacion.urls')),
    url(r'^inventario/', include('inventario.urls')),
]
