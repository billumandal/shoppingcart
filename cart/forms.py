from django import forms
from django.core.exceptions import ValidationError

from cart.models import Product, UserProfile

class ProductForm(forms.Form):

	class Meta:
		model = Product

	productname = form.CharField(label=_("Name of the Proudct"), max_lenght=255, widget=forms.TextInput,)
	price = forms.PositiveIntegerField(label=_("Price of the item: Rs."))
	selling_starts_on = forms.DateField(label=_("Selling Starts On"))
	selling_ends_on = forms.DateField(label=_("Selling Ends On"))
	despatched_from = forms.CharField(label=_("Item despatched from"), max_lenght=30)
	image = forms.ImageField(label=_("Optionally Add an Image of the Product"))

	error_css_class = 'error'
	required_css_clss = 'required'