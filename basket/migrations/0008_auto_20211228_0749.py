# Generated by Django 3.2.9 on 2021-12-28 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_shop_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basket', '0007_basket2_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('live', 'live_basket_now'), ('past', 'payed and cheked'), ('done', 'finished basket')], max_length=4)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('Basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.CreateModel(
            name='Email_response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, help_text='Enter a description for your selected prod.')),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
                ('seller_response', models.CharField(max_length=300)),
                ('buyer_response', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, help_text='Enter a description for your selected prod.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('shipping_date', models.DateTimeField()),
                ('shippment', models.CharField(choices=[('pey', 'peyk_motori'), ('pos', 'post'), ('dgp', 'digikala_post')], max_length=3)),
                ('basket', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='basket.basket')),
            ],
        ),
        migrations.RemoveField(
            model_name='basket2item',
            name='Basket',
        ),
        migrations.RemoveField(
            model_name='basket2item',
            name='product',
        ),
        migrations.RemoveField(
            model_name='email_response2',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order2',
            name='baskets',
        ),
        migrations.DeleteModel(
            name='Basket2',
        ),
        migrations.DeleteModel(
            name='Basket2Item',
        ),
        migrations.DeleteModel(
            name='Email_response2',
        ),
        migrations.DeleteModel(
            name='Order2',
        ),
        migrations.AddField(
            model_name='email_response',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.order'),
        ),
    ]