from django.urls import path
from sparkvellir.views import index, detailed

urlpatterns = [
    path('<slug:city>/', detailed),
    path('', index),
]
