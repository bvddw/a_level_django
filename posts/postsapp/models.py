from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
UserModel = get_user_model()


class Topic(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title


class UserTopic(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    prefer = models.BooleanField(default=False)
    notify = models.BooleanField(default=False)


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(validators=[MinLengthValidator(255)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    topic = models.ManyToManyField(Topic)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
