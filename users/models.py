from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.




class CustomUserManager(BaseUserManager):
    def create_user(self, email, user_name, first_name, password, **extra_fields):

        if not email and not password and not user_name and not first_name:
            raise ValueError(_('Users must have valid email, username, and first name'))
        
        user = self.model(email=self.normalize_email(email), user_name=user_name, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, user_name, first_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True'))
        if extra_fields.get('is_verified') is not True:
            raise ValueError(_('Superuser must have is_verified=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        
        user = self.create_user(email, user_name, first_name, password, **extra_fields)
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # accounts = models.ManyToOneRel('api.Account', on_delete=models.CASCADE)    
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'first_name', 'last_name']
    
    def __str__(self):
        return f'{self.email}  |  {self.user_name}'
    