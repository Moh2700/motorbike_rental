from django.shortcuts import render
from django.http import HttpResponse
from .models import tblmotorbike, customer
from django.template import loader

def index(request):
    # Fetch all motorbikes from the database
    motorbikes = tblmotorbike.objects.all()
    # Load the 'index.html' template
    template = loader.get_template('index.html')
    # Create a context dictionary to pass to the template
    context = {
        'bikeslist': motorbikes
     } 
    # Render the template with the context and return an HttpResponse  
    return HttpResponse(template.render(context, request))
    # return render(request, 'index.html')

def customers_view(request):
    # Fetch all customers from the database
    customers = customer.objects.all()
    # Load the 'customers.html' template
    template = loader.get_template('customers.html')
    # Create a context dictionary to pass to the template
    context = {
        'customerslist': customers
    } 
    # Render the template with the context and return an HttpResponse  
    return HttpResponse(template.render(context, request))

def booking_form_view(request):
    return render(request, 'booking_form.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def products_view(request):
    return render(request, 'products.html')

def admin_view(request):
    return render(request, 'admin.html')
