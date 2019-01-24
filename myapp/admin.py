from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Roles)
admin.site.register(Permissions)
admin.site.register(PermissionsRoles)
admin.site.register(UserRoles)