from .models import *
from django.contrib.auth.models import User

def get_role(users):
    role_to_user = UserRoles.objects.get(user=users)
    return role_to_user.role




