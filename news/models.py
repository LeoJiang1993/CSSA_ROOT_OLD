import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

# Create your models here.
from account.models import Account
from activity.models import Activity
from news.storage import NewsImageStorage


class NewsTopic(models.Model):
    description = models.CharField(max_length=30)
    status = models.BooleanField()

    @staticmethod
    def get_topic(topic_id):
        return NewsTopic.objects.get(id=topic_id).description

    @staticmethod
    def get_topic_list():
        return NewsTopic.objects.filter(status=True)

    @staticmethod
    def get_topic_list_edit():
        return NewsTopic.objects.all()

    @staticmethod
    def modify(topic_id, description, status):
        if int(topic_id) == 0:
            topic = NewsTopic(description=str(description), status=status)
        else:
            topic = NewsTopic(id=topic_id, description=str(description), status=status)
        topic.save()
        return topic


class News(models.Model):
    NEWS_STATUS = (
        (1, u'Online'),
        (2, u'Draft'),
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    banner = models.ImageField(upload_to="static/news/banner", null=False, storage=NewsImageStorage())
    status = models.IntegerField(choices=NEWS_STATUS)
    topic = models.ForeignKey(NewsTopic)
    activity = models.ForeignKey(Activity, blank=True)
    viewed = models.IntegerField(null=0)
    # todo:加上去，很多地方没有
    has_comment = models.BooleanField(default=True)

    @staticmethod
    def save_news(id, title, author, content, banner, status, topic, activity, has_comment):
        # id == 0, add a new news.
        if id == 0:
            new_news = News(title=title, author=author, content=content, banner=banner, status=status,
                            topic_id=topic, activity_id=activity, viewed=0, has_comment=has_comment)
            new_news.save()
            return new_news
        else:
            if activity is None:
                activity = 1
            if banner is None:
                news = News.objects.filter(id=id)
                news.update(title=title, author=author, content=content,
                            status=status, topic_id=topic, activity_id=activity, has_comment=has_comment)
            else:
                news = News.objects.filter(id=id)
                news.update(title=title, author=author, content=content, banner=banner,
                            status=status, topic_id=topic, activity_id=activity)
            return news.first()

    @staticmethod
    def get_news(news_id, status=None):
        if status is None:
            return News.objects.filter(id=news_id)
        return News.objects.filter(id=news_id, status=status)

    @staticmethod
    def get_news_list(status):
        return News.objects.filter(status=status).order_by('time').order_by('topic')

    @staticmethod
    def get_news_list_by_topic(topic, status,page=1):
        newses = News.objects.filter(status=status, topic_id=topic).order_by('time_modified').reverse()
        if newses.count() == 0:
            rt = dict(newses=None, pages=0, page=0)
            return rt
        if page == -1:
            return dict(newses=newses)
        pager = Paginator(newses, 20)
        try:
            newses = pager.page(page)
        except PageNotAnInteger:
            newses = pager.page(1)
            page = 1
        except EmptyPage:
            newses = pager.page(pager.num_pages)
            page = pager.num_pages
        return dict(newses=newses, pages=pager.num_pages, page=int(page))

    @staticmethod
    def get_news_list_edit(topic):
        return News.objects.filter(topic_id=topic)

    @staticmethod
    def get_news_edit(news_id):
        return News.objects.get(id=news_id)

    @staticmethod
    def get_status_list():
        return News.NEWS_STATUS


class NewsOnSpecialPlace(models.Model):
    SPECIAL_PLACES = (
        (1, u'ABOUT US'),
        (2, u'INDEX TOP'),
        (3, u'INDEX'),
        (4, u'NEWS TOP'),
    )
    place = models.IntegerField(choices=SPECIAL_PLACES)
    rank = models.IntegerField()
    news = models.ForeignKey(News)

    @staticmethod
    def get_list(place_id):
        return NewsOnSpecialPlace.objects.filter(place=place_id).order_by('rank')

    @staticmethod
    def set_list(place_id, rl):
        rl = json.loads(rl)
        NewsOnSpecialPlace.objects.filter(place=place_id).delete()
        c = 1
        for i in rl:
            NewsOnSpecialPlace(place=place_id, rank=c, news_id=int(i)).save()
            c += 1
        return NewsOnSpecialPlace.get_list(place_id)
