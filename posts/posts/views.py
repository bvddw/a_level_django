from django.db.models import Count
from django.http import HttpRequest, HttpResponse, Http404
from postsapp.models import Article, Comment, Topic, UserTopic
from postsapp.services import get_sorted_articles, get_sorted_topics
from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()


def main_page(request: HttpRequest) -> HttpResponse:
    ctx = {
        'articles_to_disp': Article.objects.all().order_by('author').annotate(number_of_comments=Count('comment')),
    }
    return render(request, 'index.html', ctx)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def archive(request: HttpRequest, year: str, month: str) -> HttpResponse:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    return HttpResponse(f'Archive. Year: {year}, month: {months[int(month) - 1]}.')
