from django.shortcuts import render
# appname/views.py
from django.http import HttpResponse
def index(request):
    return HttpResponse('Hello World! This came from the index view')

# Create your views here.
