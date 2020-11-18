"""
core.views
"""
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from django.views.generic.edit import DeleteView, UpdateView, FormView
from django.views.generic.detail import SingleObjectMixin

from . import models, forms

PAGE_SIZE = 24


def delete_multi(request, m, fw: str):
    """
    Delete checked items from listview.
    @param request: subj
    @param m: model
    @param fw: url redirect to
    TODO: rework to class FileDeleteMulti(View)
    """
    if request.method == 'POST':
        checks = request.POST.getlist('checked')
        if checks:
            m.objects.filter(pk__in=set(checks)).delete()
    return redirect(fw)
# def file_delete_multi(request):
#    return delete_multi(request, models.File, reverse('file_list'))


class DeleteMulti(FormView):
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class(initial={'checked': request.GET.getlist('checked')})})

    def form_valid(self, form):
        form.cleaned_data['checked'].delete()
        return super().form_valid(form)


class FileList(ListView):
    model = models.File
    paginate_by = PAGE_SIZE

    def get_queryset(self):  # 1.
        return self.model.objects.order_by(self.request.session.get('file_sort', models.DEFAULT_SORT_FILE))

    def get_context_data(self, **kwargs):  # 2.
        s = self.request.session.get('file_sort', models.DEFAULT_SORT_FILE)
        stored_desc = (s[0] == '-')
        stored_fld = s[1:] if stored_desc else s
        context = super().get_context_data(**kwargs)
        context['sorted'] = {'h': stored_fld, 'd': not stored_desc}
        return context


class FileListSort(View):

    def get(self, request, fld, *args, **kwargs):
        s = self.request.session.get('file_sort', models.DEFAULT_SORT_FILE)
        stored_desc = (s[0] == '-')
        stored_fld = s[1:] if stored_desc else s
        if fld == stored_fld and not stored_desc:
            fld = '-' + fld
        request.session['file_sort'] = fld
        return redirect('file_list')


class FileDeleteMulti(DeleteMulti):
    form_class = forms.FileDeleteMultiForm
    template_name = 'core/file_confirm_delete_multi.html'
    success_url = reverse_lazy('file_list')


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
