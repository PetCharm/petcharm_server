# Generated by Django 3.2.9 on 2022-06-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_rating_rating_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_keywords',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_senti',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]