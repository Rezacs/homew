# Generated by Django 3.2.9 on 2021-11-16 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grups', '0005_auto_20211116_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secondary_group',
            name='groupp',
        ),
        migrations.DeleteModel(
            name='Grups',
        ),
        migrations.DeleteModel(
            name='Secondary_group',
        ),
    ]
