from . import views
from django.urls import path
from .views import UserMailBoxListView


urlpatterns = [
    path('conversation_list/', views.UserMailBoxListView.as_view(), name='conversation_list'),
]
