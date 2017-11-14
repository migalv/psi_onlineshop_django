# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from shop.models import Category, Product

def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	# Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage': "I am bold font from the context"}

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.

	return render(request, 'shop/index.html', context_dict)

def base(request):
	return render(request, 'shop/base.html')

def product_list(request, catSlug=None):

	if catSlug == None:
		categories = Category.objects.all()
		products = Product.objects.all()
		category = None
	else:
		try:
			category = Category.objects.filter(catSlug=catSlug)
			products = Product.objects.get(category=category)
		except Category.DoesNotExists:
			categories = Category.objects.all()
			products = Product.objects.all()
			category = None
			
	return render(request,'shop/list.html',
					{'category': category,
					'categories': categories,
					'products': products})

def detailProduct(request, prodId, prodSlug):
	
	product = {'category': category.catName, }

	#Your code goes here
	#query that returns a product with id=protId	
	return render(request, 'shop/detail.html', {'product': product})