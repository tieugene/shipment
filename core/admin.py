from django.contrib import admin

from . import models

class FileAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'size', 'crc')
    #exclude = ('name', 'size', 'mime', 'crc')

admin.site.register(models.File, FileAdmin)
