from django.conf.urls import url, include, patterns
from . import views
app_name='dragimage'

urlpatterns = patterns('',
    url(
        regex=r'^(?P<pk>\d+)/ajax-upload/$,
        view=views.AjaxPhotoUploadView.as_view(),
        name='ajax_photo_upload_view',
        ),
    )