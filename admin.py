from django.contrib import admin
from myapp.models import *

"""
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
admin.site.register(Catagory,CategoryAdmin)
"""
admin.site.register(Catagory)
admin.site.register(Products)

# Register your models here.
