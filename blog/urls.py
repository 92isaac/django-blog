from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('read_story/<str:pk>/', views.profile, name='read_story'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_blog_post/<str:pk>/', views.update_blog_post, name='update_blog_post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]