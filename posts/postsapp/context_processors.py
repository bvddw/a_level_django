from postsapp.models import Topic


def custom_context(request):
    return {'all_topics_to_display': Topic.objects.all()}
