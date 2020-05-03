from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name="modsy"

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('rooms/', views.project1, name='project1'),
    path('goals/', views.project2, name='project2'),
    path('furniture/', views.project3, name='project3'),
    path('styles/', views.project4, name='project4'),
    path('register/', views.home, name='home'),
    path('user_register/', views.user_register, name='user_register'),
    path('login/', views.login_view,name='login'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('account', views.account,name='account'),
    path('logout/', views.logout,name='logout'),
    path('account/edit/',views.edit_profile,name="edit_profile"),
    path('account/password/',views.change_password,name='change_password'),
    path('account/resetpassword/',views.reset_password,name='reset_password'),
    path('users/', views.UserListView.as_view(), name='user_list'),





]