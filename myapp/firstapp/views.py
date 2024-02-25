from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.views import View
from .models import TodoItem
from .models import *
import googlemaps
from django.conf import settings
# Respnse takes any serialized or python data, and renders it as json data
from rest_framework.response import Response
from rest_framework.decorators import api_view

#get stuff from files for item importation
from firstapp.models import Item
from .scripts.serializers import ItemSerializer
# Create your views here.

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

class GoogleView(ListView):
    template_name = "home.html"
    context_object_name = 'mydata'
    model = locations
    success_url = "/"

class GeoCodeView(View):
    template_name = "geocoding.html"

    def get(self, request, pk):
        location = locations.objects.get(pk = pk)

        if location.address and location.country and location.city != None:
            address_string = str(location.address)+ "," + str(location.city) + ", " +str (location.country)
            gmaps = googlemaps.Client(key = settings.GOOGLE_API_KEY)
            result = gmaps.geocode(address_string)[0]

            lat = result.get('geometry', {}).get('location', None).get('lat', None)
            lng = result.get('geometry', {}).get('location', None).get('lng', None)
            place_id = result.get('place_id', {})

            location.lat = lat
            location.lng = lng
            location.place_id = place_id
            location.save()

            """ Old method to locate stuff (fill in context and html to re use this) """
            """ geometry = result.get('geometry', {})
            
            location1 = geometry.get('location', {})

            lat = location1.get('lat', None)
            lng = location1.get('lng', None) """
        else:
            result = ""   

        context = {
            'location' :location,
            'result':result,
            'lat': lat,
            'lng' : lng,
            'place_id' : place_id
        }

        return render(request, self.template_name, context)

