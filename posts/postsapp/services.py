from postsapp.models import Article, UserTopic
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def get_sorted_articles(user_id):
    """
    We will display a list of articles. All of them are preferred by user. Articles, that user want to see in
    notification has more priority, so first items in list - articles with field notify == True, then also preferred
    articles, but field notify == False.
    """
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        return None

    # take only preferred topics by current user with field notify == True
    notified_topics = UserTopic.objects.filter(user=user, notify=True).values_list('topic__title', flat=True)
    # take only articles, that connected to notified topics
    articles = Article.objects.filter(topics__title__in=notified_topics)
    # then take only their title for display
    articles_titles = [article.title for article in articles]

    # take only preferred topics by current user with field notify == False and append then to first part of articles
    preferred_topics = UserTopic.objects.filter(user=user, notify=False).values_list('topic__title', flat=True)
    # take only articles, that connected to preferred topics
    articles = Article.objects.filter(topics__title__in=preferred_topics)
    # then take only their title for display
    preferred_articles = [article.title for article in articles]

    for article_title in preferred_articles:
        if article_title not in articles_titles:
            articles_titles.append(article_title)

    return articles_titles
