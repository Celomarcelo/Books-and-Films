# Generated by Django 3.2 on 2024-12-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0027_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default_vbaelo.jpg', upload_to='profile_images/'),
        ),
    ]
