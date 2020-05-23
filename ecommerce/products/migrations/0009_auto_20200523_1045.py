# Generated by Django 3.0.6 on 2020-05-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='category',
            field=models.CharField(choices=[('size', 'size'), ('color', 'color'), ('package', 'package')], default='size', max_length=120),
        ),
        migrations.AlterField(
            model_name='variation',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]