from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView
from django.views.generic import ListView
from .forms import UserProfileForm, UserForm
from .models import UserProfile, Review


class UserProfileListView(LoginRequiredMixin, ListView):
    """
    View for listing user profiles.
    """
    model = UserProfile
    template_name = 'userprofile/profile_list.html'
    context_object_name = 'userprofile_list'


class UserProfileDetailView(LoginRequiredMixin, DetailView):
    """
    View for displaying a user profile in detail.
    """
    model = UserProfile
    template_name = 'userprofile/profile_detail.html'
    context_object_name = 'userprofile_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a user profile.
    """
    model = UserProfile
    template_name = 'userprofile/profile_update_form.html'
    form_class = UserProfileForm
    context_object_name = 'userprofile_detail'
    slug = 'slug'

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse_lazy(
            'userprofile_detail',
            kwargs={'slug': self.request.user.userprofile.slug})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating basic user information.
    """
    model = User
    template_name = 'userprofile/user_info_update_form.html'
    form_class = UserForm
    slug = 'slug'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy(
            'userprofile_detail',
            kwargs={'slug': self.request.user.userprofile.slug})


class CreateUserProfileView(View):
    """
    View for creating a user profile.
    """
    model = UserProfile
    template_name = 'userprofile/profile_create_form.html'

    def get(self, request, *args, **kwargs):
        form = UserProfileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user = get_user(request)
            user_profile.user = user
            user_profile.save()
            return redirect('userprofile_detail', slug=user_profile.slug)
        return render(request, self.template_name, {'form': form})
