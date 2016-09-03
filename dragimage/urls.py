from django.conf.urls import include, url

urlpatterns = [ 
    url(r'^$', 'dragimage.views.home', name='home'),

]
# urlpatterns +=staticfiles_urlpatterns()