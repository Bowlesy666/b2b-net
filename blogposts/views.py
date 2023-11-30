from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, CreatePostForm, EditPostForm


class PostList(generic.ListView):
    """
    List view for displaying a paginated list of published blog posts.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/blog_index.html"
    paginate_by = 6


class PostDetail(View):
    """
    View for displaying a blog post in detail and handling comments and likes.
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    """
    View for handling post likes/unlikes
    HTTP POST request that
    Redirects to the detailed view of the liked/unliked post.
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('blog/post_detail', args=[slug]))


class CreatePostView(LoginRequiredMixin, CreateView):
    """
    View for creating a new blog post.
    """
    model = Post
    template_name = 'blog/create_post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Override the form_valid method to set the author before saving the post
        """
        form.instance.author = self.request.user
        content = form.cleaned_data['content']
        form.instance.excerpt = (
            content[:50] + '...') if len(content) > 50 else content
        response = super().form_valid(form)
        return response


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    View for updating an existing blog post.
    """
    model = Post
    template_name = 'blog/edit_post.html'
    form_class = EditPostForm
    slug_field = 'slug'  # Use slug_field instead of slug
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    View for deleting an existing blog post.
    """
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        """
        This method is used to fetch the object to be deleted.
        By default, it uses self.queryset, but can be customised.
        In this case, I am using the slug field to filter the Post object.
        """
        queryset = queryset or self.get_queryset()
        return queryset.filter(
            **{self.slug_field: self.kwargs[self.slug_url_kwarg]}).first()
