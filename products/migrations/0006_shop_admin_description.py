# Generated by Django 3.2.9 on 2021-12-23 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20211223_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='admin_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
