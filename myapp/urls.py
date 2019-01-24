from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    url(r'change_password', views.change_password, name='change_password'),
    url('index', views.index, name='index'),
    url('dashboard/', views.dashboard, name='dashboard'),
    url('show_user/', views.show_user, name='show_user'),
    url('show_role/', views.show_role, name='show_role'),
    url('show_permission/', views.show_permission, name='show_permission'),
    url('show_role_to_user/', views.show_role_to_user, name='show_role_to_user'),
    url('show_permission_to_role', views.show_permission_to_role, name='show_permission_to_role'),
    url('add_user/', views.add_user, name='add_user'),
    url('add_role/', views.add_role, name='add_role'),
    url('add_permission/', views.add_permission, name='add_permission'),
    url('add_role_to_user/', views.add_role_to_user, name='add_role_to_user'),
    url('add_permission_to_role', views.add_permission_to_role, name='add_permission_to_role'),
    path('<int:id>/update_user', views.update_user, name='update_user'),
    #path('update_user', views.update_user, name='update_user'),
    path(r'<int:id>/update_role/', views.update_role, name='update_role'),
    path('<int:id>/update_permission/', views.update_permission, name='update_permission'),
    path('<int:id>/update_role_to_user/', views.update_role_to_user, name='update_role_to_user'),
    path('<int:id>/update_permission_to_role', views.update_permission_to_role, name='update_permission_to_role'),
    path('<int:id>/delete_user/', views.delete_user, name='delete_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('<int:id>/delete_role/', views.delete_role, name='delete_role'),
    path('<int:id>delete_permission/', views.delete_permission, name='delete_permission'),
    path('<int:id>/delete_role_to_user/', views.delete_role_to_user, name='delete_role_to_user'),
    path('<int:id>/delete_permission_to_role', views.delete_permission_to_role, name='delete_permission_to_role'),
    url(r'logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    url(r'', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),

   #path('hello',views.Hello.as_view()),
]
