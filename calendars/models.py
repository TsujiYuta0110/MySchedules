from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import models
from django.utils import timezone

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass

class Schedules(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.IntegerField('月', choices=[(i, i) for i in range(1, 13)])
    day = models.IntegerField('日', choices=[(i, i) for i in range(1, 32)])
    hour = models.IntegerField('時', choices=[(i, i) for i in range(0, 24)])
    minute = models.IntegerField('分', choices=[(i, i) for i in range(0, 60)])
    title = models.CharField('タイトル', max_length=20)
    text = models.TextField('内容')

    def __str__(self):
        return self.title

class MakeSchedule(forms.ModelForm):
    class Meta:
        model = Schedules
        exclude = ['user']
        fields = ['month', 'day', 'hour', 'minute', 'title', 'text']