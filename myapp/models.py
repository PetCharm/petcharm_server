# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser
from django.db import models


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_content = models.CharField(max_length=500, blank=True, null=True)
    comment_post = models.ForeignKey('Post', models.DO_NOTHING, blank=True, null=True)
    comment_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'comment'


class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'hospital'


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_display_name = models.CharField(max_length=100, blank=True, null=True)
    pet_type = models.CharField(max_length=100, blank=True, null=True)
    pet_breed = models.CharField(max_length=100, blank=True, null=True)
    pet_gender = models.CharField(max_length=100, blank=True, null=True)
    pet_date_of_birth = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'pet'


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_content = models.CharField(max_length=500, blank=True, null=True)
    post_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'post'


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rating_content = models.CharField(max_length=200, blank=True, null=True)
    rating_score = models.IntegerField(blank=True, null=True)
    rating_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='rating_1')
    rating_by_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='rating_2')

    class Meta:
        db_table = 'rating'


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100, blank=True, null=True)
    service_content = models.CharField(max_length=500, blank=True, null=True)
    service_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    service_type = models.CharField(max_length=100, blank=True, null=True)
    service_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'service'


class Star(models.Model):
    star_id = models.AutoField(primary_key=True)
    star_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='star_1')
    star_by_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='star_2')

    class Meta:
        db_table = 'star'


class User(AbstractUser):
    user_type = models.CharField(max_length=100, blank=True, null=True)
    pet = models.ForeignKey(Pet, models.DO_NOTHING, blank=True, null=True)
    user_icon_url = models.CharField(max_length=200, blank=True, null=True)
    user_phone_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'user'


class VetHospital(models.Model):
    vet_hospital_id = models.IntegerField(blank=True, null=True)
    vet = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'vet_hospital'
        unique_together = (('vet', 'hospital'),)


class WalkPoint(models.Model):
    walk_point_id = models.AutoField(primary_key=True)
    walk_point_x = models.FloatField(blank=True, null=True)
    walk_point_y = models.FloatField(blank=True, null=True)
    walk_point_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'walk_point'
