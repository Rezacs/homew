# Generated by Django 3.2.9 on 2021-11-20 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grups', '0009_category_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_on',
            field=models.DateTimeField(blank=True, default=None),
        ),
    ]
