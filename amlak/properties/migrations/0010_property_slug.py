# Generated by Django 5.1.4 on 2025-01-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_remove_property_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
