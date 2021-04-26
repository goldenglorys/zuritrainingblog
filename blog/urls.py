from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    CommentCreateView,
)

from .models import Post

urlpatterns = [
    path('comment/new/', CommentCreateView.as_view(), name='comment_new'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(model=Post), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]