from django.conf.urls import url
from shop import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'base', views.base, name='base')]