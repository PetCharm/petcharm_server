# Generated by Django 3.2.9 on 2022-05-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_application_application_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_valid',
            field=models.BooleanField(default=False),
        ),
    ]