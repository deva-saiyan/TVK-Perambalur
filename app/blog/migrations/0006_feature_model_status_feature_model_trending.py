# Generated by Django 5.1.6 on 2025-02-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_slider_model_status_slider_model_trending'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature_model',
            name='status',
            field=models.BooleanField(default=False, help_text='0-show , 1-hidden'),
        ),
        migrations.AddField(
            model_name='feature_model',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-show , 1-hidden'),
        ),
    ]
