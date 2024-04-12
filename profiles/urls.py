from django.urls import path
from django.contrib.auth.views import LoginView
from .views import profile

urlpatterns = [
        path('profiles/', LoginView.as_view(template_name='profiles/profile.html'), name='profile')
]