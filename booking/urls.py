from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookATee.as_view(), name='book_a_tee'),
    path('booking_time/', views.BookATee.as_view(), name='book_a_time'),
]
