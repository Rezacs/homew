# Generated by Django 3.2.9 on 2021-12-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_customer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
