# Generated by Django 4.2.2 on 2025-06-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_product_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["category", "name"],
                "permissions": [("can_unpublish_product", "Can unpublish product")],
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="publication_status",
            field=models.CharField(
                choices=[
                    ("published", "Опубликовать"),
                    ("unpublished", "На рассмотрении"),
                ],
                default="unpublished",
                max_length=15,
                verbose_name="Статус публикации",
            ),
        ),
    ]
