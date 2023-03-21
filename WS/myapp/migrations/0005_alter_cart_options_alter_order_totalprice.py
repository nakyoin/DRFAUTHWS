# Generated by Django 4.1.7 on 2023-03-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_product_options_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзина'},
        ),
        migrations.AlterField(
            model_name='order',
            name='totalprice',
            field=models.DecimalField(decimal_places=1, max_digits=100),
        ),
    ]
