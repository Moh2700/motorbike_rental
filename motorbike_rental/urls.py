
from django.urls import path
from motorbike_rental import views

app_name = 'motorbike_rental'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.login_view, name='login'),
    path('go_dashboard/', views.go_dashboard, name='go_dashboard'),
    path('motorbike_list/', views.motorbike_list, name='motorbike_list'),
    path('user_list/', views.user_list, name='user_list'),
    path('logout/', views.logout_view, name='logout'),
    path('get_user_details/', views.get_user_details, name='get_user_details'),
    path('get_user_profile/', views.get_user_profile, name='get_user_profile'),
    path(
        'edit_bikeuser/<int:user_id>/',
        views.edit_bikeuser,
        name='edit_bikeuser',
    ),
    path(
        'delete_bikeuser/<int:user_id>/',
        views.delete_bikeuser,
        name='delete_bikeuser',
    ),
    path(
        'hire_motorbike/<int:bike_id>/',
        views.hire_motorbike,
        name='hire_motorbike',
    ),
    path(
        'motorbike_detail/<int:bike_id>/',
        views.motorbike_detail,
        name='motorbike_detail',
    ),
    path(
        'show_booking_details/<int:booking_id>/',
        views.show_booking_details,
        name='show_booking_details',
    ),
    path('delete_motorbike/<int:bike_id>/', views.delete_motorbike, name='delete_motorbike'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('add_motorbike/', views.add_motorbike, name='add_motorbike',),
    path(
        'edit_motorbike/<int:bike_id>/',
        views.edit_motorbike,
        name='edit_motorbike',
    ),
    path(
        'add_bikeuser/',
        views.add_bikeuser,
        name='add_bikeuser'
    ),
    path(
        'all_bookings/',
        views.all_bookings,
        name="all_bookings"
    ),
    path(
        'booking_details/<int:booking_id>/',
        views.booking_details,
        name="booking_details"
    ),
    path("users_by_role/<str:role>/", views.users_by_role, name="users_by_role")
]

'''
    path(
        'all_bookings/',
        views.all_bookings,
        name="all_bookings"
    ),
'''
