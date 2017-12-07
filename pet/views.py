# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Dog

# Create your views here.

def index(request):
	all_pets_list = Dog.objects.all()
	output = ', '.join([p.name + ": " + p.species for p in all_pets_list])
	return HttpResponse("Hi there! You've reached the Pet index."
	+ "\nHere's all the pets.\n%s" % output)
