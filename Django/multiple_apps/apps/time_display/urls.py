from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index.html$', views.index, name='home'),
]
