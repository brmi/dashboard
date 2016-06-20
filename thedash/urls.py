from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.target_list, name='target_list'),
    url(r'^day/$', views.day_update, name='day_update'),
    url(r'^dashboard/(?P<pk>\d+)/$', views.dashboard, name='dashboard'),
]