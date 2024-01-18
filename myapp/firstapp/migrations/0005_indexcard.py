# Generated by Django 5.0.1 on 2024-01-17 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=5)),
                ('age', models.IntegerField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='firstapp.subject')),
            ],
        ),
    ]
