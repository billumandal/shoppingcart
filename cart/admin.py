from django.contrib import admin
from django.contrib.auth.models import User
from models import Transaction, Product, UserProfile

class TransactionInline(admin.TabularInline):
	model = Transaction

class TransactionAdmin(admin.ModelAdmin):
	fields = ('time', 'sellerid', 'buyerid', 'product_name', 'quantity', 'image')
	list_filter = ('time',)
	
class UserProfileAdmin(admin.ModelAdmin):
	#I want to display the list of products for sellers
	#and sort with list of transactions for buyers, how to?
	list_display = ('user', 'role', 'address',)
	search_fields = ('user',)
	# list_filter = ('transactions')
	# How to sort via the amount of transactions here
	inlines = [ 
		TransactionInline,
		]

class ProductAdmin(admin.ModelAdmin): #have to make a form and template for this one
	list_display = ('product_name', 'price')
	fields = ('product_name', 'sellerid', 'price', 'selling_starts_on', 'selling_ends_on', 'despatched_from','image') 
	list_filter = ('selling_starts_on',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Transaction, TransactionAdmin)