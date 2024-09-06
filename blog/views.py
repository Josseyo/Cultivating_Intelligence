from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import CommentForm
from django.views import generic, View


# Custom 404 view
def custom_404(request, exception):
    """Render the custom 404 error page."""
    return render(request, "404.html", status=404)


class PostList(generic.ListView):
    """View to list all published posts."""

    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    """View to display a specific post and its comments."""

    def get(self, request, slug, *args, **kwargs):
        """Handle GET request to display post details and comments."""
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        comment_count = comments.count()
        liked = (
            request.user.is_authenticated
            and post.likes.filter(id=request.user.id).exists()
        )
        comment_form = CommentForm()
        template_name = "post_detail.html"

        return render(
            request,
            template_name,
            {
                "post": post,
                "comments": comments,
                "comment_count": comment_count,
                "liked": liked,
                "comment_form": comment_form,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """Handle POST request to add a comment to the post."""
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = (
            post.likes.filter(id=request.user.id).exists()
            if request.user.is_authenticated
            else False
        )
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.name = request.user.username
            comment.author = request.user
            comment.save()
            messages.success(request, "Your comment has been added.")
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))

        else:
            messages.error(request, "There was an error with your comment.")

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_count": comments.count(),
                "liked": liked,
                "comment_form": comment_form,
                "commented": True,
            },
        )


class PostLike(View):
    """View to handle liking and unliking a post."""

    def post(self, request, slug, *args, **kwargs):
        """Toggle the like status of a post."""
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class CatListView(generic.ListView):
    """View to list posts by category."""

    template_name = "category.html"
    context_object_name = "catlist"

    def get_queryset(self):
        """Return posts belonging to the specified category."""
        content = {
            "cat": self.kwargs["category"],
            "posts": Post.objects.filter(
                category__name=self.kwargs["category"]
            ).filter(status=1),
        }
        return content


def category_list(request):
    """Return a list of categories excluding the default category."""
    category_list = Category.objects.exclude(name="default")
    context = {
        "category_list": category_list,
    }
    return context


def comment_edit(request, slug, comment_id):
    """Edit an existing comment on a post."""
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure only the author can edit their comment
    if comment.author != request.user:
        messages.error(request, "You are not allowed to edit this comment!")
        return HttpResponseRedirect(reverse("post_detail", args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, "Comment Updated!")
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        else:
            comment_form = CommentForm(instance=comment)

    else:
        messages.error(request, "Error updating comment!")

    return render(
        request,
        "edit_comment.html",
        {
            "post": post,
            "comment_form": comment_form,
            "comment": comment,
        },
    )


def comment_delete(request, slug, comment_id):
    """Delete a specific comment from a post."""
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
    else:
        messages.error(request, "You can only delete your own comments!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))
