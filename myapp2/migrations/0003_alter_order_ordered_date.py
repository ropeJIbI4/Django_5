# Generated by Django 5.0.4 on 2024-04-29 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0002_remove_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(),
        ),
    ]
