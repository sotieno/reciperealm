from django.contrib import admin
from .models import Contact, Recipe, CuisineType, Cuisine

class CuisineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name', 'country')
admin.site.register(Cuisine, CuisineAdmin)

class CuisineTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name')
admin.site.register(CuisineType, CuisineTypeAdmin)

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name','author','cuisine','recipe_type')
admin.site.register(Recipe, RecipeAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'postdate', 'content')
admin.site.register(Contact, ContactAdmin)