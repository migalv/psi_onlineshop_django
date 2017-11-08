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
	
	#Your code goes here
	#queries that fill, category, categories and products
	return render(request,'shop/list.html',
				{'category': category,
				'categories': categories,
				'products': products})
