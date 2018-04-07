from django.shortcuts import render
from .models import Customer
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, "djangoDT/homepage.html")

def viewCustomer(request):
    customers = Customer.objects.all()
    customerjson = serializers.serialize('json', customers)
    return HttpResponse(customerjson, content_type='application/json')