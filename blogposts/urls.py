
1. """
   -`home`:
   - URL pattern for the blog home page, displaying a list of all published posts.
   - Maps to the `PostList` view.

2. `post_like`:
   - URL pattern for handling post liking.
   - Uses a slug parameter to identify the post.
   - Maps to the `PostLike` view.

3. `create_post`:
   - URL pattern for creating a new blog post.
   - Maps to the `CreatePostView` view.

4. `update_post`:
   - URL pattern for updating an existing blog post.
   - Uses a slug parameter to identify the post.
   - Maps to the `PostUpdateView` view.

5. `delete_post`:
   - URL pattern for deleting an existing blog post.
   - Uses a slug parameter to identify the post.
   - Maps to the `PostDeleteView` view.

6. `post_detail`:
   - URL pattern for viewing a specific blog post in detail.
   - Uses a slug parameter to identify the post.
   - Maps to the `PostDetail` view.
"""
from . import views
from django.urls import path
from blogposts.views import CreatePostView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create_post/', views.CreatePostView.as_view(), name='create_post'),
    path('edit_post/<slug:slug>/',
         views.PostUpdateView.as_view(), name='update_post'),
    path('delete_post/<slug:slug>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
