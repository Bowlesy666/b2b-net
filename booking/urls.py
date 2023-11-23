from . import views
from django.urls import path
from booking.views import CreateBookingView


urlpatterns = [
    path('create_booking/', views.CreateBookingView.as_view(), name='create_booking'),
]
