'''
Created on 03-Mar-2019

@author: sushil
'''
from django.conf.urls import url
from app.views import anonymous_required
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^/?$',anonymous_required(auth_views.LoginView.as_view()), name="redirect_to_login"),
]