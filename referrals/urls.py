from . import views
from django.urls import path
from .views import CreateReferralsView, ReferralsListView, ReferralsUpdateView


urlpatterns = [
    path('create_referrals/', views.CreateReferralsView.as_view(), name='create_referrals'),
    path('referrals_list/', views.ReferralsListView.as_view(), name='referrals_list'),
    path('referrals_update/<slug:slug>', views.ReferralsUpdateView.as_view(), name='referrals_update'),
]
