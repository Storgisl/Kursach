from django.urls import path

from . import views

urlpatterns = [
    path('articles/', views.articales, name="articles"),
]