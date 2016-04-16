from django import forms
from django.core.exceptions import ValidationError

from cart.models import Product, UserProfile

class ProductForm(forms.Form):

	class Meta:
		model = Product

	productname = forms.CharField(label="Name of the Proudct", max_length=255, widget=forms.TextInput,)
	price = forms.IntegerField(label="Price of the item: Rs.")
	selling_starts_on = forms.DateField(label="Selling Starts On")
	selling_ends_on = forms.DateField(label="Selling Ends On")
	despatched_from = forms.CharField(label="Item despatched from", max_length=30)
	image = forms.ImageField(label="Optionally Add an Image of the Product")

	error_css_class = 'error'
	required_css_clss = 'required'