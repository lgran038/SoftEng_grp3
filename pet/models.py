# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from enumchoicefield import ChoiceEnum, EnumChoiceField
from django.db import models
import time
from datetime import date
from django.utils import timezone

# Create your models here.
class Species(ChoiceEnum):
	bird = "Bird"
	cat = "Cat"
	dog = "Dog"
	horse = "Horse"
	default = "none"

class dog_breed (ChoiceEnum):
	beagle = "Beagle"
	border_collie = "Border Collie"
	boxer = "Boxer"
	bulldog = "Bulldog"
	chihuahua = "Chihuahua"
	chow_chow = "Chow Chow"
	dachshund = "Dachshund"
	doberman_pinscher = "Doberman Pinscher"
	english_mastiff = "English Mastiff"
	german_shepherd = "German Shepherd"
	golden_retriever = "Golden Retriever"
	great_dane = "Great Dane"
	labrador_retreiver = "Labador Retriever"
	pitbull = "Pit Bull"
	poodle = "Poodle"
	pug = "Pug"
	rottweiler = "Rottweiler"
	shih_tzu = "Shih Tzu"
	siberian_husky = "Siberian Husky"
	yorkshire_terrier = "Yorkshire Terrier"
	default = "none"

class cat_breed (ChoiceEnum):
	abyssinian = "Abyssinian"
	bengal = "Bengal"
	british_shorthair = "British Shorthair"
	burmese = "Burmese"
	maine_coon = "Maine Coon"
	persian = "Persian"
	ragdoll = "Ragdoll"
	russian_blue = "Russian Blue"
	siamese = "Siamese"
	sphynx = "Sphynx"
	default = "none"

class horse_breed (ChoiceEnum):
	american_miniature = "American Miniature"
	american_quarter = "American Quarter"
	andalusian = "Andalusian"
	arabian = "arabian"
	belgian = "Belgian"
	clydesdale = "Clydesdale"
	friesian = "Friesian"
	paso_fino = "Paso Fino"
	percheron = "Percheron"
	shire = "shire"
	thoroughbred = "Thoroughbred"
	default = "none"

class bird_breed (ChoiceEnum):
	amazon_parrot = "Amazon Parrot"
	budgerigar = "Budgerigar"
	chicken = "Chicken"
	cockatiel = "Cockatiel"
	cockatoo = "Cockatoo"
	domestic_canary = "Canary"
	finch = "Finch"
	grey_parrot = "Grey Parrot"
	lovebird = "Love Bird"
	parrot = "Parrot"
	default = "none"

class gender (ChoiceEnum):
	male = "Male"
	female = "Female"

class color (ChoiceEnum):
	white = "White"
	black = "Black"
	gray = "Gray"
	brown = "Brown"
	orange = "Orange"
	blonde = "Blonde"
	green = "Green"
	red = "Red"
	blue = "Blue"
	purble = "Purple"
	pink = "Pink"
	default ="none"

class adopt_status (ChoiceEnum):
	available = "Available"
	adopted = "Adopted"
	reserved = "Reserved"

class states (ChoiceEnum):
	alabama = "Alabama"
	alaska = "Alaska"
	arizona = "Arizona"
	arkansas = "Arkansas"
	california = "California"
	colorado = "Colorado"
	connecticut = "Connecticut"
	delaware = "Delaware"
	florida = "Florida"
	georgia = "Georgia"
	hawaii = "Hawaii"
	idaho = "Idaho"
	illinois = "Illinois"
	indiana = "Indiana"
	iowa = "Iowa"
	kansas = "Kansas"
	kentucky = "Kentucky"
	lousiana ="Louisiana"
	maine = "Maine"
	maryland = "Maryland"
	massachusetts = "Massachusetts"
	michigan = "Michigan"
	minnesota = "Minnesota"
	mississippi = "Mississippi"
	missouri = "Missouri"
	montana = "Montana"
	nebraska = "Nebraska"
	nevada = "Nevada"
	new_hampshire = "New Hampshire"
	new_jersey = "New Jersey"
	new_mexico = "New Mexico"
	new_york = "New York"
	north_carolina = "North Carolina"
	north_dakota = "North Dakota"
	ohio = "Ohio"
	oklahoma = "Oklahoma"
	oregon = "Oregon"
	pennsylvania = "Pennsylvania"
	rhode_island = "Rhode Island"
	south_carolina = "South Carolina"
	south_dakota = "South Dakota"
	tennessee = "Tennessee"
	texas = "Texas"
	utah = "Utah"
	vermont = "Vermont"
	virginia = "Virginia"
	washington = "Washington"
	west_virginia = "West Virginia"
	wisconsin = "Wisconsin"
	wyoming = "Wyoming"
	default = "none"

class Dog(models.Model):
	name = models.CharField(max_length=50)
	date_of_birth = models.DateField('Date of Birth', blank=True, default=date.today)
	color = EnumChoiceField(color, blank=True, default=color.default)
	height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
	weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
	date_entered = models.DateField('Date Entered Shelter', default=date.today)
	bio = models.TextField(blank=True, default="")
	shelter = models.ForeignKey('shelter')
	species = EnumChoiceField(Species, default=Species.dog, editable=False)
	breed = EnumChoiceField(dog_breed, blank=True, default=dog_breed.default)
	adoption_status = EnumChoiceField(adopt_status, default=adopt_status.available)

	def __unicode__(self):
		return self.name + " " + unicode(self.date_entered.strftime('%Y-%m-%d'))

class Cat(models.Model):
	name = models.CharField(max_length=50)
	date_of_birth = models.DateField('Date of Birth', blank=True, default=date.today)
	color = EnumChoiceField(color, blank=True, default=color.default)
	height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
	weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
	date_entered = models.DateField('Date Entered Shelter', default=date.today)
	bio = models.TextField(blank=True, default="")
	shelter = models.ForeignKey('shelter')
	species = EnumChoiceField(Species, default=Species.cat, editable=False)
	breed = EnumChoiceField(cat_breed, blank=True, default=cat_breed.default)
	adoption_status = EnumChoiceField(adopt_status, default=adopt_status.available)

	def __unicode__(self):
		return self.name + " " + unicode(self.date_entered.strftime('%Y-%m-%d'))

class Horse(models.Model):
	name = models.CharField(max_length=50)
	date_of_birth = models.DateField('Date of Birth', blank=True, default=date.today)
	color = EnumChoiceField(color, blank=True, default=color.default)
	height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
	weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
	date_entered = models.DateField('Date Entered Shelter', default=date.today)
	bio = models.TextField(blank=True, default="")
	shelter = models.ForeignKey('shelter')
	species = EnumChoiceField(Species, default=Species.horse, editable=False)
	breed = EnumChoiceField(horse_breed, blank=True, default=horse_breed.default)
	adoption_status = EnumChoiceField(adopt_status, default=adopt_status.available)

	def __unicode__(self):
		return self.name + " " + unicode(self.date_entered.strftime('%Y-%m-%d'))

class Bird(models.Model):
	name = models.CharField(max_length=50)
	date_of_birth = models.DateField('Date of Birth', blank=True, default=date.today)
	color = EnumChoiceField(color, blank=True, default=color.default)
	height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
	weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, default=0)
	date_entered = models.DateField('Date Entered Shelter', default=date.today)
	bio = models.TextField(blank=True, default="")
	shelter = models.ForeignKey('shelter')
	species = EnumChoiceField(Species, default=Species.bird, editable=False)
	breed = EnumChoiceField(bird_breed, blank=True, default=bird_breed.default)
	adoption_status = EnumChoiceField(adopt_status, default=adopt_status.available)

	def __unicode__(self):
		return self.name + " " + unicode(self.date_entered.strftime('%Y-%m-%d'))

class Shelter(models.Model):
	name = models.CharField(max_length=50)
	street = models.CharField(max_length=50)
	city = models.CharField(max_length=30)
	state = EnumChoiceField(states, default=states.florida)
	zipcode = models.CharField(max_length=10)
	phone_number = models.CharField(max_length=10)
	fax_number = models.CharField(max_length=10)
	email = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name
