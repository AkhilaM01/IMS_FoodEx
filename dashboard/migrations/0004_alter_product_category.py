# Generated by Django 4.2.7 on 2023-12-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0003_alter_order_options_alter_product_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("Beverages", "Beverages"),
                    ("Vegetables", "Vegetables"),
                    ("Spices", "Spices"),
                    ("Fruits", "Fruits"),
                    ("Snacks", "Snacks"),
                    ("Grain", "Grain"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
