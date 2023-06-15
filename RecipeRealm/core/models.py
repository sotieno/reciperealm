from django.contrib.auth import get_user_model
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(User, related_name='authors', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    cuisine = models.CharField(max_length=50, default="Null")
    category = models.CharField(max_length=50,  default="Uncategorized")
    level = models.CharField(max_length=50, default='Null')
    servings = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    method = RichTextField(config_name='full_editor', blank=True, null=True)
    ingredients = RichTextField(config_name='full_editor', blank=True, null=True)
    notes = RichTextField(config_name='full_editor', blank=True, null=True)
    nutrition = RichTextField(config_name='full_editor', blank=True, null=True)
    featureimage = models.ImageField(upload_to='core/recipes/%Y/%m/')
    publishdate = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100, default="Untagged")

    def __str__(self):
        return self.name

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
