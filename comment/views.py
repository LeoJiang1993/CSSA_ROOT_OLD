from django.http import HttpResponse
from django.shortcuts import render, redirect

from comment.forms import NewComment
from comment.models import Comment
from CSSA_ROOT.util.authority_decorators import *
from news.models import News, NewsTopic


@admin
def delete_comment(request):
    cmt_id = request.GET['id']
    Comment.delete_comment(cmt_id)
    return HttpResponse('succeed')


@admin
def active_comment(request):
    cmt_id = request.GET['id']
    Comment.active_comment(cmt_id)
    return HttpResponse('succeed')


@logged_in
@ajax
def comment(request):
    cmt = NewComment(request.GET)
    if cmt.is_valid():
        account_id = request.session['user'].id
        news_id = cmt.cleaned_data['news_id']
        news = News.get_news(news_id, 1)[0]
        if not news.has_comment:
            return HttpResponse('failed')
        content = cmt.cleaned_data['content']
        Comment.comment(news_id, account_id, content)
        return HttpResponse('succeed')
    else:
        return HttpResponse('failed')


def get_comment(request, news_id):
    news = News.get_news(news_id, 1)
    if news is None:
        raise Http404()
    if not news[0].has_comment:
        raise Http404()
    page = request.GET.get('page')
    if page is None:
        page = 1
    comments = Comment.get_comment_by_news_id(news_id, page, 1)
    context = comments
    return render(request, 'comments.html', context)


@admin
def comment_admin(request):
    topics = NewsTopic.get_topic_list_edit()
    news_id = request.GET.get('news_id')
    if news_id is not None:
        news = News.get_news(news_id)[0]
        topic = news.topic_id
        newses = News.get_news_list_edit(topic)
    else:
        news = None
        newses = None
        topic = None
    status = request.GET.get('status')
    if status is not None:
        status = int(status)
    content = dict(topics=topics, newses=newses, news=news, topic=topic, status=status)
    return render(request, 'comments_admin.html', content)


@admin
def comment_admin_list(request):
    try:
        news_id = request.GET['news_id']
        status = request.GET['status']
        page = request.GET['page']
    except ():
        raise Http404()
    comments = Comment.get_comment_by_news_id(news_id, page, status)
    context = comments
    return render(request, 'comments_admin_list.html', context)



    # news = News.get_news(news_id, 1)
    # if news is None:
    #     raise Http404()
    # if not news[0].has_comment:
    #     raise Http404()
    # page = request.GET.get('page')
    # comments = Comment.get_comment_by_news_id(news_id, page, True)
    # context = comments
    # return render(request, 'comments_admin.html', context)
