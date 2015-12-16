"""
1.login
2.registration
3.
urlpatterns = patterns('',
    url('register/', CreateView.as_view(
            template_name='login_test.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
urlpatterns = [
    url(r'^login/$', TemplateView.as_view(template_name="login.html")),
   
    url(r'^test/$', TemplateView.as_view(template_name="test.html")),
    url(r'login_test/$',  login),
    url(r'^registration/$', TemplateView.as_view(template_name="registration.html")),
    url(r'^login_test/$', TemplateView.as_view(template_name="login_test.html")),

 url(r'^registration/$', TemplateView.as_view(template_name="registration.html")),
"""
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.contrib import admin
from userstore.views import *

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',
   # url('^register',login_user),
    #url(r'^register', 'django.contrib.auth.views.login'),
    #url('^accounts/', include('django.contrib.auth.urls')),
    #url(r'^login/$', TemplateView.as_view(template_name="login.html")),
   
    url(r'^test/$', TemplateView.as_view(template_name="test.html")),
   # url(r'login_test/$',  login_user),
    url(r'^registration/$', TemplateView.as_view(template_name="registration.html"), name='registration'),
    #url(r'^login_test/$', TemplateView.as_view(template_name="login_test.html")),
                       
    url(r'^accounts/login/$', 'userstore.views.login'),
    url(r'^accounts/auth/$', 'userstore.views.auth_view'),
    url(r'^accounts/logout/$', 'userstore.views.logout'),
    url(r'^accounts/loggedin/$', 'userstore.views.loggedin'),
    url(r'^accounts/invalid/$', 'userstore.views.invalid_login'),
    # rest of your URLs as normal
)

