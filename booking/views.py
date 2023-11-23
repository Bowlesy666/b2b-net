from django.shortcuts import render
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from userprofile.models import UserProfile
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponse
from django.urls import reverse_lazy


class CreateBookingView(CreateView):
    model = Booking
    template_name = 'create_booking_form.html'
    form_class = BookingForm

    def form_valid(self, form):
        # Set the sender field to the logged-in user
        form.instance.sender = self.request.user.userprofile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')
