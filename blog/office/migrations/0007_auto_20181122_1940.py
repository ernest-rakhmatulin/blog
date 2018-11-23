# Generated by Django 2.1.2 on 2018-11-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0006_request_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_type',
            field=models.CharField(choices=[('Vacation', 'Vacation'), ('Sick Leave', 'Sick Leave'), ('Compensatory Holiday', 'Compensatory Holiday'), ('Business Trip', 'Business Trip')], max_length=30),
        ),
    ]
