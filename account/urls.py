from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'account'

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', views.user_logout, name='logout')
]
