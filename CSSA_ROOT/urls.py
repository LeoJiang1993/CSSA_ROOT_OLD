"""CSSA_ROOT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from CSSA_ROOT import settings
from webroot import views
from account import urls as account_urls
from news import urls as news_urls
from activity import urls as activity_urls
from comment import urls as commnet_urls

urlpatterns = [
                  url(r'^account/', include(account_urls)),
                  url(r'^news', include(news_urls)),
                  url(r'^comment/', include(commnet_urls)),
                  url(r'^admin/', admin.site.urls),
                  url(r'^site_admin$', views.site_admin),
                  url(r'^header$', views.header),
                  url(r'^activity/', include(activity_urls)),
                  url(r'^$', views.index),

              ] + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.page_not_found
