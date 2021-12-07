# Generated by Django 3.2.9 on 2021-11-16 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grups', '0004_category'),
        ('products', '0003_products_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='secondary_group',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='grups.category'),
        ),
    ]
