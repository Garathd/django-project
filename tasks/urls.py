from django.conf.urls import url
from .views import task_info, create_or_edit_task, delete_task

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', task_info, name='task_info'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_task, name='edit_task'),
    url(r'^create/$', create_or_edit_task, name='create_task'),
    url(r'^(?P<pk>\d+)/delete/$', delete_task, name='delete_task'),
    ]
