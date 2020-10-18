from django.urls import path

from . import views

urlpatterns = [
    path('', 				views.index, name='index'),
    path(r'f/',				views.FileList.as_view(), name='file_list'),
    path(r'f/(<int:pk>/r/',	views.FileDetail.as_view(), name='file_view'),
    path(r'f/(<int:pk>/g/',	views.file_get, name='file_get'),
    path(r'f/(<int:pk>/d/',	views.file_del, name='file_del'),
]
