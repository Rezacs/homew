# Generated by Django 3.2.9 on 2021-12-12 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='theme',
            field=models.CharField(blank=True, choices=[('gre', 'green'), ('pur', 'purpule'), ('red', 'red'), ('blu', 'blue')], max_length=3, null=True),
        ),
    ]
