"""b2bproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userprofile import views
from userprofile.views import UserProfileListView, UserProfileDetailView, UserProfileUpdateView, UserUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserProfileListView.as_view(), name='profile_list'),
    path('profile/<slug:slug>/', views.UserProfileDetailView.as_view(),
         name='userprofile_detail'),
    path('profile/<slug:slug>/edit', views.UserProfileUpdateView.as_view(), name='profile_update_form'),
    path('profile/<slug:slug>/edit_user', views.UserUpdateView.as_view(), name='user_info_update_form'),
    path('accounts/', include('allauth.urls')),
]
