# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Region, Town
import logging


def index(request):
    return render(request, 'sparkvellir/index.html')

#Fix for regions, should now have to get everytime
def detailed(request, region):

    regionInfo = Region.objects.get(slug=region)
    logging.warning(regionInfo)
    tow = Town.objects.all()
    logging.warning(tow)
    towns = Town.objects.order_by('country_part')
    towns2 = Town.objects.filter(country_part=regionInfo).order_by('city_name')
    logging.warning(towns2)
    context = {
        'Region': regionInfo,
        'Towns_list': towns2,
    }

    return render(request, 'sparkvellir/detailedLocation.html', context)
