# Generated by Django 5.1.7 on 2025-03-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_alter_room_facilities_alter_room_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='photo',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
