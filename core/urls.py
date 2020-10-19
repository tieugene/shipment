from django.urls import path

from . import views

urlpatterns = [
    path('', 				views.index, name='index'),
    path('f/',				views.FileList.as_view(), name='file_list'),
    path('f/a/',			views.FileAdd.as_view(), name='file_add'),
    path('f/(<int:pk>/r/',	views.FileDetail.as_view(), name='file_view'),
    path('f/<int:pk>/u/',	views.FileUpdate.as_view(), name='file_update'),
    path('f/<int:pk>/d/',	views.FileDelete.as_view(), name='file_delete'),
    # path('f/(<int:pk>/d/',	views.file_del, name='file_del'),
    path('f/(<int:pk>/g/',	views.file_get, name='file_get'),
    path('f/(<int:pk>/v/',	views.file_preview, name='file_preview'),
]
