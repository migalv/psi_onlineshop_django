from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from shop import views

urlpatterns = [
	url(r'^$', views.product_list, name="index"), #entrada para la pagina base, con la lista de productos
	url(r'^shop/', include('shop.urls')), #entrada para las todas las url dirigidas a la aplicacion "shop"
    url(r'^base/', views.base, name="base"), #entrada para la pagina base.html
    url(r'^admin/', admin.site.urls), #entrada para entrar como admin
]

#para poder usar los ficheros de /static y /media
urlpatterns += static(settings.STATIC_URL,\
    document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,\
    document_root=settings.MEDIA_ROOT)