from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from profiles.forms import UserLoginForm

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['user'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "main_page/base.html")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLoginForm()
    return render(request, 'reg_log_page/login.html', {'form': form})