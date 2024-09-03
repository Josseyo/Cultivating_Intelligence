from django.contrib import admin
from .models import Post, Comment, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin panel settings for managing blog posts.
    """

    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "slug", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    summernote_fields = ("content",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin panel for managing comments.
    """

    list_display = (
        "post",
        "author",
        "approved",
        "created_on",
        "body",
        "updated_on",
    )
    list_filter = (
        "approved",
        "author",
        "created_on",
        "updated_on",
    )
    search_fields = ["author", "post", "body"]
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        """
        Approve selected comments.
        """
        queryset.update(approved=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin panel for managing categories.
    """
