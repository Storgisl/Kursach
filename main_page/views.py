from django.shortcuts import render

def base(request):
    return render(request, "main_page/base.html")

def index(request):
    return render(request,  "main_page/index.html")