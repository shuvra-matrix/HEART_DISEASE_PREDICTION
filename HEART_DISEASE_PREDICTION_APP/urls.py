from django.contrib import admin
from django.urls import path
from . import views

app_name = "pre"

urlpatterns = [
    path('',views.index,name="index" ),
    path("heart/",views.heart_disease,name="heart"),
    path("heart2/",views.heart_prediction_2,name="heart2"),
]
