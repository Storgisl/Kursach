from django.shortcuts import render

# Create your views here.
def reg_page(request):
    return render(request, "reg_log_page/reg_page.html")