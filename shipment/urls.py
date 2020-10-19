from django.urls import path

from . import views

urlpatterns = [
    # path('', 				views.index, name='index'),
    path('o/',				views.OrgList.as_view(), name='org_list'),
    path('o/a/',			views.OrgAdd.as_view(), name='org_add'),
    path('o/<int:pk>/r/',	views.OrgDetail.as_view(), name='org_view'),
    path('o/<int:pk>/u/',	views.OrgUpdate.as_view(), name='org_update'),
    path('o/<int:pk>/d/',	views.OrgDelete.as_view(), name='org_delete'),
    path('d/',				views.DocList.as_view(), name='doc_list'),
    path('d/a/',			views.DocAdd.as_view(), name='doc_add'),
    path('d/<int:pk>/r/',	views.DocDetail.as_view(), name='doc_view'),
    path('d/<int:pk>/u/',	views.DocUpdate.as_view(), name='doc_update'),
    path('d/<int:pk>/d/',	views.DocDelete.as_view(), name='doc_delete'),
]