# Generated by Django 3.0.6 on 2020-05-22 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200520_1737'),
        ('carts', '0010_auto_20200522_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Products'),
        ),
    ]
