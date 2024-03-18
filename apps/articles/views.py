from django.shortcuts import render

def articales(request):
    return render(request, "articles/index.html" and "articles/article_detail.html")