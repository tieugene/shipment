from django.urls import path

from . import views

urlpatterns = [
    path('f/',				views.FileList.as_view(), name='file_list'),
    path('f/s/<str:fld>/',  views.FileListSort.as_view(), name='file_list_sort'),
    path('f/d/',			views.file_delete_multi, name='file_delete_multi'),
    path('f/a/',			views.FileAdd.as_view(), name='file_add'),
    path('f/<int:pk>/r/',	views.FileDetail.as_view(), name='file_view'),
    path('f/<int:pk>/u/',	views.FileUpdate.as_view(), name='file_update'),
    path('f/<int:pk>/d/',	views.FileDelete.as_view(), name='file_delete'),
    path('f/<int:pk>/g/',	views.FileGet.as_view(), name='file_get'),
    path('f/<int:pk>/v/',	views.FileShow.as_view(), name='file_show'),
]
