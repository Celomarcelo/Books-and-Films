# Generated by Django 3.2 on 2024-12-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0023_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/default.jpg', upload_to='profile_images/'),
        ),
    ]