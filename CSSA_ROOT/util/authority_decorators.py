from django.http import Http404
from django.shortcuts import render


def admin(func):
    def admin_authority(request, *args, **kwargs):
        user = request.session.get('user')
        if user is not None:
            if user.group > 0:
                return func(request, *args, **kwargs)
        raise Http404()
    return admin_authority


def logged_in(func):
    def logged_in_authority(request, *args):
        user = request.session.get('user')
        if user is not None:
            if user.group >= 0:
                return func(request, *args)
        raise Http404()
    return logged_in_authority


def ajax(func):
    def send_by_ajax(request, *args):
        if request.is_ajax:
            return func(request, *args)
        else:
            raise Http404()
    return send_by_ajax


def post(func):
    def send_by_post(request, *args):
        if request.method == "POST":
            return func(request, *args)
        else:
            raise Http404()
    return send_by_post
