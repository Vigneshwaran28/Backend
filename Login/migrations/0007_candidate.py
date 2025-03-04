# Generated by Django 3.0.4 on 2024-09-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_auto_20240920_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qualification', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=255)),
                ('dob', models.DateField(max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('yearOfExp', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
    ]
