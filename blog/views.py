from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class PostView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 3


class MyPostView(ListView):
    model = post
    template_name = 'blog/about.html'
    context_object_name = 'posts'
    paginate_by = 3


class DetailView(DetailView):
    model = post


class CreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):

        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class DeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = post
    sucess_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
