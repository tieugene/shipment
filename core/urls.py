from django.urls import path

from . import views

urlpatterns = [
    path('f/',				views.FileList.as_view(), name='file_list'),
    path('f/a/',			views.FileAdd.as_view(), name='file_add'),
    path('f/d/',	        views.file_delete_multi, name='file_delete_multi'),
    path('f/<int:pk>/r/',	views.FileDetail.as_view(), name='file_view'),
    path('f/<int:pk>/u/',	views.FileUpdate.as_view(), name='file_update'),
    path('f/<int:pk>/d/',	views.FileDelete.as_view(), name='file_delete'),
    path('f/<int:pk>/g/',	views.file_get, name='file_get'),
    path('f/<int:pk>/v/',	views.file_show, name='file_show'),
]
