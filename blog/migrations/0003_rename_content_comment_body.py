# Generated by Django 3.2.25 on 2024-07-08 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20240708_1311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='body',
        ),
    ]
