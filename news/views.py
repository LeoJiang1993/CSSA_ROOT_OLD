import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from activity.models import Activity
from news.forms import NewsEdit
from news.models import News, NewsTopic, NewsOnSpecialPlace
from CSSA_ROOT.util.authority_decorators import *
from news.util.save_files import save_news_picture


def news(request):
    news = NewsOnSpecialPlace.get_list(4)
    topics = NewsTopic.get_topic_list()
    context = dict(newss=news, topics=topics)
    return render(request, 'top_news.html', context)


def news_content(request, news_id):
    news_object = News.get_news(news_id, 1)
    if news_object.count() == 1:
        context = dict(news_context=news_object.first())
        return render(request, "news.html", context)
    else:
        raise Http404()


def news_content_c(request, news_id):
    news_object = News.get_news(news_id, 1)
    if news_object.count() == 1:
        viewed = news_object[0].viewed
        news_object.update(viewed=viewed + 1)
        context = dict(news_context=news_object.first())
        return render(request, "news_content.html", context)
    else:
        raise Http404()


def news_list(request, news_topic_id):
    news_topic = NewsTopic.get_topic(news_topic_id)
    if news_topic is None:
        raise Http404()
    context = dict(topics=NewsTopic.get_topic_list(), news_topic=news_topic,
                   news_topic_id=news_topic_id)
    return render(request, "news_list.html", context)


def news_list_list(request):
    news_topic_id = request.GET.get('topic_id')
    page = request.GET.get('page')
    if page is None:
        page = 1
    context = News.get_news_list_by_topic(news_topic_id, 1, page)
    return render(request, 'news_list_list.html', context)


@admin
def news_admin(request):
    topics = NewsTopic.get_topic_list_edit()
    places = NewsOnSpecialPlace.SPECIAL_PLACES
    context = dict(topics=topics, places=places)
    return render(request, 'news_admin.html', context)


@admin
def news_list_edit(request, topic_id):
    newss = News.get_news_list_edit(topic_id)
    context = dict(newss=newss)
    return render(request, 'newslistedit.html', context)


@admin
def news_edit(request, news_id):
    if request.method == 'POST':
        form = NewsEdit(request.POST, request.FILES)
        if form.is_valid():
            news = News.save_news(form.cleaned_data['id'], str(form.cleaned_data['title']),
                                  str(form.cleaned_data['author']),
                                  str(form.cleaned_data['content']), form.cleaned_data['banner'],
                                  form.cleaned_data['status'],
                                  form.cleaned_data['topic'], form.cleaned_data['activity'],
                                  form.cleaned_data['comment']
                                  )
            return redirect('/newsadmin/editnews/' + str(news.id))
        else:
            return HttpResponse("failed")
    else:
        topics = NewsTopic.get_topic_list_edit()
        activities = Activity.get_activity_list_for_news_edit()
        status = News.NEWS_STATUS
        if int(news_id) != 0:
            news = News.get_news_edit(int(news_id))
            context = dict(news=news, topics=topics, activities=activities, status=status)
        else:
            context = dict(topics=topics, activities=activities, status=status)
        return render(request, 'editnews.html', context)


@admin
def upload_news_pictures(request):
    if request.method == "POST":
        file = request.FILES['upload']
        filename = save_news_picture(file)
        filename['uploaded'] = 1
        return HttpResponse(json.dumps(filename))
    else:
        raise Http404()


@admin
def edit_news_topic(request):
    topics = NewsTopic.get_topic_list_edit()
    context = dict(topics=topics)
    return render(request, 'edit_news_topic.html', context)


@admin
def save_news_topic(request):
    topic = NewsTopic.modify(request.GET['topic_id'],
                             request.GET['description'],
                             request.GET['status'])
    return HttpResponse(topic.id)


@admin
def edit_special_place_news(request, place_id):
    rs = request.GET.get('rs')
    if rs is None:
        newss = NewsOnSpecialPlace.get_list(place_id)
        topics = NewsTopic.get_topic_list()
        context = dict(newss=newss, topics=topics)
        return render(request, 'edit_special_place_news.html', context)
    else:
        NewsOnSpecialPlace.set_list(place_id, request.GET['rs'])
        return HttpResponse('succeed')


@admin
def news_list_special_place_news(request, topic_id):
    newses = News.get_news_list_by_topic(topic_id, 1, -1)
    context = newses
    return render(request, 'news_list_special_place_news.html', context)
