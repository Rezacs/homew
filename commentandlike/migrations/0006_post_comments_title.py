# Generated by Django 3.2.9 on 2021-11-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentandlike', '0005_post_comment_likes_post_comment_reply_post_comments_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_comments',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
