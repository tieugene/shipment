from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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


@login_required
def file_preview(request, id):
    return render(request, 'core/file_img.html', {'file': models.File.objects.get(pk=int(id))})


@login_required
def file_get(request, id):
    """
    Download file
    """
    file = models.File.objects.get(pk=int(id))
    response = HttpResponse(content_type=file.mime)
    response['Content-Transfer-Encoding'] = 'binary'
    response['Content-Disposition'] = '; filename=\"%s\"' % file.name.encode('utf-8')
    response.write(open(file.get_path()).read())
    return response


@login_required
def file_del(request, id):
    """
    """
    models.File.objects.get(pk=int(id)).delete()
    return redirect('file_list')
