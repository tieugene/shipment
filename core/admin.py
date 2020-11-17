"""
core.admin
https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin
"""
from django.contrib import admin

from . import models


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    fields = ('file',)

# admin.site.register(models.File)
