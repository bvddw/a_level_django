from postsapp.models import Article, UserTopic
from django.contrib.auth import get_user_model
from django.db.models import Count, Q

UserModel = get_user_model()


def get_sorted_articles(user_id):
    """
    We will display a list of articles. If user has preferred articles, we will show relevant articles to them. If
    no, will show just 3 random articles. The more the article has topics that the user prefers, the more preferable
    it is for him, so ordering by amount preferred topics in article.
    """
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        return None

    # take only preferred topics by current user
    preferred_topics = UserTopic.objects.filter(user=user).values_list('topic__title', flat=True)
    # take only articles, that connected to preferred topics
    articles_titles = Article.objects.all().annotate(number_of_topics=Count('topics', filter=Q(topics__title__in=preferred_topics)))
    # let's display only three first relevant topics for each user. Even if user has not preferred topics, we will show
    # just 3 different articles, for his/her attention.
    articles_titles = articles_titles.order_by('number_of_topics').values_list('title', flat=True)[:3]
    return articles_titles
