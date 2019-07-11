from django.db import models

# Create your models here.
class Animal(models.Model):
    animal_name = models.CharField(max_length=30)
    