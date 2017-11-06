#!/usr/local/bin/python
# coding: latin-1
import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','onlineshop.settings')

import django
django.setup()
from shop.models import Category, Product
from django.core.files import File

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
	      "price":28.50,
	      "stock":35,
	      "availability":True,},
	     {"prodName": "Pokémon 17. Diamante y Perla 1",
	      "image_name":"Pokemon17.jpg",
	      "descrip":"No",
	      "price":11.40,
	      "stock":12,
	      "availability":True,} ]
	 
	sport_books = [
	     {"prodName": "JUEGO INTERIOR DEL TENIS",
	      "image_name":"ElJuegoInterior.jpg",
	      "descrip":"No",
	      "price":6.64,
	      "stock":85,
	      "availability":True,},
	     {"prodName": "Hasta siempre, Vicente Calderón",
	      "image_name":"calderon.jpg",
	      "descrip":"No",
	      "price":20.80,
	      "stock":73,
	      "availability":False,},
	      {"prodName": "Runners superacion deportiva ",
	      "image_name":"runners.jpg",
	      "descrip":"El running no es una disciplina que involucre solamente las pistas o competencias, son muchos los aspectos que se deben considerar para ser verdaderamente exitosos en este deporte. A continuación desarrollaremos diferentes tópicos que buscan brindarte las herramientas para que seas exitoso en el desempeño deportivo",
	      "price":2.99,
	      "stock":65,
	      "availability":True,} ]
	 
	history_books = [
	     {"prodName": "Los pacientes del doctor García",
	      "image_name":"ElJuegoInterior.jpg",
	      "descrip":"No",
	      "price":6.64,
	      "stock":85,
	      "availability":True,},
	     {"prodName": "LAS DROGAS EN LA GUERRA",
	      "image_name":"lasdrogas.jpg",
	      "descrip":"Łukasz Kamieński nos ofrece una nueva visión del papel que han desempeñado las drogas en la guerra, desde los héroes homéricos que consumían opio hasta, en la actualidad, los cientos de miles de niños soldados que combaten drogados. En esta historia aprendemos cómo los ingleses forjaron un imperio basado en el ron, cómo las tropas de Napoleón descubrieron el hachís en Egipto o cómo las drogas explican las peores aberraciones de la guerra de Vietnam. Pero, al margen de este escenario de guerras, Kameński nos muestra que muchos de estos productos, prohibidos tan solo hace unos años, han formado parte por mucho tiempo de nuestra vida cotidiana, como la cocaína o como la heroína, lanzada al mercado en 1898, junto a la aspirina, como un sedante para la tos. Este libro, que Foreign Affairs",
	      "price":12.34,
	      "stock":64,
	      "availability":True,},
	      {"prodName": "Victorias frustradas (Ensayo y divulgación)",
	      "image_name":"victorias.jpg",
	      "descrip":"No",
	      "price":4532.98,
	      "stock":1,
	      "availability":True,} ]

	 
	cats = {"Comics": {"books": comic_books},
	        "Sport": {"books": sport_books}, 
	        "History": {"books": history_books } }
 
 # If you want to add more catergories or pages,
 # add them to the dictionaries above.
 
 # The code below goes through the cats dictionary, then adds each category,
 # and then adds all the associated pages for that category.
 # if you are using Python 2.x then use cats.iteritems() see
 # http://docs.quantifiedcode.com/python-anti-patterns/readability/
 # for more information about how to iterate over a dictionary properly.
 
	for cat, cat_data in cats.iteritems():
	    c = add_cat(cat)
	    for p in cat_data["books"]:
	        add_product(c, p["prodName"], p["image_name"], p["descrip"], p["price"], p["stock"], p["availability"])
	 
	# Print out the categories we have added.
	#for c in Category.objects.all():
	#	for p in Product.objects.filter(category=c):
	#		print("- {0} - {1}".format(str(c), str(p)))

def add_product(cat, prodName, image_name, description, price, stock, availability):
	p = Product.objects.get_or_create(category=cat, prodName=prodName, description = description , price=price, stock = stock, availability = availability)[0]
	imageObject = File(open(os.path.join('images', image_name),'r'))

	p.image.save(image_name, imageObject, save = True)
	p.save()
	return p

def add_cat(name):
	c = Category.objects.get_or_create(catName=name)[0]
	c.save()
	return c

# Start execution here!
if __name__ == '__main__':
	print("Starting Shop population script...")
	populate()