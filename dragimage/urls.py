from django.conf.urls import include, url
from views import upload_picture, home, index, fourthTry

urlpatterns = [ 
    url(r'^first/$', home, name='home'),
    url(r'^second/$', upload_picture, name='upload_picture'),
    url(r'^third/$', index, name='index'),
    url(r'^fourth/$', fourthTry, name='fourthtry'),

]
# urlpatterns +=staticfiles_urlpatterns()