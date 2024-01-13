from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello World! This came from the index view')


