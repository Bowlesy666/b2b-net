from . import views
from django.urls import path
from .views import CreateReferralsView, ReferralsListView, ReferralsUpdateView, ReferralsArchiveListView, ReferralsArchiveView, ReferralsConfirmAgreementView, ReferralsCancelView, ReferralsAnalysisView


urlpatterns = [
    path('create_referrals/', views.CreateReferralsView.as_view(), name='create_referrals'),
    path('referrals_list/', views.ReferralsListView.as_view(), name='referrals_list'),
    path('referrals_archive_list/', views.ReferralsArchiveListView.as_view(), name='referrals_archive_list'),
    path('referrals_analysis/', views.ReferralsAnalysisView.as_view(), name='referrals_analysis'),
    path('referrals_archive/<slug:slug>/', views.ReferralsArchiveView.as_view(), name='referrals_archive'),
    path('referrals_cancel/<slug:slug>/', views.ReferralsCancelView.as_view(), name='referrals_cancel'),
    path('referrals_agreement_completed/<slug:slug>/', views.ReferralsAgreementCompletedView.as_view(), name='referrals_agreement_completed'),
    path('referrals_confirm_agreement/<slug:slug>/', views.ReferralsConfirmAgreementView.as_view(), name='referrals_confirm_agreement'),
    path('referrals_update/<slug:slug>/', views.ReferralsUpdateView.as_view(), name='referrals_update'),
]
