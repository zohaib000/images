from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
     path('', views.image,name="image"),
     path("searching",views.searching,name="searching"),
     path("joker",views.joker,name="joker"),
     path("pig",views.pig,name="pig"),
     path("birds",views.birds,name="birds"),
     path("lion",views.lion,name="lion"),
     path("tiger",views.tiger,name="tiger"),
     path("fifa",views.fifa,name="fifa"),
     path("poetry",views.poetry,name="poetry"),
     path("animals",views.animals,name="animals"),
     path("parrot",views.parrot,name="parrot"),
     path("dogs",views.dogs,name="dogs"),
     path("cats",views.cats,name="cats"),
]
