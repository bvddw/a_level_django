from django.http import HttpRequest, HttpResponse, Http404
from postsapp.models import Article, Comment, Topic, UserTopic
from postsapp.services import get_sorted_articles, get_sorted_topics
from django.contrib.auth import get_user_model
from django.shortcuts import render

UserModel = get_user_model()


def profile(request: HttpRequest, username) -> HttpResponse:
    try:
        cur_user = UserModel.objects.get(username=username)
        articles = Article.objects.filter(author=cur_user)
        articles_on_preferred_topics = get_sorted_articles(cur_user.id)
        sorted_topics = get_sorted_topics(cur_user)

        ctx = {
            'user': cur_user,
            'users_articles': articles,
            'recommendation': articles_on_preferred_topics,
            'ordered_topics': sorted_topics,
        }

        return render(request, 'user_profile_page.html', ctx)
    except UserModel.DoesNotExist:
        raise Http404('There is no such user.')


def set_password(request: HttpRequest, username) -> HttpResponse:
    try:
        user = UserModel.objects.get(username=username)
        ctx = {'user': user}
        return render(request, 'set_password.html', ctx)
    except UserModel.DoesNotExist:
        raise Http404('User with this password does not exist.')


def set_userdata(request: HttpRequest, username) -> HttpResponse:
    try:
        user = UserModel.objects.get(username=username)
        ctx = {'user': user}
        return render(request, 'set_data.html', ctx)
    except UserModel.DoesNotExist:
        raise Http404('User with this password does not exist.')


def deactivate(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Account deactivation page.')


def register(request: HttpRequest) -> HttpResponse:
    return render(request, 'register.html')


def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')


def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Logout page.')
