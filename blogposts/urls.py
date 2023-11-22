from . import views
from django.urls import path
from blogposts.views import CreatePostView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('edit_post/<slug:slug>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<slug:slug>/', PostDeleteView.as_view(), name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
