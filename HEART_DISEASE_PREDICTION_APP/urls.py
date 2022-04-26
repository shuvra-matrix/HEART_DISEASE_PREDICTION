from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "pre"

urlpatterns = [
    path('',views.index,name="index" ),
    path("Heart Disease Prediction/",views.heart_disease,name="heart"),
    path("Heart Disease Prediction 2.0/",views.heart_prediction_2,name="heart2"),
    path("Heart Disease", views.about_heart,name="about" ),
    path("About Heart Disease", views.about1, name="about1"),
    path("Risk for Heart Disease", views.about2, name="about2"),
    path("Prevent Heart Disease", views.about3, name="about3"),
    path("Instruction", views.ins, name="ins"),
    path("About", views.about4, name="about4"),
    path('offline/', TemplateView.as_view(template_name="offline.html")),
]
