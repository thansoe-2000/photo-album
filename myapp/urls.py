from django.urls import path
from . import views

urlpatterns = [
     path('', views.loginUser, name='login'),
     path('logout/', views.logoutUser, name='logout'),
     path('register/', views.registerUser, name='register'),

     path('gallary/', views.gallary, name= "gallary"),
     path('photo/<str:pk>/', views.viewPhoto, name= "photo"),
     path('check', views.check, name="check"),
     path('add/', views.addPhoto, name= "addPhoto"),
     path('category/', views.addCategory, name= "addCategory"),
]