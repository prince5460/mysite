from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogArticle


def blog_title(request):
    querySet = request.GET.get('tag')
    if querySet:
        blogs = BlogArticle.objects.filter(tag=querySet)
    else:
        blogs = BlogArticle.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/titles.html', context)


def blog_article(request, article_id):
    # article = BlogArticle.objects.get(id=article_id)
    article = get_object_or_404(BlogArticle, id=article_id)
    pub = article.publish
    context = {'article': article, 'publish': pub}
    return render(request, 'blog/articles.html', context)
