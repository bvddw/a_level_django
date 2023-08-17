from django.db.models import Count
from django.http import HttpRequest, HttpResponse
from postsapp.models import Article, Comment, Topic, UserTopic
from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()


def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def archive(request: HttpRequest, year: str, month: str) -> HttpResponse:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    return HttpResponse(f'Archive. Year: {year}, month: {months[int(month) - 1]}.')
