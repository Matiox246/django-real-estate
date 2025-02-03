# Generated by Django 5.1.5 on 2025-01-23 23:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=100)),
                ("message", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Message",
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
                ("content", models.TextField()),
                ("is_read", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Property",
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
                ("title", models.CharField(max_length=100, verbose_name="عنوان")),
                ("location", models.CharField(max_length=150, verbose_name="آدرس")),
                ("built_year", models.IntegerField(null=True, verbose_name="سال ساخت")),
                (
                    "type",
                    models.CharField(
                        choices=[("آپارتمان", "Apartment"), ("خانه", "House")],
                        default="آپارتمان",
                        max_length=50,
                        verbose_name="نوع",
                    ),
                ),
                ("status", models.CharField(max_length=100, verbose_name="وضعیت")),
                ("bedroom", models.IntegerField(verbose_name="اتاق خواب")),
                ("bathroom", models.IntegerField(verbose_name="دستشویی")),
                ("description", models.TextField(null=True, verbose_name="توضیحات")),
                ("price", models.IntegerField(verbose_name="قیمت")),
                (
                    "post_date",
                    models.DateTimeField(null=True, verbose_name="تاریخ پست"),
                ),
                ("floors", models.IntegerField(null=True, verbose_name="تعداد طبقات")),
                ("parking", models.BooleanField(null=True, verbose_name="پارکینگ")),
                ("lot_area", models.IntegerField(verbose_name="متراژ کل")),
                (
                    "floor_area",
                    models.IntegerField(null=True, verbose_name="متراژ سازه"),
                ),
                (
                    "elevator",
                    models.BooleanField(
                        default=False, null=True, verbose_name="آسانسور"
                    ),
                ),
                (
                    "warehouse",
                    models.BooleanField(
                        default=False, null=True, verbose_name="انباری"
                    ),
                ),
                (
                    "is_approved",
                    models.BooleanField(default=False, verbose_name="وضعیت تایید"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="properties.category",
                        verbose_name="دسته بندی",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کاربر",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="property/")),
                (
                    "property",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="images",
                        to="properties.property",
                    ),
                ),
            ],
        ),
    ]
