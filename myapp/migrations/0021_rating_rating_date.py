# Generated by Django 3.2.9 on 2022-06-01 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_consultation_consultationreply'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rating_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
