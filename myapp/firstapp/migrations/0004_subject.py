# Generated by Django 5.0.1 on 2024-01-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_todoitem_delete_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teacher_name', models.CharField(max_length=50)),
                ('units', models.IntegerField()),
            ],
        ),
    ]
