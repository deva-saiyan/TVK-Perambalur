# Generated by Django 5.1.6 on 2025-02-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_feature_model_status_feature_model_trending'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=10, verbose_name='Contact Number')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('place', models.CharField(max_length=20)),
                ('ward', models.CharField(choices=[('1st ward', '1st ward'), ('2nd ward', '2nd ward'), ('3rd ward', '3rd ward'), ('4th ward', '4th ward'), ('5th ward', '5th ward'), ('6th ward', '6th ward'), ('7th ward', '7th ward'), ('8th ward', '8th ward'), ('9th ward', '9th ward'), ('10th ward', '10th ward'), ('11th ward', '11th ward'), ('12th ward', '12th ward')], max_length=10)),
                ('address', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=700)),
            ],
        ),
    ]
