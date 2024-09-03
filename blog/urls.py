from django.urls import path
from . import views
from .views import PostList, PostDetail, PostLike, CatListView

urlpatterns = [
    path("", PostList.as_view(), name="home"),
    path(
        "<slug:slug>/", PostDetail.as_view(), name="post_detail"
    ),  # This is the class-based view
    path(
        "<slug:slug>/edit_comment/<int:comment_id>/",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>/",
        views.comment_delete,
        name="comment_delete",
    ),
    path("like/<slug:slug>/", PostLike.as_view(), name="post_like"),
    path("category/<str:category>/", CatListView.as_view(), name="category"),
]
