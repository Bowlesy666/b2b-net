from django.contrib import messages
from django.shortcuts import render
from django.views import generic, View
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.db.models import Q, Avg
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import (
    CreateReferralsForm, ReferralsUpdateForm, ReferralsArchiveForm,
    ReferralsConfirmAgreementForm, ReferralsAgreementCompletedForm,
    ReferralsCancelForm
)
from .models import ReferralsModel


class CreateReferralsView(LoginRequiredMixin, CreateView):
    """
    View for creating referrals.
    """
    model = ReferralsModel
    template_name = 'referrals/create_referrals_form.html'
    form_class = CreateReferralsForm

    def get_form_kwargs(self):
        """
        Adds the user information to the form kwargs.
        """
        kwargs = super(CreateReferralsView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        """
        Sets the sender field to the logged-in user.
        """
        form.instance.referral_sender_id = self.request.user.userprofile
        messages.success(self.request, 'Referral successfully created.')
        return super().form_valid(form)

    def get_success_url(self):
        """
        Returns the URL after a successful form submission.
        """
        return reverse_lazy('referrals_list')


class ReferralsListView(LoginRequiredMixin, generic.ListView):
    """
    View for listing user referrals
    """
    model = ReferralsModel
    template_name = 'referrals/referrals_list.html'
    context_object_name = 'referrals_list'

    def get_queryset(self):
        """
        Gets the queryset for listing referrals.
        Filters if the user is the sender or reciever
        """
        user = self.request.user

        return ReferralsModel.objects.filter(
            Q(referral_sender_id=user.userprofile) | Q(
                referral_receiver_id=user.userprofile),
            is_archived=False
        )


class ReferralsUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating referral logs.
    """
    model = ReferralsModel
    template_name = 'referrals/referrals_update_form.html'
    form_class = ReferralsUpdateForm
    context_object_name = 'referrals_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('referrals_list')

    def form_valid(self, form):
        messages.success(self.request, 'Referral successfully updated.')
        return super().form_valid(form)

    def get_object(self, queryset=None):
        """
        Gets the referral object to be updated.
        """
        return self.model.objects.get(
            slug=self.kwargs.get(self.slug_url_kwarg))


class ReferralsArchiveView(LoginRequiredMixin, UpdateView):
    """
    View to archive a referral
    """
    model = ReferralsModel
    template_name = 'referrals/referrals_archive_form.html'
    form_class = ReferralsArchiveForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('referrals_list')

    def form_valid(self, form):
        messages.success(self.request, 'Referral successfully moved.')
        return super().form_valid(form)


class ReferralsArchiveListView(LoginRequiredMixin, generic.ListView):
    """
    View for listing archived referrals
    """
    model = ReferralsModel
    template_name = 'referrals/referrals_archive_list.html'
    context_object_name = 'referrals_list'

    def get_queryset(self):
        """
        Get the current user referrals that are archived
        Filters if user is receiver or sender
        """
        user = self.request.user

        return ReferralsModel.objects.filter(
            Q(referral_sender_id=user.userprofile) | Q(
                referral_receiver_id=user.userprofile),
            is_archived=True
        )


class ReferralsConfirmAgreementView(LoginRequiredMixin, UpdateView):
    """
    View for the users to confirm the agreement
    """
    model = ReferralsModel
    template_name = 'referrals/referrals_confirm_agreement_form.html'
    form_class = ReferralsConfirmAgreementForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('referrals_list')

    def form_valid(self, form):
        messages.success(self.request, 'Referral confirmation updated.')
        return super().form_valid(form)


class ReferralsAgreementCompletedView(LoginRequiredMixin, UpdateView):
    """
    View for the users to complete the agreement
    """
    model = ReferralsModel
    template_name = 'referrals/referrals_agreement_completed_form.html'
    form_class = ReferralsAgreementCompletedForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('referrals_list')

    def form_valid(self, form):
        messages.success(self.request, 'Congratulations on completing!')
        return super().form_valid(form)


class ReferralsCancelView(LoginRequiredMixin, UpdateView):
    """
    View for the users to cancel the agreement
    """
    model = ReferralsModel
    template_name = 'referrals/referrals_cancel_form.html'
    form_class = ReferralsCancelForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('referrals_list')

    def form_valid(self, form):
        messages.success(self.request, 'Referral successfully cancelled.')
        return super().form_valid(form)


class ReferralsAnalysisView(LoginRequiredMixin, TemplateView):
    """
    View for analyzing referral statistics.
    Context Data:
        total_referrals_made: Total number of referrals made.
        total_referrals_received: Total number of referrals received.
        total_revenue_earned: Total revenue earned from referrals.
        total_commission_made: Total commission made from referrals.
        average_revenue_earned: Average revenue earned per referral.
        average_commission_earned: Average commission earned per referral.
        total_revenue_completed: Total revenue earned from completed referrals
        total_commission_completed: Total commission earned from completed.
        total_earnings_completed: Total earnings from completed referrals.
    """
    template_name = 'referrals/referral_analysis.html'

    def get_context_data(self, **kwargs):
        """
        Retrieves and provides data for the template.
        Returns information as a dictionary
        """
        context = super().get_context_data(**kwargs)

        context['total_referrals_made'] = ReferralsModel.objects.filter(
            referral_sender_id=self.request.user.userprofile).count()
        context['total_referrals_received'] = ReferralsModel.objects.filter(
            referral_receiver_id=self.request.user.userprofile).count()
        context['total_revenue_earned'] = ReferralsModel.objects.filter(
            referral_receiver_id=self.request.user.userprofile).aggregate(
                total_revenue=models.Sum(
                    'proposed_amount'))['total_revenue'] or 0
        context['total_commission_made'] = ReferralsModel.objects.filter(
            referral_sender_id=self.request.user.userprofile).aggregate(
                total_commission=models.Sum(
                    'estimated_commsion'))['total_commission'] or 0
        context['average_revenue_earned'] = ReferralsModel.objects.filter(
            referral_receiver_id=self.request.user.userprofile).aggregate(
                average_revenue=models.Avg(
                    'proposed_amount'))['average_revenue'] or 0
        context['average_commission_earned'] = ReferralsModel.objects.filter(
            referral_sender_id=self.request.user.userprofile).aggregate(
                average_commission=models.Avg(
                    'estimated_commsion'))['average_commission'] or 0
        context['total_revenue_completed'] = ReferralsModel.objects.filter(
            referral_receiver_id=self.request.user.userprofile,
            is_completed=True).aggregate(revenue_completed=models.Sum(
                'proposed_amount'))['revenue_completed'] or 0
        context['total_commission_completed'] = ReferralsModel.objects.filter(
            referral_sender_id=self.request.user.userprofile,
            is_completed=True).aggregate(commission_completed=models.Sum(
                'estimated_commsion'))['commission_completed'] or 0
        context['total_earnings_completed'] = context[
            'total_revenue_completed'] + context['total_commission_completed']

        return context
