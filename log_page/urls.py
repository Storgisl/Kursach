from django.urls import path

from . import views

urlpatterns = [
    path('log_page/', views.reg_page, name="log_page"),
]