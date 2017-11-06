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
	      {"prodName": "Planeta Hulk. Integral (Marvel Deluxe)",
	      "image_name":"planeta_hulk.jpg",
	      "descrip":"Greg Pak, Carlo Pagulayan, Aaron Lopresti, Gary Frank. . ¡La más espectacular aventura jamás protagonizada por el Goliat Verde, recopilada en un único y aplastante volumen! ¡Llega 'Planeta Hulk'! Un planeta aliení­gena salvaje. Tribus bárbaras oprimidas. Un emperador corrupto. Mortí­feros guerreros. Gladiadores y esclavos. Hachas de batalla y puños golpeadores. Monstruos y héroes. El cóctel explosivo se culmina con la llegada de un Hulk que ha sido traicionado por sus amigos y está muy, muy enfadado. ¡Que comience la batalla!",
	      "price":33.20,
	      "stock":16,
	      "availability":True,},
	      {"prodName": "The Legend Of Zelda. Hyrule Historia",
	      "image_name":"legend_zelda.jpg",
	      "descrip":"Este espléndido volumen incluye información exclusiva y nunca vista hasta ahora, como la cronología oficial de la saga, arte conceptual, diseños de personajes y bocetos descartados explicados al detalle por los propios diseñadores y creadores de los juegos, así como una reveladora introducción de mano del propio Shigeru Miyamoto. Y como extra, un manga muy especial: ¡la adaptación oficial Akira Himekawa del videojuego The Legend of Zelda: Skyward Sword !",
	      "price":28.45,
	      "stock":48,
	      "availability":True,},
	      {"prodName": "Civil War (Marvel Deluxe)",
	      "image_name":"civil_war.jpg",
	      "descrip":"Mark Millar, Steve Mcniven. . ¡El mayor evento de la historia del cómic, al fin recopilado en un volumen imprescindible y plagado de extras! El Universo Marvel está cambiando. Es tiempo de elegir: ¿De qué lado estás? Un conflicto que se ha estado larvado durante años estalla al fin, rompiendo en dos a la comunidad superheroica, y enfrentando a amigo contra amigo, hermano contra hermano. Spiderman, Los Vengadores, La Patrulla-X, Los Cuatro Fantásticos... todos se verán afectados. Todos deberán elegir su lugar en la guerra. Nadie está a salvo en la saga que cambió para siempre las reglas del juego.",
	      "price":22.75,
	      "stock":95,
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
	      {"prodName": "Y POR QUÉ NO: Del gimnasio a la Titan Desert",
	      "image_name":"gimnasio_titan.jpg",
	      "descrip":"No esperes. Que no hay tiempo. Esto va en serio. La vida son dos putos días y uno ya ha pasado. En este libro se cuenta la apuesta por vivir intensamente, por sentir pasión por lo que se está haciendo, de Abel Rodríguez, una persona normal que un buen día decide afrontar una de las pruebas de mountain bike más duras del mundo, la Titan Desert, sin tener pasado deportista de nivel importante ni tener la más remota idea de cómo encararlo. En él nos relata paso a paso todo el recorrido a través de los duros meses de preparación pero sin intención de adoctrinar ni nada por el estilo, nos lo muestra de forma clara y directa, incluso se diría que áspera, pero quizá por eso nos llegue de forma tan contundente su aventura.",
	      "price":14.82,
	      "stock":54,
	      "availability":True,},
	      {"prodName": "Ciclismo y rendimiento",
	      "image_name":"ciclismo_rendimiento.jpg",
	      "descrip":"Ciclismo y rendimiento es una didáctica guía de entrenamiento para cualquier ciclista que desee mejorar su nivel de condición física, ya sea de cara a la competición o al cicloturismo. La finalidad de esta guía es que el ciclista sea capaz de diseñar su propio plan de entrenamiento siguiendo las directrices que en ella se muestran. Dado que el rendimiento deportivo no solo se basa en entrenar, se incluyen también capítulos sobre aquellos aspectos que deben tenerse en cuenta para mejorar la condición física: nutrición y ayudas ergogénicas, biomecánica y fisiología básica del ejercicio. ",
	      "price":14.25,
	      "stock":32,
	      "availability":True,},
	      {"prodName": "Verdad Sobre El Reiki, La (Filosofia Oriental)",
	      "image_name":"reiki.jpg",
	      "descrip":"Este libro es un intento de esclarecer la parte histórica y muchos mitos que se han venido explicando sobre el Reiki. También trata de agrupar todas las ideas y enseñanzas de los diferentes estilos de Reiki en los que ha sido instruido su autor, Joan Piquer. Existen muchos estilos de Reiki pero todos comparten la misma raiz: Usui Sensei. En la actualidad el 99% de los estilos de Reiki provienen de la rama de Hawayo Takata quien aprendió de Hayashi Sensei. En los años de 1980 se extendió por Occidente y recibió la influencia cultural occidental, primero por su paso y expansión por Estados Unidos y, luego, por Europa. ",
	      "price":19.00,
	      "stock":25,
	      "availability":True,},
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
	for c in Category.objects.all():
		for p in Product.objects.filter(category=c):
			print("- {0} - {1}".format(str(c), str(p)))

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