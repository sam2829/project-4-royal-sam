from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookATee.as_view(), name='book_a_tee'),
    path('booking_time/', views.BookATime.as_view(), name='book_a_time'),
    path('my_bookings/', views.MyBookings.as_view(), name='my_bookings'),
    path('edit_booking_date/<item_id>/',
         views.EditBookingDate.as_view(), name='edit_tee_date'),
    path('edit_booking_time/<item_id>/',
         views.EditBookingTime.as_view(), name='edit_tee_time'),
    path('confirm_delete_booking/<item_id>/',
         views.ConfirmDelete.as_view(), name='confirm_delete'),
    path('delete_booking/<item_id>/',
         views.DeleteBooking.as_view(), name='delete_booking'),
]
