from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'

urlpatterns = [
    # url(r'^login/$', views.user_login, name='user_login'),
    url(r'^login/$', auth_views.login, {'template_name': 'account/login.html'}, name='user_login'),
    # url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}, name='user_logout'),
    url(r'^register/$', views.register, name='user_register'),
    url(r'^password_change/$', auth_views.password_change,
        # {"template_name": "account/password_change.html"},
        {'post_change_redirect': '/account/password_change_done'},
        name='password_change'),
    url(r'^password_change_done/$', auth_views.password_change_done,
        # {'template_name': 'account/password_change_done.html'},
        name='password_change_done'),
]
