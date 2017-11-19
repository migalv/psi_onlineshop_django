from django.conf.urls import url
from shop import views
#Entradas para las url.
urlpatterns = [
        url(r'^$',	views.product_list, name='product_list'), #Pagina base, listado de los productos
        url(r'^(?P<catSlug>[-\w]+)/$',  views.product_list, name='product_list_by_category'), #Pagina con los productos filtrados por una categoria
        url(r'^(?P<id>\d+)/(?P<prodSlug>[-\w]+)/$',	views.detailProduct, name=' product_detail') #Pagina con los detalles de un producto
        ]