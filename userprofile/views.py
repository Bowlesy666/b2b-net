from . import views
from django.shortcuts import render, HttpResponse
from django.views import generic, View
from .models import UserProfile, Review

class UserProfileListView(generic.ListView):
    model = UserProfile
    template_name = 'profile_list.html'
    context_object_name = 'userprofile_list'


def profile_detail(request):
    return render(request, 'profile_detail.html')


def log_in(request):
    return render(request, 'account/login.html')


def signup(request):
    return render(request, 'account/signup.html')
