# Generated by Django 4.1.7 on 2023-03-21 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_cart_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalprice',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
