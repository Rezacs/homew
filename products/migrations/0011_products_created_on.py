# Generated by Django 3.2.9 on 2021-12-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]