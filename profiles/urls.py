from django.urls import path
from django.contrib.auth.views import LoginView
from .views import profile

urlpatterns = [
        path('profiles/', profile, name='profile')
]