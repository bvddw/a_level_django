from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from postsapp.models import Article, Comment, Topic
from django.urls import reverse


def article(request: HttpRequest, article_slug) -> HttpResponse:
    try:
        ctx = {
            'article': Article.objects.get(slug=article_slug),
        }
        return render(request, 'article_details.html', ctx)
    except Article.DoesNotExist:
        raise Http404('There no such article.')


def update_article(request: HttpRequest, article_slug) -> HttpResponse:
    try:
        cur_article = Article.objects.get(slug=article_slug)
        if request.user != cur_article.author:
            url = reverse('articles:no_access')
            return HttpResponseRedirect(url)
        # this part will be changed after forms are added, for now it's need for correct view for upd form on site
        topics = Topic.objects.all()
        topics_to_ctx = []
        for index, topic in enumerate(topics):
            cur_topic = {'option_value': index + 1, 'topic': topic}
            topics_to_ctx.append(cur_topic)
        ctx = {
            'article': cur_article,
            'topics_list': topics_to_ctx,
        }
        return render(request, 'upd_article.html', ctx)
    except Article.DoesNotExist:
        raise Http404('No articles with such title.')


def delete_article(request: HttpRequest, article_slug) -> HttpResponse:
    try:
        cur_article = Article.objects.get(slug=article_slug)
        if request.user != cur_article.author:
            url = reverse('articles:no_access')
            return HttpResponseRedirect(url)
        ctx = {'article': cur_article}
        return render(request, 'del_article.html', ctx)
    except Article.DoesNotExist:
        raise Http404('No articles with such title.')


def create_article(request: HttpRequest) -> HttpResponse:
    if not request.user.username:
        url = reverse('user:login_user')
        return HttpResponseRedirect(url)
    # this part will be changed after forms are added, for now it's need for correct view for upd form on site
    topics = Topic.objects.all()
    topics_to_ctx = []
    for index, topic in enumerate(topics):
        cur_topic = {'option_value': index + 1, 'topic': topic}
        topics_to_ctx.append(cur_topic)
    ctx = {
        'topics_list': topics_to_ctx,
    }
    return render(request, 'create_article.html', ctx)


def no_access(request):
    return render(request, 'no_access.html')