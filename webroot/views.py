# Create your views here.
from django.shortcuts import render

from CSSA_ROOT.util.authority_decorators import admin
from news.models import NewsOnSpecialPlace, NewsTopic


def index(request, info=None):
    bar_newss = NewsOnSpecialPlace.get_list(2)
    newss = NewsOnSpecialPlace.get_list(3)
    context = dict(bar_newss=bar_newss, newss=newss, info=info)
    return render(request, "index.html", context)


def header(request):
    about_us = NewsOnSpecialPlace.get_list(1)
    news_topics = NewsTopic.get_topic_list()
    context = dict(about_us=about_us, news_topics=news_topics)
    return render(request, "header.html", context)


@admin
def site_admin(request):
    return render(request, 'siteAdmin.html')


def page_not_found(request):
    return render(request, '404.html')
