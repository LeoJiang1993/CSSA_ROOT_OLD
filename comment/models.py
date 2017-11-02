import json

from django.db import models

# Create your models here.
from account.models import Account
from activity.models import Activity
from news.models import News
from django.core.paginator import *


class Comment(models.Model):
    COMMENT_STATUS = (
        (1, r'normal'),
        (2, r'blocked'),
    )
    news = models.ForeignKey(News)
    content = models.CharField(max_length=200)
    author = models.ForeignKey(Account)
    status = models.IntegerField(choices=COMMENT_STATUS)
    time = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def delete_comment(comment_id):
        try:
            cmt = Comment.objects.get(id=comment_id)
            cmt.status = 2
            cmt.save()
        except ():
            return False
        return True

    @staticmethod
    def active_comment(comment_id):
        try:
            cmt = Comment.objects.get(id=comment_id)
            cmt.status = 1
            cmt.save()
        except ():
            return False
        return True

    @staticmethod
    def comment(news_id, account_id, content):
        cmt = Comment(news_id=news_id, content=content, author_id=account_id, status=1)
        cmt.save()
        return cmt

    @staticmethod
    def get_comment_by_news_id(news_id, page, authority):
        authority = int(authority)
        if authority == 1:
            comments = Comment.objects.filter(news_id=news_id, status=1).order_by('time').reverse()
        elif authority == 2:
            comments = Comment.objects.filter(news_id=news_id, status=2).order_by('time').reverse()
        else:
            comments = Comment.objects.filter(news_id=news_id).order_by('time').reverse()
        if comments.count() == 0:
            rt = dict(comments=None, pages=0, page=0)
            return rt
        pager = Paginator(comments, 20)
        try:
            comments = pager.page(page)
        except PageNotAnInteger:
            comments = pager.page(1)
            page = 1
        except EmptyPage:
            comments = pager.page(pager.num_pages)
            page = pager.num_pages
        rt = dict(comments=comments, pages=pager.num_pages, page=int(page))
        return rt
