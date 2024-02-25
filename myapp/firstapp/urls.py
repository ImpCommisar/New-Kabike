# firstapp/urls.py
from django.urls import path
from . import views
from .views import *
urlpatterns = [
    #path('', views.home, name= 'home'),
    path('', GoogleView.as_view(), name = "Google_View"),
    path('geocoding/<int:pk>', GeoCodeView.as_view(), name = 'GeoView'),
    path("todos/", views.todos, name = "Todos"),
    path("api/", views.getData),
    path("add/", views.addItem),
]
# This might be needed, depending on your Django version