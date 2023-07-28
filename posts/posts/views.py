from django.http import HttpRequest, HttpResponse, Http404


def main_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Main page.')


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('About page.')


def profile(request: HttpRequest, username) -> HttpResponse:
    return HttpResponse(f"This is {username}'s profile page.")


def set_password(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page for changing user credentials.')


def set_userdata(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Page for changing user data.')


def deactivate(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Account deactivation page.')


def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Account creation page.')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Login page.')


def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Logout page.')


def article(request: HttpRequest, article) -> HttpResponse:
    return HttpResponse(f'This page about the article {article}.')


def article_comment(request: HttpRequest, article) -> HttpResponse:
    return HttpResponse(f'Here will be comments on the article {article}.')


def update_article(request: HttpRequest, article) -> HttpResponse:
    return HttpResponse(f'Here you will have a possibility to update article {article}.')


def delete_article(request: HttpRequest, article) -> HttpResponse:
    return HttpResponse(f'Here you will have a possibility to delete article {article}.')


def create_article(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Here will be a form for creating articles.')


def topics(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Here will be a list of available topics.')


def subscribe_topic(request: HttpRequest, topic) -> HttpResponse:
    return HttpResponse(f'A submission for subscribing to a topic {topic}.')


def unsubscribe_topic(request: HttpRequest, topic) -> HttpResponse:
    return HttpResponse(f'A submission for unsubscribing to a topic {topic}.')


def archive(request: HttpRequest, year: str, month: str) -> HttpResponse:
    if int(year) > 2023 or int(year) < 2020 or int(month) not in range(1, 13):
        raise Http404('No data about this data.')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return HttpResponse(f'Archive. Year: {year}, month: {months[int(month) - 1]}.')
