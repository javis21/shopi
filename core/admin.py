from django.contrib import admin

# Register your models here.
from . import models

# admin.site.register(models.Location)
admin.site.register(models.Place)

admin.site.register(models.Category)
admin.site.register(models.MenuItem)
admin.site.register(models.Order)