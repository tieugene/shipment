from django.contrib import admin


from . import models

class OrgAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('id', 'name', 'fullname')

admin.site.register(models.Shipper)
admin.site.register(models.Org, OrgAdmin)
admin.site.register(models.DocType)
admin.site.register(models.Document)
