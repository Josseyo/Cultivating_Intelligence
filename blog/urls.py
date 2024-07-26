from django.urls import path
from . import views
from .views import PostList, PostDetail, PostLike, CatListView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<str:category>/', views.CatListView.as_view(), name='category'),
]