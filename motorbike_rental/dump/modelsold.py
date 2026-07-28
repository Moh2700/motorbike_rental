
from django.db import models
from django.utils import timezone
import uuid

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
        default='available',
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


class motorbike (models.Model):
    bike_make = models.CharField(max_length=20)
    bike_model = models.CharField(max_length=10)
    bike_year = models.CharField(max_length=10)
    bike_imgsrc = models.CharField(max_length=255)

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


class bikeuser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    username = models.CharField(blank=True, null=True, max_length=30)
    password = models.CharField(blank=True, null=True, max_length=30)
  
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    ]

    phone_number = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    driving_licence_number = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



def generate_booking_reference():
    return "BK-" + str(uuid.uuid4())[:8].upper()

class Booking(models.Model):

    rentaluser = models.ForeignKey(
         bikeuser,
         on_delete=models.CASCADE
    )

    motorbike = models.ForeignKey(
        tblmotorbike,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    pickup_date = models.DateField()
    return_date = models.DateField()
    total_days = models.IntegerField(default=1)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
  
    booking_date = models.DateTimeField(
        auto_now_add=True
    )

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("preparing", "Preparing"),
        ("ready", "Ready for Collection"),
        ("active", "Active Hire"),
        ("completed", "Completed"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]
   
    HIRING_STAGES = [
        ("request", "Request"),
        ("verification", "Verification"),
        ("confirmation", "Confirmation"),
        ("ready", "Ready"),
        ("collection", "Collection"),
        ("completion", "Completion"),
    ]

    booking_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    hiring_status = models.CharField(
        max_length=20,
        choices=HIRING_STAGES,
        default="request"
    )

    licence_verified = models.BooleanField(default=False)
    age_verified = models.BooleanField(default=False)
    identity_verified = models.BooleanField(default=False)
    payment_verified = models.BooleanField(default=False)

    payment_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    payment_date = models.DateTimeField(
        null=True,
        blank=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    booking_reference = models.CharField(
        max_length=20,
        null=True,
        default=generate_booking_reference,
        editable=False
    )
    
    verified_date = models.DateTimeField(
        null=True,
        blank=True
    )
   

    def __str__(self):
        return f"{self.rentaluser.username} - {self.motorbike.bike_model}"


def save(self, *args, **kwargs):
    if not self.booking_reference:
        self.booking_reference = "BK-" + str(uuid.uuid4())[:8].upper()

    super().save(*args, **kwargs)

   
'''
class user(models.Model):
    CUSTOMER = "customer"
    STAFF = "staff"
    ADMIN = "admin"

    ROLE_CHOICES = [
        (CUSTOMER, "Customer"),
        (STAFF, "Staff"),
        (ADMIN, "Admin"),
    ]

    phone_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)

    driving_license_number = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
    )

    address = models.TextField(blank=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER
    )

    #profile_picture = models.ImageField(
    #    upload_to="profile_pictures/",
    #    null=True,
    #    blank=True
    #)

    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
python         return self.username
'''

