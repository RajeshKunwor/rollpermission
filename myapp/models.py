from django.db import models
import datetime
from django.utils import timezone

from django.contrib.auth.models import User
# Create your models here.

class Roles(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=2,default='')
    def __str__(self):
        return self.name


class Permissions(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=2, default='')
    def __str__(self):
        return self.name



class UserRoles(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    status = models.CharField(max_length=2, default='')
    def __str__(self):
        return f'{self.user}|{self.role}'


class PermissionsRoles(models.Model):
    permission = models.ForeignKey(Permissions,on_delete=models.CASCADE)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    status = models.CharField(max_length=2, default='')
    def __str__(self):
        return f'{self.role}|{self.permission}'
