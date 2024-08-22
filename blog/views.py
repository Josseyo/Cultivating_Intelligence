from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import CommentForm

#from django.views.generic import ListView
#from django.views.generic.edit import UpdateView, DeleteView
from django.views import generic, View

# Create your views here.

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)

class PostList(generic.ListView):
    #model = Post
    queryset = Post.objects.filter(status=1)#.order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

class PostDetail(View):
    """
    PostDetail(View):
    """
    """def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        comment_count = comments.count()
        liked = post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
        comment_form = CommentForm()  

        jls_extract_var = "post_detail.html"
        return render(request, jls_extract_var, {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "liked": liked,
            "comment_form": comment_form,
        })"""
    def get(self, request, slug, *args, **kwargs):
        # Get the post or return a 404 if not found
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        
        # Fetch approved comments and order them
        comments = post.comments.filter(approved=True).order_by("-created_on")
        
        # Count the number of approved comments
        comment_count = comments.count()
        
        # Check if the user has liked the post
        liked = post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
        
        # Initialize the comment form
        comment_form = CommentForm()  

        # Render the post detail template
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
        liked = post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.name = request.user.username
            comment.author = request.user
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

class CatListView(generic.ListView):
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

"""class CatListView(generic.ListView):  # Use generic.ListView here
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        return Post.objects.filter(category__name=self.kwargs['category'], status=1)

def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return render(request, 'category.html', context)  # Render the context"""

#Edit comment doesn't show correct message nor the update/edit date 
"""def comment_edit(request, slug, comment_id):
    if request.method == "POST":
        post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
        comment = get_object_or_404(Comment, id=comment_id)
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

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))"""


def comment_edit(request, slug, comment_id):
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure only the author can edit their comment
    if comment.author != request.user:
        messages.error(request, 'You are not allowed to edit this comment!')
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, 'Comment Updated!')
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
        #else:
            #messages.error(request, 'Error updating comment!')
        else:
        # If not POST, create a form instance with the existing comment data
            comment_form = CommentForm(instance=comment)
        
    else:
        messages.error(request, 'Error updating comment!')

    # Render the comment edit form
    return render(request, "edit_comment.html", {
        "post": post,
        "comment_form": comment_form,
        "comment": comment,
    })


def comment_delete(request, slug, comment_id):
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))