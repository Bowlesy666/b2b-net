"""
URL patterns related to user referrals

1. `create_referrals`:
   - URL pattern for creating a new referral.
   - Maps to the `CreateReferralsView` view.

2. `referrals_list`:
   - URL pattern for listing user referrals.
   - Maps to the `ReferralsListView` view.

3. `referrals_archive_list`:
   - URL pattern for listing archived referrals.
   - Maps to the `ReferralsArchiveListView` view.

4. `referrals_analysis`:
   - URL pattern for analyzing referral statistics.
   - Maps to the `ReferralsAnalysisView` view.

5. `referrals_archive`:
   - URL pattern for archiving a referral.
   - Uses a slug parameter to identify the referral.
   - Maps to the `ReferralsArchiveView` view.

6. `referrals_cancel`:
   - URL pattern for canceling a referral.
   - Uses a slug parameter to identify the referral.
   - Maps to the `ReferralsCancelView` view.

7. `referrals_agreement_completed`:
   - URL pattern for marking a referral agreement as completed.
   - Uses a slug parameter to identify the referral.
   - Maps to the `ReferralsAgreementCompletedView` view.

8. `referrals_confirm_agreement`:
   - URL pattern for confirming a referral agreement.
   - Uses a slug parameter to identify the referral.
   - Maps to the `ReferralsConfirmAgreementView` view.

9. `referrals_update`:
   - URL pattern for updating referral logs.
   - Uses a slug parameter to identify the referral.
   - Maps to the `ReferralsUpdateView` view.
"""
from . import views
from django.urls import path
from .views import (
    CreateReferralsView,
    ReferralsListView,
    ReferralsUpdateView,
    ReferralsArchiveListView,
    ReferralsArchiveView,
    ReferralsConfirmAgreementView,
    ReferralsCancelView,
    ReferralsAnalysisView
)


urlpatterns = [
    path('create_referrals/',
         views.CreateReferralsView.as_view(), name='create_referrals'),
    path('referrals_list/',
         views.ReferralsListView.as_view(), name='referrals_list'),
    path('referrals_archive_list/',
         views.ReferralsArchiveListView.as_view(),
         name='referrals_archive_list'),
    path('referrals_analysis/',
         views.ReferralsAnalysisView.as_view(), name='referrals_analysis'),
    path('referrals_archive/<slug:slug>/',
         views.ReferralsArchiveView.as_view(), name='referrals_archive'),
    path('referrals_cancel/<slug:slug>/',
         views.ReferralsCancelView.as_view(), name='referrals_cancel'),
    path('referrals_agreement_completed/<slug:slug>/',
         views.ReferralsAgreementCompletedView.as_view(),
         name='referrals_agreement_completed'),
    path('referrals_confirm_agreement/<slug:slug>/',
         views.ReferralsConfirmAgreementView.as_view(),
         name='referrals_confirm_agreement'),
    path('referrals_update/<slug:slug>/',
         views.ReferralsUpdateView.as_view(), name='referrals_update'),
]
