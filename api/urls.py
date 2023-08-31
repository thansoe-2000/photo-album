from django.urls import path
from . import views


urlpatterns = [
    path('api', views.getPhoto, name="get-photos"),
]
