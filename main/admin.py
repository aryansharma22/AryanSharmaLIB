from django.contrib import admin
from .models import Books, Item

# Register your models here.
admin.site.register(Books)
admin.site.register(Item)