# Generated by Django 4.2.17 on 2024-12-17 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='on_trial',
        ),
        migrations.RemoveField(
            model_name='school',
            name='paid_until',
        ),
    ]
