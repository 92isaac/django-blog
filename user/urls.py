from django.urls import path
from . import views as user_views


urlpatterns = [
    path('', user_views.register, name='user'),
    path('/profile', user_views.profile, name='profile'),
]