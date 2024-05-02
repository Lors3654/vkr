# Generated by Django 4.2.11 on 2024-04-18 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0004_productimage_remove_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='store_app.category', verbose_name='category'),
        ),
    ]