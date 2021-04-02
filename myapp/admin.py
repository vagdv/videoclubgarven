from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Movie

# Register your models here.

admin.site.register(Movie)
admin.site.unregister(Group)
