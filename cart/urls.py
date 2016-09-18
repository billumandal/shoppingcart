from django.conf.urls import include, url
from views import home, ListProductView, ListTransactionView, AddProductView
from django.views.generic import TemplateView

urlpatterns = [ 
    url(r'^productlist/$', ListProductView.as_view(), name='productlist'),
    url(r'^transactionlist/$', ListTransactionView.as_view(), name='transactionlist'),
    url(r'^addproduct/$', TemplateView.as_view(template_name='./add_product.html' ), name='add_product'),
    # url(r'^fourth/$', fourthTry, name='fourthtry'),

]
