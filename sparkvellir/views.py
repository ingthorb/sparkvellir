# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sparkvellir/index.html')

def detailed(request, city_name):
    # Fetch information about the Field here!
    
    context = {
        'City': city_name,
        'Street': street_name
    }
    return render(request, 'sparkvellir/detailedLocation.html', context)