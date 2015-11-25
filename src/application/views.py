
#-*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic import TemplateView
import datetime
from django.views.generic.edit import FormView
#from django import oldforms as forms
#from django.http import HttpResponseRedirect
#from django.shortcuts import render_to_response
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth


def hello(request):
    return HttpResponse("Здравствуй, Мир")




def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect("/")
    else:
        # Отображение страницы с ошибкой
        return HttpResponseRedirect("/account/invalid/")
def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/account/loggedout/")    