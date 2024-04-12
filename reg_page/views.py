from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Import User UpdateForm, ProfileUpdateForm
from profiles.forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'reg_log_page/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'reg_log_page/registertration.html', {'user_form': user_form})