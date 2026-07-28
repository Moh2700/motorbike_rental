
'''
bookings = Booking.objects.filter(
    Q(booking_status="pending") |
    Q(booking_status="active") |
    Q(hiring_status="request")
)
'''

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

#def menufile_view(request):
#    return render(request, 'motorbike_rental/pickup2.html')


#def menufile_view(request):
#    return render(request, 'motorbike_rental/customer_dashboard.html')



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


'''
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
    return redirect("motorbike_rental:index")
'''
