from django.urls import path
from . import views as user_views
from django.contrib.auth import views as my_views

urlpatterns = [
    path('', user_views.register, name='user'),
     path('login/', my_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', my_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile', user_views.profile, name='profile'),
]