# Generated by Django 3.2 on 2024-11-25 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0017_rename_text_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_img/default.jpg', upload_to='profile_images/'),
        ),
    ]
