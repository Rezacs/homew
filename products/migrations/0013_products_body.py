# Generated by Django 3.2.9 on 2021-12-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20211227_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
