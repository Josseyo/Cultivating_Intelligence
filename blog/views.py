from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment, Category
from .forms import CommentForm

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        comment_count = comments.count()
        liked = post.likes.filter(id=request.user.id).exists()
        comment_form = CommentForm()  

        return render(request, "post_detail.html", {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form,
        })

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = post.likes.filter(id=request.user.id).exists()
        
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.name = request.user.username
            comment.author = request.user
            comment.email = request.user.email
            comment.save()
            messages.success(request, "Your comment has been added.")

            return HttpResponseRedirect(reverse('post_detail', args=[slug]))  # Redirect after saving

        else:
            messages.error(request, "There was an error with your comment.")

        return render(request, "post_detail.html", {
            "post": post,
            "comments": comments,
            "comment_count": comments.count(),
            "liked": liked,
            "comment_form": comment_form,
            "commented": True,
        })

class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status=1)
        }
        return content

def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context

def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment_form.save()
            messages.success(request, 'Comment Updated!')
        else:
            messages.error(request, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
