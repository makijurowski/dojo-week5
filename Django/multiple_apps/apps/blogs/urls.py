from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^create$', views.create, name='create'),
    url(r'^(?P<num>[0-9]+)$', views.show, name='show'),
    url(r'^(?P<num>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'^(?P<num>[0-9]+)/delete$', views.destroy, name='delete'),
]
