from django.conf.urls import include, url
from views import home, ListProductView, ListTransactionView, AddProductView

urlpatterns = [ 
    url(r'^productlist/$', ListProductView.as_view(), name='productlist'),
    url(r'^transactionlist/$', ListTransactionView.as_view(), name='transactionlist'),
    # url(r'^third/$', index, name='index'),
    # url(r'^fourth/$', fourthTry, name='fourthtry'),

]
