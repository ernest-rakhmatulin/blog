# Generated by Django 2.1.2 on 2018-11-11 14:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20181111_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 11, 11, 14, 34, 44, 940540)),
        ),
    ]
