from __future__ import unicode_literals
from django.db import models
import os

def get_upload_path(instance, filename):
    # creates unique path and filename for upload
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.p_uid.ext)
    d = date.today()
    username = instance.author.username

    # Create the directory structure
    return os.path.join(
        'userpics', username, d.strftime('%Y'), d.strftime('%m'), filename
    )

class UploadFile(models.Model):
    file = models.FileField(upload_to='../dragimage_pictures/%Y/%m/%d')

class Picture(models.Model):
    file = models.ImageField(upload_to=get_upload_path)

class CustomerProfile(models.Model):
    customer_id  = models.CharField(db_column='customer_id', primary_key=True, max_length=20)  
    first_name   = models.CharField(db_column='first_name', max_length=30, blank=True, null=True) 
    last_name    = models.CharField(db_column='last_name', max_length=30,blank=True,null=True) 
    user_name    = models.CharField(db_column='user_name', max_length=50,unique=True)  
    phone_number = models.CharField(db_column='phone_number', max_length=15,blank=True,null=True)
    email_id     = models.EmailField(db_column='email_id', max_length=50,blank=True, null=True)  
    user_image1 = models.ImageField(upload_to=get_upload_path, db_column='user_image1', max_length=100)  
    user_image2 = models.ImageField(upload_to=get_upload_path, db_column='user_image2', max_length=100)  
    user_image3 = models.ImageField(upload_to=get_upload_path, db_column='user_image3', max_length=100)  
    user_image4 = models.ImageField(upload_to=get_upload_path, db_column='user_image4', max_length=100) 
    user_image5 = models.ImageField(upload_to=get_upload_path, db_column='user_image5', max_length=100)

class FourthTry(models.Model):
    picture_name = models.CharField(blank=True, max_length=50)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d')
    picture_description = models.CharField(blank=True, max_length=300)
    picture_tag = models.CharField(blank=True, max_length=50)