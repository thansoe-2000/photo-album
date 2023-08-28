from django.urls import path
from . import views

urlpatterns = [
     path('login/', views.loginUser, name='login'),
     path('logout/', views.logoutUser, name='logout'),
     path('register/', views.registerUser, name='register'),

     path('', views.gallary, name= "gallary"),
     path('photo/<str:pk>/', views.viewPhoto, name= "photo"),
     path('check', views.check, name="check"),
     path('add/', views.addPhoto, name= "addPhoto"),
]