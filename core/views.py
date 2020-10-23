from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView, FormView

from . import models, forms

PAGE_SIZE = 25


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


def _delete_multi(request, m, fw: str):
    """
    Delete checked items from listview
    """
    if request.method == 'POST':
        checks = request.POST.getlist('checked')
        if checks:
            m.objects.filter(pk__in=set(checks)).delete()
    return redirect(fw)


def file_delete_multi(request):
    return _delete_multi(request, models.File, reverse('file_list'))


def __file_download(pk, as_attach):
    file = models.File.objects.get(pk=int(pk))
    return FileResponse(
        open(file.get_path(), "rb"),
        as_attachment=as_attach,
        content_type=file.mime,
        filename=file.name)


def file_get(request, pk):
    """
    Download file
    """
    return __file_download(pk, True)


def file_show(request, pk):
    """
    Download file
    """
    return __file_download(pk, False)


'''
class FileAdd(CreateView):
    model = models.File
    fields = ('file',)

def file_add(request):
    """
    """
    if request.method == 'POST':
        form = forms.FileAddForm(request.POST, request.FILES)
        if form.is_valid():
            file = models.File(file=request.FILES['file'])
            file.save()
            return redirect(file)
    else:
        form = forms.FileAddForm()
    return render(request, 'core/file_form.html', {'form': form})
'''
