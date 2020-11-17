"""
shipment.forms
"""
import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from . import models
from core.models import get_file_mime


class OrgMergeForm(forms.Form):
    org = forms.ModelChoiceField(queryset=models.Org.objects.none(), label=_("Target"))
    checked = forms.ModelMultipleChoiceField(queryset=models.Org.objects.none(),
                                             widget=forms.CheckboxSelectMultiple(), label=_("Selected"))

    def __init__(self, *args, **kwargs):
        """
        :MultiValueDict
        """
        super().__init__(*args, **kwargs)
        chk_list = kwargs['data'].getlist('checked')
        self.fields['org'].queryset = models.Org.objects.exclude(pk__in=chk_list)
        self.fields['checked'].queryset = models.Org.objects.filter(pk__in=chk_list)
        self.fields['checked'].initial = chk_list


def years():
    return [(0, '--')] + list(((i, "%02d" % i) for i in range(14, 21)))


def months():
    return [(0, '--')] + list(((i, "%02d" % i) for i in range(1, 13)))


def days():
    return [(0, '--')] + list(((i, "%02d" % i) for i in range(1, 32)))


class DocAddForm(forms.Form):
    # date: widget=forms.SelectDateWidget,
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label=_('File'))
    shipper = forms.ModelChoiceField(queryset=models.Shipper.objects.all(), label=_("Shipper"))
    org = forms.ModelChoiceField(queryset=models.Org.objects.all(), label=_("Customer"))
    date = forms.DateField(initial=datetime.date.today, label=_("Date"))
    doctype = forms.ModelChoiceField(queryset=models.DocType.objects.all(), required=False, label=_("Type"))
    comments = forms.CharField(required=False, max_length=255, strip=True, label=_("Note"))

    def clean_file(self):
        file = self.cleaned_data.get('file', False)
        mime = get_file_mime(file)
        if "application/pdf" not in mime:
            raise ValidationError(_("File is not PDF: ") + file.name)
        return file


class DocEditMultiForm(forms.Form):
    # date: widget=forms.SelectDateWidget,
    shipper = forms.ModelChoiceField(queryset=models.Shipper.objects.all(), required=False, label=_("Shipper"))
    org = forms.ModelChoiceField(queryset=models.Org.objects.all(), required=False, label=_("Customer"))
    date = forms.DateField(widget=forms.SelectDateWidget(years=range(2014, datetime.date.today().year+1)),
                           required=False, label=_("Date"))
    doctype = forms.ModelChoiceField(queryset=models.DocType.objects.all(), required=False, label=_("Type"))
    shipper_chg = forms.BooleanField(required=False, label=_("Change shipper"), help_text="Use it!")
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
            # doctype can be cleared
        else:
            self.add_error(None, _("Choose to change something"))


class DocFilterForm(forms.Form):
    shipper = forms.ModelChoiceField(queryset=models.Shipper.objects.all(), required=False, label=_("Shipper"))
    org = forms.ModelChoiceField(queryset=models.Org.objects.all(), required=False, label=_("Customer"))
    year = forms.ChoiceField(choices=years(), required=False, label=_("Year"))
    month = forms.ChoiceField(choices=months(), required=False, label=_("Month"))
    day = forms.ChoiceField(choices=days(), required=False, label=_("Day"))
    # date = forms.DateField(widget=forms.SelectDateWidget, required=False, label=_("Date"))
    doctype = forms.ModelChoiceField(queryset=models.DocType.objects.all(), required=False, label=_("Type"))

    def __init__(self, *args, init_data=None, **kwargs):
        super().__init__(*args, **kwargs)
        if init_data:
            for i in ('shipper', 'org', 'doctype', 'year', 'month', 'day'):
                if i in init_data:
                    self.fields[i].initial = int(init_data[i])
                # if 'date' in init_data:
                #    self.fields['date'].initial = datetime.datetime.strptime(init_data['date'], "%y%m%d")
