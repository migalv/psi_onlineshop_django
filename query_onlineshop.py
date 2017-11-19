#!/usr/local/bin/python
# coding: latin-1
import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','onlineshop.settings')

import django
django.setup()
from shop.models import Category, Product
from django.core.files import File

def populate():
	
	catName1 = "ofertas"
	catName2 = "gangas"
	prodName1 = "oferta 1"
	prodName2 = "oferta 2"
	prodName3 = "oferta 3"
	prodName4 = "ganga 1"
	prodName5 = "ganga 2"
	prodName6 = "ganga 3"
	
	
	# Si no existen las categorias ofertas o gangas, se crean y se les añaden 3 productos nuevos
	
	if not Category.objects.filter(catName=catName1).exists():
		c1 = Category.objects.create(catName=catName1)
		Product.objects.create(category = c1, prodName = prodName1, image = "DragonBall_01.jpg", description = "desc1" , price = "10.00", stock = "1", availability = "True")
		Product.objects.create(category = c1, prodName = prodName2, image = "EnciclopediaMarioBros.jpg", description = "desc2" , price = "11.00", stock = "2", availability = "False")
		Product.objects.create(category = c1, prodName = prodName3, image = "planeta_hulk.jpg", description = "desc3" , price = "12.00", stock = "3", availability = "True")
	if not Category.objects.filter(catName=catName2).exists():
		c2 = Category.objects.create(catName=catName2)
		Product.objects.create(category = c2, prodName = prodName4, image = "ciclismo_rendimiento.jpg", description = "desc4" , price = "14.00", stock = "4", availability = "True")
		Product.objects.create(category = c2, prodName = prodName5, image = "reiki.jpg", description = "desc5" , price = "15.00", stock = "5", availability = "True")
		Product.objects.create(category = c2, prodName = prodName6, image = "runners.jpg", description = "desc6" , price = "16.00", stock = "6", availability = "False")
	
	# Se obtiene la categoria gangas, y despues todos los productos asociados a ella
	
	c3 = Category.objects.get(catName = catName2)
	query = Product.objects.filter(category = c3)
	print query
	
	
	# Se busca el producto con prodSlug = "oferta-1", para saber a que categoria pertenece.
	#Si dicho producto no existe se informa de ello por pantalla.
	
	key = "oferta-1"
	try:
		query = Product.objects.get(prodSlug = key)
		c = getattr(query, "category")
		cSlug = getattr(c, "catSlug")
		print "CatSlug:" + cSlug
	except Product.DoesNotExist:
		print "producto'" + key + "'inexistente"
	

	# Se busca el producto con prodSlug = "oferta-10", para saber a que categoria pertenece.
	#Si dicho producto no existe se informa de ello por pantalla.
	
	key = "oferta_10"
	try:
		query = Product.objects.get(prodSlug = key)
		c = getattr(query, "category")
		cSlug = getattr(c, "catSlug")
		print "CatSlug:" + cSlug
	except Product.DoesNotExist:
		print "producto'" + key + "'inexistente"


if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()
