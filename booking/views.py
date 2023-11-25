from django.shortcuts import render
from django.views import generic, View
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.db.models import Q
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
        return reverse_lazy('booking_list')


class BookingListView(generic.ListView):
    """
    View for listing user bookings.
    """
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'booking_list'

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Filter bookings where the user is either the sender or receiver
        return Booking.objects.filter(Q(sender=user.userprofile) | Q(receiver=user.userprofile))


class UpdateBookingView(LoginRequiredMixin, UpdateView):
    """
    View for updating a 1-2-1 meeting.
    """
    model = Booking
    template_name = 'update_booking_form.html'
    form_class = BookingForm
    context_object_name = 'booking_detail'
    slug_url_kwarg = 'slug'  # Specify the URL keyword argument for the slug

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))

    def get_success_url(self):
        return reverse_lazy('booking_list')
