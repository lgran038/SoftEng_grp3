# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Shelter, Dog, Cat, Horse, Bird

# Register your models here.

admin.site.register(Dog)

admin.site.register(Cat)

admin.site.register(Horse)

admin.site.register(Bird)

admin.site.register(Shelter)

