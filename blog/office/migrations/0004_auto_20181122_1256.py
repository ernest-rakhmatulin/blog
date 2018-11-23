# Generated by Django 2.1.2 on 2018-11-22 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_auto_20181122_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=15),
        ),
        migrations.AlterField(
            model_name='request',
            name='start_date',
            field=models.DateField(),
        ),
    ]
