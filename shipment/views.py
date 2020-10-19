#from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View, TemplateView, RedirectView # !
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import models

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


class DocAdd(CreateView):
    model = models.Document
    fields = ['name', 'fullname']
    # template_name = 'shipment/org_form.html'


class DocDetail(DetailView):
    model = models.Document
    # template_name = 'shipment/org_detail.html'


class DocUpdate(UpdateView):
    model = models.Document
    fields = ['shipper', 'org', 'doctype', 'date']
    # template_name = 'shipment/org_form.html'


class DocDelete(DeleteView):
    model = models.Document
    success_url = reverse_lazy('doc_list')
    # template_name = 'shipment/org_confirm_delete.html'
