# Generated by Django 5.1.4 on 2025-01-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0007_alter_property_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
