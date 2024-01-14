# firstapp/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name= 'home'),
    path("todos/", views.todos, name = "Todos")
]
# This might be needed, depending on your Django version
app_name = "firstapp"