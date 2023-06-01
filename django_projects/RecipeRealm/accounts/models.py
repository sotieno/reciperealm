"""
models module: handles a user class
"""
from django.db import models
from django.db.models.deletion import *
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import uuid


class UserManager(BaseUserManager):
    """
    saves a User instance as either a normal user with or without superuser previledges
    """

    def create_user(self, email, password=None):
        """
        class method that creates a normal user
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model( email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password):
        """
        class method that creates a superuser
        """
        user = self.create_user(email, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    defines a User instance
    """
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    email = models.EmailField(verbose_name=_('Email'), max_length=100, unique=True)
    alias = models.CharField(verbose_name=_('Username'), max_length=18, unique=True,
        validators=[RegexValidator(r'^[a-zA-Z0-9_]{3,18}$', message="Username should be between 3-18 characters, and must contain letters, numbers, or '_' only.")]
        )
    # password = models.CharField(
    #     verbose_name=_('Password'),
    #     max_length=24,
    #     validators=[RegexValidator(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$', message=_(" Password should be 8 to 24 characters. Must include uppercase and lowercase letters, a number and a special character."))]
    # )
    full_name = models.CharField(verbose_name=_('Full name'), max_length=255, null=True, blank=False, default="No name")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['alias',]

    def __str__(self):
        """
        Returns a strings representation of a user instance
        """
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Returns admin status of a user instance
        """
        return self.is_admin
        
    def has_module_perms(self, app_label):
        """
        Returns user instance permissions
        """
        return True
