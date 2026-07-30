
from django.http import HttpResponse
from .models import tblmotorbike, bikeuser, Booking
from django.template import loader
#from django.views import generic
from .forms import MemberForm, MotorbikeForm

from django.http import  HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from django.views.generic.base import TemplateView
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from datetime import datetime

from django.db.models import Q
from django.http import JsonResponse
from .models import bikeuser  # Your original models.Model class

from django.views.decorators.cache import never_cache


def logout_view(request):

    # Completely wipes out the session dictionary data instantly
    request.session.flush()
    messages.info (request, "You have been logged out successfully.")
    return redirect('motorbike_rental:index')


@never_cache
def login_view(request):
    # If the user is already logged in, bypass the login page
    if 'bikeuser_id' in request.session:
        return redirect('motorbike_rental:index')

    if request.method == "POST":

        # Clear any existing session
        request.session.flush()

        username_input = request.POST.get("username", "").strip()
        email_input = request.POST.get("email", "").strip()
        password_input = request.POST.get("password", "").strip()

        print("========== LOGIN ATTEMPT ==========")
        print("Username:", username_input)
        print("Email:", email_input)

        try:
            # Search by username only
            user = bikeuser.objects.filter(
                username=username_input,
                email=email_input,
                password=password_input,
            ).first()

            if user:
                # Login successful  # Store session information
                print("User found in database.")
                request.session["bikeuser_id"] = user.id
                request.session["bikeuser_username"] = user.username
                request.session["bikeuser_role"] = user.role.lower()
                request.session["bikeuser_first_name"] = user.first_name
                request.session["bikeuser_last_name"] = user.last_name
                
            else:
                messages.error(request, "Invalid login details.")
                

        except bikeuser.DoesNotExist:
            print(f"Login failed: Username '{username_input}' does not exist.")
            messages.error(request, "Access Denied: Username does not exist.")
        
            

        '''
            # Check email
            if user.email != email_input:
                print("Login failed: Incorrect email.")
                messages.error(request, 'Access Denied: Incorrect email address.')

            # Check password
            elif user.password != password_input:
                print("Login failed: Incorrect password.")
                messages.error(request, "Access Denied: Incorrect password.")

            else:
                print("Login successful!")

                # Store session information
                request.session["bikeuser_id"] = user.id
                request.session["bikeuser_username"] = user.username
                request.session["bikeuser_role"] = user.role.lower()
                request.session["bikeuser_first_name"] = user.first_name
                request.session["bikeuser_last_name"] = user.last_name

                messages.success(
                    request,
                    f"Welcome back, {user.first_name}! Access granted."
                )

                return redirect("motorbike_rental:index")

        except bikeuser.DoesNotExist:
            print(f"Login failed: Username '{username_input}' does not exist.")
            messages.error(request, "Access Denied: Username does not exist.")

        except Exception as e:
            print("Unexpected login error:", e)
            messages.error(request, "An unexpected error occurred during login.")
        '''

    return render(request, "motorbike_rental/index.html")


'''
def login_view(request):

    # If the user is already inside the session table, bypass login
    if 'bikeuser_id' in request.session:
        return redirect('motorbike_rental:index')

    if request.method == 'POST':

        request.session.flush()

        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        email_input = request.POST.get('email')

        # 1. Look up the user safely by username only to prevent a crash
        try:
            user = bikeuser.objects.get(username=username_input, email=email_input, password=password_input)

            # 2. Check if the password matches your plain-text database record
            if user.password == password_input:

                # 3. Log them in manually by assigning items to the session cookie
                request.session['bikeuser_id'] = user.id
                request.session['bikeuser_username'] = user.username
                request.session['bikeuser_role'] = user.role.lower()
                request.session['bikeuser_first_name'] = user.first_name
                request.session['bikeuser_last_name'] = user.last_name

                messages.success(request, f"Welcome back, {user.first_name}! Access granted.")
                return redirect('motorbike_rental:index')

            else:
                messages.error(request, "Access Denied: Incorrect password.")

        except bikeuser.DoesNotExist:
            messages.error(request, "Access Denied: Username does not exist.")

    # Render your actual login HTML page on a GET request
    return render(request, 'motorbike_rental/index.html')

'''

class IndexView(TemplateView):

    template_name = 'motorbike_rental/index.html'
def get_context_data(self, **kwargs):

        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)

        role = self.request.session.get("bikeuser_role")
        user_id = self.request.session.get("bikeuser_id")

        if role in ["staff", "admin"]:

            #bookings = Booking.objects.all()
            #Fetch all users from the database
            context['userlist'] = bikeuser.objects.all()

            # Fetch all motorbikes from the database
            context['bikeslist'] = tblmotorbike.objects.all()

        else:
            context['bikeslist'] = tblmotorbike.objects.filter(id=user_id)
            context['userlist'] = bikeuser.objects.filter(id=user_id)

        return context

def show_booking_details(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    # Find current stage position
    current_index = 0

    stages = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("preparing", "Preparing Bike"),
        ("ready", "Ready for Collection"),
        ("active", "Active Hire"),
        ("completed", "Completed"),
        ("rejected", "Rejected"),
        ("cancelled", "Cancelled"),
    ]
    
    for i, (status, _) in enumerate(stages):
    
        if status == booking.booking_status:
            current_index = i
            break

    # Available actions depending on current status
    actions = {
        "pending": [
            ("approved", "Approve Booking"),
            ("rejected", "Reject Booking"),
        ],
   
        "approved": [
            ("preparing", "Start Preparing Bike"),
        ],

        "preparing": [
            ("ready", "Bike Ready for Collection"),
        ],

        "ready": [
            ("active", "Confirm Customer Collection"),
        ],

        "active": [
            ("completed", "Complete Hire"),
        ],

        "completed": [],

        "rejected": [],

        "cancelled": [],
    }


    # Update booking status
    if request.method == "POST":

        new_status = request.POST.get("next_status")

        available_statuses = [
            status[0]
            for status in actions.get(
                booking.booking_status,
                []
            )
        ]


        if new_status in available_statuses:

            old_status = booking.booking_status

            booking.booking_status = new_status
            booking.save()


            print(
                f"Booking {booking.id} changed "
                f"from {old_status} to {new_status}"
            )


            messages.success(
                request,
                "Booking status updated successfully."
            )


        else:

            messages.error(
                request,
                "Invalid booking status change."
            )

        

        return redirect(
            "motorbike_rental:show_booking_details",
            booking_id=booking.id
        )


    next_actions = actions.get(
        booking.booking_status,
        []
    )

    print("Booking Status:", booking.booking_status)
    print("Next Actions:", next_actions)
    
    return render(
        request,
        "motorbike_rental/index.html",
        {
            "user": booking.rentaluser,
            "booking": booking,
            "motorbike": booking.motorbike,
            "show_motorbikebooking": True,
            "errormsg": False,
            "stages": booking.STATUS_CHOICES,
            "current_index": current_index,
            "actions": next_actions
        }
    )

def all_bookings(request):

    bookings = Booking.objects.select_related(
        "rentaluser",
        "motorbike"
    ).all().order_by("-booking_date")

    context = {
        "bookings": bookings,
        "show_allmotorbikebookings": True
    }
    return render(
            request,
            "motorbike_rental/index.html",
            context
    )

from django.http import Http404

def motorbike_detail(request, bike_id):
    booking = (
        Booking.objects.select_related(
            "rentaluser",
            "motorbike"
        )
        .filter(motorbike_id=bike_id)
        .order_by("-booking_date")
        .first()
    )

    if booking is None:
        raise Http404("No booking found for this motorbike.")

    context = {
        "motorbike": booking.motorbike,
        "booking": booking,
        "user": booking.rentaluser,
    }

    rentaluser = booking.rentaluser
    '''
    for field in rentaluser._meta.fields:
    print(f"{field.name}: {getattr(rentaluser, field.name)}")
    '''
    return render(
        request,
        "motorbike_rental/motorbikedetail.html",
        context
    )
'''    
    # Fetch the specific motorbike or show a 404 error page
    motorbike = get_object_or_404(tblmotorbike, id=bike_id)
    # We pass the motorbike object directly to the template

    return render(request, 'motorbike_rental/motorbikedetail.html', {'motorbike': motorbike})
'''

def delete_bikeuser(request, user_id):
    # 1. Fetch the user row or throw a 404 page if they don't exist
    user = get_object_or_404(bikeuser, id=user_id)
    # 2. Check if the deletion request is submitted via POST
    if request.method == "POST":
        user.delete()  # Removes the row from your database completely

        context = {
            "Motorbike_Users": True
        }
        # 3. Redirect back to your home page layout using your namespace
        return render(request, "motorbike_rental/index.html", context)

    
      # 4. Fallback safeguard: If a user tries to access this URL directly via GET, 
      # redirect them home without doing anything.
    return redirect('motorbike_rental:index')

def edit_bikeuser(request, user_id):
    user = get_object_or_404(bikeuser, id=user_id)
    users = bikeuser.objects.all().order_by("first_name", "last_name")
    err = False
    if request.method == "POST":
        form = MemberForm(request.POST, instance=user)

        if form.is_valid():
            user = form.save(commit=False)
            user.role = request.POST.get("role").lower()
            user.save()

            # Tell index page to open Motorbike Users section
            request.session["MotorbikeUsers"] = True
            return render(request, "motorbike_rental/index.html", {
                    "form": form,
                    "errormsg": err,
                    "user": user,
                    "userlist": users,
                    "MotorbikeUsers": True
                })   
            #return redirect("motorbike_rental:index")

        else:
            print("Form Validation Errors:", form.errors)

    else:
        form = MemberForm(instance=user)

    request.session["MotorbikeUsers"] = True
    
    return render(request, "motorbike_rental/index.html", {
        "form": form,
        "errormsg": err,
        "user": user,
        "userlist": users,
        "MotorbikeUsers": True
    })   

def my_bookings(request):

    user_id = request.session["bikeuser_id"]

    bookings = Booking.objects.filter(
        rentaluser_id=user_id
    ).select_related("motorbike")

    context = {
        "bookings": bookings
    }

    return render(request, "customer/my_bookings.html", context)

def get_booking_details(request, bike_id):

    booking = get_object_or_404(
        Booking.objects.select_related(
            "rentaluser",
            "motorbike"
        ),
        motorbike_id=bike_id,
        booking_status__in=[
            "Pending",
            "Approved",
            "Confirmed",
            "Ready",
            "Active"
        ]
    )

    return render(request, 'motorbike_rental:index.html', {"booking": booking})

def booking_details(request, bike_id):

    user_id = request.session.get("bikeuser_id")

    if not user_id:
        return redirect("motorbike_rental:index.html")

    user = get_object_or_404(bikeuser, id=user_id)

    booking = get_object_or_404(
        Booking.objects.select_related("motorbike"),
        rentaluser_id=user_id,
        motorbike_id=bike_id,
    )


    # Booking stages
    stages = [
        ("REQUESTED", "Requested"),
        ("Pending", "PENDING"),
        ("APPROVED", "Approved"),
        ("PREPARING", "Preparing Bike"),
        ("READY", "Ready for Collection"),
        ("ACTIVE", "Active Hire"),
        ("COMPLETED", "Completed"),
    ]

    # Find current stage position
    current_index = 0

    for i, (status, _) in enumerate(stages):

        if status == booking.booking_status:
            current_index = i
            break


    # Available actions
    actions = {

        "pending": [
            ("approved", "Approve Booking"),
            ("rejected", "Reject Booking")
        ],

        "approved": [
            ("preparing", "Start Preparing Bike")
        ],

        "preparing": [
            ("ready", "Bike Ready for Collection")
        ],

        "ready": [
            ("active", "Confirm Collection")
        ],

        "active": [
            ("completed", "Complete Hire")
        ],

        "completed": []
    }
  
    # Get actions AFTER status update
    next_actions = actions.get(
       booking.booking_status,
       []
    )

    context = {
            "user": user,
            "booking": booking,
            "motorbike": booking.motorbike,
            "show_motorbikebooking": True,
            "stages": booking.STATUS_CHOICES,
            "current_index": current_index,
            "actions": next_actions
        }
    print("Current Status:", booking.booking_status)
    print("Actions:", next_actions) 
    
    print(request.POST)
    print(request.POST.get("booking_status"))
    print(request.POST.get("notes")) 
    print("STATUS:", booking.STATUS_CHOICES)    
    
    return render(request, "motorbike_rental/index.html", context)  
    



    '''
    if request.method == "POST":

        booking.booking_status = request.POST.get("booking_status")
        booking.notes = request.POST.get("notes")

        booking.save()

        messages.success(request, "Booking updated successfully.")

        context = {
           "user": user,
           "booking": booking,
           "motorbike": booking.motorbike,
           "show_motorbikebooking": True,
           "stages": booking.STATUS_CHOICES,
           "current_index": current_index,
           "actions": next_actions
        }
        return render(request, "motorbike_rental/index.html", context)

    
    ACTION_TO_STATUS = {
        "approve": "Approved",
        "confirm": "Confirmed",
        "prepare": "Ready",
        "collect": "Active",
        "complete": "Completed",
        "cancel": "Cancelled",
    }

    action = request.POST.get("action")

    if action in ACTION_TO_STATUS:
        booking.booking_status = ACTION_TO_STATUS[action]
    booking.notes = request.POST.get("notes")

    booking.save()

    '''

def users_by_role(request, role):
    users = bikeuser.objects.filter(role__iexact=role)

    context = {
        "AllUsers": True,
        "userlist": users,
        "role": role.title()
    }
    return render(
        request,
        "motorbike_rental/index.html",
        context
    )    
    
def user_list(request):
    users = bikeuser.objects.all().order_by("first_name", "last_name")

    role = request.session.get("bikeuser_role")
    user_id = request.session.get("bikeuser_id")

    context = {
        "AllUsers": True,
        "userlist": users,
        "MotorbikeUsers": False,
    }

    if role in ["staff", "admin"]:
        # Fetch all users from the database
        context['userlist'] = bikeuser.objects.all()
        # Fetch all motorbikes from the database
        context['bikeslist'] = tblmotorbike.objects.all()
    else:
        context['bikeslist'] = tblmotorbike.objects.filter(id=user_id)
        context['userlist'] = bikeuser.objects.filter(id=user_id)

    return render(
        request,
        "motorbike_rental/index.html",
        context
    )    

def motorbike_list(request):
    motorbikes = tblmotorbike.objects.all().order_by("bike_make", "bike_model")
    context = {
        "AllMotorbikes": True,
        "bikeslist": motorbikes,
    }

    return render(
        request,
        "motorbike_rental/index.html",
        context
    )    
      
def get_user_details(request):

    user_id = request.session.get("bikeuser_id")
    if not user_id:
        return JsonResponse({"error": "User not logged in"}, status=401)

    user = get_object_or_404(bikeuser, id=user_id)
    return JsonResponse({
        "first_name": user.first_name,
        "last_name": user.last_name,
        "full_name": f"{user.first_name} {user.last_name}",
        "email": user.email,
        "phone": user.phone_number,
        "licence": user.driving_licence_number,
        "address": user.address,
    })

def hire_motorbike(request, bike_id):
    bike = get_object_or_404(tblmotorbike, id=bike_id)
    bikeuser_id = request.session.get('bikeuser_id')
    rentaluser = get_object_or_404(bikeuser,id=bikeuser_id)

    # Guard Clause: Check authentication state
    # if not bikeuser_id:
    #    messages.error(request, "Please log in to finalize your rental booking.")
    #    return redirect('login') # Point to your app's login URL configuration

    if request.method == "POST":
        
        
        # try:
        # 1. Capture dates securely from POST
        datepickup = request.POST["pickup_date"]
        datereturn = request.POST["return_date"]

        # 2. Parse strings into Python datetime objects
        pickup_date = datetime.strptime(datepickup, "%Y-%m-%d").date()
        return_date = datetime.strptime(datereturn, "%Y-%m-%d").date()

        # 3. Secure Server-Side Calculation (Prevents client tampering)
        calculated_days = (return_date - pickup_date).days
        
        if calculated_days <= 0:
            messages.error(request, "Return date must be after the pickup date.")
            return render(request, 'motorbike_rental/index.html', {'bike': bike})

        # Calculate total cost against database rates
        calculated_price = calculated_days * bike.bike_daily_rate

        # 4. Generate transaction record using verified server numbers
        Booking.objects.create(
            rentaluser=rentaluser,
            motorbike=bike,
            pickup_date=pickup_date,
            return_date=return_date,
            total_days=calculated_days,
            total_price=calculated_price,
            booking_status="pending",
            hiring_status="request"
        )

        messages.success(request, f"Successfully requested rental for {bike.bike_make}!")
        #return redirect('motorbike_rental/index.html') # Standard practice: Redirect after successful POST
        return redirect('motorbike_rental:index')
        #except (ValueError, KeyError) as error:
        # messages.error(request, "Invalid form submissions. Please verify rental dates.")
          
    return render(request, 'motorbike_rental:index.html', {'bike': bike})

def add_bikeuser(request):
    if request.method == "POST":

        context = {
            "Motorbike_Users": True
        }
        form = MemberForm(request.POST)

        if form.is_valid():
            form.save()
            #return redirect("motorbike_rental:index")
            return render (request, 'motorbike_rental:index', context)
    else:
        form = MemberForm()

    #return render(request, "add_bikeuser.html", {"form": form})
    return render (request, 'motorbike_rental:index', context)

def add_motorbike(request):
    if request.method == 'POST':
        # Use .get() to safely fall back to None or an empty string if a field is empty
        bike_make = request.POST.get('bike_make')
        bike_model = request.POST.get('bike_model')
        bike_plate_number = request.POST.get('bike_plate_number')
        bike_year = request.POST.get('bike_year')
        bike_imgsrc = request.POST.get('bike_imgsrc')
        bike_status = request.POST.get('bike_status')
        bike_daily_rate = request.POST.get('bike_daily_rate')

    # Basic validation check to prevent empty database rows
        if bike_make and bike_model and bike_plate_number:
            
            # Optional but recommended: Cast numeric fields if your model requires it
            # try:
            #     bike_year = int(bike_year) if bike_year else None
            #     bike_daily_rate = float(bike_daily_rate) if bike_daily_rate else 0.0
            # except ValueError:
            #     messages.error(request, "Invalid number format for year or rate.")
            #     return render(request, 'motorbike_rental/index.html')


            tblmotorbike.objects.get_or_create(
                bike_make=bike_make,
                bike_model=bike_model,
                bike_plate_number=bike_plate_number,
                bike_year=bike_year,
                bike_imgsrc=bike_imgsrc,
                bike_status=bike_status,
                bike_daily_rate=bike_daily_rate
            )
            # Optional: Add a success message for the user
            messages.success(request, "Motorbike added successfully!")
            
            # Redirect using the URL pattern NAME 'index' from your urls.py
            return render(request, 'motorbike_rental/index.html')
        else:
            # Handle validation failure
            messages.error(request, "Required fields are missing.")   

        # Redirect using the URL pattern NAME 'index' from your urls.py
        return render(request, 'motorbike_rental/index.html')
    
    return render(request, 'motorbike_rental/index.html')

def edit_motorbike(request, bike_id):
    bike = get_object_or_404(tblmotorbike, id=bike_id)

    if request.method == "POST":
        form = MotorbikeForm(request.POST, instance=bike)
        print(request.POST) 
        if form.is_valid():
            form.save()
            # CRUCIAL FIX: Redirect after saving data
            return redirect('motorbike_rental:index')
    else:
        form = MotorbikeForm(instance=bike)

    return render(request, 'motorbike_rental/index.html', {'form': form})

def delete_motorbike(request, bike_id):

    bike = get_object_or_404(tblmotorbike, id=bike_id)

    if request.method == 'POST':
        bike.delete()
        return redirect('motorbike_rental:index')
    return redirect('motorbike_rental:index')

def registeruser(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        phone_number = request.POST.get('phone_number')
        date_of_birth = request.POST.get('date_of_birth')
        driving_licence_number = request.POST.get('driving_licence_number')
        role = request.POST.get('role')

        bikeuser.objects.get_or_create(
            username=username,
            email=email,
            address=address,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            driving_licence_number=driving_licence_number,
            role=role
        )
        return render(request, 'motorbike_rental/index.html')
    
    return render(request, 'motorbike_rental/index.html')

def customers_view(request):
    # Fetch all customers from the database
    customers = bikeuser.objects.all()
    # Load the 'customers.html' template
    template = loader.get_template('motorbike_rental/customers.html')
    # Create a context dictionary to pass to the template
    context = {
        'customerslist': customers
    } 
    # Render the template with the context and return an HttpResponse  
    return HttpResponse(template.render(context, request))

def tblmotorbikes_view(request):
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
    # return render(request, 'customers.html')

