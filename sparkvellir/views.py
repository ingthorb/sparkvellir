# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import logging


def index(request):
    return render(request, 'sparkvellir/index.html')


def detailed(request, city):
    logging.warning('adfasdf')

    context = {
        'City': city
    }

    return render(request, 'sparkvellir/detailedLocation.html', context)