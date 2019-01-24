from django.shortcuts import render
from rolepermissions.checkers import has_role,has_object_permission
from rollpermission.roles import *
from rolepermissions.roles import get_user_roles
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from django.http import HttpResponse
from .myform import *
from .models import *
from .role import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views import View

'''class Hello(View):
    hi = "hi"
    def get(self,request):
        return HttpResponse(self.hi)'''
# Create your views here.

def index(request):
    return render (request,"myapp/index4.html")
@login_required
def dashboard(request):
    users=request.user
    #role = Roles.objects.get(pk=1)
    #print(role.name)

    userrole = UserRoles.objects.filter(user=users)
    print(userrole)
    print(f'user is {users}')


    if users.is_superuser:
        return render(request,'myapp/base.html')
    #elif role_to_user.role.name == 'Employee':
        #HttpResponse("<h1>You are employee</h1>")



        #user=User.objects.get(name=users)
        #role_to_user = UserRoles.objects.get(user=users)
        #print(role_to_user.user)
        #print(role_to_user.role)

        #role = get_role(users)
        #print(role)
    elif users in  userrole:
            #print(role)
        return HttpResponse("You are employee")
    else:
        return HttpResponse("<h1>You are not Superuser</h1>")

    '''if has_role(user,Customer):
        print(f'role is {get_user_roles(user)}')
        return HttpResponse("<h1>You are customer</h1>")
    elif has_role(user,Employee):
        return HttpResponse("<h1>You are admin employee</h1>")


    else:
        return HttpResponse("<h1>No Permission</h1>")'''




@login_required
def add_user(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username=form.cleaned_data.get('username')
           # print("user",username)

            #messages.success(request,f'Account Created for {username}')
            return redirect('myapp/base.html')

    else:
        form = UserRegisterForm()
    return render(request,'myapp/user_register.html',{'form':form})

@login_required
def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            # username=form.cleaned_data.get('username')
            # print("user",username)

            # messages.success(request,f'Account Created for {username}')
            return redirect('myapp/base.html')
    else:
        form = RoleForm()
    return render(request, 'myapp/add_role.html', {'form': form})


@login_required
def add_permission(request):
    if request.method == 'POST':
        form=PermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp/base.html')
    else:
        form = PermissionForm()
    return render(request,'myapp/add_permission.html',{'form':form})


@login_required
def add_role_to_user(request):
    if request.method == 'POST':
        form=UserRoleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp/base.html')
    else:
        form = UserRoleForm()
    return render(request,'myapp/user_role.html',{'form':form})


@login_required
def add_permission_to_role(request):
    if request.method == 'POST':
        form = RolePermissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp/base.html')
    else:
        form =RolePermissionForm()
    return render(request,'myapp/role_permission.html',{'form':form})


@login_required
def show_user(request):
    user = get_list_or_404(User)
    return render (request, 'myapp/show_user.html',{'user':user})


@login_required
def show_role(request):
    role = get_list_or_404(Roles.objects.exclude(status='D'))

    return render(request, 'myapp/show_role.html', {'role': role})


@login_required
def show_permission(request):
    perm = get_list_or_404(Permissions.objects.exclude(status='D'))
    return render(request, "myapp/show_permission.html",{'perm':perm})


@login_required
def show_role_to_user(request):
    role_to_user = get_list_or_404(UserRoles.objects.exclude(status='D'))
    return render(request,"myapp/show_role_to_user.html",{'role_to_user':role_to_user})


@login_required
def show_permission_to_role(request):
    permission_to_role = get_list_or_404(PermissionsRoles.objects.exclude(status='D'))
    return render(request,'myapp/show_permission_to_role.html',{'permission_to_role':permission_to_role})


@login_required
def update_user(request,id):
    instance = get_object_or_404(User, id=id)
    form = UserRegisterForm(request.POST, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        obj = User.objects.latest('id')
        obj.status = 'U'
        obj.save()
        #messages.success(request, f'Record for { obj.name} successfully Updated.')
        return redirect('dashboard')
        # return redirect('showcustomerprofile')

    context = {

        'form': form,
    }
    return render(request, "myapp/user_register.html", context)


@login_required
def update_role(request,id):
    instance = get_object_or_404(Roles, id=id)
    form = RoleForm(request.POST, instance=instance)
    context = {
        'form': form
        }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        obj = Roles.objects.latest('id')
        obj.status = 'U'
        obj.save()
        # messages.success(request, f'Record for { obj.name} successfully Updated.')
        return redirect('dashboard')
        # return redirect('showcustomerprofile')
    context = {

        'form': form,
    }
    return render(request, "myapp/add_role.html", context)


@login_required
def update_permission(request,id):
    instance = get_object_or_404(Permissions, id=id)
    form = PermissionForm(request.POST, instance = instance)
    context ={
        'form':form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        obj = Permissions.objects.latest('id')
        obj.status = 'U'
        obj.save()
    context = {

        'form': form,
    }
    return render(request, 'myapp/add_permission.html',context)


@login_required
def update_role_to_user(request, id):
    instance = get_object_or_404(UserRoles, id =id )
    form = UserRoleForm(request.POST, instance=instance)
    context = {
        'form': form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        obj = UserRoles.objects.latest('id')
        obj.status = 'U'
        obj.save()
    return render(request, 'myapp/user_role.html', context)


@login_required
def update_permission_to_role(request, id):
    instance = get_object_or_404(UserRoles, id = id)
    form = RolePermissionForm(request.POST, instance=instance)
    context = {
        'form': form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        obj =PermissionsRoles.objects.latest('id')
        obj.status = 'U'
        obj.save()
    return render(request, 'myapp/role_permission.html', context)


@login_required
def delete_user(request,id):
    instance = get_object_or_404(User, id=id)
    instance.status='D'
    instance.save()
    #messages.success(request, f'Record for { instance.name} successfully Deleted.')
    return redirect('dashboard')


@login_required
def delete_role(request,id):
    instance = get_object_or_404(Roles, id=id)
    instance.status='D'
    instance.save()
    #messages.success(request, f'Record for { instance.name} successfully Deleted.')
    return redirect('dashboard')


@login_required
def delete_permission(request,id):
    instance = get_object_or_404(Permissions, id=id)
    instance.status='D'
    instance.save()
    #messages.success(request, f'Record for { instance.name} successfully Deleted.')
    return redirect('dashboard')


@login_required
def delete_role_to_user(request,id):
    instance = get_object_or_404(UserRoles, id=id)
    instance.status='D'
    instance.save()
    #messages.success(request, f'Record for { instance.name} successfully Deleted.')
    return redirect('dashboard')


@login_required
def delete_permission_to_role(request,id):
    instance = get_object_or_404(PermissionsRoles, id=id)
    instance.status='D'
    instance.save()
    #messages.success(request, f'Record for { instance.name} successfully Deleted.')
    return redirect('dashboard')


@login_required
def update_permission_to_role(request, id):
    instance = get_object_or_404(PermissionsRoles,id= id)
    form = RolePermissionForm(request.POST, instance = instance)
    context ={
        'form':form,
    }

    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        obj = UserRoles.objects.latest('id')
        obj.status = 'U'
        obj.save()
    return render(request, 'myapp/user_role.html',context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)

        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
        context ={
            'form':form,
        }
    return render(request,"myapp/change_password.html",context)
    #return render(request,'myapp/user_register.html',{'form':form}






