from django.db import models
from shelter.models import Shelter

GUEST_SHELTER = -1  # shelters that no longer exist in the database
GUEST_ADOPTER = -1  # guest adopters OR registered adopter that no longer exist in the database


class Person(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)  # struct?
    email = models.EmailField()
    phone_number = models.IntegerField()


class Adopter(Person):
    def __str__(self):
        return self.name


class Employee(Person):
    shelter = models.ForeignKey(Shelter, null=True,
                                on_delete=models.CASCADE)  # if the shelter is removed, remove the employee also

    def __str__(self):
        return self.name


class Admin(Employee):
    def __str__(self):
        return self.name
