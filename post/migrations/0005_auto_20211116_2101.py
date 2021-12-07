# Generated by Django 3.2.9 on 2021-11-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20211116_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='desc',
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
