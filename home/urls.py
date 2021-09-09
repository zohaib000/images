from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.image,name="image"),
    path("searching",views.searching,name="searching"),
    path("joker",views.joker,name="joker")
]
