# Generated by Django 4.2.7 on 2023-11-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='products', verbose_name='Изображение'),
        ),
    ]
