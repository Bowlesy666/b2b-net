from django.shortcuts import render
from django.views import generic, View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CreateReferralsForm, ReferralsUpdateForm
from .models import ReferralsModel


class CreateReferralsView(CreateView):
    model = ReferralsModel
    template_name = 'create_referrals_form.html'
    form_class = CreateReferralsForm

    def get_form_kwargs(self):
        kwargs = super(CreateReferralsView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # Set the sender field to the logged-in user
        form.instance.referral_sender_id = self.request.user.userprofile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('referrals_list')


class ReferralsListView(generic.ListView):
    """
    View for listing user referrals
    """
    model = ReferralsModel
    template_name = 'referrals_list.html'
    context_object_name = 'referrals_list'

    def get_queryset(self):
        # Get the current user
        user = self.request.user

        # Filter referrals where the user is either the sender or receiver
        return ReferralsModel.objects.filter(
            Q(referral_sender_id=user.userprofile) | Q(referral_receiver_id=user.userprofile),
            is_archived=False
        )


class ReferralsUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating referral logs.
    """
    model = ReferralsModel
    template_name = 'referrals_update_form.html'
    form_class = ReferralsUpdateForm
    context_object_name = 'referrals_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'  # Specify the URL keyword argument for the slug
    success_url = reverse_lazy('referrals_list')

    def get_object(self, queryset=None):
        return self.model.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))

