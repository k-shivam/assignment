from django.conf.urls import include, url

# from django.contrib.auth.views import LoginView
from .views import home, delete, todoPost

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^todoPost/$', todoPost, name='todoPost'),
    url(r'^delete/(?P<pk>\d+)$', delete, name='delete'),
]