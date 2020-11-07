import datetime
import calendar
import json
from http import HTTPStatus

# from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
# from django.views.generic.base import View, TemplateView, RedirectView  # !
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView, FormMixin

from core.models import File, get_file_mime, get_file_crc
from core.views import delete_multi
from . import models, forms

# consts
PAGE_SIZE = 25
MIME_PDF = 'application/pdf'
BIG_FILE = 0xFFFFFF     # 16MB


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


def org_delete_multi(request):
    return delete_multi(request, models.Org, reverse('org_list'))


class DocList(FormMixin, ListView):
    """
    [RTFM](https://docs.djangoproject.com/en/3.1/topics/class-based-views/mixins/#avoid-anything-more-complex)
    [Discussion](https://stackoverflow.com/questions/6406553/django-class-based-view-listview-with-form)
    TODO: add get() filling form() from session.
    """
    form_class = forms.DocFilterForm
    model = models.Document
    success_url = reverse_lazy('doc_list')
    paginate_by = PAGE_SIZE

    def get_queryset(self):     # 1.
        q = models.Document.objects.all()
        f = self.request.session
        if f:
            # FIXME: rework to field__pk=...
            # val:int
            val = f.get('shipper')
            if val:
                q = q.filter(shipper=models.Shipper.objects.get(pk=int(val)))
            val = f.get('org')
            if val:
                q = q.filter(org=models.Org.objects.get(pk=int(val)))
            val = f.get('doctype')
            if val:
                q = q.filter(doctype=models.DocType.objects.get(pk=int(val)))
            year = f.get('year')
            if year:
                year += 2000
                month = f.get('month')
                if month:
                    day = f.get('day')
                    if day:
                        q = q.filter(date=datetime.date(year, month, day))
                    else:
                        q = q.filter(date__year=year, date__month=month)
                else:
                    q = q.filter(date__year=year)
            # val = f.get('date')
            # if val:
            #    q = q.filter(date=datetime.datetime.strptime(val, "%y%m%d"))
        return q

    def get_context_data(self, **kwargs):   # 2.
        context = super().get_context_data(**kwargs)
        f = self.request.session.get('doc_list')
        if f:
            context['form'] = self.get_form_class()(init_data=f)
        return context


class DocAdd(FormView):
    form_class = forms.DocAddForm
    template_name = 'shipment/document_form.html'
    success_url = reverse_lazy('doc_list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            files = request.FILES.getlist('file')  # get() for standalone
            for f in files:
                file = File.objects.create(file=f)
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


class DocListFilter(FormView):
    form_class = forms.DocFilterForm
    template_name = 'shipment/document_list.html'
    success_url = reverse_lazy('doc_list')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            doc_list_filter = dict()
            # val:str
            val = form.cleaned_data.get('shipper')
            if val:
                doc_list_filter['shipper'] = val.pk
            val = form.cleaned_data.get('org')
            if val:
                doc_list_filter['org'] = val.pk
            val = form.cleaned_data.get('doctype')
            if val:
                doc_list_filter['doctype'] = val.pk
            year = int(form.cleaned_data.get('year'))
            doc_list_filter['year'] = year
            month = int(form.cleaned_data.get('month'))
            doc_list_filter['month'] = month if year else 0
            day = int(form.cleaned_data.get('day'))
            doc_list_filter['day'] = day if (year and month and day and (day <= calendar.monthrange(2000+year, month)[-1])) else 0
            # val = form.cleaned_data.get('date')
            # if val:
            #    doc_list_filter['date'] = val.strftime("%y%m%d")
            if doc_list_filter:
                request.session['doc_list'] = doc_list_filter
            else:
                if 'doc_list' in request.session:
                    del request.session['doc_list']
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def doc_delete_multi(request):
    return delete_multi(request, models.Document, reverse('doc_list'))


class DocUpdateMulti(FormView):
    form_class = forms.DocEditMultiForm
    template_name = 'shipment/document_form_multi.html'
    success_url = reverse_lazy('doc_list')

    def post(self, request, *args, **kwargs):
        """
        Bulk changing docs attributes.
        """
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            to_change = dict()
            if form.cleaned_data.get('shipper_chg'):
                to_change['shipper'] = form.cleaned_data.get('shipper')
            if form.cleaned_data.get('org_chg'):
                to_change['org'] = form.cleaned_data.get('org')
            if form.cleaned_data.get('date_chg'):
                to_change['date'] = form.cleaned_data.get('date')
            if form.cleaned_data.get('doctype_chg'):
                to_change['doctype'] = form.cleaned_data.get('doctype')
            form.cleaned_data.get('checked').update(**to_change)  # hack
            return self.form_valid(form)
        else:
            if not form.cleaned_data.get('checked'):  # empty doc list == fake call
                return redirect(reverse('doc_list'))
            return self.form_invalid(form)


@csrf_exempt
def doc_bulk(request):
    """
    FIXME: chk crc not works; response == 201 (but add nothing)
    FIXME: View class
    Bulk uploading documents.
    RTFM: https://pythoncircle.com/post/713/sending-post-request-with-different-body-formats-in-django/
    Test:
    curl -X POST -F 'shipper=...' -F 'org=...' -F 'date=...' -F 'file=@filename.ext'
     http://localhost:8000/shipment/d/bulk/
    [-H "Content-Type: multipart/form-data"]
    File: 'file=@filename.pdf[;type=application/pdf][;filename=...]'
    (mimetype: `file -b --mime-type <filename>`
    Note: name/org can be ru and w/ spaces
    Requires: shipper, org, date, file[s]
    request.POST: <QueryDict: {'shipper': ['PR'], 'org': ['MyOrg']}>
    request.FILES: {'file': [<InMemoryUploadedFile: settings.py (application/pdf)>]}>
    RTFM: https://www.kite.com/python/docs/django.http.QueryDict
    ----
    Errors:
    - 400 (extra fields, no fields, no files)
    - 404 (?)
    - 405 (not POST)
    - 406 (bad shipper)
    - 412 (no shipper/org/date/files)
    - 415 (not pdf)
    - file[s] already exist[s]
    """
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))                    # 405
    # 1. get values
    shipper_name = request.POST.get('shipper', None)  # str
    org_name = request.POST.get('org', None)
    date_s = request.POST.get('date', None)
    files = request.FILES.getlist('file')
    # 2. check input
    if shipper_name is None or org_name is None or date_s is None or not files:
        # FIXME: replace with 'not (...&...)
        return HttpResponse(status=HTTPStatus.NOT_ACCEPTABLE)       # 406
    # FIXME: add note for 404
    shipper = get_object_or_404(models.Shipper, name=shipper_name)  # 404
    org_name = org_name.strip()[:32].strip()  # cut off extra chars
    try:
        date = datetime.datetime.strptime(date_s, "%d.%m.%y")
    except ValueError:
        date = None
    if not date:
        return HttpResponseBadRequest("Bad date: '{}'".format(date_s))  # 400
    org = None    # org - lazy search/creation
    response_list = list()
    # 3. add items
    for f in files:  # add file=>doc if file is pdf and not exists; add org if required.
        # 3.1. chk file (size, pdf, not exists)
        if f.size > BIG_FILE:                                       # 413
            response_list.append(dict(status=HTTPStatus.REQUEST_ENTITY_TOO_LARGE, note=f.name))
            continue
        mime = get_file_mime(f)
        if mime != MIME_PDF:                                        # 415
            response_list.append(dict(status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE, note=f.name))
            continue
        md5 = get_file_crc(f)
        if File.objects.filter(crc=md5).exists():                   # 409
            # TODO: check doc (!file) exists and its attrs
            response_list.append(dict(
                status=HTTPStatus.CONFLICT,
                note="File exists: '{}'.".format(f.name)))
            continue
        # 3.2. chk/create org
        if not org:
            org, created = models.Org.objects.get_or_create(name=org_name)
            if not (org or created):                                # 500 and get out
                return HttpResponseServerError("Org not created: '{}'".format(org_name))
        # 3.3. create file
        file = File.objects.create(file=f)
        if not file:                                                # 500
            response_list.append(dict(
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
                note="File not created: '{}'.".format(f.name)))
        # 3.4. create doc
        doc = models.Document.objects.create(file=file, shipper=shipper, org=org, date=date)
        if not doc:                                                 # 500
            response_list.append(dict(
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
                note="Doc not created: '{}'.".format(f.name)))
    # x. the end
    if response_list:   # 207 errors occur
        # TODO: try JsonResponse()
        response = HttpResponse(json.dumps(response_list), content_type="text/json", status=HTTPStatus.MULTI_STATUS)
    else:               # 201
        response = HttpResponse(status=HTTPStatus.CREATED)
    return response
