# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
	catName = models.CharField(max_length=128, unique=True, null=False)
	catSlug = models.SlugField(null=False,unique=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):  # For Python 2, use __unicode__ too
		return self.name

	def __unicode__(self):
		return self.name

class Product(models.Model):
	category = models.ForeignKey(Category, null = False)
	proName = models.CharField( unique=True, null=False,max_length=128)
	proSlug = models.SlugField(null=False,unique=True)
	image = models.ImageField(upload_to='images/products', null = False)
	description = models.CharField(null=False,max_length=128)
	price = models.FloatField(null=False)
	stock = models.IntegerField(null = False, default = 1)
	availability = models.BooleanField(null = False, default= True)
	created = models.DateTimeField(default=datetime.now())
	updated = models.DateTimeField(default=datetime.now())

	def __str__(self):  # For Python 2, use __unicode__ too
		return self.title

	def __unicode__(self):
		return self.title
