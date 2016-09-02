from django.conf.urls import include, url

urlpatterns = [ 
    url(r'^$', 'main.views.home', name='home'),

]
urlpatterns +=staticfiles_urlpatterns()