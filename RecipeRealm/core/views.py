from django.forms import ModelForm
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.translation import gettext_lazy as _
from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cuisine', 'category', 'level', 'servings', 'duration',
                  'method', 'ingredients', 'notes', 'nutrition', 'tags', 'featureimage',]


def LandingView(request):
    return render(request, "core/index.html")


def RecipesView(request):
    return render(request, "core/recipes.html")


def RecipeView(request, pk):
    context = {}
    obj = get_object_or_404(Recipe, id=pk)
    context['recipe'] = obj
    return render(request, "core/recipe.html", context)


def RecipeAddView(request):
    if not request.user.is_authenticated:
        return redirect("accounts:register")

    context = {}
    context['form'] = RecipeForm(initial={'author': request.user})

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.featureimage = request.FILES.get('featureimage')
            recipe.save()
            return redirect("core:recipe", pk=recipe.pk)
        else:
            context['form'] = form

    return render(request, "core/add.html", context)
 

def AboutView(request):
    return render(request, "core/about.html")


def ContactView(request):
    return render(request, "core/contacts.html")


def page404 (request, exception):
    return render(request, 'core/404.html')

