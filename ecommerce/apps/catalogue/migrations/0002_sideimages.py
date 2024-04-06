# Generated by Django 5.0.2 on 2024-04-05 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(height_field='height', upload_to='side_images/', verbose_name='Image', width_field='width')),
                ('height', models.PositiveIntegerField(default=420, editable=False)),
                ('width', models.PositiveIntegerField(default=100, editable=False)),
            ],
            options={
                'verbose_name': 'Side Image',
                'verbose_name_plural': 'Side Images',
            },
        ),
    ]
