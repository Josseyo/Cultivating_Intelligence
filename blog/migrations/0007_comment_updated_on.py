# Generated by Django 5.0.7 on 2024-07-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20240713_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
