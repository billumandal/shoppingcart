from __future__ import unicode_literals
from django.db import models
from shoppingcart import settings
import os

class UploadFile(models.Model):
<<<<<<< Updated upstream
    file = models.FileField(upload_to='BASE_DIR/product_pictures/%Y/%m/%d')
=======
    file = models.FileField(upload_to='~/../product_pictures/%Y/%m/%d')
>>>>>>> Stashed changes
