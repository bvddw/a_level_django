# Generated by Django 4.2.3 on 2023-08-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsapp', '0005_rename_topic_article_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
