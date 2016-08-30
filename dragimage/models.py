from __future__ import unicode_literals

from django.db import models

class Album(TimeStampedModel):
	title = models.CharField(max_length=250)
	description = models.TextField(blank=True, null=True)
	cover_photo = models.ForeignKey('Photo', related_name='+', blank=True, null=True)
	is_public = models.BooleanField(default=True)
	date_added = models.DateField(null=True, blank=True)
	tags = TaggableManager(balnk=True, help_text=None)
	order = models.PositiveIntegerField(default=9999)

class Photo(TimeStampedModel):
	album = models.ForeignKey(Album)
	file = models.ImageField(upload_to=upload_to)
	description = models.TextField(blank=True, null=True)
	is_public = models.BooleanField(default=True)
	tags = TaggableManager(blank=True, help_text=None)
