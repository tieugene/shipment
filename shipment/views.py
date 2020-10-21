from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.base import View, TemplateView, RedirectView  # !
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView
from django.views.decorators.csrf import csrf_exempt

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
            files = request.FILES.getlist('file')   # get() for standalone
            for f in files:
                file = File(file=f)
                file.save()
                models.Document.objects.create(
                    file=file,
                    shipper=form.cleaned_data['shipper'],
                    org=form.cleaned_data['org'],
                    date=form.cleaned_data['date'],
                    doctype=form.cleaned_data['doctype'],
                    comments=form.cleaned_data['comments']
                )
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

@csrf_exempt
def doc_bulk(request):
    """
    Bulk uploading documents.
    RTFM: https://pythoncircle.com/post/713/sending-post-request-with-different-body-formats-in-django/
    Test:
    curl -X POST -F 'shipper=...' -F 'org=...' -F 'date=...' -F 'file=@filename.ext' http://localhost:8000/shipment/d/bulk/
    [-H "Content-Type: multipart/form-data"]
    File: or 'file=@filename.pdf;type=application/pdf'
    (mimetype: `file -b --mime-type <filename>`
    Note: name/org can be ru and w/ spaces
    Requires: shipper, org, date, file[s]
    request.POST: <QueryDict: {'shipper': ['PR'], 'org': ['MyOrg']}>
    request.FILES: {'file': [<InMemoryUploadedFile: settings.py (application/pdf)>]}>
    RTFM: https://www.kite.com/python/docs/django.http.QueryDict
    ----
    Errors:
    - no/wrong shipper/org/date/files
    """
    if request.method != 'POST':
        print("Not POST")
        return
    print("On POST:")
    shipper = request.POST.get('shipper', None)     # str
    org = request.POST.get('org', None)
    date_s = request.POST.get('date', None)
    print("Shipper: {}, Org: {}, Date: {}".format(shipper, org, date_s))
    # print(request.POST)
    print(request.FILES)
    return HttpResponse(status=200)


'''
class DocAdd(CreateView):
    model = models.Document
    fields = ['file', 'shipper', 'org', 'date', 'doctype', 'comments']
    # template_name = 'shipment/doc_form.html'
'''

'''
= Curl tests =
Send:
curl -X POST -F 'shipper=ПроРЕсурс+' -F 'org=Чужая контора' -F 'date=01.02.15' -F 'file=@settings.py;type=application/pdf' -F 'file=@run.sh;type=text/plain' http://localhost:8000/shipment/d/bulk/
Received:
Shipper: ПроРЕсурс+, Org: Чужая контора, Date: 01.02.15
<MultiValueDict: {'file': [<InMemoryUploadedFile: settings.py (application/pdf)>, <InMemoryUploadedFile: run.sh (text/plain)>]}>
'''