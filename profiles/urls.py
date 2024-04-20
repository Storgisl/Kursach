from django.urls import path
from django.contrib.auth.views import LoginView
from .import views

urlpatterns = [
        path('profiles/', views.profile, name='profile'),
        path('settings/', views.profile_settings, name='settings')
]