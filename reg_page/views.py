from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Import User UpdateForm, ProfileUpdateForm
from profiles.forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'GET':
        user_form = UserRegisterForm()
        return render(request, 
                      template_name='reg_log_page/registration.html', 
                      context={'user_form': user_form})
    
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            #messages.success(request, 'You have singed up successfully.')
            # Save the User object
            new_user.save()
            return redirect("base")
        else:
            return render(request, 
                          template_name='reg_log_page/registration.html', 
                          context={'user_form': user_form})