# firstapp/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name= 'home'),
]
# This might be needed, depending on your Django version
app_name = "firstapp"