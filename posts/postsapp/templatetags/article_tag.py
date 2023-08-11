from django import template
from ..models import Article

register = template.Library()

@register.simple_tag(name='get_articles')
def custom_article_tag():
    return Article.objects.all()

@register.inclusion_tag('list_articles.html')
def show_articles():
    articles = Article.objects.all()
    return {'articles': articles}