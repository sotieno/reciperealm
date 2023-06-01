from django.urls import path
from views import AuthView
from signup import SubscribeView
from signin import SigninView
from logout import LogoutView
# from .controllers.pwdreset import resetPwdView, userVerifyView
# from .controllers.editpassword import resetPwdEditView

app_name = "account"

urlpatterns = [
    path('auth/', AuthView, name='auth'),
    path('subscribe/', SubscribeView, name='subscribe'),
    path('signin/', SigninView, name='signin'),
    # path('reset/', resetPwdView, name='reset1'),
    # path('reset/identifier?<uidcoded><token>/', resetPwdEditView, name='reset2'),
    # path('signin/verify?<uidcoded><token>/', userVerifyView, name='signinauth'),
    path('logout/', LogoutView, name='logout'),
]
