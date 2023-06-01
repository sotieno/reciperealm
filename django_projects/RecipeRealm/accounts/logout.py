from django.contrib.auth import logout
from django.shortcuts import redirect

# from django.contrib import messages

def LogoutView(request, *args, **kwargs):
    logout(request)
    destination = request.session['next']
    if destination:
        return redirect(f'{destination}')
    return redirect("app:recipes")