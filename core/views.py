from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView, FormView
from django.views.generic.detail import SingleObjectMixin

from . import models, forms

PAGE_SIZE = 24


class FileList(ListView):
    model = models.File
    # template_name = 'core/file_list.html'
    paginate_by = PAGE_SIZE


class FileAdd(FormView):
    """
    Exactly due doc: https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/#uploading-multiple-files
    """
    form_class = forms.MultiFileAddForm
    template_name = 'core/file_form.html'
    success_url = reverse_lazy('file_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form(self.get_form_class())
        if form.is_valid():
            for f in request.FILES.getlist('file'):
                models.File.objects.create(file=f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class FileDetail(DetailView):
    model = models.File


class FileUpdate(UpdateView):
    model = models.File
    fields = ('name',)


class FileDelete(DeleteView):
    model = models.File
    success_url = reverse_lazy('file_list')


class __FileDownload(SingleObjectMixin, View):
    model = models.File
    as_attach = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return FileResponse(
            open(self.object.get_path(), "rb"),
            as_attachment=self.as_attach,
            content_type=self.object.mime,
            filename=self.object.name)


class FileGet(__FileDownload):
    as_attach = True


class FileShow(__FileDownload):
    as_attach = False


def delete_multi(request, m, fw: str):
    """
    Delete checked items from listview.
    @param m: model
    @param fw: url redirect to
    """
    if request.method == 'POST':
        checks = request.POST.getlist('checked')
        if checks:
            m.objects.filter(pk__in=set(checks)).delete()
    return redirect(fw)


def file_delete_multi(request):
    return delete_multi(request, models.File, reverse('file_list'))
