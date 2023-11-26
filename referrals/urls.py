from . import views
from django.urls import path
from .views import CreateReferralsView, ReferralsListView


urlpatterns = [
    path('create_referrals/', views.CreateReferralsView.as_view(), name='create_referrals'),
    path('referrals_list/', views.ReferralsListView.as_view(), name='referrals_list'),
]
