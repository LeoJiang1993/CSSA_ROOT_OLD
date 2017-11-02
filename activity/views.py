from django.http import HttpResponse
from django.shortcuts import render
from CSSA_ROOT.util.authority_decorators import *
from activity.forms import EditActivity
from activity.models import Activity, SignUp


@admin
def get_activity_list(request, activity_status):
    activities = Activity.get_activity_list_by_status(activity_status)
    context = dict(activities=activities)
    return render(request, 'activity_list_edit.html', context)


@admin
def edit_activity(request, activity_id):
    if request.method == 'GET':
        form = EditActivity(request.GET)
        if form.is_valid():
            activity = Activity.save_activity(activity_id, form.cleaned_data['description'],
                                              form.cleaned_data['time'],
                                              form.cleaned_data['capacity'], form.cleaned_data['status'])
        else:
            activity = Activity.get_activity(activity_id)
        status = Activity.ACTIVITY_STATUS
        context = dict(activity=activity, status=status)
        return render(request, 'edit_activity.html', context)


@admin
def activity_admin(request):
    status = Activity.ACTIVITY_STATUS
    context = dict(status=status)
    return render(request, 'activity_admin.html', context)


@admin
def reserved_list(request, activity_id):
    reserved_list = SignUp.get_reserved_list(activity_id)
    activity = Activity.get_activity(activity_id)
    context = dict(reserved_list=reserved_list, activity=activity)
    return render(request, 'reserved_list.html', context)


@logged_in
def get_reservations(request):
    account_id = request.session['user'].id
    reservations = SignUp.get_reservations(account_id)
    context = dict(reservations=reservations)
    return render(request, 'manage_reservation.html', context)


@logged_in
def reserve(request):
    operation = request.GET['operation']
    activity = request.GET['activity_id']
    user = request.session['user']
    if operation == 'reserve':
        SignUp.sign_up(user.id, activity)
    elif operation == 'cancel':
        SignUp.cancel(user.id, activity)
    return HttpResponse("succeed")


def in_news(request, activity_id):
    if request.session.get('user') is not None:
        activity = Activity.get_activity(activity_id)
        reserved = SignUp.reserved(request.session.get('user').id, activity_id)
        booked = SignUp.ger_reserved_num(activity_id)
        context = dict(activity=activity, booked=booked, reserved=reserved)
        return render(request, 'sign_up_for_activity.html', context)
    else:
        return render(request,'sign_in.html')