# Generated by Django 3.2.9 on 2022-05-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_application_application_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='application_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterModelTable(
            name='application',
            table='application',
        ),
    ]