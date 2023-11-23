from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from . import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from .forms import UserProfileForm, UserForm
from .models import UserProfile, Review
from django.contrib.auth.models import User


class UserProfileListView(generic.ListView):
    """
    View for listing user profiles.
    """
    model = UserProfile
    template_name = 'profile_list.html'
    context_object_name = 'userprofile_list'


class UserProfileDetailView(DetailView):
    """
    View for displaying a user profile in detail.
    """
    model = UserProfile
    template_name = 'profile_detail.html'
    context_object_name = 'userprofile_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating a user profile.
    """
    model = UserProfile
    template_name = 'profile_update_form.html'
    form_class = UserProfileForm
    context_object_name = 'userprofile_detail'
    slug = 'slug'

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse_lazy('userprofile_detail', kwargs={'slug': self.request.user.userprofile.slug})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating basic user information.
    """
    model = User
    template_name = 'user_info_update_form.html'
    # success_url = reverse_lazy('profile_edit')
    form_class = UserForm
    slug = 'slug'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('userprofile_detail', kwargs={'slug': self.request.user.userprofile.slug})


class CreateUserProfileView(View):
    model = UserProfile
    template_name = 'profile_create_form.html'

    def get(self, request, *args, **kwargs):
        form = UserProfileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, 'User profile created successfully!')
            return redirect('userprofile_detail', slug=user_profile.slug)
        return render(request, self.template_name, {'form': form})
