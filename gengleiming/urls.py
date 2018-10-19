"""gengleiming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name="home"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('cms/', include("allapps.cms.urls", namespace="cms")),
    path('success/', views.SuccessView.as_view(), name="success"),
    path('fail/', views.FailView.as_view(), name="fail"),
    path('unicode_test/', views.unicode_test, name="unicode_test"),
]

# 配置{% load static %}：runserver无需此步骤，其他服务器需要，当然用{% load staticfiles %}标签可代替此步骤
urlpatterns += staticfiles_urlpatterns()
