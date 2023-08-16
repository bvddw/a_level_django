from django import template
from django.db.models import Count
from postsapp.services import get_sorted_articles
from ..models import Article, Topic

register = template.Library()


@register.simple_tag(name='get_articles')
def custom_article_tag():
    return Article.objects.all()


@register.inclusion_tag('list_articles.html')
def show_articles():
    articles = Article.objects.all().order_by('created_at').annotate(number_of_comments=Count('comment'))
    context = {
        'articles': articles,
    }
    return context