from django.conf.urls import url
from shop import views
#Entradas para las url.
urlpatterns = [
        url(r'^$',	views.product_list, name='product_list'), #Entrada para la pagina base, listado de los productos
        url(r'^(?P<catSlug>[-\w]+)/$',  views.product_list, name='product_list_by_category'), #Entrada para la pagina con los productos filtrados por una categoria
        url(r'^(?P<id>\d+)/(?P<prodSlug>[-\w]+)/$',	views.detailProduct, name=' product_detail') #Entrada para la pagina con los detalles de un producto
        ]