# Generated by Django 3.2.9 on 2022-05-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20220511_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]