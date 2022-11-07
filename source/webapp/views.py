from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from webapp.models import Article, STATUS


def index_views(request):
    articles = Article.objects.order_by('-created_at')
    context = {
        'articles': articles
    }
    return render(request, "index.html", context)


def article_view(request):
    article_id = request.GET.get('id')
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    return render(request, 'article_view.html', context)


def article_create_view(request):
    if request.method == "GET":
        return render(request, "article_create.html", {'statuses': STATUS})
    elif request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        # author = request.POST.get('author')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        new_article = Article.objects.create(content=content,  status=status, deadline=deadline)
        context = {'article': new_article}
        return render(request, 'article_view.html', context)
