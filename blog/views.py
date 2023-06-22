from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Marker
from .forms import marker_Form
from django.http import HttpResponseRedirect
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from .models import Node

def map(request):
    return render(request, 'blog/home.html', {})
    
def save_marker(request):
    if request.method == 'POST':
       
        lng = float(request.POST.get('lng'))
        lat = float(request.POST.get('lat'))

        node = Point(lng, lat)
        instance = Node()
        instance.point=node
        
        instance.save()
       
        return redirect('map')
    
    return render(request, 'blog/map.html', {})
