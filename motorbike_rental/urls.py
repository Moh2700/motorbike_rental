
from django.urls import path
from motorbike_rental import views

app_name = 'motorbike_rental'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.login_view, name='login'),
    path('motorbike_list/', views.motorbike_list, name='motorbike_list'),
    path('user_list/', views.user_list, name='user_list'),
    path('logout/', views.logout_view, name='logout'),
    path('get_user_details/', views.get_user_details, name='get_user_details'),
    path('edit_bikeuser/<int:user_id>/', views.edit_bikeuser, name='edit_bikeuser'),
    path('delete_bikeuser/<int:user_id>/', views.delete_bikeuser, name='delete_bikeuser'),
    path('hire_motorbike/<int:bike_id>/', views.hire_motorbike, name='hire_motorbike'), 
    path('motorbike_detail/<int:bike_id>/', views.motorbike_detail,name="motorbike_detail"),
    path('booking_details/<int:bike_id>/', views.booking_details, name="booking_details"),  
    path('delete_motorbike/<int:bike_id>/', views.delete_motorbike,name='delete_motorbike'),
    path('registeruser/', views.registeruser, name='registeruser'),
    path('menufile/', views.menufile_view, name='menufile'),
    path('add_motorbike/', views.add_motorbike, name='add_motorbike',),
    path('edit_motorbike/<int:bike_id>/', views.edit_motorbike, name='edit_motorbike',),
    path('customer_dashboard/', views.menufile_view, name='menufile'),
]
   #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
   #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
   #path('<int:question_id>/vote/', views.vote, name='vote'),

'''
    path(
        'hire_motorbike/<int:bike_id>/',
        views.hire_motorbike,
        name='hire_motorbike',
    ),
'''



'''
urlpatterns = [
  path('', views.index, name='index'),
  path('customers/', views.customers_view, name='customers'),
  path('about/', views.about_view, name='about'),
   
  path('menufile/', views.menufile_view, name='menufile'),
  path('popup/', views.popup_view, name='popup'),
  path('pickup2/', views.pickup2_view, name='pickup2'),
  path('contact/', views.contact_view, name='contact'),
  path('admin/', views.admin_view, name='admin'),
  path('products/', views.products_view, name='products'),
  path('booking_form/', views.booking_form_view, name='booking_form'),
  path('tblmotorbikes/', views.tblmotorbikes_view, name='tblmotorbikes'),
  path('manage_motorbikes/', views.manage_motorbikes, name='manage_motorbikes'),
  path('motorbikes/<int:pk>/edit/', views.edit_motorbike, name='edit_motorbike'),
  path('motorbikes/edit/<int:bike_id>/', views.edit_motorbike, name='edit_motorbike', ),
  path('motorbikes/delete/<int:bike_id>/', views.delete_motorbike, name='delete_motorbike',),
  path('motorbikes/add/', views.add_motorbike, name='add_motorbike'),
  path('managing_motorbike/edit/<int:bike_id>/', views.editing_motorbike, name='editing_motorbike'),
  path('motorbikes/<int:bike_id>/edit/', views.edit_motorbike, name="edit_motorbike"),
  path('<int:bike_id>/', views.motorbikedetails, name='index'),
]

'''
