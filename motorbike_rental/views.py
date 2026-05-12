from django.shortcuts import render
from django.http import HttpResponse
#from .models import Customer, MotorBike, tblMotorBike
from django.template import loader

def index(request):
     # Fetch all motorbikes from the database
    #motorbikes = tblMotorBike.objects.all()
    # Load the 'index.html' template
    #template = loader.get_template('index.html')
    # Create a context dictionary to pass to the template
    #context = {
    #    'bikeslist': motorbikes
    # } 
    # Render the template with the context and return an HttpResponse  
    #return HttpResponse (template.render(context, request))
    return render(request, 'index.html')


def booking_form_view(request):
    return render(request, 'booking_form.html')
