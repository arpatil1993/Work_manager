from django.conf.urls import url, include
from taskmanager.views import *

urlpatterns = [
    url(r'index/$', IndexView),
    url(r'^create/project/object$', create_project_object),
    url(r'^get/project/object$', get_project_object),
    url(r'^project-detail-(?P<pk>\d+)$', get_project_object),
    url(r'^create/task$', save_task_object),
    url(r'^update/task$', update_task),
    url(r'^update/client$', update_client),
    url(r'^try-delete$', delete_record),
    url(r'^queryset$', q_in_queryset),
]
