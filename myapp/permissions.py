from rolepermissions.permissions import register_object_checker
from rollpermission.roles import SystemAdmin

@register_object_checker()
def access_organizaion(role,user,org):
    if role == SystemAdmin:
        return True
    if user.org  == org:
        return True

    return False
