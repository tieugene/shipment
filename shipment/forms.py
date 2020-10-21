import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from . import models
from core.models import get_file_mime

class DocAddForm(forms.Form):
    file = forms.FileField(label=_('File'))  # , required=False
    shipper = forms.ModelChoiceField(queryset=models.Shipper.objects.all(), label=_("Shipper"))
    org = forms.ModelChoiceField(queryset=models.Org.objects.all(), label=_("Customer"))
    doctype = forms.ModelChoiceField(queryset=models.DocType.objects.all(), label=_("Type"), help_text=_("Document type"))
    date = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget, label=_("Date"), help_text=_("Shipment date"))
    comments = forms.CharField(required=False, max_length=255, strip=True, label=_("Comments"))

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        mime = get_file_mime(file)
        # print(mime)
        if not "application/pdf" in mime:
            raise ValidationError(_("File is not PDF."))
        return file
