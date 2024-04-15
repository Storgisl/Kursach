from django.shortcuts import render

def base(request):
    return render(request, "main_page/index.html" and "main_page/base.html")