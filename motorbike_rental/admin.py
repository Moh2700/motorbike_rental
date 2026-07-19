from django.contrib import admin
from .models import tblmotorbike
from .models import bikeuser
from .models import Booking

admin.site.register(tblmotorbike)
admin.site.register(bikeuser)
admin.site.register(Booking)

