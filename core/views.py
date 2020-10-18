from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from . import models

PAGE_SIZE = 25

def index(request):
    return HttpResponse("Hello, world. You're at the core index.")

class FileList(ListView):
    model = models.File
    template_name = 'core/file_list.html'
    paginate_by = PAGE_SIZE


class FileDetail(DetailView):
    model = models.File
    template_name = 'core/file_view.html'

@login_required
def file_preview(request, id):
    return render(request, 'core/file_img.html', {'file': models.File.objects.get(pk=int(id))})


@login_required
def file_get(request, id):
    '''
    Download file
    '''
    file = models.File.objects.get(pk=int(id))
    response = HttpResponse(content_type=file.mime)
    response['Content-Transfer-Encoding'] = 'binary'
    response['Content-Disposition'] = '; filename=\"%s\"' % file.name.encode('utf-8')
    response.write(open(file.get_path()).read())
    return response


@login_required
def file_del(request, id):
    '''
    '''
    models.File.objects.get(pk=int(id)).delete()
    return redirect('file_list')
