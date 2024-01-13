from django.db import models
from django.urls import reverse

""" class subject(models.Model):
    name = models.CharField(max_length = 100)
    teacher_name = models.CharField(max_length = 50)
    units = models.IntegerField()

    def __str__(self):
        return '{}: {} unit(s)'.format(self.name, self.units)
    
    def get_absolute_url(self):
        return reverse('sibject_detail', args = [str(self.name)])

    def is_tutorial(self):
        return self.units == 1 """
    
""" class IndexCard(models.Model):
    name = models.CharField(max_length = 100)
    subject = models.ForeignKey(
        subject, 
        on_delete = models.CASCADE,
        related_name = 'students'
        )
    section = models.CharField(max_length=5)
    age = models.IntegerField()  """

class TodoItem(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False)
# Create your models here.
