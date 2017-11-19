# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils import timezone
from django.template.defaultfilters import slugify

#Modelo para las categorias.
class Category(models.Model):
	#campos del modelo a definir
	catName = models.CharField(max_length=128, unique=True, null=False)
	catSlug = models.SlugField(null=False,unique=True)

	def save(self, *args, **kwargs):
		self.catSlug = slugify(self.catName) #para generar el campo dado de forma automatica
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):  # For Python 2, use __unicode__ too
		return self.catName

	def __unicode__(self):
		return self.catName

		
#Modelo para los productos.
class Product(models.Model):
	#campos del modelo a definir
	category = models.ForeignKey(Category, null = False)
	prodName = models.CharField( unique=True, null=False,max_length=128)
	prodSlug = models.SlugField(null=False,unique=True)
	image = models.ImageField(upload_to='products/', null = False)
	description = models.CharField(null=False,max_length=1500)
	price = models.DecimalField(null=False,decimal_places=2, max_digits=10)
	stock = models.IntegerField(null = False, default = 1)
	availability = models.BooleanField(null = False, default= True)
	created = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		self.prodSlug = slugify(self.prodName) #para generar el campo dado de forma automatica
		super(Product, self).save(*args, **kwargs)

	def __str__(self):  # For Python 2, use __unicode__ too
		return self.prodName

	def __unicode__(self):
		return self.prodName
