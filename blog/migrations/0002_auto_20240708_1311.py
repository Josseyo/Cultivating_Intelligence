# Generated by Django 3.2.25 on 2024-07-08 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='content',
        ),
    ]