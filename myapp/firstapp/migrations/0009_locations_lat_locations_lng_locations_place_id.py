# Generated by Django 5.0.1 on 2024-02-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='lat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='lng',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='place_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
