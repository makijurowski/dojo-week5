from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='rest'),
    url(r'^users/$', views.index, name='all_users'),
    url(r'^users/new/$', views.new, name='new_user'),
    url(r'^users/([0-9]{1,})/edit/$', views.edit, name='edit_user'),
    url(r'^users/([0-9]{1,})/$', views.show, name='show_user'),
]
