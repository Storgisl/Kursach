from django.urls import path

from .views import register

urlpatterns = [
    path('reg_page/', register, name="reg_page"),
]