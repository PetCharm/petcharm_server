# Generated by Django 3.2.9 on 2022-05-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_tracepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracepath',
            name='trace_path_coordinates_url',
        ),
        migrations.AddField(
            model_name='tracepath',
            name='trace_path_coordinates',
            field=models.TextField(blank=True, null=True),
        ),
    ]
