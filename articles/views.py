import markdown
from django.shortcuts import render
from .models import Article
def articles_detail(request):
    md = markdown.Markdown(extensions=["fenced_code"])
    markdown_content = Article.objects.get(pk=1)
    markdown_content.content = md.convert(markdown_content.text)
    context = {"markdown_content": markdown_content}
    return render(request, 
                  template_name="articles/articles_detail.html",
                  context=context)

def articles(request):
        return render(request, 
                  template_name="articles/articles.html")