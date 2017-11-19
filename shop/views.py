# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from shop.models import Category, Product

#Funcion para la template base. Muestra la pagina "base.html".
#Autor: Miguel Alvarez.
def base(request):
	return render(request, 'shop/base.html')


#Funcion para mostrar el listado de productos totales o filtrados por una categoria.
#Autor: Miguel Alvarez.
def product_list(request, catSlug=None):

	#Si "catSlug = None", es decir, no se esta filtrando por ninguna categoria,
	#se pasan todos los productos a list.html para mostrarlos.
	
	if catSlug is None:
		products = Product.objects.all()
		category = None
		
	#En caso contrario, se pasan solo los productos que pertenecen a la categoria con el catSlug dado.
	else:
		try:
			category = Category.objects.get(catSlug=catSlug)
			products = Product.objects.filter(category=category)
		except Category.DoesNotExist:
			products = None
			category = None
	
	categories = Category.objects.all()

	return render(request,'shop/list.html',
					{'category': category,
					'categories': categories,
					'products': products,
					'media_url': settings.MEDIA_URL})


#Funcion para mostrar los detalles de un producto.
#Autor: Miguel Alvarez.					
def detailProduct(request, id, prodSlug):
	
	#Se pasa a detail.html el producto con el id y el prodSlug dados, para mostrar su informacion,
	#controlando la posibilidad de que no exista.
	
	try:
		product = Product.objects.get(id=id, prodSlug=prodSlug)
	except Product.DoesNotExists:
		product = None

	return render(request, 'shop/detail.html', {'product': product,
												'media_url': settings.MEDIA_URL})