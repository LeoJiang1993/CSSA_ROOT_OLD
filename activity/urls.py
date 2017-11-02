from django.conf.urls import url

from activity import views

urlpatterns = [
    url(r'^admin/list/(?P<activity_status>\d+)$', views.get_activity_list),
    url(r'^admin/(?P<activity_id>\d+)$', views.edit_activity),
    url(r'^admin$', views.activity_admin),
    # use two paremeters
    # operation = <reserve, cancel>
    # activity_id = <activity_id>
    url(r'^reserve$', views.reserve),
    url(r'^innews/(?P<activity_id>\d+)$',views.in_news),
    url(r'^admin/reservedlist/(?P<activity_id>\d+)$', views.reserved_list),
    url(r'^reserved$', views.get_reservations),
]
