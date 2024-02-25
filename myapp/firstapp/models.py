from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator 
from django.core.exceptions import ValidationError

class subject(models.Model):
    name = models.CharField(max_length = 100)
    teacher_name = models.CharField(max_length = 50)
    units = models.IntegerField()

    def __str__(self):
        return '{}: {} unit(s)'.format(self.name, self.units)
    
    def get_absolute_url(self):
        return reverse('sibject_detail', args = [str(self.name)])

    def is_tutorial(self):
        return self.units == 1
    
class IndexCard(models.Model):
    name = models.CharField(max_length = 100)
    subject = models.ForeignKey(
        subject, 
        on_delete = models.CASCADE,
        related_name = 'students'
        )
    section = models.CharField(max_length=5)
    age = models.IntegerField() 

class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)

def int_is_even(value):
    if(value % 2 != 0):
        raise ValidationError(str(value) + 'is not even')

class Item(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)



class TestItem(models.Model):
    name = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)
    num = models.IntegerField(validators = [int_is_even])

class locations(models.Model):
    club = models.CharField(max_length = 500, blank = True, null = True)
    name = models.CharField(max_length = 500)
    zipcode = models.CharField(max_length = 500, blank = True, null = True)
    city = models.CharField(max_length = 200, blank = True, null = True)
    country = models.CharField(max_length = 200, blank = True, null = True)
    address = models.CharField(max_length = 200, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True, blank = True, null = True)
    edited_at = models.DateTimeField(auto_now = True)

    lat = models.CharField(max_length = 200, blank = True, null = True)
    lng = models.CharField(max_length = 200, blank = True, null = True)
    place_id = models.CharField(max_length = 200, blank = True, null = True)
    def __str__(self):
        return self.name

# Create your models here.
