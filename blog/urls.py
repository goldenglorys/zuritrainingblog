from django.urls import path
from .views import BlogListView, BlogDetailView
from .models import Post

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(model=Post), name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
]