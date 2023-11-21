from . import views
from django.shortcuts import render, HttpResponse
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
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


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    template_name = 'profile_update_form.html'
    fields = [
        'user',
        'business_sector',
        'company_name',
        'company_website',
        'company_contact_number',
        'alternative_company_contact_number',
        'company_contact_email',
        'company_bio',
        'company_services_post',
        'company_hero_picture',
        'user_contact_number',
        'display_user_email',
        'user_about',
        'user_profile_img',
    ]
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'userprofile_detail'

    def get_object(self, queryset=None):
        # Ensure the user can only edit their own profile
        return self.request.user.userprofile
