from django.urls import path
from . import views
from .views import PostList, PostDetail, PostLike, CatListView

urlpatterns = [
    path(
        "", PostList.as_view(), name="home"
    ),  # Home page showing the list of posts
    path(
        "<slug:slug>/", PostDetail.as_view(), name="post_detail"
    ),  # View for a specific post based on its slug
    path(
        "<slug:slug>/edit_comment/<int:comment_id>/",
        views.comment_edit,
        name="comment_edit",
    ),  # Edit a specific comment on a post
    path(
        "<slug:slug>/delete_comment/<int:comment_id>/",
        views.comment_delete,
        name="comment_delete",
    ),  # Delete a specific comment on a post
    path(
        "like/<slug:slug>/", PostLike.as_view(), name="post_like"
    ),  # Like a specific post
    path(
        "category/<str:category>/", CatListView.as_view(), name="category"
    ),  # View posts by category
]
