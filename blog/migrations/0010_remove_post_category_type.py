# Generated by Django 5.0.7 on 2024-07-26 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_type',
        ),
    ]