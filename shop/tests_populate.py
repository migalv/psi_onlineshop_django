# -*- coding: utf-8 -*-
# Uncomment if you want to run tests in transaction mode with a final rollback
#from django.test import TestCase
#uncomment this if you want to keep data after running tests
from unittest import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client
from shop.models import Product, Category

import os
base_path   = os.getcwd()
static_path = os.path.join(base_path,"static")


#python ./manage.py test shop.tests.viewsTests --keepdb

DEBUG = False
from PIL import Image
from StringIO import StringIO
from django.core.files.base import File


class viewsTests(TestCase):
    def setUp(self):
        self._client   = Client()
        self.clean_database()
        self.populate()

    def clean_database(self):
        Product.objects.all().delete()
        Category.objects.all().delete()

    # Se crea un nuevo producto en caso de que no exista otro con el mismo nombre.
    # Autor: Miguel Alvarez
    def add_product(self, cat, prodName, image_name, description, price, stock, availability):
        try:
            p = Product.objects.get(prodName=prodName)
        except Product.DoesNotExist:
            p = Product.objects.create(category=cat, prodName=prodName, 
                description = description , price=price, 
                stock = stock, availability = availability)
            imageObject = File(open(os.path.join('media/images', image_name),'r'))
            p.image.save(image_name, imageObject, save = True)
            p.save()

        return p

    # Se crea una nueva categoria en caso de que no exista otra con el mismo nombre.
    # Autor: Miguel Alvarez
    def add_cat(self, name):
        c = Category.objects.get_or_create(catName=name)[0]
        c.save()
        return c

    def test_produnct_list(self):
        response = self._client.get(reverse('product_list'), follow=True)
        for counter in range(0,3):
            self.assertIn(b'%s'%("cat_%d"%counter), response.content)
        for counterCat in range(0, 3):
            for counterProd in range(0, 5):
                self.assertIn(b"fileName_%d_%d"%(counterCat,counterProd), response.content)

    def test_produnct_list_cat_0(self):
        response = self._client.get(reverse('product_list_by_category',
                                            kwargs={'catSlug':'cat_0'}), follow=True)
        for counter in range(0, 3):
            self.assertIn(b'%s' % ("cat_%d" % counter), response.content)
        for counterCat in range(0, 1):
            for counterProd in range(0, 5):
                self.assertIn(b"fileName_%d_%d" % (counterCat, counterProd), response.content)
        for counterCat in range(1, 3):
            for counterProd in range(0, 5):
                self.assertNotIn(b"fileName_%d_%d" % (counterCat, counterProd), response.content)

    def test_product_detail_fileName_0_0(self):
        prodName='fileName_0_1'
        p = Product.objects.get(prodName = prodName)
        response = self._client.get(reverse('product_detail',
                                            kwargs={'id':p.id,
                                                    'prodSlug':p.prodSlug}), follow=True)
        self.assertIn   (b'cat_0', response.content)
        self.assertNotIn(b'cat_1', response.content)

        self.assertIn(b'No', response.content)
        self.assertNotIn(b'Greg Pak, Carlo Pagulayan, Aaron Lopresti, Gary Frank.', response.content)

    #Funcion que aniade los productos y categorias deseados a la aplicacion.
    #Autor: Miguel Alvarez
    def populate(self):

        # Se crean listas de dicccionarios que contienen los datos a generar,
        # y despues se crea un diccionario de diccionarios que contiene todas las categorias. 
        # Asi se puede iterar sobre los datos de forma sencilla.
        
        comic_books = [
             {"prodName": "fileName_0_0",
             "image_name":"DragonBall_01.jpg",
              "descrip":"No",
              "price":7.55,
              "stock":10,
              "availability":True,},    
             {"prodName": "fileName_0_1",
              "image_name":"EnciclopediaMarioBros.jpg",
              "descrip":"No",
              "price":28.50,
              "stock":35,
              "availability":True,},
              {"prodName": "fileName_0_2",
              "image_name":"planeta_hulk.jpg",
              "descrip":"Greg Pak, Carlo Pagulayan, Aaron Lopresti, Gary Frank. . ¡La mas espectacular aventura jamas protagonizada por el Goliat Verde, recopilada en un unico y aplastante volumen! ¡Llega 'Planeta Hulk'! Un planeta alieni­gena salvaje. Tribus barbaras oprimidas. Un emperador corrupto. Morti­feros guerreros. Gladiadores y esclavos. Hachas de batalla y puños golpeadores. Monstruos y heroes. El coctel explosivo se culmina con la llegada de un Hulk que ha sido traicionado por sus amigos y esta muy, muy enfadado. ¡Que comience la batalla!",
              "price":33.20,
              "stock":16,
              "availability":True,},
              {"prodName": "fileName_0_3",
              "image_name":"legend_zelda.jpg",
              "descrip":"Este esplendido volumen incluye informacion exclusiva y nunca vista hasta ahora, como la cronologia oficial de la saga, arte conceptual, diseños de personajes y bocetos descartados explicados al detalle por los propios diseñadores y creadores de los juegos, asi como una reveladora introduccion de mano del propio Shigeru Miyamoto. Y como extra, un manga muy especial: ¡la adaptacion oficial Akira Himekawa del videojuego The Legend of Zelda: Skyward Sword !",
              "price":28.45,
              "stock":48,
              "availability":True,},
              {"prodName": "fileName_0_4",
              "image_name":"civil_war.jpg",
              "descrip":"Mark Millar, Steve Mcniven. . ¡El mayor evento de la historia del comic, al fin recopilado en un volumen imprescindible y plagado de extras! El Universo Marvel esta cambiando. Es tiempo de elegir: ¿De que lado estas? Un conflicto que se ha estado larvado durante años estalla al fin, rompiendo en dos a la comunidad superheroica, y enfrentando a amigo contra amigo, hermano contra hermano. Spiderman, Los Vengadores, La Patrulla-X, Los Cuatro Fantasticos... todos se veran afectados. Todos deberan elegir su lugar en la guerra. Nadie esta a salvo en la saga que cambio para siempre las reglas del juego.",
              "price":22.75,
              "stock":95,
              "availability":True,},
             {"prodName": "fileName_0_5",
              "image_name":"Pokemon17.jpg",
              "descrip":"No",
              "price":11.40,
              "stock":12,
              "availability":True,} ]
         
        sport_books = [
             {"prodName": "fileName_1_0",
              "image_name":"ElJuegoInterior.jpg",
              "descrip":"No",
              "price":6.64,
              "stock":85,
              "availability":True,},
             {"prodName": "fileName_1_1",
              "image_name":"calderon.jpg",
              "descrip":"No",
              "price":20.80,
              "stock":73,
              "availability":False,},
              {"prodName": "fileName_1_2",
              "image_name":"gimnasio_titan.jpg",
              "descrip":"No esperes. Que no hay tiempo. Esto va en serio. La vida son dos putos dias y uno ya ha pasado. En este libro se cuenta la apuesta por vivir intensamente, por sentir pasion por lo que se esta haciendo, de Abel Rodriguez, una persona normal que un buen dia decide afrontar una de las pruebas de mountain bike mas duras del mundo, la Titan Desert, sin tener pasado deportista de nivel importante ni tener la mas remota idea de como encararlo. En el nos relata paso a paso todo el recorrido a traves de los duros meses de preparacion pero sin intencion de adoctrinar ni nada por el estilo, nos lo muestra de forma clara y directa, incluso se diria que aspera, pero quiza por eso nos llegue de forma tan contundente su aventura.",
              "price":14.82,
              "stock":54,
              "availability":True,},
              {"prodName": "CfileName_1_3",
              "image_name":"ciclismo_rendimiento.jpg",
              "descrip":"Ciclismo y rendimiento es una didactica guia de entrenamiento para cualquier ciclista que desee mejorar su nivel de condicion fisica, ya sea de cara a la competicion o al cicloturismo. La finalidad de esta guia es que el ciclista sea capaz de diseñar su propio plan de entrenamiento siguiendo las directrices que en ella se muestran. Dado que el rendimiento deportivo no solo se basa en entrenar, se incluyen tambien capitulos sobre aquellos aspectos que deben tenerse en cuenta para mejorar la condicion fisica: nutricion y ayudas ergogenicas, biomecanica y fisiologia basica del ejercicio. ",
              "price":14.25,
              "stock":32,
              "availability":True,},
              {"prodName": "fileName_1_4",
              "image_name":"reiki.jpg",
              "descrip":"Este libro es un intento de esclarecer la parte historica y muchos mitos que se han venido explicando sobre el Reiki. Tambien trata de agrupar todas las ideas y enseñanzas de los diferentes estilos de Reiki en los que ha sido instruido su autor, Joan Piquer. Existen muchos estilos de Reiki pero todos comparten la misma raiz: Usui Sensei. En la actualidad el 99% de los estilos de Reiki provienen de la rama de Hawayo Takata quien aprendio de Hayashi Sensei. En los años de 1980 se extendio por Occidente y recibio la influencia cultural occidental, primero por su paso y expansion por Estados Unidos y, luego, por Europa. ",
              "price":19.00,
              "stock":25,
              "availability":True,},
              {"prodName": "fileName_1_5",
              "image_name":"runners.jpg",
              "descrip":"El running no es una disciplina que involucre solamente las pistas o competencias, son muchos los aspectos que se deben considerar para ser verdaderamente exitosos en este deporte. A continuacion desarrollaremos diferentes topicos que buscan brindarte las herramientas para que seas exitoso en el desempeño deportivo",
              "price":2.99,
              "stock":65,
              "availability":True,} ]
         
        history_books = [
             {"prodName": "fileName_2_0",
              "image_name":"pacientes.jpg",
              "descrip":"No",
              "price":6.64,
              "stock":85,
              "availability":True,},
              {"prodName": "fileName_2_1",
              "image_name":"guarida_raposo.jpg",
              "descrip":"Mi nombre es Jose Raposo. Siendo un crio me fui a guardar cabras con Perico el Cojo. Luego, trabaje como jornalero en el cortijo de los Galvez. Hasta que los dos hijos pequeños del patron violaron a mi hermana Juana. Ellos pagaron su culpa y yo la mia: Los mate y a mi me condenaron a cadena perpetua. Fueron años terribles. Ahora que lo pienso, no bebia para olvidarme de todo, sino para acabar con aquella pesadilla. Un dia, aparecio por el penal una persona excepcional que me hizo ver que yo podia ser un buen hombre. ",
              "price":11.86,
              "stock":24,
              "availability":True,},
              {"prodName": "fileName_2_2",
              "image_name":"postguerra.jpg",
              "descrip": "En 1945 Europa se encontraba en sus momentos mas bajos. Gran parte del continente estaba devastado por la guerra, los asesinatos en masa, los bombardeos y el caos. Amplias zonas de Europa del Este empezaban a caer bajo control sovietico para cambiar un despotismo por otro. En la actualidad, la Union Sovietica ya no existe y las democracias europeas llegan hasta la frontera de Rusia.",
              "price":28.02,
              "stock":36,
              "availability":True,},
              {"prodName": "fileName_2_3",
              "image_name":"dinosaurios.jpg",
              "descrip": "Con la descripcion de todos los dinosaurios desde Tyrannosaurus hasta Velociraptor e ilustrada con mas de 700 imagenes e impresionantes reconstrucciones digitales, incluidas las de los fosiles mas espectaculares del mundo, esta obra es la guia mas actual de la vida prehistorica. Presenta y estudia en profundidad mas de 400 especies, desde milpies del tamaño de un cocodrilo y aves terrorificas gigantes devoradoras de caballos hasta nuestros propios ancestros de aspecto simiesco, desde los escorpiones gigantes de los primitivos oceanos hasta los mamuts de la era glacial exterminados por los cazadores de la Edad de Piedra.",
              "price":22.80,
              "stock":87,
              "availability":True,},
             {"prodName": "fileName_2_4",
              "image_name":"lasdrogas.jpg",
              "descrip":"Łukasz Kamieński nos ofrece una nueva vision del papel que han desempeñado las drogas en la guerra, desde los heroes homericos que consumian opio hasta, en la actualidad, los cientos de miles de niños soldados que combaten drogados. En esta historia aprendemos como los ingleses forjaron un imperio basado en el ron, como las tropas de Napoleon descubrieron el hachis en Egipto o como las drogas explican las peores aberraciones de la guerra de Vietnam. Pero, al margen de este escenario de guerras, Kameński nos muestra que muchos de estos productos, prohibidos tan solo hace unos años, han formado parte por mucho tiempo de nuestra vida cotidiana, como la cocaina o como la heroina, lanzada al mercado en 1898, junto a la aspirina, como un sedante para la tos. Este libro, que Foreign Affairs",
              "price":12.34,
              "stock":64,
              "availability":True,},
              {"prodName": "fileName_2_5",
              "image_name":"victorias.jpg",
              "descrip":"No",
              "price":4532.98,
              "stock":1,
              "availability":True,} ]

         
        cats = {"cat_0": {"books": comic_books},
                "cat_1": {"books": sport_books}, 
                "cat_2": {"books": history_books } }
        
        # Se itera sobre el diccionario de diccionarios,
        # "cats", añadiendo cada categoria que contenga, y por cada categoria, sus productos.
     
        for cat, cat_data in cats.iteritems():
            c = self.add_cat(cat)
            for p in cat_data["books"]:
                self.add_product(c, p["prodName"], p["image_name"], p["descrip"], p["price"], p["stock"], p["availability"])