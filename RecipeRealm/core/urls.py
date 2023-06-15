from django.urls import path
from .views import RecipeAddView
from .views import RecipeView
from .views import RecipesView
from .views import AboutView
from .views import ContactView
from .views import LandingView

app_name = "core"

urlpatterns = [
    path('', LandingView, name='home'),
    path('recipes/', RecipesView, name='recipes'),
    path('recipes/<int:pk>/', RecipeView, name='recipe'),
    path('recipe/add/', RecipeAddView, name='add'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
]
