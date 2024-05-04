import markdown
from django.shortcuts import render
from .models import Article
def articles_detail(request, id):
    article = Article.objects.get(pk=id)
    md = markdown.Markdown(extensions=["fenced_code"])
    markdown_content = md.convert(article.text)
    context = {"markdown_content": markdown_content, "article": article}
    return render(request, 
                  template_name="articles/articles_detail.html",
                  context=context)

def articles(request):
        articles = Article.objects.all()
        context = {"articles": articles}
        return render(request, 
                  template_name="articles/articles.html",
                  context=context)