from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.views import View
from .models import TodoItem
from .models import *
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

        context = {
            'location' :location
        }

        return render(request, self.template_name, context)

