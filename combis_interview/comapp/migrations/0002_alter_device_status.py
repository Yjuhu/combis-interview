# Generated by Django 4.2.16 on 2024-11-23 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
