# Generated by Django 3.0.4 on 2024-09-26 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_candidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
