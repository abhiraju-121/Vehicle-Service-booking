from django.urls import path
from . import views
urlpatterns = [
    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('staff_index',views.staff_index,name='staff_index'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('customer_register',views.customer_reg,name='customer_register'),
    path('customer_login',views.customer_log,name='customer_log'),
    path('customer_logout',views.customer_logout,name='customer_logout'),
    path('staff_register',views.staff_register,name='staff_register'),
    path('staff_login',views.staff_log,name='staff_log'),
    path('staff_logout',views.staff_logout,name='staff_logout'),
    path('vehicle',views.vehicle,name='vehicle'),
    path('vehicle_list',views.vehicle_list,name='vehicle_list'),
    path('vehicle/<int:item_id>/',views.vehicle_detail,name='vehicle_detail'),
    path('car',views.car,name='car'),
    path('car/<int:car_id>/',views.car_detail,name='car_detail'),
    path('book-service/', views.book_service, name='book_service'),
    path('booking-history/', views.booking_history, name='booking_history'),
    path('approve-booking-list/', views.approve_booking_list, name='approve_booking_list'),
    path('approve-booking/<int:book_id>/', views.approve_booking, name='approve_booking'),
    path('reject-booking/<int:book_id>/', views.reject_booking, name='reject_booking'),
]
