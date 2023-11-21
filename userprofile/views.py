from . import views
from django.shortcuts import render, HttpResponse
from django.views import generic, View
from django.views.generic import DetailView
from .models import UserProfile, Review


class UserProfileListView(generic.ListView):
    model = UserProfile
    template_name = 'profile_list.html'
    context_object_name = 'userprofile_list'


class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = 'profile_detail.html'
    context_object_name = 'userprofile_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def log_in(request):
    return render(request, 'account/login.html')


def signup(request):
    return render(request, 'account/signup.html')
