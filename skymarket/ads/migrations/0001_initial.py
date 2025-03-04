# Generated by Django 4.2.7 on 2023-11-30 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="название товара"),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="цена товара"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="описание товара"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время создания"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="ads/images",
                        verbose_name="изображение товара",
                    ),
                ),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="текст отзыва")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="дата и время"
                    ),
                ),
                (
                    "ad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ads.ad",
                        verbose_name="объявление",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
            },
        ),
    ]
