from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.forms import ModifyAccount, CreateAccount
from account.models import Account
from account.util.send_confirmation_email import send_confirmation_email
from CSSA_ROOT.util.authority_decorators import *

# Create your views here.
from account.util.send_password_reset_email import send_password_reset_email
from webroot.views import index
from account.util import account_info_format

def sign_up(request):
    return render(request, "sign_up.html")


@ajax
@post
def create_account(request):
    form = CreateAccount(request.POST, request.FILES)
    context = {}
    if form.is_valid():
        user_name = form.cleaned_data['user_name']
        password = form.cleaned_data['password']
        if account_info_format.check_password_format(password):
            context['password'] = 'Error'
        nick_name = form.cleaned_data['nick_name']
        photo = form.cleaned_data['photo']
        email = form.cleaned_data['email']
        email.lower()
        if account_info_format.check_email_format(email):
            context['email'] = 'Error'
        last_name = form.cleaned_data['last_name']
        first_name = form.cleaned_data['first_name']
        if context is not {}:
            return context
        user = Account.create_account(user_name, password, nick_name, photo, email, last_name, first_name)
        request.session['user'] = user
        if request.session['user'] is not None & send_confirmation_email(user):
            context = 'succeed'
        else:
            context = 'failed'
    else:
        context = 'failed'
    return HttpResponse(context)


def verify_email(request):
    code = request.GET.get('code')
    if code is None:
        raise Http404()
    else:
        request.session['user'] = Account.verify_account(code)
        return index(request, '<div class=''infoHeader>Email Confirmed!</div>' +
                     '<div>Congratulations! Now you can get full access to the website.</div>')


def sign_in(request):
    user_name = request.POST['user_name']
    password = request.POST['password']
    request.session['user'] = Account.sign_in(user_name, password)
    if request.session['user'] is not None:
        rt = "succeed"
    else:
        rt = "failed"
    return HttpResponse(rt)


def log_out(request):
    if request.session.get('user') is not None:
        del request.session["user"]
        return HttpResponse("True")
    else:
        return HttpResponse("False")


@ajax
def resend_verify_email(request):
    if request.session['user'].group == -1:
        send_confirmation_email(request.session['user'])
        return HttpResponse("success")
    else:
        raise Http404()


@logged_in
def modify(request):
    if request.method == 'POST':
        user = request.session['user']
        if user is None:
            raise Http404()
        form = ModifyAccount(request.POST, request.FILES)
        if form.is_valid():
            user = Account.modify_account(user.id, form.cleaned_data['nick_name'], form.cleaned_data['photo'],
                                          form.cleaned_data['first_name'], form.cleaned_data['last_name'])
        request.session['user'] = user
    return render(request, 'modify_account.html')


def reset_password(request):
    if request.method == "POST":
        user_id = request.session.get('change_password')
        if user_id is None:
            raise Http404()
        password = request.POST['password']
        if not Account.check_password(password):
            return HttpResponse('failed')
        account = Account.change_password(user_id, password)
        request.session.set_expiry(None)
        del request.session['change_password']
        request.session['user'] = account
        return HttpResponse('succeed')
    elif request.GET.get('code') is not None:
        code = request.GET['code']
        account = Account.request_change_password(code=code)
        if account is None:
            raise Http404()
        request.session['change_password'] = account.id
        request.session.set_expiry(600)
        context = dict(user=account)
        return render(request, 'change_password.html', context)
    elif request.session.get('user') is not None or request.GET.get('email') is not None:
        if request.GET.get('email')is not  None:
            email = request.GET['email']
        else:
            email = request.session['user'].email
        code = Account.forget_password(email=email)
        if code is None:
            return HttpResponse('failed')
        send_password_reset_email(code)
        return HttpResponse('succeed')
    else:
        return render(request, 'reset_password.html')
