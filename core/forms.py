"""
core.forms
"""
from django import forms
from django.utils.translation import gettext as _

from . import models


class DeleteMultiForm(forms.Form):
    checked = forms.ModelMultipleChoiceField(queryset=None,
                                             widget=forms.CheckboxSelectMultiple(), label=_("Selected"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        checked = kwargs['initial'].get('checked')
        if checked:
            self.fields['checked'].queryset = self.model.objects.filter(pk__in=checked)
        else:
            self.fields['checked'].queryset = self.model.objects.all()


class MultiFileAddForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label=_('File'))


class FileDeleteMultiForm(DeleteMultiForm):
    model = models.File
