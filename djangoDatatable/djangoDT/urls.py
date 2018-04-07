
from django.conf.urls import url
from .views import viewCustomer,homepage
urlpatterns = [
    url(r'^$', homepage,name='homepage'),
    url(r'^customers/$', viewCustomer,name='viewCustomer'),
]
