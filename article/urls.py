from django.conf.urls import url
from . import views

app_name = 'article'

urlpatterns = [
    url(r'^article_column/$', views.article_column, name='article_column'),
    url(r'^rename_column/$', views.rename_article_column, name="rename_article_column"),
    url(r'^del_column/$', views.del_article_column, name="del_article_column"),
    url(r'^article_post/$', views.article_post, name="article_post"),
    url(r'^article_list/$', views.article_list, name="article_list"),
    url(r'^article_detail/(?P<id>\d+)/(?P<slug>[-\w]+)$', views.article_detail, name="article_detail"),
    url(r'^del_article/$', views.del_article, name="del_article"),
]
