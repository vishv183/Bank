from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from .models import *
# Register your models here.



class UserAdminConfig(UserAdmin):
    model = User
    ordering = ('-start_date',)
    list_display = ('email', 'user_name', 'first_name')
    search_fields = ('email', 'user_name', 'first_name', 'last_name')
    list_filter = ('email', 'user_name', 'is_staff',
                   'is_superuser', 'is_verified', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff',
         'is_superuser', 'is_verified', 'is_active', 'user_permissions', 'groups')}),
        
    )


    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'user_name',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_superuser',
                    'is_verified',
                    'is_active',
                    'user_permisssions',
                    'groups'
                )
            }
        ),
    )

admin.site.register(User, UserAdminConfig)