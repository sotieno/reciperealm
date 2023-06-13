from django.urls import path
from .views import AuthView
from .views import LogoutView

app_name = "accounts"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('logout/', LogoutView, name='logout'),
]
