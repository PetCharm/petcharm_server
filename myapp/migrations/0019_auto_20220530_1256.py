# Generated by Django 3.2.9 on 2022-05-30 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_comment_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_date_of_birth',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.pet'),
        ),
    ]