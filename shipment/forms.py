import datetime

from django import forms
from django.utils.translation import gettext as _

from . import models


class DocAddForm(forms.Form):
    file = forms.FileField(label=_('File'))  # , required=False
    shipper = forms.ModelChoiceField(queryset=models.Shipper.objects.all(), label=_("Shipper"))
    org = forms.ModelChoiceField(queryset=models.Org.objects.all(), label=_("Customer"))
    doctype = forms.ModelChoiceField(queryset=models.DocType.objects.all(), label=_("Type"), help_text=_("Document type"))
    date = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget, label=_("Date"), help_text=_("Shipment date"))
    comments = forms.CharField(max_length=255, strip=True, label=_("Comments"))