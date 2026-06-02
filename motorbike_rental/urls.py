"""
URL configuration for motorbike_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from motorbike_rental import views

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
  path(
      'motorbikes/edit/<int:bike_id>/',
      views.edit_motorbike,
      name='edit_motorbike',
  ),
  path(
      'motorbikes/delete/<int:bike_id>/',
      views.delete_motorbike,
      name='delete_motorbike',
  ),
  path('motorbikes/add/', views.add_motorbike, name='add_motorbike'),
]
#path('motorbikes/', views.motorbike_list, name='motorbike_list'),
