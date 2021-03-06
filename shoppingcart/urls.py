"""shoppingcart URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from cart.views import home, ListProductView, ListTransactionView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import urls, views
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

urlpatterns = [ 
    url(r'^$', home, name='home'),
    # url(r'^$', lambda r: HttpResponseRedirect('index')),
    # url(r'^$', TemplateView.as_view(template_name='index.html' ), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^productlist/$', ListProductView.as_view(), name='productlist'),
    url(r'^transactionlist/$', ListTransactionView.as_view(), name='transactionlist'),
    url(r'^usertest/$', TemplateView.as_view(template_name='./registration/usertest.html' ), name='usertest'),
    url(r'^cart/', include('cart.urls', namespace='cart', app_name='cart')),
    url(r'^register_activate/', include('register_activate.urls', namespace='registration', app_name='register_activate')),
    url(r'^dragimage/', include('dragimage.urls', namespace='dragimage', app_name='dragimage')),
    
]

urlpatterns += staticfiles_urlpatterns()