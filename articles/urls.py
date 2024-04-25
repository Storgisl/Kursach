from django.urls import path

from . import views

urlpatterns = [
    
    path('articles_detail/', views.articles_detail, name="articles_detail"),
    path('', views.articles, name="articles"),
    
]#path('articles_detail/<int:id>/', views.articles_detail, name="articles_detail"),