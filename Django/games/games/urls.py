from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ninja_gold/', include('apps.ninja_gold.urls'), name='ninja_gold'),
    url(r'^', include('apps.ninja_gold.urls'), name='home'),
]
