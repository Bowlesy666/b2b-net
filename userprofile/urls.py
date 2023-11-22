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
