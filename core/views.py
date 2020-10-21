from urllib.parse import quote

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import models, forms

PAGE_SIZE = 25


class FileList(ListView):
    model = models.File
    # template_name = 'core/file_list.html'
    paginate_by = PAGE_SIZE


'''
class FileAdd(CreateView):
    model = models.File
    fields = ('file',)
'''


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


class FileDetail(DetailView):
    model = models.File


class FileUpdate(UpdateView):
    model = models.File
    fields = ('name',)


class FileDelete(DeleteView):
    model = models.File
    success_url = reverse_lazy('file_list')


# def file_preview(request, pk):
#    return render(request, 'core/file_img.html', {'file': models.File.objects.get(pk=int(pk))})

def __file_download(pk, as_attach):
    file = models.File.objects.get(pk=int(pk))
    return FileResponse(open(file.get_path(), "rb"), as_attachment=as_attach, content_type=file.mime,
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
