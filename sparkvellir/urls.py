from django.urls import path
from sparkvellir.views import index, detailed
from django.conf import settings

urlpatterns = [
    path('<slug:region>/', detailed, name="detailed-region"),
    path('', index, settings.STATIC_ROOT),
]
