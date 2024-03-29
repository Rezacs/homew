# Generated by Django 3.2.9 on 2021-11-16 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211116_1955'),
        ('customer', '0001_initial'),
        ('basket', '0003_order2_order2item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('shippment', models.CharField(choices=[('pey', 'peyk_motori'), ('pos', 'post'), ('dgp', 'digikala_post')], max_length=3)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Basket2Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.basket2')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
        migrations.RenameModel(
            old_name='Email_response',
            new_name='Email_response2',
        ),
        migrations.RemoveField(
            model_name='order',
            name='baskets',
        ),
        migrations.RemoveField(
            model_name='order2item',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order2item',
            name='products',
        ),
        migrations.RenameField(
            model_name='order2',
            old_name='order_date',
            new_name='date_created',
        ),
        migrations.RemoveField(
            model_name='order2',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order2',
            name='order_num',
        ),
        migrations.RemoveField(
            model_name='order2',
            name='total_count',
        ),
        migrations.RemoveField(
            model_name='order2',
            name='total_price',
        ),
        migrations.AlterField(
            model_name='email_response2',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.order2'),
        ),
        migrations.DeleteModel(
            name='Basket',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Order2Item',
        ),
        migrations.AddField(
            model_name='order2',
            name='baskets',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='basket.basket2'),
        ),
    ]
