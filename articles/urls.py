from django.urls import path

from . import views

urlpatterns = [
    
    path('articles_detail/<int:id>/', views.articles_detail, name='articles_detail'),
    path('articles/', views.articles, name="articles"),
    
]