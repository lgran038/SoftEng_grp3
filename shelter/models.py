from django.db import models

# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)


class Pet(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField() # enum
    breed = models.CharField() #enum
    gender = models.CharField()

