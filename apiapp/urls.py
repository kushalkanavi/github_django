from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^addUser/$', views.addUser.as_view(),name='addUser'),
    url(r'^searchUser/$', views.searchUser.as_view(),name='searchUser'),
    url(r'^adminReport/$', views.adminReport.as_view(),name='adminReport'),

    url(r'^$', views.index.as_view(),name='index'),
]