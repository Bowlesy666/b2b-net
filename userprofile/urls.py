"""

URL patterns related to user profiles

1. `profile_list`:
   - URL pattern for listing user profiles.
   - Maps to the `UserProfileListView` view.

2. `userprofile_detail`:
   - URL pattern for viewing a user profile in detail.
   - Uses a slug parameter to identify the user.
   - Maps to the `UserProfileDetailView` view.

3. `profile_update_form`:
   - URL pattern for accessing the form to update a user profile.
   - Uses a slug parameter to identify the user.
   - Maps to the `UserProfileUpdateView` view.

4. `user_info_update_form`:
   - URL pattern for accessing the form to update user information.
   - Uses a slug parameter to identify the user.
   - Maps to the `UserUpdateView` view.
"""   
from . import views
from django.urls import path
from userprofile.views import UserProfileListView, UserProfileDetailView, UserProfileUpdateView, UserUpdateView


urlpatterns = [
    path('profile_list', views.UserProfileListView.as_view(), name='profile_list'),
    path('<slug:slug>/', views.UserProfileDetailView.as_view(),
         name='userprofile_detail'),
    path('<slug:slug>/edit', views.UserProfileUpdateView.as_view(),
         name='profile_update_form'),
    path('<slug:slug>/edit_user', views.UserUpdateView.as_view(),
         name='user_info_update_form'),
    path('detail/<slug:slug>/edit_user', views.UserUpdateView.as_view(),
         name='user_info_update_form'),
]
