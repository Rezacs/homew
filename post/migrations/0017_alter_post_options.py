# Generated by Django 3.2.9 on 2021-12-02 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_auto_20211201_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
