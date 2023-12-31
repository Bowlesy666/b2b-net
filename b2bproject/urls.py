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
from blogposts.views import CreatePostView
from booking import views
from referrals import views
from usermailbox import views
from userprofile.views import UserProfileListView, UserProfileDetailView, UserProfileUpdateView, UserUpdateView
from allauth.account.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('blog/', include('blogposts.urls'), name='blog_urls'),
    path('profile/', include('userprofile.urls')),
    path('booking/', include('booking.urls')),
    path('referrals/', include('referrals.urls')),
    path('messages/', include('usermailbox.urls')),
    path('', LoginView.as_view(), name='login'),
    path('accounts/', include('allauth.urls')),
]
