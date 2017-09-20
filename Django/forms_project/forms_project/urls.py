from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='main_index'),
    url(r'^admin/', admin.site.urls),
    url(r'^survey/', include('apps.survey_form.urls'), name='survey'),
    url(r'^words/', include('apps.session_words.urls'), name='words'),
    url(r'^users/', include('apps.users.urls'), name='users'),
    url(r'^dojo_ninjas/', include('apps.dojo_ninjas.urls'), name='dojo_ninjas'),
    url(r'^books/', include('apps.book_authors.urls'), name='books'),
]
