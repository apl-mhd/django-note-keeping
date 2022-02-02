import imp
from django.contrib import admin
from . models import Note
from . models import Tag



admin.site.register(Note)
admin.site.register(Tag)
