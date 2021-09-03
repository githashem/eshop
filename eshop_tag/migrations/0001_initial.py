# Generated by Django 3.2.3 on 2021-05-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_product', '0002_auto_20210527_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('slug', models.SlugField(blank=True, verbose_name='url')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/غیر فعال بودن')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('products', models.ManyToManyField(to='eshop_product.Product')),
            ],
        ),
    ]