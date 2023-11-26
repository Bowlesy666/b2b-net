from . import views
from django.urls import path
from .views import CreateReferralsView


urlpatterns = [
    path('create_referrals/', views.CreateReferralsView.as_view(), name='create_referrals'),
]
