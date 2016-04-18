from django import forms
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
from cart.models import Product, UserProfile

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		exclude = ('sellerid',)

	# productname = forms.CharField(label="Name of the Product", max_length=255, widget=forms.TextInput,)
	# price = forms.IntegerField(label="Price of the item: Rs. ")
	# selling_starts_on = forms.DateField(label="Selling Starts On ", widget=AdminDateWidget)
	# selling_ends_on = forms.DateField(label="Selling Ends On ", widget=AdminDateWidget)
	# despatched_from = forms.CharField(label="Item despatched from ", max_length=30)
	# image = forms.ImageField(label="Optionally add an Image of the Product")

	error_css_class = 'error'
	required_css_clss = 'required'