from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Cuisine(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    country = models.CharField(max_length = 100)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cuisines'


class CuisineType(models.Model):
    id = models.BigAutoField(primary_key=True)
    RECIPE_TYPES = (
        ('BR', 'Breakfast'),
        ('LN', 'Lunch'),
        ('DN', 'Dinner'),
    )
    name = models.CharField(max_length=10, choices=RECIPE_TYPES)
    slug = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'recipe_types'


class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(User, related_name='authors', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    cuisine = models.ForeignKey(Cuisine, related_name='cuisines', on_delete=models.PROTECT)
    recipe_type = models.ForeignKey(CuisineType, related_name='types', on_delete=models.PROTECT)
    ingredients = models.CharField(max_length=1000, blank=True, null=True)
    cooking_duration = models.PositiveIntegerField(default=0)
    cooking_method = RichTextField(config_name='full_editor', blank=True, null=True)
    featureimage = models.ImageField(upload_to='core/article/%Y/%m/')
    publishdate = models.DateField(auto_now_add=False)

    def get_absolute_url(self):
        return f'/recipe/{self.id}/{self.slug}/'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishdate']
        db_table = 'recipes'


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    postdate = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000, blank=False)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    class Meta:
        ordering = ['-postdate']
        db_table = 'contacts'
