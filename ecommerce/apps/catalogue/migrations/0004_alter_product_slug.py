# Generated by Django 5.0.2 on 2024-04-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_remove_sideimages_height_remove_sideimages_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False, max_length=12, unique=True),
        ),
    ]