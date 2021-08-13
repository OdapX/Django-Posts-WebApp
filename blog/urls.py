
from django.urls import path
from .views import PostView, DetailView, CreateView, DeleteView, UpdateView, MyPostView
from . import views

urlpatterns = [
    path('', PostView.as_view(), name="blog-home"),
    path('post/<int:pk>/', DetailView.as_view(), name="blog-detail"),
    path('post/create/', CreateView.as_view(), name="create-blog"),
    path('post/<int:pk>/update/', UpdateView.as_view(), name="update-blog"),
    path('post/<int:pk>/delete', DeleteView.as_view(), name="delete-blog"),
    path('about/', MyPostView.as_view(), name="blog-Mine"),
]
