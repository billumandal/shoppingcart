from django.shortcuts import render
from django.views.generic import View

from braces.views import (
	AjaxResponseMixin,
	JSONResponseMixin,
	LoginRequiredMixin,
	SuperuserRequiredMixin,
)

from shoppingcart.dragimage.models import Album, Photo

