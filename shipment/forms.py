import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from . import models
from core.models import get_file_mime


class DocAddForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label=_('File'))
    shipper = forms.ModelChoiceField(queryset=models.Shipper.objects.all(), label=_("Shipper"))
    org = forms.ModelChoiceField(queryset=models.Org.objects.all(), label=_("Customer"))
    date = forms.DateField(initial=datetime.date.today, widget=forms.SelectDateWidget, label=_("Date"),
                           help_text=_("Shipment date"))
    doctype = forms.ModelChoiceField(queryset=models.DocType.objects.all(), required=False, label=_("Type"),
                                     help_text=_("Document type"))
    comments = forms.CharField(required=False, max_length=255, strip=True, label=_("Comments"))

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        mime = get_file_mime(file)
        if "application/pdf" not in mime:
            raise ValidationError(_("File is not PDF: ") + file.name)
        return file


class DocEditMultiForm(forms.Form):
    shipper = forms.ModelChoiceField(queryset=models.Shipper.objects.all(), required=False, label=_("Shipper"))
    org = forms.ModelChoiceField(queryset=models.Org.objects.all(), required=False, label=_("Customer"))
    date = forms.DateField(widget=forms.SelectDateWidget, required=False, label=_("Date"),
                           help_text=_("Shipment date"))
    doctype = forms.ModelChoiceField(queryset=models.DocType.objects.all(), required=False, label=_("Type"),
                                     help_text=_("Document type"))
    shipper_chg = forms.BooleanField(required=False, label=_("Change shipper"))
    org_chg = forms.BooleanField(required=False, label=_("Change partner"))
    date_chg = forms.BooleanField(required=False, label=_("Change date"))
    doctype_chg = forms.BooleanField(required=False, label=_("Change doctype"))
    checked = forms.ModelMultipleChoiceField(models.Document.objects.all(), widget=forms.MultipleHiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        shipper_chg = cleaned_data.get('shipper_chg')
        org_chg = cleaned_data.get('org_chg')
        date_chg = cleaned_data.get('date_chg')
        doctype_chg = cleaned_data.get('doctype_chg')
        if shipper_chg or org_chg or date_chg or doctype_chg:
            if shipper_chg and not cleaned_data.get('shipper'):
                self.add_error('shipper', _("Select one"))
            if org_chg and not cleaned_data.get('org'):
                self.add_error('org', _("Select one"))
            if date_chg and not cleaned_data.get('date'):
                self.add_error('date', _("Set right date"))
        else:
            self.add_error(None, _("Choose to change something"))
