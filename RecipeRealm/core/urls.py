from django.urls import path
from .views import HomeView, AboutView, ContactView

app_name = "core"

urlpatterns = [
    path('recipes/', HomeView, name='recipes'),
    path('about/', AboutView, name='about'),
    path('contact/', ContactView, name='contact'),
]
