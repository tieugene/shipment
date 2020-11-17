"""
core.forms
"""
from django import forms
from django.utils.translation import gettext as _


class MultiFileAddForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label=_('File'))


'''
class FileAddForm(forms.Form):
    file = forms.FileField(label=_('File'))
'''
