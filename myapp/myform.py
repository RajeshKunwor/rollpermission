from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()


    class Meta:

        model=User
        fields=['username','email','password1','password2']


class RoleForm(forms.ModelForm):
    class Meta:
        model = Roles
        exclude={'status'}
        fields = '__all__'


class PermissionForm(forms.ModelForm):
    class Meta:
        model = Permissions
        exclude = {'status'}
        fields = '__all__'


class RolePermissionForm(forms.ModelForm):
    class Meta:
        model = PermissionsRoles
        exclude = {'status'}
        fields = '__all__'


class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRoles
        exclude = {'status'}
        fields ='__all__'


