from rolepermissions.roles import AbstractUserRole

class Employee(AbstractUserRole):
    available_permissions = {
        'create_customer': True,
        'update_customer':True,
        'delete_customer': True,
    }

class Customer(AbstractUserRole):
    available_permissions ={
        'view_customer': True,
        'update_customer': True,
    }

class SystemAdmin(AbstractUserRole):
    available_permissions = {
        'view_customer': True,
    }