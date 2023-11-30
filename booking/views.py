from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponse
from django.db.models import Q
from userprofile.models import UserProfile
from .models import Booking
from .forms import (
    CreateBookingForm, UpdateBookingForm,
    CancelBookingForm, ConfirmBookingForm,
    ArchiveBookingForm, CreateDirectBookingForm
)


class CreateBookingView(CreateView):
    """
    View for creating a new booking.
    """
    model = Booking
    template_name = 'booking/create_booking_form.html'
    form_class = CreateBookingForm

    def get_form_kwargs(self):
        kwargs = super(CreateBookingView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # Set the sender field to the logged-in user
        form.instance.sender = self.request.user.userprofile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('booking_list')


class BookingListView(generic.ListView):
    """
    View for listing user bookings
    """
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'booking_list'

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Filter bookings where the user is either the sender or receiver
        return Booking.objects.filter(
            Q(sender=user.userprofile) | Q(receiver=user.userprofile),
            is_archived=False
        )


class UpdateBookingView(LoginRequiredMixin, UpdateView):
    """
    View for updating a 1-2-1 meeting.
    """
    model = Booking
    template_name = 'booking/update_booking_form.html'
    form_class = UpdateBookingForm
    context_object_name = 'booking_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'  # Specify the URL keyword argument for the slug
    success_url = reverse_lazy('booking_list')

    def get_object(self, queryset=None):
        return self.model.objects.get(
            slug=self.kwargs.get(self.slug_url_kwarg))


class CreateDirectBookingView(CreateView):
    """
    View for creating booking directly from profile.
    """
    model = Booking
    form_class = CreateDirectBookingForm
    template_name = 'booking/create_booking_form.html'
    success_url = reverse_lazy('booking_list')

    def form_valid(self, form):
        # set logged in user as sender
        form.instance.sender = self.request.user.userprofile

        # get receiver from the clicked profile
        receiver_username = self.kwargs.get('receiver_username')
        form.instance.receiver = UserProfile.objects.get(
            user__username=receiver_username)

        return super().form_valid(form)


class CancelBookingView(LoginRequiredMixin, UpdateView):
    """
    View to cancel a meeting, this will not delete
    """
    model = Booking
    template_name = 'booking/cancel_booking_form.html'
    form_class = CancelBookingForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('booking_list')


class ConfirmBookingView(LoginRequiredMixin, UpdateView):
    """
    View to confirm a meeting
    """
    model = Booking
    template_name = 'booking/confirm_booking_form.html'
    form_class = ConfirmBookingForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('booking_list')


class ArchiveBookingView(LoginRequiredMixin, UpdateView):
    """
    View to archive a meeting, this will not delete
    """
    model = Booking
    template_name = 'booking/archive_booking_form.html'
    form_class = ArchiveBookingForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('booking_list')


class ArchiveBookingListView(generic.ListView):
    """
    View for listing archived bookings
    """
    model = Booking
    template_name = 'booking/booking_archive_list.html'
    context_object_name = 'booking_list'

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Filter bookings where the user is either the sender or receiver
        return Booking.objects.filter(
            Q(sender=user.userprofile) | Q(receiver=user.userprofile),
            is_archived=True
        )
