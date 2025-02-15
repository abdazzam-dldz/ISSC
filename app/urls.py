from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('profile/', views.userProfile, name='profile'),
    path('teman-belajar/', views.temanBelajar, name='teman-belajar'),
    path('create-post/', views.createPost, name='create-post'),
]