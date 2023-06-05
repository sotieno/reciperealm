from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def HomeView(request):
    return render(request, "core/recipe.html")


def AboutView(request):
    return render(request, "core/about.html")


def ContactView(request):
    return render(request, "core/contacts.html")

