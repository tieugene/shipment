from django import forms
from django.utils.translation import gettext as _


class FileAddForm(forms.Form):
    file = forms.FileField(label=_('File'))  # , required=False


class MultiFileAddForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label=_('File'))  # , required=False
