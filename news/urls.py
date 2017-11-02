from django.conf.urls import url
from news import views

urlpatterns = [
    url(r'^$', views.news),
    url(r'^/(?P<news_id>\d+)$', views.news_content),
    url(r'^/content/(?P<news_id>\d+)$',views.news_content_c),
    url(r'^list/(?P<news_topic_id>\d+)$', views.news_list),
    url(r'^list/list$',views.news_list_list),
    url(r'^admin$', views.news_admin),
    url(r'^admin/newslist/(?P<topic_id>\d+)$', views.news_list_edit),
    url(r'^admin/editnews/(?P<news_id>\d+)$', views.news_edit),
    url(r'^admin/topic/list$', views.edit_news_topic),
    url(r'^admin/topic/save$', views.save_news_topic),
    url(r'^admin/specialplace/(?P<place_id>\d+)$', views.edit_special_place_news),
    url(r'^admin/specialplace/newslist/(?P<topic_id>\d+)$', views.news_list_special_place_news),
    url(r'^admin/upload_news_pictures$',views.upload_news_pictures),
]
