from django.contrib import admin

# Register your models here.
from myapp import models

admin.site.register(models.User)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Pet)
admin.site.register(models.Hospital)
admin.site.register(models.Rating)
admin.site.register(models.Star)
admin.site.register(models.VetHospital)
admin.site.register(models.WalkPoint)
