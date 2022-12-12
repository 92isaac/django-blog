from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('create_story/', views.create_story, name='create_story'),
    path('register', views.register, name='register'),
]