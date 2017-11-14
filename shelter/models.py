from django.db import models

GUEST_SHELTER = -1  # shelters that no longer exist in the database
GUEST_ADOPTER = -1  # guest adopters OR registered adopter that no longer exist in the database


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50) # Create ENUM
    phone_number = models.IntegerField()
    fax_number = models.IntegerField(blank=True)  # optional
    email = models.EmailField()

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    color = models.CharField(max_length=50)  # enum?
    height = models.IntegerField()
    weight = models.IntegerField()
    type = models.CharField(max_length=3)  # enum? dog cat parrot
    time_in_shelter = models.IntegerField()
    special_notes = models.CharField(blank=True) #optional
    shelter = models.ForeignKey(Shelter, null=True, on_delete=models.SET_NULL)
    owner_id = models.IntegerField()
    status = models.CharField(max_length=50)  # enum? available adopted reserved

    # pictures
    def __str__(self):
        return self.name
