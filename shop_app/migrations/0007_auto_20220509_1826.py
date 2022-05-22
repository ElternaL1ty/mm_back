# Generated by Django 3.2.13 on 2022-05-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0006_auto_20220427_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='shop_app.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/default.png', upload_to='media/'),
        ),
    ]
