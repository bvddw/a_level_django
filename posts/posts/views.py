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
        'topics': Topic.objects.all(),
    }
    return render(request, 'index.html', ctx)


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


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
            'topics': Topic.objects.all(),
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


def one_topic(request: HttpRequest, topic_title: str):
    try:
        ctx = {
            'topic': Topic.objects.get(title=topic_title),
            'topics': Topic.objects.all(),
            'articles': Article.objects.filter(topics=Topic.objects.get(title=topic_title))
        }
        return render(request, 'one_topic.html', ctx)
    except Topic.DoesNotExist:
        raise Http404('Topic with this title does not exist.')


def subscribe_topic(request: HttpRequest, topic_title) -> HttpResponse:
    try:
        cur_topic = Topic.objects.get(title=topic_title)
        ctx = {'topic': cur_topic}
        return render(request, 'sub_topic.html', ctx)
    except Topic.DoesNotExist:
        raise Http404('No topics with such title.')


def unsubscribe_topic(request: HttpRequest, topic_title) -> HttpResponse:
    try:
        cur_topic = Topic.objects.get(title=topic_title)
        ctx = {'topic': cur_topic}
        return render(request, 'unsub_topic.html', ctx)
    except Topic.DoesNotExist:
        raise Http404('No topics with such title.')


def archive(request: HttpRequest, year: str, month: str) -> HttpResponse:
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    return HttpResponse(f'Archive. Year: {year}, month: {months[int(month) - 1]}.')
