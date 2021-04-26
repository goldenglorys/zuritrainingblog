
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy 
from .models import Post, Comment


# Create your views here.
class BlogListView(LoginRequiredMixin ,ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post,
    template_name = 'post_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView): 
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class CommentCreateView(LoginRequiredMixin, CreateView): 
    model = Comment
    template_name = 'comment_new.html'
    fields = ['article', 'comment', 'author']

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

