# Generated by Django 3.2.9 on 2021-12-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grups', '0019_category_desc'),
        ('products', '0018_alter_shop_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='grups.Category'),
        ),
    ]
