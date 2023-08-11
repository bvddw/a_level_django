from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from postsapp.models import Article, Comment, Topic


def article(request: HttpRequest, article_slug) -> HttpResponse:
    # display only article content, comments on page /article_title/comments
    try:
        ctx = {
            'article': Article.objects.get(slug=article_slug),
            'comments': Comment.objects.filter(article=Article.objects.get(slug=article_slug)),
            'topics': Topic.objects.all(),
        }
        return render(request, 'one_article.html', ctx)
    except Article.DoesNotExist:
        raise Http404('There no such article.')


def article_comment(request: HttpRequest, article_slug) -> HttpResponse:
    # display article + comment to it
    try:
        cur_article = Article.objects.get(slug=article_slug)
        comments = Comment.objects.filter(article=cur_article)
        comments_text = ''
        for index, comment in enumerate(comments):
            comments_text += str(index + 1) + ') ' + comment.author.username + ': ' + comment.message + '\n'
        if comments_text == '':
            comments_text = 'There no comments yet.'
        return HttpResponse(
            f'AUTHOR: {cur_article.author.username}\n\nTITLE: {cur_article.title}\n\nCONTENT: {cur_article.content}\n\nCOMMENTS:\n{comments_text}',
            content_type='text/plain')
    except Article.DoesNotExist:
        raise Http404('There no such article.')


def update_article(request: HttpRequest, article_slug) -> HttpResponse:
    try:
        cur_article = Article.objects.get(slug=article_slug)
        topics = Topic.objects.all()
        topics_to_ctx = []
        for index, topic in enumerate(topics):
            cur_topic = {'option_value': index + 1, 'topic': topic}
            topics_to_ctx.append(cur_topic)
        ctx = {
            'article': cur_article,
            'topics_list': topics_to_ctx,
            'topics': Topic.objects.all(),
        }
        return render(request, 'upd_article.html', ctx)
    except Article.DoesNotExist:
        raise Http404('No articles with such title.')


def delete_article(request: HttpRequest, article_slug) -> HttpResponse:
    try:
        cur_article = Article.objects.get(slug=article_slug)
        ctx = {'article': cur_article}
        return render(request, 'del_article.html', ctx)
    except Article.DoesNotExist:
        raise Http404('No articles with such title.')


def create_article(request: HttpRequest) -> HttpResponse:
    topics = Topic.objects.all()
    topics_to_ctx = []
    for index, topic in enumerate(topics):
        cur_topic = {'option_value': index + 1, 'topic': topic}
        topics_to_ctx.append(cur_topic)
    ctx = {
        'topics_list': topics_to_ctx,
        'topics': Topic.objects.all(),
    }
    return render(request, 'create_article.html', ctx)
