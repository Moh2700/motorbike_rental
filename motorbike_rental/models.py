from django.db import models

# Create your models here.
"""
class Warehouse(object):
    def __init__(self):
        self.contents = ["bike1", "bike2", "bike3", "bike4", "bike5"]

    def list_contents(self):
        return self.contents

    def take(self, name, bike):
        self.contents.remove(bike)
        print("{0} took the {1}.".format(name, bike))

    def store(self, name, bike):
        self.contents.append(bike)
        print("{0} stored the {1}.".format(name, bike))

        
from __future__ import print_function
import sys

if sys.version_info < (3, 0):
    input = raw_input


class Person(object):
    def __init__(self, name):
        self.name = name

    def visit(self, warehouse):
        print("This is {0}.".format(self.name))
        self.deposit(warehouse)
        self.retrieve(warehouse)
        print("Thank you, come again!")

    def deposit(self, warehouse):
        print("The warehouse contains:", warehouse.list_contents())
        bike = input("Type the bike you want to store (or empty): ").strip()
        if bike:
            warehouse.store(self.name, bike)

    def retrieve(self, warehouse):
        print("The warehouse contains:", warehouse.list_contents())
        bike = input("Type the bike you want to take (or empty): ").strip()
        if bike:
            warehouse.take(self.name, bike)

            
class Note(models.Model):
    
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'client_note'

    @property
    def note_year(self):
        return self.created.strftime('%Y')

    def __unicode__(self):
        return '%s' % self.note
"""    


class tblmotorbike (models.Model):
    
    bike_make = models.CharField(max_length=20)
    bike_model = models.CharField(max_length=10)
    bike_year = models.CharField(max_length=10)
    bike_price = models.CharField(max_length=10, blank=True, null=True)
    bike_imgsrc = models.TextField()

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Maintenance'),
    ]

    bike_plate_number = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
    )
    bike_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available',
    )
    bike_daily_rate = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True,
    )

    def __str__(self):
        return (
            f"{self.bike_make} {self.bike_model}"
            f"{self.bike_year} {self.bike_imgsrc}"
        )


# Create your models here.
class motorbike (models.Model):
    
    bike_make = models.CharField(max_length=20)
    bike_model = models.CharField(max_length=10)
    bike_year = models.CharField(max_length=10)
    bike_imgsrc = models.CharField()

    """
    @property
    def bike_year(self):
        return self.year('%Y')

    def __init__(self, bikemake, bikemodel, bikeyear, bikeimgsrc ):
        self.bike_make = bikemake
        self.bike_model = bikemodel
        self.bike_year = bikeyear
        self.bike_imgsrc = bikeimgsrc
    """

    def __str__(self):
        return (
            f"{self.bike_make} {self.bike_model} "
            f"{self.bike_year} {self.bike_imgsrc}"
        )


class customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"