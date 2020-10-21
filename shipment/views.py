from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View, TemplateView, RedirectView  # !
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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


'''class DocAdd(CreateView):
    model = models.Document
    fields = ['file', 'shipper', 'org', 'date', 'doctype', 'comments']
    # template_name = 'shipment/doc_form.html'
'''


def doc_add(request):
    """
    """
    if request.method == 'POST':
        form = forms.DocAddForm(request.POST, request.FILES)
        if form.is_valid():
            file = File(file=request.FILES['file'])
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
            return redirect(doc)
    else:
        form = forms.DocAddForm()
    return render(request, 'shipment/document_form.html', {'form': form})


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
