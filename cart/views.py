from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator 
from cart.models import Transaction, Product

def home(request):
	return render(request, 'index.html')

def hello_world(request):
	return HttpResponse("Hello World")

class LoggedInMixin(object):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ListTransactionView(LoggedInMixin, ListView):

	model = Transaction
	template_name = 'transaction_list.html'

	def get_queryset(self):

		return Transaction.objects.all
		# return Transaction.objects.filter(owner=self.request.user)

class ListProductView(ListView):

	model = Product
	template_name = 'product_list.html'
