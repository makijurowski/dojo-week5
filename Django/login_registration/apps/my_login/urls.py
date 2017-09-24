from django.conf.urls import include, url
# from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from login_registration import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^success$', views.success, name='success'),
]

# urlpatterns += staticfiles_urlpatterns()
