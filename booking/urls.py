from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookATee.as_view(), name='book_a_tee'),
]
