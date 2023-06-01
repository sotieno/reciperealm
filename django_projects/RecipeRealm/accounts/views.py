from django import forms
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.validators import RegexValidator
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from urllib import request

User = get_user_model()


class subscribeForm(forms.ModelForm):
    """
    Defines a form instance to create a new user
    """
    email = forms.CharField(
        widget=forms.EmailInput(), 
        max_length=100,
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,20}$', message=_("Please enter a valid email"))],
    )
    alias = forms.CharField(
        validators=[RegexValidator(r'^[A-Za-z0-9-_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")],
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character (!@#$%)."))]
    )

    class Meta:
        model = User
        fields = ('email', 'alias', 'full_name', 'password')

    def clean_alias(self):
        """
        Checks username for errors

        Returns:
            Form error if username exists else continues with adding new user
        """
        cleaned_data = super(subscribeForm, self).clean()
        alias = cleaned_data.get("alias")
        if User.objects.filter(alias__iexact=alias).exists():
            msg = f"{alias} is not available!"
            self.add_error('alias', msg)
        return alias

    def save(self, commit=True):
        """
        Commits new user form to memory
        """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class signinForm(forms.Form):
    """
    creates a form instance to log in a new user
    """
    email = forms.CharField(
        widget=forms.EmailInput(), 
        max_length=100, 
        validators=[RegexValidator(r'^[a-z0-9]+(\.?[a-z0-9])*[a-z0-9]+@[a-z0-9\-]*\.[a-z]{2,20}$', message=_("Please enter a valid email"))],
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        password = cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if not user:
            msg = _("Your email and/or Password are invalid.")
            raise ValidationError(msg, code='invalid')


def AuthView(request):

    if request.user.is_authenticated:
        return redirect("app:index")
    
    context= {}
    context['regform'] = subscribeForm(initial={'full_name': 'No Name'})
    context['loginform'] = signinForm()

    if request.method == "POST":
        if 'registration' in request.POST:
            form = subscribeForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email'].lower()
                full_name = form.cleaned_data['full_name']
                alias = form.cleaned_data['alias']
                password = form.cleaned_data['password']
                user = authenticate(email=email, full_name=full_name, alias=alias, password=password)
                login(request, user)
                return redirect("app:index")
            else:
                context['regform'] = form

        if 'login' in request.POST:
            form = signinForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("app:index")
            else:
                context['loginform'] = form

    return render(request, "accounts/index.html", context)


def LogoutView(request, *args, **kwargs):
    logout(request)
    return redirect("app:index")
