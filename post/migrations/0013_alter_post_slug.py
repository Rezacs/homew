# Generated by Django 3.2.9 on 2021-11-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
