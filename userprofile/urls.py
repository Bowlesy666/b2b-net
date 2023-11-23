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
from userprofile.views import UserProfileListView, UserProfileDetailView, UserProfileUpdateView, UserUpdateView, CreateUserProfileView


urlpatterns = [
    path('profile_list', views.UserProfileListView.as_view(), name='profile_list'),
    path('create_user_profile/', views.CreateUserProfileView.as_view(),
         name='create_user_profile'),
    path('profile_detail/<slug:slug>/', views.UserProfileDetailView.as_view(),
         name='userprofile_detail'),
    path('edit/<slug:slug>/', views.UserProfileUpdateView.as_view(),
         name='profile_update_form'),
    path('edit_user/<slug:slug>/', views.UserUpdateView.as_view(),
         name='user_info_update_form'),
    path('detail/<slug:slug>/edit_user', views.UserUpdateView.as_view(),
         name='user_info_update_form'),
]
