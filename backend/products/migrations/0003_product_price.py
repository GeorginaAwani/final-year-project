# Generated by Django 4.1.7 on 2023-02-21 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_images_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
            preserve_default=False,
        ),
    ]