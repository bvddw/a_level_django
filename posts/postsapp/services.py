from postsapp.models import Article, UserTopic
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def get_sorted_articles(user_id):
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        return None

    # take only preferred topics by current user
    preferred_topics = UserTopic.objects.filter(user=user).values_list('topic__title', flat=True)

    # take only articles, that connected to preferred topics
    articles = Article.objects.filter(topics__title__in=preferred_topics)
    # then take only their title for display
    articles_titles = [article.title for article in articles]

    return articles_titles
