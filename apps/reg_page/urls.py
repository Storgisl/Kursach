from django.urls import path

from . import views

urlpatterns = [
    path('reg_page/', views.reg_page, name="reg_page"),
]