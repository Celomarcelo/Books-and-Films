# Generated by Django 3.2 on 2024-09-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='reviews/'),
        ),
    ]
