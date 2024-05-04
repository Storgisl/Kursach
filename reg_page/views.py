from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from profiles.forms import UserRegisterForm, ProfileRegisterForm
from profiles.models import Profile

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        print(user_form.errors)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = Profile(user=user)
            profile.save()  
            messages.success(request, 'You have been registered successfully')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
    return render(request, 'reg_log_page/registration.html', {'user_form': user_form})