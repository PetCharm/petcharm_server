# Generated by Django 3.2.9 on 2022-05-05 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20220504_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
