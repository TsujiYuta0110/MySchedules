from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import SignupForm, LoginForm, Schedules, MakeSchedule
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers

def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'calendars/signup.html', param)

def login_view(request):
    if request.method == 'POST':
        next = request.POST.get('next')
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                if next == 'None':
                    return redirect(to='/calendars/top/')
                else:
                    return redirect(to=next)

    else:
        form = LoginForm()
        next = request.GET.get('next')

    param = {
        'form': form,
        'next': next
    }

    return render(request, 'calendars/login.html', param)

def logout_view(request):
    logout(request)

    return render(request, 'calendars/logout.html')

@login_required
def make_schedule_view(request):
    if request.method == 'POST':
        form = MakeSchedule(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form = MakeSchedule()
            return redirect(to='/calendars/top/')
    else:
        form = MakeSchedule()

    month_data = [
        {'first_space': list(range(1, 0+1)), 'day_number': list(range(1, 31+1))},
        {'first_space': list(range(1, 3+1)), 'day_number': list(range(1, 28+1))},
        {'first_space': list(range(1, 3+1)), 'day_number': list(range(1, 31+1))},
        {'first_space': list(range(1, 6+1)), 'day_number': list(range(1, 30+1))},
        {'first_space': list(range(1, 1+1)), 'day_number': list(range(1, 31+1))},
        {'first_space': list(range(1, 4+1)), 'day_number': list(range(1, 30+1))},
        {'first_space': list(range(1, 6+1)), 'day_number': list(range(1, 31+1))},
        {'first_space': list(range(1, 2+1)), 'day_number': list(range(1, 31+1))},
        {'first_space': list(range(1, 5+1)), 'day_number': list(range(1, 30+1))},
        {'first_space': list(range(1, 0+1)), 'day_number': list(range(1, 31+1))},
        {'first_space': list(range(1, 3+1)), 'day_number': list(range(1, 30+1))},
        {'first_space': list(range(1, 5+1)), 'day_number': list(range(1, 31+1))},
    ]

    user_id = request.user.id
    data_1 = Schedules.objects.filter(user_id=user_id , month=1).order_by('day').order_by('hour').order_by('minute')
    data_2 = Schedules.objects.filter(user_id=user_id , month=2).order_by('day').order_by('hour').order_by('minute')
    data_3 = Schedules.objects.filter(user_id=user_id , month=3).order_by('day').order_by('hour').order_by('minute')
    data_4 = Schedules.objects.filter(user_id=user_id , month=4).order_by('day').order_by('hour').order_by('minute')
    data_5 = Schedules.objects.filter(user_id=user_id , month=5).order_by('day').order_by('hour').order_by('minute')
    data_6 = Schedules.objects.filter(user_id=user_id , month=6).order_by('day').order_by('hour').order_by('minute')
    data_7 = Schedules.objects.filter(user_id=user_id , month=7).order_by('day').order_by('hour').order_by('minute')
    data_8 = Schedules.objects.filter(user_id=user_id , month=8).order_by('day').order_by('hour').order_by('minute')
    data_9 = Schedules.objects.filter(user_id=user_id , month=9).order_by('day').order_by('hour').order_by('minute')
    data_10 = Schedules.objects.filter(user_id=user_id , month=10).order_by('day').order_by('hour').order_by('minute')
    data_11 = Schedules.objects.filter(user_id=user_id , month=11).order_by('day').order_by('hour').order_by('minute')
    data_12 = Schedules.objects.filter(user_id=user_id , month=12).order_by('day').order_by('hour').order_by('minute')
    set_of_data = [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10, data_11, data_12]

    params = {'form':form,
              'month_data':month_data,
              'set_of_data':set_of_data
    }

    if 'delete_id' in request.POST:
        delete_id = request.POST['delete_id']
        Schedules.objects.filter(id=delete_id).delete()
        return redirect(to='/calendars/top')

    return render(request, 'calendars/top.html', params)