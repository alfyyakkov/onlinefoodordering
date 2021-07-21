"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'hi/',Welcome,name='Welcome'),
    url(r'^food/',Foodapp,name='foodapp'),
    url(r'^login/',Login,name='Login'),
    url(r'^fileup/',Newitem,name='additem'),
    url(r'^items/',ItemDisplay,name='Items'),
    url(r'^view/',Items,name='Items'),
    url(r'^home/',HomePage,name='home'),
    url(r'^order/(\w+)/',Ordering,name='order'),
    url(r'^test/',testingorder,name='ordering'),
    url(r'^bill/',BillAmount,name='bill'),
    url(r'^orders/',ViewOrders,name='orders'),
]
