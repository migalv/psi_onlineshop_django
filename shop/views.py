# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
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

	if catSlug is None:
		products = Product.objects.all()
		category = None
	else:
		try:
			category = Category.objects.get(catSlug=catSlug)
			products = Product.objects.filter(category=category)
		except Category.DoesNotExists:
			products = None
			category = None
	
	categories = Category.objects.all()

	return render(request,'shop/list.html',
					{'category': category,
					'categories': categories,
					'products': products,
					'media_url': settings.MEDIA_URL})

def detailProduct(request, id, prodSlug):
	
	try:
		product = Product.objects.get(id=id, prodSlug=prodSlug)
	except Product.DoesNotExists:
		product = None

	return render(request, 'shop/detail.html', {'product': product,
												'media_url': settings.MEDIA_URL})