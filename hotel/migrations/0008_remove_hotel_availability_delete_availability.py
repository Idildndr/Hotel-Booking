# Generated by Django 5.0.1 on 2024-01-14 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_availability_hotel_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='availability',
        ),
        migrations.DeleteModel(
            name='Availability',
        ),
    ]
