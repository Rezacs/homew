# Generated by Django 3.2.9 on 2021-11-20 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grups', '0015_category_created_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created_on']},
        ),
    ]
