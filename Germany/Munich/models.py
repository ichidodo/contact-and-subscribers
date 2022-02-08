


# Create your models here.
from django.db import models


# Create your models here.
class Prospects(models.Model):
    Email= models.EmailField()
    First_name = models.CharField(max_length=200)
    Last_name=models.CharField(max_length=200)
    Comments=models.TextField(max_length=2000)

class Meta:
    ordering = ('Email',)
    def __str__(self):
        return self.Email

class Subscribers(models.Model):
    Email = models.EmailField()
    Name= models.CharField(max_length=200)



class Meta:
    ordering = ('Email',)
    def __str__(self):
        return self.Emai