# Generated by Django 3.0.6 on 2020-05-22 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200520_1737'),
        ('carts', '0005_auto_20200522_1649'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItems',
            new_name='CartItem',
        ),
    ]
