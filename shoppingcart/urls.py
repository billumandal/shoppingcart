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
from django.conf.urls import url
from django.contrib import admin
from cart import views
from cart.views import home, ListProductView, ListTransactionView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout

urlpatterns = [ 
    url(r'^$/', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^productlist/$', ListProductView.as_view(), name='productlist'),
    url(r'^transactionlist/$', ListTransactionView.as_view(), name='transactionlist'),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^login/$', logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()