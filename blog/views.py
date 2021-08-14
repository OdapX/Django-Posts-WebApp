from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import post
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin


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


class CreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_message = "blog was created successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message


class UpdateView(SuccessMessageMixin, UserPassesTestMixin, LoginRequiredMixin, UpdateView):
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
    success_message = "blog was Updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message


class DeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = post
    success_url = '/about'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
    success_message = "blog was deleted successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message
