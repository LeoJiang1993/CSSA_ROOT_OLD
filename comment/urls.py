from django.conf.urls import url
from comment import views

urlpatterns = [
    url('^(?P<news_id>\d+)$', views.get_comment),
    url('^comment$', views.comment),
    url('^delete$', views.delete_comment),
    url('^active$',views.active_comment),
    url('^admin$', views.comment_admin),
    url('^admin/list$',views.comment_admin_list),
]
