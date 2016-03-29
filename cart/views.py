from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorator import login_required
from cart.models import Transaction, Product

def home(request):
	return render(request, 'index.html')

def hello_world(request):
	return HttpResponse("Hello World")

class ListTransactionView(ListView):

	model = Transaction
	template_name = 'transaction_list.html'

class ListProductView(ListView):

	model = Product
	template_name = 'product_list.html'
