from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date', 'author')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(New, NewAdmin)
admin.site.register(Author, AuthorAdmin)