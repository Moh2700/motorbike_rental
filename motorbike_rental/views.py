
from django.http import HttpResponse
from .models import tblmotorbike, bikeuser, Booking
from django.template import loader
from django.views import generic
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
    messages.info(request, "You have been logged out successfully.")
    return redirect('motorbike_rental:index')
    #return redirect('index.html')



@never_cache
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
    return render(request, 'login.html')




'''
def login_view(request):
    # If the user is already inside the session table, let them proceed directly to the index
    if 'bikeuser_id' in request.session:
        return redirect('motorbike_rental:index')

    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        email_input = request.POST.get('email') 

        try:
            # 1. Check if the user is inside the bikeuser database table
            user = bikeuser.objects.get(username=username_input, email=email_input, password=password_input)

            if (user.password == password_input) and (user.email == email_input) and (user.username == username_input):
                # 3. Log them in by saving their credentials to the session
                request.session['bikeuser_id'] = user.id
                request.session['bikeuser_username'] = user.username
                request.session['bikeuser_role'] = user.role
                
                messages.success(request, f"Welcome back, {user.first_name}! Access granted.")
                
                # 4. Proceed to the main application interface
                return redirect('motorbike_rental:index')
            else:
                # Runs if the user exists, but the password was typed incorrectly
                messages.error(request, "Access Denied: Invalid username or password.")
            
            # 2. If they are inside the table, verify their password matches securely
           # if check_password(password_input, user.password):
                
                # 3. Log them in by saving their credentials to the session
            #    request.session['bikeuser_id'] = user.id
            #    request.session['bikeuser_username'] = user.username
            #    request.session['bikeuser_role'] = user.role
            
            #    messages.success(request, f"Welcome back, {user.first_name}! Access granted.")
                
                # 4. Proceed to the main application interface
            #    return redirect('motorbike_rental:index')
            #else:
                # Runs if the user exists, but the password was typed incorrectly
            #    messages.error(request, "Access Denied: Invalid password.")
                
        except bikeuser.DoesNotExist:
            # Runs if the user is completely missing from the bikeuser database table
            messages.error(request, "Access Denied: Username does not exist in our records.")

    # Render the login form if it's a GET request or authentication failed
    return redirect('motorbike_rental:index')
'''

class IndexView(TemplateView):
    
    template_name = 'motorbike_rental/index.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        
        # Add your different database querysets
        # Fetch all motorbikes from the database
        context['bikeslist'] = tblmotorbike.objects.all()

        # Fetch all users from the database
        context['userlist'] = bikeuser.objects.all()
        return context
    
        #context['latest_articles'] = Article.objects.filter(is_published = True).order_by('-pub_date')[:5]
        #context['upcoming_events'] = Event.objects.filter(status='active').order_by('event_date' )[:3]
        #context['featured_products'] = Product.objects.filter(is_featured = True)[:4]

def motorbike_detail(request, bike_id):
    # Fetch the specific motorbike or show a 404 error page
    motorbike = get_object_or_404(tblmotorbike, id=bike_id)
    
    # We pass the motorbike object directly to the template
    
    return render(request, 'motorbike_rental/motorbikedetail.html', {'motorbike': motorbike})

    #return render(request, 'motorbike_rental/motorbike_detail1.html', {'motorbike': motorbike})

def delete_bikeuser(request, user_id):
    # 1. Fetch the user row or throw a 404 page if they don't exist
    user = get_object_or_404(bikeuser, id=user_id)
    
    # 2. Check if the deletion request is submitted via POST
    if request.method == "POST":
        user.delete()  # Removes the row from your database completely
        
        # 3. Redirect back to your home page layout using your namespace
        return redirect('motorbike_rental:index')
        
    # 4. Fallback safeguard: If a user tries to access this URL directly via GET, 
    # redirect them home without doing anything.
    return redirect('motorbike_rental:index')


def edit_bikeuser(request, user_id):
    user = get_object_or_404(bikeuser, id=user_id)

    if request.method == "POST":
        form = MemberForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('motorbike_rental:index')
        else:
            # DEBUGGING: This prints validation errors to your terminal console
            print("Form Validation Errors:", form.errors)
          
    else:
        form = MemberForm(instance=user)
    return redirect('motorbike_rental:index', {'form': form, 'user': user})  


'''
bookings = Booking.objects.filter(
    Q(booking_status="pending") |
    Q(booking_status="active") |
    Q(hiring_status="request")
)
'''
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

        "preparing":[
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

    '''
        "REQUESTED": [
            ("APPROVED", "Approve Booking"),
            ("REJECTED", "Reject Booking")
        ],

        "APPROVED": [
            ("PREPARING", "Start Preparing Bike")
        ],

        "PREPARING": [
            ("READY", "Bike Ready for Collection")
        ],

        "READY": [
            ("ACTIVE", "Confirm Collection")
        ],

        "ACTIVE": [
            ("COMPLETED", "Complete Hire")
        ],

        "COMPLETED": []

    '''
    

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
    print("STATUs:", booking.STATUS_CHOICES)    
    
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

    


def user_list(request):
    users = bikeuser.objects.all().order_by("first_name", "last_name")
    context = {
        "AllUsers": True,
        "userlist": users,
    }

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
    

    
''' 
# current_index = int(0)
# current_index = int(current_index) 
if request.method == "POST":
        action = request.POST.get("action")
        show = request.POST.get("bookingprogress")
       
        show_motorbikebooking = False
        show_bookingprogress = False

        if action == "approved":
            booking.booking_status = "approved"
            booking.save()


        elif action == "rejected":
            booking.booking_status = "rejected"
            booking.save()

        
        
        if show == "true":
            #show_motorbikebooking = False
            #show_bookingprogress = True
            context = {
                "user": user,
                "booking": booking,
                "motorbike": booking.motorbike,
                "show_motorbikebooking": False,
                "show_bookingprogress": True,
                "stages": booking.STATUS_CHOICES,
                "current_index": current_index,
                "actions": next_actions
            }
            return render(request, "motorbike_rental/index.html", context)  

        else:

            #show_motorbikebooking = True
            #show_bookingprogress = False
            context = {
                "user": user,
                "booking": booking,
                "motorbike": booking.motorbike,
                "show_motorbikebooking": True,
                "show_bookingprogress": False,
                "stages": booking.STATUS_CHOICES,
                "current_index": current_index,
                "actions": next_actions
            }
            return render(request, "motorbike_rental/index.html", context)  


    return render(request, "motorbike_rental/index.html", context)  
'''             
          
   
'''
def booking_details(request, bike_id):

    # Logged-in user
    user_id = request.session.get("bikeuser_id")
    if not user_id:
        return JsonResponse({"error": "User not logged in"}, status=401)

    # Get user
    user = get_object_or_404(bikeuser, id=user_id)

    # Get booking for this user and this motorbike
    booking = get_object_or_404(
        Booking.objects.select_related("rentaluser", "motorbike"),
        rentaluser_id=user_id,
        motorbike_id=bike_id
    )

    data = {
        "user": {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "full_name": f"{user.first_name} {user.last_name}",
            "email": user.email,
            "phone": user.phone_number,
            "licence": user.driving_licence_number,
            "address": user.address,
        },
        "booking": {
            "id": booking.id,
            "booking_reference": booking.booking_reference,
            "status": booking.booking_status,
            "status_display": booking.get_booking_status_display(),
            "pickup_date": booking.pickup_date.strftime("%Y-%m-%d"),
            "return_date": booking.return_date.strftime("%Y-%m-%d"),
            
        },
        "motorbike": {
            "id": booking.motorbike.id,
            "make": booking.motorbike.bike_make,
            "model": booking.motorbike.bike_model,
            "registration_number": booking.motorbike.bike_plate_number,
            "daily_rate": float(booking.motorbike.bike_daily_rate),
        }
    }

    return JsonResponse(data)

'''


'''
def booking_details(request, bike_id):

    booking = get_object_or_404(
        Booking.objects.select_related("rentaluser", "motorbike"),
        id=bike_id)

    user_id = request.session.get("bikeuser_id")
    if not user_id:
        return JsonResponse({"error": "User not logged in"}, status=401)
   
    data = {
        "id": booking.id,
        "booking_reference": booking.booking_reference,
        "status": booking.booking_status,
        "status_display": booking.get_booking_status_display(),
        "start_date": booking.start_date.strftime("%Y-%m-%d"),
        "end_date": booking.end_date.strftime("%Y-%m-%d"),

        "rentaluser": {
            "id": booking.rentaluser.id,
            "first_name": booking.rentaluser.first_name,
            "last_name": booking.rentaluser.last_name,
            "email": booking.rentaluser.email,
        },

        "motorbike": {
            "id": booking.motorbike.id,
            "make": booking.motorbike.make,
            "model": booking.motorbike.model,
            "registration_number": booking.motorbike.registration_number,
            "daily_rate": float(booking.motorbike.daily_rate),
        }
    }

    return JsonResponse(data)

'''

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


'''
def manage_motorbikes(request):
    bikes = tblmotorbike.objects.all()
    return render(request, 'motorbike_rental/manage_motorbikes.html', {
        'bikes': bikes
    })
'''

'''
def check_bookingstatus(request):

    bookings = Booking.objects.filter(
        Q(booking_status__in=[
            "pending",
            "active"
        ]) |
        Q(hiring_status="request")
    )

    context = {
        "bookings": bookings
    }

    return render(
        request,
        "admin/bookings.html",
        context
    )
'''


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
            #return redirect('motorbike_rental/index.html') 
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


'''
class IndexView(TemplateView):
    template_name = 'myapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # 1. Public Content (Visible to everyone)
        context['public_articles'] = Article.objects.filter(is_published=True)[:5]

        # 2. Premium Content (Logged-in users only)
        if user.is_authenticated:
            context['premium_content'] = PremiumContent.objects.all()
        else:
            context['premium_content'] = None

        # 3. Staff Content (Users with explicit permissions or staff flags)
        if user.is_staff or user.has_perm('myapp.view_adminlog'):
            context['admin_logs'] = AdminLog.objects.order_by('-timestamp')[:10]
            
        return context
'''        


'''
class IndexView(generic.ListView):
    template_name = 'motorbike_rental/index.html'
    context_object_name = 'bikeslist'

    def get_queryset(self):
        # Fetch all motorbikes from the database
        return tblmotorbike.objects.all()

class IndexView(generic.ListView):
    template_name = 'motorbike_rental/index.html'
    context_object_name = 'userlist'

    def get_queryset(self):
        # Fetch all users from the database
        return bikeuser.objects.all()
'''    

'''
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
'''


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

#def menufile_view(request):
#    return render(request, 'motorbike_rental/pickup2.html')


def menufile_view(request):
    return render(request, 'motorbike_rental/customer_dashboard.html')
