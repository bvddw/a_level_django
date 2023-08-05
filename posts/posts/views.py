from django.http import HttpRequest, HttpResponse, Http404
from postsapp.models import Article, Comment, Topic
from postsapp.services import get_sorted_articles
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def main_page(request: HttpRequest) -> HttpResponse:
    articles = Article.objects.all()
    articles_title = '\n'.join(cur_article.title for cur_article in articles)
    return HttpResponse(articles_title, content_type='text/plain')


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('About page.')


def profile(request: HttpRequest, username) -> HttpResponse:
    try:
        cur_user = UserModel.objects.get(username=username)
        user_data = cur_user.username
        articles = Article.objects.filter(author=cur_user)
        articles_to_display = '\n'.join([f'{index + 1}) {article.title}' for index, article in enumerate(articles)])

        if not articles_to_display:
            articles_to_display = 'This user has not published any articles.'

        preferred_topics = get_sorted_articles(cur_user.id)
        preferred_topics_str = ', '.join(preferred_topics) if preferred_topics else 'No preferred topics'

        response_text = f"User data: {user_data}\n\nUser's articles:\n{articles_to_display}\n\nArticles on preferred topics: {preferred_topics_str}."
        return HttpResponse(response_text, content_type='text/plain')
    except UserModel.DoesNotExist:
        raise Http404('There is no such user.')


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
    try:
        cur_article = Article.objects.get(title=article)
        comments = Comment.objects.filter(article=cur_article)
        comments_text = ''
        for index, comment in enumerate(comments):
            comments_text += str(index + 1) + ') ' + comment.message + '\n'
        if comments_text == '':
            comments_text = 'There no comments yet.'
        return HttpResponse(f'TITLE: {cur_article.title}\n\nCONTENT: {cur_article.content}\n\nCOMMENTS:\n{comments_text}', content_type='text/plain')
    except Article.DoesNotExist:
        raise Http404('There no such article.')
    except Article.MultipleObjectsReturned:
        raise Http404('There two or more articles with such title.')


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
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return HttpResponse(f'Archive. Year: {year}, month: {months[int(month) - 1]}.')
