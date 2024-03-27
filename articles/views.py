from django.shortcuts import render

def articles(request):
    return render(request, "articles/article_detail.html")