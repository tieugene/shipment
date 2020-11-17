"""
shipment.admin
"""
from django.contrib import admin

from . import models

admin.site.register(models.Shipper)
admin.site.register(models.Org)
admin.site.register(models.DocType)
admin.site.register(models.Document)
