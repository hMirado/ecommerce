# Generated by Django 3.0.6 on 2020-05-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200520_1737'),
        ('carts', '0003_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Products'),
        ),
    ]
