# Generated by Django 4.2.4 on 2023-12-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stripe_product_price_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
