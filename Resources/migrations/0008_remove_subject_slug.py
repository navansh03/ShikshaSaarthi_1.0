# Generated by Django 4.2.6 on 2024-02-09 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0007_subject_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='slug',
        ),
    ]
