from django.urls import path
from .views import LoginView
from .views import LogoutView
from .views import RegisterView

app_name = "accounts"

urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
]
