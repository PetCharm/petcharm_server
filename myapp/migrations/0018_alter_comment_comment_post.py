# Generated by Django 3.2.9 on 2022-05-29 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_pet_pet_icon_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.post'),
        ),
    ]
