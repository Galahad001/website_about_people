from django.contrib import admin
from .models import *

class PeopleAdmins(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_create', 'images', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'date_create')


class CategoryAdmins(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('name',)

admin.site.register(People, PeopleAdmins)
admin.site.register(Category, CategoryAdmins)

# Register your models here.
