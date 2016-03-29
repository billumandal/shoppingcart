from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

class UserProfile(models.Model):
	ROLE = (
		('seller', 'Seller'),
		('buyer', 'Buyer'),
		('both', 'Both'),
		)

	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	phone_number = models.PositiveIntegerField(null=True)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=30)
	postal_code = models.PositiveIntegerField(null=True)
	role = models.CharField(max_length=10, choices=ROLE, null=False)

	# def __unicode__(self):
	# 	return self.user

	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)

	post_save.connect(create_user_profile, sender=User)

class Product(models.Model):
	product_name = models.CharField(max_length=100)
	sellerid = models.ManyToManyField(User)
	price = models.IntegerField()
	image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
	selling_started_on = models.DateField(null=True)
	selling_ends_on = models.DateField(null=True)
	despatched_from = models.CharField(max_length=50)

	def __unicode__(self):
		# return self.id
		return self.product_name

class Transaction(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	seller = models.ForeignKey(UserProfile, related_name = 'transaction_seller')
	buyer = models.ForeignKey(User, related_name = 'transaction_buyer')
	product_name = models.ForeignKey(Product)
	quantity = models.PositiveIntegerField(null=False)
	discount = models.IntegerField()
	despatch_time = models.DateTimeField()
	# received_time = models.DateTimeField(blank=True, null=True) #commented as I've to generate only till the invoice

	def save(self, *args, **kwargs):
		self.slug = slugify(self.id)
		super(Transaction, self).save(*args, **kwargs)

	def __unicode__(self):
		return "Transaction ID is {}".format(self.id)
		return "The transaction was for {} {} done on {}.".format(self.quantity, self.product, self.time)
		return "The buyer was {} and the seller was {}.".format(self.buyer, self.seller)