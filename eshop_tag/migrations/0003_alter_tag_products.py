# Generated by Django 3.2.3 on 2021-05-27 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product', '0002_auto_20210527_1623'),
        ('eshop_tag', '0002_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='products',
            field=models.ManyToManyField(blank=True, to='eshop_product.Product'),
        ),
    ]
