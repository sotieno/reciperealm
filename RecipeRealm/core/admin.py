from django.contrib import admin
from .models import Contact, Recipe

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    list_display = ('id','name', 'cuisine','category')
admin.site.register(Recipe, RecipeAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'postdate', 'content')
admin.site.register(Contact, ContactAdmin)