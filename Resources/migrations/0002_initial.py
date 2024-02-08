# Generated by Django 4.2.6 on 2024-02-08 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Resources', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resources.course'),
        ),
        migrations.AddField(
            model_name='prerequisites',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resources.course'),
        ),
        migrations.AddField(
            model_name='learning',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resources.course'),
        ),
        migrations.AlterUniqueTogether(
            name='usercourse',
            unique_together={('user', 'course')},
        ),
    ]
