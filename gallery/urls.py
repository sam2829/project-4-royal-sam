from . import views
from django.urls import path


urlpatterns = [
    path('', views.Gallery.as_view(), name='gallery')
]
