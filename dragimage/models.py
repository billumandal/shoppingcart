from __future__ import unicode_literals

from django.db import models

class Album(TimeStampedModel):
	title = models.CharField(max_length=250)
	
