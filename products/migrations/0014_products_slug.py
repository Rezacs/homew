# Generated by Django 3.2.9 on 2021-12-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_products_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
