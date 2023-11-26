from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import CreateReferralsForm
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
        return reverse_lazy('home')
