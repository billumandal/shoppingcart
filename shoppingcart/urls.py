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
from cart import views
from cart.views import home, ListProductView, ListTransactionView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import urls, views
from django.views.generic import TemplateView

urlpatterns = [ 
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^register_activate/', include('register_activate.urls')),
    url(r'^productlist/$', ListProductView.as_view(), name='productlist'),
    # url(r'^transactionlist/$', ListTransactionView.as_view(), name='transactionlist'),
    url(r'^$', TemplateView.as_view(template_name='index.html' ), name='home'),
    url(r'^usertest/$', TemplateView.as_view(template_name='./registration/usertest.html' ), name='usertest'),
    
    # ____________________________________________________________________________________________________________
    # url(r'^login/$', 'django.contrib.auth.views.login', name='auth_login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),

    # url(r'^password_change/$', 'django.contrib.auth.views.PasswordChangeView.as_view()', name='password_change'),
    # url(r'^password_change/done/$', 'django.contrib.auth.views.PasswordChangeDoneView.as_view()', name='password_change_done'),
    # url(r'^password_reset/$', 'PasswordResetView.as_view()', name='password_reset'),
    # url(r'^password_reset/done/$', 'django.contrib.auth.views.PasswordResetDoneView.as_view()', name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     'django.contrib.auth.views.PasswordResetConfirmView.as_view()', name='password_reset_confirm'),
    # url(r'^reset/done/$', 'django.contrib.auth.views.PasswordResetCompleteView.as_view()', name='password_reset_complete'),
    # url(r'^$', TemplateView.as_view(template_name='password_change_form.html' ), name='auth_password_change'),
    # url(r'^change_password/$', 'django.contrib.auth.views.logout', name='auth_password_change'),
    # ____________________________________________________________________________________________________________

    # url(r'^register/$', 'register'),
    # url(r'^activate/(?P<key>.+)$', 'activation'),
    # url(r'^new-activation-link/(?P<user_id>\d+)/$', 'new_activation_link'),
]

urlpatterns += staticfiles_urlpatterns()