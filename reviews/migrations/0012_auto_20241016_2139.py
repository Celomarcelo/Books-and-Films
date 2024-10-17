# Generated by Django 3.2 on 2024-10-16 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_remove_category_category_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='category',
        ),
        migrations.AddField(
            model_name='genre',
            name='category',
            field=models.ManyToManyField(related_name='genres', to='reviews.Category'),
        ),
    ]