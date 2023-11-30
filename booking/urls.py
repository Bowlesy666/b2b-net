"""
URL patterns related to user bookings

1. `create_booking`:
   - URL pattern for creating a new booking.
   - Maps to the `CreateBookingView` view.

2. `create_direct_booking`:
   - URL pattern for creating a direct booking with a specific user.
   - Uses a username parameter to identify the receiver.
   - Maps to the `CreateDirectBookingView` view.

3. `booking_list`:
   - URL pattern for listing user bookings.
   - Maps to the `BookingListView` view.

4. `update_booking`:
   - URL pattern for updating a 1-2-1 meeting.
   - Uses a slug parameter to identify the booking.
   - Maps to the `UpdateBookingView` view.

5. `cancel_booking`:
   - URL pattern for canceling a meeting without deletion.
   - Uses a slug parameter to identify the booking.
   - Maps to the `CancelBookingView` view.

6. `confirm_booking`:
   - URL pattern for confirming a meeting without deletion.
   - Uses a slug parameter to identify the booking.
   - Maps to the `ConfirmBookingView` view.

7. `archive_booking`:
   - URL pattern for archiving a meeting without deletion.
   - Uses a slug parameter to identify the booking.
   - Maps to the `ArchiveBookingView` view.

8. `archive_booking_list`:
   - URL pattern for listing archived bookings.
   - Maps to the `ArchiveBookingListView` view.
"""
from . import views
from django.urls import path
from booking.views import (
    CreateBookingView, UpdateBookingView,
    ArchiveBookingView, ArchiveBookingListView)


urlpatterns = [
    path(
        'create_booking/',
        views.CreateBookingView.as_view(), name='create_booking'),
    path('create_booking/direct/<str:receiver_username>/',
         views.CreateDirectBookingView.as_view(),
         name='create_direct_booking'),
    path(
        'booking_list/',
        views.BookingListView.as_view(), name='booking_list'),
    path('update_booking/<slug:slug>/',
         views.UpdateBookingView.as_view(), name='update_booking'),
    path('cancel_booking/<slug:slug>/',
         views.CancelBookingView.as_view(), name='cancel_booking'),
    path('confirm_booking/<slug:slug>/',
         views.ConfirmBookingView.as_view(), name='confirm_booking'),
    path('archive_booking/<slug:slug>/',
         views.ArchiveBookingView.as_view(), name='archive_booking'),
    path('archive_booking_list/',
         views.ArchiveBookingListView.as_view(), name='archive_booking_list'),
]
