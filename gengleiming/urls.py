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
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^fortestapp/', include("allapps.fortestapp.urls", namespace='fortestapp')),
    url(r'^accounts/', include("django.contrib.auth.urls", namespace='accounts')),
    url(r'^record/', include("allapps.record.urls", namespace='record')),
    url(r'^cms/', include("allapps.cms.urls", namespace='cms')),
    url(r'^success/', views.SuccessView.as_view(), name="success"),
    url(r'^fail/', views.FailView.as_view(), name="fail"),
]

urlpatterns += staticfiles_urlpatterns()  # 配置{% load static %}：runserver无需此步骤，其他服务器需要，当然用{% load staticfiles %}标签可代替此步骤
