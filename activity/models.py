from django.db import models

from account.models import Account


class Activity(models.Model):
    ACTIVITY_STATUS = (
        (1, 'ACTIVE'),
        (2, u'CANCELLED'),
        (3, u'EXPIRED'),
        (4, u'HOLD'),
    )
    description = models.CharField(max_length=100)
    time = models.DateTimeField()
    capacity = models.IntegerField()
    status = models.IntegerField(choices=ACTIVITY_STATUS)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_activity(activity_id):
        return Activity.objects.filter(id=activity_id).first()

    @staticmethod
    def get_activity_list_for_news_edit():
        return Activity.objects.filter(status=1)

    @staticmethod
    def get_activity_list_all():
        return Activity.objects.all()

    @staticmethod
    def get_activity_list_by_status(status=1):
        return Activity.objects.filter(status=status)

    @staticmethod
    def save_activity(activity_id, description, time, capacity, status):
        activity_id = int(activity_id)
        if activity_id == 0:
            activity = Activity(description=description, time=time, capacity=capacity, status=status)
            activity.save()
        else:
            activity = Activity.objects.filter(id=activity_id)
            activity.update(description=description, time=time, capacity=capacity, status=status)
            activity = activity.first()
        return activity


class SignUp(models.Model):
    activity = models.ForeignKey(Activity)
    account = models.ForeignKey(Account)
    booked = models.BooleanField(null=False)
    time = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_reservations(account_id):
        return SignUp.objects.filter(account_id=account_id, booked=True)

    @staticmethod
    def ger_reserved_num(activity_id):
        return SignUp.objects.filter(activity_id=activity_id, booked=True).count()

    @staticmethod
    def get_reserved_list(activity_id):
        return SignUp.objects.filter(activity_id=activity_id)

    @staticmethod
    def sign_up(user_id, activity_id):
        capacity = Activity.objects.filter(id=activity_id)[0].capacity
        reserved = SignUp.ger_reserved_num(activity_id)
        if reserved <= capacity:
            item = SignUp.objects.filter(account_id=user_id, activity_id=activity_id)
            if item.count() == 0:
                SignUp(account_id=user_id, activity_id=activity_id, booked=True).save()
                return 'succeed'
            else:
                item.update(booked=True)
                return 'succeed'
        else:
            return 'Full'

    @staticmethod
    def cancel(user_id, activity_id):
        SignUp.objects.filter(account_id=user_id, activity_id=activity_id).update(booked=False)

    @staticmethod
    def reserved(user_id, activity_id):
        return SignUp.objects.filter(account_id=user_id, activity_id=activity_id, booked=True).count() == 1
