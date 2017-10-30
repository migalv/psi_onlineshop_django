import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','onlineshop.settings')

import django
django.setup()
from shop.models import Category, Product
from django.core.files import File

imageObject = File(open(os.path.join(directory_with_images, image_name),’r’))

p = Product.objects.get_or_create(category = ...,prodName = ...,...)[0]
p.image.save(image_name, imageObject, save = True)

def populate():
	# First, we will create lists of dictionaries containing the pages
	# we want to add into each category.
	# Then we will create a dictionary of dictionaries for our categories.
	# This might seem a little bit confusing, but it allows us to iterate
	# through each data structure, and add the data to our models.
 
	comic_books = [
	     {"prodName": "Dragon Ball Super - Numero 01 (Manga Shonen)",
	      "image_name":"DragonBall_01.jpg",
	      "descrip":"No",
	      "price":7.55,
	      "stock":10,
	      "availability":True,},	
	     {"prodName": "Enciclopedia Super Mario Bros",
	      "image_name":"EnciclopediaMarioBros.jpg",
	      "descrip":"No",
	      "price":28,50,
	      "stock":35,
	      "availability":True,},
	     {"prodName": "Pokémon 17. Diamante y Perla 1",
	      "image_name":"Pokemon17.jpg",
	      "descrip":"No",
	      "price":11,40,
	      "stock":12,
	      "availability":True,} ]
	 
	sport_books = [
	     {"prodName": "JUEGO INTERIOR DEL TENIS",
	      "image_name":"ElJuegoInterior.jpg",
	      "descrip":"No",
	      "price":6,64,
	      "stock":85,
	      "availability":True,},
	     {"prodName": "Hasta siempre, Vicente Calderón",
	      "image_name":"calderon.jpg",
	      "descrip":"No",
	      "price":20,80,
	      "stock":73,
	      "availability":False,},
	      {"prodName": "JUEGO INTERIOR DEL TENIS",
	      "image_name":"ElJuegoInterior.jpg",
	      "descrip":"No",
	      "price":6,64,
	      "stock":85,
	      "availability":True,} ]
	 
	other_pages = [
	     {"title":"Bottle",
	      "url":"http://bottlepy.org/docs/dev/",
	      "views":10},
	     {"title":"Flask",
	      "url":"http://flask.pocoo.org",
	      "views":60} ]
	 
	cats = {"Comics": {"books": comic_books},
	        "Comics": {"books": comic_books},
	        "Comics": {"books": comic_books} }
 
 # If you want to add more catergories or pages,
 # add them to the dictionaries above.
 
 # The code below goes through the cats dictionary, then adds each category,
 # and then adds all the associated pages for that category.
 # if you are using Python 2.x then use cats.iteritems() see
 # http://docs.quantifiedcode.com/python-anti-patterns/readability/
 # for more information about how to iterate over a dictionary properly.
 
	for cat, cat_data in cats.iteritems():
	    c = add_cat(cat, cat_data["views"], cat_data["likes"])
	    for p in cat_data["pages"]:
	        add_page(c, p["title"], p["url"], p["views"])
	 
	 # Print out the categories we have added.
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p

def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name=name)[0]
	c.views=views
	c.likes=likes
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
	print("Starting Rango population script...")
	populate()