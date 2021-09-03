# Generated by Django 3.2.3 on 2021-09-03 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product', '0007_product_visit_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures/', verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_product.product', verbose_name='محصول')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductGallery',
        ),
    ]
