from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('registration/', LoginView.as_view(template_name='reg_log_page/registration.html'), name="registration"),
]