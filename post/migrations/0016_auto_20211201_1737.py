# Generated by Django 3.2.9 on 2021-12-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0015_post_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location_lat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='location_lng',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
    ]
