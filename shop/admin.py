# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
from shop.models import Category, Product

#Registro de todos los modelos a implementar para el admin (categoria, producto).
#Se guarda en "prepopulated_fields" los campos que se generan de forma automatica.
#Autor: Felix Coto
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'catSlug':('catName',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'prodSlug':('prodName',)}
	list_display = ('prodName', 'prodSlug', 'price', 'stock', 'availability', 'created', 'updated')

admin.site.register(Product, ProductAdmin)