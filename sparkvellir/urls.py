from django.conf.urls import  url
from . import views

urlpatterns = [
    url('<str:city_name>', views.detailed, name='detailed'),
    url(r'', views.index, name='index'),
];