# Generated by Django 3.2.9 on 2021-11-18 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='street',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='zip',
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=150)),
                ('zip', models.CharField(max_length=150)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
