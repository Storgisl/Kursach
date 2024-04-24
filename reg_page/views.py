from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from profiles.forms import UserRegisterForm

def register(request):
    if request.method == 'GET':
        user_form = UserRegisterForm()
        return render(request, 
                      template_name='reg_log_page/registration.html', 
                      context={'user_form': user_form})
    
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            print(user_form.is_valid())
            user_form.save()
            return redirect("base")
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 
                          template_name='reg_log_page/registration.html', 
                          context={'user_form': user_form})