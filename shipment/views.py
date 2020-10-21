from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View, TemplateView, RedirectView  # !
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

from . import models, forms
from core.models import File

PAGE_SIZE = 25


class OrgList(ListView):
    model = models.Org
    paginate_by = PAGE_SIZE
    # template_name = 'shipment/org_list.html'


class OrgAdd(CreateView):
    model = models.Org
    fields = ['name', 'fullname']
    # template_name = 'shipment/org_form.html'


class OrgDetail(DetailView):
    model = models.Org
    # template_name = 'shipment/org_detail.html'


class OrgUpdate(UpdateView):
    model = models.Org
    fields = ['name', 'fullname']
    # template_name = 'shipment/org_form.html'


class OrgDelete(DeleteView):
    model = models.Org
    success_url = reverse_lazy('org_list')
    # template_name = 'shipment/org_confirm_delete.html'


class DocList(ListView):
    model = models.Document
    paginate_by = PAGE_SIZE


class DocAdd(FormView):
    form_class = forms.DocAddForm
    template_name = 'shipment/document_form.html'
    success_url = reverse_lazy('doc_list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            f = request.FILES.get('file')
            file = File(file=f)
            file.save()
            doc = models.Document(
                file=file,
                shipper=form.cleaned_data['shipper'],
                org=form.cleaned_data['org'],
                date=form.cleaned_data['date'],
                doctype=form.cleaned_data['doctype'],
                comments=form.cleaned_data['comments']
            )
            doc.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DocDetail(DetailView):
    model = models.Document
    # template_name = 'shipment/doc_detail.html'


class DocUpdate(UpdateView):
    model = models.Document
    fields = ['shipper', 'org', 'date', 'doctype', 'comments']
    # template_name = 'shipment/doc_form.html'


class DocDelete(DeleteView):
    model = models.Document
    success_url = reverse_lazy('doc_list')
    # template_name = 'shipment/doc_confirm_delete.html'


'''class DocAdd(CreateView):
    model = models.Document
    fields = ['file', 'shipper', 'org', 'date', 'doctype', 'comments']
    # template_name = 'shipment/doc_form.html'
'''
